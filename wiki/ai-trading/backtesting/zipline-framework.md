---
title: "Zipline"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, backtesting, python, open-source]
entity_type: company
aliases: ["Zipline", "zipline", "zipline-reloaded", "Zipline framework"]
related:
  - "[[backtrader-framework]]"
  - "[[quantconnect]]"
  - "[[vectorbt]]"
  - "[[backtesting-pitfalls]]"
  - "[[walk-forward-optimization]]"
---

# Zipline

**Zipline** is the open-source backtesting engine originally built by Quantopian for equity strategy research. It powers an event-driven simulation with integrated tools for alpha factor analysis (Alphalens), performance analysis (Pyfolio), and risk metrics (Empyrical). After Quantopian shut down in 2020, the community fork **zipline-reloaded** keeps the project alive.

---

## Overview

Zipline was the backbone of Quantopian's platform (200,000+ users at peak). Its architecture is oriented toward US equity markets with a Pipeline API for cross-sectional factor screening across thousands of stocks. While [[backtrader-framework|Backtrader]] excels at single-instrument strategies, Zipline's strength is **multi-asset factor investing** -- ranking stocks by alpha factors and constructing long/short portfolios.

---

## Key Features

| Feature | Detail |
|---|---|
| **Engine** | Event-driven, bar-by-bar with realistic fills |
| **Pipeline API** | Cross-sectional factor screening across stock universes |
| **Alphalens** | Factor analysis: IC, factor returns, turnover |
| **Pyfolio** | Portfolio analytics: returns, drawdowns, exposure |
| **Empyrical** | Risk metrics: Sharpe, Sortino, max drawdown, Calmar |
| **Data Bundles** | Optimized format for fast historical replay |

---

## How to Use

1. **Install**: `pip install zipline-reloaded` (community fork)
2. **Ingest data**: `zipline ingest -b quandl` or custom bundle
3. **Write algorithm**: Define `initialize()` and `handle_data()`
4. **Run**: `zipline run -f algo.py --start 2015-1-1 --end 2023-12-31`
5. **Analyze**: Load results into Pyfolio for tearsheets

---

## The Quantopian Ecosystem

All tools live on as community forks: **zipline-reloaded** (backtesting), **alphalens-reloaded** (factor analysis), **pyfolio-reloaded** (performance tearsheets), and **Empyrical** (risk metrics). Quantopian's cloud platform shut down October 2020.

---

## Strengths and Weaknesses

**Strengths**: Best-in-class for US equity factor research. Pipeline API spans thousands of stocks. Alphalens/Pyfolio/Empyrical provide institutional-grade analytics. Well-tested engine with realistic fills.

**Weaknesses**: US equities only (limited crypto/forex). Data ingestion complex; original Quantopian bundles gone. Slower than [[vectorbt]]. No live trading bridge. Dependency conflicts during install. [[walk-forward-optimization]] not built in.

---

## Example

```python
from zipline.api import order_target_percent, symbol

def initialize(context):
    context.asset = symbol('AAPL')

def handle_data(context, data):
    short_mavg = data.history(context.asset, 'price', 20, '1d').mean()
    long_mavg = data.history(context.asset, 'price', 50, '1d').mean()
    if short_mavg > long_mavg:
        order_target_percent(context.asset, 1.0)
    else:
        order_target_percent(context.asset, 0.0)
```

---

## See Also

- [[backtrader-framework]] -- More flexible multi-asset backtester
- [[quantconnect]] -- Cloud platform with LEAN engine and built-in data
- [[vectorbt]] -- Fast vectorized alternative for rapid prototyping
- [[backtesting-pitfalls]] -- Common mistakes Zipline helps you avoid
- [[walk-forward-optimization]] -- Proper methodology for parameter optimization
