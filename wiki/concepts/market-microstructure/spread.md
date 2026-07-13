---
title: Spread
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [spread, market-microstructure, liquidity, derivatives]
aliases: ["spreads"]
domain: [market-microstructure]
prerequisites: ["[[bid-ask-spread]]", "[[order-book]]"]
difficulty: beginner
related:
  - "[[bid-ask-spread]]"
  - "[[liquidity]]"
  - "[[market-maker]]"
  - "[[order-book]]"
  - "[[options]]"
  - "[[futures]]"
---

# Spread

In trading, a *spread* is the difference between two prices, rates, or yields. The word is overloaded: it describes the bid-ask gap on a single instrument, the price differential between two related instruments, and a class of multi-leg options strategies. The common thread is that a spread isolates a *relationship* rather than an outright price level.

## Overview

The most fundamental spread is the [[bid-ask-spread]] — the gap between the best bid and best ask on an instrument, which represents the cost of immediacy and the primary revenue of [[market-maker]]s. Beyond that, "spread" is used wherever traders care about the difference between two prices: yield spreads between bonds, the basis between spot and futures, the calendar gap between two delivery months, and the net premium of a multi-leg options position. Each spread strips out a common factor (the overall market level) so the trader is exposed only to the relationship between the two legs.

## Types of Spread

### Bid-Ask (transaction) spread
- **Tight spread**: small gap between bid and ask — high [[liquidity]], active [[market-maker]]s, low transaction cost.
- **Wide spread**: large gap — thin liquidity, uncertainty, off-hours, small-cap or exotic instruments.
- Every round-trip market order pays at least one full bid-ask spread. See [[bid-ask-spread]] for the full decomposition (order-processing, inventory, and [[adverse-selection]] costs).

### Yield spread (credit / rates)
The difference in yield between two debt instruments — e.g. a corporate bond versus a duration-matched Treasury (the *credit spread*), or the 10y minus 2y Treasury (a *term spread*). Widening credit spreads signal rising default risk and risk-off conditions; an inverted term spread (negative 10y-2y) has historically preceded U.S. recessions.

### Basis / calendar spread (futures)
- **Basis spread**: the difference between a [[futures]] price and the underlying spot price, reflecting [[cost-of-carry]], financing, and [[convenience-yield]].
- **Calendar (intra-commodity) spread**: long one delivery month and short another (e.g. long Dec / short Jun crude), isolating the shape of the [[futures-curve-structure-analysis|futures curve]] ([[contango]] vs [[backwardation]]) rather than the outright price.
- **Inter-commodity spreads**: e.g. the crack spread (crude vs refined products) or the crush spread (soybeans vs meal/oil).

### Option spreads
Multi-leg [[options]] positions that buy and sell options of differing [[strike-price|strikes]] or expirations to shape the risk/reward and finance one leg with another — vertical spreads (bull/bear), calendar spreads, and ratio spreads. These define maximum risk and reward up front in exchange for capping the payoff.

## Trading Relevance

For active traders the bid-ask spread is a hard, recurring transaction cost that can dwarf commissions and must be built into any profitability or backtest model. Spread *widening* on an instrument is a leading indicator of deteriorating [[liquidity]] and approaching stress; spread *compression* signals improving conditions. As an explicit strategy, spread trades (yield-curve, calendar, inter-commodity, options spreads) let a trader express a view on a relationship while hedging out the dominant directional factor — typically lowering volatility and margin relative to an outright position. This is the core of relative-value and [[pairs-trading]].

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — futures basis, calendar and option spread strategies.
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* — bid-ask spread as the cost of immediacy.

## Related

- [[bid-ask-spread]] — the core transaction-cost spread
- [[liquidity]] — the primary driver of spread width
- [[market-maker]] — earns profit from the spread
- [[order-book]] — where the bid-ask spread is visible
- [[options]] — multi-leg option spread strategies
- [[futures]] — basis and calendar spreads
- [[pairs-trading]] — relative-value spread trading
