#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def debug_fetch_step_by_step():
    print("Debugging fetch_matches step by step...")
    
    scraper = FootballScraper()
    
    try:
        # Manually execute each step of fetch_matches
        
        # Step 1: Fetch page
        response = scraper.session.get(scraper.base_url, timeout=15)
        print(f"Step 1 - Fetch: {response.status_code}")
        
        # Step 2: Parse HTML
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Step 2 - Parse HTML: OK")
        
        # Step 3: Parse BBC matches
        parsed_matches = scraper.parse_bbc_matches(soup)
        if parsed_matches is None:
            print("Step 3 - parse_bbc_matches: returned None")
        elif isinstance(parsed_matches, dict):
            print(f"Step 3 - parse_bbc_matches: returned dict with {len(parsed_matches)} leagues")
            for league_name, matches in parsed_matches.items():
                print(f"  - {league_name}: {len(matches)} matches")
        else:
            print(f"Step 3 - parse_bbc_matches: unexpected type {type(parsed_matches)}")
            
        return parsed_matches
        
    except Exception as e:
        print(f"❌ Error in debug: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = debug_fetch_step_by_step()
    print(f"\nFinal result: {result}")
    if result is not None:
        print("✅ Should work!")
    else:
        print("❌ Still broken")