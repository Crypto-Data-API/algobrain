---
title: "Beta-Weighted Delta"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, derivatives, risk-management, indicators, portfolio-theory]
aliases: ["Beta-Weighted Delta", "SPY-Equivalent Delta"]
related: ["[[delta]]", "[[options-greeks]]", "[[options-risk-budgeting]]", "[[portfolio-greeks-aggregation]]", "[[delta-neutral]]", "[[beta]]", "[[risk-navigator]]", "[[thinkorswim]]", "[[scenario-analysis]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[delta]]", "[[options-greeks]]", "[[beta]]"]
difficulty: advanced
---

**Beta-weighted delta** translates raw option deltas across heterogeneous underlyings into a single benchmark-equivalent number — typically expressed in SPY shares (or SPX dollars). Without this translation, a portfolio-level delta is meaningless: 100 long deltas of MSFT is not the same directional exposure as 100 long deltas of TLT, because their dollar values and market betas differ. Every serious options risk system (thinkorswim Analyze, IBKR Risk Navigator, orats, livevol) computes beta-weighted deltas natively and treats them, not raw deltas, as the binding directional constraint inside [[options-risk-budgeting]].

## Overview

Raw [[delta]] tells you how an option's price moves per $1 move in *its own underlying*. When you aggregate deltas across a multi-name book, you are summing dollars of MSFT exposure with dollars of TLT exposure with dollars of [[gold|GLD]] exposure — three different return streams with three different volatilities and three different correlations to the broad market. The resulting "net delta" number has no operational meaning. You cannot use it to size, to scenario, or to hedge.

Beta-weighting rescales every position's delta into the units of a chosen benchmark — usually SPY for equity-heavy retail books, [[spx|SPX]] for institutional books, or a sector ETF for sector-concentrated sleeves. After rescaling, summing across the book produces a single number — *SPY-equivalent delta* — that answers a clean question: "If SPY moves 1%, what is my expected book P&L from delta alone?"

This number can then be capped, hedged with index futures or SPY shares, and integrated into a [[scenario-analysis|scenario grid]]. Raw deltas cannot.

## Definition / Formula

For a position in underlying *i*, with raw delta Δᵢ (in shares of *i*), the beta-weighted delta to a benchmark *B* is:

```
BWDᵢ = Δᵢ × (Pᵢ / P_B) × βᵢ,B
```

Where:
- **Δᵢ** = raw delta of the position, in shares of *i* (e.g., a long 100 ATM MSFT call has Δ ≈ +50)
- **Pᵢ** = price of underlying *i*
- **P_B** = price of benchmark *B*
- **βᵢ,B** = beta of *i* against *B*, typically estimated from 60-day or 1-year rolling daily returns

The portfolio beta-weighted delta is then the sum across all positions:

```
BWD_portfolio = Σᵢ BWDᵢ
```

Interpretation: BWD_portfolio is in units of *benchmark shares*. A BWD of +500 SPY means the book behaves directionally like a long position of 500 SPY shares — a 1% move in SPY produces roughly 500 × 0.01 × P_SPY ≈ $2,500 of P&L (at SPY ≈ $500).

### Why each factor matters

- **Δᵢ** alone is in shares of *i* — different underlyings, not summable.
- **(Pᵢ / P_B)** rescales to dollar terms, then back into benchmark shares. A delta of 100 in a $400 stock is 4× the dollar exposure of delta 100 in a $100 stock, and the formula reflects that.
- **βᵢ,B** rescales for the *correlation and amplitude* of *i*'s moves relative to *B*. A high-beta name (β = 1.6) moves 60% more than the benchmark on average, so 1 share of it acts like 1.6 SPY shares.

The three factors compose multiplicatively: dollar exposure × beta-amplification × benchmark-share denomination.

## Why It Matters (for risk-budgeted books)

Inside [[options-risk-budgeting]], the *net delta budget* is one of the six binding caps (delta, gamma, vega, theta, rho, scenario). That cap is meaningless unless deltas are comparable. Specifically:

1. **Cap enforcement.** A book with +200 deltas of MSFT, +200 of NVDA, and -200 of TLT looks delta-neutral on paper. After beta-weighting it might be +850 SPY-equivalent deltas — heavily long. The raw cap was wrong; the BWD cap binds correctly.
2. **Hedge sizing.** If the BWD is +400 SPY-eq and the manager wants to flatten directional exposure, they short 400 SPY (or the equivalent SPX or ES futures). Without beta-weighting, the trader has no idea how much index exposure to short.
3. **Scenario consistency.** A "SPX -5%" stress requires translating that index move into per-name moves via beta. The same beta used for hedging should drive the scenario, otherwise hedge and stress are inconsistent.
4. **Cross-asset books.** Mixing equities, ETFs, bonds (TLT), and commodities (GLD, USO) is impossible without a common factor. SPY-beta is the simplest common denominator; sophisticated desks decompose into multiple factors ([[size-factor]], [[value-factor]], duration, gold, USD).

A book that monitors only raw deltas can be running 3-4× the directional risk it thinks it is.

## Worked Example

A $250k account holds the following positions, all referenced to SPY at $500:

| Position | Raw Δ | Pᵢ | βᵢ,SPY | (Pᵢ/P_B) × βᵢ | BWDᵢ (SPY shares) |
|---|---|---|---|---|---|
| Long 5 MSFT 30D 420 calls (Δ=0.55 each, ×100) | +275 | $420 | 1.05 | 0.882 | **+243** |
| Long 3 NVDA 30D 800 calls (Δ=0.50 each, ×100) | +150 | $800 | 1.85 | 2.96 | **+444** |
| Short 4 TLT 45D 95 puts (Δ=+0.30 each, ×100) | +120 | $95 | -0.20 | -0.038 | **-5** |
| Long 2 GLD 60D 200 calls (Δ=0.45 each, ×100) | +90 | $200 | 0.10 | 0.040 | **+4** |
| Short 10 SPY 30D 510 calls (Δ=0.45 each, ×100) | -450 | $500 | 1.00 | 1.00 | **-450** |
| **Net** | **+185** | | | | **+236** |

Two observations:

1. **Raw net delta is +185 — looks lightly long.** The trader thinks they are roughly market-neutral.
2. **Beta-weighted delta is +236 SPY-eq.** Once you account for NVDA's 1.85 beta, the apparent neutrality disappears. NVDA alone contributes +444 SPY-eq deltas — more than the entire raw net delta of the book.

The book is in fact a *concentrated long-NVDA bet wearing a market-neutral disguise*. A 5% SPY decline drags NVDA down ~9.25% (β × 5%), and that single position dominates the P&L.

To genuinely flatten directional exposure, the trader shorts 236 SPY shares (or 1 SPX micro futures contract, ~50 SPY-eq deltas each). After this hedge, BWD is ≈ 0 and the book becomes a pure relative-value bet on NVDA outperforming SPY by its idiosyncratic component.

### thinkorswim and IBKR Risk Navigator

Both platforms compute BWD natively. In thinkorswim's *Analyze → Risk Profile* tab, the user selects a "Beta Weighting" symbol (typically SPX or SPY); the position list, P&L plot, and aggregated Greeks immediately rescale. IBKR Risk Navigator does the same via its *Equity → Beta Weighting* setting. Beta is computed by the platform from a configurable lookback (often 60 days of daily returns); advanced users can override with custom betas for stress testing.

## Common Misuse / Pitfalls

1. **Beta is unstable.** Single-name betas computed on 60-day daily returns fluctuate widely. NVDA's beta to SPY ranged from ~1.3 to ~2.4 in 2023-2024 depending on regime. A BWD computed at one moment can be materially wrong a month later. *Mitigation*: use a longer lookback (1 year) for stability; recompute betas at least weekly; stress with both high-beta and low-beta scenarios.

2. **Beta is regime-dependent.** Stocks that look low-beta in calm regimes often blow up to β ≈ 1.5+ in [[risk-off|risk-off]] selloffs (correlation rush). The 60-day β captures the recent regime, not the next one. *Mitigation*: also track *downside beta* and *crisis beta* (regression conditional on SPX < -1%).

3. **High-beta single names misbehave in stress.** β assumes a linear relationship; in reality, 5x-leveraged names ([[mstr|MSTR]], 3x-ETFs) and crypto-proxies can move 3-5× the implied β prediction in a tail event. BWD will *understate* the true directional risk for these names.

4. **Beta is asymmetric.** Some names (e.g., [[gold|GLD]]) have negative beta but only in panics; in calm markets they barely correlate. A static β = 0.05 is misleading. *Mitigation*: compute upside and downside betas separately.

5. **OTM option deltas are themselves unstable.** A 5-delta short put has a small BWD until vol moves — then it can become a 25-delta short put overnight ([[vanna]] effect). BWD that ignores vega-driven delta drift undersizes the true directional risk. See [[vanna]] and [[gamma-pnl]].

6. **Multi-factor risk requires more than SPY.** A book mixing equities and bonds cannot be summarized by SPY beta alone. TLT has β ≈ -0.2 to SPY but a duration of 17 years — a Fed surprise moves it 5-10% with no SPY move. Use a multi-factor BWD (SPY-beta + duration + USD + gold) for cross-asset books.

7. **Confusing beta-weighted delta with dollar delta.** *Dollar delta* = Δᵢ × Pᵢ (no beta), measuring dollar exposure to the underlying. *Beta-weighted delta* = dollar delta / P_B × β, in benchmark shares. Different things. Most platforms report both — read the units.

## Related

- [[delta]] — raw first-order Greek that BWD rescales
- [[options-greeks]] — primer on the Greek family
- [[options-risk-budgeting]] — the framework that uses BWD as its delta cap
- [[portfolio-greeks-aggregation]] — math of summing Greeks across underlyings
- [[delta-neutral]] — special case where BWD = 0
- [[beta]] — the regression coefficient input to BWD
- [[scenario-analysis]] — uses beta to translate index shocks into per-name moves
- [[gamma-pnl]] — companion concept; BWD is wrong if gamma is large
- [[vanna]] — IV moves shift delta, breaking the BWD snapshot
- [[risk-navigator]] — IBKR's BWD implementation
- [[thinkorswim]] — TOS Analyze tab for BWD

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on portfolio-level Greek aggregation and beta-adjustment for cross-name books
- [[book-options-futures-other-derivatives]] — Hull's treatment of delta hedging across heterogeneous underlyings
- [[itpm-trade-construction-playbook]] — ITPM curriculum on beta-weighting as the discipline that makes a book's "directional bias" a real number
