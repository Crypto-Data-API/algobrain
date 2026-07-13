---
title: Volatility Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - breakout
  - volatility
  - atr
  - nr7
  - larry-williams
  - contraction-expansion
strategy_type: breakout
timeframe: swing
markets:
  - stocks
  - futures
  - crypto
complexity: intermediate
backtest_status: untested
related:
  - "[[opening-range-breakout]]"
  - "[[channel-breakout]]"
  - "[[support-resistance-breakout]]"
  - "[[bollinger-bands]]"
---

# Volatility Breakout Strategy

## Overview

The Volatility Breakout strategy enters trades when price moves more than **X times the Average True Range (ATR)** from the previous close, capturing the explosive expansion that follows periods of contraction. Markets cycle between **contraction** (low volatility, tight ranges) and **expansion** (high volatility, trending moves). This strategy, refined by **Larry Williams** and other system traders, identifies contraction setups using patterns like **NR7** (the narrowest range of the last 7 days) and then trades the inevitable expansion. The core principle: volatility is mean-reverting, so extreme contraction reliably precedes explosive movement.

## Rules

### Entry Rules
1. **Contraction Identification:** Identify days where the daily range (high - low) is the narrowest of the last 7 days (**NR7 pattern**). Alternatively, look for 2+ consecutive days with [[atr]] declining and [[bollinger-bands]] squeezing.
2. **Breakout Trigger:** The next day, place a buy stop at the previous close + (X * ATR) and a sell stop at the previous close - (X * ATR). Typical X values range from 0.5 to 1.0.
3. **Volume Confirmation:** The breakout bar should have above-average [[volume]] (>1.5x the 20-day average volume).
4. **Direction Filter:** Prefer breakouts in the direction of the higher-timeframe trend. Use a 50-period [[moving-average]] on the daily chart to determine bias.
5. **One Side Only:** If the trend filter is bullish, only place the buy stop. If bearish, only the sell stop. This avoids whipsaw entries.

### Exit Rules
1. **ATR Target:** Set profit target at entry price + 2-3x ATR (for longs), capturing the expansion move.
2. **Time Exit:** If the trade hasn't reached 1R profit within 3-5 bars, the expansion has likely failed. Exit at market.
3. **Stop Loss:** Place the initial stop at the opposite side of the breakout (e.g., if long, stop at the sell stop level). Risk per trade = 2x ATR.
4. **Trailing Stop:** After 1R in profit, trail the stop using a [[chandelier-exit]] at 2x ATR from the highest close.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[atr]] | 14-period | Breakout threshold and stop/target |
| NR7 (Narrowest Range 7) | 7-day lookback | Contraction identification |
| [[bollinger-bands]] | 20, 2.0 | Visual contraction/squeeze detection |
| [[volume]] | 20-day average | Confirm breakout conviction |
| [[moving-average]] | 50-period | Trend direction filter |

## Example Trade

**Setup:** ES (S&P 500 futures) daily chart. The last 7 days show progressively narrower ranges. Today's range is 18 points -- the narrowest of the last 7 (NR7 confirmed). The 14-period ATR is 42 points. [[bollinger-bands]] are at their tightest in 30 days. Price is above the 50 SMA (bullish bias).

**Entry:** Next day, place a buy stop at yesterday's close (5,280) + 0.6 * ATR (25 points) = 5,305. The market gaps up and triggers the buy stop at 5,305.

**Management:** Stop loss at 5,280 - 0.6 * ATR = 5,255. Risk = 50 points. Target = 5,305 + (2 * 42) = 5,389. R/R = 1.68:1.

**Exit:** The expansion move takes ES to 5,395 over 3 days. Target hit. Trailing stop alternative: after reaching 5,355 (1R profit), trail stop to 5,313 (highest close minus 2x ATR).

## Performance Characteristics

- **Win Rate:** 45-55%; the strategy relies on large winners from expansion moves to offset frequent small losses
- **Best Conditions:** After prolonged consolidation (2+ weeks of declining ATR) followed by a catalyst
- **Worst Conditions:** Choppy markets that expand briefly then contract again, producing multiple small losses
- **Average Holding Period:** 1-5 days for the expansion phase
- **Edge:** The NR7 pattern identifies setups with statistical reliability; expansion after NR7 occurs ~70% of the time

## Advantages

- Grounded in the well-established principle that [[volatility]] is mean-reverting
- NR7 and similar patterns provide objective, scannable setup criteria
- Excellent risk/reward when expansion materializes -- large moves from tight stops
- Works across [[stocks]], [[futures]], and [[crypto]] markets
- Can be fully systematized and backtested with clear rules

## Disadvantages

- The direction of the breakout is uncertain; NR7 identifies **when** expansion will occur, not **which way**
- False breakouts can trigger the entry then reverse, hitting the stop
- Requires patience -- NR7 setups may only appear a few times per month per instrument
- ATR multiplier (X) needs optimization per market; crypto requires different settings than equity indices
- Overnight gaps in [[futures]] and [[stocks]] can blow past stop levels, creating slippage risk
- Not suitable for traders who need daily action; this is a setup-driven, event-triggered approach
