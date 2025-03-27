    #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
slider_tester_full.py - Extended Slider Component Testing Module

This module provides comprehensive accessibility testing for slider components
on web pages, focusing on keyboard navigation, ARIA attributes, state changes,
and focus management.
"""

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    ElementNotInteractableException
)


class SliderStateTracker:
    """
    Tracks the state of slider components during testing.
    """
    
    def capture_element_state(self, element):
        """
        Captures the current state of a slider element.
        
        Args:
            element: The slider element to track
            
        Returns:
            Dictionary containing slider state properties
        """
        try:
            state = {
                'aria-valuenow': element.get_attribute('aria-valuenow'),
                'aria-valuemin': element.get_attribute('aria-valuemin'),
                'aria-valuemax': element.get_attribute('aria-valuemax'),
                'aria-valuetext': element.get_attribute('aria-valuetext'),
                'is_disabled': element.get_attribute('disabled') is not None or 
                               element.get_attribute('aria-disabled') == 'true',
                'is_focused': element == element.parent.switch_to.active_element,
                'css_classes': element.get_attribute('class')
            }
            
            # Attempt to capture position visually
            try:
                location = element.location
                size = element.size
                state['visual_position'] = {
                    'x': location['x'],
                    'y': location['y'],
                    'width': size['width'],
                    'height': size['height']
                }
            except:
                state['visual_position'] = None
                
            return state
            
        except Exception as e:
            logging.error(f"Error capturing slider state: {str(e)}")
            return {}


class ExtendedSliderTester:
    """
    Provides comprehensive accessibility testing for slider components.
    """
    
    def __init__(self, driver):
        """
        Initialize the slider tester.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.action_chains = ActionChains(driver)
        self.state_tracker = SliderStateTracker()
        self.logger = logging.getLogger(__name__)
        
    def _get_accessible_name(self, element):
        """
        Determines the accessible name of an element using various methods.
        
        Args:
            element: The element to check
            
        Returns:
            String containing the accessible name or empty string if none found
        """
        try:
            # Check aria-label
            aria_label = element.get_attribute('aria-label')
            if aria_label and aria_label.strip():
                return aria_label.strip()
                
            # Check aria-labelledby
            labelledby_id = element.get_attribute('aria-labelledby')
            if labelledby_id:
                try:
                    label_element = self.driver.find_element(By.ID, labelledby_id)
                    if label_element and label_element.text.strip():
                        return label_element.text.strip()
                except:
                    pass
                    
            # Check for an associated label
            element_id = element.get_attribute('id')
            if element_id:
                try:
                    label = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{element_id}"]')
                    if label and label.text.strip():
                        return label.text.strip()
                except:
                    pass
                    
            # Check title attribute as fallback
            title = element.get_attribute('title')
            if title and title.strip():
                return title.strip()
                
            return ""
            
        except Exception as e:
            self.logger.error(f"Error getting accessible name: {str(e)}")
            return ""
    
    def _is_focus_visible(self, element):
        """
        Determines if an element has a visible focus indicator.
        
        Args:
            element: The element to check
            
        Returns:
            Boolean indicating if focus is visible
        """
        try:
            # Get computed style before focus
            unfocused_style = self.driver.execute_script("""
                let style = window.getComputedStyle(arguments[0]);
                return {
                    outlineWidth: style.outlineWidth,
                    outlineStyle: style.outlineStyle,
                    outlineColor: style.outlineColor,
                    boxShadow: style.boxShadow,
                    borderWidth: style.borderWidth,
                    borderStyle: style.borderStyle,
                    borderColor: style.borderColor,
                    backgroundColor: style.backgroundColor
                };
            """, element)
            
            # Focus the element and get style again
            element.send_keys("")  # Send empty string to focus without changing value
            
            focused_style = self.driver.execute_script("""
                let style = window.getComputedStyle(arguments[0]);
                return {
                    outlineWidth: style.outlineWidth,
                    outlineStyle: style.outlineStyle,
                    outlineColor: style.outlineColor,
                    boxShadow: style.boxShadow,
                    borderWidth: style.borderWidth,
                    borderStyle: style.borderStyle,
                    borderColor: style.borderColor,
                    backgroundColor: style.backgroundColor
                };
            """, element)
            
            # Check if any focus-indicating styles changed
            style_changed = False
            for key in unfocused_style:
                if unfocused_style[key] != focused_style[key]:
                    style_changed = True
                    break
                    
            return style_changed
            
        except Exception as e:
            self.logger.warning(f"Error checking focus visibility: {str(e)}")
            return False  # Be conservative and report as an issue
            
    def test_slider(self, slider_element):
        """
        Comprehensive accessibility test for slider components.
        
        Tests for:
        - Keyboard accessibility
        - Proper ARIA attributes
        - State changes
        - Focus management
        - Screen reader accessibility
        
        Args:
            slider_element: The slider element to test
            
        Returns:
            List of accessibility issues found
        """
        issues = []
        
        try:
            # Track initial state
            initial_state = self.state_tracker.capture_element_state(slider_element)
            
            # Check for required attributes
            if not slider_element.get_attribute('role') == 'slider':
                issues.append({
                    'element': slider_element,
                    'message': 'Slider missing proper role="slider" attribute',
                    'severity': 'critical',
                    'wcag': 'WCAG 4.1.2'
                })
                
            # Check for accessible name
            accessible_name = self._get_accessible_name(slider_element)
            if not accessible_name:
                issues.append({
                    'element': slider_element,
                    'message': 'Slider has no accessible label',
                    'severity': 'warning',
                    'wcag': 'WCAG 4.1.2'
                })
                
            # Check for aria-valuemin, aria-valuemax, and aria-valuenow
            if not slider_element.get_attribute('aria-valuemin'):
                issues.append({
                    'element': slider_element,
                    'message': 'Slider missing aria-valuemin attribute',
                    'severity': 'critical',
                    'wcag': 'WCAG 4.1.2'
                })
                
            if not slider_element.get_attribute('aria-valuemax'):
                issues.append({
                    'element': slider_element,
                    'message': 'Slider missing aria-valuemax attribute',
                    'severity': 'critical',
                    'wcag': 'WCAG 4.1.2'
                })
                
            if not slider_element.get_attribute('aria-valuenow'):
                issues.append({
                    'element': slider_element,
                    'message': 'Slider missing aria-valuenow attribute',
                    'severity': 'critical',
                    'wcag': 'WCAG 4.1.2'
                })
            
            # Check for optional but recommended attributes
            if not slider_element.get_attribute('aria-valuetext'):
                issues.append({
                    'element': slider_element,
                    'message': 'Slider missing aria-valuetext attribute for better screen reader support',
                    'severity': 'warning',
                    'wcag': 'WCAG 4.1.2'
                })
                
            # Keyboard interaction tests
            self.driver.execute_script("arguments[0].scrollIntoView(true);", slider_element)
            try:
                slider_element.click()  # Ensure it's focused
            except ElementNotInteractableException:
                issues.append({
                    'element': slider_element,
                    'message': 'Slider is not interactable',
                    'severity': 'critical',
                    'wcag': 'WCAG 2.1.1'
                })
                return issues  # Return early as further tests will fail
            
            # Test right arrow key (increment)
            current_value = slider_element.get_attribute('aria-valuenow')
            self.action_chains.send_keys(Keys.ARROW_RIGHT).perform()
            time.sleep(0.5)  # Wait for state change
            new_value = slider_element.get_attribute('aria-valuenow')
            
            try:
                if float(current_value) >= float(new_value):  # No increase occurred
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider does not respond to arrow right key',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.1.1'
                    })
            except (ValueError, TypeError):
                issues.append({
                    'element': slider_element,
                    'message': 'Slider has invalid aria-valuenow attribute',
                    'severity': 'critical',
                    'wcag': 'WCAG 4.1.2'
                })
                
            # Test left arrow key (decrement)
            current_value = new_value
            self.action_chains.send_keys(Keys.ARROW_LEFT).perform()
            time.sleep(0.5)  # Wait for state change
            new_value = slider_element.get_attribute('aria-valuenow')
            
            try:
                if float(current_value) <= float(new_value):  # No decrease occurred
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider does not respond to arrow left key',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.1.1'
                    })
            except (ValueError, TypeError):
                # Already logged this issue above
                pass
                
            # Test Home key (minimum value)
            self.action_chains.send_keys(Keys.HOME).perform()
            time.sleep(0.5)
            min_value = slider_element.get_attribute('aria-valuemin')
            current_value = slider_element.get_attribute('aria-valuenow')
            
            try:
                if float(current_value) != float(min_value):
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider does not respond to Home key to set minimum value',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.1.1'
                    })
            except (ValueError, TypeError):
                # Already logged this issue above
                pass
                
            # Test End key (maximum value)
            self.action_chains.send_keys(Keys.END).perform()
            time.sleep(0.5)
            max_value = slider_element.get_attribute('aria-valuemax')
            current_value = slider_element.get_attribute('aria-valuenow')
            
            try:
                if float(current_value) != float(max_value):
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider does not respond to End key to set maximum value',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.1.1'
                    })
            except (ValueError, TypeError):
                # Already logged this issue above
                pass
                
            # Test Page Up/Down (larger increments if applicable)
            try:
                middle_value = str((float(min_value) + float(max_value)) / 2)
                self.action_chains.send_keys(Keys.HOME).perform()  # Reset to min
                time.sleep(0.5)
                
                self.action_chains.send_keys(Keys.PAGE_UP).perform()
                time.sleep(0.5)
                current_value = slider_element.get_attribute('aria-valuenow')
                
                if float(current_value) == float(min_value):  # No change occurred
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider does not respond to Page Up key for larger increments',
                        'severity': 'warning',
                        'wcag': 'WCAG 2.1.1'
                    })
            except (ValueError, TypeError):
                # Already logged this issue above
                pass
                
            # Check for touch accessibility (presence of touch-friendly hit area)
            slider_width = slider_element.size['width']
            if slider_width < 44:  # WCAG recommends at least 44px touch target
                issues.append({
                    'element': slider_element,
                    'message': 'Slider control may be too small for touch interaction (< 44px)',
                    'severity': 'warning',
                    'wcag': 'WCAG 2.5.5'
                })
                
            # Check for visible focus indicator
            self.action_chains.send_keys(Keys.TAB).perform()  # Move focus away
            time.sleep(0.5)
            self.action_chains.send_keys(Keys.SHIFT, Keys.TAB).perform()  # Focus back
            time.sleep(0.5)
            
            focus_visible = self._is_focus_visible(slider_element)
            if not focus_visible:
                issues.append({
                    'element': slider_element,
                    'message': 'Slider does not have a visible focus indicator',
                    'severity': 'critical',
                    'wcag': 'WCAG 2.4.7'
                })
                
            # Verify state changes are announced properly (would ideally use screen reader API)
            # For now, we just verify that aria-valuenow updates properly
            final_state = self.state_tracker.capture_element_state(slider_element)
            if initial_state.get('aria-valuenow') == final_state.get('aria-valuenow'):
                # Only flag if we weren't able to change the value earlier
                if not any(issue['message'] == 'Slider does not respond to arrow right key' for issue in issues):
                    issues.append({
                        'element': slider_element,
                        'message': 'Slider state (aria-valuenow) may not update properly',
                        'severity': 'critical',
                        'wcag': 'WCAG 4.1.2'
                    })
                    
        except StaleElementReferenceException:
            self.logger.error("Element became stale during slider test")
            issues.append({
                'element': None,
                'message': 'Slider element became stale during testing, suggesting DOM changes during interaction',
                'severity': 'warning'
           })
        except Exception as e:
           self.logger.error(f"Error in slider test: {str(e)}")
           issues.append({
               'element': slider_element,
               'message': f'Error testing slider: {str(e)}',
               'severity': 'warning'
           })
           
        return issues


def find_sliders(driver):
   """
   Find all slider elements on the page.
   
   Args:
       driver: Selenium WebDriver instance
       
   Returns:
       List of slider elements
   """
   sliders = []
   
   # Find elements with role="slider"
   try:
       role_sliders = driver.find_elements(By.CSS_SELECTOR, '[role="slider"]')
       sliders.extend(role_sliders)
   except Exception as e:
       logging.error(f"Error finding role sliders: {str(e)}")
   
   # Find range inputs
   try:
       range_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="range"]')
       sliders.extend(range_inputs)
   except Exception as e:
       logging.error(f"Error finding range inputs: {str(e)}")
   
   # Find custom sliders (common patterns)
   try:
       # Look for elements that might be custom sliders
       potential_sliders = driver.find_elements(By.CSS_SELECTOR, '.slider, [class*="slider"], [id*="slider"], [class*="range"], [id*="range"]')
       
       # Filter out those that are already found or are containers
       for element in potential_sliders:
           if element not in sliders and not any(s in element.get_attribute('class').lower() for s in ['container', 'wrapper', 'track']):
               # Check if it has keyboard event listeners (indication of slider behavior)
               has_listeners = driver.execute_script("""
                   const el = arguments[0];
                   return el.onkeydown || el.onkeyup || el.onkeypress;
               """, element)
               
               if has_listeners:
                   sliders.append(element)
   except Exception as e:
       logging.error(f"Error finding custom sliders: {str(e)}")
   
   return sliders


def test_all_sliders(driver, url=None):
   """
   Test all sliders on a page for accessibility.
   
   Args:
       driver: Selenium WebDriver instance
       url: Optional URL to navigate to before testing
       
   Returns:
       Dictionary with test results
   """
   if url:
       driver.get(url)
       time.sleep(2)  # Allow page to load
   
   # Setup logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )
   logger = logging.getLogger("SliderTester")
   
   # Find all sliders
   logger.info("Searching for slider elements...")
   sliders = find_sliders(driver)
   logger.info(f"Found {len(sliders)} potential slider elements")
   
   # Test each slider
   tester = ExtendedSliderTester(driver)
   all_issues = []
   
   for i, slider in enumerate(sliders):
       logger.info(f"Testing slider {i+1}/{len(sliders)}")
       issues = tester.test_slider(slider)
       
       if issues:
           logger.info(f"Found {len(issues)} issues with slider {i+1}")
           all_issues.extend(issues)
       else:
           logger.info(f"No issues found with slider {i+1}")
   
   # Summarize results
   results = {
       'total_sliders': len(sliders),
       'sliders_with_issues': len(set(issue['element'] for issue in all_issues if issue['element'] is not None)),
       'total_issues': len(all_issues),
       'critical_issues': len([i for i in all_issues if i['severity'] == 'critical']),
       'warning_issues': len([i for i in all_issues if i['severity'] == 'warning']),
       'all_issues': all_issues
   }
   
   logger.info(f"Slider testing complete. Found {results['total_issues']} issues across {results['sliders_with_issues']} sliders.")
   return results


if __name__ == "__main__":
   # Example usage
   import argparse
   
   parser = argparse.ArgumentParser(description='Test slider components for accessibility.')
   parser.add_argument('--url', help='URL to test', required=True)
   parser.add_argument('--browser', help='Browser to use (chrome, firefox)', default='chrome')
   parser.add_argument('--output', help='Output file for results (JSON)', default=None)
   args = parser.parse_args()
   
   # Initialize driver
   if args.browser.lower() == 'chrome':
       driver = webdriver.Chrome()
   elif args.browser.lower() == 'firefox':
       driver = webdriver.Firefox()
   else:
       raise ValueError(f"Unsupported browser: {args.browser}")
   
   try:
       # Run the tests
       results = test_all_sliders(driver, args.url)
       
       # Output results
       if args.output:
           import json
           
           # Convert elements to strings for JSON serialization
           for issue in results['all_issues']:
               if issue['element'] is not None:
                   element_id = issue['element'].get_attribute('id')
                   element_class = issue['element'].get_attribute('class')
                   element_tag = issue['element'].tag_name
                   
                   issue['element'] = {
                       'id': element_id,
                       'class': element_class,
                       'tag': element_tag
                   }
           
           with open(args.output, 'w') as f:
               json.dump(results, f, indent=2)
               print(f"Results saved to {args.output}")
       else:
           # Print summary to console
           print(f"\nSummary:")
           print(f"Total sliders tested: {results['total_sliders']}")
           print(f"Sliders with issues: {results['sliders_with_issues']}")
           print(f"Critical issues: {results['critical_issues']}")
           print(f"Warning issues: {results['warning_issues']}")
           
           # Print detailed issues
           if results['all_issues']:
               print("\nDetailed Issues:")
               for i, issue in enumerate(results['all_issues']):
                   print(f"{i+1}. [{issue['severity'].upper()}] {issue['message']}")
                   if 'wcag' in issue:
                       print(f"   WCAG Reference: {issue['wcag']}")
                   print("")
           
   finally:
       driver.quit()
            