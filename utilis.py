# utils.py

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def download_data(tickers, start='2020-01-01', end='2024-01-01'):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

def plot_efficient_frontier(returns, vol_arr, sharpe_arr, opt_ret, opt_vol):
    plt.figure(figsize=(10,6))
    plt.scatter(vol_arr, returns, c=sharpe_arr, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.title('Efficient Frontier')
    plt.scatter(opt_vol, opt_ret, c='red', s=50, label='Optimal Portfolio')
    plt.legend()
    plt.savefig("efficient_frontier.png")
    plt.show()

