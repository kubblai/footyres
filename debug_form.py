#!/usr/bin/env python3

from football_scraper import FootballScraper

# Create scraper instance
scraper = FootballScraper()

print("Testing updated form extraction...")

# Fetch La Liga table data using the correct key
print("Fetching La Liga table data...")
table_data = scraper.fetch_league_table("2")

if table_data:
    print(f"Found {len(table_data)} teams")
    # Look for Real Madrid specifically
    for team in table_data:
        if 'real madrid' in team.get('team', '').lower():
            print(f"\nREAL MADRID DATA:")
            print(f"Team: {team.get('team')}")
            print(f"Played: {team.get('played')}")
            print(f"Won: {team.get('won')}")
            print(f"Form data: {team.get('form')}")
            print(f"Form type: {type(team.get('form'))}")
            
            # Test form generation
            form_result = scraper.generate_team_form(team, team.get('played', 0))
            print(f"Generated form: '{form_result}'")
            break
    
    # Also check a few other teams
    for team in table_data[:5]:
        print(f"\n{team.get('team')}: form = {team.get('form')}")
else:
    print("No table data found")