# Algo Trading System with ML & Automation

## Features
- Fetches data for NIFTY 50 stocks using yfinance
- Strategy: RSI + Moving Average crossover
- Logs trade signals and P&L in Google Sheets
- Includes ML model to predict next-day movement
- Telegram alerts for signals

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Set up Google Sheets API credentials (`credentials.json`)
3. Fill `config.py` with your settings
4. Run: `python main.py`

## Folders
- `utils/` contains modular functions
- `notebooks/` can be used for Jupyter analysis
- `logs/` can be used to store logs manually
- `data/` for storing fetched stock data manually