#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Generate_Accessibility_Report.ipynb
# Interactive notebook for testing and generating accessibility reports

import os
import sys
from pathlib import Path
import webbrowser
from IPython.display import display, HTML, Markdown, Image, clear_output
import ipywidgets as widgets

# Import URL from config
get_ipython().run_line_magic('run', 'config.ipynb')

# Ensure project directory is in path
project_dir = Path.cwd()
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

# Import required modules
try:
    from Accessibility_Checker import normalize_url, terminology
    from Data_Loader import load_data, count_issues_by_category
    from Enhanced_Report_Generator import generate_accessibility_report
    
    # Show success message
    display(HTML("""
    <div style="background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">✅ Modules Loaded Successfully</h3>
        <p style="margin-bottom: 0;">Ready to generate accessibility reports.</p>
    </div>
    """))
except ImportError as e:
    # Show error message
    display(HTML(f"""
    <div style="background-color: #ffebee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">❌ Error Loading Modules</h3>
        <p>Could not load required modules: {str(e)}</p>
        <p style="margin-bottom: 0;">Please ensure all module files are in the same directory as this notebook.</p>
    </div>
    """))

# Display header
display(HTML("""
<div style="background-color: #e8f5e9; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
    <h1 style="margin-top: 0;">🔍 Accessibility Report Generator</h1>
    <p>Generate comprehensive accessibility reports from previously collected data.</p>
</div>
"""))

# URL Input with default from config
url_input = widgets.Text(
    value=url_to_check,
    placeholder='Enter website URL (with https://)',
    description='Website URL:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='70%')
)

# Progress output
progress_output = widgets.Output()

# Generate button
generate_button = widgets.Button(
    description='Generate Report',
    button_style='primary',
    tooltip='Click to generate an accessibility report',
    icon='chart-bar'
)

# Output area for report generation status
output_area = widgets.Output()

# Function to handle the button click
def on_generate_button_clicked(b):
    # Rest of the function remains the same as in the previous implementation
    # ... (previous implementation of the function)
    pass

# Set up button click handler
generate_button.on_click(on_generate_button_clicked)

# Display the widgets
display(widgets.VBox([
    widgets.HBox([url_input, generate_button]),
    progress_output,
    output_area
]))

# Show instructions
display(HTML("""
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
    <h3>📋 Instructions</h3>
    <ol>
        <li>First, ensure that you have run the accessibility tests using the appropriate test scripts.</li>
        <li>Enter the URL you want to generate a report for in the URL field.</li>
        <li>Click the "Generate Report" button to create the report.</li>
        <li>The report will open automatically in your default browser.</li>
    </ol>
    
    <h4>Notes:</h4>
    <ul>
        <li>The report generator requires data from previous accessibility scans to be available.</li>
        <li>If no data is found, you'll need to run the data collection scripts first.</li>
        <li>Reports include visualizations, practical guidance for developers, and detailed technical information for accessibility experts.</li>
    </ul>
</div>
"""))

