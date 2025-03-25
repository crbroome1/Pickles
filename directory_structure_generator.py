#!/usr/bin/env python3
"""
Python Dependency Tree Generator

This script generates a tree-like representation of Python files that are imported (directly or indirectly)
by the primary script (accessibility_checker.py by default). This helps filter out ancillary scripts
that aren't part of the main application flow.
"""

import os
import sys
import ast
import argparse
import datetime
import importlib.util
from pathlib import Path


class ImportVisitor(ast.NodeVisitor):
    """AST visitor that collects all import statements in a Python file."""
    
    def __init__(self):
        self.imports = set()
        self.from_imports = {}
    
    def visit_Import(self, node):
        """Process regular import statements (import x, import y)."""
        for name in node.names:
            self.imports.add(name.name.split('.')[0])  # Only get the top-level module
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        """Process from import statements (from x import y)."""
        if node.level == 0:  # Absolute import
            if node.module:  # Not a relative import
                self.imports.add(node.module.split('.')[0])  # Only get the top-level module
                
                # Store what's imported from the module
                if node.module not in self.from_imports:
                    self.from_imports[node.module] = set()
                for name in node.names:
                    self.from_imports[node.module].add(name.name)
        self.generic_visit(node)


def get_file_imports(file_path):
    """Extract all imports from a Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        try:
            tree = ast.parse(file_content)
            visitor = ImportVisitor()
            visitor.visit(tree)
            return visitor.imports, visitor.from_imports
        except SyntaxError:
            print(f"Syntax error in {file_path}, skipping")
            return set(), {}
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return set(), {}


def find_module_file(module_name, search_paths):
    """Find the file path for a given module name."""
    # First, check if it's a direct .py file
    for path in search_paths:
        potential_file = os.path.join(path, f"{module_name}.py")
        if os.path.isfile(potential_file):
            return potential_file
        
        # Check if it's a module directory with __init__.py
        potential_dir = os.path.join(path, module_name)
        if os.path.isdir(potential_dir) and os.path.isfile(os.path.join(potential_dir, "__init__.py")):
            return os.path.join(potential_dir, "__init__.py")
    
    # Handle standard library and external modules
    return None


def collect_dependencies(primary_file, search_paths):
    """
    Recursively collect all dependencies of the primary file.
    
    Args:
        primary_file (str): Path to the primary Python file.
        search_paths (list): List of directories to search for modules.
        
    Returns:
        set: Set of file paths that are dependencies.
    """
    processed_files = set()
    dependencies = set()
    file_queue = [os.path.abspath(primary_file)]
    
    # Add the directory of the primary file to search paths
    primary_dir = os.path.dirname(os.path.abspath(primary_file))
    if primary_dir not in search_paths:
        search_paths.append(primary_dir)
    
    while file_queue:
        current_file = file_queue.pop(0)
        
        if current_file in processed_files:
            continue
        
        processed_files.add(current_file)
        
        # Get the directory of the current file
        current_dir = os.path.dirname(current_file)
        if current_dir not in search_paths:
            search_paths.append(current_dir)
        
        # Get imports from the current file
        imports, from_imports = get_file_imports(current_file)
        
        # Process each import
        for module_name in imports:
            # Skip standard library and external modules
            if module_name in sys.builtin_module_names or module_name in ('os', 'sys', 'time', 'datetime', 're', 'json', 'csv', 'argparse'):
                continue
            
            # Find the file for this module
            module_file = find_module_file(module_name, search_paths)
            if module_file:
                dependencies.add(module_file)
                if module_file not in processed_files:
                    file_queue.append(module_file)
                    
        # Also process the from_imports
        for module_name in from_imports:
            # Skip standard library and external modules
            top_module = module_name.split('.')[0]
            if top_module in sys.builtin_module_names or top_module in ('os', 'sys', 'time', 'datetime', 're', 'json', 'csv', 'argparse'):
                continue
            
            # Find the file for this module
            module_file = find_module_file(module_name.replace('.', os.path.sep), search_paths)
            if module_file:
                dependencies.add(module_file)
                if module_file not in processed_files:
                    file_queue.append(module_file)
    
    # Add the primary file itself to the dependencies
    dependencies.add(os.path.abspath(primary_file))
    
    return dependencies


def generate_dependency_tree(directory='.', output_file=None, primary_file="accessibility_checker.py", ignore_dirs=None):
    """
    Generate a tree showing Python files that are dependencies of the primary file.
    
    Args:
        directory (str): The directory to start from.
        output_file (file): File to write the tree to.
        primary_file (str): Name of the primary file.
        ignore_dirs (list): List of directory names to ignore.
    """
    if ignore_dirs is None:
        ignore_dirs = ['.git', '__pycache__', 'venv', '.idea', '.vscode', 'node_modules', '.pytest_cache']
    
    # Get absolute path of the primary file
    primary_path = None
    for root, _, files in os.walk(directory):
        if primary_file in files:
            primary_path = os.path.join(root, primary_file)
            break
    
    if not primary_path:
        output_file.write(f"Error: Primary file {primary_file} not found in directory {directory}\n")
        return
    
    # Define search paths for modules
    search_paths = [os.path.abspath(directory)]
    
    # Collect dependencies
    output_file.write(f"Analyzing dependencies of {primary_file}...\n\n")
    dependencies = collect_dependencies(primary_path, search_paths)
    
    # Generate tree structure
    output_file.write(f"Dependency Tree for {primary_file}\n")
    output_file.write("=" * (19 + len(primary_file)) + "\n\n")
    
    # Get root directory name
    root_dir_name = os.path.basename(os.path.abspath(directory))
    output_file.write(f"{root_dir_name}/\n")
    
    # Keep track of processed subdirectories to avoid duplication
    processed_dirs = set()
    
    # Sort dependencies by their path for a consistent output
    sorted_deps = sorted(dependencies)
    
    # Build the tree structure
    for dependency in sorted_deps:
        # Get relative path from the root directory
        try:
            rel_path = os.path.relpath(dependency, directory)
        except ValueError:
            # If files are on different drives or there's another path issue
            continue
        
        # Skip if the dependency is outside the starting directory
        if rel_path.startswith('..'):
            continue
        
        # Split the path into components
        path_parts = rel_path.split(os.path.sep)
        
        # Process each level of the path
        for i in range(len(path_parts)):
            # Build the partial path up to this level
            partial_path = os.path.sep.join(path_parts[:i+1])
            
            # Skip if already processed this directory
            if i < len(path_parts) - 1:  # This is a directory
                if partial_path in processed_dirs:
                    continue
                processed_dirs.add(partial_path)
            
            # Calculate the prefix for proper indentation
            prefix = "│   " * i
            
            # The last part is the filename or the last directory
            item = path_parts[i]
            
            # Determine if it's the primary file
            is_primary = (dependency == primary_path)
            
            # Format the line
            if i == len(path_parts) - 1:  # This is a file (the last part)
                if is_primary:
                    line = f"{prefix}└── {item}     # Main script\n"
                else:
                    line = f"{prefix}└── {item}\n"
            else:  # This is a directory
                line = f"{prefix}├── {item}/\n"
            
            output_file.write(line)


def main():
    """Parse command-line arguments and run the dependency tree generator."""
    parser = argparse.ArgumentParser(description='Generate a tree of Python dependencies of the primary file.')
    parser.add_argument('-d', '--directory', default='.', help='Directory to start from (default: current directory)')
    parser.add_argument('-p', '--primary', default='accessibility_checker.py', help='Primary Python file')
    parser.add_argument('--ignore-dirs', nargs='+', help='Additional directories to ignore')
    
    args = parser.parse_args()
    
    # Create timestamp for filename
    timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
    output_filename = f"file_structure_{timestamp}.txt"
    
    # Build ignore_dirs list
    default_ignore = ['.git', '__pycache__', 'venv', '.idea', '.vscode', 'node_modules', '.pytest_cache']
    if args.ignore_dirs:
        ignore_dirs = default_ignore + args.ignore_dirs
    else:
        ignore_dirs = default_ignore
    
    # Open output file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        generate_dependency_tree(
            directory=args.directory,
            output_file=output_file,
            primary_file=args.primary,
            ignore_dirs=ignore_dirs
        )
        
        # Add timestamp at the bottom
        output_file.write(f"\nGenerated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"Dependency tree has been saved to: {output_filename}")


if __name__ == '__main__':
    main()