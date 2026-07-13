---
title: "Event-Driven Backtesting"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [backtesting, python, algorithmic, quantitative]
aliases: ["Event-Driven Backtesting", "Event-Based Backtesting", "Bar-by-Bar Backtesting"]
domain: [backtesting]
difficulty: intermediate
prerequisites: ["[[backtesting-overview]]", "[[vectorized-backtesting]]"]
related:
  - "[[vectorized-backtesting]]"
  - "[[backtesting-pitfalls]]"
  - "[[python-for-algorithmic-trading]]"
  - "[[backtrader]]"
  - "[[zipline]]"
  - "[[quantconnect]]"
  - "[[walk-forward-optimization]]"
  - "[[custom-python-bots]]"
  - "[[book-python-for-algorithmic-trading]]"
---

Event-driven backtesting processes market data one event (bar, tick, or order fill) at a time, maintaining full portfolio state, simulating realistic order execution, and tracking positions through time. Unlike [[vectorized-backtesting]], which operates on entire arrays at once, event-driven systems iterate chronologically through each time step -- mirroring the information flow of actual live trading. This is the second backtesting approach Hilpisch teaches in *[[python-for-algorithmic-trading|Python for Algorithmic Trading]]*, after [[vectorized-backtesting]], because it bridges the gap between a working prototype and a live trading system (Source: [[book-python-for-algorithmic-trading]]).

## How It Works

An event-driven backtester follows a main loop that processes events sequentially:

1. **Market Data Event** -- The data handler emits the next bar (or tick) of price data
2. **Signal Generation** -- The strategy module receives the new data and generates a signal (buy, sell, hold) based only on information available up to that point
3. **Order Creation** -- The order management system translates the signal into a concrete order (market, limit, stop) with specific size and price parameters
4. **Execution Simulation** -- The execution handler fills the order with realistic assumptions: slippage, partial fills, [[market-impact-models|market impact]], broker commissions
5. **Portfolio Update** -- The portfolio module updates positions, cash, P&L, and risk metrics
6. **Loop** -- Return to step 1 for the next event

This loop continues until all historical data is consumed. Because each step only uses information available at that moment, event-driven backtests are inherently free from [[lookahead-bias]] (assuming correct implementation).

## Architecture Pattern

Most event-driven frameworks implement a variation of the same four-component architecture:

```
DataHandler  -->  Strategy  -->  Portfolio  -->  ExecutionHandler
     ^                                               |
     |_______________________________________________|
                        (main loop)
```

- **DataHandler** -- Reads historical data and emits bars/ticks one at a time. Can also connect to live data feeds for paper/live trading.
- **Strategy** -- Contains the trading logic. Receives market data events, computes indicators, and generates signal events.
- **Portfolio** -- Tracks positions, cash, risk exposure. Translates signals into orders with proper [[position-sizing|position sizing]]. Records all transactions for performance analysis.
- **ExecutionHandler** -- Simulates order execution (backtest mode) or routes orders to a broker API (live mode). Models [[slippage-modeling|slippage]], [[transaction-cost-modeling|commissions]], and fill probability.

This architecture is powerful because the same code structure works for backtesting, paper trading, and live trading -- only the DataHandler and ExecutionHandler change (Source: [[book-python-for-algorithmic-trading]]).

## Advantages

- **Realistic execution modeling** -- Simulates [[slippage-modeling|slippage]], partial fills, [[market-impact-models|market impact]], order queue position, and commission structures that materially affect strategy P&L
- **Full position and portfolio tracking** -- Knows the exact state of all positions, cash, margin, and exposure at every point in time
- **Handles complex logic** -- Multi-asset strategies, conditional orders (if-filled, OCO), dynamic [[position-sizing|position sizing]], [[risk-management|risk limits]] (max drawdown stops, correlation limits), and multi-timeframe logic are all natural to implement
- **Proper [[transaction-cost-modeling|transaction cost]] modeling** -- Costs can vary by asset, time of day, order size, and market conditions, just as they do in live trading
- **Direct path to live deployment** -- The strategy code written for backtesting can be reused in production with minimal changes, since the architecture already mirrors live trading flow
- **No look-ahead bias by design** -- The sequential processing model ensures the strategy never sees future data (assuming the DataHandler is implemented correctly)

## Limitations

- **Much slower than [[vectorized-backtesting|vectorized]]** -- Processing data bar-by-bar in Python is 100x to 1000x slower than vectorized NumPy operations. A backtest that takes milliseconds vectorized may take minutes or hours event-driven.
- **More complex code** -- Requires class hierarchies, event queues, and careful state management. A minimal event-driven framework is hundreds of lines of code versus 10-20 for vectorized.
- **Harder to debug** -- Bugs can hide in event ordering, state management, or edge cases that only manifest in specific market conditions
- **Requires careful architecture** -- Poor design choices early (e.g., tight coupling between components) make the system brittle and hard to extend

## Major Frameworks

Several open-source Python frameworks implement event-driven backtesting:

| Framework | Maintainer | Strengths | Limitations |
|-----------|-----------|-----------|-------------|
| [[backtrader]] | Community | Most popular, extensive documentation, flexible | Complex API, slow for large datasets |
| [[zipline]] | Community (ex-Quantopian) | Clean API, minute-level data support | US equities focused, maintenance uncertain |
| [[quantconnect]] | QuantConnect | Cloud-hosted LEAN engine, multi-asset, free data | Proprietary platform lock-in |
| Custom (Hilpisch) | DIY | Full control, educational value | No community, must maintain yourself |

Hilpisch builds a custom event loop in *[[python-for-algorithmic-trading|Python for Algorithmic Trading]]* using OANDA and FXCM APIs, which serves both as an educational exercise and as a deployable system for forex trading (Source: [[book-python-for-algorithmic-trading]]).

## When to Use

Event-driven backtesting is appropriate for:

- **Final validation** before committing real capital -- this is the last check before paper trading
- **Complex strategies** with multiple assets, timeframes, or conditional logic that cannot be expressed as column operations
- **Strategies sensitive to execution quality** -- where [[slippage-modeling|slippage]], fill probability, and [[transaction-cost-modeling|transaction costs]] materially affect returns
- **Building production systems** -- when the backtest code will evolve into the live trading system

It is **less appropriate** for:

- Rapid hypothesis screening (use [[vectorized-backtesting]] instead)
- Parameter sweeps across hundreds of combinations (too slow without parallelization)
- Quick exploratory analysis where execution details are not yet relevant

## Event-Driven vs Vectorized

| Dimension | [[vectorized-backtesting|Vectorized]] | Event-Driven |
|-----------|-----------|-------------|
| Speed | Milliseconds for years of data | Minutes to hours |
| Code complexity | 10-20 lines | Hundreds of lines, class architecture |
| Execution realism | None (perfect fills assumed) | Slippage, partial fills, market impact |
| Portfolio state | No tracking | Full position/P&L tracking |
| Transaction costs | Flat assumption at best | Realistic, dynamic modeling |
| Use case | Hypothesis screening | Final validation, live prep |

Hilpisch recommends: **prototype with vectorized, validate with event-driven, deploy with live infrastructure** (Source: [[book-python-for-algorithmic-trading]]).

## Related

- [[vectorized-backtesting]] -- The fast prototyping alternative
- [[backtesting-pitfalls]] -- Common errors in both approaches
- [[python-for-algorithmic-trading]] -- The book that teaches both approaches end-to-end
- [[backtrader]] -- Most popular Python event-driven framework
- [[zipline]] -- Quantopian's backtesting engine
- [[quantconnect]] -- Cloud-based backtesting and deployment platform
- [[walk-forward-optimization]] -- Proper out-of-sample validation methodology
- [[custom-python-bots]] -- Taking event-driven backtests to live trading
- [[trading-system-deployment]] -- The deployment step after validation

## Sources

- (Source: [[book-python-for-algorithmic-trading]]) -- Primary reference for event-driven backtesting architecture and implementation
