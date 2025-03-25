"""
Enhanced Accessibility Checker with Dynamic Content Testing

Integrates comprehensive accessibility checks including dynamic content analysis.
"""

import os
import sys
import logging
import time
import json  # Added missing import
from datetime import datetime

# Add the current directory to Python path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Selenium and WebDriver imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Import accessibility modules
from accessibility_modules.dynamic_content_tester import run_advanced_dynamic_content_test
from accessibility_modules.report_generator import integrate_dynamic_content_results, \
    generate_dynamic_content_report_section, export_dynamic_content_state_tracking

# Import other existing modules
from accessibility_modules.tab_order_checker import check_tab_order
from accessibility_modules.focusable_elements import check_missing_focusable_elements
from accessibility_modules.aria_checker import check_aria_accessibility
from accessibility_modules.color_contrast import check_color_contrast
from accessibility_modules.image_checker import check_image_accessibility

def setup_driver(browser_name='chrome', headless=True):
    """
    Set up and return a WebDriver instance for the specified browser.
    
    Args:
        browser_name (str): Name of the browser to use
        headless (bool): Whether to run in headless mode
        
    Returns:
        WebDriver: Configured WebDriver instance
    """
    browser_name = browser_name.lower()
    try:
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        # Set standard window size
        driver.set_window_size(1366, 768)
        return driver
        
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {str(e)}")
        raise

def run_comprehensive_accessibility_check(url, browser='chrome', output_dir=None):
    """
    Perform a comprehensive accessibility check on a given URL.
    
    Args:
        url (str): URL to check
        browser (str): Browser to use for testing
        output_dir (str): Directory to save reports
    
    Returns:
        dict: Comprehensive accessibility report
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    # Create output directory if not specified
    if not output_dir:
        output_dir = os.path.join(os.getcwd(), 'accessibility_reports')
    os.makedirs(output_dir, exist_ok=True)
    
    # Timestamp for this run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize report
    report = {
        "url": url,
        "timestamp": timestamp,
        "browser": browser
    }
    
    # Initialize driver
    driver = None
    try:
        # Set up WebDriver
        driver = setup_driver(browser)
        
        # Navigate to URL
        start_time = time.time()
        driver.get(url)
        
        # Allow page to load
        time.sleep(3)
        
        # Run accessibility checks
        checks = [
            ("tab_order", check_tab_order, driver),
            ("focusable_elements", check_missing_focusable_elements, driver),
            ("aria_accessibility", check_aria_accessibility, driver),
            ("color_contrast", check_color_contrast, driver),
            ("image_accessibility", check_image_accessibility, driver)
        ]
        
        # Store results of individual checks
        report['checks'] = {}
        for check_name, check_func, *args in checks:
            try:
                result = check_func(*args)
                report['checks'][check_name] = result
            except Exception as e:
                logging.error(f"Error in {check_name} check: {str(e)}")
                report['checks'][check_name] = {
                    "status": "error",
                    "error": str(e)
                }
        
        # Run dynamic content testing
        dynamic_content_results = run_advanced_dynamic_content_test(driver)
        
        # Integrate dynamic content results
        report = integrate_dynamic_content_results(report, dynamic_content_results)
        
        # Calculate overall report summary
        calculate_report_summary(report)
        
        # Generate additional outputs
        generate_report_outputs(report, output_dir)
        
        return report
        
    except Exception as e:
        logging.error(f"Comprehensive accessibility check failed: {str(e)}")
        report['error'] = str(e)
        return report
    
    finally:
        # Always quit the driver
        if driver:
            driver.quit()

def calculate_report_summary(report):
    # Initialize summary
    report['summary'] = {
        'critical_issues': 0,
        'warnings': 0,
        'passed_checks': 0,
        'total_checks': 0,
        'accessibility_score': 100,
        'dynamic_content_issues': 0  # Initialize this to avoid errors
    }
    
    # Count issues across different checks
    for check_name, check_results in report.get('checks', {}).items():
        report['summary']['total_checks'] += 1
        
        # Check for issues in each module's results
        issues = check_results.get('issues', [])
        if not issues:
            report['summary']['passed_checks'] += 1
        
        # Count issue severities
        for issue in issues:
            severity = issue.get('severity', issue.get('type', 'warning'))
            if severity == 'critical':
                report['summary']['critical_issues'] += 1
            else:
                report['summary']['warnings'] += 1
    
    # Incorporate dynamic content issues - with type checking
    dynamic_content = report.get('dynamic_content', {})
    if isinstance(dynamic_content, dict):
        dynamic_content_summary = dynamic_content.get('summary', {})
        if isinstance(dynamic_content_summary, dict):
            report['summary']['dynamic_content_issues'] = dynamic_content_summary.get('components_with_issues', 0)
            dynamic_content_score = dynamic_content_summary.get('accessibility_score', 100)
        else:
            dynamic_content_score = 100  # Default if summary isn't a dict
    else:
        dynamic_content_score = 100  # Default if dynamic_content isn't a dict
    
    # Calculate final accessibility score
    # Penalize for critical and warning issues
    total_checks = report['summary']['total_checks']
    critical_issues = report['summary']['critical_issues']
    warnings = report['summary']['warnings']
    
    # Scoring algorithm
    base_score = 100
    critical_penalty = critical_issues * 10  # Each critical issue reduces score by 10
    warning_penalty = warnings * 3  # Each warning reduces score by 3
    dynamic_content_penalty = (report['summary']['dynamic_content_issues'] * 5)
    
    final_score = max(0, base_score - critical_penalty - warning_penalty - dynamic_content_penalty)
    
    # Incorporate dynamic content score
    final_score = (final_score + dynamic_content_score) / 2
    
    report['summary']['accessibility_score'] = round(final_score, 2)
    
def generate_report_outputs(report, output_dir):
    """
    Generate various output formats for the accessibility report.
    
    Args:
        report (dict): Accessibility report
        output_dir (str): Directory to save report outputs
    """
    timestamp = report.get('timestamp', datetime.now().strftime("%Y%m%d_%H%M%S"))
    base_filename = f"accessibility_report_{timestamp}"
    
    # Generate JSON report
    json_path = os.path.join(output_dir, f"{base_filename}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Generate HTML report with dynamic content section
    html_report = generate_html_report(report)
    html_path = os.path.join(output_dir, f"{base_filename}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_report)
    
    # Export state tracking information
    state_tracking = export_dynamic_content_state_tracking(report.get('dynamic_content', {}))
    state_tracking_path = os.path.join(output_dir, f"{base_filename}_state_tracking.json")
    with open(state_tracking_path, 'w', encoding='utf-8') as f:
        json.dump(state_tracking, f, indent=2, ensure_ascii=False)

def generate_html_report(report):
    """
    Generate an enhanced HTML report with CSS-based accordions.
    Safe implementation that avoids accessing lists as dictionaries.
    
    Args:
        report (dict): Accessibility report
    
    Returns:
        str: HTML report content
    """
    # Basic HTML template with enhanced styling and CSS-only accordions
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Accessibility Report for {report.get('url', 'Unknown URL')}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; }}
            h1, h2, h3 {{ color: #333; }}
            .summary {{ 
                background: #f4f4f4; 
                padding: 20px; 
                margin-bottom: 20px; 
                border-radius: 5px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            .score {{ 
                font-size: 2em; 
                font-weight: bold; 
                color: {'green' if report.get('summary', {}).get('accessibility_score', 0) >= 90 else 'orange' if report.get('summary', {}).get('accessibility_score', 0) >= 70 else 'red'};
            }}
            .check-section {{ 
                margin-bottom: 20px; 
                background: white; 
                padding: 20px; 
                border-radius: 5px; 
                box-shadow: 0 1px 3px rgba(0,0,0,0.1); 
            }}
            .issues-list {{ list-style-type: none; padding: 0; }}
            .issue-item {{ 
                margin-bottom: 10px; 
                padding: 15px; 
                border-left: 4px solid #e74c3c;
                background-color: #f9f9f9;
            }}
            .issue-title {{ font-weight: bold; margin-bottom: 5px; }}
            .issue-details {{ margin-bottom: 5px; }}
            .issue-recommendation {{ 
                font-style: italic; 
                color: #666; 
                border-left: 2px solid #3498db; 
                padding-left: 10px;
                margin: 10px 0;
            }}
            .critical {{ color: #e74c3c; }}
            .warning {{ color: #f39c12; }}
            .passed {{ color: #2ecc71; }}
            .wcag-criterion {{ 
                display: inline-block;
                background-color: #3498db;
                color: white;
                padding: 2px 6px;
                border-radius: 3px;
                font-size: 12px;
                margin-right: 5px;
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
                padding: 15px;
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
                padding: 15px;
            }}
            
            .issue-count {{
                background-color: #e74c3c;
                color: white;
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 14px;
                margin-left: 10px;
            }}
            
            .no-issues {{
                background-color: #2ecc71;
            }}
            
            .section-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 15px;
                padding-bottom: 10px;
                border-bottom: 1px solid #eee;
            }}
            
            .next-steps {{
                background-color: #f0f8ff;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
            }}
            
            .next-steps h2 {{
                color: #3498db;
            }}
            
            footer {{
                margin-top: 30px;
                padding-top: 15px;
                border-top: 1px solid #eee;
                text-align: center;
                color: #777;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <h1>Accessibility Report</h1>
        <div class="summary">
            <h2>Summary</h2>
            <p><strong>URL:</strong> {report.get('url', 'N/A')}</p>
            <p><strong>Date:</strong> {report.get('timestamp', 'N/A')}</p>
            <p><strong>Browser:</strong> {report.get('browser', 'N/A')}</p>
            <p><strong>Accessibility Score:</strong> <span class="score">{report.get('summary', {}).get('accessibility_score', 'N/A')}%</span></p>
            <p><strong>Critical Issues:</strong> {report.get('summary', {}).get('critical_issues', 0)}</p>
            <p><strong>Warnings:</strong> {report.get('summary', {}).get('warnings', 0)}</p>
            <p><strong>Passed Checks:</strong> {report.get('summary', {}).get('passed_checks', 0)} / {report.get('summary', {}).get('total_checks', 0)}</p>
            <p><strong>Dynamic Content Issues:</strong> {report.get('summary', {}).get('dynamic_content_issues', 0)}</p>
        </div>
    """
    
    # Add section for each check
    for check_name, check_data in report.get('checks', {}).items():
        # Skip if check_data is not a dictionary
        if not isinstance(check_data, dict):
            continue
            
        # Make a human-readable name
        display_name = check_name.replace('_', ' ').title()
        
        # Get issues safely
        issues = []
        if isinstance(check_data, dict):
            issues = check_data.get('issues', [])
        
        issue_count = len(issues) if isinstance(issues, list) else 0
        
        html += f"""
        <div class="check-section">
            <div class="section-header">
                <h2>{display_name}</h2>
                <span class="issue-count {'no-issues' if issue_count == 0 else ''}">
                    {issue_count} {'Issue' if issue_count == 1 else 'Issues'}
                </span>
            </div>
        """
        
        # Show status
        status = check_data.get('status', 'Unknown') if isinstance(check_data, dict) else 'Unknown'
        html += f"<p><strong>Status:</strong> {status}</p>"
        
        # Show issues if any
        if isinstance(issues, list) and len(issues) > 0:
            accordion_id = f"accordion-{check_name.replace('_', '-')}"
            
            html += f"""
            <div class="accordion">
                <input type="checkbox" id="{accordion_id}" class="accordion-checkbox">
                <label for="{accordion_id}">Show {len(issues)} Issues</label>
                <div class="accordion-content">
                    <ul class="issues-list">
            """
            
            for i, issue in enumerate(issues):
                if isinstance(issue, dict):
                    issue_title = issue.get('issue', 'Unknown Issue')
                    details = issue.get('details', '')
                    recommendation = issue.get('recommendation', '')
                    severity = issue.get('severity', 'warning')
                    wcag = issue.get('wcag', '')
                    
                    html += f"""
                    <li class="issue-item">
                        <div class="issue-title {severity}">{issue_title}</div>
                        <div class="issue-details">{details}</div>
                        <div class="issue-recommendation">{recommendation}</div>
                        {f'<div><span class="wcag-criterion">WCAG {wcag}</span></div>' if wcag else ''}
                    </li>
                    """
            
            html += """
                    </ul>
                </div>
            </div>
            """
        else:
            html += '<p class="passed">No issues detected in this check.</p>'
        
        html += "</div>"
    
    # Add dynamic content section
    if 'dynamic_content' in report and isinstance(report['dynamic_content'], dict):
        html += """
        <div class="check-section">
            <h2>Dynamic Content Analysis</h2>
        """
        
        dynamic_content = report.get('dynamic_content', {})
        summary = dynamic_content.get('summary', {})
        
        if isinstance(summary, dict):
            html += f"""
                <p><strong>Components Tested:</strong> {summary.get('total_components_tested', 0)}</p>
                <p><strong>Components with Issues:</strong> {summary.get('components_with_issues', 0)}</p>
                <p><strong>Dynamic Content Score:</strong> {summary.get('accessibility_score', 'N/A')}%</p>
            """
            
            # Add issue type counts if available
            issue_types = summary.get('issue_types', {})
            if isinstance(issue_types, dict) and issue_types:
                html += "<p><strong>Issue Types:</strong></p><ul>"
                for issue_type, count in issue_types.items():
                    html += f"<li>{issue_type}: {count}</li>"
                html += "</ul>"
        
        html += "</div>"
    
    # Add next steps section
    html += """
    <div class="next-steps">
        <h2>Next Steps</h2>
        <ol>
            <li><strong>Review the JSON report</strong> for detailed information on each issue</li>
            <li><strong>Prioritize critical issues</strong> - these have the most significant impact on accessibility</li>
            <li><strong>Address keyboard navigation barriers</strong> - ensure all interactive elements can be accessed with a keyboard</li>
            <li><strong>Fix color contrast issues</strong> - ensure text is readable against its background</li>
            <li><strong>Check image alternatives</strong> - ensure all images have appropriate text alternatives</li>
            <li><strong>Test with assistive technologies</strong> - verify fixes with screen readers and other tools</li>
        </ol>
    </div>
    
    <footer>
        <p>Generated by Accessibility Checker on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </footer>
    """
    
    html += """
    </body>
    </html>
    """
    
    return html

def main():
    """
    Command-line interface for running accessibility checks.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Web Accessibility Checker")
    parser.add_argument("url", help="URL to check for accessibility")
    parser.add_argument("--browser", choices=['chrome', 'firefox', 'edge'], 
                        default='chrome', help="Browser to use for testing")
    parser.add_argument("--output", help="Directory to save reports")
    
    args = parser.parse_args()
    
    # Run comprehensive check
    report = run_comprehensive_accessibility_check(
        args.url, 
        browser=args.browser, 
        output_dir=args.output
    )
    
    # Print summary to console
    print("\n--- Accessibility Report Summary ---")
    print(f"URL: {report.get('url', 'N/A')}")
    print(f"Accessibility Score: {report['summary'].get('accessibility_score', 'N/A')}%")
    print(f"Critical Issues: {report['summary'].get('critical_issues', 0)}")
    print(f"Warnings: {report['summary'].get('warnings', 0)}")
    print(f"Passed Checks: {report['summary'].get('passed_checks', 0)} / {report['summary'].get('total_checks', 0)}")

if __name__ == "__main__":
    main()