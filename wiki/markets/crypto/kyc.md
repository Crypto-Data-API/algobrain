---
title: "Know Your Customer (KYC)"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, regulation]
aliases: ["KYC", "Know Your Customer"]
domain: [regulation]
difficulty: beginner
related: ["[[regulation]]", "[[austrac]]", "[[aml]]", "[[aml-ctf]]", "[[vasp-regulation]]", "[[centralised-exchanges]]", "[[stablecoins]]"]
---

Know Your Customer (KYC) is the identity-verification process that financial institutions and centralised [[centralised-exchanges|crypto exchanges]] must perform on their users to comply with anti-money-laundering ([[aml-ctf|AML]]) and counter-terrorism-financing (CTF) regulations. KYC typically involves collecting a government-issued ID, proof of address, a selfie or liveness check, and sometimes source-of-funds documentation. It is the gateway that determines whether — and how much — a user can deposit, trade, and withdraw on a regulated venue. KYC is one component of the broader [[aml-ctf|AML/CTF]] compliance stack — alongside transaction monitoring, sanctions screening, and suspicious-activity reporting — that any [[vasp-regulation|Virtual Asset Service Provider (VASP)]] must operate to access banking and stay licensed.

## KYC in the AML/CTF Stack

KYC is the "front door" of a wider control framework. The components and how they interlock:

| Control | What it does | When it runs |
|---------|--------------|--------------|
| **CIP (Customer Identification Program)** | Verify the customer is who they claim — ID, DOB, address | At onboarding |
| **CDD (Customer Due Diligence)** | Assess customer risk, understand expected activity | At onboarding, refreshed periodically |
| **EDD (Enhanced Due Diligence)** | Deeper checks for high-risk customers (PEPs, high-risk jurisdictions, large flows) | Triggered by risk score |
| **Sanctions / watchlist screening** | Match customer + counterparties against OFAC, UN, EU lists | Onboarding + ongoing |
| **Transaction monitoring** | Flag anomalous patterns (structuring, mixer use, rapid in/out) | Continuous |
| **SAR / SMR filing** | Report suspicious activity to the financial intelligence unit | On trigger |
| **[[travel-rule|Travel Rule]] messaging** | Pass originator/beneficiary data with transfers between [[vasp-regulation|VASPs]] | Per qualifying transfer |

KYC feeds every downstream control: without a verified identity, sanctions screening and transaction monitoring have nothing to anchor to. This is why regulators treat weak KYC as a systemic failing rather than a paperwork lapse.

## Why KYC Exists

KYC is not a crypto-specific invention; it is inherited from traditional banking regulation. The goal is to attach a real-world identity to financial activity so that exchanges can screen against sanctions lists, detect money laundering, and report suspicious activity to regulators. For crypto exchanges, KYC is the price of operating legally and maintaining banking relationships (fiat on/off ramps). A platform that skips KYC risks losing its banking partners, being fined, or being shut down.

## Tiered KYC

Most exchanges implement **tiered verification**, where each level unlocks higher limits in exchange for more documentation:

| Tier | Typical requirements | Typical capability |
|------|----------------------|--------------------|
| **Tier 0 / Unverified** | Email + password only | View-only, or no trading; often crypto deposits but **no withdrawals** |
| **Tier 1 / Basic** | Name, DOB, country, government ID number | Limited daily withdrawal (e.g. up to a few thousand USD), basic trading |
| **Tier 2 / Intermediate** | Photo ID upload + selfie/liveness, proof of address | Higher withdrawal limits, fiat on/off ramps, derivatives |
| **Tier 3 / Full / Institutional** | Source-of-funds, source-of-wealth, enhanced due diligence (EDD) | High/unlimited limits, OTC, corporate accounts |

Limits scale with verification because higher money flows carry higher AML risk. Enhanced Due Diligence (EDD) is applied to high-risk customers — politically exposed persons (PEPs), users in high-risk jurisdictions, or accounts with unusual flow patterns.

## The Travel Rule

The **[[travel-rule|Travel Rule]]** (FATF Recommendation 16) requires that when value above a threshold (commonly ~USD/EUR 1,000) is transferred, the originating institution must pass identifying information about the sender and recipient ("originator" and "beneficiary") to the receiving institution. Originally written for bank wires, FATF extended it to **[[vasp-regulation|Virtual Asset Service Providers (VASPs)]]** — i.e. crypto exchanges — in 2019. In practice this means a withdrawal from one exchange to another can require name/wallet/identity data to "travel" alongside the crypto, and some exchanges now block or flag withdrawals to wallets they cannot identify. The Travel Rule is one of the main forces pushing crypto toward the same surveillance posture as banking.

A persistent friction is the **"sunrise problem"**: jurisdictions adopted the Travel Rule on different timelines, so a compliant VASP in one country may need to send data to a counterparty in a country that has not yet implemented it (or vice versa). Competing messaging standards (TRP, IVMS101 data format, and protocols like TRISA, Sygna, and Notabene) add further interoperability friction. The **"unhosted wallet" question** is the sharpest edge: when a user withdraws to a self-custodied wallet there is no counterparty VASP to receive the data, so some regulators require the exchange to collect (and sometimes verify ownership of) the destination address before releasing funds.

## KYC vs DeFi Privacy Tradeoff

KYC sits at the centre of crypto's defining tension between **regulatory compliance and permissionless privacy**:

- **Centralised exchanges (CeFi)** require full KYC. They are convenient, offer fiat ramps and customer support, but the user surrenders both custody and identity.
- **[[decentralized-exchanges|Decentralised exchanges (DEXs)]] and [[defi|DeFi]] protocols** generally require **no KYC** — anyone with a wallet can trade. This preserves privacy and access but offers no recourse, no support, and exposes users to smart-contract risk.

This gap is a form of **regulatory arbitrage** that governments are actively working to close — by pressuring front-end interfaces, sanctioning protocols (e.g. the Tornado Cash mixer sanctions), and exploring "KYC at the wallet/on-ramp layer." Privacy advocates counter that mandatory identity collection is both a civil-liberties and a security problem (see below). The likely long-run equilibrium is KYC at the fiat boundary (on/off ramps) while pure on-chain activity stays pseudonymous.

### Privacy-preserving KYC

An emerging middle ground tries to prove compliance facts without exposing raw documents:

- **Reusable / portable KYC** — verify once with a trusted provider, then present a credential to many venues, reducing the number of databases holding your passport.
- **Zero-knowledge proofs of personhood / jurisdiction / age** — prove "I am over 18 and not in a sanctioned country" without revealing name or document. Projects exploring this include zk-based identity credentials and proof-of-humanity schemes.
- **Soulbound / verifiable credentials** — on-chain attestations that a wallet passed KYC, decoupling the proof from the underlying PII.

These reduce — but do not eliminate — the honeypot problem, because some entity still performs the original verification and could be breached.

## Australia: AUSTRAC

In Australia, KYC and [[aml-ctf|AML/CTF]] obligations are enforced by **[[austrac|AUSTRAC]]** (the Australian Transaction Reports and Analysis Centre) under the *Anti-Money Laundering and Counter-Terrorism Financing Act 2006*. Crypto exchanges operating in Australia must register with AUSTRAC as **Digital Currency Exchange (DCE) providers**, perform customer identification, monitor transactions, and file Suspicious Matter Reports (SMRs) and Threshold Transaction Reports (TTRs) for cash transactions of AUD 10,000 or more. AUSTRAC has publicly pressured exchanges over crypto ATMs and scam-related flows.

### Other major regimes

| Jurisdiction | Framework / regulator | Notable KYC features |
|--------------|----------------------|----------------------|
| **EU** | MiCA + AMLR / 6AMLD; AMLA supervisor | Unified [[vasp-regulation|CASP]] licensing; EUR 1,000 Travel Rule threshold; tightening on unhosted-wallet transfers |
| **US** | FinCEN (BSA), state money-transmitter licences, IRS reporting | MSB registration, SAR/CTR filing, 1099 reporting, OFAC sanctions screening |
| **UK** | FCA cryptoasset registration | Mandatory AML registration; Travel Rule live since 2023 |
| **Singapore** | MAS under the Payment Services Act | DPT-service licensing with full KYC/CDD |
| **Australia** | [[austrac|AUSTRAC]] (DCE register) | SMRs, TTRs, AUD 10,000 threshold |

The common thread is convergence on the [[vasp-regulation|FATF VASP standard]]: register, identify customers, screen, monitor, and report.

## Data-Breach Risk

A core criticism of mandatory KYC is that it concentrates highly sensitive identity data — passports, driver licences, selfies, addresses — into exchange databases that become prime targets. Real incidents underline the danger:

- **Ledger (2020)** — a marketing-database breach exposed ~1 million emails and ~270,000 customers' full names, postal addresses, and phone numbers, leading to phishing and physical-extortion ("$5 wrench") threats against hardware-wallet owners.
- **Gemini (2022)** — a third-party incident exposed email addresses and partial phone numbers of ~5.7 million users.
- **Coinbase (2025)** — insiders bribed at overseas support contractors leaked customer data, used for targeted social-engineering scams.

These cases show that KYC creates a "honeypot" risk: the very data collected to fight crime can itself be stolen and weaponised against users.

## Trading Implications

KYC is not just a compliance footnote — it directly shapes how and where you can trade:

- **Withdrawal limits and freezes.** Un- or under-verified accounts often face low or zero withdrawal limits; an exchange can freeze withdrawals pending re-verification, stranding capital exactly when a trader wants to move.
- **Onboarding latency.** Full verification can take minutes to days; during fast markets, an unverified account cannot act.
- **Geographic gating.** KYC reveals residency; many venues geo-block users from restricted jurisdictions (e.g. US users barred from certain derivatives venues), and using a VPN to evade this can void the account.
- **Capital fragmentation.** Travel-Rule frictions and per-venue limits make moving size between exchanges slower, affecting arbitrage and rebalancing strategies.
- **Tax and reporting.** KYC links on-chain activity to identity, feeding exchange tax reporting (e.g. 1099 forms in the US) and on-chain analytics.

## Related

- [[aml-ctf]] — the anti-money-laundering / counter-terrorism-financing framework KYC anchors
- [[vasp-regulation]] — the FATF VASP standard that mandates KYC for exchanges
- [[travel-rule]] — originator/beneficiary data passed between VASPs
- [[regulation]] — broader regulatory context
- [[austrac]] — the Australian AML/CTF regulator
- [[aml]] — anti-money-laundering framework KYC serves
- [[centralised-exchanges]] — where KYC is mandatory
- [[decentralized-exchanges]] — the no-KYC alternative
- [[defi]] — the permissionless ecosystem in tension with KYC
- [[stablecoins]] — increasingly subject to issuer-level KYC/freeze powers

## Sources

- General market knowledge; no specific wiki source ingested yet.
