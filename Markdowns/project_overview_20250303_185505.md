# Project Scripts Overview
*Generated on 2025-03-03 18:55:05 from folder: C:\Users\clint\Pickles*
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
- **Last Modified**: 2025-03-03 18:55:01
- **Size**: 17028 bytes

### Code
#### Cell 1
```python
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
        "keyboard_issues": [],
        "code_snippets": {}
    }
    
    # Load data from JSON reports
    try:
        # Load tab order data
        tab_files = list(REPORTS_DIR.glob(f"tab_order_{clean_url}_*.json"))
        if tab_files:
            latest_tab = max(tab_files, key=lambda p: p.stat().st_mtime)
            with open(latest_tab, 'r') as f:
                tab_data = json.load(f)
                data["tab_order"] = tab_data.get("tab_order_data", [])
                data["tab_issues"] = tab_data.get("tab_order_issues", [])
                
        # Load missing focusable data
        missing_files = list(REPORTS_DIR.glob(f"missing_focusable_{clean_url}_*.json"))
        if missing_files:
            latest_missing = max(missing_files, key=lambda p: p.stat().st_mtime)
            with open(latest_missing, 'r') as f:
                missing_data = json.load(f)
                data["missing_elements"] = missing_data.get("missing_focusable_issues", [])
        
        # Load comprehensive data for ARIA and keyboard issues
        comp_files = list(REPORTS_DIR.glob(f"comprehensive_{clean_url}_*.json"))
        if comp_files:
            latest_comp = max(comp_files, key=lambda p: p.stat().st_mtime)
            with open(latest_comp, 'r') as f:
                comp_data = json.load(f)
                data["aria_issues"] = comp_data.get("aria_issues", [])
                data["keyboard_issues"] = comp_data.get("keyboard_issues", [])
        
        # Load relevant code snippets if available
        snippets_file = REPORTS_DIR / f"code_snippets_{clean_url}.json"
        if snippets_file.exists():
            with open(snippets_file, 'r') as f:  
                data["code_snippets"] = json.load(f)

    except Exception as e:
        print(f"Error loading data: {e}")
        import traceback
        traceback.print_exc()
        
    return data

def generate_html_report(data, output_path=None):
    """Generate an accessibility report with more valuable insights for auditors."""
    # Prepare output path
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = normalize_url(data.get("url", "unknown"))
        output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
    
    # Extract data variables
    url = data.get("url", "Unknown URL")
    timestamp = data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  
    tab_order = data.get("tab_order", [])
    tab_issues = data.get("tab_issues", [])
    missing_elements = data.get("missing_elements", [])
    aria_issues = data.get("aria_issues", [])
    keyboard_issues = data.get("keyboard_issues", [])
    code_snippets = data.get("code_snippets", {})
    
    # Generate the HTML report
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Accessibility Report - {url}</title>
        <style>
            /* CSS styles */
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
        
        <main class="container">
            
            <section class="section">
                <h2>Summary</h2>
                <div class="summary">
                    <div class="summary-item">
                        <div class="summary-number">{len(missing_elements)}</div>
                        <div>Potentially Focusable Elements</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-number">{len(tab_issues)}</div>
                        <div>Tab Order Sequence Issues</div>
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
            </section>
            
            <section class="section">
                <h2>Potentially Focusable Elements</h2>
    '''
    
    if missing_elements:
        html += '''
                <p>The following elements appear to be interactive but are not fully accessible with the keyboard:</p>
        '''
        for element in missing_elements:
            html += f'<div class="issue">{element}</div>'
        
        html += '''
                <p>Please manually verify if these elements should be reachable with the Tab key and provide proper keyboard support.</p>
                <p>Note: Some elements might be intentionally removed from the tab order or hidden for valid design reasons.</p>
        '''
    else:
        html += '''
                <p>No potentially focusable elements were found that lack full keyboard support. Great work!</p>
                <p>Keep in mind that some elements might be dynamically added or removed from the tab order with JavaScript.</p>
        '''
    
    if 'focusable_code' in code_snippets:
        html += f'''
                <div class="code-snippet">
                    <h3>Relevant Code Snippet</h3>
                    <pre><code>{code_snippets['focusable_code']}</code></pre>
                </div>
        '''
        
    html += '</section>'
    
    html += '''
            <section class="section">
                <h2>Tab Order Sequence Issues</h2>
    '''
    
    if tab_issues:
        html += '''
                <p>The following issues were detected with the tab order sequence:</p>
        '''
        for issue in tab_issues:
            html += f'<div class="issue tab-order">{issue}</div>'
        
        html += '''
                <p>Please review these elements and ensure the tab order follows a logical and intuitive sequence.</p>
                <p>Be aware that dynamic content updates, such as sliders or accordions, might affect the tab order.</p>
        '''
    else:
        html += '''
                <p>No issues found with the tab order sequence. The keyboard navigation appears to follow a logical flow.</p>
                <p>Remember to test the tab order manually, especially for dynamic content and custom controls.</p>
        '''
    
    if 'tab_order_code' in code_snippets:
        html += f'''
                <div class="code-snippet">
                    <h3>Relevant Code Snippet</h3>
                    <pre><code>{code_snippets['tab_order_code']}</code></pre>
                </div>
        '''
        
    html += '</section>'
    
    html += '''  
            <section class="section">
                <h2>ARIA and Semantic HTML Issues</h2>
    '''
    
    if aria_issues:
        html += '''
                <p>The following issues were found with ARIA attributes and semantic HTML elements:</p>
        '''
        for issue in aria_issues:
            html += f'<div class="issue aria">{issue}</div>'
        
        html += '''    
                <p>Address these issues to ensure proper accessibility for users of assistive technologies.</p>
                <p>Refer to the <a href="https://www.w3.org/TR/wai-aria-practices/" target="_blank">WAI-ARIA Authoring Practices</a> for guidance on correct ARIA usage.</p>
        '''
    else:
        html += '''
                <p>No issues detected with ARIA attributes or semantic HTML elements. Excellent!</p>  
                <p>Remember to use semantic HTML whenever possible and only use ARIA when necessary to supplement native semantics.</p>
        '''
    
    if 'aria_code' in code_snippets:
        html += f'''
                <div class="code-snippet">
                    <h3>Relevant Code Snippet</h3>
                    <pre><code>{code_snippets['aria_code']}</code></pre>
                </div>
        '''
        
    html += '</section>'
    
    html += '''
            <section class="section">
                <h2>Keyboard Navigation Issues</h2>
    '''
    
    if keyboard_issues:
        html += '''
                <p>The following issues were found with keyboard navigation:</p>
        '''
        for issue in keyboard_issues:
            html += f'<div class="issue keyboard">{issue}</div>'
        
        html += '''
                <p>Ensure that all interactive elements are reachable and operable with the keyboard alone.</p>
                <p>Pay special attention to custom controls, complex widgets, and dynamically updated content.</p>
        '''
    else:
        html += '''  
                <p>No keyboard navigation issues found. All interactive elements appear to be reachable and operable with the keyboard.</p>
                <p>Continue to test keyboard support thoroughly, especially for any custom widgets or controls.</p>
        '''
    
    if 'keyboard_code' in code_snippets:
        html += f'''
                <div class="code-snippet">
                    <h3>Relevant Code Snippet</h3>  
                    <pre><code>{code_snippets['keyboard_code']}</code></pre>
                </div>
        '''
        
    html += '</section>'
    
    # Tab Order Elements Sample
    if tab_order:
        html += '''
            <section class="section">
                <h2>Tab Order Sequence Sample</h2>
                <p>First few elements in the tab order sequence:</p>
        '''
        for i, element in enumerate(tab_order[:5], 1):
            html += f'<div class="issue tab-order">{i}. {element}</div>'
        
        if len(tab_order) > 5:
            html += f'<p>...and {len(tab_order) - 5} more elements in the tab order.</p>'
        
        html += '''
                <p>Please verify the tab order manually with the keyboard to ensure a logical navigation flow.</p>
            </section>
        '''
        
    html += '''
        </main>
        
        <footer>
            <div class="container">
                <p>This accessibility report was generated by the Accessibility Checker Tool.</p>
                <p>For more information, visit <a href="https://www.w3.org/WAI/standards-guidelines/wcag/" target="_blank">Web Content Accessibility Guidelines (WCAG)</a>.</p>
            </div>
        </footer>
        
    </body>
    </html>
    '''
    
    # Save HTML report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Accessibility report saved to: {output_path}")
    return str(output_path)

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
        print(f"Accessibility report generated successfully!")
        print(f"Report saved to: {os.path.abspath(report_path)}")  
        print(f"{'='*60}")
    else:
        print(f"Failed to generate accessibility report")

if __name__ == "__main__":
    website_url = "https://www.example.com"  # Replace with the target website URL
    generate_accessibility_report(website_url)
```
#### Cell 2
```python

```
## Fresh_JSON_Reports <a id='Fresh_JSON_Reports'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 18:37:03
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
- **Last Modified**: 2025-03-03 18:37:06
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
- **Last Modified**: 2025-03-03 18:37:09
- **Size**: 4524 bytes

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