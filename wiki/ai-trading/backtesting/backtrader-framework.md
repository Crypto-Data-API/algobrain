---
title: "Backtrader"
type: entity
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [ai-trading, backtesting, python, open-source]
entity_type: company
website: "https://www.backtrader.com"
aliases: ["Backtrader", "backtrader"]
related:
  - "[[zipline-framework]]"
  - "[[quantconnect]]"
  - "[[vectorbt]]"
  - "[[backtesting-pitfalls]]"
  - "[[freqtrade]]"
---

# Backtrader

**Backtrader** is a popular open-source Python backtesting framework. Its event-driven architecture supports multiple data feeds, broker simulations, and strategies simultaneously, making it one of the most flexible tools for testing trading ideas before going live.

---

## Overview

Created by Daniel Rodriguez, Backtrader uses a **Cerebro** engine that orchestrates data loading, strategy execution, broker simulation, and analytics. It supports any asset with OHLCV data and bridges to live trading via Interactive Brokers and OANDA. It sits between [[vectorbt]] (faster but less realistic) and [[quantconnect|QuantConnect]] (more data but cloud-locked) -- the go-to choice for Python traders who want event-driven accuracy with local control.

---

## Key Features

| Feature | Detail |
|---|---|
| **Engine** | Event-driven, bar-by-bar; Cerebro orchestrates everything |
| **Indicators** | 100+ built-in (SMA, RSI, MACD, Bollinger, etc.) |
| **Analyzers** | Sharpe, drawdown, trade list, annual returns, custom |
| **Broker Sim** | Commissions, [[slippage]], margin, position sizing |
| **Live Trading** | Interactive Brokers and OANDA bridges |
| **Optimization** | Parameter sweeps with multiprocessing |

---

## How to Use

1. **Install**: `pip install backtrader`
2. **Prepare data**: CSV with OHLCV or built-in Yahoo Finance feed
3. **Write strategy**: Subclass `bt.Strategy`, define `__init__()` and `next()`
4. **Configure**: Add data, strategy, broker settings to Cerebro
5. **Run and analyze**: `cerebro.run()` then `cerebro.plot()`

---

## Strengths and Weaknesses

**Strengths**: Mature, battle-tested. Event-driven design mimics real execution. Multiple data feeds and strategies per run. Broker simulation with commissions, [[slippage]], margin, partial fills. Large community. Free. Backtest-to-live with minimal code changes.

**Weaknesses**: Slower than [[vectorbt]] for parameter sweeps. Plotting can be finicky. Reduced maintenance activity recently. No built-in data sources. [[walk-forward-optimization]] requires manual implementation.

---

## Example

```python
import backtrader as bt
class SmaCross(bt.Strategy):
    params = dict(fast=10, slow=30)
    def __init__(self):
        sma_fast = bt.ind.SMA(period=self.p.fast)
        sma_slow = bt.ind.SMA(period=self.p.slow)
        self.crossover = bt.ind.CrossOver(sma_fast, sma_slow)
    def next(self):
        if self.crossover > 0: self.buy()
        elif self.crossover < 0: self.close()

cerebro = bt.Cerebro()
cerebro.adddata(bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=...))
cerebro.addstrategy(SmaCross)
cerebro.run()
```

---

## See Also

- [[zipline-framework]] -- Quantopian's event-driven backtester
- [[vectorbt]] -- Vectorized backtesting for speed
- [[quantconnect]] -- Cloud platform with built-in data
- [[backtesting-pitfalls]] -- Common backtesting mistakes
- [[walk-forward-optimization]] -- Proper parameter optimization
- [[optuna]] -- Bayesian optimization for strategy parameter tuning
- [[backtesting-py]] -- Lightweight vectorized alternative
- [[pybroker]] -- ML-first backtesting framework
