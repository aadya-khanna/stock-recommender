from concurrent.futures import ThreadPoolExecutor
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

print("Fetcher module loaded.")

tickers_list = ["AAPL", "MSFT", "TSLA"]

def get_stats():
    hist_dict = {} 
    for t in tickers_list:
        stock = yf.Ticker(t)
        stock_history = stock.history(period="1mo", interval="1d")
        hist_dict[t] = stock_history
    return hist_dict

data = get_stats()

print(type(data))



# metrics to track - avg return, volatility, momentum, P/E, dividend yielf 

# metrics_dict = {}



