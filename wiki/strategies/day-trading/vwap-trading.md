---
title: VWAP Trading Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - vwap
  - intraday
  - institutional
  - fair-value
  - anchored-vwap
  - day-trading
strategy_type: scalping
timeframe: intraday
markets:
  - stocks
  - futures
  - crypto
complexity: intermediate
backtest_status: untested
related:
  - "[[scalping]]"
  - "[[order-flow-scalping]]"
  - "[[opening-range-breakout]]"
  - "[[support-resistance-breakout]]"
---

# VWAP Trading Strategy

## Overview

The Volume Weighted Average Price ([[vwap]]) represents the **average price an instrument has traded at throughout the session, weighted by volume**. It serves as the intraday **fair value benchmark** used by institutional traders to evaluate execution quality. If a fund buys below VWAP, they got a good fill; above VWAP, they overpaid. This institutional behavior creates a gravitational pull around VWAP, making it a powerful level for intraday trading. The strategy buys **below VWAP when the broader trend is bullish** (price is undervalued relative to the session average) and sells **above VWAP when the trend is bearish**. **Anchored VWAP** -- calculated from a specific event (earnings, gap, pivot high/low) rather than session start -- extends the concept to multi-day analysis and provides dynamic support/resistance levels that professional traders closely monitor.

## Rules

### Entry Rules
1. **VWAP Bounce (Mean Reversion):** In an uptrending market (price above VWAP for most of the session), buy when price pulls back **to or slightly below VWAP** and shows a rejection candle (e.g., [[hammer]], [[bullish-engulfing]]). VWAP acts as dynamic support.
2. **VWAP Rejection (Trend Continuation Short):** In a downtrending session (price below VWAP), sell when price rallies **to or slightly above VWAP** and rejects with a bearish candle. VWAP acts as dynamic resistance.
3. **VWAP Breakout:** If price opens below VWAP and then breaks decisively above it with strong [[volume]], enter long -- the session character has shifted from bearish to bullish. The converse applies for shorts.
4. **VWAP Standard Deviation Bands:** Use +1 and +2 standard deviation bands above and below VWAP as overbought/oversold zones. Fade trades at the +2/-2 bands when the trend is range-bound.
5. **Anchored VWAP Entry:** Anchor VWAP from a major event (earnings release, significant gap, multi-week high/low). When current price retests the anchored VWAP from that event, it acts as a key support/resistance level.

### Exit Rules
1. **Opposite Band Exit:** If entering at VWAP on a bounce, target the +1 standard deviation band. If entering at the -2 band, target VWAP as the mean reversion destination.
2. **End-of-Day Close:** VWAP resets each session. Close all VWAP-based positions before the session ends (typically by 15:45 for US equities).
3. **Stop Loss:** Place stops 0.5-1x [[atr]](14, on 5-min chart) beyond VWAP. If price closes a full candle beyond VWAP against your position, the VWAP as support/resistance has failed.
4. **VWAP Cross Exit:** If you are long and price closes below VWAP on increasing volume, exit. The institutional benchmark has shifted against you.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[vwap]] | Session (standard) | Intraday fair value / mean |
| VWAP Standard Deviation Bands | +/- 1, 2 SD | Overbought/oversold zones |
| Anchored VWAP | From key events | Multi-day dynamic support/resistance |
| [[volume]] | Per bar | Confirm conviction at VWAP tests |
| [[atr]] | 14-period (5-min) | Stop loss sizing |
| [[moving-average]] (9 EMA) | 5-min chart | Short-term trend direction |

## Example Trade

**Setup:** MSFT 5-minute chart. The market opened gap-up on strong earnings. MSFT opened at $435 and rallied to $440 in the first hour. Session VWAP is at $437.50. Price pulls back to $437.80 (just above VWAP) at 10:45 AM. The overall session trend is bullish (price has been above VWAP since 9:40 AM).

**Entry:** A [[bullish-engulfing]] candle forms at $437.60, bouncing off VWAP. Enter long at $438.00. Volume on the bounce candle is 1.8x the 20-bar average.

**Management:** Stop loss at $436.50 (below VWAP by 0.7x 5-min ATR). Risk = $1.50. Target at the +1 VWAP standard deviation band at $441.00. R/R = 2:1.

**Exit:** Price rallies back to $441.00 by 12:30 PM. Target hit, close position. Alternatively, if price had broken below VWAP and closed a full 5-min candle at $436.80, exit for a $1.20 loss.

## Performance Characteristics

- **Win Rate:** 55-65% on VWAP bounce trades in trending sessions; lower (40-50%) on range-bound days where VWAP gets chopped through repeatedly
- **Best Conditions:** Strong trending sessions where price respects VWAP as support (uptrend) or resistance (downtrend) throughout the day
- **Worst Conditions:** Choppy, rotational days where price crosses VWAP 10+ times, generating whipsaws
- **Average Holding Period:** 15 minutes to 3 hours
- **Key Filter:** The first VWAP touch/bounce of the session is the highest probability setup; subsequent touches have diminishing reliability

## Advantages

- VWAP is the **institutional benchmark** -- aligning with how the largest market participants evaluate price gives a structural edge
- Provides a clear, objective, and dynamically updating support/resistance level throughout the day
- Anchored VWAP extends the concept beyond intraday, providing multi-day institutional reference points
- Works on all liquid instruments: stocks, [[futures]], [[crypto]]
- Standard deviation bands provide built-in overbought/oversold framework without additional indicators
- Combines naturally with [[order-flow-scalping]] and [[opening-range-breakout]] strategies

## Disadvantages

- VWAP is **session-specific** and resets daily, limiting its use for [[swing-trading]] or longer timeframes (use anchored VWAP instead)
- On choppy days, price crosses VWAP repeatedly, generating many false signals and whipsaws
- VWAP is a lagging indicator -- it reflects the average of past prices, not future direction
- In low-volume premarket or afterhours sessions, VWAP calculations are unreliable due to thin participation
- VWAP is most useful in the first half of the session; by the afternoon, it becomes very slow-moving and less actionable
- The strategy requires real-time charting with VWAP overlay capability (most platforms support this, but some free tools do not include standard deviation bands)
- Because VWAP is widely watched, obvious levels can attract [[stop-hunting]] and liquidity grabs
