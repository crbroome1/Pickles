"""
Focusable Elements Module
Detects elements that should be keyboard-accessible but aren't.
Enhanced version with better error handling and robust element detection.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException

def check_missing_focusable_elements(driver):
    """
    Identifies potentially interactive elements that should be focusable but aren't.
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        list: Elements missing proper keyboard accessibility
    """
    logging.info("Checking for keyboard navigation barriers...")
    missing_focusable = []
    
    try:
        # Get all potentially interactive elements
        # This uses a comprehensive selector to find elements that appear interactive
        potential_interactive_selectors = [
            # Common clickable elements
            "a:not([href='#']):not([href='javascript:void(0)']):not([tabindex='-1']):not([role='presentation'])",
            "button:not([tabindex='-1']):not([disabled])",
            "[onclick]:not([tabindex='-1']):not([role='presentation'])",
            
            # Elements with interactive roles
            "[role='button']:not([tabindex='-1'])",
            "[role='link']:not([tabindex='-1'])",
            "[role='checkbox']:not([tabindex='-1'])",
            "[role='menuitem']:not([tabindex='-1'])",
            "[role='tab']:not([tabindex='-1'])",
            
            # Form controls
            "input:not([type='hidden']):not([tabindex='-1']):not([disabled])",
            "select:not([tabindex='-1']):not([disabled])",
            "textarea:not([tabindex='-1']):not([disabled])",
            
            # Interactive HTML5 elements
            "details:not([tabindex='-1'])",
            "summary:not([tabindex='-1'])",
            
            # Custom elements that look interactive by class/styling
            "[class*='button']:not(button):not(a):not([role='button']):not([tabindex='-1'])",
            "[class*='btn']:not(button):not(a):not([role='button']):not([tabindex='-1'])",
            "[class*='clickable']:not([tabindex='-1'])"
        ]
        
        # Find all potentially interactive elements, filter for visible ones
        all_potential_interactive = []
        for selector in potential_interactive_selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    try:
                        if element.is_displayed() and element.is_enabled():
                            all_potential_interactive.append(element)
                    except StaleElementReferenceException:
                        continue
            except Exception as e:
                logging.warning(f"Error finding elements with selector '{selector}': {str(e)}")
        
        # Remove duplicates by checking tag, id, and classes
        unique_elements = []
        unique_signatures = set()
        
        for element in all_potential_interactive:
            try:
                tag = element.tag_name if hasattr(element, 'tag_name') else "unknown"
                element_id = element.get_attribute("id") or ""
                element_class = element.get_attribute("class") or ""
                
                # Create a signature for this element
                signature = f"{tag}#{element_id}.{element_class}"
                
                if signature not in unique_signatures:
                    unique_signatures.add(signature)
                    unique_elements.append(element)
            except StaleElementReferenceException:
                continue
        
        logging.info(f"Found {len(unique_elements)} potentially interactive elements")
        
        # Check each element to see if it's properly focusable
        for element in unique_elements:
            try:
                # Skip elements that are likely not meant to be interactive
                if is_likely_decorative(element):
                    continue
                
                # Check for explicit tabindex=-1 (intentionally not focusable)
                tabindex = element.get_attribute("tabindex")
                if tabindex == "-1":
                    # Only report this as an issue if the element looks interactive
                    if looks_interactive(element):
                        missing_focusable.append({
                            "element": element.tag_name,
                            "text": get_element_text(element),
                            "issue": "Keyboard navigation barrier",
                            "details": "Interactive element with tabindex=-1",
                            "recommendation": "Remove tabindex=-1 or provide alternative keyboard access",
                            "wcag": "2.1.1"
                        })
                    continue
                
                # Check if the element is focusable using a safe approach
                is_focusable = check_if_focusable_safely(driver, element)
                
                # If it's not focusable but looks interactive, that's an issue
                if not is_focusable and looks_interactive(element):
                    missing_focusable.append({
                        "element": element.tag_name,
                        "text": get_element_text(element),
                        "location": get_element_location(element),
                        "issue": "Keyboard navigation barrier",
                        "details": "Element appears interactive but isn't keyboard accessible",
                        "recommendation": "Add proper keyboard accessibility (tabindex='0' and keyboard event handlers)",
                        "wcag": "2.1.1"
                    })
            except StaleElementReferenceException:
                continue
            except Exception as e:
                logging.warning(f"Error checking element: {str(e)}")
                continue
        
        logging.info(f"Found {len(missing_focusable)} elements with keyboard accessibility issues")
        return missing_focusable
    
    except WebDriverException as e:
        logging.error(f"Error checking for missing focusable elements: {str(e)}")
        return [{"error": str(e)}]

def check_if_focusable_safely(driver, element):
    """
    Safely check if an element can receive focus
    """
    try:
        # Method 1: Use JavaScript to check if element is focusable
        # This avoids actually changing focus, which is safer
        is_focusable = driver.execute_script("""
            var elem = arguments[0];
            
            // Skip elements that are likely not meant to be interactive
            if (window.getComputedStyle(elem).display === 'none' || 
                window.getComputedStyle(elem).visibility === 'hidden') {
                return false;
            }
            
            // These elements are inherently focusable if not disabled
            var nodeName = elem.nodeName.toLowerCase();
            if (nodeName === 'a' || nodeName === 'area') {
                return !!elem.href;
            }
            if (nodeName === 'input' || nodeName === 'select' || nodeName === 'textarea' || 
                nodeName === 'button') {
                return !elem.disabled;
            }
            
            // Check if it has a non-negative tabindex
            if (elem.hasAttribute('tabindex')) {
                return parseInt(elem.getAttribute('tabindex')) >= 0;
            }
            
            // Some elements can be focused by default 
            return nodeName === 'iframe' || nodeName === 'details' || 
                   nodeName === 'summary' || elem.isContentEditable;
        """, element)
        
        return is_focusable
    except Exception as e:
        logging.warning(f"Error in focusability check: {str(e)}")
        # Fall back to a simpler check
        try:
            # Check for elements that should be focusable by default
            tag = element.tag_name.lower()
            if tag in ['a', 'button', 'input', 'select', 'textarea', 'details', 'summary']:
                return True
                
            # Check for tabindex
            tabindex = element.get_attribute('tabindex')
            if tabindex and tabindex != '-1':
                return True
                
            # Check for role that implies interactivity
            role = element.get_attribute('role')
            if role in ['button', 'link', 'checkbox', 'radio', 'menuitem', 'tab']:
                return True
                
            return False
        except Exception:
            return False

def looks_interactive(element):
    """
    Check if an element appears to be interactive based on various heuristics
    """
    try:
        # Check for elements that are inherently interactive
        tag = element.tag_name.lower()
        if tag in ['a', 'button', 'input', 'select', 'textarea']:
            return True
        
        # Check for ARIA roles that suggest interactivity
        role = element.get_attribute('role')
        if role in ['button', 'link', 'checkbox', 'radio', 'tab', 'menuitem']:
            return True
        
        # Check for onclick attributes
        if element.get_attribute('onclick'):
            return True
        
        # Check for class names that suggest interactivity
        class_attr = element.get_attribute('class') or ''
        interactive_classes = ['button', 'btn', 'link', 'clickable', 'selectable', 'toggle']
        if any(cls in class_attr.lower() for cls in interactive_classes):
            return True
        
        # Check for cursor style
        try:
            cursor = element.value_of_css_property('cursor')
            if cursor in ['pointer', 'hand']:
                return True
        except:
            pass
        
        return False
    except:
        return False

def is_likely_decorative(element):
    """
    Check if an element is likely decorative rather than interactive
    """
    try:
        # Check for presentation role
        role = element.get_attribute('role')
        if role in ['presentation', 'none']:
            return True
        
        # Check for aria-hidden
        aria_hidden = element.get_attribute('aria-hidden')
        if aria_hidden == 'true':
            return True
        
        # Check if it's an empty/spacer element
        if element.get_attribute('class') and ('spacer' in element.get_attribute('class').lower() or 
                                              'divider' in element.get_attribute('class').lower()):
            return True
        
        return False
    except:
        return False

def get_element_text(element):
    """Get readable text from an element, looking at various attributes"""
    try:
        # Try visible text first
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        if element_text:
            return element_text
        
        # Check for aria-label
        aria_label = element.get_attribute("aria-label")
        if aria_label:
            return f"[aria-label: {aria_label}]"
        
        # Check for title
        title = element.get_attribute("title")
        if title:
            return f"[title: {title}]"
        
        # Check for value (for inputs)
        value = element.get_attribute("value")
        if value:
            return f"[value: {value}]"
        
        # Check for placeholder
        placeholder = element.get_attribute("placeholder")
        if placeholder:
            return f"[placeholder: {placeholder}]"
        
        # Check for image alt text
        try:
            img = element.find_element(By.TAG_NAME, "img")
            alt = img.get_attribute("alt")
            if alt:
                return f"[image: {alt}]"
        except:
            pass
        
        # Return a fallback
        tag = element.tag_name if hasattr(element, 'tag_name') else "unknown"
        element_id = element.get_attribute("id") or ""
        
        if element_id:
            return f"[{tag} id={element_id}]"
        else:
            return f"[{tag}]"
    except:
        return "[No text]"

def get_element_location(element):
    """Get a readable description of an element's location in the page"""
    try:
        # Try to get an ID
        element_id = element.get_attribute("id")
        if element_id:
            return f"id='{element_id}'"
            
        # Try to get a class
        element_class = element.get_attribute("class")
        if element_class:
            return f"class='{element_class}'"
            
        # Try to get nearby text
        try:
            parent = element.find_element(By.XPATH, "./..")
            parent_text = parent.text.strip()
            if parent_text and len(parent_text) < 50:  # Only use if it's reasonably short
                return f"near text '{parent_text}'"
        except:
            pass
            
        # Fallback to XPath
        return "in page (no specific identifier available)"
            
    except Exception:
        return "in page (location detection failed)"