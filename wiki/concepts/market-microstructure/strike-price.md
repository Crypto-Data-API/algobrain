---
title: Strike Price
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - options
  - derivatives
  - market-microstructure
aliases:
  - exercise-price
  - strike
domain: [market-microstructure]
prerequisites: ["[[options]]", "[[calls-vs-puts]]"]
difficulty: beginner
related:
  - "[[options]]"
  - "[[calls-vs-puts]]"
  - "[[delta]]"
  - "[[bear-put-spread]]"
  - "[[premium]]"
---

# Strike Price

The strike price (or *exercise price*) is the predetermined price at which an option contract can be exercised — the price at which the holder can buy (a call) or sell (a put) the underlying asset, regardless of where the underlying is trading at expiration. It is fixed when the contract is written and, together with the expiration date, defines the option. See [[options]] for a full overview.

## Moneyness: ITM, ATM, OTM

The relationship between the strike price and the current underlying price defines an option's **moneyness**:

- **In-the-money (ITM)**: A call with a strike below the underlying price, or a put with a strike above it. ITM options have intrinsic value.
- **At-the-money (ATM)**: The strike price is equal (or very close) to the current underlying price. ATM options have the highest time value and are the most actively traded.
- **Out-of-the-money (OTM)**: A call with a strike above the underlying price, or a put with a strike below it. OTM options have no intrinsic value and are cheaper, offering more leverage but lower probability of profit.

## Strike Selection and Premium

The choice of strike price directly affects the premium paid and the risk/reward profile. Deeper ITM options cost more but have a higher probability of profit and behave more like the underlying asset. OTM options are cheaper, offering greater percentage returns if the trade works but are more likely to expire worthless.

## Delta Relationship

An option's [[delta]] is closely tied to its strike. ATM options have a delta near 0.50 (calls) or -0.50 (puts). Deep ITM options approach a delta of 1.0 (or -1.0 for puts), while far OTM options have deltas near zero. Delta can be loosely interpreted as the market's implied probability that the option will expire in the money.

## Choosing Strikes for Strategies

Different strategies demand different strike selections. Covered calls typically use OTM strikes for income. Protective puts use ATM or slightly OTM strikes for cost-effective hedging. Vertical spreads like the [[bear-put-spread]] use two different strikes to define maximum risk and reward. Understanding how strike selection shapes a position's Greeks is essential for options traders. See [[calls-vs-puts]] for more on directional strategies.

## Trading Relevance

Strike selection is the single most consequential choice in any options trade after direction and expiry: it sets the breakeven, the cost (premium), the leverage, and the probability of profit. Selling OTM strikes harvests time decay (theta) but caps upside and carries assignment risk; buying ATM strikes maximizes gamma/theta sensitivity; buying deep ITM strikes substitutes for the underlying with less capital. The available strikes (the *strike ladder*) and their spacing are set by the exchange and tighten near the money for liquid names. Open interest clustered at specific strikes can also create [[market-maker]] hedging flows ("gamma walls" / pinning) that influence the underlying near expiration.

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — definition of strike/exercise price and moneyness.
- CBOE / OCC contract specifications — strike intervals and the listed strike ladder.
- Sheldon Natenberg, *Option Volatility and Pricing* — strike selection, delta as approximate probability, and strategy construction.

## Related

- [[options]]
- [[calls-vs-puts]]
- [[delta]]
- [[bear-put-spread]]
- [[premium]]
