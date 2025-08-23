#!/usr/bin/env python3
"""
Debug script to examine missing scorers in high-scoring matches
"""

from bs4 import BeautifulSoup
import re
import json

def debug_missing_scorers():
    # Look at the raw JSON for Arsenal vs Leeds United (5-0 with missing scorers)
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
                    
                    # Find Premier League
                    for group in event_groups:
                        if group.get('displayLabel') == 'Premier League':
                            for secondary in group.get('secondaryGroups', []):
                                for event in secondary.get('events', []):
                                    home = event.get('home', {})
                                    away = event.get('away', {})
                                    
                                    home_name = home.get('fullName', '')
                                    away_name = away.get('fullName', '')
                                    home_score = home.get('score', 0)
                                    away_score = away.get('score', 0)
                                    
                                    # Look for Arsenal vs Leeds match
                                    if 'Arsenal' in home_name and 'Leeds' in away_name:
                                        print(f'Found: {home_name} {home_score}-{away_score} {away_name}')
                                        print()
                                        print('Home team (Arsenal) actions:')
                                        home_actions = home.get('actions', [])
                                        print(f'  Total actions: {len(home_actions)}')
                                        
                                        goal_count = 0
                                        for i, action in enumerate(home_actions):
                                            action_type = action.get('actionType', 'unknown')
                                            player = action.get('playerName', 'Unknown')
                                            print(f'  Action {i+1}: {action_type} by {player}')
                                            
                                            # Check ALL action types, not just 'goal'
                                            goal_actions = action.get('actions', [])
                                            for goal_action in goal_actions:
                                                goal_type = goal_action.get('type', 'unknown')
                                                time_val = goal_action.get('timeLabel', {}).get('value', '?')
                                                print(f'    -> {goal_type}: {player} {time_val}')
                                                
                                                # Count goals of any type
                                                if 'goal' in goal_type.lower():
                                                    goal_count += 1
                                        
                                        print(f'  Total goals found in actions: {goal_count}')
                                        home_score_int = int(home_score)
                                        print(f'  Expected goals (from score): {home_score_int}')
                                        
                                        if goal_count != home_score_int:
                                            print(f'  ⚠️  MISMATCH! Missing {home_score_int - goal_count} goals')
                                        
                                        return
            break

if __name__ == "__main__":
    debug_missing_scorers()