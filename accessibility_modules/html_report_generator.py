"""
Enhanced HTML Report Generator
Generates a clean and reliable HTML report with working accordions and detailed element information.
"""

import os
from datetime import datetime
from urllib.parse import urlparse
import logging

def generate_html_report(accessibility_report, output_dir=None):
    """
    Generate an enhanced HTML accessibility report with detailed element information
    using CSS-only accordions for maximum compatibility.
    
    Args:
        accessibility_report (dict): Dictionary containing accessibility check results
        output_dir (str, optional): Directory to save the report. Defaults to None.
        
    Returns:
        str: Path to the generated HTML report
    """
    logging.info("Generating enhanced HTML accessibility report...")
    
    # Set default output directory if not provided
    if not output_dir:
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                'accessibility_reports')
    
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a filename based on URL and timestamp
    url = accessibility_report.get('url', 'unknown')
    # Fix URL for better filename compatibility
    if '\\' in url:
        # Convert backslashes to forward slashes
        url = url.replace('\\', '/')
    
    domain = urlparse(url).netloc
    if not domain:
        domain = 'unknown'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accessibility_report_{domain}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    # Build HTML content using string parts to avoid syntax errors
    html_parts = []
    
    # Extract report data
    issues = accessibility_report.get('issues', [])
    
    # Group issues by check type for better organization
    issues_by_type = {}
    for issue in issues:
        check_type = issue.get('check_type', 'general')
        if check_type not in issues_by_type:
            issues_by_type[check_type] = []
        issues_by_type[check_type].append(issue)
    
    # Add HTML header and styles
    html_parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Accessibility Report - {url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f7f7f7;
        }}
        
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        
        .section {{
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 20px;
        }}
        
        .issue-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }}
        
        .issue-count {{
            background-color: #e74c3c;
            color: white;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 14px;
        }}
        
        .issue-count.no-issues {{
            background-color: #2ecc71;
        }}
        
        /* CSS-only accordion styling */
        .accordion {{
            margin-bottom: 10px;
        }}
        
        .accordion input[type="checkbox"] {{
            display: none;
        }}
        
        .accordion label {{
            background-color: #f8f9fa;
            color: #444;
            cursor: pointer;
            padding: 12px 15px;
            width: 100%;
            display: block;
            text-align: center;
            border: none;
            border-radius: 4px;
            outline: none;
            font-size: 16px;
            transition: 0.3s;
            margin-bottom: 5px;
            position: relative;
        }}
        
        .accordion label:hover {{
            background-color: #e9ecef;
        }}
        
        .accordion label::after {{
            content: '+';
            position: absolute;
            right: 15px;
            font-weight: bold;
        }}
        
        .accordion input:checked + label::after {{
            content: '-';
        }}
        
        .accordion-content {{
            background-color: #f9f9f9;
            border-radius: 0 0 4px 4px;
            overflow: hidden;
            padding: 0;
            max-height: 0;
            transition: max-height 0.3s ease-out;
        }}
        
        .accordion input:checked ~ .accordion-content {{
            max-height: 9999px; /* Large value to accommodate any content */
            padding: 18px;
        }}
        
        .issue-item {{
            margin-bottom: 20px;
            padding: 15px;
            border-left: 4px solid #e74c3c;
            background-color: white;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }}
        
        .issue-title {{
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 16px;
        }}
        
        .issue-details {{
            margin-bottom: 10px;
        }}
        
        .issue-recommendation {{
            font-style: italic;
            color: #666;
            margin-bottom: 15px;
            padding-left: 10px;
            border-left: 2px solid #3498db;
        }}
        
        .critical {{
            color: #e74c3c;
        }}
        
        .warning {{
            color: #f39c12;
        }}
        
        /* CSS-only element info panel */
        .element-info-panel {{
            margin-top: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
        }}
        
        .element-info-panel input[type="checkbox"] {{
            display: none;
        }}
        
        .element-info-header {{
            background-color: #f1f1f1;
            padding: 8px 12px;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0;
        }}
        
        .element-info-header:hover {{
            background-color: #e5e5e5;
        }}
        
        .element-info-header::after {{
            content: '+';
            position: relative;
            font-weight: bold;
        }}
        
        .element-info-panel input:checked + .element-info-header::after {{
            content: '-';
        }}
        
        .element-info-content {{
            padding: 0;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #fff;
        }}
        
        .element-info-panel input:checked ~ .element-info-content {{
            max-height: 2000px;
            padding: 12px;
        }}
        
        .element-property {{
            margin-bottom: 8px;
            display: flex;
            flex-wrap: wrap;
        }}
        
        .property-name {{
            font-weight: bold;
            min-width: 120px;
            color: #555;
        }}
        
        .property-value {{
            flex: 1;
            word-break: break-word;
            font-family: monospace;
            background-color: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        
        .selector-path {{
            font-family: monospace;
            background-color: #f5f5f5;
            padding: 8px;
            border-radius: 4px;
            margin-top: 5px;
            word-break: break-all;
            border: 1px solid #e0e0e0;
        }}
        
        .position-diagram {{
            width: 100%;
            max-width: 300px;
            height: 150px;
            margin: 10px 0;
            border: 1px solid #ddd;
            position: relative;
            background-color: #f9f9f9;
        }}
        
        .element-box {{
            position: absolute;
            background-color: rgba(52, 152, 219, 0.3);
            border: 2px solid rgba(52, 152, 219, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-family: monospace;
            color: #333;
        }}
        
        .attribute-list {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
        }}
        
        .attribute-list th, .attribute-list td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        
        .attribute-list th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        
        .attribute-list tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        .tags-list {{
            margin-top: 10px;
        }}
        
        .tags-list span {{
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .wcag-tag {{
            background-color: #9b59b6;
        }}
        
        .severity-tag {{
            background-color: #e74c3c;
        }}
        
        /* Dynamic content specific styles */
        .state-tag {{
            display: inline-block;
            background-color: #17a2b8;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .component-type-tag {{
            display: inline-block;
            background-color: #6f42c1;
            color: white;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }}
        
        .component-container {{
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-top: 15px;
            background-color: #f8f9fa;
        }}
        
        .component-header {{
            font-weight: bold;
            margin-bottom: 10px;
            padding-bottom: 5px;
            border-bottom: 1px solid #eee;
        }}
        
        /* Verification buttons */
        .verification-section {{
            display: flex;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #eee;
            justify-content: flex-start;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .verification-button {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            text-align: center;
            transition: all 0.3s ease;
            border: 2px solid;
            min-width: 120px;
            position: relative;
        }}
        
        .verify-button {{
            background-color: #f0f8ff;
            color: #0077cc;
            border-color: #0077cc;
        }}
        
        .verify-button:hover {{
            background-color: #e0f0ff;
        }}
        
        .verify-button.active {{
            background-color: #0077cc;
            color: white;
        }}
        
        .verify-button.active::before {{
            content: "✓ ";
        }}
        
        .fix-button {{
            background-color: #f0fff0;
            color: #2e8b57;
            border-color: #2e8b57;
        }}
        
        .fix-button:hover {{
            background-color: #e0ffe0;
        }}
        
        .fix-button.active {{
            background-color: #2e8b57;
            color: white;
        }}
        
        .fix-button.active::before {{
            content: "✓ ";
        }}
        
        /* Export button */
        .export-btn {{
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        
        .export-btn:hover {{
            background-color: #2980b9;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            margin-top: 20px;
            color: #666;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="section">
        <h1>Enhanced Accessibility Audit Report</h1>
        <p><strong>URL:</strong> {url}</p>
        <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><strong>Elements Analyzed:</strong> {accessibility_report.get('summary', {}).get('elements_checked', 'Unknown')}</p>
    </div>
""")
    
    # Add section for each issue type
    section_counter = 0
    for check_type, issues_list in issues_by_type.items():
        # Create user-friendly name from check_type
        check_name = check_type.replace('_', ' ').title()
        
        # Common conversions for clarity
        if check_type == 'keyboard_navigation_sequence':
            check_name = 'Keyboard Navigation Sequence'
        elif check_type == 'aria_accessibility':
            check_name = 'ARIA Accessibility'
        elif check_type == 'dynamic_content':
            check_name = 'Dynamic Content'
        
        section_counter += 1
        accordion_id = f"accordion-{section_counter}"
        
        html_parts.append(f"""
    <div class="section">
        <div class="issue-header">
            <h2>{check_name}</h2>
            <span class="issue-count {'no-issues' if not issues_list else ''}">
                {len(issues_list)} {'Issue' if len(issues_list) == 1 else 'Issues'}
            </span>
        </div>
        
        <div class="accordion">
            <input type="checkbox" id="{accordion_id}" class="accordion-checkbox">
            <label for="{accordion_id}">View Issues</label>
            <div class="accordion-content">
""")
        
        if issues_list:
            html_parts.append("""
            <div class="issues-list">
""")
            
            for i, issue in enumerate(issues_list):
                title = issue.get('issue', 'Unknown Issue')
                details = issue.get('details', '')
                recommendation = issue.get('recommendation', '')
                severity = issue.get('severity', 'warning')
                wcag = issue.get('wcag', '')
                
                # Use preferred terminology
                if "inconsistent keyboard navigation sequence" in title.lower():
                    title = "Inconsistent keyboard navigation sequence"
                elif "keyboard navigation barrier" in title.lower():
                    title = "Keyboard navigation barrier"
                
                issue_id = f"issue-{section_counter}-{i}"
                
                html_parts.append(f"""
                <div class="issue-item" id="{issue_id}">
                    <div class="issue-title {severity}">{title}</div>
                    <div class="issue-details">{details}</div>
                    <div class="issue-recommendation">{recommendation}</div>
                    <div class="tags-list">
                        {f'<span class="wcag-tag">WCAG {wcag}</span>' if wcag else ''}
                        <span class="severity-tag">{severity.title()}</span>
                    </div>
""")

                # Add special information for dynamic content issues
                if issue.get("check_type") == "dynamic_content":
                    state_info = issue.get("state_info", "")
                    component_type = issue.get("component_type", "")
                    component_id = issue.get("component_id", "")
                    
                    if state_info or component_type:
                        html_parts.append(f"""
                        <div class="component-container">
                            <div class="component-header">
                                {f'<span class="component-type-tag">{component_type.title()}</span>' if component_type else ''}
                                {f'<span class="state-tag">{state_info}</span>' if state_info else ''}
                            </div>
                            <div class="component-details">
                                <p>This issue was detected in a dynamic component that may change state during user interaction.</p>
                                {f'<p><strong>Component ID:</strong> {component_id}</p>' if component_id else ''}
                            </div>
                        </div>
""")
                
                # Add detailed element information section
                element_info = issue.get('element_info', {})
                if element_info:
                    element_id = f"element-info-{section_counter}-{i}"
                    
                    # Get the main element properties
                    tag = element_info.get('tag', 'unknown')
                    element_id_value = element_info.get('id', '')
                    element_class = element_info.get('class', '')
                    element_src = element_info.get('src', '')
                    dom_path = element_info.get('dom_path', '')
                    css_selector = element_info.get('css_selector', '')
                    position = element_info.get('position', {})
                    attributes = element_info.get('attributes', {})
                    
                    html_parts.append(f"""
                    <div class="element-info-panel">
                        <input type="checkbox" id="{element_id}" class="element-info-checkbox">
                        <label class="element-info-header" for="{element_id}">
                            Element Details: &lt;{tag}&gt;{f' #{element_id_value}' if element_id_value else ''}
                        </label>
                        <div class="element-info-content">
                            <!-- Basic Element Info -->
                            <div class="element-property">
                                <div class="property-name">Element Type:</div>
                                <div class="property-value">&lt;{tag}&gt;</div>
                            </div>
""")
                    
                    # Add ID if available
                    if element_id_value:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Element ID:</div>
                                <div class="property-value">{element_id_value}</div>
                            </div>
""")
                    
                    # Add Class if available
                    if element_class:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">CSS Classes:</div>
                                <div class="property-value">{element_class}</div>
                            </div>
""")
                    
                    # Add Source if available (for images, scripts, etc.)
                    if element_src:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Source:</div>
                                <div class="property-value">{element_src}</div>
                            </div>
""")
                    
                    # Add DOM path if available
                    if dom_path:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">DOM Path:</div>
                                <div class="property-value">{dom_path}</div>
                            </div>
""")
                    
                    # Add CSS Selector if available
                    if css_selector:
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">CSS Selector:</div>
                                <div class="selector-path">{css_selector}</div>
                            </div>
""")
                    
                    # Add Position information if available
                    if position:
                        # Calculate scaled position for the visual representation
                        container_width = 300
                        container_height = 150
                        
                        # Default values in case properties are missing
                        x = position.get('x', 0)
                        y = position.get('y', 0)
                        width = position.get('width', 100)
                        height = position.get('height', 50)
                        
                        # Handle edge case where dimensions or position might be invalid
                        if width <= 0: width = 100
                        if height <= 0: height = 50
                        
                        # Scale factor (max 10x reduction to fit within diagram)
                        scale_factor_x = min(1, container_width / (width * 3))
                        scale_factor_y = min(1, container_height / (height * 3))
                        scale_factor = min(scale_factor_x, scale_factor_y, 0.1)  # Max 10x reduction
                        
                        # Calculate scaled dimensions
                        scaled_width = max(10, width * scale_factor)  # Minimum 10px width
                        scaled_height = max(10, height * scale_factor)  # Minimum 10px height
                        
                        # Center the element in the container
                        scaled_x = (container_width - scaled_width) / 2
                        scaled_y = (container_height - scaled_height) / 2
                        
                        html_parts.append(f"""
                            <div class="element-property">
                                <div class="property-name">Position:</div>
                                <div class="property-value">
                                    x: {x}px, y: {y}px, width: {width}px, height: {height}px
                                </div>
                            </div>
                            
                            <!-- Visual position diagram -->
                            <div class="position-diagram">
                                <div class="element-box" style="
                                    left: {scaled_x}px;
                                    top: {scaled_y}px;
                                    width: {scaled_width}px;
                                    height: {scaled_height}px;
                                ">
                                    &lt;{tag}&gt;
                                </div>
                            </div>
""")
                    
                    # Add Attributes table if available
                    if attributes:
                        html_parts.append("""
                            <div class="element-property">
                                <div class="property-name">Attributes:</div>
                                <div class="property-value">
                                    <table class="attribute-list">
                                        <tr>
                                            <th>Name</th>
                                            <th>Value</th>
                                        </tr>
""")
                        
                        # Add each attribute
                        for attr_name, attr_value in attributes.items():
                            # Skip attributes already shown above
                            if attr_name in ['id', 'class', 'src']:
                                continue
                                
                            html_parts.append(f"""
                                        <tr>
                                            <td>{attr_name}</td>
                                            <td>{attr_value}</td>
                                        </tr>
""")
                            
                        html_parts.append("""
                                    </table>
                                </div>
                            </div>
""")
                    
                    # Close the element info panel
                    html_parts.append("""
                        </div>
                    </div>
""")
                
                # Add verification buttons
                html_parts.append(f"""
                    <div class="verification-section">
                        <div class="verification-button verify-button" 
                             onclick="toggleVerificationStatus(this, '{issue_id}', 'verified')">VERIFY</div>
                        <div class="verification-button fix-button" 
                             onclick="toggleVerificationStatus(this, '{issue_id}', 'fixed')">MARK FIXED</div>
                    </div>
                </div>
""")
            
            html_parts.append("""
            </div>
""")
        else:
            html_parts.append("""
            <p>No issues detected for this check.</p>
""")
        
        # Close the accordion content and section
        html_parts.append("""
            </div>
        </div>
    </div>
""")
    
    # Add footer and CSV export script (only JavaScript remaining)
    html_parts.append(f"""
    <div class="section">
        <h2>Export Options</h2>
        <button class="export-btn" onclick="exportToCsv()">Export Issues to CSV</button>
    </div>
    
    <footer>
        <p>Generated by Accessibility Checker on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </footer>
    
    <script>
        // Toggle verification status with more obvious visual feedback
        function toggleVerificationStatus(button, issueId, status) {{
            // Toggle active class
            button.classList.toggle('active');
            
            // If it's a fixed button, also activate the verify button if it's active
            if (status === 'fixed' && button.classList.contains('active')) {{
                // Find the verify button in the same verification section
                var verifyBtn = button.parentElement.querySelector('.verify-button');
                if (verifyBtn) {{
                    verifyBtn.classList.add('active');
                }}
            }}
        }}
        
        // CSV Export Function - only JavaScript needed
        function exportToCsv() {{
            // Collect all issues
            var issues = [];
            var issueItems = document.querySelectorAll('.issue-item');
            
            issueItems.forEach(function(item) {{
                var checkType = item.closest('.section').querySelector('h2').textContent;
                var title = item.querySelector('.issue-title').textContent;
                var details = item.querySelector('.issue-details').textContent;
                var recommendation = item.querySelector('.issue-recommendation').textContent;
                var verified = item.querySelector('.verify-button').classList.contains('active') ? 'Yes' : 'No';
                var fixed = item.querySelector('.fix-button').classList.contains('active') ? 'Yes' : 'No';
                
                // Get dynamic content info if present
                var componentInfo = '';
                var componentContainer = item.querySelector('.component-container');
                if (componentContainer) {{
                    var componentType = componentContainer.querySelector('.component-type-tag');
                    var stateInfo = componentContainer.querySelector('.state-tag');
                    
                    if (componentType) {{
                        componentInfo += componentType.textContent + ' ';
                    }}
                    
                    if (stateInfo) {{
                        componentInfo += stateInfo.textContent;
                    }}
                }}
                
                issues.push([
                    checkType,
                    title,
                    details,
                    recommendation,
                    componentInfo ? componentInfo : 'N/A',
                    verified,
                    fixed
                ]);
            }});
            
            // Create CSV content
            var csvContent = "Check Type,Issue,Details,Recommendation,Component Info,Verified,Fixed\\n";
            
            issues.forEach(function(issue) {{
                // Properly escape CSV fields
                var formattedIssue = issue.map(function(field) {{
                    // Escape quotes and wrap in quotes if contains comma
                    var escaped = String(field).replace(/"/g, '""');
                    if (escaped.includes(',')) {{
                        escaped = '"' + escaped + '"';
                    }}
                    return escaped;
                }});
                
                csvContent += formattedIssue.join(',') + "\\n";
            }});
            
            // Create download link
            var encodedUri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvContent);
            var link = document.createElement('a');
            link.setAttribute('href', encodedUri);
            link.setAttribute('download', 'accessibility_issues_{timestamp}.csv');
            
            // Trigger download
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}
    </script>
</body>
</html>
""")
    
    # Join all HTML parts into a single string
    html_content = ''.join(html_parts)
    
    # Write HTML to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logging.info(f"Enhanced HTML report saved to: {filepath}")
    return filepath