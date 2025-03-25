"""
Enhanced Image Accessibility Checker Module
Checks for proper image accessibility with improved auditor-focused information.
"""

import logging
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from urllib.parse import urlparse
import base64
import hashlib

def check_image_accessibility(driver):
    """
    Comprehensive check for image accessibility with enhanced element identification.
    Addresses WCAG Success Criterion 1.1.1: Non-text Content
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of image accessibility checks with detailed element info
    """
    logging.info("Checking image accessibility (WCAG 1.1.1: Non-text Content)...")
    results = {
        "status": "completed",
        "wcag_criterion": "1.1.1",
        "image_count": 0,
        "svg_count": 0,
        "canvas_count": 0,
        "other_nontext_count": 0,
        "issues": []
    }
    
    try:
        # Check standard images
        check_standard_images(driver, results)
        
        # Check SVG elements
        check_svg_elements(driver, results)
        
        # Check icon fonts
        check_icon_fonts(driver, results)
        
        # Group similar issues for better reporting
        results["grouped_issues"] = group_similar_issues(results["issues"])
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking image accessibility: {str(e)}")
        results["error"] = str(e)
        return results

def check_standard_images(driver, results):
    """Check standard <img> elements for proper alt text with enhanced element info"""
    images = driver.find_elements(By.TAG_NAME, "img")
    results["image_count"] = len(images)
    
    for index, image in enumerate(images):
        # Skip very small images that are likely decorative
        if is_likely_decorative_by_size(image):
            continue
            
        # Collect comprehensive element information
        element_info = collect_element_info(driver, image, index)
            
        # Check for alt attribute
        alt_text = image.get_attribute("alt")
        src = element_info["src"]
        role = image.get_attribute("role") or ""
        aria_hidden = image.get_attribute("aria-hidden") == "true"
        
        # Check for missing alt attribute
        if alt_text is None:
            results["issues"].append({
                "element": "img",
                "element_info": element_info,
                "issue": "Missing text alternative",
                "details": "Image has no alt attribute, which is required for accessibility",
                "recommendation": "Add appropriate alt text or empty alt (alt='') for decorative images",
                "wcag": "1.1.1",
                "severity": "critical"
            })
        # Check for empty alt text - might be appropriate for decorative images
        elif alt_text.strip() == "":
            # If it has empty alt text but doesn't appear decorative
            if not is_likely_decorative(image) and not is_likely_decorative_by_size(image) and not aria_hidden and role != "presentation":
                results["issues"].append({
                    "element": "img",
                    "element_info": element_info,
                    "issue": "Potentially informative image has empty alt text",
                    "details": "Image appears to convey information but has empty alt text",
                    "recommendation": "Add descriptive alt text if the image conveys information",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })
        # Has alt text, but check quality
        else:
            # Check for inadequate alt text
            if is_inadequate_alt_text(alt_text, image):
                results["issues"].append({
                    "element": "img",
                    "element_info": element_info,
                    "issue": "Potentially inadequate text alternative",
                    "details": f"Alt text '{alt_text}' may not adequately describe the image",
                    "recommendation": "Ensure alt text conveys the purpose and content of the image",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })
            
            # Check for redundant alt text
            if is_redundant_alt_text(alt_text, image):
                results["issues"].append({
                    "element": "img",
                    "element_info": element_info,
                    "issue": "Redundant text alternative",
                    "details": "Alt text appears to duplicate adjacent text content",
                    "recommendation": "Consider using empty alt text (alt='') if the image is adequately described by nearby text",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def check_svg_elements(driver, results):
    """Check SVG elements for proper accessibility with enhanced element info"""
    svg_elements = driver.find_elements(By.TAG_NAME, "svg")
    results["svg_count"] = len(svg_elements)
    
    for index, svg in enumerate(svg_elements):
        # Get comprehensive element information
        element_info = collect_element_info(driver, svg, index, element_type="svg")
        
        # Get attributes for accessibility checks
        role = svg.get_attribute("role") or ""
        aria_label = svg.get_attribute("aria-label") or ""
        aria_labelledby = svg.get_attribute("aria-labelledby") or ""
        aria_hidden = svg.get_attribute("aria-hidden") == "true"
        
        # Skip if explicitly marked as hidden/decorative
        if aria_hidden or role == "presentation" or role == "none":
            continue
        
        # Check if SVG has accessible name
        has_title = len(svg.find_elements(By.TAG_NAME, "title")) > 0
        has_desc = len(svg.find_elements(By.TAG_NAME, "desc")) > 0
        
        if not (has_title or aria_label or aria_labelledby):
            results["issues"].append({
                "element": "svg",
                "element_info": element_info,
                "issue": "SVG lacks text alternative",
                "details": "SVG element has no accessible name or description",
                "recommendation": "Add a <title> element, aria-label, or aria-labelledby attribute to describe the SVG",
                "wcag": "1.1.1",
                "severity": "critical" if is_likely_informative(svg) else "warning"
            })

def check_icon_fonts(driver, results):
    """Check icon fonts for proper accessibility with enhanced element info"""
    # Common icon font classes
    icon_selectors = [
        "[class*='icon']", 
        "[class*='fa-']",      # Font Awesome
        "[class*='glyphicon']", # Bootstrap
        "[class*='material-icons']", # Material Design
        "i[class]"             # Common tag for icons
    ]
    
    for selector in icon_selectors:
        icons = driver.find_elements(By.CSS_SELECTOR, selector)
        
        for index, icon in enumerate(icons):
            # Get comprehensive element information
            element_info = collect_element_info(driver, icon, index, element_type="icon")
            
            # Skip if already marked as hidden
            aria_hidden = icon.get_attribute("aria-hidden") == "true"
            if aria_hidden:
                continue
                
            # Check if icon has text or accessible name
            icon_text = icon.text.strip() if hasattr(icon, 'text') else ""
            aria_label = icon.get_attribute("aria-label") or ""
            aria_labelledby = icon.get_attribute("aria-labelledby")
            
            # Check if it's inside a button or link that has text
            parent_element = None
            try:
                parent_element = icon.find_element(By.XPATH, "./..")
                element_info["parent_tag"] = parent_element.tag_name
                element_info["parent_text"] = parent_element.text.strip() if hasattr(parent_element, 'text') else ""
                element_info["parent_role"] = parent_element.get_attribute("role") or ""
            except:
                pass
                
            parent_has_text = False
            if parent_element:
                parent_tag = parent_element.tag_name
                parent_text = parent_element.text.strip() if hasattr(parent_element, 'text') else ""
                parent_has_text = parent_text != "" and parent_text != icon_text
                
                # If parent is a button/link and has its own text or aria-label
                if (parent_tag in ["button", "a"] or parent_element.get_attribute("role") in ["button", "link"]) and (
                    parent_has_text or 
                    parent_element.get_attribute("aria-label") or 
                    parent_element.get_attribute("aria-labelledby")
                ):
                    # In this case, icon should be hidden
                    if not aria_hidden:
                        results["issues"].append({
                            "element": icon.tag_name,
                            "element_info": element_info,
                            "issue": "Decorative icon not hidden from screen readers",
                            "details": "Icon inside a labeled element should be hidden from screen readers",
                            "recommendation": "Add aria-hidden='true' to the icon element",
                            "wcag": "1.1.1",
                            "severity": "warning"
                        })
                    continue
            
            # If icon is standalone and has no accessible name
            if not (icon_text or aria_label or aria_labelledby) and not parent_has_text:
                results["issues"].append({
                    "element": icon.tag_name,
                    "element_info": element_info,
                    "issue": "Icon lacks text alternative",
                    "details": "Icon has no accessible name and is not hidden from screen readers",
                    "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def collect_element_info(driver, element, index, element_type="img"):
    """
    Collect comprehensive information about an element for auditor use.
    
    Args:
        driver: Selenium WebDriver instance
        element: The web element to analyze
        index: Element index for tracking
        element_type: Type of element being analyzed
        
    Returns:
        dict: Detailed information about the element
    """
    # Basic element info
    element_id = element.get_attribute("id") or ""
    element_class = element.get_attribute("class") or ""
    element_tag = element.tag_name
    
    # Create a unique identifier for the element
    unique_id = f"{element_type}-{index}"
    if element_id:
        unique_id = f"{element_id}"
    elif element_class:
        # Create a hash of the element class and position as a unique identifier
        hash_input = f"{element_class}-{index}"
        unique_id = hashlib.md5(hash_input.encode()).hexdigest()[:8]
    
    # Get element source (for images)
    src = ""
    if element_type == "img":
        src = element.get_attribute("src") or ""
        # Handle data URLs by creating a truncated version
        if src.startswith("data:"):
            src = "[data URL]"
        # Extract filename for normal URLs
        else:
            filename_match = re.search(r'/([^/]+\.(jpg|jpeg|png|gif|webp|svg))(\?|$)', src, re.IGNORECASE)
            if filename_match:
                src = filename_match.group(1)
    
    # Get position information
    position = {"x": 0, "y": 0, "width": 0, "height": 0}
    try:
        rect = element.rect
        position = {
            "x": rect.get('x', 0),
            "y": rect.get('y', 0),
            "width": rect.get('width', 0),
            "height": rect.get('height', 0)
        }
    except:
        pass
    
    # Get DOM path
    try:
        dom_path = driver.execute_script("""
            function getPathTo(element) {
                if (element.id !== '')
                    return 'id("' + element.id + '")';
                if (element === document.body)
                    return element.tagName.toLowerCase();

                var ix = 0;
                var siblings = element.parentNode.childNodes;
                for (var i = 0; i < siblings.length; i++) {
                    var sibling = siblings[i];
                    if (sibling === element)
                        return getPathTo(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix + 1) + ']';
                    if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                        ix++;
                }
            }
            return getPathTo(arguments[0]);
        """, element)
    except:
        dom_path = "Unknown path"
    
    # Get element visibility
    is_visible = element.is_displayed() if hasattr(element, 'is_displayed') else False
    
    # Collect all attributes
    attributes = {}
    try:
        attributes_dict = driver.execute_script("""
            var items = {};
            for (var i = 0; i < arguments[0].attributes.length; i++) {
                var attr = arguments[0].attributes[i];
                items[attr.name] = attr.value;
            }
            return items;
        """, element)
        attributes = attributes_dict or {}
    except:
        pass
    
    # Get simplified CSS selector
    try:
        css_selector = driver.execute_script("""
            function getSelector(el) {
                if (el.id) return '#' + el.id;
                if (el.className) {
                    var classes = el.className.split(/\\s+/);
                    if (classes.length > 0 && classes[0]) {
                        return el.tagName.toLowerCase() + '.' + classes[0];
                    }
                }
                var parent = el.parentNode;
                if (!parent || parent === document.body) return el.tagName.toLowerCase();
                var siblings = parent.children;
                var count = 0;
                for (var i = 0; i < siblings.length; i++) {
                    var sibling = siblings[i];
                    if (sibling === el) {
                        return getSelector(parent) + ' > ' + el.tagName.toLowerCase() + ':nth-child(' + (count + 1) + ')';
                    }
                    if (sibling.nodeType === 1 && sibling.tagName === el.tagName) {
                        count++;
                    }
                }
                return getSelector(parent) + ' > ' + el.tagName.toLowerCase();
            }
            return getSelector(arguments[0]);
        """, element)
    except:
        css_selector = f"{element_tag}.{element_class.split()[0]}" if element_class else element_tag
    
    # Create the enhanced element info
    element_info = {
        "unique_id": unique_id,
        "tag": element_tag,
        "id": element_id,
        "class": element_class,
        "src": src,
        "position": position,
        "dom_path": dom_path,
        "css_selector": css_selector,
        "visible": is_visible,
        "attributes": attributes
    }
    
    return element_info

def group_similar_issues(issues):
    """
    Group similar issues for better reporting.
    
    Args:
        issues: List of issues to group
        
    Returns:
        dict: Grouped issues by issue type
    """
    grouped = {}
    
    for issue in issues:
        issue_key = issue["issue"]
        if issue_key not in grouped:
            grouped[issue_key] = {
                "count": 0,
                "instances": [],
                "severity": issue["severity"],
                "recommendation": issue["recommendation"],
                "wcag": issue["wcag"]
            }
        
        grouped[issue_key]["count"] += 1
        grouped[issue_key]["instances"].append({
            "element_info": issue["element_info"],
            "details": issue["details"]
        })
    
    return grouped

# Helper functions (keep existing helper functions)

def is_likely_decorative_by_size(image):
    """Check if image is likely decorative based on size"""
    try:
        width = image.size['width']
        height = image.size['height']
        
        # Very small images are likely icons or decorative elements
        if (width < 20 and height < 20) or (width == 1 and height == 1):
            return True
            
        return False
    except:
        return False

def is_likely_decorative(image):
    """
    Check if image is likely decorative based on various attributes
    """
    # Check for role="presentation" or role="none"
    role = image.get_attribute("role") or ""
    if role.lower() in ["presentation", "none"]:
        return True
        
    # Check for classes that suggest decorative images
    class_attr = image.get_attribute("class") or ""
    decorative_classes = ["icon", "decoration", "bg", "background", "separator", "divider"]
    if any(cls in class_attr.lower() for cls in decorative_classes):
        return True
        
    # Check for file names that suggest icons
    src = image.get_attribute("src") or ""
    if re.search(r'icon|logo|bg|background|separator|divider', src.lower()):
        return True
        
    return False

def is_likely_informative(element):
    """Check if an element is likely to convey important information"""
    # Check for classes or IDs that suggest important content
    class_attr = element.get_attribute("class") or ""
    id_attr = element.get_attribute("id") or ""
    
    informative_patterns = ["chart", "graph", "map", "diagram", "infographic", "banner", "hero", "content"]
    
    if any(pattern in class_attr.lower() or pattern in id_attr.lower() for pattern in informative_patterns):
        return True
        
    # Large elements are more likely to be informative
    try:
        width = element.size['width']
        height = element.size['height']
        if width > 200 and height > 200:
            return True
    except:
        pass
        
    return False

def is_inadequate_alt_text(alt_text, image):
    """Check for common patterns of inadequate alt text"""
    alt_lower = alt_text.lower()
    
    # Very short alt text is suspicious for meaningful images
    if len(alt_text) < 5 and not is_likely_decorative(image):
        return True
        
    # Generic or unhelpful alt text
    generic_patterns = [
        'image', 'picture', 'photo', 'pic', 'graphic', 'icon', 'img', 
        '.jpg', '.png', '.gif', '.jpeg'
    ]
    
    if any(pattern in alt_lower for pattern in generic_patterns):
        return True
        
    # File name used as alt text (a common mistake)
    src = image.get_attribute("src") or ""
    if src:
        # Extract filename from URL
        filename_match = re.search(r'/([^/]+\.(jpg|jpeg|png|gif|webp|svg))(\?|$)', src, re.IGNORECASE)
        if filename_match and filename_match.group(1).lower() in alt_lower:
            return True
    
    return False

def is_redundant_alt_text(alt_text, image):
    """Check if alt text duplicates adjacent text content"""
    try:
        # Try to find parent element with text
        parent = image.find_element(By.XPATH, "./..")
        parent_text = parent.text.strip()
        
        # If parent has no other children but has text, it might be duplicating the alt
        if parent_text and alt_text in parent_text:
            other_children = parent.find_elements(By.XPATH, "./*[not(self::img)]")
            if not other_children:
                return True
                
        # Check for nearby headings that match the alt text
        nearby_headings = parent.find_elements(By.XPATH, "../h1|../h2|../h3|../h4|../h5|../h6")
        for heading in nearby_headings:
            heading_text = heading.text.strip()
            if heading_text and alt_text == heading_text:
                return True
                
        return False
    except:
        return False