# Project Scripts Overview
*Generated on 2025-03-02 21:41:34 from folder: C:\Users\clint\Pickles*
*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*

## How to Continue This Project with Claude
1. Upload or copy the contents of this entire markdown file to Claude
2. Tell Claude: "These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task]."
3. Reference specific scripts or code blocks by their section names when asking questions

*The structured format below will help Claude understand your project's organization and codebase.*
## Table of Contents
- [Aria_Checks](#Aria_Checks)
- [check_tab_order](#check_tab_order)
- [Check_URL](#Check_URL)
- [Comprehensive_Report](#Comprehensive_Report)
- [Enhanced_Report](#Enhanced_Report)
- [Main](#Main)
- [MissingFocusable](#MissingFocusable)
- [Report](#Report)
- [reset_jupyter_kernels](#reset_jupyter_kernels)
- [Script_Extract](#Script_Extract)
- [Verify_Missing_Focusable](#Verify_Missing_Focusable)

## Aria_Checks <a id='Aria_Checks'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-27 22:07:45
- **Size**: 15208 bytes

### Code
#### Cell 1
```python
# ARIA and Keyboard Navigation Accessibility Checker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime
from pathlib import Path

# Include the webdriver function here instead of importing from check_tab_order
def get_webdriver(browser='chrome'):
    """
    Initialize and return a WebDriver instance for the specified browser.
    
    Args:
        browser (str): Browser name ('chrome', 'firefox', or 'edge')
        
    Returns:
        WebDriver: Initialized WebDriver instance
    """
    if browser == 'chrome':
        service = ChromeService()
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)
    elif browser == 'edge':
        service = EdgeService()
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browser. Choose 'chrome', 'firefox', or 'edge'.")
    return driver

def check_aria_attributes(url, browser='chrome'):
    """
    Check for proper ARIA attributes on a webpage.
    
    Args:
        url (str): URL of the webpage to check
        browser (str): Browser to use for checking
        
    Returns:
        list: Issues found with ARIA attributes
    """
    driver = get_webdriver(browser)
    issues = []
    
    try:
        driver.get(url)
        
        # Wait for page to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
        except Exception as e:
            issues.append(f"Page load error: {str(e)}")
            return issues
        
        # Get page HTML
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # Check for missing alt attributes on images
        images = soup.find_all('img')
        for idx, img in enumerate(images):
            if not img.has_attr('alt'):
                src = img.get('src', '[no src]')
                issues.append(f"Image {idx+1} missing alt attribute: {src[:50]}")
        
        # Check for proper form labeling
        form_elements = soup.find_all(['input', 'textarea', 'select'])
        for idx, elem in enumerate(form_elements):
            # Skip hidden and submit inputs
            if elem.get('type') in ['hidden', 'submit', 'button']:
                continue
                
            has_label = False
            elem_id = elem.get('id')
            
            # Check for associated label
            if elem_id:
                label = soup.find('label', attrs={'for': elem_id})
                if label:
                    has_label = True
            
            # Check for aria-label or aria-labelledby
            if elem.has_attr('aria-label') or elem.has_attr('aria-labelledby'):
                has_label = True
            
            # Check for placeholder (not ideal, but better than nothing)
            has_placeholder = elem.has_attr('placeholder')
            
            if not has_label:
                elem_type = elem.get('type', elem.name)
                elem_name = elem.get('name', '[no name]')
                if has_placeholder:
                    issues.append(f"Form element {idx+1} ({elem_type}: {elem_name}) has placeholder but no proper label")
                else:
                    issues.append(f"Form element {idx+1} ({elem_type}: {elem_name}) has no label")
        
        # Check for proper heading structure
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if headings:
            # Check if H1 exists
            h1_count = len(soup.find_all('h1'))
            if h1_count == 0:
                issues.append("Page has no H1 heading")
            elif h1_count > 1:
                issues.append(f"Page has {h1_count} H1 headings (should typically have only one)")
            
            # Check for proper heading hierarchy
            level_order = []
            for heading in headings:
                level = int(heading.name[1])
                level_order.append(level)
            
            # Check for skipped levels (e.g., h1 -> h3)
            for i in range(len(level_order) - 1):
                if level_order[i+1] > level_order[i] + 1:
                    issues.append(f"Heading hierarchy skips from h{level_order[i]} to h{level_order[i+1]}")
        else:
            issues.append("Page has no heading elements")
        
        # Check for ARIA landmark roles
        has_main = bool(soup.find(attrs={'role': 'main'}) or soup.find('main'))
        has_nav = bool(soup.find(attrs={'role': 'navigation'}) or soup.find('nav'))
        has_banner = bool(soup.find(attrs={'role': 'banner'}) or soup.find('header'))
        
        if not has_main:
            issues.append("Page missing main content landmark (role='main' or <main>)")
        if not has_nav:
            issues.append("Page missing navigation landmark (role='navigation' or <nav>)")
        if not has_banner:
            issues.append("Page missing banner/header landmark (role='banner' or <header>)")
        
        return issues
    
    finally:
        driver.quit()

def check_keyboard_navigation(url, browser='chrome'):
    """
    Test basic keyboard navigation on a webpage.
    
    Args:
        url (str): URL of the webpage to check
        browser (str): Browser to use for checking
        
    Returns:
        list: Issues found with keyboard navigation
    """
    driver = get_webdriver(browser)
    issues = []
    
    try:
        driver.get(url)
        
        # Wait for page to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
        except Exception as e:
            issues.append(f"Page load error: {str(e)}")
            return issues, []
        
        # Find focusable elements
        focusable_elements = driver.find_elements(By.CSS_SELECTOR, 
            "a, button, input, select, textarea, [tabindex]:not([tabindex='-1'])")
        
        if not focusable_elements:
            issues.append("No focusable elements found on the page")
            return issues, []
        
        # Test keyboard navigation with Tab key
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.TAB)
        
        # Check if something gets focused
        active_element = driver.switch_to.active_element
        if active_element == body:
            issues.append("First Tab press doesn't focus any element")
        
        # Test basic keyboard navigation through the page
        tab_count = 0
        max_tabs = min(20, len(focusable_elements))  # Limit to 20 tabs or number of elements
        
        focused_elements = []
        
        for i in range(max_tabs):
            active_element = driver.switch_to.active_element
            
            # Get some identifying info about the element
            tag_name = active_element.tag_name
            element_text = active_element.text[:30] if active_element.text else ""
            element_type = active_element.get_attribute("type") or ""
            
            element_info = f"{tag_name}"
            if element_type:
                element_info += f"[type='{element_type}']"
            if element_text:
                element_info += f": '{element_text}'"
            
            focused_elements.append(element_info)
            
            # Press Tab to move to next element
            active_element.send_keys(Keys.TAB)
            tab_count += 1
            
            # Small delay to let focus change
            time.sleep(0.2)
        
        # Check if we could navigate through elements
        if tab_count < 2:
            issues.append("Could not navigate through page using Tab key")
        
        # Check for visible focus indicators
        issues.append("Note: Manual check needed for visible focus indicators")
        
        return issues, focused_elements
    
    finally:
        driver.quit()

def run_comprehensive_check(url, browser='chrome'):
    """
    Run a comprehensive accessibility check including tab order, ARIA, and keyboard navigation.
    
    Args:
        url (str): URL of the webpage to check
        browser (str): Browser to use for checking
        
    Returns:
        dict: Comprehensive report data
    """
    # We need to have run check_tab_order.ipynb first to have access to check_tab_order function
    print(f"Running comprehensive accessibility check for {url} using {browser}...")
    start_time = time.time()
    
    # Run all checks
    try:
        # First try to run with the check_tab_order function that should be in the global namespace
        tab_order, tab_issues = check_tab_order(url, browser)
        print(f"Tab order check complete: Found {len(tab_order)} elements, {len(tab_issues)} issues")
    except NameError:
        # If check_tab_order is not defined, make a placeholder
        print("Warning: check_tab_order function not found. Run check_tab_order.ipynb first.")
        tab_order, tab_issues = [], ["Tab order check not run"]
    
    # Run ARIA and keyboard checks
    aria_issues = check_aria_attributes(url, browser)
    print(f"ARIA check complete: Found {len(aria_issues)} issues")
    
    keyboard_issues, focused_elements = check_keyboard_navigation(url, browser)
    print(f"Keyboard navigation check complete: Found {len(keyboard_issues)} issues")
    
    check_time = time.time() - start_time
    
    # Create reports directory if it doesn't exist
    reports_dir = Path("accessibility_reports")
    if not reports_dir.exists():
        reports_dir.mkdir(exist_ok=True)
    
    # Compile comprehensive report
    report_data = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "browser": browser,
        "summary": {
            "total_elements": len(tab_order),
            "tab_order_issues": len(tab_issues),
            "aria_issues": len(aria_issues),
            "keyboard_issues": len(keyboard_issues),
            "scan_time_seconds": check_time
        },
        "tab_order_data": tab_order,
        "tab_order_issues": tab_issues,
        "aria_issues": aria_issues,
        "keyboard_issues": keyboard_issues,
        "keyboard_navigation_elements": focused_elements
    }
    
    # Save report
    clean_url = url.replace('http://', '').replace('https://', '').replace('/', '_')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"accessibility_reports/comprehensive_{clean_url}_{timestamp}.json"
    
    with open(output_filename, "w") as f:
        json.dump(report_data, f, indent=4)
    
    print(f"Comprehensive check completed in {check_time:.2f} seconds")
    print(f"Found {len(tab_issues)} tab order issues, {len(aria_issues)} ARIA issues, and {len(keyboard_issues)} keyboard navigation issues")
    print(f"Report saved to {output_filename}")
    
    return report_data

# This notebook is designed to be run from Main.ipynb and will use the URL from Check_URL.ipynb
# No standalone tests are included to avoid duplicating work
```
## check_tab_order <a id='check_tab_order'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-27 22:07:41
- **Size**: 4715 bytes

### Code
#### Cell 1
```python
# Import necessary libraries for web scraping and automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from bs4 import BeautifulSoup

def get_webdriver(browser='chrome'):
    """
    Initialize and return a WebDriver instance for the specified browser.
    
    Args:
        browser (str): Browser name ('chrome', 'firefox', or 'edge')
        
    Returns:
        WebDriver: Initialized WebDriver instance
    """
    if browser == 'chrome':
        service = ChromeService()
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)
    elif browser == 'edge':
        service = EdgeService()
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browser. Choose 'chrome', 'firefox', or 'edge'.")
    return driver

def check_tab_order(url, browser='chrome'):
    """
    Check the tab order of interactive elements on a webpage.
    
    Args:
        url (str): URL of the webpage to check
        browser (str): Browser to use for checking
        
    Returns:
        tuple: (tab_order, issues) where tab_order is a list of elements with their tab order
               and issues is a list of tab order problems
    """
    driver = get_webdriver(browser)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    elements = soup.find_all(['a', 'button', 'input', 'textarea', 'select'])
    
    tab_order = []
    
    for idx, elem in enumerate(elements):
        # Extract text and limit to 30 characters for readability
        text = elem.get_text().strip()[:30] if elem.get_text() else "[No text]"
        # For input elements, try to get placeholder or name attributes
        if elem.name == 'input' and not text:
            if elem.has_attr('placeholder'):
                text = f"[Input: {elem['placeholder'][:30]}]"
            elif elem.has_attr('name'):
                text = f"[Input: {elem['name'][:30]}]"
        
        if elem.has_attr('tabindex'):
            tab_order.append((idx+1, elem.name, text, elem['tabindex']))
        else:
            tab_order.append((idx+1, elem.name, text, None))
    
    driver.quit()
    
    issues = []
    for i in range(len(tab_order) - 1):
        current = tab_order[i]
        next_elem = tab_order[i + 1]
        if current[3] is not None and next_elem[3] is not None:
            if int(current[3]) >= int(next_elem[3]):
                issues.append(f"Tab order issue: Element {current[0]} (tabindex={current[3]}) comes before Element {next_elem[0]} (tabindex={next_elem[3]})")
    
    return tab_order, issues

# Test the function if running this notebook directly
if __name__ == "__main__":
    test_url = 'http://example.com'
    test_browser = 'chrome'
    result, found_issues = check_tab_order(test_url, test_browser)
    print(f"Found {len(result)} elements and {len(found_issues)} issues")
```
#### Cell 2
```python

```
## Check_URL <a id='Check_URL'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-28 16:10:10
- **Size**: 5606 bytes

### Code
#### Cell 1
```python
# URL Checker - A dedicated script for checking tab orders on specific URLs
%run check_tab_order.ipynb
import json
import time
from datetime import datetime
import os
from pathlib import Path

# Define the reports directory with proper path handling
REPORTS_DIR = Path("accessibility_reports")

# Create accessibility_reports directory if it doesn't exist (case-insensitive check)
if not REPORTS_DIR.exists():
    REPORTS_DIR.mkdir(exist_ok=True)
    print(f"📁 Created {REPORTS_DIR} directory")
else:
    print(f"📁 Using existing {REPORTS_DIR} directory")

# URL Configuration - Configure your check parameters here
url = 'https://sse.com'  # Change this to the URL you want to check
browser_choice = 'firefox'  # 'chrome', 'firefox', or 'edge'

# Print configuration info
print(f"📌 URL to check: {url}")
print(f"🌐 Browser: {browser_choice}")

# Create a timestamp for file naming
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
safe_url = url.replace('http://', '').replace('https://', '').replace('/', '_')
output_filename = f"tab_order_{safe_url}_{timestamp}.json"
output_file = REPORTS_DIR / output_filename

# Check tab order
print(f"🔍 Checking tab order for {url} using {browser_choice}...")
start_time = time.time()

try:
    tab_order, issues = check_tab_order(url, browser_choice)
    check_time = time.time() - start_time
    print(f"✅ Scan complete in {check_time:.2f} seconds")
    print(f"📊 Found {len(tab_order)} tabbable elements and {len(issues)} issues")

    # Save to JSON file
    report_data = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "browser": browser_choice,
        "summary": {
            "total_elements": len(tab_order),
            "issues_found": len(issues),
            "scan_time_seconds": check_time
        },
        "report_data": tab_order,
        "issues": issues
    }

    # Save the timestamped report
    with open(output_file, "w") as f:
        json.dump(report_data, f, indent=4)
    print(f"💾 Report saved to {output_file}")

    # Save the main report file
    main_report_path = REPORTS_DIR / "tab_order_report.json"
    with open(main_report_path, "w") as f:
        json.dump(report_data, f, indent=4)
    print(f"💾 Report also saved as {main_report_path} for Enhanced Report.ipynb")

    # Print tab order issues
    if issues:
        print("\n⚠️ Tab order issues found:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("\n✅ No tab order issues found.")

    # Print sample of elements found
    print("\n📋 Sample of elements found:")
    sample_size = min(5, len(tab_order))
    for index, tag, text, tabindex in tab_order[:sample_size]:
        tabindex_display = tabindex if tabindex is not None else "auto"
        print(f"{index}. <{tag}> '{text}' (tabindex={tabindex_display})")
    if len(tab_order) > sample_size:
        print(f"... and {len(tab_order) - sample_size} more elements")

except Exception as e:
    check_time = time.time() - start_time
    print(f"❌ Error during scan: {str(e)}")
    # Create an error report
    report_data = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "browser": browser_choice,
        "summary": {
            "error": str(e),
            "scan_time_seconds": check_time
        },
        "report_data": [],
        "issues": [f"Error during scan: {str(e)}"]
    }
    # Save the error report
    with open(output_file, "w") as f:
        json.dump(report_data, f, indent=4)
    print(f"💾 Error report saved to {output_file}")

print("\n📊 Next steps:")
print("1. Run Enhanced Report.ipynb to see full analysis")
print("2. Edit url and browser_choice above to check a different website")
```
#### Cell 2
```python

```
## Comprehensive_Report <a id='Comprehensive_Report'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-28 23:44:14
- **Size**: 11468 bytes

### Code
#### Cell 1
```python
import os
import json
from datetime import datetime
from pathlib import Path

def generate_report_filename(prefix='comprehensive', extension='html'):
    """Generate a consistently formatted filename with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports_dir = Path("accessibility_reports")
    reports_dir.mkdir(exist_ok=True)
    filename = f"{prefix}_report_{timestamp}.{extension}"
    return str(reports_dir / filename)

def generate_comprehensive_report(report_data, missing_focusable_data=None):
    """Generate an enhanced HTML report with consistent timestamping."""
    # Generate a timestamped filename
    output_file = generate_report_filename()
    
    # Use current timestamp if not provided in the report
    current_timestamp = datetime.now()
    
    # Try to use timestamp from report data if available
    if report_data and report_data.get("timestamp"):
        try:
            report_timestamp = datetime.fromisoformat(report_data["timestamp"])
            current_timestamp = report_timestamp
        except:
            pass
    
    # Format timestamp for display
    formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare issues lists
    tab_order_issues = report_data.get('tab_order_issues', [])
    aria_issues = report_data.get('aria_issues', [])
    keyboard_issues = report_data.get('keyboard_issues', [])
    missing_focusable_issues = missing_focusable_data.get('missing_focusable_issues', []) if missing_focusable_data else []
    
    # Calculate total issues
    total_issues = len(tab_order_issues) + len(aria_issues) + len(keyboard_issues) + len(missing_focusable_issues)
    
    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comprehensive Accessibility Report - {formatted_timestamp}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            background-color: #005A9C;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1rem;
        }}
        .stat-card {{
            background-color: #f5f5f5;
            padding: 1rem;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #005A9C;
        }}
        .stat-label {{
            color: #666;
        }}
        .section {{
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 1rem;
            margin-bottom: 1rem;
        }}
        h1, h2 {{
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }}
        .issue {{
            color: #d32f2f;
            background-color: #ffebee;
            padding: 0.5rem;
            border-radius: 3px;
            margin-bottom: 0.5rem;
        }}
        .issue-severity-high {{ border-left: 4px solid #d32f2f; }}
        .issue-severity-medium {{ border-left: 4px solid #ff9800; }}
        .issue-severity-low {{ border-left: 4px solid #4caf50; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Comprehensive Accessibility Report</h1>
            <p>Generated on {formatted_timestamp}</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{total_issues}</div>
                <div class="stat-label">Total Accessibility Issues</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(tab_order_issues)}</div>
                <div class="stat-label">Tab Order Issues</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(aria_issues)}</div>
                <div class="stat-label">ARIA Attribute Issues</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(keyboard_issues)}</div>
                <div class="stat-label">Keyboard Navigation Issues</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(missing_focusable_issues)}</div>
                <div class="stat-label">Missing Focusable Elements</div>
            </div>
        </div>
        
        <section class="section">
            <h2>Report Summary</h2>
            <p><strong>URL:</strong> {report_data.get('url', 'N/A')}</p>
            <p><strong>Browser:</strong> {report_data.get('browser', 'N/A')}</p>
        </section>
        
        <section class="section">
            <h2>Tab Order Issues</h2>
            {"".join(f'<div class="issue issue-severity-high">{issue}</div>' for issue in tab_order_issues) if tab_order_issues else '<p>No tab order issues found.</p>'}
        </section>
        
        <section class="section">
            <h2>ARIA Attribute Issues</h2>
            {"".join(f'<div class="issue issue-severity-medium">{issue}</div>' for issue in aria_issues) if aria_issues else '<p>No ARIA attribute issues found.</p>'}
        </section>
        
        <section class="section">
            <h2>Keyboard Navigation Issues</h2>
            {"".join(f'<div class="issue issue-severity-medium">{issue}</div>' for issue in keyboard_issues) if keyboard_issues else '<p>No keyboard navigation issues found.</p>'}
        </section>
        
        <section class="section">
            <h2>Missing Focusable Elements</h2>
            {"".join(f'<div class="issue issue-severity-high">{issue.get("issue", "Unknown issue")}</div>' for issue in missing_focusable_issues) if missing_focusable_issues else '<p>No missing focusable elements found.</p>'}
        </section>
        
        <footer>
            <p>Accessibility Report Generated on {formatted_timestamp}</p>
        </footer>
    </div>
</body>
</html>"""
    
    # Save the HTML report
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Comprehensive report generated and saved to {output_file}")
    return output_file

# Rest of the previous implementation remains the same (save_report_metadata, load functions, etc.)
# Auto-generate the comprehensive report when this notebook is run
try:
    # Try to find the latest comprehensive report file
    report_files = list(REPORTS_DIR.glob("comprehensive_*.json"))
    
    if report_files:
        # Use the most recent comprehensive report
        latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
        with open(latest_report, "r") as f:
            report_data = json.load(f)
            
        # Try to get missing focusable data if available
        try:
            url = report_data.get("url", "")
            missing_files = list(REPORTS_DIR.glob(f"missing_focusable_{url.replace(':', '_').replace('/', '_')}*.json"))
            missing_data = None
            
            if missing_files:
                latest_missing = max(missing_files, key=lambda f: f.stat().st_mtime)
                with open(latest_missing, "r") as f:
                    missing_data = json.load(f)
                    
            # Generate the report
            output_file = generate_comprehensive_report(report_data, missing_data)
            print(f"✅ Comprehensive HTML report generated at: {output_file}")
        except Exception as e:
            # Fall back to generating report without missing data
            output_file = generate_comprehensive_report(report_data)
            print(f"✅ Comprehensive HTML report generated at: {output_file} (without missing focusable data)")
    else:
        print("⚠️ No comprehensive report data found. Run Aria_Checks.ipynb to generate the report data first.")
except Exception as e:
    print(f"❌ Error generating comprehensive report: {e}")
```
#### Cell 2
```python

```
## Enhanced_Report <a id='Enhanced_Report'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-27 22:07:28
- **Size**: 17891 bytes

### Code
#### Cell 1
```python
# Accessibility Tab Order Report Generator
import json
import os
import base64
import re
from datetime import datetime
from pathlib import Path

# Define the reports directory with proper path handling
REPORTS_DIR = Path("accessibility_reports")

# Create accessibility_reports directory if it doesn't exist (case-insensitive check)
if not REPORTS_DIR.exists():
    REPORTS_DIR.mkdir(exist_ok=True)
    print(f"📁 Created {REPORTS_DIR} directory")
else:
    print(f"📁 Using existing {REPORTS_DIR} directory")

# Define the path for the main report file
MAIN_REPORT_PATH = REPORTS_DIR / "tab_order_report.json"

def load_tab_order_report(json_file=None):
    """
    Load tab order report from JSON file with robust error handling.
    
    Args:
        json_file (str): Path to the JSON report file
    
    Returns:
        dict: Parsed report data or empty report structure
    """
    if json_file is None:
        json_file = MAIN_REPORT_PATH
    
    json_path = Path(json_file)
    
    # If the file doesn't exist in the specified path, try to look for it in alternative locations
    if not json_path.exists():
        # Try the root directory
        alt_path = Path("tab_order_report.json")
        if alt_path.exists():
            json_path = alt_path
            print(f"📄 Using report from root directory: {alt_path}")
        else:
            # Try to find any available report
            possible_reports = list(REPORTS_DIR.glob("tab_order_*.json"))
            if possible_reports:
                # Use the most recent report
                json_path = max(possible_reports, key=lambda p: p.stat().st_mtime)
                print(f"📄 Using most recent report found: {json_path}")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ Successfully loaded report from {json_path}")
        return data
    except FileNotFoundError:
        print(f"❌ File {json_path} not found. Make sure to run Check_URL.ipynb first.")
        return {
            "report_data": [], 
            "issues": [], 
            "url": "", 
            "timestamp": "", 
            "browser": "",
            "summary": {}
        }
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON from {json_path}. File may be corrupted.")
        return {
            "report_data": [], 
            "issues": [], 
            "url": "", 
            "timestamp": "", 
            "browser": "",
            "summary": {}
        }
    except Exception as e:
        print(f"❌ Unexpected error reading {json_path}: {str(e)}")
        return {
            "report_data": [], 
            "issues": [], 
            "url": "", 
            "timestamp": "", 
            "browser": "",
            "summary": {}
        }

def create_bookmarklet(element_index, element_text, url):
    """
    Generate a bookmarklet for locating a specific element directly on the website.
    
    Args:
        element_index (int): Index of the element
        element_text (str): Text description of the element
        url (str): Website URL to navigate to
    
    Returns:
        str: Bookmarklet JavaScript code
    """
    # Escaped element text to prevent potential JS injection
    safe_text = element_text.replace("'", "\\'").replace('"', '\\"')
    
    # Very simple JavaScript to open the URL
    js_code = f"""
    (function() {{
        // Open the website
        var newWindow = window.open('{url}', '_blank');
        
        // Optional: Show a message to the user
        if (newWindow) {{
            newWindow.focus();
            alert('Opened {url}\\n\\nElement details:\\nIndex: {element_index}\\nText: {safe_text}');
        }} else {{
            alert('Unable to open website. Please check your browser\\'s popup settings.');
        }}
    }})();
    """
    
    # Encode the JavaScript as a base64 bookmarklet
    js_encoded = base64.b64encode(js_code.encode()).decode()
    return f"javascript:eval(atob('{js_encoded}'))"

def count_tag_types(elements):
    """Count the frequency of different HTML tags"""
    tag_counts = {}
    for _, tag, _, _ in elements:
        if tag in tag_counts:
            tag_counts[tag] += 1
        else:
            tag_counts[tag] = 1
    return tag_counts

def generate_enhanced_report(report_data):
    """
    Generate an enhanced HTML report with visualizations and analysis.
    
    Args:
        report_data (dict): Report data dictionary
        
    Returns:
        str: Path to the generated HTML file
    """
    if not report_data or not report_data.get("report_data"):
        print("❌ No valid report data found to generate enhanced report")
        return None
    
    # Extract key data
    elements = report_data.get("report_data", [])
    issues = report_data.get("issues", [])
    url = report_data.get("url", "Unknown URL")
    timestamp = report_data.get("timestamp", "")
    if timestamp:
        try:
            timestamp = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass
    browser = report_data.get("browser", "Unknown")
    
    # Count element types
    tag_counts = count_tag_types(elements)
    total_elements = len(elements)
    
    # Create an HTML report
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tab Order Accessibility Report - {url}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
            }}
            header {{
                background-color: #005A9C;
                color: white;
                padding: 1rem;
                border-radius: 5px;
                margin-bottom: 1rem;
            }}
            h1, h2, h3 {{
                margin-top: 1.5rem;
                margin-bottom: 0.5rem;
            }}
            .card {{
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 1rem;
                margin-bottom: 1rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 1rem;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            .issue {{
                color: #d32f2f;
                background-color: #ffebee;
                padding: 0.5rem;
                border-radius: 3px;
                margin-bottom: 0.5rem;
            }}
            .stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin-bottom: 1rem;
            }}
            .stat-card {{
                background-color: #f5f5f5;
                padding: 1rem;
                border-radius: 5px;
                text-align: center;
            }}
            .stat-number {{
                font-size: 2rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }}
            .badge {{
                display: inline-block;
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 0.8rem;
                background-color: #e0e0e0;
            }}
            .badge-auto {{
                background-color: #4caf50;
                color: white;
            }}
            .badge-custom {{
                background-color: #ff9800;
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Tab Order Accessibility Report</h1>
                <p>Generated on {timestamp}</p>
            </header>
            
            <section class="card">
                <h2>Report Summary</h2>
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">{len(elements)}</div>
                        <div>Tabbable Elements</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{len(issues)}</div>
                        <div>Tab Order Issues</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{browser.upper()}</div>
                        <div>Browser Used</div>
                    </div>
                </div>
                <p><strong>URL:</strong> <a href="{url}" target="_blank">{url}</a></p>
            </section>
    """
    
    # Add issues section if there are any
    if issues:
        html_content += f"""
            <section class="card">
                <h2>Tab Order Issues</h2>
                <p>The following issues were found with the tab order:</p>
        """
        
        for i, issue in enumerate(issues, 1):
            html_content += f"""
                <div class="issue">
                    <strong>Issue #{i}:</strong> {issue}
                </div>
            """
        
        html_content += """
            </section>
        """
    else:
        html_content += f"""
            <section class="card">
                <h2>No Tab Order Issues</h2>
                <p>Great job! No tab order issues were found on this page.</p>
            </section>
        """
    
    # Add element breakdown
    html_content += f"""
        <section class="card">
            <h2>Element Type Breakdown</h2>
            <table>
                <tr>
                    <th>Element Type</th>
                    <th>Count</th>
                    <th>Percentage</th>
                </tr>
    """
    
    for tag, count in tag_counts.items():
        percentage = (count / total_elements) * 100 if total_elements > 0 else 0
        html_content += f"""
            <tr>
                <td>&lt;{tag}&gt;</td>
                <td>{count}</td>
                <td>{percentage:.1f}%</td>
            </tr>
        """
    
    html_content += """
            </table>
        </section>
    """
    
    # Add full element list
    html_content += f"""
        <section class="card">
            <h2>All Tabbable Elements</h2>
            <p>The following elements were found in tab order sequence:</p>
            <table>
                <tr>
                    <th>Index</th>
                    <th>Element Type</th>
                    <th>Description</th>
                    <th>Tab Index</th>
                </tr>
    """
    
    for idx, tag, text, tabindex in elements:
        tabindex_display = tabindex if tabindex is not None else "auto"
        tabindex_class = "badge-auto" if tabindex is None or tabindex == "auto" else "badge-custom"
        html_content += f"""
            <tr>
                <td>{idx}</td>
                <td>&lt;{tag}&gt;</td>
                <td>{text}</td>
                <td><span class="badge {tabindex_class}">{tabindex_display}</span></td>
            </tr>
        """
    
    html_content += """
            </table>
        </section>
    """
    
    # Add recommendations
    html_content += f"""
        <section class="card">
            <h2>Recommendations</h2>
            <ul>
                <li>The natural DOM order should usually be used for tab order (avoid using tabindex values greater than 0)</li>
                <li>Use tabindex="0" to make non-interactive elements focusable, but keep them in natural DOM order</li>
                <li>Use tabindex="-1" for elements that should be programmatically focusable but not in the tab order</li>
                <li>Make sure all interactive elements have appropriate keyboard interaction and visible focus states</li>
                <li>Check that the tab order makes logical sense from a user's perspective</li>
            </ul>
        </section>
        
        <footer>
            <p>Tab Order Accessibility Checker — Generated on {timestamp}</p>
        </footer>
        </div>
    </body>
    </html>
    """
    
    # Save the HTML report
    output_file = "enhanced_report.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Enhanced report generated and saved to {output_file}")
    return output_file

# If notebook is run directly, load the report and generate the enhanced report
if __name__ == "__main__":
    report_data = load_tab_order_report()
    if report_data and report_data.get("report_data"):
        output_file = generate_enhanced_report(report_data)
        print(f"📊 Open {output_file} in your browser to view the full report")
    else:
        print("❌ No valid report data found. Please run Check_URL.ipynb first to generate a report.")
```
## Main <a id='Main'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-02 21:17:16
- **Size**: 6572 bytes

### Code
#### Cell 1
```python
# Comprehensive Accessibility Checker - Main Workflow
# This script coordinates the entire accessibility checking workflow

# First run check_tab_order.ipynb to define the check_tab_order function
%run check_tab_order.ipynb

# Now run Check_URL.ipynb to get the URL configuration
%run Check_URL.ipynb
# The URL and browser_choice variables are now available from Check_URL.ipynb

# Run the MissingFocusable.ipynb to get those functions
%run MissingFocusable.ipynb

# Now run Aria_Checks.ipynb which needs check_tab_order
%run Aria_Checks.ipynb

# Finally run the report generator
%run Comprehensive_Report.ipynb

import os
import json
import glob
from datetime import datetime
import sys
from pathlib import Path
import time

# Define the reports directory with proper path handling
REPORTS_DIR = Path("accessibility_reports")

# Create accessibility_reports directory if it doesn't exist
if not REPORTS_DIR.exists():
    REPORTS_DIR.mkdir(exist_ok=True)
    print(f"📁 Created {REPORTS_DIR} directory")
else:
    print(f"📁 Using existing {REPORTS_DIR} directory")

def load_comprehensive_report(report_path=None):
    """Load the comprehensive report data from a JSON file."""
    if report_path is None:
        report_path = REPORTS_DIR / "comprehensive_report.json"
    
    if not report_path.exists():
        return {
            "url": "",
            "timestamp": "",
            "browser": "",
            "tab_order_data": [],
            "tab_order_issues": [],
            "aria_issues": [],
            "keyboard_issues": []
        }
    
    with open(report_path, "r") as f:
        return json.load(f)

def load_missing_focusable_report(url):
    """Load the missing focusable report data for a given URL."""
    # Find the latest report for the given URL
    report_files = REPORTS_DIR.glob(f"missing_focusable_*{url.replace(':', '_').replace('/', '_')}*.json")
    latest_report = max(report_files, key=lambda f: f.stat().st_mtime, default=None)
    
    if latest_report:
        with open(latest_report, "r") as f:
            return json.load(f)
    else:
        return {
            "url": url,
            "missing_elements": [],
            "missing_focusable_issues": [],
            "summary": {
                "total_missing": 0,
                "total_issues": 0
            }
        }

# Display welcome message
print("=" * 60)
print("📋 Comprehensive Web Accessibility Checker")
print("=" * 60)
print("This tool checks websites for accessibility issues including:")
print("  ✓ Tab Order & Focus Management")
print("  ✓ Missing Focusable Elements")
print("  ✓ ARIA Attributes & Semantic HTML")
print("  ✓ Keyboard Navigation")
print("  ✓ WCAG 2.1 Success Criteria")
print("-" * 60)

# Display current URL configuration
print(f"Current URL configuration: {url}")
print(f"Current browser: {browser_choice}")
print("-" * 60)

#
# Run the comprehensive checks
print("\n" + "=" * 60)
print("Running comprehensive accessibility checks...")
print("=" * 60)

try:
    # Run comprehensive check
    comprehensive_data = run_comprehensive_check(url, browser_choice)
    print(f"✅ Comprehensive check completed for {url}")
    
    # Run missing focusable check
    missing_focusable_data = run_missing_focusable_check(url, browser_choice)
    print(f"✅ Missing focusable check completed for {url}")
    
    # Generate comprehensive HTML report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_url = url.replace('http://', '').replace('https://', '').replace('/', '_')
    
    # Get the latest comprehensive report file
    latest_report = None
    report_files = list(REPORTS_DIR.glob(f"comprehensive_{clean_url}_*.json"))
    if report_files:
        latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
        with open(latest_report, "r") as f:
            comprehensive_data = json.load(f)
    
    # Generate the HTML report using the data from both checks
    output_file = generate_comprehensive_report(comprehensive_data, missing_focusable_data)
    print(f"✅ Final HTML report generated: {output_file}")
    
    # Add a message about viewing the report
    print("\n" + "=" * 60)
    print(f"🎉 All checks completed! Open this file in your browser to view the report:")
    print(f"   {os.path.abspath(output_file)}")
    print("=" * 60)
    
except Exception as e:
    print(f"❌ Error during final report generation: {e}")
    import traceback
    traceback.print_exc()
```
#### Cell 2
```python

```
## MissingFocusable <a id='MissingFocusable'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-28 21:34:43
- **Size**: 26848 bytes

### Code
#### Cell 1
```python
import time
import json
import os
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import pandas as pd
import re
from bs4 import BeautifulSoup

def identify_visual_clickables(driver):
    """Identify elements that visually appear to be clickable based on CSS properties"""
    # Common CSS selectors for clickable elements
    css_selectors = [
        # Elements with cursor:pointer
        "*[style*='cursor: pointer'], *[style*='cursor:pointer']",
        # Elements with common button-like classes
        "*[class*='btn'], *[class*='button'], *[class*='clickable']",
        # Elements with hover effects
        "*[class*='hover']",
        # Elements with event handlers
        "*[onclick], *[onmousedown], *[onmouseup]"
    ]
    
    visual_clickables = set()
    
    for selector in css_selectors:
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for element in elements:
                if element.is_displayed():
                    visual_clickables.add(element)
        except:
            continue
    
    # Execute JavaScript to find elements with computed cursor:pointer style
    js_script = """
    const elements = [];
    const allElements = document.querySelectorAll('*');
    for (let i = 0; i < allElements.length; i++) {
        const style = window.getComputedStyle(allElements[i]);
        if (style.cursor === 'pointer' && allElements[i].offsetParent !== null) {
            elements.push(allElements[i]);
        }
    }
    return elements;
    """
    js_elements = driver.execute_script(js_script)
    visual_clickables.update(js_elements)
    
    return list(visual_clickables)

def get_all_focusable_elements(driver):
    """Get all elements that can receive keyboard focus"""
    # Standard focusable elements selector
    focusable_selector = (
        "a[href], button, input:not([type='hidden']), select, textarea, " + 
        "[tabindex]:not([tabindex='-1']), [contentEditable=true], " +
        "video[controls], audio[controls]"
    )
    
    # Find all elements that should be focusable
    focusable_elements = driver.find_elements(By.CSS_SELECTOR, focusable_selector)
    
    # Filter out hidden elements
    visible_focusable = []
    for element in focusable_elements:
        try:
            if element.is_displayed() and element.is_enabled():
                visible_focusable.append(element)
        except:
            continue
            
    return visible_focusable

def get_element_identifier(driver, element):
    """
    Generate a unique identifier for an element based on its attributes and position
    This helps with comparing elements across different collections
    """
    script = """
    function getElementIdentifier(element) {
        if (!element) return null;
        
        let id = element.tagName.toLowerCase();
        
        // Add ID if it exists
        if (element.id) {
            id += '#' + element.id;
            return id; // ID should be unique enough
        }
        
        // Add classes
        if (element.className && typeof element.className === 'string') {
            const classes = element.className.trim().split(/\\s+/).join('.');
            if (classes) {
                id += '.' + classes;
            }
        }
        
        // Add name attribute for form elements
        if (element.name) {
            id += '[name="' + element.name + '"]';
        }
        
        // Add type for inputs
        if (element.tagName.toLowerCase() === 'input' && element.type) {
            id += '[type="' + element.type + '"]';
        }
        
        // Add position info if still not unique enough
        let position = '';
        let parent = element.parentElement;
        if (parent) {
            let siblings = Array.from(parent.children);
            let index = siblings.indexOf(element);
            position = `:nth-child(${index + 1})`;
        }
        
        return id + position;
    }
    
    return getElementIdentifier(arguments[0]);
    """
    
    try:
        return driver.execute_script(script, element)
    except:
        # Fallback to basic info if the script fails
        tag_name = element.tag_name
        element_id = element.get_attribute("id") or ""
        if element_id:
            return f"{tag_name}#{element_id}"
        return f"{tag_name}#{hash(element)}"

def test_keyboard_focusability(driver, elements):
    """Test if elements can actually receive keyboard focus"""
    # Reset focus to body
    driver.find_element(By.TAG_NAME, "body").click()
    
    keyboard_focusable = []
    non_focusable = []
    
    # Store the original active element
    original_active = driver.execute_script("return document.activeElement")
    
    for element in elements:
        try:
            # Try to focus using JavaScript
            driver.execute_script("arguments[0].focus()", element)
            
            # Check if element became focused
            active_element = driver.execute_script("return document.activeElement")
            
            if active_element == element:
                keyboard_focusable.append(element)
            else:
                non_focusable.append(element)
                
            # Reset focus
            driver.execute_script("arguments[0].focus()", original_active)
            
        except:
            non_focusable.append(element)
            continue
            
    return keyboard_focusable, non_focusable

def simulate_tab_order(driver):
    """Simulate pressing Tab key and record the tab order"""
    # Focus on the body to start
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    
    tab_order = []
    tab_order_identifiers = set()
    max_tabs = 300  # Safety limit to prevent infinite loops
    
    actions = ActionChains(driver)
    
    # Record the initial active element
    initial_active = driver.execute_script("return document.activeElement")
    initial_active_id = get_element_identifier(driver, initial_active)
    
    for _ in range(max_tabs):
        # Press Tab key
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.1)  # Small delay to ensure focus shifts
        
        # Get currently focused element
        active_element = driver.execute_script("return document.activeElement")
        element_id = get_element_identifier(driver, active_element)
        
        # If we've looped back to the beginning or hit the body, we're done
        if element_id in tab_order_identifiers or active_element == initial_active or element_id == initial_active_id:
            break
            
        # Add to tab order and mark as visited
        tab_order.append(active_element)
        tab_order_identifiers.add(element_id)
    
    return tab_order, tab_order_identifiers

def check_for_missing_focusable(driver, url):
    """Find elements that appear interactive but aren't in the tab order"""
    # Navigate to the URL
    print(f"Navigating to {url}...")
    driver.get(url)
    time.sleep(5)  # Allow page to fully load
    
    # Get visually clickable elements
    visual_clickables = identify_visual_clickables(driver)
    print(f"Found {len(visual_clickables)} visually clickable elements")
    
    # Generate identifiers for visual clickables
    visual_clickable_ids = set()
    for element in visual_clickables:
        element_id = get_element_identifier(driver, element)
        visual_clickable_ids.add(element_id)
    
    # Get standard focusable elements
    focusable_elements = get_all_focusable_elements(driver)
    print(f"Found {len(focusable_elements)} potentially focusable elements")
    
    # Test which elements are actually keyboard focusable
    keyboard_focusable, non_focusable = test_keyboard_focusability(driver, focusable_elements)
    print(f"Found {len(keyboard_focusable)} keyboard focusable elements")
    print(f"Found {len(non_focusable)} non-focusable elements that should be focusable")
    
    # Get tab order and their identifiers
    tab_order, tab_order_identifiers = simulate_tab_order(driver)
    print(f"Found {len(tab_order)} elements in tab order")
    
    # Find clickable elements that aren't in the tab order
    missing_from_tab_order = []
    
    for element in visual_clickables:
        element_id = get_element_identifier(driver, element)
        
        # Skip if element is already in tab order
        if element_id in tab_order_identifiers:
            continue
        
        # Check if it's an interactive element
        tag_name = element.tag_name.lower()
        element_type = element.get_attribute("type") or ""
        
        # Skip known non-interactive elements unless they have click handlers
        if tag_name in ["div", "span", "p", "img"] and not element.get_attribute("onclick"):
            # Special case: check if it's a container with an interactive child
            has_interactive_child = driver.execute_script("""
                return Boolean(arguments[0].querySelector('a, button, input, select, textarea'));
            """, element)
            
            if has_interactive_child:
                continue
        
        # Skip hidden inputs
        if tag_name == "input" and element_type == "hidden":
            continue
        
        # Skip if the element is a child of a focusable element already in tab order
        is_child_of_focusable = driver.execute_script("""
            let element = arguments[0];
            let parents = [];
            let parent = element.parentElement;
            
            while (parent) {
                parents.push(parent);
                parent = parent.parentElement;
            }
            
            for (let i = 0; i < parents.length; i++) {
                if (parents[i].tagName === 'A' || 
                    parents[i].tagName === 'BUTTON' ||
                    (parents[i].tagName === 'INPUT' && parents[i].type !== 'hidden')) {
                    return true;
                }
            }
            
            return false;
        """, element)
        
        if is_child_of_focusable:
            continue
        
        # Add to missing list
        missing_from_tab_order.append(element)
    
    return {
        "url": url,
        "tab_order_elements": tab_order,
        "visual_clickables": visual_clickables,
        "missing_focusable": missing_from_tab_order,
        "non_focusable": non_focusable
    }

def format_element_info(driver, element):
    """Format element information for reporting"""
    try:
        element_text = element.text[:50] + ("..." if len(element.text) > 50 else "")
        tag_name = element.tag_name
        element_id = element.get_attribute("id") or ""
        element_class = element.get_attribute("class") or ""
        element_type = element.get_attribute("type") or ""
        element_role = element.get_attribute("role") or ""
        element_onclick = element.get_attribute("onclick") or ""
        
        # Determine the reason this element should be keyboard accessible
        reasons = []
        if tag_name.lower() in ["a", "button", "input", "select", "textarea"]:
            reasons.append(f"is a <{tag_name}> element")
        if element_onclick:
            reasons.append("has onClick handler")
        if "btn" in element_class.lower() or "button" in element_class.lower():
            reasons.append("has button-like class")
        if element_role in ["button", "link", "menuitem", "tab", "checkbox", "radio"]:
            reasons.append(f"has role=\"{element_role}\"")
            
        # Get computed styles that suggest interactivity
        is_visually_interactive = driver.execute_script("""
            const style = window.getComputedStyle(arguments[0]);
            return {
                cursor: style.cursor,
                hasHoverEffect: (style.getPropertyValue('--has-hover') === 'true' || 
                                 arguments[0].matches(':hover')),
            };
        """, element)
        
        if is_visually_interactive['cursor'] == 'pointer':
            reasons.append("has cursor:pointer style")
        if is_visually_interactive['hasHoverEffect']:
            reasons.append("has hover effect")
        
        # Try to get XPath for element location
        xpath = ""
        try:
            xpath = driver.execute_script('''
                function getPathTo(element) {
                    if (element.id !== '')
                        return '//*[@id="' + element.id + '"]';
                    if (element === document.body)
                        return '/html/body';

                    var index = 1;
                    var siblings = element.parentNode.childNodes;
                    for (var i = 0; i < siblings.length; i++) {
                        var sibling = siblings[i];
                        if (sibling === element)
                            return getPathTo(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + index + ']';
                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                            index++;
                    }
                }
                return getPathTo(arguments[0]);
            ''', element)
        except:
            pass
        
        return {
            "tag": tag_name,
            "id": element_id,
            "class": element_class,
            "type": element_type,
            "text": element_text,
            "xpath": xpath,
            "reasons": reasons,
            "role": element_role
        }
    except:
        return {"error": "Could not retrieve element information"}

def generate_missing_focusable_report(driver, results):
    """Generate a report of elements missing from tab order"""
    report = []
    
    for result in results:
        url = result["url"]
        missing_elements = result["missing_focusable"]
        non_focusable = result["non_focusable"]
        
        url_report = {
            "url": url,
            "total_missing": len(missing_elements),
            "total_non_focusable": len(non_focusable),
            "missing_elements": [],
            "non_focusable_elements": []
        }
        
        # Format missing elements info
        for element in missing_elements:
            url_report["missing_elements"].append(format_element_info(driver, element))
            
        # Format non-focusable elements info
        for element in non_focusable:
            url_report["non_focusable_elements"].append(format_element_info(driver, element))
            
        report.append(url_report)
        
    return report

def run_missing_focusable_check(url, browser_choice="chrome"):
    """
    Main entry point for checking missing focusable elements.
    This function is called from Main.ipynb.
    
    Parameters:
    url (str): The URL to check
    browser_choice (str): Browser to use (chrome, firefox, etc.)
    
    Returns:
    dict: Results of the missing focusable analysis with keys for 'missing_elements' and 'missing_focusable_issues'
    """
    driver = None
    try:
        print(f"Checking for missing focusable elements on {url}...")
        
        # Set up WebDriver based on browser choice
        if browser_choice.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1366,768")
            driver = webdriver.Chrome(options=options)
        elif browser_choice.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1366")
            options.add_argument("--height=768")
            driver = webdriver.Firefox(options=options)
        else:
            # Default to Chrome
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1366,768")
            driver = webdriver.Chrome(options=options)
        
        # Run the analysis
        results = [check_for_missing_focusable(driver, url)]
        report = generate_missing_focusable_report(driver, results)
        
        # Format the results for Main.ipynb compatibility
        if len(report) > 0:
            first_report = report[0]
            
            # Extract missing elements
            missing_elements = first_report.get("missing_elements", [])
            
            # Generate issues from the missing elements
            missing_focusable_issues = []
            for idx, element in enumerate(missing_elements):
                tag = element.get("tag", "unknown")
                text = element.get("text", "")
                reasons = element.get("reasons", [])
                
                # Skip elements with no clear reasons to be focusable
                if not reasons:
                    continue
                
                reason_text = ", ".join(reasons)
                
                issue = {
                    "issue": f"Interactive element not in tab order: <{tag}> {text} ({reason_text})",
                    "impact": "High" if tag.lower() in ['button', 'a', 'input'] else "Medium", 
                    "recommendation": "Make element keyboard accessible by adding tabindex='0' and appropriate keyboard event handlers."
                }
                missing_focusable_issues.append(issue)
            
            # Create timestamp for report
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_url = url.replace('http://', '').replace('https://', '').replace('/', '_')
            
            # Create report directory if it doesn't exist
            report_dir = Path("accessibility_reports")
            if not report_dir.exists():
                report_dir.mkdir(exist_ok=True)
            
            # Create report data structure
            report_data = {
                "url": url,
                "timestamp": datetime.now().isoformat(),
                "browser": browser_choice,
                "missing_elements": missing_elements,
                "missing_focusable_issues": missing_focusable_issues,
                "summary": {
                    "total_missing": len(missing_elements),
                    "total_issues": len(missing_focusable_issues)
                }
            }
            
            # Save report to JSON
            output_filename = f"missing_focusable_{safe_url}_{timestamp}.json"
            output_path = report_dir / output_filename
            
            with open(output_path, "w") as f:
                json.dump(report_data, f, indent=4)
            
            print(f"Found {len(missing_elements)} potentially missing focusable elements")
            print(f"Found {len(missing_focusable_issues)} accessibility issues")
            print(f"Report saved to {output_path}")
            
        else:
            report_data = {
                "url": url,
                "missing_elements": [],
                "missing_focusable_issues": [],
                "summary": {
                    "total_missing": 0,
                    "total_issues": 0
                }
            }
        
        # Close the driver
        driver.quit()
        
        return report_data
    
    except Exception as e:
        print(f"Error in missing focusable check: {str(e)}")
        import traceback
        traceback.print_exc()
        
        if driver:
            driver.quit()
        
        return {
            "url": url,
            "missing_elements": [],
            "missing_focusable_issues": [],
            "summary": {
                "error": str(e)
            }
        }

# Uncomment to test the script independently
# if __name__ == "__main__":
#     url = "https://example.com"
#     results = run_missing_focusable_check(url, "chrome")
#     print(f"Found {len(results.get('missing_elements', []))} missing focusable elements")
#     print(f"Found {len(results.get('missing_focusable_issues', []))} issues")
```
#### Cell 2
```python

```
## Report <a id='Report'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-27 22:07:23
- **Size**: 6072 bytes

### Code
#### Cell 1
```python
import json
# Load data from JSON file
json_file = "tab_order_report.json"
try:
    with open(json_file, "r") as f:
        data = json.load(f)
    print(f"Successfully loaded report from {json_file}")
except FileNotFoundError:
    print(f"File {json_file} not found. Make sure to run main.ipynb first.")
    data = {"report_data": [], "issues": []}
report_data = data["report_data"]
issues = data["issues"]
# Generate the report
print(f"\nTab Order Report ({len(report_data)} elements):")
for index, tag, text, tabindex in report_data:
    print(f"{index}. Tag: {tag}, Text: {text}, Tabindex: {tabindex}")
# Print any tab order issues
print(f"\nTab Order Issues ({len(issues)}):")
if issues:
    for i, issue in enumerate(issues, 1):
        print(f"{i}. {issue}")
else:
    print("No tab order issues found.")
# Generate some statistics
if report_data:
    # Count elements by type
    element_counts = {}
    for _, tag, _, _ in report_data:  # Use underscores, not asterisks
        if tag in element_counts:
            element_counts[tag] += 1
        else:
            element_counts[tag] = 1
    
    print("\nElement type statistics:")
    for tag, count in element_counts.items():
        print(f"- {tag}: {count} elements")
    
    # Count elements with explicit tabindex
    tabindex_count = sum(1 for _, _, _, tabindex in report_data if tabindex is not None)  # Fixed variable name and syntax
    print(f"\nElements with explicit tabindex: {tabindex_count} ({tabindex_count/len(report_data)*100:.1f}%)")

# Add this function to the end of your Report.ipynb
def generate_simple_finder_bookmarklet():
    js_code = """
    javascript:(function() {
        // Function to find an element by index
        function findElementByIndex(index) {
            var elements = document.querySelectorAll('a, button, input, textarea, select');
            if (index <= elements.length) {
                var targetElement = elements[index-1];
                targetElement.scrollIntoView({behavior: 'smooth', block: 'center'});
                
                // Highlight the element
                var originalOutline = targetElement.style.outline;
                targetElement.style.outline = '3px solid red';
                
                // Create notification
                var notification = document.createElement('div');
                notification.style.position = 'fixed';
                notification.style.top = '10px';
                notification.style.left = '50%';
                notification.style.transform = 'translateX(-50%)';
                notification.style.backgroundColor = 'rgba(0,0,0,0.8)';
                notification.style.color = 'white';
                notification.style.padding = '10px 20px';
                notification.style.borderRadius = '5px';
                notification.style.zIndex = '10000';
                notification.innerHTML = 'Element ' + index + ' found';
                document.body.appendChild(notification);
                
                // Reset after 3 seconds
                setTimeout(function() {
                    targetElement.style.outline = originalOutline;
                    document.body.removeChild(notification);
                }, 3000);
                
                return true;
            }
            return false;
        }
        
        // Show prompt to enter element index
        var elementIndex = prompt('Enter element index (1-151):', '');
        if (elementIndex && !isNaN(elementIndex)) {
            var index = parseInt(elementIndex);
            if (!findElementByIndex(index)) {
                alert('Element not found. Please check the index.');
            }
        }
    })();
    """
    
    bookmarklet = js_code.replace('\n', '').replace('    ', '')
    
    print("Element Finder Bookmarklet:")
    print("1. Copy the following code:")
    print(bookmarklet)
    print("\n2. Create a new bookmark in your browser")
    print("3. Paste this code as the URL of the bookmark")
    print("4. Save the bookmark with a name like 'SSE Element Finder'")
    print("5. Visit sse.com and click the bookmark")
    print("6. Enter the element number you want to find when prompted")

# Run this function at the end of your notebook
generate_simple_finder_bookmarklet()
```
#### Cell 2
```python

```
## reset_jupyter_kernels <a id='reset_jupyter_kernels'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-28 23:43:59
- **Size**: 6967 bytes

### Code
#### Cell 1
```python
import os
import nbformat
from jupyter_client.kernelspec import KernelSpecManager
import ipykernel

def should_process_notebook(notebook_file):
    """
    Determine if a notebook should be processed.
    
    Criteria:
    1. Must have .ipynb extension
    2. Exclude notebooks with specific names (like this script itself)
    3. Optional: Add more specific filtering criteria
    """
    # Basic extension check
    if not notebook_file.lower().endswith('.ipynb'):
        return False
    
    # Exclude current script or known system notebooks
    excluded_names = [
        'reset_notebooks.ipynb',  # name of this script
        '.ipynb_checkpoints',  # Jupyter checkpoint files
        'untitled.ipynb'  # Default unnamed notebook
    ]
    
    for excluded in excluded_names:
        if excluded in notebook_file.lower():
            return False
    
    return True

def clear_notebook_outputs():
    """
    Clear outputs of notebooks in the current directory.
    """
    # Get the list of notebooks in the current directory
    all_files = os.listdir('.')
    notebook_files = [f for f in all_files if should_process_notebook(f)]
    
    print("Notebooks found:")
    for notebook_file in notebook_files:
        print(f"- {notebook_file}")
    
    # List to store processed files
    processed_files = []
    
    print("\nProcessing notebooks:")
    for notebook_file in notebook_files:
        try:
            # Read the notebook
            with open(notebook_file, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Flag to track if changes were made
            changes_made = False
            
            # Clear output of all cells
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    if cell.outputs or cell.execution_count is not None:
                        cell.outputs = []
                        cell.execution_count = None
                        changes_made = True
            
            # Only write back if changes were made
            if changes_made:
                with open(notebook_file, 'w', encoding='utf-8') as f:
                    nbformat.write(nb, f)
                print(f"✓ Cleared outputs for {notebook_file}")
                processed_files.append(notebook_file)
            else:
                print(f"- No changes needed for {notebook_file}")
        
        except Exception as e:
            print(f"✗ Error processing {notebook_file}: {e}")
    
    return processed_files

def reset_jupyter_kernels():
    """
    Reset and remove all existing Jupyter kernels.
    """
    # Get kernel spec manager
    ksm = KernelSpecManager()
    
    # Find all existing kernel specs
    kernel_specs = ksm.find_kernel_specs()
    
    print("\nExisting Kernel Specs:")
    for kernel_name in kernel_specs:
        try:
            print(f"- {kernel_name}")
            ksm.remove_kernel_spec(kernel_name)
        except Exception as e:
            print(f"✗ Error removing kernel {kernel_name}: {e}")
    
    # Reinstall the default IPython kernel
    try:
        import subprocess
        import sys
        subprocess.run([sys.executable, '-m', 'ipykernel', 'install', '--user'], check=True)
        print("\n✓ Reinstalled default IPython kernel")
    except Exception as e:
        print(f"✗ Error reinstalling default kernel: {e}")

# Run functions to clear outputs and reset kernels
processed_files = clear_notebook_outputs()
reset_jupyter_kernels()

print("\nSummary:")
print(f"Total notebooks processed: {len(processed_files)}")
if processed_files:
    print("Processed notebooks:")
    for file in processed_files:
        print(f"- {file}")
```
#### Cell 2
```python

```
## Script_Extract <a id='Script_Extract'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-02 21:41:09
- **Size**: 4339 bytes

### Code
#### Cell 1
```python
import os
import json
from pathlib import Path
from datetime import datetime

def extract_code_from_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def generate_markdown_file(folder_path):
    notebook_files = list(Path(folder_path).glob('*.ipynb'))

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*\n"
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
        markdown_content += extract_code_from_notebook(notebook_file)

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
## Verify_Missing_Focusable <a id='Verify_Missing_Focusable'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-02-28 23:44:20
- **Size**: 6386 bytes

### Code
#### Cell 1
```python
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Get the current working directory
current_dir = os.getcwd()

# Set the path to the geckodriver executable
geckodriver_path = os.path.join(current_dir, 'geckodriver')  # Use the correct filename

try:
    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service)
    print("Firefox WebDriver successfully initialized")
    driver.quit()
except Exception as e:
    print(f"WebDriver Error: {e}")

{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Selenium and WebDriver Diagnostic Check"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 0,
            "metadata": {},
            "source": [
                "import sys\n",
                "import platform\n",
                "\n",
                "# Python details\n",
                "print(\"Python Version:\", sys.version)\n",
                "print(\"Python Platform:\", platform.platform())\n",
                "\n",
                "# Selenium check\n",
                "try:\n",
                "    import selenium\n",
                "    print(\"Selenium Version:\", selenium.__version__)\n",
                "except ImportError:\n",
                "    print(\"Selenium is not installed\")\n",
                "\n",
                "# WebDriver check\n",
                "try:\n",
                "    from selenium import webdriver\n",
                "    driver = webdriver.Firefox()\n",
                "    print(\"Firefox WebDriver successfully initialized\")\n",
                "    driver.quit()\n",
                "except Exception as e:\n",
                "    print(f\"WebDriver Error: {e}\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}
```
#### Cell 2
```python

```