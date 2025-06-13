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
    )
    plt.legend()
    plt.grid(True)
    plt.show()
