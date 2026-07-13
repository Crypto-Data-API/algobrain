---
title: "SOFR (Secured Overnight Financing Rate)"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [bonds, derivatives, risk-management, treasuries, market-microstructure]
aliases: ["SOFR", "sofr", "Secured Overnight Financing Rate"]
related: ["[[risk-free-rate]]", "[[fed-funds-rate]]", "[[libor]]", "[[interest-rate-swaps]]", "[[floating-rate-notes]]", "[[bonds]]", "[[derivatives]]", "[[quantitative-easing]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[risk-free-rate]]"]
difficulty: intermediate
---

The **Secured Overnight Financing Rate (SOFR)** is the benchmark U.S.-dollar overnight interest rate that measures the cost of borrowing cash overnight collateralised by U.S. Treasury securities. It is published each business day by the **Federal Reserve Bank of New York** and is the primary replacement for U.S.-dollar **LIBOR**. Because it is calculated from actual, executed repo transactions rather than from bank estimates, SOFR is treated as a nearly risk-free reference rate and now underpins a large share of USD floating-rate loans, [[floating-rate-notes]], swaps, and futures.

## Overview

SOFR is a **secured** rate: it reflects the interest paid in the overnight **Treasury repurchase (repo) market**, where one party sells Treasuries and agrees to buy them back the next day, effectively borrowing cash against Treasury collateral. Because the loan is collateralised by the most default-remote asset in the dollar system, SOFR contains essentially no bank-credit risk and no term premium — it is close to a pure overnight [[risk-free-rate]].

The New York Fed computes SOFR as a **volume-weighted median** of rates across several segments of the overnight Treasury repo market, including tri-party repo, cleared bilateral repo, and General Collateral Financing (GCF) repo transactions cleared through the Fixed Income Clearing Corporation. Because it aggregates an extremely large volume of real daily transactions across the deepest funding market in the world, SOFR is highly robust and very difficult to manipulate — the property its predecessor most conspicuously lacked. The rate is backward-looking: each day's published SOFR describes borrowing that has already occurred overnight, not an expectation of future rates.

## Why SOFR Replaced LIBOR

[[libor]] (the London Interbank Offered Rate) was, for decades, the world's dominant reference rate, embedded in hundreds of trillions of dollars of contracts. It was fundamentally different from SOFR in two ways:

- **It was unsecured.** LIBOR was meant to capture the rate at which large banks could borrow from one another *without collateral*, so it embedded bank-credit and liquidity premia that rise sharply in a crisis.
- **It was estimate-based, not transaction-based.** LIBOR was produced from a daily survey in which panel banks *submitted* the rate at which they believed they could borrow. As unsecured interbank lending dried up, these submissions rested on expert judgment rather than real trades — a thin, discretionary foundation.

That discretion enabled the **LIBOR manipulation scandal** that surfaced around 2012, in which traders at several major banks were found to have coordinated to nudge submissions up or down to benefit their derivatives positions. The scandal, combined with the collapse in underlying transaction volumes, convinced regulators that a rate built on judgment was no longer credible. In the U.S., the **Alternative Reference Rates Committee (ARRC)**, convened by the Federal Reserve, selected SOFR in 2017 as its recommended replacement, and the New York Fed began publishing it in April 2018.

The transition then ran on a fixed timetable. New USD-LIBOR contract creation was wound down after end-2021, and the remaining widely used USD-LIBOR settings ceased publication after **30 June 2023** — the "2023 LIBOR cessation" that made SOFR (and related fallbacks) the operative benchmark for legacy dollar contracts.

## Term Structure: Overnight, Term SOFR, and Compounded-in-Arrears

SOFR is natively an **overnight** rate, which raises a practical problem: many loans and notes need to know their interest rate at the *start* of a period, whereas LIBOR conveniently quoted forward-looking 1-month, 3-month, and 6-month tenors. Three conventions have emerged to bridge this gap:

- **Compounded SOFR in arrears** — daily overnight SOFR is compounded across the interest period, so the rate for a period is only known near its end. This is the most robust convention and is standard for many derivatives and [[floating-rate-notes]].
- **Simple average / daily SOFR in arrears** — a non-compounded variant used in some loan markets for operational simplicity.
- **Term SOFR (CME Term SOFR)** — a *forward-looking* rate published by CME Group and derived from SOFR futures, giving 1-month, 3-month, 6-month, and 12-month tenors known at the start of the period. ARRC endorsed Term SOFR for specific uses, notably business loans, where borrowers need rate certainty in advance; its use in derivatives is deliberately restricted to preserve liquidity in the overnight-compounded market.

Because SOFR strips out the bank-credit and term premia that were baked into LIBOR, a like-for-like swap from LIBOR to SOFR would shift value between counterparties. To keep legacy contracts economically neutral, the transition applies a fixed **credit-spread adjustment (CSA)** on top of SOFR. The ISDA/ARRC-standard adjustments were set from the historical median difference between LIBOR and SOFR over a five-year lookback (for example, the 3-month USD adjustment is on the order of a quarter of a percentage point). Legacy loan and derivative fallbacks generally reference "SOFR + spread adjustment" so the replaced rate lands close to where LIBOR would have been.

## Where SOFR Is Used

- **Floating-rate loans** — syndicated and corporate loans that previously priced off 3-month LIBOR now typically price off Term SOFR or daily SOFR plus a margin.
- **[[floating-rate-notes]]** — SOFR-linked FRNs (including U.S. Treasury FRNs and agency/corporate issuance) reset off compounded or averaged SOFR.
- **[[interest-rate-swaps|Interest-rate swaps]] and other [[derivatives]]** — the USD OIS (overnight index swap) market now references SOFR, and SOFR discounting is the market convention for valuing collateralised swap portfolios.
- **Futures and options** — CME SOFR futures and options are among the most actively traded interest-rate contracts in the world, having largely replaced the legacy Eurodollar (LIBOR) futures complex.
- **A proxy for the [[risk-free-rate]] in derivatives pricing** — because it is secured and near-riskless, the SOFR/OIS curve is widely used as the discounting and "riskless" reference in money-market and derivatives valuation, even though equity valuation still typically anchors on the Treasury curve.

## SOFR vs. the Fed Funds Rate and LIBOR

SOFR sits alongside the [[fed-funds-rate]], the other principal USD overnight benchmark, but the two measure different markets:

- **Fed funds** is the rate on **unsecured** overnight lending of reserve balances between banks; it is the rate the Federal Reserve targets directly through monetary policy (the FOMC sets the target range).
- **SOFR** is the rate on **secured** overnight borrowing against Treasuries; it is a *market-determined* rate that the Fed influences only indirectly, mainly through the supply of reserves and its administered rates (such as the interest on reserve balances and the overnight reverse-repo facility).

In normal conditions SOFR and the effective fed funds rate track closely and both hug the policy target. SOFR, however, is sensitive to conditions in the repo market and can spike temporarily when cash is scarce relative to collateral — most visibly during the **September 2019 repo-market disruption**, when overnight repo rates jumped sharply before the Fed intervened with liquidity operations. Such episodes are a reminder that although SOFR is near-riskless with respect to *credit*, it still reflects real **funding and [[liquidity]]** conditions. Compared with LIBOR, SOFR's key structural distinction is the absence of a bank-credit component: in a banking stress, LIBOR-style unsecured rates widen while a secured rate like SOFR need not, which is precisely why some lenders have supplemented SOFR with separate credit-sensitive benchmarks.

Broad central-bank operations also feed into where SOFR trades: large-scale asset purchases and reserve creation under [[quantitative-easing]] tend to push abundant cash into the system and hold repo rates near the floor, whereas balance-sheet runoff can tighten funding and lift SOFR relative to administered rates.

## Related

- [[risk-free-rate]] — SOFR/OIS is the near-riskless reference used in derivatives pricing
- [[fed-funds-rate]] — the unsecured overnight benchmark and direct policy target, contrasted with secured SOFR
- [[libor]] — the discredited, estimate-based predecessor SOFR replaced
- [[interest-rate-swaps]] — USD OIS and swap discounting now reference SOFR
- [[floating-rate-notes]] — FRNs reset off compounded or averaged SOFR
- [[bonds]], [[derivatives]] — asset classes that price and discount off the SOFR curve
- [[quantitative-easing]] — central-bank liquidity operations that move repo and SOFR conditions

## Sources

- Federal Reserve Bank of New York — SOFR publication, calculation methodology, and reference-rate data (general, publicly documented methodology; no specific figures reproduced here).
- Alternative Reference Rates Committee (ARRC) — recommendations on SOFR adoption, Term SOFR use cases, and LIBOR-to-SOFR spread adjustments.
- ISDA — fallback protocol and standardised credit-spread adjustments for legacy USD-LIBOR contracts.
- General, widely-taught fixed-income and money-market knowledge on repo markets, LIBOR history, and the 2021–2023 LIBOR transition timeline.
