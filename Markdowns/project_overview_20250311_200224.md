# Project Scripts Overview
*Generated on 2025-03-11 20:02:24 from folder: C:\Users\clint\Pickles*
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

### Text Files (Main Folder Only)
- [project structure.txt](#project structure_txt)
- [requirements.txt](#requirements_txt)

### JSON Files (Main Folder Only)
- [accessibility_terminology.json](#accessibility_terminology_json)

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
- **Last Modified**: 2025-03-11 19:59:39
- **Size**: 17768 bytes

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
    Check if a path contains archive-related directories.
    
    Args:
        path (Path): The path to check
    
    Returns:
        bool: True if path is in an archive, False otherwise
    """
    archive_keywords = ['archive', 'archived', 'backup', 'old']
    path_parts = str(path).lower().split(os.sep)
    return any(keyword in part for part in path_parts for keyword in archive_keywords)

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
    notebook_files = [f for f, ext in all_files if ext == '.ipynb']
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
- **Last Modified**: 2025-03-11 19:59:39
- **Size**: 17768 bytes

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
    Check if a path contains archive-related directories.
    
    Args:
        path (Path): The path to check
    
    Returns:
        bool: True if path is in an archive, False otherwise
    """
    archive_keywords = ['archive', 'archived', 'backup', 'old']
    path_parts = str(path).lower().split(os.sep)
    return any(keyword in part for part in path_parts for keyword in archive_keywords)

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
    notebook_files = [f for f, ext in all_files if ext == '.ipynb']
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
## Text Files (Main Folder Only)

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