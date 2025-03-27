#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
carousel_tester.py - Extended Carousel Component Testing Module

This module provides comprehensive accessibility testing for carousel components
on web pages, focusing on keyboard navigation, ARIA attributes, state changes,
and focus management.
"""

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    ElementNotInteractableException,
    NoSuchElementException
)
import validators


class CarouselStateTracker:
    """
    Tracks the state of carousel components during testing.
    """
    
    def capture_element_state(self, element):
        """
        Captures the current state of a carousel element.
        
        Args:
            element: The carousel element to track
            
        Returns:
            Dictionary containing carousel state properties
        """
        try:
            state = {
                'aria-live': element.get_attribute('aria-live'),
                'aria-roledescription': element.get_attribute('aria-roledescription'),
                'aria-label': element.get_attribute('aria-label'),
                'role': element.get_attribute('role'),
                'is_focused': element == element.parent.switch_to.active_element,
                'css_classes': element.get_attribute('class'),
                'active_slide_index': None,
                'slides_count': None
            }
            
            # Try to determine active slide and total slides count
            try:
                # Look for common carousel indicators
                indicators = element.find_elements(By.CSS_SELECTOR, 
                    '.carousel-indicators li, [role="tablist"] [role="tab"], .carousel-dot, .slick-dots li')
                
                if indicators:
                    state['slides_count'] = len(indicators)
                    for i, indicator in enumerate(indicators):
                        if 'active' in indicator.get_attribute('class') or indicator.get_attribute('aria-selected') == 'true':
                            state['active_slide_index'] = i
                            break
                
                # If we couldn't find indicators, try looking at the slides directly
                if state['active_slide_index'] is None:
                    slides = element.find_elements(By.CSS_SELECTOR, 
                        '.carousel-item, .slick-slide, [role="tabpanel"], .slide')
                    
                    if slides:
                        state['slides_count'] = len(slides)
                        for i, slide in enumerate(slides):
                            if 'active' in slide.get_attribute('class') or slide.get_attribute('aria-hidden') == 'false':
                                state['active_slide_index'] = i
                                break
            except Exception as e:
                logging.error(f"Error determining carousel state details: {str(e)}")
                
            return state
            
        except Exception as e:
            logging.error(f"Error capturing carousel state: {str(e)}")
            return {}


class ExtendedCarouselTester:
    """
    Provides comprehensive accessibility testing for carousel components.
    """
    
    def __init__(self, driver):
        """
        Initialize the carousel tester.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.action_chains = ActionChains(driver)
        self.state_tracker = CarouselStateTracker()
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
            if (aria_label and aria_label.strip()):
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
                    
            # Look for a heading inside the carousel
            try:
                heading = element.find_element(By.CSS_SELECTOR, 'h1, h2, h3, h4, h5, h6')
                if heading and heading.text.strip():
                    return heading.text.strip()
            except:
                pass
                    
            # Check for a figcaption if the carousel is in a figure
            try:
                figure = element.find_element(By.XPATH, './ancestor::figure')
                figcaption = figure.find_element(By.TAG_NAME, 'figcaption')
                if figcaption and figcaption.text.strip():
                    return figcaption.text.strip()
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
            focused_style = self.driver.execute_script("""
                let style = window.getComputedStyle(arguments[0]);
                return {
                    outlineWidth: style.outlineWidth,
                    outlineStyle: style.outlineStyle,
                    outlineColor: style.outlineColor,
                    boxShadow: style.boxShadow
                };
            """, element)
            return focused_style['outlineStyle'] != 'none' or focused_style['boxShadow'] != 'none'
        except Exception as e:
            self.logger.warning(f"Error checking focus visibility: {str(e)}")
            return False  # Be conservative and report as an issue
    
    def _find_control(self, carousel_element, selectors):
        for selector in selectors:
            try:
                return carousel_element.find_element(By.CSS_SELECTOR, selector)
            except NoSuchElementException:
                continue
        return None

    def _find_carousel_controls(self, carousel_element):
        controls = {
            'prev': self._find_control(carousel_element, ['.carousel-control-prev', '.prev', '.slick-prev']),
            'next': self._find_control(carousel_element, ['.carousel-control-next', '.next', '.slick-next']),
            'pause': self._find_control(carousel_element, ['.carousel-pause', '.pause', '[aria-label*="Pause"]'])
        }
        return controls
        
    def _test_carousel_keyboard_navigation(self, carousel_element, controls):
        """
        Test keyboard navigation for a carousel.
        
        Args:
            carousel_element: The carousel element
            controls: Dictionary containing control buttons
            
        Returns:
            List of issues found
        """
        issues = []
        
        try:
            # Get initial state
            initial_state = self.state_tracker.capture_element_state(carousel_element)
            
            # Test previous button keyboard access
            if controls['prev']:
                try:
                    # Tab to the previous button
                    self.action_chains.send_keys(Keys.TAB).perform()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                    
                    # Continue tabbing until we reach the prev button or cycle through all elements
                    max_tabs = 20  # Prevent infinite loop
                    tabs = 0
                    while (self.driver.switch_to.active_element != controls['prev'] and 
                           tabs < max_tabs):
                        self.action_chains.send_keys(Keys.TAB).perform()
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        tabs += 1
                        
                    if self.driver.switch_to.active_element == controls['prev']:
                        # Test activation with both Enter and Space
                        current_state = self.state_tracker.capture_element_state(carousel_element)
                        
                        # Press Enter
                        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        
                        # Check if the carousel state changed
                        new_state = self.state_tracker.capture_element_state(carousel_element)
                        if (new_state['active_slide_index'] is not None and 
                            current_state['active_slide_index'] is not None and
                            new_state['active_slide_index'] == current_state['active_slide_index']):
                            issues.append({
                                'element': controls['prev'],
                                'message': 'Previous button does not respond to Enter key',
                                'severity': 'critical',
                                'wcag': 'WCAG 2.1.1'
                            })
                            
                        # Test Space key
                        current_state = new_state
                        self.driver.switch_to.active_element.send_keys(Keys.SPACE)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        
                        new_state = self.state_tracker.capture_element_state(carousel_element)
                        if (new_state['active_slide_index'] is not None and 
                            current_state['active_slide_index'] is not None and
                            new_state['active_slide_index'] == current_state['active_slide_index']):
                            issues.append({
                                'element': controls['prev'],
                                'message': 'Previous button does not respond to Space key',
                                'severity': 'critical',
                                'wcag': 'WCAG 2.1.1'
                            })
                    else:
                        issues.append({
                            'element': controls['prev'],
                            'message': 'Previous button is not keyboard accessible via tab navigation',
                            'severity': 'critical',
                            'wcag': 'WCAG 2.1.1'
                        })
                except Exception as e:
                    self.logger.error(f"Error testing previous button: {str(e)}")
                    issues.append({
                        'element': controls['prev'],
                        'message': f'Error testing previous button: {str(e)}',
                        'severity': 'warning'
                    })
            
            # Test next button keyboard access
            if controls['next']:
                try:
                    # Tab to the next button
                    self.action_chains.send_keys(Keys.TAB).perform()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                    
                    # Continue tabbing until we reach the next button or cycle through all elements
                    max_tabs = 20  # Prevent infinite loop
                    tabs = 0
                    while (self.driver.switch_to.active_element != controls['next'] and 
                           tabs < max_tabs):
                        self.action_chains.send_keys(Keys.TAB).perform()
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        tabs += 1
                        
                    if self.driver.switch_to.active_element == controls['next']:
                        # Test activation with both Enter and Space
                        current_state = self.state_tracker.capture_element_state(carousel_element)
                        
                        # Press Enter
                        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        
                        # Check if the carousel state changed
                        new_state = self.state_tracker.capture_element_state(carousel_element)
                        if (new_state['active_slide_index'] is not None and 
                            current_state['active_slide_index'] is not None and
                            new_state['active_slide_index'] == current_state['active_slide_index']):
                            issues.append({
                                'element': controls['next'],
                                'message': 'Next button does not respond to Enter key',
                                'severity': 'critical',
                                'wcag': 'WCAG 2.1.1'
                            })
                        
                        # Test Space key
                        current_state = new_state
                        self.driver.switch_to.active_element.send_keys(Keys.SPACE)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        
                        new_state = self.state_tracker.capture_element_state(carousel_element)
                        if (new_state['active_slide_index'] is not None and 
                            current_state['active_slide_index'] is not None and
                            new_state['active_slide_index'] == current_state['active_slide_index']):
                            issues.append({
                                'element': controls['next'],
                                'message': 'Next button does not respond to Space key',
                                'severity': 'critical',
                                'wcag': 'WCAG 2.1.1'
                            })
                    else:
                        issues.append({
                            'element': controls['next'],
                            'message': 'Next button is not keyboard accessible via tab navigation',
                            'severity': 'critical',
                            'wcag': 'WCAG 2.1.1'
                        })
                except Exception as e:
                    self.logger.error(f"Error testing next button: {str(e)}")
                    issues.append({
                        'element': controls['next'],
                        'message': f'Error testing next button: {str(e)}',
                        'severity': 'warning'
                    })
                   
            # Test pause button if present
            if controls['pause']:
                try:
                    # Tab to the pause button
                    self.action_chains.send_keys(Keys.TAB).perform()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                   
                    # Continue tabbing until we reach the pause button or cycle through all elements
                    max_tabs = 20  # Prevent infinite loop
                    tabs = 0
                    while (self.driver.switch_to.active_element != controls['pause'] and 
                           tabs < max_tabs):
                        self.action_chains.send_keys(Keys.TAB).perform()
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                        tabs += 1
                       
                    if self.driver.switch_to.active_element == controls['pause']:
                        # Test activation with Enter
                        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                       
                        # No reliable way to detect if autoplay was paused, so just check for errors
                       
                        # Test Space key
                        self.driver.switch_to.active_element.send_keys(Keys.SPACE)
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
                    else:
                        issues.append({
                            'element': controls['pause'],
                            'message': 'Pause button is not keyboard accessible via tab navigation',
                            'severity': 'critical',
                            'wcag': 'WCAG 2.1.1'
                        })
                except Exception as e:
                    self.logger.error(f"Error testing pause button: {str(e)}")
                    issues.append({
                        'element': controls['pause'],
                        'message': f'Error testing pause button: {str(e)}',
                        'severity': 'warning'
                    })
                   
        except Exception as e:
            self.logger.error(f"Error in keyboard navigation test: {str(e)}")
            issues.append({
                'element': carousel_element,
                'message': f'Error testing keyboard navigation: {str(e)}',
                'severity': 'warning'
            })
           
        return issues
       
    def test_carousel(self, carousel_element):
        """
        Comprehensive accessibility test for carousel components.
       
        Tests for:
        - Keyboard accessibility
        - Proper ARIA attributes
        - State changes
        - Focus management
        - Autoplay control
        - Screen reader accessibility
       
        Args:
            carousel_element: The carousel element to test
           
        Returns:
            List of accessibility issues found
        """
        issues = []
       
        try:
            # Track initial state
            initial_state = self.state_tracker.capture_element_state(carousel_element)
           
            # Check for proper role
            role = carousel_element.get_attribute('role')
            if not role:
                issues.append({
                    'element': carousel_element,
                    'message': 'Carousel missing role attribute',
                    'severity': 'warning',
                    'wcag': 'WCAG 1.3.1'
                })
            elif role not in ['region', 'group', 'list']:
                issues.append({
                    'element': carousel_element,
                    'message': f'Carousel has potentially inappropriate role="{role}" (recommended: region, group, or list)',
                    'severity': 'warning',
                    'wcag': 'WCAG 1.3.1'
                })
               
            # Check for aria-roledescription
            aria_roledescription = carousel_element.get_attribute('aria-roledescription')
            if not aria_roledescription or 'carousel' not in aria_roledescription.lower():
                issues.append({
                    'element': carousel_element,
                    'message': 'Carousel missing aria-roledescription="carousel"',
                    'severity': 'warning',
                    'wcag': 'WCAG 1.3.1'
                })
               
            # Check for accessible name
            accessible_name = self._get_accessible_name(carousel_element)
            if not accessible_name:
                issues.append({
                    'element': carousel_element,
                    'message': 'Carousel has no accessible name',
                    'severity': 'critical',
                    'wcag': 'WCAG 1.3.1'
                })
               
            # Check for aria-live attribute for auto-rotating carousels
            aria_live = carousel_element.get_attribute('aria-live')
           
            # Auto-rotation can't be reliably detected, so suggest best practice
            if not aria_live:
                issues.append({
                    'element': carousel_element,
                    'message': 'Auto-rotating carousel should have aria-live attribute',
                    'severity': 'warning',
                    'wcag': 'WCAG 4.1.2'
                })
               
            # Find carousel controls
            controls = self._find_carousel_controls(carousel_element)
           
            # Check for presence of controls
            if not controls['prev'] or not controls['next']:
                issues.append({
                    'element': carousel_element,
                    'message': 'Carousel missing accessible previous/next controls',
                    'severity': 'critical',
                    'wcag': 'WCAG 2.1.1'
                })
               
            # Check for pause button for auto-advancing carousels
            if not controls['pause']:
                issues.append({
                    'element': carousel_element,
                    'message': 'Carousel should have a pause control if it auto-advances',
                    'severity': 'warning',
                    'wcag': 'WCAG 2.2.2'
                })
               
            # Test keyboard navigation for controls
            keyboard_issues = self._test_carousel_keyboard_navigation(carousel_element, controls)
            issues.extend(keyboard_issues)
           
            # Check if slides have proper ARIA attributes
            try:
                slides = carousel_element.find_elements(By.CSS_SELECTOR, 
                    '.carousel-item, .slick-slide, [role="tabpanel"], .slide')
               
                if slides:
                    for i, slide in enumerate(slides):
                        # Check if slide is properly labeled
                        slide_label = self._get_accessible_name(slide)
                        if not slide_label:
                            # If no label, check if it has meaningful image content
                            images = slide.find_elements(By.TAG_NAME, 'img')
                            if images:
                                for img in images:
                                    if not img.get_attribute('alt'):
                                        issues.append({
                                            'element': img,
                                            'message': 'Carousel slide image missing alt text',
                                            'severity': 'critical',
                                            'wcag': 'WCAG 1.1.1'
                                        })
                                       
                        # Check if inactive slides are properly hidden
                        is_active = 'active' in slide.get_attribute('class') or slide.get_attribute('aria-hidden') == 'false'
                        if not is_active and slide.get_attribute('aria-hidden') != 'true':
                            issues.append({
                                'element': slide,
                                'message': 'Inactive carousel slide not hidden with aria-hidden="true"',
                                'severity': 'warning',
                                'wcag': 'WCAG 4.1.2'
                            })
            except Exception as e:
                self.logger.error(f"Error checking carousel slides: {str(e)}")
               
            # Check for visible focus indicators on controls
            if controls['prev']:
                # Try to focus the element
                controls['prev'].click()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
               
                focus_visible = self._is_focus_visible(controls['prev'])
                if not focus_visible:
                    issues.append({
                        'element': controls['prev'],
                        'message': 'Previous button does not have a visible focus indicator',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.4.7'
                    })
                   
            if controls['next']:
                # Try to focus the element
                controls['next'].click()
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.carousel-control-prev')))
               
                focus_visible = self._is_focus_visible(controls['next'])
                if not focus_visible:
                    issues.append({
                        'element': controls['next'],
                        'message': 'Next button does not have a visible focus indicator',
                        'severity': 'critical',
                        'wcag': 'WCAG 2.4.7'
                    })
               
        except StaleElementReferenceException:
            self.logger.error("Element became stale during carousel test")
            issues.append({
                'element': None,
                'message': 'Carousel element became stale during testing, suggesting DOM changes during interaction',
                'severity': 'warning'
            })
            try:
                carousel_element = self.driver.find_element(By.CSS_SELECTOR, '.carousel')
            except Exception as e:
                self.logger.error(f"Error finding carousel element: {str(e)}")
                issues.append({
                    'element': None,
                    'message': f'Error finding carousel element: {str(e)}',
                    'severity': 'warning'
                })
        except Exception as e:
            self.logger.error(f"Error in carousel test: {str(e)}")
            issues.append({
                'element': carousel_element,
                'message': f'Error testing carousel: {str(e)}',
                'severity': 'warning'
            })
           
        return issues


def find_carousels(driver):
    """
    Find all carousel elements on the page.
   
    Args:
        driver: Selenium WebDriver instance
       
    Returns:
        List of carousel elements
    """
    carousels = []
   
    # Find elements with common carousel class names
    try:
        class_carousels = driver.find_elements(By.CSS_SELECTOR, 
            '.carousel, .slick-slider, .slider, [class*="carousel"], [class*="slider"]')
        carousels.extend(class_carousels)
    except Exception as e:
        logging.error(f"Error finding carousels by class: {str(e)}")
   
    # Find elements with carousel role description
    try:
        role_carousels = driver.find_elements(By.CSS_SELECTOR, '[aria-roledescription="carousel"]')
        for carousel in role_carousels:
            if (carousel not in carousels):
                carousels.append(carousel)
    except Exception as e:
        logging.error(f"Error finding carousels by role description: {str(e)}")
   
    # Find common carousel frameworks by their structure
    try:
        # Bootstrap carousels
        bootstrap_carousels = driver.find_elements(By.CSS_SELECTOR, '.carousel[data-ride="carousel"]')
        for carousel in bootstrap_carousels:
            if carousel not in carousels:
                carousels.append(carousel)
               
        # Slick carousels
        slick_carousels = driver.find_elements(By.CSS_SELECTOR, '.slick-initialized')
        for carousel in slick_carousels:
            if carousel not in carousels:
                carousels.append(carousel)
               
        # OWL carousels
        owl_carousels = driver.find_elements(By.CSS_SELECTOR, '.owl-carousel')
        for carousel in owl_carousels:
            if carousel not in carousels:
                carousels.append(carousel)
    except Exception as e:
        logging.error(f"Error finding framework-specific carousels: {str(e)}")
   
    return carousels


def test_all_carousels(driver, url=None):
    """
    Test all carousels on a page for accessibility.
   
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
    logger = logging.getLogger("CarouselTester")
   
    # Find all carousels
    logger.info("Searching for carousel elements...")
    carousels = find_carousels(driver)
    logger.info(f"Found {len(carousels)} potential carousel elements")
   
    # Test each carousel
    tester = ExtendedCarouselTester(driver)
    all_issues = []
   
    for i, carousel in enumerate(carousels):
        logger.info(f"Testing carousel {i+1}/{len(carousels)} with ID: {carousel.get_attribute('id')}")
        issues = tester.test_carousel(carousel)
       
        if issues:
            logger.info(f"Found {len(issues)} issues with carousel {i+1}")
            all_issues.extend(issues)
        else:
            logger.info(f"No issues found with carousel {i+1}")
   
    # Summarize results
    results = {
        'total_carousels': len(carousels),
        'carousels_with_issues': len(set(issue['element'] for issue in all_issues if issue['element'] is not None)),
        'total_issues': len(all_issues),
        'critical_issues': len([i for i in all_issues if i['severity'] == 'critical']),
        'warning_issues': len([i for i in all_issues if i['severity'] == 'warning']),
        'all_issues': all_issues
    }
   
    logger.info(f"Carousel testing complete. Found {results['total_issues']} issues across {results['carousels_with_issues']} carousels.")
    return results


if __name__ == "__main__":
    # Example usage
    import argparse
   
    parser = argparse.ArgumentParser(description='Test carousel components for accessibility.')
    parser.add_argument('--url', help='URL to test', required=True)
    parser.add_argument('--browser', help='Browser to use (chrome, firefox)', default='chrome')
    parser.add_argument('--output', help='Output file for results (JSON)', default=None)
    args = parser.parse_args()
   
    if not validators.url(args.url):
        raise ValueError(f"Invalid URL: {args.url}")
   
    # Initialize driver
    if args.browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif args.browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {args.browser}")
   
    try:
        # Run the tests
        results = test_all_carousels(driver, args.url)
       
        # Output results
        if args.output:
            import json
           
            # Convert elements to strings for JSON serialization
            for issue in results['all_issues']:
                if issue['element']:
                    issue['element'] = {
                        'id': issue['element'].get_attribute('id'),
                        'class': issue['element'].get_attribute('class'),
                        'tag': issue['element'].tag_name
                    }
           
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
                print(f"Results saved to {args.output}")
        else:
            # Print summary to console
            print(f"\nSummary:")
            print(f"Total carousels tested: {results['total_carousels']}")
            print(f"Carousels with issues: {results['carousels_with_issues']}")
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
