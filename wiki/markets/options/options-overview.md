---
title: "Options Markets"
type: overview
created: 2026-04-06
updated: 2026-06-19
status: excellent
tags: [options, markets, derivatives, overview]
aliases: ["options-strategies", "Options Overview"]
related: ["[[options]]", "[[derivatives]]", "[[volatility]]", "[[implied-volatility]]", "[[options-greeks]]"]
---

# Options Markets

Options contracts, pricing models, Greeks, and options-based strategies. This page serves as the central hub linking all options-related content in the wiki.

Options give the holder the right — but not the obligation — to buy ([[call-options|call]]) or sell ([[put-options|put]]) an underlying asset at a specified [[strike-price]] before expiration. The asymmetric payoff structure makes options uniquely versatile: hedging, income generation, directional speculation with defined risk, and [[volatility]] trading.

## How to Read This Hub

Options content in the wiki is organized along four axes, and most pages can be located by asking which axis a question belongs to:

1. **Mechanics** — what the contract *is* and how it settles (see [[options]], [[moneyness]], [[assignment-and-exercise]], [[american-vs-european-options]]).
2. **Pricing** — what the contract is *worth* and why ([[black-scholes]], [[put-call-parity]], the [[options-greeks|Greeks]]).
3. **Volatility** — the single most important pricing input, and an asset class in itself ([[implied-volatility]], [[volatility-surface]], [[volatility-risk-premium]], [[vix]]).
4. **Strategy** — how the building blocks combine into positions with shaped payoffs (the strategy catalog below).

A useful mental model: every options position is a bet on some combination of *direction* ([[delta]]), *speed of direction* ([[gamma]]), *the passage of time* ([[theta]]), and *the level of volatility* ([[vega]]). Knowing which of these four you are actually exposed to — and which you are inadvertently short — is the core discipline of options trading.

## The Two Sides of Every Trade

Options are a zero-sum transfer between a buyer and a seller, and the two sides have structurally opposite risk profiles. This asymmetry is the most important thing a new options trader must internalize:

| | Option buyer (long) | Option seller (short) |
|---|---|---|
| Pays / receives | Pays [[premium]] | Receives premium |
| Max loss | Premium paid (defined) | Often undefined (naked) |
| Max gain | Large / unbounded | Premium received (capped) |
| Time decay ([[theta]]) | Works against you | Works for you |
| Volatility ([[vega]]) | Long — wants IV to rise | Short — wants IV to fall |
| Win rate | Lower (most options expire worthless) | Higher |
| Payoff shape | Convex (lottery-like) | Concave (insurance-like) |
| Edge source | Convexity, leverage, defined risk | [[volatility-risk-premium]] |

Most systematic options *income* strategies (covered calls, cash-secured puts, condors, strangles) are forms of selling insurance to harvest the [[volatility-risk-premium]] — collecting small, frequent premiums while bearing a left tail. Most *hedging and speculation* strategies are forms of buying that insurance. Understanding which side a strategy sits on tells you its failure mode before you ever backtest it.

## Settlement & Exercise — the One-Page Summary

Two binary distinctions govern what physically happens at expiration. They matter for tax, assignment risk, and capital efficiency:

| Distinction | Option A | Option B |
|---|---|---|
| **Exercise style** | American — exercisable any time before expiry (most equity/ETF options) | European — exercisable only at expiry (most cash index options) |
| **Settlement** | Physical — shares change hands (equity, ETF options) | Cash — net cash difference paid (index options) |

Practical consequences: American + physical options (equity-options, ETF options like SPY) carry **early-assignment risk** — especially short calls before ex-dividend and deep-ITM short puts — and create [[assignment-and-exercise|pin risk]] near the strike at expiry. European + cash options (index options like SPX, XSP, RUT, NDX) cannot be assigned early and settle to an index print, eliminating delivery and pin risk but introducing **settlement-print risk** (AM SOQ vs PM close — see am-vs-pm-settlement). See [[assignment-and-exercise]] and [[cash-vs-physical-settlement]] for full mechanics.

## Tax Treatment at a Glance

US tax treatment is a first-order determinant of after-tax return for active traders and is often the deciding factor between otherwise-equivalent products:

- **[[section-1256-contracts|Section 1256]] (broad-based index options — SPX, XSP, RUT, NDX, VIX):** every gain/loss is taxed **60% long-term / 40% short-term** regardless of holding period, marked-to-market at year-end on Form 6781. The blended rate (~26.8% top-bracket vs ~37% short-term) is a structural edge for short-term-heavy strategies.
- **Standard equity treatment (single-name and ETF options — SPY, QQQ, IWM, xle, xlf, xlk):** holding period determines short- vs long-term; subject to wash-sale rules.

This is why an active trader running an S&P premium-selling book will often accept the wider quoted spreads of XSP over SPY, or RUT over IWM — the Section 1256 advantage compounds across a year of round trips. See [[section-1256-contracts]].

## The US Index-Options Franchise

The cash-settled, European-style index options form a coherent family differentiated mainly by *underlying* and *notional size*. They share Section 1256 treatment and no early assignment:

| Product | Underlying | Notional / contract | Liquidity | Notes |
|---|---|---|---|---|
| SPX | S&P 500 | ~$500K | Deepest US index options | Institutional default; AM monthlies + PM weeklies |
| XSP | 1/10 S&P 500 | ~$50K | Growing | "SPX for retail size," same tax/settlement |
| NDX | Nasdaq-100 | ~$500K+ | Deep | Tech-concentrated; [[qqq-options\|QQQ]] is the ETF cousin |
| RUT | Russell 2000 | ~$200K | Thinnest of the four | Small-cap; highest IV, steepest skew |
| [[vix-options\|VIX]] | VIX index | varies | Deep | Volatility-of-volatility; special settlement |

Their ETF counterparts (SPY, [[qqq-options|QQQ]], IWM) are American-style, physically settled, penny-quoted, and taxed as standard equity — the retail-friendly, smaller-notional alternatives. The recurring trade-off across the franchise is **liquidity and penny pricing (ETF options) vs tax efficiency and no-early-assignment (index options)**.

## Core Concepts

### Fundamentals
- [[options]] — comprehensive overview of options contracts, terminology, and mechanics
- [[call-options]] — right to buy the underlying
- [[put-options]] — right to sell the underlying
- [[moneyness]] — ITM, ATM, OTM mechanics, intrinsic vs. extrinsic value
- [[strike-price]] — the fixed price in the contract
- [[premium]] — option pricing components
- [[assignment-and-exercise]] — exercise mechanics, early exercise, pin risk, settlement

### Pricing & Valuation
- [[black-scholes]] — the foundational option pricing model
- [[put-call-parity]] — the fundamental no-arbitrage relationship linking calls, puts, and stock
- [[synthetic-positions]] — replicating positions using put-call parity (conversions, reversals, synthetic stock)

### Comparisons
- [[american-vs-european-options]] — exercise style differences and implications
- [[options-vs-futures]] — comparing the two major derivative types

## The Greeks

### Primary Greeks
- [[options-greeks]] — overview and interactions of all Greeks
- [[delta]] — directional risk (price sensitivity)
- [[gamma]] — acceleration of delta (convexity)
- [[theta]] — time decay
- [[vega]] — volatility sensitivity
- [[delta-neutral]] — maintaining zero directional exposure
- [[delta-divergence]] — delta-based signal analysis

### Second-Order Greeks
- [[second-order-greeks]] — vanna, charm, vomma/volga, speed, color — how the primary Greeks themselves change

## Volatility

- [[implied-volatility]] — the market's forward-looking volatility estimate
- [[realized-volatility]] — backward-looking historical volatility
- [[volatility]] — general volatility concept
- [[volatility-surface]] — the 3D IV surface across strikes and expirations (smile, skew, term structure)
- [[volatility-risk-premium]] — the persistent gap between IV and RV
- [[vix]] — the S&P 500 "fear index"
- [[options-implied-vol-skew]] — skew as a return predictor

## Options Strategies

### Income & Premium Selling
- [[covered-call]] — own stock + sell OTM call
- [[cash-secured-put]] — sell put + hold cash for potential assignment
- [[wheel-strategy]] — systematic covered call + cash-secured put rotation
- [[options-selling]] — premium selling overview
- [[iron-condor]] — sell OTM put spread + OTM call spread (range-bound)
- [[iron-butterfly]] — sell ATM straddle + buy OTM wings
- [[short-straddle]] — sell ATM call + ATM put
- [[short-strangle]] — sell OTM call + OTM put

### Directional Spreads
- [[vertical-spread]] — vertical spread overview
- [[bull-call-spread]] — buy lower call, sell higher call
- [[bear-put-spread]] — buy higher put, sell lower put
- [[bull-put-spread]] — sell higher put, buy lower put (credit)
- [[bear-call-spread]] — sell lower call, buy higher call (credit)

### Volatility Strategies
- [[straddle-strangle]] — long straddles and strangles (volatility buying)
- [[gamma-scalping]] — dynamic delta hedging to harvest gamma
- [[volatility-arbitrage]] — trading the IV vs RV spread
- [[skew-trading]] — trading the shape of the volatility smile

### Multi-Leg & Advanced Spreads
- [[butterfly-spread]] — three-strike spread for range targeting
- [[broken-wing-butterfly]] — asymmetric butterfly
- [[calendar-spread]] — same strike, different expirations
- [[diagonal-spread]] — different strike + different expiration
- [[double-diagonal]] — two diagonal spreads combined
- [[ratio-spread]] — unequal number of long/short options
- [[backspread]] — net long options with ratio construction
- [[box-spread]] — risk-free interest rate trade via put-call parity
- [[christmas-tree-spread]], [[gut-spread]], [[reverse-iron-condor]], [[jade-lizard]], [[strip-strap]], [[seagull-option]]

### Hedging & Protective
- [[protective-put]] — long stock + long put for downside protection
- [[married-put]] — protective put entered simultaneously with stock purchase
- [[collar-strategy]] / [[collar]] — long stock + protective put + covered call
- [[risk-reversal]] — OTM put + OTM call for directional exposure

### Long-Dated

### Modern
- [[0dte-trading]] — zero-days-to-expiration strategies, gamma mechanics, market impact

## Portfolio & Risk Management

- [[options-position-sizing]] — Greeks-based position sizing, portfolio limits, risk of ruin
- [[trade-repair-and-rolling]] — rolling, repair, and adjustment techniques
- [[delta-neutral-yield-farming]] — delta-neutral crypto strategies

## Options in Long/Short Portfolio Management

Options can serve as the primary vehicle for long-short-equity portfolio construction:

- Replace stock positions with [[call-options|call]] and [[put-options|put]] options to leverage [[volatility]] while capping risk at premium paid
- 20-60 day expiration horizons aligned with fundamental catalysts
- [[trade-repair-and-rolling|Rolling and repair]] techniques to manage losing positions
- Portfolio-level hedging using options on index ETFs (e.g., TLT, SPY)
- Focus on understanding [[implied-volatility]] as the driver of option pricing

## Data & Infrastructure

- [[open-interest]] — open interest as market structure indicator

## Education

- [[option-volatility-and-pricing]] — Natenberg's definitive options textbook
- [[book-options-futures-other-derivatives]] — Hull's canonical derivatives reference

## Sources

This is a hub/overview page that synthesizes and links the wiki's standalone options pages; each linked page carries its own sourcing. General market knowledge; no specific wiki source ingested yet.

## Pages in This Section

```dataview
TABLE status, updated, tags
FROM "wiki/markets/options"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```
