---
title: "Interest Rate Risk"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [risk-management, bonds, volatility]
aliases: ["Interest Rate Risk", "Rate Risk", "interest-rate-risk", "duration risk"]
domain: [risk-management]
prerequisites: ["[[bonds]]", "[[duration]]"]
difficulty: intermediate
related: ["[[bonds]]", "[[corporate-bonds]]", "[[duration]]", "[[convexity]]", "[[yield-curve]]", "[[credit-cycle]]"]
---

Interest rate risk is the potential for investment losses arising from changes in interest rates. It is the primary risk factor for fixed-income securities: when interest rates rise, bond prices fall, and vice versa. The relationship exists because a bond's price is the present value of its future cash flows, and higher discount rates mechanically reduce that present value. This risk affects not only bond portfolios but also equities (through discount rate effects on [[valuation]]), real estate, and the banking sector.

The standard measure of interest rate sensitivity is [[duration]], which quantifies the approximate percentage change in a bond's price for a 1% change in yield. A bond with a duration of 7 years will lose roughly 7% of its value if rates rise by 100 basis points. Modified duration provides a linear approximation, while [[convexity]] captures the curvature -- the fact that duration itself changes as yields move. For large rate moves, ignoring convexity leads to significant pricing errors. Portfolio managers use these metrics to construct immunized portfolios where asset duration matches liability duration, neutralizing interest rate exposure. Techniques like duration matching, cash flow matching, and barbell vs. bullet portfolio construction are core tools in fixed-income [[risk-management-overview|risk management]].

For banks and financial institutions, interest rate risk manifests differently through net interest income (NII) risk: the danger that the spread between lending rates (assets) and deposit rates (liabilities) compresses. Banks with significant duration mismatches -- borrowing short and lending long -- are particularly vulnerable to rising rate environments, as demonstrated during the 2023 US regional banking crisis when rapid rate hikes caused unrealized losses on long-duration bond portfolios to wipe out bank capital (notably [[silicon-valley-bank|Silicon Valley Bank]]). Equity investors must also account for interest rate risk, as higher rates generally compress [[price-to-earnings|P/E]] multiples, disproportionately affecting growth stocks whose value depends on distant future cash flows.

## Types of Interest Rate Risk

- **Price (market) risk** — the most direct: rising yields drive down the market value of existing fixed-coupon bonds. Magnitude scales with [[duration]].
- **Reinvestment risk** — the mirror image: when rates fall, coupons and maturing principal must be reinvested at lower yields. Long-duration assets carry low reinvestment risk but high price risk; short-duration assets the reverse. [[convexity]] and immunization aim to balance the two.
- **Yield curve (twist) risk** — exposure to non-parallel shifts. A barbell (short + long maturities) and a duration-matched bullet (intermediate) can have the same duration yet behave very differently when the curve steepens or flattens. Key-rate durations decompose this exposure.
- **Basis risk** — when the rate hedging an exposure (e.g. SOFR) diverges from the rate driving it (e.g. a specific issuer's funding cost).
- **Repricing/NII risk** — the bank balance-sheet form described above; quantified via gap analysis and earnings-at-risk.

## Measuring and Hedging

The standard sensitivity toolkit:

```
Modified duration  D_mod = Macaulay duration / (1 + y/k)
Price change ≈  -D_mod * Δy * Price        (first order)
Better:         ΔPrice/Price ≈ -D_mod*Δy + 0.5*Convexity*(Δy)^2
DV01 (dollar value of 1bp) = D_mod * Price * 0.0001
```

DV01 is the practitioner's hedge unit: to neutralize a book, traders short enough [[us-treasury-bonds|Treasury futures]] or pay fixed in interest-rate swaps so the portfolio's net DV01 ≈ 0. Common hedges are Treasury futures, [[interest-rate-swaps]], swaptions, and Eurodollar/SOFR futures. Bond convexity means a long-bond position gains more from a rate fall than it loses from an equal rate rise — a feature options buyers pay for and that callable-bond holders are short.

## Trading Relevance

Interest rate risk is the master variable behind most cross-asset regimes. The 2022 Fed hiking cycle (fastest in 40 years) produced the worst total-return year for US Treasuries on record and a simultaneous selloff in bonds and equities that broke the classic 60/40 hedge. Rate-sensitive trades cluster around the data: CPI prints, FOMC decisions, and the quarterly refunding announcement are the highest-DV01 events on the macro calendar. Practical expressions include curve steepeners/flatteners (2s10s), duration-extension trades when the cycle is expected to peak, and pairing long-duration growth equity shorts against value when real yields rise. Knowing your portfolio's aggregate DV01 — including the hidden duration in growth stocks, REITs, and long-dated cash flows — is the core of rate risk management.

## Related

- [[duration]] — the primary sensitivity measure
- [[convexity]] — the second-order correction
- [[bonds]], [[corporate-bonds]], [[us-treasury-bonds]]
- [[yield-curve]] — the term structure that twists
- [[credit-cycle]] — interacts with rate risk in credit instruments

## Sources

- CFA Institute curriculum, Fixed Income — duration, convexity, and the sources of interest rate risk
- Bank for International Settlements, "Interest rate risk in the banking book" (IRRBB) standards
- Federal Reserve, post-mortem on Silicon Valley Bank (2023) — duration mismatch and unrealized losses
- Tuckman & Serrat, *Fixed Income Securities* — DV01, key-rate durations, hedging mechanics
