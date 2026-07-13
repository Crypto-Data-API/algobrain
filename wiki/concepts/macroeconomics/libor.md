---
title: "LIBOR (London Interbank Offered Rate)"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [bonds, derivatives, risk-management, market-microstructure, regulation]
aliases: ["LIBOR", "libor", "London Interbank Offered Rate"]
related: ["[[sofr]]", "[[risk-free-rate]]", "[[fed-funds-rate]]", "[[interest-rate-swaps]]", "[[floating-rate-notes]]", "[[bonds]]", "[[derivatives]]", "[[liquidity]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[risk-free-rate]]"]
difficulty: intermediate
---

The **London Interbank Offered Rate (LIBOR)** was, for roughly three decades, the world's most widely used benchmark interest rate — a daily, survey-based estimate of the rate at which large banks could borrow **unsecured** funds from one another in the London wholesale market. It was quoted across five currencies and seven tenors and embedded in an estimated hundreds of trillions of dollars of notional loans, [[floating-rate-notes]], mortgages, and [[derivatives]]. Following a manipulation scandal and the collapse of the underlying interbank lending it was meant to measure, LIBOR was progressively discontinued between 2021 and 2023 and replaced by transaction-based risk-free rates such as [[sofr]] for the U.S. dollar.

## Overview

LIBOR answered a single question: *at what rate could a leading bank borrow cash, without posting collateral, from another leading bank?* Because it captured **unsecured** interbank funding, LIBOR embedded both a bank-credit premium and a liquidity premium — the extra yield lenders demand for the risk that the borrowing bank might fail or that cash might become scarce. That credit sensitivity was, for years, seen as a feature: a floating-rate loan priced off LIBOR automatically re-priced higher when bank funding stress rose. It later proved to be the rate's defining structural vulnerability.

LIBOR originated in the 1980s under the **British Bankers' Association (BBA)**, which first published it in a standardised form in 1986. Administration passed to **ICE Benchmark Administration (IBA)** in 2014 as part of post-scandal reforms, and the rate was thereafter branded **ICE LIBOR**. In its latter, consolidated form it was published for **five currencies** — U.S. dollar (USD), pound sterling (GBP), euro (EUR), Japanese yen (JPY), and Swiss franc (CHF) — across **seven tenors**: overnight/spot-next, one week, and one, two, three, six, and twelve months. The most economically important settings by far were 3-month and 1-month USD LIBOR.

## How LIBOR Was Set

LIBOR was **estimate-based, not transaction-based** — the property that most sharply distinguishes it from its successors. Each business day a **panel** of contributor banks for each currency submitted the rate at which they believed they *could* borrow a reasonable market size, just prior to a fixed morning cut-off. The administrator discarded the highest and lowest submissions and averaged the remainder — a **trimmed mean** — to produce the published fixing for each currency and tenor.

The fatal weakness lay in the word *could*. Submissions were **expert judgment**, not records of executed trades. In normal times, when banks lent to one another freely, the judgment was reasonably anchored to real activity. But unsecured term interbank lending thinned dramatically after the 2007–2009 financial crisis, so submissions increasingly rested on discretion rather than on observable transactions. A benchmark referencing hundreds of trillions of dollars of contracts was, in effect, produced by a daily poll — and any poll can be gamed.

## The Manipulation Scandal

Beginning around **2012**, investigations by regulators in the United Kingdom, the United States, and elsewhere revealed that traders and submitters at several major banks had **rigged their LIBOR submissions**. Two distinct motives emerged:

- **Derivatives profit.** Because vast portfolios of [[interest-rate-swaps]] and futures settled against LIBOR fixings, nudging a submission a fraction of a basis point up or down could move a bank's daily [[derivatives]] profit-and-loss. Traders were found coordinating — sometimes across institutions — to push fixings in the direction that favoured their books.
- **Masking funding stress.** During the crisis, submitting an honestly high borrowing rate would have signalled that a bank was struggling to fund itself. Some banks **lowballed** their submissions to appear healthier than they were, distorting LIBOR downward as a side effect.

The fallout was severe: multiple global banks paid record regulatory fines across several jurisdictions, and a number of individual traders faced criminal prosecution and, in some cases, imprisonment. Beyond the penalties, the scandal delivered a structural verdict — a globally systemic benchmark built on unverifiable estimates was no longer credible. It set in motion the search for transaction-based replacements.

## The Transition and Cessation

In **July 2017**, the UK's **Financial Conduct Authority (FCA)** announced that it would no longer compel panel banks to make LIBOR submissions after the end of 2021, effectively signalling the benchmark's phase-out. The critical problem was not merely the scandal but the **absence of underlying transactions**: a rate meant to measure unsecured interbank borrowing could not be sustained when that borrowing had largely disappeared.

Regulators and industry bodies coordinated a move to **risk-free reference rates (RFRs)** anchored in deep, real markets. Each major currency adopted its own overnight RFR:

- **USD** → **[[sofr]]** (Secured Overnight Financing Rate), selected by the Federal Reserve-convened **Alternative Reference Rates Committee (ARRC)**
- **GBP** → **[[sonia]]** (Sterling Overnight Index Average)
- **EUR** → **[[estr]]** (Euro Short-Term Rate, €STR)
- **JPY** → **TONA** (Tokyo Overnight Average Rate)
- **CHF** → **SARON** (Swiss Average Rate Overnight)

The wind-down followed a staged timetable. **New** LIBOR-referencing contracts were to stop being written after end-2021, and **most LIBOR settings** — all sterling, yen, euro, and franc tenors, plus the less-used USD tenors — ceased publication at the **end of 2021**. The five most heavily used **USD** settings (overnight and 1-, 3-, 6-, and 12-month) were granted an extension and were published for the last time on a representative basis after **30 June 2023**.

To ease the very large stock of contracts that could not be renegotiated in time, the FCA required a temporary **"synthetic" LIBOR** — a value calculated from the relevant RFR plus a fixed spread rather than from bank submissions — for certain sterling and dollar tenors. Synthetic LIBOR was explicitly a bridging measure for legacy use only and was itself wound down, with the final synthetic USD settings ceasing at the end of September 2024.

## LIBOR vs. SOFR

The clearest way to understand LIBOR is by contrast with the rate that replaced it in dollars, [[sofr]]:

| Dimension | LIBOR | SOFR |
|-----------|-------|------|
| Basis | Estimates (bank submissions) | Executed transactions (Treasury repo) |
| Security | **Unsecured** interbank lending | **Secured** by U.S. Treasuries |
| Credit content | Embeds bank-credit and liquidity premia | Near risk-free; essentially no bank credit |
| Term structure | Forward-looking term rates (1M, 3M, 6M…) quoted up front | Natively overnight; term rates derived (compounded in arrears or CME Term SOFR) |
| Robustness | Thin/absent underlying market; manipulable | Very deep market; difficult to manipulate |

The credit-sensitivity difference is not cosmetic. In a banking crisis, an unsecured rate like LIBOR **widens** as lenders price in default risk, whereas a secured, near-[[risk-free-rate]] like SOFR need not. That is why LIBOR historically traded above overnight risk-free rates by a spread that blew out during stress episodes, and why some lenders have supplemented SOFR with separate credit-sensitive add-ons to recover the built-in crisis hedge that LIBOR provided.

Because SOFR strips out the credit and term premia baked into LIBOR, converting a legacy LIBOR contract directly to SOFR would transfer value between the two counterparties. To keep such conversions economically neutral, standardised fallbacks add a fixed **credit-spread adjustment** — set from the historical median gap between the two rates over a multi-year lookback — so that "SOFR + spread adjustment" lands close to where LIBOR would have fixed. (See [[sofr]] for the mechanics of the term conventions and the spread adjustment.)

## Legacy: Why LIBOR Still Matters

Although LIBOR no longer fixes, it remains relevant for several reasons:

- **Fallback language.** Contracts written before the transition often contained (or were amended to contain) **fallback provisions** specifying what rate applies once LIBOR ceases. Interpreting older loan agreements, bonds, and swaps still requires understanding what LIBOR was and how its replacement is calculated.
- **"Tough legacy" contracts.** A residue of long-dated instruments — some maturing decades out, some lacking workable fallback terms — could not be renegotiated before cessation. Synthetic LIBOR and statutory fallback frameworks in the UK, US, and EU were created specifically to keep these contracts functioning without litigation.
- **Historical interpretation.** A great deal of pre-2022 financial data, research, and documentation is quoted relative to LIBOR (for example, "LIBOR + 250 bps"). Reading historical pricing, credit spreads, and the mechanics of past crises requires knowing that LIBOR was the reference and that it carried a bank-credit component the current risk-free benchmarks do not.

For these reasons LIBOR endures as an essential piece of financial-markets literacy even though, as a live rate, it has been fully retired.

## Related

- [[sofr]] — the transaction-based, secured USD benchmark that replaced LIBOR
- [[risk-free-rate]] — the near-riskless reference concept; SOFR-style rates are near-risk-free, LIBOR was not
- [[fed-funds-rate]] — like LIBOR, an *unsecured* overnight rate, but transaction/administered rather than survey-based
- [[interest-rate-swaps]] — vast swap portfolios once settled against LIBOR and were repapered to RFRs
- [[floating-rate-notes]] — FRNs and loans historically priced off LIBOR now reference RFRs
- [[bonds]], [[derivatives]] — asset classes whose legacy pricing and fallbacks reference LIBOR
- [[liquidity]] — LIBOR's credit/liquidity premium was its defining feature and its structural weakness

## Sources

- Financial Conduct Authority (FCA) — announcements on the end of LIBOR panel submissions (2017) and the timetable for cessation and synthetic LIBOR wind-down (general, publicly documented; no specific figures reproduced here).
- ICE Benchmark Administration (IBA) — LIBOR methodology, panel-bank submission process, and the currencies and tenors published under ICE LIBOR.
- Alternative Reference Rates Committee (ARRC) and ISDA — LIBOR-to-RFR transition guidance, fallback language, and credit-spread-adjustment framework.
- General, widely-taught fixed-income and money-market knowledge on the LIBOR manipulation scandal, unsecured interbank lending, and the 2021–2024 LIBOR transition timeline.
