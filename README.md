# Football Results Scraper

🏆 **Real-time football results and league tables from BBC Sport with interactive terminal interface.**

## Demo

[![asciicast](https://asciinema.org/a/demo.cast.svg)](https://asciinema.org/a/demo.cast)

*Note: Upload demo.cast to [asciinema.org](https://asciinema.org) and replace the URL above with your recording ID for the demo to work on GitHub.*

### Preview
```
🏆 FOOTBALL RESULTS SCRAPER 🏆
============================================================
Select a league to view:
[1] Premier League  [2] La Liga  [3] Bundesliga
[4] Serie A  [5] Ligue 1  [6] Primeira Liga
[7] UEFA Champions League  [8] MLS
[0] All Leagues  [q] Quit
```

## Features

✅ **Live Match Results** - Real-time scores, goal scorers, and match status  
✅ **League Tables** - Current standings with real BBC Sport statistics  
✅ **8 Major Leagues** - Premier League, La Liga, Bundesliga, Serie A, Ligue 1, Primeira Liga, UEFA Champions League, MLS  
✅ **Command-Line Flags** - Direct league access with `--pl`, `--cl`, `--mls`, etc.  
✅ **Form Indicators** - W/D/L boxes showing recent team performance  
✅ **HT/Live Markers** - Half-time and live match status indicators  
✅ **Auto-Update** - Refreshes every 30 seconds  
✅ **Colorized Display** - Win/loss colors and league table formatting  

## Quick Start

```bash
# Option 1: Use runner script (recommended)
chmod +x footyres.sh
./footyres.sh                    # Interactive menu
./footyres.sh --cl               # Direct Champions League access
./footyres.sh --help             # Show all CLI options

# Option 2: Manual installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python football_scraper.py
```

## Usage

### Command-Line Flags (New!)

You can now jump directly into any league using command-line flags:

#### League Flags
```bash
python football_scraper.py --cl          # UEFA Champions League
python football_scraper.py --pl          # Premier League  
python football_scraper.py --la          # La Liga
python football_scraper.py --bu          # Bundesliga
python football_scraper.py --sa          # Serie A
python football_scraper.py --l1          # Ligue 1
python football_scraper.py --pr          # Primeira Liga
python football_scraper.py --mls         # MLS (Major League Soccer)
python football_scraper.py --all         # All Leagues
```

#### Date Options
```bash
python football_scraper.py --cl -y       # Champions League yesterday
python football_scraper.py --pl -t       # Premier League tomorrow
```

#### Alternative Flag Names
```bash
python football_scraper.py --champions   # Same as --cl
python football_scraper.py --premier     # Same as --pl
python football_scraper.py --laliga      # Same as --la
python football_scraper.py --bundesliga  # Same as --bu
python football_scraper.py --seriea      # Same as --sa
python football_scraper.py --ligue1      # Same as --l1
python football_scraper.py --primeira    # Same as --pr
python football_scraper.py --majorleague # Same as --mls
```

#### Return to Menu
After viewing league results with flags, you can:
- Press `m` to go to the main menu
- Press `Enter` to exit
- Use the normal navigation options (`r` refresh, `t` table, etc.)

#### Examples
```bash
# Using runner script (recommended)
./footyres.sh --cl               # Champions League today
./footyres.sh --pl -y            # Premier League yesterday
./footyres.sh --mls              # MLS standings and matches
./footyres.sh --help             # Show help

# Using Python directly
python football_scraper.py --cl
python football_scraper.py --pl --yesterday
python football_scraper.py --mls
python football_scraper.py --help
```

### Interactive Menu (Traditional)

Run without any flags for the traditional interactive menu:
```bash
python football_scraper.py
```

**Main Menu:**
- `[1-8]` - Individual leagues (including MLS as [8])
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
- `argparse` - Command-line argument parsing (built-in)

## Notes

- **Real Data**: Extracts live statistics from BBC Sport tables
- **Educational Use**: Designed for personal/educational purposes
- **Cross-Platform**: Works on Linux, macOS, Windows
- **Offline Fallback**: Shows sample data if BBC Sport unavailable
