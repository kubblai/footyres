#!/usr/bin/env python3

import sys
import os
import requests
from bs4 import BeautifulSoup
import json
import re

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def debug_extraction_step_by_step():
    print("Debugging extraction step by step...")
    
    try:
        # Step 1: Fetch data like the scraper does
        print("Step 1: Fetching BBC Sport page...")
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        response = session.get('https://www.bbc.co.uk/sport/football/scores-fixtures', timeout=15)
        print(f"✅ Got response: {response.status_code}")
        
        # Step 2: Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"✅ Parsed HTML: {len(soup.find_all('script'))} script tags")
        
        # Step 3: Find __INITIAL_DATA__ script
        scripts = soup.find_all('script')
        initial_data_script = None
        
        for i, script in enumerate(scripts):
            if script.string and '__INITIAL_DATA__' in script.string:
                print(f"✅ Found __INITIAL_DATA__ in script {i}")
                initial_data_script = script.string
                break
                
        if not initial_data_script:
            print("❌ No __INITIAL_DATA__ found")
            return False
            
        # Step 4: Test regex extraction
        print("Step 4: Testing regex patterns...")
        
        # Old pattern (broken)
        old_match = re.search(r'window\.__INITIAL_DATA__=\"(.*)\"', initial_data_script)
        print(f"Old pattern match: {'✅' if old_match else '❌'}")
        
        # New pattern (should work)
        new_match = re.search(r'window\.__INITIAL_DATA__="(.*?)"(?:\s*;\s*$|\s*;|\s*$)', initial_data_script, re.DOTALL)
        print(f"New pattern match: {'✅' if new_match else '❌'}")
        
        if not new_match:
            print("Trying alternative patterns...")
            # Try without semicolon requirement
            alt_match1 = re.search(r'window\.__INITIAL_DATA__="(.*?)"', initial_data_script, re.DOTALL)
            print(f"Alternative pattern 1: {'✅' if alt_match1 else '❌'}")
            
            # Try with single quotes
            alt_match2 = re.search(r"window\.__INITIAL_DATA__='(.*?)'", initial_data_script, re.DOTALL)
            print(f"Alternative pattern 2: {'✅' if alt_match2 else '❌'}")
            
            # Show a sample of the script to see the actual format
            print(f"Script sample around __INITIAL_DATA__:")
            start = initial_data_script.find('__INITIAL_DATA__')
            if start >= 0:
                sample = initial_data_script[start-20:start+100]
                print(repr(sample))
                
            return False
            
        # Step 5: Parse JSON
        json_str = new_match.group(1).replace('\\\"', '"').replace('\\\\', '\\')
        print(f"✅ Extracted JSON string length: {len(json_str)}")
        
        try:
            data = json.loads(json_str)
            print("✅ Successfully parsed JSON")
        except json.JSONDecodeError as e:
            print(f"❌ JSON parse error: {e}")
            print(f"JSON sample: {json_str[:200]}...")
            return False
            
        # Step 6: Navigate to sports data
        data_section = data.get('data', {})
        print(f"✅ Found data section with {len(data_section)} keys")
        
        fixtures_key = None
        for key in data_section.keys():
            if 'sport-data-scores-fixtures' in key:
                fixtures_key = key
                break
                
        if fixtures_key:
            print(f"✅ Found fixtures key: {fixtures_key}")
            
            fixtures_data = data_section[fixtures_key]
            if 'data' in fixtures_data:
                match_data = fixtures_data['data']
                event_groups = match_data.get('eventGroups', [])
                print(f"✅ Found {len(event_groups)} event groups")
                
                for group in event_groups:
                    league_name = group.get('displayLabel', 'Unknown')
                    secondary_groups = group.get('secondaryGroups', [])
                    total_events = sum(len(sg.get('events', [])) for sg in secondary_groups)
                    print(f"  - {league_name}: {total_events} matches")
                    
                return True
            else:
                print("❌ No 'data' key in fixtures_data")
        else:
            print(f"❌ No sport-data-scores-fixtures key found")
            print(f"Available keys: {list(data_section.keys())}")
            
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    debug_extraction_step_by_step()