import json
import os

def create_terminology_file(file_path):
    """Create a terminology JSON file with default mappings"""
    terminology = {
        "tab order issue": "inconsistent keyboard navigation sequence",
        "interactive element not in tab order": "keyboard navigation barrier",
        "missing alt text": "missing text alternative"
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(terminology, f, indent=2)
        print(f"Created terminology file at: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating terminology file: {str(e)}")
        return False

# Use this function
create_terminology_file('C:\\Users\\clint\\Pickles\\accessibility_terminology.json')