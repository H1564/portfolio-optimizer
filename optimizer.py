import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioOptimizer:
    def __init__(self, price_data: pd.DataFrame):
        self.price_data = price_data
        self.returns = price_data.pct_change().dropna()

    def simulate_random_portfolios(self, num_portfolios=5000):
        results = {"Returns": [], "Volatility": [], "Sharpe": [], "Weights": []}
        num_assets = self.returns.shape[1]

        for _ in range(num_portfolios):
            weights = np.random.random(num_assets)
            weights /= np.sum(weights)
            portfolio_return = np.sum(self.returns.mean() * weights) * 252
            portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.returns.cov() * 252, weights)))
            sharpe_ratio = portfolio_return / portfolio_volatility
            results["Returns"].append(portfolio_return)
            results["Volatility"].append(portfolio_volatility)
            results["Sharpe"].append(sharpe_ratio)
            results["Weights"].append(weights)
        return pd.DataFrame(results)

    def optimize_portfolio(self):
        num_assets = self.returns.shape[1]

        def neg_sharpe(weights):
            port_return = np.sum(self.returns.mean() * weights) * 252
            port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.returns.cov() * 252, weights)))
            return -port_return / port_volatility

        constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(num_assets))
        init_guess = np.ones(num_assets) / num_assets
        optimized = minimize(neg_sharpe, init_guess, method="SLSQP", bounds=bounds, constraints=constraints)
        return optimized
