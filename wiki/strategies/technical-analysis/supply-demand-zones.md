---
title: "Supply and Demand Zones"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [supply-demand, demand-zones, supply-zones, order-flow, institutional-trading, sam-seiden, rally-base-rally, drop-base-drop, technical-analysis]
aliases: ["Supply and Demand Trading", "S/D Zones", "Demand Zone Strategy", "Supply Zone Strategy"]
strategy_type: technical
timeframe: swing
markets: [forex, stocks, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[smart-money-concepts]]", "[[wyckoff-method]]", "[[support-and-resistance]]", "[[fibonacci-trading]]", "[[volume]]"]
---

# Supply and Demand Zones

## Overview

Supply and Demand Zone trading identifies specific price areas where **institutional orders** created significant imbalances between buyers and sellers, causing sharp price movements. Unlike traditional [[support-and-resistance]] which marks horizontal lines at previous highs and lows, supply and demand zones are **price ranges** (zones, not lines) that represent areas where large pending orders from banks, hedge funds, and other institutional participants are likely sitting unfilled. The concept was popularized by **Sam Seiden** and the Online Trading Academy, drawing on principles from the [[wyckoff-method]] and basic microeconomics. A **demand zone** is an area where institutional buyers overwhelmed sellers, creating a base before a rally -- unfilled buy orders may remain, making it a zone where price is likely to bounce. A **supply zone** is where sellers overwhelmed buyers before a price drop. The strategy is straightforward: wait for price to return to a previously established zone and enter in the direction of the original institutional move. Supply and demand analysis has become a foundational element of [[smart-money-concepts]] and is widely applied in [[forex]], stocks, and [[crypto]].

## How It Works

### Zone Formation Patterns
Supply and demand zones are created by specific price action sequences:

- **Rally-Base-Rally (RBR):** Price rallies, pauses in a narrow consolidation (the base), then rallies again. The base is a **demand zone** -- institutional buyers accumulated here. When price later revisits this zone, it may bounce.
- **Drop-Base-Drop (DBD):** Price drops, consolidates briefly, then drops again. The base is a **supply zone** -- institutional sellers distributed here. When price later revisits, it may reverse downward.
- **Rally-Base-Drop (RBD):** Price rallies into a base, then drops sharply. The base is a **supply zone** formed at the top. This is a reversal pattern.
- **Drop-Base-Rally (DBR):** Price drops into a base, then rallies sharply. The base is a **demand zone** formed at the bottom. This is a reversal pattern.

### Zone Drawing Rules
1. Identify the **departure candle(s)** -- the base candles before the explosive move. Draw the zone from the **high of the highest base candle** to the **low of the lowest base candle.**
2. **The strength of the move away determines zone quality.** A zone that produced a 200-pip rally is stronger than one that produced a 20-pip move.
3. **Fresh zones are strongest.** A zone never revisited has the highest probability. Each retest absorbs pending orders, weakening the zone. By the third visit, it is typically exhausted.

## Rules and Signals

### Entry
1. **Identify fresh supply or demand zones** on the higher timeframe (daily or 4-hour). Mark the zone boundaries.
2. **Wait for price to return to the zone.** Do not chase -- let price come to you.
3. **Enter on the first touch of a fresh zone.** For demand zones: limit buy at the top of the zone (aggressive) or wait for bullish confirmation (conservative). For supply zones: limit sell at the bottom or wait for bearish confirmation. Higher-timeframe zones take priority.

### Stop-Loss
- Place the stop just beyond the opposite edge of the zone. For a demand zone long entry: stop below the bottom of the demand zone. For a supply zone short entry: stop above the top of the supply zone.
- If the zone is very wide, use the midpoint or the opposite end of the base candles as a tighter stop.

### Profit Targets
- **Target the nearest opposing zone.** Long from demand? Target the nearest supply zone above, and vice versa. Minimum 1:2 risk-reward required -- skip the trade if the nearest opposing zone is too close. Take partial profits at 1:1 R:R and trail the remainder.

## Example Trade

**Asset:** GBP/USD 4-hour chart
1. GBP/USD drops from 1.2800 to 1.2600, consolidates in a tight 20-pip range (1.2600-1.2620) for 3 candles, then rallies sharply to 1.2750. This creates a **Drop-Base-Rally demand zone** at 1.2600-1.2620.
2. Over the next week, price trades between 1.2700-1.2780. The demand zone at 1.2600-1.2620 is fresh -- never revisited.
3. Price begins to decline again, reaching the demand zone. Set a limit buy at 1.2620 (top of the zone). Stop at 1.2590 (below the zone). Risk: 30 pips.
4. Price touches 1.2615, filling the limit order, and a bullish engulfing candle forms on the 4-hour chart. The nearest supply zone above is at 1.2780-1.2800.
5. Target: 1.2780 (bottom of supply zone). Reward: 160 pips. Risk-reward: 5.3:1.
6. Price rallies to 1.2790 over the next 3 days. Take profit at 1.2780.
7. **Result:** Entry 1.2620, exit 1.2780. Profit: 160 pips on 30 pips of risk. Risk-reward: 5.3:1.

## Advantages
- Provides specific, objective price zones for entries and exits rather than subjective judgment calls
- Excellent risk-reward ratios: zones create tight stop-losses with wide profit targets to the opposing zone
- Conceptually intuitive -- the idea that institutional orders create footprints that price revisits is logical and grounded in market microstructure
- Works across all markets and timeframes, from 5-minute scalping in [[forex]] to weekly charts in stocks
- Complements and enhances [[smart-money-concepts]], [[wyckoff-method]], and [[fibonacci-trading]] analysis

## Disadvantages
- **Zones fail regularly:** Institutional dynamics change, and pending orders at old zones may be canceled or already filled
- Subjectivity in zone drawing: different traders will define the zone boundaries differently (which candles constitute the "base"?)
- The theory that "unfilled institutional orders" remain at zones is an oversimplification of how institutional trading actually works
- In strongly trending markets, price often slices through zones without hesitation, especially on second or third retests
- The strategy does not incorporate [[volume]] analysis in its standard form, which is a significant omission given the institutional flow thesis

## See Also
- [[smart-money-concepts]] -- the modern evolution of supply/demand theory with order blocks, fair value gaps, and liquidity concepts
- [[wyckoff-method]] -- the original institutional accumulation/distribution framework that supply/demand zones are derived from
- [[support-and-resistance]] -- traditional S/R identifies price levels; supply/demand adds the institutional order flow thesis
- [[fibonacci-trading]] -- Fibonacci retracement levels that coincide with supply/demand zones create high-confluence setups
- [[volume]] -- volume analysis at supply/demand zones confirms or denies the institutional presence theory
