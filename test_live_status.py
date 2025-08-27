#!/usr/bin/env python3

import sys
import os

# Add current directory to path so we can import the scraper
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from football_scraper import FootballScraper

def test_live_status():
    print("Testing live status extraction...")
    scraper = FootballScraper()
    
    # Get today's matches from BBC
    try:
        all_matches = scraper.fetch_matches()
        
        print(f"\n=== LIVE MATCHES DETECTED ===")
        
        for league_name, matches in all_matches.items():
            if not matches:
                continue
                
            live_matches = []
            for match in matches:
                status = match.get('status', '')
                if status and status != 'FT' and status != '':
                    live_matches.append(match)
            
            if live_matches:
                print(f"\n--- {league_name} ---")
                for match in live_matches:
                    home_team = match.get('home_team', 'Unknown')
                    away_team = match.get('away_team', 'Unknown')
                    home_score = match.get('home_score', 0)
                    away_score = match.get('away_score', 0)
                    status = match.get('status', '')
                    match_time = match.get('time', '')
                    
                    print(f"  {home_team} {home_score}-{away_score} {away_team} - Status: [{status}] (Kick-off: {match_time})")
                    
    except Exception as e:
        print(f"Error getting matches: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_live_status()