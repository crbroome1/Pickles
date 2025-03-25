"""
Simplified HTML Report Generator
Generates a clean CSS-only HTML accessibility report optimized for Jupyter and Firefox.
"""

import os
import logging
import re
from datetime import datetime
from urllib.parse import urlparse

def generate_simplified_html_report(accessibility_report, output_dir=None):
    """
    Generate a simplified CSS-only HTML accessibility report.
    
    Args:
        accessibility_report (dict): Dictionary containing accessibility check results
        output_dir (str, optional): Directory to save the report
        
    Returns:
        str: Path to the generated HTML report
    """
    # Set default output directory if not provided
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), 'accessibility_reports')
    
    # Create directory if it doesn't exist
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
    
    # Extract and organize issues by category
    categorized_issues = categorize_issues(accessibility_report)
    
    # Generate HTML content
    html_content = build_html_report(accessibility_report, categorized_issues)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logging.info(f"Simplified HTML report saved to: {filepath}")
    return filepath

def categorize_issues(accessibility_report):
    """
    Organize issues into categories for the tab structure
    
    Args:
        accessibility_report (dict): Full accessibility report
        
    Returns:
        dict: Issues organized by category
    """
    categories = {
        'keyboard_navigation': [],
        'color_contrast': [],
        'aria_semantics': [],
        'images': [],
        'dynamic_content': [],
        'forms': [],
        'other': []
    }
    
    # Process issues from all checks
    if 'checks' in accessibility_report:
        for check_name, check_data in accessibility_report.get('checks', {}).items():
            if isinstance(check_data, dict) and 'issues' in check_data:
                for issue in check_data.get('issues', []):
                    if not isinstance(issue, dict):
                        continue
                        
                    # Add category for easier reference
                    issue['check_type'] = check_name
                    
                    # Categorize based on check type or issue content
                    if check_name in ['tab_order', 'focus_order_checker', 'focusable_elements']:
                        categories['keyboard_navigation'].append(issue)
                    elif check_name == 'color_contrast':
                        categories['color_contrast'].append(issue)
                    elif check_name == 'aria_accessibility':
                        categories['aria_semantics'].append(issue)
                    elif check_name == 'image_accessibility':
                        categories['images'].append(issue)
                    elif 'form' in check_name.lower():
                        categories['forms'].append(issue)
                    else:
                        # Try to categorize based on issue content
                        issue_text = issue.get('issue', '').lower()
                        if 'keyboard' in issue_text or 'focus' in issue_text or 'tab' in issue_text:
                            categories['keyboard_navigation'].append(issue)
                        elif 'contrast' in issue_text or 'color' in issue_text:
                            categories['color_contrast'].append(issue)
                        elif 'aria' in issue_text or 'role' in issue_text:
                            categories['aria_semantics'].append(issue)
                        elif 'image' in issue_text or 'alt' in issue_text:
                            categories['images'].append(issue)
                        elif 'form' in issue_text or 'input' in issue_text or 'label' in issue_text:
                            categories['forms'].append(issue)
                        else:
                            categories['other'].append(issue)
    
    # Process dynamic content issues separately
    if 'dynamic_content' in accessibility_report:
        dynamic_content = accessibility_report.get('dynamic_content', {})
        if isinstance(dynamic_content, dict):
            # From detailed_results dictionary
            for component_type, component_issues in dynamic_content.get('detailed_results', {}).items():
                if component_type != 'state_tracking' and isinstance(component_issues, list):
                    for issue in component_issues:
                        if isinstance(issue, dict):
                            issue['check_type'] = 'dynamic_content'
                            issue['component_type'] = component_type
                            categories['dynamic_content'].append(issue)
    
    return categories

def build_html_report(report, categorized_issues):
    """
    Build the HTML report content using the simplified template
    
    Args:
        report (dict): Full accessibility report
        categorized_issues (dict): Issues organized by category
        
    Returns:
        str: Complete HTML document as a string
    """
    # Extract summary data
    summary = report.get('summary', {})
    critical_issues = summary.get('critical_issues', 0)
    warnings = summary.get('warnings', 0)
    passed_checks = summary.get('passed_checks', 0)
    total_checks = summary.get('total_checks', 0)
    accessibility_score = summary.get('accessibility_score', 0)
    
    url = report.get('url', 'unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    browser = report.get('browser', 'unknown')
    
    # Start building HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - {url}</title>
    <style>
    /* Core styles - clean and simple */
    :root {{
        --primary-color: #2563eb;
        --primary-light: #dbeafe;
        --warning-color: #f59e0b;
        --error-color: #dc2626;
        --success-color: #16a34a;
        --text-color: #1f2937;
        --text-light: #6b7280;
        --bg-color: #f8fafc;
        --card-color: #ffffff;
        --border-color: #e5e7eb;
        --heading-color: #111827;
    }}

    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.5;
        color: var(--text-color);
        background-color: var(--bg-color);
        margin: 0;
        padding: 20px;
    }}

    /* Container */
    .container {{
        max-width: 1200px;
        margin: 0 auto;
    }}

    /* Header */
    .header {{
        margin-bottom: 30px;
    }}

    .header h1 {{
        color: var(--heading-color);
        margin-bottom: 10px;
    }}

    .header-meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 20px;
    }}

    .header-meta-item {{
        display: flex;
        align-items: center;
        gap: 5px;
    }}

    /* Summary Card */
    .summary-card {{
        background-color: var(--card-color);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }}

    .summary-card h2 {{
        margin-top: 0;
        margin-bottom: 15px;
        color: var(--heading-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
    }}

    .summary-stats {{
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }}

    .stat-item {{
        flex: 1;
        min-width: 120px;
        padding: 15px;
        border-radius: 6px;
        background-color: var(--primary-light);
    }}

    .stat-value {{
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
        color: var(--primary-color);
    }}

    .stat-label {{
        color: var(--text-light);
        font-size: 14px;
    }}

    .critical {{ background-color: #fee2e2; }}
    .critical .stat-value {{ color: var(--error-color); }}

    .warning {{ background-color: #fef3c7; }}
    .warning .stat-value {{ color: var(--warning-color); }}

    .success {{ background-color: #dcfce7; }}
    .success .stat-value {{ color: var(--success-color); }}

    /* Issues Section Tabs - CSS Only */
    .tabs {{
        margin-bottom: 30px;
    }}

    .tab-list {{
        display: flex;
        flex-wrap: wrap;
        gap: 2px;
        margin: 0;
        padding: 0;
        list-style: none;
        border-bottom: 2px solid var(--border-color);
    }}

    .tab-list li {{
        margin-bottom: -2px;
    }}

    .tab-list label {{
        display: inline-block;
        padding: 10px 15px;
        cursor: pointer;
        border-radius: 4px 4px 0 0;
        color: var(--text-light);
        transition: all 0.2s ease;
    }}

    .tab-list label:hover {{
        background-color: #f1f5f9;
        color: var(--primary-color);
    }}

    .tab-content {{
        display: none;
        padding: 20px 0;
    }}

    /* CSS-only tab mechanism */
    .tab-input {{
        position: absolute;
        opacity: 0;
        z-index: -1;
    }}

    .tab-input:checked + label {{
        border: 1px solid var(--border-color);
        border-bottom: 2px solid white;
        color: var(--primary-color);
        font-weight: 500;
        margin-bottom: -1px;
        background-color: white;
    }}

    .tab-input:checked + label + .tab-content {{
        display: block;
    }}

    /* Issue Cards */
    .issue-card {{
        background-color: var(--card-color);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }}

    .issue-card.critical {{
        border-left: 4px solid var(--error-color);
    }}

    .issue-card.warning {{
        border-left: 4px solid var(--warning-color);
    }}

    .issue-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 15px;
    }}

    .issue-title {{
        font-weight: 600;
        font-size: 18px;
        color: var(--heading-color);
        margin: 0;
    }}

    .issue-title.critical {{ color: var(--error-color); }}
    .issue-title.warning {{ color: var(--warning-color); }}

    .severity-badge {{
        font-size: 12px;
        padding: 3px 8px;
        border-radius: 99px;
        background-color: #f1f5f9;
        color: var(--text-light);
    }}

    .severity-badge.critical {{
        background-color: #fee2e2;
        color: var(--error-color);
    }}

    .severity-badge.warning {{
        background-color: #fef3c7;
        color: var(--warning-color);
    }}

    .issue-description {{
        margin-bottom: 15px;
    }}

    .issue-recommendation {{
        background-color: #f1f5f9;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 15px;
        border-left: 3px solid var(--primary-color);
    }}

    .issue-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }}

    .issue-tag {{
        font-size: 12px;
        padding: 3px 8px;
        border-radius: 4px;
        background-color: #e0f2fe;
        color: #0284c7;
    }}

    .issue-tag.wcag {{
        background-color: #e0e7ff;
        color: #4f46e5;
    }}

    /* CSS-only accordion for element details */
    .element-details {{
        margin-top: 15px;
        border-top: 1px solid var(--border-color);
        padding-top: 15px;
    }}

    .accordion-control {{
        position: absolute;
        opacity: 0;
        z-index: -1;
    }}

    .accordion-label {{
        display: block;
        padding: 10px;
        background-color: #f1f5f9;
        color: var(--text-color);
        font-weight: 500;
        cursor: pointer;
        border-radius: 4px;
        margin-bottom: 10px;
        transition: all 0.2s ease;
    }}

    .accordion-label:hover {{
        background-color: #e0f2fe;
    }}

    .accordion-label::after {{
        content: "+";
        float: right;
        font-weight: bold;
    }}

    .accordion-content {{
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.35s ease;
    }}

    .accordion-control:checked + .accordion-label::after {{
        content: "−";
    }}

    .accordion-control:checked ~ .accordion-content {{
        max-height: 1000px;
    }}

    /* Element details table */
    .element-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        font-size: 14px;
    }}

    .element-table th, 
    .element-table td {{
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid var(--border-color);
    }}

    .element-table th {{
        background-color: #f8fafc;
        font-weight: 500;
    }}

    /* Code display */
    .code-block {{
        background-color: #1e293b;
        color: #e2e8f0;
        padding: 12px;
        border-radius: 6px;
        overflow-x: auto;
        margin: 10px 0;
        font-family: monospace;
    }}

    /* Element highlight box */
    .element-highlight {{
        border: 2px dashed var(--primary-color);
        padding: 8px;
        border-radius: 4px;
        margin: 10px 0;
        background-color: #f8fafc;
    }}

    /* Badge for easy visual indicators */
    .badge {{
        display: inline-block;
        min-width: 18px;
        padding: 2px 6px;
        font-size: 12px;
        font-weight: 500;
        line-height: 14px;
        text-align: center;
        border-radius: 99px;
        background-color: var(--text-light);
        color: white;
    }}

    /* Element positioning visualization */
    .position-diagram {{
        width: 100%;
        max-width: 300px;
        height: 150px;
        border: 1px solid var(--border-color);
        position: relative;
        background-color: #f8fafc;
        margin: 10px 0;
    }}

    .element-box {{
        position: absolute;
        background-color: rgba(37, 99, 235, 0.2);
        border: 2px solid rgba(37, 99, 235, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 10px;
        font-family: monospace;
        color: #1e293b;
    }}

    /* Basic responsive styling */
    @media (max-width: 768px) {{
        .summary-stats {{
            flex-direction: column;
        }}

        .stat-item {{
            width: 100%;
        }}

        .tab-list {{
            flex-direction: column;
        }}

        .tab-list li {{
            width: 100%;
        }}

        .tab-list label {{
            display: block;
            width: 100%;
            border-radius: 0;
        }}

        .tab-input:checked + label {{
            border-bottom: none;
            border-left: 3px solid var(--primary-color);
        }}
    }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Report Header -->
        <div class="header">
            <h1>Accessibility Audit Report</h1>
            <div class="header-meta">
                <div class="header-meta-item">
                    <strong>URL:</strong> {url}
                </div>
                <div class="header-meta-item">
                    <strong>Date:</strong> {timestamp}
                </div>
                <div class="header-meta-item">
                    <strong>Browser:</strong> {browser}
                </div>
            </div>
        </div>

        <!-- Summary Card -->
        <div class="summary-card">
            <h2>Summary</h2>
            <div class="summary-stats">
                <div class="stat-item critical">
                    <div class="stat-value">{critical_issues}</div>
                    <div class="stat-label">Critical Issues</div>
                </div>
                <div class="stat-item warning">
                    <div class="stat-value">{warnings}</div>
                    <div class="stat-label">Warnings</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{accessibility_score}%</div>
                    <div class="stat-label">Compliance Score</div>
                </div>
                <div class="stat-item success">
                    <div class="stat-value">{passed_checks}</div>
                    <div class="stat-label">Passed Checks</div>
                </div>
            </div>
        </div>

        <!-- Issues Section with CSS-only tabs -->
        <div class="tabs">
            <ul class="tab-list">
"""
    
    # Add tab headers
    categories = [
        ('keyboard_navigation', 'Keyboard Navigation'),
        ('color_contrast', 'Color Contrast'),
        ('aria_semantics', 'ARIA & Semantics'),
        ('images', 'Images'),
        ('dynamic_content', 'Dynamic Content'),
        ('forms', 'Forms'),
        ('other', 'Other Issues')
    ]
    
    # Default to first tab that has issues
    first_tab_with_issues = None
    
    # Only include tabs that have issues or are important categories
    for i, (category_key, category_name) in enumerate(categories):
        issues = categorized_issues.get(category_key, [])
        if issues or category_key in ['keyboard_navigation', 'aria_semantics', 'images']:
            # Remember the first tab with issues
            if issues and first_tab_with_issues is None:
                first_tab_with_issues = i
                
            html += f"""
                <li>
                    <input type="radio" name="tabs" id="tab{i+1}" class="tab-input">
                    <label for="tab{i+1}">{category_name} <span class="badge">{len(issues)}</span></label>
                    <div class="tab-content">
            """
            
            if issues:
                # Add all issues for this category
                for j, issue in enumerate(issues):
                    html += build_issue_card(issue, f"{category_key}-{j+1}")
            else:
                html += f"""
                        <p>No {category_name.lower()} issues detected.</p>
                """
                
            html += """
                    </div>
                </li>
            """
    
    # Set the first tab with issues as checked (or the first tab if none have issues)
    if first_tab_with_issues is not None:
        # Find the tab{i+1} ID and add checked attribute
        tab_id = f"tab{first_tab_with_issues+1}"
        html = html.replace(f'id="{tab_id}" class="tab-input"', f'id="{tab_id}" class="tab-input" checked')
    else:
        # If no tabs have issues, check the first tab
        html = html.replace('id="tab1" class="tab-input"', 'id="tab1" class="tab-input" checked')
    
    # Close tabs and container, add footer
    html += """
            </ul>
        </div>

        <!-- Footer with link to standard -->
        <footer style="margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border-color); text-align: center; color: var(--text-light);">
            <p>Report generated by Accessibility Checker • <a href="https://www.w3.org/WAI/WCAG21/quickref/" style="color: var(--primary-color);">WCAG 2.1 AA</a></p>
        </footer>
    </div>
</body>
</html>
    """
    
    return html

def build_issue_card(issue, issue_id):
    """
    Build an HTML issue card for a single accessibility issue
    
    Args:
        issue (dict): Issue data
        issue_id (str): Unique ID for this issue
        
    Returns:
        str: HTML for a single issue card
    """
    # Extract issue data with safe defaults
    title = issue.get('issue', 'Unknown Issue')
    details = issue.get('details', '')
    recommendation = issue.get('recommendation', '')
    severity = issue.get('severity', 'warning')
    wcag = issue.get('wcag', '')
    
    # Clean up severity value
    severity = severity.lower()
    if severity not in ['critical', 'warning']:
        severity = 'warning'
    
    # Build the HTML for the issue card - simplified version
    card_html = f"""
        <div id="issue-{issue_id}" class="issue-card {severity}">
            <div class="issue-header">
                <h3 class="issue-title {severity}">{title}</h3>
                <span class="severity-badge {severity}">{severity.capitalize()}</span>
            </div>
            <div class="issue-description">
                <p>{details}</p>
            </div>
    """
    
    if recommendation:
        card_html += f"""
            <div class="issue-recommendation">
                <p><strong>Recommendation:</strong> {recommendation}</p>
            </div>
        """
    
    # Add tags
    card_html += """
            <div class="issue-tags">
    """
    
    if wcag:
        card_html += f"""
                <span class="issue-tag wcag">WCAG {wcag}</span>
        """
    
    # Add more tags based on issue type
    if "keyboard" in title.lower() or "focus" in title.lower() or "tab" in title.lower():
        card_html += """
                <span class="issue-tag">Keyboard Access</span>
        """
    elif "contrast" in title.lower() or "color" in title.lower():
        card_html += """
                <span class="issue-tag">Contrast</span>
        """
    elif "aria" in title.lower() or "role" in title.lower():
        card_html += """
                <span class="issue-tag">ARIA</span>
        """
    elif "alt" in title.lower() or "image" in title.lower():
        card_html += """
                <span class="issue-tag">Images</span>
        """
    elif "form" in title.lower() or "label" in title.lower() or "input" in title.lower():
        card_html += """
                <span class="issue-tag">Forms</span>
        """
    
    card_html += """
            </div>
    """
    
    # Element information - simplified to avoid None errors
    element_tag = issue.get('element', '')
    if element_tag:
        card_html += f"""
            <div class="element-details">
                <input type="checkbox" id="accordion-{issue_id}" class="accordion-control">
                <label for="accordion-{issue_id}" class="accordion-label">Element Details</label>
                <div class="accordion-content">
                    <table class="element-table">
                        <tr>
                            <th>Element Type</th>
                            <td>&lt;{element_tag}&gt;</td>
                        </tr>
    """
        
        element_text = issue.get('text', '')
        if element_text:
            card_html += f"""
                        <tr>
                            <th>Content</th>
                            <td>{element_text}</td>
                        </tr>
            """
            
        location = issue.get('location', '')
        if location:
            card_html += f"""
                        <tr>
                            <th>Location</th>
                            <td>{location}</td>
                        </tr>
            """
            
        card_html += """
                    </table>
                </div>
            </div>
        """
        
    # Close the card
    card_html += """
        </div>
    """
    
    return card_html