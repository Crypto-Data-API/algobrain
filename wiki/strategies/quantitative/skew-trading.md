---
title: "Skew Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, skew, volatility-surface, implied-volatility, quantitative, vol-trading]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[implied-volatility]]", "[[risk-reversal]]", "[[ratio-spread]]", "[[vix-trading]]", "[[garch-volatility]]", "[[gamma-scalping]]"]
---

# Skew Trading

## Overview

Skew Trading exploits the **implied volatility skew** -- the phenomenon where OTM puts trade at higher [[implied-volatility]] than equivalent OTM calls because market participants pay a premium for crash insurance. Skew traders **sell expensive skew and buy cheap skew**, capturing the premium differential when skew mean-reverts or proves overpriced relative to realized outcomes.

The strategy requires deep understanding of the [[volatility]]-surface. Traders analyze skew using metrics like the 25-delta risk reversal (IV of 25-delta call minus IV of 25-delta put) and compare current skew to historical norms.

## Setup

### Risk Reversal (Sell Skew)
1. **Sell 1 OTM put** (expensive side, e.g., 25-delta) + **buy 1 OTM call** (cheap side, e.g., 25-delta) at the same expiration.
2. Net credit if skew is steep (put IV >> call IV). Profits if skew flattens or the stock rallies.

### Ratio Spread (Exploit Skew)
1. **Buy 1 ATM put** + **sell 2 OTM puts** further down the chain. Elevated skew on OTM puts finances the ATM put.
2. Profits if the stock declines moderately; risk below the lower short strike.

### Skew Mean-Reversion
1. Monitor the 25-delta risk reversal over time. When skew reaches historical extremes (e.g., >2 standard deviations), fade it.
2. Sell the rich side, buy the cheap side, and wait for normalization. Delta-hedge to isolate pure skew exposure.

## Payoff Profile

| Scenario | Risk Reversal Outcome | Ratio Spread Outcome |
|---|---|---|
| Skew flattens (normalizes) | Profit as put IV drops relative to call IV | Profit from OTM put IV decline |
| Stock rallies | Call gains value, put expires OTM; profit | ATM put loses, OTM puts expire; mixed |
| Stock crashes | Short put goes deep ITM; significant loss | Risk below lower strike; potential large loss |
| Skew steepens further | Loss as the expensive side gets more expensive | Short OTM puts increase in value; loss |

## When to Use

- Implied [[volatility]] skew is at **historical extremes** -- puts are disproportionately expensive relative to calls.
- You have quantitative tools to measure skew (25-delta RR, skew index) and compare to historical distributions.
- You want to express a view on **relative volatility** rather than direction or absolute vol levels.
- After a sharp market decline when fear-driven put buying has pushed skew to extreme levels.

## Advantages
- Captures a well-documented and persistent [[volatility]] premium (put overpricing)
- Can be structured as delta-neutral, isolating pure skew exposure
- Multiple implementation methods ([[risk-reversal]], [[ratio-spread]], butterfly adjustments)
- The skew premium has historically mean-reverted, providing a statistical edge

## Disadvantages
- **Tail risk:** selling puts into a crash is the exact wrong time; skew is expensive for a reason
- Requires sophisticated vol-surface analytics -- not a strategy for visual chart traders
- Delta-hedging costs can erode the skew premium, especially in volatile markets
- Timing is difficult; skew can remain elevated far longer than expected before normalizing

## See Also
- [[implied-volatility]] -- the foundation of all skew analysis
- [[risk-reversal]] -- the primary instrument for expressing skew views
- [[ratio-spread]] -- an alternative structure for harvesting skew premium
- [[vix-trading]] -- related volatility strategies using the VIX complex
