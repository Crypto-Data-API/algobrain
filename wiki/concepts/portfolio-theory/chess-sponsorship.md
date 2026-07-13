---
title: "CHESS Sponsorship"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [australia, market-microstructure, exchanges, regulation]
aliases: ["CHESS", "CHESS Sponsored", "Holder Identification Number", "HIN"]
domain: [market-microstructure]
difficulty: beginner
prerequisites: []
related: ["[[australian-investing]]", "[[commsec]]", "[[selfwealth]]", "[[nabtrade]]", "[[bell-direct]]", "[[morgans]]", "[[risk-management]]", "[[market-microstructure]]", "[[smsf]]", "[[superannuation]]", "[[asic]]"]
---

CHESS (Clearing House Electronic Subregister System) is Australia's electronic system for the registration, transfer, and settlement of ASX-listed securities. It is one of the most distinctive features of the Australian market — when you buy shares through a CHESS-sponsored broker, ownership is registered directly in YOUR name on the ASX's electronic subregister, not held by a broker or custodian on your behalf. This direct ownership model provides a level of investor protection that is uncommon in global markets.

## Overview

CHESS was introduced by the ASX in 1994 to replace paper-based share certificates with electronic records. It serves two primary functions:

1. **Settlement**: Facilitating the transfer of shares and payment between buyers and sellers (T+2 settlement cycle)
2. **Registration**: Maintaining an electronic record of who owns which shares, registered to individual Holder Identification Numbers (HINs)

Every investor who trades through a CHESS-sponsored broker receives a **HIN (Holder Identification Number)** — a unique 10-digit identifier starting with "X" (e.g., X0012345678). This HIN links your identity directly to the ASX's subregister, establishing you as the legal owner of the shares.

> This page describes the factual operation of the ASX CHESS holding model. It is general information, not financial, tax or legal advice — confirm current arrangements with your broker, the [[asic|ASX/ASIC]], or a licensed adviser.

### Key Terms

| Term | Meaning |
|---|---|
| **CHESS** | Clearing House Electronic Subregister System — the ASX's electronic settlement and registration system |
| **HIN** | Holder Identification Number — your unique 10-digit identifier on the CHESS subregister (starts with "X") |
| **SRN** | Securityholder Reference Number — used for **issuer-sponsored** holdings (managed by the company's share registry, starts with "I"), not CHESS |
| **Subregister** | The portion of a company's share register; the CHESS subregister holds CHESS-sponsored holdings, the issuer-sponsored subregister holds SRN holdings |
| **Sponsoring participant** | Your broker, who links your HIN to CHESS but does **not** own your shares |
| **Holding statement** | Monthly/event-based confirmation of your holdings (sent when a holding changes) |
| **Settlement (T+2)** | Trade date plus two business days for shares and cash to change hands |

### CHESS-sponsored vs Issuer-sponsored

Both are forms of **direct registered ownership** in Australia — the distinction is who administers the holding:

| Feature | CHESS-sponsored (HIN) | Issuer-sponsored (SRN) |
|---|---|---|
| Administered by | Your broker via CHESS | The company's share registry (e.g., Computershare, Link) |
| Identifier | HIN (starts "X") | SRN (starts "I") |
| To sell | Through any CHESS broker | Must first convert to a HIN or use a one-off sale facility |
| Portability | Move HIN between CHESS brokers | Tied to that issuer's registry |
| Common origin | Buying on-market through a broker | IPO allocations, DRP, off-market issues |

Both models keep you as the legal registered owner — distinct from the US street-name system described below.

## How CHESS Works

### The CHESS-Sponsored Model

1. You open an account with a CHESS-sponsored broker (e.g., [[commsec]], [[nabtrade]], [[bell-direct]])
2. The broker "sponsors" your HIN — they are your link to the CHESS system, but they do NOT own your shares
3. When you buy shares, the ASX registers ownership under your HIN on the electronic subregister
4. You receive a **CHESS holding statement** (via mail or email) confirming the registration
5. Dividends, corporate actions (rights issues, buybacks), and voting rights flow directly to you as the registered owner

### Key Difference from the US "Street Name" System

| Feature | Australia (CHESS) | United States (Street Name) |
|---------|-------------------|---------------------------|
| **Registered owner** | YOU — the individual investor | Your broker (e.g., Schwab, Fidelity) |
| **Where shares are held** | ASX subregister under your HIN | Broker's omnibus account at DTC/Cede & Co |
| **Broker insolvency** | Shares are safe — registered to your HIN, not the broker | Shares are held by broker — SIPC insurance required |
| **Transfer to new broker** | Transfer HIN to new broker — no need to sell | Must initiate ACATS transfer — can take days |
| **Corporate actions** | Direct from company to you | Via broker (may be delayed or incomplete) |
| **Voting rights** | Direct — you receive proxy materials | Via broker — "street name" voting, often complex |
| **Visibility on register** | Company can see you as a shareholder | Company sees broker, not you |

In the US, when you "own" shares through a broker, they are legally held in the name of the Depository Trust Company (DTC) subsidiary Cede & Co. You have a beneficial interest but not direct registered ownership. In Australia, CHESS ensures you are the **legal registered owner**.

## Broker Insolvency Protection

This is the most practically important benefit of CHESS. If your broker goes bankrupt:

- **CHESS model**: Your shares are on the ASX's register under your HIN. The broker's creditors have no claim on them. You simply transfer your HIN to a new broker and continue trading. Your shares are completely safe.
- **Custodial model**: Your shares are held by the custodian. While they should be segregated from the custodian's own assets, the process of recovering them can be complex and time-consuming. There is a (small) risk of loss if the custodian commingled assets.

This protection is a form of counterparty [[risk-management]] — by owning shares directly rather than through an intermediary, you eliminate the broker as a single point of failure.

### Historical Example

When broker Opes Prime collapsed in 2008, clients who held shares via CHESS (direct registration) retained ownership. However, Opes Prime had also used a securities lending structure where client shares were lent out — those clients lost their shares because they had transferred ownership as part of the lending agreement. The distinction between CHESS-registered shares and shares subject to lending arrangements was critical.

## HIN Portability

One of CHESS's most practical advantages is HIN portability:

- Your HIN can be **transferred to a new broker** without selling and rebuying your shares
- This avoids triggering capital gains tax events that would occur if you had to sell and rebuy
- The transfer process typically takes 3–5 business days
- You fill out a "Broker-to-Broker Transfer" form with both the old and new broker
- All your share holdings, with their original acquisition dates and cost bases, move with the HIN

This contrasts with custodial models where changing brokers often requires selling all positions with one broker and rebuying with another — triggering capital gains, losing cost base continuity, and paying brokerage twice.

## Verifying and Protecting Your Holdings

Because the register is the source of truth, investors can independently confirm ownership:

- **Holding statements** arrive whenever a holding changes (a buy, sell, or corporate action) and periodically thereafter. Keep them — they are also useful as [[capital-gains]] cost-base evidence.
- **Company share registries** (Computershare, Link/MUFG, Boardroom, Automic) let you view holdings tied to your details, set a communication preference, and manage [[dividend|dividends]] / [[franking-credits]].
- **HIN locking / CHESS holding lock** — investors can request a lock on their HIN with their sponsoring broker to prevent unauthorised off-market transfers, mitigating identity-theft risk.
- **Reconcile against the register** — your broker's portfolio view should match the holding statements; discrepancies should be queried promptly.

This verifiability is itself a [[risk-management]] feature: the investor is not reliant solely on a broker's internal ledger.

## CHESS vs Custodial/Nominee Models

Some Australian brokers (particularly newer fintechs) have used custodial or nominee models for some or all of their offerings:

| Feature | CHESS Sponsored | Custodial/Nominee |
|---------|----------------|-------------------|
| **Ownership** | Directly in your name on ASX register | Held by custodian on your behalf |
| **HIN** | Personal HIN — unique to you | No personal HIN — shares pooled under custodian's HIN |
| **Broker insolvency** | Shares fully protected | Depends on custodian structure and segregation |
| **Portability** | Transfer HIN to any CHESS broker | Must sell and rebuy, or wait for complex custodian transfer |
| **Corporate actions** | Direct from company | Via custodian (may be delayed) |
| **Cost** | Sometimes slightly higher brokerage | Often lower brokerage (part of the cost saving) |
| **International shares** | CHESS only covers ASX — international via custodian | Can cover both ASX and international |
| **Fractional shares** | Not supported by CHESS | Can be supported via custodial structure |

## Which Brokers Are CHESS-Sponsored?

### Full CHESS Sponsorship (ASX Shares)

| Broker | CHESS Sponsored | Notes |
|--------|----------------|-------|
| [[commsec]] | Yes | CBA-owned, Australia's largest broker |
| [[selfwealth]] | Yes | $9.50 flat fee discount broker |
| [[nabtrade]] | Yes | NAB-owned, options + international |
| [[bell-direct]] | Yes | Bell Financial Group, Bell Potter research |
| [[morgans]] | Yes | Full-service, 40+ offices |
| [[ig-markets]] | Yes | CHESS for ASX shares, CFDs also available |
| [[cmc-markets]] | Yes | CHESS for ASX shares, major CFD platform |
| [[stake]] | Yes (ASX only) | US shares held via DriveWealth (custodial) |
| [[superhero]] | Yes (since 2023) | Switched from custodial to CHESS after industry criticism |
| [[interactive-brokers]] | Yes | Global broker, CHESS for ASX |

### Important Note on International Shares

CHESS **only covers ASX-listed securities**. When you buy US, UK, or other international shares through an Australian broker, those shares are held via a **custodian** (e.g., DriveWealth for [[stake]], Pershing for [[commsec]]). You do not get a HIN for international holdings — they are held in nominee/custodial structures, similar to the US domestic model.

This means the direct ownership protection of CHESS does not extend to international share portfolios held through Australian brokers.

## CHESS for SMSFs

[[smsf|Self-Managed Super Funds]] particularly benefit from CHESS:

- SMSF shares are registered under the **fund's HIN** (separate from any personal HIN)
- This provides clear legal separation between personal and SMSF assets — critical for compliance
- Direct [[dividend]] payments and [[franking-credits]] flow to the SMSF's bank account
- SMSF trustees can see exactly which shares the fund owns on the ASX register
- Multiple CHESS-sponsored brokers offer dedicated SMSF account types: [[commsec]], [[nabtrade]], [[bell-direct]], [[morgans]]

## CHESS Replacement Project (Failed)

The ASX embarked on an ambitious project to replace CHESS with a new system built on distributed ledger technology (DLT / blockchain):

| Date | Event |
|------|-------|
| **2017** | ASX announced plan to replace CHESS with a DLT-based system developed by Digital Asset Holdings |
| **2018–2020** | Multiple delays as industry consultation revealed complexity of replacing core market infrastructure |
| **2021** | Go-live date pushed to April 2023 |
| **2022** | ASX announced further delays, commissioned independent review |
| **November 2022** | ASX **abandoned the DLT-based replacement** after an independent review found the project was not fit for purpose |
| **2023** | ASX announced it would pursue a conventional (non-DLT) replacement — writing off **$250 million+** spent on the failed DLT project |
| **2023–present** | New replacement project underway, with no confirmed go-live date |

The failed CHESS replacement became one of Australia's most high-profile technology project failures. [[asic|ASIC]] subsequently investigated ASX's market disclosures about the project's status. The existing CHESS system — now over 30 years old — continues to operate and remains reliable, but its age is a growing concern for market infrastructure resilience.

## Settlement Mechanics (T+2)

CHESS performs the *settlement* leg of every ASX trade, not just registration:

1. **Trade date (T)** — broker executes your order on the ASX order book.
2. **T+1** — trade details are confirmed and netted through CHESS; obligations are calculated.
3. **T+2** — delivery-versus-payment (DvP) settlement: shares move on the subregister to your HIN while cash settles simultaneously, eliminating the risk that one side delivers without receiving.

This DvP design is a core market-microstructure safeguard: neither counterparty is exposed to the other's default during settlement. A faster cycle (e.g., a move toward T+1, as some markets have adopted) would compress this window further but increases operational pressure — one of the considerations weighed in CHESS's replacement program.

## Tax and Cost-Base Continuity

Because HIN portability moves holdings *with their original acquisition dates and cost bases*, CHESS sponsorship interacts directly with [[capital-gains]] and broader [[australian-investor-tax|Australian investor tax]]:

- Transferring a HIN between brokers is **not a CGT event** — no disposal occurs, so no gain is crystallised.
- Holding statements provide contemporaneous cost-base records.
- For [[smsf|SMSFs]], the fund's HIN keeps fund assets clearly segregated from personal assets for audit and compliance.

By contrast, custodial models that require selling and rebuying to change provider can trigger CGT events and break cost-base continuity.

## Connection to Risk Management

CHESS is fundamentally a [[risk-management]] tool for Australian investors:

- **Counterparty risk mitigation**: Direct ownership eliminates the risk of broker failure affecting your share holdings
- **Transparency**: You can verify your holdings directly on the ASX register
- **Legal clarity**: As the registered owner, your rights are clearly defined under Australian law
- **Portability**: The ability to move your HIN between brokers means you are never locked in to a single intermediary

For investors building long-term portfolios — particularly within [[superannuation]] or [[smsf|SMSFs]] — CHESS provides a foundation of ownership security that supports the confidence needed for [[compounding]] wealth over decades.

## Related

- [[australian-investing]]
- [[australian-investor-tax]] — CGT and cost-base continuity on HIN transfers
- [[capital-gains]] — why a HIN transfer is not a disposal
- [[commsec]]
- [[selfwealth]]
- [[nabtrade]]
- [[bell-direct]]
- [[morgans]]
- [[risk-management]]
- [[market-microstructure]]
- [[insider-trading-australia]] — companion ASX market-integrity topic
- [[smsf]]
- [[superannuation]]
- [[asic]]

## Sources

- ASX — CHESS and settlement information
- ASIC — Share ownership and broker regulation guidance
- ASX — CHESS replacement project announcements
- ASX — Listing and settlement (T+2) operating rules
- *General information on the ASX CHESS holding model — not financial, tax or legal advice.*
