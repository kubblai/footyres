# Football Results Scraper (FootyRes)

A Python-based football results scraper that fetches live scores and match data from BBC Sport with an integrated stream search feature.

## Project Structure

- **Main Script**: `football_scraper.py` - Contains the entire application
- **Entry Point**: `footyres.sh` - Bash script to run the Python application
- **Dependencies**: Listed in `requirements.txt` (requests, beautifulsoup4, colorama)

## Key Components

### 1. StreamSearcher Class (`football_scraper.py:45-114`)
- **Purpose**: Search and validate streaming links for football matches
- **Streaming Sites**: 18 different streaming platforms including watchsports.to, sportyhunter.com, ppv.to, etc.
- **Key Methods**:
  - `validate_link()`: Checks if streaming URLs are accessible
  - `search_streams_for_match()`: Searches for working streams for specific matches

### 2. FootballScraper Class (`football_scraper.py:116+`)
- **Purpose**: Main application class handling data fetching, display, and user interaction
- **Key Attributes**:
  - `self.stream_searcher`: Instance of StreamSearcher class
  - `self.leagues`: Dictionary mapping league IDs to names and BBC Sport URLs
  - `self.current_streamable_matches`: Stores matches available for stream search

### Key Methods

#### Stream Search Features
- `is_streamable_match()` (`football_scraper.py:2632`): Determines if a match is live or starting within 30 minutes
- `display_streamable_matches()` (`football_scraper.py:2660`): Shows numbered list of streamable matches
- `search_and_display_streams()` (`football_scraper.py:2713`): Searches and displays working stream links
- `show_stream_search_menu()` (`football_scraper.py:2745`): Stream search interface
- `handle_stream_search_for_league()` (`football_scraper.py:2775`): Handles stream search workflow for specific leagues

#### Original Features
- `fetch_matches()`: Scrapes BBC Sport for match data
- `display_league_matches()`: Displays match results with scores, status, and actions
- `show_menu()`: Main menu interface
- `run()`: Main application loop

## Supported Leagues

1. Premier League
2. La Liga
3. Bundesliga
4. Serie A
5. Ligue 1
6. Primeira Liga
7. UEFA Champions League
8. MLS (Major League Soccer)

## Stream Search Feature

The app now includes a comprehensive stream search feature:

### How It Works
1. Select "Search Streams" option from main menu
2. Choose a league
3. App displays only matches that are:
   - Currently live (LIVE, HT, or showing minutes)
   - Starting within the next 30 minutes
4. Each match is numbered for easy selection
5. Select a match number to search for streams
6. App validates each streaming link before displaying
7. Shows working stream URLs with site names

### Streaming Sites Searched
- watchsports.to
- sportyhunter.com
- ppv.to
- sport7.pro
- fstv.online
- rbtv77.kaufen
- bintv.fun
- livetv.sx/enx
- viprow.nu
- timstreams.xyz
- totalsportek.at
- totalsportek.to
- crackstreams.blog
- goalietrend.com
- 720pstream.nu
- en12.sportplus.live
- soccerdoge.com
- app.buffstream.io

### Team Name Processing
- Uses actual team names from BBC Sport data (not constructed/fake names)
- Handles common team name variations (e.g., "Manchester City" → "manchester-city")
- Includes abbreviation matching for well-known teams (e.g., "Manchester United" → "man-utd", "mufc")
- Tests multiple URL patterns per streaming site (football/, soccer/, live/, stream/)

### Multi-Strategy Stream Search
1. **Real Match Scraping**: Scrapes all 18 streaming sites to find actual match listings (e.g., "LIV @ BUR" on watchsports.to)
2. **Constructed URLs**: Attempts direct links using team names (e.g., `site.com/football/burnley-vs-liverpool`)
3. **Base Site Fallback**: Provides working streaming sites with search hints when matches aren't found
4. **Category Links**: Links to football/soccer sections on sites for manual browsing

### Link Validation
- Strict validation for specific match URLs (HTTP 200 only)
- Relaxed validation for base sites (accepts 200, 302, 403 status codes)
- Uses proper User-Agent headers to avoid blocking
- Dual validation methods (HEAD request with GET fallback)
- Returns mix of direct links and searchable base sites for comprehensive coverage

## Usage

### Command Line
```bash
./footyres.sh
# or
python3 football_scraper.py
```

### Interactive Menu
- Select league number (1-8) for today's matches
- Use 'y' for yesterday's results
- Use 't' for tomorrow's fixtures
- Use 's' for stream search (new feature)
- Use 'q' to quit

### Stream Search Workflow
1. Main menu → 's' → Select league → View streamable matches
2. Enter match number → View working stream links
3. Copy/paste URLs to access streams

## Development Notes

### Code Style
- Uses colorama for terminal colors
- Object-oriented design with clear separation of concerns
- Comprehensive error handling for network requests
- Type hints used throughout

### Adding New Streaming Sites
To add new streaming sites, update the `streaming_sites` list in `StreamSearcher.__init__()` (`football_scraper.py:47`).

### Modifying Stream Search Logic
Stream search URL construction happens in `search_streams_for_match()` - modify the URL patterns there to match different site structures.

### Testing Stream Validation
The `validate_link()` method can be adjusted for different timeout values or validation criteria.

## Error Handling
- Network timeouts handled gracefully
- Invalid user inputs caught and handled
- Missing match data scenarios covered
- Stream validation failures handled silently

## Performance Considerations
- Stream validation can be slow due to network requests
- Limited to 3 working streams per match to balance speed vs options
- HEAD requests used instead of GET for faster validation
- User feedback provided during longer operations