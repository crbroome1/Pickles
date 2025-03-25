"""
Enhanced Accessibility Checker with Dynamic Content Testing and Simplified Reporting

Integrates comprehensive accessibility checks including dynamic content analysis.
Uses a simplified CSS-only reporting mechanism for better browser compatibility.
"""

import os
import sys
import logging
import time
import json
import traceback
from datetime import datetime
from urllib.parse import urlparse

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

# Import the simplified report generator
from accessibility_modules.simplified_report_generator import generate_simplified_html_report

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
        
        # Run dynamic content testing with careful error handling
        try:
            # Run dynamic content testing
            dynamic_content_results = run_advanced_dynamic_content_test(driver)
            logging.info("Dynamic content testing completed")
            
            # Integrate dynamic content results with careful error handling
            try:
                report = integrate_dynamic_content_results(report, dynamic_content_results)
                logging.info("Dynamic content integration completed")
            except Exception as e:
                logging.error(f"Error integrating dynamic content results: {str(e)}")
                report['dynamic_content_error'] = str(e)
        except Exception as e:
            logging.error(f"Error in dynamic content testing: {str(e)}")
            report['dynamic_content_error'] = str(e)
        
        # Calculate overall report summary
        try:
            calculate_report_summary(report)
            logging.info("Report summary calculated")
        except Exception as e:
            logging.error(f"Error calculating report summary: {str(e)}")
            report['summary_error'] = str(e)
            # Create a minimal summary to avoid further errors
            report['summary'] = {
                'critical_issues': 0,
                'warnings': 0,
                'passed_checks': 0,
                'total_checks': 0,
                'accessibility_score': 100
            }
        
        # Generate report outputs
        try:
            generate_report_outputs(report, output_dir)
            logging.info("Report outputs generated")
        except Exception as e:
            logging.error(f"Error generating report outputs: {str(e)}")
            report['output_error'] = str(e)
        
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
    """
    Calculate an overall accessibility summary for the report.
    Simplified version with improved error handling.
    
    Args:
        report (dict): Accessibility report to summarize
    """
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
        if isinstance(check_results, dict):
            issues = check_results.get('issues', [])
            if not issues:
                report['summary']['passed_checks'] += 1
            
            # Count issue severities
            for issue in issues:
                if isinstance(issue, dict):
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
    Generates both JSON and HTML reports.
    
    Args:
        report (dict): Accessibility report
        output_dir (str): Directory to save report outputs
    """
    timestamp = report.get('timestamp', datetime.now().strftime("%Y%m%d_%H%M%S"))
    base_filename = f"accessibility_report_{timestamp}"
    
    # Generate JSON report using a custom encoder to handle non-serializable objects
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            try:
                return super().default(obj)
            except:
                return str(obj)
    
    json_path = os.path.join(output_dir, f"{base_filename}.json")
    try:
        # First, clean the report of any non-serializable objects
        clean_report = clean_report_for_export(report)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(clean_report, f, indent=2, ensure_ascii=False, cls=CustomEncoder)
        
        logging.info(f"JSON report saved to: {json_path}")
    except Exception as e:
        logging.error(f"Error saving JSON report: {str(e)}")
    
    # Generate simplified HTML report as primary option
    try:
        html_path = generate_simplified_html_report(report, output_dir)
        logging.info(f"Simplified HTML report saved to: {html_path}")
    except Exception as e:
        logging.error(f"Error generating simplified HTML report: {str(e)}")
        
        # Fall back to basic HTML report if simplified version fails
        try:
            basic_html_report = generate_basic_html_report(report)
            basic_html_path = os.path.join(output_dir, f"{base_filename}_basic.html")
            with open(basic_html_path, 'w', encoding='utf-8') as f:
                f.write(basic_html_report)
            logging.info(f"Basic HTML report saved to: {basic_html_path}")
        except Exception as inner_e:
            logging.error(f"Error generating basic HTML report: {str(inner_e)}")
    
    # Export state tracking information for dynamic content if available
    try:
        if 'dynamic_content' in report:
            state_tracking = export_dynamic_content_state_tracking(report.get('dynamic_content', {}))
            state_tracking_path = os.path.join(output_dir, f"{base_filename}_state_tracking.json")
            with open(state_tracking_path, 'w', encoding='utf-8') as f:
                json.dump(state_tracking, f, indent=2, ensure_ascii=False, cls=CustomEncoder)
            logging.info(f"State tracking information saved to: {state_tracking_path}")
    except Exception as e:
        logging.error(f"Error exporting state tracking: {str(e)}")

def clean_report_for_export(report):
    """
    Create a clean copy of the report with no non-serializable objects.
    
    Args:
        report (dict): The original report
    
    Returns:
        dict: A cleaned version safe for JSON export
    """
    # Helper function to recursively clean objects
    def clean(obj):
        if isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                # Skip any reference to WebDriver elements or other complex objects
                if k == 'element':
                    continue
                result[k] = clean(v)
            return result
        elif isinstance(obj, list):
            return [clean(item) for item in obj]
        # Convert any non-standard object to string
        try:
            json.dumps(obj)
            return obj
        except (TypeError, OverflowError):
            return str(obj)
    
    return clean(report)

def generate_basic_html_report(report):
    """
    Generate a minimal HTML report without any complex styling or interactivity.
    Used as a fallback if the other report generators fail.
    
    Args:
        report (dict): Accessibility report
    
    Returns:
        str: Simple HTML report content
    """
    # Basic HTML template with minimal styling
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Basic Accessibility Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
            h1, h2 {{ color: #333; }}
            .summary {{ background: #f4f4f4; padding: 15px; margin-bottom: 20px; }}
            .issue {{ margin-bottom: 15px; padding: 10px; border-left: 3px solid #999; }}
            .critical {{ border-left-color: #c00; }}
            .warning {{ border-left-color: #f90; }}
        </style>
    </head>
    <body>
        <h1>Accessibility Report for {report.get('url', 'Unknown URL')}</h1>
        <div class="summary">
            <h2>Summary</h2>
            <p><strong>URL:</strong> {report.get('url', 'N/A')}</p>
            <p><strong>Date:</strong> {report.get('timestamp', 'N/A')}</p>
            <p><strong>Browser:</strong> {report.get('browser', 'N/A')}</p>
            <p><strong>Accessibility Score:</strong> {report.get('summary', {}).get('accessibility_score', 'N/A')}%</p>
            <p><strong>Critical Issues:</strong> {report.get('summary', {}).get('critical_issues', 0)}</p>
            <p><strong>Warnings:</strong> {report.get('summary', {}).get('warnings', 0)}</p>
            <p><strong>Passed Checks:</strong> {report.get('summary', {}).get('passed_checks', 0)} / {report.get('summary', {}).get('total_checks', 0)}</p>
        </div>
        
        <h2>Accessibility Issues</h2>
    """
    
    # Add issues from all checks
    for check_name, check_data in report.get('checks', {}).items():
        if isinstance(check_data, dict) and 'issues' in check_data:
            issues = check_data.get('issues', [])
            if issues:
                html += f"<h3>{check_name.replace('_', ' ').title()}</h3>"
                
                for issue in issues:
                    if isinstance(issue, dict):
                        severity = issue.get('severity', 'warning')
                        title = issue.get('issue', 'Unknown Issue')
                        details = issue.get('details', '')
                        recommendation = issue.get('recommendation', '')
                        
                        html += f"""
                        <div class="issue {severity}">
                            <p><strong>{title}</strong></p>
                            <p>{details}</p>
                            {f'<p><strong>Recommendation:</strong> {recommendation}</p>' if recommendation else ''}
                        </div>
                        """
    
    # Close the HTML document
    html += """
        <p>For a more detailed report, please refer to the JSON report file.</p>
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
    print(f"Report saved to: {args.output or os.path.join(os.getcwd(), 'accessibility_reports')}")

if __name__ == "__main__":
    main()