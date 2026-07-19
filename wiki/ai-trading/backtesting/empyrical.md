---
title: "empyrical"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [backtesting, python, risk-management, quantitative]
aliases: ["empyrical", "Empyrical", "empyrical-reloaded"]
domain: [backtesting, risk-management]
difficulty: beginner
related:
  - "[[pyfolio]]"
  - "[[zipline-framework]]"
  - "[[quantstats]]"
  - "[[sharpe-sortino-calmar]]"
  - "[[drawdown]]"
  - "[[ai-backtesting-overview]]"
  - "[[options-concentration-risk]]"
---

**empyrical** is the open-source Python library that computes the standard suite of risk and performance metrics — Sharpe ratio, Sortino ratio, max drawdown, Calmar ratio, alpha, beta, value-at-risk, conditional VaR, and dozens of others — from a returns series. Originally developed by Quantopian as the math layer beneath [[pyfolio]] and Zipline, it is the de facto reference implementation for these metrics in the Python quant ecosystem. If a backtest framework reports a Sharpe ratio in Python, there is a high probability it is computed by `empyrical` (or a near-identical fork).

## Role in the Quant Stack

The Quantopian-era stack had three layers:

1. **[[zipline-framework|Zipline]]** — event-driven backtesting engine (data + strategy + execution simulation)
2. **[[pyfolio]]** — tear-sheet and visualization layer (charts, tables, attribution)
3. **empyrical** — the underlying math layer that pyfolio and Zipline both call to compute risk metrics

`empyrical` is intentionally framework-agnostic. Any Python project — a Zipline backtest, a vectorbt backtest, a Jupyter notebook with hand-coded returns, or a live-trading P&L stream — can call `empyrical` functions on a pandas Series of returns and get standardized metric output.

## Install

```python
# Quantopian original (less actively maintained)
pip install empyrical

# Community fork (recommended for new projects)
pip install empyrical-reloaded
```

The community fork is the recommended install; it tracks pandas / NumPy compatibility better than the original Quantopian release.

## Core Functions

`empyrical.stats` exposes the metric functions. Typical usage:

```python
import empyrical as ep
import pandas as pd

returns = pd.Series([...])  # daily strategy returns
benchmark = pd.Series([...])  # daily benchmark returns

ep.sharpe_ratio(returns)             # annualized Sharpe
ep.sortino_ratio(returns)            # annualized Sortino (downside dev)
ep.calmar_ratio(returns)             # annual return / max drawdown
ep.omega_ratio(returns, threshold=0) # Omega above threshold
ep.max_drawdown(returns)             # worst peak-to-trough
ep.annual_volatility(returns)        # annualized stdev
ep.cagr(returns)                     # compound annual growth rate
ep.alpha(returns, benchmark)         # CAPM alpha vs benchmark
ep.beta(returns, benchmark)          # CAPM beta vs benchmark
ep.value_at_risk(returns, cutoff=0.05)  # 5% VaR
ep.conditional_value_at_risk(returns, cutoff=0.05)  # CVaR / expected shortfall
ep.tail_ratio(returns)               # 95th percentile / |5th percentile|
ep.stability_of_timeseries(returns)  # R-squared of cumulative log returns
ep.downside_risk(returns)            # downside semi-deviation
ep.excess_sharpe(returns, factor)    # information ratio
```

## Metrics Reference

| Metric | Function | What It Measures |
|--------|----------|------------------|
| Sharpe | `sharpe_ratio` | Risk-adjusted return (mean / stdev, annualized) |
| Sortino | `sortino_ratio` | Risk-adjusted using downside deviation only |
| Calmar | `calmar_ratio` | Annual return / max drawdown |
| Omega | `omega_ratio` | Probability-weighted gains/losses ratio |
| Max DD | `max_drawdown` | Worst peak-to-trough decline |
| Annual Vol | `annual_volatility` | sqrt(252) * daily stdev |
| CAGR | `cagr` | Compound annual growth rate |
| Alpha | `alpha` | Mean of (returns - beta × benchmark) annualized |
| Beta | `beta` | Covariance(returns, benchmark) / Var(benchmark) |
| VaR | `value_at_risk` | Loss threshold at given confidence |
| CVaR | `conditional_value_at_risk` | Expected loss conditional on VaR breach |
| Tail Ratio | `tail_ratio` | Right-tail vs left-tail asymmetry |
| Stability | `stability_of_timeseries` | R² of log cumulative returns (smoothness) |

All functions accept a `period` argument (`'daily'`, `'weekly'`, `'monthly'`) for proper annualization, and most accept an optional `risk_free` rate.

## Conventions and Common Arguments

The reason to standardize on `empyrical` is precisely that the *conventions* are pinned down. The shared keyword arguments are where most "why does my Sharpe differ?" disputes get resolved:

| Argument | Meaning | Default behavior |
|----------|---------|------------------|
| `period` | Return frequency for annualization (`'daily'`, `'weekly'`, `'monthly'`) | `'daily'` → ×√252 for vol, ×252 for return |
| `annualization` | Override the periods-per-year factor directly | Inferred from `period` (e.g. 252) |
| `risk_free` | Per-period risk-free rate subtracted before ratio | `0` |
| `required_return` | Threshold for Sortino/Omega downside | `0` |
| `cutoff` | Tail probability for VaR / CVaR | `0.05` |

Two strategies' Sharpe ratios are only comparable if they share `period`, `annualization`, and `risk_free`. `empyrical` makes those explicit and identical across every caller, which is its core value — see [[sharpe-ratio]] for how easily the number is mis-stated otherwise.

## Aggregate and Rolling Helpers

Beyond the scalar metrics, `empyrical` exposes helpers that backtest frameworks lean on:

| Helper | Purpose |
|--------|---------|
| `cum_returns` / `cum_returns_final` | Cumulative (compounded) return path and its final value |
| `aggregate_returns` | Resample returns to weekly/monthly/yearly buckets |
| `roll_*` (e.g. `roll_sharpe_ratio`, `roll_max_drawdown`) | Rolling-window versions of the scalar metrics |
| `simple_returns` | Convert a price series to a returns series |

The `roll_*` family is what underpins rolling-Sharpe and rolling-beta charts in [[pyfolio]] tear sheets and is directly useful for detecting regime change in a live book (see the options-concentration discussion below).

## Why It Matters

`empyrical` solves a small but real problem: Sharpe ratio computation has many subtle gotchas (annualization factor, geometric vs arithmetic, treatment of zero-variance edge cases, NaN handling). Different libraries computing "Sharpe ratio" can produce meaningfully different numbers. Using `empyrical` everywhere ensures consistency and matches the convention used in academic and industry research that built on Zipline / pyfolio.

For [[backtesting]] workflows specifically, `empyrical` becomes the metric backbone:

- A custom backtester computes a returns series → call `empyrical.sharpe_ratio` to get a comparable Sharpe number
- A Zipline backtest produces results → pyfolio calls empyrical under the hood
- A live-trading P&L stream is converted to returns → same `empyrical` functions work unchanged

## How Trading and AI Systems Use It

Because `empyrical` is pure math on a returns array, it is the metric layer of choice *inside* automated systems, where the heavier [[quantstats]] HTML reporting is too slow:

| Context | Role of empyrical |
|---------|-------------------|
| Optimization inner loop | Compute a scalar objective (e.g. `sharpe_ratio` or `calmar_ratio`) per parameter set — fast enough to call thousands of times |
| ML / RL reward shaping | Use risk-adjusted metrics (Sharpe, Sortino, max drawdown) as a reward or selection criterion instead of raw return |
| Walk-forward validation | Compute the same metric on each out-of-sample fold for honest comparison |
| Live monitoring | Convert running P&L to returns and track `roll_sharpe_ratio` / `max_drawdown` for [[when-to-retire-a-strategy|kill-criteria]] |
| Framework backends | [[pyfolio]] and [[zipline-framework|Zipline]] call it under the hood so reported numbers match research |

The division of labour with [[quantstats]] is clean: use `empyrical` for the scalar metric in tight loops and automated decisions, and use `quantstats` (or [[pyfolio]]) once at the end for the human-readable tear sheet. Both ultimately compute the same family of metrics, so the numbers reconcile.

## Relationship to Options Concentration Risk

For options books, [[options-concentration-risk]] notes that a custom Python risk system at scale typically uses `pyfolio` / `empyrical` / Barra factor data for full decomposition. `empyrical` specifically handles:

- **Drawdown analysis**: max drawdown, drawdown duration, underwater periods — directly relevant for understanding what concentrated books actually do in stress
- **Tail risk metrics**: VaR, CVaR, tail ratio — standard inputs for assessing whether a short-vol book has the tail-risk profile the trader thinks it has
- **Rolling windows**: rolling Sharpe, rolling beta — useful for detecting regime changes that often coincide with concentration revealing itself
- **Attribution**: when paired with pyfolio's tear sheets, empyrical-computed metrics let a trader see how the concentrated book performs vs benchmark across regimes

It does *not* compute factor exposures (that's barra / axioma / northfield or a custom factor model on top), and it does *not* understand options Greeks at the position level. It works on returns series — what positions do, not why.

## Caveats

- **Returns-only, no positions.** It cannot do round-trip/per-trade attribution or position-level Greeks — pair with [[pyfolio]] for trade-level analysis and a factor model for exposures.
- **Annualization must match the data.** Passing daily metrics on weekly returns (or forgetting `period`) silently produces wrong numbers — see the conventions table above.
- **NaN / edge-case handling.** Some functions return `NaN` quietly on zero-variance or empty inputs (one of the issues `empyrical-reloaded` improves); validate inputs in automated pipelines.
- **Metrics inherit the returns' biases.** Look-ahead, survivorship, or cost-free returns produce flattering but meaningless metrics (see [[backtesting-pitfalls]]).
- **Math layer only.** No visualization — use [[quantstats]] or [[pyfolio]] for charts and reports.

## Current Status and Maintenance

Quantopian shut down in October 2020. The original `empyrical` package on PyPI is no longer actively maintained.

The community fork **`empyrical-reloaded`** (`pip install empyrical-reloaded`) is the recommended install for new projects. It is maintained by Stefan Jansen (author of *Machine Learning for Algorithmic Trading*) alongside `pyfolio-reloaded` and `zipline-reloaded`.

Known issues with the original Quantopian `empyrical`:
- Compatibility with newer pandas versions (2.x) is fragile in places
- Some functions silently return NaN on edge cases without warnings
- Documentation has gaps in places where Quantopian had relied on internal usage knowledge

`empyrical-reloaded` addresses many of these.

## empyrical vs Alternatives

| Library | Strength | Weakness |
|---------|----------|----------|
| **empyrical / empyrical-reloaded** | Standard metric set, framework-agnostic, paired with pyfolio | Math-only; no visualization |
| [[quantstats]] | Built-in HTML reporting, more visualization | Larger surface, less of a focused math library |
| `pyportfolioopt` | Portfolio optimization, not just metrics | Different scope |
| `riskfolio-lib` | Advanced portfolio risk + optimization | Heavier dependency |
| Custom NumPy | Maximum control | Reimplements known-correct math |

For most backtesting workflows: use `empyrical-reloaded` as the metric layer, `pyfolio-reloaded` or `quantstats` as the visualization layer, and any backtest framework underneath.

## Sources

- empyrical-reloaded: https://github.com/stefan-jansen/empyrical-reloaded
- Original Quantopian empyrical (archived): https://github.com/quantopian/empyrical
- Referenced in [[options-concentration-risk]] as part of a custom Python risk-system stack
- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

## Related

- [[pyfolio]] — sister library; pyfolio uses empyrical for all metric computations
- [[zipline-framework]] — Zipline reports use empyrical-computed metrics
- [[quantstats]] — alternative library combining metrics and visualization
- [[sharpe-sortino-calmar]] — the headline metrics empyrical implements
- [[sharpe-ratio]] — why a single number needs pinned conventions
- [[drawdown]] — empyrical's max-drawdown function is a reference implementation
- [[vectorbt]] — backtest engine that can feed empyrical a returns series
- [[ai-backtesting-overview]] — broader backtesting framework comparison
- [[backtesting-pitfalls]] — biased returns make clean metrics meaningless
- [[when-to-retire-a-strategy]] — rolling-metric kill criteria built on empyrical
- [[options-concentration-risk]] — empyrical is part of a custom Python risk-system build
- [[risk-management]] — broader risk-management context
