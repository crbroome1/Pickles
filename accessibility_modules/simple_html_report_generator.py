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