#!/bin/bash
# Football Scraper Runner Script

# Check for --help flag
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Football Results Scraper - Live scores from BBC Sport"
    echo ""
    echo "Usage:"
    echo "  ./footyres.sh [options]     Run with league flags"
    echo "  ./footyres.sh               Run interactive menu"
    echo ""
    echo "League Flags:"
    echo "  --pl, --premier      Premier League"
    echo "  --la, --laliga       La Liga"
    echo "  --bu, --bundesliga   Bundesliga"
    echo "  --sa, --seriea       Serie A"
    echo "  --l1, --ligue1       Ligue 1"
    echo "  --pr, --primeira     Primeira Liga"
    echo "  --cl, --champions    UEFA Champions League"
    echo "  --mls, --majorleague MLS (Major League Soccer)"
    echo "  --all                All Leagues"
    echo ""
    echo "Date Options:"
    echo "  -y, --yesterday      Yesterday's results"
    echo "  -t, --tomorrow       Tomorrow's fixtures"
    echo ""
    echo "Examples:"
    echo "  ./footyres.sh --cl           # Champions League today"
    echo "  ./footyres.sh --pl -y        # Premier League yesterday"
    echo "  ./footyres.sh --mls -t       # MLS tomorrow"
    echo "  ./footyres.sh --help         # Show this help"
    echo ""
    exit 0
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
source venv/bin/activate
pip install -q -r requirements.txt

# Run the scraper with all passed arguments
echo "Starting Football Scraper..."
python football_scraper.py "$@"