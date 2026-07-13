---
title: "Synthetic Long"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, synthetic, replication, leverage, equity-options, undefined-risk]
aliases: ["Synthetic Short"]
strategy_type: quantitative
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[collar]]", "[[risk-reversal]]", "[[leaps-strategies]]", "[[covered-call]]", "[[delta]]"]
---

# Synthetic Long

## Overview

A Synthetic Long replicates the profit-and-loss profile of owning 100 shares by buying an ATM [[call-option]] and selling an ATM [[put-option]] at the **same strike and expiration**. The combined position has a [[delta]] of approximately +100, identical to holding the shares, but requires far less capital because you never purchase the stock. The mirror image -- selling the call and buying the put at the same strike -- creates a **Synthetic Short**, which replicates a short stock position. Synthetics are widely used to gain directional exposure when capital efficiency matters or when borrowing shares for a short sale is difficult.

## Setup

1. **Buy 1 ATM call** at the strike nearest the current stock price.
2. **Sell 1 ATM put** at the same strike and expiration.
3. **Expiration:** 60-120 DTE gives time for the thesis to play out while keeping [[theta]] manageable.
4. Net cost is typically close to zero (slight debit or credit depending on skew and interest rates).
5. For the **Synthetic Short**, reverse the legs: sell the call, buy the put.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock rises above strike | Profit mirrors owning shares; call gains, put expires worthless |
| Stock stays at strike | Both options expire near zero; minimal gain or loss |
| Stock falls below strike | Loss mirrors owning shares; short put incurs loss |

**Max profit** = unlimited (stock can rise without limit). **Max loss** = substantial (stock can fall to zero). **Break-even** = strike price + net debit (or minus net credit).

## When to Use

- You want **long stock exposure** without tying up capital to buy 100 shares outright.
- Shares are hard to borrow and you need a synthetic short instead of a traditional short sale.
- You want to quickly establish a delta-equivalent position for hedging or [[pairs-trading]].
- You expect a strong directional move and prefer the capital efficiency of options.

## Advantages
- Replicates stock ownership at a fraction of the capital outlay
- Near-zero or zero net cost at inception
- Delta of +100 (or -100 for synthetic short) matches share-for-share exposure
- Avoids the borrow costs and locate issues associated with short selling

## Disadvantages
- The short put leg carries significant downside risk and requires margin
- No [[dividend]] income since you do not own the actual shares
- [[pin-risk|Pin risk]] near expiration can result in unwanted assignment on the short leg
- Less liquid strikes or wide bid-ask spreads can increase execution cost

## See Also
- [[risk-reversal]] -- closely related structure sometimes used synonymously
- [[leaps-strategies]] -- another capital-efficient way to gain long exposure
- [[collar]] -- adds protection to a synthetic or real stock position
- [[covered-call]] -- requires actual share ownership unlike the synthetic
