---
title: "Position Trading"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [position-trading, technical-analysis, fundamental-analysis, trend-following]
aliases: ["Position Trading", "Position Trader"]
domain: [technical-analysis]
prerequisites: ["[[trend-following]]", "[[risk-management-overview]]"]
difficulty: intermediate
related: ["[[swing-trading]]", "[[day-trading]]", "[[trend-following]]", "[[technical-analysis]]", "[[atr]]", "[[position-sizing]]", "[[asset-allocation]]"]
---

Position trading is a longer-term trading style in which positions are held for weeks to months — and sometimes years — to capture major price trends or fundamental revaluation. Unlike [[day-trading]] or [[swing-trading]], position trading tolerates significant short-term fluctuations in pursuit of larger moves, typically targeting gains of 20%+ per trade. Position traders combine fundamental-analysis (identifying undervalued or improving companies) with [[technical-analysis]] (timing entries at support or breakouts and managing risk with wide trailing stops on higher timeframes).

## Overview

Position trading sits at the long end of the active-trading spectrum:

| Style | Hold period | Chart timeframe | Trades/year | Screen time |
|---|---|---|---|---|
| Scalping | seconds-minutes | tick/1m | thousands | constant |
| [[day-trading]] | intraday | 1m-15m | hundreds | full day |
| [[swing-trading]] | days-weeks | 1h-daily | ~50-200 | daily check |
| **Position trading** | weeks-months+ | daily/weekly/monthly | ~20-50 | weekly check |
| Buy-and-hold investing | years | monthly | <10 | minimal |

The defining trade-off is **signal-to-noise versus capital efficiency**: higher timeframes filter out intraday and daily noise, making trends more visible and directional moves more pronounced, at the cost of tying up capital for long stretches.

## How it works

**Entry.** Position traders generally enter on confirmed higher-timeframe signals: weekly breakouts from multi-month bases, pullbacks to a rising long-term moving average (e.g. 30-week / 200-day), or fundamental catalysts (sustained earnings acceleration, sector rotation into a strengthening industry). [[mark-minervini|Minervini]]-style growth-stock investing and Stan Weinstein's "Stage 2" breakouts are canonical position-trading frameworks.

**Exit.** Wide trailing stops on weekly closes, breaks of the long-term moving average, or deterioration of the original fundamental thesis. The goal is to ride a trend through normal pullbacks rather than to exit on the first dip.

**Position sizing.** This is the critical discipline. Because higher-timeframe stops are wide (often 15-25%), each share risks a larger dollar amount, so positions must be smaller to keep portfolio risk constant. The standard fixed-fractional rule:

```
Shares = (Account × Risk%) / (Entry − Stop)
```

A trader risking 1% of a $100,000 account on a stock entered at $50 with a $40 stop (20% stop) risks $10/share, so buys `(100,000 × 0.01) / 10 = 100 shares` ($5,000 position). A swing trader using a 5% stop on the same name could hold 4x the position for the same 1% account risk. [[atr|ATR]]-based sizing — setting the stop at a multiple of Average True Range — adapts position size to each instrument's volatility.

## Variants

- **Trend-following position trading** — riding weekly/monthly trends (the [[trend-following]] / managed-futures approach applied to single names or sectors).
- **Sector rotation** — rotating capital toward sectors strengthening in the current phase of the [[economic-indicators|economic cycle]].
- **Growth (CANSLIM / Minervini)** — buying leading growth stocks breaking out of bases and holding through the advance.
- **Value / mean-reversion position trading** — accumulating undervalued names and holding for multi-quarter re-rating.

## Trading relevance

- **Lower costs, lower turnover.** With only 20-50 trades a year, commissions, spreads, and slippage barely dent returns — the opposite of high-frequency styles where [[transaction-costs]] dominate. This widens the set of viable strategies.
- **Compatible with a day job.** No constant screen-watching, making it the realistic style for most non-professionals.
- **Tax efficiency.** Longer holds can qualify for long-term capital-gains treatment in many jurisdictions, materially improving after-tax returns versus rapid trading.
- **Psychological demands.** The hard part is holding through pullbacks that temporarily erase large open profits and through extended flat periods. Clearly pre-defined exit rules and conviction are required; discretionary intervention is the main failure mode.
- **Opportunity cost and drawdown duration.** Capital is locked for long periods, and a losing streak can take months to recover. Diversification across uncorrelated positions and disciplined sizing are the defenses.
- **Trend dependence.** Position trading thrives in trending regimes and bleeds in choppy, range-bound markets — performance is regime-dependent (see [[market-regime]]).

## Related

- [[swing-trading]] — the next-shorter timeframe style
- [[day-trading]] — the short-timeframe contrast
- [[trend-following]] — the dominant position-trading methodology
- [[technical-analysis]] — entry/exit timing on higher timeframes
- [[atr]] — volatility-based stop and sizing input
- [[position-sizing]] — the core risk-control discipline
- [[asset-allocation]] — portfolio context for long-hold positions

## Sources

- Weinstein, S. *Secrets for Profiting in Bull and Bear Markets* — stage analysis and weekly-chart position trading.
- Minervini, M. *Trade Like a Stock Market Wizard* — growth-stock position trading with risk control.
- O'Neil, W. *How to Make Money in Stocks* — CANSLIM, base breakouts, and holding leaders.
- Van Tharp, *Trade Your Way to Financial Freedom* — position sizing and fixed-fractional risk models.
