"""
ARIA Checker Module
Checks for proper use of ARIA attributes and keyboard accessibility features.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

def check_aria_accessibility(driver):
    """
    Check ARIA and keyboard accessibility of a webpage.
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of ARIA and keyboard accessibility checks
    """
    logging.info("Checking ARIA and keyboard accessibility...")
    results = {
        "status": "completed",
        "issues": []
    }
    
    try:
        # Check for elements with ARIA roles but missing required attributes
        elements_with_roles = driver.find_elements(By.CSS_SELECTOR, "[role]")
        
        for element in elements_with_roles:
            role = element.get_attribute("role")
            
            # Check common required attributes for specific roles
            if role == "checkbox" or role == "switch":
                if not element.get_attribute("aria-checked"):
                    results["issues"].append({
                        "element": element.tag_name,
                        "text": element.text.strip() if element.text else "[No text]",
                        "issue": "Incomplete ARIA implementation",
                        "details": f"Element with role='{role}' is missing required aria-checked attribute",
                        "recommendation": f"Add aria-checked attribute to the {role} element",
                        "wcag": "4.1.2",
                        "severity": "critical"
                    })
            
            elif role == "combobox":
                if not element.get_attribute("aria-expanded"):
                    results["issues"].append({
                        "element": element.tag_name,
                        "text": element.text.strip() if element.text else "[No text]",
                        "issue": "Incomplete ARIA implementation",
                        "details": "Combobox is missing required aria-expanded attribute",
                        "recommendation": "Add aria-expanded attribute to the combobox element",
                        "wcag": "4.1.2",
                        "severity": "critical"
                    })
            
            elif role in ["slider", "progressbar", "scrollbar"]:
                if not element.get_attribute("aria-valuenow") or not element.get_attribute("aria-valuemin") or not element.get_attribute("aria-valuemax"):
                    results["issues"].append({
                        "element": element.tag_name,
                        "text": element.text.strip() if element.text else "[No text]",
                        "issue": "Incomplete ARIA implementation",
                        "details": f"Element with role='{role}' is missing required value attributes",
                        "recommendation": "Add aria-valuenow, aria-valuemin, and aria-valuemax attributes",
                        "wcag": "4.1.2",
                        "severity": "critical"
                    })
        
        # Check for elements that have aria-hidden="true" but are focusable
        hidden_elements = driver.find_elements(By.CSS_SELECTOR, "[aria-hidden='true']")
        for element in hidden_elements:
            tabindex = element.get_attribute("tabindex")
            if tabindex and tabindex != "-1":
                results["issues"].append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "issue": "Inconsistent accessibility attributes",
                    "details": "Element is aria-hidden='true' but remains in the tab order",
                    "recommendation": "Add tabindex='-1' to elements with aria-hidden='true'",
                    "wcag": "1.3.1",
                    "severity": "critical"
                })
                
            # Check if hidden element has focusable children
            focusable_children = element.find_elements(By.CSS_SELECTOR, 
                "a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")
            
            if focusable_children:
                results["issues"].append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "issue": "Hidden element contains focusable elements",
                    "details": f"Element with aria-hidden='true' contains {len(focusable_children)} focusable children",
                    "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
                    "wcag": "1.3.1",
                    "severity": "critical"
                })
        
        # Check for form elements without associated labels
        form_elements = driver.find_elements(By.CSS_SELECTOR, 
            "input:not([type='hidden']), select, textarea")
            
        for element in form_elements:
            has_label = False
            
            # Check for explicit label
            element_id = element.get_attribute("id")
            if element_id:
                label = driver.execute_script(
                    "return document.querySelector('label[for=\"" + element_id + "\"]');"
                )
                has_label = label is not None
            
            # Check for aria-label
            aria_label = element.get_attribute("aria-label")
            has_label = has_label or (aria_label is not None and aria_label.strip() != "")
            
            # Check for aria-labelledby
            aria_labelledby = element.get_attribute("aria-labelledby")
            if aria_labelledby:
                # Check if the referenced element exists
                referenced_element = driver.execute_script(
                    "return document.getElementById('" + aria_labelledby + "');"
                )
                has_label = has_label or referenced_element is not None
            
            # Check for implicit label (element is inside a label tag)
            parent_label = driver.execute_script(
                "return arguments[0].closest('label');", element
            )
            has_label = has_label or parent_label is not None
            
            # Check for placeholder (not sufficient for accessibility but common)
            placeholder = element.get_attribute("placeholder")
            has_placeholder = placeholder is not None and placeholder.strip() != ""
            
            if not has_label:
                severity = "critical"
                issue = "Form element without label"
                if has_placeholder:
                    severity = "warning"
                    issue = "Form element with placeholder but no label"
                
                results["issues"].append({
                    "element": element.tag_name,
                    "type": element.get_attribute("type") or element.tag_name,
                    "issue": issue,
                    "details": "Form control lacks proper labeling for screen readers",
                    "recommendation": "Add an associated label, aria-label, or aria-labelledby attribute",
                    "wcag": "1.3.1, 3.3.2",
                    "severity": severity
                })
        
        # Check for buttons without accessible names
        buttons = driver.find_elements(By.CSS_SELECTOR, 
            "button, [role='button'], input[type='button'], input[type='submit'], input[type='reset']")
            
        for button in buttons:
            # Check various ways a button can have an accessible name
            button_text = button.text.strip() if hasattr(button, 'text') else ""
            aria_label = button.get_attribute("aria-label") or ""
            has_accessible_name = (
                button_text != "" or 
                aria_label.strip() != "" or 
                button.get_attribute("aria-labelledby") is not None or
                button.get_attribute("title") is not None or
                button.get_attribute("value") is not None
            )
            
            # Also check for icon buttons with aria-hidden icons
            if not has_accessible_name:
                # Check for child img or svg elements
                has_img = len(button.find_elements(By.TAG_NAME, "img")) > 0
                has_svg = len(button.find_elements(By.TAG_NAME, "svg")) > 0
                has_icon_class = any(cls for cls in (button.get_attribute("class") or "").split() 
                                    if "icon" in cls.lower())
                
                if has_img or has_svg or has_icon_class:
                    results["issues"].append({
                        "element": button.tag_name,
                        "issue": "Button without accessible name",
                        "details": "Icon button lacks text alternative for screen readers",
                        "recommendation": "Add aria-label or visible text to describe button's purpose",
                        "wcag": "4.1.2",
                        "severity": "critical"
                    })
        
        # Add more ARIA checks as needed
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking ARIA accessibility: {str(e)}")
        results["error"] = str(e)
        return results