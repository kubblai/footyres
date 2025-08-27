#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def debug_aggregate():
    print("Debugging aggregate scores...")
    scraper = FootballScraper()
    
    try:
        all_matches = scraper.fetch_matches()
        
        if 'UEFA Champions League' in all_matches:
            matches = all_matches['UEFA Champions League']
            print(f"\n=== UEFA CHAMPIONS LEAGUE DEBUG ===")
            
            for match in matches:
                home_team = match.get('home_team', 'Unknown')
                away_team = match.get('away_team', 'Unknown')
                
                # Look specifically for Club Brugge vs Rangers
                if 'Club Brugge' in home_team or 'Rangers' in away_team or 'Brugge' in home_team:
                    print(f"\n*** FOUND TARGET MATCH ***")
                    print(f"Match: {home_team} vs {away_team}")
                    print(f"is_multi_leg: {match.get('is_multi_leg', 'NOT SET')}")
                    print(f"home_agg: {match.get('home_agg', 'NOT SET')}")
                    print(f"away_agg: {match.get('away_agg', 'NOT SET')}")
                    print(f"Full match data keys: {list(match.keys())}")
                    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_aggregate()