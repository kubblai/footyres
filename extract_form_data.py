#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import re

def extract_form_data():
    url = "https://www.bbc.co.uk/sport/football/spanish-la-liga/table"
    
    print(f"Fetching: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look specifically for form guide table cells
        form_cells = soup.find_all('td', class_=lambda x: x and 'FormGuideTableCell' in ' '.join(x))
        
        print(f"Found {len(form_cells)} FormGuideTableCell elements")
        
        for i, cell in enumerate(form_cells):
            print(f"\nForm cell {i+1}:")
            print(f"  HTML: {str(cell)[:200]}...")
            print(f"  Text: {cell.get_text().strip()[:50]}...")
            
            # Look for nested elements that might contain individual form results
            nested_elements = cell.find_all(['span', 'div', 'li'])
            print(f"  Nested elements: {len(nested_elements)}")
            
            for j, nested in enumerate(nested_elements[:5]):
                text = nested.get_text().strip()
                if text:
                    print(f"    Element {j+1}: '{text}' - classes: {nested.get('class')}")
        
        # Also look for the __INITIAL_DATA__ which might contain structured form data
        scripts = soup.find_all('script')
        
        for script in scripts:
            if script.string and '__INITIAL_DATA__' in script.string:
                print(f"\nFound __INITIAL_DATA__ script")
                # Extract the JSON part
                match = re.search(r'__INITIAL_DATA__="([^"]+)"', script.string)
                if match:
                    try:
                        # Decode the JSON (it's double-encoded)
                        json_str = match.group(1).encode().decode('unicode_escape')
                        data = json.loads(json_str)
                        
                        # Search for table/form data in the structure
                        def search_for_form_data(obj, path=""):
                            if isinstance(obj, dict):
                                for key, value in obj.items():
                                    if 'form' in key.lower() or 'table' in key.lower():
                                        print(f"  Found form/table key at {path}.{key}")
                                        print(f"    Value preview: {str(value)[:100]}...")
                                    search_for_form_data(value, f"{path}.{key}")
                            elif isinstance(obj, list):
                                for i, item in enumerate(obj):
                                    search_for_form_data(item, f"{path}[{i}]")
                        
                        search_for_form_data(data)
                        
                    except Exception as e:
                        print(f"  Error parsing JSON: {e}")
                
                break
                        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_form_data()