---
title: Support and Resistance
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [technical-analysis, indicators]
aliases: [support, resistance, "S/R", "support-resistance", "Support Level", "Resistance Level", "S/R Levels"]
domain: [indicators]
prerequisites: ["[[indicators-ta-primer]]"]
difficulty: beginner
related:
  - "[[moving-averages]]"
  - "[[volume]]"
  - "[[order-book]]"
  - "[[vwap]]"
  - "[[fibonacci-retracement]]"
  - "[[volume-profile]]"
  - "[[support-resistance-breakout]]"
  - "[[swing-high]]"
  - "[[swing-low]]"
  - "[[stop-loss]]"
  - "[[price-action]]"
---

# Support and Resistance

Support and resistance are **price levels where buying or selling pressure has historically been strong enough to halt or reverse a price move**. Support acts as a floor where demand absorbs selling pressure; resistance acts as a ceiling where supply overwhelms buying pressure. They are the most foundational concept in [[indicators-ta-primer|technical analysis]] — virtually every chart-based strategy references them for entries, exits, and [[stop-loss]] placement.

## Overview

When price approaches support, buyers view the asset as cheap and step in while sellers ease off, so price tends to bounce. When price approaches resistance, sellers view it as expensive and step up while buyers pull back, so price tends to reverse. The more times a level has been tested and held, the more significant it is considered — though each successive test without a fresh catalyst can gradually exhaust the willing buyers (or sellers) defending it.

When a level breaks, the role frequently inverts: broken support tends to become resistance, and broken resistance tends to become support. This is called **polarity** (or role reversal). The mechanism is behavioral: traders who bought at former support and are now underwater become motivated sellers as price returns to their entry, capping the rally at the old floor.

## Types of Support and Resistance

| Type | Description |
|------|-------------|
| **Horizontal** | Static price levels where prior swing highs, swing lows, or consolidation zones created supply/demand. The classic, most-watched form. |
| **Trendline** | Dynamic diagonal levels drawn along ascending [[swing-low\|swing lows]] (rising support) or descending [[swing-high\|swing highs]] (falling resistance). |
| **Moving averages** | Dynamic floors/ceilings from [[moving-averages]] (commonly the 50-day and [[200-day-ma\|200-day MA]]) that institutions reference, creating self-fulfilling order clustering. |
| **Fibonacci** | Levels derived from [[fibonacci-retracement]] ratios (38.2%, 50%, 61.8%) applied to a prior price swing. |
| **Volume profile** | High-volume nodes from [[volume-profile]] analysis act as magnets where significant prior trading occurred. |
| **Round numbers** | Psychological levels ($100, $50,000 for BTC) where human order placement clusters. |
| **VWAP** | Intraday institutional benchmark; [[vwap]] acts as dynamic support/resistance for the session. |

## How to Identify Key Levels

1. **Multiple touches** — the more times price has bounced off or rejected a level, the stronger it is.
2. **Prior swing points** — note prior [[swing-high|swing highs]] (resistance) and [[swing-low|swing lows]] (support).
3. **Volume confirmation** — strong levels typically coincide with high-volume areas; use [[volume-profile]] to find them.
4. **Timeframe hierarchy** — weekly/monthly levels are stronger than daily; daily are stronger than intraday.
5. **Confluence** — when multiple types of S/R align at one price (horizontal + Fibonacci + moving average), the level is strongest.

## Psychology

Support and resistance work in large part because of anchoring and loss aversion. Traders who bought near a prior low and saw price rise feel validated when price returns and often buy again to defend their thesis; traders who missed the move see the retest as a second chance. This clustering of buy orders creates genuine demand. [[volume|Volume]] confirmation matters: a bounce on heavy volume is more meaningful than one on thin volume, and a break on heavy volume signals genuine distribution or accumulation rather than a wick.

## Trading Relevance

### Bounce / Reversal
Buy near support with a stop just below it; sell near resistance with a stop just above. This works best in ranging markets where price oscillates between defined levels, and the reward/risk is highest when the level is well-established and price approaches on declining volume.

### Breakout
Enter when price breaks through support (short) or resistance (long) with [[volume]] confirmation — see [[support-resistance-breakout]]. False breakouts (fakeouts) are common, so many traders wait for a retest of the broken level (now flipped by polarity) before committing.

### Stop Placement
Place stops **beyond** the level, not exactly at it, to allow room for wicks and false tests. If support is at $100, a stop at $98–99 avoids being knocked out by a wick that probes $99.50 before bouncing.

## Common Mistakes

- **Drawing too many levels** — focus on the 2–3 most significant levels on each timeframe.
- **Treating S/R as exact prices** — they are zones, not precise lines; use a range (e.g., $100–102).
- **Ignoring timeframe** — a level on a 5-minute chart is trivial next to one on a weekly chart.
- **Not adapting** — levels go stale if they haven't been tested recently.

## Related

- [[support-resistance-breakout]] — breakout strategy built on S/R
- [[indicators-ta-primer]] — broader TA framework
- [[fibonacci-retracement]] — Fibonacci-derived S/R
- [[volume-profile]] — volume-based S/R
- [[swing-high]] / [[swing-low]] — the pivots that define horizontal levels
- [[moving-averages]] — dynamic S/R
- [[order-book]] — shows resting orders at S/R levels
- [[vwap]] — institutional intraday S/R benchmark

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — foundational treatment of support, resistance, and polarity (see [[technical-analysis-of-the-financial-markets]]).
- Edwards, R. & Magee, J. *Technical Analysis of Stock Trends* — classic source for support/resistance and role reversal.
- Bulkowski, T. *Encyclopedia of Chart Patterns* — empirical data on level reliability and breakout behavior.
