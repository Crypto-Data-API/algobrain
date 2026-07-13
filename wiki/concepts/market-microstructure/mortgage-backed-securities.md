---
title: Mortgage-Backed Securities
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - bonds
  - derivatives
  - history
aliases:
  - MBS
  - mortgage-backed-security
  - mortgage backed securities
  - RMBS
  - agency MBS
related:
  - "[[subprime-mortgage]]"
  - "[[collateralized-debt-obligations]]"
  - "[[freddie-mac]]"
  - "[[2008-global-financial-crisis]]"
  - "[[quantitative-easing]]"
  - "[[duration]]"
  - "[[credit-default-swaps]]"
domain: [market-microstructure]
prerequisites: ["[[duration]]", "[[derivatives]]"]
difficulty: intermediate
---

# Mortgage-Backed Securities

**Mortgage-Backed Securities (MBS)** are bonds backed by pools of residential or commercial mortgages. Investors receive payments derived from the underlying mortgage interest and principal.

MBS backed by [[subprime-mortgage]] loans were a primary catalyst of the [[2008-global-financial-crisis]]. Agencies like fannie-mae and [[freddie-mac]] were major issuers.

## How Securitization Works

Banks originate individual mortgages and then pool hundreds or thousands of them together into a trust. The trust issues bonds (MBS) to investors, with payments derived from the underlying mortgage interest and principal. This process allows banks to move loans off their balance sheets, freeing up capital to originate more mortgages, while providing investors with access to mortgage cash flows.

## Types of MBS

- **Pass-through securities** -- the simplest form. All principal and interest payments from the underlying mortgages are passed directly through to investors on a pro-rata basis.
- **Collateralized Mortgage Obligations (CMOs)** -- more complex structures that divide the mortgage pool's cash flows into multiple tranches with different maturities, payment priorities, and risk profiles. See [[collateralized-debt-obligations]] for the broader CDO structure.

## Key Risks

- **Prepayment risk** -- when interest rates fall, borrowers refinance their mortgages, returning principal early and cutting short the higher-yielding cash flows investors expected. This makes MBS duration uncertain and complicates hedging.
- **Default risk** -- if borrowers stop paying, the underlying cash flows decline. This risk varies dramatically between agency and private-label MBS.

## Agency vs. Private Label

- **Agency MBS** -- issued or guaranteed by government-sponsored enterprises (fannie-mae, [[freddie-mac]]) or the government agency Ginnie Mae. These carry an implicit or explicit government guarantee, making them among the safest fixed-income instruments after Treasuries.
- **Private-label MBS** -- issued by private institutions without government backing. These carried the subprime and Alt-A mortgages that were at the center of the 2008 crisis, and their losses devastated investors worldwide.

## Negative Convexity

The defining quirk of MBS for traders is **negative convexity**, a direct result of prepayment risk. A normal bond gains more from a given rate fall than it loses from an equal rate rise (positive convexity). An MBS does the opposite: when rates fall, borrowers refinance, principal returns early, and the bond's upside is capped (it cannot rally far above par because it keeps getting called away at par); when rates rise, refinancing slows, the average life *extends* exactly when the investor would rather get cash back, deepening the loss. This "extension risk vs. contraction risk" asymmetry means MBS hedging is dynamic — duration changes with the level of rates — and mortgage portfolios must be re-hedged as rates move, which itself can amplify Treasury market volatility (so-called "convexity hedging" flows).

## Trading Relevance

- **Agency MBS** are a core holding for fixed-income and total-return funds, valued for their yield pickup over Treasuries in exchange for prepayment/convexity risk. They trade most actively in the **To-Be-Announced (TBA)** market, a liquid forward market for generic agency pools.
- The [[federal-reserve|Fed]] bought trillions of dollars of agency MBS during [[quantitative-easing]] (2008-2014 and 2020-2021), directly compressing mortgage spreads and lowering consumer mortgage rates — making the MBS market a key transmission channel for [[monetary-policy]]. Quantitative tightening reverses this.
- The MBS-Treasury spread (and the "primary-secondary spread") is watched as a gauge of housing-credit and liquidity conditions.
- During 2008, traders famously used [[credit-default-swaps]] and the ABX index to short private-label subprime MBS — the "Big Short."

## Related

- [[subprime-mortgage]]
- [[collateralized-debt-obligations]]
- [[freddie-mac]]
- [[2008-global-financial-crisis]]
- [[quantitative-easing]] — the Fed's large-scale agency-MBS purchases
- [[duration]] — and the negative-convexity twist specific to MBS
- [[credit-default-swaps]] — the instrument used to short subprime MBS

## Sources

- Frank J. Fabozzi (ed.), *The Handbook of Mortgage-Backed Securities* (Oxford University Press) — the standard reference.
- SIFMA, agency MBS and TBA market documentation and trading practices.
- Financial Crisis Inquiry Commission, *The Financial Crisis Inquiry Report* (2011) — role of private-label MBS in 2008.
- Federal Reserve releases on agency MBS purchase programs (QE1-QE3, 2020 QE).
