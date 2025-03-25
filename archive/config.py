#!/usr/bin/env python
# coding: utf-8
from pathlib import Path

# Website to be audited
url_to_check = "https://www.sse.com"

# Browser for testing
browser_choice = "firefox"  # Options: 'chrome', 'firefox', 'edge'

# Reports directory
REPORTS_DIR = Path("accessibility_reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Logging directory
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Logging configuration
LOG_FILE = LOGS_DIR / 'accessibility_checker.log'

# Accessibility check settings
CHECKS = {
    'tab_order': True,
    'missing_focusable': True,
    'aria': True,
    'keyboard_accessibility': True,
    'non_text_content': True
}

# Issue thresholds for reporting
ISSUE_THRESHOLDS = {
    'tab_order_issues': 5,
    'missing_focusable_issues': 3,
    'aria_issues': 3,
    'keyboard_issues': 3
}

# Optional additional configurations can be added here

# Export configuration for use in other modules
__all__ = [
    'url_to_check', 
    'browser_choice', 
    'REPORTS_DIR', 
    'LOGS_DIR', 
    'CHECKS', 
    'ISSUE_THRESHOLDS'
]