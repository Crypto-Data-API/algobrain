---
title: "Interest Rate Swaps"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [derivatives, interest-rates, macro, risk-management, leverage]
aliases: ["Interest Rate Swap", "IRS", "Plain Vanilla Swap", "Fixed-for-Floating Swap"]
related: ["[[interest-rates]]", "[[yield-curve]]", "[[bond-market]]", "[[duration]]", "[[derivatives]]", "[[basis-trade]]", "[[carry-trade]]", "[[fed-policy]]", "[[volatility]]"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[interest-rates]]", "[[bond-market]]"]
difficulty: intermediate
---

An **interest rate swap (IRS)** is an over-the-counter derivative in which two counterparties agree to exchange streams of interest payments on a notional principal amount over a fixed term. In the canonical *plain-vanilla* swap, one party pays a **fixed rate** and receives a **floating rate** (historically LIBOR, now [[interest-rates|SOFR]], EURIBOR, etc.), while the other does the reverse. No principal changes hands; only the net interest difference is settled periodically. Swaps are the largest interest-rate derivative market in the world — the notional outstanding runs into the hundreds of trillions of dollars — and they are the primary tool institutions use to manage, hedge, or speculate on [[interest-rates|interest-rate]] exposure.

## Overview / Mechanics

A plain-vanilla fixed-for-floating swap has these components:

- **Notional principal** — the reference amount used to compute payments (e.g. $100m). It is never exchanged.
- **Fixed leg** — the *swap rate*, set at inception so the swap has zero value to both parties on day one.
- **Floating leg** — resets each period to a reference rate (e.g. 3-month SOFR) plus/minus a spread.
- **Tenor** — the life of the swap (2y, 5y, 10y, 30y are the liquid points).
- **Payment frequency** — fixed leg often annual/semi-annual; floating leg quarterly.

Each settlement, the parties net the two legs:

```
net_payment = notional * (fixed_rate - floating_rate_for_period) * day_count_fraction
```

If the floating rate rises above the fixed rate, the fixed-rate payer profits (they locked in the lower fixed cost); if rates fall, the fixed-rate receiver profits.

### Valuation

A swap is valued as the difference between the present value of the two legs, discounted off the appropriate curve (post-2008, OIS/SOFR discounting):

```
V_swap (to fixed payer) = PV(floating leg) - PV(fixed leg)
                        = notional * [ (1 - DF_n) - fixed_rate * Σ (DF_i * τ_i) ]
```

where `DF_i` are discount factors and `τ_i` are accrual fractions. At inception the fixed rate is chosen so `V = 0`. The **par swap rate** is therefore:

```
swap_rate = (1 - DF_n) / Σ (DF_i * τ_i)
```

This makes the swap curve essentially a smoothed, credit-clean version of the [[yield-curve|government yield curve]], and **swap spreads** (swap rate minus the same-maturity Treasury yield) are a watched gauge of funding stress and balance-sheet costs.

### DV01 and duration

A swap's risk is measured in **DV01** (dollar value of a 1bp move). Receiving fixed is economically like being *long* a bond (positive [[duration]]); paying fixed is like being *short* a bond. A 10-year swap carries roughly the same rate risk as a 10-year Treasury of equal notional, which is why swaps are the cheapest, most capital-efficient way to add or strip duration without buying or shorting cash bonds.

## Why Swaps Exist (the edge / use cases)

1. **Liability transformation.** A corporate with floating-rate bank debt can pay-fixed/receive-floating to convert it to synthetic fixed-rate debt, locking in borrowing costs. Conversely, a fixed-rate borrower expecting rate cuts can swap to floating.
2. **Asset-liability management.** Banks, insurers, and pension funds use swaps to match the duration of assets to liabilities. Pensions with long-dated liabilities are structural *receivers* of long-end fixed rates — a flow that helps explain persistently low/negative long-end swap spreads.
3. **Speculation / macro expression.** A trader who thinks the [[fed-policy|Fed]] will hike more than the market expects can *pay fixed* on a swap to profit if rates rise — a leveraged, capital-efficient alternative to shorting bond [[futures]].
4. **Curve and relative-value trades.** Swaps express curve steepeners/flatteners (e.g. receive 2y / pay 10y) and feed the [[basis-trade|swap-spread basis]] between cash Treasuries and swaps.

## Variants

- **Overnight Index Swap (OIS)** — floating leg references a compounded overnight rate (SOFR, ESTR, SONIA). The OIS curve is the modern risk-free discounting benchmark.
- **Basis swap** — exchanges two floating rates (e.g. 1m SOFR vs 3m SOFR, or cross-currency basis).
- **Cross-currency swap** — exchanges principal and interest in two different currencies; central to [[carry-trade|FX funding]] and the cross-currency basis.
- **Forward-starting swap / swaption** — a swap that begins later, or an option on a swap (the building block of interest-rate volatility trading).
- **Amortizing / accreting swaps** — notional changes over time to match a loan schedule.

## The LIBOR → SOFR Transition

Following the LIBOR manipulation scandals, the global benchmark for floating legs shifted from **LIBOR** (an unsecured term rate based on bank submissions) to **SOFR** (Secured Overnight Financing Rate, a transaction-based overnight Treasury repo rate) in the US, with USD LIBOR ceasing for new contracts after 2021 and remaining tenors ending by mid-2023. SOFR is an overnight, risk-free, secured rate, so swap conventions moved to compounding-in-arrears and OIS-style discounting. Other jurisdictions adopted SONIA (UK), ESTR (EU), TONA (Japan).

## Trading / Portfolio Relevance

- **Capital-efficient duration.** Swaps let a portfolio add or remove [[interest-rates|rate]] exposure with minimal cash outlay vs. buying cash bonds, freeing balance sheet — central to [[risk-parity]] and overlay strategies.
- **Hedging.** Bond portfolios, mortgage books, and corporate liabilities are hedged by paying or receiving fixed to neutralize DV01.
- **A read on rate expectations.** The swap curve and forward swap rates embed the market's path for policy rates; deviations from the [[yield-curve|Treasury curve]] (swap spreads) signal funding and balance-sheet stress, as seen when swap spreads went sharply negative post-2008 and during the 2020 dash-for-cash.
- **Counterparty / clearing risk.** Standardized swaps now clear through CCPs (LCH, CME) with daily margin, mutualizing the bilateral counterparty risk that amplified the [[2008-global-financial-crisis|2008 crisis]] (AIG's uncleared CDS/rate exposure being the cautionary tale). Margin calls on swap books are themselves a [[volatility|volatility]] transmission channel — the 2022 UK gilt/LDI crisis was a forced-deleveraging of pension swap and repo positions.

## Related

- [[interest-rates]] — the underlying the swap references
- [[yield-curve]] — swaps trade as a near-mirror of the curve; swap spreads vs. Treasuries
- [[duration]] — receive-fixed = long duration; pay-fixed = short duration
- [[bond-market]] — cash-bond alternative to synthetic swap exposure
- [[derivatives]] — swaps are the largest OTC derivative class
- [[basis-trade]] — swap-spread and cross-currency basis trades
- [[carry-trade]] — cross-currency swaps as FX funding
- [[fed-policy]] — policy path drives the floating leg and the curve
- [[volatility]] — swaptions and margin dynamics

## Sources

- BIS OTC derivatives statistics — notional and gross market value of interest rate swaps.
- ISDA — standard swap documentation, the IBOR transition, and clearing/margin frameworks.
- Federal Reserve Bank of New York — SOFR methodology and the LIBOR transition timeline.
- Hull, J. *Options, Futures, and Other Derivatives* — swap valuation and the par-swap-rate derivation.
