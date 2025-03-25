"""
Dynamic Content Accessibility Tester
Coordinates specialized test modules for comprehensive testing of interactive web components.
"""
import logging
import time
import json
import traceback
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# Import specialized test modules
try:
    from accessibility_modules.component_tests.slider_tester import test_sliders
except ImportError:
    def test_sliders(driver, state_tracker, timeout=15):
        logging.warning("Slider tester module not found, using placeholder")
        return []

try:
    from accessibility_modules.component_tests.carousel_tester import test_carousels
except ImportError:
    def test_carousels(driver, state_tracker, timeout=15):
        logging.warning("Carousel tester module not found, using placeholder")
        return []

try:
    from accessibility_modules.component_tests.modal_tester import test_modals
except ImportError:
    def test_modals(driver, state_tracker, timeout=15):
        logging.warning("Modal tester module not found, using placeholder")
        return []

try:
    from accessibility_modules.component_tests.accordion_tester import test_accordions
except ImportError:
    def test_accordions(driver, state_tracker, timeout=15):
        logging.warning("Accordion tester module not found, using placeholder")
        return []

try:
    from accessibility_modules.component_tests.dropdown_tester import test_dropdowns
except ImportError:
    def test_dropdowns(driver, state_tracker, timeout=15):
        logging.warning("Dropdown tester module not found, using placeholder")
        return []

try:
    from accessibility_modules.component_tests.tab_tester import test_tabs
except ImportError:
    def test_tabs(driver, state_tracker, timeout=15):
        logging.warning("Tab tester module not found, using placeholder")
        return []

class DynamicContentStateTracker:
    """Basic state tracker for dynamic components"""
    
    def __init__(self):
        self.component_states = {}
        self.interaction_log = []
    
    def record_state(self, component_type, component_id, state):
        """Record the state of a component"""
        if component_type not in self.component_states:
            self.component_states[component_type] = {}
        
        if component_id not in self.component_states[component_type]:
            self.component_states[component_type][component_id] = []
        
        self.component_states[component_type][component_id].append({
            'timestamp': time.time(),
            'state': state
        })
    
    def log_interaction(self, component_type, component_id, interaction_type, details=None):
        """Log an interaction with a component"""
        self.interaction_log.append({
            'timestamp': time.time(),
            'component_type': component_type,
            'component_id': component_id,
            'interaction_type': interaction_type,
            'details': details or {}
        })
    
    def export_states(self):
        """Export state data as JSON"""
        export_data = {
            'component_states': self.component_states,
            'interaction_log': self.interaction_log
        }
        return export_data

def run_advanced_dynamic_content_test(driver, timeout=15):
    """
    Convenience function to run dynamic content accessibility tests.
    This is the function imported by accessibility_checker.py.
    
    Args:
        driver: Selenium WebDriver instance
        timeout: Maximum time to spend testing each component type
    
    Returns:
        Dict of test results for different component types
    """
    try:
        # Create state tracker that can be shared with test modules
        state_tracker = DynamicContentStateTracker()
        
        # Call the specialized test modules - make sure they all return lists
        slider_results = test_sliders(driver, state_tracker, timeout)
        carousel_results = test_carousels(driver, state_tracker, timeout)
        modal_results = test_modals(driver, state_tracker, timeout)
        accordion_results = test_accordions(driver, state_tracker, timeout)
        dropdown_results = test_dropdowns(driver, state_tracker, timeout)
        tab_results = test_tabs(driver, state_tracker, timeout)
        
        # Ensure all results are in list format
        def ensure_list(result):
            if isinstance(result, dict):
                # If it's a dict with an 'issues' key, extract the issues
                if 'issues' in result:
                    return result['issues']
                # Otherwise, convert to a list with the dict as the only item
                return [result]
            elif isinstance(result, list):
                return result
            else:
                return []
        
        # Make sure our results are all lists
        results = {
            "sliders": ensure_list(slider_results),
            "carousels": ensure_list(carousel_results),
            "modals": ensure_list(modal_results),
            "accordions": ensure_list(accordion_results),
            "dropdowns": ensure_list(dropdown_results),
            "tabs": ensure_list(tab_results),
            "state_tracking": state_tracker.export_states()  # This is a dictionary
        }
        
        return results
        
    except Exception as e:
        logging.error(f"Error in dynamic content testing: {str(e)}")
        return {
            "error": str(e),
            "details": "Failed to complete dynamic content testing",
            "traceback": traceback.format_exc()
        }

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)