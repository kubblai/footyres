#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def test_scraper_class():
    print("Testing FootballScraper class...")
    
    try:
        scraper = FootballScraper()
        print("✅ FootballScraper created successfully")
        
        print("Fetching matches...")
        all_matches = scraper.fetch_matches()
        
        if all_matches is None:
            print("❌ fetch_matches returned None")
            return False
            
        if isinstance(all_matches, dict):
            print(f"✅ Got match data: {len(all_matches)} leagues")
            
            for league_name, matches in all_matches.items():
                print(f"  - {league_name}: {len(matches)} matches")
                
            return True
        else:
            print(f"❌ Unexpected return type: {type(all_matches)}")
            return False
            
    except Exception as e:
        print(f"❌ Error in FootballScraper: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_scraper_class()