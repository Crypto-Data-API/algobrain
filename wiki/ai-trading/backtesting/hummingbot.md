---
title: "Hummingbot (Backtesting & Optimization)"
type: concept
created: 2026-04-14
updated: 2026-06-12
status: good
tags: [algorithmic, crypto, market-making, backtesting]
aliases: ["Hummingbot backtesting", "Hummingbot Optuna"]
domain: [backtesting]
difficulty: advanced
related:
  - "[[optuna]]"
  - "[[market-making]]"
  - "[[arbitrage]]"
  - "[[crypto-markets]]"
  - "[[trading-system-deployment]]"
  - "[[custom-python-bots]]"
  - "[[backtesting-overview]]"
  - "[[freqtrade]]"
---

# Hummingbot — Backtesting & Optimization

This page covers Hummingbot from the **backtesting and parameter-optimization** angle. For the bot framework itself — installation, exchange support, governance, and live operation — see the canonical entity page [[hummingbot|Hummingbot]] in the trading-bots section.

**Hummingbot** is an open-source market-making and arbitrage framework with built-in [[optuna|Optuna]] optimization, 40+ exchange connectors, and historical order-book replay for backtesting. It is **not** a general-purpose backtesting framework — it is purpose-built for [[market-making]] and [[arbitrage]] strategies in crypto markets, and its backtest model is fundamentally different from the price-bar replay used by [[backtrader-framework|Backtrader]] or [[vectorbt|VectorBT]]. Governed by the Hummingbot Foundation. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Why Market-Making Backtesting Is Different

Most backtesting frameworks ([[backtrader-framework|Backtrader]], [[vectorbt|VectorBT]], [[pybroker|PyBroker]]) focus on directional strategies — buy/sell based on price signals, with fills assumed at OHLC prices. Hummingbot operates in a different domain: **liquidity provision and cross-venue arbitrage**, where the strategy continuously quotes bid and ask prices and profits from the spread.

The central challenge is **adverse selection**: a market maker's limit orders only fill when the market moves against the quoted price. The fills you get are biased toward losses, and the orders that would have been profitable often don't fill at all. A naive backtest that assumes all resting orders fill will dramatically overstate market-making profitability. Hummingbot addresses this with order-book replay.

---

## Backtesting via Order-Book Replay

Unlike price-bar backtesting, Hummingbot replays **historical order-book snapshots** to simulate how limit orders would have been filled:

- Bid/ask placement is evaluated against the historical book
- Fill probability depends on order placement relative to the prevailing book and subsequent price action
- More realistic than assuming fills at OHLC close prices
- Captures the adverse-selection bias inherent to market-making

This makes Hummingbot one of the few retail-accessible tools that backtests liquidity provision with any fidelity. It still has limits — replaying snapshots does not perfectly model queue position, latency, or the reflexive effect of your own quotes on the book — but it is far closer to reality than bar-based fill assumptions.

---

## Optuna Integration

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

The search ranges over spread widths, order sizes, refresh intervals, and inventory-skew parameters to maximize PnL (or risk-adjusted PnL) on historical book data. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]) The same [[overfitting-in-trading|overfitting]] cautions apply as with any optimized strategy: pair Optuna with out-of-sample testing and parameter-sensitivity analysis, because a market-making config tuned to one volatility regime can lose money in another.

---

## Strategy Controllers (Backtested Units)

Hummingbot organizes logic into **controllers** — the modular units you backtest and optimize:

- **Pure Market Making** — quote bid/ask around mid-price; profit when both sides fill. Key params: spread, order amount, refresh time, inventory skew.
- **Cross-Exchange Market Making** — quote on a lower-liquidity venue, immediately hedge on a higher-liquidity venue; capture the liquidity premium.
- **TWAP / VWAP Execution** — time- and volume-weighted slicing of large orders.
- **Arbitrage** — execute when the cross-venue spread exceeds fees + slippage + transfer time.

---

## Limitations for Backtesting

| Limitation | Detail |
|-----------|--------|
| **Crypto only** | No equity, forex, or futures support |
| **Market-making focused** | Not suitable for trend-following or mean-reversion backtests — use [[backtrader-framework|Backtrader]] / [[vectorbt|VectorBT]] |
| **Replay fidelity** | Snapshot replay does not model queue position, latency, or quote reflexivity |
| **Data availability** | High-quality historical order-book data is harder to source than OHLCV |
| **Inventory risk** | Backtests must account for accumulated directional exposure, not just spread capture |

---

## When to Use Hummingbot for Backtesting

**Good for:** crypto market-making parameter studies; cross-exchange arbitrage feasibility; liquidity provision on DEXes; optimizing controller parameters with [[optuna|Optuna]] against order-book replay.

**Not good for:** general directional strategy backtesting (use [[backtrader-framework|Backtrader]], [[vectorbt|VectorBT]], or [[pybroker|PyBroker]]); equity or forex; low-frequency position trading.

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- Hummingbot documentation: https://docs.hummingbot.org

## Related

- [[hummingbot|Hummingbot]] — canonical bot/entity page (install, exchanges, live operation)
- [[optuna]] — the optimizer Hummingbot uses for controller tuning
- [[market-making]], [[arbitrage]] — the strategy classes Hummingbot targets
- [[backtesting-overview]] — broader backtesting framework survey
- [[freqtrade]] — directional crypto bot alternative
