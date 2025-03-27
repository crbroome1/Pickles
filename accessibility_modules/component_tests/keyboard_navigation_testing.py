from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from typing import List, Dict, Any

from modal_accessibility_core import AccessibilityTestModule


class KeyboardNavigationTester(AccessibilityTestModule):
    """Module for testing keyboard accessibility of modals."""
    
    def __init__(self):
        """Initialize the keyboard navigation tester."""
        super().__init__(
            name="keyboard_navigation",
            description="Tests keyboard accessibility features of modals"
        )
    
    def test(self, modal_element) -> Dict[str, Any]:
        """
        Test keyboard navigation for a modal.
        
        Args:
            modal_element: WebElement representing the modal
            
        Returns:
            Dictionary with test results
        """
        issues = []
        warnings = []
        passed = True
        
        # Check if the modal is focusable or contains focusable elements
        focusable_elements = self.get_focusable_elements(modal_element)
        if not focusable_elements:
            issues.append(self.create_issue(
                modal_element,
                "Modal does not contain any focusable elements, making keyboard navigation impossible.",
                "error",
                "keyboard-nav-1"
            ))
            passed = False
        
        # Check for keyboard-accessible close mechanism (Escape key or visible close button)
        has_close_button = self.has_accessible_close_button(modal_element)
        if not has_close_button:
            issues.append(self.create_issue(
                modal_element,
                "Modal does not have a visible, keyboard-accessible close button.",
                "error",
                "keyboard-nav-2"
            ))
            passed = False
        
        # Check for focus trap (focus should be constrained within the modal)
        has_focus_trap = self.test_focus_trap(modal_element)
        if not has_focus_trap:
            warnings.append(self.create_warning(
                modal_element,
                "Modal may not properly trap keyboard focus within it.",
                "keyboard-nav-3"
            ))
        
        # Check tab order within the modal
        has_logical_tab_order = self.test_tab_order(modal_element, focusable_elements)
        if not has_logical_tab_order:
            warnings.append(self.create_warning(
                modal_element,
                "Tab order within the modal may not follow a logical sequence.",
                "keyboard-nav-4"
            ))
        
        return {
            "passed": passed,
            "issues": issues,
            "warnings": warnings
        }
    
    def get_focusable_elements(self, container) -> List:
        """
        Get all focusable elements within a container.
        
        Args:
            container: WebElement to search within
            
        Returns:
            List of focusable WebElements
        """
        # Common selectors for focusable elements
        focusable_selectors = [
            'a[href]',
            'button:not([disabled])',
            'input:not([disabled]):not([type="hidden"])',
            'select:not([disabled])',
            'textarea:not([disabled])',
            '[tabindex]:not([tabindex="-1"])',
            'area[href]',
            'iframe',
            'object',
            'embed',
            '[contenteditable]'
        ]
        
        # Combine all selectors
        combined_selector = ', '.join(focusable_selectors)
        
        try:
            return container.find_elements(By.CSS_SELECTOR, combined_selector)
        except WebDriverException as e:
            print(f"Error finding focusable elements: {e}")
            return []
    
    def has_accessible_close_button(self, modal_element) -> bool:
        """
        Check if a modal has an accessible close button.
        
        Args:
            modal_element: WebElement representing the modal
            
        Returns:
            True if an accessible close button is found, False otherwise
        """
        # Look for common close button patterns
        close_buttons = []
        
        # Common selectors for close buttons
        selectors = [
            # Common class names
            '.close, .close-button, .btn-close',
            
            # ARIA labels
            '[aria-label*="close" i], [aria-label*="dismiss" i]'
        ]
        
        # Find elements matching the selectors
        for selector in selectors:
            try:
                elements = modal_element.find_elements(By.CSS_SELECTOR, selector)
                close_buttons.extend(elements)
            except WebDriverException:
                continue
        
        # Find buttons with text containing 'close', 'cancel', or 'dismiss'
        try:
            buttons = modal_element.find_elements(By.TAG_NAME, 'button')
            for button in buttons:
                try:
                    text = button.text.lower()
                    if 'close' in text or 'cancel' in text or 'dismiss' in text:
                        close_buttons.append(button)
                except WebDriverException:
                    continue
        except WebDriverException:
            pass
        
        # Find elements with X symbols that might be close buttons
        try:
            elements = modal_element.find_elements(By.CSS_SELECTOR, 'button, [role="button"]')
            for element in elements:
                try:
                    if '×' in element.text or '✕' in element.text or '✖' in element.text:
                        close_buttons.append(element)
                except WebDriverException:
                    continue
        except WebDriverException:
            pass
        
        # Check if any of the close buttons are keyboard accessible
        for button in close_buttons:
            try:
                # Is the button displayed?
                if not button.is_displayed():
                    continue
                
                # Is the button focusable?
                tag_name = button.tag_name.lower()
                tab_index = button.get_attribute('tabindex')
                
                is_focusable = (
                    tag_name == 'button' or 
                    tag_name == 'a' or
                    (tab_index is not None and tab_index != '-1')
                )
                
                if is_focusable:
                    return True
            except WebDriverException:
                continue
        
        # Check for escape key handling - this is a simplified check
        # A full check would require actually pressing Escape and checking if the modal closes
        try:
            # Check for event listeners (simplified approach - limited browser support)
            driver = modal_element.parent
            has_keydown_listener = driver.execute_script("""
                return (arguments[0].onkeydown !== null || 
                        arguments[0].onkeypress !== null ||
                        document.onkeydown !== null ||
                        document.onkeypress !== null);
            """, modal_element)
            
            if has_keydown_listener:
                return True
        except WebDriverException:
            pass
        
        return False
    
    def test_focus_trap(self, modal_element) -> bool:
        """
        Test if focus is properly trapped within the modal.
        
        Args:
            modal_element: WebElement representing the modal
            
        Returns:
            True if focus appears to be trapped, False otherwise
        """
        # This is a simplified check - a comprehensive check would require
        # actually simulating tab navigation through the modal
        
        try:
            # Check for common focus trap implementations
            
            # 1. Check for aria-modal attribute
            aria_modal = modal_element.get_attribute('aria-modal')
            if aria_modal == 'true':
                return True
            
            # 2. Check for dialog role with modal behavior
            role = modal_element.get_attribute('role')
            if role in ['dialog', 'alertdialog']:
                # Dialog role often implies focus trapping
                return True
            
            # 3. Check for inert attribute on elements outside the modal
            driver = modal_element.parent
            inert_elements = driver.find_elements(By.CSS_SELECTOR, '[inert]')
            if inert_elements:
                return True
            
            # 4. Check for common focus trap class names
            class_name = modal_element.get_attribute('class') or ''
            if 'focus-trap' in class_name or 'focus-trap-active' in class_name:
                return True
            
            # 5. Check for tabindex="-1" on elements outside the modal
            # This is a common technique to prevent tabbing outside
            try:
                # Check if document body or other container has tabindex="-1"
                body = driver.find_element(By.TAG_NAME, 'body')
                if body.get_attribute('tabindex') == '-1':
                    return True
            except WebDriverException:
                pass
                
            return False
        except WebDriverException as e:
            print(f"Error testing focus trap: {e}")
            return False
    
    def test_tab_order(self, modal_element, focusable_elements) -> bool:
        """
        Test if tab order is logical within the modal.
        
        Args:
            modal_element: WebElement representing the modal
            focusable_elements: List of focusable elements within the modal
            
        Returns:
            True if tab order appears logical, False otherwise
        """
        if not focusable_elements:
            return False
            
        try:
            # Compare visual positions to detect reading order issues
            previous_top = -1
            previous_left = -1
            reading_order_violations = 0
            
            for element in focusable_elements:
                try:
                    # Get element position
                    rect = element.rect
                    
                    # Check if the element is visually below previous elements (main reading direction)
                    if rect['y'] < previous_top and rect['x'] <= previous_left:
                        reading_order_violations += 1
                        
                    previous_top = rect['y']
                    previous_left = rect['x']
                except WebDriverException:
                    continue
            
            # Allow a small number of violations (some designs have valid exceptions)
            max_allowed_violations = max(1, len(focusable_elements) // 10)
            return reading_order_violations <= max_allowed_violations
            
        except WebDriverException as e:
            print(f"Error testing tab order: {e}")
            return False