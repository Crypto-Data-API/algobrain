---
title: "vectorbt"
type: entity
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [ai-trading, backtesting, python, performance]
entity_type: company
related:
  - "[[backtrader-framework]]"
  - "[[zipline-framework]]"
  - "[[quantconnect]]"
  - "[[backtesting-pitfalls]]"
  - "[[monte-carlo-backtesting]]"
---

# vectorbt

**vectorbt** is a high-performance vectorized backtesting library for Python. By leveraging NumPy and Pandas array operations instead of event-driven loops, it achieves **100-1000x speedups** over frameworks like [[backtrader-framework|Backtrader]] or [[zipline-framework|Zipline]], making it the tool of choice for rapid strategy exploration and large-scale parameter optimization.

---

## Overview

Traditional event-driven backtesting processes bar-by-bar -- realistic but slow. vectorbt expresses strategy logic as vectorized array operations, testing thousands of parameter combinations in seconds. The tradeoff: simplified execution (fills at close with optional fixed slippage, no complex order types or partial fills). Use for exploration; validate with [[backtrader-framework|Backtrader]] or [[quantconnect|QuantConnect]] before going live.

---

## Key Features

| Feature | Detail |
|---|---|
| **Engine** | Vectorized NumPy/Pandas -- no Python loops; 100-1000x faster |
| **Parameter Sweeps** | Thousands of combinations in one call |
| **Indicators** | MA, RSI, MACD, Bollinger, ATR, custom via `IndicatorFactory` |
| **Portfolio Sim** | Full tracking with fees, slippage, sizing |
| **Visualization** | Interactive Plotly: equity curves, drawdowns, heatmaps |
| **Statistics** | Sharpe, Sortino, Calmar, max drawdown, win rate |

---

## How to Use

1. **Install**: `pip install vectorbt`
2. **Load data**: `vbt.YFData.download()` or bring your own DataFrame
3. **Define signals**: Boolean entry/exit arrays from vectorized indicators
4. **Simulate**: `vbt.Portfolio.from_signals(close, entries, exits)`
5. **Analyze**: `.stats()`, `.total_return()`, `.sharpe_ratio()`, `.plot()`

---

## Strengths and Weaknesses

**Strengths**: Unmatched speed -- 10,000 parameter combos in seconds. Excellent for prototyping and hypothesis filtering. Interactive Plotly heatmaps show profitable parameter regions. Great for [[monte-carlo-backtesting|Monte Carlo]] resampling. Combines well with ML workflows.

**Weaknesses**: No order book simulation, partial fills, or complex order types. Assumes fills at close (look-ahead risk). Not for HFT or market making. Memory-intensive for huge sweeps. No live trading. Must validate with event-driven framework before deploying.

---

## Example

```python
import vectorbt as vbt
price = vbt.YFData.download('BTC-USD', period='2y').get('Close')
rsi = vbt.RSI.run(price, window=14)
entries = rsi.rsi_crossed_below([20, 25, 30])  # 3 entry thresholds
exits = rsi.rsi_crossed_above([70, 75, 80])    # 3 exit thresholds
pf = vbt.Portfolio.from_signals(price, entries, exits, fees=0.001)  # 9 combos
pf.total_return().vbt.heatmap()  # Heatmap of returns by parameter
```

Tests 9 RSI threshold combinations in one vectorized pass -- milliseconds vs minutes in [[backtrader-framework|Backtrader]].

---

## When to Use vectorbt vs Event-Driven

| Use vectorbt When | Use Event-Driven When |
|---|---|
| Exploring strategy ideas rapidly | Validating a strategy for live deployment |
| Running parameter sweeps (1000+ combos) | Modeling complex execution logic |
| Initial hypothesis filtering | Simulating [[slippage]], partial fills, order types |
| [[monte-carlo-backtesting|Monte Carlo]] resampling | Multi-asset strategies with rebalancing logic |
| Portfolio-level analysis | Strategies with path-dependent state |

---

## See Also

- [[backtrader-framework]] -- Event-driven backtester for validation
- [[quantconnect]] -- Cloud platform for live deployment
- [[monte-carlo-backtesting]] -- Robustness testing vectorbt excels at
- [[backtesting-pitfalls]] -- Pitfalls that vectorbt's speed can amplify (testing too many hypotheses)
- [[walk-forward-optimization]] -- Proper optimization methodology
- [[optuna]] -- Bayesian optimization for parameter tuning (pairs well with vectorbt's speed)
- [[quantstats]] -- Portfolio analytics and tearsheet generation
- [[pybroker]] -- ML-first backtesting framework
- [[backtesting-py]] -- Lightweight alternative vectorized backtester
