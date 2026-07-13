---
title: "Investor Protection (Australia)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [regulation, australia, education, consumer-protection]
aliases: ["Australian Investor Protection", "AFCA", "Investor Compensation"]
related: ["[[asic]]", "[[australian-regulatory-framework]]", "[[afsl]]", "[[risk-management]]", "[[regulation]]", "[[vasp-regulation]]"]
domain: [regulation]
difficulty: beginner
---

Australia provides multiple layers of investor protection for retail investors — including direct share ownership through CHESS, free dispute resolution through AFCA, compensation through the National Guarantee Fund (NGF), and product regulation by [[asic|ASIC]]. However, these protections have significant boundaries: they primarily apply to regulated products traded through AFSL-holding brokers on Australian markets. Crypto on unregistered exchanges, [[defi]] protocols, international shares in custodial accounts, and unlicensed financial products fall outside most protections. Understanding what is and is not protected is essential for managing risk.

> **Not legal or financial advice.** This page is general educational information about the Australian [[australian-regulatory-framework|investor-protection framework]]. Compensation caps, thresholds, and scheme rules are **indexed and amended frequently** — figures below are indicative as at the dates noted. Confirm current limits and eligibility directly with [[asic|ASIC]] (asic.gov.au), AFCA (afca.org.au), the ASX/SEGC, or a licensed adviser before relying on any figure.

## Overview

Australia's investor protection framework is generally strong by international standards — the CHESS system provides direct ownership protections that the US market lacks, ASIC has broad product intervention powers, and AFCA provides free dispute resolution. However, Australia does not have an equivalent of the US SIPC (~$500,000 per account insurance) or the UK FSCS (~£85,000 per institution guarantee) — instead relying on structural protections (CHESS, client money segregation) and entity-specific compensation rather than a blanket investor insurance scheme.

### The Five Layers at a Glance

Australian retail protection is best understood as five overlapping layers, each addressing a different failure mode. No single layer is comprehensive; their *combination* is what gives broad coverage for on-market AU products and leaves clear gaps elsewhere.

| Layer | Mechanism | Protects against | Administered by | Legislative basis |
|---|---|---|---|---|
| **1. Structural ownership** | CHESS / HIN | Broker insolvency (your shares survive) | ASX | Corporations Act, ASX rules |
| **2. Asset segregation** | Client money trust accounts | Misuse / commingling of client cash | [[asic\|ASIC]] | Corporations Act Part 7.8 |
| **3. Last-resort compensation** | National Guarantee Fund (NGF) | Cash/unsettled trades lost in participant insolvency | SEGC | Corporations Act, SEGC rules |
| **4. Conduct & product rules** | Product intervention, DDO, best-interests duty | Mis-selling, unsuitable products, bad advice | [[asic\|ASIC]] | Corporations Act, ASIC Act |
| **5. Dispute resolution** | AFCA (free EDR) | Firm wrongdoing where the firm holds an [[afsl\|AFSL]] | AFCA | Corporations Act |

The recurring theme: **all five layers attach to AFSL-holding entities and on-market AU products.** Step outside that perimeter — unregistered crypto, offshore platforms, [[defi]] — and most layers fall away. This perimeter is the single most important thing for an Australian investor to internalise.

## CHESS Sponsorship — Direct Ownership

CHESS (Clearing House Electronic Subregister System) is the foundation of Australian investor protection for ASX-traded securities:

- When you buy shares through a CHESS-sponsored broker, your ownership is registered **directly in your name** on the ASX subregister
- You receive a unique **Holder Identification Number (HIN)** — your shares are tied to you, not to your broker
- **If your broker fails**: Your shares are safe — they are registered to your HIN, not to the broker's balance sheet. You simply transfer your HIN to a new broker
- **No pooling**: Unlike the US "street name" system where a broker holds all client shares in its own name and maintains internal records of who owns what, CHESS creates a direct legal ownership record for each investor
- CHESS-sponsored brokers include: commsec, selfwealth, nabtrade, bell-direct, ig-markets, cmc-markets, stake (for ASX), superhero (since 2023)

CHESS is widely regarded as one of the strongest share ownership protection systems in the world.

## AFCA (Australian Financial Complaints Authority)

AFCA is Australia's external dispute resolution (EDR) scheme for financial services complaints:

### Key Features
- **Free for consumers**: No cost to lodge or pursue a complaint — AFCA is funded by levies on its member firms
- **Mandatory membership**: All [[afsl|AFSL]] holders must be AFCA members — it is a condition of holding an AFSL
- **Binding on the firm**: AFCA determinations are binding on the financial firm but not on the consumer — if the consumer is dissatisfied, they can still pursue the matter in court
- **Compensation**: AFCA can award compensation of up to roughly **$1.085 million** (indicative, as of 2024; indexed annually — confirm the current cap with AFCA) for most financial complaints, and higher limits apply in some categories (e.g., superannuation, small business credit)

### What AFCA Covers

*Compensation caps below are indicative as of 2024 and indexed annually — treat as order-of-magnitude.*

| Category | Examples | Maximum Compensation (indicative) |
|----------|---------|---------------------|
| **Banking and finance** | Disputed transactions, unauthorised transfers, credit card fraud, loan disputes | $1,085,000 |
| **Investments and financial advice** | Inappropriate advice, failure to execute orders, misleading conduct by advisers | $1,085,000 |
| **Superannuation** | Trustee decisions on death benefits, total and permanent disability claims, account errors | No monetary limit (trustee decisions) |
| **Insurance** | Claim denials, delays, policy interpretation disputes | $1,085,000 |
| **Small business credit** | Loans, guarantees, facilities for small businesses | $1,085,000 |

### What AFCA Does NOT Cover
- Complaints against entities that do not hold an AFSL (e.g., unregistered crypto exchanges, overseas platforms)
- Investment losses from market movements (AFCA is not insurance against losing money)
- Disputes already resolved by a court or tribunal
- Complaints about ASIC, APRA, or other regulators (they have separate accountability mechanisms)
- Complaints older than 6 years (unless the consumer only became aware within 2 years)

### How AFCA Replaced Previous Schemes
AFCA was established on **1 November 2018**, replacing three previous schemes:
- **Financial Ombudsman Service (FOS)** — financial services complaints
- **Credit and Investments Ombudsman (CIO)** — credit and investment complaints
- **Superannuation Complaints Tribunal (SCT)** — super complaints

The consolidation created a single, more powerful dispute resolution body with higher compensation limits and broader jurisdiction.

## National Guarantee Fund (NGF)

The NGF is a fund maintained by the ASX that compensates investors who lose money due to the insolvency of an ASX market participant:

- **Purpose**: If an ASX broker becomes insolvent and cannot return your property (cash or securities), the NGF can compensate you
- **Coverage**: ASX-traded products (equities, ETFs, warrants, options) held or transacted through ASX market participants
- **No individual cap**: The NGF does not impose a per-claim maximum — the total fund is available (currently approximately AUD $100 million)
- **Trigger**: The broker must be declared insolvent and unable to meet its obligations to clients
- **Administered by**: Securities Exchanges Guarantee Corporation (SEGC)
- **CHESS interaction**: Because CHESS registers shares in your name, most shares survive broker insolvency without needing NGF compensation. The NGF primarily covers cash and unsettled trades

### NGF vs US SIPC vs UK FSCS

| Feature | NGF (Australia) | SIPC (US) | FSCS (UK) |
|---------|----------------|-----------|-----------|
| **Per-account limit** | No individual cap (fund is ~$100M total) | $500,000 (of which max $250K cash) | £85,000 per institution |
| **What's covered** | ASX broker insolvency | US broker-dealer insolvency | Bank/investment firm failure |
| **Share ownership model** | CHESS = direct ownership (shares survive insolvency) | Street name = shares at risk without SIPC | Nominee = shares at risk without FSCS |
| **Funding** | ASX levies | SIPC member assessments | Industry levies |
| **Crypto covered** | No | No | No |

## Client Money Rules

ASIC's client money regime (Corporations Act Part 7.8) requires AFSL holders to:

- **Segregate client money**: Client money must be held in designated trust accounts, separate from the firm's own money
- **Not use for own purposes**: AFSL holders cannot use client money for the firm's working capital, investments, or any purpose other than holding it for the client
- **Reconciliation**: Regular reconciliation of client money accounts required
- **Audit**: Client money accounts are subject to annual external audit
- **Notification**: ASIC must be notified immediately if there is any shortfall in client money

### Important Limitation
Client money rules apply to **money** (cash), not to **securities** — securities protection comes from CHESS (for ASX products) and the NGF. For CFD accounts (cmc-markets, ig-markets), client money rules are particularly important because all client funds are held as cash (there are no CHESS-registered securities in a CFD account).

## Negative Balance Protection

Since **March 2021**, ASIC requires negative balance protection for all retail CFD accounts:

- **Retail accounts cannot go below zero** — if a market move exceeds the client's margin, the broker absorbs the loss beyond zero
- This prevents the scenario (common before these rules) where a sudden market move could leave a retail trader owing the broker more than they deposited
- Applies to all CFD products: forex, shares, indices, commodities, crypto CFDs
- Applies to all AFSL-holding CFD providers operating in Australia
- **Does NOT apply to wholesale/professional client accounts** — wholesale clients can still incur negative balances

## Product Intervention Power

Since 2019, ASIC has had the power to proactively ban or restrict financial products without needing to prove that a specific law has been broken:

### Notable Product Interventions
| Year | Intervention | Impact |
|------|-------------|--------|
| **2021** | **Binary options banned** for retail investors | Complete ban — no retail binary options trading in Australia |
| **2021** | **CFD leverage restrictions** | Max 30:1 (major forex), 20:1 (minor forex/gold), 10:1 (commodities/indices), 5:1 (shares), 2:1 (crypto) |
| **2021** | **Negative balance protection** required for retail CFDs | Retail accounts cannot go below zero |
| **2021** | **Margin close-out** required at 50% of total margin | Positions must be closed when margin falls to 50% |
| **2022** | **Short-term credit** restrictions | Payday lending product interventions |

## Design and Distribution Obligations (DDO)

Effective October 2021, DDO is a proactive consumer protection measure:

- **Target Market Determination (TMD)**: Product issuers must define who the product is designed for — e.g., a crypto CFD product's TMD might specify "experienced traders who understand leverage, have a high risk tolerance, and can afford to lose their entire deposit"
- **Distribution controls**: Distributors must take reasonable steps to ensure the product reaches the target market — not just anyone who opens an account
- **Review triggers**: If significant numbers of consumers outside the target market are acquiring the product, the issuer must review and potentially amend the TMD
- **Reporting**: Distributors must report to issuers on distribution outcomes; issuers must report to ASIC on significant dealing outside the target market

## Financial Adviser Protections

When receiving financial advice in Australia:

- **Best interests duty**: Advisers must act in the client's best interests (s961B Corporations Act)
- **Appropriate advice**: Advice must be appropriate for the client's circumstances
- **Fee disclosure**: All fees must be disclosed upfront in the Financial Services Guide (FSG) and Statement of Advice (SoA)
- **Annual renewal (opt-in)**: Clients must actively opt in to ongoing fee arrangements each year — no more indefinite fee deductions
- **Professional indemnity insurance**: AFSL holders must carry PI insurance to compensate clients for losses caused by breaches
- **AFCA access**: If the advice is inappropriate, the client can complain to AFCA

## Cooling-Off Periods

For certain financial products, consumers have a **14-day cooling-off period** during which they can withdraw without penalty:

- Managed investment scheme interests (unit trusts, managed funds)
- Life insurance policies
- Superannuation products
- **NOT** direct share purchases, ETFs on market, or derivatives

During the cooling-off period, the consumer can cancel the product and receive a refund (adjusted for market movements in the case of managed funds).

## What Is NOT Protected

Understanding the limits of investor protection is as important as understanding the protections themselves:

| Scenario | Protection Available |
|----------|---------------------|
| **Broker insolvency (CHESS-sponsored ASX shares)** | Fully protected — shares are in your name |
| **Broker insolvency (cash in broker account)** | Client money rules + NGF |
| **Investment losses from market movements** | No protection — this is investment risk |
| **International shares in custodial accounts** | Depends on the custodian's jurisdiction — NOT covered by NGF or CHESS |
| **Crypto on AUSTRAC-registered exchanges** | AML/CTF compliance only — no AFCA, no NGF, no CHESS equivalent |
| **Crypto on unregistered exchanges** | No protection whatsoever |
| **[[defi]] protocols** | No protection — no regulated entity, no compensation, no dispute resolution |
| **Unregulated or unlicensed products** | No AFCA access — potentially fraudulent |
| **CFD/leveraged product losses within limits** | No protection — you can lose your entire deposit (but not more, due to negative balance protection) |
| **Scam losses** | Banks increasingly offering scam reimbursement (voluntary); AFCA may consider bank's obligations; no guaranteed compensation |

## Worked Scenario: A Broker Goes Insolvent

Consider a retail investor holding three asset types when their AU broker collapses. The outcome differs sharply by how the asset is held — illustrating why the *structure* of ownership, not just the broker's reputation, determines protection.

| Asset held with the failed broker | What happens | Layer that helps |
|---|---|---|
| **ASX shares, CHESS-sponsored (own HIN)** | Shares are registered in the investor's name on the ASX subregister; they survive untouched. The investor moves the HIN to a new broker. | Layer 1 (CHESS) — no claim needed |
| **ASX shares held in a custodial/nominee structure** | Shares are pooled in the broker's nominee; recovery depends on the administrator reconstructing records — more like the US "street name" risk. | Layers 2-3 (segregation + NGF) |
| **Cash in the broker's client account** | Should be in a segregated trust account; if a shortfall exists, the NGF may compensate for cash/unsettled trades, subject to the fund's rules and total size. | Layers 2-3 |
| **Crypto bought through the broker's offshore affiliate** | Typically outside CHESS, NGF, and often AFCA; recovery may depend on a foreign insolvency process. | None of the AU layers reliably apply |

The lesson: a CHESS-sponsored HIN converts broker insolvency from a *compensation* problem into an *administrative transfer* — which is why this page repeatedly recommends CHESS-sponsored brokers for AU equities.

## How the Schemes Relate to Each Other

These schemes are sometimes confused. They address different stages of the same risk:

| Question | Scheme |
|---|---|
| "My broker collapsed and my shares were in my name." | CHESS (no claim — shares are yours) |
| "My broker collapsed and there's a shortfall in my cash/unsettled trades." | NGF (last-resort fund) |
| "My broker is solvent but mishandled my money / gave bad advice / refused a claim." | AFCA (dispute resolution) |
| "The product was unsuitable / mis-sold to me." | [[asic\|ASIC]] conduct rules + AFCA |
| "I lost money because the market fell." | **No scheme** — that is investment risk |

A common misconception is that AFCA or the NGF insures against *losses*. Neither does. They address *misconduct* and *insolvency* respectively — never ordinary market risk. See [[risk-management]].

## Practical Checklist for Investors

1. **Check the AFSL register**: Before depositing money with any broker, adviser, or financial services provider, verify their AFSL on ASIC Connect (connectonline.asic.gov.au)
2. **Use CHESS-sponsored brokers**: For ASX shares and ETFs, always use a CHESS-sponsored broker — your shares are registered in your name
3. **Understand custodial arrangements**: For international shares (US stocks, global ETFs), understand whether the custodian provides equivalent protections — and that the NGF does not apply
4. **Check AUSTRAC registration**: For crypto exchanges, verify registration on the AUSTRAC DCE register
5. **Know your complaint options**: If something goes wrong with a regulated provider, contact AFCA (1800 931 678 or afca.org.au) — it's free
6. **Separate your assets**: Don't hold all investments with a single broker or exchange — diversification applies to counterparty risk too
7. **DeFi = unprotected**: If you use DeFi protocols, accept that you have no regulatory recourse if funds are lost

## Related

- [[asic]]
- [[australian-regulatory-framework]]
- [[afsl]]
- [[risk-management]]
- [[regulation]]
- [[vasp-regulation]]
- [[australian-investor-tax]]
- [[risk-management]]
- [[austrac]]
- [[afca]]

## Sources

- AFCA — Complaint resolution scheme rules (compensation caps are indexed; confirm current figure)
- ASIC — Regulatory Guide 126: Compensation arrangements for AFS licensees
- ASX / SEGC — National Guarantee Fund fact sheet
- ASIC — Product Intervention Orders (binary options ban; CFD leverage and negative-balance rules)
- ASIC — Regulatory Guide 274: Product design and distribution obligations (DDO)
- Australian Government — Corporations Act 2001, Parts 7.6-7.9 (AFSL, client money, market conduct)

> Figures, caps, and thresholds on this page are indicative as at the dates noted and are subject to annual indexation and legislative amendment. Not legal or financial advice — confirm current rules with ASIC, AFCA, or the ASX/SEGC.
