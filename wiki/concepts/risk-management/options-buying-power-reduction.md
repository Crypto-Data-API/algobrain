---
title: "Options Buying Power Reduction"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, risk-management, margin, position-sizing]
aliases: ["BPR", "Buying Power Reduction", "Options Margin Requirement", "Options BP", "Margin Reduction"]
related: ["[[margin]]", "[[portfolio-margin]]", "[[span-margin]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[options-position-sizing]]", "[[short-strangle]]", "[[iron-condor]]", "[[credit-spread]]", "[[naked-option]]", "[[options-premium-selling]]", "[[volatility-regime]]", "[[capacity-constraints]]", "[[liquidation-risk]]", "[[volmageddon]]", "[[delta]]", "[[implied-volatility]]"]
domain: [risk-management]
prerequisites: ["[[margin]]", "[[options-greeks]]", "[[options]]"]
difficulty: advanced
---

**Buying Power Reduction (BPR)** is the dollar amount a broker subtracts from a trader's available capital to collateralize an options position. Unlike a stock purchase — where BPR equals the cash outlay (or 50% under Reg-T) — options BPR is computed by a formula that depends on the structure (defined-risk vs undefined-risk), the underlying's volatility, and the margin regime (Reg-T, [[portfolio-margin]], or [[span-margin|SPAN]]). For short-premium portfolios, BPR — not premium collected, not theta — is usually the binding capacity constraint, and it **reprices in real time as [[implied-volatility|IV]] expands**, mechanically shrinking the book at exactly the moments tail risk is highest.

## Overview

The BPR question is: *how much of my account does this position consume?* Three answers exist depending on margin regime:

1. **Defined-risk position, any regime** — BPR = max loss = spread width × 100 − credit received. Predictable, simple, the same in Reg-T and [[portfolio-margin]].
2. **Undefined-risk position, Reg-T** — BPR is computed by a formula derived from CBOE Rule 12.3 / FINRA 4210, scaling with stock price and out-of-the-moneyness. Typically **20-30% of notional** for naked short options on equities.
3. **Undefined-risk position, [[portfolio-margin]] or [[span-margin|SPAN]]** — BPR is the worst loss across a grid of stress scenarios (typically ±15% spot × ±IV shifts). Often **3-5x more capital-efficient** than Reg-T for diversified short-premium books.

For an income trader running [[short-strangle|strangles]] and [[iron-condor|iron condors]], BPR is what determines how much theta the account can produce. A book whose theta target requires 60% BPR utilization in a 14-VIX environment will be **margin-deficient** if VIX moves to 24, because the existing positions' BPR will rise faster than the new theta they generate.

## Definition / Formulas

### Defined-risk structures

For [[credit-spread|vertical spreads]] (put credit spread, call credit spread, [[iron-condor|iron condor]], [[iron-butterfly|iron fly]]):

```
BPR = (max_loss_per_contract) * 100 * n_contracts
    = (spread_width − net_credit) * 100 * n_contracts
```

A 10-wide SPX put credit spread sold for $1.20 credit:
- Max loss = $10 − $1.20 = $8.80 per share
- BPR = $880 per contract

This is identical under Reg-T, portfolio margin, and SPAN. The defined-risk wrapper is a contract-level capital cap that the regulators and clearing houses honor.

### Undefined-risk: Reg-T (CBOE / FINRA standard)

For a naked short put or short call, Reg-T requires the **greater** of:

```
Method A (the "20% rule"):
  BPR = (0.20 * underlying_price − OTM_amount + option_premium) * 100

Method B (the "10% floor"):
  BPR = (0.10 * underlying_price + option_premium) * 100

For OTM puts only, OTM_amount cannot exceed the strike price.
BPR = max(A, B)
```

The 20% term (15% for indices in some implementations) is the dominant component for at-the-money or near-the-money strikes. The 10% floor binds only deep out-of-the-money.

Worked: short 1 SPX 4900 put with SPX at 5000, premium $20, IV moderate:
- Method A: (0.20 × 5000 − 100 + 20) × 100 = (1000 − 100 + 20) × 100 = **$92,000**
- Method B: (0.10 × 5000 + 20) × 100 = $52,000
- BPR = max = **$92,000**

Same put on SPY (price 500, premium $0.20):
- Method A: (0.20 × 500 − 1 + 0.20) × 100 = $99.20 × 100 = $9,920
- Method B: (0.10 × 500 + 0.20) × 100 = $5,020
- BPR = $9,920

### Undefined-risk: Portfolio Margin

[[portfolio-margin]] (available to PM-approved accounts $125K+ at most US brokers, $25K at tastytrade) computes BPR as:

```
BPR = max( |portfolio P&L| ) over a stress grid
```

For broad-based indices (SPX, NDX, RUT) the grid is **±6% spot** in 0.5% increments paired with **±IV scenarios**. For single-name equities the grid is **±15% spot**. The worst loss across the grid (subject to a $0.375 × shares minimum) is the BPR.

Same SPX 4900 put example under portfolio margin:
- Worst-case loss in the −6% scenario (SPX → 4700): put becomes ~$200 ITM
- BPR ≈ $20,000 per contract — roughly **4.6x more efficient** than Reg-T

This is why institutional and serious retail short-premium traders move to portfolio margin as soon as they qualify.

### Undefined-risk: SPAN (futures and futures options)

[[span-margin|SPAN]] (Standard Portfolio Analysis of Risk, CME's regime since 1988) uses 16 standardized **risk arrays** combining ±3 spot levels × ±2 vol levels plus extreme-move and inter-month scenarios. The worst loss is the initial margin. SPAN is portfolio-aware: a short ES strangle hedged by long ES futures gets the offset baked in. Effective capital efficiency is similar to portfolio margin, sometimes better for hedged structures.

### Margin-regime comparison at a glance

| Property | Reg-T | [[portfolio-margin\|Portfolio Margin]] | [[span-margin\|SPAN]] |
|----------|--------|------------------|------|
| Basis | Fixed formula (CBOE 12.3 / FINRA 4210) | Stress grid (±6% index / ±15% single-name × IV) | 16 risk arrays (±spot × ±vol) |
| Vol-aware | Weakly (premium term only) | Yes — grid widens in stress | Yes — exchange resets scan range |
| Portfolio-aware (offsets) | No | Yes | Yes |
| Min account | $2K | ~$125K (most brokers); $25K tastytrade | Futures account |
| Typical naked-put efficiency vs Reg-T | 1x (baseline) | ~4-5x more efficient | similar to PM |
| Reprices in real time | Slowly | Yes — intraday | Daily (exchange) + ad-hoc |
| Governs | US equity/index options | US equity/index options | Futures + futures options |

The headline: **Reg-T over-collateralizes undefined risk; PM and SPAN price it closer to true [[value-at-risk|VaR]] but reprice against you in a shock.** Neither defended-risk efficiency comes free — PM and SPAN trade lower calm-market BPR for higher stress-market BPR volatility.

## How It Works

### Why naked short puts/calls eat huge BPR under Reg-T

The Reg-T formula was written in the 1970s and is intentionally conservative. It treats every naked short option as if a 20% adverse move is *normal*. For a $5000-level index, that implies a $1000 buffer per contract regardless of strike. The structure is **insensitive to how OTM the option is** above the 10% floor and insensitive to current implied volatility — both features make Reg-T BPR much higher than any plausible loss for a 16-delta short put.

Empirically, on liquid index products under moderate IV:
- 16-delta short SPX put: Reg-T BPR ≈ $80-100K, true 1-day 99% VaR ≈ $5-8K. **10-15x over-margined.**
- 30-delta short SPX put: Reg-T BPR ≈ $90-110K, true 1-day 99% VaR ≈ $12-18K. **5-7x over-margined.**

This is why portfolio margin is transformative for short premium.

### How BPR scales with VIX (vol-aware margin reprices in stress)

Both Reg-T and portfolio-margin BPR rise when IV rises, but for different reasons:

- **Reg-T**: the `option_premium` term grows directly with IV. A short put paying $5 in VIX 14 might pay $15 in VIX 28. BPR rises by `(15 − 5) × 100 = $1000` per contract from that term alone, plus the OTM_amount may shrink as the underlying drops.
- **Portfolio margin**: the stress-grid scenarios use **higher absolute moves** when realized vol is high (the broker's risk engine often scales the grid by short-dated vol). BPR can rise 2-3x in a vol shock.
- **SPAN**: the **scanning range** parameter is updated daily by the exchange. A vol regime shift can trigger an explicit margin-multiplier increase (the CME does this manually after stress events; see [[march-2020-margin-changes]]).

The mechanics produce a brutal feedback loop: vol expands → existing positions lose money → BPR on *unchanged* positions rises → free buying power collapses → trader must close into a falling market → forced selling further compresses liquidity. This is the basic mechanism behind every short-vol blowup: [[volmageddon|Volmageddon 2018]], [[ljm-funds|LJM Preservation 2018]], [[allianz-structured-alpha|Allianz Structured Alpha 2020]], and many less famous individual blowups in March 2020 and August 2024.

### Practical BPR for canonical structures

Approximate BPR per contract in moderate-vol (VIX ~16) on liquid US index options:

| Structure | Reg-T BPR | Portfolio Margin BPR | Notes |
|---|---|---|---|
| Long 1 SPX call | premium debit | premium debit | Same in both regimes |
| 16-delta SPX [[short-strangle\|short strangle]] | ~$180K | ~$15-20K | The PM ratio (~10x) is the headline efficiency gain |
| 16-delta SPX [[iron-condor\|iron condor]], 50-pt wings | $4,400-$4,500 (max loss) | $4,400-$4,500 | Defined-risk; identical BPR |
| 30-delta short SPX put credit spread, 25-wide | $2,200-$2,400 | $2,200-$2,400 | Identical |
| 16-delta naked short SPX put | ~$95K | ~$20K | PM is 4-5x more efficient |
| 16-delta naked short put on $200 stock | ~$3,800 | ~$1,400 | Single-name PM uses ±15% grid, less generous |
| Short 1 ES strangle (futures option) | $9,000-$15,000 (SPAN) | n/a | SPAN regime |

These are approximate and broker-specific. [[tastytrade-platform|tastytrade]] tends to be more aggressive on PM than Schwab or Fidelity; interactive-brokers uses its own real-time risk model that often yields the lowest BPR for hedged books.

## Worked Example — BPR-Driven Capacity for a Theta-Targeted Book

Setting: $250K SPX-only short-premium account, $80/day calendar-day theta target ([[theta-targeting]]), portfolio margin enabled.

Structure: 45-DTE 16-delta SPX [[iron-condor|iron condors]], 50-pt wings, ~$13/day theta per contract. To hit $80/day target requires ~6 contracts.

**Capital math under PM (and Reg-T identical for defined-risk):**
- BPR per contract: ~$4,400 (max loss on 50-pt wings minus ~$6 credit)
- Total BPR: 6 × $4,400 = **$26,400**
- BPR utilization: 26,400 / 250,000 = **10.6%**
- Free BP: ~$223K — plenty of dry powder.

**Same theta with naked strangles instead:**
- 16-delta SPX strangle theta: ~$25/day per contract
- Contracts needed: 4
- PM BPR per contract: ~$18,000
- Total BPR: 4 × $18,000 = **$72,000** (PM)
- Total BPR under Reg-T: 4 × $180,000 = **$720,000** (impossible on $250K — the position cannot be opened at all under Reg-T)

The Reg-T account literally cannot run a 4-contract naked SPX strangle with $250K. Portfolio margin makes it possible but at 29% BPR utilization — meaningful capital concentration.

**Vol shock — VIX 16 → 24, no spot move:**

Under PM, the broker's stress grid widens. New per-contract BPR for the strangles rises to ~$28,000. Total book BPR: 4 × $28,000 = **$112,000** = **45% utilization**. The book can survive but is now operating with materially less dry powder. Adding any new positions is restricted by the higher BPR on existing ones.

For the iron condor variant: per-contract BPR is unchanged at $4,400 (defined risk). Total BPR remains $26,400. **The defined-risk book is unaffected by vol expansion at the BPR level**, freeing the trader to deploy *more* premium-selling into the richer environment rather than being forced to cut.

This is the primary reason tastytrade-style and other professional portfolios prefer defined-risk structures even though naked strangles harvest more theta per dollar of BPR in calm markets. **Vol-shock BPR resilience is what determines whether a book survives.**

## Common Misuse

- **Treating Reg-T BPR as the "true" risk** of a position. It's a regulatory minimum, often 5-15x the actual VaR. Sizing to Reg-T leaves enormous capacity unused.
- **Treating PM BPR as the "true" risk.** Portfolio margin reprices BPR in stress; the BPR you see at trade open is not the BPR you'll have during a shock. Stress-test BPR under +5 vol points, not just current.
- **Maxing out BPR at trade entry.** A book at 80% BPR utilization in calm markets has no room when vol spikes. Standard professional discipline: keep BPR utilization **under 35-40%** in calm markets, leaving 60% buffer for vol expansion and adjustments.
- **Confusing BPR with collateral.** BPR is the deduction from buying power; the broker may also require additional **maintenance margin** if a position moves against you. Both can rise simultaneously in a stress.
- **Ignoring the BPR of un-paired legs.** When closing one leg of a multi-leg structure, the remaining leg often becomes "undefined" and BPR jumps. Always close legs in an order that preserves the defined-risk wrapper.
- **Over-relying on cross-product offsets.** Some platforms net BPR for SPX vs SPY positions; many do not. Read the broker's [[portfolio-margin]] disclosure for the specific offsets recognized.

## BPR Utilization Decision Table

A practical discipline guide for a short-premium book. Utilization = total BPR ÷ account equity:

| BPR utilization | Vol regime | State | Recommended action |
|-----------------|------------|-------|--------------------|
| < 25% | Calm (low [[iv-rank-and-iv-percentile\|IVR]]) | Under-deployed | Room to add; check vega/theta budgets bind first |
| 25-40% | Calm | Healthy | Standard target zone; keep buffer for expansion |
| 40-55% | Calm | Stretched | Stop adding; pre-stage rolls/defenses |
| > 55% | Calm | Over-deployed | Trim; a routine vol pop forces liquidation |
| Any | Vol expanding (IV rising) | Repricing risk | Stress-test BPR at +5 to +10 vol points *before* it happens |
| Rising toward 80%+ | Stress | Danger | Close into the move while you still choose the trades |
| > 100% | Stress | Margin call | Broker liquidates — you lose trade selection ([[liquidation-risk]]) |

**Rule of thumb:** size so that a VIX 14→24 shock leaves utilization below ~60%. Defined-risk structures ([[iron-condor]], [[credit-spread]]) hold BPR flat through vol expansion; undefined-risk structures ([[short-strangle]], [[naked-option]]) do not. This single property is why defined-risk books survive shocks that liquidate naked books — see the worked example above.

## Linkage to Theta Targeting and Vega Budgeting

BPR is the third leg of the [[options-risk-budgeting|risk budgeting]] tripod alongside [[theta-targeting]] and [[vega-budgeting]]:

- **Theta target** sets the income objective (`$/day`).
- **Vega budget** caps the volatility-risk exposure (`$/IV point`).
- **BPR cap** sets the capital-deployment ceiling (`% of account`).

Any of the three can bind first. In a low-vol regime, vega is small per contract and the theta target binds via a high contract count, making BPR the bottleneck. In a high-vol regime, vega per contract is large and the vega budget binds, so BPR is rarely the issue. In the worst regime — *vol expansion mid-trade* — BPR rises while vega rises while theta target is harder to hit, and the trader is forced to cut into adverse pricing.

Practitioners track all three simultaneously. See [[options-risk-budgeting]] for the integrated framework and [[options-portfolio-construction]] for trade-by-trade sizing.

## Related

- [[margin]] — general margin mechanics
- [[portfolio-margin]] — risk-array regime that dramatically reduces BPR
- [[span-margin]] — futures-options analogue (CME)
- [[theta-targeting]] — the income side of the sizing tripod
- [[vega-budgeting]] — the vol-risk side of the sizing tripod
- [[options-position-sizing]] — Greeks-based sizing that lives downstream of BPR
- [[short-strangle]], [[iron-condor]], [[credit-spread]] — canonical structures with very different BPR profiles
- [[volmageddon]], [[allianz-structured-alpha]] — case studies of BPR-driven blowups
- [[liquidation-risk]] — what happens when BPR exceeds account equity
- [[capacity-constraints]] — BPR as the binding constraint on book size
- [[iv-rank-and-iv-percentile]] — the vol-regime gauge that drives BPR repricing
- [[implied-volatility]] — the input that reprices undefined-risk BPR in stress
- [[delta-hedging]] — short-vol hedged books consume BPR per this page's formulas
- [[delta]] — the directional Greek that feeds the Reg-T and PM grids
- [[market-regime]] — calm vs stress determines BPR resilience
- [[value-at-risk]] — the true-risk benchmark Reg-T over-collateralizes against

## Sources

- CBOE Rule 12.3 — Margin requirements for option positions.
- FINRA Rule 4210 — Customer margin requirements.
- CFTC / CME SPAN methodology documentation.
- [[tastytrade-portfolio-margin-research]] — empirical comparison of PM vs Reg-T BPR for canonical short-premium structures.
- [[book-option-volatility-and-pricing]] — Natenberg on margin as a portfolio-level risk constraint.
- Schwab / Interactive Brokers / tastytrade margin disclosure documents (per-broker variations in PM grid widths).
