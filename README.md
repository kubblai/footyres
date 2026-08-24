# Football Results Scraper

An interactive terminal app for 2026-27 football fixtures, live scores, incidents, and league tables from [BBC Sport](https://www.bbc.co.uk/sport/football).

## Features

- Live and scheduled matches across nine competitions
- Current BBC league tables and form guides
- A 30-second Now Playing dashboard for all leagues
- Live score, match minute, scorers, and yellow/red cards
- Yesterday, today, and tomorrow views
- Direct league access through command-line flags
- Best-effort stream-link search for live and upcoming matches
- Colorized Linux, macOS, and Windows terminal output

Supported competitions: Premier League, La Liga, Bundesliga, Serie A, Ligue 1, Primeira Liga, UEFA Champions League, MLS, and Allsvenskan.

## Requirements

- Python 3.14+
- pip 26.0.1

## Install And Run

### Linux / macOS

```bash
chmod +x footyres.sh
./footyres.sh
```

### Windows

```cmd
footyres.bat
```

The launchers install dependencies automatically. To run manually:

```bash
python3.14 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python -m pip install -r requirements.txt
python football_scraper.py
```

## Command Line

Open a league directly instead of using the menu:

| Competition | Flags |
| --- | --- |
| Premier League | `--pl`, `--premier` |
| La Liga | `--la`, `--laliga` |
| Bundesliga | `--bu`, `--bundesliga` |
| Serie A | `--sa`, `--seriea` |
| Ligue 1 | `--l1`, `--ligue1` |
| Primeira Liga | `--pr`, `--primeira` |
| UEFA Champions League | `--cl`, `--champions` |
| MLS | `--mls`, `--majorleague` |
| Allsvenskan | `--as`, `--allsvenskan` |
| All leagues | `--all` |

Use `-y` / `--yesterday` or `-t` / `--tomorrow` with a league flag:

```bash
./footyres.sh --pl -y
./footyres.sh --cl
python football_scraper.py --mls -t
python football_scraper.py --help
```

## Interactive Controls

From the main menu:

| Key | Action |
| --- | --- |
| `1`-`9` | Open a competition |
| `0` | Show all leagues |
| `n` | Open Now Playing |
| `y` / `t` | Show yesterday / tomorrow |
| `s` | Search for streams |
| `q` | Quit |

League views support refresh (`r`), auto-update (`a`), stream search (`s`), table view (`Enter`), and return to menu (`m`).

## Now Playing

Now Playing combines all supported leagues and refreshes every 30 seconds. Press `Ctrl+C` to return to the menu.

- **Live Now:** score, current minute or half-time, scorers, and yellow/red cards
- **Starting Soon:** fixtures beginning within 30 minutes
- **Just Finished:** final scores for matches estimated to have ended within 30 minutes

```text
--- LIVE NOW ---
 14:00 Arsenal 2-1 Chelsea [67'] (Premier League)
      Arsenal:
        ⚽ B. Saka 12'
        🟨 D. Rice 44'
      Chelsea:
        ⚽ C. Palmer 51'
        🟥 M. Cucurella 65'
```

BBC match-detail requests are fetched concurrently to keep refreshes timely. If card details cannot be loaded, the dashboard reports them as unavailable rather than silently presenting incomplete data.

## Live Data Behavior

BBC Sport is the source of truth for team names, fixtures, scores, incidents, form, and standings. The scraper reads BBC's embedded structured data first and uses HTML/text parsing only as a fallback.

The 2026-27 update removed season-specific team rosters, stale team-ID mappings, and fabricated table fallbacks. When BBC data is unavailable or changes shape, the app reports that data as unavailable instead of showing sample results or standings.

Finished-match timing in Now Playing is estimated from kick-off plus a typical 110-minute match duration because BBC does not provide an end timestamp.

## Development

See [`AGENTS.md`](AGENTS.md) for repository conventions and validation guidance. Core checks are:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m ruff check .
PYTHONDONTWRITEBYTECODE=1 python test_all_leagues.py
PYTHONDONTWRITEBYTECODE=1 python -m py_compile football_scraper.py
git diff --check
```

`test_all_leagues.py` and table checks use the live BBC website, so results vary with the current schedule.

## Dependencies

- `requests`
- `beautifulsoup4`
- `colorama`

This project is intended for personal and educational use. External stream links are third-party content and may be unavailable.
