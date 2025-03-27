from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union

class ModalAccessibilityChecker:
    """Core framework for testing modal accessibility."""
    
    def __init__(self, driver=None):
        """
        Initialize the accessibility checker.
        
        Args:
            driver: An optional Selenium WebDriver instance. If not provided,
                   a new Chrome driver will be created.
        """
        self.driver = driver or self._create_default_driver()
        self.modules = {}
        self.results = {}
        self.modal_elements = []
        
    @staticmethod
    def _create_default_driver():
        """Create a default Chrome WebDriver instance."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode by default
        return webdriver.Chrome(options=options)
    
    def register_module(self, name: str, module_instance):
        """
        Register a testing module with the checker.
        
        Args:
            name: Name of the module
            module_instance: Instance of an AccessibilityTestModule
        
        Returns:
            self for method chaining
        """
        if name in self.modules:
            print(f"Warning: Module '{name}' is already registered. It will be overwritten.")
        
        self.modules[name] = module_instance
        self.results[name] = {"passed": False, "issues": [], "warnings": []}
        return self
    
    def detect_modals(self) -> List:
        """
        Find all modals on the current page.
        
        Returns:
            List of WebElement objects representing modals
        """
        # Basic detection logic - can be enhanced by specialized detector module
        possible_modals = []
        
        # Common modal selectors
        selectors = [
            'dialog',  # HTML5 dialog element
            '[role="dialog"]',  # ARIA dialog role
            '[role="alertdialog"]',  # ARIA alertdialog role
            '.modal',  # Common class names
            '.dialog',
            '.popup',
            '.overlay'
        ]
        
        # Collect all elements matching selectors
        for selector in selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                possible_modals.extend(elements)
            except WebDriverException as e:
                print(f"Error finding elements with selector '{selector}': {e}")
        
        # Filter to only visible modals or those with visible children
        visible_modals = []
        for modal in possible_modals:
            try:
                if modal.is_displayed() or self._has_visible_children(modal):
                    visible_modals.append(modal)
            except WebDriverException:
                # Skip elements that cause errors when checking visibility
                continue
        
        self.modal_elements = visible_modals
        return self.modal_elements
    
    def _has_visible_children(self, element) -> bool:
        """Check if an element has any visible children."""
        try:
            children = element.find_elements(By.CSS_SELECTOR, '*')
            return any(child.is_displayed() for child in children)
        except WebDriverException:
            return False
    
    def run_all_tests(self) -> Dict[str, Any]:
        """
        Run all registered modules on detected modals.
        
        Returns:
            Dictionary containing test results and summary
        """
        if not self.modal_elements:
            self.detect_modals()
            
        if not self.modal_elements:
            return {"error": "No modals detected on the page."}
        
        # Reset results
        for module_name in self.modules:
            self.results[module_name] = {"passed": True, "issues": [], "warnings": []}
        
        # Run each module on each modal
        for modal in self.modal_elements:
            for module_name, module_instance in self.modules.items():
                try:
                    module_results = module_instance.test(modal)
                    self.results[module_name]["issues"].extend(module_results.get("issues", []))
                    self.results[module_name]["warnings"].extend(module_results.get("warnings", []))
                    self.results[module_name]["passed"] = (
                        self.results[module_name]["passed"] and 
                        module_results.get("passed", False)
                    )
                except Exception as e:
                    print(f"Error running module '{module_name}': {e}")
                    self.results[module_name]["issues"].append({
                        "element_description": self._describe_element(modal),
                        "message": f"Module error: {str(e)}",
                        "severity": "error"
                    })
                    self.results[module_name]["passed"] = False
        
        return self.generate_report()
    
    def run_module(self, module_name: str) -> Dict[str, Any]:
        """
        Run a specific module on detected modals.
        
        Args:
            module_name: Name of the module to run
            
        Returns:
            Dictionary containing test results for the module
        """
        if module_name not in self.modules:
            return {"error": f"Module '{module_name}' not found."}
            
        if not self.modal_elements:
            self.detect_modals()
            
        module_instance = self.modules[module_name]
        self.results[module_name] = {"passed": True, "issues": [], "warnings": []}
        
        for modal in self.modal_elements:
            try:
                module_results = module_instance.test(modal)
                self.results[module_name]["issues"].extend(module_results.get("issues", []))
                self.results[module_name]["warnings"].extend(module_results.get("warnings", []))
                self.results[module_name]["passed"] = (
                    self.results[module_name]["passed"] and 
                    module_results.get("passed", False)
                )
            except Exception as e:
                print(f"Error running module '{module_name}': {e}")
                self.results[module_name]["issues"].append({
                    "element_description": self._describe_element(modal),
                    "message": f"Module error: {str(e)}",
                    "severity": "error"
                })
                self.results[module_name]["passed"] = False
                
        return self.results[module_name]
    
    def _describe_element(self, element) -> str:
        """Generate a human-readable description of a web element."""
        try:
            tag_name = element.tag_name
            element_id = element.get_attribute("id")
            element_class = element.get_attribute("class")
            element_role = element.get_attribute("role")
            
            description = f"<{tag_name}"
            if element_id:
                description += f" id='{element_id}'"
            if element_class:
                description += f" class='{element_class}'"
            if element_role:
                description += f" role='{element_role}'"
            description += ">"
            
            return description
        except WebDriverException:
            return "Unknown element"
    
    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive report of all test results.
        
        Returns:
            Dictionary with test summary and detailed results
        """
        summary = {
            "total_modals": len(self.modal_elements),
            "modules_passed": 0,
            "modules_failed": 0,
            "total_issues": 0,
            "total_warnings": 0,
            "results": self.results,
            "timestamp": datetime.now().isoformat()
        }
        
        for result in self.results.values():
            if result.get("passed", False):
                summary["modules_passed"] += 1
            else:
                summary["modules_failed"] += 1
            summary["total_issues"] += len(result.get("issues", []))
            summary["total_warnings"] += len(result.get("warnings", []))
        
        return summary
    
    def save_report(self, filename: str) -> str:
        """
        Save the current test results to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            Path to the saved file
        """
        report = self.generate_report()
        
        if not filename.endswith('.json'):
            filename += '.json'
            
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
            
        return os.path.abspath(filename)
    
    def close(self):
        """Close the WebDriver and release resources."""
        if self.driver:
            self.driver.quit()
            self.driver = None


class AccessibilityTestModule(ABC):
    """Base class for all accessibility test modules."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize the test module.
        
        Args:
            name: Module name
            description: Module description
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    def test(self, element) -> Dict[str, Any]:
        """
        Test an element for accessibility issues.
        
        Args:
            element: WebElement to test
            
        Returns:
            Dictionary with test results
        """
        pass
    
    def create_issue(self, element, message: str, severity: str = "error", code: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a standardized issue object.
        
        Args:
            element: WebElement with the issue
            message: Description of the issue
            severity: Issue severity (error, warning, info)
            code: Optional issue code for reference
            
        Returns:
            Dictionary representing the issue
        """
        return {
            "element_description": self._describe_element(element),
            "message": message,
            "severity": severity,
            "code": code,
            "timestamp": datetime.now().isoformat()
        }
    
    def create_warning(self, element, message: str, code: Optional[str] = None) -> Dict[str, Any]:
        """Convenience method to create a warning."""
        return self.create_issue(element, message, "warning", code)
    
    def _describe_element(self, element) -> str:
        """Generate a human-readable description of a web element."""
        try:
            tag_name = element.tag_name
            element_id = element.get_attribute("id")
            element_class = element.get_attribute("class")
            element_role = element.get_attribute("role")
            
            description = f"<{tag_name}"
            if element_id:
                description += f" id='{element_id}'"
            if element_class:
                description += f" class='{element_class}'"
            if element_role:
                description += f" role='{element_role}'"
            description += ">"
            
            return description
        except WebDriverException:
            return "Unknown element"