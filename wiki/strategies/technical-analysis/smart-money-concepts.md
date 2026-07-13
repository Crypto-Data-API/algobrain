---
title: "Smart Money Concepts"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [smart-money, ICT, order-blocks, fair-value-gap, liquidity-sweep, market-structure, institutional-trading]
aliases: ["SMC", "ICT Trading", "Inner Circle Trader", "Institutional Order Flow"]
strategy_type: technical
timeframe: intraday
markets: [forex, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[fibonacci-trading]]", "[[support-and-resistance]]", "[[supply-and-demand]]", "[[price-action]]", "[[volume-profile]]"]
---

# Smart Money Concepts

## Overview

Smart Money Concepts (SMC) is a [[technical-analysis]] framework that attempts to identify and trade alongside **institutional order flow** -- the activity of banks, hedge funds, and market makers who move markets with large positions. The methodology was popularized by the **Inner Circle Trader (ICT)**, Michael Huddleston, and has become one of the most widely discussed retail trading approaches, especially in [[forex]] and [[crypto]] markets. SMC reframes traditional [[support-and-resistance]] and [[supply-and-demand]] concepts through the lens of how institutional traders actually execute.

The core premise is that institutions cannot execute large orders at a single price -- they need **liquidity** (other traders' stop-losses and limit orders) to fill their positions. Therefore, price moves to areas of liquidity (above swing highs, below swing lows) to trigger retail stops, which provides the volume institutions need. SMC traders learn to identify these **liquidity pools**, **order blocks** (zones where institutions placed their orders), **fair value gaps** (imbalances in price action), and **market structure shifts** (changes in trend direction) to anticipate where price is heading and enter alongside the "smart money."

## Rules

### Entry
1. **Identify market structure:** Determine whether the market is in a bullish structure (higher highs and higher lows) or bearish structure (lower highs and lower lows). A **market structure shift (MSS)** or **break of structure (BOS)** occurs when this pattern changes -- the first signal of a potential reversal.
2. **Locate order blocks:** An **order block** is the last bearish candle before a strong bullish move (bullish OB) or the last bullish candle before a strong bearish move (bearish OB). These zones represent where institutions placed their initial orders.
3. **Identify fair value gaps (FVG):** A FVG is a three-candle pattern where the middle candle's body creates a gap between the first and third candles' wicks. Price tends to return to fill these imbalances. In bullish trends, buy when price retraces into a bullish FVG.
4. **Wait for a liquidity sweep:** Before entering, look for price to sweep beyond a recent swing high or low (taking out retail stop-losses). The **liquidity grab** signals that institutions have accumulated their position. Enter on the reversal after the sweep.
5. **Combine signals:** The highest-probability setup is: market structure shift + price retraces into an order block that overlaps with a fair value gap + a prior liquidity sweep. Enter with a limit order at the order block zone.

### Exit
1. **Target the opposing liquidity pool:** If you entered long after a sweep of lows, target the next liquidity pool above (previous swing high where sell stops are resting).
2. **Risk-reward minimum 1:3.** SMC entries are precise, allowing tight stops just beyond the order block, with targets at the next liquidity zone.
3. **Stop-loss:** Place below the order block (for longs) or above it (for shorts). If the order block fails (price trades through it convincingly), the institutional thesis is invalidated.
4. **Partial profits:** Take 50% at the first significant resistance/support level. Move stop to breakeven. Let the remaining 50% run to the full target.

### Position Sizing
Risk 1-2% per trade. The tight stop-loss placement (relative to targets) allows for favorable risk-reward even with small position sizes.

## Indicators Used
- **Market structure analysis:** Manual identification of swing highs and lows, BOS and MSS levels
- **Order blocks:** Last opposing candle before an impulsive move (drawn as a zone on the chart)
- **Fair value gaps:** Three-candle imbalance zones where price did not trade efficiently
- **Liquidity zones:** Areas above swing highs and below swing lows where stop-losses cluster
- **Premium/Discount zones:** Using the [[fibonacci-trading|Fibonacci]] 50% level (equilibrium) of a range to determine if price is in a premium zone (above 50%, look to sell) or discount zone (below 50%, look to buy)
- [[volume]] for confirmation of institutional activity at key levels
- Kill zones: Specific trading sessions (London Open, New York Open) when institutional activity peaks

## Example Trade
**Market:** EUR/USD 15-minute chart during London session
1. EUR/USD has been in a bearish structure (lower highs, lower lows) on the 1-hour chart. Price makes a low at 1.0850.
2. On the 15-minute chart, price sweeps below 1.0850 (taking out retail sell stops) and immediately reverses with a strong bullish candle. This is a **liquidity sweep** at a key low.
3. A **market structure shift** occurs: price breaks above the last 15-minute lower high at 1.0870, establishing a new bullish structure.
4. Price retraces to a **bullish order block** at 1.0865 (the last bearish candle before the impulsive move up) which overlaps with a **fair value gap** from 1.0862 to 1.0868.
5. Enter long at 1.0865 with stop-loss at 1.0845 (below the order block and the liquidity sweep low). Risk: 20 pips.
6. Target: The next liquidity pool at 1.0920 (previous swing high where buy stops are resting). Reward: 55 pips. Risk-reward: 1:2.75.
7. Price rallies during the New York session and hits 1.0920. **Result:** +55 pips profit on a 20-pip risk.

## Performance Characteristics
- **Win Rate:** 45-55% when applied with strict confluence requirements. Drops significantly when traders force setups without proper confirmation.
- **Profit Factor:** 1.5-2.5. The favorable risk-reward ratios (1:2 to 1:5) allow profitability at lower win rates.
- **Best Market Conditions:** Trending markets with clear structure. Markets during high-liquidity sessions (London, New York) where institutional activity is most visible.
- **Worst Market Conditions:** Choppy, low-volume markets (Asian session for forex pairs, weekends for crypto). Markets in consolidation where order blocks and FVGs are constantly invalidated.
- **Typical Timeframes:** 15-minute to 1-hour for intraday execution, with higher timeframe (4H, daily) for directional bias.

## Advantages
- Provides a logical framework for understanding WHY price moves to certain levels (institutional liquidity needs)
- Precise entry zones (order blocks + FVGs) allow for tight stop-losses and favorable risk-reward ratios
- Encourages trading with the institutional flow rather than against it
- Applicable across all markets, though most widely used in [[forex]] and [[crypto]]
- Free educational content widely available (ICT YouTube, online communities)
- Combines well with [[fibonacci-trading]] and [[price-action]] analysis

## Disadvantages
- **Subjectivity:** Different traders identify order blocks, FVGs, and market structure differently, leading to inconsistent application
- **Hindsight bias:** Many SMC concepts are easy to identify in hindsight but ambiguous in real-time
- **No institutional validation:** The claim that this reveals actual bank/hedge fund behavior is unverified -- institutions use algorithms, not candlestick patterns
- **Overcomplicated terminology:** SMC often rebrands simple concepts ([[support-and-resistance]], [[supply-and-demand]]) with new names, adding complexity without proven additional edge
- Heavily marketed on social media with unrealistic profit claims, attracting underprepared traders
- Requires significant screen time for intraday execution during specific kill zones

## See Also
- [[fibonacci-trading]] -- SMC practitioners often use Fibonacci levels for premium/discount analysis
- [[support-and-resistance]] -- order blocks are a refined version of S/R zones
- [[supply-and-demand]] -- SMC builds directly on supply/demand zone concepts
- [[price-action]] -- raw price action reading is the foundation of all SMC analysis
- [[volume-profile]] -- institutional footprint analysis that complements SMC concepts
