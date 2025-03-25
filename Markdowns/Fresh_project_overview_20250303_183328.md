# Project Scripts Overview
*Generated on 2025-03-03 18:33:28 from folder: C:\Users\clint\Pickles*
*This is a Jupyter Notebooks project. The following code snippets provide context for continuing development.*

## How to Continue This Project with Claude
1. Upload or copy the contents of this entire markdown file to Claude
2. Tell Claude: "These are the files from my Jupyter Notebooks project. I'd like to continue working on [specific task]."
3. Reference specific scripts or code blocks by their section names when asking questions

*The structured format below will help Claude understand your project's organization and codebase.*
## Table of Contents
- [Fresh_Accessibility_Report.ipynb](#Fresh_Accessibility_Report.ipynb)
- [Fresh_JSON_Reports](#Fresh_JSON_Reports)
- [Fresh_Reports](#Fresh_Reports)
- [Script_Extract](#Script_Extract)

## Fresh_Accessibility_Report.ipynb <a id='Fresh_Accessibility_Report.ipynb'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 18:23:18
- **Size**: 18752 bytes

### Code
#### Cell 1
```python
# Fresh Accessibility Report Generator
import json
import os
from pathlib import Path
from datetime import datetime
import re

# Define constants
REPORTS_DIR = Path("accessibility_reports")

def normalize_url(url):
    """Normalize URLs to prevent duplicate files"""
    if not url:
        return "unknown"
    normalized = url.lower().replace('http://', '').replace('https://', '')
    normalized = normalized.replace('www.', '')
    normalized = normalized.rstrip('/')
    normalized = re.sub(r'[^a-zA-Z0-9_\-.]', '_', normalized)
    return normalized

def load_data(url):
    """Load all necessary data for report generation"""
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tab_order": [],
        "missing_elements": [],
        "aria_issues": [],
        "keyboard_issues": []
    }
    
    # Find the latest files for this URL
    try:
        # 1. Load tab order data
        tab_files = list(REPORTS_DIR.glob(f"tab_order_{clean_url}_*.json"))
        if tab_files:
            latest_tab = max(tab_files, key=lambda p: p.stat().st_mtime)
            print(f"Loading tab order data from {latest_tab}")
            with open(latest_tab, 'r') as f:
                tab_data = json.load(f)
                data["tab_order"] = tab_data.get("tab_order_data", [])
                data["tab_issues"] = tab_data.get("tab_order_issues", [])
        
        # 2. Load missing focusable data
        missing_files = list(REPORTS_DIR.glob(f"missing_focusable_{clean_url}_*.json"))
        if missing_files:
            latest_missing = max(missing_files, key=lambda p: p.stat().st_mtime)
            print(f"Loading missing focusable data from {latest_missing}")
            with open(latest_missing, 'r') as f:
                missing_data = json.load(f)
                data["missing_elements"] = [issue.get("issue") if isinstance(issue, dict) else issue 
                                           for issue in missing_data.get("missing_focusable_issues", [])]
        
        # 3. Load comprehensive data for ARIA and keyboard issues
        comp_files = list(REPORTS_DIR.glob(f"comprehensive_{clean_url}_*.json"))
        if comp_files:
            latest_comp = max(comp_files, key=lambda p: p.stat().st_mtime)
            print(f"Loading comprehensive data from {latest_comp}")
            with open(latest_comp, 'r') as f:
                comp_data = json.load(f)
                data["aria_issues"] = comp_data.get("aria_issues", [])
                data["keyboard_issues"] = comp_data.get("keyboard_issues", [])
        
        return data
    
    except Exception as e:
        print(f"Error loading data: {e}")
        import traceback
        traceback.print_exc()
        return data

def generate_html_report(data, output_path=None):
    """Generate a clean, well-formatted HTML accessibility report"""
    # Prepare output path
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = normalize_url(data.get("url", "unknown"))
        output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
    
    # Extract data
    url = data.get("url", "Unknown URL")
    timestamp = data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    tab_order = data.get("tab_order", [])
    tab_issues = data.get("tab_issues", [])
    missing_elements = data.get("missing_elements", [])
    aria_issues = data.get("aria_issues", [])
    keyboard_issues = data.get("keyboard_issues", [])
    
    # Create HTML content
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Accessibility Report - {url}</title>
        <style>
            /* Clean, modern styling */
            :root {{
                --primary-color: #0057b7;
                --secondary-color: #f8f9fa;
                --accent-color: #ffd700;
                --text-color: #333;
                --light-text: #666;
                --border-color: #ddd;
                --warning-color: #ff9800;
                --error-color: #f44336;
                --success-color: #4caf50;
            }}
            
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: #fff;
                margin: 0;
                padding: 0;
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
                margin-bottom: 30px;
            }}
            
            header h1 {{
                margin: 0;
                font-size: 28px;
                font-weight: 500;
            }}
            
            header p {{
                margin: 5px 0 0;
                opacity: 0.9;
            }}
            
            .section {{
                background-color: var(--secondary-color);
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 30px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .section h2 {{
                margin-top: 0;
                color: var(--primary-color);
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 10px;
                font-weight: 500;
            }}
            
            .issue {{
                background-color: white;
                padding: 15px;
                margin-bottom: 15px;
                border-radius: 5px;
                border-left: 4px solid var(--error-color);
            }}
            
            .issue.tab-order {{
                border-left-color: var(--warning-color);
            }}
            
            .issue.aria {{
                border-left-color: var(--primary-color);
            }}
            
            .issue.keyboard {{
                border-left-color: var(--accent-color);
            }}
            
            .summary {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 20px;
            }}
            
            .summary-item {{
                background-color: white;
                padding: 15px;
                border-radius: 5px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .summary-number {{
                font-size: 36px;
                font-weight: bold;
                color: var(--primary-color);
                margin-bottom: 5px;
            }}
            
            .no-issues {{
                background-color: #e8f5e9;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 15px;
                text-align: center;
                color: var(--success-color);
            }}
            
            footer {{
                text-align: center;
                padding: 20px;
                margin-top: 30px;
                border-top: 1px solid var(--border-color);
                color: var(--light-text);
                font-size: 14px;
            }}
            
            /* Responsive adjustments */
            @media (max-width: 768px) {{
                .container {{
                    padding: 10px;
                }}
                header {{
                    padding: 15px;
                }}
                .section {{
                    padding: 15px;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <div class="container">
                <h1>Accessibility Report</h1>
                <p>Website: {url}</p>
                <p>Generated on: {timestamp}</p>
            </div>
        </header>
        
        <div class="container">
            <div class="section">
                <h2>Summary</h2>
                <div class="summary">
                    <div class="summary-item">
                        <div class="summary-number">{len(missing_elements)}</div>
                        <div>Keyboard Inaccessible Elements</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{len(tab_issues)}</div>
                        <div>Tab Order Issues</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{len(aria_issues)}</div>
                        <div>ARIA & Semantic Issues</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{len(keyboard_issues)}</div>
                        <div>Keyboard Navigation Issues</div>
                    </div>
                </div>
            </div>
    """
    
    # Add Keyboard Inaccessible Elements section
    html += """
            <div class="section">
                <h2>Keyboard Inaccessible Elements</h2>
    """
    
    if missing_elements:
        html += "                <p>The following interactive elements cannot be accessed using keyboard navigation:</p>\n"
        for element in missing_elements:
            html += f"""                <div class="issue">{element}</div>\n"""
    else:
        html += """                <div class="no-issues">No keyboard inaccessible elements found. Great job!</div>\n"""
    
    html += "            </div>\n"
    
    # Add Tab Order Issues section
    html += """
            <div class="section">
                <h2>Tab Order Issues</h2>
    """
    
    if tab_issues:
        html += "                <p>The following issues were found with the tab order sequence:</p>\n"
        for issue in tab_issues:
            html += f"""                <div class="issue tab-order">{issue}</div>\n"""
    else:
        html += """                <div class="no-issues">No tab order issues found. Great job!</div>\n"""
    
    html += "            </div>\n"
    
    # Add ARIA Issues section
    html += """
            <div class="section">
                <h2>ARIA and Semantic HTML Issues</h2>
    """
    
    if aria_issues:
        html += "                <p>The following issues were found with ARIA attributes and semantic HTML:</p>\n"
        for issue in aria_issues:
            html += f"""                <div class="issue aria">{issue}</div>\n"""
    else:
        html += """                <div class="no-issues">No ARIA or semantic HTML issues found. Great job!</div>\n"""
    
    html += "            </div>\n"
    
    # Add Keyboard Navigation Issues section
    html += """
            <div class="section">
                <h2>Keyboard Navigation Issues</h2>
    """
    
    if keyboard_issues:
        html += "                <p>The following issues were found with keyboard navigation:</p>\n"
        for issue in keyboard_issues:
            html += f"""                <div class="issue keyboard">{issue}</div>\n"""
    else:
        html += """                <div class="no-issues">No keyboard navigation issues found. Great job!</div>\n"""
    
    html += "            </div>\n"
    
    # Add Tab Order Element Sample section if there are elements
    if tab_order:
        html += """
            <div class="section">
                <h2>Tab Order Sample</h2>
                <p>First few elements in the tab order sequence:</p>
        """
        
        for i, element in enumerate(tab_order[:5]):
            html += f"""                <div class="issue tab-order">{element}</div>\n"""
        
        if len(tab_order) > 5:
            html += f"""                <p>...and {len(tab_order) - 5} more elements</p>\n"""
        
        html += "            </div>\n"
    
    # Add footer and close tags
    html += f"""
            <footer>
                <p>This report was generated automatically using the Accessibility Checker Tool</p>
                <p>For more information on web accessibility, visit <a href="https://www.w3.org/WAI/" target="_blank">W3C Web Accessibility Initiative</a></p>
            </footer>
        </div>
    </body>
    </html>
    """
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save HTML report
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Report successfully generated at: {output_path}")
        return str(output_path)
    except Exception as e:
        print(f"Error saving report: {e}")
        import traceback
        traceback.print_exc()
        return None

# Main function to run the report generation
def generate_accessibility_report(url):
    """Generate an accessibility report for the specified URL"""
    print(f"Generating accessibility report for {url}...")
    
    # Ensure reports directory exists
    REPORTS_DIR.mkdir(exist_ok=True)
    
    # Load data from existing reports
    data = load_data(url)
    
    # Generate HTML report
    report_path = generate_html_report(data)
    
    if report_path:
        print(f"\n{'='*60}")
        print(f"🎉 Accessibility report generated successfully!")
        print(f"📄 Report saved to: {os.path.abspath(report_path)}")
        print(f"{'='*60}")
        return report_path
    else:
        print(f"\n{'='*60}")
        print(f"❌ Failed to generate accessibility report")
        print(f"{'='*60}")
        return None

# Run the report generation if this is the main script
if __name__ == "__main__":
    # URL to generate report for
    website_url = "https://www.sse.com"  # Change this to your target website
    
    # Generate the report
    generate_accessibility_report(website_url)
```
## Fresh_JSON_Reports <a id='Fresh_JSON_Reports'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 18:26:18
- **Size**: 24319 bytes

### Code
#### Cell 1
```python
# Fresh JSON Report Generator
# Generates clean, timestamped reports without duplication

import json
import os
from pathlib import Path
from datetime import datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from bs4 import BeautifulSoup

# Define constants
REPORTS_DIR = Path("accessibility_reports")

def clean_url_for_filename(url):
    """Create a clean, consistent filename-safe version of a URL"""
    # Remove protocol
    clean_url = url.lower().replace('http://', '').replace('https://', '')
    
    # Remove www
    clean_url = clean_url.replace('www.', '')
    
    # Remove trailing slash
    clean_url = clean_url.rstrip('/')
    
    # Replace characters that aren't filename-safe
    clean_url = re.sub(r'[^a-z0-9\-_]', '_', clean_url)
    
    # Limit length to avoid overly long filenames
    if len(clean_url) > 30:
        clean_url = clean_url[:30]
    
    return clean_url

def get_webdriver(browser='chrome'):
    """Get a webdriver instance for the specified browser"""
    if browser.lower() == 'chrome':
        service = ChromeService()
        driver = webdriver.Chrome(service=service)
    elif browser.lower() == 'firefox':
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)
    elif browser.lower() == 'edge':
        service = EdgeService()
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}. Use 'chrome', 'firefox', or 'edge'.")
    
    return driver

def generate_tab_order_report(url, browser='chrome'):
    """Generate a fresh tab order report for the given URL"""
    print(f"Generating tab order report for {url}...")
    
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Use BeautifulSoup to parse the page
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all potentially focusable elements
        elements = soup.find_all(['a', 'button', 'input', 'textarea', 'select'])
        
        # Extract relevant information
        tab_order_data = []
        tab_order_issues = []
        
        for idx, elem in enumerate(elements, 1):
            # Extract text (limited to reasonable length)
            text = elem.get_text().strip()[:50] if elem.get_text() else "[No text]"
            
            # Handle input elements specially
            if elem.name == 'input' and not text:
                if elem.has_attr('placeholder'):
                    text = f"[Input: {elem['placeholder'][:30]}]"
                elif elem.has_attr('name'):
                    text = f"[Input: {elem['name'][:30]}]"
            
            # Create element detail
            element_detail = {
                'index': idx,
                'type': elem.name,
                'text': text,
                'tabindex': elem.get('tabindex')
            }
            
            # Add ID and class if available
            if elem.has_attr('id'):
                element_detail['id'] = elem['id']
            if elem.has_attr('class'):
                element_detail['class'] = ' '.join(elem['class']) if isinstance(elem['class'], list) else elem['class']
            
            tab_order_data.append(element_detail)
        
        # Find tab order issues
        for i in range(len(tab_order_data) - 1):
            current = tab_order_data[i]
            next_elem = tab_order_data[i + 1]
            
            # Check for tabindex issues (non-sequential or negative)
            if (current.get('tabindex') is not None and next_elem.get('tabindex') is not None 
                and int(current['tabindex']) >= int(next_elem['tabindex'])):
                issue = f"Tab order issue: Element {current['index']} (tabindex={current['tabindex']}) comes before Element {next_elem['index']} (tabindex={next_elem['tabindex']})"
                tab_order_issues.append(issue)
        
        # Prepare the report data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = clean_url_for_filename(url)
        page_title_snippet = clean_url_for_filename(driver.title)[:20]
        
        report_data = {
            'url': url,
            'page_title': driver.title,
            'timestamp': datetime.now().isoformat(),
            'browser': browser,
            'tab_order_elements': [
                f"{elem['index']}: {elem['type']} - {elem['text']}" 
                for elem in tab_order_data
            ],
            'tab_order_details': tab_order_data,
            'tab_order_issues': tab_order_issues,
            'summary': {
                'total_elements': len(tab_order_data),
                'issue_count': len(tab_order_issues)
            }
        }
        
        # Create a unique filename with timestamp and URL snippet
        filename = f"tab_order_{clean_url}_{page_title_snippet}_{timestamp}.json"
        filepath = REPORTS_DIR / filename
        
        # Ensure directory exists
        REPORTS_DIR.mkdir(exist_ok=True)
        
        # Write the report to a file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"Tab order report saved to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"Error generating tab order report: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    finally:
        if 'driver' in locals():
            driver.quit()

def generate_missing_focusable_report(url, browser='chrome'):
    """Generate a fresh missing focusable elements report"""
    print(f"Generating missing focusable elements report for {url}...")
    
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Use JavaScript to find visually interactive elements
        js_script = """
        function findInteractiveElements() {
            // Find elements with cursor: pointer style
            const pointerElements = Array.from(document.querySelectorAll('*')).filter(el => {
                const style = window.getComputedStyle(el);
                return style.cursor === 'pointer' && el.offsetParent !== null;
            });
            
            // Find elements with click handlers
            const clickableElements = Array.from(document.querySelectorAll('[onclick], [onmousedown], [onmouseup]'));
            
            // Find elements with common interactive classes
            const classElements = Array.from(document.querySelectorAll('.btn, .button, [class*="btn-"], [class*="button"], .clickable, [class*="clickable"]'));
            
            // Combine and deduplicate
            const allElements = [...new Set([...pointerElements, ...clickableElements, ...classElements])];
            
            // Get basic info about each element
            return allElements.map(el => {
                return {
                    tagName: el.tagName.toLowerCase(),
                    id: el.id || '',
                    className: el.className || '',
                    text: el.textContent.trim().substring(0, 50),
                    isInTabOrder: el.tagName === 'A' || el.tagName === 'BUTTON' || 
                                  (el.tagName === 'INPUT' && el.type !== 'hidden') ||
                                  el.tagName === 'SELECT' || el.tagName === 'TEXTAREA' ||
                                  el.tabIndex >= 0
                };
            });
        }
        
        return findInteractiveElements();
        """
        
        interactive_elements = driver.execute_script(js_script)
        
        # Filter for elements that appear interactive but aren't in tab order
        missing_focusable = [elem for elem in interactive_elements if not elem['isInTabOrder']]
        
        # Format issues
        missing_focusable_issues = []
        for i, elem in enumerate(missing_focusable, 1):
            tag = elem['tagName']
            text = elem['text'] or "[No text]"
            id_class = f" id='{elem['id']}'" if elem['id'] else ""
            id_class += f" class='{elem['className']}'" if elem['className'] else ""
            
            issue = f"Element {i}: <{tag}{id_class}> {text} appears interactive but is not keyboard accessible"
            missing_focusable_issues.append({
                "issue": issue,
                "element_info": elem,
                "impact": "High" if tag in ['div', 'span'] and ('btn' in elem['className'].lower() or 'button' in elem['className'].lower()) else "Medium",
                "recommendation": "Add tabindex='0' and appropriate keyboard event handlers."
            })
        
        # Prepare the report data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = clean_url_for_filename(url)
        page_title_snippet = clean_url_for_filename(driver.title)[:20]
        
        report_data = {
            'url': url,
            'page_title': driver.title,
            'timestamp': datetime.now().isoformat(),
            'browser': browser,
            'missing_focusable_elements': missing_focusable,
            'missing_focusable_issues': missing_focusable_issues,
            'summary': {
                'total_interactive': len(interactive_elements),
                'total_missing_focusable': len(missing_focusable),
                'issue_count': len(missing_focusable_issues)
            }
        }
        
        # Create a unique filename with timestamp and URL snippet
        filename = f"missing_focusable_{clean_url}_{page_title_snippet}_{timestamp}.json"
        filepath = REPORTS_DIR / filename
        
        # Ensure directory exists
        REPORTS_DIR.mkdir(exist_ok=True)
        
        # Write the report to a file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"Missing focusable report saved to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"Error generating missing focusable report: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    finally:
        if 'driver' in locals():
            driver.quit()

def generate_comprehensive_report(url, browser='chrome'):
    """Generate a comprehensive accessibility report"""
    print(f"Generating comprehensive accessibility report for {url}...")
    
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Check for ARIA issues
        aria_issues = []
        
        # Find images without alt text
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        images = soup.find_all('img')
        for i, img in enumerate(images, 1):
            if not img.has_attr('alt'):
                src = img.get('src', '[no src]')[:50]
                aria_issues.append(f"Image {i} missing alt attribute: {src}")
        
        # Find form elements without labels
        form_elements = soup.find_all(['input', 'textarea', 'select'])
        for i, elem in enumerate(form_elements, 1):
            # Skip hidden inputs
            if elem.get('type') == 'hidden':
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
            
            if not has_label:
                elem_type = elem.get('type', elem.name)
                elem_name = elem.get('name', '[no name]')
                if elem.has_attr('placeholder'):
                    aria_issues.append(f"Form element {i} ({elem_type}: {elem_name}) has placeholder but no proper label")
                else:
                    aria_issues.append(f"Form element {i} ({elem_type}: {elem_name}) has no label")
        
        # Check for proper heading structure
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if headings:
            # Check if H1 exists
            h1_count = len(soup.find_all('h1'))
            if h1_count == 0:
                aria_issues.append("Page has no H1 heading")
            elif h1_count > 1:
                aria_issues.append(f"Page has {h1_count} H1 headings (should typically have only one)")
            
            # Check for heading level skips
            level_order = []
            for heading in headings:
                level = int(heading.name[1])
                level_order.append(level)
            
            for i in range(len(level_order) - 1):
                if level_order[i+1] > level_order[i] + 1:
                    aria_issues.append(f"Heading hierarchy skips from h{level_order[i]} to h{level_order[i+1]}")
        else:
            aria_issues.append("Page has no heading elements")
        
        # Check for landmark roles
        has_main = bool(soup.find(attrs={'role': 'main'}) or soup.find('main'))
        has_nav = bool(soup.find(attrs={'role': 'navigation'}) or soup.find('nav'))
        has_banner = bool(soup.find(attrs={'role': 'banner'}) or soup.find('header'))
        
        if not has_main:
            aria_issues.append("Page missing main content landmark (role='main' or <main>)")
        if not has_nav:
            aria_issues.append("Page missing navigation landmark (role='navigation' or <nav>)")
        if not has_banner:
            aria_issues.append("Page missing banner/header landmark (role='banner' or <header>)")
        
        # Check keyboard navigation issues
        keyboard_issues = []
        
        # Find visually focused elements with no visible focus indicator using JavaScript
        js_script = """
        function checkFocusIndicators() {
            const issues = [];
            const focusableElements = document.querySelectorAll('a[href], button, input:not([type="hidden"]), select, textarea, [tabindex]:not([tabindex="-1"])');
            
            for (let i = 0; i < focusableElements.length; i++) {
                const el = focusableElements[i];
                const originalOutline = el.style.outline;
                const originalBoxShadow = el.style.boxShadow;
                
                // Focus the element
                el.focus();
                
                // Get computed style
                const style = window.getComputedStyle(el);
                
                // Check if focus is visibly indicated
                if (style.outline === 'none' || style.outline === '0px none' || 
                    style.outline === originalOutline) {
                    if (style.boxShadow === 'none' || style.boxShadow === originalBoxShadow) {
                        // Element has no visible focus indicator
                        issues.push({
                            tagName: el.tagName.toLowerCase(),
                            id: el.id || '',
                            className: el.className || '',
                            text: el.textContent.trim().substring(0, 50)
                        });
                    }
                }
                
                // Restore original state
                el.blur();
            }
            
            return issues;
        }
        
        return checkFocusIndicators();
        """
        
        try:
            focus_issues = driver.execute_script(js_script)
            for i, elem in enumerate(focus_issues, 1):
                tag = elem['tagName']
                text = elem['text'] or "[No text]"
                id_info = f" id='{elem['id']}'" if elem['id'] else ""
                keyboard_issues.append(f"Element {i}: <{tag}{id_info}> {text} has no visible focus indicator")
        except Exception as js_error:
            keyboard_issues.append(f"Error checking focus indicators: {str(js_error)}")
        
        # Prepare the report data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = clean_url_for_filename(url)
        page_title_snippet = clean_url_for_filename(driver.title)[:20]
        
        report_data = {
            'url': url,
            'page_title': driver.title,
            'timestamp': datetime.now().isoformat(),
            'browser': browser,
            'aria_issues': aria_issues,
            'keyboard_issues': keyboard_issues,
            'summary': {
                'aria_issue_count': len(aria_issues),
                'keyboard_issue_count': len(keyboard_issues),
                'total_issues': len(aria_issues) + len(keyboard_issues)
            }
        }
        
        # Create a unique filename with timestamp and URL snippet
        filename = f"comprehensive_{clean_url}_{page_title_snippet}_{timestamp}.json"
        filepath = REPORTS_DIR / filename
        
        # Ensure directory exists
        REPORTS_DIR.mkdir(exist_ok=True)
        
        # Write the report to a file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"Comprehensive report saved to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"Error generating comprehensive report: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    finally:
        if 'driver' in locals():
            driver.quit()

def run_all_reports(url, browser='chrome'):
    """Run all accessibility reports for a URL"""
    print(f"Running all accessibility reports for {url} using {browser}...")
    
    # Ensure reports directory exists
    REPORTS_DIR.mkdir(exist_ok=True)
    
    # Run tab order report
    tab_order_file = generate_tab_order_report(url, browser)
    
    # Run missing focusable report
    missing_focusable_file = generate_missing_focusable_report(url, browser)
    
    # Run comprehensive report
    comprehensive_file = generate_comprehensive_report(url, browser)
    
    print("\n" + "=" * 60)
    print(f"Accessibility reports generated for {url}")
    print("=" * 60)
    
    if tab_order_file:
        print(f"Tab Order Report: {tab_order_file}")
    
    if missing_focusable_file:
        print(f"Missing Focusable Report: {missing_focusable_file}")
    
    if comprehensive_file:
        print(f"Comprehensive Report: {comprehensive_file}")
    
    print("=" * 60)

# Run this script directly to test
if __name__ == "__main__":
    test_url = "https://www.sse.com"  # Change to your target website
    browser_choice = "firefox"  # Change to your preferred browser
    
    run_all_reports(test_url, browser_choice)
```
## Fresh_Reports <a id='Fresh_Reports'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 18:31:51
- **Size**: 810 bytes

### Code
#### Cell 1
```python
test_url = "https://www.sse.com"  # Your target website
browser_choice = "firefox"  # Your preferred browser

run_all_reports(test_url, browser_choice)
```
## Script_Extract <a id='Script_Extract'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 18:32:25
- **Size**: 337 bytes

### Code
#### Cell 1
```python

```