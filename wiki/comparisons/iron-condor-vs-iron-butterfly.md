---
title: Iron Condor vs Iron Butterfly
type: comparison
created: 2026-04-07
updated: 2026-04-07
status: good
tags:
  - options
  - premium-selling
  - defined-risk
subjects:
  - "[[iron-condor]]"
  - "[[iron-butterfly]]"
comparison_dimensions:
  - structure
  - profit-zone
  - premium
  - risk-reward
  - vol-environment
  - adjustments
  - probability
related:
  - "[[theta-decay]]"
  - "[[implied-volatility]]"
  - "[[options-greeks]]"
---

# Iron Condor vs Iron Butterfly

## Overview

The [[iron-condor]] and [[iron-butterfly]] are both defined-risk, premium-selling strategies designed to profit when a stock stays within a range. They share the same four-leg structure (two spreads, one call side and one put side) but differ in where the short strikes are placed. The iron condor uses out-of-the-money short strikes, creating a wider profit zone with less premium. The iron butterfly uses at-the-money short strikes, creating a narrower profit zone with more premium. This single difference drives every tradeoff between them.

## Comparison Table

| Dimension | Iron Condor | Iron Butterfly |
|-----------|------------|----------------|
| **Structure** | Short OTM put + long further OTM put, short OTM call + long further OTM call | Short ATM put + short ATM call (straddle) + long OTM put + long OTM call (wings) |
| **Short Strike Placement** | Out of the money on both sides | At the money on both sides (same strike) |
| **Profit Zone Width** | Wide (between the two short strikes) | Narrow (centered on the ATM strike) |
| **Max Profit** | Net credit received (lower amount) | Net credit received (higher amount) |
| **Max Loss** | Width of one spread minus credit | Width of one spread minus credit |
| **Probability of Profit** | Higher (55-75% typical) | Lower (30-45% typical) |
| **Theta Decay** | Slower (OTM options decay slower initially) | Faster (ATM options have highest theta) |
| **Vega Exposure** | Lower (OTM options have less vega) | Higher (ATM options have maximum vega) |
| **Adjustment Ease** | Easier (more room before threatened) | Harder (any move threatens profitability) |
| **Best Vol Environment** | High IV (premium inflated across strikes) | High IV (maximum ATM premium to collect) |
| **Break-Even Width** | Wider (short strikes +/- credit) | Narrower (ATM strike +/- credit) |

## Key Differences

**Risk/reward tradeoff.** The iron condor collects less premium but wins more often. The iron butterfly collects more premium but requires the stock to stay very close to one price. A typical iron condor might collect $1.50 with a 65% win rate. A comparable iron butterfly might collect $4.00 with a 35% win rate. Over many trades, expected value can be similar, but the experience is very different.

**Theta dynamics.** Iron butterflies benefit from faster [[theta-decay]] because at-the-money options have the highest theta. This means an iron butterfly generates income faster in the early days of the trade. Iron condors start with slower theta decay that accelerates as expiration approaches, assuming the stock stays between the short strikes.

**Vega sensitivity.** Because ATM options have the highest vega, iron butterflies are more sensitive to changes in [[implied-volatility]]. A spike in IV after entering an iron butterfly can cause an immediate unrealized loss, even if the stock price has not moved. Iron condors are less exposed to IV changes because OTM options have lower vega.

**Management and adjustments.** Iron condors give you breathing room. The stock can move significantly before either short strike is threatened. This makes them easier to manage and adjust. Iron butterflies are immediately sensitive to any price movement, requiring more active management and faster adjustment decisions.

**Profit realization.** Iron condors often reach max profit near expiration as both OTM options expire worthless. Iron butterflies rarely reach max profit because that requires the stock to pin exactly at the short strike at expiration. Most iron butterfly traders target 25-50% of max profit and close early.

## When to Use Each

**Use iron condors when:**
- You expect the stock to stay within a broad range
- You prefer higher probability trades with less management
- IV is elevated but you want moderate vega risk
- You are newer to options selling (more forgiving)
- You want to set the trade and check it once daily

**Use iron butterflies when:**
- You have a strong conviction the stock will stay near a specific price
- You want to maximize premium collected per trade
- You are comfortable with lower win rates and active management
- Earnings or events have inflated IV and you expect a pin
- You plan to take profits early (25-50% of max credit)

## Verdict

For most traders, the iron condor is the better default choice. Its wider profit zone, higher probability, and easier management make it more forgiving and less stressful. The iron butterfly is a specialized tool best used when you have high conviction on a price target or when IV is extremely elevated and you want to maximize premium capture. Think of the iron condor as the everyday workhorse and the iron butterfly as the precision instrument you deploy in specific situations.
