#!/usr/bin/env python
# coding: utf-8


import os
import json
from pathlib import Path
from datetime import datetime
import re

class AccessibilityTerminologyValidator:
    """
    Manages and validates accessibility terminology across project scripts.
    """
    def __init__(self, terminology_file='accessibility_terminology.json'):
        self.terminology_file = terminology_file
        self.terminology = self._load_terminology()
    
    def _load_terminology(self):
        """
        Load or create a default terminology mapping.
        """
        if os.path.exists(self.terminology_file):
            with open(self.terminology_file, 'r') as f:
                return json.load(f)
        
        # Default terminology mapping
        default_terminology = {
            "technical_terms": {
                "interactive element not in tab order": {
                    "preferred": "Keyboard navigation barrier",
                    "explanation": "Elements that appear interactive but cannot be accessed via keyboard"
                },
                "tab order issue": {
                    "preferred": "Inconsistent keyboard navigation sequence",
                    "explanation": "Elements that disrupt the expected keyboard navigation flow"
                }
            },
            "impact_categories": [
                "Screen Reader Accessibility",
                "Keyboard Navigation",
                "Visual Focus",
                "Interactive Element Accessibility"
            ]
        }
        
        # Save default terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(default_terminology, f, indent=2)
        
        return default_terminology
    
    def validate_terminology(self, text):
        """
        Validate and potentially replace technical terms with more descriptive language.
        
        Args:
            text (str): The text to validate
        
        Returns:
            str: Validated and potentially modified text
        """
        for technical_term, replacement in self.terminology['technical_terms'].items():
            if technical_term.lower() in text.lower():
                text = text.replace(technical_term, replacement['preferred'])
        
        return text
    
    def update_terminology(self, technical_term, preferred_term, explanation):
        """
        Update the terminology mapping.
        
        Args:
            technical_term (str): The technical term to replace
            preferred_term (str): The preferred, more descriptive term
            explanation (str): Context or explanation for the term
        """
        self.terminology['technical_terms'][technical_term] = {
            "preferred": preferred_term,
            "explanation": explanation
        }
        
        # Save updated terminology
        with open(self.terminology_file, 'w') as f:
            json.dump(self.terminology, f, indent=2)

def extract_code_from_notebook(notebook_path, terminology_validator=None):
    """
    Extract code from notebook with optional terminology validation.
    
    Args:
        notebook_path (str): Path to the Jupyter notebook
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code snippets
    """
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    
    code_snippets = []
    for index, cell in enumerate(code_cells, start=1):
        code = ''.join(cell['source'])
        
        # Validate terminology if validator is provided
        if terminology_validator:
            code = _validate_code_terminology(code, terminology_validator)
        
        code_snippets.append(f"#### Cell {index}\n```python\n{code}\n```")

    return '\n'.join(code_snippets)

def extract_code_from_python_file(file_path, terminology_validator=None):
    """
    Extract code from Python file with optional terminology validation.
    
    Args:
        file_path (str): Path to the Python file
        terminology_validator (AccessibilityTerminologyValidator, optional): 
            Validator to check and standardize terminology
    
    Returns:
        str: Extracted and validated code 
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    # Validate terminology if validator is provided
    if terminology_validator:
        code = _validate_code_terminology(code, terminology_validator)
    
    return f"```python\n{code}\n```"

def extract_content_from_text_file(file_path):
    """
    Extract content from text file (README, TXT, etc.).
    
    Args:
        file_path (str): Path to the text file
    
    Returns:
        str: Extracted content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    
    return f"```\n{content}\n```"

def extract_content_from_json_file(file_path):
    """
    Extract and format content from JSON file.
    
    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        str: Extracted and formatted JSON content
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        try:
            json_data = json.load(file)
            # Pretty-print the JSON with indentation
            content = json.dumps(json_data, indent=2)
        except json.JSONDecodeError:
            # If JSON is invalid, return it as plain text
            file.seek(0)  # Reset file pointer to beginning
            content = file.read()
    
    return f"```json\n{content}\n```"

def _validate_code_terminology(code, terminology_validator):
    """
    Validate and potentially modify code terminology.
    
    Args:
        code (str): The code to validate
        terminology_validator (AccessibilityTerminologyValidator): 
            Validator to check and standardize terminology
    
    Returns:
        str: Validated code
    """
    # Split code into lines and validate each line
    validated_lines = []
    for line in code.split('\n'):
        validated_line = terminology_validator.validate_terminology(line)
        validated_lines.append(validated_line)
    
    return '\n'.join(validated_lines)

def is_archive_path(path):
    """
    Check if a path contains archive-related directories or is a checkpoint file.
    
    Args:
        path (Path): The path to check
    
    Returns:
        bool: True if path is in an archive or is a checkpoint, False otherwise
    """
    # Check for archive directories
    archive_keywords = ['archive', 'archived', 'backup', 'old']
    path_parts = str(path).lower().split(os.sep)
    is_archive = any(keyword in part for part in path_parts for keyword in archive_keywords)
    
    # Check for .ipynb_checkpoints directory
    is_checkpoint = '.ipynb_checkpoints' in str(path)
    
    # Check for checkpoint files (which end with -checkpoint.py)
    is_checkpoint_file = str(path).endswith('-checkpoint.py')
    
    return is_archive or is_checkpoint or is_checkpoint_file

def is_main_folder_file(base_path, file_path):
    """
    Check if a file is directly in the main folder (not in subdirectories).
    
    Args:
        base_path (Path): The base project path
        file_path (Path): The file path to check
    
    Returns:
        bool: True if file is in the main folder, False otherwise
    """
    return file_path.parent == base_path

def generate_markdown_file(folder_path):
    # Initialize terminology validator
    terminology_validator = AccessibilityTerminologyValidator()
    
    # Use rglob to find files in the folder and all subfolders
    base_path = Path(folder_path)
    
    # Find all files but filter out those in archive directories
    all_files = [(f, f.suffix.lower()) for f in base_path.rglob('*') if f.is_file() and not is_archive_path(f)]
    
    # Filter files by type and location
    # Exclude .ipynb files
    notebook_files = []  # Empty list as we're no longer including notebook files
    python_files = [f for f, ext in all_files if ext == '.py']
    
    # Only include .txt files directly in the main folder (not in subdirectories)
    text_files = [f for f, ext in all_files if ext == '.txt' and is_main_folder_file(base_path, f)]
    
    # Only include .json files directly in the main folder (not in subdirectories)
    json_files = [f for f, ext in all_files if ext == '.json' and is_main_folder_file(base_path, f)]
    
    # Filter out .md files completely
    # No need to collect them since we're excluding them entirely
    
    # Find README files (README.md, README.txt, etc.)
    readme_files = []
    for pattern in ['README.md', 'README.txt', 'README', 'readme.md', 'readme.txt', 'readme']:
        readme_files.extend([f for f in base_path.rglob(pattern) if not is_archive_path(f)])
    
    # Remove README.txt files from text_files to avoid duplication
    text_files = [f for f in text_files if f not in readme_files]

    markdown_content = f"# Project Scripts Overview\n"
    markdown_content += f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from folder: {folder_path}*\n"
    markdown_content += "*This is a project containing Jupyter Notebooks, Python scripts, and README files. The following content provides context for continuing development.*\n"
    markdown_content += "\n## Accessibility Terminology\n"
    
    # Add terminology section to markdown
    for term, details in terminology_validator.terminology['technical_terms'].items():
        markdown_content += f"- **{term}**\n"
        markdown_content += f"  - Preferred: {details['preferred']}\n"
        markdown_content += f"  - Explanation: {details['explanation']}\n"
    
    markdown_content += "\n## How to Continue This Project with Claude\n"
    markdown_content += "1. Upload or copy the contents of this entire markdown file to Claude\n"
    markdown_content += "2. Tell Claude: \"These are the files from my project. I'd like to continue working on [specific task].\"\n"
    markdown_content += "3. Reference specific scripts or code blocks by their section names when asking questions\n"
    markdown_content += "\n*The structured format below will help Claude understand your project's organization and codebase.*"

    # Table of Contents
    markdown_content += "\n## Table of Contents\n"
    
    # Add README files to TOC
    if readme_files:
        markdown_content += "### README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Removed Jupyter Notebooks TOC section since we're no longer including them
    
    # Add Python files to TOC
    if python_files:
        markdown_content += "\n### Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add Text files to TOC (only main folder)
    if text_files:
        markdown_content += "\n### Text Files (Main Folder Only)\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"
    
    # Add JSON files to TOC (only main folder)
    if json_files:
        markdown_content += "\n### JSON Files (Main Folder Only)\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"- [{rel_path}](#{section_id})\n"

    # Add README content
    if readme_files:
        markdown_content += "\n## README Files\n"
        for readme_file in readme_files:
            rel_path = readme_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: README\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(readme_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(readme_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(readme_file)

    # Removed Jupyter Notebooks content section since we're no longer including them

    # Add Python file content
    if python_files:
        markdown_content += "\n## Python Scripts\n"
        for python_file in python_files:
            rel_path = python_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Python Script\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(python_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(python_file)} bytes\n"
            markdown_content += "\n#### Code\n"
            markdown_content += extract_code_from_python_file(python_file, terminology_validator)
    
    # Add Text file content (only main folder)
    if text_files:
        markdown_content += "\n## Text Files (Main Folder Only)\n"
        for text_file in text_files:
            rel_path = text_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: Text File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(text_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(text_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_text_file(text_file)
    
    # Add JSON file content (only main folder)
    if json_files:
        markdown_content += "\n## JSON Files (Main Folder Only)\n"
        for json_file in json_files:
            rel_path = json_file.relative_to(base_path)
            section_id = str(rel_path).replace('/', '_').replace('\\', '_').replace('.', '_')
            markdown_content += f"\n### {rel_path} <a id='{section_id}'></a>\n"
            markdown_content += f"#### File Information\n"
            markdown_content += f"- **Type**: JSON File\n"
            markdown_content += f"- **Path**: {rel_path}\n"
            markdown_content += f"- **Last Modified**: {datetime.fromtimestamp(os.path.getmtime(json_file)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            markdown_content += f"- **Size**: {os.path.getsize(json_file)} bytes\n"
            markdown_content += "\n#### Content\n"
            markdown_content += extract_content_from_json_file(json_file)

    return markdown_content

# Usage
folder_path = r'C:\Users\clint\Pickles'  # Replace with the path to your project folder
markdown_content = generate_markdown_file(folder_path)

# Create the "Markdowns" folder if it doesn't exist
markdown_folder = 'Markdowns'
Path(markdown_folder).mkdir(exist_ok=True)

# Generate a timestamp for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Save the markdown content to a file with timestamp in the "Markdowns" folder
output_file = Path(markdown_folder) / f'project_overview_{timestamp}.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"Markdown file '{output_file}' generated successfully.")