# Football Results Scraper

🏆 **Real-time football results and league tables from BBC Sport with interactive terminal interface.**

## Features

✅ **Live Match Results** - Real-time scores, goal scorers, and match status  
✅ **League Tables** - Current standings with real BBC Sport statistics  
✅ **6 Major Leagues** - Premier League, La Liga, Bundesliga, Serie A, Ligue 1, Primeira Liga  
✅ **Form Indicators** - W/D/L boxes showing recent team performance  
✅ **HT/Live Markers** - Half-time and live match status indicators  
✅ **Auto-Update** - Refreshes every 30 seconds  
✅ **Colorized Display** - Win/loss colors and league table formatting  

## Quick Start

```bash
# Option 1: Use runner script (recommended)
chmod +x footyres.sh
./footyres.sh

# Option 2: Manual installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python football_scraper.py
```

## Usage

**Main Menu:**
- `[1-6]` - Select individual league
- `[0]` - View all leagues
- `[y]` - Yesterday's results  
- `[t]` - Tomorrow's fixtures
- `[q]` - Quit

**League View:**
- `[r]` - Refresh results
- `[a]` - Auto-update mode
- `[m]` - Return to menu
- `[Enter]` - View league table

## Sample Output

```
🟢1   Arsenal                   2   2   0   0   6    0    +6   6    W W
🟢2   Tottenham Hotspur         2   2   0   0   5    0    +5   6    L W  
🟢3   Chelsea                   2   1   1   0   5    1    +4   4    W L
🟢4   Nottingham Forest         2   1   1   0   4    2    +2   4    D L

Match 1: 15:00
  Manchester City               2-1  Arsenal                [HT]
  ⚽ Haaland 23'                     ⚽ Saka 45'
```

## Dependencies

- `requests` - BBC Sport API calls
- `beautifulsoup4` - HTML parsing  
- `colorama` - Terminal colors

## Notes

- **Real Data**: Extracts live statistics from BBC Sport tables
- **Educational Use**: Designed for personal/educational purposes
- **Cross-Platform**: Works on Linux, macOS, Windows
- **Offline Fallback**: Shows sample data if BBC Sport unavailable
