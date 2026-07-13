---
title: "Protective Put"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, risk-management, hedging]
aliases: ["Protective Puts", "Married Put"]
related: ["[[put-options|put-option]]", "[[hedging]]", "[[covered-call]]", "[[risk-management-overview|risk-management]]"]
strategy_type: technical
timeframe: position
markets: [stocks, options]
complexity: beginner
backtest_status: untested
---

# Protective Put

A **protective put** (also called a married put) involves buying a [[put-options|put option]] on a stock you already own, providing insurance against downside risk while preserving unlimited upside potential. It is the options equivalent of buying an insurance policy on your portfolio.

## Overview

The protective put is one of the simplest and most intuitive options strategies. The trader holds long shares and simultaneously purchases a put option at or below the current stock price. If the stock falls below the put's [[strike-price]], the put gains value dollar-for-dollar, effectively creating a floor on losses. If the stock rises, the trader participates fully in the upside (minus the cost of the put premium).

The total cost of protection equals the put premium paid. This premium acts as a deductible -- the maximum loss on the combined position is: **(stock purchase price - put strike price) + premium paid**.

## Rules

### Entry
1. **Own shares** of the underlying stock (or buy them simultaneously -- the "married put" variant).
2. **Buy a put option** with a strike at or slightly below the current stock price. ATM puts provide maximum protection but cost more; OTM puts are cheaper but leave a gap of unprotected downside.
3. **Choose expiration** based on how long you need protection. Longer-dated puts cost more but provide coverage over a greater time horizon.

### Risk Profile
- **Maximum loss**: (stock price - strike price) + premium paid
- **Maximum gain**: Unlimited (stock can rise indefinitely; put expires worthless)
- **Breakeven**: Stock purchase price + premium paid

### Exit
- If the stock rises: let the put expire worthless and keep the shares. The put premium is the cost of insurance.
- If the stock falls: exercise the put to sell shares at the strike price, or sell the put for its intrinsic value and reassess the stock position.

## Comparison with Covered Calls

The protective put and [[covered-call]] represent opposite risk profiles:

| | Protective Put | Covered Call |
|---|---|---|
| **Cost** | Costs premium (debit) | Collects premium (credit) |
| **Upside** | Unlimited | Capped at strike |
| **Downside** | Protected below strike | Reduced by premium only |
| **Best for** | Hedging, volatile markets | Income, sideways markets |

## When to Use

- Before earnings announcements or major events when you want to hold shares but fear a large drop
- In volatile or uncertain markets where drawdown protection is worth the premium cost
- For long-term holders who want to stay invested but need temporary insurance
- Portfolio-level hedging by buying puts on an index ETF

## Limitations

- The put premium is a recurring cost that reduces overall returns in bull markets
- [[theta|Theta decay]] erodes the put's value daily, making ongoing protection expensive
- In practice, rolling protective puts quarter after quarter can significantly drag on returns (often 3-5% annually)

## Related Strategies

- [[covered-call]] -- opposite approach: sells upside for income instead of buying downside protection
- [[collar]] -- combines a protective put with a covered call to finance the put premium
- [[cash-secured-put]] -- sells puts with intent to acquire stock at lower prices

## Sources

- (Source: [[book-option-volatility-and-pricing]])
