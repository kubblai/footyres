#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json

def debug_bbc_form_data():
    url = "https://www.bbc.co.uk/sport/football/spanish-la-liga/table"
    
    print(f"Fetching: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print("Looking for form data in HTML...")
        
        # Look for form-related elements
        form_elements = soup.find_all(attrs={'class': lambda x: x and 'form' in x.lower()})
        print(f"Found {len(form_elements)} elements with 'form' in class name")
        
        for i, elem in enumerate(form_elements[:3]):
            print(f"Form element {i+1}: {elem.name} - {elem.get('class')} - {elem.get_text()[:50]}...")
        
        # Look for table cells that might contain form data (W, D, L boxes)
        table_cells = soup.find_all(['td', 'th'])
        form_cells = []
        for cell in table_cells:
            text = cell.get_text().strip()
            if any(char in text for char in ['W', 'D', 'L']) and len(text) <= 10:
                form_cells.append(cell)
        
        print(f"\nFound {len(form_cells)} table cells with potential form data:")
        for i, cell in enumerate(form_cells[:10]):
            print(f"Cell {i+1}: '{cell.get_text().strip()}' - classes: {cell.get('class')}")
        
        # Look for JSON data containing form information
        scripts = soup.find_all('script', type='application/ld+json')
        print(f"\nFound {len(scripts)} JSON-LD scripts")
        
        # Look for inline JavaScript with data
        all_scripts = soup.find_all('script')
        print(f"Total scripts: {len(all_scripts)}")
        
        for i, script in enumerate(all_scripts):
            if script.string and ('form' in script.string.lower() or 'table' in script.string.lower()):
                content = script.string[:200]
                print(f"Script {i+1} with form/table data: {content}...")
        
        # Look for data attributes
        elements_with_data = soup.find_all(attrs=lambda x: x and any(k.startswith('data-') for k in x.keys()))
        print(f"\nFound {len(elements_with_data)} elements with data attributes")
        
        for i, elem in enumerate(elements_with_data[:5]):
            data_attrs = {k: v for k, v in elem.attrs.items() if k.startswith('data-')}
            if data_attrs:
                print(f"Element {i+1}: {elem.name} - {data_attrs}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_bbc_form_data()