#!/usr/bin/env python
# coding: utf-8

import sys
import os
import importlib
import argparse
from pathlib import Path

# Add current directory to Python path to ensure module imports work
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(current_dir / 'accessibility_checker.log'),
        logging.StreamHandler()
    ]
)

# Available modules for accessibility checking
AVAILABLE_MODULES = {
    'tab_order': 'missing_focusable_elements',
    'missing_focusable': 'missing_focusable_elements',
    'generate_report': 'generate_accessibility_report',
    'aria_check': 'generate_accessibility_report'
}

def import_module(module_name):
    """
    Dynamically import a module by name.

    Args:
        module_name (str): Name of the module to import

    Returns:
        module: Imported module or None if import fails
    """
    try:
        # Normalize the module name (convert to lowercase, remove any IPython remnants)
        normalized_name = module_name.lower().replace('ipython.', '')

        # Try importing from the predefined module names
        if normalized_name in AVAILABLE_MODULES:
            module_path = AVAILABLE_MODULES[normalized_name]
            logging.info(f"Attempting to import module: {module_path}")
            return importlib.import_module(module_path)

        # Try importing the exact module name provided
        logging.info(f"Attempting to import module directly: {normalized_name}")
        return importlib.import_module(normalized_name)
    except ImportError as e:
        logging.error(f"Could not import module '{module_name}': {e}")
        print(f"❌ Could not import module '{module_name}': {e}")
        # Print additional context about available modules
        print("Available modules:", list(sys.modules.keys()))
        return None

def run_tab_order_check(url, browser='chrome'):
    """
    Run tab order accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Tab order check module not available.")
    return None

def run_missing_focusable_check(url, browser='chrome'):
    """
    Run missing focusable elements check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('missing_focusable_elements')
    if module and hasattr(module, 'check_missing_focusable'):
        return module.check_missing_focusable(url, browser)
    print("❌ Missing focusable elements check module not available.")
    return None

def generate_comprehensive_report(url):
    """
    Generate a comprehensive accessibility report.

    Args:
        url (str): Website URL to generate report for
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ Report generation module not available.")
    return None

def run_aria_check(url, browser='chrome'):
    """
    Run ARIA and keyboard accessibility check.

    Args:
        url (str): Website URL to check
        browser (str, optional): Browser to use. Defaults to 'chrome'.
    """
    module = import_module('generate_accessibility_report')
    if module and hasattr(module, 'generate_accessibility_report'):
        return module.generate_accessibility_report(url)
    print("❌ ARIA and keyboard accessibility check module not available.")
    return None

def main():
    """
    Main entry point for the Accessibility Checker.
    """
    # Import URL from config
    from config import url_to_check

    parser = argparse.ArgumentParser(description="Accessibility Checker - Comprehensive Web Accessibility Testing Tool")

    # Add arguments
    parser.add_argument('--url', help='Website URL to check', default=url_to_check)
    parser.add_argument('--browser', default='chrome',
                        choices=['chrome', 'firefox', 'edge'],
                        help='Browser to use for testing (default: chrome)')
    parser.add_argument('--check', choices=['tab_order', 'missing_focusable', 'aria', 'report', 'all'],
                        default='all',
                        help='Specific type of accessibility check to run')

    # Parse arguments
    args = parser.parse_args()

    # Welcome message
    print("=" * 60)
    print("🌐 Accessibility Checker")
    print("=" * 60)
    print(f"Checking URL: {args.url}")
    print(f"Browser: {args.browser}")
    print("=" * 60)

    # Run specific or all checks
    try:
        if args.check in ['tab_order', 'all']:
            print("\n📊 Running Tab Order Check...")
            tab_order_result = run_tab_order_check(args.url, args.browser)

        if args.check in ['missing_focusable', 'all']:
            print("\n🕵️ Checking Missing Focusable Elements...")
            missing_focusable_result = run_missing_focusable_check(args.url, args.browser)

        if args.check in ['aria', 'all']:
            print("\n♿ Running ARIA and Keyboard Accessibility Check...")
            aria_result = run_aria_check(args.url, args.browser)

        if args.check in ['report', 'all']:
            print("\n📄 Generating Comprehensive Report...")
            report = generate_comprehensive_report(args.url)

        print("\n" + "=" * 60)
        print("✅ Accessibility Check Complete")
        print("=" * 60)

    except Exception as e:
        logging.error(f"An error occurred during the accessibility check: {e}")
        print(f"\n❌ An error occurred during the accessibility check: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()