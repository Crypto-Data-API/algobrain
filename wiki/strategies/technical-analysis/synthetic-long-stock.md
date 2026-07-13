---
title: "Synthetic Long Stock"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, synthetic, replication, capital-efficiency, equity-options]
aliases: ["Synthetic Short Stock"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[leaps-strategies]]", "[[vertical-spreads]]", "[[risk-reversal]]", "[[delta]]", "[[gamma-scalping]]"]
---

# Synthetic Long Stock

## Overview

A Synthetic Long Stock replicates the payoff of owning 100 shares by buying an ATM [[call-option]] and selling an ATM [[put-option]] at the **same strike and expiration**. The combined position has a [[delta]] of approximately 1.0, meaning it moves dollar-for-dollar with the underlying -- just like stock. The key advantage is **capital efficiency**: instead of deploying the full share price, the trader posts only margin on the short put plus the net debit or credit of the two premiums.

The inverse -- **Synthetic Short Stock** -- reverses the legs: buy an ATM put and sell an ATM call at the same strike. This replicates a short stock position with delta of approximately -1.0, useful when shares are hard to borrow or short-sale fees are high.

## Setup

1. **Buy 1 ATM call** and **sell 1 ATM put** at the same [[strike-price]] and expiration.
2. Choose a strike nearest the current stock price. The net debit or credit should be small if [[put-call-parity|put-call parity]] holds.
3. **Expiration:** 60-180 DTE or longer to minimize frequent rolling. Shorter expirations increase [[gamma]] exposure and rolling costs.
4. Margin requirement: the short put creates an obligation, so sufficient margin or cash collateral is needed.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock rises | Gains mirror long stock (call appreciates, put decays) |
| Stock falls | Losses mirror long stock (call decays, put appreciates against you) |
| Stock flat | Minimal P&L; [[theta]] effects roughly cancel between the two legs |

**Max profit** = unlimited (to the upside). **Max loss** = substantial (stock can fall to zero, same as owning shares). **Break-even** = strike price + net debit paid.

## When to Use

- You are **capital-constrained** and want stock-like exposure without tying up the full purchase price.
- The underlying is **hard to borrow** (for the synthetic short variant) or has high borrowing costs.
- You want to establish a position quickly with options [[liquidity]] while the stock has wide bid-ask spreads.
- Useful as a component inside more complex structures like [[risk-reversal]] trades.

## Advantages
- Dramatically less capital required compared to buying shares outright
- Identical payoff profile to long stock (or short stock for the inverse)
- No borrowing fees for the synthetic short variant
- Can be combined with other option legs for advanced strategies

## Disadvantages
- **Margin requirements** on the short put can still be significant
- Subject to [[assignment]] risk on the short leg, especially near [[ex-dividend]] dates
- Must be rolled at expiration, incurring transaction costs and potential slippage
- Does not receive [[dividends]] -- an important gap versus actual stock ownership
- Two-leg structure means wider total bid-ask spread than a single stock trade

## See Also
- [[leaps-strategies]] -- another capital-efficient stock replacement approach
- [[risk-reversal]] -- closely related structure, often used as a directional volatility trade
- [[vertical-spreads]] -- defined-risk alternatives for directional bets
