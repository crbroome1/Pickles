# Project Scripts Overview
*Generated on 2025-03-03 21:06:55 from folder: C:\Users\clint\Pickles*
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
- [Data_Loader](#Data_Loader)
- [Enhanced_Report_Generator2](#Enhanced_Report_Generator2)
- [Fresh_Accessibility_Report](#Fresh_Accessibility_Report)
- [Fresh_Accessibility_Report.ipynb](#Fresh_Accessibility_Report.ipynb)
- [Fresh_JSON_Reports](#Fresh_JSON_Reports)
- [Fresh_Reports](#Fresh_Reports)
- [Missing_Focusable_Elements](#Missing_Focusable_Elements)
- [Script_Extract](#Script_Extract)

## Accessibility_Checker <a id='Accessibility_Checker'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:02:07
- **Size**: 16892 bytes

### Code
#### Cell 1
```python
# Accessibility_Checker.ipynb

import sys
import os
from pathlib import Path
import json
import uuid
import re
import time
from datetime import datetime
from urllib.parse import quote_plus

# Add the project directory to the path so we can import our modules
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Create config directory for reports and settings
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)
print(f"📁 Reports will be saved in: {REPORTS_DIR.absolute()}")

class AccessibilityTerminology:
    """Manages consistent accessibility terminology across the project"""
    
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = Path(terminology_file)
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """Load or create a default terminology mapping."""
        if self.terminology_file.exists():
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
    
    def translate_term(self, text):
        """Replace technical terms with more descriptive language."""
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = re.sub(
                    re.escape(technical_term), 
                    replacement['preferred'], 
                    text, 
                    flags=re.IGNORECASE
                )
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """Update the terminology mapping."""
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)
            
    def get_explanation(self, term):
        """Get the explanation for a term if it exists"""
        for tech_term, details in self.terminology['technical_terms'].items():
            if term.lower() == details['preferred'].lower():
                return details['explanation']
        return None

class AccessibilityIssue:
    """Represents a single accessibility issue with enhanced tracking capabilities."""
    
    def __init__(self, description, category, severity='medium'):
        self.id = str(uuid.uuid4())  # Unique identifier for the issue
        self.description = description
        self.category = category
        self.severity = severity
        self.tags = self._generate_tags()
        
    def _generate_tags(self):
        """Generate recommended tags based on issue description and category."""
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
        """Generate a Jira ticket creation URL."""
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
        """Generate a GitHub issue creation URL."""
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

def translate_accessibility_issue(original_issue, category, terminology):
    """
    Translate technical issue descriptions into user-impact statements.
    
    Args:
        original_issue (str): The original technical issue description
        category (str): The category of the issue (Tab Order, Missing Focusable, etc.)
        terminology: The terminology translator
    
    Returns:
        dict: A more descriptive and user-focused issue description
    """
    # First apply standard terminology translations
    issue_text = terminology.translate_term(original_issue)
    
    translations = {
        # Tab Order Issues
        "comes before": {
            "description": "Keyboard navigation sequence is unpredictable, potentially disorienting for users relying on sequential keyboard navigation",
            "impact": "Users navigating with keyboard may struggle to understand the logical flow of interactive elements",
            "recommendation": "Review and adjust tabindex values to ensure a clear, logical tab order"
        },
        
        # Missing Focusable Issues
        "keyboard navigation barrier": {
            "description": lambda issue: (
                f"'{issue.split(':')[1].strip() if ':' in issue else issue}' is visually interactive but not keyboard accessible, "
                "creating a navigation barrier for keyboard-only and assistive technology users"
            ),
            "impact": "Users who cannot use a mouse are prevented from accessing or interacting with this element",
            "recommendation": "Add tabindex='0' and ensure the element can be activated with keyboard events"
        },
        
        # ARIA Issues
        "missing alt": {
            "description": lambda issue: f"Image {issue.split(':')[1].strip() if ':' in issue else issue} lacks alternative text, preventing screen reader users from understanding its content",
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
        if key in issue_text.lower():
            try:
                if callable(translation['description']):
                    description = translation['description'](issue_text)
                else:
                    description = translation['description']
                
                return {
                    'original': original_issue,
                    'category': category,
                    'description': description,
                    'impact': translation['impact'],
                    'recommendation': translation['recommendation']
                }
            except Exception as e:
                print(f"Error translating issue: {e}")
                # Fallback to default if specific translation fails
                return translations['default']
    
    # Fallback for completely unmatched issues
    default_translation = translations['default']
    try:
        return {
            'original': original_issue,
            'category': category,
            'description': default_translation['description'](issue_text),
            'impact': default_translation['impact'],
            'recommendation': default_translation['recommendation']
        }
    except Exception as e:
        print(f"Error with default translation: {e}")
        return {
            'original': original_issue,
            'category': category,
            'description': f"Accessibility issue in {category}: {issue_text}",
            'impact': "Potential accessibility barrier for users",
            'recommendation': "Review and address the issue according to WCAG guidelines"
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

# Initialize the terminology manager
terminology = AccessibilityTerminology()
print(f"✅ Accessibility terminology loaded with {len(terminology.terminology['technical_terms'])} terms")

# Test the terminology replacement
test_issue = "Tab order issue: Element 5 comes before Element 3"
translated = terminology.translate_term(test_issue)
print(f"\nTest terminology replacement:")
print(f"Original: {test_issue}")
print(f"Translated: {translated}")

print("\n📋 Enhanced Accessibility Checker initialized and ready to use")
print("=" * 60)
```
## Data_Loader <a id='Data_Loader'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:00:58
- **Size**: 8976 bytes

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
from Accessibility_Checker import (
    REPORTS_DIR, 
    AccessibilityIssue, 
    normalize_url, 
    translate_accessibility_issue,
    determine_severity,
    terminology
)

def load_data(url):
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
    test_url = "https://www.sse.com"  # Replace with your target website
    
    print(f"Testing data loader with URL: {test_url}")
    data = load_data(test_url)
    
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
## Enhanced_Report_Generator2 <a id='Enhanced_Report_Generator2'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:03:20
- **Size**: 14148 bytes

### Code
#### Cell 1
```python
# Enhanced_Report_Generator.ipynb

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
        categorized_issues[
```
## Fresh_Accessibility_Report <a id='Fresh_Accessibility_Report'></a>
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
## Fresh_Accessibility_Report.ipynb <a id='Fresh_Accessibility_Report.ipynb'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 20:45:42
- **Size**: 46401 bytes

### Code
#### Cell 1
```python
import nbimport  # This must come first!
from enhanced_report_generator import generate_enhanced_html_report
import json
import os
import uuid
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus
# Remove this duplicate import
# from enhanced_report_generator import generate_enhanced_html_report

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
    report_path = generate_enhanced_html_report(data)
    
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
# Import system modules for path management
import sys
import os
# Add the current directory to the path if needed
sys.path.append('.')

# Try to import the enhanced version
try:
    from enhanced_report_generator import generate_enhanced_html_report
    print("Successfully imported enhanced report generator")
except ImportError as e:
    print(f"Could not import enhanced report generator: {e}")
    print("Falling back to standard report generator")
    # Define a fallback if import fails
    generate_enhanced_html_report = None

import json
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
    
    # Generate HTML report - using the enhanced version if available, otherwise fallback
    if generate_enhanced_html_report:
        print("Using enhanced HTML report generator")
        report_path = generate_enhanced_html_report(data)
    else:
        print("Using standard HTML report generator")
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
## Fresh_JSON_Reports <a id='Fresh_JSON_Reports'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 20:31:07
- **Size**: 40098 bytes

### Code
#### Cell 1
```python
# Enhanced JSON Report Generator
# Generates clean, timestamped reports without duplication
# Now with improved interactive element detection and keyboard accessibility validation

import json
import os
from pathlib import Path
from datetime import datetime
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser.lower() == 'firefox':
        service = FirefoxService()
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif browser.lower() == 'edge':
        service = EdgeService()
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}. Use 'chrome', 'firefox', or 'edge'.")
    
    # Set window size to ensure consistency
    driver.set_window_size(1366, 768)
    return driver

def is_truly_interactive(driver, element):
    """
    Comprehensively determine if an element is genuinely interactive and requires keyboard accessibility.
    
    Criteria for true interactivity:
    1. Natively focusable elements (links, buttons, inputs, etc.)
    2. Elements with explicit keyboard event listeners
    3. Elements with ARIA roles that imply interaction
    4. Elements with onclick/onkeydown/onkeyup events
    5. Dynamic elements with potential user interaction
    
    Args:
        driver: Selenium WebDriver instance
        element: Selenium WebElement to evaluate
    
    Returns:
        dict: Detailed assessment of the element's interactivity
    """
    # Native interactive elements
    native_interactive_tags = ['a', 'button', 'input', 'select', 'textarea']
    
    # ARIA roles that imply interaction
    interactive_aria_roles = [
        'button', 'link', 'menuitem', 'tab', 'checkbox', 
        'radio', 'switch', 'combobox', 'searchbox'
    ]
    
    # Gather element details
    tag_name = element.tag_name.lower()
    classes = element.get_attribute('class') or ''
    role = element.get_attribute('role')
    
    # Check for native interactive elements
    if tag_name in native_interactive_tags:
        return {
            'interactive': True,
            'reason': 'Native interactive element',
            'details': {
                'tag': tag_name,
                'native_interactive': True
            }
        }
    
    # Check ARIA role
    if role and role.lower() in interactive_aria_roles:
        return {
            'interactive': True,
            'reason': 'ARIA interactive role',
            'details': {
                'role': role,
                'aria_interactive': True
            }
        }
    
    # Check for dynamic event listeners
    try:
        # Use JavaScript to check for event listeners
        has_click_listener = element.get_attribute('onclick') is not None
        has_keyboard_listeners = (
            element.get_attribute('onkeydown') is not None or
            element.get_attribute('onkeyup') is not None or
            element.get_attribute('onkeypress') is not None
        )
        
        # Check for jQuery or other event binding
        try:
            has_events = driver.execute_script("""
                var element = arguments[0];
                // Check jQuery events if jQuery is available
                var hasJQueryEvents = typeof jQuery !== 'undefined' && 
                    jQuery && jQuery._data && jQuery._data(element, 'events') != null;
                
                // Check for native events
                var hasNativeEvents = false;
                try {
                    if (typeof getEventListeners === 'function') {
                        hasNativeEvents = Object.keys(getEventListeners(element) || {}).length > 0;
                    }
                } catch (e) {}
                
                return hasJQueryEvents || hasNativeEvents;
            """, element)
        except:
            has_events = False
        
        if has_click_listener or has_keyboard_listeners or has_events:
            return {
                'interactive': True,
                'reason': 'Dynamic event listeners detected',
                'details': {
                    'click_listener': has_click_listener,
                    'keyboard_listeners': has_keyboard_listeners,
                    'other_events': has_events
                }
            }
    except Exception:
        # Fallback to more basic checks if event detection fails
        pass
    
    # Check for specific interactive class patterns
    interactive_class_patterns = [
        'btn', 'button', 'clickable', 'interactive', 
        'dropdown', 'toggle', 'nav-link', 'menu-item'
    ]
    
    if any(pattern in classes.lower() for pattern in interactive_class_patterns):
        return {
            'interactive': True,
            'reason': 'Interactive class pattern',
            'details': {
                'classes': classes,
                'matched_patterns': [
                    pattern for pattern in interactive_class_patterns 
                    if pattern in classes.lower()
                ]
            }
        }
    
    # Compute style to check for cursor and visibility
    try:
        computed_style = driver.execute_script("""
            var style = window.getComputedStyle(arguments[0]);
            return {
                cursor: style.cursor,
                display: style.display,
                visibility: style.visibility
            };
        """, element)
        
        # Check cursor and visibility
        cursor = computed_style.get('cursor')
        display = computed_style.get('display')
        visibility = computed_style.get('visibility')
        
        # Additional context-based interactivity
        if cursor == 'pointer' and display != 'none' and visibility != 'hidden':
            # Look for parent or sibling context
            try:
                # Check for nearby interactive elements or context
                parent_context = driver.execute_script("""
                    var element = arguments[0];
                    var parent = element.closest('nav, .menu, .dropdown, .navigation');
                    return parent ? 'contextual_interactive' : null;
                """, element)
                
                if parent_context:
                    return {
                        'interactive': True,
                        'reason': 'Contextual interactive element',
                        'details': {
                            'cursor': cursor,
                            'parent_context': parent_context
                        }
                    }
            except Exception:
                pass
    except Exception:
        # Fallback if style computation fails
        pass
    
    # If no clear interactivity is found
    return {
        'interactive': False,
        'reason': 'No interactive characteristics detected',
        'details': {}
    }

def validate_keyboard_accessibility(driver, elements):
    """
    Comprehensively validate keyboard accessibility of interactive elements.
    
    Args:
        driver: Selenium WebDriver instance
        elements (list): List of WebElements to check
    
    Returns:
        dict: Detailed report of keyboard accessibility
    """
    accessibility_report = {
        'total_elements': len(elements),
        'interactive_elements': [],
        'non_interactive_elements': [],
        'partially_interactive_elements': []
    }
    
    # First reset focus to the document body
    try:
        driver.execute_script("document.body.focus();")
    except:
        pass
    
    for element in elements:
        try:
            # Skip elements that are no longer attached to the DOM
            if not driver.execute_script("return arguments[0].isConnected", element):
                continue
                
            # Skip elements that are not visible
            if not element.is_displayed():
                continue
                
            # Get element information for reporting
            element_info = {
                'tag': element.tag_name,
                'text': element.text[:50] if element.text else '[No text]',
                'id': element.get_attribute('id') or '',
                'class': element.get_attribute('class') or '',
                'role': element.get_attribute('role') or ''
            }
            
            # Determine interactivity
            interactivity_check = is_truly_interactive(driver, element)
            
            # If interactive, perform additional keyboard checks
            if interactivity_check['interactive']:
                # First, try tabbing to the element using JavaScript
                original_element = driver.execute_script("return document.activeElement;")
                
                try:
                    # Try scrolling to the element
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
                    
                    # Try focusing directly
                    driver.execute_script("arguments[0].focus();", element)
                    
                    # Get the currently focused element
                    focused_element = driver.execute_script("return document.activeElement;")
                    
                    # Check if our element received focus
                    is_focused = driver.execute_script("""
                        return arguments[0] === arguments[1];
                    """, element, focused_element)
                    
                    if is_focused:
                        # Check if element can be activated
                        can_be_activated = False
                        tag_name = element.tag_name.lower()
                        
                        if tag_name in ['a', 'button', 'input', 'select']:
                            # For these elements, check if Enter key would work
                            can_be_activated = True
                        
                        accessibility_check = {
                            'element_info': element_info,
                            'interactivity_details': interactivity_check,
                            'fully_keyboard_accessible': True,
                            'can_be_activated': can_be_activated
                        }
                        
                        accessibility_report['interactive_elements'].append(accessibility_check)
                    else:
                        # Element could not receive focus
                        partial_check = {
                            'element_info': element_info,
                            'interactivity_details': interactivity_check,
                            'fully_keyboard_accessible': False,
                            'error': 'Element cannot receive keyboard focus'
                        }
                        
                        accessibility_report['partially_interactive_elements'].append(partial_check)
                    
                    # Reset focus for next element
                    driver.execute_script("arguments[0].focus();", original_element)
                    
                except Exception as e:
                    # Partial interactivity due to error
                    partial_check = {
                        'element_info': element_info,
                        'interactivity_details': interactivity_check,
                        'fully_keyboard_accessible': False,
                        'error': str(e)
                    }
                    
                    accessibility_report['partially_interactive_elements'].append(partial_check)
            else:
                # Non-interactive elements
                non_interactive_check = {
                    'element_info': element_info,
                    'interactivity_details': interactivity_check
                }
                
                accessibility_report['non_interactive_elements'].append(non_interactive_check)
        except Exception as e:
            # Skip elements that cause errors
            print(f"Error checking element: {str(e)}")
            continue
    
    return accessibility_report

def enhanced_focusable_check(driver, url):
    """
    Enhanced check for keyboard-accessible elements on a webpage.
    
    Args:
        driver: Selenium WebDriver instance
        url: URL to check
    
    Returns:
        dict: Detailed report of keyboard accessibility issues
    """
    print(f"Running enhanced focusable check for {url}...")
    
    # Find potentially interactive elements
    interactive_selectors = [
        '[role]',  # ARIA roles
        'a[href]', 'button', 'input:not([type="hidden"])', 'select', 'textarea',  # Native interactive
        '[onclick]', '[onkeydown]', '[onkeyup]',  # Event handlers
        '[class*="btn"]', '[class*="button"]',  # Class-based interactivity
        '[class*="menu"]', '[class*="nav"]',  # Navigation items
        '[class*="clickable"]', '[class*="selectable"]', # Explicit clickables
        '[tabindex]'  # Elements with explicit tabindex
    ]
    
    # Use comprehensive selector
    selector = ', '.join(interactive_selectors)
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    
    # Validate keyboard accessibility
    accessibility_report = validate_keyboard_accessibility(driver, elements)
    
    # Log results
    print(f"Total Elements Checked: {accessibility_report['total_elements']}")
    print(f"Fully Interactive Elements: {len(accessibility_report['interactive_elements'])}")
    print(f"Partially Interactive Elements: {len(accessibility_report['partially_interactive_elements'])}")
    print(f"Non-Interactive Elements: {len(accessibility_report['non_interactive_elements'])}")
    
    # Process the report to create a more streamlined version for JSON output
    missing_focusable_issues = []
    
    # Add partially interactive elements to the issues list
    for i, elem in enumerate(accessibility_report['partially_interactive_elements'], 1):
        element_info = elem['element_info']
        tag = element_info['tag']
        text = element_info['text']
        id_attr = f" id='{element_info['id']}'" if element_info['id'] else ""
        class_attr = f" class='{element_info['class']}'" if element_info['class'] else ""
        reason = elem['interactivity_details']['reason']
        error = elem.get('error', 'Unknown error')
        
        issue = f"Element {i}: <{tag}{id_attr}{class_attr}> {text} appears interactive ({reason}) but is not keyboard accessible: {error}"
        
        element_data = {
            "issue": issue,
            "element_info": element_info,
            "interactivity_reason": reason,
            "error": error,
            "impact": "High" if tag in ['a', 'button', 'input'] else "Medium",
            "recommendation": "Ensure the element can receive keyboard focus and be activated using keyboard commands."
        }
        
        missing_focusable_issues.append(element_data)
    
    # Find elements that appear to be buttons but aren't properly implemented for keyboard access
    for i, elem in enumerate(accessibility_report['non_interactive_elements'], len(missing_focusable_issues) + 1):
        element_info = elem['element_info']
        tag = element_info['tag']
        classes = element_info['class'].lower()
        text = element_info['text']
        
        # Check if this non-interactive element looks visually interactive
        if (tag in ['div', 'span'] and 
            ('button' in classes or 'btn' in classes or 'clickable' in classes or 'nav' in classes)):
            
            id_attr = f" id='{element_info['id']}'" if element_info['id'] else ""
            class_attr = f" class='{element_info['class']}'" if element_info['class'] else ""
            
            issue = f"Element {i}: <{tag}{id_attr}{class_attr}> {text} appears visually interactive but lacks proper keyboard support"
            
            element_data = {
                "issue": issue,
                "element_info": element_info,
                "interactivity_reason": "Visual styling suggests interactivity",
                "error": "Element is not implemented as an interactive control",
                "impact": "High",
                "recommendation": "Convert to semantic button/link or add appropriate ARIA role, tabindex, and keyboard event handlers."
            }
            
            missing_focusable_issues.append(element_data)
    
    # Create the final report structure
    report = {
        'url': url,
        'total_elements_checked': accessibility_report['total_elements'],
        'fully_interactive_elements': len(accessibility_report['interactive_elements']),
        'partially_interactive_elements': len(accessibility_report['partially_interactive_elements']),
        'missing_focusable_issues': missing_focusable_issues
    }
    
    return report

def generate_tab_order_report(url, browser='chrome'):
    """Generate a fresh tab order report for the given URL"""
    print(f"Generating tab order report for {url}...")
    
    driver = None
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Wait for page to be fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
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
                issue = f"Inconsistent keyboard navigation sequence: Element {current['index']} (tabindex={current['tabindex']}) comes before Element {next_elem['index']} (tabindex={next_elem['tabindex']})"
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
            'tab_order_data': [
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
        if driver:
            driver.quit()

def generate_missing_focusable_report(url, browser='chrome'):
    """Generate an enhanced report of elements with keyboard accessibility issues"""
    print(f"Generating enhanced missing focusable elements report for {url}...")
    
    driver = None
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Wait for page to be fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Allow additional time for scripts to initialize
        time.sleep(2)
        
        # Run the enhanced focusable check
        accessibility_data = enhanced_focusable_check(driver, url)
        
        # Extract the missing focusable issues
        missing_focusable_issues = accessibility_data['missing_focusable_issues']
        
        # Prepare the report data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_url = clean_url_for_filename(url)
        page_title_snippet = clean_url_for_filename(driver.title)[:20]
        
        report_data = {
            'url': url,
            'page_title': driver.title,
            'timestamp': datetime.now().isoformat(),
            'browser': browser,
            'missing_focusable_issues': missing_focusable_issues,
            'summary': {
                'total_elements_checked': accessibility_data['total_elements_checked'],
                'fully_interactive_elements': accessibility_data['fully_interactive_elements'],
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
        
        print(f"Enhanced missing focusable report saved to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"Error generating missing focusable report: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    finally:
        if driver:
            driver.quit()

def generate_comprehensive_report(url, browser='chrome'):
    """Generate a comprehensive accessibility report"""
    print(f"Generating comprehensive accessibility report for {url}...")
    
    driver = None
    try:
        driver = get_webdriver(browser)
        driver.get(url)
        print(f"Page loaded: {driver.title}")
        
        # Wait for page to be fully loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Allow additional time for scripts to initialize
        time.sleep(2)
        
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
        
        # Find visually focused elements with no visible focus indicator
        try:
            js_script = """
            function checkFocusIndicators() {
                const issues = [];
                const focusableElements = document.querySelectorAll('a[href], button, input:not([type="hidden"]), select, textarea, [tabindex]:not([tabindex="-1"])');
                
                for (let i = 0; i < Math.min(focusableElements.length, 50); i++) {
                    const el = focusableElements[i];
                    
                    // Skip elements that aren't visible
                    if (el.offsetParent === null) continue;
                    
                    const originalOutline = el.style.outline;
                    const originalBoxShadow = el.style.boxShadow;
                    
                    // Focus the element
                    try {
                        el.focus();
                        
                        // Get computed style
                        const style = window.getComputedStyle(el);
                        
                        // Check if focus is visibly indicated
                        if (style.outline === 'none' || style.outline === '0px none') {
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
                        document.body.focus();
                    } catch (e) {
                        // Skip errors
                        continue;
                    }
                }
                
                return issues;
            }
            
            return checkFocusIndicators();
            """
            
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
## Missing_Focusable_Elements <a id='Missing_Focusable_Elements'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 21:05:05
- **Size**: 337 bytes

### Code
#### Cell 1
```python

```
## Script_Extract <a id='Script_Extract'></a>
### File Information
- **Type**: Jupyter Notebook
- **Last Modified**: 2025-03-03 20:46:35
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