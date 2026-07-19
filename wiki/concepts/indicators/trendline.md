---
title: "Trendline"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [technical-analysis, indicators, trend-following, price-action]
aliases: ["trendline", "trend line", "trend lines", "uptrend line", "downtrend line", "trendlines"]
domain: [indicators]
prerequisites: ["[[indicators-ta-primer]]", "[[trend]]"]
difficulty: beginner
related:
  - "[[support-and-resistance]]"
  - "[[trend]]"
  - "[[trend-following]]"
  - "[[swing-high]]"
  - "[[swing-low]]"
  - "[[chart-patterns]]"
  - "[[price-action]]"
  - "[[breakout-trading]]"
  - "[[moving-averages]]"
  - "[[donchian-channels]]"
  - "[[dow-theory]]"
  - "[[volume]]"
---

A **trendline** is a straight line drawn on a price chart connecting a series of [[swing-high|swing highs]] or [[swing-low|swing lows]] to visualise the direction and slope of a [[trend]]. It is the simplest and oldest tool in [[indicators-ta-primer|technical analysis]] — a diagonal form of [[support-and-resistance]] that acts as a moving floor under an uptrend or a moving ceiling over a downtrend. Trendlines are used to define the trend, to time entries on pullbacks to the line, and to flag a possible trend change when the line breaks.

## Overview

Whereas horizontal [[support-and-resistance]] marks a static price level, a trendline marks a *sloping* level that rises or falls over time. The underlying idea, rooted in [[dow-theory]], is that trends consist of a sequence of higher highs and higher lows (an uptrend) or lower highs and lower lows (a downtrend). A trendline simply connects the relevant pivots of that sequence so the trader can see, at a glance, the path the trend has been respecting.

There are two basic forms:

- **Uptrend line (rising support):** drawn underneath an advance by connecting two or more ascending [[swing-low|swing lows]]. As long as price stays above it and keeps making higher lows along it, the uptrend is intact.
- **Downtrend line (falling resistance):** drawn above a decline by connecting two or more descending [[swing-high|swing highs]]. As long as price stays below it and keeps making lower highs along it, the downtrend is intact.

## How to draw a valid trendline

1. **Identify the trend first.** Decide whether price is making higher highs/lows (up) or lower highs/lows (down). Draw the line along the *lows* in an uptrend and along the *highs* in a downtrend.
2. **Connect at least two pivots.** Two points define a line; the line only becomes *meaningful* once price tests it a third time and holds. More touches generally mean a more significant line.
3. **Respect the wicks vs bodies choice.** Some traders connect candle extremes (wicks), others connect closing prices. Closing-price lines are less sensitive to single-bar spikes; be consistent.
4. **Favour the right slope.** A sustainable trendline is typically a moderate angle (roughly 30–45°). A near-vertical line is unsustainable and tends to break quickly; a near-flat line barely qualifies as a trend.
5. **Higher timeframe = stronger line.** A weekly trendline carries far more weight than a 5-minute one, the same hierarchy that applies to horizontal levels.

A trendline is best thought of as a *zone* rather than a precise line — price often probes slightly through it (a wick) before resuming, so allow a small margin rather than treating the line as an exact price.

## Channels and the return line

Drawing a second, parallel line on the opposite side of price creates a **channel**. In an uptrend, the lower line (rising support) connects the lows and a parallel upper "return line" connects the highs; price oscillates between them. Channels help traders buy near the lower boundary, take partial profit near the upper boundary, and spot acceleration (price breaking *above* an up-channel) or exhaustion. Channel construction is closely related to [[donchian-channels]] and to the channels used in [[chart-patterns]] such as flags and rising/falling wedges.

## How traders use trendlines

- **Trend definition.** The slope and integrity of the line answer the first question of any chart: which way is it trending, and is the trend still healthy?
- **Pullback entries.** In an uptrend, a pullback to the rising trendline is a classic lower-risk long entry (buy the dip), with a [[stop-loss]] just below the line. The reward/risk is attractive because the invalidation point is close and well-defined.
- **Trendline breaks.** A decisive close *through* the line — ideally on rising [[volume]] — warns that the trend may be changing and is a core trigger in [[breakout-trading]]. Many traders wait for a retest of the broken line (which often flips role, as with horizontal [[support-and-resistance]] polarity) before committing.
- **Combination with other tools.** Trendlines gain conviction at [[confluence]] with [[moving-averages]], [[fibonacci-retracement]] levels, or horizontal support/resistance.

## Hypothetical example

A stock bottoms at $20, rallies to $26, pulls back to $22, then rallies to $30 and pulls back to $25. Connecting the two rising lows ($20 and $22) projects an upward-sloping trendline. Weeks later price dips again and touches the line near $27 — a third touch that holds. A trend-following trader buys there with a stop just under the line at $26.20, reasoning that a break below would signal the higher-lows sequence is over. Months later, after a further advance, price closes hard *below* the line on heavy volume; the trader treats that break as a warning that the uptrend's character has changed and tightens or exits. (Illustrative scenario, not a recorded trade.)

## Pitfalls and limitations

- **Subjectivity.** Which pivots to connect, and whether to use wicks or closes, is a judgement call; two analysts can draw different lines on the same chart. This is the most-cited criticism of trendlines.
- **Curve-fitting after the fact.** It is easy to draw a line that perfectly fits past data and means nothing forward. A line is only useful if it was drawable *before* the latest move.
- **False breaks (fakeouts).** Price frequently pierces a trendline intrabar and snaps back. Waiting for a *closing* break, or a retest, filters many false signals.
- **Redrawing.** As trends accelerate or decelerate, the relevant line changes; clinging to an old line that price has long abandoned leads to bad decisions.
- **Not predictive on its own.** A trendline describes what price has done; it does not guarantee continuation. It works best combined with [[volume]], momentum, and [[support-and-resistance]] confirmation.

## Related

- [[support-and-resistance]] — horizontal cousin; trendlines are diagonal S/R
- [[trend]] / [[trend-following]] / [[dow-theory]] — the trend framework trendlines visualise
- [[swing-high]] / [[swing-low]] — the pivots a trendline connects
- [[breakout-trading]] — strategy built on trendline (and level) breaks
- [[chart-patterns]] — many patterns (wedges, triangles, channels) are pairs of trendlines
- [[donchian-channels]] / [[moving-averages]] — dynamic alternatives to hand-drawn lines
- [[price-action]] — the broader discipline trendlines belong to

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — foundational treatment of trendlines, channels, and breaks.
- Edwards, R. & Magee, J. *Technical Analysis of Stock Trends* — classic source for trendline construction and validity.
- Pring, Martin J. *Technical Analysis Explained* — trendline significance, slope, and confirmation.
