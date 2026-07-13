---
title: "QuantStats"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [backtesting, python, risk-management]
aliases: ["QuantStats", "quantstats"]
domain: [backtesting]
difficulty: beginner
related:
  - "[[vectorbt]]"
  - "[[pyfolio]]"
  - "[[sharpe-sortino-calmar]]"
  - "[[drawdown]]"
  - "[[backtesting-overview]]"
---

# QuantStats

**QuantStats** is an open-source portfolio analytics library for Python that generates HTML reports with interactive charts, monthly return heatmaps, drawdown analysis, and comprehensive risk metrics. It is the modern, more actively maintained alternative to [[pyfolio]], and integrates natively with [[vectorbt]]. Install with `pip install quantstats`. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Overview

QuantStats takes a pandas Series of daily returns and produces publication-quality analytics — either as an interactive HTML report, individual metrics, or inline plots. It is designed to be the fastest path from "I have a returns series" to "I understand this strategy's risk/return profile."

---

## Module Layout

QuantStats is organized into three submodules plus a convenience extension. Knowing which submodule a call lives in is the fastest way to navigate the library:

| Submodule | Purpose | Representative calls |
|-----------|---------|----------------------|
| `quantstats.stats` | Scalar metrics from a returns series | `sharpe`, `sortino`, `max_drawdown`, `cagr`, `volatility` |
| `quantstats.plots` | Individual matplotlib charts | `monthly_heatmap`, `drawdown`, `rolling_sharpe`, `snapshot` |
| `quantstats.reports` | Composed multi-section tear sheets | `html`, `full`, `basic`, `metrics` |
| `quantstats.extend_pandas()` | Monkey-patches the methods onto pandas Series | `returns.sharpe()`, `returns.max_drawdown()` |

After `qs.extend_pandas()`, every `stats` function is also callable as a method on a returns Series — e.g. `returns.sharpe()` — which is convenient in notebooks. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Core API

### Full HTML Report

```python
import quantstats as qs

# Generate a complete HTML tear sheet
qs.reports.html(returns, benchmark="SPY", output="report.html")
```

This single line produces a multi-section HTML report with:
- Performance summary table (20+ metrics)
- Cumulative returns vs benchmark
- Drawdown chart with underwater periods
- Monthly returns heatmap
- Distribution of daily returns
- Rolling Sharpe ratio
- Worst drawdown periods table

The `reports` submodule offers tiers of increasing detail, all driven by the same returns Series:

| Call | Output | Use |
|------|--------|-----|
| `qs.reports.metrics(returns)` | Metrics table only (text/DataFrame) | Quick numeric summary, scripting |
| `qs.reports.basic(returns)` | Key metrics + a few core plots | Lightweight review |
| `qs.reports.full(returns)` | Full set of metrics + all plots (inline) | Notebook deep-dive |
| `qs.reports.html(returns, output=...)` | Standalone interactive HTML file | Shareable tear sheet |

### Individual Metrics

```python
qs.stats.sharpe(returns)
qs.stats.sortino(returns)
qs.stats.max_drawdown(returns)
qs.stats.calmar(returns)
qs.stats.win_rate(returns)
qs.stats.profit_factor(returns)
qs.stats.payoff_ratio(returns)
qs.stats.cagr(returns)
qs.stats.volatility(returns)
```

### Comparative Analysis

```python
# Compare strategy against a benchmark
qs.reports.html(returns, benchmark="SPY", output="strategy_vs_spy.html")

# Compare against Bitcoin
qs.reports.html(returns, benchmark="BTC-USD", output="strategy_vs_btc.html")
```

QuantStats automatically downloads benchmark data from Yahoo Finance for comparison.

---

## Key Metrics

| Metric | What It Measures |
|--------|-----------------|
| **Sharpe Ratio** | Risk-adjusted return (excess return / volatility) |
| **Sortino Ratio** | Downside-risk-adjusted return |
| **Calmar Ratio** | CAGR / max drawdown |
| **Max Drawdown** | Largest peak-to-trough decline |
| **Profit Factor** | Gross profit / gross loss |
| **Win Rate** | Percentage of positive-return periods |
| **Payoff Ratio** | Average win / average loss |
| **Longest Drawdown** | Maximum number of days underwater |
| **Recovery Factor** | Net profit / max drawdown |
| **CAGR** | Compound annual growth rate |
| **Volatility** | Annualized standard deviation |

---

## Monthly Returns Heatmap

One of QuantStats' signature outputs — a color-coded grid showing returns for each month/year combination:

```python
qs.plots.monthly_heatmap(returns)
```

This immediately reveals seasonality patterns and helps identify whether returns are consistent or driven by a few exceptional months.

---

## VectorBT Integration

[[vectorbt|VectorBT]] uses QuantStats under the hood for its `.stats()` method:

```python
import vectorbt as vbt

# VectorBT portfolio stats use QuantStats
pf = vbt.Portfolio.from_signals(close, entries, exits)
pf.stats()  # QuantStats metrics

# Or generate a full QuantStats report from VectorBT results
qs.reports.html(pf.returns(), benchmark="SPY", output="vbt_report.html")
```

This makes QuantStats the natural analytics layer for the [[vectorbt]] + [[optuna]] optimization workflow: VectorBT runs the backtest, Optuna optimizes parameters, and QuantStats generates the final performance report. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## How Trading and AI Systems Use It

QuantStats sits at the *reporting* end of a pipeline. Because every function operates on a plain returns Series, it slots in regardless of how the returns were produced:

| Context | Role of QuantStats |
|---------|--------------------|
| Manual research | Generate an HTML tear sheet per candidate strategy and eyeball risk/return |
| Parameter optimization | After [[optuna]] picks parameters, produce the final report on the winning config |
| ML / RL strategy eval | Convert a model's simulated equity curve to returns, then report standardized metrics for apples-to-apples comparison |
| Live monitoring | Feed a live P&L-derived returns Series in periodically to track realized [[sharpe-ratio]], [[drawdown]], and rolling stats |
| Walk-forward / OOS | Run separate reports on in-sample vs out-of-sample slices to spot overfitting |

Two practical cautions when automating it:

- **Use it for reporting, not decision-making in tight loops.** The HTML report renders charts and downloads benchmark data; it is too heavy to call inside an optimization inner loop. Use `qs.stats.*` scalars (or [[empyrical]]) for the loop and `qs.reports.html` once at the end.
- **A single returns Series is the contract.** Anything that can emit daily (or resampled) returns — a [[vectorbt]] portfolio, a custom event-driven backtest, a [[zipline-framework|Zipline]] run, or a live ledger — can be reported identically. This is what makes it a good standard layer across an AI-trading stack.

---

## Relationship to empyrical and pyfolio

QuantStats overlaps heavily with [[empyrical]] (the metric-math layer behind [[pyfolio]]) in *what* it computes — Sharpe, Sortino, Calmar, drawdown, VaR-style stats — but differs in *packaging*: QuantStats bundles the math with built-in visualization and one-call HTML reporting, whereas empyrical is a focused math library and pyfolio is the older Quantopian-era visualization layer. For a returns-only workflow that wants a shareable report fast, QuantStats is usually the single dependency; when you need the *exact* Quantopian/academic metric conventions or factor decomposition, reach for [[empyrical]] / [[pyfolio]]. (See the comparison tables below and on [[empyrical]].)

---

## QuantStats vs pyfolio

| Feature | QuantStats | [[pyfolio]] |
|---------|-----------|---------|
| **Active maintenance** | Yes | Community fork (less active) |
| **Output format** | Interactive HTML | Static matplotlib |
| **Monthly heatmap** | Yes | No |
| **Benchmark comparison** | Simple (pass ticker string) | Manual (provide returns series) |
| **Factor exposure** | No | Fama-French built-in |
| **Round-trip analysis** | No | Yes |
| **VectorBT integration** | Native | Manual |
| **Crypto support** | Good | Limited |

QuantStats is the recommended default for new projects. Use [[pyfolio]] when you specifically need Fama-French factor decomposition or round-trip trade-level analysis. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Limitations and Caveats

- **No round-trip (per-trade) analysis** — only works with a returns series, not individual trade records; use [[pyfolio]] for trade-level/round-trip stats.
- **No factor decomposition (Fama-French)** — use [[pyfolio]] for factor attribution.
- **Yahoo Finance dependency** for benchmark data (the `benchmark="SPY"` convenience) can be unreliable or rate-limited; pass your own benchmark returns Series for production use.
- **Frequency assumptions** — several metrics assume daily data and a 252-day year; intraday or weekly/monthly returns need the appropriate periods/annualization argument or the numbers will be wrong.
- **Garbage-in on the returns Series** — metrics are only as good as the input. If returns are gross of [[transaction-costs|costs]], contain look-ahead, or are survivorship-biased, the tear sheet will look great and mean nothing (see [[backtesting-pitfalls]]).
- **Reporting cost in loops** — `reports.html` is comparatively heavy (rendering + benchmark download); do not call it inside optimization inner loops.

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- QuantStats GitHub: https://github.com/ranaroussi/quantstats

## Related

- [[empyrical]] — focused metric-math library with the same core stats; use it in tight loops
- [[pyfolio]] — older tear-sheet library; needed for round-trip and Fama-French factor analysis
- [[vectorbt]] — backtest engine that uses QuantStats for its `.stats()` method
- [[optuna]] — parameter optimizer in the VectorBT + QuantStats workflow
- [[zipline-framework]] — alternative backtest engine whose returns can be reported here
- [[sharpe-ratio]] / [[sharpe-sortino-calmar]] — the headline risk-adjusted metrics in the report
- [[drawdown]] — underwater/drawdown analysis is a signature QuantStats output
- [[backtesting-overview]] — where QuantStats fits in the overall workflow
- [[backtesting-pitfalls]] — why a clean tear sheet does not guarantee a real edge
