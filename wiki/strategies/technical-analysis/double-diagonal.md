---
title: "Double Diagonal"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, double-diagonal, diagonal-spread, income, range-bound, advanced, time-decay]
strategy_type: quantitative
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[diagonal-spread]]", "[[calendar-spread]]", "[[iron-condor]]", "[[theta]]"]
---

# Double Diagonal

## Overview

The Double Diagonal combines a diagonal call spread and a diagonal put spread into a single position. The trader sells short-term OTM options on both sides (a call above and a put below the current price) and buys longer-dated options at different strikes as a hedge. This structure blends **directional flexibility** with **time decay income**: the short-dated options decay rapidly while the longer-dated wings retain value. It functions like a wider, more flexible [[iron-condor]] with the added dimension of differing expirations across the short and long legs.

## Setup

1. **Sell 1 short-term OTM call** (front-month, 30-45 DTE) above the current price.
2. **Buy 1 longer-term OTM call** (back-month, 60-90 DTE) at a higher strike.
3. **Sell 1 short-term OTM put** (same front-month expiration) below the current price.
4. **Buy 1 longer-term OTM put** (same back-month expiration) at a lower strike.
5. Net result is typically a small debit or near-neutral cost at entry. The short legs generate [[theta]] income; the long legs define risk.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock stays between short strikes | Short options decay; long options retain value; maximum profit zone |
| Stock drifts toward one short strike | One side under pressure; the other decays favorably; partial profit |
| Stock breaks past a long strike | Loss on that side; long option limits the damage; defined risk |

**Max profit** is realized when the stock sits between the two short strikes at front-month expiration. **Max loss** is limited by the long-dated wings, though exact figures depend on the time remaining on the long legs.

## When to Use

- You expect the stock to be **range-bound** in the near term but want flexibility to adjust if it drifts.
- You want [[theta]] income from selling short-term options while maintaining longer-dated protection.
- You prefer a wider profit zone and more adjustment opportunities than a standard [[iron-condor]].
- You are comfortable managing a **four-leg, two-expiration** structure.

## Advantages
- Wider profit zone than an iron condor due to the calendar-like time spread component
- Defined risk through the longer-dated protective wings
- The surviving long options retain value after front-month expiration, allowing follow-up trades
- Flexible to adjust -- short legs can be rolled to new strikes or expirations

## Disadvantages
- Complex four-leg structure with two different expirations -- harder to manage and analyze
- Wider bid-ask spreads on four simultaneous legs increase execution cost
- Profit profile is non-linear and harder to visualize than simpler strategies
- Requires active management: rolling short legs, monitoring both expirations, adjusting as the stock moves
- [[vega]] risk cuts both ways -- an IV spike helps long legs but hurts profitability if you need to close early

## See Also
- [[diagonal-spread]] -- the single-side building block of the double diagonal
- [[calendar-spread]] -- a simpler time-spread structure at a single strike
- [[iron-condor]] -- a similar range-bound income strategy with same-expiration legs
