---
title: "Options Greeks"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, derivatives, risk-management]
aliases: ["Greeks", "Option Greeks", "The Greeks"]
related: ["[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[rho]]", "[[black-scholes]]", "[[implied-volatility]]", "[[options]]"]
domain: [risk-management, derivatives]
difficulty: intermediate
---

The **Options Greeks** are a set of risk measures that quantify how an option's price responds to changes in underlying variables such as the stock price, time, volatility, and interest rates. They are essential tools for options traders managing complex portfolios, allowing precise measurement and hedging of each source of risk independently.

## Overview

The Greeks derive their names from Greek letters (with the exception of [[vega]], which is not actually a Greek letter). Each Greek isolates a single dimension of risk. Professional options traders and market makers monitor the Greeks continuously, adjusting positions to maintain desired risk profiles. The [[black-scholes]] model and its extensions provide the mathematical framework from which the Greeks are calculated as partial derivatives of the option pricing function.

Understanding the Greeks transforms options trading from directional speculation into nuanced risk management. A trader who only thinks about whether a stock will go up or down is ignoring the majority of forces that move option prices -- time decay, volatility shifts, and the non-linear relationship between the option and its underlying.

## The Primary Greeks

### [[delta]] -- Directional Risk

Delta measures how much an option's price changes for a $1 move in the underlying asset. Call deltas range from 0 to +1; put deltas range from -1 to 0. A delta of 0.50 means the option moves roughly $0.50 for every $1 move in the stock. Delta also serves as a rough approximation of the probability that the option will expire in-the-money.

### [[gamma]] -- Acceleration of Delta

Gamma measures the rate of change of delta per $1 move in the underlying. It tells you how quickly your directional exposure shifts. Gamma is highest for at-the-money options near expiration. Long options have positive gamma (delta moves in your favor); short options have negative gamma (delta moves against you).

### [[theta]] -- Time Decay

Theta measures the daily erosion of an option's value due to the passage of time, holding all else constant. Theta is typically negative for option buyers (they lose value each day) and positive for option sellers (they collect decay). Theta decay accelerates as expiration approaches, particularly for at-the-money options.

### [[vega]] -- Volatility Sensitivity

Vega measures how much an option's price changes for a 1-percentage-point change in [[implied-volatility]]. Long options have positive vega (they benefit from rising IV), while short options have negative vega. Vega is highest for at-the-money options with longer time to expiration.

### Rho -- Interest Rate Sensitivity

Rho measures sensitivity to changes in the risk-free interest rate. Calls have positive rho (they benefit from rising rates) and puts have negative rho. Rho is generally the least important Greek for short-term options but can matter for long-dated LEAPS.

## How the Greeks Interact

The Greeks are not independent -- they interact in important ways:

- **Gamma and theta are inversely related**: Options with high gamma (benefiting from large moves) also have high theta (paying for that privilege through time decay). This is sometimes called the gamma-theta tradeoff. You cannot have the convexity benefit of gamma without paying for it in theta.
- **Vega and theta can conflict**: A long vega position benefits from rising volatility, but if volatility stays flat, theta erodes the position. Traders must weigh the potential for a volatility increase against the daily cost of holding.
- **Delta changes with gamma**: A delta-neutral portfolio will not stay neutral if the underlying moves. The rate at which it drifts depends on gamma. Frequent rehedging (delta adjustments) is required for portfolios with significant gamma exposure.
- **Higher-order Greeks**: Professional traders also track charm (delta decay over time), vanna (delta sensitivity to volatility), and volga/vomma (vega sensitivity to volatility), though these are less commonly discussed outside institutional desks.

## Trading Applications

- **Portfolio risk management**: Traders aggregate Greeks across all positions to understand total portfolio exposure to direction, time, and volatility. A portfolio might be delta-neutral but long gamma and short theta.
- **Market making**: Market makers use the Greeks to hedge their inventory. After filling a customer order, they immediately delta-hedge and monitor gamma and vega to manage residual risk.
- **Strategy selection**: The Greeks help traders choose the right structure. If you want to profit from time decay, you select strategies with positive theta (e.g., [[iron-condor]], [[covered-call]]). If you want to profit from a volatility spike, you select strategies with positive vega (e.g., [[straddle-strangle|straddles]], [[calendar-spread|calendars]]).
- **Position sizing**: Greeks-based position sizing ensures that no single position contributes disproportionate risk. A trader might limit total portfolio gamma or vega to predefined thresholds.

## Related

- [[delta]]
- [[gamma]]
- [[theta]]
- [[vega]]
- [[black-scholes]]
- [[implied-volatility]]
- [[options]]
- [[risk-management]]

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg's comprehensive treatment of the Greeks and their interactions is the standard reference for options traders
