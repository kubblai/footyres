#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import re

def extract_form_simple():
    url = "https://www.bbc.co.uk/sport/football/spanish-la-liga/table"
    
    print(f"Fetching: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for all table cells with form in the class name
        form_related = soup.find_all(attrs={'class': lambda x: x and any('form' in cls.lower() for cls in x)})
        
        print(f"Found {len(form_related)} form-related elements")
        
        for i, elem in enumerate(form_related[:5]):
            print(f"\nElement {i+1}:")
            print(f"  Tag: {elem.name}")
            print(f"  Classes: {elem.get('class')}")
            print(f"  Text: '{elem.get_text().strip()[:100]}...'")
            
            # If this looks like a form container, examine its children
            if 'form' in ' '.join(elem.get('class', [])).lower():
                children = elem.find_all(['span', 'li', 'div'])
                print(f"  Children: {len(children)}")
                for j, child in enumerate(children[:5]):
                    child_text = child.get_text().strip()
                    if child_text and len(child_text) < 20:
                        print(f"    Child {j+1}: '{child_text}' - {child.get('class')}")
        
        # Also look for spans or elements that contain W, D, L results
        potential_results = soup.find_all(text=re.compile(r'[WDL].*Result'))
        print(f"\nFound {len(potential_results)} potential W/D/L result texts:")
        for i, text in enumerate(potential_results[:10]):
            print(f"  Result {i+1}: '{text.strip()}'")
            # Get the parent element
            parent = text.parent
            if parent:
                print(f"    Parent: {parent.name} - {parent.get('class')}")
        
        # Look for any element that has exactly W, D, or L as text
        single_results = soup.find_all(text=re.compile(r'^[WDL]$'))
        print(f"\nFound {len(single_results)} single W/D/L texts:")
        for i, text in enumerate(single_results[:10]):
            parent = text.parent
            print(f"  '{text}' in {parent.name} - {parent.get('class')}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_form_simple()