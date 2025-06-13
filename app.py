from optimizer import PortfolioOptimizer
from utils import fetch_data, save_to_csv
import matplotlib.pyplot as plt

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

if __name__ == "__main__":
    df = fetch_data(TICKERS)
    save_to_csv(df)

    optimizer = PortfolioOptimizer(df)
    sim = optimizer.simulate_random_portfolios()

    optimal = optimizer.optimize_portfolio()
    print("Optimal Weights:", optimal.x)
    print("Maximum Sharpe Ratio:", -optimal.fun)

    # Plot Efficient Frontier
    plt.figure(figsize=(10, 6))
    plt.scatter(sim["Volatility"], sim["Returns"], c=sim["Sharpe"], cmap='viridis', alpha=0.7)
    plt.xlabel("Volatility")
    plt.ylabel("Expected Return")
    plt.title("Portfolio Optimization - Efficient Frontier")
    plt.colorbar(label="Sharpe Ratio")
    plt.scatter(
        np.sqrt(np.dot(optimal.x.T, np.dot(optimizer.returns.cov() * 252, optimal.x))),
        np.sum(optimizer.returns.mean() * optimal.x) * 252,
        color="red",
        marker="*",
        s=200,
        label="Optimal Portfolio"
        from optimizer import simulate_portfolios, optimize_portfolio
from utils import download_data, plot_efficient_frontier

# Set your tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Download stock data
data = download_data(tickers)

# Run simulations
returns, volatilities, sharpe_ratios, weights_record = simulate_portfolios(data, num_portfolios=5000)

# Optimize
opt_weights, opt_ret, opt_vol = optimize_portfolio(data)

# Plot
plot_efficient_frontier(returns, volatilities, sharpe_ratios, opt_ret, opt_vol)    
    plt.legend()
    plt.grid(True)
    plt.Show()
