---
title: "Fibonacci Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [fibonacci, retracement, extension, golden-ratio, technical-analysis, support-resistance, swing-trading]
aliases: ["Fibonacci Retracement Strategy", "Fib Trading", "Golden Ratio Trading"]
strategy_type: technical
timeframe: swing
markets: [stocks, crypto, forex]
complexity: beginner
backtest_status: untested
related: ["[[smart-money-concepts]]", "[[support-and-resistance]]", "[[elliott-wave]]", "[[price-action]]", "[[moving-average-crossover]]"]
---

# Fibonacci Trading

## Overview

Fibonacci Trading uses mathematically derived levels based on the **Fibonacci sequence** (0, 1, 1, 2, 3, 5, 8, 13, 21...) to identify potential [[support-and-resistance]] zones in price charts. The key ratios -- **23.6%, 38.2%, 50%, 61.8%, and 78.6%** -- are derived from the relationships between numbers in the sequence. The most important is **61.8%**, the **golden ratio** (approximately 1/1.618), which appears throughout nature, architecture, and, arguably, financial markets. Fibonacci **extensions** (1.272, 1.618, 2.618) project potential profit targets beyond the original move.

Fibonacci levels are among the most widely used tools in [[technical-analysis]], applied by retail and institutional traders across all markets and timeframes. The theory is that retracements within a trend tend to find support or resistance at these mathematically significant levels. Whether this works because of some intrinsic mathematical property of markets or simply because enough traders watch the same levels (creating a self-fulfilling prophecy) is debated. Regardless of the reason, Fibonacci levels frequently coincide with actual turning points, making them a valuable tool -- especially when combined with other forms of analysis like [[price-action]], [[volume]], or [[smart-money-concepts]].

## Rules

### Entry
1. **Identify a clear impulse move:** Find a significant swing from a low to a high (uptrend) or from a high to a low (downtrend). The move should be sharp and directional, not choppy.
2. **Draw the Fibonacci retracement** from the swing low to the swing high (uptrend) or swing high to swing low (downtrend) using your charting platform's Fibonacci tool.
3. **Watch key retracement levels for entry:**
   - **38.2%** -- shallow retracement. Strong trends often bounce here. Enter only if you see bullish [[price-action]] confirmation (e.g., hammer, engulfing candle).
   - **50%** -- the equilibrium level. Not a true Fibonacci number but widely watched. A popular entry zone.
   - **61.8%** -- the golden ratio. The most important level. Deep retracements to 61.8% that hold are high-probability reversal zones.
   - **78.6%** -- very deep retracement. If this level fails, the impulse move is likely fully reversed.
4. **Confirmation required:** Do not buy blindly at a Fibonacci level. Wait for confirming signals: bullish/bearish candlestick patterns, [[rsi]] divergence, [[volume]] increase, or the level coinciding with a [[moving-average]] or horizontal [[support-and-resistance]].
5. **Confluence is key:** The strongest setups occur when a Fibonacci level aligns with another technical factor -- e.g., the 61.8% retracement sits exactly on the 200-day [[moving-average]] and a prior horizontal support level.

### Exit
1. **Fibonacci extensions for targets:**
   - **1.272 extension** -- conservative target (first take-profit zone)
   - **1.618 extension** -- standard target (the golden ratio projection)
   - **2.618 extension** -- aggressive target for strongly trending markets
2. **Partial profit-taking:** Take 50% at the 1.272 extension, move stop to breakeven, and let the rest ride to 1.618 or 2.618.
3. **Stop-loss:** Place just below the next deeper Fibonacci level. If you enter at the 61.8% retracement, place the stop below the 78.6% level (or below the swing low for the most conservative stop).
4. **Invalidation:** If price closes convincingly below the 78.6% retracement (for longs), the bullish thesis is broken. Exit the trade.

### Position Sizing
Risk 1-2% of account per trade. The distance from entry (Fibonacci level) to stop-loss (next deeper level) determines the position size. Tighter Fibonacci spacing allows larger positions for the same dollar risk.

## Indicators Used
- **Fibonacci Retracement Tool** (built into all charting platforms: TradingView, MT4/MT5, thinkorswim)
- **Fibonacci Extension Tool** for profit targets
- [[rsi]] -- divergence at Fibonacci levels strengthens reversal signals
- Candlestick patterns (hammer, engulfing, doji) for entry confirmation
- [[volume]] -- increased volume at Fibonacci levels indicates institutional interest
- [[moving-average]] -- confluence with the 50 or 200-day MA and a Fibonacci level is powerful
- [[support-and-resistance]] -- horizontal S/R overlapping with Fibonacci levels

## Example Trade
**Asset:** ETH/USD daily chart, uptrend retracement
1. ETH rallies from a swing low of $2,200 to a swing high of $4,000 (+$1,800 impulse move). The trend is firmly bullish.
2. Draw Fibonacci retracement from $2,200 to $4,000. Key levels: 38.2% = $3,312, 50% = $3,100, 61.8% = $2,888.
3. ETH retraces over 10 days and finds support at $2,900, just above the 61.8% level ($2,888). A bullish engulfing candle forms on the daily chart. [[rsi]] shows bullish divergence (price made a lower low, RSI made a higher low).
4. Enter long at $2,920. Stop-loss at $2,820 (below the 78.6% level of $2,587 is too wide, so use a tighter stop below recent price action). Risk: $100/ETH.
5. Set targets using Fibonacci extensions from the retracement low: 1.272 extension = $4,290, 1.618 extension = $5,112.
6. ETH resumes its uptrend. Take 50% profit at $4,290 (+$1,370/ETH, +47%). Move stop to breakeven. The remaining position runs to $4,800 before reversing. Exit at $4,700.
7. **Result:** Average gain of ~$1,535/ETH (~52.6%) with a risk of $100/ETH. Risk-reward ratio: ~15:1 on the first half, ~17.8:1 on the second.

## Performance Characteristics
- **Win Rate:** 45-55% when used with proper confirmation. Drops below 40% when used as the sole entry method without confluence.
- **Profit Factor:** 1.5-2.5. The tight stop-losses enabled by precise Fibonacci entries allow for strong risk-reward ratios.
- **Best Market Conditions:** Trending markets with clean impulse-correction-impulse patterns. The strategy excels in [[crypto]] and [[forex]] where trends are often technically driven.
- **Worst Market Conditions:** Choppy, range-bound markets where there are no clear impulse moves to measure. Also fails in V-shaped reversals where price does not retrace to any Fibonacci level.
- **Universal applicability:** Works on all timeframes from 5-minute to monthly charts. Higher timeframes produce more reliable levels because more participants watch them.

## Advantages
- Extremely easy to learn and apply -- the Fibonacci tool is built into every charting platform
- Provides precise, objective price levels for entries, stops, and targets
- Universally used across all markets and timeframes, creating potential self-fulfilling prophecy effects
- Combines seamlessly with other [[technical-analysis]] tools: [[rsi]], [[moving-average]], [[price-action]], [[smart-money-concepts]]
- Applicable to both retracements (entries) and extensions (targets), providing a complete trade framework
- Works in any trending market without requiring indicators or complex calculations

## Disadvantages
- **No scientific basis:** The claim that markets follow Fibonacci ratios from nature is mathematically unproven. The levels work primarily because many traders watch them (self-fulfilling prophecy)
- **Multiple levels create ambiguity:** With five retracement levels (23.6%, 38.2%, 50%, 61.8%, 78.6%), price will almost always land "near" one of them, making it easy to see patterns in hindsight that were not predictive in real-time
- **Subjective anchor points:** Different traders choose different swing highs and lows to draw from, producing different levels
- **No edge in isolation:** Backtests of pure Fibonacci strategies (buy at 61.8%, stop at 78.6%) show marginal results without additional filters
- Does not account for fundamental changes that can override technical levels
- Over-reliance on Fibonacci can create confirmation bias and tunnel vision

## See Also
- [[smart-money-concepts]] -- uses Fibonacci concepts (premium/discount zones) within its framework
- [[elliott-wave]] -- Elliott Wave theory heavily incorporates Fibonacci ratios for wave relationships
- [[support-and-resistance]] -- Fibonacci levels are a form of dynamic support and resistance
- [[price-action]] -- essential confirmation tool at Fibonacci levels
- [[moving-average-crossover]] -- MA levels that coincide with Fibonacci levels create strong confluence
