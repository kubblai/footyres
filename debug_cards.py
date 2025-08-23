#!/usr/bin/env python3
"""
Debug script to find red cards in BBC Sport JSON data
"""

from bs4 import BeautifulSoup
import re
import json

def debug_red_cards():
    with open('bbc_debug.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and '__INITIAL_DATA__' in script.string:
            match = re.search(r'window\.__INITIAL_DATA__="(.*)"', script.string)
            if match:
                json_str = match.group(1).replace('\\"', '"').replace('\\\\', '\\')
                data = json.loads(json_str)
                
                data_section = data.get('data', {})
                fixtures_key = None
                for key in data_section.keys():
                    if 'sport-data-scores-fixtures' in key:
                        fixtures_key = key
                        break
                
                if fixtures_key:
                    fixtures_data = data_section[fixtures_key]
                    match_data = fixtures_data['data']
                    event_groups = match_data.get('eventGroups', [])
                    
                    print('Looking for red cards in all matches...')
                    
                    for group in event_groups[:6]:  # Check our target leagues
                        league_name = group.get('displayLabel', 'Unknown')
                        print(f'\n=== {league_name} ===')
                        
                        for secondary in group.get('secondaryGroups', []):
                            for event in secondary.get('events', []):
                                home = event.get('home', {})
                                away = event.get('away', {})
                                
                                home_name = home.get('fullName', 'Unknown')
                                away_name = away.get('fullName', 'Unknown')
                                
                                # Check all actions for any disciplinary actions
                                all_actions = []
                                
                                for action in home.get('actions', []):
                                    action_type = action.get('actionType', '')
                                    if action_type != 'goal':
                                        all_actions.append((home_name, action))
                                
                                for action in away.get('actions', []):
                                    action_type = action.get('actionType', '')
                                    if action_type != 'goal':
                                        all_actions.append((away_name, action))
                                
                                if all_actions:
                                    print(f'\nMatch: {home_name} vs {away_name}')
                                    for team, action in all_actions:
                                        action_type = action.get('actionType', 'unknown')
                                        player = action.get('playerName', 'Unknown')
                                        print(f'  {team} - {player}: {action_type}')
                                        
                                        # Show the structure of the action
                                        for sub_action in action.get('actions', []):
                                            sub_type = sub_action.get('type', 'unknown')
                                            time_val = sub_action.get('timeLabel', {}).get('value', '?')
                                            print(f'    -> {sub_type} at {time_val}')
                                        
            break

if __name__ == "__main__":
    debug_red_cards()