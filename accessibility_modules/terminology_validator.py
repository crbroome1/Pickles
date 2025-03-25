"""
Accessibility Terminology Validator
Ensures consistent terminology is used throughout the accessibility checker.
"""

import re
import json
import os
import logging

class AccessibilityTerminologyValidator:
    """
    Validates and standardizes accessibility terminology used in reports and issue descriptions.
    Uses a central terminology mapping to ensure consistency.
    """
    
    def __init__(self, terminology_file=None):
        """
        Initialize the terminology validator.
        
        Args:
            terminology_file: Path to a JSON file containing terminology mappings
        """
        self.terminology_mapping = {
            # Default terminology mappings
            "tab order issue": "inconsistent keyboard navigation sequence",
            "interactive element not in tab order": "keyboard navigation barrier",
            "missing alt": "missing text alternative",
            "missing alt text": "missing text alternative",
            "alt text missing": "missing text alternative",
            "no alt": "missing text alternative",
            "no alt text": "missing text alternative",
            "alt attribute missing": "missing text alternative",
            "empty alt": "empty text alternative",
            "bad alt": "inadequate text alternative",
            "poor alt": "inadequate text alternative",
            "inadequate alt": "inadequate text alternative",
            "inappropriate alt": "inadequate text alternative",
            "insufficient alt": "inadequate text alternative",
            "incorrect alt": "inadequate text alternative",
            "wrong alt": "inadequate text alternative",
            "missing label": "form control without label",
            "unlabeled": "form control without label",
            "no label": "form control without label",
            "contrast issue": "insufficient color contrast",
            "low contrast": "insufficient color contrast",
            "poor contrast": "insufficient color contrast",
            "contrast problem": "insufficient color contrast",
            "contrast error": "insufficient color contrast",
            "color contrast issue": "insufficient color contrast",
            "color contrast problem": "insufficient color contrast",
            "color contrast error": "insufficient color contrast",
            "keyboard trap": "keyboard navigation barrier",
            "focus trap": "keyboard navigation barrier",
            "focus issue": "keyboard navigation barrier",
            "focus problem": "keyboard navigation barrier",
            "focus error": "keyboard navigation barrier",
            "keyboard issue": "keyboard navigation barrier",
            "keyboard problem": "keyboard navigation barrier",
            "keyboard error": "keyboard navigation barrier",
            "missing aria": "incomplete ARIA implementation",
            "incorrect aria": "incomplete ARIA implementation",
            "aria issue": "incomplete ARIA implementation",
            "aria problem": "incomplete ARIA implementation",
            "aria error": "incomplete ARIA implementation",
            "aria-label missing": "incomplete ARIA implementation",
            "aria-labelledby missing": "incomplete ARIA implementation",
            "aria-describedby missing": "incomplete ARIA implementation",
            "missing landmark": "missing page structure landmarks",
            "landmark issue": "missing page structure landmarks",
            "landmark problem": "missing page structure landmarks",
            "landmark error": "missing page structure landmarks",
            "heading issue": "improper heading structure",
            "heading problem": "improper heading structure",
            "heading error": "improper heading structure",
            "heading structure issue": "improper heading structure",
            "missing heading": "improper heading structure",
            "heading level skipped": "improper heading structure",
            "heading level issue": "improper heading structure"
        }
        
        # Load additional or override terminology from file if provided
        if terminology_file and os.path.exists(terminology_file):
            try:
                with open(terminology_file, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
            except Exception as e:
                logging.error(f"Error loading terminology file: {str(e)}")
    
    def standardize_terminology(self, text):
        """
        Standardize terminology in the provided text.
        
        Args:
            text: The text to standardize
            
        Returns:
            str: Text with standardized terminology
        """
        if not text:
            return text
            
        standardized_text = text
        
        # Apply each terminology mapping
        for incorrect, correct in self.terminology_mapping.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(incorrect), re.IGNORECASE)
            standardized_text = pattern.sub(correct, standardized_text)
        
        return standardized_text
    
    def validate_report_terminology(self, report):
        """
        Validate and standardize terminology in an accessibility report.
        
        Args:
            report: Dictionary containing accessibility report data
            
        Returns:
            dict: Report with standardized terminology
        """
        if not report or not isinstance(report, dict):
            return report
            
        # Create a copy of the report to avoid modifying the original
        validated_report = report.copy()
        
        # Process issues
        if "issues" in validated_report:
            for i, issue in enumerate(validated_report["issues"]):
                if "issue" in issue:
                    issue["issue"] = self.standardize_terminology(issue["issue"])
                if "details" in issue:
                    issue["details"] = self.standardize_terminology(issue["details"])
                if "recommendation" in issue:
                    issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        # Process checks
        if "checks" in validated_report:
            for check_name, check_data in validated_report["checks"].items():
                if isinstance(check_data, dict) and "issues" in check_data:
                    for i, issue in enumerate(check_data["issues"]):
                        if isinstance(issue, dict):
                            if "issue" in issue:
                                issue["issue"] = self.standardize_terminology(issue["issue"])
                            if "details" in issue:
                                issue["details"] = self.standardize_terminology(issue["details"])
                            if "recommendation" in issue:
                                issue["recommendation"] = self.standardize_terminology(issue["recommendation"])
        
        return validated_report
    
    def load_terminology_file(self, file_path):
        """
        Load terminology mappings from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    custom_terminology = json.load(f)
                    self.terminology_mapping.update(custom_terminology)
                    logging.info(f"Loaded {len(custom_terminology)} custom terminology mappings")
                return True
            else:
                logging.error(f"Terminology file not found: {file_path}")
                return False
        except Exception as e:
            logging.error(f"Error loading terminology file: {str(e)}")
            return False
    
    def save_terminology_file(self, file_path):
        """
        Save the current terminology mappings to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.terminology_mapping, f, indent=4, sort_keys=True)
                
            logging.info(f"Saved {len(self.terminology_mapping)} terminology mappings to {file_path}")
            return True
        except Exception as e:
            logging.error(f"Error saving terminology file: {str(e)}")
            return False
    
    def add_terminology_mapping(self, incorrect, correct):
        """
        Add a new terminology mapping.
        
        Args:
            incorrect: The incorrect or inconsistent term
            correct: The preferred term to use instead
            
        Returns:
            bool: True if added successfully
        """
        if not incorrect or not correct:
            return False
            
        self.terminology_mapping[incorrect.lower()] = correct.lower()
        return True
    
    def remove_terminology_mapping(self, incorrect):
        """
        Remove a terminology mapping.
        
        Args:
            incorrect: The incorrect term to remove from mappings
            
        Returns:
            bool: True if removed, False if not found
        """
        if incorrect and incorrect.lower() in self.terminology_mapping:
            del self.terminology_mapping[incorrect.lower()]
            return True
        return False