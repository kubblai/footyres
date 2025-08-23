#!/bin/bash
# Football Scraper Runner Script

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
source venv/bin/activate
pip install -q -r requirements.txt

# Run the scraper
echo "Starting Football Scraper..."
python football_scraper.py