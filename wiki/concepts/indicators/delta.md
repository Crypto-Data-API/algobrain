---
title: "Delta"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, derivatives, delta]
aliases: ["Option Delta", "Delta Hedging"]
related: ["[[options-greeks]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[black-scholes]]", "[[delta-neutral]]", "[[implied-volatility]]", "[[options]]"]
domain: [derivatives, risk-management]
difficulty: intermediate
---

**Delta** measures how much an option's price changes for a $1 move in the underlying asset. It is the most intuitive of the [[options-greeks]] and serves multiple roles: a measure of directional exposure, a hedge ratio, and a rough proxy for the probability of an option expiring in-the-money.

## Overview

Delta is expressed as a number between -1 and +1 (or equivalently, -100 to +100 in some conventions):

- **Call options** have delta between 0 and +1. A deep in-the-money call approaches +1.0 (moves dollar-for-dollar with the stock). A far out-of-the-money call approaches 0.
- **Put options** have delta between -1 and 0. A deep in-the-money put approaches -1.0. A far out-of-the-money put approaches 0.
- **At-the-money options** have delta near +0.50 (calls) or -0.50 (puts).

Delta is the first partial derivative of the option price with respect to the underlying price in the [[black-scholes]] framework. It is the most heavily monitored Greek in professional trading, as it directly determines how much a portfolio gains or loses from a move in the underlying.

## How It Works

### Delta as Directional Exposure

A portfolio's total delta measures its net directional exposure. For example:

- **Long 100 shares of stock**: Delta = +100
- **Long 1 ATM call (50 delta)**: Equivalent directional exposure to ~50 shares
- **Long 1 ATM put (-50 delta)**: Equivalent to being short ~50 shares

Traders express positions in "delta terms" to compare apples to apples. A portfolio with +200 delta behaves roughly like being long 200 shares of the underlying for small price changes.

### Delta as Probability Proxy

Delta roughly approximates the market's implied probability that the option expires in-the-money. A 30-delta call has approximately a 30% chance of expiring ITM; a 70-delta call has approximately a 70% chance. This is an approximation, not an exact equivalence, but it is widely used for strike selection:

- **High-probability trades**: Sell options at low delta (e.g., 10-15 delta) for a high probability of expiring worthless
- **Directional trades**: Buy options at 40-60 delta for meaningful directional exposure
- **Deep ITM substitutes**: Buy 80-90 delta options as stock replacement strategies with less capital

### Delta Hedging

[[delta-neutral]] positioning means constructing a portfolio with zero net delta -- no directional exposure. Market makers and institutional traders continuously delta-hedge their options inventory:

1. Sell a call option (negative delta)
2. Buy shares of stock to offset (positive delta)
3. As the stock moves, delta changes (due to [[gamma]]), requiring rebalancing

This process of continuous rebalancing is called **dynamic delta hedging** and is the practical foundation of options pricing theory. The [[black-scholes]] model assumes perfect, continuous delta hedging -- which is impossible in practice due to transaction costs and discrete trading.

### How Delta Changes

Delta is not static. It shifts based on:

- **Underlying price**: As the stock rises, call deltas increase toward 1.0 and put deltas increase toward 0. This rate of change is measured by [[gamma]].
- **Time to expiration**: As expiration nears, ITM options see delta approach 1.0 (or -1.0 for puts) and OTM options see delta approach 0. ATM options remain near 0.50 until very close to expiration, when they snap toward 0 or 1.
- **Implied volatility**: Higher [[implied-volatility]] "spreads out" delta, making deep ITM and OTM options have deltas closer to 0.50. Lower IV makes delta more binary (closer to 0 or 1).

## Trading Applications

- **Position sizing**: Traders use delta to normalize position sizes. Instead of "I own 5 calls," they think "I have 250 delta of exposure" -- comparable to 250 shares.
- **Strike selection**: Delta guides strike selection for various strategies. Income sellers often choose 15-30 delta strikes. Directional traders favor 40-60 delta. Stock replacement uses 70-90 delta.
- **Portfolio management**: Aggregating delta across a portfolio of options, stock, and futures reveals total directional exposure. Professional traders set delta limits per position and per portfolio.
- **Hedging**: Delta tells you exactly how many shares (or futures contracts) to buy or sell to neutralize the directional risk of an options position.
- **Risk assessment**: A position's delta tells you the immediate P&L impact of a $1 move. A +500 delta portfolio gains ~$500 on a $1 up move and loses ~$500 on a $1 down move.

## Related

- [[options-greeks]]
- [[gamma]]
- [[theta]]
- [[vega]]
- [[delta-neutral]]
- [[black-scholes]]
- [[implied-volatility]]
- [[options]]

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg's treatment of delta as both a hedge ratio and probability measure is the industry-standard reference
