#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def test_all_leagues():
    print("Testing all leagues option...")
    
    try:
        scraper = FootballScraper()
        
        # Get all matches
        all_matches = scraper.fetch_matches()
        
        if all_matches is None:
            print("❌ No matches returned")
            return False
            
        if not all_matches:
            print("❌ Empty matches dictionary")
            return False
            
        print(f"✅ Found matches in {len(all_matches)} leagues:")
        for league_name, matches in all_matches.items():
            print(f"  - {league_name}: {len(matches)} matches")
            
        # Now test with process_choice to see what "0" (All Leagues) does
        print("\nTesting process_choice with '0' (All Leagues)...")
        # This should show all available leagues including the unmapped ones
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_all_leagues()