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

