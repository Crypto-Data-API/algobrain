---
title: Derivatives
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [derivatives, options, futures, leverage, volatility, market-microstructure]
aliases: ["Derivative", "Derivative Contracts"]
domain: [market-microstructure, derivatives]
prerequisites: ["[[leverage]]", "[[volatility]]"]
difficulty: intermediate
related:
  - "[[futures]]"
  - "[[options]]"
  - "[[leverage]]"
  - "[[volatility]]"
  - "[[margin]]"
  - "[[perpetual-futures]]"
---

# Derivatives

A derivative is a financial instrument whose value is *derived* from the price of an underlying asset, index, rate, or benchmark. The contract specifies terms between two parties referencing that underlying; no party need own the underlying itself. Derivatives are the primary tools for hedging, leveraged speculation, and transferring specific risks (price, rate, credit, volatility) between participants.

## Overview

Derivatives let traders gain exposure to an asset without owning it directly, and let hedgers offload risks they do not want. The global derivatives market is the largest financial market by notional value — the BIS estimates the gross notional of outstanding OTC derivatives at well over $600 trillion, dwarfing global equities and bonds combined (though notional vastly overstates true economic exposure, which is closer to gross market value of a few trillion).

Two structural distinctions matter most:

- **Linear vs non-linear payoff.** [[futures]], forwards, and swaps have linear payoffs (P&L moves ~1:1 with the underlying). [[options]] have non-linear (convex) payoffs — the defining feature that lets traders bet on [[volatility]] itself.
- **Exchange-traded vs OTC.** Exchange-traded derivatives (listed futures and options) are standardized and centrally cleared, removing bilateral counterparty risk. Over-the-counter (OTC) derivatives (forwards, swaps, exotic options) are customized and carry [[counterparty-risk]] unless centrally cleared (a change pushed by the [[dodd-frank-act|Dodd-Frank Act]] after 2008).

## Key Types

| Type | Payoff | Venue | Notes |
|------|--------|-------|-------|
| **[[futures]]** | Linear | Exchange | Obligation to buy/sell at a set price on a future date. Standardized, marked-to-market daily, centrally cleared. |
| **Forwards** | Linear | OTC | Like futures but customized and bilateral — carries [[counterparty-risk]]. |
| **[[options]]** | Non-linear | Exchange + OTC | Right (not obligation) to buy/sell at a strike. Buyer pays a premium; the only major instrument for trading [[volatility]] directly. |
| **Swaps** | Linear | OTC (mostly cleared) | Exchange of cash flows — interest-rate swaps, total-return swaps, currency swaps. |
| **[[credit-default-swaps\|CDS]]** | Step | OTC | Insurance against a credit event; central to the 2008 crisis. |
| **[[perpetual-futures\|Perpetual contracts]]** | Linear | Crypto exchanges | Crypto-native futures with no expiry; a [[funding-rate]] mechanism tethers the contract to spot. |

## How It Works

All derivatives share a common structure: two parties agree on terms referencing an underlying's price, and the contract's value fluctuates as the underlying moves. Settlement can be **physical** (the asset is delivered) or **cash** (the difference is paid). Most derivatives provide [[leverage]], because only a fraction of notional value is posted as [[margin]] — a futures position controlling $100,000 of an index might require only $5,000–$10,000 in initial margin. This embedded leverage is the source of both their capital efficiency and their tail risk: a position sized by notional rather than by margin can wipe out the account on a modest adverse move.

Pricing of linear derivatives follows from no-arbitrage carry relationships (forward price = spot adjusted for cost of carry: rates, dividends, storage). Options pricing rests on [[black-scholes|Black-Scholes]] and its descendants, which translate the underlying price, strike, time, rates, and implied [[volatility]] into a premium via the [[options-greeks|Greeks]].

## Trading Relevance

Derivatives are essential for:

- **Hedging** — a portfolio manager buys index puts or sells futures to neutralize downside without liquidating holdings.
- **Leverage** — controlling large notional exposure with limited capital, enabling capital-efficient long/short books (e.g. the [[itpm]] options-only [[long-short-equity]] approach).
- **Price discovery** — derivatives markets often *lead* spot, because they are where informed and hedging flow concentrates. The [[basis]] (futures minus spot) and the [[funding-rate]] encode positioning and carry.
- **Volatility trading** — options let a trader bet on the *magnitude* of moves regardless of direction, capturing the [[volatility-risk-premium]].
- **Risk transfer** — swaps and CDS let institutions isolate and trade a single risk factor (rates, credit) without touching the underlying bond or loan.

The core risks to manage are leverage-driven gap risk, [[counterparty-risk]] (for OTC), [[liquidity]] in stress (bid-ask blowouts and margin spirals), and — for options — the path dependence of the Greeks.

## Related

- [[futures]] — most widely traded linear derivative
- [[options]] — key tool for hedging and volatility trading
- [[perpetual-futures]] — crypto-native derivative with funding mechanism
- [[leverage]] — derivatives inherently provide leverage
- [[margin]] — collateral required for derivative positions
- [[counterparty-risk]] — central risk in OTC derivatives
- [[dodd-frank-act]] — post-2008 derivatives clearing reform

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — the canonical derivatives textbook ([[book-options-futures-other-derivatives]])
- Bank for International Settlements (BIS) — OTC derivatives statistics (semiannual)
- CFTC and CBOE official documentation on listed futures and options
