# Project Scripts Overview
*Generated on 2025-03-03 19:37:43 from folder: C:\Users\clint\Pickles*
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
- [Fresh_Accessibility_Report.ipynb](#Fresh_Accessibility_Report.ipynb)
- [Fresh_JSON_Reports](#Fresh_JSON_Reports)
- [Fresh_Reports](#Fresh_Reports)
- [Script_Extract](#Script_Extract)

## Fresh_Accessibility_Report.ipynb <a id='Fresh_Accessibility_Report.ipynb'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 19:27:03
- **Size**: 23577 bytes

### Code
#### Cell 1
```python
import json
import os
import uuid
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus

# Define constants
REPORTS_DIR = Path("accessibility_reports")

# Ensure reports directory exists
REPORTS_DIR.mkdir(exist_ok=True)

def translate_accessibility_issue(original_issue, category):
    """
    Translate technical issue descriptions into user-impact statements.
    
    Args:
        original_issue (str): The original technical issue description
        category (str): The category of the issue (Tab Order, Missing Focusable, etc.)
    
    Returns:
        dict: A more descriptive and user-focused issue description
    """
    translations = {
        # Tab Order Issues
        "comes before": {
            "description": "Keyboard navigation sequence is unpredictable, potentially disorienting for users relying on sequential keyboard navigation",
            "impact": "Users navigating with keyboard may struggle to understand the logical flow of interactive elements",
            "recommendation": "Review and adjust tabindex values to ensure a clear, logical tab order"
        },
        
        # Missing Focusable Issues
        "Keyboard navigation barrier": {
            "description": lambda issue: (
                f"'{issue.split(':')[1].strip()}' is visually interactive but not keyboard accessible, "
                "creating a navigation barrier for keyboard-only and assistive technology users"
            ),
            "impact": "Users who cannot use a mouse are prevented from accessing or interacting with this element",
            "recommendation": "Add tabindex='0' and ensure the element can be activated with keyboard events"
        },
        
        # ARIA Issues
        "missing alt": {
            "description": lambda issue: f"Image {issue.split(':')[1].strip()} lacks alternative text, preventing screen reader users from understanding its content",
            "impact": "Users relying on screen readers cannot interpret the image's meaning or context",
            "recommendation": "Add descriptive alt text that conveys the image's purpose or content"
        },
        
        # Keyboard Navigation Issues
        "no visible focus indicator": {
            "description": "Interactive element lacks a clear visual focus indicator, making keyboard navigation difficult to track",
            "impact": "Users navigating with keyboard cannot easily determine their current position on the page",
            "recommendation": "Add a clear, high-contrast focus outline that meets WCAG contrast requirements"
        },
        
        # Default fallback
        "default": {
            "description": lambda issue: f"Accessibility barrier detected in {category}: {issue}",
            "impact": "Potential difficulty for users with assistive technologies",
            "recommendation": "Manually review and address the accessibility concern"
        }
    }
    
    # Attempt to match and translate the issue
    for key, translation in translations.items():
        if key in original_issue.lower():
            try:
                if callable(translation['description']):
                    description = translation['description'](original_issue)
                else:
                    description = translation['description']
                
                return {
                    'original': original_issue,
                    'category': category,
                    'description': description,
                    'impact': translation['impact'],
                    'recommendation': translation['recommendation']
                }
            except Exception:
                # Fallback to default if specific translation fails
                return translations['default']
    
    # Fallback for completely unmatched issues
    default_translation = translations['default']
    return {
        'original': original_issue,
        'category': category,
        'description': default_translation['description'](original_issue),
        'impact': default_translation['impact'],
        'recommendation': default_translation['recommendation']
    }

def determine_severity(issue_text):
    """
    Determine severity based on issue description.
    
    Args:
        issue_text (str): Description of the accessibility issue
    
    Returns:
        str: Severity level (critical, high, medium, low)
    """
    severity_keywords = {
        'critical': [
            'completely inaccessible', 'impossible to use', 'blocking', 
            'cannot access at all', 'severe barrier'
        ],
        'high': [
            'significant barrier', 'major impact', 'substantial difficulty', 
            'prevents key functionality', 'critical user flow'
        ],
        'medium': [
            'moderate impact', 'some difficulty', 'partial barrier', 
            'intermittent issue', 'usable with significant effort'
        ],
        'low': [
            'minor issue', 'slight inconvenience', 'cosmetic', 
            'minimal impact', 'negligible barrier'
        ]
    }
    
    # Convert issue text to lowercase for case-insensitive matching
    lower_issue = issue_text.lower()
    
    # Check for severity keywords
    for severity, keywords in severity_keywords.items():
        if any(keyword in lower_issue for keyword in keywords):
            return severity
    
    # Default to medium severity if no specific keywords are found
    return 'medium'

class AccessibilityIssue:
    """
    Represents a single accessibility issue with enhanced tracking capabilities.
    """
    def __init__(self, description, category, severity='medium'):
        self.id = str(uuid.uuid4())  # Unique identifier for the issue
        self.description = description
        self.category = category
        self.severity = severity
        self.tags = self._generate_tags()
        
    def _generate_tags(self):
        """
        Generate recommended tags based on issue description and category.
        """
        base_tags = [self.category, self.severity]
        
        # Specific tag generation logic
        if 'ARIA' in self.description:
            base_tags.append('aria')
        if 'keyboard' in self.description.lower():
            base_tags.append('keyboard-nav')
        if 'focusable' in self.description.lower():
            base_tags.append('focusable')
        
        return base_tags
    
    def get_jira_ticket_url(self):
        """
        Generate a Jira ticket creation URL.
        """
        base_url = 'https://your-org.atlassian.net/secure/CreateIssueRedirect.jspa'
        params = {
            'pid': '',  # Project ID
            'issuetype': '',  # Issue Type ID
            'summary': f"Accessibility Issue: {self.description[:100]}",
            'description': (
                f"*Issue ID*: {self.id}\n"
                f"*Category*: {self.category}\n"
                f"*Severity*: {self.severity}\n"
                f"*Description*: {self.description}\n\n"
                "h3. Recommended Actions:\n"
                "- Verify the accessibility issue\n"
                "- Develop a remediation plan\n"
                "- Test proposed solution\n"
            )
        }
        
        # URL encode parameters
        encoded_params = '&'.join([f"{k}={quote_plus(str(v))}" for k, v in params.items() if v])
        return f"{base_url}?{encoded_params}"
    
    def get_github_issue_url(self):
        """
        Generate a GitHub issue creation URL.
        """
        base_url = 'https://github.com/your-org/your-repo/issues/new'
        params = {
            'title': f"Accessibility Issue: {self.description[:100]}",
            'body': (
                f"## Accessibility Issue Details\n"
                f"- **Issue ID**: `{self.id}`\n"
                f"- **Category**: {self.category}\n"
                f"- **Severity**: {self.severity}\n\n"
                f"### Description\n"
                f"{self.description}\n\n"
                "### Recommended Actions\n"
                "- [ ] Verify the accessibility issue\n"
                "- [ ] Develop a remediation plan\n"
                "- [ ] Test proposed solution\n"
            )
        }
        
        # URL encode parameters
        encoded_params = '&'.join([f"{k}={quote_plus(str(v))}" for k, v in params.items() if v])
        return f"{base_url}?{encoded_params}"

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
    """Load accessibility data for a given URL"""
    clean_url = normalize_url(url)
    data = {
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issues": []
    }
    
    # Existing data loading logic
    try:
        # Load data from various report files
        report_types = [
            ("tab_order", f"tab_order_{clean_url}_*.json"),
            ("missing_focusable", f"missing_focusable_{clean_url}_*.json"),
            ("comprehensive", f"comprehensive_{clean_url}_*.json")
        ]
        
        found_data = False
        for report_type, pattern in report_types:
            files = list(REPORTS_DIR.glob(pattern))
            if files:
                latest_file = max(files, key=lambda p: p.stat().st_mtime)
                with open(latest_file, 'r') as f:
                    report_data = json.load(f)
                    
                    # Define issue_sources
                    issue_sources = {
                        "Tab Order": report_data.get("tab_order_issues", []),
                        "Missing Focusable": report_data.get("missing_focusable_issues", []),
                        "ARIA": report_data.get("aria_issues", []),
                        "Keyboard": report_data.get("keyboard_issues", [])
                    }
                    
                    for category, issues in issue_sources.items():
                        for issue_text in issues:
                            found_data = True
                            if isinstance(issue_text, dict):
                                issue_text = issue_text.get('issue', str(issue_text))
                            
                            # Translate the issue to a more descriptive format
                            translated_issue = translate_accessibility_issue(issue_text, category)
                            
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
            print(f"Warning: No accessibility reports found for {url}")
    
    except Exception as e:
        print(f"Error loading data: {e}")
        import traceback
        traceback.print_exc()
    
    return data

def generate_html_report(data, output_path=None):
    """
    Generate an advanced HTML report with issue tracking integration
    """
    # Prepare output path
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = normalize_url(data.get("url", "unknown"))
        output_path = REPORTS_DIR / f"accessibility_report_{clean_url}_{timestamp}.html"
    
    # Prepare issue categorization
    categorized_issues = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }
    
    for issue in data.get("issues", []):
        categorized_issues[issue.severity].append(issue)
    
    # HTML Generation with Issue Tracking Features
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Accessibility Report - {data.get('url', 'Unknown Site')}</title>
        <style>
            :root {{
                --critical-color: #dc3545;
                --high-color: #fd7e14;
                --medium-color: #ffc107;
                --low-color: #28a745;
            }}
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            .summary {{
                display: flex;
                justify-content: space-between;
                background-color: #f4f4f4;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .issue-list {{ margin-bottom: 20px; }}
            .issue {{
                padding: 15px;
                margin: 10px 0;
                border-left: 5px solid;
                background-color: #fff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .issue.critical {{
                border-left-color: var(--critical-color);
                background-color: #ffebee;
            }}
            .issue.high {{
                border-left-color: var(--high-color);
                background-color: #fff3e0;
            }}
            .issue.medium {{
                border-left-color: var(--medium-color);
                background-color: #fffde7;
            }}
            .issue.low {{
                border-left-color: var(--low-color);
                background-color: #e8f5e9;
            }}
            .issue-details {{
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .issue-actions {{
                display: flex;
                gap: 10px;
            }}
            .issue-actions a {{
                text-decoration: none;
                padding: 5px 10px;
                border-radius: 3px;
                background-color: #007bff;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>Accessibility Report for {data.get('url', 'Unknown Site')}</h1>
        <p>Generated on: {data.get('timestamp', 'Unknown Date')}</p>
        
        <div class="summary">
            <div>Critical Issues: {len(categorized_issues['critical'])}</div>
            <div>High Priority Issues: {len(categorized_issues['high'])}</div>
            <div>Medium Priority Issues: {len(categorized_issues['medium'])}</div>
            <div>Low Priority Issues: {len(categorized_issues['low'])}</div>
        </div>
    """
    
    # Generate sections for each severity level
    severity_order = ['critical', 'high', 'medium', 'low']
    for severity in severity_order:
        issues = categorized_issues[severity]
        if issues:
            html += f"""
            <h2>{severity.capitalize()} Priority Issues</h2>
            <div class="issue-list">
                {''.join([f'''
                <div class="issue {severity}">
                    <div class="issue-details">
                        <div>
                            <strong>{issue.category}:</strong> {issue.description}
                            <br>
                            <small><em>Impact: {getattr(issue, 'impact', 'Not specified')}</em></small>
                            <br>
                            <small><em>Recommendation: {getattr(issue, 'recommendation', 'No specific recommendation')}</em></small>
                        </div>
                        <div class="issue-actions">
                            <a href="{issue.get_jira_ticket_url()}" target="_blank">Create Jira Ticket</a>
                            <a href="{issue.get_github_issue_url()}" target="_blank">Create GitHub Issue</a>
                        </div>
                    </div>
                </div>
                ''' for issue in issues])}
            </div>
            """
    
    html += """
    </body>
    </html>
    """
    
    # Save the report
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
    website_url = "https://www.sse.com"  # Replace with the target website URL
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
        
        # Find Inconsistent keyboard navigation sequences
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
- **Last Modified**: 2025-03-03 19:16:13
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