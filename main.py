from utils.data_fetcher import fetch_data
from utils.notifier import send_telegram
from utils.backtester import backtest
from utils.google_sheets import connect_to_sheets, log_trade
from config import API_STOCKS
from datetime import datetime
import schedule
import time
import os
import base64

# 🔓 Decode and write credentials.json from ENCODED_GOOGLE_CREDS
if os.getenv("ENCODED_GOOGLE_CREDS"):
    with open("credentials.json", "wb") as f:
        f.write(base64.b64decode(os.getenv("ENCODED_GOOGLE_CREDS")))


def run_trading_job():
    sheet = connect_to_sheets()
    for stock in API_STOCKS:
        df = fetch_data(stock)
        total_return, win_ratio, result_df = backtest(df)
        log_trade(sheet, [stock, f"{total_return:.2%}", f"{win_ratio:.2%}"])
        print(f"Logged: {stock}, Return: {total_return:.2%}, Win Ratio: {win_ratio:.2%}")
        message = f"""
        📈 Algo-Trading Signal ({datetime.now().strftime('%d %B %Y')})

        🔹 Stock: {stock}
        🔸 Strategy: RSI < 40 + 20DMA > 50DMA
        🔹 Backtest Return: {total_return:.2%}
        🔹 Win Ratio: {win_ratio:.2%}

        Note: Return is the cumulative strategy gain over 12 months.
        Win Ratio = % of trades that were profitable.
        """
        send_telegram(message)



run_trading_job()