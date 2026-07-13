---
title: "Options Approval Levels"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, regulation, market-microstructure, risk-management, derivatives]
aliases: ["Options Trading Levels", "Options Trading Authority", "Option Approval Tiers"]
domain: [market-microstructure]
prerequisites: ["[[options-trading]]", "[[margin-trading]]"]
difficulty: beginner
related:
  - "[[finra]]"
  - "[[regulation]]"
  - "[[options-disclosure-document]]"
  - "[[portfolio-margin]]"
  - "[[pattern-day-trader-rule]]"
  - "[[itpm-trade-construction-playbook]]"
  - "[[interactive-brokers]]"
  - "[[tastytrade]]"
  - "[[etrade]]"
  - "[[charles-schwab]]"
  - "[[robinhood]]"
  - "[[webull]]"
---

Options approval levels (also called "trading levels" or "options trading authority") are the broker-assigned tiers that determine which options strategies a customer is allowed to trade in a given account. They exist because [[finra|FINRA]] Rule 2360 (Options Account Approval) requires broker-dealers to perform suitability analysis on every options account, and because brokers want to limit their own risk to losses that exceed customer equity (which would become the broker's bad debt). The level a customer receives controls everything from being able to write a covered call to being able to short an uncovered SPX put.

## Overview: FINRA Rule 2360

FINRA Rule 2360(b)(16) requires that before any account is approved for options trading, a Registered Options Principal (ROP) at the broker must review the customer's:

- Investment objectives (income, growth, speculation, hedging)
- Trading experience and knowledge (years trading, types of products)
- Financial situation (annual income, net worth, liquid net worth)
- Age, employment status, marital status, dependents
- Tax bracket and investment time horizon

The customer must also receive the Options Disclosure Document (ODD), formally titled "Characteristics and Risks of Standardized Options," published by the [[occ|OCC]]. Brokers then assign a tier based on their internal suitability matrix. The CFTC and SEC do not specify the tier names or counts - those are broker-defined - so naming conventions vary. The underlying principle is universal: more potentially loss-bearing strategies require more demonstrated experience and net worth.

## Standard Tier Definitions

The following levels are the conventional ladder used by most US retail brokers. Names and exact contents vary, but the risk-ordering is consistent.

### Level 1: Covered and Protective Strategies

Strategies that **reduce** risk on existing positions or are fully cash-collateralized.

- **Covered calls** - sell a call against 100 shares already owned per contract.
- **Cash-secured puts** - sell a put with cash equal to (strike x 100) set aside.
- **Protective puts** - buy a put against shares owned (insurance).
- **Married puts** - buy stock and put simultaneously.

Risk profile: defined; cannot lose more than the underlying position is worth (in the case of covered calls/protective puts) or the strike-defined cash (in the case of CSPs).

Approval bar: low. Most accounts including IRAs are approved at this level by default once an options application is filed.

### Level 2: Long Options (Debit, Defined Risk)

Buying calls and puts outright.

- **Long calls** - directional bullish, max loss = premium paid.
- **Long puts** - directional bearish, max loss = premium paid.
- Sometimes includes **long straddles/strangles** (two long legs).

Risk profile: defined; max loss is the debit paid.

Approval bar: requires demonstrating some options knowledge but accessible to most brokerage customers. Many brokers bundle Level 1 + Level 2 as their starter options approval.

### Level 3: Defined-Risk Multi-Leg Spreads

Strategies built from multiple legs where the worst case is bounded.

- **Vertical spreads** (bull call, bear put, bull put, bear call) - long+short same expiry, different strikes.
- **Calendar spreads** - long+short same strike, different expiries.
- **Diagonal spreads** - long+short different strikes and expiries.
- **Iron condors** - short call spread + short put spread on the same underlying.
- **Iron butterflies** - short straddle + protective wings.
- **Butterflies and broken-wing butterflies**.
- **Box spreads** (synthetic loans).

Risk profile: defined; max loss is the spread width minus credit received (or debit paid).

Approval bar: requires moderate experience, often 1-2 years of options trading and demonstrated knowledge of multi-leg mechanics. Margin is typically the spread width per contract, which makes capital requirements transparent.

### Level 4: Uncovered (Naked) Equity Options

Selling options without the underlying or offsetting option position.

- **Naked short calls on equities/ETFs** - theoretically unlimited loss if underlying rises.
- **Naked short puts on equities/ETFs** - max loss is (strike - 0) x 100 if stock goes to zero.
- **Short straddles and strangles on equities** - undefined risk on both wings.

Risk profile: substantial; short calls have theoretically unlimited loss, short puts have very large defined loss.

Approval bar: high. Brokers typically require:
- Several years of options experience
- Substantial net worth ($100k+ liquid is common)
- Income suitable for absorbing losses
- Margin account (cannot trade naked options in cash account or IRA at most brokers)
- "Speculation" listed as an investment objective

### Level 5: Uncovered Index Options and Advanced Combinations

The highest tier, generally reserved for sophisticated accounts.

- **Naked short index options** (SPX, NDX, RUT, [[xsp-options|XSP]], VIX) - cash-settled, European, no early exercise risk but very large notional.
- **Complex undefined-risk combinations** across multiple underlyings.
- **Short volatility structures** that can produce losses many multiples of premium received.

Approval bar: very high. Typically requires:
- [[portfolio-margin|Portfolio margin]] (which itself requires $125,000+ equity and an exam at most brokers)
- Documented experience trading uncovered options
- Large account size (often $250k+ in practice)
- Explicit speculative or income-from-premium-selling objective

Not every broker has a "Level 5" - some lump index uncovered into Level 4, others gate it behind portfolio margin specifically.

## Broker-by-Broker Variations

Naming and tier counts differ by broker. Selected examples (subject to change - check current broker docs):

| Broker | Tier System | Notes |
|---|---|---|
| **[[etrade|E*TRADE]]** | Levels 1-4 | Level 4 covers naked equity options; index uncovered also at Level 4. |
| **[[charles-schwab|Schwab/thinkorswim]]** | Levels 0, 1, 2, 3, plus "spreads" approval | Schwab uses 0 (covered) through 3 (uncovered) with separate spread approval. |
| **[[interactive-brokers|Interactive Brokers]]** | Tiered with explicit per-strategy permissions | Most granular; can grant permissions per strategy class and per underlying type. |
| **[[tastytrade|tastytrade]]** | "The Works" | Single combined approval that grants all defined-risk and naked options once approved. |
| **[[robinhood|Robinhood]]** | Levels 1-3 | Level 3 is the highest; no naked option selling on equities. Level 3 enables spreads. |
| **[[webull|Webull]]** | Levels 1-3 | Similar to Robinhood; naked options not generally available. |
| **Fidelity** | Levels 1-5 | Closest to the textbook 5-level ladder; Level 5 explicitly covers uncovered index options. |
| **TastyWorks (legacy)** | Same as tastytrade ("The Works") | Single approval encompassing naked equity and index options. |

The practical takeaway: do not assume your strategy is allowed because another broker permits it. Robinhood and Webull customers cannot sell naked options at all; tastytrade and IBKR customers can with the right approval.

## Application Process

To upgrade, customers complete an options application (or update an existing one) providing:

- **Income** - annual gross from all sources.
- **Net worth and liquid net worth** - total assets minus liabilities; liquid excludes home equity, retirement accounts, and illiquid holdings.
- **Investment experience** - years trading stocks, options, futures, with self-reported knowledge level (none/limited/good/extensive).
- **Investment objectives** - capital preservation, income, growth, speculation, or some combination.
- **Time horizon** - short, medium, long.
- **Risk tolerance** - low, medium, high.
- **Employment status** - including whether employed by a FINRA member (which triggers Rule 3210 disclosure requirements).

Typical approval criteria for higher tiers:
- **Level 3 (spreads)**: 1+ year options experience, "good" knowledge, growth or speculation objective, margin account.
- **Level 4 (naked equity)**: 2-3+ years options experience, "extensive" knowledge, $50k-$100k+ net worth, speculation objective.
- **Level 5 (naked index)**: 3-5+ years experience, "extensive" knowledge, $250k+ liquid net worth, often portfolio margin enabled.

A Registered Options Principal must approve. Denials can be appealed by adding documentation of experience (statements from prior brokers showing options trading) or by completing a smaller account first and reapplying after a track record is built.

## Why Brokers Tier

Two driving forces:

**Regulatory.** FINRA Rule 2360 requires diligent customer suitability assessment for options accounts. Brokers face fines, customer complaints, and FINRA arbitration awards if they grant a complete novice access to naked short index options and the customer blows up. Tier systems are the operational embodiment of suitability.

**Self-preservation.** A customer who loses more than their account equity creates a debit balance. The broker is legally entitled to collect, but in practice many such debits are uncollectable and become the broker's bad debt. The 2021 Robinhood-Archegos and 2018 catastrophic short-volatility blowups (e.g., the [[xiv-collapse-february-2018|XIV event]]) made every retail broker more conservative on uncovered short options. Tier limits protect the broker's balance sheet.

## Implications for ITPM-Style Portfolios

The [[itpm-trade-construction-playbook|ITPM trade construction playbook]] makes heavy use of:

- **Defined-risk debit and credit spreads** in equities and indices - these only require Level 3.
- **Premium selling on indices** (e.g., short SPX/XSP put spreads) - typically Level 3 if defined-risk; Level 4-5 if naked.
- **Calendar and diagonal time-spread structures** - Level 3.
- **Earnings vol structures** (iron condors, butterflies) - Level 3.
- **Tactical naked premium selling** to express a strong directional or vol view - Level 4 (equity) or Level 5 (index).
- **Adjustment legs** (rolling, defending, converting) - whatever tier the resulting structure occupies, which can shift mid-trade.

A self-directed ITPM-style trader at most retail brokers will hit a ceiling at Level 3 unless they:
1. Maintain a substantial account ($100k+ for naked equity, $250k+ for naked index in practice).
2. Apply for and pass [[portfolio-margin|portfolio margin]].
3. Document multi-year options trading history.

Robinhood and Webull users running ITPM-style books will find that some core ITPM structures (naked short index options, certain ratio spreads, undefined-risk strangles for premium income) are simply not available regardless of account size. Migrating to [[interactive-brokers|IBKR]], [[tastytrade|tastytrade]], or thinkorswim is the standard upgrade path.

## How to Get Approved for Higher Levels

Practical ladder for moving up:

1. **Start at Level 1-2** with a clean, accurate options application.
2. **Build a track record** at the current level for 6-12+ months. Brokers can pull statements showing actual trading.
3. **Reapply for Level 3** after demonstrating spread-style trading - typically straightforward if account size and answers are reasonable.
4. **Trade Level 3 structures consistently** for 1-2 years before requesting Level 4.
5. **Build account equity**. Net worth and account size are the single biggest factors at the top tiers.
6. **Apply for [[portfolio-margin|portfolio margin]]** once account equity exceeds the broker's threshold (typically $125k+). This often unlocks effective Level 5 capabilities even at brokers without an explicit Level 5 label.
7. **Migrate brokers if necessary**. Some brokers (Robinhood, Webull, M1) cap out at Level 3 regardless. Moving to IBKR, tastytrade, Schwab/thinkorswim, or Fidelity opens the upper tiers.
8. **Document experience honestly**. Lying on an options application can result in account closure and is, in extreme cases, securities fraud.

Denials are not permanent. Reapply after 6-12 months with updated income, net worth, and trading history.

## Related

- [[finra]] - the SRO behind Rule 2360
- [[regulation]] - umbrella concept page
- [[options-disclosure-document]] - the ODD that all customers must receive
- [[portfolio-margin]] - the alternate margin framework that effectively unlocks high-tier strategies
- [[pattern-day-trader-rule]] - separate but related FINRA rule affecting options day traders
- [[itpm-trade-construction-playbook]] - which strategies in the playbook need which tier
- [[interactive-brokers]], [[tastytrade]], [[etrade]], [[charles-schwab]], [[robinhood]], [[webull]] - broker-specific tier implementations
- [[xsp-vs-mes-futures]] - related comparison where MES sidesteps options-tier restrictions

## Sources

- FINRA Rule 2360 (Options) - account approval and supervision requirements.
- OCC "Characteristics and Risks of Standardized Options" (the Options Disclosure Document).
- Public options application forms and customer agreements from E*TRADE, Schwab, Fidelity, Interactive Brokers, tastytrade, Robinhood, and Webull.
- FINRA Rule 4210 (Margin Requirements) - margin treatment of option strategies.
- SEC Rule 9b-1 - disclosure requirements for standardized options.
