#!/usr/bin/env python3

import sys
import os
import requests
from bs4 import BeautifulSoup
import json
import re

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def debug_scraper_detailed():
    print("Debugging FootballScraper in detail...")
    
    # Create scraper
    scraper = FootballScraper()
    
    # Fetch the page manually like the scraper does
    try:
        response = scraper.session.get(scraper.base_url, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print(f"✅ Fetched page: {response.status_code}")
        
        # Call extract_json_matches directly
        print("Calling extract_json_matches...")
        result = scraper.extract_json_matches(soup)
        
        if result is None:
            print("❌ extract_json_matches returned None")
        elif isinstance(result, dict):
            print(f"✅ extract_json_matches returned dict with {len(result)} leagues")
            for league_name, matches in result.items():
                print(f"  - {league_name}: {len(matches)} matches")
        else:
            print(f"❌ Unexpected return type: {type(result)}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_scraper_detailed()