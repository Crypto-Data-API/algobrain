---
title: "MOVE Index"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [bonds, volatility, derivatives, indicators, treasuries, rates, fixed-income, ice, bofa]
aliases: ["MOVE", "ICE BofA MOVE Index", "Merrill Option Volatility Estimate", "Bond VIX", "Treasury VIX"]
domain: [market-microstructure, indicators, fixed-income]
prerequisites: ["[[implied-volatility]]", "[[treasuries]]", "[[options]]"]
difficulty: intermediate
related: ["[[vix]]", "[[implied-volatility]]", "[[treasuries]]", "[[tlt]]", "[[ief]]", "[[bond-volatility]]", "[[interest-rate-options]]", "[[swaption]]", "[[10-year-treasury]]", "[[2-year-treasury]]", "[[fed-funds-rate]]", "[[fomc-meetings]]", "[[duration-risk]]", "[[carry-trade]]", "[[long-vol-vs-short-vol]]", "[[options-concentration-risk]]", "[[tail-risk-hedging]]", "[[volatility-regime-classification]]", "[[ice-bofa]]", "[[march-2023-banking-crisis]]"]
---

The **MOVE Index** (officially the **ICE BofA MOVE Index**, ticker **MOVE**) is the bond-market analogue of the [[vix|VIX]]: a yield-curve-weighted index of one-month [[implied-volatility]] across the most liquid US Treasury maturities (2-year, 5-year, 10-year, and 30-year). It is the canonical measure of *forward-looking* US Treasury volatility and the single most-watched indicator of stress in the global rates complex. While VIX measures equity vol, MOVE measures the volatility the options market is pricing into Treasuries — and because Treasuries are the global reserve duration asset, the MOVE Index propagates risk pricing into mortgages, credit, FX, and emerging-market debt. A short premium book that ignores MOVE is implicitly assuming the rates regime stays calm; a [[options-concentration-risk|properly diversified]] book uses MOVE-driven structures as one of its uncorrelated [[long-vol-overlay|long-vol overlays]].

## Origin and Construction

The MOVE Index was created by **Harley Bassman** at Merrill Lynch in **1988** to give bond traders a single number for cross-tenor implied vol. It was originally branded the "Merrill Option Volatility Estimate." After Bank of America acquired Merrill Lynch in 2008, the index continued under the BofA Merrill brand. In **2019**, Intercontinental Exchange (ICE) acquired the index family and rebranded it the **ICE BofA MOVE Index**.

### Methodology

The index is a yield-curve-weighted average of normalized one-month at-the-money [[swaption]] (or Treasury option) implied volatilities at four key tenors:

| Component | Weight | What it captures |
|---|---|---|
| 2-year ATM 1m IV | 0.20 | Short-end / Fed expectations vol |
| 5-year ATM 1m IV | 0.20 | Belly / cycle vol |
| 10-year ATM 1m IV | 0.40 | Benchmark duration vol |
| 30-year ATM 1m IV | 0.20 | Long-end / inflation expectations vol |

The 10-year tenor receives **double weight** because it is the global benchmark duration asset and the most actively hedged.

The output is expressed in **basis points per annum** — a MOVE level of 100 means options are pricing a one-standard-deviation 1-month move in 10-year yields of about 28-29 basis points (100 / sqrt(12) ≈ 28.9).

### Conversion to Yield Move

A common shorthand: **monthly expected one-sigma 10-year yield move ≈ MOVE / sqrt(12)**.

| MOVE level | Implied 1-month 10y move | Regime |
|---|---|---|
| 60-80 | ~17-23 bp | Calm — rare since 2021 |
| 80-110 | ~23-32 bp | Normal range |
| 110-150 | ~32-43 bp | Stressed |
| 150-200 | ~43-58 bp | Crisis |
| 200+ | 58+ bp | Tail event (banking, default scares) |

### Worked conversion (illustrative)

*(Numbers below illustrate the arithmetic, not a live quote.)* Suppose MOVE reads **130**:

```
1-month expected 1σ 10y yield move ≈ MOVE / sqrt(12)
                                    = 130 / 3.464
                                    ≈ 37.5 basis points
```

So at MOVE = 130, the options market is pricing roughly a two-thirds chance the 10-year yield moves less than ~37 bp over the next month, and a one-third chance it moves more — in either direction. Translating to price: a 37 bp move on a 10-year note (duration ≈ 8.5) implies a price swing of roughly `8.5 × 0.375% ≈ 3.2%`, and on [[tlt]] (duration ≈ 16-17) closer to `~6%`. This is why a MOVE jump from 100 to 150 is a material widening of the expected [[tlt]] trading range, not a cosmetic number change.

## Historical Levels and Notable Events

| Period | MOVE level | Context |
|---|---|---|
| 1990s normal | 80-100 | Calm rates regime |
| 2008-09 GFC peak | 200+ | Treasury rally and panic |
| 2010-2019 (post-QE) | 50-90 | Suppressed rate vol due to forward guidance and QE |
| March 2020 (COVID) | 160+ | Rate-vol spike; Treasury market dysfunction |
| Mid-2021 | 50-65 | All-time-low rate vol; Fed extended forward guidance |
| Q1 2022 | 90-110 | Inflation print acceleration |
| Q2 2022 | 130-150 | Aggressive Fed hiking cycle begins |
| October 2022 | 160 | Gilts crisis (UK LDI), peak hiking-cycle uncertainty |
| March 2023 | 198 (intraday) | [[march-2023-banking-crisis|SVB / banking crisis]] — largest 2-day move in 10y yields since 1987 |
| 2024 | 90-130 | Elevated baseline — "new normal" since hiking cycle |
| 2025-2026 (current) | 80-115 | Range-bound at structurally higher level than pre-2022 |

The defining structural fact since 2022: **MOVE has not returned to its 2010-2019 lows**. The post-pandemic rate-vol regime shifted permanently higher as central banks abandoned forward guidance and inflation persistence reintroduced two-way risk into the rates curve.

## Why MOVE Matters

### 1. Cross-Asset Spillover

Bond vol does not stay in bonds:

- **Mortgages.** Mortgage-backed securities have negative convexity (prepayment risk); a MOVE spike forces MBS portfolio managers to sell duration, accelerating Treasury moves.
- **FX.** [[carry-trade|Carry trades]] are short rate-vol; a MOVE spike unwinds carry positions, particularly in JPY and EM currencies. The [[vix-august-2024-spike|August 2024 yen-carry unwind]] coincided with a MOVE spike.
- **Credit.** Investment-grade and high-yield credit spreads widen mechanically with rate vol because corporate balance sheet duration becomes harder to hedge.
- **Equities.** Higher MOVE implies higher cost of equity (via DCF discount rate uncertainty) and reduces multiples on long-duration equity assets (tech, biotech).

### 2. Predictor of Crises

A rising MOVE is a leading indicator of:

- Sovereign debt crises (Eurozone 2011-2012)
- Banking stress ([[march-2023-banking-crisis|SVB 2023]])
- Carry trade unwinds ([[vix-august-2024-spike|August 2024]])
- Mortgage market dislocations (2008, 2020)

Empirically, sustained MOVE > 130 has preceded most major rates-driven dislocations of the past 20 years.

### 3. Input to Variance Risk Premium Calculations

Just as VIX defines the equity [[variance-risk-premium]], MOVE defines the rates VRP. Short rate-vol strategies (selling [[swaption|swaptions]], short-vol Treasury overlays) are paid the VRP between MOVE-implied vol and realized Treasury vol — typically 1-3 vol points per year in calm regimes.

### 4. Diversification for Equity Vol Books

Equity vol (VIX) and rate vol (MOVE) are correlated but imperfectly. A short premium book that sells *only* equity vol is concentrated; adding a sleeve of short rate-vol via MOVE-related structures (or directly via swaptions) provides genuine diversification — different macro driver, different participant base, different shock cycle.

## How to Trade MOVE

The MOVE Index itself is **not directly tradable** — it is a calculated index, like VIX. Exposure is gained through:

| Instrument | Direction | Notes |
|---|---|---|
| **OTC interest-rate swaptions** | Long or short | Most direct exposure; institutional-only |
| **TY (10-year Treasury futures) options** | Long or short | Listed on CME; closest retail equivalent |
| **TLT options** | Long or short | ETF on long-duration Treasuries; retail-accessible |
| **IEF options** | Long or short | ETF on 7-10 year Treasuries; retail-accessible |
| **MOVE-linked structured notes** | Long | Issued by major banks; not standardized |
| **CME interest rate volatility (CVOL) futures** | Long or short | Newer product; tracks 10y rate vol implied surface |

Most retail users trade rate vol via [[tlt]] options, accepting basis risk vs the MOVE Index in exchange for listed liquidity and standard margin treatment.

## MOVE vs VIX

The two most-watched implied-vol indices, compared:

| Dimension | VIX | MOVE |
|---|---|---|
| Underlying | SPX 30-day implied vol | UST 1-month implied vol (yield-curve-weighted) |
| Units | Annualized vol points (% per year) | Basis points per annum |
| Inception | 1993 (revised methodology 2003) | 1988 |
| Manager | Cboe Global Markets | ICE BofA |
| Tradable instruments | VIX futures, VIX options | Indirect (swaptions, TY options) |
| Typical range | 12-25 normal; 30-80 stress | 80-130 normal; 150-200 stress |
| Correlation to spot underlying | Strong negative (vol-up = equity-down) | Symmetric (vol-up = both directions matter) |
| Crowding | Heavily traded; retail and institutional | Mostly institutional |
| Settlement quirk | SOQ from SPX option opens | No direct settlement (calculated index) |

## MOVE in Options-Concentration-Risk Context

A short premium book on US equities (single-name strangles, SPX iron condors, [[short-strangle|short strangles]]) is implicitly:

- Short equity vol ([[vix]])
- Short rate vol (MOVE) — because equity downside scenarios usually involve rates spikes
- Short credit vol — because credit spreads widen in equity downside scenarios

These three risks are correlated *in stress* but **not in calm** — meaning the apparent diversification of the equity vol book hides correlated exposures. Adding **short rate-vol** (more concentration) or **long rate-vol** ([[long-vol-overlay|long-vol overlay]]) explicitly via MOVE-linked structures rebalances the book's vol-regime exposure.

The [[options-concentration-risk]] page recommends MOVE-driven long-vol overlays specifically for this reason: the rates vol surface frequently leads equity vol surface, so a long-MOVE structure can pay off *before* short equity vol gets into trouble.

## Calm vs Crisis Regime Behaviour

| Regime | MOVE level | Implied 10y monthly move | What it means |
|---|---|---|---|
| **Calm** | < 80 | < 23 bp | Suppressed rate vol; rare since QE era |
| **Normal** | 80-110 | 23-32 bp | Standard range |
| **Stressed** | 110-150 | 32-43 bp | Hiking cycle, mid-cycle inflation surprises |
| **Crisis** | 150-200 | 43-58 bp | Banking dislocation, sovereign concerns |
| **Tail event** | 200+ | 58+ bp | Market dysfunction (March 2020, March 2023) |

Compared to VIX, MOVE moves more deliberately — it rarely doubles intraday like VIX did in 2018 or 2024. But a sustained move from 80 to 150+ over 6-8 weeks (as happened in early 2022) is itself a regime change with persistent cross-asset effects.

## Common Misuse / Pitfalls

1. **Comparing MOVE to VIX in raw points.** They are in different units — MOVE is basis points of *yield* volatility, VIX is annualized *percentage* equity volatility. "MOVE is 120 and VIX is 18, so bonds are scarier" is meaningless. Compare each to its *own* history and regime table.

2. **Treating the post-2022 baseline as the long-run normal.** MOVE's structurally higher range since 2022 (80-130) reflects the abandonment of forward guidance. A short rate-vol strategy calibrated only on 2010-2019 data ([[implied-volatility]] suppressed by QE) will badly misprice the current variance risk premium. Segment by regime — see [[volatility-regime-classification]].

3. **Assuming MOVE is tradable.** It is a calculated index, like [[vix|VIX]] *before* VIX futures existed — there is no direct MOVE future or option. Exposure is via [[swaption|swaptions]], TY options, or [[tlt]]/[[ief]] options, each carrying basis risk to the index itself.

4. **Ignoring the spillover lead/lag.** Rate vol frequently *leads* equity vol into stress (mortgages and carry unwind first). Watching only [[vix]] while short a rate-sensitive book misses the earliest warning. The [[options-concentration-risk]] page leans on exactly this lead for [[long-vol-overlay|long-vol overlays]].

5. **Conflating the level with the change.** A MOVE *level* of 110 in a falling-vol regime and the same 110 on the way up to a crisis are very different signals. Direction and rate-of-change matter as much as the absolute reading.

6. **Forgetting tenor mix.** MOVE is yield-curve-weighted with the 10y double-weighted. A spike driven by short-end (Fed-repricing) vol is a different macro story than one driven by long-end (term-premium / inflation) vol, even at the same headline level.

## Related

- [[vix]] — the equity-vol counterpart
- [[implied-volatility]] — the underlying concept
- [[treasuries]] — the asset class measured
- [[tlt]] — long-duration Treasury ETF; primary retail vehicle for MOVE-related trades
- [[ief]] — 7-10 year Treasury ETF
- [[bond-volatility]] — broader topic
- [[interest-rate-options]] — the underlying instruments
- [[swaption]] — the OTC option on a swap; primary input to MOVE
- [[10-year-treasury]] — most heavily weighted MOVE component
- [[2-year-treasury]] — short-end MOVE component
- [[fed-funds-rate]] — primary driver of short-end vol
- [[fomc-meetings]] — primary catalyst for MOVE spikes
- [[duration-risk]] — what MOVE measures the volatility of
- [[carry-trade]] — strategy short rate-vol
- [[long-vol-vs-short-vol]] — the framework
- [[options-concentration-risk]] — context for diversifying with rate-vol overlays
- [[tail-risk-hedging]] — related strategy class
- [[volatility-regime-classification]] — applies to rate vol as well as equity vol
- [[march-2023-banking-crisis]] — recent MOVE crisis spike

## Sources

- ICE Data Indices, *MOVE Index Methodology* (current edition)
- Bassman, Harley. Original 1988 Merrill Lynch publication on the MOVE construction (*Convexity Maven* archive contains historical commentary).
- Bank for International Settlements, *Quarterly Review* — periodic commentary on global rate-vol regimes
- Federal Reserve Bank of New York, *Liberty Street Economics* — research on Treasury market dysfunction and rate-vol spikes
- Various sell-side rates-strategy desks (Goldman, JPMorgan, Citi) — recurring MOVE Index commentary
- Bhansali, Vineer. *Tail Risk Hedging* (2014) — section on rate-vol overlays
