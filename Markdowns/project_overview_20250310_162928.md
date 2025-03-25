# Project Scripts Overview
*Generated on 2025-03-10 16:29:27 from folder: C:\Users\clint\Pickles*
*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*

## Accessibility Terminology
- **interactive element not in tab order**
  - Preferred: Keyboard navigation barrier
  - Explanation: Elements that appear interactive but cannot be accessed via keyboard
- **tab order issue**
  - Preferred: Inconsistent keyboard navigation sequence
  - Explanation: Elements that disrupt the expected keyboard navigation flow

## How to Continue This Project with Claude
1. Upload or copy the contents of this entire markdown file to Claude
2. Tell Claude: "These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task]."
3. Reference specific scripts or code blocks by their section names when asking questions

*The structured format below will help Claude understand your project's organization and codebase.*
## Table of Contents
- [Accessibility_Checker](#Accessibility_Checker)
- [Accessibility_Checker_Starter](#Accessibility_Checker_Starter)
- [config](#config)
- [Data_Loader](#Data_Loader)
- [Enhanced_Report_Generator](#Enhanced_Report_Generator)
- [Generate_Accessibility_Report](#Generate_Accessibility_Report)
- [Missing_Focusable_Elements](#Missing_Focusable_Elements)
- [Script_Extract](#Script_Extract)
- [Untitled](#Untitled)

## Accessibility_Checker <a id='Accessibility_Checker'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:13:15
- **Size**: 4270 bytes

### Code
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
# First, ensure the modules are available
module_files = [
    "Accessibility_Checker.py",
    "Data_Loader.py",
    "Enhanced_Report_Generator.py"
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
    <h3>A comprehensive tool for e
```
## Accessibility_Checker_Starter <a id='Accessibility_Checker_Starter'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:24:40
- **Size**: 9190 bytes

### Code
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
## config <a id='config'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:48:48
- **Size**: 1124 bytes

### Code
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
## Data_Loader <a id='Data_Loader'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:13:30
- **Size**: 9082 bytes

### Code
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
## Enhanced_Report_Generator <a id='Enhanced_Report_Generator'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:04:57
- **Size**: 14466 bytes

### Code
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
## Generate_Accessibility_Report <a id='Generate_Accessibility_Report'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:53:37
- **Size**: 5323 bytes

### Code
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
## Missing_Focusable_Elements <a id='Missing_Focusable_Elements'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:39:13
- **Size**: 3389 bytes

### Code
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
## Script_Extract <a id='Script_Extract'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 22:11:03
- **Size**: 10569 bytes

### Code
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
## Untitled <a id='Untitled'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-05 18:31:07
- **Size**: 821 bytes

### Code
#### Cell 1
```python
!conda clean --all
```
#### Cell 2
```python
 
```