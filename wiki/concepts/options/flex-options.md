---
title: "FLEX Options"
type: concept
created: 2026-05-06
updated: 2026-06-21
status: excellent
tags: [options, derivatives, market-microstructure]
aliases: ["FLEX Options", "FLexible EXchange Options", "FLEX"]
domain: [options, derivatives]
difficulty: advanced
related: ["[[options-greeks]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[volatility-skew]]", "[[cboe]]", "[[occ]]", "[[options-pricing]]", "[[options-pricing-models]]", "[[options-strategies-overview]]", "[[gamma-squeeze]]", "[[max-pain]]", "[[put-call-parity]]"]
---

FLEX options (FLexible EXchange options) are exchange-listed, exchange-traded option contracts whose key terms -- strike price, expiration date, exercise style, and settlement type -- are negotiated between counterparties at trade time rather than fixed by the exchange. They were introduced on the [[cboe|CBOE]] in 1993 to give institutional users a way to obtain customized option exposure while retaining central clearing through the [[occ|OCC]], thereby eliminating the bilateral counterparty risk inherent in [[over-the-counter|OTC]] derivatives.

## Overview

Standard listed options come with a fixed grid of strikes, monthly/weekly expirations, American exercise (for equities), and physical settlement (for equities) or cash settlement (for indexes). This standardization is what makes the listed market liquid, but it also makes listed options a poor fit for many institutional hedging and structuring needs. FLEX options were the [[cboe|CBOE]]'s answer: keep the central counterparty (the OCC), keep the exchange auction mechanism, but let the user pick the contract terms.

FLEX trades are reported and cleared on-exchange, satisfy regulatory requirements for transparent execution, and are margined under the same risk-based regimes as standard options at participating clearing firms. Volume in FLEX has historically been small relative to standard listed options -- but it grew materially after the 2008 financial crisis and the 2010 Dodd-Frank Act, which pushed institutional structured products away from purely OTC venues toward centrally cleared alternatives.

### FLEX vs. standard listed vs. OTC options

FLEX occupies the middle ground between the fully standardized listed market and the fully bespoke OTC market — it borrows the customization of OTC and the clearing/credit profile of listed.

| Dimension | Standard listed | **FLEX** | OTC |
|---|---|---|---|
| Strike | Fixed exchange grid | Any price (often 4 dp) | Any price |
| Expiration | Fixed Fridays / weeklys | Any business day, up to ~15 yrs | Any date |
| Exercise style | Preset (American equity / European index) | American **or** European, chosen at trade | Negotiated |
| Settlement | Physical (equity) / cash (index) | Physical or cash, chosen at trade | Negotiated |
| Counterparty | [[occ\|OCC]] (novated) | [[occ\|OCC]] (novated) | Bilateral dealer |
| Default risk | Mutualized via OCC | Mutualized via OCC | Bilateral credit exposure |
| Secondary liquidity | Deep, continuous | Thin / bilateral unwind | None (bilateral) |
| Minimum size | 1 contract | ~250 contracts (institutional) | Negotiated, large |
| Retail access | Yes | No (direct); indirect via buffered ETFs | No |
| Max tenor | ~3 yr ([[leaps\|LEAPS]]) | ~15 yr | Unlimited |

The single most important column distinction: FLEX gives you OTC-grade customization **without** the bilateral counterparty credit risk that bank capital rules penalize. That is the entire reason the product exists.

## How it works / Mechanics

### Customizable terms

For each FLEX option contract, the parties (typically through a broker-dealer) specify:

| Term | Range / Options |
|---|---|
| Strike price | Any price, often to 4 decimal places (vs. fixed strike grid) |
| Expiration date | Any business day up to 15 years out |
| Exercise style | American or European |
| Settlement type | Physical (for equity FLEX) or cash (for index FLEX) |
| Settlement value method | (for index FLEX) opening or closing index level |

Standard listed options give you the cross-product of an exchange-fixed strike grid, monthly expirations, and one or two preset styles. FLEX gives you the entire continuous space.

### Listing and trading mechanism

A FLEX trade is initiated when a market participant (usually through a broker-dealer with a FLEX trading desk) submits a Request for Quote (RFQ) to the exchange specifying all custom terms. Liquidity providers and other interested parties respond with bids and offers in a brief auction window. The trade is matched, reported to the tape, and submitted to the [[occ|OCC]] for clearing -- exactly like a standard option, but on a one-off contract.

Subsequent trading in the *same* FLEX series is possible (the contract terms are standardized once created), but secondary-market liquidity is typically thin. Most FLEX contracts are held to expiration or unwound bilaterally with the original counterparty.

### Minimum size and product scope

FLEX contracts have minimum size requirements that vary by product:

- Index FLEX: minimum 250 contracts (or smaller in some FLEX-Micro variants introduced more recently)
- Equity FLEX: minimum 250 contracts opening transaction historically (CBOE has reduced and added smaller tiers over time; check current rules)

The minimum-size constraint means FLEX is effectively an institutional product. Listed exchanges offering FLEX include the [[cboe|CBOE]] (the original, and still the largest), as well as NYSE Arca/Amex, Nasdaq PHLX, MIAX, and others under their respective FLEX rule frameworks.

### Clearing and counterparty risk

All FLEX trades are novated to the [[occ|OCC]] post-trade. The OCC becomes the counterparty to both sides, which is the structural feature that distinguishes FLEX from a true OTC option. This:

- Eliminates bilateral default risk
- Provides standard margin treatment under SEC/CFTC frameworks
- Facilitates portfolio margining for sophisticated accounts
- Makes the position transferable across clearing members without renegotiation

### Symbology

FLEX contracts use a different symbology from standard options. They typically carry an exchange-specific FLEX prefix (e.g., a `1` or `9` indicator depending on venue and series) so they do not collide with the OPRA standard symbology used for the listed option chain. Most retail data feeds do not show FLEX series.

## When to reach for FLEX (decision table)

| Situation | Standard listed adequate? | Use FLEX? | Reasoning |
|---|---|---|---|
| Hedge expiring on a specific non-Friday date (vesting, plan end) | No | **Yes** | Only FLEX matches an arbitrary calendar date |
| Downside floor at an exact strike (e.g., 93% of spot) | No | **Yes** | Off-grid strike precision |
| Tail hedge with 5-15 year horizon | No ([[leaps\|LEAPS]] cap ~3 yr) | **Yes** | Only on-exchange long-dated route |
| Defined-outcome / buffered ETF construction | No | **Yes** | Custom strikes + outcome-period expiries + European exercise |
| Standard monthly hedge on a liquid index, small size | Yes | No | Listed market is cheaper and deeper |
| Retail-sized directional trade | Yes | No (blocked) | 250-contract minimum |
| Replicate an embedded OTC structured-note option with central clearing | Partially | **Yes** | OCC clearing cuts counterparty-credit capital charges |

## Practical use / Trading applications

### Hedging non-standard corporate positions

A corporate insider with a 10b5-1 plan ending on a specific date, or an employee with a restricted stock vesting schedule, may want a hedge that aligns *exactly* to that date. Standard listed options expire only on certain Fridays. A FLEX put expiring on the precise vesting date solves the calendar-mismatch hedging problem.

### Replicating OTC structures with central clearing

Structured products desks frequently package equity-linked notes, principal-protected notes, and auto-callables that embed multi-year European options on indexes or single names. Pre-Dodd-Frank, those embedded options were typically OTC. Post-2010, more dealers prefer to lay off the embedded option as a FLEX trade, gaining OCC clearing and reducing counterparty-credit charges under bank capital rules.

### Buffered ETFs and defined-outcome ETFs

A large and visibly growing use case: defined-outcome ETFs (Innovator, FT Cboe Vest, AllianzIM, BlackRock iShares "Max" series, and others) hold portfolios of FLEX options on the S&P 500 or other indexes to engineer specific outcome profiles -- buffered downside, capped upside, defined-outcome periods that do not align to standard third-Friday expirations. These funds rely on FLEX precisely because:

1. The fund's outcome period (e.g., 12 months from inception of a tranche) does not match standard expirations.
2. The strike levels needed to engineer specific buffer/cap levels do not match standard strikes.
3. The fund needs European exercise to avoid early-assignment risk on the embedded option.
4. OCC clearing allows the fund to operate within ETF regulatory and operational constraints.

The growth of buffered ETFs has been a major driver of FLEX volume since around 2018.

### Pension and insurer hedging

Defined-benefit pension funds and insurance company general accounts often hold large equity exposures and want long-dated downside hedges (5-15 year horizons). The listed market caps out at LEAPS expirations of about three years; FLEX is the only on-exchange way to obtain longer-dated puts.

### ETF and index portfolio hedging at custom levels

A fund manager who wants to put a -7% floor on an S&P 500 portfolio to a specific quarter-end date can establish a FLEX put at the exact 93%-of-spot strike with the exact desired expiration. Doing the same trade in standard listed options would require the manager to accept a strike grid offset, an expiration mismatch, or both.

## Limitations / What can go wrong

### Liquidity is thin and bilateral

While the trade clears through OCC, secondary-market liquidity in any specific FLEX series is usually negligible. If a holder needs to unwind, the practical path is often back to the original counterparty for an unwind quote -- which can produce wide bid-ask spreads when market conditions have shifted. Mid-life mark-to-market is dealer-quote-dependent.

### Pricing transparency is limited

Trade prints appear on the consolidated tape but the FLEX universe is so heterogeneous (every contract is potentially unique) that there is no useful "FLEX implied vol surface" the way there is for listed options. Pricing relies on dealer models and the implied-vol input from the standard listed surface, with proprietary adjustments for tenor and strike interpolation/extrapolation.

### Minimum sizes block retail access

The 250-contract minimum (or larger) effectively excludes individual investors. This is by design -- FLEX is positioned as an institutional product -- but it means retail traders cannot access FLEX directly. Indirect access is available through buffered ETFs and defined-outcome funds, which package FLEX exposure into ETF wrappers.

### Operational complexity

FLEX trades require infrastructure that not all clearing firms or back offices support. Margin systems must accept non-standard expirations and strikes; risk systems must price contracts that do not appear in any standard data feed; and reporting systems must handle the FLEX symbology. For mid-sized institutions, the operational overhead can be a real barrier.

### Regulatory and tax treatment nuances

Long-dated FLEX positions can interact with section 1256 contract rules, constructive sale rules, and (for index FLEX) the 60/40 capital gains treatment in non-obvious ways. Tax outcomes depend on whether a specific FLEX is treated as a section 1256 contract or a non-1256 option, which in turn depends on the underlying and exercise style. Always involve qualified tax counsel for sizable positions.

### Confusion with put-call parity in customized exercise styles

Because FLEX permits American or European exercise on the same underlying, [[put-call-parity]] relationships between two FLEX contracts with different exercise styles do not hold exactly -- a subtle point that occasionally trips up traders moving from listed to FLEX strategies.

## Examples

### Buffered ETF construction

A 12-month outcome-period buffered ETF launching on April 15, 2026 might hold the following FLEX legs on SPX, all expiring April 15, 2027 (European, cash-settled):

| Leg | Direction | Strike (% of inception spot) | Purpose |
|---|---|---|---|
| Long deep ITM call | Long | ~5% | Provides upside participation |
| Short OTM call | Short | ~115% (the cap) | Sells the upside above the cap |
| Long ATM put | Long | 100% | Begins the buffer |
| Short OTM put | Short | 90% (end of buffer) | Caps the buffer at -10% |

The combined position synthesizes the fund's outcome profile: roughly 1:1 upside up to ~+15%, full downside protection from 0 to -10%, and pass-through losses below -10%. None of these legs would be available with the *exact* strikes and expiration dates required using standard listed options -- which is why FLEX is essential to the product category.

### Pension five-year hedge

A pension consultant working with a $5B equity portfolio wants a tail hedge: -20% floor over a 5-year horizon on the S&P 500. They negotiate a FLEX put on SPX with strike at 80% of current index level, expiring on a specific business day five years out, European exercise, cash settlement. Premium is paid up front. The position clears through OCC with the same margin and credit treatment as any other listed option. Standard listed options cannot deliver this trade because their longest LEAPS expirations do not extend five years.

### Corporate insider hedge

An executive with a 100,000-share restricted stock grant vesting on a specific Tuesday five months out wants a costless collar locked to that exact date. A FLEX collar -- short call and long put expiring on that Tuesday, with strikes negotiated for zero net premium -- aligns the hedge to the vesting calendar precisely. Doing the same trade in listed options would require accepting either an early-expiring (and rolled) hedge or one expiring after the vesting -- introducing rebalancing risk in either direction.

## Related

- [[cboe]] -- originator and largest FLEX venue
- [[occ]] -- central clearer that novates every FLEX trade
- [[options-pricing]]
- [[options-pricing-models]]
- [[options-greeks]]
- [[implied-volatility]]
- [[volatility-surface]] -- the listed surface FLEX pricing interpolates/extrapolates from
- [[volatility-skew]]
- [[options-strategies-overview]]
- [[put-call-parity]]
- [[max-pain]]
- [[gamma-squeeze]]
- [[leaps]] -- the longest-dated *standard* alternative (caps out ~3 yr)
- [[buffered-etfs]] / [[defined-outcome-etfs]] -- the largest retail-facing FLEX use case
- [[tail-risk-hedging]] -- long-dated FLEX puts as standing protection
- [[over-the-counter]] -- the bilateral alternative FLEX displaces
- [[tradestation-options-workflow]] -- contrast: retail listed-options automation vs. institutional FLEX

## Sources

- CBOE FLEX Options product specifications (cboe.com/flex)
- OCC public documentation on cleared FLEX product
- Innovator ETFs / FT Cboe Vest / AllianzIM defined-outcome ETF prospectuses (FLEX position disclosures)
- SEC and CFTC commentary on the migration of OTC structured products to centrally cleared venues post-Dodd-Frank
- Industry press coverage of buffered ETF growth, 2018-2025 (Bloomberg, Wall Street Journal, ETF.com)
- *Options as a Strategic Investment* (McMillan) -- chapter on flexible exchange options
