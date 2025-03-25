# Project Scripts Overview
*Generated on 2025-03-17 23:40:47 from folder: C:\Users\clint\Pickles*
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

### Python Scripts
- [accessibility_checker.py](#accessibility_checker_py)
- [create_terminology.py](#create_terminology_py)
- [create_terminology_file.py](#create_terminology_file_py)
- [script_extract.py](#script_extract_py)
- [accessibility_modules\aria_checker.py](#accessibility_modules_aria_checker_py)
- [accessibility_modules\color_contrast.py](#accessibility_modules_color_contrast_py)
- [accessibility_modules\dynamic_content_tester.py](#accessibility_modules_dynamic_content_tester_py)
- [accessibility_modules\focusable_elements.py](#accessibility_modules_focusable_elements_py)
- [accessibility_modules\focus_order_checker.py](#accessibility_modules_focus_order_checker_py)
- [accessibility_modules\html_report_generator.py](#accessibility_modules_html_report_generator_py)
- [accessibility_modules\image_checker.py](#accessibility_modules_image_checker_py)
- [accessibility_modules\report_generator.py](#accessibility_modules_report_generator_py)
- [accessibility_modules\simple_html_report_generator.py](#accessibility_modules_simple_html_report_generator_py)
- [accessibility_modules\tab_order_checker.py](#accessibility_modules_tab_order_checker_py)
- [accessibility_modules\terminology_validator.py](#accessibility_modules_terminology_validator_py)
- [accessibility_modules\__init__.py](#accessibility_modules___init___py)
- [accessibility_modules\component_tests\slider_tester.py](#accessibility_modules_component_tests_slider_tester_py)
- [accessibility_modules\component_tests\__init__.py](#accessibility_modules_component_tests___init___py)

### Text Files (Main Folder Only)
- [next_steps.txt](#next_steps_txt)
- [paste.txt](#paste_txt)
- [project structure.txt](#project structure_txt)
- [requirements.txt](#requirements_txt)

### JSON Files (Main Folder Only)
- [accessibility_terminology.json](#accessibility_terminology_json)

## Python Scripts

### accessibility_checker.py <a id='accessibility_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_checker.py
- **Last Modified**: 2025-03-17 23:38:20
- **Size**: 13124 bytes

#### Code
```python
"""
Enhanced Accessibility Checker with Dynamic Content Testing

Integrates comprehensive accessibility checks including dynamic content analysis.
"""

import os
import sys
import logging
import time
import json  # Added missing import
from datetime import datetime

# Add the current directory to Python path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Selenium and WebDriver imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Import accessibility modules
from accessibility_modules.dynamic_content_tester import run_advanced_dynamic_content_test
from accessibility_modules.report_generator import integrate_dynamic_content_results, \
    generate_dynamic_content_report_section, export_dynamic_content_state_tracking

# Import other existing modules
from accessibility_modules.tab_order_checker import check_tab_order
from accessibility_modules.focusable_elements import check_missing_focusable_elements
from accessibility_modules.aria_checker import check_aria_accessibility
from accessibility_modules.color_contrast import check_color_contrast
from accessibility_modules.image_checker import check_image_accessibility

def setup_driver(browser_name='chrome', headless=True):
    """
    Set up and return a WebDriver instance for the specified browser.
    
    Args:
        browser_name (str): Name of the browser to use
        headless (bool): Whether to run in headless mode
        
    Returns:
        WebDriver: Configured WebDriver instance
    """
    browser_name = browser_name.lower()
    try:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        # Set standard window size
        driver.set_window_size(1366, 768)
        return driver
        
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {str(e)}")
        raise

def run_comprehensive_accessibility_check(url, browser='chrome', output_dir=None):
    """
    Perform a comprehensive accessibility check on a given URL.
    
    Args:
        url (str): URL to check
        browser (str): Browser to use for testing
        output_dir (str): Directory to save reports
    
    Returns:
        dict: Comprehensive accessibility report
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    # Create output directory if not specified
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), 'accessibility_reports')
    os.makedirs(output_dir, exist_ok=True)
    
    # Timestamp for this run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize report
    report = {
        "url": url,
        "timestamp": timestamp,
        "browser": browser
    }
    
    # Initialize driver
    driver = None
    try:
        # Set up WebDriver
        driver = setup_driver(browser)
        
        # Navigate to URL
        start_time = time.time()
        driver.get(url)
        
        # Allow page to load
        time.sleep(3)
        
        # Run accessibility checks
        checks = [
            ("tab_order", check_tab_order, driver),
            ("focusable_elements", check_missing_focusable_elements, driver),
            ("aria_accessibility", check_aria_accessibility, driver),
            ("color_contrast", check_color_contrast, driver),
            ("image_accessibility", check_image_accessibility, driver)
        ]
        
        # Store results of individual checks
        report['checks'] = {}
        for check_name, check_func, *args in checks:
            try:
                result = check_func(*args)
                report['checks'][check_name] = result
            except Exception as e:
                logging.error(f"Error in {check_name} check: {str(e)}")
                report['checks'][check_name] = {
                    "status": "error",
                    "error": str(e)
                }
        
        # Run dynamic content testing
        dynamic_content_results = run_advanced_dynamic_content_test(driver)
        
        # Integrate dynamic content results
        report = integrate_dynamic_content_results(report, dynamic_content_results)
        
        # Calculate overall report summary
        calculate_report_summary(report)
        
        # Generate additional outputs
        generate_report_outputs(report, output_dir)
        
        return report
        
    except Exception as e:
        logging.error(f"Comprehensive accessibility check failed: {str(e)}")
        report['error'] = str(e)
        return report
    
    finally:
        # Always quit the driver
        if driver:
            driver.quit()

def calculate_report_summary(report):
    """
    Calculate an overall accessibility summary for the report.
    
    Args:
        report (dict): Accessibility report to summarize
    """
    # Initialize summary
    report['summary'] = {
        'critical_issues': 0,
        'warnings': 0,
        'passed_checks': 0,
        'total_checks': 0,
        'accessibility_score': 100
    }
    
    # Count issues across different checks
    for check_name, check_results in report.get('checks', {}).items():
        report['summary']['total_checks'] += 1
        
        # Check for issues in each module's results
        issues = check_results.get('issues', [])
        if not issues:
            report['summary']['passed_checks'] += 1
        
        # Count issue severities
        for issue in issues:
            severity = issue.get('severity', issue.get('type', 'warning'))
            if severity == 'critical':
                report['summary']['critical_issues'] += 1
            else:
                report['summary']['warnings'] += 1
    
    # Incorporate dynamic content issues
    dynamic_content = report.get('dynamic_content', {}).get('summary', {})
    report['summary']['dynamic_content_issues'] = dynamic_content.get('components_with_issues', 0)
    dynamic_content_score = dynamic_content.get('accessibility_score', 100)
    
    # Calculate final accessibility score
    # Penalize for critical and warning issues
    total_checks = report['summary']['total_checks']
    critical_issues = report['summary']['critical_issues']
    warnings = report['summary']['warnings']
    
    # Scoring algorithm
    base_score = 100
    critical_penalty = critical_issues * 10  # Each critical issue reduces score by 10
    warning_penalty = warnings * 3  # Each warning reduces score by 3
    dynamic_content_penalty = (dynamic_content.get('components_with_issues', 0) * 5)
    
    final_score = max(0, base_score - critical_penalty - warning_penalty - dynamic_content_penalty)
    
    # Incorporate dynamic content score
    final_score = (final_score + dynamic_content_score) / 2
    
    report['summary']['accessibility_score'] = round(final_score, 2)

def generate_report_outputs(report, output_dir):
    """
    Generate various output formats for the accessibility report.
    
    Args:
        report (dict): Accessibility report
        output_dir (str): Directory to save report outputs
    """
    timestamp = report.get('timestamp', datetime.now().strftime("%Y%m%d_%H%M%S"))
    base_filename = f"accessibility_report_{timestamp}"
    
    # Generate JSON report
    json_path = os.path.join(output_dir, f"{base_filename}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Generate HTML report with dynamic content section
    html_report = generate_html_report(report)
    html_path = os.path.join(output_dir, f"{base_filename}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_report)
    
    # Export state tracking information
    state_tracking = export_dynamic_content_state_tracking(report.get('dynamic_content', {}))
    state_tracking_path = os.path.join(output_dir, f"{base_filename}_state_tracking.json")
    with open(state_tracking_path, 'w', encoding='utf-8') as f:
        json.dump(state_tracking, f, indent=2, ensure_ascii=False)

def generate_html_report(report):
    """
    Generate a comprehensive HTML report.
    
    Args:
        report (dict): Accessibility report
    
    Returns:
        str: HTML report content
    """
    # Basic HTML template with embedded styling
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Accessibility Report for {report.get('url', 'Unknown URL')}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; }}
            h1, h2 {{ color: #333; }}
            .summary {{ background: #f4f4f4; padding: 15px; margin-bottom: 20px; }}
            .score {{ 
                font-size: 2em; 
                font-weight: bold; 
                color: {'green' if report['summary']['accessibility_score'] >= 90 else 'orange' if report['summary']['accessibility_score'] >= 70 else 'red'}
            }}
            .check-section {{ margin-bottom: 20px; }}
            .issues-list {{ list-style-type: none; padding: 0; }}
            .issue {{ 
                margin-bottom: 10px; 
                padding: 10px; 
                border-left: 4px solid 
                {'red' if 'critical' in str(severity) else 'orange' if 'warning' in str(severity) else 'blue'}
            }}
        </style>
    </head>
    <body>
        <h1>Accessibility Report</h1>
        <div class="summary">
            <h2>Summary</h2>
            <p>URL: {report.get('url', 'N/A')}</p>
            <p>Timestamp: {report.get('timestamp', 'N/A')}</p>
            <p>Accessibility Score: <span class="score">{report['summary'].get('accessibility_score', 'N/A')}%</span></p>
            <p>Critical Issues: {report['summary'].get('critical_issues', 0)}</p>
            <p>Warnings: {report['summary'].get('warnings', 0)}</p>
            <p>Passed Checks: {report['summary'].get('passed_checks', 0)} / {report['summary'].get('total_checks', 0)}</p>
        </div>
    """
    
    # Add dynamic content section
    dynamic_content_section = generate_dynamic_content_report_section(
        report.get('dynamic_content', {}).get('detailed_results', {})
    )
    html += dynamic_content_section
    
    # Close HTML
    html += """
    </body>
    </html>
    """
    
    return html

def main():
    """
    Command-line interface for running accessibility checks.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Web Accessibility Checker")
    parser.add_argument("url", help="URL to check for accessibility")
    parser.add_argument("--browser", choices=['chrome', 'firefox', 'edge'], 
                        default='chrome', help="Browser to use for testing")
    parser.add_argument("--output", help="Directory to save reports")
    
    args = parser.parse_args()
    
    # Run comprehensive check
    report = run_comprehensive_accessibility_check(
        args.url, 
        browser=args.browser, 
        output_dir=args.output
    )
    
    # Print summary to console
    print("\n--- Accessibility Report Summary ---")
    print(f"URL: {report.get('url', 'N/A')}")
    print(f"Accessibility Score: {report['summary'].get('accessibility_score', 'N/A')}%")
    print(f"Critical Issues: {report['summary'].get('critical_issues', 0)}")
    print(f"Warnings: {report['summary'].get('warnings', 0)}")
    print(f"Passed Checks: {report['summary'].get('passed_checks', 0)} / {report['summary'].get('total_checks', 0)}")

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
- **Last Modified**: 2025-03-11 20:13:21
- **Size**: 17033 bytes

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

def is_archive_path(path):
    """
    Check if a path contains archive-related directories or is a checkpoint file.
    
    Args:
        path (Path): The path to check
    
    Returns:
        bool: True if path is in an archive or is a checkpoint, False otherwise
    """
    # Check for archive directories
    archive_keywords = ['archive', 'archived', 'backup', 'old']
    path_parts = str(path).lower().split(os.sep)
    is_archive = any(keyword in part for part in path_parts for keyword in archive_keywords)
    
    # Check for .ipynb_checkpoints directory
    is_checkpoint = '.ipynb_checkpoints' in str(path)
    
    # Check for checkpoint files (which end with -checkpoint.py)
    is_checkpoint_file = str(path).endswith('-checkpoint.py')
    
    return is_archive or is_checkpoint or is_checkpoint_file

def is_main_folder_file(base_path, file_path):
    """
    Check if a file is directly in the main folder (not in subdirectories).
    
    Args:
        base_path (Path): The base project path
        file_path (Path): The file path to check
    
    Returns:
        bool: True if file is in the main folder, False otherwise
    """
    return file_path.parent == base_path

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    # Use rglob to find files in the folder and all subfolders
    base_path = Path(folder_path)
    
    # Find all files but filter out those in archive directories
    all_files = [(f, f.suffix.lower()) for f in base_path.rglob('*') if f.is_file() and not is_archive_path(f)]
    
    # Filter files by type and location
    # Exclude .ipynb files
    notebook_files = []  # Empty list as we're no longer including notebook files
    python_files = [f for f, ext in all_files if ext == '.py']
    
    # Only include .txt files directly in the main folder (not in subdirectories)
    text_files = [f for f, ext in all_files if ext == '.txt' and is_main_folder_file(base_path, f)]
    
    # Only include .json files directly in the main folder (not in subdirectories)
    json_files = [f for f, ext in all_files if ext == '.json' and is_main_folder_file(base_path, f)]
    
    # Filter out .md files completely
    # No need to collect them since we're excluding them entirely
    
    # Find README files (README.md, README.txt, etc.)
    readme_files = []
    for pattern in ['README.md', 'README.txt', 'README', 'readme.md', 'readme.txt', 'readme']:
        readme_files.extend([f for f in base_path.rglob(pattern) if not is_archive_path(f)])
    
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
    
    # Removed Jupyter Notebooks TOC section since we're no longer including them
    
    # Add Python files to TOC
    if python_files:
        markdown_content += "\n### Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Text files to TOC (only main folder)
    if text_files:
        markdown_content += "\n### Text Files (Main Folder Only)\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add JSON files to TOC (only main folder)
    if json_files:
        markdown_content += "\n### JSON Files (Main Folder Only)\n"
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

    # Removed Jupyter Notebooks content section since we're no longer including them

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
    
    # Add Text file content (only main folder)
    if text_files:
        markdown_content += "\n## Text Files (Main Folder Only)\n"
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
    
    # Add JSON file content (only main folder)
    if json_files:
        markdown_content += "\n## JSON Files (Main Folder Only)\n"
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
### accessibility_modules\color_contrast.py <a id='accessibility_modules_color_contrast_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\color_contrast.py
- **Last Modified**: 2025-03-11 20:36:36
- **Size**: 12987 bytes

#### Code
```python
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
```
### accessibility_modules\dynamic_content_tester.py <a id='accessibility_modules_dynamic_content_tester_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\dynamic_content_tester.py
- **Last Modified**: 2025-03-17 23:39:54
- **Size**: 5304 bytes

#### Code
```python
"""
Dynamic Content Accessibility Tester
Coordinates specialized test modules for comprehensive testing of interactive web components.
"""
import logging
import time
import json
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        return json.dumps(export_data, indent=2)

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
        
        # Call the specialized test modules
        slider_results = test_sliders(driver, state_tracker, timeout)
        carousel_results = test_carousels(driver, state_tracker, timeout)
        modal_results = test_modals(driver, state_tracker, timeout)
        accordion_results = test_accordions(driver, state_tracker, timeout)
        dropdown_results = test_dropdowns(driver, state_tracker, timeout)
        tab_results = test_tabs(driver, state_tracker, timeout)
        
        # Initialize state_tracking as a dictionary, not a list
        results = {
            "sliders": slider_results,
            "carousels": carousel_results,
            "modals": modal_results,
            "accordions": accordion_results,
            "dropdowns": dropdown_results,
            "tabs": tab_results,
            "state_tracking": {
                "exported_states": state_tracker.export_states()
            }
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
```
### accessibility_modules\focusable_elements.py <a id='accessibility_modules_focusable_elements_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\focusable_elements.py
- **Last Modified**: 2025-03-17 19:06:14
- **Size**: 13286 bytes

#### Code
```python
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
- **Last Modified**: 2025-03-17 19:27:38
- **Size**: 30653 bytes

#### Code
```python
"""
Enhanced HTML Report Generator
Generates a clean and reliable HTML report with working accordions and detailed element information.
"""

import os
from datetime import datetime
from urllib.parse import urlparse
import logging

def generate_html_report(accessibility_report, output_dir=None):
    """
    Generate an enhanced HTML accessibility report with detailed element information
    using CSS-only accordions for maximum compatibility.
    
    Args:
        accessibility_report (dict): Dictionary containing accessibility check results
        output_dir (str, optional): Directory to save the report. Defaults to None.
        
    Returns:
        str: Path to the generated HTML report
    """
    logging.info("Generating enhanced HTML accessibility report...")
    
    # Set default output directory if not provided
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                'accessibility_reports')
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a filename based on URL and timestamp
    url = accessibility_report.get('url', 'unknown')
    # Fix URL for better filename compatibility
    if '\\' in url:
        # Convert backslashes to forward slashes
        url = url.replace('\\', '/')
    
    domain = urlparse(url).netloc
    if not domain:
        domain = 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Build HTML content using string parts to avoid syntax errors
    html_parts = []
    
    # Extract report data
    issues = accessibility_report.get('issues', [])
    
    # Group issues by check type for better organization
    issues_by_type = {}
    for issue in issues:
        check_type = issue.get('check_type', 'general')
        if check_type not in issues_by_type:
            issues_by_type[check_type] = []
        issues_by_type[check_type].append(issue)
    
    # Add HTML header and styles
    html_parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Accessibility Report - {url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f7f7f7;
        }}
        
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        
        .section {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
        }}
        
        .issue-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }}
        
        .issue-count {{
            background-color: #e74c3c;
            color: white;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 14px;
        }}
        
        .issue-count.no-issues {{
            background-color: #2ecc71;
        }}
        
        /* CSS-only accordion styling */
        .accordion {{
            margin-bottom: 10px;
        }}
        
        .accordion input[type="checkbox"] {{
            display: none;
        }}
        
        .accordion label {{
            background-color: #f8f9fa;
            color: #444;
            cursor: pointer;
            padding: 12px 15px;
            width: 100%;
            display: block;
            text-align: center;
            border: none;
            border-radius: 4px;
            outline: none;
            font-size: 16px;
            transition: 0.3s;
            margin-bottom: 5px;
            position: relative;
        }}
        
        .accordion label:hover {{
            background-color: #e9ecef;
        }}
        
        .accordion label::after {{
            content: '+';
            position: absolute;
            right: 15px;
            font-weight: bold;
        }}
        
        .accordion input:checked + label::after {{
            content: '-';
        }}
        
        .accordion-content {{
            background-color: #f9f9f9;
            border-radius: 0 0 4px 4px;
            overflow: hidden;
            padding: 0;
            max-height: 0;
            transition: max-height 0.3s ease-out;
        }}
        
        .accordion input:checked ~ .accordion-content {{
            max-height: 9999px; /* Large value to accommodate any content */
            padding: 18px;
        }}
        
        .issue-item {{
            margin-bottom: 20px;
            padding: 15px;
            border-left: 4px solid #e74c3c;
            background-color: white;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}
        
        .issue-title {{
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 16px;
        }}
        
        .issue-details {{
            margin-bottom: 10px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            color: #666;
            margin-bottom: 15px;
            padding-left: 10px;
            border-left: 2px solid #3498db;
        }}
        
        .critical {{
            color: #e74c3c;
        }}
        
        .warning {{
            color: #f39c12;
        }}
        
        /* CSS-only element info panel */
        .element-info-panel {{
            margin-top: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .element-info-panel input[type="checkbox"] {{
            display: none;
        }}
        
        .element-info-header {{
            background-color: #f1f1f1;
            padding: 8px 12px;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0;
        }}
        
        .element-info-header:hover {{
            background-color: #e5e5e5;
        }}
        
        .element-info-header::after {{
            content: '+';
            position: relative;
            font-weight: bold;
        }}
        
        .element-info-panel input:checked + .element-info-header::after {{
            content: '-';
        }}
        
        .element-info-content {{
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #fff;
        }}
        
        .element-info-panel input:checked ~ .element-info-content {{
            max-height: 2000px;
            padding: 12px;
        }}
        
        .element-property {{
            margin-bottom: 8px;
            display: flex;
            flex-wrap: wrap;
        }}
        
        .property-name {{
            font-weight: bold;
            min-width: 120px;
            color: #555;
        }}
        
        .property-value {{
            flex: 1;
            word-break: break-word;
            font-family: monospace;
            background-color: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        
        .selector-path {{
            font-family: monospace;
            background-color: #f5f5f5;
            padding: 8px;
            border-radius: 4px;
            margin-top: 5px;
            word-break: break-all;
            border: 1px solid #e0e0e0;
        }}
        
        .position-diagram {{
            width: 100%;
            max-width: 300px;
            height: 150px;
            margin: 10px 0;
            border: 1px solid #ddd;
            position: relative;
            background-color: #f9f9f9;
        }}
        
        .element-box {{
            position: absolute;
            background-color: rgba(52, 152, 219, 0.3);
            border: 2px solid rgba(52, 152, 219, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-family: monospace;
            color: #333;
        }}
        
        .attribute-list {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
        }}
        
        .attribute-list th, .attribute-list td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        
        .attribute-list th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        
        .attribute-list tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        .tags-list {{
            margin-top: 10px;
        }}
        
        .tags-list span {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .wcag-tag {{
            background-color: #9b59b6;
        }}
        
        .severity-tag {{
            background-color: #e74c3c;
        }}
        
        /* Dynamic content specific styles */
        .state-tag {{
            display: inline-block;
            background-color: #17a2b8;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .component-type-tag {{
            display: inline-block;
            background-color: #6f42c1;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .component-container {{
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-top: 15px;
            background-color: #f8f9fa;
        }}
        
        .component-header {{
            font-weight: bold;
            margin-bottom: 10px;
            padding-bottom: 5px;
            border-bottom: 1px solid #eee;
        }}
        
        /* Verification buttons */
        .verification-section {{
            display: flex;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #eee;
            justify-content: flex-start;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .verification-button {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            text-align: center;
            transition: all 0.3s ease;
            border: 2px solid;
            min-width: 120px;
            position: relative;
        }}
        
        .verify-button {{
            background-color: #f0f8ff;
            color: #0077cc;
            border-color: #0077cc;
        }}
        
        .verify-button:hover {{
            background-color: #e0f0ff;
        }}
        
        .verify-button.active {{
            background-color: #0077cc;
            color: white;
        }}
        
        .verify-button.active::before {{
            content: "✓ ";
        }}
        
        .fix-button {{
            background-color: #f0fff0;
            color: #2e8b57;
            border-color: #2e8b57;
        }}
        
        .fix-button:hover {{
            background-color: #e0ffe0;
        }}
        
        .fix-button.active {{
            background-color: #2e8b57;
            color: white;
        }}
        
        .fix-button.active::before {{
            content: "✓ ";
        }}
        
        /* Export button */
        .export-btn {{
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        
        .export-btn:hover {{
            background-color: #2980b9;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            margin-top: 20px;
            color: #666;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="section">
        <h1>Enhanced Accessibility Audit Report</h1>
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><strong>Elements Analyzed:</strong> {accessibility_report.get('summary', {}).get('elements_checked', 'Unknown')}</p>
    </div>
""")
    
    # Add section for each issue type
    section_counter = 0
    for check_type, issues_list in issues_by_type.items():
        # Create user-friendly name from check_type
        check_name = check_type.replace('_', ' ').title()
        
        # Common conversions for clarity
        if check_type == 'keyboard_navigation_sequence':
            check_name = 'Keyboard Navigation Sequence'
        elif check_type == 'aria_accessibility':
            check_name = 'ARIA Accessibility'
        elif check_type == 'dynamic_content':
            check_name = 'Dynamic Content'
        
        section_counter += 1
        accordion_id = f"accordion-{section_counter}"
        
        html_parts.append(f"""
    <div class="section">
        <div class="issue-header">
            <h2>{check_name}</h2>
            <span class="issue-count {'no-issues' if not issues_list else ''}">
                {len(issues_list)} {'Issue' if len(issues_list) == 1 else 'Issues'}
            </span>
        </div>
        
        <div class="accordion">
            <input type="checkbox" id="{accordion_id}" class="accordion-checkbox">
            <label for="{accordion_id}">View Issues</label>
            <div class="accordion-content">
""")
        
        if issues_list:
            html_parts.append("""
            <div class="issues-list">
""")
            
            for i, issue in enumerate(issues_list):
                title = issue.get('issue', 'Unknown Issue')
                details = issue.get('details', '')
                recommendation = issue.get('recommendation', '')
                severity = issue.get('severity', 'warning')
                wcag = issue.get('wcag', '')
                
                # Use preferred terminology
                if "inconsistent keyboard navigation sequence" in title.lower():
                    title = "Inconsistent keyboard navigation sequence"
                elif "keyboard navigation barrier" in title.lower():
                    title = "Keyboard navigation barrier"
                
                issue_id = f"issue-{section_counter}-{i}"
                
                html_parts.append(f"""
                <div class="issue-item" id="{issue_id}">
                    <div class="issue-title {severity}">{title}</div>
                    <div class="issue-details">{details}</div>
                    <div class="issue-recommendation">{recommendation}</div>
                    <div class="tags-list">
                        {f'<span class="wcag-tag">WCAG {wcag}</span>' if wcag else ''}
                        <span class="severity-tag">{severity.title()}</span>
                    </div>
""")

                # Add special information for dynamic content issues
                if issue.get("check_type") == "dynamic_content":
                    state_info = issue.get("state_info", "")
                    component_type = issue.get("component_type", "")
                    component_id = issue.get("component_id", "")
                    
                    if state_info or component_type:
                        html_parts.append(f"""
                        <div class="component-container">
                            <div class="component-header">
                                {f'<span class="component-type-tag">{component_type.title()}</span>' if component_type else ''}
                                {f'<span class="state-tag">{state_info}</span>' if state_info else ''}
                            </div>
                            <div class="component-details">
                                <p>This issue was detected in a dynamic component that may change state during user interaction.</p>
                                {f'<p><strong>Component ID:</strong> {component_id}</p>' if component_id else ''}
                            </div>
                        </div>
""")
                
                # Add detailed element information section
                element_info = issue.get('element_info', {})
                if element_info:
                    element_id = f"element-info-{section_counter}-{i}"
                    
                    # Get the main element properties
                    tag = element_info.get('tag', 'unknown')
                    element_id_value = element_info.get('id', '')
                    element_class = element_info.get('class', '')
                    element_src = element_info.get('src', '')
                    dom_path = element_info.get('dom_path', '')
                    css_selector = element_info.get('css_selector', '')
                    position = element_info.get('position', {})
                    attributes = element_info.get('attributes', {})
                    
                    html_parts.append(f"""
                    <div class="element-info-panel">
                        <input type="checkbox" id="{element_id}" class="element-info-checkbox">
                        <label class="element-info-header" for="{element_id}">
                            Element Details: &lt;{tag}&gt;{f' #{element_id_value}' if element_id_value else ''}
                        </label>
                        <div class="element-info-content">
                            <!-- Basic Element Info -->
                            <div class="element-property">
                                <div class="property-name">Element Type:</div>
                                <div class="property-value">&lt;{tag}&gt;</div>
                            </div>
""")
                    
                    # Add ID if available
                    if element_id_value:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Element ID:</div>
                                <div class="property-value">{element_id_value}</div>
                            </div>
""")
                    
                    # Add Class if available
                    if element_class:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">CSS Classes:</div>
                                <div class="property-value">{element_class}</div>
                            </div>
""")
                    
                    # Add Source if available (for images, scripts, etc.)
                    if element_src:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Source:</div>
                                <div class="property-value">{element_src}</div>
                            </div>
""")
                    
                    # Add DOM path if available
                    if dom_path:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">DOM Path:</div>
                                <div class="property-value">{dom_path}</div>
                            </div>
""")
                    
                    # Add CSS Selector if available
                    if css_selector:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">CSS Selector:</div>
                                <div class="selector-path">{css_selector}</div>
                            </div>
""")
                    
                    # Add Position information if available
                    if position:
                        # Calculate scaled position for the visual representation
                        container_width = 300
                        container_height = 150
                        
                        # Default values in case properties are missing
                        x = position.get('x', 0)
                        y = position.get('y', 0)
                        width = position.get('width', 100)
                        height = position.get('height', 50)
                        
                        # Handle edge case where dimensions or position might be invalid
                        if width <= 0: width = 100
                        if height <= 0: height = 50
                        
                        # Scale factor (max 10x reduction to fit within diagram)
                        scale_factor_x = min(1, container_width / (width * 3))
                        scale_factor_y = min(1, container_height / (height * 3))
                        scale_factor = min(scale_factor_x, scale_factor_y, 0.1)  # Max 10x reduction
                        
                        # Calculate scaled dimensions
                        scaled_width = max(10, width * scale_factor)  # Minimum 10px width
                        scaled_height = max(10, height * scale_factor)  # Minimum 10px height
                        
                        # Center the element in the container
                        scaled_x = (container_width - scaled_width) / 2
                        scaled_y = (container_height - scaled_height) / 2
                        
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Position:</div>
                                <div class="property-value">
                                    x: {x}px, y: {y}px, width: {width}px, height: {height}px
                                </div>
                            </div>
                            
                            <!-- Visual position diagram -->
                            <div class="position-diagram">
                                <div class="element-box" style="
                                    left: {scaled_x}px;
                                    top: {scaled_y}px;
                                    width: {scaled_width}px;
                                    height: {scaled_height}px;
                                ">
                                    &lt;{tag}&gt;
                                </div>
                            </div>
""")
                    
                    # Add Attributes table if available
                    if attributes:
                        html_parts.append("""
                            <div class="element-property">
                                <div class="property-name">Attributes:</div>
                                <div class="property-value">
                                    <table class="attribute-list">
                                        <tr>
                                            <th>Name</th>
                                            <th>Value</th>
                                        </tr>
""")
                        
                        # Add each attribute
                        for attr_name, attr_value in attributes.items():
                            # Skip attributes already shown above
                            if attr_name in ['id', 'class', 'src']:
                                continue
                                
                            html_parts.append(f"""
                                        <tr>
                                            <td>{attr_name}</td>
                                            <td>{attr_value}</td>
                                        </tr>
""")
                            
                        html_parts.append("""
                                    </table>
                                </div>
                            </div>
""")
                    
                    # Close the element info panel
                    html_parts.append("""
                        </div>
                    </div>
""")
                
                # Add verification buttons
                html_parts.append(f"""
                    <div class="verification-section">
                        <div class="verification-button verify-button" 
                             onclick="toggleVerificationStatus(this, '{issue_id}', 'verified')">VERIFY</div>
                        <div class="verification-button fix-button" 
                             onclick="toggleVerificationStatus(this, '{issue_id}', 'fixed')">MARK FIXED</div>
                    </div>
                </div>
""")
            
            html_parts.append("""
            </div>
""")
        else:
            html_parts.append("""
            <p>No issues detected for this check.</p>
""")
        
        # Close the accordion content and section
        html_parts.append("""
            </div>
        </div>
    </div>
""")
    
    # Add footer and CSV export script (only JavaScript remaining)
    html_parts.append(f"""
    <div class="section">
        <h2>Export Options</h2>
        <button class="export-btn" onclick="exportToCsv()">Export Issues to CSV</button>
    </div>
    
    <footer>
        <p>Generated by Accessibility Checker on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </footer>
    
    <script>
        // Toggle verification status with more obvious visual feedback
        function toggleVerificationStatus(button, issueId, status) {{
            // Toggle active class
            button.classList.toggle('active');
            
            // If it's a fixed button, also activate the verify button if it's active
            if (status === 'fixed' && button.classList.contains('active')) {{
                // Find the verify button in the same verification section
                var verifyBtn = button.parentElement.querySelector('.verify-button');
                if (verifyBtn) {{
                    verifyBtn.classList.add('active');
                }}
            }}
        }}
        
        // CSV Export Function - only JavaScript needed
        function exportToCsv() {{
            // Collect all issues
            var issues = [];
            var issueItems = document.querySelectorAll('.issue-item');
            
            issueItems.forEach(function(item) {{
                var checkType = item.closest('.section').querySelector('h2').textContent;
                var title = item.querySelector('.issue-title').textContent;
                var details = item.querySelector('.issue-details').textContent;
                var recommendation = item.querySelector('.issue-recommendation').textContent;
                var verified = item.querySelector('.verify-button').classList.contains('active') ? 'Yes' : 'No';
                var fixed = item.querySelector('.fix-button').classList.contains('active') ? 'Yes' : 'No';
                
                // Get dynamic content info if present
                var componentInfo = '';
                var componentContainer = item.querySelector('.component-container');
                if (componentContainer) {{
                    var componentType = componentContainer.querySelector('.component-type-tag');
                    var stateInfo = componentContainer.querySelector('.state-tag');
                    
                    if (componentType) {{
                        componentInfo += componentType.textContent + ' ';
                    }}
                    
                    if (stateInfo) {{
                        componentInfo += stateInfo.textContent;
                    }}
                }}
                
                issues.push([
                    checkType,
                    title,
                    details,
                    recommendation,
                    componentInfo ? componentInfo : 'N/A',
                    verified,
                    fixed
                ]);
            }});
            
            // Create CSV content
            var csvContent = "Check Type,Issue,Details,Recommendation,Component Info,Verified,Fixed\\n";
            
            issues.forEach(function(issue) {{
                // Properly escape CSV fields
                var formattedIssue = issue.map(function(field) {{
                    // Escape quotes and wrap in quotes if contains comma
                    var escaped = String(field).replace(/"/g, '""');
                    if (escaped.includes(',')) {{
                        escaped = '"' + escaped + '"';
                    }}
                    return escaped;
                }});
                
                csvContent += formattedIssue.join(',') + "\\n";
            }});
            
            // Create download link
            var encodedUri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvContent);
            var link = document.createElement('a');
            link.setAttribute('href', encodedUri);
            link.setAttribute('download', 'accessibility_issues_{timestamp}.csv');
            
            // Trigger download
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}
    </script>
</body>
</html>
""")
    
    # Join all HTML parts into a single string
    html_content = ''.join(html_parts)
    
    # Write HTML to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logging.info(f"Enhanced HTML report saved to: {filepath}")
    return filepath
```
### accessibility_modules\image_checker.py <a id='accessibility_modules_image_checker_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\image_checker.py
- **Last Modified**: 2025-03-17 17:42:36
- **Size**: 20323 bytes

#### Code
```python
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
```
### accessibility_modules\report_generator.py <a id='accessibility_modules_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\report_generator.py
- **Last Modified**: 2025-03-17 23:40:42
- **Size**: 8086 bytes

#### Code
```python
"""
Enhanced Accessibility Report Generator

Incorporates advanced dynamic content testing results into comprehensive reports.
"""

import json
import logging
from datetime import datetime

def integrate_dynamic_content_results(report, dynamic_content_results):
    """
    Integrate dynamic content testing results into the main accessibility report.
    
    Args:
        report: Main accessibility report dictionary
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        Updated report with dynamic content insights
    """
    # Ensure dynamic content section exists
    report['dynamic_content'] = {
        'summary': {
            'total_components_tested': 0,
            'components_with_issues': 0,
            'issue_types': {}
        },
        'detailed_results': dynamic_content_results
    }
    
    # Analyze and summarize issues
    for component_type, component_results in dynamic_content_results.items():
        if component_type == 'state_tracking':
            continue  # Skip state tracking export
            
        # Make sure component_results is a list
        if not isinstance(component_results, list):
            logging.warning(f"Expected list for {component_type} results, got {type(component_results)}")
            continue
        
        # Count components and issues
        issues_for_type = [issue for issue in component_results if isinstance(issue, dict)]
        
        # Update summary
        report['dynamic_content']['summary']['total_components_tested'] += len(component_results)
        
        if issues_for_type:
            report['dynamic_content']['summary']['components_with_issues'] += len(issues_for_type)
            
            # Categorize issue types
            for issue in issues_for_type:
                issue_type = issue.get('type', 'unknown')
                if issue_type not in report['dynamic_content']['summary']['issue_types']:
                    report['dynamic_content']['summary']['issue_types'][issue_type] = 0
                report['dynamic_content']['summary']['issue_types'][issue_type] += 1
    
    # Calculate overall dynamic content accessibility score
    total_components = report['dynamic_content']['summary']['total_components_tested']
    components_with_issues = report['dynamic_content']['summary']['components_with_issues']
    
    if total_components > 0:
        dynamic_content_score = max(0, 100 - (components_with_issues / total_components * 100))
        report['dynamic_content']['summary']['accessibility_score'] = round(dynamic_content_score, 2)
    else:
        report['dynamic_content']['summary']['accessibility_score'] = 100
    
    return report

def generate_dynamic_content_report_section(dynamic_content_results):
    """
    Generate a detailed HTML section for dynamic content testing results.
    
    Args:
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        HTML string with detailed dynamic content testing report
    """
    html = """
    <div class="dynamic-content-section">
        <h2>Dynamic Content Accessibility Analysis</h2>
    """
    
    # Check if dynamic_content_results is a dictionary
    if not isinstance(dynamic_content_results, dict):
        html += "<p>No dynamic content results available.</p>"
        html += "</div>"
        return html
    
    # Iterate through component types
    for component_type, component_results in dynamic_content_results.items():
        if component_type == 'state_tracking' or component_type == 'error':
            continue  # Skip state tracking export and error info
        
        html += f"""
        <div class="component-type-section">
            <h3>{component_type.capitalize()} Accessibility</h3>
        """
        
        # Ensure component_results is a list
        if not isinstance(component_results, list):
            html += "<p>No data available for this component type.</p>"
            html += "</div>"
            continue
        
        # Filter and process issues
        issues = [issue for issue in component_results if isinstance(issue, dict)]
        
        if not issues:
            html += "<p>No accessibility issues detected for this component type.</p>"
        else:
            html += """
            <table class="issues-table">
                <thead>
                    <tr>
                        <th>Issue Type</th>
                        <th>Details</th>
                        <th>Severity</th>
                    </tr>
                </thead>
                <tbody>
            """
            
            for issue in issues:
                html += f"""
                    <tr>
                        <td>{issue.get('type', 'Unknown')}</td>
                        <td>{issue.get('details', 'No additional details')}</td>
                        <td>{issue.get('severity', 'Warning')}</td>
                    </tr>
                """
            
            html += """
                </tbody>
            </table>
            """
        
        html += "</div>"
    
    html += "</div>"
    
    return html

def export_dynamic_content_state_tracking(dynamic_content_results):
    """
    Export detailed state tracking information.
    
    Args:
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        Formatted state tracking export
    """
    # Make sure we're working with a dictionary
    if not isinstance(dynamic_content_results, dict):
        logging.error("dynamic_content_results is not a dictionary")
        return {"error": "Invalid data format"}
    
    # Access state_tracking safely
    state_tracking = dynamic_content_results.get('state_tracking', {})
    
    # Make sure state_tracking is a dictionary
    if not isinstance(state_tracking, dict):
        logging.error(f"state_tracking is not a dictionary, it's a {type(state_tracking)}")
        return {"error": "Invalid state tracking format"}
    
    try:
        # Parse the exported states
        exported_states_str = state_tracking.get('exported_states', '{}')
        exported_states = json.loads(exported_states_str)
        
        # Generate a more readable format
        formatted_export = {
            'timestamp': datetime.now().isoformat(),
            'component_states': {}
        }
        
        if isinstance(exported_states, dict) and 'component_states' in exported_states:
            for component_type, components in exported_states.get('component_states', {}).items():
                formatted_export['component_states'][component_type] = {}
                
                for component_id, state_info in components.items():
                    # Handle both list and dictionary formats for state_info
                    if isinstance(state_info, list) and state_info:
                        # Take the last state if it's a list
                        last_state = state_info[-1]
                        formatted_export['component_states'][component_type][component_id] = {
                            'timestamp': last_state.get('timestamp', ''),
                            'state': last_state.get('state', {})
                        }
                    elif isinstance(state_info, dict):
                        formatted_export['component_states'][component_type][component_id] = {
                            'timestamp': state_info.get('timestamp', ''),
                            'state': state_info.get('state', {})
                        }
        
        return formatted_export
    
    except json.JSONDecodeError:
        logging.error("Failed to parse state tracking export")
        return {
            'error': 'Failed to parse state tracking export',
            'raw_data': state_tracking.get('exported_states', '')
        }
    except Exception as e:
        logging.error(f"Error processing state tracking: {str(e)}")
        return {
            'error': f'Error processing state tracking: {str(e)}',
            'raw_data': str(state_tracking)
        }
```
### accessibility_modules\simple_html_report_generator.py <a id='accessibility_modules_simple_html_report_generator_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\simple_html_report_generator.py
- **Last Modified**: 2025-03-11 20:30:22
- **Size**: 8869 bytes

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
        
        /* Content div style */
        .content {{
            padding: 0 18px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #f9f9f9;
            border-radius: 0 0 5px 5px;
            margin-top: 5px;
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
        if check_type == 'keyboard_navigation_sequence':
            check_name = 'Keyboard Navigation Sequence'
        elif check_type == 'aria_accessibility':
            check_name = 'ARIA Accessibility'
        elif check_type == 'color_contrast':
            check_name = 'Color Contrast'
        
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
                
                # Use preferred terminology
                if "inconsistent keyboard navigation sequence" in title.lower():
                    title = "Inconsistent keyboard navigation sequence"
                elif "keyboard navigation barrier" in title.lower():
                    title = "Keyboard navigation barrier"
                elif "insufficient color contrast" in title.lower():
                    title = "Insufficient color contrast"
                
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
- **Last Modified**: 2025-03-17 20:35:21
- **Size**: 26942 bytes

#### Code
```python
"""
Tab Order Checker Module
Checks the tab order of focusable elements to ensure they follow a logical sequence.
Enhanced with advanced focus order detection.
"""

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_tab_order(driver):
    """
    Checks the tab order of focusable elements on a webpage with improved detection.
    
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
        # Enhanced selector for potentially focusable elements
        # This better matches what browsers consider focusable
        focusable_selector = (
            "a[href]:not([tabindex='-1']), button:not([tabindex='-1']):not([disabled]), " +
            "input:not([type='hidden']):not([tabindex='-1']):not([disabled]), select:not([tabindex='-1']):not([disabled]), " +
            "textarea:not([tabindex='-1']):not([disabled]), [tabindex]:not([tabindex='-1']), [contenteditable='true']:not([tabindex='-1']), " +
            "details:not([tabindex='-1']), summary:not([tabindex='-1']), [role='button']:not([tabindex='-1']), " +
            "[role='link']:not([tabindex='-1']), [role='checkbox']:not([tabindex='-1']), [role='radio']:not([tabindex='-1']), " +
            "[role='tab']:not([tabindex='-1']), [role='menuitem']:not([tabindex='-1']), [role='combobox']:not([tabindex='-1']), " +
            "[role='listbox']:not([tabindex='-1']), [role='slider']:not([tabindex='-1']), [role='switch']:not([tabindex='-1']), " +
            "[role='textbox']:not([tabindex='-1']), [role='searchbox']:not([tabindex='-1']), [role='spinbutton']:not([tabindex='-1'])"
        )
        
        # Get all focusable elements and filter for visible ones
        logging.info("Finding potentially focusable elements...")
        all_focusable = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
        
        # Filter visible and enabled elements to get a more accurate count
        visible_focusable = []
        for element in all_focusable:
            try:
                if element.is_displayed() and element.is_enabled():
                    visible_focusable.append(element)
            except StaleElementReferenceException:
                continue
        
        logging.info(f"Found {len(all_focusable)} potentially focusable elements, {len(visible_focusable)} visible and enabled")
        tab_order_results["potentially_focusable_count"] = len(visible_focusable)
        
        # Attempt to follow tab sequence using multiple approaches
        tab_sequence = detect_tab_sequence_robustly(driver, visible_focusable)
        tab_order_results["tab_sequence"] = tab_sequence
        
        # Analyze the tab order for issues
        analyze_tab_order(tab_order_results)
        
        return tab_order_results
        
    except WebDriverException as e:
        logging.error(f"Error checking tab order: {str(e)}")
        tab_order_results["error"] = str(e)
        return tab_order_results

def detect_tab_sequence_robustly(driver, visible_focusable):
    """Enhanced tab sequence detection with multiple fallback strategies"""
    try:
        # First attempt: Traditional method with direct tabbing
        tab_sequence = attempt_direct_tab_sequence(driver, len(visible_focusable))
        
        # If we didn't get many elements, try alternative approach
        if len(tab_sequence) < min(10, len(visible_focusable) / 5):
            logging.info(f"Direct tabbing only found {len(tab_sequence)} elements. Trying JavaScript approach...")
            tab_sequence = attempt_javascript_tab_sequence(driver, visible_focusable)
        
        # If still not enough elements, try a hybrid approach
        if len(tab_sequence) < min(10, len(visible_focusable) / 5):
            logging.info(f"JavaScript approach only found {len(tab_sequence)} elements. Trying hybrid approach...")
            tab_sequence = attempt_hybrid_tab_sequence(driver, visible_focusable)
        
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in robust tab sequence detection: {str(e)}")
        # Return whatever we have so far
        return tab_sequence if 'tab_sequence' in locals() else []

def attempt_direct_tab_sequence(driver, max_elements):
    """Attempt to detect tab sequence by directly sending Tab keys"""
    tab_sequence = []
    focused_signatures = set()
    
    # Reset to beginning of document
    try:
        driver.execute_script("document.activeElement.blur();")
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()
    except Exception as e:
        logging.warning(f"Couldn't reset focus: {str(e)}")
    
    # Use a longer timeout for slow-loading pages
    timeout = 10  # seconds
    start_time = time.time()
    
    # First press Tab to start
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        time.sleep(0.5)  # Give the page time to update focus
    except Exception as e:
        logging.warning(f"Couldn't send initial tab: {str(e)}")
    
    # Loop through elements with tab
    for i in range(min(max_elements, 100)):  # Limit to avoid infinite loops
        if time.time() - start_time > timeout:
            logging.warning("Timeout reached while detecting tab sequence")
            break
            
        try:
            # Get current active element
            active_element = driver.execute_script("return document.activeElement;")
            
            # Generate a signature to detect cycles
            element_signature = generate_element_signature(active_element)
            
            # Skip if we've seen this element (avoid infinite loops)
            if element_signature in focused_signatures:
                # If we're back at the first element, we've completed a cycle
                if len(tab_sequence) > 1 and element_signature == generate_element_signature(tab_sequence[0]["element"]):
                    logging.info("Detected full tab cycle - stopping")
                    break
                else:
                    # Allow some duplicates (some widgets cycle through their own elements)
                    duplicate_count = sum(1 for sig in focused_signatures if sig == element_signature)
                    if duplicate_count > 2:
                        logging.info(f"Detected too many duplicates of {element_signature} - stopping")
                        break
            
            # Add to tab sequence
            element_info = get_element_info(active_element)
            element_info["signature"] = element_signature
            element_info["tab_index"] = i + 1
            tab_sequence.append(element_info)
            focused_signatures.add(element_signature)
            
            # Send Tab to go to next element
            active_element.send_keys(Keys.TAB)
            time.sleep(0.2)  # Small delay to allow focus to move
            
        except Exception as e:
            logging.warning(f"Error in tab sequence at step {i+1}: {str(e)}")
            break
    
    logging.info(f"Direct tabbing detected {len(tab_sequence)} elements")
    return tab_sequence

def attempt_javascript_tab_sequence(driver, visible_focusable):
    """Use JavaScript to analyze and determine the tab sequence"""
    tab_sequence = []
    
    try:
        # Use JavaScript to get elements sorted by tabindex
        sorted_elements = driver.execute_script("""
            // Get all focusable elements
            var elements = Array.from(arguments[0]);
            
            // Sort them by tabindex
            elements.sort(function(a, b) {
                var aTabIndex = parseInt(a.getAttribute('tabindex'));
                var bTabIndex = parseInt(b.getAttribute('tabindex'));
                
                // Elements with positive tabindex come first (in numerical order)
                if (!isNaN(aTabIndex) && aTabIndex > 0 && (!isNaN(bTabIndex) && bTabIndex > 0)) {
                    return aTabIndex - bTabIndex;
                }
                
                // Elements with positive tabindex come before elements with tabindex="0" or no tabindex
                if (!isNaN(aTabIndex) && aTabIndex > 0) {
                    return -1;
                }
                if (!isNaN(bTabIndex) && bTabIndex > 0) {
                    return 1;
                }
                
                // Otherwise, use DOM order
                return 0;
            });
            
            return elements;
        """, visible_focusable)
        
        # Convert to tab sequence format
        for i, element in enumerate(sorted_elements):
            element_info = get_element_info(element)
            element_info["signature"] = generate_element_signature(element)
            element_info["tab_index"] = i + 1
            tab_sequence.append(element_info)
        
        logging.info(f"JavaScript approach detected {len(tab_sequence)} elements")
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in JavaScript tab sequence: {str(e)}")
        return []

def attempt_hybrid_tab_sequence(driver, visible_focusable):
    """Combine direct interaction and estimation to determine tab sequence"""
    tab_sequence = []
    
    try:
        # Sample a subset of elements to test direct focus
        sample_size = min(20, len(visible_focusable))
        sample = visible_focusable[:sample_size]
        
        for i, element in enumerate(sample):
            try:
                # Try to focus the element directly
                driver.execute_script("arguments[0].focus();", element)
                time.sleep(0.1)
                
                # Check if it actually received focus
                active_element = driver.execute_script("return document.activeElement;")
                
                # If it did, add it to our sequence
                if active_element == element:
                    element_info = get_element_info(element)
                    element_info["signature"] = generate_element_signature(element)
                    element_info["tab_index"] = i + 1
                    element_info["verified_focusable"] = True
                    tab_sequence.append(element_info)
            except Exception:
                continue
        
        # If we found some focusable elements, extrapolate to the rest
        if tab_sequence:
            # Estimate how many elements are likely focusable based on our sample
            focusable_ratio = len(tab_sequence) / sample_size
            estimated_total = int(len(visible_focusable) * focusable_ratio)
            
            logging.info(f"Hybrid approach found {len(tab_sequence)} focusable elements in sample")
            logging.info(f"Estimated total focusable elements: {estimated_total}")
            
            # Add remaining visible elements with a note that they're estimated
            remaining = visible_focusable[sample_size:]
            for i, element in enumerate(remaining[:50]):  # Limit to 50 more elements
                element_info = get_element_info(element)
                element_info["signature"] = generate_element_signature(element)
                element_info["tab_index"] = len(tab_sequence) + i + 1
                element_info["estimated_focusable"] = True
                tab_sequence.append(element_info)
        
        return tab_sequence
    except Exception as e:
        logging.error(f"Error in hybrid tab sequence: {str(e)}")
        return tab_sequence if tab_sequence else []

def get_element_info(element):
    """Extract useful information about an element"""
    try:
        tag_name = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_text = element.text.strip() if hasattr(element, 'text') else ""
        
        info = {
            "element": element,
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
        
        # Handle element without text
        if info["text"] == "[No text]":
            # Try to get inner image alt text
            try:
                img = element.find_element(By.TAG_NAME, "img")
                alt = img.get_attribute("alt")
                if alt:
                    info["text"] = f"[Image: {alt}]"
            except:
                pass
                    
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

def generate_element_signature(element):
    """Generate a unique-ish signature for an element to detect duplicates in tab order"""
    try:
        tag = element.tag_name if hasattr(element, 'tag_name') else element.get_attribute("tagName").lower()
        element_id = element.get_attribute("id") or ""
        classes = element.get_attribute("class") or ""
        href = element.get_attribute("href") or ""
        src = element.get_attribute("src") or ""
        
        # Create a more distinctive signature
        signature_parts = [tag]
        if element_id:
            signature_parts.append(f"id={element_id}")
        if classes:
            signature_parts.append(f"class={classes}")
        if href:
            # Just include hostname from href to avoid long URLs
            try:
                from urllib.parse import urlparse
                hostname = urlparse(href).hostname or ""
                signature_parts.append(f"href={hostname}")
            except:
                signature_parts.append("href=...")
        if src:
            # Just include filename from src
            try:
                src_parts = src.split('/')
                signature_parts.append(f"src={src_parts[-1]}")
            except:
                signature_parts.append("src=...")
        
        return ":".join(signature_parts)
    except:
        return "unknown"

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
    potential_count = results.get("potentially_focusable_count", 0)
    if potential_count > 0 and len(tab_sequence) < potential_count / 3:  # If less than 1/3 are actually focusable
        issues.append({
            "type": "warning",
            "issue": "Keyboard navigation barrier",
            "details": f"Tab sequence ({len(tab_sequence)} elements) is much shorter than expected ({potential_count} potentially focusable elements)",
            "recommendation": "Check for elements that should be focusable but aren't",
            "wcag": "2.1.1",
            "notes": "Manual verification recommended - automated detection found fewer focusable elements than expected"
        })
    
    # Add advanced focus order analysis
    advanced_issues = check_visual_reading_order(tab_sequence)
    issues.extend(advanced_issues)
    
    # Add form field sequence analysis
    form_issues = check_form_field_sequence(tab_sequence)
    issues.extend(form_issues)
    
    results["issues"] = issues

def check_visual_reading_order(tab_sequence):
    """
    Identify cases where tab order doesn't follow visual reading order (top-to-bottom, left-to-right).
    Uses a more sophisticated approach to detect reading order violations.
    """
    issues = []
    
    # Get elements with position info
    elements_with_position = [e for e in tab_sequence if e.get("position")]
    
    # Skip if we don't have enough elements with position
    if len(elements_with_position) < 3:
        return issues
    
    # Define reading direction thresholds
    # These define how much movement in a direction is significant
    VERTICAL_THRESHOLD = 30  # px - Significant vertical movement
    HORIZONTAL_THRESHOLD = 50  # px - Significant horizontal movement
    
    # Track the current "reading line"
    current_reading_y = elements_with_position[0]["position"]["y"]
    last_line_x_boundary = 0
    
    # Analyze the sequence
    for i in range(1, len(elements_with_position)):
        prev = elements_with_position[i-1]
        current = elements_with_position[i]
        
        prev_pos = prev["position"]
        current_pos = current["position"]
        
        # Calculate position changes
        y_change = current_pos["y"] - prev_pos["y"]
        x_change = current_pos["x"] - prev_pos["x"]
        
        # Check if we're moving to a new reading line
        if abs(y_change) > VERTICAL_THRESHOLD:
            if y_change < 0:
                # Moving up - might be okay if it's a new column
                # Check if the horizontal position is significantly different
                if abs(current_pos["x"] - prev_pos["x"]) < HORIZONTAL_THRESHOLD:
                    # Not far enough horizontally to be a new column, likely an issue
                    issues.append({
                        "type": "warning",
                        "tab_index": current.get("tab_index"),
                        "element": f"{current.get('tag')} {current.get('text', '')}",
                        "prev_element": f"{prev.get('tag')} {prev.get('text', '')}",
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Tab order moves upward against the expected reading order",
                        "recommendation": "Ensure tab order follows the logical reading order of the content",
                        "wcag": "2.4.3"
                    })
            
            # Update the current reading line
            current_reading_y = current_pos["y"]
            last_line_x_boundary = prev_pos["x"] + prev_pos["width"]
        else:
            # Within the same reading line, check if we're going backward
            if x_change < -HORIZONTAL_THRESHOLD:
                # Moving significantly left on the same visual line
                # This might be okay if we're at the start of a new line that's very close to the previous
                if not (abs(y_change) > 10):  # Small vertical change
                    issues.append({
                        "type": "warning",
                        "tab_index": current.get("tab_index"),
                        "element": f"{current.get('tag')} {current.get('text', '')}",
                        "prev_element": f"{prev.get('tag')} {prev.get('text', '')}",
                        "issue": "Inconsistent keyboard navigation sequence",
                        "details": "Tab order moves backward (right to left) on the same line",
                        "recommendation": "Ensure tab order follows left-to-right reading direction within lines",
                        "wcag": "2.4.3"
                    })
    
    return issues

def check_form_field_sequence(tab_sequence):
    """
    Check if form fields follow a logical sequence.
    Focuses on identifying common form patterns and ensuring they follow expected tab order.
    """
    issues = []
    
    # Identify form fields
    form_fields = []
    for i, element in enumerate(tab_sequence):
        tag = element.get("tag", "").lower()
        role = element.get("role", "")
        
        if tag in ["input", "select", "textarea", "button"] or role in ["textbox", "combobox", "checkbox", "radio"]:
            form_fields.append((i, element))
    
    # Skip if not enough form fields
    if len(form_fields) < 2:
        return issues
    
    # Group form fields that appear to be part of the same form or section
    form_groups = []
    current_group = [form_fields[0]]
    
    for i in range(1, len(form_fields)):
        prev_idx, prev_field = form_fields[i-1]
        curr_idx, curr_field = form_fields[i]
        
        # Check if these are likely in the same form
        # If more than 3 other elements between them, likely different forms
        if curr_idx - prev_idx <= 3:
            current_group.append((curr_idx, curr_field))
        else:
            # Start a new group if we have enough fields
            if len(current_group) > 1:
                form_groups.append(current_group)
            current_group = [(curr_idx, curr_field)]
    
    # Add the last group if it exists
    if len(current_group) > 1:
        form_groups.append(current_group)
    
    # Check each group of form fields
    for group in form_groups:
        # Check if fields are in a logical order
        for i in range(1, len(group)):
            prev_idx, prev_field = group[i-1]
            curr_idx, curr_field = group[i]
            
            # Skip if no position info
            if not prev_field.get("position") or not curr_field.get("position"):
                continue
            
            prev_pos = prev_field["position"]
            curr_pos = curr_field["position"]
            
            # Check for unusual vertical ordering
            if curr_pos["y"] < prev_pos["y"] - 20:  # Moving up significantly
                # This field appears above the previous field but comes later in tab order
                issues.append({
                    "type": "warning",
                    "tab_index": curr_field.get("tab_index"),
                    "element": f"{curr_field.get('tag')} {curr_field.get('text', '')}",
                    "prev_element": f"{prev_field.get('tag')} {prev_field.get('text', '')}",
                    "issue": "Inconsistent form field tab order",
                    "details": "Form field appears above the previous field visually but comes later in tab order",
                    "recommendation": "Ensure form fields receive focus in a logical order matching their visual layout",
                    "wcag": "2.4.3"
                })
    
    return issues

def check_if_related_fields(field1, field2):
    """
    Check if two form fields are likely related (like label and input)
    This is a simple heuristic - it could be enhanced further
    """
    # For now, we're not using this in the form checks
    # This is a stub for future enhancement
    return False

def fields_properly_sequenced(field1, field2):
    """
    Check if related fields are properly sequenced
    This is a simple heuristic - it could be enhanced further
    """
    # For now, we're not using this in the form checks
    # This is a stub for future enhancement
    return True
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
### accessibility_modules\component_tests\slider_tester.py <a id='accessibility_modules_component_tests_slider_tester_py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\component_tests\slider_tester.py
- **Last Modified**: 2025-03-17 23:31:52
- **Size**: 2447 bytes

#### Code
```python
# accessibility_modules/component_tests/slider_tester.py
"""
Slider Component Accessibility Tester
Specialized module for testing range sliders and similar controls.
"""

import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

def test_sliders(driver, state_tracker, timeout=15):
    """
    Test slider components for accessibility.
    
    Args:
        driver: Selenium WebDriver instance
        state_tracker: DynamicContentStateTracker for recording state
        timeout: Maximum time to spend testing
        
    Returns:
        Dict with slider accessibility issues and summary info
    """
    logging.info("Testing slider components")
    
    # Initialize results with expected structure
    results = {
        "status": "completed",
        "issues": []
    }
    
    slider_selectors = [
        "input[type='range']",
        "[role='slider']",
        ".slider",
        ".range-slider",
        "[data-slider]"
    ]
    
    # Basic implementation to detect sliders
    for selector in slider_selectors:
        try:
            sliders = driver.find_elements(By.CSS_SELECTOR, selector)
            
            for idx, slider in enumerate(sliders):
                slider_id = f"{selector}_{idx}"
                
                # Record basic state
                initial_state = {
                    'value': slider.get_attribute('value') or '',
                    'min': slider.get_attribute('min') or '',
                    'max': slider.get_attribute('max') or ''
                }
                
                state_tracker.record_state('slider', slider_id, initial_state)
                
                # Basic accessibility checks
                if not slider.get_attribute('aria-label') and not slider.get_attribute('aria-labelledby'):
                    results["issues"].append({
                        "type": "missing_label",
                        "component_type": "slider",
                        "component_id": slider_id,
                        "details": "Slider has no accessible label",
                        "recommendation": "Add an aria-label or aria-labelledby attribute"
                    })
        
        except WebDriverException as e:
            logging.warning(f"Error finding sliders with selector {selector}: {str(e)}")
    
    return results
```
### accessibility_modules\component_tests\__init__.py <a id='accessibility_modules_component_tests___init___py'></a>
#### File Information
- **Type**: Python Script
- **Path**: accessibility_modules\component_tests\__init__.py
- **Last Modified**: 2025-03-17 23:22:57
- **Size**: 106 bytes

#### Code
```python
# accessibility_modules/component_tests/__init__.py
"""Component test modules for accessibility testing"""
```
## Text Files (Main Folder Only)

### next_steps.txt <a id='next_steps_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: next_steps.txt
- **Last Modified**: 2025-03-17 22:49:05
- **Size**: 2407 bytes

#### Content
```
Next Potential Improvements

Machine learning-based interaction detection
More sophisticated state tracking
Integration with testing frameworks
Enhanced browser compatibility

Would you like me to elaborate on any specific aspect of the implementation? Or would you prefer to discuss the next steps in developing the accessibility testing framework?


-----------------------------------------------------

You're correct. The code is incomplete. There are critical methods missing that were referenced in the code:

    _extended_slider_test
    _extended_carousel_test
    _extended_modal_test
    _extended_accordion_test
    _extended_dropdown_test

I see the comment: # Methods would be added here, following the comprehensive testing approach

Would you like me to complete the implementation with full methods for these component tests? The existing pattern suggests I should implement these methods similar to the _extended_tab_test method, with comprehensive keyboard interaction testing, state tracking, and error handling.

Would you confirm you want me to add these missing methods to ensure the implementation is complete with no omissions?
CB

Yes pls. write the complete code with no omissions

I'll provide the complete implementation, adding the missing methods while maintaining the existing code structure. I'll create an artifact with the full, complete implementation:
CB

contineu

I'll continue the implementation by adding the remaining methods:
CB

I think the second part of the code was put at the beginning of the code.

You're correct. Let me help you complete the code by adding the final part of the run_advanced_dynamic_content_test function and the logging configuration:

Now the code is complete. I've added the final part of the run_advanced_dynamic_content_test function and the logging configuration at the end of the file.

The implementation includes:

    A comprehensive DynamicContentStateTracker class
    An AdvancedDynamicContentTester class with methods for testing:
        Sliders
        Carousels
        Modals
        Accordions
        Dropdowns
        Tabs
    Robust error handling
    Detailed state tracking
    Keyboard accessibility testing
    A convenience function for running tests

Would you like me to explain any part of the implementation or verify anything?
Claude can make mistakes. Please double-check responses.


Tip:
Long chats caus
```
### paste.txt <a id='paste_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: paste.txt
- **Last Modified**: 2025-03-17 23:05:45
- **Size**: 13994 bytes

#### Content
```
 def _extended_dropdown_test(self, timeout):
        """
        Comprehensive testing of dropdown components for accessibility.
        
        Args:
            timeout: Maximum time to spend testing dropdowns
        
        Returns:
            List of dropdown accessibility issues
        """
        dropdown_issues = []
        
        dropdown_selectors = [
            "select",
            ".dropdown",
            "[role='combobox']",
            "[role='listbox']",
            "[aria-haspopup='listbox']",
            "[aria-haspopup='menu']",
            ".select",
            "[data-toggle='dropdown']"
        ]
        
        for selector in dropdown_selectors:
            try:
                dropdowns = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                for idx, dropdown in enumerate(dropdowns):
                    dropdown_id = f"{selector}_{idx}"
                    
                    # Handle differently based on whether it's a native select or custom dropdown
                    is_native_select = dropdown.tag_name.lower() == 'select'
                    
                    # Record initial state
                    initial_state = {
                        'type': 'native_select' if is_native_select else 'custom_dropdown',
                        'expanded': dropdown.get_attribute('aria-expanded') == 'true' if not is_native_select else None,
                        'selected_text': self._get_dropdown_selected_text(dropdown)
                    }
                    
                    self.state_tracker.record_state('dropdown', dropdown_id, initial_state)
                    
                    # Test keyboard accessibility
                    keyboard_issues = []
                    
                    if is_native_select:
                        # Native select elements have built-in keyboard support
                        # Test if they're actually usable
                        try:
                            dropdown.click()  # Focus the select
                            time.sleep(0.2)
                            
                            # Send arrow down to change selection
                            dropdown.send_keys(Keys.ARROW_DOWN)
                            time.sleep(0.2)
                            
                            # Get new selected value
                            new_text = self._get_dropdown_selected_text(dropdown)
                            
                            # Log the interaction
                            self.state_tracker.log_interaction(
                                'dropdown', 
                                dropdown_id, 
                                "arrow_down",
                                {'before': initial_state['selected_text'], 'after': new_text}
                            )
                            
                            # Record new state
                            self.state_tracker.record_state('dropdown', dropdown_id, {
                                'selected_text': new_text,
                                'action': 'arrow_down'
                            })
                            
                            # Check if selection changed
                            if new_text == initial_state['selected_text']:
                                dropdown_issues.append({
                                    "type": "selection_change_failure",
                                    "component_type": "dropdown",
                                    "component_id": dropdown_id,
                                    "details": "Arrow key doesn't change selection in native select",
                                    "recommendation": "Ensure select elements respond to arrow keys"
                                })
                            
                        except Exception as e:
                            dropdown_issues.append({
                                "type": "keyboard_interaction_error",
                                "component_type": "dropdown",
                                "component_id": dropdown_id,
                                "details": f"Error testing keyboard interaction: {str(e)}"
                            })
                    
                    else:
                        # Custom dropdown - more complex testing needed
                        # First, test opening the dropdown
                        try:
                            # Check initial expanded state
                            was_expanded = dropdown.get_attribute('aria-expanded') == 'true'
                            
                            # Click to toggle
                            dropdown.click()
                            time.sleep(0.3)  # Wait for animation
                            
                            # Check if expanded state changed
                            now_expanded = dropdown.get_attribute('aria-expanded') == 'true'
                            
                            # Log the interaction
                            self.state_tracker.log_interaction(
                                'dropdown', 
                                dropdown_id, 
                                "click",
                                {'before_expanded': was_expanded, 'after_expanded': now_expanded}
                            )
                            
                            # Record new state
                            self.state_tracker.record_state('dropdown', dropdown_id, {
                                'expanded': now_expanded,
                                'action': 'click'
                            })
                            
                            # If state didn't change, report an issue
                            if was_expanded == now_expanded:
                                dropdown_issues.append({
                                    "type": "state_change_failure",
                                    "component_type": "dropdown",
                                    "component_id": dropdown_id,
                                    "details": "Clicking dropdown doesn't toggle expanded state",
                                    "recommendation": "Ensure dropdowns toggle their expanded state when clicked"
                                })
                            
                            # If dropdown opened, test keyboard navigation within it
                            if now_expanded:
                                # Find dropdown options
                                dropdown_list = self._find_dropdown_list(dropdown)
                                if dropdown_list:
                                    options = dropdown_list.find_elements(By.CSS_SELECTOR, 
                                        "li, [role='option'], option, .dropdown-item")
                                    
                                    if options:
                                        # Try to navigate with arrow keys
                                        actions = ActionChains(self.driver)
                                        actions.send_keys(Keys.ARROW_DOWN)
                                        actions.perform()
                                        time.sleep(0.2)
                                        
                                        # Try to select with Enter
                                        actions = ActionChains(self.driver)
                                        actions.send_keys(Keys.ENTER)
                                        actions.perform()
                                        time.sleep(0.2)
                                        
                                        # Check if dropdown closed after selection
                                        still_expanded = dropdown.get_attribute('aria-expanded') == 'true'
                                        if still_expanded:
                                            dropdown_issues.append({
                                                "type": "selection_behavior",
                                                "component_type": "dropdown",
                                                "component_id": dropdown_id,
                                                "details": "Dropdown doesn't close after keyboard selection",
                                                "recommendation": "Ensure dropdowns close after an option is selected with Enter"
                                            })
                                    else:
                                        dropdown_issues.append({
                                            "type": "missing_options",
                                            "component_type": "dropdown",
                                            "component_id": dropdown_id,
                                            "details": "No options found in dropdown list",
                                            "recommendation": "Ensure dropdown contains selectable options"
                                        })
                                
                                # Close the dropdown if still open
                                if dropdown.get_attribute('aria-expanded') == 'true':
                                    try:
                                        dropdown.click()
                                        time.sleep(0.2)
                                    except:
                                        # Try Escape key to close
                                        actions = ActionChains(self.driver)
                                        actions.send_keys(Keys.ESCAPE)
                                        actions.perform()
                                        time.sleep(0.2)
                        
                        except Exception as e:
                            dropdown_issues.append({
                                "type": "interaction_error",
                                "component_type": "dropdown",
                                "component_id": dropdown_id,
                                "details": f"Error testing dropdown interaction: {str(e)}"
                            })
                    
                    # Check for proper ARIA attributes on custom dropdowns
                    if not is_native_select:
                        # Check for missing required attributes
                        required_attrs = []
                        
                        if dropdown.get_attribute('role') == 'combobox':
                            required_attrs = ['aria-expanded', 'aria-controls']
                        elif dropdown.get_attribute('role') == 'listbox':
                            required_attrs = ['aria-activedescendant']
                        elif dropdown.get_attribute('aria-haspopup'):
                            required_attrs = ['aria-expanded']
                        
                        missing_attrs = [attr for attr in required_attrs if not dropdown.get_attribute(attr)]
                        
                        if missing_attrs:
                            dropdown_issues.append({
                                "type": "missing_aria",
                                "component_type": "dropdown",
                                "component_id": dropdown_id,
                                "details": f"Dropdown missing required ARIA attributes: {', '.join(missing_attrs)}",
                                "recommendation": "Add missing ARIA attributes for screen reader support"
                            })
                        
                        # Check if dropdown has a label
                        if not (
                            dropdown.get_attribute('aria-label') or
                            dropdown.get_attribute('aria-labelledby') or
                            self._has_associated_label(dropdown)
                        ):
                            dropdown_issues.append({
                                "type": "missing_label",
                                "component_type": "dropdown",
                                "component_id": dropdown_id,
                                "details": "Dropdown has no accessible label",
                                "recommendation": "Add a visible label, aria-label, or aria-labelledby attribute"
                            })
            
            except WebDriverException:
                self.logger.warning(f"Could not find dropdowns with selector: {selector}")
        
        return dropdown_issuesdef _extended_tab_test(self, timeout):
    """
    Comprehensive testing of tab components for accessibility.
    
    Args:
        timeout: Maximum time to spend testing tabs
    
    Returns:
        List of tab accessibility issues
    """
    # Implementation of tab testing...

# Helper methods
def _has_associated_label(self, element):
    """Check if an element has an associated label"""
    # Implementation...

# More helper methods...

def run_advanced_dynamic_content_test(driver, timeout=15):
    """
    Convenience function to run advanced dynamic content accessibility tests.
    
    Args:
        driver: Selenium WebDriver instance
        timeout: Maximum time to spend testing each component type
    
    Returns:
        Dict of test results for different component types
    """
    try:
        tester = AdvancedDynamicContentTester(driver)
        return tester.test_interactive_components(timeout)
    except Exception as e:
        logging.error(f"Error in advanced dynamic content testing: {str(e)}")
        return {
            "error": str(e),
            "details": "Failed to complete advanced dynamic content testing",
            "traceback": traceback.format_exc()
        }

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)
```
### project structure.txt <a id='project structure_txt'></a>
#### File Information
- **Type**: Text File
- **Path**: project structure.txt
- **Last Modified**: 2025-03-11 20:19:29
- **Size**: 1604 bytes

#### Content
```
accessibility_checker/
│
├── accessibility_checker.py     # Main script
├── requirements.txt             # Dependencies
├── script_extract.py            # Tool for extracting and organizing code
├── create_terminology.py        # Create terminology JSON files
├── create_terminology_file.py   # Create terminology JSON files (alternative)
├── accessibility_terminology.json # Standardized terminology mappings
│
└── accessibility_modules/       # Module directory
    ├── __init__.py              # Makes the directory a package
    ├── tab_order_checker.py     # Tab order checking functionality
    ├── focus_order_checker.py   # Enhanced focus order testing
    ├── focusable_elements.py    # Missing focusable elements detection
    ├── aria_checker.py          # ARIA and keyboard accessibility checks
    ├── image_checker.py         # Image accessibility checks
    ├── color_contrast.py        # Color contrast analysis (to be implemented)
    ├── form_checker.py          # Form accessibility checks (to be implemented)
    ├── landmark_checker.py      # Landmark and structure checks (to be implemented)
    ├── terminology_validator.py # Ensures consistent accessibility terminology
    ├── report_generator.py      # Main report generation coordinator
    ├── html_report_generator.py # Professional HTML report generator
    ├── simple_html_report_generator.py # Simpler HTML report generator
    └── test_accordion.py        # Test script for report accordions
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
## JSON Files (Main Folder Only)

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