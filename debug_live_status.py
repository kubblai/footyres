#!/usr/bin/env python3

import json
import re
import requests
from bs4 import BeautifulSoup

def debug_live_status():
    print("Debugging live status extraction...")
    
    # Always fetch fresh data to see current live matches
    print("Fetching fresh data from BBC...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get('https://www.bbc.co.uk/sport/football/scores-fixtures', headers=headers)
    html_content = response.text
    
    # Save for debugging
    with open('debug_bbc_fresh.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the JSON data
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and '__INITIAL_DATA__' in script.string:
            # Extract JSON
            match = re.search(r'window\.__INITIAL_DATA__="(.*?)"(?:\s*;\s*$|\s*;|\s*$)', script.string, re.DOTALL)
            if match:
                json_str = match.group(1)
                # Clean up the JSON
                json_str = json_str.replace('\\"', '"').replace('\\\\', '\\')
                
                try:
                    data = json.loads(json_str)
                    
                    # Navigate to the fixtures data
                    data_section = data.get('data', {})
                    for key, value in data_section.items():
                        if 'sport-data-scores-fixtures' in key:
                            fixtures_data = value
                            break
                    
                    if 'fixtures_data' in locals():
                        match_data = fixtures_data['data']
                        event_groups = match_data.get('eventGroups', [])
                        
                        print("\n=== ANALYZING MATCH STATUS DATA ===")
                        
                        for group in event_groups:
                            league_name = group.get('displayLabel', 'Unknown')
                            print(f"\n--- {league_name} ---")
                            
                            for secondary in group.get('secondaryGroups', []):
                                for event in secondary.get('events', []):
                                    home = event.get('home', {}).get('fullName', 'Unknown')
                                    away = event.get('away', {}).get('fullName', 'Unknown')
                                    
                                    # Extract all status-related fields
                                    status = event.get('status', 'Unknown')
                                    period_label = event.get('periodLabel', {}).get('value', 'N/A')
                                    status_comment = event.get('statusComment', {}).get('value', 'N/A')
                                    event_progress = event.get('eventProgress', {})
                                    start_time = event.get('startDateTime', 'Unknown')
                                    
                                    print(f"\nMatch: {home} vs {away}")
                                    print(f"  Status: {status}")
                                    print(f"  Period Label: {period_label}")
                                    print(f"  Status Comment: {status_comment}")
                                    print(f"  Start Time: {start_time}")
                                    
                                    # Check for eventProgress data
                                    if event_progress:
                                        print(f"  Event Progress: {event_progress}")
                                    
                                    # Check for Club Brugge vs Rangers specifically
                                    if ('Club Brugge' in home or 'Club Brugge' in away or 
                                        'Rangers' in home or 'Rangers' in away):
                                        print(f"  *** FOUND TARGET MATCH ***")
                                        print(f"  Full event data: {json.dumps(event, indent=2)}")
                                        
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")
                    print(f"JSON string preview: {json_str[:500]}...")
                break

if __name__ == "__main__":
    debug_live_status()