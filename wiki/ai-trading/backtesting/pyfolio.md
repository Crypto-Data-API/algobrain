---
title: "pyfolio"
type: concept
created: 2026-04-14
updated: 2026-06-12
status: good
tags: [backtesting, python, risk-management]
aliases: ["pyfolio", "Pyfolio"]
domain: [backtesting]
difficulty: beginner
related:
  - "[[zipline-framework]]"
  - "[[quantstats]]"
  - "[[sharpe-sortino-calmar]]"
  - "[[drawdown]]"
  - "[[vectorbt]]"
  - "[[ai-backtesting-overview]]"
---

# pyfolio

**pyfolio** is an open-source portfolio analytics library for Python, originally developed by Quantopian as the analytics companion to [[zipline-framework|Zipline]]. It generates comprehensive "tear sheets" from a returns series — performance summaries, drawdown analysis, rolling statistics, factor exposure, and round-trip trade analysis. Install with `pip install pyfolio-reloaded` (community-maintained fork). (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Overview

pyfolio takes a pandas Series of daily returns and produces a full statistical profile of a strategy's performance. It was designed to answer the question: "beyond the equity curve, what does this strategy's risk profile actually look like?" The library standardized the concept of "tear sheets" in the quant trading community — multi-page reports covering returns, risk, factor exposure, and trade-level analysis.

---

## Tear Sheet Components

### Performance Summary
- Total return, annual return, CAGR
- [[sharpe-sortino-calmar|Sharpe ratio, Sortino ratio, Calmar ratio]]
- Max [[drawdown]], longest drawdown duration
- Stability of returns (R-squared of cumulative log returns)
- Tail ratio, common sense ratio

### Drawdown Analysis
- Top 5 drawdowns with start date, trough date, recovery date, duration
- Underwater plot (time spent below previous high-water mark)

### Rolling Statistics
- 6-month and 12-month rolling Sharpe ratio
- Rolling beta to benchmark
- Rolling volatility

### Factor Exposure (Fama-French)
- Market beta, SMB (size), HML (value), UMD (momentum)
- Requires Fama-French factor data (included or downloadable)

### Round-Trip Analysis
- Per-trade statistics: duration, return, PnL
- Win rate, average win vs average loss
- Profit factor

---

## Basic Usage

```python
import pyfolio as pf

# From a returns series
pf.create_full_tear_sheet(returns, benchmark_rets=spy_returns)

# Individual components
pf.create_returns_tear_sheet(returns)
pf.create_position_tear_sheet(returns, positions)
pf.create_round_trip_tear_sheet(returns, positions, transactions)
```

pyfolio works with any pandas Series of daily returns — it is framework-agnostic despite being designed alongside Zipline.

---

## Key Metrics Calculated

| Metric | What It Measures |
|--------|-----------------|
| Sharpe Ratio | Risk-adjusted return (annualized) |
| Sortino Ratio | Downside-risk-adjusted return |
| Calmar Ratio | Annual return / max drawdown |
| Max Drawdown | Largest peak-to-trough decline |
| Stability | R-squared of cumulative log returns (higher = smoother equity curve) |
| Tail Ratio | 95th percentile return / abs(5th percentile) — measures tail asymmetry |
| Common Sense Ratio | Tail ratio × profit factor |
| Annual Volatility | Annualized standard deviation of returns |
| Omega Ratio | Probability-weighted gains vs losses at threshold return |

---

## Integration with Zipline

pyfolio was designed as [[zipline-framework|Zipline]]'s native analytics layer:

```python
# After running a Zipline backtest
perf = zipline.run_algorithm(...)
returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(perf)
pf.create_full_tear_sheet(returns, positions=positions, transactions=transactions)
```

This extracts the full position and transaction history for round-trip analysis and factor exposure decomposition.

---

## Current Status and Maintenance

Quantopian shut down in October 2020. The original `pyfolio` package is no longer actively maintained. The community fork **`pyfolio-reloaded`** (`pip install pyfolio-reloaded`) is the recommended installation, maintained by the same community that maintains `zipline-reloaded`.

**Known issues:**
- Some dependencies (particularly empyrical, the risk metrics library) have compatibility issues with newer pandas versions
- Fama-French data download can be flaky
- Primarily designed for equities — limited built-in support for crypto, futures, or options analytics
- Plotting uses matplotlib (static images, not interactive)

---

## pyfolio vs QuantStats

| Feature | pyfolio | [[quantstats|QuantStats]] |
|---------|---------|-----------|
| **Maintenance** | Community fork (less active) | Actively maintained |
| **Output** | Matplotlib (static) | HTML + interactive charts |
| **Benchmark comparison** | Yes | Yes (easier API) |
| **Monthly heatmap** | No | Yes |
| **Factor exposure** | Fama-French built-in | No |
| **Round-trip analysis** | Yes (with positions data) | No |
| **VectorBT integration** | Manual | Native |
| **Crypto/Futures** | Limited | Better support |

**Recommendation:** Use [[quantstats|QuantStats]] for most new projects — it is more actively maintained, produces better visual output, and integrates natively with [[vectorbt]]. Use pyfolio when you need Fama-French factor decomposition or round-trip trade analysis, or when working with [[zipline-framework|Zipline]] pipelines. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- pyfolio-reloaded: https://github.com/stefan-jansen/pyfolio-reloaded
