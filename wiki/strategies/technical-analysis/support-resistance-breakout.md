---
title: Support and Resistance Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags:
  - breakout
  - support-resistance
  - volume
  - fakeout
  - retest
strategy_type: breakout
timeframe: swing
markets:
  - stocks
  - crypto
  - forex
complexity: beginner
backtest_status: untested
related:
  - "[[channel-breakout]]"
  - "[[opening-range-breakout]]"
  - "[[volatility-breakout]]"
  - "[[rsi-divergence]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
---

# Support and Resistance Breakout Strategy

## Overview

The Support and Resistance Breakout strategy trades price breaking through established horizontal levels that have previously acted as barriers. When price breaks above [[resistance]] with strong [[volume]], former resistance becomes new support, offering a high-probability continuation setup. Conversely, when price breaks below [[support]], it becomes new resistance. The **retest** of the broken level is often the safest entry point, as it confirms the breakout is genuine rather than a **false breakout (fakeout)**. This strategy is foundational to [[technical-analysis]] and forms the basis of many other breakout approaches (Source: [[book-technical-analysis-of-the-financial-markets]]).

## Rules

### Entry Rules
1. **Identify Key Levels:** Mark horizontal [[support-resistance]] levels that price has tested at least **2-3 times**. The more touches, the more significant the level.
2. **Breakout Entry:** Enter when price closes **above resistance** (for longs) or **below support** (for shorts) on a candle with above-average [[volume]] (>1.5x the 20-bar average).
3. **Retest Entry (Preferred):** Wait for price to break through the level, then pull back to retest the broken level (former resistance becomes support). Enter on the retest candle that holds the level. This avoids fakeouts.
4. **Volume Confirmation:** The breakout candle must show a meaningful volume spike. Low-volume breakouts have a high probability of failure (Source: book-how-to-make-money-in-stocks).
5. **Multiple Timeframe Alignment:** The breakout on the entry timeframe should align with the trend on one timeframe higher (e.g., break out on the 4H, trend is bullish on the daily).

### Exit Rules
1. **Measured Move:** Target the distance equal to the height of the prior range (from support to resistance) projected from the breakout point.
2. **Next Level Target:** Set the target at the next significant support/resistance level above (longs) or below (shorts).
3. **Stop Loss:** Place the stop just below the broken resistance level (for longs) or above the broken support (for shorts). The broken level should now hold as support/resistance.
4. **Failure Exit:** If price breaks back through the level on heavy volume and closes on the other side, the breakout has failed. Exit immediately.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[support-resistance]] (horizontal) | Manual identification | Key breakout levels |
| [[volume]] | 20-bar average | Breakout confirmation |
| [[moving-average]] | 20 and 50 EMA | Trend context |
| [[rsi]] | 14-period | Avoid buying into overbought breakouts |
| [[candlestick-patterns]] | N/A | Retest confirmation |

## Example Trade

**Setup:** SOL/USD daily chart. A clear resistance level at $175 has been tested and rejected 3 times over the past 6 weeks. Price is in a higher-low pattern, indicating building pressure. The 20 EMA is above the 50 EMA (bullish trend structure).

**Entry (Aggressive):** Price closes above $175 at $177.50 on volume that is 2.1x the 20-day average. Enter long at $177.50.

**Entry (Conservative/Retest):** Price breaks to $182, then pulls back to $176 over 2 days. A bullish [[hammer]] candle forms at $175.80 -- the old resistance holding as new support. Enter long at $176.50.

**Management:** Stop loss at $172 (below the breakout level). Risk = $4.50. Target = $175 + ($175 - $152 range height) = $198. R/R = 4.8:1.

**Exit:** Price rallies to $198 target over 12 days. Or: if price closes back below $175 on strong volume, exit immediately as a failed breakout.

## Performance Characteristics

- **Win Rate:** 55-65% for retest entries; 40-50% for aggressive breakout entries
- **Best Conditions:** Markets emerging from extended consolidation ranges with building volume
- **Worst Conditions:** Low-liquidity environments, news-driven chop, or markets with wide spreads
- **Average Holding Period:** 3-20 days depending on the range width and target distance
- **Key Insight:** Retests offer dramatically better risk/reward and win rate than aggressive breakout entries

## Advantages

- Conceptually simple and intuitive; beginner-friendly entry into [[technical-analysis]]
- Clear, predefined levels remove ambiguity from trade planning
- Works on all timeframes and all liquid markets (stocks, [[crypto]], [[forex]])
- The retest entry provides excellent risk/reward with tight stops
- Breakout levels are visible to many traders, creating self-reinforcing dynamics

## Disadvantages

- **False breakouts (fakeouts)** are the primary risk -- price breaks through, triggers entries, then reverses sharply
- Requires patience to wait for proper retests; aggressive entries get caught in fakeouts more often
- Support/resistance identification has a subjective element -- different traders may draw levels differently
- Breakouts in low-[[volume]] environments are unreliable
- Stop placement just below the broken level may be too obvious, inviting [[stop-hunting]] by larger players
- Round numbers and obvious levels attract institutional manipulation and liquidity grabs

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy's foundational treatment of support/resistance theory, role reversal (broken support becoming resistance and vice versa), and breakout confirmation techniques
