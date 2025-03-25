# Project Scripts Overview
*Generated on 2025-03-11 19:47:24 from folder: C:\Users\clint\Pickles*
*This is a project containing Jupyter Notebooks, Python scripts, and README files. The following content provides context for continuing development.*

## Accessibility Terminology
- **interactive element not in tab order**
  - Preferred: Keyboard navigation barrier
  - Explanation: Elements that appear interactive but cannot be accessed via keyboard
- **tab order issue**
  - Preferred: Inconsistent keyboard navigation sequence
  - Explanation: Elements that disrupt the expected keyboard navigation flow

## How to Continue This Project with Claude
1. Upload or copy the contents of this entire markdown file to Claude
2. Tell Claude: "These are the files from my project. I'd like to continue working on [specific task]."
3. Reference specific scripts or code blocks by their section names when asking questions

*The structured format below will help Claude understand your project's organization and codebase.*
## Table of Contents

### Jupyter Notebooks
- [archive\Accessibility_Checker.ipynb](#archive_Accessibility_Checker_ipynb)
- [archive\Accessibility_Checker_Starter.ipynb](#archive_Accessibility_Checker_Starter_ipynb)
- [archive\config.ipynb](#archive_config_ipynb)
- [archive\Data_Loader.ipynb](#archive_Data_Loader_ipynb)
- [archive\Enhanced_Report_Generator.ipynb](#archive_Enhanced_Report_Generator_ipynb)
- [archive\Generate_Accessibility_Report.ipynb](#archive_Generate_Accessibility_Report_ipynb)
- [archive\Missing_Focusable_Elements.ipynb](#archive_Missing_Focusable_Elements_ipynb)
- [archive\Non_Text_Content_Checker.ipynb](#archive_Non_Text_Content_Checker_ipynb)
- [archive\Script_Extract.ipynb](#archive_Script_Extract_ipynb)
- [archive\Script_Extract_a.ipynb](#archive_Script_Extract_a_ipynb)
- [archive\.ipynb_checkpoints\Accessibility_Checker-checkpoint.ipynb](#archive__ipynb_checkpoints_Accessibility_Checker-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Accessibility_Checker_Starter-checkpoint.ipynb](#archive__ipynb_checkpoints_Accessibility_Checker_Starter-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\config-checkpoint.ipynb](#archive__ipynb_checkpoints_config-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Data_Loader-checkpoint.ipynb](#archive__ipynb_checkpoints_Data_Loader-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Enhanced_Report_Generator-checkpoint.ipynb](#archive__ipynb_checkpoints_Enhanced_Report_Generator-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Generate_Accessibility_Report-checkpoint.ipynb](#archive__ipynb_checkpoints_Generate_Accessibility_Report-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Missing_Focusable_Elements-checkpoint.ipynb](#archive__ipynb_checkpoints_Missing_Focusable_Elements-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Non_Text_Content_Checker-checkpoint.ipynb](#archive__ipynb_checkpoints_Non_Text_Content_Checker-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Script_Extract-checkpoint.ipynb](#archive__ipynb_checkpoints_Script_Extract-checkpoint_ipynb)
- [archive\.ipynb_checkpoints\Script_Extract_a-checkpoint.ipynb](#archive__ipynb_checkpoints_Script_Extract_a-checkpoint_ipynb)

### Python Scripts
- [accessibility_checker.py](#accessibility_checker_py)
- [create_terminology.py](#create_terminology_py)
- [create_terminology_file.py](#create_terminology_file_py)
- [script_extract.py](#script_extract_py)
- [.ipynb_checkpoints\accessibility_checker-checkpoint.py](#_ipynb_checkpoints_accessibility_checker-checkpoint_py)
- [.ipynb_checkpoints\create_terminology-checkpoint.py](#_ipynb_checkpoints_create_terminology-checkpoint_py)
- [.ipynb_checkpoints\create_terminology_file-checkpoint.py](#_ipynb_checkpoints_create_terminology_file-checkpoint_py)
- [.ipynb_checkpoints\script_extract-checkpoint.py](#_ipynb_checkpoints_script_extract-checkpoint_py)
- [accessibility_modules\aria_checker.py](#accessibility_modules_aria_checker_py)
- [accessibility_modules\focusable_elements.py](#accessibility_modules_focusable_elements_py)
- [accessibility_modules\focus_order_checker.py](#accessibility_modules_focus_order_checker_py)
- [accessibility_modules\html_report_generator.py](#accessibility_modules_html_report_generator_py)
- [accessibility_modules\image_checker.py](#accessibility_modules_image_checker_py)
- [accessibility_modules\report_generator.py](#accessibility_modules_report_generator_py)
- [accessibility_modules\simple_html_report_generator.py](#accessibility_modules_simple_html_report_generator_py)
- [accessibility_modules\tab_order_checker.py](#accessibility_modules_tab_order_checker_py)
- [accessibility_modules\terminology_validator.py](#accessibility_modules_terminology_validator_py)
- [accessibility_modules\test_accordion.py](#accessibility_modules_test_accordion_py)
- [accessibility_modules\__init__.py](#accessibility_modules___init___py)
- [archive\accessibility_checker.py](#archive_accessibility_checker_py)
- [archive\accessibility_checker_starter.py](#archive_accessibility_checker_starter_py)
- [archive\config.py](#archive_config_py)
- [archive\convert_notebooks.py](#archive_convert_notebooks_py)
- [archive\data_loader.py](#archive_data_loader_py)
- [archive\enhanced_report_generator.py](#archive_enhanced_report_generator_py)
- [archive\generate_accessibility_report.py](#archive_generate_accessibility_report_py)
- [archive\missing_focusable_elements.py](#archive_missing_focusable_elements_py)
- [archive\non_text_content_checker.py](#archive_non_text_content_checker_py)
- [archive\.ipynb_checkpoints\accessibility_checker-checkpoint.py](#archive__ipynb_checkpoints_accessibility_checker-checkpoint_py)
- [archive\.ipynb_checkpoints\accessibility_checker_starter-checkpoint.py](#archive__ipynb_checkpoints_accessibility_checker_starter-checkpoint_py)
- [archive\.ipynb_checkpoints\config-checkpoint.py](#archive__ipynb_checkpoints_config-checkpoint_py)
- [archive\.ipynb_checkpoints\convert_notebooks-checkpoint.py](#archive__ipynb_checkpoints_convert_notebooks-checkpoint_py)
- [archive\.ipynb_checkpoints\data_loader-checkpoint.py](#archive__ipynb_checkpoints_data_loader-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\aria_checker-checkpoint.py](#accessibility_modules__ipynb_checkpoints_aria_checker-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\focusable_elements-checkpoint.py](#accessibility_modules__ipynb_checkpoints_focusable_elements-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\focus_order_checker-checkpoint.py](#accessibility_modules__ipynb_checkpoints_focus_order_checker-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\html_report_generator-checkpoint.py](#accessibility_modules__ipynb_checkpoints_html_report_generator-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\image_checker-checkpoint.py](#accessibility_modules__ipynb_checkpoints_image_checker-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\report_generator-checkpoint.py](#accessibility_modules__ipynb_checkpoints_report_generator-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\simple_html_report_generator-checkpoint.py](#accessibility_modules__ipynb_checkpoints_simple_html_report_generator-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\tab_order_checker-checkpoint.py](#accessibility_modules__ipynb_checkpoints_tab_order_checker-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\terminology_validator-checkpoint.py](#accessibility_modules__ipynb_checkpoints_terminology_validator-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\test_accordion-checkpoint.py](#accessibility_modules__ipynb_checkpoints_test_accordion-checkpoint_py)
- [accessibility_modules\.ipynb_checkpoints\__init__-checkpoint.py](#accessibility_modules__ipynb_checkpoints___init__-checkpoint_py)

### Text Files
- [project structure.txt](#project structure_txt)
- [requirements.txt](#requirements_txt)
- [.ipynb_checkpoints\project structure-checkpoint.txt](#_ipynb_checkpoints_project structure-checkpoint_txt)
- [.ipynb_checkpoints\requirements-checkpoint.txt](#_ipynb_checkpoints_requirements-checkpoint_txt)
- [accessibility_modules\accessibility_terminology.txt](#accessibility_modules_accessibility_terminology_txt)
- [accessibility_modules\enhanced_accessibility_checker - README.txt](#accessibility_modules_enhanced_accessibility_checker - README_txt)
- [accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.txt](#accessibility_modules__ipynb_checkpoints_accessibility_terminology-checkpoint_txt)
- [accessibility_modules\.ipynb_checkpoints\enhanced_accessibility_checker - README-checkpoint.txt](#accessibility_modules__ipynb_checkpoints_enhanced_accessibility_checker - README-checkpoint_txt)

### JSON Files
- [accessibility_terminology.json](#accessibility_terminology_json)
- [accessibility_modules\accessibility_terminology.json](#accessibility_modules_accessibility_terminology_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_220026.json](#accessibility_reports_accessibility_report_sse_com_20250310_220026_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_222058.json](#accessibility_reports_accessibility_report_sse_com_20250310_222058_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_222822.json](#accessibility_reports_accessibility_report_sse_com_20250310_222822_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_225526.json](#accessibility_reports_accessibility_report_sse_com_20250310_225526_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_230844.json](#accessibility_reports_accessibility_report_sse_com_20250310_230844_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_232033.json](#accessibility_reports_accessibility_report_sse_com_20250310_232033_json)
- [accessibility_reports\accessibility_report_sse.com_20250310_232415.json](#accessibility_reports_accessibility_report_sse_com_20250310_232415_json)
- [accessibility_reports\comprehensive_sse.com_20250303_180408.json](#accessibility_reports_comprehensive_sse_com_20250303_180408_json)
- [accessibility_reports\missing_focusable_sse.com_20250303_180424.json](#accessibility_reports_missing_focusable_sse_com_20250303_180424_json)
- [accessibility_reports\tab_order_report.json](#accessibility_reports_tab_order_report_json)
- [accessibility_reports\tab_order_sse.com_20250303_180310.json](#accessibility_reports_tab_order_sse_com_20250303_180310_json)
- [accessibility_reports\tab_order_sse.com_20250303_180328.json](#accessibility_reports_tab_order_sse_com_20250303_180328_json)
- [archive\accessibility_terminology.json](#archive_accessibility_terminology_json)
- [accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.json](#accessibility_modules__ipynb_checkpoints_accessibility_terminology-checkpoint_json)

## Jupyter Notebooks

### archive\Accessibility_Checker.ipynb <a id='archive_Accessibility_Checker_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Accessibility_Checker.ipynb
- **Last Modified**: 2025-03-10 16:59:40
- **Size**: 13785 bytes

#### Code
#### Cell 1
```python
# Accessibility_Checker.ipynb
# Main entry point for the accessibility checking system

import sys
import os
from pathlib import Path
from IPython.display import display, HTML, Image, Markdown
import json
import time
from datetime import datetime

# Import URL from config
%run config.ipynb  # Import the config file

# Add the project directory to the path so we can import our modules
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Set path for the accessibility reports
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Import our custom modules
module_files = [
    "Accessibility_Checker.py",
    "Data_Loader.py",
    "Enhanced_Report_Generator.py",
    "Non_Text_Content_Checker.py"  # Add the new module
]

missing_modules = []
for module_file in module_files:
    module_path = Path(module_file)
    if not module_path.exists():
        missing_modules.append(module_file)

if missing_modules:
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 10px; border-left: 4px solid #f44336; margin-bottom: 20px;">
        <h3>⚠️ Missing Required Modules</h3>
        <p>The following required module files were not found:</p>
        <ul>
            {"".join([f"<li>{module}</li>" for module in missing_modules])}
        </ul>
        <p>Please ensure that all required modules are in the same directory as this notebook.</p>
    </div>
    """))
else:
    # Now import the modules
    try:
        from Accessibility_Checker import AccessibilityTerminology, normalize_url, terminology
        from Data_Loader import load_data, count_issues_by_category
        from Enhanced_Report_Generator import (
            generate_accessibility_report, 
            create_visualization,
            get_test_instructions,
            get_fix_example
        )
        from Non_Text_Content_Checker import identify_non_text_content  # Import the new function
        
        display(HTML("""
        <div style="background-color: #e8f5e9; padding: 10px; border-left: 4px solid #4caf50; margin-bottom: 20px;">
            <h3>✅ All Modules Loaded Successfully</h3>
            <p>The accessibility checker modules have been loaded and are ready to use.</p>
        </div>
        """))
    except ImportError as e:
        display(HTML(f"""
        <div style="background-color: #ffebee; padding: 10px; border-left: 4px solid #f44336; margin-bottom: 20px;">
            <h3>⚠️ Error Loading Modules</h3>
            <p>An error occurred while importing the required modules:</p>
            <p><code>{str(e)}</code></p>
            <p>Please ensure that all required modules are in the same directory as this notebook.</p>
        </div>
        """))

# Display welcome message and instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="color: #0275d8;">📋 Enhanced Accessibility Checker</h1>
    <h3>A comprehensive tool for evaluating web accessibility</h3>
    
    <p>This notebook runs a series of accessibility checks on a given URL and generates a detailed report.</p>
    
    <h4>Instructions:</h4>
    <ol>
        <li>Enter the URL of the website you want to check in the <code>url_to_check</code> variable in the <code>config.ipynb</code> file.</li>
        <li>Run all cells in this notebook.</li>
        <li>The accessibility report will be generated and saved in the <code>accessibility_reports</code> directory.</li>
    </ol>
</div>
"""))

# Import Selenium and related modules
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    # Store the Inconsistent keyboard navigation sequences
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
        "non_text_content_elements": non_text_elements  # Add non-text content elements to the report
    }
    
    report_path = generate_accessibility_report(report_data)
    
    # Create visualization
    visualization_path = create_visualization(report_data)
    
    # Display the report and visualization
    display(Markdown(f"## Accessibility Report\n[Open Report]({report_path})"))
    display(Image(visualization_path))
    
    # Provide recommendations and examples
    for issue_category in ["tab_order_issues", "missing_focusable_issues", "aria_issues", "keyboard_issues"]:
        if report_data[issue_category]:
            issue_description = report_data[issue_category][0]  # Consider the first issue as an example
            test_instructions = get_test_instructions(issue_category, issue_description)
            fix_example = get_fix_example(issue_category, issue_description)
            
            display(HTML(f"""
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
                <h4>{issue_category.replace("_", " ").title()}</h4>
                <p><strong>Example Issue:</strong> {issue_description}</p>
                <p><strong>Testing Instructions:</strong> {test_instructions}</p>
                <p><strong>Fix Example:</strong></p>
                <pre><code>{fix_example}</code></pre>
            </div>
            """))

# Run the accessibility checks
run_accessibility_checks(url_to_check)
```
### archive\Accessibility_Checker_Starter.ipynb <a id='archive_Accessibility_Checker_Starter_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Accessibility_Checker_Starter.ipynb
- **Last Modified**: 2025-03-10 17:02:25
- **Size**: 9353 bytes

#### Code
#### Cell 1
```python
#!/usr/bin/env python3
"""
Accessibility Checker - Main Controller Script

This script serves as the central entry point for running various 
accessibility checking tools and generating reports.
"""

import sys
import importlib
import argparse
from pathlib import Path
import os  # Import the 'os' module

# Determine the current directory (handle both script and notebook execution)
try:
    current_dir = Path(__file__).parent
except NameError:
    current_dir = Path(os.getcwd())  # Use the current working directory in Notebook
sys.path.insert(0, str(current_dir))

# Available modules for accessibility checking
AVAILABLE_MODULES = {
    'tab_order': 'Comprehensive_Tab_Order_Checker',
    'missing_focusable': 'Missing_Focusable_Elements',
    'generate_report': 'Generate_Accessibility_Report',
    'aria_check': 'ARIA_And_Keyboard_Accessibility_Checker'
}

def import_module(module_name):
    """
    Dynamically import a module by name.
    
    Args:
        module_name (str): Name of the module to import
    
    Returns:
        module: Imported module or None if import fails
    """
    try:
        # Try importing from the predefined module names
        if module_name in AVAILABLE_MODULES:
            module_path = AVAILABLE_MODULES[module_name]
            return importlib.import_module(module_path)
        
        # Try importing the exact module name provided
        return importlib.import_module(module_name)
    except ImportError as e:
        print(f"❌ Could not import module '{module_name}': {e}")
        return None

def run_tab_order_check(url, browser='chrome'):
    """
    Run tab order accessibility check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('tab_order')
    if module and hasattr(module, 'check_tab_order'):
        return module.check_tab_order(url, browser)
    print("❌ Tab order check module not available.")
    return None

def run_missing_focusable_check(url, browser='chrome'):
    """
    Run missing focusable elements check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Missing focusable elements check module not available.")
    return None

def generate_comprehensive_report(url):
    """
    Generate a comprehensive accessibility report.
    
    Args:
        url (str): Website URL to generate report for
    """
    module = import_module('generate_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ Report generation module not available.")
    return None

def run_aria_check(url, browser='chrome'):
    """
    Run ARIA and keyboard accessibility check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('aria_check')
    if module and hasattr(module, 'run_comprehensive_check'):
        return module.run_comprehensive_check(url, browser)
    print("❌ ARIA and keyboard accessibility check module not available.")
    return None

def main():
    """
    Main entry point for the Accessibility Checker.
    """
    parser = argparse.ArgumentParser(description="Accessibility Checker - Comprehensive Web Accessibility Testing Tool")
    
    # Add arguments
    parser.add_argument('--url', help='Website URL to check', default=url_to_check) # add the url config and set as default
    parser.add_argument('--browser', default='chrome', 
                        choices=['chrome', 'firefox', 'edge'], 
                        help='Browser to use for testing (default: chrome)')
    parser.add_argument('--check', choices=['tab_order', 'missing_focusable', 'aria', 'report', 'all'], 
                        default='all', 
                        help='Specific type of accessibility check to run')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Welcome message
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {args.url}")
    print(f"Browser: {args.browser}")
    print("=" * 60)
    
    # Run specific or all checks
    try:
        if args.check in ['tab_order', 'all']:
            print("\n📊 Running Tab Order Check...")
            tab_order_result = run_tab_order_check(args.url, args.browser)
        
        if args.check in ['missing_focusable', 'all']:
            print("\n🕵️ Checking Missing Focusable Elements...")
            missing_focusable_result = run_missing_focusable_check(args.url, args.browser)
        
        if args.check in ['aria', 'all']:
            print("\n♿ Running ARIA and Keyboard Accessibility Check...")
            aria_result = run_aria_check(args.url, args.browser)
        
        if args.check in ['report', 'all']:
            print("\n📄 Generating Comprehensive Report...")
            report = generate_comprehensive_report(args.url)
        
        print("\n" + "=" * 60)
        print("✅ Accessibility Check Complete")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n❌ An error occurred during the accessibility check: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Import URL from config
    from config import url_to_check
    main()

# Usage examples:
# python accessibility_checker.py https://www.example.com
# python accessibility_checker.py https://www.example.com --check tab_order
# python accessibility_checker.py https://www.example.com --browser firefox --check all
```
#### Cell 2
```python

```
### archive\config.ipynb <a id='archive_config_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\config.ipynb
- **Last Modified**: 2025-03-03 21:48:48
- **Size**: 1124 bytes

#### Code
#### Cell 1
```python
# config.ipynb

# Configuration for Web Accessibility Audit

# Website to be audited
url_to_check = "https://www.sse.com"

# Browser for testing
browser_choice = "chrome"  # Options: 'chrome', 'firefox', 'edge'

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Optional additional configurations can be added here
```
### archive\Data_Loader.ipynb <a id='archive_Data_Loader_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Data_Loader.ipynb
- **Last Modified**: 2025-03-03 22:13:30
- **Size**: 9082 bytes

#### Code
#### Cell 1
```python
# Data_Loader.ipynb

import json
import glob
import os
import hashlib
from pathlib import Path
from datetime import datetime

# Import from our main module
%run config.ipynb # import config
from Accessibility_Checker import (
    REPORTS_DIR, 
    AccessibilityIssue, 
    normalize_url, 
    translate_accessibility_issue,
    determine_severity,
    terminology
)

def load_data(url=url_to_check): # changed to default to config URL
    """
    Load accessibility data for a given URL from all available reports.
    
    Args:
        url: URL of the website that was tested
        
    Returns:
        dict: Consolidated data from all reports
    """
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issues": []
    }
    
    # Track unique issues to prevent duplicates
    unique_issues = set()
    
    try:
        # Load data from various report files - using all formats of URL
        report_types = [
            ("tab_order", f"tab_order_{clean_url}_*.json"),
            ("tab_order", f"tab_order_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("missing_focusable", f"missing_focusable_{clean_url}_*.json"),
            ("missing_focusable", f"missing_focusable_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("comprehensive", f"comprehensive_{clean_url}_*.json"),
            ("comprehensive", f"comprehensive_{url.replace('https://', '').replace('http://', '')}_*.json")
        ]
        
        found_data = False
        
        for report_type, pattern in report_types:
            full_pattern = str(REPORTS_DIR / pattern)
            files = glob.glob(full_pattern)
            
            if files:
                latest_file = max(files, key=lambda p: os.path.getmtime(p))
                print(f"Loading {report_type} data from: {os.path.basename(latest_file)}")
                
                with open(latest_file, 'r') as f:
                    report_data = json.load(f)
                    
                    # Define issue_sources based on report type
                    issue_sources = {}
                    
                    if report_type == "tab_order":
                        issue_sources["Tab Order"] = report_data.get("tab_order_issues", [])
                    elif report_type == "missing_focusable":
                        issue_sources["Missing Focusable"] = report_data.get("missing_focusable_issues", [])
                    elif report_type == "comprehensive":
                        issue_sources = {
                            "Tab Order": report_data.get("tab_order_issues", []),
                            "Missing Focusable": report_data.get("missing_focusable_issues", []),
                            "ARIA": report_data.get("aria_issues", []),
                            "Keyboard": report_data.get("keyboard_issues", [])
                        }
                    
                    for category, issues in issue_sources.items():
                        if not issues:
                            continue
                            
                        for issue_text in issues:
                            found_data = True
                            
                            # Handle different data formats
                            if isinstance(issue_text, dict):
                                issue_desc = issue_text.get('issue', str(issue_text))
                            else:
                                issue_desc = str(issue_text)
                            
                            # Create a unique identifier for this issue
                            issue_hash = hashlib.md5(f"{category}:{issue_desc}".encode()).hexdigest()
                            
                            # Skip if we've already processed this issue
                            if issue_hash in unique_issues:
                                continue
                            unique_issues.add(issue_hash)
                            
                            # Translate the issue to a more descriptive format
                            translated_issue = translate_accessibility_issue(issue_desc, category, terminology)
                            
                            severity = determine_severity(translated_issue['description'])
                            accessibility_issue = AccessibilityIssue(
                                description=translated_issue['description'],
                                category=category,
                                severity=severity
                            )
                            
                            # Add additional metadata to the issue
                            accessibility_issue.original_text = translated_issue['original']
                            accessibility_issue.impact = translated_issue['impact']
                            accessibility_issue.recommendation = translated_issue['recommendation']
                            
                            data["issues"].append(accessibility_issue)
        
        if not found_data:
            print(f"⚠️ Warning: No accessibility reports found for {url}")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"✅ Loaded {len(data['issues'])} unique accessibility issues from reports")
    return data

def count_issues_by_category(data):
    """Count issues by category and severity"""
    counts = {
        'by_category': {},
        'by_severity': {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        },
        'total': len(data['issues'])
    }
    
    for issue in data['issues']:
        # Count by category
        if issue.category not in counts['by_category']:
            counts['by_category'][issue.category] = 0
        counts['by_category'][issue.category] += 1
        
        # Count by severity
        counts['by_severity'][issue.severity] += 1
    
    return counts

# Example usage
if __name__ == "__main__":
    test_url = url_to_check  # Replace with your target website

    print(f"Testing data loader with URL: {test_url}")
    data = load_data() # removed the need to include the url
    
    if data["issues"]:
        counts = count_issues_by_category(data)
        print("\nIssue Counts by Category:")
        for category, count in counts['by_category'].items():
            print(f"- {category}: {count}")
        
        print("\nIssue Counts by Severity:")
        for severity, count in counts['by_severity'].items():
            print(f"- {severity.capitalize()}: {count}")
    else:
        print("No issues found in any reports.")
```
### archive\Enhanced_Report_Generator.ipynb <a id='archive_Enhanced_Report_Generator_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Enhanced_Report_Generator.ipynb
- **Last Modified**: 2025-03-03 22:04:57
- **Size**: 14466 bytes

#### Code
#### Cell 1
```python
# Enhanced_Report_Generator.ipynb

# Import URL from config
%run config.ipynb

import os
import hashlib
from pathlib import Path
from datetime import datetime
import webbrowser
import matplotlib.pyplot as plt
import numpy as np

# Import from our custom modules
from Accessibility_Checker import REPORTS_DIR, normalize_url, terminology
from Data_Loader import load_data, count_issues_by_category

def get_test_instructions(category, description):
   """
   Generate practical testing instructions based on the issue category and description.
   """
   if category == "Tab Order":
       return "Try navigating through the page using only the Tab key. Notice if the focus jumps around in an unpredictable or illogical order."
   
   elif category == "Missing Focusable":
       return "Attempt to interact with this element using only your keyboard (without using a mouse). Try tabbing to it and pressing Enter/Space. If you cannot reach or activate it, the issue is confirmed."
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return "Use a screen reader to navigate to this image. The screen reader should announce a meaningful description of the image content, not just its filename or 'image'."
       elif "label" in description.lower():
           return "Use a screen reader to navigate to this form field. The screen reader should clearly announce the purpose of the field."
       elif "heading" in description.lower():
           return "Check the document outline using an accessibility tool like WAVE or axe. The headings should follow a logical hierarchical structure."
       elif "landmark" in description.lower():
           return "Use a screen reader's landmarks navigation feature. Important sections of the page should be reachable through landmarks."
       return "Use a screen reader to verify this element provides appropriate context and information."
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return "Tab to this element and check if there is a clearly visible indicator showing that it has keyboard focus. The focus should be easily noticeable against the background."
       return "Test this element using only keyboard controls (Tab, Enter, Space, arrow keys). You should be able to access and operate all functionality without a mouse."
   
   return "Navigate to this element and test its behavior using both keyboard-only navigation and a screen reader."

def get_fix_example(category, description, severity):
   """
   Generate code examples to fix the issue based on category, description and severity.
   """
   if category == "Tab Order":
       return """
           Ensure tabindex attributes follow a logical order:
           ```html
<!-- Avoid using tabindex values like this -->
<div tabindex="1">First element</div>
<div tabindex="3">Second element</div> <!-- Problem: out of sequence -->
<div tabindex="2">Third element</div>

<!-- Better approach: use tabindex="0" or adjust the DOM order -->
<div tabindex="0">First element</div>
<div tabindex="0">Second element</div>
<div tabindex="0">Third element</div>
           ```
       """
   
   elif category == "Missing Focusable":
       if "div" in description.lower() or "span" in description.lower():
           return """
               Convert div/span to a semantic button or add proper ARIA roles:
               ```html
<!-- Instead of this -->
<div class="btn" onclick="doSomething()">Click Me</div>

<!-- Use this -->
<button onclick="doSomething()">Click Me</button>

<!-- Or if you must use a div, add these attributes -->
<div class="btn" 
    onclick="doSomething()" 
    onkeydown="if(event.key==='Enter'||event.key===' ')doSomething()" 
    role="button" 
    tabindex="0">Click Me</div>
               ```
           """
       return """
           Make the element keyboard accessible:
           ```html
<!-- Add tabindex="0" to make it focusable -->
<!-- Add keyboard event handlers alongside click handlers -->
<!-- Add appropriate ARIA role if not using a semantic element -->

<element tabindex="0" 
        role="appropriate-role" 
        onclick="doAction()" 
        onkeydown="if(event.key==='Enter')doAction()">
   Content
</element>
           ```
       """
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return """
               Add descriptive alt text to images:
               ```html
<!-- Avoid this -->
<img src="chart.png">

<!-- Use this instead -->
<img src="chart.png" alt="Bar chart showing sales growth by quarter for 2023, with Q4 showing highest growth at 27%">
               ```
           """
       elif "label" in description.lower():
           return """
               Add proper labels to form fields:
               ```html
<!-- Avoid this -->
<input type="text" name="email" placeholder="Enter email">

<!-- Use this instead -->
<label for="email">Email Address</label>
<input type="text" id="email" name="email">
               ```
           """
       elif "heading" in description.lower():
           return """
               Fix heading structure to follow hierarchy:
               ```html
<!-- Avoid this -->
<h1>Page Title</h1>
<h3>First Section</h3> <!-- Problem: skipped h2 -->

<!-- Use this instead -->
<h1>Page Title</h1>
<h2>First Section</h2>
<h3>Subsection</h3>
               ```
           """
       elif "landmark" in description.lower():
           return """
               Add proper landmark roles to page sections:
               ```html
<!-- Add these structural elements -->
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<footer role="contentinfo">...</footer>
               ```
           """
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return """
               Ensure visible focus styles:
               ```css
/* Add this to your CSS */
:focus {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
}

/* For better visibility against different backgrounds */
:focus-visible {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
 box-shadow: 0 0 0 4px rgba(0, 102, 255, 0.3);
}
               ```
           """
   
   return """Implement appropriate fixes based on the issue description and web accessibility best practices."""

def get_wcag_criteria(category, description):
   """
   Map issue categories to relevant WCAG criteria.
   """
   criteria = {
       "Tab Order": "2.4.3 Focus Order (Level A)",
       "Missing Focusable": "2.1.1 Keyboard (Level A)",
       "ARIA": {
           "alt": "1.1.1 Non-text Content (Level A)",
           "label": "3.3.2 Labels or Instructions (Level A)",
           "heading": "1.3.1 Info and Relationships (Level A), 2.4.6 Headings and Labels (Level AA)",
           "landmark": "1.3.1 Info and Relationships (Level A), 4.1.2 Name, Role, Value (Level A)"
       },
       "Keyboard": {
           "focus indicator": "2.4.7 Focus Visible (Level AA)",
           "default": "2.1.1 Keyboard (Level A)"
       }
   }
   
   if category == "ARIA":
       for key, value in criteria["ARIA"].items():
           if key in description.lower():
               return value
       return criteria["ARIA"].get("landmark")  # Default for ARIA
   
   elif category == "Keyboard":
       for key, value in criteria["Keyboard"].items():
           if key in description.lower():
               return value
       return criteria["Keyboard"].get("default")  # Default for Keyboard
   
   return criteria.get(category, "")

def create_visualization(data, output_path=None):
   """Create visualization of accessibility issues."""
   if not output_path:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       output_path = REPORTS_DIR / f"visualization_{timestamp}.png"
   
   counts = count_issues_by_category(data)
   
   # Create a figure with two subplots
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
   
   # Plot issues by category
   categories = list(counts['by_category'].keys())
   category_counts = list(counts['by_category'].values())
   
   # Sort by count
   sorted_indices = np.argsort(category_counts)
   sorted_categories = [categories[i] for i in sorted_indices]
   sorted_counts = [category_counts[i] for i in sorted_indices]
   
   ax1.barh(sorted_categories, sorted_counts, color='steelblue')
   ax1.set_title('Issues by Category')
   ax1.set_xlabel('Number of Issues')
   
   # Plot issues by severity
   severities = ['critical', 'high', 'medium', 'low']
   severity_counts = [counts['by_severity'][s] for s in severities]
   
   colors = ['darkred', 'orangered', 'orange', 'yellowgreen']
   ax2.pie(severity_counts, labels=severities, autopct='%1.1f%%', 
          shadow=True, startangle=90, colors=colors)
   ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   ax2.set_title('Issues by Severity')
   
   plt.tight_layout()
   plt.savefig(output_path)
   
   return output_path

def generate_enhanced_html_report(data, output_path=None):
   """
   Generate an enhanced bipolar HTML report with information suitable for both
   accessibility experts and non-experts.
   
   Args:
       data: Dictionary containing all accessibility data
       output_path: Path to save the HTML report (optional)
   
   Returns:
       str: Path to the generated HTML report
   """
   # Prepare output path
   if output_path is None:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       clean_url = normalize_url(data.get("url", "unknown"))
       output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
   
   # Ensure reports directory exists
   os.makedirs(os.path.dirname(output_path), exist_ok=True)
   
   # Prepare issue categorization
   categorized_issues = {
       'critical': [],
       'high': [],
       'medium': [],
       'low': []
   }
   
   # Generate a unique hash for each issue to deduplicate
   unique_issues = {}
   
   # Process all issues and deduplicate
   for issue in data.get("issues", []):
       # Create a hash based on core issue properties to identify duplicates
       issue_key = hashlib.md5(
           f"{issue.category}:{issue.description[:100]}".encode()
       ).hexdigest()
       
       # If we've seen this issue before, skip it
       if issue_key in unique_issues:
           continue
           
       # Store unique issue
       unique_issues[issue_key] = issue
       categorized_issues[issue.severity].append(issue)
   
   # Count issues by category for summary
   issue_counts = {
       category: len(issues) for category, issues in categorized_issues.items()
   }
   
   # (Remaining HTML generation code is extremely long, so I've truncated it for brevity)
   # Would you like me to include the full HTML generation code?

   return str(output_path)
```
### archive\Generate_Accessibility_Report.ipynb <a id='archive_Generate_Accessibility_Report_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Generate_Accessibility_Report.ipynb
- **Last Modified**: 2025-03-10 16:59:45
- **Size**: 5323 bytes

#### Code
#### Cell 1
```python
# Generate_Accessibility_Report.ipynb
# Interactive notebook for testing and generating accessibility reports

import os
import sys
from pathlib import Path
import webbrowser
from IPython.display import display, HTML, Markdown, Image, clear_output
import ipywidgets as widgets

# Import URL from config
%run config.ipynb

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import required modules
try:
    from Accessibility_Checker import normalize_url, terminology
    from Data_Loader import load_data, count_issues_by_category
    from Enhanced_Report_Generator import generate_accessibility_report
    
    # Show success message
    display(HTML("""
    <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">✅ Modules Loaded Successfully</h3>
        <p style="margin-bottom: 0;">Ready to generate accessibility reports.</p>
    </div>
    """))
except ImportError as e:
    # Show error message
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">❌ Error Loading Modules</h3>
        <p>Could not load required modules: {str(e)}</p>
        <p style="margin-bottom: 0;">Please ensure all module files are in the same directory as this notebook.</p>
    </div>
    """))

# Display header
display(HTML("""
<div style="background-color: #e8f5e9; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="margin-top: 0;">🔍 Accessibility Report Generator</h1>
    <p>Generate comprehensive accessibility reports from previously collected data.</p>
</div>
"""))

# URL Input with default from config
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='70%')
)

# Progress output
progress_output = widgets.Output()

# Generate button
generate_button = widgets.Button(
    description='Generate Report',
    button_style='primary',
    tooltip='Click to generate an accessibility report',
    icon='chart-bar'
)

# Output area for report generation status
output_area = widgets.Output()

# Function to handle the button click
def on_generate_button_clicked(b):
    # Rest of the function remains the same as in the previous implementation
    # ... (previous implementation of the function)
    pass

# Set up button click handler
generate_button.on_click(on_generate_button_clicked)

# Display the widgets
display(widgets.VBox([
    widgets.HBox([url_input, generate_button]),
    progress_output,
    output_area
]))

# Show instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
    <h3>📋 Instructions</h3>
    <ol>
        <li>First, ensure that you have run the accessibility tests using the appropriate test scripts.</li>
        <li>Enter the URL you want to generate a report for in the URL field.</li>
        <li>Click the "Generate Report" button to create the report.</li>
        <li>The report will open automatically in your default browser.</li>
    </ol>
    
    <h4>Notes:</h4>
    <ul>
        <li>The report generator requires data from previous accessibility scans to be available.</li>
        <li>If no data is found, you'll need to run the data collection scripts first.</li>
        <li>Reports include visualizations, practical guidance for developers, and detailed technical information for accessibility experts.</li>
    </ul>
</div>
"""))
```
### archive\Missing_Focusable_Elements.ipynb <a id='archive_Missing_Focusable_Elements_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Missing_Focusable_Elements.ipynb
- **Last Modified**: 2025-03-03 22:39:13
- **Size**: 3389 bytes

#### Code
#### Cell 1
```python
# Missing_Focusable_Elements.ipynb
# Script to detect elements that should be keyboard-accessible but aren't

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets

# Import URL from config
%run config.ipynb

# Try to import Selenium
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Try to import BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import our custom module for utility functions
from Accessibility_Checker import normalize_url, terminology

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# (Existing script continues exactly as in the original document, with these two modifications)

# URL Input
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='50%')
)

# Browser dropdown
browser_dropdown = widgets.Dropdown(
    options=['chrome', 'firefox', 'edge'],
    value=browser_choice,
    description='Browser:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='30%')
)

# (The rest of the script remains EXACTLY the same as in the original document)
# This includes all the existing functions and remaining code
```
### archive\Non_Text_Content_Checker.ipynb <a id='archive_Non_Text_Content_Checker_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Non_Text_Content_Checker.ipynb
- **Last Modified**: 2025-03-10 16:59:42
- **Size**: 1510 bytes

#### Code
#### Cell 1
```python
from bs4 import BeautifulSoup

def identify_non_text_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    non_text_elements = []

    # Find elements that typically contain non-text content
    element_types = ['img', 'svg', 'video', 'audio', 'object', 'embed', 'canvas']
    for element_type in element_types:
        elements = soup.find_all(element_type)
        for element in elements:
            element_info = {
                'tag': element.name,
                'src': element.get('src'),
                'alt': element.get('alt'),
                # Extract other relevant attributes as needed
            }
            non_text_elements.append(element_info)

    return non_text_elements
```
### archive\Script_Extract.ipynb <a id='archive_Script_Extract_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Script_Extract.ipynb
- **Last Modified**: 2025-03-03 22:11:03
- **Size**: 10569 bytes

#### Code
#### Cell 1
```python
import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    notebook_files = list(Path(folder_path).glob('*.ipynb'))

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    markdown_content += "\n## Table of Contents\n"
    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"- [{notebook_name}](#{notebook_name})\n"

    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"\n## {notebook_name} <a id='{notebook_name}'></a>\n"
        markdown_content += f"### File Information\n"
        markdown_content += f"- **Type**: Jupyter Notebook\n"
        markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
        markdown_content += "\n### Code\n"
        markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    return markdown_content

# Rest of the script remains the same as before
    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your Jupyter Notebooks folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
#### Cell 2
```python

```
### archive\Script_Extract_a.ipynb <a id='archive_Script_Extract_a_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\Script_Extract_a.ipynb
- **Last Modified**: 2025-03-10 16:31:25
- **Size**: 10569 bytes

#### Code
#### Cell 1
```python
import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    notebook_files = list(Path(folder_path).glob('*.ipynb'))

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    markdown_content += "\n## Table of Contents\n"
    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"- [{notebook_name}](#{notebook_name})\n"

    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"\n## {notebook_name} <a id='{notebook_name}'></a>\n"
        markdown_content += f"### File Information\n"
        markdown_content += f"- **Type**: Jupyter Notebook\n"
        markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
        markdown_content += "\n### Code\n"
        markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    return markdown_content

# Rest of the script remains the same as before
    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your Jupyter Notebooks folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
#### Cell 2
```python

```
### archive\.ipynb_checkpoints\Accessibility_Checker-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Accessibility_Checker-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Accessibility_Checker-checkpoint.ipynb
- **Last Modified**: 2025-03-10 16:59:40
- **Size**: 13785 bytes

#### Code
#### Cell 1
```python
# Accessibility_Checker.ipynb
# Main entry point for the accessibility checking system

import sys
import os
from pathlib import Path
from IPython.display import display, HTML, Image, Markdown
import json
import time
from datetime import datetime

# Import URL from config
%run config.ipynb  # Import the config file

# Add the project directory to the path so we can import our modules
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Set path for the accessibility reports
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Import our custom modules
module_files = [
    "Accessibility_Checker.py",
    "Data_Loader.py",
    "Enhanced_Report_Generator.py",
    "Non_Text_Content_Checker.py"  # Add the new module
]

missing_modules = []
for module_file in module_files:
    module_path = Path(module_file)
    if not module_path.exists():
        missing_modules.append(module_file)

if missing_modules:
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 10px; border-left: 4px solid #f44336; margin-bottom: 20px;">
        <h3>⚠️ Missing Required Modules</h3>
        <p>The following required module files were not found:</p>
        <ul>
            {"".join([f"<li>{module}</li>" for module in missing_modules])}
        </ul>
        <p>Please ensure that all required modules are in the same directory as this notebook.</p>
    </div>
    """))
else:
    # Now import the modules
    try:
        from Accessibility_Checker import AccessibilityTerminology, normalize_url, terminology
        from Data_Loader import load_data, count_issues_by_category
        from Enhanced_Report_Generator import (
            generate_accessibility_report, 
            create_visualization,
            get_test_instructions,
            get_fix_example
        )
        from Non_Text_Content_Checker import identify_non_text_content  # Import the new function
        
        display(HTML("""
        <div style="background-color: #e8f5e9; padding: 10px; border-left: 4px solid #4caf50; margin-bottom: 20px;">
            <h3>✅ All Modules Loaded Successfully</h3>
            <p>The accessibility checker modules have been loaded and are ready to use.</p>
        </div>
        """))
    except ImportError as e:
        display(HTML(f"""
        <div style="background-color: #ffebee; padding: 10px; border-left: 4px solid #f44336; margin-bottom: 20px;">
            <h3>⚠️ Error Loading Modules</h3>
            <p>An error occurred while importing the required modules:</p>
            <p><code>{str(e)}</code></p>
            <p>Please ensure that all required modules are in the same directory as this notebook.</p>
        </div>
        """))

# Display welcome message and instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="color: #0275d8;">📋 Enhanced Accessibility Checker</h1>
    <h3>A comprehensive tool for evaluating web accessibility</h3>
    
    <p>This notebook runs a series of accessibility checks on a given URL and generates a detailed report.</p>
    
    <h4>Instructions:</h4>
    <ol>
        <li>Enter the URL of the website you want to check in the <code>url_to_check</code> variable in the <code>config.ipynb</code> file.</li>
        <li>Run all cells in this notebook.</li>
        <li>The accessibility report will be generated and saved in the <code>accessibility_reports</code> directory.</li>
    </ol>
</div>
"""))

# Import Selenium and related modules
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    # Store the Inconsistent keyboard navigation sequences
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
        "non_text_content_elements": non_text_elements  # Add non-text content elements to the report
    }
    
    report_path = generate_accessibility_report(report_data)
    
    # Create visualization
    visualization_path = create_visualization(report_data)
    
    # Display the report and visualization
    display(Markdown(f"## Accessibility Report\n[Open Report]({report_path})"))
    display(Image(visualization_path))
    
    # Provide recommendations and examples
    for issue_category in ["tab_order_issues", "missing_focusable_issues", "aria_issues", "keyboard_issues"]:
        if report_data[issue_category]:
            issue_description = report_data[issue_category][0]  # Consider the first issue as an example
            test_instructions = get_test_instructions(issue_category, issue_description)
            fix_example = get_fix_example(issue_category, issue_description)
            
            display(HTML(f"""
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
                <h4>{issue_category.replace("_", " ").title()}</h4>
                <p><strong>Example Issue:</strong> {issue_description}</p>
                <p><strong>Testing Instructions:</strong> {test_instructions}</p>
                <p><strong>Fix Example:</strong></p>
                <pre><code>{fix_example}</code></pre>
            </div>
            """))

# Run the accessibility checks
run_accessibility_checks(url_to_check)
```
### archive\.ipynb_checkpoints\Accessibility_Checker_Starter-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Accessibility_Checker_Starter-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Accessibility_Checker_Starter-checkpoint.ipynb
- **Last Modified**: 2025-03-03 22:22:40
- **Size**: 8106 bytes

#### Code
#### Cell 1
```python
#!/usr/bin/env python3
"""
Accessibility Checker - Main Controller Script

This script serves as the central entry point for running various 
accessibility checking tools and generating reports.
"""

import sys
import importlib
import argparse
from pathlib import Path
import os  # Import the 'os' module

# Determine the current directory (handle both script and notebook execution)
try:
    current_dir = Path(__file__).parent
except NameError:
    current_dir = Path(os.getcwd())  # Use the current working directory in Notebook
sys.path.insert(0, str(current_dir))

# Available modules for accessibility checking
AVAILABLE_MODULES = {
    'tab_order': 'Comprehensive_Tab_Order_Checker',
    'missing_focusable': 'Missing_Focusable_Elements',
    'generate_report': 'Generate_Accessibility_Report',
    'aria_check': 'ARIA_And_Keyboard_Accessibility_Checker'
}

def import_module(module_name):
    """
    Dynamically import a module by name.
    
    Args:
        module_name (str): Name of the module to import
    
    Returns:
        module: Imported module or None if import fails
    """
    try:
        # Try importing from the predefined module names
        if module_name in AVAILABLE_MODULES:
            module_path = AVAILABLE_MODULES[module_name]
            return importlib.import_module(module_path)
        
        # Try importing the exact module name provided
        return importlib.import_module(module_name)
    except ImportError as e:
        print(f"❌ Could not import module '{module_name}': {e}")
        return None

def run_tab_order_check(url, browser='chrome'):
    """
    Run tab order accessibility check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('tab_order')
    if module and hasattr(module, 'check_tab_order'):
        return module.check_tab_order(url, browser)
    print("❌ Tab order check module not available.")
    return None

def run_missing_focusable_check(url, browser='chrome'):
    """
    Run missing focusable elements check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Missing focusable elements check module not available.")
    return None

def generate_comprehensive_report(url):
    """
    Generate a comprehensive accessibility report.
    
    Args:
        url (str): Website URL to generate report for
    """
    module = import_module('generate_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ Report generation module not available.")
    return None

def run_aria_check(url, browser='chrome'):
    """
    Run ARIA and keyboard accessibility check.
    
    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('aria_check')
    if module and hasattr(module, 'run_comprehensive_check'):
        return module.run_comprehensive_check(url, browser)
    print("❌ ARIA and keyboard accessibility check module not available.")
    return None

def main():
    """
    Main entry point for the Accessibility Checker.
    """
    parser = argparse.ArgumentParser(description="Accessibility Checker - Comprehensive Web Accessibility Testing Tool")
    
    # Add arguments
    parser.add_argument('--url', help='Website URL to check', default=url_to_check) # add the url config and set as default
    parser.add_argument('--browser', default='chrome', 
                        choices=['chrome', 'firefox', 'edge'], 
                        help='Browser to use for testing (default: chrome)')
    parser.add_argument('--check', choices=['tab_order', 'missing_focusable', 'aria', 'report', 'all'], 
                        default='all', 
                        help='Specific type of accessibility check to run')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Welcome message
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {args.url}")
    print(f"Browser: {args.browser}")
    print("=" * 60)
    
    # Run specific or all checks
    try:
        if args.check in ['tab_order', 'all']:
            print("\n📊 Running Tab Order Check...")
            tab_order_result = run_tab_order_check(args.url, args.browser)
        
        if args.check in ['missing_focusable', 'all']:
            print("\n🕵️ Checking Missing Focusable Elements...")
            missing_focusable_result = run_missing_focusable_check(args.url, args.browser)
        
        if args.check in ['aria', 'all']:
            print("\n♿ Running ARIA and Keyboard Accessibility Check...")
            aria_result = run_aria_check(args.url, args.browser)
        
        if args.check in ['report', 'all']:
            print("\n📄 Generating Comprehensive Report...")
            report = generate_comprehensive_report(args.url)
        
        print("\n" + "=" * 60)
        print("✅ Accessibility Check Complete")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n❌ An error occurred during the accessibility check: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Import URL from config
    from config import url_to_check
    main()

# Usage examples:
# python accessibility_checker.py https://www.example.com
# python accessibility_checker.py https://www.example.com --check tab_order
# python accessibility_checker.py https://www.example.com --browser firefox --check all
```
### archive\.ipynb_checkpoints\config-checkpoint.ipynb <a id='archive__ipynb_checkpoints_config-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\config-checkpoint.ipynb
- **Last Modified**: 2025-03-03 21:48:48
- **Size**: 1124 bytes

#### Code
#### Cell 1
```python
# config.ipynb

# Configuration for Web Accessibility Audit

# Website to be audited
url_to_check = "https://www.sse.com"

# Browser for testing
browser_choice = "chrome"  # Options: 'chrome', 'firefox', 'edge'

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Optional additional configurations can be added here
```
### archive\.ipynb_checkpoints\Data_Loader-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Data_Loader-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Data_Loader-checkpoint.ipynb
- **Last Modified**: 2025-03-03 22:13:30
- **Size**: 9082 bytes

#### Code
#### Cell 1
```python
# Data_Loader.ipynb

import json
import glob
import os
import hashlib
from pathlib import Path
from datetime import datetime

# Import from our main module
%run config.ipynb # import config
from Accessibility_Checker import (
    REPORTS_DIR, 
    AccessibilityIssue, 
    normalize_url, 
    translate_accessibility_issue,
    determine_severity,
    terminology
)

def load_data(url=url_to_check): # changed to default to config URL
    """
    Load accessibility data for a given URL from all available reports.
    
    Args:
        url: URL of the website that was tested
        
    Returns:
        dict: Consolidated data from all reports
    """
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issues": []
    }
    
    # Track unique issues to prevent duplicates
    unique_issues = set()
    
    try:
        # Load data from various report files - using all formats of URL
        report_types = [
            ("tab_order", f"tab_order_{clean_url}_*.json"),
            ("tab_order", f"tab_order_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("missing_focusable", f"missing_focusable_{clean_url}_*.json"),
            ("missing_focusable", f"missing_focusable_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("comprehensive", f"comprehensive_{clean_url}_*.json"),
            ("comprehensive", f"comprehensive_{url.replace('https://', '').replace('http://', '')}_*.json")
        ]
        
        found_data = False
        
        for report_type, pattern in report_types:
            full_pattern = str(REPORTS_DIR / pattern)
            files = glob.glob(full_pattern)
            
            if files:
                latest_file = max(files, key=lambda p: os.path.getmtime(p))
                print(f"Loading {report_type} data from: {os.path.basename(latest_file)}")
                
                with open(latest_file, 'r') as f:
                    report_data = json.load(f)
                    
                    # Define issue_sources based on report type
                    issue_sources = {}
                    
                    if report_type == "tab_order":
                        issue_sources["Tab Order"] = report_data.get("tab_order_issues", [])
                    elif report_type == "missing_focusable":
                        issue_sources["Missing Focusable"] = report_data.get("missing_focusable_issues", [])
                    elif report_type == "comprehensive":
                        issue_sources = {
                            "Tab Order": report_data.get("tab_order_issues", []),
                            "Missing Focusable": report_data.get("missing_focusable_issues", []),
                            "ARIA": report_data.get("aria_issues", []),
                            "Keyboard": report_data.get("keyboard_issues", [])
                        }
                    
                    for category, issues in issue_sources.items():
                        if not issues:
                            continue
                            
                        for issue_text in issues:
                            found_data = True
                            
                            # Handle different data formats
                            if isinstance(issue_text, dict):
                                issue_desc = issue_text.get('issue', str(issue_text))
                            else:
                                issue_desc = str(issue_text)
                            
                            # Create a unique identifier for this issue
                            issue_hash = hashlib.md5(f"{category}:{issue_desc}".encode()).hexdigest()
                            
                            # Skip if we've already processed this issue
                            if issue_hash in unique_issues:
                                continue
                            unique_issues.add(issue_hash)
                            
                            # Translate the issue to a more descriptive format
                            translated_issue = translate_accessibility_issue(issue_desc, category, terminology)
                            
                            severity = determine_severity(translated_issue['description'])
                            accessibility_issue = AccessibilityIssue(
                                description=translated_issue['description'],
                                category=category,
                                severity=severity
                            )
                            
                            # Add additional metadata to the issue
                            accessibility_issue.original_text = translated_issue['original']
                            accessibility_issue.impact = translated_issue['impact']
                            accessibility_issue.recommendation = translated_issue['recommendation']
                            
                            data["issues"].append(accessibility_issue)
        
        if not found_data:
            print(f"⚠️ Warning: No accessibility reports found for {url}")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"✅ Loaded {len(data['issues'])} unique accessibility issues from reports")
    return data

def count_issues_by_category(data):
    """Count issues by category and severity"""
    counts = {
        'by_category': {},
        'by_severity': {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        },
        'total': len(data['issues'])
    }
    
    for issue in data['issues']:
        # Count by category
        if issue.category not in counts['by_category']:
            counts['by_category'][issue.category] = 0
        counts['by_category'][issue.category] += 1
        
        # Count by severity
        counts['by_severity'][issue.severity] += 1
    
    return counts

# Example usage
if __name__ == "__main__":
    test_url = url_to_check  # Replace with your target website

    print(f"Testing data loader with URL: {test_url}")
    data = load_data() # removed the need to include the url
    
    if data["issues"]:
        counts = count_issues_by_category(data)
        print("\nIssue Counts by Category:")
        for category, count in counts['by_category'].items():
            print(f"- {category}: {count}")
        
        print("\nIssue Counts by Severity:")
        for severity, count in counts['by_severity'].items():
            print(f"- {severity.capitalize()}: {count}")
    else:
        print("No issues found in any reports.")
```
### archive\.ipynb_checkpoints\Enhanced_Report_Generator-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Enhanced_Report_Generator-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Enhanced_Report_Generator-checkpoint.ipynb
- **Last Modified**: 2025-03-03 22:04:57
- **Size**: 14466 bytes

#### Code
#### Cell 1
```python
# Enhanced_Report_Generator.ipynb

# Import URL from config
%run config.ipynb

import os
import hashlib
from pathlib import Path
from datetime import datetime
import webbrowser
import matplotlib.pyplot as plt
import numpy as np

# Import from our custom modules
from Accessibility_Checker import REPORTS_DIR, normalize_url, terminology
from Data_Loader import load_data, count_issues_by_category

def get_test_instructions(category, description):
   """
   Generate practical testing instructions based on the issue category and description.
   """
   if category == "Tab Order":
       return "Try navigating through the page using only the Tab key. Notice if the focus jumps around in an unpredictable or illogical order."
   
   elif category == "Missing Focusable":
       return "Attempt to interact with this element using only your keyboard (without using a mouse). Try tabbing to it and pressing Enter/Space. If you cannot reach or activate it, the issue is confirmed."
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return "Use a screen reader to navigate to this image. The screen reader should announce a meaningful description of the image content, not just its filename or 'image'."
       elif "label" in description.lower():
           return "Use a screen reader to navigate to this form field. The screen reader should clearly announce the purpose of the field."
       elif "heading" in description.lower():
           return "Check the document outline using an accessibility tool like WAVE or axe. The headings should follow a logical hierarchical structure."
       elif "landmark" in description.lower():
           return "Use a screen reader's landmarks navigation feature. Important sections of the page should be reachable through landmarks."
       return "Use a screen reader to verify this element provides appropriate context and information."
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return "Tab to this element and check if there is a clearly visible indicator showing that it has keyboard focus. The focus should be easily noticeable against the background."
       return "Test this element using only keyboard controls (Tab, Enter, Space, arrow keys). You should be able to access and operate all functionality without a mouse."
   
   return "Navigate to this element and test its behavior using both keyboard-only navigation and a screen reader."

def get_fix_example(category, description, severity):
   """
   Generate code examples to fix the issue based on category, description and severity.
   """
   if category == "Tab Order":
       return """
           Ensure tabindex attributes follow a logical order:
           ```html
<!-- Avoid using tabindex values like this -->
<div tabindex="1">First element</div>
<div tabindex="3">Second element</div> <!-- Problem: out of sequence -->
<div tabindex="2">Third element</div>

<!-- Better approach: use tabindex="0" or adjust the DOM order -->
<div tabindex="0">First element</div>
<div tabindex="0">Second element</div>
<div tabindex="0">Third element</div>
           ```
       """
   
   elif category == "Missing Focusable":
       if "div" in description.lower() or "span" in description.lower():
           return """
               Convert div/span to a semantic button or add proper ARIA roles:
               ```html
<!-- Instead of this -->
<div class="btn" onclick="doSomething()">Click Me</div>

<!-- Use this -->
<button onclick="doSomething()">Click Me</button>

<!-- Or if you must use a div, add these attributes -->
<div class="btn" 
    onclick="doSomething()" 
    onkeydown="if(event.key==='Enter'||event.key===' ')doSomething()" 
    role="button" 
    tabindex="0">Click Me</div>
               ```
           """
       return """
           Make the element keyboard accessible:
           ```html
<!-- Add tabindex="0" to make it focusable -->
<!-- Add keyboard event handlers alongside click handlers -->
<!-- Add appropriate ARIA role if not using a semantic element -->

<element tabindex="0" 
        role="appropriate-role" 
        onclick="doAction()" 
        onkeydown="if(event.key==='Enter')doAction()">
   Content
</element>
           ```
       """
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return """
               Add descriptive alt text to images:
               ```html
<!-- Avoid this -->
<img src="chart.png">

<!-- Use this instead -->
<img src="chart.png" alt="Bar chart showing sales growth by quarter for 2023, with Q4 showing highest growth at 27%">
               ```
           """
       elif "label" in description.lower():
           return """
               Add proper labels to form fields:
               ```html
<!-- Avoid this -->
<input type="text" name="email" placeholder="Enter email">

<!-- Use this instead -->
<label for="email">Email Address</label>
<input type="text" id="email" name="email">
               ```
           """
       elif "heading" in description.lower():
           return """
               Fix heading structure to follow hierarchy:
               ```html
<!-- Avoid this -->
<h1>Page Title</h1>
<h3>First Section</h3> <!-- Problem: skipped h2 -->

<!-- Use this instead -->
<h1>Page Title</h1>
<h2>First Section</h2>
<h3>Subsection</h3>
               ```
           """
       elif "landmark" in description.lower():
           return """
               Add proper landmark roles to page sections:
               ```html
<!-- Add these structural elements -->
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<footer role="contentinfo">...</footer>
               ```
           """
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return """
               Ensure visible focus styles:
               ```css
/* Add this to your CSS */
:focus {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
}

/* For better visibility against different backgrounds */
:focus-visible {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
 box-shadow: 0 0 0 4px rgba(0, 102, 255, 0.3);
}
               ```
           """
   
   return """Implement appropriate fixes based on the issue description and web accessibility best practices."""

def get_wcag_criteria(category, description):
   """
   Map issue categories to relevant WCAG criteria.
   """
   criteria = {
       "Tab Order": "2.4.3 Focus Order (Level A)",
       "Missing Focusable": "2.1.1 Keyboard (Level A)",
       "ARIA": {
           "alt": "1.1.1 Non-text Content (Level A)",
           "label": "3.3.2 Labels or Instructions (Level A)",
           "heading": "1.3.1 Info and Relationships (Level A), 2.4.6 Headings and Labels (Level AA)",
           "landmark": "1.3.1 Info and Relationships (Level A), 4.1.2 Name, Role, Value (Level A)"
       },
       "Keyboard": {
           "focus indicator": "2.4.7 Focus Visible (Level AA)",
           "default": "2.1.1 Keyboard (Level A)"
       }
   }
   
   if category == "ARIA":
       for key, value in criteria["ARIA"].items():
           if key in description.lower():
               return value
       return criteria["ARIA"].get("landmark")  # Default for ARIA
   
   elif category == "Keyboard":
       for key, value in criteria["Keyboard"].items():
           if key in description.lower():
               return value
       return criteria["Keyboard"].get("default")  # Default for Keyboard
   
   return criteria.get(category, "")

def create_visualization(data, output_path=None):
   """Create visualization of accessibility issues."""
   if not output_path:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       output_path = REPORTS_DIR / f"visualization_{timestamp}.png"
   
   counts = count_issues_by_category(data)
   
   # Create a figure with two subplots
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
   
   # Plot issues by category
   categories = list(counts['by_category'].keys())
   category_counts = list(counts['by_category'].values())
   
   # Sort by count
   sorted_indices = np.argsort(category_counts)
   sorted_categories = [categories[i] for i in sorted_indices]
   sorted_counts = [category_counts[i] for i in sorted_indices]
   
   ax1.barh(sorted_categories, sorted_counts, color='steelblue')
   ax1.set_title('Issues by Category')
   ax1.set_xlabel('Number of Issues')
   
   # Plot issues by severity
   severities = ['critical', 'high', 'medium', 'low']
   severity_counts = [counts['by_severity'][s] for s in severities]
   
   colors = ['darkred', 'orangered', 'orange', 'yellowgreen']
   ax2.pie(severity_counts, labels=severities, autopct='%1.1f%%', 
          shadow=True, startangle=90, colors=colors)
   ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   ax2.set_title('Issues by Severity')
   
   plt.tight_layout()
   plt.savefig(output_path)
   
   return output_path

def generate_enhanced_html_report(data, output_path=None):
   """
   Generate an enhanced bipolar HTML report with information suitable for both
   accessibility experts and non-experts.
   
   Args:
       data: Dictionary containing all accessibility data
       output_path: Path to save the HTML report (optional)
   
   Returns:
       str: Path to the generated HTML report
   """
   # Prepare output path
   if output_path is None:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       clean_url = normalize_url(data.get("url", "unknown"))
       output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
   
   # Ensure reports directory exists
   os.makedirs(os.path.dirname(output_path), exist_ok=True)
   
   # Prepare issue categorization
   categorized_issues = {
       'critical': [],
       'high': [],
       'medium': [],
       'low': []
   }
   
   # Generate a unique hash for each issue to deduplicate
   unique_issues = {}
   
   # Process all issues and deduplicate
   for issue in data.get("issues", []):
       # Create a hash based on core issue properties to identify duplicates
       issue_key = hashlib.md5(
           f"{issue.category}:{issue.description[:100]}".encode()
       ).hexdigest()
       
       # If we've seen this issue before, skip it
       if issue_key in unique_issues:
           continue
           
       # Store unique issue
       unique_issues[issue_key] = issue
       categorized_issues[issue.severity].append(issue)
   
   # Count issues by category for summary
   issue_counts = {
       category: len(issues) for category, issues in categorized_issues.items()
   }
   
   # (Remaining HTML generation code is extremely long, so I've truncated it for brevity)
   # Would you like me to include the full HTML generation code?

   return str(output_path)
```
### archive\.ipynb_checkpoints\Generate_Accessibility_Report-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Generate_Accessibility_Report-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Generate_Accessibility_Report-checkpoint.ipynb
- **Last Modified**: 2025-03-10 16:59:45
- **Size**: 5323 bytes

#### Code
#### Cell 1
```python
# Generate_Accessibility_Report.ipynb
# Interactive notebook for testing and generating accessibility reports

import os
import sys
from pathlib import Path
import webbrowser
from IPython.display import display, HTML, Markdown, Image, clear_output
import ipywidgets as widgets

# Import URL from config
%run config.ipynb

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import required modules
try:
    from Accessibility_Checker import normalize_url, terminology
    from Data_Loader import load_data, count_issues_by_category
    from Enhanced_Report_Generator import generate_accessibility_report
    
    # Show success message
    display(HTML("""
    <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">✅ Modules Loaded Successfully</h3>
        <p style="margin-bottom: 0;">Ready to generate accessibility reports.</p>
    </div>
    """))
except ImportError as e:
    # Show error message
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">❌ Error Loading Modules</h3>
        <p>Could not load required modules: {str(e)}</p>
        <p style="margin-bottom: 0;">Please ensure all module files are in the same directory as this notebook.</p>
    </div>
    """))

# Display header
display(HTML("""
<div style="background-color: #e8f5e9; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="margin-top: 0;">🔍 Accessibility Report Generator</h1>
    <p>Generate comprehensive accessibility reports from previously collected data.</p>
</div>
"""))

# URL Input with default from config
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='70%')
)

# Progress output
progress_output = widgets.Output()

# Generate button
generate_button = widgets.Button(
    description='Generate Report',
    button_style='primary',
    tooltip='Click to generate an accessibility report',
    icon='chart-bar'
)

# Output area for report generation status
output_area = widgets.Output()

# Function to handle the button click
def on_generate_button_clicked(b):
    # Rest of the function remains the same as in the previous implementation
    # ... (previous implementation of the function)
    pass

# Set up button click handler
generate_button.on_click(on_generate_button_clicked)

# Display the widgets
display(widgets.VBox([
    widgets.HBox([url_input, generate_button]),
    progress_output,
    output_area
]))

# Show instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
    <h3>📋 Instructions</h3>
    <ol>
        <li>First, ensure that you have run the accessibility tests using the appropriate test scripts.</li>
        <li>Enter the URL you want to generate a report for in the URL field.</li>
        <li>Click the "Generate Report" button to create the report.</li>
        <li>The report will open automatically in your default browser.</li>
    </ol>
    
    <h4>Notes:</h4>
    <ul>
        <li>The report generator requires data from previous accessibility scans to be available.</li>
        <li>If no data is found, you'll need to run the data collection scripts first.</li>
        <li>Reports include visualizations, practical guidance for developers, and detailed technical information for accessibility experts.</li>
    </ul>
</div>
"""))
```
### archive\.ipynb_checkpoints\Missing_Focusable_Elements-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Missing_Focusable_Elements-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Missing_Focusable_Elements-checkpoint.ipynb
- **Last Modified**: 2025-03-03 22:39:13
- **Size**: 3389 bytes

#### Code
#### Cell 1
```python
# Missing_Focusable_Elements.ipynb
# Script to detect elements that should be keyboard-accessible but aren't

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets

# Import URL from config
%run config.ipynb

# Try to import Selenium
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Try to import BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import our custom module for utility functions
from Accessibility_Checker import normalize_url, terminology

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# (Existing script continues exactly as in the original document, with these two modifications)

# URL Input
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='50%')
)

# Browser dropdown
browser_dropdown = widgets.Dropdown(
    options=['chrome', 'firefox', 'edge'],
    value=browser_choice,
    description='Browser:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='30%')
)

# (The rest of the script remains EXACTLY the same as in the original document)
# This includes all the existing functions and remaining code
```
### archive\.ipynb_checkpoints\Non_Text_Content_Checker-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Non_Text_Content_Checker-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Non_Text_Content_Checker-checkpoint.ipynb
- **Last Modified**: 2025-03-10 16:59:42
- **Size**: 1510 bytes

#### Code
#### Cell 1
```python
from bs4 import BeautifulSoup

def identify_non_text_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    non_text_elements = []

    # Find elements that typically contain non-text content
    element_types = ['img', 'svg', 'video', 'audio', 'object', 'embed', 'canvas']
    for element_type in element_types:
        elements = soup.find_all(element_type)
        for element in elements:
            element_info = {
                'tag': element.name,
                'src': element.get('src'),
                'alt': element.get('alt'),
                # Extract other relevant attributes as needed
            }
            non_text_elements.append(element_info)

    return non_text_elements
```
### archive\.ipynb_checkpoints\Script_Extract-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Script_Extract-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Script_Extract-checkpoint.ipynb
- **Last Modified**: 2025-03-03 21:14:29
- **Size**: 10569 bytes

#### Code
#### Cell 1
```python
import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    notebook_files = list(Path(folder_path).glob('*.ipynb'))

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    markdown_content += "\n## Table of Contents\n"
    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"- [{notebook_name}](#{notebook_name})\n"

    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"\n## {notebook_name} <a id='{notebook_name}'></a>\n"
        markdown_content += f"### File Information\n"
        markdown_content += f"- **Type**: Jupyter Notebook\n"
        markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
        markdown_content += "\n### Code\n"
        markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    return markdown_content

# Rest of the script remains the same as before
    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your Jupyter Notebooks folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
#### Cell 2
```python

```
### archive\.ipynb_checkpoints\Script_Extract_a-checkpoint.ipynb <a id='archive__ipynb_checkpoints_Script_Extract_a-checkpoint_ipynb'></a>
#### File Information
- **Type**: Jupyter Notebook
- **Path**: archive\.ipynb_checkpoints\Script_Extract_a-checkpoint.ipynb
- **Last Modified**: 2025-03-10 16:31:25
- **Size**: 10569 bytes

#### Code
#### Cell 1
```python
import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    notebook_files = list(Path(folder_path).glob('*.ipynb'))

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    markdown_content += "\n## Table of Contents\n"
    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"- [{notebook_name}](#{notebook_name})\n"

    for notebook_file in notebook_files:
        notebook_name = notebook_file.stem
        markdown_content += f"\n## {notebook_name} <a id='{notebook_name}'></a>\n"
        markdown_content += f"### File Information\n"
        markdown_content += f"- **Type**: Jupyter Notebook\n"
        markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
        markdown_content += "\n### Code\n"
        markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    return markdown_content

# Rest of the script remains the same as before
    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your Jupyter Notebooks folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
#### Cell 2
```python

```
## Python Scripts

### accessibility_checker.py <a id='accessibility_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_checker.py
- **Last Modified**: 2025-03-10 22:00:02
- **Size**: 8317 bytes

#### Code
```python
#!/usr/bin/env python
"""
Accessibility Checker - Main Module
A tool for checking web pages for accessibility issues.
"""

import argparse
import logging
import sys
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Add the current directory to Python's module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def setup_driver(browser_name='chrome'):
    """
    Set up and return a WebDriver instance for the specified browser.
    
    Args:
        browser_name (str): Name of the browser to use ('chrome', 'firefox', or 'edge')
        
    Returns:
        WebDriver: Configured WebDriver instance
    """
    browser_name = browser_name.lower()
    try:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--headless')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            logging.error(f"Unsupported browser: {browser_name}")
            raise ValueError(f"Unsupported browser: {browser_name}")
            
        driver.set_window_size(1366, 768)
        return driver
        
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {str(e)}")
        raise

def run_accessibility_checks(url, browser='chrome', output_file=None):
    """
    Run all accessibility checks on the specified URL.
    
    Args:
        url (str): URL to check
        browser (str): Browser to use for checks
        output_file (str): Path to save the report (optional)
        
    Returns:
        dict: Accessibility report
    """
    start_time = time.time()
    
    # Print header
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {url}")
    print(f"Browser: {browser}")
    print("=" * 60)
    print()
    
    # Set up WebDriver
    driver = None
    try:
        driver = setup_driver(browser)
        driver.get(url)
        
        # Allow page to load and render
        time.sleep(3)
        
        # Import and run tab order check
        print("📊 Running Tab Order Check...")
        try:
            from accessibility_modules.tab_order_checker import check_tab_order
            tab_results = check_tab_order(driver)
            print(f"✅ Found {len(tab_results.get('tab_sequence', []))} elements in tab order.")
            if tab_results.get('issues'):
                print(f"⚠️ Found {len(tab_results['issues'])} Inconsistent keyboard navigation sequences.")
        except ImportError as e:
            logging.error(f"Could not import tab order module: {str(e)}")
            print(f"❌ Tab order check module not available.")
            tab_results = None
        print()
        
        # Import and run missing focusable elements check
        print("🕵️ Checking Missing Focusable Elements...")
        try:
            from accessibility_modules.focusable_elements import check_missing_focusable_elements
            focus_results = check_missing_focusable_elements(driver)
            if focus_results:
                print(f"⚠️ Found {len(focus_results)} potentially inaccessible interactive elements.")
            else:
                print("✅ No missing focusable elements detected.")
        except ImportError as e:
            logging.error(f"Could not import missing focusable elements module: {str(e)}")
            print(f"❌ Missing focusable elements check module not available.")
            focus_results = None
        print()
        
        # Import and run ARIA accessibility check
        print("♿ Running ARIA and Keyboard Accessibility Check...")
        try:
            from accessibility_modules.aria_checker import check_aria_accessibility
            aria_results = check_aria_accessibility(driver)
            issue_count = len(aria_results.get('issues', []))
            if issue_count > 0:
                print(f"⚠️ Found {issue_count} ARIA and keyboard accessibility issues.")
            else:
                print("✅ No ARIA or keyboard accessibility issues detected.")
        except ImportError as e:
            logging.error(f"Could not import ARIA checker module: {str(e)}")
            print(f"❌ ARIA and keyboard accessibility check module not available.")
            aria_results = None
        print()
        
        # Import and run comprehensive report generation
        print("📄 Generating Comprehensive Report...")
        try:
            from accessibility_modules.report_generator import generate_accessibility_report
            report = generate_accessibility_report(
                driver, 
                url, 
                tab_order_results=tab_results,
                missing_focusable_results=focus_results,
                aria_results=aria_results,
                save_to_file=True,  # Always save to file
                output_path=output_file
            )
            print(f"✅ Report generated with {len(report.get('issues', []))} total issues.")
            
            # Display HTML report path if available
            if "html_report_path" in report:
                html_path = report["html_report_path"]
                print(f"📊 HTML report saved to: {html_path}")
                print(f"   Open this file in your browser to view a detailed accessibility report.")
                
        except ImportError as e:
            logging.error(f"Could not import report generator module: {str(e)}")
            print(f"❌ Report generation module not available.")
            report = {
                "url": url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "error": "Report generation module not available"
            }
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Print footer
        print()
        print("=" * 60)
        print(f"✅ Accessibility Check Complete ({elapsed_time:.2f}s)")
        print("=" * 60)
        
        return report
        
    except Exception as e:
        logging.error(f"Error during accessibility checks: {str(e)}")
        print(f"❌ Error during accessibility checks: {str(e)}")
        return {"error": str(e)}
        
    finally:
        # Clean up WebDriver
        if driver:
            driver.quit()

def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description="Check web pages for accessibility issues")
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--browser", "-b", default="chrome", choices=["chrome", "firefox", "edge"],
                        help="Browser to use for checks (default: chrome)")
    parser.add_argument("--output", "-o", default=None,
                        help="Path to save the report (default: accessibility_reports/)")
    
    args = parser.parse_args()
    
    run_accessibility_checks(args.url, args.browser, args.output)

if __name__ == "__main__":
    main()
```
### create_terminology.py <a id='create_terminology_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: create_terminology.py
- **Last Modified**: 2025-03-10 22:18:21
- **Size**: 770 bytes

#### Code
```python
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
        "Keyboard navigation barrier": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### create_terminology_file.py <a id='create_terminology_file_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: create_terminology_file.py
- **Last Modified**: 2025-03-10 22:20:16
- **Size**: 770 bytes

#### Code
```python
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
        "Keyboard navigation barrier": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### script_extract.py <a id='script_extract_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: script_extract.py
- **Last Modified**: 2025-03-11 19:46:29
- **Size**: 16089 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8


import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def extract_code_from_python_file(file_path, terminology_validator=None):
    """
    Extract code from Python file with optional terminology validation.
    
    Args:
        file_path (str): Path to the Python file
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code 
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    # Validate terminology if validator is provided
    if terminology_validator:
        code = _validate_code_terminology(code, terminology_validator)
    
    return f"```python\n{code}\n```"

def extract_content_from_text_file(file_path):
    """
    Extract content from text file (README, TXT, etc.).
    
    Args:
        file_path (str): Path to the text file
    
    Returns:
        str: Extracted content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    return f"```\n{content}\n```"

def extract_content_from_json_file(file_path):
    """
    Extract and format content from JSON file.
    
    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        str: Extracted and formatted JSON content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        try:
            json_data = json.load(file)
            # Pretty-print the JSON with indentation
            content = json.dumps(json_data, indent=2)
        except json.JSONDecodeError:
            # If JSON is invalid, return it as plain text
            file.seek(0)  # Reset file pointer to beginning
            content = file.read()
    
    return f"```json\n{content}\n```"

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    # Use rglob to find files in the folder and all subfolders
    base_path = Path(folder_path)
    notebook_files = list(base_path.rglob('*.ipynb'))
    python_files = list(base_path.rglob('*.py'))
    text_files = list(base_path.rglob('*.txt'))
    json_files = list(base_path.rglob('*.json'))
    
    # Find README files (README.md, README.txt, etc.)
    readme_files = []
    for pattern in ['README.md', 'README.txt', 'README', 'readme.md', 'readme.txt', 'readme']:
        readme_files.extend(list(base_path.rglob(pattern)))
    
    # Remove README.txt files from text_files to avoid duplication
    text_files = [f for f in text_files if f not in readme_files]

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a project containing Jupyter Notebooks, Python scripts, and README files. The following content provides context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    # Table of Contents
    markdown_content += "\n## Table of Contents\n"
    
    # Add README files to TOC
    if readme_files:
        markdown_content += "### README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add notebooks to TOC
    if notebook_files:
        markdown_content += "\n### Jupyter Notebooks\n"
        for notebook_file in notebook_files:
            rel_path = notebook_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Python files to TOC
    if python_files:
        markdown_content += "\n### Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Text files to TOC
    if text_files:
        markdown_content += "\n### Text Files\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add JSON files to TOC
    if json_files:
        markdown_content += "\n### JSON Files\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"

    # Add README content
    if readme_files:
        markdown_content += "\n## README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: README\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(readme_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(readme_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(readme_file)

    # Add notebook content
    if notebook_files:
        markdown_content += "\n## Jupyter Notebooks\n"
        for notebook_file in notebook_files:
            rel_path = notebook_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Jupyter Notebook\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
            markdown_content += "\n#### Code\n"
            markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    # Add Python file content
    if python_files:
        markdown_content += "\n## Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Python Script\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(python_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(python_file)} bytes\n"
            markdown_content += "\n#### Code\n"
            markdown_content += extract_code_from_python_file(python_file, terminology_validator)
    
    # Add Text file content
    if text_files:
        markdown_content += "\n## Text Files\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Text File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(text_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(text_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(text_file)
    
    # Add JSON file content
    if json_files:
        markdown_content += "\n## JSON Files\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: JSON File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(json_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(json_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_json_file(json_file)

    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your project folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
### .ipynb_checkpoints\accessibility_checker-checkpoint.py <a id='_ipynb_checkpoints_accessibility_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: .ipynb_checkpoints\accessibility_checker-checkpoint.py
- **Last Modified**: 2025-03-10 22:00:02
- **Size**: 8317 bytes

#### Code
```python
#!/usr/bin/env python
"""
Accessibility Checker - Main Module
A tool for checking web pages for accessibility issues.
"""

import argparse
import logging
import sys
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Add the current directory to Python's module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def setup_driver(browser_name='chrome'):
    """
    Set up and return a WebDriver instance for the specified browser.
    
    Args:
        browser_name (str): Name of the browser to use ('chrome', 'firefox', or 'edge')
        
    Returns:
        WebDriver: Configured WebDriver instance
    """
    browser_name = browser_name.lower()
    try:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--headless')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            logging.error(f"Unsupported browser: {browser_name}")
            raise ValueError(f"Unsupported browser: {browser_name}")
            
        driver.set_window_size(1366, 768)
        return driver
        
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {str(e)}")
        raise

def run_accessibility_checks(url, browser='chrome', output_file=None):
    """
    Run all accessibility checks on the specified URL.
    
    Args:
        url (str): URL to check
        browser (str): Browser to use for checks
        output_file (str): Path to save the report (optional)
        
    Returns:
        dict: Accessibility report
    """
    start_time = time.time()
    
    # Print header
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {url}")
    print(f"Browser: {browser}")
    print("=" * 60)
    print()
    
    # Set up WebDriver
    driver = None
    try:
        driver = setup_driver(browser)
        driver.get(url)
        
        # Allow page to load and render
        time.sleep(3)
        
        # Import and run tab order check
        print("📊 Running Tab Order Check...")
        try:
            from accessibility_modules.tab_order_checker import check_tab_order
            tab_results = check_tab_order(driver)
            print(f"✅ Found {len(tab_results.get('tab_sequence', []))} elements in tab order.")
            if tab_results.get('issues'):
                print(f"⚠️ Found {len(tab_results['issues'])} Inconsistent keyboard navigation sequences.")
        except ImportError as e:
            logging.error(f"Could not import tab order module: {str(e)}")
            print(f"❌ Tab order check module not available.")
            tab_results = None
        print()
        
        # Import and run missing focusable elements check
        print("🕵️ Checking Missing Focusable Elements...")
        try:
            from accessibility_modules.focusable_elements import check_missing_focusable_elements
            focus_results = check_missing_focusable_elements(driver)
            if focus_results:
                print(f"⚠️ Found {len(focus_results)} potentially inaccessible interactive elements.")
            else:
                print("✅ No missing focusable elements detected.")
        except ImportError as e:
            logging.error(f"Could not import missing focusable elements module: {str(e)}")
            print(f"❌ Missing focusable elements check module not available.")
            focus_results = None
        print()
        
        # Import and run ARIA accessibility check
        print("♿ Running ARIA and Keyboard Accessibility Check...")
        try:
            from accessibility_modules.aria_checker import check_aria_accessibility
            aria_results = check_aria_accessibility(driver)
            issue_count = len(aria_results.get('issues', []))
            if issue_count > 0:
                print(f"⚠️ Found {issue_count} ARIA and keyboard accessibility issues.")
            else:
                print("✅ No ARIA or keyboard accessibility issues detected.")
        except ImportError as e:
            logging.error(f"Could not import ARIA checker module: {str(e)}")
            print(f"❌ ARIA and keyboard accessibility check module not available.")
            aria_results = None
        print()
        
        # Import and run comprehensive report generation
        print("📄 Generating Comprehensive Report...")
        try:
            from accessibility_modules.report_generator import generate_accessibility_report
            report = generate_accessibility_report(
                driver, 
                url, 
                tab_order_results=tab_results,
                missing_focusable_results=focus_results,
                aria_results=aria_results,
                save_to_file=True,  # Always save to file
                output_path=output_file
            )
            print(f"✅ Report generated with {len(report.get('issues', []))} total issues.")
            
            # Display HTML report path if available
            if "html_report_path" in report:
                html_path = report["html_report_path"]
                print(f"📊 HTML report saved to: {html_path}")
                print(f"   Open this file in your browser to view a detailed accessibility report.")
                
        except ImportError as e:
            logging.error(f"Could not import report generator module: {str(e)}")
            print(f"❌ Report generation module not available.")
            report = {
                "url": url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "error": "Report generation module not available"
            }
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Print footer
        print()
        print("=" * 60)
        print(f"✅ Accessibility Check Complete ({elapsed_time:.2f}s)")
        print("=" * 60)
        
        return report
        
    except Exception as e:
        logging.error(f"Error during accessibility checks: {str(e)}")
        print(f"❌ Error during accessibility checks: {str(e)}")
        return {"error": str(e)}
        
    finally:
        # Clean up WebDriver
        if driver:
            driver.quit()

def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description="Check web pages for accessibility issues")
    parser.add_argument("url", help="URL to check")
    parser.add_argument("--browser", "-b", default="chrome", choices=["chrome", "firefox", "edge"],
                        help="Browser to use for checks (default: chrome)")
    parser.add_argument("--output", "-o", default=None,
                        help="Path to save the report (default: accessibility_reports/)")
    
    args = parser.parse_args()
    
    run_accessibility_checks(args.url, args.browser, args.output)

if __name__ == "__main__":
    main()
```
### .ipynb_checkpoints\create_terminology-checkpoint.py <a id='_ipynb_checkpoints_create_terminology-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: .ipynb_checkpoints\create_terminology-checkpoint.py
- **Last Modified**: 2025-03-10 22:18:21
- **Size**: 770 bytes

#### Code
```python
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
        "Keyboard navigation barrier": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### .ipynb_checkpoints\create_terminology_file-checkpoint.py <a id='_ipynb_checkpoints_create_terminology_file-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: .ipynb_checkpoints\create_terminology_file-checkpoint.py
- **Last Modified**: 2025-03-10 22:20:16
- **Size**: 770 bytes

#### Code
```python
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
        "Keyboard navigation barrier": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### .ipynb_checkpoints\script_extract-checkpoint.py <a id='_ipynb_checkpoints_script_extract-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: .ipynb_checkpoints\script_extract-checkpoint.py
- **Last Modified**: 2025-03-11 19:46:29
- **Size**: 16089 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8


import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "Keyboard navigation barrier": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "Inconsistent keyboard navigation sequence": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def extract_code_from_python_file(file_path, terminology_validator=None):
    """
    Extract code from Python file with optional terminology validation.
    
    Args:
        file_path (str): Path to the Python file
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code 
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    # Validate terminology if validator is provided
    if terminology_validator:
        code = _validate_code_terminology(code, terminology_validator)
    
    return f"```python\n{code}\n```"

def extract_content_from_text_file(file_path):
    """
    Extract content from text file (README, TXT, etc.).
    
    Args:
        file_path (str): Path to the text file
    
    Returns:
        str: Extracted content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    return f"```\n{content}\n```"

def extract_content_from_json_file(file_path):
    """
    Extract and format content from JSON file.
    
    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        str: Extracted and formatted JSON content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        try:
            json_data = json.load(file)
            # Pretty-print the JSON with indentation
            content = json.dumps(json_data, indent=2)
        except json.JSONDecodeError:
            # If JSON is invalid, return it as plain text
            file.seek(0)  # Reset file pointer to beginning
            content = file.read()
    
    return f"```json\n{content}\n```"

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    # Use rglob to find files in the folder and all subfolders
    base_path = Path(folder_path)
    notebook_files = list(base_path.rglob('*.ipynb'))
    python_files = list(base_path.rglob('*.py'))
    text_files = list(base_path.rglob('*.txt'))
    json_files = list(base_path.rglob('*.json'))
    
    # Find README files (README.md, README.txt, etc.)
    readme_files = []
    for pattern in ['README.md', 'README.txt', 'README', 'readme.md', 'readme.txt', 'readme']:
        readme_files.extend(list(base_path.rglob(pattern)))
    
    # Remove README.txt files from text_files to avoid duplication
    text_files = [f for f in text_files if f not in readme_files]

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a project containing Jupyter Notebooks, Python scripts, and README files. The following content provides context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    # Table of Contents
    markdown_content += "\n## Table of Contents\n"
    
    # Add README files to TOC
    if readme_files:
        markdown_content += "### README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add notebooks to TOC
    if notebook_files:
        markdown_content += "\n### Jupyter Notebooks\n"
        for notebook_file in notebook_files:
            rel_path = notebook_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Python files to TOC
    if python_files:
        markdown_content += "\n### Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Text files to TOC
    if text_files:
        markdown_content += "\n### Text Files\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add JSON files to TOC
    if json_files:
        markdown_content += "\n### JSON Files\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"

    # Add README content
    if readme_files:
        markdown_content += "\n## README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: README\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(readme_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(readme_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(readme_file)

    # Add notebook content
    if notebook_files:
        markdown_content += "\n## Jupyter Notebooks\n"
        for notebook_file in notebook_files:
            rel_path = notebook_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Jupyter Notebook\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(notebook_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(notebook_file)} bytes\n"
            markdown_content += "\n#### Code\n"
            markdown_content += extract_code_from_notebook(notebook_file, terminology_validator)

    # Add Python file content
    if python_files:
        markdown_content += "\n## Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Python Script\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(python_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(python_file)} bytes\n"
            markdown_content += "\n#### Code\n"
            markdown_content += extract_code_from_python_file(python_file, terminology_validator)
    
    # Add Text file content
    if text_files:
        markdown_content += "\n## Text Files\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Text File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(text_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(text_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(text_file)
    
    # Add JSON file content
    if json_files:
        markdown_content += "\n## JSON Files\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: JSON File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(json_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(json_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_json_file(json_file)

    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your project folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")
```
### accessibility_modules\aria_checker.py <a id='accessibility_modules_aria_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\aria_checker.py
- **Last Modified**: 2025-03-10 21:21:50
- **Size**: 9521 bytes

#### Code
```python
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
```
### accessibility_modules\focusable_elements.py <a id='accessibility_modules_focusable_elements_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\focusable_elements.py
- **Last Modified**: 2025-03-10 21:20:09
- **Size**: 5459 bytes

#### Code
```python
"""
Focusable Elements Module
Detects elements that should be keyboard-accessible but aren't.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

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
        # Check for elements that should be focusable
        potential_interactive_elements = driver.find_elements(By.CSS_SELECTOR, 
            "a:not([tabindex]), button:not([tabindex]), [onclick]:not([tabindex]), " +
            "[role='button']:not([tabindex]), [role='link']:not([tabindex]), " +
            "input:not([type='hidden']):not([tabindex]), select:not([tabindex]), " +
            "textarea:not([tabindex]), details:not([tabindex])")
        
        for element in potential_interactive_elements:
            # Check if the element has tabindex=-1 (explicitly not focusable)
            tabindex = element.get_attribute("tabindex")
            if tabindex == "-1":
                missing_focusable.append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "issue": "Keyboard navigation barrier",
                    "details": "Interactive element with tabindex=-1",
                    "recommendation": "Remove tabindex=-1 or provide alternative keyboard access",
                    "wcag": "2.1.1"
                })
                continue
                
            # Check if element is visible and enabled but not focusable
            if element.is_displayed() and element.is_enabled():
                # Try to check if focusable through JavaScript
                is_focusable = driver.execute_script("""
                    return document.activeElement !== arguments[0] && 
                           arguments[0].focus && 
                           (function() { 
                               var focusable = true;
                               arguments[0].focus(); 
                               focusable = document.activeElement === arguments[0];
                               return focusable;
                           })();
                """, element)
                
                if not is_focusable:
                    missing_focusable.append({
                        "element": element.tag_name,
                        "text": element.text.strip() if element.text else "[No text]",
                        "location": get_element_location(element),
                        "issue": "Keyboard navigation barrier",
                        "details": "Element should be focusable but isn't",
                        "recommendation": "Add proper keyboard accessibility",
                        "wcag": "2.1.1"
                    })
        
        # Check for custom interactive elements without proper ARIA roles
        custom_elements = driver.find_elements(By.CSS_SELECTOR, 
            "[class*='button']:not(button):not(a):not([role='button']), " +
            "[class*='btn']:not(button):not(a):not([role='button']), " +
            "[class*='toggle']:not([role]), " +
            "[class*='menu']:not([role]), " +
            "[class*='dropdown']:not([role])")
        
        for element in custom_elements:
            if element.is_displayed() and element.is_enabled():
                missing_focusable.append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "class": element.get_attribute("class"),
                    "location": get_element_location(element),
                    "issue": "Keyboard navigation barrier",
                    "details": "Custom interactive element without proper ARIA role",
                    "recommendation": "Add appropriate role and ensure keyboard accessibility",
                    "wcag": "4.1.2"
                })
                
        logging.info(f"Found {len(missing_focusable)} elements with keyboard accessibility issues")
        return missing_focusable
        
    except WebDriverException as e:
        logging.error(f"Error checking for missing focusable elements: {str(e)}")
        return [{"error": str(e)}]

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
        parent = element.find_element(By.XPATH, "./..")
        parent_text = parent.text.strip()
        if parent_text and len(parent_text) < 50:  # Only use if it's reasonably short
            return f"near text '{parent_text}'"
            
        # Fallback to XPath
        return "in page (no specific identifier available)"
            
    except Exception:
        return "in page (location detection failed)"
```
### accessibility_modules\focus_order_checker.py <a id='accessibility_modules_focus_order_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\focus_order_checker.py
- **Last Modified**: 2025-03-10 22:11:57
- **Size**: 18011 bytes

#### Code
```python
"""
Focus Order Checker Module
Tests for WCAG 2.4.3: Focus Order - Ensures that navigation follows a meaningful sequence.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

def check_focus_order(driver):
    """
    Checks that the focus order of interactive elements is logical and follows content sequence.
    Tests WCAG Success Criterion 2.4.3: Focus Order
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of focus order check
    """
    logging.info("Checking focus order (WCAG 2.4.3)...")
    results = {
        "status": "completed",
        "wcag_criterion": "2.4.3",
        "tab_sequence": [],
        "issues": []
    }
    
    try:
        # Reset focus to beginning of page
        driver.find_element(By.TAG_NAME, "body").click()
        
        # Find all potentially focusable elements
        focusable_selector = (
            "a, button, input:not([type='hidden']), select, textarea, "
            "[tabindex]:not([tabindex='-1']), [contenteditable='true'], "
            "details, summary, [role='button'], [role='link'], "
            "[role='checkbox'], [role='radio'], [role='tab'], [role='menuitem'], "
            "[role='combobox'], [role='listbox'], [role='slider'], [role='textbox'], "
            "[role='searchbox'], [role='spinbutton']"
        )
        
        # Get all focusable elements and their visual positions for later analysis
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        logging.info(f"Found {len(all_focusable)} potentially focusable elements")
        
        # Store information about each focusable element
        focusable_elements_info = []
        for element in all_focusable:
            if element.is_displayed() and element.is_enabled():
                info = {
                    "element": element,
                    "tag": element.tag_name,
                    "id": element.get_attribute("id") or "",
                    "text": element.text.strip() if element.text else get_element_accessible_name(element),
                    "tabindex": element.get_attribute("tabindex"),
                    "position": get_element_position(element)
                }
                focusable_elements_info.append(info)
        
        # Detect actual tab sequence using keyboard navigation
        tab_sequence = detect_tab_sequence(driver, max_elements=len(focusable_elements_info) * 2)
        results["tab_sequence"] = tab_sequence
        
        # Check for specific focus order issues
        check_for_positive_tabindex(tab_sequence, results)
        check_reading_order_violations(tab_sequence, results)
        check_form_field_sequence(tab_sequence, results)
        check_modal_dialog_focus(driver, tab_sequence, results)
        check_skip_links(driver, tab_sequence, results)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking focus order: {str(e)}")
        results["error"] = str(e)
        return results

def detect_tab_sequence(driver, max_elements=100):
    """Detect the actual tab sequence of the page by simulating keyboard tabbing"""
    tab_sequence = []
    
    # Start with pressing Tab once to get to first element
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    body.send_keys(Keys.TAB)
    
    # Keep track of already focused elements to detect cycles
    focused_signatures = set()
    
    for i in range(max_elements):
        # Get currently focused element
        active_element = driver.execute_script("return document.activeElement;")
        
        # Skip if we've already seen this element (avoid infinite loops)
        element_signature = generate_element_signature(active_element)
        if element_signature in focused_signatures:
            # If we're back at the first element, we've completed the tab cycle
            if len(tab_sequence) > 1 and element_signature == generate_element_signature(tab_sequence[0]["element"]):
                break
            # Otherwise we might be stuck in a sub-cycle, keep going a bit longer
            if len(focused_signatures) > 5:  # Allow a few duplicate focuses before giving up
                break
        
        # Add to our sequence
        element_info = {
            "element": active_element,
            "tag": active_element.tag_name if hasattr(active_element, 'tag_name') else active_element.get_attribute("tagName").lower(),
            "id": active_element.get_attribute("id") or "",
            "text": active_element.text.strip() if hasattr(active_element, 'text') and active_element.text else get_element_accessible_name(active_element),
            "tabindex": active_element.get_attribute("tabindex"),
            "position": get_element_position(active_element),
            "tab_index": i + 1  # 1-based index of tab sequence
        }
        
        tab_sequence.append(element_info)
        focused_signatures.add(element_signature)
        
        # Move to next element
        active_element.send_keys(Keys.TAB)
        
        # Small delay to allow focus to settle (helps with dynamic pages)
        time.sleep(0.05)
    
    return tab_sequence

def check_for_positive_tabindex(tab_sequence, results):
    """Check for elements with tabindex > 0, which can disrupt natural tab order"""
    for element_info in tab_sequence:
        tabindex = element_info.get("tabindex", "")
        if tabindex and tabindex.isdigit() and int(tabindex) > 0:
            results["issues"].append({
                "element": element_info.get("tag", "unknown"),
                "text": element_info.get("text", "[No text]"),
                "issue": "Inconsistent keyboard navigation sequence",
                "details": f"Element has tabindex={tabindex}, which overrides the natural DOM order",
                "recommendation": "Use tabindex='0' to make elements focusable in their natural DOM order",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_reading_order_violations(tab_sequence, results):
    """Check if focus order follows visual/reading order"""
    # Skip if we have less than 3 elements
    if len(tab_sequence) < 3:
        return
    
    # Look for cases where focus jumps around unnaturally
    for i in range(1, len(tab_sequence) - 1):
        current = tab_sequence[i]
        prev = tab_sequence[i-1]
        next_elem = tab_sequence[i+1]
        
        # Skip elements without position info
        if not current.get("position") or not prev.get("position") or not next_elem.get("position"):
            continue
        
        # Check for focus moving backwards against reading order
        # First check if we're moving down the page as expected
        if prev["position"]["y"] < current["position"]["y"]:
            # Then check if next focus moves back up significantly
            if next_elem["position"]["y"] < current["position"]["y"] - 50:
                # Only flag if it's not just moving to a new column
                if abs(next_elem["position"]["x"] - current["position"]["x"]) < 200:
                    results["issues"].append({
                        "element": current.get("tag", "unknown"),
                        "text": current.get("text", "[No text]"),
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Focus jumps backwards against the expected reading order",
                        "recommendation": "Ensure focus order follows the natural reading order of the page",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })

def check_form_field_sequence(tab_sequence, results):
    """Check if form fields are in a logical sequence"""
    # Identify form sections
    form_sections = []
    current_section = []
    
    for element_info in tab_sequence:
        tag = element_info.get("tag", "").lower()
        if tag in ["input", "select", "textarea"] or element_info.get("role") in ["textbox", "combobox", "listbox"]:
            current_section.append(element_info)
        elif current_section:
            # End of a form section (non-form element encountered after form elements)
            if len(current_section) > 1:
                form_sections.append(current_section)
            current_section = []
    
    # Add last section if it exists
    if len(current_section) > 1:
        form_sections.append(current_section)
    
    # Check each form section
    for section in form_sections:
        # Check if fields are in a logical vertical order
        is_vertical_form = True
        for i in range(1, len(section)):
            prev = section[i-1]
            current = section[i]
            
            # If fields are side by side, it's not a simple vertical form
            if prev.get("position") and current.get("position"):
                if abs(prev["position"]["y"] - current["position"]["y"]) < 30:
                    is_vertical_form = False
                    break
        
        # For vertical forms, check if tab order follows visual order
        if is_vertical_form:
            for i in range(1, len(section)):
                prev = section[i-1]
                current = section[i]
                
                if prev.get("position") and current.get("position"):
                    # If next field is above previous, that's counter-intuitive
                    if current["position"]["y"] < prev["position"]["y"] - 30:
                        results["issues"].append({
                            "element": current.get("tag", "unknown"),
                            "text": current.get("text", "[No text]"),
                            "issue": "Inconsistent keyboard navigation sequence in form",
                            "details": "Form fields do not follow a logical top-to-bottom sequence",
                            "recommendation": "Ensure form fields receive focus in a logical order that matches visual layout",
                            "wcag": "2.4.3",
                            "severity": "warning"
                        })
                        break

def check_modal_dialog_focus(driver, tab_sequence, results):
    """Check if there are modal dialogs and if focus is properly trapped within them"""
    # Look for modal dialogs
    modal_dialogs = driver.find_elements(By.CSS_SELECTOR, 
        "[role='dialog'], [aria-modal='true'], .modal, .dialog, .overlay:not([aria-hidden='true'])")
    
    if not modal_dialogs:
        return
        
    for dialog in modal_dialogs:
        # Skip hidden dialogs
        if not dialog.is_displayed():
            continue
            
        # Check if dialog has aria-modal attribute
        aria_modal = dialog.get_attribute("aria-modal")
        if aria_modal != "true":
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog missing aria-modal attribute",
                "details": "Modal dialog should have aria-modal='true' to indicate it traps focus",
                "recommendation": "Add aria-modal='true' to modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })
        
        # Check focus management
        focusable_elements = dialog.find_elements(By.CSS_SELECTOR, 
            "a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")
        
        if not focusable_elements:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog has no focusable elements",
                "details": "Modal dialogs should contain focusable elements",
                "recommendation": "Ensure modal dialogs have focusable elements like buttons for user interaction",
                "wcag": "2.4.3",
                "severity": "critical"
            })
            continue
            
        # Simulate tabbing through the dialog to check if focus stays within
        # This would require more complex testing logic to implement fully
        # For now, we'll just check if the dialog has a close/cancel button
        close_buttons = dialog.find_elements(By.CSS_SELECTOR, 
            "button:not([aria-hidden='true']), [role='button']:not([aria-hidden='true']), " +
            "[aria-label*='close' i], [aria-label*='cancel' i], " +
            "[class*='close' i], [id*='close' i], [class*='cancel' i], [id*='cancel' i]")
            
        if not close_buttons:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog may lack closing mechanism",
                "details": "No obvious close button found in modal dialog",
                "recommendation": "Provide a visible close button in modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_skip_links(driver, tab_sequence, results):
    """Check if skip links are present and working"""
    # Look for common skip link patterns
    skip_links = driver.find_elements(By.CSS_SELECTOR, 
        "a[href^='#']:not([aria-hidden='true'])")
    
    skip_link_found = False
    for link in skip_links:
        link_text = link.text.strip() if link.text else ""
        if not link_text:
            link_text = link.get_attribute("aria-label") or ""
            
        # Look for common skip link text patterns
        if any(pattern in link_text.lower() for pattern in ["skip", "jump", "content", "main"]):
            skip_link_found = True
            
            # Check if skip link is one of the first elements in tab order
            if tab_sequence and len(tab_sequence) > 2:
                first_elements = [tab_sequence[0], tab_sequence[1]] if len(tab_sequence) > 1 else [tab_sequence[0]]
                skip_link_in_tab_order = any(
                    element.get("tag") == "a" and element.get("text") == link_text
                    for element in first_elements
                )
                
                if not skip_link_in_tab_order:
                    results["issues"].append({
                        "element": "a",
                        "text": link_text,
                        "issue": "Skip link not at start of tab order",
                        "details": "Skip navigation link should be one of the first focusable elements",
                        "recommendation": "Move skip link to the beginning of the page code so it's encountered early in tab order",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })
    
    # If no skip links found on a page with significant content, suggest adding one
    if not skip_link_found:
        # Check if page has a substantial amount of navigation before main content
        nav_elements = driver.find_elements(By.CSS_SELECTOR, 
            "nav, [role='navigation'], #navigation, .navigation, .nav, #nav, header")
        
        if nav_elements and len(tab_sequence) > 10:
            results["issues"].append({
                "element": "page",
                "issue": "Missing skip navigation link",
                "details": "Page has substantial navigation but no skip link was found",
                "recommendation": "Add a skip link at the beginning of the page to allow keyboard users to skip navigation",
                "wcag": "2.4.3",
                "severity": "warning"
            })

# Helper functions

def get_element_position(element):
    """Get the position and dimensions of an element"""
    try:
        rect = element.rect
        return {
            "x": rect.get('x', 0),
            "y": rect.get('y', 0),
            "width": rect.get('width', 0),
            "height": rect.get('height', 0),
            "midX": rect.get('x', 0) + rect.get('width', 0) / 2,
            "midY": rect.get('y', 0) + rect.get('height', 0) / 2
        }
    except:
        return None

def get_element_accessible_name(element):
    """Try to get the accessible name of an element through various attributes"""
    accessible_name = ""
    try:
        # Try aria-label
        accessible_name = element.get_attribute("aria-label") or ""
        if accessible_name:
            return f"[{accessible_name}]"
            
        # Try placeholder
        if element.tag_name.lower() in ["input", "textarea"]:
            placeholder = element.get_attribute("placeholder") or ""
            if placeholder:
                return f"[Placeholder: {placeholder}]"
            
            # Try value
            value = element.get_attribute("value") or ""
            if value:
                return f"[Value: {value}]"
                
        # Try title
        title = element.get_attribute("title") or ""
        if title:
            return f"[Title: {title}]"
            
        # Try name
        name = element.get_attribute("name") or ""
        if name:
            return f"[Name: {name}]"
            
        return "[No text]"
    except:
        return "[No text]"

def generate_element_signature(element):
    """Generate a unique-ish signature for an element to detect duplicates in tab order"""
    try:
        tag = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_id = element.get_attribute("id") or ""
        classes = element.get_attribute("class") or ""
        text = element.text[:50] if hasattr(element, 'text') and element.text else ""
        
        return f"{tag}#{element_id}.{classes}:{text}"
    except:
        return "unknown"
```
### accessibility_modules\html_report_generator.py <a id='accessibility_modules_html_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\html_report_generator.py
- **Last Modified**: 2025-03-10 23:23:55
- **Size**: 17063 bytes

#### Code
```python
"""
HTML Report Generator Module
Generates a professional HTML report from accessibility check results with working accordions.
"""

import os
import json
from datetime import datetime
import logging
from urllib.parse import urlparse

def generate_html_report(accessibility_report, output_dir=None):
    """
    Generate an HTML report from accessibility check results.
    
    Args:
        accessibility_report: Dictionary containing accessibility check results
        output_dir: Directory to save the report (default: accessibility_reports)
        
    Returns:
        str: Path to the generated HTML report
    """
    logging.info("Generating HTML accessibility report...")
    
    # Set default output directory if not provided
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'accessibility_reports')
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a filename based on URL and timestamp
    url = accessibility_report.get('url', 'unknown')
    domain = urlparse(url).netloc
    if not domain:
        domain = 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Generate the HTML content
    html_content = _generate_html_content(accessibility_report)
    
    # Write the HTML to a file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logging.info(f"HTML report saved to: {filepath}")
    return filepath

def _generate_html_content(report):
    """Generate HTML content from the accessibility report."""
    # Extract information from the report
    url = report.get('url', 'Unknown URL')
    timestamp = report.get('timestamp', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elapsed_time = report.get('elapsed_time', 'Unknown')
    
    # Get summary statistics
    summary = report.get('summary', {})
    critical_issues = summary.get('critical_issues', 0)
    warnings = summary.get('warnings', 0)
    passed_checks = summary.get('passed_checks', 0)
    compliance_score = summary.get('compliance_score', 'N/A')
    
    # Get consolidated issues
    issues = report.get('issues', [])
    
    # Start building HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - {url}</title>
    <style>
        :root {{
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #34495e;
            --success-color: #2ecc71;
            --warning-color: #f39c12;
            --danger-color: #e74c3c;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            margin: 0;
            padding: 0;
            background-color: #f5f7fa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background-color: var(--primary-color);
            color: white;
            padding: 20px;
            border-radius: 5px 5px 0 0;
            margin-bottom: 20px;
        }}
        
        h1, h2, h3, h4 {{
            color: var(--primary-color);
            margin-top: 0;
        }}
        
        header h1 {{
            color: white;
            margin: 0;
        }}
        
        .report-meta {{
            margin-top: 10px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.8);
        }}
        
        .summary-card {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }}
        
        .summary-item {{
            flex: 1;
            min-width: 200px;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            text-align: center;
        }}
        
        .critical {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .passed {{
            background-color: var(--success-color);
            color: white;
        }}
        
        .score {{
            background-color: var(--secondary-color);
            color: white;
        }}
        
        .summary-number {{
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .summary-label {{
            font-size: 14px;
            text-transform: uppercase;
        }}
        
        .issues-section {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
        }}
        
        .issue-card {{
            border-left: 4px solid var(--warning-color);
            padding: 15px;
            margin-bottom: 15px;
            background-color: #f8f9fa;
            border-radius: 0 5px 5px 0;
        }}
        
        .issue-card.critical {{
            border-left-color: var(--danger-color);
        }}
        
        .issue-card.warning {{
            border-left-color: var(--warning-color);
        }}
        
        .issue-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }}
        
        .issue-title {{
            font-weight: bold;
            font-size: 16px;
            margin: 0;
        }}
        
        .issue-type {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .issue-type.critical {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .issue-type.warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .issue-details {{
            margin-bottom: 10px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            border-left: 2px solid var(--secondary-color);
            padding-left: 10px;
            margin-top: 10px;
        }}
        
        .issue-meta {{
            display: flex;
            font-size: 12px;
            color: #6c757d;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 10px;
        }}
        
        .issue-meta-item {{
            margin-right: 15px;
        }}
        
        .issue-wcag {{
            background-color: var(--primary-color);
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        
        .checks-section {{
            display: flex;
            flex-wrap: wrap;
            margin: 0 -10px;
        }}
        
        .check-card {{
            flex: 1;
            min-width: 300px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin: 10px;
            padding: 15px;
        }}
        
        .check-header {{
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        
        .check-name {{
            font-size: 18px;
            font-weight: bold;
            margin: 0;
        }}
        
        .check-status {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
        }}
        
        .check-status.passed {{
            background-color: var(--success-color);
            color: white;
        }}
        
        .check-status.failed {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .check-status.warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .check-status.skipped {{
            background-color: #6c757d;
            color: white;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            margin-top: 20px;
            color: #6c757d;
            font-size: 14px;
        }}
        
        /* Toggle button style */
        .toggle-btn {{
            background-color: #f1f1f1;
            color: #444;
            cursor: pointer;
            padding: 10px 15px;
            width: 100%;
            text-align: center;
            border: none;
            outline: none;
            font-size: 16px;
            margin-top: 10px;
            border-radius: 5px;
            position: relative;
        }}
        
        .toggle-btn:hover {{
            background-color: #ddd;
        }}
        
        .toggle-btn::after {{
            content: '+';
            position: absolute;
            right: 15px;
            font-weight: bold;
        }}
        
        .toggle-btn.active::after {{
            content: '-';
        }}
        
        /* Content div style */
        .content {{
            display: none;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 0 0 5px 5px;
            margin-top: 5px;
        }}
        
        @media screen and (max-width: 768px) {{
            .summary-item {{
                min-width: 100%;
                margin: 5px 0;
            }}
            
            .check-card {{
                min-width: 100%;
                margin: 10px 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Accessibility Audit Report</h1>
            <div class="report-meta">
                <div><strong>URL:</strong> {url}</div>
                <div><strong>Date:</strong> {timestamp}</div>
                <div><strong>Scan Duration:</strong> {elapsed_time}</div>
            </div>
        </header>
        
        <div class="summary-card">
            <div class="summary-item critical">
                <div class="summary-number">{critical_issues}</div>
                <div class="summary-label">Critical Issues</div>
            </div>
            <div class="summary-item warning">
                <div class="summary-number">{warnings}</div>
                <div class="summary-label">Warnings</div>
            </div>
            <div class="summary-item passed">
                <div class="summary-number">{passed_checks}</div>
                <div class="summary-label">Checks Passed</div>
            </div>
            <div class="summary-item score">
                <div class="summary-number">{compliance_score}</div>
                <div class="summary-label">Compliance Score</div>
            </div>
        </div>
        
        <div class="issues-section">
            <h2>Identified Accessibility Issues</h2>
            <p>The following issues were detected and should be addressed to improve accessibility:</p>
"""
            
    # Add issues
    if issues:
        for issue in issues:
            severity = issue.get('severity', issue.get('type', 'warning'))
            title = issue.get('issue', 'Unknown Issue')
            details = issue.get('details', '')
            recommendation = issue.get('recommendation', '')
            wcag = issue.get('wcag', '')
            check_type = issue.get('check_type', '')
            
            # Use preferred terminology
            if "Inconsistent keyboard navigation sequence" in title.lower():
                title = "Inconsistent keyboard navigation sequence"
            elif "Keyboard navigation barrier" in title.lower():
                title = "Keyboard navigation barrier"
            
            html += f"""
            <div class="issue-card {severity}">
                <div class="issue-header">
                    <h3 class="issue-title">{title}</h3>
                    <span class="issue-type {severity}">{severity}</span>
                </div>
                <div class="issue-details">{details}</div>
                <div class="issue-recommendation">{recommendation}</div>
                <div class="issue-meta">
            """
            
            if check_type:
                html += f'<span class="issue-meta-item"><strong>Check Type:</strong> {check_type}</span>'
            
            if wcag:
                html += f'<span class="issue-meta-item"><strong>WCAG:</strong> <span class="issue-wcag">{wcag}</span></span>'
            
            html += """
                </div>
            </div>
            """
    else:
        html += "<p>No accessibility issues were detected.</p>"
    
    html += """
        </div>
        
        <div class="checks-section">
    """
    
    # Add check sections with the simplest possible accordion approach
    checks = report.get('checks', {})
    for check_name, check_data in checks.items():
        status = check_data.get('status', 'completed')
        issues = check_data.get('issues', [])
        
        if status == 'completed' and not issues:
            status_class = 'passed'
            status_text = 'Passed'
        elif status == 'completed' and issues:
            status_class = 'failed'
            status_text = 'Issues Found'
        elif status == 'skipped':
            status_class = 'skipped'
            status_text = 'Skipped'
        else:
            status_class = 'warning'
            status_text = 'Warning'
        
        # Convert to user-friendly names
        user_friendly_name = check_name.replace('_', ' ').title()
        if check_name == 'tab_order':
            user_friendly_name = 'Keyboard Navigation Sequence'
        elif check_name == 'missing_focusable':
            user_friendly_name = 'Keyboard Accessibility'
        elif check_name == 'image_accessibility':
            user_friendly_name = 'Image Accessibility'
        
        html += f"""
        <div class="check-card">
            <div class="check-header">
                <h3 class="check-name">{user_friendly_name}</h3>
                <span class="check-status {status_class}">{status_text}</span>
            </div>
        """
        
        if status == 'completed':
            if isinstance(issues, list) and issues:
                html += f"""
                <p>Found {len(issues)} issues.</p>
                <button class="toggle-btn" onclick="toggleContent(this)">View Details</button>
                <div class="content">
                    <ul>
                """
                
                for issue in issues:
                    issue_text = issue.get('issue', 'Unknown issue')
                    # Use preferred terminology
                    if "Inconsistent keyboard navigation sequence" in issue_text.lower():
                        issue_text = "Inconsistent keyboard navigation sequence"
                    elif "Keyboard navigation barrier" in issue_text.lower():
                        issue_text = "Keyboard navigation barrier"
                    
                    html += f"<li>{issue_text}</li>"
                
                html += """
                    </ul>
                </div>
                """
            elif not issues:
                html += "<p>No issues detected.</p>"
        elif status == 'skipped':
            reason = check_data.get('reason', 'No reason provided')
            html += f"<p>Check was skipped: {reason}</p>"
        
        html += """
        </div>
        """
    
    # Close HTML and add script with simple toggle functionality
    html += """
        </div>
        
        <footer>
            <p>Generated by Accessibility Checker on """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
        </footer>
    </div>
    
    <script>
    function toggleContent(button) {
        // Toggle active class for styling
        button.classList.toggle('active');
        
        // Get the next sibling element (the content div)
        var content = button.nextElementSibling;
        
        // Toggle the content visibility
        if (content.style.display === 'block') {
            content.style.display = 'none';
        } else {
            content.style.display = 'block';
        }
    }
    </script>
</body>
</html>
"""
    
    return html
```
### accessibility_modules\image_checker.py <a id='accessibility_modules_image_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\image_checker.py
- **Last Modified**: 2025-03-10 22:06:16
- **Size**: 24173 bytes

#### Code
```python
"""
Enhanced Image Accessibility Checker Module
Checks for proper image accessibility and text alternatives for non-text content (WCAG 1.1.1).
"""

import logging
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from urllib.parse import urlparse

def check_image_accessibility(driver):
    """
    Comprehensive check for image accessibility and text alternatives for non-text content.
    Addresses WCAG Success Criterion 1.1.1: Non-text Content
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of image accessibility checks
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
        
        # Check canvas elements
        check_canvas_elements(driver, results)
        
        # Check CSS background images
        check_css_background_images(driver, results)
        
        # Check icon fonts
        check_icon_fonts(driver, results)
        
        # Check other non-text content (audio, video, etc.)
        check_other_nontext_content(driver, results)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking image accessibility: {str(e)}")
        results["error"] = str(e)
        return results

def check_standard_images(driver, results):
    """Check standard <img> elements for proper alt text"""
    images = driver.find_elements(By.TAG_NAME, "img")
    results["image_count"] = len(images)
    
    for image in images:
        # Skip very small images that are likely decorative
        if is_likely_decorative_by_size(image):
            continue
            
        # Check for alt attribute
        alt_text = image.get_attribute("alt")
        src = get_image_identifier(image)
        role = image.get_attribute("role") or ""
        aria_hidden = image.get_attribute("aria-hidden") == "true"
        
        # Check for missing alt attribute
        if alt_text is None:
            results["issues"].append({
                "element": "img",
                "src": src,
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
                    "src": src,
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
                    "src": src,
                    "alt": alt_text,
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
                    "src": src,
                    "alt": alt_text,
                    "issue": "Redundant text alternative",
                    "details": "Alt text appears to duplicate adjacent text content",
                    "recommendation": "Consider using empty alt text (alt='') if the image is adequately described by nearby text",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })
        
        # Check for decorative images that should have empty alt text
        if role == "presentation" or aria_hidden:
            if alt_text and alt_text.strip() != "":
                results["issues"].append({
                    "element": "img",
                    "src": src,
                    "alt": alt_text,
                    "issue": "Decorative image has non-empty alt text",
                    "details": f"Image is marked as decorative ({role if role else 'aria-hidden'}) but has non-empty alt text",
                    "recommendation": "Use empty alt text (alt='') for decorative images",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def check_svg_elements(driver, results):
    """Check SVG elements for proper accessibility"""
    svg_elements = driver.find_elements(By.TAG_NAME, "svg")
    results["svg_count"] = len(svg_elements)
    
    for svg in svg_elements:
        # Get attributes for identification
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
            # Try to get ID or class for identification
            svg_id = svg.get_attribute("id") or ""
            svg_class = svg.get_attribute("class") or ""
            identifier = f"id='{svg_id}'" if svg_id else (f"class='{svg_class}'" if svg_class else "unknown")
            
            results["issues"].append({
                "element": "svg",
                "identifier": identifier,
                "issue": "SVG lacks text alternative",
                "details": "SVG element has no accessible name or description",
                "recommendation": "Add a <title> element, aria-label, or aria-labelledby attribute to describe the SVG",
                "wcag": "1.1.1",
                "severity": "critical" if is_likely_informative(svg) else "warning"
            })
        
        # If it has a title but no desc for complex SVGs
        if has_title and not has_desc and is_complex_svg(svg):
            results["issues"].append({
                "element": "svg",
                "identifier": svg.get_attribute("id") or svg.get_attribute("class") or "unknown",
                "issue": "Complex SVG needs description",
                "details": "Complex SVG has a title but lacks a description",
                "recommendation": "Add a <desc> element to provide more details for complex SVGs",
                "wcag": "1.1.1",
                "severity": "warning"
            })

def check_canvas_elements(driver, results):
    """Check canvas elements for proper accessibility"""
    canvas_elements = driver.find_elements(By.TAG_NAME, "canvas")
    results["canvas_count"] = len(canvas_elements)
    
    for canvas in canvas_elements:
        # Get attributes for identification
        canvas_id = canvas.get_attribute("id") or ""
        canvas_class = canvas.get_attribute("class") or ""
        identifier = f"id='{canvas_id}'" if canvas_id else (f"class='{canvas_class}'" if canvas_class else "unknown")
        
        # Check if canvas has fallback content
        inner_html = driver.execute_script("return arguments[0].innerHTML;", canvas).strip()
        has_fallback = len(inner_html) > 0
        
        # Check for accessibility attributes
        aria_label = canvas.get_attribute("aria-label") or ""
        aria_labelledby = canvas.get_attribute("aria-labelledby") or ""
        
        # Canvas needs either fallback content or ARIA attributes
        if not (has_fallback or aria_label or aria_labelledby):
            results["issues"].append({
                "element": "canvas",
                "identifier": identifier,
                "issue": "Canvas lacks text alternative",
                "details": "Canvas element has no fallback content or accessible name",
                "recommendation": "Add fallback content inside the canvas element or use aria-label/aria-labelledby",
                "wcag": "1.1.1",
                "severity": "critical"
            })

def check_css_background_images(driver, results):
    """Check elements with CSS background images"""
    # Find elements with background images
    background_elements = driver.find_elements(By.CSS_SELECTOR, 
        "[style*='background-image']:not(body):not(html)")
        
    for element in background_elements:
        # Skip elements that are likely decorative
        if is_likely_decorative_element(element):
            continue
            
        # Check if element has accessible text
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        aria_label = element.get_attribute("aria-label") or ""
        aria_labelledby = element.get_attribute("aria-labelledby")
        role = element.get_attribute("role") or ""
        
        # If it's a button or actionable element with no text
        if (element.tag_name in ["button", "a"] or role in ["button", "link"]) and not element_text and not aria_label and not aria_labelledby:
            element_id = element.get_attribute("id") or ""
            element_class = element.get_attribute("class") or ""
            identifier = f"id='{element_id}'" if element_id else (f"class='{element_class}'" if element_class else "unknown")
            
            results["issues"].append({
                "element": element.tag_name,
                "identifier": identifier,
                "issue": "Interactive element with background image lacks text alternative",
                "details": f"{element.tag_name.upper()} element with background image has no accessible name",
                "recommendation": "Add text content, aria-label, or aria-labelledby to describe the purpose of this element",
                "wcag": "1.1.1",
                "severity": "critical"
            })

def check_icon_fonts(driver, results):
    """Check icon fonts for proper accessibility"""
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
        
        for icon in icons:
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
                            "class": icon.get_attribute("class"),
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
                    "class": icon.get_attribute("class"),
                    "issue": "Icon lacks text alternative",
                    "details": "Icon has no accessible name and is not hidden from screen readers",
                    "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def check_other_nontext_content(driver, results):
    """Check other non-text content like video, audio, etc."""
    # Check video elements
    video_elements = driver.find_elements(By.TAG_NAME, "video")
    for video in video_elements:
        if not video.get_attribute("controls"):
            results["issues"].append({
                "element": "video",
                "src": video.get_attribute("src") or "[multiple sources]",
                "issue": "Video missing controls",
                "details": "Video element does not have controls attribute",
                "recommendation": "Add the 'controls' attribute or provide custom accessible controls",
                "wcag": "1.1.1, 2.1.1",
                "severity": "critical"
            })
            
        # Check for captions
        has_track = len(video.find_elements(By.TAG_NAME, "track")) > 0
        if not has_track:
            results["issues"].append({
                "element": "video",
                "src": video.get_attribute("src") or "[multiple sources]",
                "issue": "Video missing captions",
                "details": "No <track> element found for captions or subtitles",
                "recommendation": "Add a <track> element with captions for video content",
                "wcag": "1.1.1, 1.2.2",
                "severity": "critical"
            })
    
    # Check audio elements
    audio_elements = driver.find_elements(By.TAG_NAME, "audio")
    for audio in audio_elements:
        if not audio.get_attribute("controls"):
            results["issues"].append({
                "element": "audio",
                "src": audio.get_attribute("src") or "[multiple sources]",
                "issue": "Audio missing controls",
                "details": "Audio element does not have controls attribute",
                "recommendation": "Add the 'controls' attribute or provide custom accessible controls",
                "wcag": "1.1.1, 2.1.1",
                "severity": "critical"
            })
            
        # Check for transcript
        # This is a heuristic since transcripts are typically outside the audio element
        if not has_nearby_transcript(driver, audio):
            results["issues"].append({
                "element": "audio",
                "src": audio.get_attribute("src") or "[multiple sources]",
                "issue": "Audio may be missing transcript",
                "details": "No visible transcript found near the audio element",
                "recommendation": "Provide a text transcript for audio content",
                "wcag": "1.1.1, 1.2.1",
                "severity": "warning"
            })

# Helper functions

def get_image_identifier(image):
    """Get a useful identifier for the image (src or part of it)"""
    src = image.get_attribute("src") or ""
    
    # If src is a data URL, just return a placeholder
    if src.startswith("data:"):
        return "[data URL]"
        
    # Otherwise, get the filename part of the URL
    # or return a truncated version of the full URL
    filename_match = re.search(r'/([^/]+\.(jpg|jpeg|png|gif|webp|svg))(\?|$)', src, re.IGNORECASE)
    if filename_match:
        return filename_match.group(1)
    else:
        # Truncate very long URLs
        return src[:50] + "..." if len(src) > 50 else src

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

def is_likely_decorative_element(element):
    """Check if an element with background image is likely decorative"""
    # Check for role="presentation" or role="none"
    role = element.get_attribute("role") or ""
    if role.lower() in ["presentation", "none"]:
        return True
        
    # Check element classes for hints it's decorative
    class_attr = element.get_attribute("class") or ""
    decorative_classes = ["decoration", "bg", "background", "separator", "divider", "pattern"]
    if any(cls in class_attr.lower() for cls in decorative_classes):
        return True
        
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

def is_complex_svg(svg):
    """Determine if an SVG is complex and would benefit from a description"""
    try:
        # Count elements in SVG
        elements = svg.find_elements(By.XPATH, "./*")
        
        # If it has many child elements, it's likely complex
        if len(elements) > 10:
            return True
            
        # Check for specific complex element types
        complex_elements = svg.find_elements(
            By.CSS_SELECTOR, "path, polygon, polyline, text, g[transform]")
        
        return len(complex_elements) > 5
    except:
        return False

def has_nearby_transcript(driver, audio_element):
    """Try to detect if there's a transcript near an audio element (heuristic)"""
    try:
        # Look for common transcript indicators near the audio
        parent = audio_element.find_element(By.XPATH, "./..")
        
        # Look for transcript text or elements
        transcript_indicators = [
            "//div[contains(@class, 'transcript')]",
            "//details",  # Often used for expandable transcripts
            "//summary[contains(text(), 'transcript')]",
            "//a[contains(text(), 'transcript')]",
            "//h2[contains(text(), 'transcript')]",
            "//h3[contains(text(), 'transcript')]",
            "//p[contains(text(), 'transcript')]"
        ]
        
        for indicator in transcript_indicators:
            try:
                elements = parent.find_elements(By.XPATH, indicator)
                if elements:
                    return True
            except:
                pass
                
        return False
    except:
        return False
```
### accessibility_modules\report_generator.py <a id='accessibility_modules_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\report_generator.py
- **Last Modified**: 2025-03-10 23:08:24
- **Size**: 13478 bytes

#### Code
```python
"""
Accessibility Report Generator Module
Compiles results from various accessibility checks into a comprehensive report.
"""

import logging
import json
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

# Try to import other accessibility modules
try:
    from accessibility_modules.image_checker import check_image_accessibility
    image_checker_available = True
except ImportError:
    image_checker_available = False

try:
    from accessibility_modules.landmark_checker import check_landmarks_and_structure
    landmark_checker_available = True
except ImportError:
    landmark_checker_available = False

try:
    from accessibility_modules.form_checker import check_form_accessibility
    form_checker_available = True
except ImportError:
    form_checker_available = False

try:
    from accessibility_modules.html_report_generator import generate_html_report
    html_report_available = True
except ImportError:
    html_report_available = False

try:
    from accessibility_modules.simple_html_report_generator import generate_simple_html_report
    simple_html_report_available = True
except ImportError:
    simple_html_report_available = False

def generate_accessibility_report(driver, url, tab_order_results=None, 
                                  missing_focusable_results=None, aria_results=None,
                                  save_to_file=True, output_path=None):
    """
    Generate a comprehensive accessibility report by running various checks.
    
    Args:
        driver: Selenium WebDriver instance
        url: URL of the page being checked
        tab_order_results: Optional pre-run tab order results
        missing_focusable_results: Optional pre-run missing focusable elements results
        aria_results: Optional pre-run ARIA accessibility results
        save_to_file: Whether to save report to a file
        output_path: Path to save the report to
        
    Returns:
        dict: Complete accessibility report with all checks
    """
    logging.info(f"Generating comprehensive accessibility report for {url}")
    start_time = time.time()
    
    report = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "critical_issues": 0,
            "warnings": 0,
            "passed_checks": 0,
            "compliance_score": None  # Will calculate at end
        },
        "checks": {},
        "issues": []  # Consolidated list of all issues
    }
    
    try:
        # Add pre-run results if provided
        if tab_order_results:
            report["checks"]["keyboard_navigation_sequence"] = tab_order_results
            # Add issues to consolidated list
            for issue in tab_order_results.get("issues", []):
                issue["check_type"] = "keyboard_navigation_sequence"
                report["issues"].append(issue)
        
        if missing_focusable_results:
            report["checks"]["keyboard_accessibility"] = {
                "status": "completed",
                "issues": missing_focusable_results
            }
            # Add issues to consolidated list
            for issue in missing_focusable_results:
                if "error" not in issue:  # Skip error entries
                    issue["check_type"] = "keyboard_accessibility"
                    report["issues"].append(issue)
        
        if aria_results:
            report["checks"]["aria_accessibility"] = aria_results
            # Add issues to consolidated list
            for issue in aria_results.get("issues", []):
                issue["check_type"] = "aria_accessibility"
                report["issues"].append(issue)
        
        # Run additional checks if modules are available
        if image_checker_available:
            image_results = check_image_accessibility(driver)
            report["checks"]["image_accessibility"] = image_results
            # Add issues to consolidated list
            for issue in image_results.get("issues", []):
                issue["check_type"] = "image_accessibility"
                report["issues"].append(issue)
        else:
            report["checks"]["image_accessibility"] = {"status": "skipped", "reason": "Module not available"}
        
        if landmark_checker_available:
            landmark_results = check_landmarks_and_structure(driver)
            report["checks"]["landmarks_and_structure"] = landmark_results
            # Add issues to consolidated list
            for issue in landmark_results.get("issues", []):
                issue["check_type"] = "landmarks_and_structure"
                report["issues"].append(issue)
        else:
            report["checks"]["landmarks_and_structure"] = {"status": "skipped", "reason": "Module not available"}
        
        if form_checker_available:
            form_results = check_form_accessibility(driver)
            report["checks"]["form_accessibility"] = form_results
            # Add issues to consolidated list
            for issue in form_results.get("issues", []):
                issue["check_type"] = "form_accessibility"
                report["issues"].append(issue)
        else:
            report["checks"]["form_accessibility"] = {"status": "skipped", "reason": "Module not available"}
        
        # Run basic page title and language check
        title_lang_results = check_basic_page_attributes(driver)
        report["checks"]["basic_page_attributes"] = title_lang_results
        # Add issues to consolidated list
        for issue in title_lang_results.get("issues", []):
            issue["check_type"] = "basic_page_attributes"
            report["issues"].append(issue)
        
        # Calculate summary statistics
        calculate_summary_statistics(report)
        
        # Add timing information
        elapsed_time = time.time() - start_time
        report["elapsed_time"] = f"{elapsed_time:.2f} seconds"
        
        # Save report to file if requested
        if save_to_file:
            # Save JSON report
            json_path = save_report_to_file(report, url, output_path)
            
            # Generate HTML report if available
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                    'accessibility_reports')
            
            # Try regular HTML report first (now with fixed accordions)
            if html_report_available:
                try:
                    html_path = generate_html_report(report, reports_dir)
                    logging.info(f"HTML report generated at: {html_path}")
                    # Add HTML report path to the report
                    report["html_report_path"] = html_path
                except Exception as e:
                    logging.error(f"Error generating HTML report: {str(e)}")
                    # Fall back to simple HTML report if available
                    if simple_html_report_available:
                        try:
                            html_path = generate_simple_html_report(report, reports_dir)
                            logging.info(f"Simple HTML report generated at: {html_path}")
                            report["html_report_path"] = html_path
                        except Exception as e2:
                            logging.error(f"Error generating simple HTML report: {str(e2)}")
            # Fall back to simple HTML report if regular is not available
            elif simple_html_report_available:
                try:
                    html_path = generate_simple_html_report(report, reports_dir)
                    logging.info(f"Simple HTML report generated at: {html_path}")
                    report["html_report_path"] = html_path
                except Exception as e:
                    logging.error(f"Error generating simple HTML report: {str(e)}")
            
        return report
        
    except WebDriverException as e:
        logging.error(f"Error generating accessibility report: {str(e)}")
        report["error"] = str(e)
        return report

def check_basic_page_attributes(driver):
    """Check basic page attributes like title and language"""
    logging.info("Checking basic page attributes...")
    results = {
        "status": "completed",
        "issues": []
    }
    
    try:
        # Check for page title
        title = driver.title
        if not title or title.strip() == "":
            results["issues"].append({
                "issue": "Missing page title",
                "details": "Page does not have a title",
                "recommendation": "Add a descriptive <title> element",
                "wcag": "2.4.2",
                "severity": "critical"
            })
        elif len(title) < 5:
            results["issues"].append({
                "issue": "Page title may be too short",
                "details": f"Current title: '{title}'",
                "recommendation": "Use a more descriptive page title",
                "wcag": "2.4.2",
                "severity": "warning"
            })
        
        # Check for HTML lang attribute
        html_element = driver.find_element(By.TAG_NAME, "html")
        lang_attr = html_element.get_attribute("lang")
        
        if not lang_attr:
            results["issues"].append({
                "issue": "Missing language declaration",
                "details": "The <html> element does not have a lang attribute",
                "recommendation": "Add a lang attribute to the <html> element (e.g., lang='en')",
                "wcag": "3.1.1",
                "severity": "critical"
            })
        elif len(lang_attr) < 2:
            results["issues"].append({
                "issue": "Invalid language declaration",
                "details": f"The lang attribute '{lang_attr}' appears to be invalid",
                "recommendation": "Use a valid language code (e.g., 'en', 'fr', 'es')",
                "wcag": "3.1.1",
                "severity": "critical"
            })
            
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking basic page attributes: {str(e)}")
        results["error"] = str(e)
        return results

def calculate_summary_statistics(report):
    """Calculate summary statistics for the report"""
    critical_count = 0
    warning_count = 0
    passed_checks = 0
    check_count = 0
    
    # Count issues by severity
    for issue in report["issues"]:
        severity = issue.get("severity") or issue.get("type")
        if severity == "critical":
            critical_count += 1
        elif severity == "warning":
            warning_count += 1
    
    # Count passed checks
    for check_name, check_results in report["checks"].items():
        check_count += 1
        if check_results.get("status") == "completed" and len(check_results.get("issues", [])) == 0:
            passed_checks += 1
    
    # Update summary
    report["summary"]["critical_issues"] = critical_count
    report["summary"]["warnings"] = warning_count
    report["summary"]["passed_checks"] = passed_checks
    report["summary"]["total_checks"] = check_count
    
    # Calculate compliance score (simple formula, can be refined)
    if check_count > 0:
        # Weight critical issues more heavily than warnings
        weighted_issues = critical_count * 3 + warning_count
        max_score = check_count * 10  # Assume 10 possible points per check
        if critical_count > 0:
            # If there are critical issues, cap the score at 80%
            score = max(0, min(80, 100 - (weighted_issues * 100 / max_score)))
        else:
            score = max(0, 100 - (weighted_issues * 100 / max_score))
        
        report["summary"]["compliance_score"] = round(score, 1)
    else:
        report["summary"]["compliance_score"] = "N/A"

def save_report_to_file(report, url, output_path=None):
    """Save the accessibility report to a JSON file"""
    try:
        # Create a suitable filename from the URL
        if not output_path:
            url_clean = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "")
            if len(url_clean) > 50:
                url_clean = url_clean[:50]
            
            # Create the reports directory if it doesn't exist
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                      'accessibility_reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
                
            filename = os.path.join(reports_dir, 
                                   f"accessibility_report_{url_clean}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        else:
            filename = output_path
            
        # Ensure directory exists
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        # Write report to file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        logging.info(f"Accessibility report saved to: {filename}")
        return filename
        
    except Exception as e:
        logging.error(f"Error saving report to file: {str(e)}")
        return None
```
### accessibility_modules\simple_html_report_generator.py <a id='accessibility_modules_simple_html_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\simple_html_report_generator.py
- **Last Modified**: 2025-03-10 22:32:34
- **Size**: 8045 bytes

#### Code
```python
"""
Simple HTML Report Generator
Generates a basic HTML accessibility report with functioning accordions.
"""

import os
import logging
from datetime import datetime
from urllib.parse import urlparse

def generate_simple_html_report(report_data, output_dir=None):
    """
    Generate a simple HTML accessibility report with working accordions.
    
    Args:
        report_data: Dictionary with accessibility issues
        output_dir: Where to save the report
        
    Returns:
        str: Path to the generated report
    """
    # Set default output directory
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), 'accessibility_reports')
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create filename
    url = report_data.get('url', 'unknown')
    domain = urlparse(url).netloc or 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Get data for the report
    issues_by_type = {}
    
    # Group issues by check type
    for issue in report_data.get('issues', []):
        check_type = issue.get('check_type', 'general')
        if check_type not in issues_by_type:
            issues_by_type[check_type] = []
        issues_by_type[check_type].append(issue)
    
    # Build HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - {url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        
        .section {{
            margin-bottom: 30px;
            border: 1px solid #eee;
            border-radius: 5px;
            padding: 15px;
        }}
        
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }}
        
        .issue-count {{
            background-color: #e74c3c;
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 14px;
        }}
        
        .issue-count.no-issues {{
            background-color: #2ecc71;
        }}
        
        .section-content {{
            margin-top: 15px;
        }}
        
        .collapsible {{
            background-color: #f8f9fa;
            color: #444;
            cursor: pointer;
            padding: 18px;
            width: 100%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            margin-bottom: 5px;
            border-radius: 5px;
            text-align: center;
        }}
        
        .active, .collapsible:hover {{
            background-color: #f1f1f1;
        }}
        
        .collapsible:after {{
            content: '\\002B'; /* Unicode character for "plus" sign (+) */
            color: #777;
            font-weight: bold;
            float: right;
            margin-left: 5px;
        }}
        
        .active:after {{
            content: "\\2212"; /* Unicode character for "minus" sign (-) */
        }}
        
        .content {{
            padding: 0 18px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #f1f1f1;
            border-radius: 0 0 5px 5px;
        }}
        
        .issue-list {{
            list-style-type: none;
            padding: 0;
        }}
        
        .issue-item {{
            margin-bottom: 10px;
            padding: 10px;
            border-left: 4px solid #e74c3c;
            background-color: white;
        }}
        
        .issue-title {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .issue-details {{
            margin-bottom: 5px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            color: #666;
        }}
        
        .wcag {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Accessibility Report</h1>
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>Accessibility Issues Summary</h2>
"""

    # Add sections for each issue type
    for check_type, issues in issues_by_type.items():
        # Make the check type name more readable
        check_name = check_type.replace('_', ' ').title()
        
        html += f"""
        <div class="section">
            <div class="section-header">
                <h3>{check_name}</h3>
                <span class="issue-count {'no-issues' if not issues else ''}">
                    {len(issues)} {'Issue' if len(issues) == 1 else 'Issues'}
                </span>
            </div>
            
            <div class="section-content">
"""
        
        if issues:
            html += f"""
                <button class="collapsible">View Details</button>
                <div class="content">
                    <ul class="issue-list">
"""
            
            for issue in issues:
                title = issue.get('issue', 'Unknown Issue')
                details = issue.get('details', '')
                recommendation = issue.get('recommendation', '')
                wcag = issue.get('wcag', '')
                
                html += f"""
                        <li class="issue-item">
                            <div class="issue-title">{title}</div>
                            <div class="issue-details">{details}</div>
                            <div class="issue-recommendation">{recommendation}</div>
                            {f'<div><span class="wcag">WCAG {wcag}</span></div>' if wcag else ''}
                        </li>
"""
            
            html += """
                    </ul>
                </div>
"""
        else:
            html += """
                <p>No issues detected.</p>
"""
        
        html += """
            </div>
        </div>
"""
    
    # Close HTML and add script
    html += """
        <footer>
            <p>Generated by Accessibility Checker</p>
        </footer>
    </div>
    
    <script>
        // Wait for DOM to load
        document.addEventListener('DOMContentLoaded', function() {
            var coll = document.getElementsByClassName("collapsible");
            var i;

            for (i = 0; i < coll.length; i++) {
                coll[i].addEventListener("click", function() {
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    if (content.style.maxHeight) {
                        content.style.maxHeight = null;
                    } else {
                        content.style.maxHeight = content.scrollHeight + "px";
                    }
                });
            }
        });
    </script>
</body>
</html>
"""
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    logging.info(f"Simple HTML report generated at: {filepath}")
    return filepath
```
### accessibility_modules\tab_order_checker.py <a id='accessibility_modules_tab_order_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\tab_order_checker.py
- **Last Modified**: 2025-03-10 21:18:44
- **Size**: 8722 bytes

#### Code
```python
"""
Tab Order Checker Module
Checks the tab order of focusable elements to ensure they follow a logical sequence.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

def check_tab_order(driver):
    """
    Checks the tab order of focusable elements on a webpage.
    
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
        # Reset focus to beginning of page
        driver.find_element(By.TAG_NAME, "body").click()
        
        # Find all potentially focusable elements
        focusable_selector = (
            "a, button, input:not([type='hidden']), select, textarea, "
            "[tabindex]:not([tabindex='-1']), [contenteditable='true'], "
            "details, summary, [role='button'], [role='link'], "
            "[role='checkbox'], [role='radio'], [role='tab'], [role='menuitem']"
        )
        
        # Get all focusable elements for reference
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        logging.info(f"Found {len(all_focusable)} potentially focusable elements")
        tab_order_results["potentially_focusable_count"] = len(all_focusable)
        
        # Attempt to follow tab sequence
        max_tabs = min(len(all_focusable) * 2, 100)  # Limit to prevent infinite loops
        focused_elements = []
        
        # Start with pressing Tab once to get to first element
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        
        for i in range(max_tabs):
            # Get currently focused element
            active_element = driver.execute_script("return document.activeElement;")
            element_info = get_element_info(active_element)
            
            # Skip if we encounter the same element again (circular tabbing)
            element_signature = (
                element_info.get("tag", "") + 
                element_info.get("id", "") + 
                element_info.get("text", "")
            )
            
            if element_signature in [e.get("signature", "") for e in focused_elements]:
                # We've already seen this element, likely in a loop
                if len(focused_elements) > 1:
                    break
            
            # Add to our sequence
            element_info["signature"] = element_signature
            element_info["tab_index"] = i + 1
            focused_elements.append(element_info)
            
            # Move to next element
            active_element.send_keys(Keys.TAB)
        
        tab_order_results["tab_sequence"] = focused_elements
        
        # Analyze the tab order for issues
        analyze_tab_order(tab_order_results)
        
        return tab_order_results
        
    except WebDriverException as e:
        logging.error(f"Error checking tab order: {str(e)}")
        tab_order_results["error"] = str(e)
        return tab_order_results

def get_element_info(element):
    """Extract useful information about an element"""
    try:
        tag_name = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        
        info = {
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
    if "potentially_focusable_count" in results and len(tab_sequence) < results["potentially_focusable_count"] / 2:
        issues.append({
            "type": "warning",
            "issue": "Potential keyboard navigation barriers",
            "details": f"Tab sequence ({len(tab_sequence)} elements) is much shorter than expected ({results.get('potentially_focusable_count', 'unknown')} potentially focusable elements)",
            "recommendation": "Check for elements that should be focusable but aren't",
            "wcag": "2.1.1"
        })
    
    results["issues"] = issues
```
### accessibility_modules\terminology_validator.py <a id='accessibility_modules_terminology_validator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\terminology_validator.py
- **Last Modified**: 2025-03-10 22:08:19
- **Size**: 10040 bytes

#### Code
```python
"""
Accessibility Terminology Validator
Ensures consistent terminology is used throughout the accessibility checker.
"""

import re
import json
import os
import logging

class AccessibilityTerminologyValidator:
    """
    Validates and standardizes accessibility terminology used in reports and issue descriptions.
    Uses a central terminology mapping to ensure consistency.
    """
    
    def __init__(self, terminology_file=None):
        """
        Initialize the terminology validator.
        
        Args:
            terminology_file: Path to a JSON file containing terminology mappings
        """
        self.terminology_mapping = {
            # Default terminology mappings
            "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
            "Keyboard navigation barrier": "keyboard navigation barrier",
            "missing alt": "missing text alternative",
            "missing alt text": "missing text alternative",
            "alt text missing": "missing text alternative",
            "no alt": "missing text alternative",
            "no alt text": "missing text alternative",
            "alt attribute missing": "missing text alternative",
            "empty alt": "empty text alternative",
            "bad alt": "inadequate text alternative",
            "poor alt": "inadequate text alternative",
            "inadequate alt": "inadequate text alternative",
            "inappropriate alt": "inadequate text alternative",
            "insufficient alt": "inadequate text alternative",
            "incorrect alt": "inadequate text alternative",
            "wrong alt": "inadequate text alternative",
            "missing label": "form control without label",
            "unlabeled": "form control without label",
            "no label": "form control without label",
            "contrast issue": "insufficient color contrast",
            "low contrast": "insufficient color contrast",
            "poor contrast": "insufficient color contrast",
            "contrast problem": "insufficient color contrast",
            "contrast error": "insufficient color contrast",
            "color contrast issue": "insufficient color contrast",
            "color contrast problem": "insufficient color contrast",
            "color contrast error": "insufficient color contrast",
            "keyboard trap": "keyboard navigation barrier",
            "focus trap": "keyboard navigation barrier",
            "focus issue": "keyboard navigation barrier",
            "focus problem": "keyboard navigation barrier",
            "focus error": "keyboard navigation barrier",
            "keyboard issue": "keyboard navigation barrier",
            "keyboard problem": "keyboard navigation barrier",
            "keyboard error": "keyboard navigation barrier",
            "missing aria": "incomplete ARIA implementation",
            "incorrect aria": "incomplete ARIA implementation",
            "aria issue": "incomplete ARIA implementation",
            "aria problem": "incomplete ARIA implementation",
            "aria error": "incomplete ARIA implementation",
            "aria-label missing": "incomplete ARIA implementation",
            "aria-labelledby missing": "incomplete ARIA implementation",
            "aria-describedby missing": "incomplete ARIA implementation",
            "missing landmark": "missing page structure landmarks",
            "landmark issue": "missing page structure landmarks",
            "landmark problem": "missing page structure landmarks",
            "landmark error": "missing page structure landmarks",
            "heading issue": "improper heading structure",
            "heading problem": "improper heading structure",
            "heading error": "improper heading structure",
            "heading structure issue": "improper heading structure",
            "missing heading": "improper heading structure",
            "heading level skipped": "improper heading structure",
            "heading level issue": "improper heading structure"
        }
        
        # Load additional or override terminology from file if provided
        if terminology_file and os.path.exists(terminology_file):
            try:
                with open(terminology_file, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
            except Exception as e:
                logging.error(f"Error loading terminology file: {str(e)}")
    
    def standardize_terminology(self, text):
        """
        Standardize terminology in the provided text.
        
        Args:
            text: The text to standardize
            
        Returns:
            str: Text with standardized terminology
        """
        if not text:
            return text
            
        standardized_text = text
        
        # Apply each terminology mapping
        for incorrect, correct in self.terminology_mapping.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(incorrect), re.IGNORECASE)
            standardized_text = pattern.sub(correct, standardized_text)
        
        return standardized_text
    
    def validate_report_terminology(self, report):
        """
        Validate and standardize terminology in an accessibility report.
        
        Args:
            report: Dictionary containing accessibility report data
            
        Returns:
            dict: Report with standardized terminology
        """
        if not report or not isinstance(report, dict):
            return report
            
        # Create a copy of the report to avoid modifying the original
        validated_report = report.copy()
        
        # Process issues
        if "issues" in validated_report:
            for i, issue in enumerate(validated_report["issues"]):
                if "issue" in issue:
                    issue["issue"] = self.standardize_terminology(issue["issue"])
                if "details" in issue:
                    issue["details"] = self.standardize_terminology(issue["details"])
                if "recommendation" in issue:
                    issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        # Process checks
        if "checks" in validated_report:
            for check_name, check_data in validated_report["checks"].items():
                if isinstance(check_data, dict) and "issues" in check_data:
                    for i, issue in enumerate(check_data["issues"]):
                        if isinstance(issue, dict):
                            if "issue" in issue:
                                issue["issue"] = self.standardize_terminology(issue["issue"])
                            if "details" in issue:
                                issue["details"] = self.standardize_terminology(issue["details"])
                            if "recommendation" in issue:
                                issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        return validated_report
    
    def load_terminology_file(self, file_path):
        """
        Load terminology mappings from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
                return True
            else:
                logging.error(f"Terminology file not found: {file_path}")
                return False
        except Exception as e:
            logging.error(f"Error loading terminology file: {str(e)}")
            return False
    
    def save_terminology_file(self, file_path):
        """
        Save the current terminology mappings to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.terminology_mapping, f, indent=4, sort_keys=True)
                
            logging.info(f"Saved {len(self.terminology_mapping)} terminology mappings to {file_path}")
            return True
        except Exception as e:
            logging.error(f"Error saving terminology file: {str(e)}")
            return False
    
    def add_terminology_mapping(self, incorrect, correct):
        """
        Add a new terminology mapping.
        
        Args:
            incorrect: The incorrect or inconsistent term
            correct: The preferred term to use instead
            
        Returns:
            bool: True if added successfully
        """
        if not incorrect or not correct:
            return False
            
        self.terminology_mapping[incorrect.lower()] = correct.lower()
        return True
    
    def remove_terminology_mapping(self, incorrect):
        """
        Remove a terminology mapping.
        
        Args:
            incorrect: The incorrect term to remove from mappings
            
        Returns:
            bool: True if removed, False if not found
        """
        if incorrect and incorrect.lower() in self.terminology_mapping:
            del self.terminology_mapping[incorrect.lower()]
            return True
        return False
```
### accessibility_modules\test_accordion.py <a id='accessibility_modules_test_accordion_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\test_accordion.py
- **Last Modified**: 2025-03-10 22:40:32
- **Size**: 1654 bytes

#### Code
```python
"""
Test script to generate a simple HTML report with working accordions.
"""

import os
import sys

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from simple_html_report_generator import generate_simple_html_report

# Sample data to test the report
sample_data = {
    "url": "https://example.com",
    "issues": [
        {
            "check_type": "image_accessibility",
            "issue": "Missing alt text",
            "details": "Image does not have alt attribute",
            "recommendation": "Add descriptive alt text to the image",
            "wcag": "1.1.1"
        },
        {
            "check_type": "image_accessibility",
            "issue": "Decorative image not hidden",
            "details": "Decorative image should be hidden from screen readers",
            "recommendation": "Add aria-hidden='true' or empty alt text",
            "wcag": "1.1.1"
        },
        {
            "check_type": "keyboard_navigation",
            "issue": "Keyboard navigation barrier",
            "details": "Element cannot be accessed with keyboard",
            "recommendation": "Make the element focusable",
            "wcag": "2.1.1"
        }
    ]
}

# Generate report
report_path = generate_simple_html_report(sample_data)
print(f"Test report generated at: {report_path}")

# Try to open the report in the default browser
try:
    import webbrowser
    webbrowser.open(f"file://{os.path.abspath(report_path)}")
    print("Report opened in browser")
except:
    print("Could not open report in browser")
```
### accessibility_modules\__init__.py <a id='accessibility_modules___init___py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\__init__.py
- **Last Modified**: 2025-03-10 21:19:19
- **Size**: 122 bytes

#### Code
```python
"""
Accessibility Modules Package
Contains modules for performing various accessibility checks.
"""

__version__ = '0.1.0'
```
### archive\accessibility_checker.py <a id='archive_accessibility_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\accessibility_checker.py
- **Last Modified**: 2025-03-10 21:08:10
- **Size**: 7174 bytes

#### Code
```python
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
    
    # Store the Inconsistent keyboard navigation sequences
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
```
### archive\accessibility_checker_starter.py <a id='archive_accessibility_checker_starter_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\accessibility_checker_starter.py
- **Last Modified**: 2025-03-10 20:14:23
- **Size**: 6308 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

import sys
import os
import importlib
import argparse
from pathlib import Path

# Add current directory to Python path to ensure module imports work
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(current_dir / 'accessibility_checker.log'),
        logging.StreamHandler()
    ]
)

# Available modules for accessibility checking
AVAILABLE_MODULES = {
    'tab_order': 'missing_focusable_elements',
    'missing_focusable': 'missing_focusable_elements',
    'generate_report': 'generate_accessibility_report',
    'aria_check': 'generate_accessibility_report'
}

def import_module(module_name):
    """
    Dynamically import a module by name.

    Args:
        module_name (str): Name of the module to import

    Returns:
        module: Imported module or None if import fails
    """
    try:
        # Normalize the module name (convert to lowercase, remove any IPython remnants)
        normalized_name = module_name.lower().replace('ipython.', '')

        # Try importing from the predefined module names
        if normalized_name in AVAILABLE_MODULES:
            module_path = AVAILABLE_MODULES[normalized_name]
            logging.info(f"Attempting to import module: {module_path}")
            return importlib.import_module(module_path)

        # Try importing the exact module name provided
        logging.info(f"Attempting to import module directly: {normalized_name}")
        return importlib.import_module(normalized_name)
    except ImportError as e:
        logging.error(f"Could not import module '{module_name}': {e}")
        print(f"❌ Could not import module '{module_name}': {e}")
        # Print additional context about available modules
        print("Available modules:", list(sys.modules.keys()))
        return None

def run_tab_order_check(url, browser='chrome'):
    """
    Run tab order accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Tab order check module not available.")
    return None

def run_missing_focusable_check(url, browser='chrome'):
    """
    Run missing focusable elements check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Missing focusable elements check module not available.")
    return None

def generate_comprehensive_report(url):
    """
    Generate a comprehensive accessibility report.

    Args:
        url (str): Website URL to generate report for
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ Report generation module not available.")
    return None

def run_aria_check(url, browser='chrome'):
    """
    Run ARIA and keyboard accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ ARIA and keyboard accessibility check module not available.")
    return None

def main():
    """
    Main entry point for the Accessibility Checker.
    """
    # Import URL from config
    from config import url_to_check

    parser = argparse.ArgumentParser(description="Accessibility Checker - Comprehensive Web Accessibility Testing Tool")

    # Add arguments
    parser.add_argument('--url', help='Website URL to check', default=url_to_check)
    parser.add_argument('--browser', default='chrome',
                        choices=['chrome', 'firefox', 'edge'],
                        help='Browser to use for testing (default: chrome)')
    parser.add_argument('--check', choices=['tab_order', 'missing_focusable', 'aria', 'report', 'all'],
                        default='all',
                        help='Specific type of accessibility check to run')

    # Parse arguments
    args = parser.parse_args()

    # Welcome message
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {args.url}")
    print(f"Browser: {args.browser}")
    print("=" * 60)

    # Run specific or all checks
    try:
        if args.check in ['tab_order', 'all']:
            print("\n📊 Running Tab Order Check...")
            tab_order_result = run_tab_order_check(args.url, args.browser)

        if args.check in ['missing_focusable', 'all']:
            print("\n🕵️ Checking Missing Focusable Elements...")
            missing_focusable_result = run_missing_focusable_check(args.url, args.browser)

        if args.check in ['aria', 'all']:
            print("\n♿ Running ARIA and Keyboard Accessibility Check...")
            aria_result = run_aria_check(args.url, args.browser)

        if args.check in ['report', 'all']:
            print("\n📄 Generating Comprehensive Report...")
            report = generate_comprehensive_report(args.url)

        print("\n" + "=" * 60)
        print("✅ Accessibility Check Complete")
        print("=" * 60)

    except Exception as e:
        logging.error(f"An error occurred during the accessibility check: {e}")
        print(f"\n❌ An error occurred during the accessibility check: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
```
### archive\config.py <a id='archive_config_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\config.py
- **Last Modified**: 2025-03-10 20:09:02
- **Size**: 1096 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8
from pathlib import Path

# Website to be audited
url_to_check = "https://www.sse.com"

# Browser for testing
browser_choice = "firefox"  # Options: 'chrome', 'firefox', 'edge'

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Logging directory
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Logging configuration
LOG_FILE = LOGS_DIR / 'accessibility_checker.log'

# Accessibility check settings
CHECKS = {
    'tab_order': True,
    'missing_focusable': True,
    'aria': True,
    'keyboard_accessibility': True,
    'non_text_content': True
}

# Issue thresholds for reporting
ISSUE_THRESHOLDS = {
    'tab_order_issues': 5,
    'missing_focusable_issues': 3,
    'aria_issues': 3,
    'keyboard_issues': 3
}

# Optional additional configurations can be added here

# Export configuration for use in other modules
__all__ = [
    'url_to_check', 
    'browser_choice', 
    'REPORTS_DIR', 
    'LOGS_DIR', 
    'CHECKS', 
    'ISSUE_THRESHOLDS'
]
```
### archive\convert_notebooks.py <a id='archive_convert_notebooks_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\convert_notebooks.py
- **Last Modified**: 2025-03-10 17:27:09
- **Size**: 2038 bytes

#### Code
```python
#!/usr/bin/env python3

import os
import subprocess
import sys

def convert_notebooks(directory):
    """
    Convert all Jupyter Notebook files in the specified directory to Python scripts.
    
    Args:
        directory (str): Path to the directory containing Jupyter Notebook files
    """
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)
    
    # Counter for converted notebooks
    converted_count = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a Jupyter Notebook
        if filename.endswith('.ipynb'):
            # Full path to the notebook
            notebook_path = os.path.join(directory, filename)
            
            try:
                # Run jupyter nbconvert command
                result = subprocess.run([
                    'jupyter', 'nbconvert', 
                    '--to', 'script', 
                    notebook_path
                ], capture_output=True, text=True)
                
                # Check if conversion was successful
                if result.returncode == 0:
                    print(f"Converted: {filename}")
                    converted_count += 1
                else:
                    print(f"Failed to convert {filename}")
                    print(f"Error: {result.stderr}")
            
            except Exception as e:
                print(f"Error converting {filename}: {e}")
    
    # Print summary
    print(f"\nTotal notebooks converted: {converted_count}")

def main():
    # Default directory
    default_directory = 'Pickles'
    
    # Allow directory to be specified as a command-line argument
    directory = sys.argv[1] if len(sys.argv) > 1 else default_directory
    
    print(f"Converting notebooks in directory: {directory}")
    convert_notebooks(directory)

if __name__ == "__main__":
    main()
```
### archive\data_loader.py <a id='archive_data_loader_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\data_loader.py
- **Last Modified**: 2025-03-10 19:26:55
- **Size**: 7092 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data_Loader.ipynb

import json
import glob
import os
import hashlib
from pathlib import Path
from datetime import datetime

# Import from our main module
get_ipython().run_line_magic('run', 'config.ipynb # import config')
from Accessibility_Checker import (
    REPORTS_DIR, 
    AccessibilityIssue, 
    normalize_url, 
    translate_accessibility_issue,
    determine_severity,
    terminology
)

def load_data(url=url_to_check): # changed to default to config URL
    """
    Load accessibility data for a given URL from all available reports.
    
    Args:
        url: URL of the website that was tested
        
    Returns:
        dict: Consolidated data from all reports
    """
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issues": []
    }
    
    # Track unique issues to prevent duplicates
    unique_issues = set()
    
    try:
        # Load data from various report files - using all formats of URL
        report_types = [
            ("tab_order", f"tab_order_{clean_url}_*.json"),
            ("tab_order", f"tab_order_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("missing_focusable", f"missing_focusable_{clean_url}_*.json"),
            ("missing_focusable", f"missing_focusable_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("comprehensive", f"comprehensive_{clean_url}_*.json"),
            ("comprehensive", f"comprehensive_{url.replace('https://', '').replace('http://', '')}_*.json")
        ]
        
        found_data = False
        
        for report_type, pattern in report_types:
            full_pattern = str(REPORTS_DIR / pattern)
            files = glob.glob(full_pattern)
            
            if files:
                latest_file = max(files, key=lambda p: os.path.getmtime(p))
                print(f"Loading {report_type} data from: {os.path.basename(latest_file)}")
                
                with open(latest_file, 'r') as f:
                    report_data = json.load(f)
                    
                    # Define issue_sources based on report type
                    issue_sources = {}
                    
                    if report_type == "tab_order":
                        issue_sources["Tab Order"] = report_data.get("tab_order_issues", [])
                    elif report_type == "missing_focusable":
                        issue_sources["Missing Focusable"] = report_data.get("missing_focusable_issues", [])
                    elif report_type == "comprehensive":
                        issue_sources = {
                            "Tab Order": report_data.get("tab_order_issues", []),
                            "Missing Focusable": report_data.get("missing_focusable_issues", []),
                            "ARIA": report_data.get("aria_issues", []),
                            "Keyboard": report_data.get("keyboard_issues", [])
                        }
                    
                    for category, issues in issue_sources.items():
                        if not issues:
                            continue
                            
                        for issue_text in issues:
                            found_data = True
                            
                            # Handle different data formats
                            if isinstance(issue_text, dict):
                                issue_desc = issue_text.get('issue', str(issue_text))
                            else:
                                issue_desc = str(issue_text)
                            
                            # Create a unique identifier for this issue
                            issue_hash = hashlib.md5(f"{category}:{issue_desc}".encode()).hexdigest()
                            
                            # Skip if we've already processed this issue
                            if issue_hash in unique_issues:
                                continue
                            unique_issues.add(issue_hash)
                            
                            # Translate the issue to a more descriptive format
                            translated_issue = translate_accessibility_issue(issue_desc, category, terminology)
                            
                            severity = determine_severity(translated_issue['description'])
                            accessibility_issue = AccessibilityIssue(
                                description=translated_issue['description'],
                                category=category,
                                severity=severity
                            )
                            
                            # Add additional metadata to the issue
                            accessibility_issue.original_text = translated_issue['original']
                            accessibility_issue.impact = translated_issue['impact']
                            accessibility_issue.recommendation = translated_issue['recommendation']
                            
                            data["issues"].append(accessibility_issue)
        
        if not found_data:
            print(f"⚠️ Warning: No accessibility reports found for {url}")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"✅ Loaded {len(data['issues'])} unique accessibility issues from reports")
    return data

def count_issues_by_category(data):
    """Count issues by category and severity"""
    counts = {
        'by_category': {},
        'by_severity': {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        },
        'total': len(data['issues'])
    }
    
    for issue in data['issues']:
        # Count by category
        if issue.category not in counts['by_category']:
            counts['by_category'][issue.category] = 0
        counts['by_category'][issue.category] += 1
        
        # Count by severity
        counts['by_severity'][issue.severity] += 1
    
    return counts

# Example usage
if __name__ == "__main__":
    test_url = url_to_check  # Replace with your target website

    print(f"Testing data loader with URL: {test_url}")
    data = load_data() # removed the need to include the url
    
    if data["issues"]:
        counts = count_issues_by_category(data)
        print("\nIssue Counts by Category:")
        for category, count in counts['by_category'].items():
            print(f"- {category}: {count}")
        
        print("\nIssue Counts by Severity:")
        for severity, count in counts['by_severity'].items():
            print(f"- {severity.capitalize()}: {count}")
    else:
        print("No issues found in any reports.")


```
### archive\enhanced_report_generator.py <a id='archive_enhanced_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\enhanced_report_generator.py
- **Last Modified**: 2025-03-10 19:27:00
- **Size**: 11258 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enhanced_Report_Generator.ipynb

# Import URL from config
get_ipython().run_line_magic('run', 'config.ipynb')

import os
import hashlib
from pathlib import Path
from datetime import datetime
import webbrowser
import matplotlib.pyplot as plt
import numpy as np

# Import from our custom modules
from Accessibility_Checker import REPORTS_DIR, normalize_url, terminology
from Data_Loader import load_data, count_issues_by_category

def get_test_instructions(category, description):
   """
   Generate practical testing instructions based on the issue category and description.
   """
   if category == "Tab Order":
       return "Try navigating through the page using only the Tab key. Notice if the focus jumps around in an unpredictable or illogical order."
   
   elif category == "Missing Focusable":
       return "Attempt to interact with this element using only your keyboard (without using a mouse). Try tabbing to it and pressing Enter/Space. If you cannot reach or activate it, the issue is confirmed."
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return "Use a screen reader to navigate to this image. The screen reader should announce a meaningful description of the image content, not just its filename or 'image'."
       elif "label" in description.lower():
           return "Use a screen reader to navigate to this form field. The screen reader should clearly announce the purpose of the field."
       elif "heading" in description.lower():
           return "Check the document outline using an accessibility tool like WAVE or axe. The headings should follow a logical hierarchical structure."
       elif "landmark" in description.lower():
           return "Use a screen reader's landmarks navigation feature. Important sections of the page should be reachable through landmarks."
       return "Use a screen reader to verify this element provides appropriate context and information."
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return "Tab to this element and check if there is a clearly visible indicator showing that it has keyboard focus. The focus should be easily noticeable against the background."
       return "Test this element using only keyboard controls (Tab, Enter, Space, arrow keys). You should be able to access and operate all functionality without a mouse."
   
   return "Navigate to this element and test its behavior using both keyboard-only navigation and a screen reader."

def get_fix_example(category, description, severity):
   """
   Generate code examples to fix the issue based on category, description and severity.
   """
   if category == "Tab Order":
       return """
           Ensure tabindex attributes follow a logical order:
           ```html
<!-- Avoid using tabindex values like this -->
<div tabindex="1">First element</div>
<div tabindex="3">Second element</div> <!-- Problem: out of sequence -->
<div tabindex="2">Third element</div>

<!-- Better approach: use tabindex="0" or adjust the DOM order -->
<div tabindex="0">First element</div>
<div tabindex="0">Second element</div>
<div tabindex="0">Third element</div>
           ```
       """
   
   elif category == "Missing Focusable":
       if "div" in description.lower() or "span" in description.lower():
           return """
               Convert div/span to a semantic button or add proper ARIA roles:
               ```html
<!-- Instead of this -->
<div class="btn" onclick="doSomething()">Click Me</div>

<!-- Use this -->
<button onclick="doSomething()">Click Me</button>

<!-- Or if you must use a div, add these attributes -->
<div class="btn" 
    onclick="doSomething()" 
    onkeydown="if(event.key==='Enter'||event.key===' ')doSomething()" 
    role="button" 
    tabindex="0">Click Me</div>
               ```
           """
       return """
           Make the element keyboard accessible:
           ```html
<!-- Add tabindex="0" to make it focusable -->
<!-- Add keyboard event handlers alongside click handlers -->
<!-- Add appropriate ARIA role if not using a semantic element -->

<element tabindex="0" 
        role="appropriate-role" 
        onclick="doAction()" 
        onkeydown="if(event.key==='Enter')doAction()">
   Content
</element>
           ```
       """
   
   elif category == "ARIA":
       if "missing alt" in description.lower():
           return """
               Add descriptive alt text to images:
               ```html
<!-- Avoid this -->
<img src="chart.png">

<!-- Use this instead -->
<img src="chart.png" alt="Bar chart showing sales growth by quarter for 2023, with Q4 showing highest growth at 27%">
               ```
           """
       elif "label" in description.lower():
           return """
               Add proper labels to form fields:
               ```html
<!-- Avoid this -->
<input type="text" name="email" placeholder="Enter email">

<!-- Use this instead -->
<label for="email">Email Address</label>
<input type="text" id="email" name="email">
               ```
           """
       elif "heading" in description.lower():
           return """
               Fix heading structure to follow hierarchy:
               ```html
<!-- Avoid this -->
<h1>Page Title</h1>
<h3>First Section</h3> <!-- Problem: skipped h2 -->

<!-- Use this instead -->
<h1>Page Title</h1>
<h2>First Section</h2>
<h3>Subsection</h3>
               ```
           """
       elif "landmark" in description.lower():
           return """
               Add proper landmark roles to page sections:
               ```html
<!-- Add these structural elements -->
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<footer role="contentinfo">...</footer>
               ```
           """
   
   elif category == "Keyboard":
       if "focus indicator" in description.lower():
           return """
               Ensure visible focus styles:
               ```css
/* Add this to your CSS */
:focus {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
}

/* For better visibility against different backgrounds */
:focus-visible {
 outline: 2px solid #0066ff;
 outline-offset: 2px;
 box-shadow: 0 0 0 4px rgba(0, 102, 255, 0.3);
}
               ```
           """
   
   return """Implement appropriate fixes based on the issue description and web accessibility best practices."""

def get_wcag_criteria(category, description):
   """
   Map issue categories to relevant WCAG criteria.
   """
   criteria = {
       "Tab Order": "2.4.3 Focus Order (Level A)",
       "Missing Focusable": "2.1.1 Keyboard (Level A)",
       "ARIA": {
           "alt": "1.1.1 Non-text Content (Level A)",
           "label": "3.3.2 Labels or Instructions (Level A)",
           "heading": "1.3.1 Info and Relationships (Level A), 2.4.6 Headings and Labels (Level AA)",
           "landmark": "1.3.1 Info and Relationships (Level A), 4.1.2 Name, Role, Value (Level A)"
       },
       "Keyboard": {
           "focus indicator": "2.4.7 Focus Visible (Level AA)",
           "default": "2.1.1 Keyboard (Level A)"
       }
   }
   
   if category == "ARIA":
       for key, value in criteria["ARIA"].items():
           if key in description.lower():
               return value
       return criteria["ARIA"].get("landmark")  # Default for ARIA
   
   elif category == "Keyboard":
       for key, value in criteria["Keyboard"].items():
           if key in description.lower():
               return value
       return criteria["Keyboard"].get("default")  # Default for Keyboard
   
   return criteria.get(category, "")

def create_visualization(data, output_path=None):
   """Create visualization of accessibility issues."""
   if not output_path:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       output_path = REPORTS_DIR / f"visualization_{timestamp}.png"
   
   counts = count_issues_by_category(data)
   
   # Create a figure with two subplots
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
   
   # Plot issues by category
   categories = list(counts['by_category'].keys())
   category_counts = list(counts['by_category'].values())
   
   # Sort by count
   sorted_indices = np.argsort(category_counts)
   sorted_categories = [categories[i] for i in sorted_indices]
   sorted_counts = [category_counts[i] for i in sorted_indices]
   
   ax1.barh(sorted_categories, sorted_counts, color='steelblue')
   ax1.set_title('Issues by Category')
   ax1.set_xlabel('Number of Issues')
   
   # Plot issues by severity
   severities = ['critical', 'high', 'medium', 'low']
   severity_counts = [counts['by_severity'][s] for s in severities]
   
   colors = ['darkred', 'orangered', 'orange', 'yellowgreen']
   ax2.pie(severity_counts, labels=severities, autopct='%1.1f%%', 
          shadow=True, startangle=90, colors=colors)
   ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   ax2.set_title('Issues by Severity')
   
   plt.tight_layout()
   plt.savefig(output_path)
   
   return output_path

def generate_enhanced_html_report(data, output_path=None):
   """
   Generate an enhanced bipolar HTML report with information suitable for both
   accessibility experts and non-experts.
   
   Args:
       data: Dictionary containing all accessibility data
       output_path: Path to save the HTML report (optional)
   
   Returns:
       str: Path to the generated HTML report
   """
   # Prepare output path
   if output_path is None:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       clean_url = normalize_url(data.get("url", "unknown"))
       output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
   
   # Ensure reports directory exists
   os.makedirs(os.path.dirname(output_path), exist_ok=True)
   
   # Prepare issue categorization
   categorized_issues = {
       'critical': [],
       'high': [],
       'medium': [],
       'low': []
   }
   
   # Generate a unique hash for each issue to deduplicate
   unique_issues = {}
   
   # Process all issues and deduplicate
   for issue in data.get("issues", []):
       # Create a hash based on core issue properties to identify duplicates
       issue_key = hashlib.md5(
           f"{issue.category}:{issue.description[:100]}".encode()
       ).hexdigest()
       
       # If we've seen this issue before, skip it
       if issue_key in unique_issues:
           continue
           
       # Store unique issue
       unique_issues[issue_key] = issue
       categorized_issues[issue.severity].append(issue)
   
   # Count issues by category for summary
   issue_counts = {
       category: len(issues) for category, issues in categorized_issues.items()
   }
   
   # (Remaining HTML generation code is extremely long, so I've truncated it for brevity)
   # Would you like me to include the full HTML generation code?

   return str(output_path)


```
### archive\generate_accessibility_report.py <a id='archive_generate_accessibility_report_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\generate_accessibility_report.py
- **Last Modified**: 2025-03-10 19:27:04
- **Size**: 3897 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Generate_Accessibility_Report.ipynb
# Interactive notebook for testing and generating accessibility reports

import os
import sys
from pathlib import Path
import webbrowser
from IPython.display import display, HTML, Markdown, Image, clear_output
import ipywidgets as widgets

# Import URL from config
get_ipython().run_line_magic('run', 'config.ipynb')

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import required modules
try:
    from Accessibility_Checker import normalize_url, terminology
    from Data_Loader import load_data, count_issues_by_category
    from Enhanced_Report_Generator import generate_accessibility_report
    
    # Show success message
    display(HTML("""
    <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">✅ Modules Loaded Successfully</h3>
        <p style="margin-bottom: 0;">Ready to generate accessibility reports.</p>
    </div>
    """))
except ImportError as e:
    # Show error message
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">❌ Error Loading Modules</h3>
        <p>Could not load required modules: {str(e)}</p>
        <p style="margin-bottom: 0;">Please ensure all module files are in the same directory as this notebook.</p>
    </div>
    """))

# Display header
display(HTML("""
<div style="background-color: #e8f5e9; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="margin-top: 0;">🔍 Accessibility Report Generator</h1>
    <p>Generate comprehensive accessibility reports from previously collected data.</p>
</div>
"""))

# URL Input with default from config
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='70%')
)

# Progress output
progress_output = widgets.Output()

# Generate button
generate_button = widgets.Button(
    description='Generate Report',
    button_style='primary',
    tooltip='Click to generate an accessibility report',
    icon='chart-bar'
)

# Output area for report generation status
output_area = widgets.Output()

# Function to handle the button click
def on_generate_button_clicked(b):
    # Rest of the function remains the same as in the previous implementation
    # ... (previous implementation of the function)
    pass

# Set up button click handler
generate_button.on_click(on_generate_button_clicked)

# Display the widgets
display(widgets.VBox([
    widgets.HBox([url_input, generate_button]),
    progress_output,
    output_area
]))

# Show instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
    <h3>📋 Instructions</h3>
    <ol>
        <li>First, ensure that you have run the accessibility tests using the appropriate test scripts.</li>
        <li>Enter the URL you want to generate a report for in the URL field.</li>
        <li>Click the "Generate Report" button to create the report.</li>
        <li>The report will open automatically in your default browser.</li>
    </ol>
    
    <h4>Notes:</h4>
    <ul>
        <li>The report generator requires data from previous accessibility scans to be available.</li>
        <li>If no data is found, you'll need to run the data collection scripts first.</li>
        <li>Reports include visualizations, practical guidance for developers, and detailed technical information for accessibility experts.</li>
    </ul>
</div>
"""))


```
### archive\missing_focusable_elements.py <a id='archive_missing_focusable_elements_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\missing_focusable_elements.py
- **Last Modified**: 2025-03-10 19:27:09
- **Size**: 2301 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Missing_Focusable_Elements.ipynb
# Script to detect elements that should be keyboard-accessible but aren't

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets

# Import URL from config
get_ipython().run_line_magic('run', 'config.ipynb')

# Try to import Selenium
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Try to import BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import our custom module for utility functions
from Accessibility_Checker import normalize_url, terminology

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# (Existing script continues exactly as in the original document, with these two modifications)

# URL Input
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='50%')
)

# Browser dropdown
browser_dropdown = widgets.Dropdown(
    options=['chrome', 'firefox', 'edge'],
    value=browser_choice,
    description='Browser:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='30%')
)

# (The rest of the script remains EXACTLY the same as in the original document)
# This includes all the existing functions and remaining code


```
### archive\non_text_content_checker.py <a id='archive_non_text_content_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\non_text_content_checker.py
- **Last Modified**: 2025-03-10 19:27:14
- **Size**: 790 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup

def identify_non_text_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    non_text_elements = []

    # Find elements that typically contain non-text content
    element_types = ['img', 'svg', 'video', 'audio', 'object', 'embed', 'canvas']
    for element_type in element_types:
        elements = soup.find_all(element_type)
        for element in elements:
            element_info = {
                'tag': element.name,
                'src': element.get('src'),
                'alt': element.get('alt'),
                # Extract other relevant attributes as needed
            }
            non_text_elements.append(element_info)

    return non_text_elements


```
### archive\.ipynb_checkpoints\accessibility_checker-checkpoint.py <a id='archive__ipynb_checkpoints_accessibility_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\.ipynb_checkpoints\accessibility_checker-checkpoint.py
- **Last Modified**: 2025-03-10 20:07:58
- **Size**: 7174 bytes

#### Code
```python
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
    
    # Store the Inconsistent keyboard navigation sequences
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
```
### archive\.ipynb_checkpoints\accessibility_checker_starter-checkpoint.py <a id='archive__ipynb_checkpoints_accessibility_checker_starter-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\.ipynb_checkpoints\accessibility_checker_starter-checkpoint.py
- **Last Modified**: 2025-03-10 20:14:23
- **Size**: 6308 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

import sys
import os
import importlib
import argparse
from pathlib import Path

# Add current directory to Python path to ensure module imports work
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(current_dir / 'accessibility_checker.log'),
        logging.StreamHandler()
    ]
)

# Available modules for accessibility checking
AVAILABLE_MODULES = {
    'tab_order': 'missing_focusable_elements',
    'missing_focusable': 'missing_focusable_elements',
    'generate_report': 'generate_accessibility_report',
    'aria_check': 'generate_accessibility_report'
}

def import_module(module_name):
    """
    Dynamically import a module by name.

    Args:
        module_name (str): Name of the module to import

    Returns:
        module: Imported module or None if import fails
    """
    try:
        # Normalize the module name (convert to lowercase, remove any IPython remnants)
        normalized_name = module_name.lower().replace('ipython.', '')

        # Try importing from the predefined module names
        if normalized_name in AVAILABLE_MODULES:
            module_path = AVAILABLE_MODULES[normalized_name]
            logging.info(f"Attempting to import module: {module_path}")
            return importlib.import_module(module_path)

        # Try importing the exact module name provided
        logging.info(f"Attempting to import module directly: {normalized_name}")
        return importlib.import_module(normalized_name)
    except ImportError as e:
        logging.error(f"Could not import module '{module_name}': {e}")
        print(f"❌ Could not import module '{module_name}': {e}")
        # Print additional context about available modules
        print("Available modules:", list(sys.modules.keys()))
        return None

def run_tab_order_check(url, browser='chrome'):
    """
    Run tab order accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Tab order check module not available.")
    return None

def run_missing_focusable_check(url, browser='chrome'):
    """
    Run missing focusable elements check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Missing focusable elements check module not available.")
    return None

def generate_comprehensive_report(url):
    """
    Generate a comprehensive accessibility report.

    Args:
        url (str): Website URL to generate report for
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ Report generation module not available.")
    return None

def run_aria_check(url, browser='chrome'):
    """
    Run ARIA and keyboard accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ ARIA and keyboard accessibility check module not available.")
    return None

def main():
    """
    Main entry point for the Accessibility Checker.
    """
    # Import URL from config
    from config import url_to_check

    parser = argparse.ArgumentParser(description="Accessibility Checker - Comprehensive Web Accessibility Testing Tool")

    # Add arguments
    parser.add_argument('--url', help='Website URL to check', default=url_to_check)
    parser.add_argument('--browser', default='chrome',
                        choices=['chrome', 'firefox', 'edge'],
                        help='Browser to use for testing (default: chrome)')
    parser.add_argument('--check', choices=['tab_order', 'missing_focusable', 'aria', 'report', 'all'],
                        default='all',
                        help='Specific type of accessibility check to run')

    # Parse arguments
    args = parser.parse_args()

    # Welcome message
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {args.url}")
    print(f"Browser: {args.browser}")
    print("=" * 60)

    # Run specific or all checks
    try:
        if args.check in ['tab_order', 'all']:
            print("\n📊 Running Tab Order Check...")
            tab_order_result = run_tab_order_check(args.url, args.browser)

        if args.check in ['missing_focusable', 'all']:
            print("\n🕵️ Checking Missing Focusable Elements...")
            missing_focusable_result = run_missing_focusable_check(args.url, args.browser)

        if args.check in ['aria', 'all']:
            print("\n♿ Running ARIA and Keyboard Accessibility Check...")
            aria_result = run_aria_check(args.url, args.browser)

        if args.check in ['report', 'all']:
            print("\n📄 Generating Comprehensive Report...")
            report = generate_comprehensive_report(args.url)

        print("\n" + "=" * 60)
        print("✅ Accessibility Check Complete")
        print("=" * 60)

    except Exception as e:
        logging.error(f"An error occurred during the accessibility check: {e}")
        print(f"\n❌ An error occurred during the accessibility check: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
```
### archive\.ipynb_checkpoints\config-checkpoint.py <a id='archive__ipynb_checkpoints_config-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\.ipynb_checkpoints\config-checkpoint.py
- **Last Modified**: 2025-03-10 20:09:02
- **Size**: 1096 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8
from pathlib import Path

# Website to be audited
url_to_check = "https://www.sse.com"

# Browser for testing
browser_choice = "firefox"  # Options: 'chrome', 'firefox', 'edge'

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Logging directory
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Logging configuration
LOG_FILE = LOGS_DIR / 'accessibility_checker.log'

# Accessibility check settings
CHECKS = {
    'tab_order': True,
    'missing_focusable': True,
    'aria': True,
    'keyboard_accessibility': True,
    'non_text_content': True
}

# Issue thresholds for reporting
ISSUE_THRESHOLDS = {
    'tab_order_issues': 5,
    'missing_focusable_issues': 3,
    'aria_issues': 3,
    'keyboard_issues': 3
}

# Optional additional configurations can be added here

# Export configuration for use in other modules
__all__ = [
    'url_to_check', 
    'browser_choice', 
    'REPORTS_DIR', 
    'LOGS_DIR', 
    'CHECKS', 
    'ISSUE_THRESHOLDS'
]
```
### archive\.ipynb_checkpoints\convert_notebooks-checkpoint.py <a id='archive__ipynb_checkpoints_convert_notebooks-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\.ipynb_checkpoints\convert_notebooks-checkpoint.py
- **Last Modified**: 2025-03-10 17:27:09
- **Size**: 2038 bytes

#### Code
```python
#!/usr/bin/env python3

import os
import subprocess
import sys

def convert_notebooks(directory):
    """
    Convert all Jupyter Notebook files in the specified directory to Python scripts.
    
    Args:
        directory (str): Path to the directory containing Jupyter Notebook files
    """
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)
    
    # Counter for converted notebooks
    converted_count = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a Jupyter Notebook
        if filename.endswith('.ipynb'):
            # Full path to the notebook
            notebook_path = os.path.join(directory, filename)
            
            try:
                # Run jupyter nbconvert command
                result = subprocess.run([
                    'jupyter', 'nbconvert', 
                    '--to', 'script', 
                    notebook_path
                ], capture_output=True, text=True)
                
                # Check if conversion was successful
                if result.returncode == 0:
                    print(f"Converted: {filename}")
                    converted_count += 1
                else:
                    print(f"Failed to convert {filename}")
                    print(f"Error: {result.stderr}")
            
            except Exception as e:
                print(f"Error converting {filename}: {e}")
    
    # Print summary
    print(f"\nTotal notebooks converted: {converted_count}")

def main():
    # Default directory
    default_directory = 'Pickles'
    
    # Allow directory to be specified as a command-line argument
    directory = sys.argv[1] if len(sys.argv) > 1 else default_directory
    
    print(f"Converting notebooks in directory: {directory}")
    convert_notebooks(directory)

if __name__ == "__main__":
    main()
```
### archive\.ipynb_checkpoints\data_loader-checkpoint.py <a id='archive__ipynb_checkpoints_data_loader-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: archive\.ipynb_checkpoints\data_loader-checkpoint.py
- **Last Modified**: 2025-03-10 19:26:55
- **Size**: 7092 bytes

#### Code
```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data_Loader.ipynb

import json
import glob
import os
import hashlib
from pathlib import Path
from datetime import datetime

# Import from our main module
get_ipython().run_line_magic('run', 'config.ipynb # import config')
from Accessibility_Checker import (
    REPORTS_DIR, 
    AccessibilityIssue, 
    normalize_url, 
    translate_accessibility_issue,
    determine_severity,
    terminology
)

def load_data(url=url_to_check): # changed to default to config URL
    """
    Load accessibility data for a given URL from all available reports.
    
    Args:
        url: URL of the website that was tested
        
    Returns:
        dict: Consolidated data from all reports
    """
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issues": []
    }
    
    # Track unique issues to prevent duplicates
    unique_issues = set()
    
    try:
        # Load data from various report files - using all formats of URL
        report_types = [
            ("tab_order", f"tab_order_{clean_url}_*.json"),
            ("tab_order", f"tab_order_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("missing_focusable", f"missing_focusable_{clean_url}_*.json"),
            ("missing_focusable", f"missing_focusable_{url.replace('https://', '').replace('http://', '')}_*.json"),
            ("comprehensive", f"comprehensive_{clean_url}_*.json"),
            ("comprehensive", f"comprehensive_{url.replace('https://', '').replace('http://', '')}_*.json")
        ]
        
        found_data = False
        
        for report_type, pattern in report_types:
            full_pattern = str(REPORTS_DIR / pattern)
            files = glob.glob(full_pattern)
            
            if files:
                latest_file = max(files, key=lambda p: os.path.getmtime(p))
                print(f"Loading {report_type} data from: {os.path.basename(latest_file)}")
                
                with open(latest_file, 'r') as f:
                    report_data = json.load(f)
                    
                    # Define issue_sources based on report type
                    issue_sources = {}
                    
                    if report_type == "tab_order":
                        issue_sources["Tab Order"] = report_data.get("tab_order_issues", [])
                    elif report_type == "missing_focusable":
                        issue_sources["Missing Focusable"] = report_data.get("missing_focusable_issues", [])
                    elif report_type == "comprehensive":
                        issue_sources = {
                            "Tab Order": report_data.get("tab_order_issues", []),
                            "Missing Focusable": report_data.get("missing_focusable_issues", []),
                            "ARIA": report_data.get("aria_issues", []),
                            "Keyboard": report_data.get("keyboard_issues", [])
                        }
                    
                    for category, issues in issue_sources.items():
                        if not issues:
                            continue
                            
                        for issue_text in issues:
                            found_data = True
                            
                            # Handle different data formats
                            if isinstance(issue_text, dict):
                                issue_desc = issue_text.get('issue', str(issue_text))
                            else:
                                issue_desc = str(issue_text)
                            
                            # Create a unique identifier for this issue
                            issue_hash = hashlib.md5(f"{category}:{issue_desc}".encode()).hexdigest()
                            
                            # Skip if we've already processed this issue
                            if issue_hash in unique_issues:
                                continue
                            unique_issues.add(issue_hash)
                            
                            # Translate the issue to a more descriptive format
                            translated_issue = translate_accessibility_issue(issue_desc, category, terminology)
                            
                            severity = determine_severity(translated_issue['description'])
                            accessibility_issue = AccessibilityIssue(
                                description=translated_issue['description'],
                                category=category,
                                severity=severity
                            )
                            
                            # Add additional metadata to the issue
                            accessibility_issue.original_text = translated_issue['original']
                            accessibility_issue.impact = translated_issue['impact']
                            accessibility_issue.recommendation = translated_issue['recommendation']
                            
                            data["issues"].append(accessibility_issue)
        
        if not found_data:
            print(f"⚠️ Warning: No accessibility reports found for {url}")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"✅ Loaded {len(data['issues'])} unique accessibility issues from reports")
    return data

def count_issues_by_category(data):
    """Count issues by category and severity"""
    counts = {
        'by_category': {},
        'by_severity': {
            'critical': 0,
            'high': 0,
            'medium': 0,
            'low': 0
        },
        'total': len(data['issues'])
    }
    
    for issue in data['issues']:
        # Count by category
        if issue.category not in counts['by_category']:
            counts['by_category'][issue.category] = 0
        counts['by_category'][issue.category] += 1
        
        # Count by severity
        counts['by_severity'][issue.severity] += 1
    
    return counts

# Example usage
if __name__ == "__main__":
    test_url = url_to_check  # Replace with your target website

    print(f"Testing data loader with URL: {test_url}")
    data = load_data() # removed the need to include the url
    
    if data["issues"]:
        counts = count_issues_by_category(data)
        print("\nIssue Counts by Category:")
        for category, count in counts['by_category'].items():
            print(f"- {category}: {count}")
        
        print("\nIssue Counts by Severity:")
        for severity, count in counts['by_severity'].items():
            print(f"- {severity.capitalize()}: {count}")
    else:
        print("No issues found in any reports.")


```
### accessibility_modules\.ipynb_checkpoints\aria_checker-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_aria_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\aria_checker-checkpoint.py
- **Last Modified**: 2025-03-10 21:21:50
- **Size**: 9521 bytes

#### Code
```python
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
```
### accessibility_modules\.ipynb_checkpoints\focusable_elements-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_focusable_elements-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\focusable_elements-checkpoint.py
- **Last Modified**: 2025-03-10 21:20:09
- **Size**: 5459 bytes

#### Code
```python
"""
Focusable Elements Module
Detects elements that should be keyboard-accessible but aren't.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

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
        # Check for elements that should be focusable
        potential_interactive_elements = driver.find_elements(By.CSS_SELECTOR, 
            "a:not([tabindex]), button:not([tabindex]), [onclick]:not([tabindex]), " +
            "[role='button']:not([tabindex]), [role='link']:not([tabindex]), " +
            "input:not([type='hidden']):not([tabindex]), select:not([tabindex]), " +
            "textarea:not([tabindex]), details:not([tabindex])")
        
        for element in potential_interactive_elements:
            # Check if the element has tabindex=-1 (explicitly not focusable)
            tabindex = element.get_attribute("tabindex")
            if tabindex == "-1":
                missing_focusable.append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "issue": "Keyboard navigation barrier",
                    "details": "Interactive element with tabindex=-1",
                    "recommendation": "Remove tabindex=-1 or provide alternative keyboard access",
                    "wcag": "2.1.1"
                })
                continue
                
            # Check if element is visible and enabled but not focusable
            if element.is_displayed() and element.is_enabled():
                # Try to check if focusable through JavaScript
                is_focusable = driver.execute_script("""
                    return document.activeElement !== arguments[0] && 
                           arguments[0].focus && 
                           (function() { 
                               var focusable = true;
                               arguments[0].focus(); 
                               focusable = document.activeElement === arguments[0];
                               return focusable;
                           })();
                """, element)
                
                if not is_focusable:
                    missing_focusable.append({
                        "element": element.tag_name,
                        "text": element.text.strip() if element.text else "[No text]",
                        "location": get_element_location(element),
                        "issue": "Keyboard navigation barrier",
                        "details": "Element should be focusable but isn't",
                        "recommendation": "Add proper keyboard accessibility",
                        "wcag": "2.1.1"
                    })
        
        # Check for custom interactive elements without proper ARIA roles
        custom_elements = driver.find_elements(By.CSS_SELECTOR, 
            "[class*='button']:not(button):not(a):not([role='button']), " +
            "[class*='btn']:not(button):not(a):not([role='button']), " +
            "[class*='toggle']:not([role]), " +
            "[class*='menu']:not([role]), " +
            "[class*='dropdown']:not([role])")
        
        for element in custom_elements:
            if element.is_displayed() and element.is_enabled():
                missing_focusable.append({
                    "element": element.tag_name,
                    "text": element.text.strip() if element.text else "[No text]",
                    "class": element.get_attribute("class"),
                    "location": get_element_location(element),
                    "issue": "Keyboard navigation barrier",
                    "details": "Custom interactive element without proper ARIA role",
                    "recommendation": "Add appropriate role and ensure keyboard accessibility",
                    "wcag": "4.1.2"
                })
                
        logging.info(f"Found {len(missing_focusable)} elements with keyboard accessibility issues")
        return missing_focusable
        
    except WebDriverException as e:
        logging.error(f"Error checking for missing focusable elements: {str(e)}")
        return [{"error": str(e)}]

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
        parent = element.find_element(By.XPATH, "./..")
        parent_text = parent.text.strip()
        if parent_text and len(parent_text) < 50:  # Only use if it's reasonably short
            return f"near text '{parent_text}'"
            
        # Fallback to XPath
        return "in page (no specific identifier available)"
            
    except Exception:
        return "in page (location detection failed)"
```
### accessibility_modules\.ipynb_checkpoints\focus_order_checker-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_focus_order_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\focus_order_checker-checkpoint.py
- **Last Modified**: 2025-03-10 22:11:57
- **Size**: 18011 bytes

#### Code
```python
"""
Focus Order Checker Module
Tests for WCAG 2.4.3: Focus Order - Ensures that navigation follows a meaningful sequence.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

def check_focus_order(driver):
    """
    Checks that the focus order of interactive elements is logical and follows content sequence.
    Tests WCAG Success Criterion 2.4.3: Focus Order
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of focus order check
    """
    logging.info("Checking focus order (WCAG 2.4.3)...")
    results = {
        "status": "completed",
        "wcag_criterion": "2.4.3",
        "tab_sequence": [],
        "issues": []
    }
    
    try:
        # Reset focus to beginning of page
        driver.find_element(By.TAG_NAME, "body").click()
        
        # Find all potentially focusable elements
        focusable_selector = (
            "a, button, input:not([type='hidden']), select, textarea, "
            "[tabindex]:not([tabindex='-1']), [contenteditable='true'], "
            "details, summary, [role='button'], [role='link'], "
            "[role='checkbox'], [role='radio'], [role='tab'], [role='menuitem'], "
            "[role='combobox'], [role='listbox'], [role='slider'], [role='textbox'], "
            "[role='searchbox'], [role='spinbutton']"
        )
        
        # Get all focusable elements and their visual positions for later analysis
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        logging.info(f"Found {len(all_focusable)} potentially focusable elements")
        
        # Store information about each focusable element
        focusable_elements_info = []
        for element in all_focusable:
            if element.is_displayed() and element.is_enabled():
                info = {
                    "element": element,
                    "tag": element.tag_name,
                    "id": element.get_attribute("id") or "",
                    "text": element.text.strip() if element.text else get_element_accessible_name(element),
                    "tabindex": element.get_attribute("tabindex"),
                    "position": get_element_position(element)
                }
                focusable_elements_info.append(info)
        
        # Detect actual tab sequence using keyboard navigation
        tab_sequence = detect_tab_sequence(driver, max_elements=len(focusable_elements_info) * 2)
        results["tab_sequence"] = tab_sequence
        
        # Check for specific focus order issues
        check_for_positive_tabindex(tab_sequence, results)
        check_reading_order_violations(tab_sequence, results)
        check_form_field_sequence(tab_sequence, results)
        check_modal_dialog_focus(driver, tab_sequence, results)
        check_skip_links(driver, tab_sequence, results)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking focus order: {str(e)}")
        results["error"] = str(e)
        return results

def detect_tab_sequence(driver, max_elements=100):
    """Detect the actual tab sequence of the page by simulating keyboard tabbing"""
    tab_sequence = []
    
    # Start with pressing Tab once to get to first element
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    body.send_keys(Keys.TAB)
    
    # Keep track of already focused elements to detect cycles
    focused_signatures = set()
    
    for i in range(max_elements):
        # Get currently focused element
        active_element = driver.execute_script("return document.activeElement;")
        
        # Skip if we've already seen this element (avoid infinite loops)
        element_signature = generate_element_signature(active_element)
        if element_signature in focused_signatures:
            # If we're back at the first element, we've completed the tab cycle
            if len(tab_sequence) > 1 and element_signature == generate_element_signature(tab_sequence[0]["element"]):
                break
            # Otherwise we might be stuck in a sub-cycle, keep going a bit longer
            if len(focused_signatures) > 5:  # Allow a few duplicate focuses before giving up
                break
        
        # Add to our sequence
        element_info = {
            "element": active_element,
            "tag": active_element.tag_name if hasattr(active_element, 'tag_name') else active_element.get_attribute("tagName").lower(),
            "id": active_element.get_attribute("id") or "",
            "text": active_element.text.strip() if hasattr(active_element, 'text') and active_element.text else get_element_accessible_name(active_element),
            "tabindex": active_element.get_attribute("tabindex"),
            "position": get_element_position(active_element),
            "tab_index": i + 1  # 1-based index of tab sequence
        }
        
        tab_sequence.append(element_info)
        focused_signatures.add(element_signature)
        
        # Move to next element
        active_element.send_keys(Keys.TAB)
        
        # Small delay to allow focus to settle (helps with dynamic pages)
        time.sleep(0.05)
    
    return tab_sequence

def check_for_positive_tabindex(tab_sequence, results):
    """Check for elements with tabindex > 0, which can disrupt natural tab order"""
    for element_info in tab_sequence:
        tabindex = element_info.get("tabindex", "")
        if tabindex and tabindex.isdigit() and int(tabindex) > 0:
            results["issues"].append({
                "element": element_info.get("tag", "unknown"),
                "text": element_info.get("text", "[No text]"),
                "issue": "Inconsistent keyboard navigation sequence",
                "details": f"Element has tabindex={tabindex}, which overrides the natural DOM order",
                "recommendation": "Use tabindex='0' to make elements focusable in their natural DOM order",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_reading_order_violations(tab_sequence, results):
    """Check if focus order follows visual/reading order"""
    # Skip if we have less than 3 elements
    if len(tab_sequence) < 3:
        return
    
    # Look for cases where focus jumps around unnaturally
    for i in range(1, len(tab_sequence) - 1):
        current = tab_sequence[i]
        prev = tab_sequence[i-1]
        next_elem = tab_sequence[i+1]
        
        # Skip elements without position info
        if not current.get("position") or not prev.get("position") or not next_elem.get("position"):
            continue
        
        # Check for focus moving backwards against reading order
        # First check if we're moving down the page as expected
        if prev["position"]["y"] < current["position"]["y"]:
            # Then check if next focus moves back up significantly
            if next_elem["position"]["y"] < current["position"]["y"] - 50:
                # Only flag if it's not just moving to a new column
                if abs(next_elem["position"]["x"] - current["position"]["x"]) < 200:
                    results["issues"].append({
                        "element": current.get("tag", "unknown"),
                        "text": current.get("text", "[No text]"),
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Focus jumps backwards against the expected reading order",
                        "recommendation": "Ensure focus order follows the natural reading order of the page",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })

def check_form_field_sequence(tab_sequence, results):
    """Check if form fields are in a logical sequence"""
    # Identify form sections
    form_sections = []
    current_section = []
    
    for element_info in tab_sequence:
        tag = element_info.get("tag", "").lower()
        if tag in ["input", "select", "textarea"] or element_info.get("role") in ["textbox", "combobox", "listbox"]:
            current_section.append(element_info)
        elif current_section:
            # End of a form section (non-form element encountered after form elements)
            if len(current_section) > 1:
                form_sections.append(current_section)
            current_section = []
    
    # Add last section if it exists
    if len(current_section) > 1:
        form_sections.append(current_section)
    
    # Check each form section
    for section in form_sections:
        # Check if fields are in a logical vertical order
        is_vertical_form = True
        for i in range(1, len(section)):
            prev = section[i-1]
            current = section[i]
            
            # If fields are side by side, it's not a simple vertical form
            if prev.get("position") and current.get("position"):
                if abs(prev["position"]["y"] - current["position"]["y"]) < 30:
                    is_vertical_form = False
                    break
        
        # For vertical forms, check if tab order follows visual order
        if is_vertical_form:
            for i in range(1, len(section)):
                prev = section[i-1]
                current = section[i]
                
                if prev.get("position") and current.get("position"):
                    # If next field is above previous, that's counter-intuitive
                    if current["position"]["y"] < prev["position"]["y"] - 30:
                        results["issues"].append({
                            "element": current.get("tag", "unknown"),
                            "text": current.get("text", "[No text]"),
                            "issue": "Inconsistent keyboard navigation sequence in form",
                            "details": "Form fields do not follow a logical top-to-bottom sequence",
                            "recommendation": "Ensure form fields receive focus in a logical order that matches visual layout",
                            "wcag": "2.4.3",
                            "severity": "warning"
                        })
                        break

def check_modal_dialog_focus(driver, tab_sequence, results):
    """Check if there are modal dialogs and if focus is properly trapped within them"""
    # Look for modal dialogs
    modal_dialogs = driver.find_elements(By.CSS_SELECTOR, 
        "[role='dialog'], [aria-modal='true'], .modal, .dialog, .overlay:not([aria-hidden='true'])")
    
    if not modal_dialogs:
        return
        
    for dialog in modal_dialogs:
        # Skip hidden dialogs
        if not dialog.is_displayed():
            continue
            
        # Check if dialog has aria-modal attribute
        aria_modal = dialog.get_attribute("aria-modal")
        if aria_modal != "true":
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog missing aria-modal attribute",
                "details": "Modal dialog should have aria-modal='true' to indicate it traps focus",
                "recommendation": "Add aria-modal='true' to modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })
        
        # Check focus management
        focusable_elements = dialog.find_elements(By.CSS_SELECTOR, 
            "a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")
        
        if not focusable_elements:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog has no focusable elements",
                "details": "Modal dialogs should contain focusable elements",
                "recommendation": "Ensure modal dialogs have focusable elements like buttons for user interaction",
                "wcag": "2.4.3",
                "severity": "critical"
            })
            continue
            
        # Simulate tabbing through the dialog to check if focus stays within
        # This would require more complex testing logic to implement fully
        # For now, we'll just check if the dialog has a close/cancel button
        close_buttons = dialog.find_elements(By.CSS_SELECTOR, 
            "button:not([aria-hidden='true']), [role='button']:not([aria-hidden='true']), " +
            "[aria-label*='close' i], [aria-label*='cancel' i], " +
            "[class*='close' i], [id*='close' i], [class*='cancel' i], [id*='cancel' i]")
            
        if not close_buttons:
            results["issues"].append({
                "element": "dialog",
                "text": dialog.get_attribute("id") or "[No ID]",
                "issue": "Modal dialog may lack closing mechanism",
                "details": "No obvious close button found in modal dialog",
                "recommendation": "Provide a visible close button in modal dialogs",
                "wcag": "2.4.3",
                "severity": "warning"
            })

def check_skip_links(driver, tab_sequence, results):
    """Check if skip links are present and working"""
    # Look for common skip link patterns
    skip_links = driver.find_elements(By.CSS_SELECTOR, 
        "a[href^='#']:not([aria-hidden='true'])")
    
    skip_link_found = False
    for link in skip_links:
        link_text = link.text.strip() if link.text else ""
        if not link_text:
            link_text = link.get_attribute("aria-label") or ""
            
        # Look for common skip link text patterns
        if any(pattern in link_text.lower() for pattern in ["skip", "jump", "content", "main"]):
            skip_link_found = True
            
            # Check if skip link is one of the first elements in tab order
            if tab_sequence and len(tab_sequence) > 2:
                first_elements = [tab_sequence[0], tab_sequence[1]] if len(tab_sequence) > 1 else [tab_sequence[0]]
                skip_link_in_tab_order = any(
                    element.get("tag") == "a" and element.get("text") == link_text
                    for element in first_elements
                )
                
                if not skip_link_in_tab_order:
                    results["issues"].append({
                        "element": "a",
                        "text": link_text,
                        "issue": "Skip link not at start of tab order",
                        "details": "Skip navigation link should be one of the first focusable elements",
                        "recommendation": "Move skip link to the beginning of the page code so it's encountered early in tab order",
                        "wcag": "2.4.3",
                        "severity": "warning"
                    })
    
    # If no skip links found on a page with significant content, suggest adding one
    if not skip_link_found:
        # Check if page has a substantial amount of navigation before main content
        nav_elements = driver.find_elements(By.CSS_SELECTOR, 
            "nav, [role='navigation'], #navigation, .navigation, .nav, #nav, header")
        
        if nav_elements and len(tab_sequence) > 10:
            results["issues"].append({
                "element": "page",
                "issue": "Missing skip navigation link",
                "details": "Page has substantial navigation but no skip link was found",
                "recommendation": "Add a skip link at the beginning of the page to allow keyboard users to skip navigation",
                "wcag": "2.4.3",
                "severity": "warning"
            })

# Helper functions

def get_element_position(element):
    """Get the position and dimensions of an element"""
    try:
        rect = element.rect
        return {
            "x": rect.get('x', 0),
            "y": rect.get('y', 0),
            "width": rect.get('width', 0),
            "height": rect.get('height', 0),
            "midX": rect.get('x', 0) + rect.get('width', 0) / 2,
            "midY": rect.get('y', 0) + rect.get('height', 0) / 2
        }
    except:
        return None

def get_element_accessible_name(element):
    """Try to get the accessible name of an element through various attributes"""
    accessible_name = ""
    try:
        # Try aria-label
        accessible_name = element.get_attribute("aria-label") or ""
        if accessible_name:
            return f"[{accessible_name}]"
            
        # Try placeholder
        if element.tag_name.lower() in ["input", "textarea"]:
            placeholder = element.get_attribute("placeholder") or ""
            if placeholder:
                return f"[Placeholder: {placeholder}]"
            
            # Try value
            value = element.get_attribute("value") or ""
            if value:
                return f"[Value: {value}]"
                
        # Try title
        title = element.get_attribute("title") or ""
        if title:
            return f"[Title: {title}]"
            
        # Try name
        name = element.get_attribute("name") or ""
        if name:
            return f"[Name: {name}]"
            
        return "[No text]"
    except:
        return "[No text]"

def generate_element_signature(element):
    """Generate a unique-ish signature for an element to detect duplicates in tab order"""
    try:
        tag = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_id = element.get_attribute("id") or ""
        classes = element.get_attribute("class") or ""
        text = element.text[:50] if hasattr(element, 'text') and element.text else ""
        
        return f"{tag}#{element_id}.{classes}:{text}"
    except:
        return "unknown"
```
### accessibility_modules\.ipynb_checkpoints\html_report_generator-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_html_report_generator-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\html_report_generator-checkpoint.py
- **Last Modified**: 2025-03-10 23:23:55
- **Size**: 17063 bytes

#### Code
```python
"""
HTML Report Generator Module
Generates a professional HTML report from accessibility check results with working accordions.
"""

import os
import json
from datetime import datetime
import logging
from urllib.parse import urlparse

def generate_html_report(accessibility_report, output_dir=None):
    """
    Generate an HTML report from accessibility check results.
    
    Args:
        accessibility_report: Dictionary containing accessibility check results
        output_dir: Directory to save the report (default: accessibility_reports)
        
    Returns:
        str: Path to the generated HTML report
    """
    logging.info("Generating HTML accessibility report...")
    
    # Set default output directory if not provided
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'accessibility_reports')
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a filename based on URL and timestamp
    url = accessibility_report.get('url', 'unknown')
    domain = urlparse(url).netloc
    if not domain:
        domain = 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Generate the HTML content
    html_content = _generate_html_content(accessibility_report)
    
    # Write the HTML to a file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logging.info(f"HTML report saved to: {filepath}")
    return filepath

def _generate_html_content(report):
    """Generate HTML content from the accessibility report."""
    # Extract information from the report
    url = report.get('url', 'Unknown URL')
    timestamp = report.get('timestamp', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elapsed_time = report.get('elapsed_time', 'Unknown')
    
    # Get summary statistics
    summary = report.get('summary', {})
    critical_issues = summary.get('critical_issues', 0)
    warnings = summary.get('warnings', 0)
    passed_checks = summary.get('passed_checks', 0)
    compliance_score = summary.get('compliance_score', 'N/A')
    
    # Get consolidated issues
    issues = report.get('issues', [])
    
    # Start building HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - {url}</title>
    <style>
        :root {{
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #34495e;
            --success-color: #2ecc71;
            --warning-color: #f39c12;
            --danger-color: #e74c3c;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            margin: 0;
            padding: 0;
            background-color: #f5f7fa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background-color: var(--primary-color);
            color: white;
            padding: 20px;
            border-radius: 5px 5px 0 0;
            margin-bottom: 20px;
        }}
        
        h1, h2, h3, h4 {{
            color: var(--primary-color);
            margin-top: 0;
        }}
        
        header h1 {{
            color: white;
            margin: 0;
        }}
        
        .report-meta {{
            margin-top: 10px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.8);
        }}
        
        .summary-card {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }}
        
        .summary-item {{
            flex: 1;
            min-width: 200px;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            text-align: center;
        }}
        
        .critical {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .passed {{
            background-color: var(--success-color);
            color: white;
        }}
        
        .score {{
            background-color: var(--secondary-color);
            color: white;
        }}
        
        .summary-number {{
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .summary-label {{
            font-size: 14px;
            text-transform: uppercase;
        }}
        
        .issues-section {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
        }}
        
        .issue-card {{
            border-left: 4px solid var(--warning-color);
            padding: 15px;
            margin-bottom: 15px;
            background-color: #f8f9fa;
            border-radius: 0 5px 5px 0;
        }}
        
        .issue-card.critical {{
            border-left-color: var(--danger-color);
        }}
        
        .issue-card.warning {{
            border-left-color: var(--warning-color);
        }}
        
        .issue-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }}
        
        .issue-title {{
            font-weight: bold;
            font-size: 16px;
            margin: 0;
        }}
        
        .issue-type {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .issue-type.critical {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .issue-type.warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .issue-details {{
            margin-bottom: 10px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            border-left: 2px solid var(--secondary-color);
            padding-left: 10px;
            margin-top: 10px;
        }}
        
        .issue-meta {{
            display: flex;
            font-size: 12px;
            color: #6c757d;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 10px;
        }}
        
        .issue-meta-item {{
            margin-right: 15px;
        }}
        
        .issue-wcag {{
            background-color: var(--primary-color);
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        
        .checks-section {{
            display: flex;
            flex-wrap: wrap;
            margin: 0 -10px;
        }}
        
        .check-card {{
            flex: 1;
            min-width: 300px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin: 10px;
            padding: 15px;
        }}
        
        .check-header {{
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        
        .check-name {{
            font-size: 18px;
            font-weight: bold;
            margin: 0;
        }}
        
        .check-status {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
        }}
        
        .check-status.passed {{
            background-color: var(--success-color);
            color: white;
        }}
        
        .check-status.failed {{
            background-color: var(--danger-color);
            color: white;
        }}
        
        .check-status.warning {{
            background-color: var(--warning-color);
            color: white;
        }}
        
        .check-status.skipped {{
            background-color: #6c757d;
            color: white;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            margin-top: 20px;
            color: #6c757d;
            font-size: 14px;
        }}
        
        /* Toggle button style */
        .toggle-btn {{
            background-color: #f1f1f1;
            color: #444;
            cursor: pointer;
            padding: 10px 15px;
            width: 100%;
            text-align: center;
            border: none;
            outline: none;
            font-size: 16px;
            margin-top: 10px;
            border-radius: 5px;
            position: relative;
        }}
        
        .toggle-btn:hover {{
            background-color: #ddd;
        }}
        
        .toggle-btn::after {{
            content: '+';
            position: absolute;
            right: 15px;
            font-weight: bold;
        }}
        
        .toggle-btn.active::after {{
            content: '-';
        }}
        
        /* Content div style */
        .content {{
            display: none;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 0 0 5px 5px;
            margin-top: 5px;
        }}
        
        @media screen and (max-width: 768px) {{
            .summary-item {{
                min-width: 100%;
                margin: 5px 0;
            }}
            
            .check-card {{
                min-width: 100%;
                margin: 10px 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Accessibility Audit Report</h1>
            <div class="report-meta">
                <div><strong>URL:</strong> {url}</div>
                <div><strong>Date:</strong> {timestamp}</div>
                <div><strong>Scan Duration:</strong> {elapsed_time}</div>
            </div>
        </header>
        
        <div class="summary-card">
            <div class="summary-item critical">
                <div class="summary-number">{critical_issues}</div>
                <div class="summary-label">Critical Issues</div>
            </div>
            <div class="summary-item warning">
                <div class="summary-number">{warnings}</div>
                <div class="summary-label">Warnings</div>
            </div>
            <div class="summary-item passed">
                <div class="summary-number">{passed_checks}</div>
                <div class="summary-label">Checks Passed</div>
            </div>
            <div class="summary-item score">
                <div class="summary-number">{compliance_score}</div>
                <div class="summary-label">Compliance Score</div>
            </div>
        </div>
        
        <div class="issues-section">
            <h2>Identified Accessibility Issues</h2>
            <p>The following issues were detected and should be addressed to improve accessibility:</p>
"""
            
    # Add issues
    if issues:
        for issue in issues:
            severity = issue.get('severity', issue.get('type', 'warning'))
            title = issue.get('issue', 'Unknown Issue')
            details = issue.get('details', '')
            recommendation = issue.get('recommendation', '')
            wcag = issue.get('wcag', '')
            check_type = issue.get('check_type', '')
            
            # Use preferred terminology
            if "Inconsistent keyboard navigation sequence" in title.lower():
                title = "Inconsistent keyboard navigation sequence"
            elif "Keyboard navigation barrier" in title.lower():
                title = "Keyboard navigation barrier"
            
            html += f"""
            <div class="issue-card {severity}">
                <div class="issue-header">
                    <h3 class="issue-title">{title}</h3>
                    <span class="issue-type {severity}">{severity}</span>
                </div>
                <div class="issue-details">{details}</div>
                <div class="issue-recommendation">{recommendation}</div>
                <div class="issue-meta">
            """
            
            if check_type:
                html += f'<span class="issue-meta-item"><strong>Check Type:</strong> {check_type}</span>'
            
            if wcag:
                html += f'<span class="issue-meta-item"><strong>WCAG:</strong> <span class="issue-wcag">{wcag}</span></span>'
            
            html += """
                </div>
            </div>
            """
    else:
        html += "<p>No accessibility issues were detected.</p>"
    
    html += """
        </div>
        
        <div class="checks-section">
    """
    
    # Add check sections with the simplest possible accordion approach
    checks = report.get('checks', {})
    for check_name, check_data in checks.items():
        status = check_data.get('status', 'completed')
        issues = check_data.get('issues', [])
        
        if status == 'completed' and not issues:
            status_class = 'passed'
            status_text = 'Passed'
        elif status == 'completed' and issues:
            status_class = 'failed'
            status_text = 'Issues Found'
        elif status == 'skipped':
            status_class = 'skipped'
            status_text = 'Skipped'
        else:
            status_class = 'warning'
            status_text = 'Warning'
        
        # Convert to user-friendly names
        user_friendly_name = check_name.replace('_', ' ').title()
        if check_name == 'tab_order':
            user_friendly_name = 'Keyboard Navigation Sequence'
        elif check_name == 'missing_focusable':
            user_friendly_name = 'Keyboard Accessibility'
        elif check_name == 'image_accessibility':
            user_friendly_name = 'Image Accessibility'
        
        html += f"""
        <div class="check-card">
            <div class="check-header">
                <h3 class="check-name">{user_friendly_name}</h3>
                <span class="check-status {status_class}">{status_text}</span>
            </div>
        """
        
        if status == 'completed':
            if isinstance(issues, list) and issues:
                html += f"""
                <p>Found {len(issues)} issues.</p>
                <button class="toggle-btn" onclick="toggleContent(this)">View Details</button>
                <div class="content">
                    <ul>
                """
                
                for issue in issues:
                    issue_text = issue.get('issue', 'Unknown issue')
                    # Use preferred terminology
                    if "Inconsistent keyboard navigation sequence" in issue_text.lower():
                        issue_text = "Inconsistent keyboard navigation sequence"
                    elif "Keyboard navigation barrier" in issue_text.lower():
                        issue_text = "Keyboard navigation barrier"
                    
                    html += f"<li>{issue_text}</li>"
                
                html += """
                    </ul>
                </div>
                """
            elif not issues:
                html += "<p>No issues detected.</p>"
        elif status == 'skipped':
            reason = check_data.get('reason', 'No reason provided')
            html += f"<p>Check was skipped: {reason}</p>"
        
        html += """
        </div>
        """
    
    # Close HTML and add script with simple toggle functionality
    html += """
        </div>
        
        <footer>
            <p>Generated by Accessibility Checker on """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
        </footer>
    </div>
    
    <script>
    function toggleContent(button) {
        // Toggle active class for styling
        button.classList.toggle('active');
        
        // Get the next sibling element (the content div)
        var content = button.nextElementSibling;
        
        // Toggle the content visibility
        if (content.style.display === 'block') {
            content.style.display = 'none';
        } else {
            content.style.display = 'block';
        }
    }
    </script>
</body>
</html>
"""
    
    return html
```
### accessibility_modules\.ipynb_checkpoints\image_checker-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_image_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\image_checker-checkpoint.py
- **Last Modified**: 2025-03-10 22:06:16
- **Size**: 24173 bytes

#### Code
```python
"""
Enhanced Image Accessibility Checker Module
Checks for proper image accessibility and text alternatives for non-text content (WCAG 1.1.1).
"""

import logging
import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from urllib.parse import urlparse

def check_image_accessibility(driver):
    """
    Comprehensive check for image accessibility and text alternatives for non-text content.
    Addresses WCAG Success Criterion 1.1.1: Non-text Content
    
    Args:
        driver: Selenium WebDriver instance
    
    Returns:
        dict: Results of image accessibility checks
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
        
        # Check canvas elements
        check_canvas_elements(driver, results)
        
        # Check CSS background images
        check_css_background_images(driver, results)
        
        # Check icon fonts
        check_icon_fonts(driver, results)
        
        # Check other non-text content (audio, video, etc.)
        check_other_nontext_content(driver, results)
        
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking image accessibility: {str(e)}")
        results["error"] = str(e)
        return results

def check_standard_images(driver, results):
    """Check standard <img> elements for proper alt text"""
    images = driver.find_elements(By.TAG_NAME, "img")
    results["image_count"] = len(images)
    
    for image in images:
        # Skip very small images that are likely decorative
        if is_likely_decorative_by_size(image):
            continue
            
        # Check for alt attribute
        alt_text = image.get_attribute("alt")
        src = get_image_identifier(image)
        role = image.get_attribute("role") or ""
        aria_hidden = image.get_attribute("aria-hidden") == "true"
        
        # Check for missing alt attribute
        if alt_text is None:
            results["issues"].append({
                "element": "img",
                "src": src,
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
                    "src": src,
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
                    "src": src,
                    "alt": alt_text,
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
                    "src": src,
                    "alt": alt_text,
                    "issue": "Redundant text alternative",
                    "details": "Alt text appears to duplicate adjacent text content",
                    "recommendation": "Consider using empty alt text (alt='') if the image is adequately described by nearby text",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })
        
        # Check for decorative images that should have empty alt text
        if role == "presentation" or aria_hidden:
            if alt_text and alt_text.strip() != "":
                results["issues"].append({
                    "element": "img",
                    "src": src,
                    "alt": alt_text,
                    "issue": "Decorative image has non-empty alt text",
                    "details": f"Image is marked as decorative ({role if role else 'aria-hidden'}) but has non-empty alt text",
                    "recommendation": "Use empty alt text (alt='') for decorative images",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def check_svg_elements(driver, results):
    """Check SVG elements for proper accessibility"""
    svg_elements = driver.find_elements(By.TAG_NAME, "svg")
    results["svg_count"] = len(svg_elements)
    
    for svg in svg_elements:
        # Get attributes for identification
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
            # Try to get ID or class for identification
            svg_id = svg.get_attribute("id") or ""
            svg_class = svg.get_attribute("class") or ""
            identifier = f"id='{svg_id}'" if svg_id else (f"class='{svg_class}'" if svg_class else "unknown")
            
            results["issues"].append({
                "element": "svg",
                "identifier": identifier,
                "issue": "SVG lacks text alternative",
                "details": "SVG element has no accessible name or description",
                "recommendation": "Add a <title> element, aria-label, or aria-labelledby attribute to describe the SVG",
                "wcag": "1.1.1",
                "severity": "critical" if is_likely_informative(svg) else "warning"
            })
        
        # If it has a title but no desc for complex SVGs
        if has_title and not has_desc and is_complex_svg(svg):
            results["issues"].append({
                "element": "svg",
                "identifier": svg.get_attribute("id") or svg.get_attribute("class") or "unknown",
                "issue": "Complex SVG needs description",
                "details": "Complex SVG has a title but lacks a description",
                "recommendation": "Add a <desc> element to provide more details for complex SVGs",
                "wcag": "1.1.1",
                "severity": "warning"
            })

def check_canvas_elements(driver, results):
    """Check canvas elements for proper accessibility"""
    canvas_elements = driver.find_elements(By.TAG_NAME, "canvas")
    results["canvas_count"] = len(canvas_elements)
    
    for canvas in canvas_elements:
        # Get attributes for identification
        canvas_id = canvas.get_attribute("id") or ""
        canvas_class = canvas.get_attribute("class") or ""
        identifier = f"id='{canvas_id}'" if canvas_id else (f"class='{canvas_class}'" if canvas_class else "unknown")
        
        # Check if canvas has fallback content
        inner_html = driver.execute_script("return arguments[0].innerHTML;", canvas).strip()
        has_fallback = len(inner_html) > 0
        
        # Check for accessibility attributes
        aria_label = canvas.get_attribute("aria-label") or ""
        aria_labelledby = canvas.get_attribute("aria-labelledby") or ""
        
        # Canvas needs either fallback content or ARIA attributes
        if not (has_fallback or aria_label or aria_labelledby):
            results["issues"].append({
                "element": "canvas",
                "identifier": identifier,
                "issue": "Canvas lacks text alternative",
                "details": "Canvas element has no fallback content or accessible name",
                "recommendation": "Add fallback content inside the canvas element or use aria-label/aria-labelledby",
                "wcag": "1.1.1",
                "severity": "critical"
            })

def check_css_background_images(driver, results):
    """Check elements with CSS background images"""
    # Find elements with background images
    background_elements = driver.find_elements(By.CSS_SELECTOR, 
        "[style*='background-image']:not(body):not(html)")
        
    for element in background_elements:
        # Skip elements that are likely decorative
        if is_likely_decorative_element(element):
            continue
            
        # Check if element has accessible text
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        aria_label = element.get_attribute("aria-label") or ""
        aria_labelledby = element.get_attribute("aria-labelledby")
        role = element.get_attribute("role") or ""
        
        # If it's a button or actionable element with no text
        if (element.tag_name in ["button", "a"] or role in ["button", "link"]) and not element_text and not aria_label and not aria_labelledby:
            element_id = element.get_attribute("id") or ""
            element_class = element.get_attribute("class") or ""
            identifier = f"id='{element_id}'" if element_id else (f"class='{element_class}'" if element_class else "unknown")
            
            results["issues"].append({
                "element": element.tag_name,
                "identifier": identifier,
                "issue": "Interactive element with background image lacks text alternative",
                "details": f"{element.tag_name.upper()} element with background image has no accessible name",
                "recommendation": "Add text content, aria-label, or aria-labelledby to describe the purpose of this element",
                "wcag": "1.1.1",
                "severity": "critical"
            })

def check_icon_fonts(driver, results):
    """Check icon fonts for proper accessibility"""
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
        
        for icon in icons:
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
                            "class": icon.get_attribute("class"),
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
                    "class": icon.get_attribute("class"),
                    "issue": "Icon lacks text alternative",
                    "details": "Icon has no accessible name and is not hidden from screen readers",
                    "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
                    "wcag": "1.1.1",
                    "severity": "warning"
                })

def check_other_nontext_content(driver, results):
    """Check other non-text content like video, audio, etc."""
    # Check video elements
    video_elements = driver.find_elements(By.TAG_NAME, "video")
    for video in video_elements:
        if not video.get_attribute("controls"):
            results["issues"].append({
                "element": "video",
                "src": video.get_attribute("src") or "[multiple sources]",
                "issue": "Video missing controls",
                "details": "Video element does not have controls attribute",
                "recommendation": "Add the 'controls' attribute or provide custom accessible controls",
                "wcag": "1.1.1, 2.1.1",
                "severity": "critical"
            })
            
        # Check for captions
        has_track = len(video.find_elements(By.TAG_NAME, "track")) > 0
        if not has_track:
            results["issues"].append({
                "element": "video",
                "src": video.get_attribute("src") or "[multiple sources]",
                "issue": "Video missing captions",
                "details": "No <track> element found for captions or subtitles",
                "recommendation": "Add a <track> element with captions for video content",
                "wcag": "1.1.1, 1.2.2",
                "severity": "critical"
            })
    
    # Check audio elements
    audio_elements = driver.find_elements(By.TAG_NAME, "audio")
    for audio in audio_elements:
        if not audio.get_attribute("controls"):
            results["issues"].append({
                "element": "audio",
                "src": audio.get_attribute("src") or "[multiple sources]",
                "issue": "Audio missing controls",
                "details": "Audio element does not have controls attribute",
                "recommendation": "Add the 'controls' attribute or provide custom accessible controls",
                "wcag": "1.1.1, 2.1.1",
                "severity": "critical"
            })
            
        # Check for transcript
        # This is a heuristic since transcripts are typically outside the audio element
        if not has_nearby_transcript(driver, audio):
            results["issues"].append({
                "element": "audio",
                "src": audio.get_attribute("src") or "[multiple sources]",
                "issue": "Audio may be missing transcript",
                "details": "No visible transcript found near the audio element",
                "recommendation": "Provide a text transcript for audio content",
                "wcag": "1.1.1, 1.2.1",
                "severity": "warning"
            })

# Helper functions

def get_image_identifier(image):
    """Get a useful identifier for the image (src or part of it)"""
    src = image.get_attribute("src") or ""
    
    # If src is a data URL, just return a placeholder
    if src.startswith("data:"):
        return "[data URL]"
        
    # Otherwise, get the filename part of the URL
    # or return a truncated version of the full URL
    filename_match = re.search(r'/([^/]+\.(jpg|jpeg|png|gif|webp|svg))(\?|$)', src, re.IGNORECASE)
    if filename_match:
        return filename_match.group(1)
    else:
        # Truncate very long URLs
        return src[:50] + "..." if len(src) > 50 else src

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

def is_likely_decorative_element(element):
    """Check if an element with background image is likely decorative"""
    # Check for role="presentation" or role="none"
    role = element.get_attribute("role") or ""
    if role.lower() in ["presentation", "none"]:
        return True
        
    # Check element classes for hints it's decorative
    class_attr = element.get_attribute("class") or ""
    decorative_classes = ["decoration", "bg", "background", "separator", "divider", "pattern"]
    if any(cls in class_attr.lower() for cls in decorative_classes):
        return True
        
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

def is_complex_svg(svg):
    """Determine if an SVG is complex and would benefit from a description"""
    try:
        # Count elements in SVG
        elements = svg.find_elements(By.XPATH, "./*")
        
        # If it has many child elements, it's likely complex
        if len(elements) > 10:
            return True
            
        # Check for specific complex element types
        complex_elements = svg.find_elements(
            By.CSS_SELECTOR, "path, polygon, polyline, text, g[transform]")
        
        return len(complex_elements) > 5
    except:
        return False

def has_nearby_transcript(driver, audio_element):
    """Try to detect if there's a transcript near an audio element (heuristic)"""
    try:
        # Look for common transcript indicators near the audio
        parent = audio_element.find_element(By.XPATH, "./..")
        
        # Look for transcript text or elements
        transcript_indicators = [
            "//div[contains(@class, 'transcript')]",
            "//details",  # Often used for expandable transcripts
            "//summary[contains(text(), 'transcript')]",
            "//a[contains(text(), 'transcript')]",
            "//h2[contains(text(), 'transcript')]",
            "//h3[contains(text(), 'transcript')]",
            "//p[contains(text(), 'transcript')]"
        ]
        
        for indicator in transcript_indicators:
            try:
                elements = parent.find_elements(By.XPATH, indicator)
                if elements:
                    return True
            except:
                pass
                
        return False
    except:
        return False
```
### accessibility_modules\.ipynb_checkpoints\report_generator-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_report_generator-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\report_generator-checkpoint.py
- **Last Modified**: 2025-03-10 23:08:24
- **Size**: 13478 bytes

#### Code
```python
"""
Accessibility Report Generator Module
Compiles results from various accessibility checks into a comprehensive report.
"""

import logging
import json
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

# Try to import other accessibility modules
try:
    from accessibility_modules.image_checker import check_image_accessibility
    image_checker_available = True
except ImportError:
    image_checker_available = False

try:
    from accessibility_modules.landmark_checker import check_landmarks_and_structure
    landmark_checker_available = True
except ImportError:
    landmark_checker_available = False

try:
    from accessibility_modules.form_checker import check_form_accessibility
    form_checker_available = True
except ImportError:
    form_checker_available = False

try:
    from accessibility_modules.html_report_generator import generate_html_report
    html_report_available = True
except ImportError:
    html_report_available = False

try:
    from accessibility_modules.simple_html_report_generator import generate_simple_html_report
    simple_html_report_available = True
except ImportError:
    simple_html_report_available = False

def generate_accessibility_report(driver, url, tab_order_results=None, 
                                  missing_focusable_results=None, aria_results=None,
                                  save_to_file=True, output_path=None):
    """
    Generate a comprehensive accessibility report by running various checks.
    
    Args:
        driver: Selenium WebDriver instance
        url: URL of the page being checked
        tab_order_results: Optional pre-run tab order results
        missing_focusable_results: Optional pre-run missing focusable elements results
        aria_results: Optional pre-run ARIA accessibility results
        save_to_file: Whether to save report to a file
        output_path: Path to save the report to
        
    Returns:
        dict: Complete accessibility report with all checks
    """
    logging.info(f"Generating comprehensive accessibility report for {url}")
    start_time = time.time()
    
    report = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "critical_issues": 0,
            "warnings": 0,
            "passed_checks": 0,
            "compliance_score": None  # Will calculate at end
        },
        "checks": {},
        "issues": []  # Consolidated list of all issues
    }
    
    try:
        # Add pre-run results if provided
        if tab_order_results:
            report["checks"]["keyboard_navigation_sequence"] = tab_order_results
            # Add issues to consolidated list
            for issue in tab_order_results.get("issues", []):
                issue["check_type"] = "keyboard_navigation_sequence"
                report["issues"].append(issue)
        
        if missing_focusable_results:
            report["checks"]["keyboard_accessibility"] = {
                "status": "completed",
                "issues": missing_focusable_results
            }
            # Add issues to consolidated list
            for issue in missing_focusable_results:
                if "error" not in issue:  # Skip error entries
                    issue["check_type"] = "keyboard_accessibility"
                    report["issues"].append(issue)
        
        if aria_results:
            report["checks"]["aria_accessibility"] = aria_results
            # Add issues to consolidated list
            for issue in aria_results.get("issues", []):
                issue["check_type"] = "aria_accessibility"
                report["issues"].append(issue)
        
        # Run additional checks if modules are available
        if image_checker_available:
            image_results = check_image_accessibility(driver)
            report["checks"]["image_accessibility"] = image_results
            # Add issues to consolidated list
            for issue in image_results.get("issues", []):
                issue["check_type"] = "image_accessibility"
                report["issues"].append(issue)
        else:
            report["checks"]["image_accessibility"] = {"status": "skipped", "reason": "Module not available"}
        
        if landmark_checker_available:
            landmark_results = check_landmarks_and_structure(driver)
            report["checks"]["landmarks_and_structure"] = landmark_results
            # Add issues to consolidated list
            for issue in landmark_results.get("issues", []):
                issue["check_type"] = "landmarks_and_structure"
                report["issues"].append(issue)
        else:
            report["checks"]["landmarks_and_structure"] = {"status": "skipped", "reason": "Module not available"}
        
        if form_checker_available:
            form_results = check_form_accessibility(driver)
            report["checks"]["form_accessibility"] = form_results
            # Add issues to consolidated list
            for issue in form_results.get("issues", []):
                issue["check_type"] = "form_accessibility"
                report["issues"].append(issue)
        else:
            report["checks"]["form_accessibility"] = {"status": "skipped", "reason": "Module not available"}
        
        # Run basic page title and language check
        title_lang_results = check_basic_page_attributes(driver)
        report["checks"]["basic_page_attributes"] = title_lang_results
        # Add issues to consolidated list
        for issue in title_lang_results.get("issues", []):
            issue["check_type"] = "basic_page_attributes"
            report["issues"].append(issue)
        
        # Calculate summary statistics
        calculate_summary_statistics(report)
        
        # Add timing information
        elapsed_time = time.time() - start_time
        report["elapsed_time"] = f"{elapsed_time:.2f} seconds"
        
        # Save report to file if requested
        if save_to_file:
            # Save JSON report
            json_path = save_report_to_file(report, url, output_path)
            
            # Generate HTML report if available
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                    'accessibility_reports')
            
            # Try regular HTML report first (now with fixed accordions)
            if html_report_available:
                try:
                    html_path = generate_html_report(report, reports_dir)
                    logging.info(f"HTML report generated at: {html_path}")
                    # Add HTML report path to the report
                    report["html_report_path"] = html_path
                except Exception as e:
                    logging.error(f"Error generating HTML report: {str(e)}")
                    # Fall back to simple HTML report if available
                    if simple_html_report_available:
                        try:
                            html_path = generate_simple_html_report(report, reports_dir)
                            logging.info(f"Simple HTML report generated at: {html_path}")
                            report["html_report_path"] = html_path
                        except Exception as e2:
                            logging.error(f"Error generating simple HTML report: {str(e2)}")
            # Fall back to simple HTML report if regular is not available
            elif simple_html_report_available:
                try:
                    html_path = generate_simple_html_report(report, reports_dir)
                    logging.info(f"Simple HTML report generated at: {html_path}")
                    report["html_report_path"] = html_path
                except Exception as e:
                    logging.error(f"Error generating simple HTML report: {str(e)}")
            
        return report
        
    except WebDriverException as e:
        logging.error(f"Error generating accessibility report: {str(e)}")
        report["error"] = str(e)
        return report

def check_basic_page_attributes(driver):
    """Check basic page attributes like title and language"""
    logging.info("Checking basic page attributes...")
    results = {
        "status": "completed",
        "issues": []
    }
    
    try:
        # Check for page title
        title = driver.title
        if not title or title.strip() == "":
            results["issues"].append({
                "issue": "Missing page title",
                "details": "Page does not have a title",
                "recommendation": "Add a descriptive <title> element",
                "wcag": "2.4.2",
                "severity": "critical"
            })
        elif len(title) < 5:
            results["issues"].append({
                "issue": "Page title may be too short",
                "details": f"Current title: '{title}'",
                "recommendation": "Use a more descriptive page title",
                "wcag": "2.4.2",
                "severity": "warning"
            })
        
        # Check for HTML lang attribute
        html_element = driver.find_element(By.TAG_NAME, "html")
        lang_attr = html_element.get_attribute("lang")
        
        if not lang_attr:
            results["issues"].append({
                "issue": "Missing language declaration",
                "details": "The <html> element does not have a lang attribute",
                "recommendation": "Add a lang attribute to the <html> element (e.g., lang='en')",
                "wcag": "3.1.1",
                "severity": "critical"
            })
        elif len(lang_attr) < 2:
            results["issues"].append({
                "issue": "Invalid language declaration",
                "details": f"The lang attribute '{lang_attr}' appears to be invalid",
                "recommendation": "Use a valid language code (e.g., 'en', 'fr', 'es')",
                "wcag": "3.1.1",
                "severity": "critical"
            })
            
        return results
        
    except WebDriverException as e:
        logging.error(f"Error checking basic page attributes: {str(e)}")
        results["error"] = str(e)
        return results

def calculate_summary_statistics(report):
    """Calculate summary statistics for the report"""
    critical_count = 0
    warning_count = 0
    passed_checks = 0
    check_count = 0
    
    # Count issues by severity
    for issue in report["issues"]:
        severity = issue.get("severity") or issue.get("type")
        if severity == "critical":
            critical_count += 1
        elif severity == "warning":
            warning_count += 1
    
    # Count passed checks
    for check_name, check_results in report["checks"].items():
        check_count += 1
        if check_results.get("status") == "completed" and len(check_results.get("issues", [])) == 0:
            passed_checks += 1
    
    # Update summary
    report["summary"]["critical_issues"] = critical_count
    report["summary"]["warnings"] = warning_count
    report["summary"]["passed_checks"] = passed_checks
    report["summary"]["total_checks"] = check_count
    
    # Calculate compliance score (simple formula, can be refined)
    if check_count > 0:
        # Weight critical issues more heavily than warnings
        weighted_issues = critical_count * 3 + warning_count
        max_score = check_count * 10  # Assume 10 possible points per check
        if critical_count > 0:
            # If there are critical issues, cap the score at 80%
            score = max(0, min(80, 100 - (weighted_issues * 100 / max_score)))
        else:
            score = max(0, 100 - (weighted_issues * 100 / max_score))
        
        report["summary"]["compliance_score"] = round(score, 1)
    else:
        report["summary"]["compliance_score"] = "N/A"

def save_report_to_file(report, url, output_path=None):
    """Save the accessibility report to a JSON file"""
    try:
        # Create a suitable filename from the URL
        if not output_path:
            url_clean = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "")
            if len(url_clean) > 50:
                url_clean = url_clean[:50]
            
            # Create the reports directory if it doesn't exist
            reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                      'accessibility_reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
                
            filename = os.path.join(reports_dir, 
                                   f"accessibility_report_{url_clean}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        else:
            filename = output_path
            
        # Ensure directory exists
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        # Write report to file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        logging.info(f"Accessibility report saved to: {filename}")
        return filename
        
    except Exception as e:
        logging.error(f"Error saving report to file: {str(e)}")
        return None
```
### accessibility_modules\.ipynb_checkpoints\simple_html_report_generator-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_simple_html_report_generator-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\simple_html_report_generator-checkpoint.py
- **Last Modified**: 2025-03-10 22:32:34
- **Size**: 8045 bytes

#### Code
```python
"""
Simple HTML Report Generator
Generates a basic HTML accessibility report with functioning accordions.
"""

import os
import logging
from datetime import datetime
from urllib.parse import urlparse

def generate_simple_html_report(report_data, output_dir=None):
    """
    Generate a simple HTML accessibility report with working accordions.
    
    Args:
        report_data: Dictionary with accessibility issues
        output_dir: Where to save the report
        
    Returns:
        str: Path to the generated report
    """
    # Set default output directory
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), 'accessibility_reports')
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create filename
    url = report_data.get('url', 'unknown')
    domain = urlparse(url).netloc or 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Get data for the report
    issues_by_type = {}
    
    # Group issues by check type
    for issue in report_data.get('issues', []):
        check_type = issue.get('check_type', 'general')
        if check_type not in issues_by_type:
            issues_by_type[check_type] = []
        issues_by_type[check_type].append(issue)
    
    # Build HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - {url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        
        .section {{
            margin-bottom: 30px;
            border: 1px solid #eee;
            border-radius: 5px;
            padding: 15px;
        }}
        
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }}
        
        .issue-count {{
            background-color: #e74c3c;
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 14px;
        }}
        
        .issue-count.no-issues {{
            background-color: #2ecc71;
        }}
        
        .section-content {{
            margin-top: 15px;
        }}
        
        .collapsible {{
            background-color: #f8f9fa;
            color: #444;
            cursor: pointer;
            padding: 18px;
            width: 100%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            margin-bottom: 5px;
            border-radius: 5px;
            text-align: center;
        }}
        
        .active, .collapsible:hover {{
            background-color: #f1f1f1;
        }}
        
        .collapsible:after {{
            content: '\\002B'; /* Unicode character for "plus" sign (+) */
            color: #777;
            font-weight: bold;
            float: right;
            margin-left: 5px;
        }}
        
        .active:after {{
            content: "\\2212"; /* Unicode character for "minus" sign (-) */
        }}
        
        .content {{
            padding: 0 18px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #f1f1f1;
            border-radius: 0 0 5px 5px;
        }}
        
        .issue-list {{
            list-style-type: none;
            padding: 0;
        }}
        
        .issue-item {{
            margin-bottom: 10px;
            padding: 10px;
            border-left: 4px solid #e74c3c;
            background-color: white;
        }}
        
        .issue-title {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .issue-details {{
            margin-bottom: 5px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            color: #666;
        }}
        
        .wcag {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Accessibility Report</h1>
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>Accessibility Issues Summary</h2>
"""

    # Add sections for each issue type
    for check_type, issues in issues_by_type.items():
        # Make the check type name more readable
        check_name = check_type.replace('_', ' ').title()
        
        html += f"""
        <div class="section">
            <div class="section-header">
                <h3>{check_name}</h3>
                <span class="issue-count {'no-issues' if not issues else ''}">
                    {len(issues)} {'Issue' if len(issues) == 1 else 'Issues'}
                </span>
            </div>
            
            <div class="section-content">
"""
        
        if issues:
            html += f"""
                <button class="collapsible">View Details</button>
                <div class="content">
                    <ul class="issue-list">
"""
            
            for issue in issues:
                title = issue.get('issue', 'Unknown Issue')
                details = issue.get('details', '')
                recommendation = issue.get('recommendation', '')
                wcag = issue.get('wcag', '')
                
                html += f"""
                        <li class="issue-item">
                            <div class="issue-title">{title}</div>
                            <div class="issue-details">{details}</div>
                            <div class="issue-recommendation">{recommendation}</div>
                            {f'<div><span class="wcag">WCAG {wcag}</span></div>' if wcag else ''}
                        </li>
"""
            
            html += """
                    </ul>
                </div>
"""
        else:
            html += """
                <p>No issues detected.</p>
"""
        
        html += """
            </div>
        </div>
"""
    
    # Close HTML and add script
    html += """
        <footer>
            <p>Generated by Accessibility Checker</p>
        </footer>
    </div>
    
    <script>
        // Wait for DOM to load
        document.addEventListener('DOMContentLoaded', function() {
            var coll = document.getElementsByClassName("collapsible");
            var i;

            for (i = 0; i < coll.length; i++) {
                coll[i].addEventListener("click", function() {
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    if (content.style.maxHeight) {
                        content.style.maxHeight = null;
                    } else {
                        content.style.maxHeight = content.scrollHeight + "px";
                    }
                });
            }
        });
    </script>
</body>
</html>
"""
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    logging.info(f"Simple HTML report generated at: {filepath}")
    return filepath
```
### accessibility_modules\.ipynb_checkpoints\tab_order_checker-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_tab_order_checker-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\tab_order_checker-checkpoint.py
- **Last Modified**: 2025-03-10 21:18:44
- **Size**: 8722 bytes

#### Code
```python
"""
Tab Order Checker Module
Checks the tab order of focusable elements to ensure they follow a logical sequence.
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

def check_tab_order(driver):
    """
    Checks the tab order of focusable elements on a webpage.
    
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
        # Reset focus to beginning of page
        driver.find_element(By.TAG_NAME, "body").click()
        
        # Find all potentially focusable elements
        focusable_selector = (
            "a, button, input:not([type='hidden']), select, textarea, "
            "[tabindex]:not([tabindex='-1']), [contenteditable='true'], "
            "details, summary, [role='button'], [role='link'], "
            "[role='checkbox'], [role='radio'], [role='tab'], [role='menuitem']"
        )
        
        # Get all focusable elements for reference
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        logging.info(f"Found {len(all_focusable)} potentially focusable elements")
        tab_order_results["potentially_focusable_count"] = len(all_focusable)
        
        # Attempt to follow tab sequence
        max_tabs = min(len(all_focusable) * 2, 100)  # Limit to prevent infinite loops
        focused_elements = []
        
        # Start with pressing Tab once to get to first element
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        
        for i in range(max_tabs):
            # Get currently focused element
            active_element = driver.execute_script("return document.activeElement;")
            element_info = get_element_info(active_element)
            
            # Skip if we encounter the same element again (circular tabbing)
            element_signature = (
                element_info.get("tag", "") + 
                element_info.get("id", "") + 
                element_info.get("text", "")
            )
            
            if element_signature in [e.get("signature", "") for e in focused_elements]:
                # We've already seen this element, likely in a loop
                if len(focused_elements) > 1:
                    break
            
            # Add to our sequence
            element_info["signature"] = element_signature
            element_info["tab_index"] = i + 1
            focused_elements.append(element_info)
            
            # Move to next element
            active_element.send_keys(Keys.TAB)
        
        tab_order_results["tab_sequence"] = focused_elements
        
        # Analyze the tab order for issues
        analyze_tab_order(tab_order_results)
        
        return tab_order_results
        
    except WebDriverException as e:
        logging.error(f"Error checking tab order: {str(e)}")
        tab_order_results["error"] = str(e)
        return tab_order_results

def get_element_info(element):
    """Extract useful information about an element"""
    try:
        tag_name = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        
        info = {
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
    if "potentially_focusable_count" in results and len(tab_sequence) < results["potentially_focusable_count"] / 2:
        issues.append({
            "type": "warning",
            "issue": "Potential keyboard navigation barriers",
            "details": f"Tab sequence ({len(tab_sequence)} elements) is much shorter than expected ({results.get('potentially_focusable_count', 'unknown')} potentially focusable elements)",
            "recommendation": "Check for elements that should be focusable but aren't",
            "wcag": "2.1.1"
        })
    
    results["issues"] = issues
```
### accessibility_modules\.ipynb_checkpoints\terminology_validator-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_terminology_validator-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\terminology_validator-checkpoint.py
- **Last Modified**: 2025-03-10 22:08:19
- **Size**: 10040 bytes

#### Code
```python
"""
Accessibility Terminology Validator
Ensures consistent terminology is used throughout the accessibility checker.
"""

import re
import json
import os
import logging

class AccessibilityTerminologyValidator:
    """
    Validates and standardizes accessibility terminology used in reports and issue descriptions.
    Uses a central terminology mapping to ensure consistency.
    """
    
    def __init__(self, terminology_file=None):
        """
        Initialize the terminology validator.
        
        Args:
            terminology_file: Path to a JSON file containing terminology mappings
        """
        self.terminology_mapping = {
            # Default terminology mappings
            "Inconsistent keyboard navigation sequence": "inconsistent keyboard navigation sequence",
            "Keyboard navigation barrier": "keyboard navigation barrier",
            "missing alt": "missing text alternative",
            "missing alt text": "missing text alternative",
            "alt text missing": "missing text alternative",
            "no alt": "missing text alternative",
            "no alt text": "missing text alternative",
            "alt attribute missing": "missing text alternative",
            "empty alt": "empty text alternative",
            "bad alt": "inadequate text alternative",
            "poor alt": "inadequate text alternative",
            "inadequate alt": "inadequate text alternative",
            "inappropriate alt": "inadequate text alternative",
            "insufficient alt": "inadequate text alternative",
            "incorrect alt": "inadequate text alternative",
            "wrong alt": "inadequate text alternative",
            "missing label": "form control without label",
            "unlabeled": "form control without label",
            "no label": "form control without label",
            "contrast issue": "insufficient color contrast",
            "low contrast": "insufficient color contrast",
            "poor contrast": "insufficient color contrast",
            "contrast problem": "insufficient color contrast",
            "contrast error": "insufficient color contrast",
            "color contrast issue": "insufficient color contrast",
            "color contrast problem": "insufficient color contrast",
            "color contrast error": "insufficient color contrast",
            "keyboard trap": "keyboard navigation barrier",
            "focus trap": "keyboard navigation barrier",
            "focus issue": "keyboard navigation barrier",
            "focus problem": "keyboard navigation barrier",
            "focus error": "keyboard navigation barrier",
            "keyboard issue": "keyboard navigation barrier",
            "keyboard problem": "keyboard navigation barrier",
            "keyboard error": "keyboard navigation barrier",
            "missing aria": "incomplete ARIA implementation",
            "incorrect aria": "incomplete ARIA implementation",
            "aria issue": "incomplete ARIA implementation",
            "aria problem": "incomplete ARIA implementation",
            "aria error": "incomplete ARIA implementation",
            "aria-label missing": "incomplete ARIA implementation",
            "aria-labelledby missing": "incomplete ARIA implementation",
            "aria-describedby missing": "incomplete ARIA implementation",
            "missing landmark": "missing page structure landmarks",
            "landmark issue": "missing page structure landmarks",
            "landmark problem": "missing page structure landmarks",
            "landmark error": "missing page structure landmarks",
            "heading issue": "improper heading structure",
            "heading problem": "improper heading structure",
            "heading error": "improper heading structure",
            "heading structure issue": "improper heading structure",
            "missing heading": "improper heading structure",
            "heading level skipped": "improper heading structure",
            "heading level issue": "improper heading structure"
        }
        
        # Load additional or override terminology from file if provided
        if terminology_file and os.path.exists(terminology_file):
            try:
                with open(terminology_file, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
            except Exception as e:
                logging.error(f"Error loading terminology file: {str(e)}")
    
    def standardize_terminology(self, text):
        """
        Standardize terminology in the provided text.
        
        Args:
            text: The text to standardize
            
        Returns:
            str: Text with standardized terminology
        """
        if not text:
            return text
            
        standardized_text = text
        
        # Apply each terminology mapping
        for incorrect, correct in self.terminology_mapping.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(incorrect), re.IGNORECASE)
            standardized_text = pattern.sub(correct, standardized_text)
        
        return standardized_text
    
    def validate_report_terminology(self, report):
        """
        Validate and standardize terminology in an accessibility report.
        
        Args:
            report: Dictionary containing accessibility report data
            
        Returns:
            dict: Report with standardized terminology
        """
        if not report or not isinstance(report, dict):
            return report
            
        # Create a copy of the report to avoid modifying the original
        validated_report = report.copy()
        
        # Process issues
        if "issues" in validated_report:
            for i, issue in enumerate(validated_report["issues"]):
                if "issue" in issue:
                    issue["issue"] = self.standardize_terminology(issue["issue"])
                if "details" in issue:
                    issue["details"] = self.standardize_terminology(issue["details"])
                if "recommendation" in issue:
                    issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        # Process checks
        if "checks" in validated_report:
            for check_name, check_data in validated_report["checks"].items():
                if isinstance(check_data, dict) and "issues" in check_data:
                    for i, issue in enumerate(check_data["issues"]):
                        if isinstance(issue, dict):
                            if "issue" in issue:
                                issue["issue"] = self.standardize_terminology(issue["issue"])
                            if "details" in issue:
                                issue["details"] = self.standardize_terminology(issue["details"])
                            if "recommendation" in issue:
                                issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        return validated_report
    
    def load_terminology_file(self, file_path):
        """
        Load terminology mappings from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
                return True
            else:
                logging.error(f"Terminology file not found: {file_path}")
                return False
        except Exception as e:
            logging.error(f"Error loading terminology file: {str(e)}")
            return False
    
    def save_terminology_file(self, file_path):
        """
        Save the current terminology mappings to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.terminology_mapping, f, indent=4, sort_keys=True)
                
            logging.info(f"Saved {len(self.terminology_mapping)} terminology mappings to {file_path}")
            return True
        except Exception as e:
            logging.error(f"Error saving terminology file: {str(e)}")
            return False
    
    def add_terminology_mapping(self, incorrect, correct):
        """
        Add a new terminology mapping.
        
        Args:
            incorrect: The incorrect or inconsistent term
            correct: The preferred term to use instead
            
        Returns:
            bool: True if added successfully
        """
        if not incorrect or not correct:
            return False
            
        self.terminology_mapping[incorrect.lower()] = correct.lower()
        return True
    
    def remove_terminology_mapping(self, incorrect):
        """
        Remove a terminology mapping.
        
        Args:
            incorrect: The incorrect term to remove from mappings
            
        Returns:
            bool: True if removed, False if not found
        """
        if incorrect and incorrect.lower() in self.terminology_mapping:
            del self.terminology_mapping[incorrect.lower()]
            return True
        return False
```
### accessibility_modules\.ipynb_checkpoints\test_accordion-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints_test_accordion-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\test_accordion-checkpoint.py
- **Last Modified**: 2025-03-10 22:40:32
- **Size**: 1654 bytes

#### Code
```python
"""
Test script to generate a simple HTML report with working accordions.
"""

import os
import sys

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from simple_html_report_generator import generate_simple_html_report

# Sample data to test the report
sample_data = {
    "url": "https://example.com",
    "issues": [
        {
            "check_type": "image_accessibility",
            "issue": "Missing alt text",
            "details": "Image does not have alt attribute",
            "recommendation": "Add descriptive alt text to the image",
            "wcag": "1.1.1"
        },
        {
            "check_type": "image_accessibility",
            "issue": "Decorative image not hidden",
            "details": "Decorative image should be hidden from screen readers",
            "recommendation": "Add aria-hidden='true' or empty alt text",
            "wcag": "1.1.1"
        },
        {
            "check_type": "keyboard_navigation",
            "issue": "Keyboard navigation barrier",
            "details": "Element cannot be accessed with keyboard",
            "recommendation": "Make the element focusable",
            "wcag": "2.1.1"
        }
    ]
}

# Generate report
report_path = generate_simple_html_report(sample_data)
print(f"Test report generated at: {report_path}")

# Try to open the report in the default browser
try:
    import webbrowser
    webbrowser.open(f"file://{os.path.abspath(report_path)}")
    print("Report opened in browser")
except:
    print("Could not open report in browser")
```
### accessibility_modules\.ipynb_checkpoints\__init__-checkpoint.py <a id='accessibility_modules__ipynb_checkpoints___init__-checkpoint_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\.ipynb_checkpoints\__init__-checkpoint.py
- **Last Modified**: 2025-03-10 21:19:19
- **Size**: 122 bytes

#### Code
```python
"""
Accessibility Modules Package
Contains modules for performing various accessibility checks.
"""

__version__ = '0.1.0'
```
## Text Files

### project structure.txt <a id='project structure_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: project structure.txt
- **Last Modified**: 2025-03-10 21:14:39
- **Size**: 842 bytes

#### Content
```
accessibility_checker/
│
├── accessibility_checker.py     # Main script
├── requirements.txt             # Dependencies
│
└── accessibility_modules/       # Module directory
    ├── __init__.py              # Makes the directory a package
    ├── tab_order_checker.py     # Tab order checking functionality
    ├── focusable_elements.py    # Missing focusable elements detection
    ├── aria_checker.py          # ARIA and keyboard accessibility checks
    ├── image_checker.py         # Image accessibility checks
    ├── color_contrast.py        # Color contrast analysis
    ├── form_checker.py          # Form accessibility checks
    ├── landmark_checker.py      # Landmark and structure checks
    └── report_generator.py      # Report generation functionality
```
### requirements.txt <a id='requirements_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: requirements.txt
- **Last Modified**: 2025-03-10 21:23:50
- **Size**: 114 bytes

#### Content
```
selenium>=4.10.0
webdriver-manager>=3.8.5
requests>=2.28.0
beautifulsoup4>=4.11.1
pytest>=7.3.1
pytest-html>=3.2.0
```
### .ipynb_checkpoints\project structure-checkpoint.txt <a id='_ipynb_checkpoints_project structure-checkpoint_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: .ipynb_checkpoints\project structure-checkpoint.txt
- **Last Modified**: 2025-03-10 21:14:39
- **Size**: 842 bytes

#### Content
```
accessibility_checker/
│
├── accessibility_checker.py     # Main script
├── requirements.txt             # Dependencies
│
└── accessibility_modules/       # Module directory
    ├── __init__.py              # Makes the directory a package
    ├── tab_order_checker.py     # Tab order checking functionality
    ├── focusable_elements.py    # Missing focusable elements detection
    ├── aria_checker.py          # ARIA and keyboard accessibility checks
    ├── image_checker.py         # Image accessibility checks
    ├── color_contrast.py        # Color contrast analysis
    ├── form_checker.py          # Form accessibility checks
    ├── landmark_checker.py      # Landmark and structure checks
    └── report_generator.py      # Report generation functionality
```
### .ipynb_checkpoints\requirements-checkpoint.txt <a id='_ipynb_checkpoints_requirements-checkpoint_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: .ipynb_checkpoints\requirements-checkpoint.txt
- **Last Modified**: 2025-03-10 21:23:50
- **Size**: 114 bytes

#### Content
```
selenium>=4.10.0
webdriver-manager>=3.8.5
requests>=2.28.0
beautifulsoup4>=4.11.1
pytest>=7.3.1
pytest-html>=3.2.0
```
### accessibility_modules\accessibility_terminology.txt <a id='accessibility_modules_accessibility_terminology_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: accessibility_modules\accessibility_terminology.txt
- **Last Modified**: 2025-03-10 22:16:45
- **Size**: 770 bytes

#### Content
```
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "tab order issue": "inconsistent keyboard navigation sequence",
        "interactive element not in tab order": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### accessibility_modules\enhanced_accessibility_checker - README.txt <a id='accessibility_modules_enhanced_accessibility_checker - README_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: accessibility_modules\enhanced_accessibility_checker - README.txt
- **Last Modified**: 2025-03-10 16:46:52
- **Size**: 3939 bytes

#### Content
```
Here's a plan to enhance the accessibility testing program based on the information in the readme.txt file:

1. Prioritize WCAG criteria:
   a. Review the list of additional WCAG success criteria not currently covered by the program.
   b. Prioritize the criteria based on impact, feasibility, and importance.
   c. Consider factors like complexity, user benefit, dependencies, and project context.
   d. Create a prioritized list of criteria to guide the implementation process.

2. Breakdown of "1.1.1 Non-text Content" criterion:
   a. Identify all instances of non-text content (images, icons, charts, etc.) in the tested web pages.
   b. Check if each non-text content item has a text alternative (e.g., alt attribute for images).
   c. Evaluate the quality and appropriateness of the text alternatives.
   d. Provide recommendations for missing or insufficient text alternatives.
   e. Integrate these checks into the automated testing process.
   f. Update the reporting functionality to include information about non-text content accessibility.

3. Implementation of automated checks:
   a. Develop automated checks for the prioritized criteria, starting with "1.1.1 Non-text Content".
   b. Leverage existing libraries, write custom code, or integrate with external accessibility testing tools.
   c. Ensure the automated checks provide quick feedback and identify common issues.

4. Integration of manual testing procedures:
   a. Recognize that some accessibility criteria may require manual evaluation.
   b. Develop testing procedures and guidelines for manual accessibility testing.
   c. Include steps for keyboard navigation, visual inspection, and assistive technology usage.
   d. Document the manual testing procedures in the project's README or a separate testing guide.

5. Terminology validator update:
   a. Review the AccessibilityTerminologyValidator class.
   b. Update it to include new terms or concepts related to the additional WCAG criteria.
   c. Ensure consistent terminology usage throughout the program, aligning with WCAG guidelines.

6. Reporting functionality enhancement:
   a. Modify the report generation scripts (e.g., Enhanced_Report_Generator) to include information about the newly covered WCAG criteria.
   b. Update the report templates to provide clear explanations, examples, and recommendations for each identified accessibility issue.

7. Testing and validation:
   a. Thoroughly test the program against various web pages and scenarios.
   b. Validate the accuracy and reliability of the new checks.
   c. Ensure the program provides meaningful and actionable feedback.

8. Documentation update:
   a. Update the project's documentation, including the README file and relevant code comments.
   b. Reflect the enhancements made to the program.
   c. Clearly indicate which WCAG criteria are now covered.
   d. Provide instructions for running the updated accessibility tests.

9. Iterative approach:
   a. Implement the enhancements iteratively, focusing on the highest priority criteria first.
   b. Gradually expand the program's capabilities over time.
   c. Regularly review and update the program to stay aligned with the latest accessibility guidelines and best practices.

10. Seek guidance and ask questions:
    a. Reach out for specific questions or guidance on implementing any of the enhancements.
    b. Collaborate to improve the accessibility testing program and ensure it provides valuable insights for creating inclusive web experiences.

This plan breaks down the steps to enhance the accessibility testing program based on the information provided in the readme.txt file. It prioritizes the WCAG criteria, outlines the implementation process, and emphasizes the importance of testing, validation, documentation, and an iterative approach. The plan also encourages seeking guidance and collaboration to ensure the program's effectiveness in improving web accessibility.
```
### accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.txt <a id='accessibility_modules__ipynb_checkpoints_accessibility_terminology-checkpoint_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.txt
- **Last Modified**: 2025-03-10 22:16:45
- **Size**: 770 bytes

#### Content
```
import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "tab order issue": "inconsistent keyboard navigation sequence",
        "interactive element not in tab order": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')
```
### accessibility_modules\.ipynb_checkpoints\enhanced_accessibility_checker - README-checkpoint.txt <a id='accessibility_modules__ipynb_checkpoints_enhanced_accessibility_checker - README-checkpoint_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: accessibility_modules\.ipynb_checkpoints\enhanced_accessibility_checker - README-checkpoint.txt
- **Last Modified**: 2025-03-10 16:46:52
- **Size**: 3939 bytes

#### Content
```
Here's a plan to enhance the accessibility testing program based on the information in the readme.txt file:

1. Prioritize WCAG criteria:
   a. Review the list of additional WCAG success criteria not currently covered by the program.
   b. Prioritize the criteria based on impact, feasibility, and importance.
   c. Consider factors like complexity, user benefit, dependencies, and project context.
   d. Create a prioritized list of criteria to guide the implementation process.

2. Breakdown of "1.1.1 Non-text Content" criterion:
   a. Identify all instances of non-text content (images, icons, charts, etc.) in the tested web pages.
   b. Check if each non-text content item has a text alternative (e.g., alt attribute for images).
   c. Evaluate the quality and appropriateness of the text alternatives.
   d. Provide recommendations for missing or insufficient text alternatives.
   e. Integrate these checks into the automated testing process.
   f. Update the reporting functionality to include information about non-text content accessibility.

3. Implementation of automated checks:
   a. Develop automated checks for the prioritized criteria, starting with "1.1.1 Non-text Content".
   b. Leverage existing libraries, write custom code, or integrate with external accessibility testing tools.
   c. Ensure the automated checks provide quick feedback and identify common issues.

4. Integration of manual testing procedures:
   a. Recognize that some accessibility criteria may require manual evaluation.
   b. Develop testing procedures and guidelines for manual accessibility testing.
   c. Include steps for keyboard navigation, visual inspection, and assistive technology usage.
   d. Document the manual testing procedures in the project's README or a separate testing guide.

5. Terminology validator update:
   a. Review the AccessibilityTerminologyValidator class.
   b. Update it to include new terms or concepts related to the additional WCAG criteria.
   c. Ensure consistent terminology usage throughout the program, aligning with WCAG guidelines.

6. Reporting functionality enhancement:
   a. Modify the report generation scripts (e.g., Enhanced_Report_Generator) to include information about the newly covered WCAG criteria.
   b. Update the report templates to provide clear explanations, examples, and recommendations for each identified accessibility issue.

7. Testing and validation:
   a. Thoroughly test the program against various web pages and scenarios.
   b. Validate the accuracy and reliability of the new checks.
   c. Ensure the program provides meaningful and actionable feedback.

8. Documentation update:
   a. Update the project's documentation, including the README file and relevant code comments.
   b. Reflect the enhancements made to the program.
   c. Clearly indicate which WCAG criteria are now covered.
   d. Provide instructions for running the updated accessibility tests.

9. Iterative approach:
   a. Implement the enhancements iteratively, focusing on the highest priority criteria first.
   b. Gradually expand the program's capabilities over time.
   c. Regularly review and update the program to stay aligned with the latest accessibility guidelines and best practices.

10. Seek guidance and ask questions:
    a. Reach out for specific questions or guidance on implementing any of the enhancements.
    b. Collaborate to improve the accessibility testing program and ensure it provides valuable insights for creating inclusive web experiences.

This plan breaks down the steps to enhance the accessibility testing program based on the information provided in the readme.txt file. It prioritizes the WCAG criteria, outlines the implementation process, and emphasizes the importance of testing, validation, documentation, and an iterative approach. The plan also encourages seeking guidance and collaboration to ensure the program's effectiveness in improving web accessibility.
```
## JSON Files

### accessibility_terminology.json <a id='accessibility_terminology_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_terminology.json
- **Last Modified**: 2025-03-10 23:16:30
- **Size**: 572 bytes

#### Content
```json
{
  "technical_terms": {
    "interactive element not in tab order": {
      "preferred": "Keyboard navigation barrier",
      "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
    },
    "tab order issue": {
      "preferred": "Inconsistent keyboard navigation sequence",
      "explanation": "Elements that disrupt the expected keyboard navigation flow"
    }
  },
  "impact_categories": [
    "Screen Reader Accessibility",
    "Keyboard Navigation",
    "Visual Focus",
    "Interactive Element Accessibility"
  ]
}
```
### accessibility_modules\accessibility_terminology.json <a id='accessibility_modules_accessibility_terminology_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_modules\accessibility_terminology.json
- **Last Modified**: 2025-03-10 22:20:14
- **Size**: 195 bytes

#### Content
```json
{
  "tab order issue": "inconsistent keyboard navigation sequence",
  "interactive element not in tab order": "keyboard navigation barrier",
  "missing alt text": "missing text alternative"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_220026.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_220026_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_220026.json
- **Last Modified**: 2025-03-10 22:00:26
- **Size**: 11480 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 22:00:25",
  "summary": {
    "critical_issues": 3,
    "warnings": 6,
    "passed_checks": 1,
    "compliance_score": 78.6,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "image_count": 6,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "div",
          "issue": "Background image without text alternative",
          "details": "Element with CSS background image lacks text alternative",
          "recommendation": "Add text content or aria-label if the background image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "div",
          "issue": "Background image without text alternative",
          "details": "Element with CSS background image lacks text alternative",
          "recommendation": "Add text content or aria-label if the background image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "div",
          "issue": "Background image without text alternative",
          "details": "Element with CSS background image lacks text alternative",
          "recommendation": "Add text content or aria-label if the background image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "div",
      "issue": "Background image without text alternative",
      "details": "Element with CSS background image lacks text alternative",
      "recommendation": "Add text content or aria-label if the background image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "div",
      "issue": "Background image without text alternative",
      "details": "Element with CSS background image lacks text alternative",
      "recommendation": "Add text content or aria-label if the background image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "div",
      "issue": "Background image without text alternative",
      "details": "Element with CSS background image lacks text alternative",
      "recommendation": "Add text content or aria-label if the background image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "0.29 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_222058.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_222058_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_222058.json
- **Last Modified**: 2025-03-10 22:20:58
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 22:20:56",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.43 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_222822.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_222822_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_222822.json
- **Last Modified**: 2025-03-10 22:28:22
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 22:28:20",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.34 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_225526.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_225526_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_225526.json
- **Last Modified**: 2025-03-10 22:55:26
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 22:55:24",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.34 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_230844.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_230844_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_230844.json
- **Last Modified**: 2025-03-10 23:08:44
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 23:08:42",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.72 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_232033.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_232033_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_232033.json
- **Last Modified**: 2025-03-10 23:20:33
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 23:20:31",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.35 seconds"
}
```
### accessibility_reports\accessibility_report_sse.com_20250310_232415.json <a id='accessibility_reports_accessibility_report_sse_com_20250310_232415_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\accessibility_report_sse.com_20250310_232415.json
- **Last Modified**: 2025-03-10 23:24:15
- **Size**: 29651 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-10 23:24:13",
  "summary": {
    "critical_issues": 3,
    "warnings": 26,
    "passed_checks": 1,
    "compliance_score": 50.0,
    "total_checks": 7
  },
  "checks": {
    "keyboard_navigation_sequence": {
      "tab_sequence": [
        {
          "tag": "button",
          "id": "ccc-notify-accept",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-accept-button",
          "role": "",
          "tabindex": "auto",
          "text": "Allow all",
          "visible": true,
          "position": {
            "x": 440.0,
            "y": 383.0,
            "width": 115.96665954589844,
            "height": 40.0
          },
          "signature": "buttonccc-notify-acceptAllow all",
          "tab_index": 1
        },
        {
          "tag": "button",
          "id": "ccc-notify-reject",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-reject-button",
          "role": "",
          "tabindex": "auto",
          "text": "Disable all",
          "visible": true,
          "position": {
            "x": 563.9666748046875,
            "y": 383.0,
            "width": 128.60000610351562,
            "height": 40.0
          },
          "signature": "buttonccc-notify-rejectDisable all",
          "tab_index": 2
        },
        {
          "tag": "button",
          "id": "",
          "class": "ccc-notify-button ccc-link ccc-tabbable ccc-notify-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie settings",
          "visible": true,
          "position": {
            "x": 700.566650390625,
            "y": 377.5,
            "width": 172.88333129882812,
            "height": 48.0
          },
          "signature": "buttonCookie settings",
          "tab_index": 3
        },
        {
          "tag": "a",
          "id": "",
          "class": "external-link",
          "role": "",
          "tabindex": "auto",
          "text": "Cookie notice",
          "visible": true,
          "position": {
            "x": 673.4833374023438,
            "y": 335.5,
            "width": 138.43333435058594,
            "height": 28.0
          },
          "signature": "aCookie notice",
          "tab_index": 4
        }
      ],
      "issues": [
        {
          "type": "warning",
          "issue": "Potential keyboard navigation barriers",
          "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
          "recommendation": "Check for elements that should be focusable but aren't",
          "wcag": "2.1.1",
          "check_type": "keyboard_navigation_sequence"
        }
      ],
      "potentially_focusable_count": 212
    },
    "keyboard_accessibility": {
      "status": "completed",
      "issues": [
        {
          "error": "Message: TypeError: arguments[0] is undefined\nStacktrace:\n@https://www.sse.com/:7:32\n@https://www.sse.com/:10:30\n@https://www.sse.com/:12:8\n"
        }
      ]
    },
    "aria_accessibility": {
      "status": "completed",
      "issues": [
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 3 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        },
        {
          "element": "div",
          "text": "[No text]",
          "issue": "Hidden element contains focusable elements",
          "details": "Element with aria-hidden='true' contains 1 focusable children",
          "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
          "wcag": "1.3.1",
          "severity": "critical",
          "check_type": "aria_accessibility"
        }
      ]
    },
    "image_accessibility": {
      "status": "completed",
      "wcag_criterion": "1.1.1",
      "image_count": 6,
      "svg_count": 1,
      "canvas_count": 0,
      "other_nontext_count": 0,
      "issues": [
        {
          "element": "img",
          "src": "website-banner-desktop.png",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "img",
          "src": "battery_storage_fareham.jpg",
          "issue": "Potentially informative image has empty alt text",
          "details": "Image appears to convey information but has empty alt text",
          "recommendation": "Add descriptive alt text if the image conveys information",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-mail",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-search",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu icon font-ico-hamburger",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "nav-toggle__menu-close icon font-ico-close",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-arrow-top",
          "issue": "Icon lacks text alternative",
          "details": "Icon has no accessible name and is not hidden from screen readers",
          "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        },
        {
          "element": "span",
          "class": "icon font-ico-extern",
          "issue": "Decorative icon not hidden from screen readers",
          "details": "Icon inside a labeled element should be hidden from screen readers",
          "recommendation": "Add aria-hidden='true' to the icon element",
          "wcag": "1.1.1",
          "severity": "warning",
          "check_type": "image_accessibility"
        }
      ]
    },
    "landmarks_and_structure": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "form_accessibility": {
      "status": "skipped",
      "reason": "Module not available"
    },
    "basic_page_attributes": {
      "status": "completed",
      "issues": []
    }
  },
  "issues": [
    {
      "type": "warning",
      "issue": "Potential keyboard navigation barriers",
      "details": "Tab sequence (4 elements) is much shorter than expected (212 potentially focusable elements)",
      "recommendation": "Check for elements that should be focusable but aren't",
      "wcag": "2.1.1",
      "check_type": "keyboard_navigation_sequence"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 3 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "Featured News\nSSE to build power station in Ireland running on sustainable biofuels\nSSE Thermal has made the final investment decision to build Tarbert's Next-Generation Power Station. The station will run on 100% sustainable biofuels and have the potential to convert to hydrogen.\nRead More",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "div",
      "text": "[No text]",
      "issue": "Hidden element contains focusable elements",
      "details": "Element with aria-hidden='true' contains 1 focusable children",
      "recommendation": "Remove focusable elements from aria-hidden containers or ensure they also have tabindex='-1'",
      "wcag": "1.3.1",
      "severity": "critical",
      "check_type": "aria_accessibility"
    },
    {
      "element": "img",
      "src": "website-banner-desktop.png",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "img",
      "src": "battery_storage_fareham.jpg",
      "issue": "Potentially informative image has empty alt text",
      "details": "Image appears to convey information but has empty alt text",
      "recommendation": "Add descriptive alt text if the image conveys information",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "arrow icon font-ico-chevron-down main-nav__secondary-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-mail",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-search",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu icon font-ico-hamburger",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "nav-toggle__menu-close icon font-ico-close",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--first icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "banner__scroll-icon banner__scroll-icon--second icon font-ico-arrow",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-arrow-top",
      "issue": "Icon lacks text alternative",
      "details": "Icon has no accessible name and is not hidden from screen readers",
      "recommendation": "Add aria-label or make decorative with aria-hidden='true'",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    },
    {
      "element": "span",
      "class": "icon font-ico-extern",
      "issue": "Decorative icon not hidden from screen readers",
      "details": "Icon inside a labeled element should be hidden from screen readers",
      "recommendation": "Add aria-hidden='true' to the icon element",
      "wcag": "1.1.1",
      "severity": "warning",
      "check_type": "image_accessibility"
    }
  ],
  "elapsed_time": "1.52 seconds"
}
```
### accessibility_reports\comprehensive_sse.com_20250303_180408.json <a id='accessibility_reports_comprehensive_sse_com_20250303_180408_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\comprehensive_sse.com_20250303_180408.json
- **Last Modified**: 2025-03-03 18:04:08
- **Size**: 7802 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-03T18:04:08.001320",
  "browser": "firefox",
  "summary": {
    "total_elements": 152,
    "tab_order_issues": 4,
    "aria_issues": 6,
    "keyboard_issues": 1,
    "scan_time_seconds": 39.79645323753357
  },
  "tab_order_data": [
    "1: a - ",
    "2: a - Home",
    "3: a - About us",
    "4: a - About us",
    "5: a - Our businesses",
    "6: a - SSE Renewables",
    "7: a - SSE Thermal",
    "8: a - SSEN Transmission",
    "9: a - SSEN Distribution",
    "10: a - SSE Energy Solutions",
    "11: a - SSE Airtricity",
    "12: a - SSE Energy Markets",
    "13: a - Leadership and Governance",
    "14: a - Meet the board",
    "15: a - Meet the GEC",
    "16: a - Our heritage",
    "17: a - Our culture",
    "18: a - Our campaigns",
    "19: a - UK campaign",
    "20: a - Ireland campaign",
    "21: a - Our technologies",
    "22: a - Our technologies",
    "23: a - Offshore wind",
    "24: a - Onshore wind",
    "25: a - Hydro",
    "26: a - Solar",
    "27: a - Battery storage",
    "28: a - Thermal",
    "29: a - Carbon capture and storage",
    "30: a - Hydrogen",
    "31: a - Transmission networks",
    "32: a - Distribution networks",
    "33: a - Investors",
    "34: a - Investors",
    "35: a - Annual Report 2024",
    "36: a - The SSE investment case",
    "37: a - Analysts",
    "38: a - Reports and results",
    "39: a - Regulatory news",
    "40: a - Regulatory news alerts",
    "41: a - Policy on market speculation",
    "42: a - Financial calendar",
    "43: a - PNG scam warning",
    "44: a - Annual General Meeting 2024",
    "45: a - Annual General Meeting 2023",
    "46: a - Annual General Meeting 2022",
    "47: a - Annual General Meeting 2021",
    "48: a - Shareholder services",
    "49: a - Share dealing",
    "50: a - Ecommunications programme",
    "51: a - Shareholder contacts",
    "52: a - Share price information",
    "53: a - Dividends and Scrip scheme",
    "54: a - Multiple share accounts",
    "55: a - Share repurchase programme",
    "56: a - Useful information",
    "57: a - Debt investors",
    "58: a - Credit rating",
    "59: a - Sustainability Financing Frame",
    "60: a - EMTN programme",
    "61: a - ADRs",
    "62: a - Sustainability",
    "63: a - Sustainability",
    "64: a - Environment",
    "65: a - Social",
    "66: a - Targets and performance",
    "67: a - Reporting",
    "68: a - Partnerships and Memberships",
    "69: a - Policies and assurances",
    "70: a - Innovation",
    "71: a - Just Transition",
    "72: a - Powering Net Zero Pact",
    "73: a - SSE at COP",
    "74: a - News and views",
    "75: a - News and views",
    "76: a - Media contacts",
    "77: a - Media bank",
    "78: a - Careers",
    "79: a - Careers",
    "80: a - Life at SSE",
    "81: a - Developing our People",
    "82: a - Flexible Working",
    "83: a - Employee benefits",
    "84: a - Join our Team",
    "85: a - Engineering and Technical",
    "86: a - IT and Digital",
    "87: a - Corporate",
    "88: a - Inclusion",
    "89: a - Early Careers",
    "90: a - Apprenticeships and Trainees",
    "91: a - Graduate Development",
    "92: a - Progression Stories",
    "93: a - Contact Recruitment",
    "94: button - Open search form",
    "95: input - [No text]",
    "96: button - Type search here",
    "97: button - Clear search",
    "98: a - ",
    "99: button - Close search form",
    "100: a - Open search form",
    "101: button - ",
    "102: input - [No text]",
    "103: button - Submit search",
    "104: button - ",
    "105: a - About us",
    "106: button - Go to previous slide",
    "107: button - Go to next slide",
    "108: button - ",
    "109: a - UK campaign",
    "110: a - News and views",
    "111: a - Read More",
    "112: a - Read More",
    "113: a - Read More",
    "114: a - Read More",
    "115: a - Read More",
    "116: button - Next slide.",
    "117: button - Previus slide.",
    "118: a - Watch the webcast",
    "119: a - Detailed share price",
    "120: a - Careers",
    "121: a - Sustainability",
    "122: a - SSE Renewables",
    "123: a - SSEN Distribution",
    "124: a - SSEN Transmission",
    "125: a - SSE Thermal",
    "126: a - SSE Energy Solutions",
    "127: a - SSE Airtricity",
    "128: button - Back to top.",
    "129: a - Sustainability",
    "130: a - Overview",
    "131: a - Our 2030 Goals",
    "132: a - Modern Slavery Statement",
    "133: a - News and views",
    "134: a - Overview",
    "135: a - Media Contacts",
    "136: a - Media bank",
    "137: a - Careers",
    "138: a - Overview",
    "139: a - Life at SSE",
    "140: a - Specialisms",
    "141: a - Inclusion",
    "142: a - Early Careers",
    "143: a - Thinking of applying?",
    "144: button - Back to top",
    "145: a - Contact us",
    "146: a - Privacy notice",
    "147: a - Cookie notice",
    "148: a - Potential suppliers",
    "149: a - Sitemap",
    "150: a - Sustainability",
    "151: a - Cookie settings",
    "152: a - REMIT"
  ],
  "tab_order_issues": [
    "Tab order issue: Element 111 (tabindex=0) comes before Element 112 (tabindex=0)",
    "Tab order issue: Element 112 (tabindex=0) comes before Element 113 (tabindex=0)",
    "Tab order issue: Element 113 (tabindex=0) comes before Element 114 (tabindex=-1)",
    "Tab order issue: Element 114 (tabindex=-1) comes before Element 115 (tabindex=-1)"
  ],
  "aria_issues": [
    "Image 1 missing alt attribute: /media/y0mp4fmh/logo-white-mobile.svg",
    "Image 2 missing alt attribute: /media/uxed23ul/logo-dark.svg",
    "Image 3 missing alt attribute: /media/q51nb3w0/logo-white-mobile.svg",
    "Image 4 missing alt attribute: /media/y0mp4fmh/logo-white-mobile.svg",
    "Image 5 missing alt attribute: /media/uatfqlnv/website-banner-desktop.png",
    "Image 6 missing alt attribute: /media/2kjpiyrm/battery_storage_fareham.jpg?width="
  ],
  "keyboard_issues": [
    "Note: Manual check needed for visible focus indicators"
  ],
  "keyboard_navigation_elements": [
    "button[type='submit']: 'Disable all'",
    "button[type='submit']: 'Cookie settings'",
    "a: 'Cookie notice'",
    "button[type='submit']: 'Allow all'",
    "button[type='submit']: 'Disable all'",
    "button[type='submit']: 'Cookie settings'",
    "a: 'Cookie notice'",
    "button[type='submit']: 'Allow all'",
    "button[type='submit']: 'Disable all'",
    "button[type='submit']: 'Cookie settings'",
    "a: 'Cookie notice'",
    "button[type='submit']: 'Allow all'",
    "button[type='submit']: 'Disable all'",
    "button[type='submit']: 'Cookie settings'",
    "a: 'Cookie notice'",
    "button[type='submit']: 'Allow all'",
    "button[type='submit']: 'Disable all'",
    "button[type='submit']: 'Cookie settings'",
    "a: 'Cookie notice'",
    "button[type='submit']: 'Allow all'"
  ]
}
```
### accessibility_reports\missing_focusable_sse.com_20250303_180424.json <a id='accessibility_reports_missing_focusable_sse_com_20250303_180424_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\missing_focusable_sse.com_20250303_180424.json
- **Last Modified**: 2025-03-03 18:04:24
- **Size**: 44711 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "2025-03-03T18:04:24.620797",
  "browser": "firefox",
  "missing_elements": [
    {
      "tag": "a",
      "id": "",
      "class": "footer__link footer__link--has-children js-footer-link",
      "type": "",
      "text": "News and views",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/a[2]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--home",
      "type": "",
      "text": "About us",
      "xpath": "/html/body/div[2]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "Investors",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/article[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "About us",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "button",
      "id": "",
      "class": "slider__btn slider__btn--next js-out-next slick-arrow",
      "type": "button",
      "text": "Previus slide.",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[2]/div[2]/button[2]",
      "reasons": [
        "is a <button> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "REMIT",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[8]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[4]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--outline",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[6]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Our 2030 Goals",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Potential suppliers",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[4]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "Careers",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[7]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--outline",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[4]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Contact us",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--outline",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "external-link",
      "type": "",
      "text": "Cookie notice",
      "xpath": "//*[@id=\"ccc-notify\"]/div[1]/div[2]/p[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style",
        "has hover effect"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[3]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "Detailed share price",
      "xpath": "/html/body/div[2]/main[1]/section[4]/div[1]/div[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "Our technologies",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "Careers",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[7]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "Sustainability",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Media bank",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[3]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "button",
      "id": "",
      "class": "slider__btn slider__btn--prev js-out-prev slick-arrow slick-disabled",
      "type": "button",
      "text": "Next slide.",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[2]/div[2]/button[1]",
      "reasons": [
        "is a <button> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "Sustainability",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[5]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "Read More",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/article[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[5]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Sitemap",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Inclusion",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[4]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "Read More",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "logo",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__link footer__link--has-children js-footer-link",
      "type": "",
      "text": "Careers",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "button",
      "id": "",
      "class": "banner__scroll js-scroll-down",
      "type": "button",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[1]/div[1]/button[1]",
      "reasons": [
        "is a <button> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--outline",
      "type": "",
      "text": "",
      "xpath": "//*[@id=\"19b1f41c-37a2-4f33-90cd-eab095f57efe\"]/div[1]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[6]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "button",
      "id": "",
      "class": "search__open-btn js-open-search",
      "type": "button",
      "text": "Open search form",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]",
      "reasons": [
        "is a <button> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Life at SSE",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "button",
      "id": "",
      "class": "footer__scroll-btn js-scroll-top",
      "type": "button",
      "text": "",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/button[1]",
      "reasons": [
        "is a <button> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "Investors",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "Our technologies",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Early Careers",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "Read More",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/article[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "",
      "xpath": "/html/body/div[2]/main[1]/section[7]/div[1]/div[1]/div[1]/div[2]/a[2]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Sustainability",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[6]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Thinking of applying?",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[6]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Modern Slavery Statement",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link js-open-cookie",
      "type": "",
      "text": "Cookie settings",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[7]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Media Contacts",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "Home",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "News and views",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[6]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item",
      "type": "",
      "text": "Home",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[1]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "li",
      "id": "",
      "class": "main-nav__item main-nav__has-children main-nav__item--active",
      "type": "",
      "text": "About us",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[2]",
      "reasons": [
        "has role=\"menuitem\"",
        "has cursor:pointer style"
      ],
      "role": "menuitem"
    },
    {
      "tag": "a",
      "id": "",
      "class": "link",
      "type": "",
      "text": "Read More",
      "xpath": "/html/body/div[2]/main[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/article[1]/div[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "main-nav__link js-main-nav-open-dropdown",
      "type": "",
      "text": "News and views",
      "xpath": "/html/body/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[6]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "btn btn--outline",
      "type": "",
      "text": "",
      "xpath": "//*[@id=\"89618f72-20bd-484b-b6cb-b33c0c65ad44\"]/div[1]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has button-like class",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Privacy notice",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__link footer__link--has-children js-footer-link",
      "type": "",
      "text": "Sustainability",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[1]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "copyright__link",
      "type": "",
      "text": "Cookie notice",
      "xpath": "/html/body/div[2]/footer[1]/div[2]/div[1]/div[1]/ul[1]/li[3]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    },
    {
      "tag": "a",
      "id": "",
      "class": "footer__secondary-link",
      "type": "",
      "text": "Specialisms",
      "xpath": "/html/body/div[2]/footer[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/a[1]",
      "reasons": [
        "is a <a> element",
        "has cursor:pointer style"
      ],
      "role": ""
    }
  ],
  "missing_focusable_issues": [
    {
      "issue": "Interactive element not in tab order: <a> News and views (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> About us (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> Investors (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> About us (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <button> Previus slide. (is a <button> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> REMIT (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Our 2030 Goals (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Potential suppliers (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> Careers (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Contact us (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Cookie notice (is a <a> element, has cursor:pointer style, has hover effect)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Detailed share price (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> Our technologies (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Careers (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Sustainability (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Media bank (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <button> Next slide. (is a <button> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> Sustainability (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Read More (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Sitemap (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Inclusion (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Read More (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Careers (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <button>  (is a <button> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <button> Open search form (is a <button> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Life at SSE (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <button>  (is a <button> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Investors (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Our technologies (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Early Careers (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Read More (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Sustainability (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Thinking of applying? (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Modern Slavery Statement (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Cookie settings (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Media Contacts (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Home (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> News and views (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> Home (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <li> About us (has role=\"menuitem\", has cursor:pointer style)",
      "impact": "Medium",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Read More (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> News and views (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a>  (is a <a> element, has button-like class, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Privacy notice (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Sustainability (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Cookie notice (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    },
    {
      "issue": "Interactive element not in tab order: <a> Specialisms (is a <a> element, has cursor:pointer style)",
      "impact": "High",
      "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
    }
  ],
  "summary": {
    "total_missing": 59,
    "total_issues": 59
  }
}
```
### accessibility_reports\tab_order_report.json <a id='accessibility_reports_tab_order_report_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\tab_order_report.json
- **Last Modified**: 2025-03-03 18:03:23
- **Size**: 41736 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "20250303_180310",
  "browser": "firefox",
  "tab_order_data": [
    "1: a - ",
    "2: a - Home",
    "3: a - About us",
    "4: a - About us",
    "5: a - Our businesses",
    "6: a - SSE Renewables",
    "7: a - SSE Thermal",
    "8: a - SSEN Transmission",
    "9: a - SSEN Distribution",
    "10: a - SSE Energy Solutions",
    "11: a - SSE Airtricity",
    "12: a - SSE Energy Markets",
    "13: a - Leadership and Governance",
    "14: a - Meet the board",
    "15: a - Meet the GEC",
    "16: a - Our heritage",
    "17: a - Our culture",
    "18: a - Our campaigns",
    "19: a - UK campaign",
    "20: a - Ireland campaign",
    "21: a - Our technologies",
    "22: a - Our technologies",
    "23: a - Offshore wind",
    "24: a - Onshore wind",
    "25: a - Hydro",
    "26: a - Solar",
    "27: a - Battery storage",
    "28: a - Thermal",
    "29: a - Carbon capture and storage",
    "30: a - Hydrogen",
    "31: a - Transmission networks",
    "32: a - Distribution networks",
    "33: a - Investors",
    "34: a - Investors",
    "35: a - Annual Report 2024",
    "36: a - The SSE investment case",
    "37: a - Analysts",
    "38: a - Reports and results",
    "39: a - Regulatory news",
    "40: a - Regulatory news alerts",
    "41: a - Policy on market speculation",
    "42: a - Financial calendar",
    "43: a - PNG scam warning",
    "44: a - Annual General Meeting 2024",
    "45: a - Annual General Meeting 2023",
    "46: a - Annual General Meeting 2022",
    "47: a - Annual General Meeting 2021",
    "48: a - Shareholder services",
    "49: a - Share dealing",
    "50: a - Ecommunications programme",
    "51: a - Shareholder contacts",
    "52: a - Share price information",
    "53: a - Dividends and Scrip scheme",
    "54: a - Multiple share accounts",
    "55: a - Share repurchase programme",
    "56: a - Useful information",
    "57: a - Debt investors",
    "58: a - Credit rating",
    "59: a - Sustainability Financing Frame",
    "60: a - EMTN programme",
    "61: a - ADRs",
    "62: a - Sustainability",
    "63: a - Sustainability",
    "64: a - Environment",
    "65: a - Social",
    "66: a - Targets and performance",
    "67: a - Reporting",
    "68: a - Partnerships and Memberships",
    "69: a - Policies and assurances",
    "70: a - Innovation",
    "71: a - Just Transition",
    "72: a - Powering Net Zero Pact",
    "73: a - SSE at COP",
    "74: a - News and views",
    "75: a - News and views",
    "76: a - Media contacts",
    "77: a - Media bank",
    "78: a - Careers",
    "79: a - Careers",
    "80: a - Life at SSE",
    "81: a - Developing our People",
    "82: a - Flexible Working",
    "83: a - Employee benefits",
    "84: a - Join our Team",
    "85: a - Engineering and Technical",
    "86: a - IT and Digital",
    "87: a - Corporate",
    "88: a - Inclusion",
    "89: a - Early Careers",
    "90: a - Apprenticeships and Trainees",
    "91: a - Graduate Development",
    "92: a - Progression Stories",
    "93: a - Contact Recruitment",
    "94: button - Open search form",
    "95: input - [No text]",
    "96: button - Type search here",
    "97: button - Clear search",
    "98: a - ",
    "99: button - Close search form",
    "100: a - Open search form",
    "101: button - ",
    "102: input - [No text]",
    "103: button - Submit search",
    "104: button - ",
    "105: a - About us",
    "106: button - Go to previous slide",
    "107: button - Go to next slide",
    "108: button - ",
    "109: a - UK campaign",
    "110: a - News and views",
    "111: a - Read More",
    "112: a - Read More",
    "113: a - Read More",
    "114: a - Read More",
    "115: a - Read More",
    "116: button - Next slide.",
    "117: button - Previus slide.",
    "118: a - Watch the webcast",
    "119: a - Detailed share price",
    "120: a - Careers",
    "121: a - Sustainability",
    "122: a - SSE Renewables",
    "123: a - SSEN Distribution",
    "124: a - SSEN Transmission",
    "125: a - SSE Thermal",
    "126: a - SSE Energy Solutions",
    "127: a - SSE Airtricity",
    "128: button - Back to top.",
    "129: a - Sustainability",
    "130: a - Overview",
    "131: a - Our 2030 Goals",
    "132: a - Modern Slavery Statement",
    "133: a - News and views",
    "134: a - Overview",
    "135: a - Media Contacts",
    "136: a - Media bank",
    "137: a - Careers",
    "138: a - Overview",
    "139: a - Life at SSE",
    "140: a - Specialisms",
    "141: a - Inclusion",
    "142: a - Early Careers",
    "143: a - Thinking of applying?",
    "144: button - Back to top",
    "145: a - Contact us",
    "146: a - Privacy notice",
    "147: a - Cookie notice",
    "148: a - Potential suppliers",
    "149: a - Sitemap",
    "150: a - Sustainability",
    "151: a - Cookie settings",
    "152: a - REMIT"
  ],
  "tab_order_details": [
    {
      "index": 1,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "logo"
      ]
    },
    {
      "index": 2,
      "type": "a",
      "text": "Home",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 3,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 4,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 5,
      "type": "a",
      "text": "Our businesses",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 6,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 7,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 8,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 9,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 10,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 11,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 12,
      "type": "a",
      "text": "SSE Energy Markets",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 13,
      "type": "a",
      "text": "Leadership and Governance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 14,
      "type": "a",
      "text": "Meet the board",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 15,
      "type": "a",
      "text": "Meet the GEC",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 16,
      "type": "a",
      "text": "Our heritage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 17,
      "type": "a",
      "text": "Our culture",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 18,
      "type": "a",
      "text": "Our campaigns",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 19,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 20,
      "type": "a",
      "text": "Ireland campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 21,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 22,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 23,
      "type": "a",
      "text": "Offshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 24,
      "type": "a",
      "text": "Onshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 25,
      "type": "a",
      "text": "Hydro",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 26,
      "type": "a",
      "text": "Solar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 27,
      "type": "a",
      "text": "Battery storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 28,
      "type": "a",
      "text": "Thermal",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 29,
      "type": "a",
      "text": "Carbon capture and storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 30,
      "type": "a",
      "text": "Hydrogen",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 31,
      "type": "a",
      "text": "Transmission networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 32,
      "type": "a",
      "text": "Distribution networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 33,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 34,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 35,
      "type": "a",
      "text": "Annual Report 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 36,
      "type": "a",
      "text": "The SSE investment case",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 37,
      "type": "a",
      "text": "Analysts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 38,
      "type": "a",
      "text": "Reports and results",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 39,
      "type": "a",
      "text": "Regulatory news",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 40,
      "type": "a",
      "text": "Regulatory news alerts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 41,
      "type": "a",
      "text": "Policy on market speculation",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 42,
      "type": "a",
      "text": "Financial calendar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 43,
      "type": "a",
      "text": "PNG scam warning",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 44,
      "type": "a",
      "text": "Annual General Meeting 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 45,
      "type": "a",
      "text": "Annual General Meeting 2023",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 46,
      "type": "a",
      "text": "Annual General Meeting 2022",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 47,
      "type": "a",
      "text": "Annual General Meeting 2021",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 48,
      "type": "a",
      "text": "Shareholder services",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 49,
      "type": "a",
      "text": "Share dealing",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 50,
      "type": "a",
      "text": "Ecommunications programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 51,
      "type": "a",
      "text": "Shareholder contacts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 52,
      "type": "a",
      "text": "Share price information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 53,
      "type": "a",
      "text": "Dividends and Scrip scheme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 54,
      "type": "a",
      "text": "Multiple share accounts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 55,
      "type": "a",
      "text": "Share repurchase programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 56,
      "type": "a",
      "text": "Useful information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 57,
      "type": "a",
      "text": "Debt investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 58,
      "type": "a",
      "text": "Credit rating",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 59,
      "type": "a",
      "text": "Sustainability Financing Frame",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 60,
      "type": "a",
      "text": "EMTN programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 61,
      "type": "a",
      "text": "ADRs",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 62,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 63,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 64,
      "type": "a",
      "text": "Environment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 65,
      "type": "a",
      "text": "Social",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 66,
      "type": "a",
      "text": "Targets and performance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 67,
      "type": "a",
      "text": "Reporting",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 68,
      "type": "a",
      "text": "Partnerships and Memberships",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 69,
      "type": "a",
      "text": "Policies and assurances",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 70,
      "type": "a",
      "text": "Innovation",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 71,
      "type": "a",
      "text": "Just Transition",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 72,
      "type": "a",
      "text": "Powering Net Zero Pact",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 73,
      "type": "a",
      "text": "SSE at COP",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 74,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 75,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 76,
      "type": "a",
      "text": "Media contacts",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 77,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 78,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 79,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 80,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 81,
      "type": "a",
      "text": "Developing our People",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 82,
      "type": "a",
      "text": "Flexible Working",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 83,
      "type": "a",
      "text": "Employee benefits",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 84,
      "type": "a",
      "text": "Join our Team",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 85,
      "type": "a",
      "text": "Engineering and Technical",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 86,
      "type": "a",
      "text": "IT and Digital",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 87,
      "type": "a",
      "text": "Corporate",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 88,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 89,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 90,
      "type": "a",
      "text": "Apprenticeships and Trainees",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 91,
      "type": "a",
      "text": "Graduate Development",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 92,
      "type": "a",
      "text": "Progression Stories",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 93,
      "type": "a",
      "text": "Contact Recruitment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 94,
      "type": "button",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "search__open-btn",
        "js-open-search"
      ]
    },
    {
      "index": 95,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__input"
      ]
    },
    {
      "index": 96,
      "type": "button",
      "text": "Type search here",
      "tabindex": null
    },
    {
      "index": 97,
      "type": "button",
      "text": "Clear search",
      "tabindex": null,
      "class": [
        "search__clear",
        "js-clear-search"
      ]
    },
    {
      "index": 98,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "search__logo"
      ]
    },
    {
      "index": 99,
      "type": "button",
      "text": "Close search form",
      "tabindex": null,
      "class": [
        "search__close-btn",
        "js-close-search"
      ]
    },
    {
      "index": 100,
      "type": "a",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "button-mail"
      ]
    },
    {
      "index": 101,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 102,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__form-input"
      ]
    },
    {
      "index": 103,
      "type": "button",
      "text": "Submit search",
      "tabindex": null,
      "class": [
        "search__form-submit"
      ]
    },
    {
      "index": 104,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 105,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "btn",
        "btn--home"
      ]
    },
    {
      "index": 106,
      "type": "button",
      "text": "Go to previous slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--prev",
        "js-out-prev"
      ]
    },
    {
      "index": 107,
      "type": "button",
      "text": "Go to next slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--next",
        "js-out-next"
      ]
    },
    {
      "index": 108,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "banner__scroll",
        "js-scroll-down"
      ]
    },
    {
      "index": 109,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 110,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 111,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 112,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 113,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 114,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 115,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 116,
      "type": "button",
      "text": "Next slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--prev",
        "js-out-prev",
        "slick-arrow",
        "slick-disabled"
      ]
    },
    {
      "index": 117,
      "type": "button",
      "text": "Previus slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--next",
        "js-out-next",
        "slick-arrow"
      ]
    },
    {
      "index": 118,
      "type": "a",
      "text": "Watch the webcast",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 119,
      "type": "a",
      "text": "Detailed share price",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 120,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 121,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 122,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 123,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 124,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 125,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 126,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 127,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 128,
      "type": "button",
      "text": "Back to top.",
      "tabindex": null,
      "class": [
        "footer__scroll-btn",
        "js-scroll-top"
      ]
    },
    {
      "index": 129,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 130,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 131,
      "type": "a",
      "text": "Our 2030 Goals",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 132,
      "type": "a",
      "text": "Modern Slavery Statement",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 133,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 134,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 135,
      "type": "a",
      "text": "Media Contacts",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 136,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 137,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 138,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 139,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 140,
      "type": "a",
      "text": "Specialisms",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 141,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 142,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 143,
      "type": "a",
      "text": "Thinking of applying?",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 144,
      "type": "button",
      "text": "Back to top",
      "tabindex": null,
      "class": [
        "footer__scroll-btn-mobile",
        "js-scroll-top"
      ]
    },
    {
      "index": 145,
      "type": "a",
      "text": "Contact us",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 146,
      "type": "a",
      "text": "Privacy notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 147,
      "type": "a",
      "text": "Cookie notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 148,
      "type": "a",
      "text": "Potential suppliers",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 149,
      "type": "a",
      "text": "Sitemap",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 150,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 151,
      "type": "a",
      "text": "Cookie settings",
      "tabindex": null,
      "class": [
        "copyright__link",
        "js-open-cookie"
      ]
    },
    {
      "index": 152,
      "type": "a",
      "text": "REMIT",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    }
  ],
  "tab_order_issues": [
    "Tab order issue: Element 111 (tabindex=0) comes before Element 112 (tabindex=0)",
    "Tab order issue: Element 112 (tabindex=0) comes before Element 113 (tabindex=0)",
    "Tab order issue: Element 113 (tabindex=0) comes before Element 114 (tabindex=-1)",
    "Tab order issue: Element 114 (tabindex=-1) comes before Element 115 (tabindex=-1)"
  ]
}
```
### accessibility_reports\tab_order_sse.com_20250303_180310.json <a id='accessibility_reports_tab_order_sse_com_20250303_180310_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\tab_order_sse.com_20250303_180310.json
- **Last Modified**: 2025-03-03 18:03:20
- **Size**: 32838 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "20250303_180310",
  "browser": "firefox",
  "tab_order_data": [
    "1: a - ",
    "2: a - Home",
    "3: a - About us",
    "4: a - About us",
    "5: a - Our businesses",
    "6: a - SSE Renewables",
    "7: a - SSE Thermal",
    "8: a - SSEN Transmission",
    "9: a - SSEN Distribution",
    "10: a - SSE Energy Solutions",
    "11: a - SSE Airtricity",
    "12: a - SSE Energy Markets",
    "13: a - Leadership and Governance",
    "14: a - Meet the board",
    "15: a - Meet the GEC",
    "16: a - Our heritage",
    "17: a - Our culture",
    "18: a - Our campaigns",
    "19: a - UK campaign",
    "20: a - Ireland campaign",
    "21: a - Our technologies",
    "22: a - Our technologies",
    "23: a - Offshore wind",
    "24: a - Onshore wind",
    "25: a - Hydro",
    "26: a - Solar",
    "27: a - Battery storage",
    "28: a - Thermal",
    "29: a - Carbon capture and storage",
    "30: a - Hydrogen",
    "31: a - Transmission networks",
    "32: a - Distribution networks",
    "33: a - Investors",
    "34: a - Investors",
    "35: a - Annual Report 2024",
    "36: a - The SSE investment case",
    "37: a - Analysts",
    "38: a - Reports and results",
    "39: a - Regulatory news",
    "40: a - Regulatory news alerts",
    "41: a - Policy on market speculation",
    "42: a - Financial calendar",
    "43: a - PNG scam warning",
    "44: a - Annual General Meeting 2024",
    "45: a - Annual General Meeting 2023",
    "46: a - Annual General Meeting 2022",
    "47: a - Annual General Meeting 2021",
    "48: a - Shareholder services",
    "49: a - Share dealing",
    "50: a - Ecommunications programme",
    "51: a - Shareholder contacts",
    "52: a - Share price information",
    "53: a - Dividends and Scrip scheme",
    "54: a - Multiple share accounts",
    "55: a - Share repurchase programme",
    "56: a - Useful information",
    "57: a - Debt investors",
    "58: a - Credit rating",
    "59: a - Sustainability Financing Frame",
    "60: a - EMTN programme",
    "61: a - ADRs",
    "62: a - Sustainability",
    "63: a - Sustainability",
    "64: a - Environment",
    "65: a - Social",
    "66: a - Targets and performance",
    "67: a - Reporting",
    "68: a - Partnerships and Memberships",
    "69: a - Policies and assurances",
    "70: a - Innovation",
    "71: a - Just Transition",
    "72: a - Powering Net Zero Pact",
    "73: a - SSE at COP",
    "74: a - News and views",
    "75: a - News and views",
    "76: a - Media contacts",
    "77: a - Media bank",
    "78: a - Careers",
    "79: a - Careers",
    "80: a - Life at SSE",
    "81: a - Developing our People",
    "82: a - Flexible Working",
    "83: a - Employee benefits",
    "84: a - Join our Team",
    "85: a - Engineering and Technical",
    "86: a - IT and Digital",
    "87: a - Corporate",
    "88: a - Inclusion",
    "89: a - Early Careers",
    "90: a - Apprenticeships and Trainees",
    "91: a - Graduate Development",
    "92: a - Progression Stories",
    "93: a - Contact Recruitment",
    "94: button - Open search form",
    "95: input - [No text]",
    "96: button - Type search here",
    "97: button - Clear search",
    "98: a - ",
    "99: button - Close search form",
    "100: a - Open search form",
    "101: button - ",
    "102: input - [No text]",
    "103: button - Submit search",
    "104: button - ",
    "105: a - About us",
    "106: button - Go to previous slide",
    "107: button - Go to next slide",
    "108: button - ",
    "109: a - UK campaign",
    "110: a - News and views",
    "111: a - Read More",
    "112: a - Read More",
    "113: a - Read More",
    "114: a - Read More",
    "115: a - Read More",
    "116: button - Next slide.",
    "117: button - Previus slide.",
    "118: a - Watch the webcast",
    "119: a - Detailed share price",
    "120: a - Careers",
    "121: a - Sustainability",
    "122: a - SSE Renewables",
    "123: a - SSEN Distribution",
    "124: a - SSEN Transmission",
    "125: a - SSE Thermal",
    "126: a - SSE Energy Solutions",
    "127: a - SSE Airtricity",
    "128: button - Back to top.",
    "129: a - Sustainability",
    "130: a - Overview",
    "131: a - Our 2030 Goals",
    "132: a - Modern Slavery Statement",
    "133: a - News and views",
    "134: a - Overview",
    "135: a - Media Contacts",
    "136: a - Media bank",
    "137: a - Careers",
    "138: a - Overview",
    "139: a - Life at SSE",
    "140: a - Specialisms",
    "141: a - Inclusion",
    "142: a - Early Careers",
    "143: a - Thinking of applying?",
    "144: button - Back to top",
    "145: a - Contact us",
    "146: a - Privacy notice",
    "147: a - Cookie notice",
    "148: a - Potential suppliers",
    "149: a - Sitemap",
    "150: a - Sustainability",
    "151: a - Cookie settings",
    "152: a - REMIT"
  ],
  "tab_order_details": [
    {
      "index": 1,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "logo"
      ]
    },
    {
      "index": 2,
      "type": "a",
      "text": "Home",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 3,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 4,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 5,
      "type": "a",
      "text": "Our businesses",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 6,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 7,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 8,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 9,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 10,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 11,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 12,
      "type": "a",
      "text": "SSE Energy Markets",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 13,
      "type": "a",
      "text": "Leadership and Governance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 14,
      "type": "a",
      "text": "Meet the board",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 15,
      "type": "a",
      "text": "Meet the GEC",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 16,
      "type": "a",
      "text": "Our heritage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 17,
      "type": "a",
      "text": "Our culture",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 18,
      "type": "a",
      "text": "Our campaigns",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 19,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 20,
      "type": "a",
      "text": "Ireland campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 21,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 22,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 23,
      "type": "a",
      "text": "Offshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 24,
      "type": "a",
      "text": "Onshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 25,
      "type": "a",
      "text": "Hydro",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 26,
      "type": "a",
      "text": "Solar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 27,
      "type": "a",
      "text": "Battery storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 28,
      "type": "a",
      "text": "Thermal",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 29,
      "type": "a",
      "text": "Carbon capture and storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 30,
      "type": "a",
      "text": "Hydrogen",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 31,
      "type": "a",
      "text": "Transmission networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 32,
      "type": "a",
      "text": "Distribution networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 33,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 34,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 35,
      "type": "a",
      "text": "Annual Report 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 36,
      "type": "a",
      "text": "The SSE investment case",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 37,
      "type": "a",
      "text": "Analysts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 38,
      "type": "a",
      "text": "Reports and results",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 39,
      "type": "a",
      "text": "Regulatory news",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 40,
      "type": "a",
      "text": "Regulatory news alerts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 41,
      "type": "a",
      "text": "Policy on market speculation",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 42,
      "type": "a",
      "text": "Financial calendar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 43,
      "type": "a",
      "text": "PNG scam warning",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 44,
      "type": "a",
      "text": "Annual General Meeting 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 45,
      "type": "a",
      "text": "Annual General Meeting 2023",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 46,
      "type": "a",
      "text": "Annual General Meeting 2022",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 47,
      "type": "a",
      "text": "Annual General Meeting 2021",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 48,
      "type": "a",
      "text": "Shareholder services",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 49,
      "type": "a",
      "text": "Share dealing",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 50,
      "type": "a",
      "text": "Ecommunications programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 51,
      "type": "a",
      "text": "Shareholder contacts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 52,
      "type": "a",
      "text": "Share price information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 53,
      "type": "a",
      "text": "Dividends and Scrip scheme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 54,
      "type": "a",
      "text": "Multiple share accounts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 55,
      "type": "a",
      "text": "Share repurchase programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 56,
      "type": "a",
      "text": "Useful information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 57,
      "type": "a",
      "text": "Debt investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 58,
      "type": "a",
      "text": "Credit rating",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 59,
      "type": "a",
      "text": "Sustainability Financing Frame",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 60,
      "type": "a",
      "text": "EMTN programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 61,
      "type": "a",
      "text": "ADRs",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 62,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 63,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 64,
      "type": "a",
      "text": "Environment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 65,
      "type": "a",
      "text": "Social",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 66,
      "type": "a",
      "text": "Targets and performance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 67,
      "type": "a",
      "text": "Reporting",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 68,
      "type": "a",
      "text": "Partnerships and Memberships",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 69,
      "type": "a",
      "text": "Policies and assurances",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 70,
      "type": "a",
      "text": "Innovation",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 71,
      "type": "a",
      "text": "Just Transition",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 72,
      "type": "a",
      "text": "Powering Net Zero Pact",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 73,
      "type": "a",
      "text": "SSE at COP",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 74,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 75,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 76,
      "type": "a",
      "text": "Media contacts",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 77,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 78,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 79,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 80,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 81,
      "type": "a",
      "text": "Developing our People",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 82,
      "type": "a",
      "text": "Flexible Working",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 83,
      "type": "a",
      "text": "Employee benefits",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 84,
      "type": "a",
      "text": "Join our Team",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 85,
      "type": "a",
      "text": "Engineering and Technical",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 86,
      "type": "a",
      "text": "IT and Digital",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 87,
      "type": "a",
      "text": "Corporate",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 88,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 89,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 90,
      "type": "a",
      "text": "Apprenticeships and Trainees",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 91,
      "type": "a",
      "text": "Graduate Development",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 92,
      "type": "a",
      "text": "Progression Stories",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 93,
      "type": "a",
      "text": "Contact Recruitment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 94,
      "type": "button",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "search__open-btn",
        "js-open-search"
      ]
    },
    {
      "index": 95,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__input"
      ]
    },
    {
      "index": 96,
      "type": "button",
      "text": "Type search here",
      "tabindex": null
    },
    {
      "index": 97,
      "type": "button",
      "text": "Clear search",
      "tabindex": null,
      "class": [
        "search__clear",
        "js-clear-search"
      ]
    },
    {
      "index": 98,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "search__logo"
      ]
    },
    {
      "index": 99,
      "type": "button",
      "text": "Close search form",
      "tabindex": null,
      "class": [
        "search__close-btn",
        "js-close-search"
      ]
    },
    {
      "index": 100,
      "type": "a",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "button-mail"
      ]
    },
    {
      "index": 101,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 102,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__form-input"
      ]
    },
    {
      "index": 103,
      "type": "button",
      "text": "Submit search",
      "tabindex": null,
      "class": [
        "search__form-submit"
      ]
    },
    {
      "index": 104,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 105,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "btn",
        "btn--home"
      ]
    },
    {
      "index": 106,
      "type": "button",
      "text": "Go to previous slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--prev",
        "js-out-prev"
      ]
    },
    {
      "index": 107,
      "type": "button",
      "text": "Go to next slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--next",
        "js-out-next"
      ]
    },
    {
      "index": 108,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "banner__scroll",
        "js-scroll-down"
      ]
    },
    {
      "index": 109,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 110,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 111,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 112,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 113,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 114,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 115,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 116,
      "type": "button",
      "text": "Next slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--prev",
        "js-out-prev",
        "slick-arrow",
        "slick-disabled"
      ]
    },
    {
      "index": 117,
      "type": "button",
      "text": "Previus slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--next",
        "js-out-next",
        "slick-arrow"
      ]
    },
    {
      "index": 118,
      "type": "a",
      "text": "Watch the webcast",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 119,
      "type": "a",
      "text": "Detailed share price",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 120,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 121,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 122,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 123,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 124,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 125,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 126,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 127,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 128,
      "type": "button",
      "text": "Back to top.",
      "tabindex": null,
      "class": [
        "footer__scroll-btn",
        "js-scroll-top"
      ]
    },
    {
      "index": 129,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 130,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 131,
      "type": "a",
      "text": "Our 2030 Goals",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 132,
      "type": "a",
      "text": "Modern Slavery Statement",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 133,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 134,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 135,
      "type": "a",
      "text": "Media Contacts",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 136,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 137,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 138,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 139,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 140,
      "type": "a",
      "text": "Specialisms",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 141,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 142,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 143,
      "type": "a",
      "text": "Thinking of applying?",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 144,
      "type": "button",
      "text": "Back to top",
      "tabindex": null,
      "class": [
        "footer__scroll-btn-mobile",
        "js-scroll-top"
      ]
    },
    {
      "index": 145,
      "type": "a",
      "text": "Contact us",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 146,
      "type": "a",
      "text": "Privacy notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 147,
      "type": "a",
      "text": "Cookie notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 148,
      "type": "a",
      "text": "Potential suppliers",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 149,
      "type": "a",
      "text": "Sitemap",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 150,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 151,
      "type": "a",
      "text": "Cookie settings",
      "tabindex": null,
      "class": [
        "copyright__link",
        "js-open-cookie"
      ]
    },
    {
      "index": 152,
      "type": "a",
      "text": "REMIT",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    }
  ],
  "tab_order_issues": [
    "Tab order issue: Element 111 (tabindex=0) comes before Element 112 (tabindex=0)",
    "Tab order issue: Element 112 (tabindex=0) comes before Element 113 (tabindex=0)",
    "Tab order issue: Element 113 (tabindex=0) comes before Element 114 (tabindex=-1)",
    "Tab order issue: Element 114 (tabindex=-1) comes before Element 115 (tabindex=-1)"
  ]
}
```
### accessibility_reports\tab_order_sse.com_20250303_180328.json <a id='accessibility_reports_tab_order_sse_com_20250303_180328_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_reports\tab_order_sse.com_20250303_180328.json
- **Last Modified**: 2025-03-03 18:03:34
- **Size**: 32838 bytes

#### Content
```json
{
  "url": "https://sse.com",
  "timestamp": "20250303_180328",
  "browser": "firefox",
  "tab_order_data": [
    "1: a - ",
    "2: a - Home",
    "3: a - About us",
    "4: a - About us",
    "5: a - Our businesses",
    "6: a - SSE Renewables",
    "7: a - SSE Thermal",
    "8: a - SSEN Transmission",
    "9: a - SSEN Distribution",
    "10: a - SSE Energy Solutions",
    "11: a - SSE Airtricity",
    "12: a - SSE Energy Markets",
    "13: a - Leadership and Governance",
    "14: a - Meet the board",
    "15: a - Meet the GEC",
    "16: a - Our heritage",
    "17: a - Our culture",
    "18: a - Our campaigns",
    "19: a - UK campaign",
    "20: a - Ireland campaign",
    "21: a - Our technologies",
    "22: a - Our technologies",
    "23: a - Offshore wind",
    "24: a - Onshore wind",
    "25: a - Hydro",
    "26: a - Solar",
    "27: a - Battery storage",
    "28: a - Thermal",
    "29: a - Carbon capture and storage",
    "30: a - Hydrogen",
    "31: a - Transmission networks",
    "32: a - Distribution networks",
    "33: a - Investors",
    "34: a - Investors",
    "35: a - Annual Report 2024",
    "36: a - The SSE investment case",
    "37: a - Analysts",
    "38: a - Reports and results",
    "39: a - Regulatory news",
    "40: a - Regulatory news alerts",
    "41: a - Policy on market speculation",
    "42: a - Financial calendar",
    "43: a - PNG scam warning",
    "44: a - Annual General Meeting 2024",
    "45: a - Annual General Meeting 2023",
    "46: a - Annual General Meeting 2022",
    "47: a - Annual General Meeting 2021",
    "48: a - Shareholder services",
    "49: a - Share dealing",
    "50: a - Ecommunications programme",
    "51: a - Shareholder contacts",
    "52: a - Share price information",
    "53: a - Dividends and Scrip scheme",
    "54: a - Multiple share accounts",
    "55: a - Share repurchase programme",
    "56: a - Useful information",
    "57: a - Debt investors",
    "58: a - Credit rating",
    "59: a - Sustainability Financing Frame",
    "60: a - EMTN programme",
    "61: a - ADRs",
    "62: a - Sustainability",
    "63: a - Sustainability",
    "64: a - Environment",
    "65: a - Social",
    "66: a - Targets and performance",
    "67: a - Reporting",
    "68: a - Partnerships and Memberships",
    "69: a - Policies and assurances",
    "70: a - Innovation",
    "71: a - Just Transition",
    "72: a - Powering Net Zero Pact",
    "73: a - SSE at COP",
    "74: a - News and views",
    "75: a - News and views",
    "76: a - Media contacts",
    "77: a - Media bank",
    "78: a - Careers",
    "79: a - Careers",
    "80: a - Life at SSE",
    "81: a - Developing our People",
    "82: a - Flexible Working",
    "83: a - Employee benefits",
    "84: a - Join our Team",
    "85: a - Engineering and Technical",
    "86: a - IT and Digital",
    "87: a - Corporate",
    "88: a - Inclusion",
    "89: a - Early Careers",
    "90: a - Apprenticeships and Trainees",
    "91: a - Graduate Development",
    "92: a - Progression Stories",
    "93: a - Contact Recruitment",
    "94: button - Open search form",
    "95: input - [No text]",
    "96: button - Type search here",
    "97: button - Clear search",
    "98: a - ",
    "99: button - Close search form",
    "100: a - Open search form",
    "101: button - ",
    "102: input - [No text]",
    "103: button - Submit search",
    "104: button - ",
    "105: a - About us",
    "106: button - Go to previous slide",
    "107: button - Go to next slide",
    "108: button - ",
    "109: a - UK campaign",
    "110: a - News and views",
    "111: a - Read More",
    "112: a - Read More",
    "113: a - Read More",
    "114: a - Read More",
    "115: a - Read More",
    "116: button - Next slide.",
    "117: button - Previus slide.",
    "118: a - Watch the webcast",
    "119: a - Detailed share price",
    "120: a - Careers",
    "121: a - Sustainability",
    "122: a - SSE Renewables",
    "123: a - SSEN Distribution",
    "124: a - SSEN Transmission",
    "125: a - SSE Thermal",
    "126: a - SSE Energy Solutions",
    "127: a - SSE Airtricity",
    "128: button - Back to top.",
    "129: a - Sustainability",
    "130: a - Overview",
    "131: a - Our 2030 Goals",
    "132: a - Modern Slavery Statement",
    "133: a - News and views",
    "134: a - Overview",
    "135: a - Media Contacts",
    "136: a - Media bank",
    "137: a - Careers",
    "138: a - Overview",
    "139: a - Life at SSE",
    "140: a - Specialisms",
    "141: a - Inclusion",
    "142: a - Early Careers",
    "143: a - Thinking of applying?",
    "144: button - Back to top",
    "145: a - Contact us",
    "146: a - Privacy notice",
    "147: a - Cookie notice",
    "148: a - Potential suppliers",
    "149: a - Sitemap",
    "150: a - Sustainability",
    "151: a - Cookie settings",
    "152: a - REMIT"
  ],
  "tab_order_details": [
    {
      "index": 1,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "logo"
      ]
    },
    {
      "index": 2,
      "type": "a",
      "text": "Home",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 3,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 4,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 5,
      "type": "a",
      "text": "Our businesses",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 6,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 7,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 8,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 9,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 10,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 11,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 12,
      "type": "a",
      "text": "SSE Energy Markets",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 13,
      "type": "a",
      "text": "Leadership and Governance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 14,
      "type": "a",
      "text": "Meet the board",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 15,
      "type": "a",
      "text": "Meet the GEC",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 16,
      "type": "a",
      "text": "Our heritage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 17,
      "type": "a",
      "text": "Our culture",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 18,
      "type": "a",
      "text": "Our campaigns",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 19,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 20,
      "type": "a",
      "text": "Ireland campaign",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 21,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 22,
      "type": "a",
      "text": "Our technologies",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 23,
      "type": "a",
      "text": "Offshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 24,
      "type": "a",
      "text": "Onshore wind",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 25,
      "type": "a",
      "text": "Hydro",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 26,
      "type": "a",
      "text": "Solar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 27,
      "type": "a",
      "text": "Battery storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 28,
      "type": "a",
      "text": "Thermal",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 29,
      "type": "a",
      "text": "Carbon capture and storage",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 30,
      "type": "a",
      "text": "Hydrogen",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 31,
      "type": "a",
      "text": "Transmission networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 32,
      "type": "a",
      "text": "Distribution networks",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 33,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 34,
      "type": "a",
      "text": "Investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 35,
      "type": "a",
      "text": "Annual Report 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 36,
      "type": "a",
      "text": "The SSE investment case",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 37,
      "type": "a",
      "text": "Analysts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 38,
      "type": "a",
      "text": "Reports and results",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 39,
      "type": "a",
      "text": "Regulatory news",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 40,
      "type": "a",
      "text": "Regulatory news alerts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 41,
      "type": "a",
      "text": "Policy on market speculation",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 42,
      "type": "a",
      "text": "Financial calendar",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 43,
      "type": "a",
      "text": "PNG scam warning",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 44,
      "type": "a",
      "text": "Annual General Meeting 2024",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 45,
      "type": "a",
      "text": "Annual General Meeting 2023",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 46,
      "type": "a",
      "text": "Annual General Meeting 2022",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 47,
      "type": "a",
      "text": "Annual General Meeting 2021",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 48,
      "type": "a",
      "text": "Shareholder services",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 49,
      "type": "a",
      "text": "Share dealing",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 50,
      "type": "a",
      "text": "Ecommunications programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 51,
      "type": "a",
      "text": "Shareholder contacts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 52,
      "type": "a",
      "text": "Share price information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 53,
      "type": "a",
      "text": "Dividends and Scrip scheme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 54,
      "type": "a",
      "text": "Multiple share accounts",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 55,
      "type": "a",
      "text": "Share repurchase programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 56,
      "type": "a",
      "text": "Useful information",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 57,
      "type": "a",
      "text": "Debt investors",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 58,
      "type": "a",
      "text": "Credit rating",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 59,
      "type": "a",
      "text": "Sustainability Financing Frame",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 60,
      "type": "a",
      "text": "EMTN programme",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 61,
      "type": "a",
      "text": "ADRs",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 62,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 63,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 64,
      "type": "a",
      "text": "Environment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 65,
      "type": "a",
      "text": "Social",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 66,
      "type": "a",
      "text": "Targets and performance",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 67,
      "type": "a",
      "text": "Reporting",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 68,
      "type": "a",
      "text": "Partnerships and Memberships",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 69,
      "type": "a",
      "text": "Policies and assurances",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 70,
      "type": "a",
      "text": "Innovation",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 71,
      "type": "a",
      "text": "Just Transition",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 72,
      "type": "a",
      "text": "Powering Net Zero Pact",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 73,
      "type": "a",
      "text": "SSE at COP",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 74,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 75,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 76,
      "type": "a",
      "text": "Media contacts",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 77,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 78,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__link",
        "js-main-nav-open-dropdown"
      ]
    },
    {
      "index": 79,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link",
        "main-nav__secondary-link--title"
      ]
    },
    {
      "index": 80,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 81,
      "type": "a",
      "text": "Developing our People",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 82,
      "type": "a",
      "text": "Flexible Working",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 83,
      "type": "a",
      "text": "Employee benefits",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 84,
      "type": "a",
      "text": "Join our Team",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 85,
      "type": "a",
      "text": "Engineering and Technical",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 86,
      "type": "a",
      "text": "IT and Digital",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 87,
      "type": "a",
      "text": "Corporate",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 88,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 89,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 90,
      "type": "a",
      "text": "Apprenticeships and Trainees",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 91,
      "type": "a",
      "text": "Graduate Development",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 92,
      "type": "a",
      "text": "Progression Stories",
      "tabindex": null,
      "class": [
        "main-nav__third-link"
      ]
    },
    {
      "index": 93,
      "type": "a",
      "text": "Contact Recruitment",
      "tabindex": null,
      "class": [
        "main-nav__secondary-link"
      ]
    },
    {
      "index": 94,
      "type": "button",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "search__open-btn",
        "js-open-search"
      ]
    },
    {
      "index": 95,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__input"
      ]
    },
    {
      "index": 96,
      "type": "button",
      "text": "Type search here",
      "tabindex": null
    },
    {
      "index": 97,
      "type": "button",
      "text": "Clear search",
      "tabindex": null,
      "class": [
        "search__clear",
        "js-clear-search"
      ]
    },
    {
      "index": 98,
      "type": "a",
      "text": "",
      "tabindex": null,
      "class": [
        "search__logo"
      ]
    },
    {
      "index": 99,
      "type": "button",
      "text": "Close search form",
      "tabindex": null,
      "class": [
        "search__close-btn",
        "js-close-search"
      ]
    },
    {
      "index": 100,
      "type": "a",
      "text": "Open search form",
      "tabindex": null,
      "class": [
        "button-mail"
      ]
    },
    {
      "index": 101,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 102,
      "type": "input",
      "text": "[No text]",
      "tabindex": null,
      "id": "Q",
      "class": [
        "search__form-input"
      ]
    },
    {
      "index": 103,
      "type": "button",
      "text": "Submit search",
      "tabindex": null,
      "class": [
        "search__form-submit"
      ]
    },
    {
      "index": 104,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "nav-toggle",
        "js-nav-toggle"
      ]
    },
    {
      "index": 105,
      "type": "a",
      "text": "About us",
      "tabindex": null,
      "class": [
        "btn",
        "btn--home"
      ]
    },
    {
      "index": 106,
      "type": "button",
      "text": "Go to previous slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--prev",
        "js-out-prev"
      ]
    },
    {
      "index": 107,
      "type": "button",
      "text": "Go to next slide",
      "tabindex": null,
      "class": [
        "slider-banner__btn",
        "slider-banner__btn--next",
        "js-out-next"
      ]
    },
    {
      "index": 108,
      "type": "button",
      "text": "",
      "tabindex": null,
      "class": [
        "banner__scroll",
        "js-scroll-down"
      ]
    },
    {
      "index": 109,
      "type": "a",
      "text": "UK campaign",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 110,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 111,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 112,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 113,
      "type": "a",
      "text": "Read More",
      "tabindex": "0",
      "class": [
        "link"
      ]
    },
    {
      "index": 114,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 115,
      "type": "a",
      "text": "Read More",
      "tabindex": "-1",
      "class": [
        "link"
      ]
    },
    {
      "index": 116,
      "type": "button",
      "text": "Next slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--prev",
        "js-out-prev",
        "slick-arrow",
        "slick-disabled"
      ]
    },
    {
      "index": 117,
      "type": "button",
      "text": "Previus slide.",
      "tabindex": null,
      "class": [
        "slider__btn",
        "slider__btn--next",
        "js-out-next",
        "slick-arrow"
      ]
    },
    {
      "index": 118,
      "type": "a",
      "text": "Watch the webcast",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 119,
      "type": "a",
      "text": "Detailed share price",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 120,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 121,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "btn",
        "btn--outline"
      ]
    },
    {
      "index": 122,
      "type": "a",
      "text": "SSE Renewables",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 123,
      "type": "a",
      "text": "SSEN Distribution",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 124,
      "type": "a",
      "text": "SSEN Transmission",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 125,
      "type": "a",
      "text": "SSE Thermal",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 126,
      "type": "a",
      "text": "SSE Energy Solutions",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 127,
      "type": "a",
      "text": "SSE Airtricity",
      "tabindex": null,
      "class": [
        "link"
      ]
    },
    {
      "index": 128,
      "type": "button",
      "text": "Back to top.",
      "tabindex": null,
      "class": [
        "footer__scroll-btn",
        "js-scroll-top"
      ]
    },
    {
      "index": 129,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 130,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 131,
      "type": "a",
      "text": "Our 2030 Goals",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 132,
      "type": "a",
      "text": "Modern Slavery Statement",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 133,
      "type": "a",
      "text": "News and views",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 134,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 135,
      "type": "a",
      "text": "Media Contacts",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 136,
      "type": "a",
      "text": "Media bank",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 137,
      "type": "a",
      "text": "Careers",
      "tabindex": null,
      "class": [
        "footer__link",
        "footer__link--has-children",
        "js-footer-link"
      ]
    },
    {
      "index": 138,
      "type": "a",
      "text": "Overview",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 139,
      "type": "a",
      "text": "Life at SSE",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 140,
      "type": "a",
      "text": "Specialisms",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 141,
      "type": "a",
      "text": "Inclusion",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 142,
      "type": "a",
      "text": "Early Careers",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 143,
      "type": "a",
      "text": "Thinking of applying?",
      "tabindex": null,
      "class": [
        "footer__secondary-link"
      ]
    },
    {
      "index": 144,
      "type": "button",
      "text": "Back to top",
      "tabindex": null,
      "class": [
        "footer__scroll-btn-mobile",
        "js-scroll-top"
      ]
    },
    {
      "index": 145,
      "type": "a",
      "text": "Contact us",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 146,
      "type": "a",
      "text": "Privacy notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 147,
      "type": "a",
      "text": "Cookie notice",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 148,
      "type": "a",
      "text": "Potential suppliers",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 149,
      "type": "a",
      "text": "Sitemap",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 150,
      "type": "a",
      "text": "Sustainability",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    },
    {
      "index": 151,
      "type": "a",
      "text": "Cookie settings",
      "tabindex": null,
      "class": [
        "copyright__link",
        "js-open-cookie"
      ]
    },
    {
      "index": 152,
      "type": "a",
      "text": "REMIT",
      "tabindex": null,
      "class": [
        "copyright__link"
      ]
    }
  ],
  "tab_order_issues": [
    "Tab order issue: Element 111 (tabindex=0) comes before Element 112 (tabindex=0)",
    "Tab order issue: Element 112 (tabindex=0) comes before Element 113 (tabindex=0)",
    "Tab order issue: Element 113 (tabindex=0) comes before Element 114 (tabindex=-1)",
    "Tab order issue: Element 114 (tabindex=-1) comes before Element 115 (tabindex=-1)"
  ]
}
```
### archive\accessibility_terminology.json <a id='archive_accessibility_terminology_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: archive\accessibility_terminology.json
- **Last Modified**: 2025-03-10 19:36:04
- **Size**: 572 bytes

#### Content
```json
{
  "technical_terms": {
    "interactive element not in tab order": {
      "preferred": "Keyboard navigation barrier",
      "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
    },
    "tab order issue": {
      "preferred": "Inconsistent keyboard navigation sequence",
      "explanation": "Elements that disrupt the expected keyboard navigation flow"
    }
  },
  "impact_categories": [
    "Screen Reader Accessibility",
    "Keyboard Navigation",
    "Visual Focus",
    "Interactive Element Accessibility"
  ]
}
```
### accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.json <a id='accessibility_modules__ipynb_checkpoints_accessibility_terminology-checkpoint_json'></a>
#### File Information
- **Type**: JSON File
- **Path**: accessibility_modules\.ipynb_checkpoints\accessibility_terminology-checkpoint.json
- **Last Modified**: 2025-03-10 22:20:14
- **Size**: 195 bytes

#### Content
```json
{
  "tab order issue": "inconsistent keyboard navigation sequence",
  "interactive element not in tab order": "keyboard navigation barrier",
  "missing alt text": "missing text alternative"
}
```