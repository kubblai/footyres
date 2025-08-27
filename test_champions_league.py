#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def test_champions_league():
    print("Testing Champions League matches...")
    scraper = FootballScraper()
    
    try:
        all_matches = scraper.fetch_matches()
        
        if 'UEFA Champions League' in all_matches:
            matches = all_matches['UEFA Champions League']
            print(f"\n=== UEFA CHAMPIONS LEAGUE ===")
            print(f"Found {len(matches)} matches")
            
            for i, match in enumerate(matches, 1):
                home_team = match.get('home_team', 'Unknown')
                away_team = match.get('away_team', 'Unknown')
                home_score = match.get('home_score', 0)
                away_score = match.get('away_score', 0)
                status = match.get('status', '')
                match_time = match.get('time', '')
                
                print(f"\nMatch {i}: {match_time}")
                print(f"  {home_team:<30} {home_score}-{away_score} {away_team:<30} {status}")
                
                # Look specifically for Club Brugge vs Rangers
                if 'Club Brugge' in home_team or 'Rangers' in away_team or 'Brugge' in home_team:
                    print(f"  *** FOUND TARGET MATCH ***")
                    print(f"  Status: {status} (should show [HT] not [FT])")
        else:
            print("No Champions League matches found")
            print(f"Available leagues: {list(all_matches.keys())}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_champions_league()