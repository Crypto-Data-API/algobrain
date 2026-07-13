---
title: Premium
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - options
  - derivatives
  - volatility
aliases:
  - options-premium
  - futures-premium
  - option premium
related:
  - "[[options]]"
  - "[[contango]]"
  - "[[strike-price]]"
  - "[[volatility]]"
  - "[[time-decay]]"
  - "[[spot-price]]"
  - "[[volatility-risk-premium]]"
domain: [market-microstructure, derivatives]
prerequisites: ["[[options]]", "[[spot-price]]"]
difficulty: beginner
---

# Premium

The amount paid above fair or spot value. In options trading, the premium is the price paid to acquire the contract; in futures, the premium is the amount by which the futures price exceeds the spot price.

## Options Premium

An [[options]] premium consists of two components: **intrinsic value** and **extrinsic value** (also called time value). Intrinsic value is the amount by which the option is in-the-money -- for a call, this is the difference between the underlying price and the [[strike-price]] when the underlying trades above the strike. Extrinsic value reflects time remaining until expiration, implied [[volatility]], and interest rates.

As expiration approaches, an option's extrinsic value erodes through a process called **time decay** (theta). Options sellers collect premium upfront and profit when the contract expires worthless, making premium selling a popular income strategy.

## Futures Premium (Basis)

In futures markets, the premium (or **basis**) is the difference between the futures price and the [[spot-price]]. When futures trade above spot, the market is in [[contango]] -- a positive premium driven by storage costs, financing costs, and convenience yield. The premium typically converges to zero as the contract approaches expiration.

## Insurance Premium Concept

The concept of premium extends beyond trading into a broader financial framework: paying a price today for protection against future uncertainty. Buying put [[options]] as portfolio insurance, paying for hedges against tail risk, or holding cash as a buffer all represent forms of insurance premium in trading.

## Trading Relevance

For traders, "premium" is most often the price of an [[options]] contract, and the central edge debate is whether option premia are systematically too rich. The [[volatility-risk-premium]] — the persistent gap between option-implied volatility and subsequently realised volatility — means sellers of premium are, on average, paid more than the eventual cost of the risk they assume. This is the basis of income strategies such as covered calls, cash-secured puts, and short straddles/strangles. The trade-off is asymmetric: premium sellers collect small, steady credits but face large, infrequent losses when realised volatility spikes (a short-volatility, negatively-skewed payoff). In futures, watching the premium/basis to [[spot-price|spot]] reveals the market's storage and financing expectations and signals [[contango]] versus backwardation.

## Related

- [[options]]
- [[contango]]
- [[strike-price]]
- [[volatility]]
- [[time-decay]]
- [[spot-price]]
- [[volatility-risk-premium]]

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* (Pearson) — option pricing and intrinsic/extrinsic value
- Sheldon Natenberg, *Option Volatility and Pricing* (McGraw-Hill) — premium decomposition and time decay
- CME Group educational materials — futures basis and convergence
