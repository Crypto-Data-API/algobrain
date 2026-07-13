---
title: "Credit Risk"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [risk-management, bonds, fundamental-analysis]
aliases: ["Credit Risk", "credit-risk", "Default Risk", "Counterparty Credit Risk"]
related: ["[[risk-free-rate]]", "[[credit-default-swap]]", "[[corporate-bonds]]", "[[counterparty-risk]]", "[[sovereign-debt]]", "[[collateral]]", "[[interest-rate-risk]]", "[[duration]]", "[[diversification]]", "[[leverage]]", "[[bonds]]", "[[credit-rating]]", "[[market-risk]]"]
domain: [risk-management]
prerequisites: ["[[bonds]]", "[[risk-free-rate]]"]
difficulty: intermediate
---

**Credit risk** (also *default risk* or, between trading counterparties, *counterparty credit risk*) is the risk that a borrower or counterparty fails to meet a contractual obligation — a missed coupon, an unpaid principal, or a defaulted swap payment — causing the lender or holder to lose some or all of the money owed. It is one of the two dominant risks embedded in any fixed-income instrument (the other being [[interest-rate-risk]]) and is the reason a corporate bond, an emerging-market sovereign, or an over-the-counter derivative yields more than the [[risk-free-rate]].

## Overview

Wherever one party has promised to pay another in the future, the promise can be broken. Credit risk is the compensation-bearing acknowledgement of that possibility. A U.S. Treasury bill is treated as (essentially) free of credit risk; every other IOU — a corporate bond, a bank loan, a repo, a trade receivable, a derivative marked in a dealer's favour — carries some probability that the obligor will not perform. The lender is not paid to take *no* risk; it is paid to take *this* risk, and the whole discipline of credit analysis is about pricing and containing it.

Credit risk has three faces that often get conflated:

- **Default risk** — the obligor simply fails to pay.
- **Downgrade / migration risk** — the obligor's creditworthiness deteriorates (even without default), so the market re-prices its debt lower.
- **Spread risk** — the market's *required* compensation for credit risk widens for reasons that may have nothing to do with a specific issuer (a recession scare, a liquidity crunch), marking down every credit-sensitive position at once.

## Components: how credit loss is decomposed

The market and bank-regulatory convention decomposes the *expected* loss on an exposure into three multiplicative pieces:

- **Probability of Default (PD)** — the likelihood the obligor defaults over a given horizon (often one year). Estimated from credit ratings, historical default tables, structural models (e.g. distance-to-default), or the market-implied probability backed out of bond spreads and [[credit-default-swap|CDS]] quotes.
- **Loss Given Default (LGD)** — the fraction of the exposure *not* recovered after default, i.e. `LGD = 1 − recovery rate`. Recovery depends on seniority (senior secured recovers far more than subordinated or unsecured debt), collateral, and how the bankruptcy plays out.
- **Exposure at Default (EAD)** — how much is actually at risk when default occurs. For a drawn loan this is the outstanding balance; for a derivative or revolving facility it varies with market moves and undrawn commitments.

These combine into the standard **expected loss** identity:

```
Expected Loss (EL) = PD × LGD × EAD
```

Expected loss is what a lender should *price in* on average and provision for. The tail beyond the average — the risk that many obligors default together, or that recoveries collapse in a crisis — is **unexpected loss**, and it is unexpected loss (not expected loss) that economic and regulatory capital are held against.

## How credit risk is priced and compensated

The price of credit risk is the **credit spread**: the extra yield a credit-risky bond offers over a comparable-maturity risk-free benchmark. If a 5-year Treasury yields *r* and a 5-year corporate bond of the same maturity yields *r + s*, then *s* is the credit spread — the market's per-annum charge for bearing that issuer's default and downgrade risk (plus a liquidity component). It shows up inside the bond's **yield-to-maturity** and is the credit portion of the discount rate applied to its cash flows.

> **Disambiguation:** in this wiki the page [[credit-spread]] documents the **options income strategy** (selling a nearer option and buying a further one for a net credit). Here, "credit spread" means the **bond yield premium over the risk-free rate** — a different, same-named concept. They are unrelated beyond the shared word "spread."

Spreads are dynamic. **Spread widening** (spreads rising) means the market is demanding more compensation for credit risk — bad for holders, since existing bonds fall in price — and typically accompanies recessions, defaults, or liquidity stress. **Spread tightening** (spreads falling) reflects improving credit conditions or risk appetite and lifts credit-bond prices. Because a bond's total return blends its credit spread move with its rate/[[duration]] move, credit and rate risk have to be disentangled to understand performance (see *Relationship to other risks* below).

## Credit ratings

Rating agencies publish an ordinal opinion of an obligor's creditworthiness, condensing PD and, to a degree, LGD into a letter grade. The three dominant agencies are **Moody's**, **S&P Global Ratings**, and **Fitch Ratings**. Their scales split at a crucial boundary:

- **Investment grade (IG)** — Moody's Baa3 / S&P and Fitch BBB− and above. Lower default probability; eligible for many regulated and mandate-constrained portfolios.
- **High yield ("junk" / speculative grade)** — Ba1 / BB+ and below. Higher yields to compensate for materially higher default risk.

The IG/HY line is economically load-bearing because many institutions are *contractually barred* from holding sub-IG paper. Two rating dynamics matter for risk management:

- **Rating migration / downgrade risk** — even without default, a downgrade re-prices the bond wider and can force selling.
- **Fallen angels** — issuers downgraded *from* IG *into* high yield. Because index and mandate rules can force IG holders to sell just as HY buyers are absorbing supply, fallen angels can suffer outsized, technically-driven price drops. See [[credit-rating]] for the full scale and methodology.

Ratings are opinions, not guarantees — their lag and their pre-2008 mis-rating of structured credit are standing cautions against treating them as ground truth.

## Credit events and instruments

A **credit event** is a defined trigger of credit loss. The main categories are:

- **Default / failure to pay** — a missed scheduled payment (often after a grace period).
- **Restructuring** — the obligor forces a change to terms (maturity extension, coupon cut, principal haircut) that leaves creditors worse off — a "distressed exchange."
- **Bankruptcy** — the obligor enters formal insolvency proceedings; creditors recover according to the seniority waterfall.

The purpose-built instrument for isolating and transferring credit risk is the **[[credit-default-swap|credit default swap (CDS)]]**. The protection buyer pays a periodic premium (the CDS spread) and, if a defined credit event occurs, is compensated for the loss by the protection seller. A CDS therefore acts both as a **hedge** (buy protection to offload an issuer's default risk) and as a **market price of credit risk** — the CDS spread is a clean, tradable, real-time read on perceived default probability, often more responsive than cash-bond spreads. Related instruments include CDS indices (e.g. the CDX and iTraxx families) for hedging broad credit exposure.

## Where credit risk shows up

- **Corporate credit** — [[corporate-bonds]] and bank loans are the archetypal credit exposure; the entire spread over Treasuries is compensation for it.
- **Sovereign credit** — [[sovereign-debt]] carries credit risk too, especially for emerging markets or issuers borrowing in a foreign currency they cannot print. Downgrades and default fears drive sovereign spreads.
- **Counterparty credit risk** — in OTC derivatives, repo, and securities lending, the risk is that the party owing you a mark-to-market gain defaults before settling. This is the domain of [[counterparty-risk]], managed with collateral and netting.
- **Bank loan books** — a bank's core business *is* warehousing credit risk; loan-loss provisioning and capital are built around expected and unexpected credit loss.
- **Money-market and cash instruments** — even "safe" cash vehicles hold commercial paper and short bank paper, so a money-market fund can "break the buck" if an issuer defaults (as happened in 2008).
- **Equity investors** — credit risk reaches equities as **distress risk**. A highly [[leverage|leveraged]] firm whose fundamentals deteriorate faces rising odds of default, and equity — the most junior claim — is wiped out first in bankruptcy. Analysts gauge this with balance-sheet screens such as the altman-z-score (a bankruptcy-prediction score) and coverage metrics like interest-coverage (EBIT ÷ interest expense), which show whether earnings comfortably service the debt. Widening credit spreads on a company's bonds are often an early warning for its stock.

## Measuring and managing credit risk

- **Credit analysis** — assessing an obligor's capacity and willingness to pay: cash flows, leverage, interest-coverage, asset quality, and the structural protections in the bond's covenants.
- **Diversification across issuers** — because idiosyncratic default is largely uncorrelated across unrelated names, spreading exposure over many issuers and sectors sharply reduces portfolio credit risk (see [[diversification]]). It does *not*, however, remove **systematic** credit risk — the tendency for defaults to cluster in downturns.
- **Position and concentration limits** — caps on exposure to any single name, sector, or rating bucket.
- **Collateral and margin** — posting [[collateral]] against an exposure reduces LGD and EAD; daily variation margin on derivatives shrinks how much can be owed before default.
- **Netting** — legally enforceable close-out netting collapses many offsetting trades with one counterparty into a single net exposure, dramatically cutting counterparty credit risk.
- **Hedging** — buying CDS protection or shorting credit indices transfers default risk to a willing seller.
- **Provisions and capital** — lenders reserve for expected loss and hold capital against unexpected loss. Bank capital treatment of credit risk is codified in the Basel framework; see [[basel-iii]] for standardised and internal-ratings-based approaches to credit risk-weighted assets.

## Relationship to other risks

Credit risk is distinct from, but interacts with, the other principal risks of a fixed-income position:

- **vs. [[interest-rate-risk]]** — interest-rate risk is the sensitivity of a bond's price to changes in the *risk-free* yield curve (measured by [[duration]]); it exists even for default-free Treasuries. Credit risk is the *additional* sensitivity to the issuer's creditworthiness and to credit spreads. A corporate bond's total return decomposes into a **rate/duration** component and a **credit/spread** component, and the two frequently move in opposite directions — in a "flight to quality," risk-free yields fall (helping the rate component) while credit spreads widen (hurting the credit component).
- **vs. [[market-risk]]** — market risk is the risk of loss from broad market-price moves (equities, rates, FX, commodities). Credit spread risk is sometimes treated as a market-risk factor for traded credit, but *default* risk — the jump-to-default loss when an issuer actually fails — is a distinct, fat-tailed exposure that ordinary volatility-based market-risk measures understate.

## Example (qualitative)

Consider two five-year bonds bought at the same time: a government note treated as risk-free, and a corporate bond from a BBB-rated manufacturer. The corporate bond yields more — that extra yield is the credit spread, the investor's pay for bearing default and downgrade risk.

If the economy weakens and the manufacturer's sales fall, its interest coverage thins and rating agencies place it on negative watch. Even before any missed payment, the market demands more compensation: the bond's credit spread **widens**, its price **falls**, and a holder marking to market shows a loss driven purely by credit — not by any move in the risk-free curve. Should the firm be **downgraded to high yield**, mandate-constrained investors may be forced to sell, pushing the price lower still (a *fallen angel* dynamic). In the worst case the firm defaults: recovery on the senior unsecured bond is only a fraction of face value (a high LGD), and the firm's *equity*, being the most junior claim, is effectively wiped out first. A lender who had instead **bought CDS protection** on the name would have been compensated for the default loss, having paid the CDS premium as the ongoing price of hedging that credit risk. (Illustrative only — no specific figures implied.)

## Related

- [[risk-free-rate]] — the benchmark over which the credit spread is earned
- [[interest-rate-risk]], [[duration]] — the rate side of a bond's total return, distinct from credit
- [[market-risk]] — broad price risk; how credit spread vs. jump-to-default risk fit in
- [[credit-default-swap]] — the instrument that hedges and prices credit risk
- [[credit-spread]] — the options income strategy (same name, different concept — see disambiguation above)
- [[credit-rating]] — the letter-grade scale, agencies, and migration risk
- [[corporate-bonds]], [[bonds]], [[sovereign-debt]] — the instruments where credit risk lives
- [[counterparty-risk]], [[collateral]] — credit risk in derivatives, repo, and securities lending
- [[diversification]] — the primary tool against idiosyncratic default risk
- [[leverage]], interest-coverage, altman-z-score — how credit / distress risk reaches equity investors
- [[basel-iii]] — bank capital treatment of credit risk

## Sources

- General, widely-taught fixed-income and risk-management knowledge (e.g. Fabozzi, *Bond Markets, Analysis, and Strategies*; Hull, *Options, Futures, and Other Derivatives* and *Risk Management and Financial Institutions*). The PD × LGD × EAD expected-loss decomposition and the expected/unexpected-loss capital distinction follow the Basel Committee on Banking Supervision's credit-risk framework (BIS/Basel documents).
- Rating-scale definitions and the investment-grade / high-yield boundary follow the published rating methodologies of Moody's, S&P Global Ratings, and Fitch Ratings.
