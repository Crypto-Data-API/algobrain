---
title: "Harmonic Patterns"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [harmonic-patterns, gartley, bat, butterfly, crab, shark, fibonacci, prz, geometric-patterns, technical-analysis]
aliases: ["Harmonic Trading", "Gartley Pattern", "XABCD Patterns", "Harmonic Price Patterns"]
strategy_type: technical
timeframe: swing
markets: [forex, stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[fibonacci-trading]]", "[[elliott-wave]]", "[[supply-demand-zones]]", "[[support-and-resistance]]", "[[smart-money-concepts]]"]
---

# Harmonic Patterns

## Overview

Harmonic Patterns are **geometric price structures** defined by precise [[fibonacci-trading]] ratios between each leg of the pattern. Originally introduced by **H.M. Gartley** in his 1935 book *Profits in the Stock Market* and later refined by **Scott Carney**, Larry Pesavento, and others, harmonic trading identifies specific XABCD patterns where each swing (XA, AB, BC, CD) must conform to exact Fibonacci retracement and extension relationships. The key patterns -- **Gartley, Bat, Butterfly, Crab, and Shark** -- each have distinct ratio requirements. The trade is entered at the **Potential Reversal Zone (PRZ)**, where the pattern completes and the CD leg reaches its expected Fibonacci level. Because the entry, stop-loss, and target are all mathematically derived, harmonic trading provides unusually precise trade parameters. The strategy is particularly popular in [[forex]] markets, where clean price action and 24-hour liquidity produce well-formed geometric patterns.

## How It Works

Every harmonic pattern follows an **XABCD structure** -- five points connected by four price swings (legs). The X point is the origin, and the pattern unfolds as price swings from X to A, retraces to B, extends to C, then completes at D. The D point is the PRZ where you enter the trade. What distinguishes each pattern is the **specific Fibonacci ratio** required at each leg:

- **Gartley (222 pattern):** AB retraces 61.8% of XA. BC retraces 38.2-88.6% of AB. CD completes at the 78.6% retracement of XA. The most common and reliable pattern.
- **Bat:** AB retraces 38.2-50% of XA. BC retraces 38.2-88.6% of AB. CD completes at the 88.6% retracement of XA. Deep retracement pattern.
- **Butterfly:** AB retraces 78.6% of XA. CD extends to 1.272-1.618% of XA (beyond the X point). An extension pattern that forms at market extremes.
- **Crab:** AB retraces 38.2-61.8% of XA. CD extends to the 1.618% of XA. The most extreme extension pattern with the tightest PRZ.
- **Shark:** Uses the 0-5 labeling system. Relies on the 88.6% and 1.13% ratios. A newer pattern identified by Scott Carney.

The PRZ is where multiple Fibonacci levels converge from different legs, creating a **cluster** of support or resistance. This confluence is what gives harmonic patterns their edge.

## Rules and Signals

### Entry
1. **Identify the developing XABCD structure** as price unfolds. Most traders use pattern recognition software (TradingView's harmonic pattern indicators, or tools like Harmonic Scanner).
2. **Validate each leg** against the required Fibonacci ratios for the specific pattern. If any leg falls outside the acceptable ratio range, the pattern is invalid.
3. **Enter at the PRZ (D point)** when price reaches the calculated completion zone. Wait for a confirming candle -- a reversal candlestick pattern (hammer, engulfing, pin bar) at the PRZ.
4. **Do not front-run the PRZ.** Wait for price to reach the zone and show signs of rejection before committing capital.

### Stop-Loss
- Place the stop just beyond the PRZ. For Gartley and Bat patterns, this is below the X point. For Butterfly and Crab patterns, use a fixed stop beyond the 1.618 extension.
- Stops are typically tight because the PRZ is precisely defined. If price blows through the PRZ, the pattern has failed and you exit immediately.

### Profit Targets
- **Target 1:** The 38.2% retracement of the CD leg (conservative). **Target 2:** The 61.8% retracement (standard). **Target 3:** The A or C point (aggressive). Take partial profits at each level.

## Example Trade

**Asset:** EUR/USD 4-hour chart, bullish Gartley
1. XA leg: Price drops from 1.1200 (X) to 1.0800 (A) -- a 400-pip decline.
2. AB leg: Price retraces upward to 1.1047 (B) -- a 61.8% retracement of XA. Valid.
3. BC leg: Price drops to 1.0900 (C) -- a 57% retracement of AB. Valid (within 38.2-88.6%).
4. CD leg developing: Calculate the PRZ at the 78.6% retracement of XA = 1.0800 + (400 x 0.786) = 1.1114 (D).
5. Price reaches 1.1110 and forms a bearish engulfing candle. Enter short at 1.1100. Stop at 1.1210 (above X). Risk: 110 pips.
6. Target 1 at 38.2% of CD = 1.0985 (+115 pips). Target 2 at 61.8% of CD = 1.0914 (+186 pips). Target 3 at the A point = 1.0800 (+300 pips).
7. **Result:** Take 50% at Target 1 (1:1 R:R), 30% at Target 2 (1.7:1 R:R), and let 20% run to Target 3 (2.7:1 R:R).

## Advantages
- Provides extremely precise entry, stop, and target levels -- removes much of the ambiguity in trade planning
- The PRZ concept -- where multiple [[fibonacci-trading]] levels converge -- creates high-probability reversal zones
- Excellent risk-reward ratios due to tight stop-losses at mathematically defined invalidation points
- Pattern recognition software automates identification, reducing manual scanning effort
- Works well in [[forex]] markets where technical levels are widely respected by algorithmic and institutional traders

## Disadvantages
- **Steep learning curve:** Memorizing the ratio requirements for each pattern and validating legs in real-time takes significant study
- Subjectivity in choosing the X point -- different starting points produce different patterns
- In strongly trending markets, patterns complete and immediately fail as momentum overrides the reversal signal
- Over-optimization risk: with enough Fibonacci levels, almost any price structure can be labeled as "close enough" to a harmonic pattern
- Requires constant chart monitoring to catch patterns as they complete at the PRZ

## See Also
- [[fibonacci-trading]] -- the mathematical foundation for all harmonic ratio calculations
- [[elliott-wave]] -- another Fibonacci-based structural analysis framework
- [[supply-demand-zones]] -- institutional order flow zones that can confirm or invalidate harmonic PRZs
- [[support-and-resistance]] -- horizontal levels that add confluence when they align with the PRZ
- [[smart-money-concepts]] -- order block theory that can explain why harmonic PRZs work (institutional orders sitting at those levels)
