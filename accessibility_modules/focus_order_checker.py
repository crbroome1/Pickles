"""
Focus Order Checker Module
Tests for WCAG 2.4.3: Focus Order - Ensures that navigation follows a meaningful sequence.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

def check_focus_order(driver):
    """
    Checks that the focus order of interactive elements is logical and follows content sequence.
    Tests WCAG Success Criterion 2.4.3: Focus Order
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of focus order check
    """
    logging.info("Checking focus order (WCAG 2.4.3)...")
    results = {
        "status": "completed",
        "wcag_criterion": "2.4.3",
        "tab_sequence": [],
        "issues": []
    }
    
    try:
        # Reset focus to beginning of page
        driver.find_element(By.TAG_NAME, "body").click()
        
        # Find all potentially focusable elements
        focusable_selector = (
            "a, button, input:not([type='hidden']), select, textarea, "
            "[tabindex]:not([tabindex='-1']), [contenteditable='true'], "
            "details, summary, [role='button'], [role='link'], "
            "[role='checkbox'], [role='radio'], [role='tab'], [role='menuitem'], "
            "[role='combobox'], [role='listbox'], [role='slider'], [role='textbox'], "
            "[role='searchbox'], [role='spinbutton']"
        )
        
        # Get all focusable elements and their visual positions for later analysis
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        logging.info(f"Found {len(all_focusable)} potentially focusable elements")
        
        # Store information about each focusable element
        focusable_elements_info = []
        for element in all_focusable:
            if element.is_displayed() and element.is_enabled():
                info = {
                    "element": element,
                    "tag": element.tag_name,
                    "id": element.get_attribute("id") or "",
                    "text": element.text.strip() if element.text else get_element_accessible_name(element),
                    "tabindex": element.get_attribute("tabindex"),
                    "position": get_element_position(element)
                }
                focusable_elements_info.append(info)
        
        # Detect actual tab sequence using keyboard navigation
        tab_sequence = detect_tab_sequence(driver, max_elements=len(focusable_elements_info) * 2)
        results["tab_sequence"] = tab_sequence
        
        # Check for specific focus order issues
        check_for_positive_tabindex(tab_sequence, results)
        check_reading_order_violations(tab_sequence, results)
        check_form_field_sequence(tab_sequence, results)
        check_modal_dialog_focus(driver, tab_sequence, results)
        check_skip_links(driver, tab_sequence, results)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking focus order: {str(e)}")
        results["error"] = str(e)
        return results

def detect_tab_sequence(driver, max_elements=100):
    """Detect the actual tab sequence of the page by simulating keyboard tabbing"""
    tab_sequence = []
    
    # Start with pressing Tab once to get to first element
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    body.send_keys(Keys.TAB)
    
    # Keep track of already focused elements to detect cycles
    focused_signatures = set()
    
    for i in range(max_elements):
        # Get currently focused element
        active_element = driver.execute_script("return document.activeElement;")
        
        # Skip if we've already seen this element (avoid infinite loops)
        element_signature = generate_element_signature(active_element)
        if element_signature in focused_signatures:
            # If we're back at the first element, we've completed the tab cycle
            if len(tab_sequence) > 1 and element_signature == generate_element_signature(tab_sequence[0]["element"]):
                break
            # Otherwise we might be stuck in a sub-cycle, keep going a bit longer
            if len(focused_signatures) > 5:  # Allow a few duplicate focuses before giving up
                break
        
        # Add to our sequence
        element_info = {
            "element": active_element,
            "tag": active_element.tag_name if hasattr(active_element, 'tag_name') else active_element.get_attribute("tagName").lower(),
            "id": active_element.get_attribute("id") or "",
            "text": active_element.text.strip() if hasattr(active_element, 'text') and active_element.text else get_element_accessible_name(active_element),
            "tabindex": active_element.get_attribute("tabindex"),
            "position": get_element_position(active_element),
            "tab_index": i + 1  # 1-based index of tab sequence
        }
        
        tab_sequence.append(element_info)
        focused_signatures.add(element_signature)
        
        # Move to next element
        active_element.send_keys(Keys.TAB)
        
        # Small delay to allow focus to settle (helps with dynamic pages)
        time.sleep(0.05)
    
    return tab_sequence

def check_for_positive_tabindex(tab_sequence, results):
    """Check for elements with tabindex > 0, which can disrupt natural tab order"""
    for element_info in tab_sequence:
        tabindex = element_info.get("tabindex", "")
        if tabindex and tabindex.isdigit() and int(tabindex) > 0:
            results["issues"].append({
                "element": element_info.get("tag", "unknown"),
                "text": element_info.get("text", "[No text]"),
                "issue": "Inconsistent keyboard navigation sequence",
                "details": f"Element has tabindex={tabindex}, which overrides the natural DOM order",
                "recommendation": "Use tabindex='0' to make elements focusable in their natural DOM order",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_reading_order_violations(tab_sequence, results):
    """Check if focus order follows visual/reading order"""
    # Skip if we have less than 3 elements
    if len(tab_sequence) < 3:
        return
    
    # Look for cases where focus jumps around unnaturally
    for i in range(1, len(tab_sequence) - 1):
        current = tab_sequence[i]
        prev = tab_sequence[i-1]
        next_elem = tab_sequence[i+1]
        
        # Skip elements without position info
        if not current.get("position") or not prev.get("position") or not next_elem.get("position"):
            continue
        
        # Check for focus moving backwards against reading order
        # First check if we're moving down the page as expected
        if prev["position"]["y"] < current["position"]["y"]:
            # Then check if next focus moves back up significantly
            if next_elem["position"]["y"] < current["position"]["y"] - 50:
                # Only flag if it's not just moving to a new column
                if abs(next_elem["position"]["x"] - current["position"]["x"]) < 200:
                    results["issues"].append({
                        "element": current.get("tag", "unknown"),
                        "text": current.get("text", "[No text]"),
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Focus jumps backwards against the expected reading order",
                        "recommendation": "Ensure focus order follows the natural reading order of the page",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })

def check_form_field_sequence(tab_sequence, results):
    """Check if form fields are in a logical sequence"""
    # Identify form sections
    form_sections = []
    current_section = []
    
    for element_info in tab_sequence:
        tag = element_info.get("tag", "").lower()
        if tag in ["input", "select", "textarea"] or element_info.get("role") in ["textbox", "combobox", "listbox"]:
            current_section.append(element_info)
        elif current_section:
            # End of a form section (non-form element encountered after form elements)
            if len(current_section) > 1:
                form_sections.append(current_section)
            current_section = []
    
    # Add last section if it exists
    if len(current_section) > 1:
        form_sections.append(current_section)
    
    # Check each form section
    for section in form_sections:
        # Check if fields are in a logical vertical order
        is_vertical_form = True
        for i in range(1, len(section)):
            prev = section[i-1]
            current = section[i]
            
            # If fields are side by side, it's not a simple vertical form
            if prev.get("position") and current.get("position"):
                if abs(prev["position"]["y"] - current["position"]["y"]) < 30:
                    is_vertical_form = False
                    break
        
        # For vertical forms, check if tab order follows visual order
        if is_vertical_form:
            for i in range(1, len(section)):
                prev = section[i-1]
                current = section[i]
                
                if prev.get("position") and current.get("position"):
                    # If next field is above previous, that's counter-intuitive
                    if current["position"]["y"] < prev["position"]["y"] - 30:
                        results["issues"].append({
                            "element": current.get("tag", "unknown"),
                            "text": current.get("text", "[No text]"),
                            "issue": "Inconsistent keyboard navigation sequence in form",
                            "details": "Form fields do not follow a logical top-to-bottom sequence",
                            "recommendation": "Ensure form fields receive focus in a logical order that matches visual layout",
                            "wcag": "2.4.3",
                            "severity": "warning"
                        })
                        break

def check_modal_dialog_focus(driver, tab_sequence, results):
    """Check if there are modal dialogs and if focus is properly trapped within them"""
    # Look for modal dialogs
    modal_dialogs = driver.find_elements(By.CSS_SELECTOR, 
        "[role='dialog'], [aria-modal='true'], .modal, .dialog, .overlay:not([aria-hidden='true'])")
    
    if not modal_dialogs:
        return
        
    for dialog in modal_dialogs:
        # Skip hidden dialogs
        if not dialog.is_displayed():
            continue
            
        # Check if dialog has aria-modal attribute
        aria_modal = dialog.get_attribute("aria-modal")
        if aria_modal != "true":
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog missing aria-modal attribute",
                "details": "Modal dialog should have aria-modal='true' to indicate it traps focus",
                "recommendation": "Add aria-modal='true' to modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })
        
        # Check focus management
        focusable_elements = dialog.find_elements(By.CSS_SELECTOR, 
            "a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")
        
        if not focusable_elements:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog has no focusable elements",
                "details": "Modal dialogs should contain focusable elements",
                "recommendation": "Ensure modal dialogs have focusable elements like buttons for user interaction",
                "wcag": "2.4.3",
                "severity": "critical"
            })
            continue
            
        # Simulate tabbing through the dialog to check if focus stays within
        # This would require more complex testing logic to implement fully
        # For now, we'll just check if the dialog has a close/cancel button
        close_buttons = dialog.find_elements(By.CSS_SELECTOR, 
            "button:not([aria-hidden='true']), [role='button']:not([aria-hidden='true']), " +
            "[aria-label*='close' i], [aria-label*='cancel' i], " +
            "[class*='close' i], [id*='close' i], [class*='cancel' i], [id*='cancel' i]")
            
        if not close_buttons:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog may lack closing mechanism",
                "details": "No obvious close button found in modal dialog",
                "recommendation": "Provide a visible close button in modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_skip_links(driver, tab_sequence, results):
    """Check if skip links are present and working"""
    # Look for common skip link patterns
    skip_links = driver.find_elements(By.CSS_SELECTOR, 
        "a[href^='#']:not([aria-hidden='true'])")
    
    skip_link_found = False
    for link in skip_links:
        link_text = link.text.strip() if link.text else ""
        if not link_text:
            link_text = link.get_attribute("aria-label") or ""
            
        # Look for common skip link text patterns
        if any(pattern in link_text.lower() for pattern in ["skip", "jump", "content", "main"]):
            skip_link_found = True
            
            # Check if skip link is one of the first elements in tab order
            if tab_sequence and len(tab_sequence) > 2:
                first_elements = [tab_sequence[0], tab_sequence[1]] if len(tab_sequence) > 1 else [tab_sequence[0]]
                skip_link_in_tab_order = any(
                    element.get("tag") == "a" and element.get("text") == link_text
                    for element in first_elements
                )
                
                if not skip_link_in_tab_order:
                    results["issues"].append({
                        "element": "a",
                        "text": link_text,
                        "issue": "Skip link not at start of tab order",
                        "details": "Skip navigation link should be one of the first focusable elements",
                        "recommendation": "Move skip link to the beginning of the page code so it's encountered early in tab order",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })
    
    # If no skip links found on a page with significant content, suggest adding one
    if not skip_link_found:
        # Check if page has a substantial amount of navigation before main content
        nav_elements = driver.find_elements(By.CSS_SELECTOR, 
            "nav, [role='navigation'], #navigation, .navigation, .nav, #nav, header")
        
        if nav_elements and len(tab_sequence) > 10:
            results["issues"].append({
                "element": "page",
                "issue": "Missing skip navigation link",
                "details": "Page has substantial navigation but no skip link was found",
                "recommendation": "Add a skip link at the beginning of the page to allow keyboard users to skip navigation",
                "wcag": "2.4.3",
                "severity": "warning"
            })

# Helper functions

def get_element_position(element):
    """Get the position and dimensions of an element"""
    try:
        rect = element.rect
        return {
            "x": rect.get('x', 0),
            "y": rect.get('y', 0),
            "width": rect.get('width', 0),
            "height": rect.get('height', 0),
            "midX": rect.get('x', 0) + rect.get('width', 0) / 2,
            "midY": rect.get('y', 0) + rect.get('height', 0) / 2
        }
    except:
        return None

def get_element_accessible_name(element):
    """Try to get the accessible name of an element through various attributes"""
    accessible_name = ""
    try:
        # Try aria-label
        accessible_name = element.get_attribute("aria-label") or ""
        if accessible_name:
            return f"[{accessible_name}]"
            
        # Try placeholder
        if element.tag_name.lower() in ["input", "textarea"]:
            placeholder = element.get_attribute("placeholder") or ""
            if placeholder:
                return f"[Placeholder: {placeholder}]"
            
            # Try value
            value = element.get_attribute("value") or ""
            if value:
                return f"[Value: {value}]"
                
        # Try title
        title = element.get_attribute("title") or ""
        if title:
            return f"[Title: {title}]"
            
        # Try name
        name = element.get_attribute("name") or ""
        if name:
            return f"[Name: {name}]"
            
        return "[No text]"
    except:
        return "[No text]"

def generate_element_signature(element):
    """Generate a unique-ish signature for an element to detect duplicates in tab order"""
    try:
        tag = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_id = element.get_attribute("id") or ""
        classes = element.get_attribute("class") or ""
        text = element.text[:50] if hasattr(element, 'text') and element.text else ""
        
        return f"{tag}#{element_id}.{classes}:{text}"
    except:
        return "unknown"