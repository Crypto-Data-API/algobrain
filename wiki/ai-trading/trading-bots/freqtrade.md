---
title: "Freqtrade"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, crypto, open-source]
entity_type: company
website: "https://www.freqtrade.io"
related:
  - "[[custom-python-bots]]"
  - "[[bot-architecture]]"
  - "[[backtrader-framework]]"
  - "[[hummingbot]]"
  - "[[backtesting-pitfalls]]"
---

# Freqtrade

**Freqtrade** is the most popular open-source cryptocurrency trading bot framework. Written in Python, it provides a complete pipeline from [[backtesting-pitfalls|strategy backtesting]] to live trading across 30+ exchanges via the [[custom-python-bots|CCXT]] library. It is entirely free and community-driven.

---

## Overview

Freqtrade lets traders write strategies in Python, backtest them against historical data, optimize parameters using hyperopt (Bayesian optimization), and deploy to live or dry-run mode -- all from one codebase. Actively maintained since 2017 with hundreds of GitHub contributors, it targets crypto traders with Python skills who want full control without paying for [[three-commas|3Commas]] or [[pionex|Pionex]].

---

## Key Features

| Feature | Detail |
|---|---|
| **Strategy Development** | Python classes with `populate_indicators()`, `populate_entry_trend()`, `populate_exit_trend()` |
| **Backtesting + Hyperopt** | Built-in backtester; Bayesian optimization via Optuna |
| **Exchange Support** | 30+ exchanges via CCXT (Binance, Kraken, OKX, Bybit) |
| **Dry-Run Mode** | Paper trading against live data |
| **Deployment** | Docker-first; FreqUI web dashboard for monitoring |

---

## How to Use

1. **Install**: `pip install freqtrade` or Docker image
2. **Configure**: `freqtrade create-config` -- exchange, stake amount, pairs
3. **Write strategy**: Subclass `IStrategy`, define indicators and entry/exit signals
4. **Backtest**: `freqtrade backtesting --strategy MyStrategy`
5. **Optimize**: `freqtrade hyperopt --hyperopt-loss SharpeHyperOptLoss`
6. **Dry-run then live**: `freqtrade trade --strategy MyStrategy`

---

## Strengths and Weaknesses

**Strengths**: Free, open source, most mature crypto bot framework. Excellent docs and community. [[walk-forward-optimization|Hyperopt]] prevents naive overfitting. Docker deployment. Spot + futures.

**Weaknesses**: Python and crypto only. Requires solid Python skills. Hyperopt can still [[backtesting-pitfalls|overfit]]. No [[monte-carlo-backtesting|Monte Carlo]] analysis.

---

## Example

```python
class MyStrategy(IStrategy):
    minimal_roi = {"0": 0.04}
    stoploss = -0.02
    timeframe = '5m'

    def populate_indicators(self, dataframe, metadata):
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['ema_fast'] = ta.EMA(dataframe, timeperiod=8)
        dataframe['ema_slow'] = ta.EMA(dataframe, timeperiod=21)
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[(dataframe['ema_fast'] > dataframe['ema_slow']) &
                      (dataframe['rsi'] < 35), 'enter_long'] = 1
        return dataframe
```

---

## See Also

- [[hummingbot]] -- Open-source market making alternative
- [[custom-python-bots]] -- Building bots from scratch
- [[bot-architecture]] -- How trading bots are structured
- [[bot-risks-and-pitfalls]] -- What can go wrong with automated trading
