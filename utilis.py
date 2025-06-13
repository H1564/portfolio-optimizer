import pandas as pd
import yfinance as yf

def fetch_data(tickers, start='2022-01-01', end='2024-01-01'):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data.dropna()

def save_to_csv(data: pd.DataFrame, filename: str = "data/sample_assets.csv"):
    data.to_csv(filename)
