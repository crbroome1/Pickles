"""
Enhanced Accessibility Report Generator

Incorporates advanced dynamic content testing results into comprehensive reports.
"""

import json
import logging
from datetime import datetime

def integrate_dynamic_content_results(report, dynamic_content_results):
    """
    Integrate dynamic content testing results into the main accessibility report.
    
    Args:
        report: Main accessibility report dictionary
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        Updated report with dynamic content insights
    """
    # Ensure dynamic content section exists
    report['dynamic_content'] = {
        'summary': {
            'total_components_tested': 0,
            'components_with_issues': 0,
            'issue_types': {}
        },
        'detailed_results': dynamic_content_results
    }
    
    # Analyze and summarize issues
    for component_type, component_results in dynamic_content_results.items():
        if component_type == 'state_tracking' or component_type == 'error':
            continue  # Skip state tracking export and error info
            
        # Make sure component_results is a list
        if not isinstance(component_results, list):
            logging.warning(f"Expected list for {component_type} results, got {type(component_results)}")
            continue
        
        # Count components and issues
        report['dynamic_content']['summary']['total_components_tested'] += len(component_results)
        
        # Count issues from this component type
        issue_count = len(component_results)
        if issue_count > 0:
            report['dynamic_content']['summary']['components_with_issues'] += issue_count
            
            # Categorize issue types
            for issue in component_results:
                if isinstance(issue, dict):  # Make sure it's a dictionary before accessing keys
                    issue_type = issue.get('type', 'unknown')
                    if issue_type not in report['dynamic_content']['summary']['issue_types']:
                        report['dynamic_content']['summary']['issue_types'][issue_type] = 0
                    report['dynamic_content']['summary']['issue_types'][issue_type] += 1
    
    # Calculate overall dynamic content accessibility score
    total_components = report['dynamic_content']['summary']['total_components_tested']
    components_with_issues = report['dynamic_content']['summary']['components_with_issues']
    
    if total_components > 0:
        dynamic_content_score = max(0, 100 - (components_with_issues / total_components * 100))
        report['dynamic_content']['summary']['accessibility_score'] = round(dynamic_content_score, 2)
    else:
        report['dynamic_content']['summary']['accessibility_score'] = 100
    
    return report

def generate_dynamic_content_report_section(dynamic_content_results):
    """
    Generate a detailed HTML section for dynamic content testing results.
    
    Args:
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        HTML string with detailed dynamic content testing report
    """
    html = """
    <div class="dynamic-content-section">
        <h2>Dynamic Content Accessibility Analysis</h2>
    """
    
    # Check if dynamic_content_results is a dictionary
    if not isinstance(dynamic_content_results, dict):
        html += "<p>No dynamic content results available.</p>"
        html += "</div>"
        return html
    
    # Iterate through component types
    for component_type, component_results in dynamic_content_results.items():
        if component_type == 'state_tracking' or component_type == 'error':
            continue  # Skip state tracking export and error info
        
        html += f"""
        <div class="component-type-section">
            <h3>{component_type.capitalize()} Accessibility</h3>
        """
        
        # Ensure component_results is a list
        if not isinstance(component_results, list):
            html += "<p>No data available for this component type.</p>"
            html += "</div>"
            continue
        
        # Filter and process issues
        issues = [issue for issue in component_results if isinstance(issue, dict)]
        
        if not issues:
            html += "<p>No accessibility issues detected for this component type.</p>"
        else:
            html += """
            <table class="issues-table">
                <thead>
                    <tr>
                        <th>Issue Type</th>
                        <th>Details</th>
                        <th>Severity</th>
                    </tr>
                </thead>
                <tbody>
            """
            
            for issue in issues:
                html += f"""
                    <tr>
                        <td>{issue.get('type', 'Unknown')}</td>
                        <td>{issue.get('details', 'No additional details')}</td>
                        <td>{issue.get('severity', 'Warning')}</td>
                    </tr>
                """
            
            html += """
                </tbody>
            </table>
            """
        
        html += "</div>"
    
    html += "</div>"
    
    return html

def export_dynamic_content_state_tracking(dynamic_content_results):
    """
    Export detailed state tracking information.
    
    Args:
        dynamic_content_results: Results from dynamic content testing
    
    Returns:
        Formatted state tracking export
    """
    # Validate input type
    if not isinstance(dynamic_content_results, dict):
        logging.error("dynamic_content_results is not a dictionary")
        return {"error": "Invalid data format"}
    
    # Safely access state_tracking, ensuring it's a dictionary
    state_tracking = dynamic_content_results.get('state_tracking', {})
    
    # If state_tracking is a list, convert it to a dictionary
    if isinstance(state_tracking, list):
        logging.warning("state_tracking is a list, converting to dictionary")
        state_tracking = {"exported_states": "{}"}
    
    try:
        # Parse the exported states
        exported_states_str = state_tracking.get('exported_states', '{}')
        
        # Handle the case where exported_states might be an object already
        if isinstance(exported_states_str, dict):
            exported_states = exported_states_str
        else:
            # Try to parse JSON string
            try:
                exported_states = json.loads(exported_states_str)
            except json.JSONDecodeError:
                logging.warning("Failed to parse state tracking export as JSON, using empty dict")
                exported_states = {}
        
        # Generate a more readable format
        formatted_export = {
            'timestamp': datetime.now().isoformat(),
            'component_states': {}
        }
        
        # Process component states
        if isinstance(exported_states, dict) and 'component_states' in exported_states:
            for component_type, components in exported_states.get('component_states', {}).items():
                formatted_export['component_states'][component_type] = {}
                
                for component_id, state_info in components.items():
                    # Handle both list and dictionary formats for state_info
                    if isinstance(state_info, list) and state_info:
                        # Take the last state if it's a list
                        last_state = state_info[-1]
                        formatted_export['component_states'][component_type][component_id] = {
                            'timestamp': last_state.get('timestamp', ''),
                            'state': last_state.get('state', {})
                        }
                    elif isinstance(state_info, dict):
                        formatted_export['component_states'][component_type][component_id] = {
                            'timestamp': state_info.get('timestamp', ''),
                            'state': state_info.get('state', {})
                        }
        
        # Add interaction log if available
        if isinstance(exported_states, dict) and 'interaction_log' in exported_states:
            formatted_export['interaction_log'] = exported_states.get('interaction_log', [])
        
        return formatted_export
    
    except Exception as e:
        logging.error(f"Error processing state tracking: {str(e)}")
        return {
            'error': f'Error processing state tracking: {str(e)}',
            'raw_data': str(state_tracking)
        }