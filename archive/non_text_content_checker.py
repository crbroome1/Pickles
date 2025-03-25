#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup

def identify_non_text_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    non_text_elements = []

    # Find elements that typically contain non-text content
    element_types = ['img', 'svg', 'video', 'audio', 'object', 'embed', 'canvas']
    for element_type in element_types:
        elements = soup.find_all(element_type)
        for element in elements:
            element_info = {
                'tag': element.name,
                'src': element.get('src'),
                'alt': element.get('alt'),
                # Extract other relevant attributes as needed
            }
            non_text_elements.append(element_info)

    return non_text_elements

