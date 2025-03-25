"""
Color Contrast Checker Module
Analyzes text and background colors for sufficient contrast according to WCAG guidelines.
"""

import logging
import re
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import WebDriverException

def check_color_contrast(driver):
    """
    Analyze text and background colors for sufficient contrast according to WCAG guidelines.
    Addresses WCAG Success Criterion 1.4.3: Contrast (Minimum) and 1.4.11: Non-text Contrast
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of color contrast analysis
    """
    logging.info("Checking color contrast (WCAG 1.4.3, 1.4.11)...")
    results = {
        "status": "completed",
        "wcag_criterion": ["1.4.3", "1.4.11"],
        "elements_checked": 0,
        "issues": []
    }
    
    try:
        # Get visible text elements
        text_elements = driver.find_elements(By.CSS_SELECTOR, 
            "p, h1, h2, h3, h4, h5, h6, a, span, div, label, button, input, select, textarea, li, td, th")
        
        # Get UI components that need to meet non-text contrast requirements
        ui_components = driver.find_elements(By.CSS_SELECTOR,
            "button, [role='button'], input[type='button'], input[type='submit'], input[type='reset'], " +
            "input[type='checkbox'], input[type='radio'], input[type='range'], " +
            "progress, .progress, [role='progressbar'], " +
            "select, .dropdown, [role='menu'], [role='menuitem'], " +
            "a:not(:empty)")
        
        # Check text elements for contrast
        check_text_elements_contrast(driver, text_elements, results)
        
        # Check UI components for contrast
        check_ui_components_contrast(driver, ui_components, results)
        
        # Add summary information
        results["element_count"] = len(text_elements) + len(ui_components)
        results["elements_checked"] = results["element_count"]
        results["pass_rate"] = round(
            (results["elements_checked"] - len(results["issues"])) / results["elements_checked"] * 100
            if results["elements_checked"] > 0 else 0, 2)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking color contrast: {str(e)}")
        results["status"] = "error"
        results["error"] = str(e)
        return results

def check_text_elements_contrast(driver, elements, results):
    """Check contrast for text elements"""
    for element in elements:
        # Skip hidden elements
        if not element.is_displayed():
            continue
            
        # Skip elements with no text
        element_text = element.text.strip()
        if not element_text:
            continue
        
        # Skip very small text (likely not important)
        font_size = get_font_size(driver, element)
        if font_size and font_size < 8:
            continue
        
        try:
            # Get text and background colors
            text_color = get_element_text_color(driver, element)
            bg_color = get_element_background_color(driver, element)
            
            # Skip if we couldn't get the colors
            if not text_color or not bg_color:
                continue
                
            # Convert to RGB for contrast calculation
            text_rgb = convert_to_rgb(text_color)
            bg_rgb = convert_to_rgb(bg_color)
            
            if not text_rgb or not bg_rgb:
                continue
                
            # Calculate contrast ratio
            contrast_ratio = calculate_contrast_ratio(text_rgb, bg_rgb)
            
            # Determine if large text
            is_large_text = font_size and (font_size >= 18 or (font_size >= 14 and is_bold(driver, element)))
            
            # WCAG contrast requirements
            required_ratio = 3.0 if is_large_text else 4.5
            
            # Check if contrast is sufficient
            if contrast_ratio < required_ratio:
                issue = {
                    "element": element.tag_name,
                    "text": truncate_text(element_text, 50),
                    "issue": "Insufficient color contrast",
                    "details": f"Contrast ratio: {contrast_ratio:.2f}:1 (required: {required_ratio}:1)",
                    "colors": {
                        "text": text_color,
                        "background": bg_color
                    },
                    "recommendation": f"Increase contrast to at least {required_ratio}:1",
                    "wcag": "1.4.3",
                    "severity": "critical"
                }
                
                # Add font size info
                if font_size:
                    issue["font_size"] = f"{font_size}px"
                    issue["is_large_text"] = is_large_text
                
                results["issues"].append(issue)
        
        except Exception as e:
            logging.warning(f"Error checking contrast for element: {str(e)}")
            continue

def check_ui_components_contrast(driver, elements, results):
    """Check contrast for UI components (non-text)"""
    for element in elements:
        # Skip hidden elements
        if not element.is_displayed():
            continue
        
        try:
            # Get foreground and background colors
            border_color = get_element_border_color(driver, element)
            bg_color = get_element_background_color(driver, element)
            
            # Try to get the most prominent color for the component
            fg_color = None
            if border_color and border_color.lower() != "rgba(0, 0, 0, 0)" and border_color.lower() != "transparent":
                fg_color = border_color
            
            # If no border, use text color if it's an interactive element
            if not fg_color and element.tag_name in ["button", "a", "input", "select"]:
                fg_color = get_element_text_color(driver, element)
            
            # Skip if we couldn't get both colors
            if not fg_color or not bg_color:
                continue
                
            # Convert to RGB for contrast calculation
            fg_rgb = convert_to_rgb(fg_color)
            bg_rgb = convert_to_rgb(bg_color)
            
            if not fg_rgb or not bg_rgb:
                continue
                
            # Calculate contrast ratio
            contrast_ratio = calculate_contrast_ratio(fg_rgb, bg_rgb)
            
            # WCAG non-text contrast requirement is 3.0:1
            required_ratio = 3.0
            
            # Check if contrast is sufficient
            if contrast_ratio < required_ratio:
                element_text = element.text.strip() if element.text else ""
                element_type = element.get_attribute("type") or element.tag_name
                
                issue = {
                    "element": element.tag_name,
                    "type": element_type,
                    "text": truncate_text(element_text, 50) if element_text else f"[{element_type}]",
                    "issue": "Insufficient UI component contrast",
                    "details": f"Contrast ratio: {contrast_ratio:.2f}:1 (required: {required_ratio}:1)",
                    "colors": {
                        "foreground": fg_color,
                        "background": bg_color
                    },
                    "recommendation": f"Increase component contrast to at least {required_ratio}:1",
                    "wcag": "1.4.11",
                    "severity": "critical"
                }
                
                results["issues"].append(issue)
        
        except Exception as e:
            logging.warning(f"Error checking UI component contrast: {str(e)}")
            continue

# Helper functions

def get_element_text_color(driver, element):
    """Get the computed text color of an element"""
    return driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('color');", 
        element
    )

def get_element_background_color(driver, element):
    """Get the computed background color of an element"""
    bg_color = driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", 
        element
    )
    
    # If no background color (transparent), traverse up the DOM to find a parent with background
    if not bg_color or bg_color == "rgba(0, 0, 0, 0)" or bg_color == "transparent":
        bg_color = driver.execute_script("""
            function getBackgroundColor(element) {
                var bgColor = window.getComputedStyle(element).backgroundColor;
                if (bgColor === 'rgba(0, 0, 0, 0)' || bgColor === 'transparent') {
                    return element.parentElement ? getBackgroundColor(element.parentElement) : 'rgb(255, 255, 255)';
                }
                return bgColor;
            }
            return getBackgroundColor(arguments[0]);
        """, element)
    
    return bg_color

def get_element_border_color(driver, element):
    """Get the computed border color of an element"""
    return driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('border-color');", 
        element
    )

def get_font_size(driver, element):
    """Get the computed font size of an element in pixels"""
    font_size = driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('font-size');", 
        element
    )
    
    if font_size:
        # Convert to pixels if possible
        match = re.search(r'(\d+(\.\d+)?)px', font_size)
        if match:
            return float(match.group(1))
    
    return None

def is_bold(driver, element):
    """Check if an element has bold font weight"""
    font_weight = driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('font-weight');", 
        element
    )
    
    if font_weight:
        # Font weight of 700 or above is typically bold
        if font_weight.isdigit() and int(font_weight) >= 700:
            return True
        if font_weight == "bold" or font_weight == "bolder":
            return True
    
    return False

def convert_to_rgb(color):
    """Convert various color formats to RGB tuple"""
    try:
        # Handle rgb/rgba format
        if color.startswith("rgb"):
            matches = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color)
            if matches:
                return (
                    int(matches.group(1)),
                    int(matches.group(2)),
                    int(matches.group(3))
                )
        
        # Handle hex format like #RRGGBB or #RGB
        elif color.startswith("#"):
            color = color.lstrip("#")
            if len(color) == 3:
                color = "".join([c*2 for c in color])
            if len(color) == 6:
                return (
                    int(color[0:2], 16),
                    int(color[2:4], 16),
                    int(color[4:6], 16)
                )
        
        # Try to use selenium's color parser as a fallback
        selenium_color = Color.from_string(color)
        return (
            selenium_color.red,
            selenium_color.green,
            selenium_color.blue
        )
    
    except Exception:
        return None

def calculate_contrast_ratio(rgb1, rgb2):
    """
    Calculate contrast ratio between two colors using WCAG formula.
    
    Returns:
        float: Contrast ratio (1 to 21)
    """
    # Calculate luminance for the first color
    l1 = calculate_luminance(rgb1)
    
    # Calculate luminance for the second color
    l2 = calculate_luminance(rgb2)
    
    # Calculate contrast ratio: (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter color
    lighter = max(l1, l2)
    darker = min(l1, l2)
    
    return (lighter + 0.05) / (darker + 0.05)

def calculate_luminance(rgb):
    """
    Calculate relative luminance of an RGB color using the formula from WCAG.
    
    Returns:
        float: Relative luminance (0 to 1)
    """
    # Normalize RGB values to 0-1 range
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    
    # Apply gamma correction (sRGB color space)
    r = gamma_correct(r)
    g = gamma_correct(g)
    b = gamma_correct(b)
    
    # Calculate luminance using WCAG formula
    l = 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    return l

def gamma_correct(value):
    """Apply gamma correction to a color channel value"""
    if value <= 0.03928:
        return value / 12.92
    else:
        return math.pow((value + 0.055) / 1.055, 2.4)

def truncate_text(text, max_length=50):
    """Truncate text to a maximum length if necessary"""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text