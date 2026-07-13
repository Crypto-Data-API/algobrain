---
title: "Swing Trading Strategies"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [swing-trading, technical-analysis, momentum]
aliases: ["Swing Trading"]
related: ["[[strategies-overview]]", "[[day-trading-overview]]", "[[position-trading-overview]]", "[[technical-analysis-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]"]
---

# Swing Trading

Swing trading targets price moves that develop over days to weeks — too slow for day traders, too fast for position traders. It is among the most popular approaches for part-time traders because it does not require watching screens all day, yet still captures meaningful directional moves.

## What Distinguishes This Family

- **Edge sources** — mostly *behavioral*: pullback entries exploit other traders' premature profit-taking in trends, breakout trades exploit underreaction to new information, and mean-reversion swings fade overreaction. See [[edge-taxonomy]].
- **Typical timeframe** — multi-day to multi-week holds. Direction is read on daily charts; entries are refined on 4-hour or 1-hour charts (multi-timeframe analysis).
- **Capital and data requirements** — low: end-of-day or hourly OHLCV is sufficient, and most setups are managed with a few minutes per day. The hidden cost is *overnight gap risk* — position sizing must assume the stop can be jumped, so per-trade risk is typically kept to 1% or less of equity.
- **Who it suits** — part-time traders with day jobs, and anyone who wants more activity than position trading without the screen-time and cost drag of day trading. Core skills: support/resistance reading, volume confirmation, and disciplined stop placement (see [[atr-trailing-stop]] and [[atr-position-sizing]]).
- **Regime sensitivity** — pullback and breakout setups need a trending regime; range setups need a quiet one. Check the [[regime-matrix]] before favoring one setup family over another.

## Strategies in This Category

This folder does not yet contain dedicated strategy pages — swing-timeframe strategies currently live elsewhere in the catalog. The curated list below collects them; new swing-specific pages should be created in this folder.

### Core Reference

- [[swing-trading]] — The main strategy page: setups, entry/exit rules, and risk management for the style.

### Swing-Timeframe Setups Elsewhere in the Catalog

- [[triple-screen-system]] — Elder's multi-timeframe filter: weekly trend, daily oscillator, intraday entry.
- [[range-trading]] — Buying support and selling resistance inside established ranges.
- [[breakout-trading]] — Entering when price escapes consolidation with volume confirmation.
- [[breakout-strategies]] — Survey of breakout variants and their filters.
- [[support-resistance-breakout]] — Trading the failure of well-tested horizontal levels.
- [[channel-breakout]] — Entries on escapes from trend channels.
- [[donchian-channel-breakout]] — Rule-based N-day high/low breakouts (the turtle entry).
- [[moving-average-crossover]] — Simple trend signal commonly traded on daily bars.
- [[macd-crossover]] — Momentum crossover signal suited to multi-day holds.
- [[rsi-divergence]] — Spotting swing reversals where price and momentum disagree.
- [[small-cap-momentum]] — Multi-day momentum continuation in small-cap stocks.
- [[momentum-stocks]] — Screening and riding stocks in strong momentum phases.
- [[earnings-volatility-trading]] — Trading the multi-day move around earnings events.

### Risk Tools for Swing Trades

- [[atr-position-sizing]] — Volatility-scaled sizing that respects overnight gap risk.
- [[atr-trailing-stop]] — Letting winners run while protecting open profit.

## All Pages (auto)

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/swing-trading"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Coverage Gaps

Dedicated pages still to create in this folder: pullback/retracement entry playbook, multi-timeframe analysis methodology, and gap-risk-aware position sizing for swing trades.

## Related

- [[strategies-overview]] — top-level strategy catalog
- [[day-trading-overview]] — the next-faster timeframe family
- [[position-trading-overview]] — the next-slower timeframe family
- [[technical-analysis-overview]] — the toolkit most swing setups are built from
- [[edge-taxonomy]] — where swing-trading edges come from
- [[regime-matrix]] — matching setup type to market regime
