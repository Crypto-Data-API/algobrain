---
title: Bollinger Bands vs Keltner Channels
type: comparison
created: 2026-04-07
updated: 2026-04-07
status: good
tags:
  - volatility
  - envelopes
  - indicators
subjects:
  - "[[bollinger-bands]]"
  - "[[atr]]"
comparison_dimensions:
  - calculation
  - volatility-measure
  - squeeze
  - breakouts
  - trend
  - combining
related:
  - "[[volatility]]"
  - "[[standard-deviation]]"
  - "[[breakout-trading]]"
---

# Bollinger Bands vs Keltner Channels

## Overview

[[bollinger-bands]] and Keltner Channels are both volatility envelope indicators that plot bands around a central moving average. They look nearly identical on a chart but differ in one critical way: Bollinger Bands use standard deviation to set band width while Keltner Channels use [[atr]] (Average True Range). This difference in volatility measurement changes how the bands behave, and using both together creates one of the most powerful setups in technical analysis -- the volatility squeeze.

## Comparison Table

| Dimension | Bollinger Bands | Keltner Channels |
|-----------|----------------|-----------------|
| **Center Line** | 20-period SMA (default) | 20-period EMA (default) |
| **Band Calculation** | Center +/- 2 standard deviations | Center +/- 1.5x ATR |
| **Volatility Measure** | Standard deviation (close-to-close) | ATR (includes gaps and intrabar range) |
| **Band Width Behavior** | Expands and contracts dramatically | Smoother expansion and contraction |
| **Reaction to Gaps** | Slow to reflect gaps | Immediately reflects gaps via true range |
| **Squeeze Detection** | BB narrowing signals compression | Steadier width makes squeeze less obvious |
| **Breakout Signals** | Close outside bands is significant | Close outside bands is rarer, stronger |
| **Walk the Bands** | Price can ride upper/lower band in trends | Less band-walking behavior |
| **Trend Identification** | Band slope and walk direction | Channel slope and position within channel |
| **Mean Reversion** | Touch of outer band as entry trigger | Touch of outer channel as entry trigger |

## Key Differences

**Standard deviation vs ATR.** Standard deviation only measures close-to-close volatility, which means it can understate volatility when there are large intraday ranges or gaps that close near the open. ATR captures the full true range including gaps, making Keltner Channels more responsive to all forms of volatility, not just closing price dispersion.

**Band expansion dynamics.** Bollinger Bands expand and contract much more aggressively than Keltner Channels. A single large bar can push Bollinger Bands significantly wider. Keltner Channels smooth this out because ATR is typically calculated over 10-20 periods. This makes Bollinger Bands more visually dramatic and Keltner Channels more stable.

**The squeeze.** The most important application of these two indicators together is the volatility squeeze. When Bollinger Bands contract inside the Keltner Channels, it signals extreme [[volatility]] compression. Since BB react more to vol changes than KC, the BB contracting inside KC means volatility has dropped below its normal range. The subsequent breakout when BB expand back outside KC often produces powerful directional moves.

**Breakout interpretation.** A close outside Bollinger Bands occurs roughly 5% of the time (with 2 standard deviation bands). It can mean either a breakout or an exhaustion signal depending on context. Keltner Channel breakouts are less frequent and more often indicate genuine trend continuation.

## When to Use Each

**Use Bollinger Bands when:**
- You want to identify volatility compression and expansion
- Trading mean-reversion strategies (fade touches of outer bands)
- You need a visual gauge of whether price is statistically stretched
- Looking for squeeze setups (ideally combined with Keltner Channels)
- Trading individual equities where close-to-close vol matters

**Use Keltner Channels when:**
- Trading instruments with frequent gaps (futures, forex)
- You want smoother, more stable envelope boundaries
- Trading trend-following pullback entries (buy near lower channel in uptrend)
- You need a more conservative breakout signal
- The asset has high intraday volatility relative to close-to-close volatility

**Use both together for the squeeze.** Plot Bollinger Bands (20, 2) and Keltner Channels (20, 1.5) on the same chart. When BB moves inside KC, a squeeze is on. When BB expands back outside KC, the squeeze fires. Use the [[macd]] histogram or momentum oscillator to determine the breakout direction.

## Verdict

Bollinger Bands are the more popular and versatile of the two, offering better squeeze detection and more widely recognized signal levels. Keltner Channels provide a smoother, more stable alternative that better accounts for gap and intrabar volatility. The real edge comes from using both together for squeeze detection -- this is one of the few multi-indicator setups that genuinely adds value rather than just adding noise. If you only use one, Bollinger Bands are the standard choice, but learning to combine them with Keltner Channels unlocks a powerful volatility-based trading framework.
