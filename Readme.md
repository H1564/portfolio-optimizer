# 🧠 Portfolio Optimizer

A high-level Python-based Portfolio Optimizer using Modern Portfolio Theory and the Sharpe Ratio. It downloads live stock data, simulates thousands of portfolios, and finds the optimal weights using constrained optimization.

---

## 🚀 Features
- Pulls real-time financial data using `yfinance`
- Calculates portfolio returns, volatility, and Sharpe ratio
- Runs thousands of portfolio simulations
- Uses `SciPy` to compute the optimal portfolio
- Visualizes the Efficient Frontier with optimal point

---

## 🛠️ How It Works

### 1. Data Collection
Pulls historical stock prices for a list of tickers.

### 2. Simulation
Creates random portfolio weights and calculates return, volatility, and Sharpe ratio.

### 3. Optimization
Uses the SLSQP algorithm to find weights with maximum Sharpe ratio.

---

## 📈 Output Example

![Efficient Frontier](https://raw.githubusercontent.com/your-username/portfolio-optimizer/main/efficient_frontier_example.png)

---

## 🧩 Requirements
