---
title: "Gamma"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, derivatives, gamma]
aliases: ["Option Gamma", "Gamma Risk", "Gamma Exposure"]
related: ["[[options-greeks]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma-scalping]]", "[[black-scholes]]", "[[implied-volatility]]", "[[options]]"]
domain: [derivatives, risk-management]
difficulty: advanced
---

**Gamma** measures the rate of change of [[delta]] for a $1 move in the underlying asset. It is the second derivative of the option's price with respect to the underlying price -- the "acceleration" of directional exposure. Gamma determines how rapidly a trader's risk profile shifts as the underlying moves, making it one of the most important [[options-greeks]] for risk management.

## Overview

While [[delta]] tells you your current directional exposure, gamma tells you how quickly that exposure will change. A high-gamma position means that even small moves in the underlying will significantly alter your delta, requiring frequent rehedging. A low-gamma position is more stable, with delta changing slowly.

Gamma is always positive for long options (both calls and puts) and always negative for short options. This creates a fundamental asymmetry:

- **Long gamma**: Your delta moves in your favor. If the stock rises, your delta becomes more positive (or less negative), amplifying gains. If the stock falls, your delta becomes less positive (or more negative), reducing losses. Long gamma positions benefit from large moves in either direction.
- **Short gamma**: Your delta moves against you. If the stock rises, your delta becomes more negative relative to your position, creating losses. If the stock falls, the opposite occurs. Short gamma positions are harmed by large moves and profit from stability.

## How It Works

### Gamma by Moneyness and Time

Gamma's behavior varies significantly based on where the option sits relative to the underlying price and how much time remains:

- **At-the-money (ATM)** options have the highest gamma. Their delta is most sensitive to price changes because they sit at the inflection point between ITM and OTM.
- **Deep ITM and far OTM** options have low gamma. Their deltas are already near the extremes (close to 1.0 or 0) and do not change much with small price movements.
- **Near expiration**: Gamma increases dramatically for ATM options. In the final days before expiration, ATM gamma can spike to very high levels, creating what traders call **gamma risk** or **pin risk**. Small moves can swing delta from near 0 to near 1.0 (or vice versa) in hours.
- **Far from expiration**: Gamma is lower and more evenly distributed across strikes.

### The Gamma-Theta Tradeoff

Gamma and [[theta]] are fundamentally linked. The [[black-scholes]] model shows that, in a risk-neutral world, the benefit of gamma (profiting from moves) exactly equals the cost of theta (paying time decay) on average. This relationship is central to options pricing:

- A position with high positive gamma (benefiting from large moves) must have high negative theta (losing money each day the underlying stays still).
- A position with high negative gamma (profiting from stability) earns high positive theta (collecting time decay daily).

This tradeoff cannot be avoided. It is the mathematical reason why there is no free lunch in options: you either pay for convexity through theta or collect theta by accepting concavity.

### Gamma Exposure (GEX)

**Gamma exposure** is an aggregate market-level metric that estimates the total gamma held by options market makers across all strikes. When market makers are **long gamma**, they buy dips and sell rallies (stabilizing effect). When they are **short gamma**, they sell dips and buy rallies (destabilizing effect, amplifying moves). GEX has become a popular metric for predicting short-term market behavior, particularly around large options expirations.

## Trading Applications

### [[gamma-scalping|Gamma Scalping]]

Gamma scalping (also called dynamic hedging for profit) involves holding a long gamma position and repeatedly delta-hedging to lock in profits from price oscillations. The trader:

1. Buys options (establishing long gamma)
2. Delta-hedges by buying/selling the underlying
3. As the underlying moves up, delta increases -- the trader sells some underlying to re-neutralize
4. As the underlying moves back down, the trader buys back the underlying
5. Each round trip captures a small profit from the oscillation

The profit from gamma scalping must exceed the theta paid on the long options for the strategy to be net profitable. This works best in environments where [[realized-volatility]] exceeds [[implied-volatility]].

### Managing Short Gamma Risk

Many popular income strategies -- [[iron-condor]], [[short-strangle]], [[credit-spread]] -- are inherently short gamma. Traders manage this risk by:

- Setting position size limits based on total portfolio gamma
- Closing or rolling positions as expiration approaches (when gamma spikes)
- Using defined-risk structures (spreads) rather than naked short options to cap maximum loss
- Monitoring gamma exposure at the portfolio level, not just individual positions

### Gamma and Large Moves

Short gamma is the reason why option sellers can experience sudden, outsized losses. A short strangle might earn $200/day in theta but lose $5,000 in a single large move. The non-linearity of gamma means that losses accelerate -- each additional dollar of movement in the underlying causes proportionally larger losses for short gamma positions.

## Related

- [[options-greeks]]
- [[delta]]
- [[theta]]
- [[vega]]
- [[gamma-scalping]]
- [[delta-neutral]]
- [[black-scholes]]
- [[implied-volatility]]
- [[options]]
- [[gamma-exposure-trading]] -- strategy based on aggregate market-maker gamma exposure levels

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg provides the definitive treatment of gamma dynamics, the gamma-theta tradeoff, and practical gamma management for professional traders
