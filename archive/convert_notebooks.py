#!/usr/bin/env python3

import os
import subprocess
import sys

def convert_notebooks(directory):
    """
    Convert all Jupyter Notebook files in the specified directory to Python scripts.
    
    Args:
        directory (str): Path to the directory containing Jupyter Notebook files
    """
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)
    
    # Counter for converted notebooks
    converted_count = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a Jupyter Notebook
        if filename.endswith('.ipynb'):
            # Full path to the notebook
            notebook_path = os.path.join(directory, filename)
            
            try:
                # Run jupyter nbconvert command
                result = subprocess.run([
                    'jupyter', 'nbconvert', 
                    '--to', 'script', 
                    notebook_path
                ], capture_output=True, text=True)
                
                # Check if conversion was successful
                if result.returncode == 0:
                    print(f"Converted: {filename}")
                    converted_count += 1
                else:
                    print(f"Failed to convert {filename}")
                    print(f"Error: {result.stderr}")
            
            except Exception as e:
                print(f"Error converting {filename}: {e}")
    
    # Print summary
    print(f"\nTotal notebooks converted: {converted_count}")

def main():
    # Default directory
    default_directory = 'Pickles'
    
    # Allow directory to be specified as a command-line argument
    directory = sys.argv[1] if len(sys.argv) > 1 else default_directory
    
    print(f"Converting notebooks in directory: {directory}")
    convert_notebooks(directory)

if __name__ == "__main__":
    main()