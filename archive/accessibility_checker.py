#!/usr/bin/env python
# coding: utf-8

import sys
import os
from pathlib import Path
import json
import time
from datetime import datetime

# Add the project directory to the path so we can import our modules
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import URL from config
from config import url_to_check, browser_choice

# Set path for the accessibility reports
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Import our custom modules
from data_loader import load_data, count_issues_by_category
from enhanced_report_generator import (
    generate_accessibility_report, 
    create_visualization,
    get_test_instructions,
    get_fix_example
)
from non_text_content_checker import identify_non_text_content

# Selenium and related modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setup_webdriver(browser='chrome'):
    """Set up the WebDriver based on the selected browser."""
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver

def check_tab_order(driver, url):
    """Check the tab order of the webpage."""
    driver.get(url)
    
    # Find all focusable elements
    focusable_elements = driver.find_elements(By.CSS_SELECTOR, "a[href], button, input, select, textarea, [tabindex]")
    
    # Store the tab order issues
    tab_order_issues = []
    
    # Simulate pressing the Tab key and check the focus order
    for i in range(len(focusable_elements)):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(focusable_elements[i]))
            focusable_elements[i].send_keys(Keys.TAB)
            next_focused_element = driver.switch_to.active_element
            if next_focused_element != focusable_elements[(i + 1) % len(focusable_elements)]:
                tab_order_issues.append(f"Unexpected focus order: {focusable_elements[i].tag_name} -> {next_focused_element.tag_name}")
        except TimeoutException:
            tab_order_issues.append(f"Element not focusable: {focusable_elements[i].tag_name}")
    
    return tab_order_issues

def check_missing_focusable(driver, url):
    """Check for missing focusable elements."""
    driver.get(url)
    
    # Find all interactive elements
    interactive_elements = driver.find_elements(By.XPATH, "//a | //button | //input | //select | //textarea")
    
    # Store the missing focusable issues
    missing_focusable_issues = []
    
    # Check if each interactive element is focusable
    for element in interactive_elements:
        if not element.is_enabled() or not element.is_displayed():
            missing_focusable_issues.append(f"Element not focusable: {element.tag_name}")
    
    return missing_focusable_issues

def check_aria(driver, url):
    """Check for ARIA-related issues."""
    driver.get(url)
    
    # Find elements with ARIA attributes
    aria_elements = driver.find_elements(By.XPATH, "//*[@aria-label or @aria-describedby or @aria-labelledby or @role]")
    
    # Store the ARIA issues
    aria_issues = []
    
    # Check each element with ARIA attributes
    for element in aria_elements:
        if not element.is_displayed():
            aria_issues.append(f"ARIA element not visible: {element.tag_name}")
        if not element.is_enabled():
            aria_issues.append(f"ARIA element not enabled: {element.tag_name}")
        if element.get_attribute("tabindex") == "-1":
            aria_issues.append(f"ARIA element not focusable: {element.tag_name}")
    
    return aria_issues

def check_keyboard_accessibility(driver, url):
    """Check for keyboard accessibility issues."""
    driver.get(url)
    
    # Find all focusable elements
    focusable_elements = driver.find_elements(By.CSS_SELECTOR, "a[href], button, input, select, textarea, [tabindex]")
    
    # Store the keyboard accessibility issues
    keyboard_issues = []
    
    # Check each focusable element
    for element in focusable_elements:
        try:
            element.send_keys(Keys.ENTER)
            if "active" not in element.get_attribute("class"):
                keyboard_issues.append(f"Element not activated by Enter key: {element.tag_name}")
            element.send_keys(Keys.SPACE)
            if "active" not in element.get_attribute("class"):
                keyboard_issues.append(f"Element not activated by Space key: {element.tag_name}")
        except:
            keyboard_issues.append(f"Error interacting with element: {element.tag_name}")
    
    return keyboard_issues

def run_accessibility_checks(url):
    """Run comprehensive accessibility checks on the given URL."""
    driver = setup_webdriver(browser_choice)  # Use the selected browser from config
    
    print("Running accessibility checks...")
    
    # Check tab order
    tab_order_issues = check_tab_order(driver, url)
    print(f"Tab order issues: {len(tab_order_issues)}")
    
    # Check missing focusable elements
    missing_focusable_issues = check_missing_focusable(driver, url)
    print(f"Missing focusable elements: {len(missing_focusable_issues)}")
    
    # Check ARIA-related issues
    aria_issues = check_aria(driver, url)
    print(f"ARIA-related issues: {len(aria_issues)}")
    
    # Check keyboard accessibility
    keyboard_issues = check_keyboard_accessibility(driver, url)
    print(f"Keyboard accessibility issues: {len(keyboard_issues)}")
    
    # Check for non-text content elements
    page_source = driver.page_source
    non_text_elements = identify_non_text_content(page_source)
    print(f"Found {len(non_text_elements)} non-text content elements.")
    
    driver.quit()
    
    # Generate the accessibility report
    report_data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tab_order_issues": tab_order_issues,
        "missing_focusable_issues": missing_focusable_issues,
        "aria_issues": aria_issues,
        "keyboard_issues": keyboard_issues,
        "non_text_content_elements": non_text_elements
    }
    
    # Generate report and visualization
    report_path = generate_accessibility_report(report_data)
    visualization_path = create_visualization(report_data)
    
    # Print paths for reference
    print(f"Report saved to: {report_path}")
    print(f"Visualization saved to: {visualization_path}")
    
    return report_data

# If run directly, execute accessibility checks
if __name__ == "__main__":
    run_accessibility_checks(url_to_check)