"""
Debug script to identify where the 'list' object has no attribute 'get' error is occurring
"""

import sys
import os
import logging
import traceback

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import necessary functions
from accessibility_modules.dynamic_content_tester import run_advanced_dynamic_content_test
from accessibility_modules.report_generator import integrate_dynamic_content_results
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def debug_accessibility_checker():
    """
    Debug function to trace exactly where the error is occurring
    """
    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG,  # Use DEBUG level for more detailed information
        format='%(asctime)s - %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    url = "http://example.com"  # Use a simple site for testing
    driver = None
    
    try:
        # Set up WebDriver
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        # Navigate to URL
        driver.get(url)
        
        # Initialize a simple report structure
        report = {
            "url": url,
            "checks": {}
        }
        
        # Debug step 1: Run dynamic content testing
        logging.debug("Starting dynamic content testing")
        dynamic_content_results = run_advanced_dynamic_content_test(driver)
        logging.debug(f"Dynamic content results type: {type(dynamic_content_results)}")
        
        # Print the structure to identify any issues
        for key, value in dynamic_content_results.items():
            logging.debug(f"Key: {key}, Value type: {type(value)}")
            
            # If it's a list, check its contents
            if isinstance(value, list):
                logging.debug(f"  List length: {len(value)}")
                for i, item in enumerate(value[:2]):  # Show first 2 items
                    logging.debug(f"  Item {i} type: {type(item)}")
                    if isinstance(item, dict):
                        logging.debug(f"    Keys: {item.keys()}")
        
        # Debug step 2: Try integrating results
        logging.debug("Attempting to integrate dynamic content results")
        report = integrate_dynamic_content_results(report, dynamic_content_results)
        logging.debug("Integration successful")
        
        logging.debug("All debug steps completed successfully")
        
    except Exception as e:
        logging.error(f"Error in debug: {str(e)}")
        logging.error(traceback.format_exc())
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    debug_accessibility_checker()