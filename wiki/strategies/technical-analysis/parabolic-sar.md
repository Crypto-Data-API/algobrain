---
title: "Parabolic SAR"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [trend-following, trailing-stop, parabolic-sar, welles-wilder, technical-analysis]
aliases: ["Parabolic Stop and Reverse", "PSAR", "Parabolic SAR Strategy"]
strategy_type: technical
timeframe: scalp|intraday|swing
markets: [stocks, crypto, forex]
complexity: beginner
backtest_status: untested
related: ["[[atr]]", "[[supertrend]]", "[[moving-average-crossover]]", "[[adx]]", "[[j-welles-wilder]]"]
---

# Parabolic SAR

## Overview

The Parabolic SAR (Stop and Reverse) was created by J. Welles Wilder Jr. and introduced in his 1978 book *New Concepts in Technical Trading Systems* alongside the [[rsi]] and [[adx]]. The indicator places dots above or below price to indicate the current trend direction. When dots are below price, the trend is bullish; when above, bearish. The "parabolic" name comes from the parabolic curve the dots trace as they accelerate toward price over time.

The key innovation is the **Acceleration Factor (AF)**, which starts at 0.02 and increases by 0.02 each time a new extreme point (highest high or lowest low) is made, up to a maximum of 0.20. This causes the SAR to tighten progressively, acting as an increasingly aggressive [[trailing-stop]]. When price finally touches the SAR, the system reverses direction -- it is always in the market, either long or short.

## Rules

### Entry
1. **Long Entry:** The SAR flips from above price to below price (dots move below candles). This occurs when the previous downtrend's SAR is hit and the indicator reverses.
2. **Short Entry:** The SAR flips from below price to above price (dots move above candles).
3. **Filter (recommended):** Only take signals in the direction of the larger trend. Use [[adx]] > 25 to confirm a trending market, or a longer-term [[moving-average-crossover|moving average]] as a directional filter.

### Exit
1. **SAR Reversal:** The default exit is when the SAR flips to the opposite side -- this simultaneously closes the current position and opens the reverse.
2. **Partial Exit:** Take partial profits at a fixed target (e.g., 2x [[atr]]) and let the remainder ride with the SAR as a trailing stop.
3. **Non-reversal Mode:** Some traders only use SAR as an exit/trailing stop, not as an entry trigger. Enter via another system, then use SAR dots to trail the stop.

### Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| AF Start | 0.02 | Initial acceleration factor |
| AF Increment | 0.02 | Step increase per new extreme |
| AF Maximum | 0.20 | Cap on acceleration factor |

Increasing AF Start/Increment makes the SAR tighter and more sensitive (more signals, more whipsaws). Decreasing them makes it looser (fewer signals, later exits).

## Indicators Used
- **Parabolic SAR** (core indicator)
- [[adx]] to confirm trending conditions (ADX > 25)
- [[atr]] for additional stop-loss calibration
- [[volume]] for entry confirmation

## Example Trade
**Asset:** ETH/USD, 4-hour chart
1. ETH is in a downtrend with SAR dots above price. ETH bottoms at $2,800.
2. Price rallies through the SAR dots. The SAR flips to below price at $2,870. Enter long.
3. ADX reads 32, confirming a trending environment. Proceed with the trade.
4. Over the next 3 days, SAR dots trail below price: $2,850, $2,860, $2,880, $2,920, $2,970 (accelerating).
5. ETH reaches $3,200 then reverses. SAR has accelerated to $3,100. Price hits $3,100, triggering the exit.
6. **Result:** Entry $2,870, exit $3,100 = +$230 per ETH (8.0% gain).

## Performance Characteristics
- **Win Rate:** 30-40% in all conditions; 50-55% when filtered with ADX or another trend filter.
- **Profit Factor:** 1.2-1.8. The tightening SAR captures a meaningful portion of trends but gives back profits quickly on reversal.
- **Best Market Conditions:** Strong, sustained trends with clear directional momentum. Works well in crypto and forex trends.
- **Worst Market Conditions:** Choppy, sideways, low-ADX markets. The SAR will flip constantly, generating whipsaw after whipsaw.

## Advantages
- Visual simplicity -- dots above or below price are immediately intuitive
- Built-in trailing stop that automatically tightens as the trend progresses
- Always provides a clear stop level (the current SAR value)
- The acceleration factor rewards strong trends by keeping you in longer
- Works on any timeframe from 1-minute scalping to daily swing trading

## Disadvantages
- **Choppy market killer:** In range-bound markets, SAR flips constantly, producing a string of small losses
- **Always-in-market design** means you are perpetually positioned, which may not suit all traders
- **Lagging on trend start:** The first few SAR dots after a flip are far from price, creating wide initial risk
- No built-in volume or momentum confirmation -- should be combined with other indicators
- The fixed AF parameters may not suit all instruments equally

## Backtesting Evidence

One illustrative backtesting study across US equities reported Parabolic SAR with a 44.7% win rate. As a trend-following/exit system, SAR is designed to capture large trending moves while accepting frequent small losses during choppy conditions. The value lies in its risk/reward ratio rather than win rate (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## See Also
- [[supertrend]] -- a modern ATR-based alternative that serves a similar trailing-stop function
- [[adx]] -- Wilder's companion indicator for measuring trend strength (essential SAR filter)
- [[atr]] -- another Wilder creation, useful for calibrating stops alongside SAR
- [[trailing-stop]] -- the general concept SAR implements
- [[moving-average-crossover]] -- a slower but less whipsaw-prone trend-following approach
- [[j-welles-wilder]] -- Parabolic SAR's creator, from the same 1978 book as RSI and ADX
