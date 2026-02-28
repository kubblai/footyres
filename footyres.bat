@echo off
REM Football Results Scraper - Windows Batch Script
REM Runs the football_scraper.py script with Python
set "PIP_VERSION=26.0.1"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check Python version (requires 3.14+)
python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 14) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python 3.14 or newer is required
    pause
    exit /b 1
)

REM Ensure pip version is up to date for this project
python -m pip install --disable-pip-version-check -q --upgrade pip==%PIP_VERSION%
if %errorlevel% neq 0 (
    echo Error: Failed to upgrade pip to %PIP_VERSION%
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import requests, bs4, colorama" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Error: Failed to install required packages
        pause
        exit /b 1
    )
)

REM Run the script with all arguments passed to this batch file
python football_scraper.py %*
