---
title: Liquidity
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [liquidity, market-microstructure]
aliases: ["Market Liquidity", "Liquid Market", "Illiquidity"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[bid-ask-spread]]"]
difficulty: beginner
related:
  - "[[bid-ask-spread]]"
  - "[[slippage]]"
  - "[[order-book]]"
  - "[[market-maker]]"
  - "[[volume]]"
  - "[[liquidity-provider]]"
  - "[[liquidity-evaporation]]"
  - "[[liquidity-risk]]"
---

Liquidity is the ability to buy or sell an asset quickly and in quantity without causing a significant change in its price.

## Overview

A liquid market has many buyers and sellers, tight [[bid-ask-spread]]s, deep [[order-book]]s, and minimal [[slippage]]. An illiquid market has few participants, wide spreads, and large price impact even for modest orders. Liquidity is one of the most important factors affecting trade execution quality.

## Key Details

- **Bid-ask spread**: The tightest measure of liquidity. Narrow spreads indicate a liquid market; wide spreads indicate illiquidity.
- **Market depth**: The total volume of orders at various price levels in the [[order-book]]. Deep books absorb large orders with minimal price impact.
- **Slippage**: The difference between expected and actual execution price. Worse in illiquid markets. See [[slippage]].
- **Volume**: Higher trading [[volume]] generally correlates with better liquidity, though volume alone does not guarantee depth.

## Liquidity Providers

[[market-maker]]s are the primary source of liquidity, continuously quoting bid and ask prices. In return, they earn the spread. Institutional participants, algorithmic traders, and passive limit orders also contribute to market liquidity.

## Trading Relevance

Always assess liquidity before entering a position. Key considerations:
- Can you enter and exit at your desired size without excessive slippage?
- Does liquidity dry up at certain times (overnight, weekends, holidays)?
- Illiquid assets can trap you in positions during volatile moves.
- Liquidity tends to evaporate precisely when you need it most -- during crashes and panics.

## Related

- [[flash-crashes]] — liquidity evaporation is the core mechanism of every flash crash
- [[flash-crash-2010]] — quoted depth vanished in seconds
- [[flash-crash-2015-etf]] — ETF liquidity proved illusory when underlying stocks halted
- [[crypto-flash-crashes]] — thin order books + extreme leverage = cascading liquidations
- [[high-frequency-trading]] — the dominant (and unreliable) source of electronic liquidity
- [[spoofing]] — fake orders create phantom liquidity in the order book
- [[bid-ask-spread]] — primary liquidity metric
- [[slippage]] — cost of trading in illiquid markets
- [[order-book]] — where liquidity is visible
- [[market-maker]] — entities that provide liquidity
- [[liquidity-provider]] — the agents whose quotes constitute liquidity
- [[liquidity-evaporation]] — what happens when liquidity disappears in stress
- [[liquidity-risk]] — the risk framework around funding and market liquidity

## Sources

- Harris, Larry. *Trading and Exchanges: Market Microstructure for Practitioners* (2003) — foundational definitions of liquidity, depth, and immediacy.
- Amihud, Yakov. "Illiquidity and Stock Returns: Cross-Section and Time-Series Effects." *Journal of Financial Markets* 5(1), 2002 — the Amihud illiquidity measure and the liquidity premium.
- Kyle, Albert S. "Continuous Auctions and Insider Trading." *Econometrica* 53(6), 1985 — formalizes market depth and price impact (Kyle's lambda).
- Brunnermeier, Markus K., and Lasse Heje Pedersen. "Market Liquidity and Funding Liquidity." *Review of Financial Studies* 22(6), 2009 — the funding/market-liquidity feedback loop behind evaporation.
