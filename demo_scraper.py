#!/usr/bin/env python3
"""
Demo script showing the improved scorer display
"""

import sys
sys.path.append('.')
from football_scraper import FootballScraper

def demo_display():
    scraper = FootballScraper()
    
    # Fetch matches
    matches = scraper.fetch_matches()
    
    if matches:
        for league_name, league_matches in matches.items():
            scraper.display_league_matches(league_name, league_matches)
    else:
        print("No matches found")

if __name__ == "__main__":
    demo_display()