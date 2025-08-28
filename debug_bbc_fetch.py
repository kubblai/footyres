#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import re

def test_bbc_fetch():
    print("Testing BBC Sport data fetching...")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        print("Fetching BBC Sport page...")
        response = requests.get('https://www.bbc.co.uk/sport/football/scores-fixtures', headers=headers, timeout=10)
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Content length: {len(response.content)}")
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch page: HTTP {response.status_code}")
            return
            
        print("✅ Successfully fetched page")
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Parsed HTML successfully")
        
        # Look for the JSON data
        scripts = soup.find_all('script')
        print(f"Found {len(scripts)} script tags")
        
        json_found = False
        for i, script in enumerate(scripts):
            if script.string and '__INITIAL_DATA__' in script.string:
                print(f"✅ Found __INITIAL_DATA__ in script tag {i}")
                json_found = True
                
                # Try to extract JSON
                match = re.search(r'window\.__INITIAL_DATA__="(.*?)"(?:\s*;\s*$|\s*;|\s*$)', script.string, re.DOTALL)
                if match:
                    print("✅ Successfully extracted JSON string")
                    json_str = match.group(1)
                    print(f"JSON string length: {len(json_str)}")
                    
                    # Clean up and parse
                    try:
                        json_str = json_str.replace('\\"', '"').replace('\\\\', '\\')
                        data = json.loads(json_str)
                        print("✅ Successfully parsed JSON")
                        
                        # Look for match data
                        data_section = data.get('data', {})
                        sports_data_found = False
                        
                        for key in data_section.keys():
                            if 'sport-data-scores-fixtures' in key:
                                print(f"✅ Found sports data key: {key}")
                                sports_data_found = True
                                
                                fixtures_data = data_section[key]
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
                                    
                        if not sports_data_found:
                            print("❌ No sport-data-scores-fixtures found in data keys")
                            print(f"Available keys: {list(data_section.keys())}")
                            
                    except json.JSONDecodeError as e:
                        print(f"❌ JSON decode error: {e}")
                        print(f"JSON preview: {json_str[:500]}...")
                        
                else:
                    print("❌ Could not extract JSON from script tag")
                    
                break
                
        if not json_found:
            print("❌ No __INITIAL_DATA__ found in any script tags")
            
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_bbc_fetch()