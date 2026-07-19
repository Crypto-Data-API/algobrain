---
title: "Hummingbot"
type: entity
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [ai-trading, trading-bots, market-making, crypto, open-source, backtesting]
entity_type: company
website: "https://hummingbot.io"
aliases: ["Hummingbot", "hummingbot", "Hummingbot backtesting", "Hummingbot Optuna"]
related:
  - "[[freqtrade]]"
  - "[[bot-architecture]]"
  - "[[custom-python-bots]]"
  - "[[liquidity]]"
  - "[[arbitrage]]"
  - "[[optuna]]"
  - "[[market-making]]"
  - "[[ai-backtesting-overview]]"
  - "[[trading-system-deployment]]"
---

# Hummingbot

**Hummingbot** is an open-source trading bot framework specializing in market making and arbitrage strategies. It supports both centralized exchanges (CEX) and decentralized exchanges (DEX), making it unique among retail-accessible bot frameworks.

---

## Overview

Founded in 2019 by CoinAlpha, Hummingbot democratizes [[liquidity]] provision and [[arbitrage]] -- strategies traditionally reserved for institutional market makers. Configurable strategy templates let users run sophisticated strategies without coding from scratch. The Gateway module enables DEX connectivity on Ethereum, Polygon, BNB Chain, and others. Free, open source, governed by the HBOT token.

---

## Key Features

| Feature | Detail |
|---|---|
| **Pure Market Making** | Place bid/ask orders around mid-price with configurable spread, order size, and levels |
| **Cross-Exchange Market Making** | Make markets on one exchange, hedge on another |
| **Arbitrage** | Exploit price differences between exchanges |
| **TWAP** | Time-weighted average price execution for large orders |
| **Avellaneda-Stoikov** | Academic market making model with inventory risk management |
| **DEX Support** | Gateway module connects to Uniswap, PancakeSwap, dYdX, and more |
| **Exchange Support** | Binance, Kraken, Gate.io, KuCoin, and 30+ other CEXs |

---

## How to Use

1. **Install**: Docker (recommended) or `conda` environment
2. **Configure**: `create` walks through API keys, pairs, strategy parameters
3. **Select strategy**: Pure market making, cross-exchange, arbitrage, or TWAP
4. **Paper trade**: Validate behavior before going live
5. **Start**: `start` command begins execution; monitor via terminal or Telegram

---

## Strengths and Weaknesses

**Strengths**: Best open-source tool for [[liquidity|market making]] strategies. CEX + DEX support is unique. No coding required for built-in strategies. Academic market making models (Avellaneda-Stoikov) built in. Active community and documentation. Free.

**Weaknesses**: Market making is inherently risky -- inventory risk, adverse selection, and wide spreads in volatile markets can cause losses. DEX gateway can be complex to set up. Not designed for momentum or trend-following strategies (use [[freqtrade]] instead). Performance depends heavily on parameter tuning and market conditions.

---

## Example

```
Strategy: pure_market_making    Exchange: binance
Trading pair: ETH-USDT          Bid/Ask spread: 0.3%
Order amount: 0.1 ETH           Order levels: 3
Order level spread: 0.2%        Inventory skew: enabled
Kill switch: -2%
```

Places three levels of buy/sell orders around mid-price, each 0.2% apart, with 0.3% minimum spread and automatic inventory balancing.

---

## Backtesting & Optimization

Hummingbot is **not** a general-purpose backtesting framework — it is purpose-built for [[market-making]] and [[arbitrage]] strategies in crypto markets, and its backtest model is fundamentally different from the price-bar replay used by [[backtrader-framework|Backtrader]] or [[vectorbt|VectorBT]].

### Why Market-Making Backtesting Is Different

Most backtesting frameworks focus on directional strategies — buy/sell based on price signals, with fills assumed at OHLC prices. Hummingbot operates in a different domain: **liquidity provision and cross-venue arbitrage**, where the strategy continuously quotes bid and ask prices and profits from the spread.

The central challenge is **adverse selection**: a market maker's limit orders only fill when the market moves against the quoted price. The fills you get are biased toward losses, and the orders that would have been profitable often don't fill at all. A naive backtest that assumes all resting orders fill will dramatically overstate market-making profitability. Hummingbot addresses this with order-book replay.

### Backtesting via Order-Book Replay

Unlike price-bar backtesting, Hummingbot replays **historical order-book snapshots** to simulate how limit orders would have been filled:

- Bid/ask placement is evaluated against the historical book
- Fill probability depends on order placement relative to the prevailing book and subsequent price action
- More realistic than assuming fills at OHLC close prices
- Captures the adverse-selection bias inherent to market-making

This makes Hummingbot one of the few retail-accessible tools that backtests liquidity provision with any fidelity. It still has limits — replaying snapshots does not perfectly model queue position, latency, or the reflexive effect of your own quotes on the book — but it is far closer to reality than bar-based fill assumptions.

### Optuna Integration

Hummingbot's [[optuna|Optuna]] integration optimizes controller parameters (spread width, order amount, refresh time, inventory skew) using the TPE sampler over historical exchange data:

```python
# Conceptual workflow (Hummingbot's internal optimization)
def objective(trial):
    spread        = trial.suggest_float("spread", 0.001, 0.02)
    order_amount  = trial.suggest_float("order_amount", 0.01, 1.0)
    refresh_time  = trial.suggest_int("refresh_time", 10, 120)
    inventory_skew = trial.suggest_float("inventory_skew", 0.0, 1.0)

    result = replay_backtest(
        controller="pure_market_making",
        pair="BTC-USDT", exchange="binance",
        spread=spread, order_amount=order_amount,
        refresh_time=refresh_time, inventory_skew=inventory_skew,
    )
    return result.pnl

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)
```

The same [[overfitting-in-trading|overfitting]] cautions apply as with any optimized strategy: pair Optuna with out-of-sample testing and parameter-sensitivity analysis.

### Strategy Controllers (Backtested Units)

| Controller | Description |
|-----------|-------------|
| **Pure Market Making** | Quote bid/ask around mid-price; profit when both sides fill. Key params: spread, order amount, refresh time, inventory skew. |
| **Cross-Exchange Market Making** | Quote on a lower-liquidity venue, immediately hedge on a higher-liquidity venue; capture the liquidity premium. |
| **TWAP / VWAP Execution** | Time- and volume-weighted slicing of large orders. |
| **Arbitrage** | Execute when the cross-venue spread exceeds fees + slippage + transfer time. |

### Backtesting Limitations

| Limitation | Detail |
|-----------|--------|
| **Crypto only** | No equity, forex, or futures support |
| **Market-making focused** | Not suitable for trend-following or mean-reversion backtests — use [[backtrader-framework\|Backtrader]] / [[vectorbt\|VectorBT]] |
| **Replay fidelity** | Snapshot replay does not model queue position, latency, or quote reflexivity |
| **Data availability** | High-quality historical order-book data is harder to source than OHLCV |
| **Inventory risk** | Backtests must account for accumulated directional exposure, not just spread capture |

**Good for:** crypto market-making parameter studies; cross-exchange arbitrage feasibility; optimizing controller parameters with [[optuna|Optuna]] against order-book replay.

**Not good for:** general directional strategy backtesting (use [[backtrader-framework|Backtrader]], [[vectorbt|VectorBT]], or [[pybroker|PyBroker]]); equity or forex; low-frequency position trading.

## See Also

- [[freqtrade]] -- Open-source crypto bot for momentum/trend strategies
- [[bot-architecture]] -- General trading bot design patterns
- [[arbitrage]] -- Exploiting price differences across venues
- [[liquidity]] -- What market makers provide to the market
- [[bot-risks-and-pitfalls]] -- Risks specific to automated trading
- [[optuna]] -- The optimizer Hummingbot uses for controller tuning
- [[ai-backtesting-overview]] -- Broader backtesting framework survey
