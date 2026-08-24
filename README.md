# Football Results Scraper

🏆 **2026-27 live football results and league tables from BBC Sport with an interactive terminal interface.**

## Preview
```
🏆 FOOTBALL RESULTS SCRAPER - 2026-27 🏆
============================================================
Select a league to view:
[1] Premier League  [2] La Liga  [3] Bundesliga
[4] Serie A  [5] Ligue 1  [6] Primeira Liga
[7] UEFA Champions League  [8] MLS  [9] Allsvenskan
[0] All Leagues  [q] Quit
```

## Features

✅ **Live Match Results** - Real-time scores, goal scorers, and match status
✅ **Now Playing** - Auto-refreshing view of live matches, matches starting within 30 minutes, and matches that just finished (all leagues)
✅ **League Tables** - Current standings with real BBC Sport statistics
✅ **Stream Search** - Find working stream links for live/upcoming matches across 18+ streaming sites
✅ **9 Major Leagues** - Premier League, La Liga, Bundesliga, Serie A, Ligue 1, Primeira Liga, UEFA Champions League, MLS, Allsvenskan
✅ **Command-Line Flags** - Direct league access with `--pl`, `--cl`, `--mls`, `--all`, etc.
✅ **Form Indicators** - W/D/L boxes showing recent team performance
✅ **HT/Live Markers** - Half-time and live match status indicators
✅ **Auto-Update** - Refreshes every 30 seconds
✅ **Colorized Display** - Win/loss colors and league table formatting  

## Quick Start

### Requirements

- Python `3.14.3`
- pip `26.0.1`

### Linux / macOS

```bash
# Option 1: Use runner script (recommended)
chmod +x footyres.sh
./footyres.sh                    # Interactive menu
./footyres.sh --cl               # Direct Champions League access
./footyres.sh --help             # Show all CLI options

# Option 2: Manual installation
python3.14 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip==26.0.1
python -m pip install -r requirements.txt
python football_scraper.py
```

### Windows

```cmd
# Option 1: Use batch script (recommended)
footyres.bat                     # Interactive menu
footyres.bat --cl                # Direct Champions League access
footyres.bat --help              # Show all CLI options

# Option 2: Manual installation
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip==26.0.1
python -m pip install -r requirements.txt
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
python football_scraper.py --as          # Allsvenskan (Swedish League)
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
python football_scraper.py --allsvenskan # Same as --as
```

#### Return to Menu
After viewing league results with flags, you can:
- Press `m` to go to the main menu
- Press `Enter` to exit
- Use the normal navigation options (`r` refresh, `t` table, etc.)

#### Examples

**Linux / macOS:**
```bash
# Using runner script (recommended)
./footyres.sh --cl               # Champions League today
./footyres.sh --pl -y            # Premier League yesterday
./footyres.sh --mls              # MLS standings and matches
./footyres.sh --as               # Allsvenskan today
./footyres.sh --help             # Show help

# Using Python directly
python3.14 football_scraper.py --cl
python3.14 football_scraper.py --pl --yesterday
python3.14 football_scraper.py --mls
python3.14 football_scraper.py --help
```

**Windows:**
```cmd
# Using batch script (recommended)
footyres.bat --cl                # Champions League today
footyres.bat --pl -y             # Premier League yesterday
footyres.bat --mls               # MLS standings and matches
footyres.bat --as                # Allsvenskan today
footyres.bat --help              # Show help

# Using Python directly
python football_scraper.py --cl
python football_scraper.py --pl --yesterday
python football_scraper.py --mls
python football_scraper.py --help
```

### Interactive Menu (Traditional)

Run without any flags for the traditional interactive menu:

**Linux / macOS:**
```bash
./footyres.sh
# or
python3.14 football_scraper.py
```

**Windows:**
```cmd
footyres.bat
# or
python football_scraper.py
```

**Main Menu:**
- `[1-9]` - Individual leagues (including MLS as [8] and Allsvenskan as [9])
- `[0]` - View all leagues
- `[n]` - Now Playing (live / starting soon / just finished, all leagues)
- `[y]` - Yesterday's results
- `[t]` - Tomorrow's fixtures
- `[s]` - Search streams for live/upcoming matches
- `[q]` - Quit

## Now Playing Feature

Select `[n]` from the main menu for a live dashboard covering **all leagues at once**, which refreshes automatically every 30 seconds (press `Ctrl+C` to return to the menu).

It shows three groups of matches:

- **LIVE NOW** - Matches currently in play (including half-time and minute indicators like `67'`)
- **STARTING SOON (NOT YET STARTED)** - Fixtures kicking off within the next 30 minutes, with a "starts in X min" countdown
- **JUST FINISHED** - Final scores of matches that ended within the last 30 minutes

Sample output:

```
⚽ NOW PLAYING - ALL LEAGUES ⚽

--- LIVE NOW ---
 14:00 Arsenal 2-1 Chelsea [67'] (Premier League)
 14:30 Getafe vs Sevilla HT (La Liga)

--- STARTING SOON (NOT YET STARTED) ---
 15:45 Inter vs Juventus [NOT STARTED] (starts in 12 min) (Serie A)

--- JUST FINISHED ---
 13:30 Celtic 2-0 Rangers [JUST FINISHED] (FT) (Premier League)
```

> Finished matches are detected by estimating full time as kick-off plus a typical match duration (~110 minutes), since BBC Sport does not publish an end timestamp.


**League View:**
- `[r]` - Refresh results
- `[a]` - Auto-update mode
- `[m]` - Return to menu
- `[Enter]` - View league table

## Stream Search Feature

The app now includes a powerful stream search feature that finds working stream links for live and upcoming matches (within the next hour).

### How It Works

1. **Access**: Select `[s]` from the main menu or press `[s]` in any league view
2. **Match Selection**: Choose a league to see numbered list of streamable matches
3. **Stream Search**: Select a match number (1-N) to search for working streams
4. **Results**: Get up to 10+ working stream links, prioritized by reliability

### Supported Streaming Sites

The searcher checks 18+ streaming platforms including:
- **ppv.to** (prioritized with league-specific URLs)
- watchsports.to, sportyhunter.com, crackstreams.com
- streameast.io, buffstreams.tv, sportsurge.net
- And many more...

### Stream Search Examples

```
🔴 LIVE/UPCOMING MATCHES - La Liga:

1. 🟢 LIVE    Real Madrid vs Barcelona     [45' - HT]
2. 🔵 19:30   Celta Vigo vs Girona         [Starting soon]
3. 🔵 21:45   Valencia vs Sevilla          [Upcoming]

Enter match number (1-3) to search for streams...
```

**Sample Stream Results:**
```
🎯 Found 12 working streams for Real Madrid vs Barcelona:

🥇 PRIORITY STREAMS (ppv.to):
1. https://ppv.to/live/laliga/2026-09-14/rmad-bar

🥈 DIRECT MATCH STREAMS:
2. https://watchsports.to/live/madrid-barcelona
3. https://streameast.io/soccer/el-clasico-live

🥉 CATEGORY STREAMS:
4. https://crackstreams.com/soccer/la-liga
...
```

### Stream Search Features

✅ **Live Match Detection** - Automatically finds matches starting within 1 hour or already live
✅ **League-Specific URLs** - ppv.to links use correct league codes (epl, laliga, bundesliga, etc.)
✅ **Link Validation** - All URLs are tested before display
✅ **Priority Sorting** - Direct match links prioritized over category pages
✅ **Multi-Site Search** - Searches across 18+ streaming platforms simultaneously
✅ **Team Name Processing** - Handles various team name formats and abbreviations

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
- **2026-27 Season**: Team names, fixtures, scores, and standings come from BBC Sport rather than a hardcoded club list
- **Educational Use**: Designed for personal/educational purposes
- **Cross-Platform**: Works on Linux, macOS, Windows
- **No Fabricated Standings**: Reports when BBC data is unavailable instead of showing stale sample data
