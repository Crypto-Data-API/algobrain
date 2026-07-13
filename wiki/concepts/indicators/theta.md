---
title: "Theta"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, derivatives, theta]
aliases: ["Time Decay", "Theta Decay", "Option Time Decay", "theta-decay", "time-decay"]
related: ["[[options-greeks]]", "[[gamma]]", "[[delta]]", "[[vega]]", "[[implied-volatility]]", "[[iron-condor]]", "[[covered-call]]", "[[wheel-strategy]]", "[[black-scholes]]"]
domain: [derivatives, risk-management]
difficulty: intermediate
---

**Theta** measures the rate at which an option's price declines as time passes, with all other factors held constant. Often called "time decay," theta represents the daily cost of owning an option -- or equivalently, the daily income earned by selling one. It is one of the most important [[options-greeks]] for income-oriented strategies.

## Overview

Every option is a wasting asset. As expiration approaches, the probability of a large favorable move diminishes, and the "optionality" embedded in the contract loses value. Theta quantifies this erosion. For example, if an option has a theta of -0.05, it will lose approximately $0.05 per day (or $5 per contract) in value, assuming no change in the underlying price or [[implied-volatility]].

Theta is a central concept in options trading because it creates a fundamental asymmetry: option buyers pay theta to maintain their positions, while option sellers collect theta as compensation for the risks they assume. This dynamic is why many professional options strategies -- such as [[iron-condor]], [[covered-call]], [[credit-spread]], and [[wheel-strategy]] -- are structured to be net theta-positive (collecting time decay).

## How It Works

### Mathematical Definition

Theta is the partial derivative of the option's price with respect to time:

**Theta = dV/dT**

where V is the option value and T is time to expiration. In the [[black-scholes]] model, theta is always negative for long options (both calls and puts), reflecting the guaranteed erosion of extrinsic value over time.

### Theta Acceleration

Theta decay is not linear -- it accelerates as expiration approaches. This is one of the most important practical facts about options:

- **Far from expiration (60+ days)**: Theta is relatively small. An at-the-money option might lose only a few cents per day.
- **30-45 days to expiration**: Theta begins to increase noticeably. Many income traders sell options in this window to capture the steepest part of the decay curve.
- **Final 2 weeks**: Theta accelerates sharply, especially for at-the-money options. The last week can see dramatic daily losses for option holders.
- **Final day**: Remaining extrinsic value collapses to zero by the close of trading on expiration day.

This non-linear decay pattern is why many options sellers target the 30-45 days-to-expiration (DTE) window: they capture significant decay while avoiding the heightened [[gamma]] risk of the final week.

### Theta by Moneyness

- **At-the-money (ATM)** options have the highest theta. They contain the most extrinsic value, so they have the most to lose.
- **In-the-money (ITM)** options have lower theta because much of their value is intrinsic (which does not decay).
- **Out-of-the-money (OTM)** options have lower absolute theta than ATM options, but their entire value is extrinsic, so theta represents a larger percentage of their price.

### The Gamma-Theta Tradeoff

There is a fundamental relationship between [[gamma]] and theta: they are opposite sides of the same coin. Options with high gamma (which benefit the holder when the underlying makes large moves) also have high theta (which costs the holder when the underlying stays still). This is not a coincidence -- it reflects the mathematical structure of option pricing. You cannot get the convexity benefit of gamma without paying for it through theta, and you cannot collect theta income without accepting the gamma risk.

## Trading Applications

### Theta-Positive Strategies (Collecting Decay)

- **[[covered-call]]**: Selling calls against long stock. Theta income supplements dividends and reduces cost basis.
- **[[iron-condor]]**: Selling both a [[call-spread]] and a [[put-spread]]. Maximum profit occurs when the underlying stays within the short strikes, allowing all options to expire worthless.
- **[[wheel-strategy]]**: Alternating between selling cash-secured puts and covered calls. Pure theta collection strategy.
- **[[credit-spread]]**: Selling a spread to collect premium. Profits from time decay if the underlying stays away from the short strike.
- **[[short-straddle]] / [[short-strangle]]**: Selling ATM or OTM options on both sides. High theta but high gamma risk.
- **[[calendar-spread]]**: Selling a near-term option and buying a longer-term option at the same strike. Profits from the differential theta decay rate.

### Theta-Negative Strategies (Paying for Optionality)

- **Long calls or puts**: Directional bets that pay theta daily for the right to unlimited gains.
- **[[straddle-strangle|Long straddles/strangles]]**: Volatility bets that need a large move to overcome daily theta cost.
- **[[debit-spread]]**: Buying a spread to limit cost but still net theta-negative.

### Managing Theta in a Portfolio

Professional traders aggregate theta across all positions to understand their portfolio's daily P&L from time decay alone. A portfolio with +$500 daily theta earns approximately $500 per day if nothing else changes -- but this income comes with corresponding [[gamma]] and [[vega]] risks that could produce much larger losses from adverse moves or volatility changes.

## Related

- [[options-greeks]]
- [[gamma]]
- [[delta]]
- [[vega]]
- [[implied-volatility]]
- [[iron-condor]]
- [[covered-call]]
- [[wheel-strategy]]
- [[black-scholes]]
- [[options]]

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg provides the definitive explanation of theta dynamics, decay curves, and the gamma-theta tradeoff
