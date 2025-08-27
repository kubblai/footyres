#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def test_display_aggregate():
    print("Testing aggregate score display...")
    scraper = FootballScraper()
    
    try:
        all_matches = scraper.fetch_matches()
        
        if 'UEFA Champions League' in all_matches:
            matches = all_matches['UEFA Champions League']
            print("Calling display_league_matches...")
            scraper.display_league_matches('UEFA Champions League', matches)
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_display_aggregate()