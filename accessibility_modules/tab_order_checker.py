"""
Tab Order Checker Module
Checks the tab order of focusable elements to ensure they follow a logical sequence.
Enhanced with advanced focus order detection.
"""

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_tab_order(driver):
    """
    Checks the tab order of focusable elements on a webpage with improved detection.
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of tab order check including issues found
    """
    logging.info("Checking keyboard navigation sequence...")
    tab_order_results = {
        "tab_sequence": [],
        "issues": []
    }
    
    try:
        # Enhanced selector for potentially focusable elements
        # This better matches what browsers consider focusable
        focusable_selector = (
            "a[href]:not([tabindex='-1']), button:not([tabindex='-1']):not([disabled]), " +
            "input:not([type='hidden']):not([tabindex='-1']):not([disabled]), select:not([tabindex='-1']):not([disabled]), " +
            "textarea:not([tabindex='-1']):not([disabled]), [tabindex]:not([tabindex='-1']), [contenteditable='true']:not([tabindex='-1']), " +
            "details:not([tabindex='-1']), summary:not([tabindex='-1']), [role='button']:not([tabindex='-1']), " +
            "[role='link']:not([tabindex='-1']), [role='checkbox']:not([tabindex='-1']), [role='radio']:not([tabindex='-1']), " +
            "[role='tab']:not([tabindex='-1']), [role='menuitem']:not([tabindex='-1']), [role='combobox']:not([tabindex='-1']), " +
            "[role='listbox']:not([tabindex='-1']), [role='slider']:not([tabindex='-1']), [role='switch']:not([tabindex='-1']), " +
            "[role='textbox']:not([tabindex='-1']), [role='searchbox']:not([tabindex='-1']), [role='spinbutton']:not([tabindex='-1'])"
        )
        
        # Get all focusable elements and filter for visible ones
        logging.info("Finding potentially focusable elements...")
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        
        # Filter visible and enabled elements to get a more accurate count
        visible_focusable = []
        for element in all_focusable:
            try:
                if element.is_displayed() and element.is_enabled():
                    visible_focusable.append(element)
            except StaleElementReferenceException:
                continue
        
        logging.info(f"Found {len(all_focusable)} potentially focusable elements, {len(visible_focusable)} visible and enabled")
        tab_order_results["potentially_focusable_count"] = len(visible_focusable)
        
        # Attempt to follow tab sequence using multiple approaches
        tab_sequence = detect_tab_sequence_robustly(driver, visible_focusable)
        tab_order_results["tab_sequence"] = tab_sequence
        
        # Analyze the tab order for issues
        analyze_tab_order(tab_order_results)
        
        return tab_order_results
        
    except WebDriverException as e:
        logging.error(f"Error checking tab order: {str(e)}")
        tab_order_results["error"] = str(e)
        return tab_order_results

def detect_tab_sequence_robustly(driver, visible_focusable):
    """Enhanced tab sequence detection with multiple fallback strategies"""
    try:
        # First attempt: Traditional method with direct tabbing
        tab_sequence = attempt_direct_tab_sequence(driver, len(visible_focusable))
        
        # If we didn't get many elements, try alternative approach
        if len(tab_sequence) < min(10, len(visible_focusable) / 5):
            logging.info(f"Direct tabbing only found {len(tab_sequence)} elements. Trying JavaScript approach...")
            tab_sequence = attempt_javascript_tab_sequence(driver, visible_focusable)
        
        # If still not enough elements, try a hybrid approach
        if len(tab_sequence) < min(10, len(visible_focusable) / 5):
            logging.info(f"JavaScript approach only found {len(tab_sequence)} elements. Trying hybrid approach...")
            tab_sequence = attempt_hybrid_tab_sequence(driver, visible_focusable)
        
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in robust tab sequence detection: {str(e)}")
        # Return whatever we have so far
        return tab_sequence if 'tab_sequence' in locals() else []

def attempt_direct_tab_sequence(driver, max_elements):
    """Attempt to detect tab sequence by directly sending Tab keys"""
    tab_sequence = []
    focused_signatures = set()
    
    # Reset to beginning of document
    try:
        driver.execute_script("document.activeElement.blur();")
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()
    except Exception as e:
        logging.warning(f"Couldn't reset focus: {str(e)}")
    
    # Use a longer timeout for slow-loading pages
    timeout = 10  # seconds
    start_time = time.time()
    
    # First press Tab to start
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        time.sleep(0.5)  # Give the page time to update focus
    except Exception as e:
        logging.warning(f"Couldn't send initial tab: {str(e)}")
    
    # Loop through elements with tab
    for i in range(min(max_elements, 100)):  # Limit to avoid infinite loops
        if time.time() - start_time > timeout:
            logging.warning("Timeout reached while detecting tab sequence")
            break
            
        try:
            # Get current active element
            active_element = driver.execute_script("return document.activeElement;")
            
            # Generate a signature to detect cycles
            element_signature = generate_element_signature(active_element)
            
            # Skip if we've seen this element (avoid infinite loops)
            if element_signature in focused_signatures:
                # If we're back at the first element, we've completed a cycle
                if len(tab_sequence) > 1 and element_signature == generate_element_signature(tab_sequence[0]["element"]):
                    logging.info("Detected full tab cycle - stopping")
                    break
                else:
                    # Allow some duplicates (some widgets cycle through their own elements)
                    duplicate_count = sum(1 for sig in focused_signatures if sig == element_signature)
                    if duplicate_count > 2:
                        logging.info(f"Detected too many duplicates of {element_signature} - stopping")
                        break
            
            # Add to tab sequence
            element_info = get_element_info(active_element)
            element_info["signature"] = element_signature
            element_info["tab_index"] = i + 1
            tab_sequence.append(element_info)
            focused_signatures.add(element_signature)
            
            # Send Tab to go to next element
            active_element.send_keys(Keys.TAB)
            time.sleep(0.2)  # Small delay to allow focus to move
            
        except Exception as e:
            logging.warning(f"Error in tab sequence at step {i+1}: {str(e)}")
            break
    
    logging.info(f"Direct tabbing detected {len(tab_sequence)} elements")
    return tab_sequence

def attempt_javascript_tab_sequence(driver, visible_focusable):
    """Use JavaScript to analyze and determine the tab sequence"""
    tab_sequence = []
    
    try:
        # Use JavaScript to get elements sorted by tabindex
        sorted_elements = driver.execute_script("""
            // Get all focusable elements
            var elements = Array.from(arguments[0]);
            
            // Sort them by tabindex
            elements.sort(function(a, b) {
                var aTabIndex = parseInt(a.getAttribute('tabindex'));
                var bTabIndex = parseInt(b.getAttribute('tabindex'));
                
                // Elements with positive tabindex come first (in numerical order)
                if (!isNaN(aTabIndex) && aTabIndex > 0 && (!isNaN(bTabIndex) && bTabIndex > 0)) {
                    return aTabIndex - bTabIndex;
                }
                
                // Elements with positive tabindex come before elements with tabindex="0" or no tabindex
                if (!isNaN(aTabIndex) && aTabIndex > 0) {
                    return -1;
                }
                if (!isNaN(bTabIndex) && bTabIndex > 0) {
                    return 1;
                }
                
                // Otherwise, use DOM order
                return 0;
            });
            
            return elements;
        """, visible_focusable)
        
        # Convert to tab sequence format
        for i, element in enumerate(sorted_elements):
            element_info = get_element_info(element)
            element_info["signature"] = generate_element_signature(element)
            element_info["tab_index"] = i + 1
            tab_sequence.append(element_info)
        
        logging.info(f"JavaScript approach detected {len(tab_sequence)} elements")
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in JavaScript tab sequence: {str(e)}")
        return []

def attempt_hybrid_tab_sequence(driver, visible_focusable):
    """Combine direct interaction and estimation to determine tab sequence"""
    tab_sequence = []
    
    try:
        # Sample a subset of elements to test direct focus
        sample_size = min(20, len(visible_focusable))
        sample = visible_focusable[:sample_size]
        
        for i, element in enumerate(sample):
            try:
                # Try to focus the element directly
                driver.execute_script("arguments[0].focus();", element)
                time.sleep(0.1)
                
                # Check if it actually received focus
                active_element = driver.execute_script("return document.activeElement;")
                
                # If it did, add it to our sequence
                if active_element == element:
                    element_info = get_element_info(element)
                    element_info["signature"] = generate_element_signature(element)
                    element_info["tab_index"] = i + 1
                    element_info["verified_focusable"] = True
                    tab_sequence.append(element_info)
            except Exception:
                continue
        
        # If we found some focusable elements, extrapolate to the rest
        if tab_sequence:
            # Estimate how many elements are likely focusable based on our sample
            focusable_ratio = len(tab_sequence) / sample_size
            estimated_total = int(len(visible_focusable) * focusable_ratio)
            
            logging.info(f"Hybrid approach found {len(tab_sequence)} focusable elements in sample")
            logging.info(f"Estimated total focusable elements: {estimated_total}")
            
            # Add remaining visible elements with a note that they're estimated
            remaining = visible_focusable[sample_size:]
            for i, element in enumerate(remaining[:50]):  # Limit to 50 more elements
                element_info = get_element_info(element)
                element_info["signature"] = generate_element_signature(element)
                element_info["tab_index"] = len(tab_sequence) + i + 1
                element_info["estimated_focusable"] = True
                tab_sequence.append(element_info)
        
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in hybrid tab sequence: {str(e)}")
        return tab_sequence if tab_sequence else []

def get_element_info(element):
    """Extract useful information about an element"""
    try:
        tag_name = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        
        info = {
            "element": element,
            "tag": tag_name,
            "id": element.get_attribute("id") or "",
            "class": element.get_attribute("class") or "",
            "role": element.get_attribute("role") or "",
            "tabindex": element.get_attribute("tabindex") or "auto",
            "text": element_text if element_text else "[No text]",
            "visible": element.is_displayed() if hasattr(element, 'is_displayed') else True
        }
        
        # Add special handling for form elements
        if tag_name in ["input", "select", "textarea"]:
            input_type = element.get_attribute("type") or "text"
            info["type"] = input_type
            
            # For inputs with no visible text, use placeholder or name
            if not element_text:
                placeholder = element.get_attribute("placeholder")
                name = element.get_attribute("name")
                aria_label = element.get_attribute("aria-label")
                
                if placeholder:
                    info["text"] = f"[Placeholder: {placeholder}]"
                elif aria_label:
                    info["text"] = f"[ARIA Label: {aria_label}]"
                elif name:
                    info["text"] = f"[Name: {name}]"
        
        # Handle element without text
        if info["text"] == "[No text]":
            # Try to get inner image alt text
            try:
                img = element.find_element(By.TAG_NAME, "img")
                alt = img.get_attribute("alt")
                if alt:
                    info["text"] = f"[Image: {alt}]"
            except:
                pass
                    
        # Get coordinates for position analysis (used to detect tab order vs visual order)
        if hasattr(element, 'rect'):
            location = element.rect
            info["position"] = {
                "x": location.get('x', 0),
                "y": location.get('y', 0),
                "width": location.get('width', 0),
                "height": location.get('height', 0)
            }
        
        return info
        
    except Exception as e:
        logging.warning(f"Error getting element info: {str(e)}")
        return {
            "tag": "unknown",
            "text": "[Error getting element info]",
            "error": str(e)
        }

def generate_element_signature(element):
    """Generate a unique-ish signature for an element to detect duplicates in tab order"""
    try:
        tag = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_id = element.get_attribute("id") or ""
        classes = element.get_attribute("class") or ""
        href = element.get_attribute("href") or ""
        src = element.get_attribute("src") or ""
        
        # Create a more distinctive signature
        signature_parts = [tag]
        if element_id:
            signature_parts.append(f"id={element_id}")
        if classes:
            signature_parts.append(f"class={classes}")
        if href:
            # Just include hostname from href to avoid long URLs
            try:
                from urllib.parse import urlparse
                hostname = urlparse(href).hostname or ""
                signature_parts.append(f"href={hostname}")
            except:
                signature_parts.append("href=...")
        if src:
            # Just include filename from src
            try:
                src_parts = src.split('/')
                signature_parts.append(f"src={src_parts[-1]}")
            except:
                signature_parts.append("src=...")
        
        return ":".join(signature_parts)
    except:
        return "unknown"

def analyze_tab_order(results):
    """Analyze tab sequence for accessibility issues"""
    tab_sequence = results["tab_sequence"]
    issues = []
    
    if len(tab_sequence) == 0:
        issues.append({
            "type": "critical",
            "issue": "No focusable elements found on the page",
            "wcag": "2.1.1",
            "impact": "Users who rely on keyboard navigation will be unable to interact with the page"
        })
        results["issues"] = issues
        return
    
    # Check for tabindex > 0 (which can disrupt natural tab order)
    for element in tab_sequence:
        tabindex = element.get("tabindex", "auto")
        if tabindex.isdigit() and int(tabindex) > 0:
            issues.append({
                "type": "warning",
                "tab_index": element.get("tab_index"),
                "element": f"{element.get('tag')} {element.get('text', '')}",
                "issue": "Inconsistent keyboard navigation sequence",
                "details": f"Element has tabindex={tabindex}, which can disrupt natural tab order",
                "recommendation": "Use tabindex='0' for interactive elements unless there's a compelling reason",
                "wcag": "2.4.3"
            })
    
    # Check for logical sequence (top to bottom, left to right)
    # This is a heuristic and might have false positives
    for i in range(1, len(tab_sequence) - 1):
        current = tab_sequence[i].get("position", {})
        next_elem = tab_sequence[i + 1].get("position", {})
        
        # Skip elements without position info
        if not current or not next_elem:
            continue
            
        # Very simple heuristic: 
        # If next element is higher on page (y is significantly smaller) but not in a new column
        if (next_elem.get("y", 0) < current.get("y", 0) - 50 and
                abs(next_elem.get("x", 0) - current.get("x", 0)) < 100):
            issues.append({
                "type": "warning",
                "tab_index": tab_sequence[i].get("tab_index"),
                "element": f"{tab_sequence[i].get('tag')} {tab_sequence[i].get('text', '')}",
                "next_element": f"{tab_sequence[i+1].get('tag')} {tab_sequence[i+1].get('text', '')}",
                "issue": "Inconsistent keyboard navigation sequence",
                "details": "Tab order might not follow visual layout (next element is above current)",
                "recommendation": "Check if the tab order follows a logical reading order",
                "wcag": "2.4.3"
            })
    
    # Check if sequence is too short compared to potential focusable elements
    potential_count = results.get("potentially_focusable_count", 0)
    if potential_count > 0 and len(tab_sequence) < potential_count / 3:  # If less than 1/3 are actually focusable
        issues.append({
            "type": "warning",
            "issue": "Keyboard navigation barrier",
            "details": f"Tab sequence ({len(tab_sequence)} elements) is much shorter than expected ({potential_count} potentially focusable elements)",
            "recommendation": "Check for elements that should be focusable but aren't",
            "wcag": "2.1.1",
            "notes": "Manual verification recommended - automated detection found fewer focusable elements than expected"
        })
    
    # Add advanced focus order analysis
    advanced_issues = check_visual_reading_order(tab_sequence)
    issues.extend(advanced_issues)
    
    # Add form field sequence analysis
    form_issues = check_form_field_sequence(tab_sequence)
    issues.extend(form_issues)
    
    results["issues"] = issues

def check_visual_reading_order(tab_sequence):
    """
    Identify cases where tab order doesn't follow visual reading order (top-to-bottom, left-to-right).
    Uses a more sophisticated approach to detect reading order violations.
    """
    issues = []
    
    # Get elements with position info
    elements_with_position = [e for e in tab_sequence if e.get("position")]
    
    # Skip if we don't have enough elements with position
    if len(elements_with_position) < 3:
        return issues
    
    # Define reading direction thresholds
    # These define how much movement in a direction is significant
    VERTICAL_THRESHOLD = 30  # px - Significant vertical movement
    HORIZONTAL_THRESHOLD = 50  # px - Significant horizontal movement
    
    # Track the current "reading line"
    current_reading_y = elements_with_position[0]["position"]["y"]
    last_line_x_boundary = 0
    
    # Analyze the sequence
    for i in range(1, len(elements_with_position)):
        prev = elements_with_position[i-1]
        current = elements_with_position[i]
        
        prev_pos = prev["position"]
        current_pos = current["position"]
        
        # Calculate position changes
        y_change = current_pos["y"] - prev_pos["y"]
        x_change = current_pos["x"] - prev_pos["x"]
        
        # Check if we're moving to a new reading line
        if abs(y_change) > VERTICAL_THRESHOLD:
            if y_change < 0:
                # Moving up - might be okay if it's a new column
                # Check if the horizontal position is significantly different
                if abs(current_pos["x"] - prev_pos["x"]) < HORIZONTAL_THRESHOLD:
                    # Not far enough horizontally to be a new column, likely an issue
                    issues.append({
                        "type": "warning",
                        "tab_index": current.get("tab_index"),
                        "element": f"{current.get('tag')} {current.get('text', '')}",
                        "prev_element": f"{prev.get('tag')} {prev.get('text', '')}",
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Tab order moves upward against the expected reading order",
                        "recommendation": "Ensure tab order follows the logical reading order of the content",
                        "wcag": "2.4.3"
                    })
            
            # Update the current reading line
            current_reading_y = current_pos["y"]
            last_line_x_boundary = prev_pos["x"] + prev_pos["width"]
        else:
            # Within the same reading line, check if we're going backward
            if x_change < -HORIZONTAL_THRESHOLD:
                # Moving significantly left on the same visual line
                # This might be okay if we're at the start of a new line that's very close to the previous
                if not (abs(y_change) > 10):  # Small vertical change
                    issues.append({
                        "type": "warning",
                        "tab_index": current.get("tab_index"),
                        "element": f"{current.get('tag')} {current.get('text', '')}",
                        "prev_element": f"{prev.get('tag')} {prev.get('text', '')}",
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Tab order moves backward (right to left) on the same line",
                        "recommendation": "Ensure tab order follows left-to-right reading direction within lines",
                        "wcag": "2.4.3"
                    })
    
    return issues

def check_form_field_sequence(tab_sequence):
    """
    Check if form fields follow a logical sequence.
    Focuses on identifying common form patterns and ensuring they follow expected tab order.
    """
    issues = []
    
    # Identify form fields
    form_fields = []
    for i, element in enumerate(tab_sequence):
        tag = element.get("tag", "").lower()
        role = element.get("role", "")
        
        if tag in ["input", "select", "textarea", "button"] or role in ["textbox", "combobox", "checkbox", "radio"]:
            form_fields.append((i, element))
    
    # Skip if not enough form fields
    if len(form_fields) < 2:
        return issues
    
    # Group form fields that appear to be part of the same form or section
    form_groups = []
    current_group = [form_fields[0]]
    
    for i in range(1, len(form_fields)):
        prev_idx, prev_field = form_fields[i-1]
        curr_idx, curr_field = form_fields[i]
        
        # Check if these are likely in the same form
        # If more than 3 other elements between them, likely different forms
        if curr_idx - prev_idx <= 3:
            current_group.append((curr_idx, curr_field))
        else:
            # Start a new group if we have enough fields
            if len(current_group) > 1:
                form_groups.append(current_group)
            current_group = [(curr_idx, curr_field)]
    
    # Add the last group if it exists
    if len(current_group) > 1:
        form_groups.append(current_group)
    
    # Check each group of form fields
    for group in form_groups:
        # Check if fields are in a logical order
        for i in range(1, len(group)):
            prev_idx, prev_field = group[i-1]
            curr_idx, curr_field = group[i]
            
            # Skip if no position info
            if not prev_field.get("position") or not curr_field.get("position"):
                continue
            
            prev_pos = prev_field["position"]
            curr_pos = curr_field["position"]
            
            # Check for unusual vertical ordering
            if curr_pos["y"] < prev_pos["y"] - 20:  # Moving up significantly
                # This field appears above the previous field but comes later in tab order
                issues.append({
                    "type": "warning",
                    "tab_index": curr_field.get("tab_index"),
                    "element": f"{curr_field.get('tag')} {curr_field.get('text', '')}",
                    "prev_element": f"{prev_field.get('tag')} {prev_field.get('text', '')}",
                    "issue": "Inconsistent form field tab order",
                    "details": "Form field appears above the previous field visually but comes later in tab order",
                    "recommendation": "Ensure form fields receive focus in a logical order matching their visual layout",
                    "wcag": "2.4.3"
                })
    
    return issues

def check_if_related_fields(field1, field2):
    """
    Check if two form fields are likely related (like label and input)
    This is a simple heuristic - it could be enhanced further
    """
    # For now, we're not using this in the form checks
    # This is a stub for future enhancement
    return False

def fields_properly_sequenced(field1, field2):
    """
    Check if related fields are properly sequenced
    This is a simple heuristic - it could be enhanced further
    """
    # For now, we're not using this in the form checks
    # This is a stub for future enhancement
    return True