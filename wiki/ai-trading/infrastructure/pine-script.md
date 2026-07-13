---
title: "Pine Script"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [technical-analysis, backtesting, algorithmic]
aliases: ["Pine Script", "PineScript", "Pine"]
domain: [algorithmic]
difficulty: beginner
related: ["[[backtesting]]", "[[indicators]]", "[[technical-analysis]]", "[[easylanguage]]", "[[python]]", "[[ninjatrader]]", "[[sierra-chart]]"]
---

Pine Script is the proprietary, domain-specific scripting language of TradingView, used to build custom [[indicators]], strategies, alerts, and screeners that run directly on TradingView charts. It is the most widely used retail strategy-development language in the world by user count, owing to TradingView's 30M+ monthly active users and a public library of hundreds of thousands of community-published scripts. Pine Script is deliberately constrained and chart-centric — closer to a spreadsheet formula language than a general-purpose language like [[python|Python]] — which makes it fast to learn but limited for anything beyond chart-bound logic.

## What It Is and How It Works

Pine Script executes once **per bar**, left to right across the chart's history and then in real time on each new tick/bar. Each script variable is implicitly a *time series* (a value per bar), and most built-in functions operate over that series. The current major version is **Pine Script v6** (rolled out 2024-2025), which added dynamic requests, boolean/int type improvements, and more flexible `request.*` calls.

Two script types dominate:

- **Indicators** (`indicator()`) — overlay or pane studies that plot values (moving averages, oscillators, custom signals). They do not place trades.
- **Strategies** (`strategy()`) — add a built-in [[backtesting]] and broker-emulation layer: `strategy.entry`, `strategy.exit`, `strategy.close`, position sizing, commission/slippage modelling, and an auto-generated performance report (net profit, max drawdown, profit factor, win rate, Sharpe).

A minimal strategy sketch:

```pine
//@version=6
strategy("MA Cross", overlay=true)
fast = ta.sma(close, 10)
slow = ta.sma(close, 30)
if ta.crossover(fast, slow)
    strategy.entry("Long", strategy.long)
if ta.crossunder(fast, slow)
    strategy.close("Long")
plot(fast, color=color.blue)
plot(slow, color=color.orange)
```

## Trading / Finance Relevance

Pine Script is where most retail [[technical-analysis]] ideas get prototyped and shared. Its relevance to a trading workflow:

- **Rapid signal prototyping** — express an indicator or rule in minutes, see it on a chart instantly, and iterate visually.
- **Built-in backtesting** — the `strategy()` framework gives an immediate (if simplistic) historical performance read without separate tooling.
- **Alerts and automation** — Pine alerts can fire webhooks to bots/brokers (e.g. via [[traderspost]] or broker integrations), making Pine a common front-end for semi-automated retail execution.
- **Sentiment / crowd signal** — the popularity ranking of community scripts and "ideas" is itself a read on what indicators retail traders are crowding into.

## Limitations (important for serious backtesting)

Pine Script's convenience hides several traps that make it unsuitable as a primary research engine for systematic strategies:

- **Repainting** — scripts that reference higher-timeframe or future-confirmed values can show signals in backtest that would not have existed live. This is the single most common source of inflated Pine backtest results.
- **Limited bar history** — non-premium accounts backtest on a capped number of bars, biasing results.
- **No portfolio backtesting** — a strategy runs on one symbol at a time; cross-sectional/factor research and portfolio-level risk are out of scope.
- **Closed sandbox** — no arbitrary file/network access, no external libraries; you cannot pull in custom data or ML models the way you can in [[python|Python]].
- **Optimistic fill assumptions** — default fill and slippage modelling understates real transaction costs unless explicitly configured.

For production systematic work, traders typically move from Pine prototypes to [[python|Python]] frameworks (Backtrader, VectorBT, [[backtesting|backtesting.py]]) or platform-native languages — NinjaScript ([[ninjatrader]]), EasyLanguage ([[easylanguage]]), or C++ ACSIL ([[sierra-chart|Sierra Chart]]).

## Comparison to Other Strategy Languages

| Language | Platform | Power | Use case |
|---|---|---|---|
| **Pine Script** | TradingView | Low-mid (chart-bound) | Fast retail indicator/strategy prototyping, alerts |
| [[easylanguage\|EasyLanguage]] | TradeStation/MultiCharts | Mid | Retail systematic backtesting |
| NinjaScript (C#) | [[ninjatrader\|NinjaTrader]] | Mid-high | Automated futures strategies |
| ACSIL (C++) | [[sierra-chart\|Sierra Chart]] | High | Latency-sensitive order-flow studies |
| [[python\|Python]] | Open / QuantConnect | Highest | Full research-to-production, ML, portfolio |

## Related

- [[backtesting]] — Pine's `strategy()` framework, and its pitfalls
- [[indicators]] — what most Pine scripts compute
- [[technical-analysis]] — the discipline Pine serves
- [[easylanguage]] — comparable retail strategy language
- [[python]] — the upgrade path for serious systematic work
- [[ninjatrader]], [[sierra-chart]] — alternative platforms with their own scripting

## Sources

- TradingView Pine Script v6 reference and user manual — https://www.tradingview.com/pine-script-docs/
- See tradingview for platform context (user base, Pine community library).
