Football Results Scraper with Interactive Menu

A Python application that scrapes football results from BBC Sport and displays them in a colorized terminal interface. Features an interactive menu system for selecting individual leagues or viewing all leagues together.
Features

    Interactive Menu System: Choose individual leagues or view all at once
    Live Updates: Refreshes every 30 seconds with auto-update mode
    Colorized Display: Different colors for winning/losing teams and league headers
    Major Leagues: Shows results for:
        Premier League (England)
        Spanish La Liga
        German Bundesliga
        Italian Serie A
        French Ligue 1
        Portuguese Primeira Liga
    Goal Scorers: Displays goal scorers with timing when available
    Navigation Options: Easy navigation between menu, refresh, and auto-update
    Clean Interface: Clear terminal display with organized match information

Installation

Clone or download the files:

    football_scraper.py - Main scraper application
    requirements.txt - Python dependencies
    run_scraper.sh - Convenience runner script

Install dependencies:

# Option 1: Use the runner script (recommended)
chmod +x run_scraper.sh
./run_scraper.sh

# Option 2: Manual installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python football_scraper.py

Usage
Quick Start

./run_scraper.sh

Manual Execution

# Activate virtual environment
source venv/bin/activate

# Run the scraper
python football_scraper.py

Menu Navigation

    Main Menu: Select league by number (1-6) or 0 for all leagues
    League View:
        [r] Refresh - Get latest results
        [a] Auto-update - Updates every 30 seconds
        [m] Main menu - Return to main menu
    Controls:
        Ctrl+C: Return to menu (during auto-update) or quit (from menu)
        q: Quit application

Output Example
Main Menu

============================================================
 ⚽ FOOTBALL RESULTS SCRAPER ⚽ 
============================================================

Select a league to view:

[1] Premier League
[2] La Liga
[3] Bundesliga
[4] Serie A
[5] Ligue 1
[6] Primeira Liga
[0] All Leagues

[q] Quit

League Results View

Updated: 2025-08-23 15:30:45

======================================================================
 PREMIER LEAGUE - 2025-08-23 
======================================================================

Match 1: 15:00
  Manchester City           2-1 Arsenal                   [FT]
  Goal scorers:
    ⚽ Haaland 23'
    ⚽ De Bruyne 67'
    ⚽ Saka 45'

Match 2: 17:30
  Liverpool                 3-2 Chelsea                   [FT]
  Goal scorers:
    ⚽ Salah 12'
    ⚽ Mané 34'
    ⚽ Firmino 78'
    ⚽ Sterling 25'
    ⚽ Mount 89'

==================================================
Options:
[r] Refresh  [a] Auto-update (30s)  [m] Main menu

Color Coding

    Green: Winning team
    Red: Losing team
    Yellow: Draw
    Cyan: League headers and borders
    Yellow: Goal scorers (⚽)
    Magenta: Match status

Dependencies

    requests - HTTP requests to BBC Sport
    beautifulsoup4 - HTML parsing
    colorama - Cross-platform colored terminal output

Notes

    The scraper attempts to fetch live data from BBC Sport
    If BBC Sport blocks requests or data is unavailable, it displays sample data
    Requires an internet connection
    Works on Linux, macOS, and Windows
    The scraper is designed for educational and personal use

Troubleshooting

    Module not found errors: Make sure to activate the virtual environment
    Permission denied: Run chmod +x run_scraper.sh to make the script executable
    No data displayed: BBC Sport may be blocking requests; the app will show sample data
    Terminal colors not working: Install colorama: pip install colorama

Customization
You can modify the target leagues by editing the target_leagues dictionary in the FootballScraper class.
