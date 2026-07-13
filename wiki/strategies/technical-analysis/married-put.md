---
title: "Married Put"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, hedging, protective-put, married-put, insurance, equity-options, defined-risk]
aliases: ["Protective Put"]
strategy_type: quantitative
markets: [stocks]
complexity: beginner
backtest_status: untested
related: ["[[collar]]", "[[covered-call]]", "[[leaps-strategies]]", "[[vertical-spreads]]", "[[implied-volatility]]"]
---

# Married Put

## Overview

A Married Put (also called a **Protective Put**) pairs a long stock position with a purchased ATM [[put-option]]. It functions as insurance: the put guarantees a minimum exit price for the shares, capping the maximum loss at the difference between the stock price and the [[strike-price]] plus the [[premium]] paid. Unlike a [[collar]], no call is sold, so upside remains **unlimited**. The trade-off is straightforward -- you pay a premium for downside peace of mind.

## Setup

1. **Own 100 shares** (or buy shares and the put simultaneously -- hence "married").
2. **Buy 1 ATM put** for maximum protection, or 1 slightly OTM put (2-5% below current price) to reduce cost.
3. **Expiration:** 30-90 DTE for short-term event hedging; use [[leaps-strategies]] puts for multi-month coverage.
4. Purchase when [[implied-volatility]] is low to minimize insurance cost.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock drops below put strike | Put gains offset stock losses; max loss locked in |
| Stock stays flat | Lose the put premium; shares unchanged |
| Stock rallies | Unlimited upside minus premium paid |

**Max loss** = (stock price - put strike) + premium paid. **Max profit** = unlimited. **Break-even** = stock entry price + premium paid.

## When to Use

- Holding a concentrated position through a high-risk event (earnings, FDA decision, macro shock).
- You are **bullish long-term** but want a safety net for the next 1-3 months.
- [[implied-volatility]] is low, making puts affordable.
- You prefer simplicity over the capped-upside structure of a [[collar]].

## Advantages
- Unlimited upside potential -- no cap on gains unlike the collar
- Maximum loss is defined and known at entry
- Extremely simple to understand and execute -- ideal for beginners
- Can be applied to any stock position at any time

## Disadvantages
- The put [[premium]] is a direct cost that reduces returns if the stock rises or stays flat
- [[theta]] decay erodes the put's value daily -- time works against you
- Repeated use over many cycles significantly drags long-term performance
- In high-[[implied-volatility]] environments the insurance premium can be prohibitively expensive

## See Also
- [[collar]] -- adds a sold call to offset the put's cost
- [[covered-call]] -- generates income instead of buying protection
- [[leaps-strategies]] -- long-dated puts for extended protection
- [[bear-put-spread]] -- a cheaper defined-risk bearish alternative
