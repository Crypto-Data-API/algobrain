---
title: "Trading Bots"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [ai-trading, trading-bots, index]
aliases: ["Trading Bots", "trading-bots"]
---

# Trading Bots

Automated trading systems, frameworks, and platforms — the software that turns a strategy into hands-off execution.

Trading bots remove human emotion and latency from execution and can operate 24/7 -- critical in crypto markets that never close. But automation is a force multiplier in both directions: a flawed strategy, a bug, or an unhandled exchange error becomes an *automated* money-losing machine. Robust error handling, position limits, idempotent order logic, and kill switches are non-negotiable regardless of complexity. See [[bot-risks-and-pitfalls]] before deploying capital.

This section covers the building blocks ([[bot-architecture]]), open-source frameworks you self-host, and hosted no-code platforms.

## Start Here

- [[bot-architecture]] -- Design patterns for reliable automated trading systems (signal generation, risk gating, order execution, state management, reconciliation)
- [[bot-risks-and-pitfalls]] -- What goes wrong with bots and how to protect yourself
- [[freqtrade]] -- Open-source Python bot framework for crypto trading

## Bot Categories by Strategy

- **Grid bots** -- place a ladder of buy/sell orders across a range; profit from oscillation in sideways markets
- **DCA bots** -- dollar-cost-average entries and scale into positions on adverse moves
- **Arbitrage bots** -- exploit price differences across venues (see [[cross-exchange-arbitrage]], [[funding-rate-arbitrage]])
- **Market-making bots** -- quote both sides and earn the spread (see [[hummingbot]])
- **MEV bots (crypto)** -- extract value from transaction ordering on-chain
- **Signal/strategy bots** -- execute discretionary or systematic signals via webhook or code

## Frameworks (self-hosted / code)

- [[freqtrade]] -- open-source Python framework for crypto; backtesting, hyperopt, dry-run, Telegram control
- [[hummingbot]] -- open-source market-making and arbitrage framework (CEX + DEX)
- [[custom-python-bots]] -- rolling your own with CCXT/exchange SDKs when frameworks don't fit

## Platforms (hosted / no-code)

- [[pionex]] -- exchange with built-in free grid/DCA bots
- [[three-commas]] -- hosted bot platform (DCA, grid, options) across multiple exchanges
- [[composer-trade]] -- no-code systematic strategy builder (US equities/ETFs)
- [[traderspost]] -- webhook bridge connecting TradingView/signals to broker execution

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/ai-trading/trading-bots"
WHERE type != "index"
SORT updated DESC
```

## Comparisons

- [[freqtrade-vs-hummingbot]] -- comparing two popular open-source trading bot frameworks
- [[tradingview-vs-metatrader]] -- comparing charting and trading platforms

## Related

- [[backtesting-pitfalls]] -- bots amplify backtest-to-live decay; validate before deploying
- [[ai-trading-agents]] -- LLM-driven autonomous agents, the frontier beyond rule-based bots
- [[risk-management]] -- position limits and kill criteria for automated systems

## Sources

- Section overview; see individual framework/platform pages for cited sources and current feature/pricing details.
