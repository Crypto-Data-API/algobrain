---
title: "Mortgages"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [bonds, leverage, interest-rates, derivatives]
aliases: ["Mortgage", "Home Loan", "Mortgage Rates"]
related: ["[[mortgage-backed-securities]]", "[[mbs]]", "[[securitization]]", "[[subprime-mortgage]]", "[[interest-rates]]", "[[yield-curve]]", "[[duration]]", "[[convexity]]", "[[fed-policy]]", "[[real-estate]]", "[[leverage]]", "[[credit-cycle]]", "[[credit-risk]]"]
domain: [bonds, fixed-income]
prerequisites: ["[[interest-rates]]", "[[bonds]]"]
difficulty: beginner
---

A **mortgage** is a long-term loan secured by real property, in which the borrower repays principal and interest over a fixed term (commonly 15-30 years) and the lender holds a lien allowing foreclosure on default. Mortgages are the largest consumer-debt market in the world and the raw collateral from which [[mortgage-backed-securities]] (MBS) are constructed through [[securitization]], making the mortgage market a central node connecting household [[leverage]], the [[yield-curve]], [[fed-policy|monetary policy]], and the fixed-income trading complex.

## Core Mechanics

- **Amortisation.** A standard fixed-rate mortgage is repaid in equal monthly payments; early payments are mostly interest, later payments mostly principal. The schedule is computed from the loan amount, rate, and term using the standard annuity formula:

  $$M = P \cdot \frac{r(1+r)^{n}}{(1+r)^{n}-1}$$

  where `M` = monthly payment, `P` = principal, `r` = monthly rate (annual rate / 12), and `n` = number of payments (years × 12).
- **Fixed vs. adjustable rate.** A fixed-rate mortgage (FRM) locks the rate for the full term. An adjustable-rate mortgage (ARM) resets periodically against a reference index (historically LIBOR, now SOFR or the Treasury yield) plus a margin, shifting interest-rate risk from lender to borrower.
- **Loan-to-value (LTV) and the down payment.** LTV = loan / property value. Higher LTV means more borrower [[leverage]] and higher default risk; lenders price this in or require private mortgage insurance (PMI).
- **The embedded prepayment option.** US borrowers can usually refinance or pre-pay with little penalty. This is effectively a *call option the borrower holds against the lender*: when rates fall, borrowers refinance, returning principal to the lender exactly when reinvestment yields are low. This option is the defining risk feature that flows through into [[mortgage-backed-securities|MBS]].

### Worked Amortisation Example

A \$300,000 30-year FRM at a 6% annual rate (`r` = 0.005/month, `n` = 360) gives a monthly payment of about **\$1,799**. Of the *first* payment, \$1,500 is interest (\$300,000 × 0.005) and only \$299 reduces principal. By the final years, almost the entire payment is principal. Over the full term the borrower pays roughly **\$347,500 in interest** — more than the amount borrowed. This front-loaded interest structure is why early prepayment or refinancing has such a large effect on the lender's realised yield, and why MBS cash flows are so sensitive to prepayment behaviour. *(Numbers illustrative; depends on the actual rate.)*

### Fixed vs. Adjustable Rate

| Feature | Fixed-rate (FRM) | Adjustable-rate (ARM) |
|---|---|---|
| Rate over life | Locked for full term | Fixed teaser period, then resets to index + margin |
| Who bears rate risk | Lender (and MBS holder) | Borrower |
| Payment certainty | High | Low after reset |
| Typical appeal | Rate-lock when rates low; the "lock-in effect" | Lower initial payment; bet on falling/stable rates |
| Prepayment driver | Refinancing when rates fall | Refinancing or reset shock |
| Reference index | n/a (set at origination) | SOFR / Treasury yield + margin (formerly LIBOR) |

## Mortgages, Rates, and the Curve

Mortgage rates are not set directly by the central bank. The 30-year US mortgage rate tracks the 10-year Treasury yield plus a **primary mortgage spread** (lender margin + the cost of the prepayment option + credit/servicing costs). So mortgage rates are driven by:

- The level and shape of the [[yield-curve]] (long-end Treasury yields, not the policy rate, anchor 30-year FRMs).
- [[fed-policy|Fed policy]] indirectly, via expectations and via the Fed's own MBS holdings (quantitative easing/tightening compresses or widens the spread).
- MBS demand from banks, the GSEs (Fannie Mae, Freddie Mac), and global investors.

Because the long end drives mortgage rates, the housing market can stay frozen even after the Fed cuts short rates if long yields stay high — a recurring source of macro confusion.

## From Mortgages to MBS — Securitisation

Individual mortgages are illiquid and idiosyncratic; [[securitization|securitisation]] pools thousands of them into tradable bonds. The pipeline:

1. **Origination** — a lender writes the loan to a borrower.
2. **Pooling** — many loans with similar characteristics (rate, term, credit) are aggregated.
3. **Issuance** — the pool is sold into a trust that issues [[mortgage-backed-securities|MBS]] / [[mbs|MBS]] backed by the pooled cash flows.
4. **Tranching (for non-agency / CMO structures)** — cash flows are sliced into tranches with different priority and risk; senior tranches absorb losses last, junior/equity tranches first. This is the same machinery that produced [[collateralized-debt-obligations|CDOs]] in 2008.

| MBS type | Credit backing | Main risk to the holder |
|---|---|---|
| **Agency MBS** (Fannie/Freddie/Ginnie) | Government / GSE guarantee on credit | **Prepayment / interest-rate risk** (credit largely guaranteed) |
| **Non-agency / private-label** | No guarantee | **Both credit risk and prepayment risk** |

Securitisation transfers the mortgage's [[credit-risk]] and prepayment risk from the originator to capital-market investors, freeing the originator to lend again. Its great strength (liquidity, risk transfer, lower funding costs) is also its danger: when the chain disconnects underwriting incentives from who bears the loss ("originate-to-distribute"), it can mass-produce bad loans, as 2008 showed.

## Trading Relevance

Mortgages matter to traders well beyond home-buyers:

- **MBS and rates trading.** Pools of mortgages are securitised into [[mortgage-backed-securities|MBS]], one of the largest fixed-income markets. Trading agency MBS centres on modelling the prepayment option — **negative convexity**: when rates fall, prepayments accelerate and the MBS *shortens* [[duration]] (you lose the rally upside), while when rates rise it *extends* (you eat the selloff). This asymmetry is the core risk MBS desks hedge with Treasuries and swaptions.
- **Credit and the cycle.** Mortgage underwriting standards are a leading indicator of the [[credit-cycle]]. Loose standards ([[subprime-mortgage|subprime]], no-doc loans) preceded the 2008 crisis; tracking delinquency and origination data informs macro and credit positioning.
- **Macro reads.** Mortgage application volume, refinancing activity, and the lock-in effect (homeowners unwilling to move and lose a low locked rate) feed into housing, consumption, and labour-mobility forecasts.
- **Bank balance sheets.** Banks holding long-duration fixed-rate mortgages and MBS carry interest-rate risk that became acutely visible in the 2023 regional-bank stress, when rising rates marked down held-to-maturity portfolios.

### Key Risks and Pitfalls

- **Negative convexity is the central MBS hazard.** Because the borrower's prepayment option works *against* the holder, MBS underperform a duration-matched Treasury whether rates rise or fall — the upside is capped by refinancing, the downside extended by slowing prepayments (see [[convexity]] and [[duration]]).
- **Prepayment-model risk.** MBS valuation depends on a behavioural prepayment model; if borrowers prepay faster or slower than modelled (because of rate moves, the lock-in effect, or burnout), the realised yield and duration diverge sharply from the assumption.
- **Extension and reinvestment risk.** Rising rates *extend* duration (cash returns slower, locked into a below-market coupon); falling rates create reinvestment risk (cash returns fast into low yields).
- **Credit risk on non-agency paper.** Without a GSE guarantee, the holder eats borrower defaults — magnified by tranching, where junior tranches can be wiped out by modest pool losses.
- **Correlation/tail risk in securitised structures.** 2008 showed that house-price declines hit many pools at once, so "diversified" pools were far more correlated than models assumed, and highly-rated tranches still failed.

## Historical Significance

The mortgage market is at the centre of the largest financial crisis of the modern era. The 2007-2008 crisis began in subprime mortgages: lax underwriting, high-LTV lending, and the repackaging of poor-quality mortgages into highly-rated [[mortgage-backed-securities|MBS]] and [[collateralized-debt-obligations|CDOs]] propagated losses through the global financial system when house prices fell and borrowers defaulted. The episode is the canonical case study in how household leverage, securitisation, and mispriced tail risk interact (see [[subprime-mortgage]] and [[2008-financial-crisis]]).

## Related

- [[mortgage-backed-securities]] / [[mbs]] — securitised pools of mortgages; the traded instrument
- [[securitization]] — the process turning mortgages into tradable bonds
- [[subprime-mortgage]] — low-credit-quality lending at the centre of 2008
- [[duration]] / [[convexity]] — and the negative convexity prepayment imposes on MBS
- [[interest-rates]] / [[yield-curve]] — what actually drives mortgage rates
- [[fed-policy]] — indirect influence via long rates and MBS holdings
- [[credit-cycle]] / [[credit-risk]] — mortgage underwriting as a cycle indicator; default risk on the loans
- [[leverage]] — mortgages as the primary household leverage instrument
- [[real-estate]] — the underlying asset class

## Sources

- Fabozzi, F.J. — *The Handbook of Mortgage-Backed Securities* — standard reference on mortgage cash flows, prepayment modelling, and convexity.
- Freddie Mac Primary Mortgage Market Survey (PMMS) — the canonical US 30-year and 15-year mortgage-rate series.
- Federal Reserve / FRED — mortgage rate, origination, and delinquency time series.
- Financial Crisis Inquiry Commission (2011) — *The Financial Crisis Inquiry Report* — the role of mortgages and securitisation in the 2008 crisis.
- General market knowledge; no specific wiki source ingested yet beyond the above references. Current mortgage rates and spreads are intentionally left qualitative — see FRED/PMMS for live figures.
