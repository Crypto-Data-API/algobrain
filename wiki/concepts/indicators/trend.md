---
title: Trend
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [trend-following, technical-analysis, momentum, indicators]
aliases: ["Uptrend", "Downtrend", "Sideways Trend", "Market Trend", "trend"]
domain: [technical-analysis]
prerequisites: ["[[support-and-resistance]]", "[[moving-averages]]"]
difficulty: beginner
related:
  - "[[trend-following]]"
  - "[[momentum]]"
  - "[[adx]]"
  - "[[moving-average]]"
  - "[[moving-averages]]"
  - "[[dow-theory]]"
  - "[[golden-cross]]"
  - "[[market-breadth]]"
  - "[[support-and-resistance]]"
---

A **trend** is the prevailing directional movement of a market's price over a given period. Trends are conventionally classified as **uptrends** (a sequence of higher highs and higher lows), **downtrends** (lower highs and lower lows), or **sideways / ranging** markets (price oscillating within a horizontal band with no net direction). Identifying the dominant trend is foundational to most discretionary and systematic strategies, since trading with the trend carries a structurally higher probability of success than trading against it.

## Types of Trend

- **Uptrend** — successive higher highs and higher lows; demand exceeds supply and buyers control price.
- **Downtrend** — successive lower highs and lower lows; supply exceeds demand and sellers control price.
- **Sideways / range** — price bounded between horizontal [[support-and-resistance|support and resistance]]; neither side dominates and breakout direction is uncertain.

| Trend | Swing structure | Underlying balance | Bias / typical play |
|-------|-----------------|--------------------|----------------------|
| Uptrend | Higher highs, higher lows | Demand > supply | Buy pullbacks to support / rising MA |
| Downtrend | Lower highs, lower lows | Supply > demand | Sell rallies; long-only sit out |
| Sideways | Equal highs/lows in a band | Balance | Fade the edges; await breakout |

[[dow-theory|Dow Theory]] further decomposes trends by duration: the **primary** trend (months to years), the **secondary** (corrective swings of weeks), and **minor** fluctuations (days). It adds two principles still cited today: trends persist until a clear reversal proves otherwise, and a move must be **confirmed** across related indices ([[dow-theory]] originally required the Industrials and Transports to agree) before it is trusted. A trend remains intact until its defining swing structure is broken — e.g., an uptrend is invalidated when price makes a lower low beneath the prior swing low.

### Worked example: reading swing structure

A stock prints a low of $40, rallies to $48, pulls back to $43, then pushes to $52. That sequence — low $40 → high $48 → higher low $43 → higher high $52 — is a textbook **uptrend** (each swing low and high above the last). The trend stays valid while pullbacks hold above the prior swing low ($43). If a later dip breaks $43 and the next bounce fails below $52, the higher-high/higher-low chain is broken and the uptrend is in question — the first objective evidence of a possible reversal.

## How Trends Are Identified

Trends exist on every timeframe simultaneously: a stock can be in a daily uptrend, a weekly downtrend, and a monthly uptrend at once, which is why multiple-timeframe analysis is standard practice.

Common identification tools:

- **Moving averages** — price holding above a rising [[moving-average|moving average]] (e.g. the 50- or 200-day) signals an uptrend; the slope and stacking order of multiple MAs gauge strength. When the 50-day crosses above the 200-day — the [[golden-cross]] — it is widely read as confirmation a primary uptrend has taken hold; the bearish mirror is the [[death-cross]].
- **Trendlines** — connecting consecutive swing lows (uptrend) or swing highs (downtrend); a break of the line warns of a possible change.
- **Swing structure** — the higher-high/higher-low (or lower-high/lower-low) sequence itself is the most direct definition.
- **[[adx|ADX]]** — quantifies trend *strength* irrespective of direction; readings above ~25 indicate a trending regime, below ~20 a range.
- **[[market-breadth|Market breadth]]** — advancing-vs-declining stocks confirm whether an index trend is broadly supported or driven by a narrow set of names.

## Trading Relevance

"The trend is your friend" captures the central trading maxim: align with the dominant direction. [[trend-following]] strategies and managed-futures CTAs ([[trend-following-cta]]) seek to capture the body of established trends, while [[mean-reversion]] strategies bet on trend exhaustion and reversion to a mean. Distinguishing a *trending* regime from a *ranging* one is itself a [[market-regime|regime-detection]] problem — many strategies fail not because the logic is wrong but because it is applied in the wrong regime. Trend definition also drives risk: counter-trend trades warrant tighter stops and smaller size because the prevailing flow is against the position.

How traders actually use trend in practice:

- **Direction filter first.** Decide the dominant trend before choosing a tactic — buy-the-dip in an uptrend, sell-the-rally in a downtrend, fade-the-edges in a range. The same setup has opposite expectancy in different trends.
- **Trade the higher timeframe, time the lower.** Establish the primary trend on the daily/weekly chart, then use an intraday chart to find a low-risk entry in that direction (multiple-timeframe alignment).
- **Let winners run with trailing stops.** Trend-following expectancy comes from a few large wins, so [[trend-following]] systems exit on a trailing stop or a structure break rather than a fixed profit target.
- **Respect the regime.** [[adx|ADX]] or a moving-average slope filter can switch a book between trend and mean-reversion logic so each is run only where it has edge.

## Pitfalls and Risks

- **Trend is defined in hindsight.** You only know a trend existed after the swings have formed; acting on a "trend" too early often means trading noise.
- **Whipsaws in ranges.** Moving-average and breakout signals fire repeatedly and fail in sideways markets — the single biggest source of trend-system losses. Combine with an [[adx|ADX]]/range filter.
- **Trends end abruptly.** Reversals are often faster and sharper than the trend that preceded them; a trailing stop, not a forecast, should take you out.
- **Timeframe conflict.** A daily uptrend inside a weekly downtrend can trap traders who fixate on one chart — always note which timeframe a trend claim refers to.
- **Confirmation lag vs. early signal trade-off.** More confirmation (price above a rising 200-day, [[dow-theory]]-style cross-index agreement) reduces false signals but gives back more of the move at the turn.

## Related

- [[trend-following]] — the strategy family built on riding trends.
- [[momentum]] — the closely related tendency of recent winners to keep winning.
- [[adx]] — the canonical trend-strength filter.
- [[dow-theory]] — the classical framework for primary/secondary/minor trends and confirmation.
- [[golden-cross]] / [[death-cross]] — moving-average crossovers used to flag trend changes.
- [[moving-average]] — the workhorse tool for identifying and confirming trend.
- [[support-and-resistance]] — the levels that define ranges and pullback entries.
- [[market-regime]] — trending vs ranging regime classification.

## Sources

- Charles H. Dow / William P. Hamilton, *The Stock Market Barometer* (1922) — origin of Dow Theory and the three-trend classification.
- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — standard reference on trend, trendlines, and multiple-timeframe analysis.
- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* (1948) — classic treatment of trend structure and reversal.
