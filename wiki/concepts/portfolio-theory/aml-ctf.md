---
title: "AML/CTF (Anti-Money Laundering & Counter-Terrorism Financing)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [regulation, australia, compliance, crypto, banking]
aliases: ["AML/CTF", "Anti-Money Laundering", "Counter-Terrorism Financing", "AML", "KYC/AML"]
related: ["[[austrac]]", "[[asic]]", "[[vasp-regulation]]", "[[regulation]]", "[[cryptocurrency-tax-australia]]", "[[wash-trading]]", "[[binance]]", "[[coinbase]]", "[[australian-regulatory-framework]]", "[[australian-crypto-regulation]]"]
domain: [regulation]
difficulty: intermediate
---

Anti-Money Laundering and Counter-Terrorism Financing (AML/CTF) is the regulatory framework designed to prevent the financial system from being used to launder the proceeds of crime or finance terrorism. In Australia, the framework is governed by the **Anti-Money Laundering and Counter-Terrorism Financing Act 2006** (AML/CTF Act), administered by [[austrac|AUSTRAC]]. For Australian investors and traders, AML/CTF compliance manifests primarily as KYC (Know Your Customer) requirements at brokers and exchanges, transaction monitoring, and reporting obligations that affect how quickly and freely money can move.

> **Not legal or compliance advice.** This page is an indicative, qualitative overview of how AML/CTF rules work and how they affect ordinary investors. Thresholds, penalties, lists, and obligations change over time and differ by jurisdiction. Reporting entities must rely on the current legislation, [[austrac|AUSTRAC]] guidance, and qualified compliance counsel — not this summary.

## Overview

Money laundering is the process of making illegally obtained money appear legitimate. The AML/CTF framework aims to detect and prevent this by requiring financial institutions and other "reporting entities" to know who their customers are, monitor their transactions, and report suspicious activity to the authorities. Australia's framework follows international standards set by the **Financial Action Task Force (FATF)**, the global AML standard-setter.

The AML/CTF Act 2006 replaced the earlier Financial Transaction Reports Act 1988 and significantly expanded both the scope of regulated entities and the depth of compliance obligations. The 2017 amendment to include digital currency exchanges (effective April 2018) was a landmark change that brought the crypto industry under AML/CTF regulation.

## Who Must Comply

The following "reporting entities" must comply with the AML/CTF Act:

| Entity Type | Examples |
|-------------|---------|
| **Banks and ADIs** | CBA, Westpac, NAB, ANZ, credit unions, building societies |
| **Securities dealers** | commsec, selfwealth, nabtrade, ig-markets, cmc-markets |
| **Insurance companies** | General insurers, life insurers |
| **Superannuation providers** | Industry funds, retail funds (APRA-regulated) |
| **Gambling providers** | Casinos, online betting operators |
| **Bullion dealers** | Gold and precious metal dealers |
| **Remittance providers** | Money transfer services (Western Union, etc.) |
| **Digital currency exchanges** | [[binance]] Australia, [[coinbase]] Australia, CoinSpot, Independent Reserve, BTC Markets |
| **Financial planners/advisers** | Under certain circumstances |
| **Lawyers and accountants** | Currently partial coverage — "Tranche 2" reforms would expand this |

## The Three Pillars of AML Compliance

### 1. Customer Due Diligence (CDD) / KYC

Every reporting entity must verify the identity of its customers before providing services:

- **Standard CDD**: Verify identity using the 100-point identification check — combination of primary ID (passport, driver's licence = 70 points each) and secondary documents (bank statement, utility bill = 25-40 points each)
- **Simplified CDD**: Lower verification for low-risk customers and low-value transactions (not commonly applied by exchanges or brokers)
- **Enhanced Due Diligence (EDD)**: Additional scrutiny required for:
  - **Politically Exposed Persons (PEPs)**: Politicians, senior government officials, military leaders, and their associates/family members — treated as higher risk due to potential for corruption
  - **High-risk jurisdictions**: Countries on the FATF grey list or black list (e.g., Myanmar, Iran, North Korea)
  - **Complex ownership structures**: Trusts, shell companies, nominees
  - **Unusual or high-value transactions**: Patterns inconsistent with the customer's profile
- **Ongoing CDD**: Identity verification is not a one-time event — entities must continuously update customer information and monitor for changes

### 2. Transaction Monitoring

Reporting entities must implement systems (typically automated) to detect suspicious transaction patterns:

- **Structuring (smurfing)**: Deliberately splitting transactions into amounts below $10,000 to avoid Threshold Transaction Report (TTR) obligations — this is a **criminal offence** under s142 of the AML/CTF Act, punishable by up to **5 years imprisonment**, even if the underlying funds are entirely legitimate
- **Rapid movement of funds**: Money deposited and immediately transferred or withdrawn
- **Round-dollar transactions**: Repeated transactions of suspiciously round amounts
- **Inconsistency with profile**: A customer whose declared income is $50K/year suddenly depositing $500K
- **Layering patterns**: Funds moved through multiple accounts, institutions, or jurisdictions to obscure the trail
- **Crypto-specific patterns**: Use of mixing/tumbling services, privacy coins ([[bitcoin|Monero]], Zcash), chain-hopping (converting between blockchains to obscure origin), interaction with known high-risk wallet addresses

### 3. Reporting

Three mandatory report types must be submitted to [[austrac|AUSTRAC]]:

| Report | Trigger | Timeframe |
|--------|---------|-----------|
| **Threshold Transaction Report (TTR)** | Cash transactions of **AUD $10,000 or more** | Within 10 business days |
| **Suspicious Matter Report (SMR)** | Any activity suspected of relating to ML, TF, tax evasion, or other serious offences — **no dollar threshold** | 24 hours (terrorism-related) or 3 business days (other) |
| **International Funds Transfer Instruction (IFTI)** | All electronic transfers into or out of Australia, regardless of amount | Within 10 business days |

**Tipping off**: Informing a customer that an SMR has been (or will be) filed about them is a **criminal offence** under s123 of the AML/CTF Act, punishable by up to **2 years imprisonment**. This means brokers and exchanges cannot tell you if they have reported you.

## Money Laundering Stages

The standard three-stage model of money laundering:

1. **Placement**: Introducing illicit funds into the financial system — cash deposits, purchasing monetary instruments, crypto purchases with cash
2. **Layering**: Moving and transforming the funds through multiple transactions to create distance from the source — wire transfers between accounts, currency conversion, crypto mixing, trade-based laundering
3. **Integration**: Returning the "cleaned" funds to the legitimate economy — real estate purchases, business investment, luxury goods

AML/CTF controls are designed to detect activity at all three stages, but are most effective at the placement stage (where cash enters the system) and at the layering stage (where patterns of unusual transactions can be detected).

## Record Keeping

All reporting entities must retain:
- Customer identification records — for **7 years** after the business relationship ends
- Transaction records — for **7 years** from the date of the transaction
- AML/CTF program documentation — for the life of the program plus 7 years
- Correspondence with AUSTRAC — for 7 years

## AML/CTF Program

Every reporting entity must have a documented AML/CTF program that includes:
- Board-level governance and accountability
- Risk assessment methodology
- Customer identification and verification procedures
- Transaction monitoring procedures
- Employee training requirements
- Independent review/audit (at least every 3 years)
- Record-keeping procedures
- Procedures for reporting to AUSTRAC

## FATF and International Standards

The **Financial Action Task Force (FATF)** is the international body that sets AML/CTF standards. Australia is a founding member (since 1989). Key FATF concepts:

- **40 Recommendations**: The core international AML/CTF standards that member countries must implement
- **Mutual Evaluations**: Peer reviews of each country's AML/CTF framework — Australia's last evaluation was in 2015 (rated "compliant" or "largely compliant" on most recommendations)
- **Grey List**: Countries with strategic AML/CTF deficiencies — being grey-listed restricts a country's access to the global financial system and increases transaction costs
- **Black List**: Countries with severe deficiencies and no commitment to reform (currently: Iran, Myanmar, North Korea)
- **Travel Rule**: FATF Recommendation 16 — requires financial institutions (including crypto exchanges) to share originator and beneficiary information for transfers above a threshold (AUD $1,000 in Australia for crypto)

### FATF Implementation Across Major Jurisdictions

FATF sets the global standard; each member implements it through a domestic regulator and statute. The structure is broadly parallel — KYC, monitoring, reporting to a Financial Intelligence Unit (FIU) — but thresholds and naming differ. Indicative, non-exhaustive:

| Jurisdiction | Primary AML regulator / FIU | Core statute(s) | Crypto coverage |
|---|---|---|---|
| Australia | [[austrac\|AUSTRAC]] | AML/CTF Act 2006 | Digital currency exchanges since Apr 2018; Tranche 2 expanding |
| United States | FinCEN (Treasury) | Bank Secrecy Act; USA PATRIOT Act | MSB registration for exchanges; OFAC sanctions overlay |
| European Union | National FIUs + AMLA (new EU authority) | AML Directives (5AMLD/6AMLD); MiCA for crypto | CASPs under MiCA + Transfer of Funds Regulation |
| United Kingdom | FCA (+ NCA for FIU) | Money Laundering Regulations 2017; POCA 2002 | Cryptoasset firms must register with the FCA |
| Singapore | MAS | AML/CFT notices; Payment Services Act | Digital payment token services licensed under PSA |

The common thread is FATF's **40 Recommendations** and the risk-based approach: obligations scale with assessed money-laundering / terrorism-financing risk rather than a one-size rule.

## Crypto-Specific AML Challenges

Cryptocurrency creates unique challenges for the AML/CTF framework:

| Challenge | Description |
|-----------|-------------|
| **Pseudonymity** | Blockchain addresses are pseudonymous — linked to alphanumeric strings, not identities (though blockchain analysis firms like Chainalysis can increasingly de-anonymise) |
| **Cross-border transfers** | Crypto moves across borders instantly without using traditional correspondent banking |
| **Mixing/tumbling** | Services like Tornado Cash (sanctioned by US OFAC in 2022) deliberately obscure transaction trails |
| **Privacy coins** | Monero, Zcash, and others offer enhanced privacy that makes tracing difficult or impossible |
| **[[defi]] protocols** | No central entity to apply KYC or report suspicious transactions — smart contracts execute autonomously |
| **Peer-to-peer trading** | Direct trades between individuals can bypass exchange-based AML controls |
| **Chain-hopping** | Converting between blockchains to break the tracing chain |
| **[[nft]] washing** | Using NFT sales to move value with plausible deniability |

## Penalties

### Criminal Penalties (for money laundering offences)
- Division 400 of the Criminal Code Act 1995
- Money laundering: up to **25 years imprisonment** and/or fines of up to **$555,000** per offence for individuals
- Dealing with proceeds of crime: up to **20 years imprisonment**
- Structuring: up to **5 years imprisonment**

### Civil Penalties (for reporting entity compliance failures)
- Failure to implement adequate AML/CTF program: up to **$22.2 million** per contravention for corporations
- Failure to report (TTR, SMR, IFTI): penalties per contravention — can aggregate to billions (as seen in the CBA and Westpac cases)
- AUSTRAC can also issue remedial directions, enforceable undertakings, and infringement notices

## Impact on Investors and Traders

AML/CTF compliance affects everyday investing in several practical ways:

1. **KYC delays**: Opening a new brokerage or exchange account requires identity verification — can take hours to days depending on the provider
2. **Large withdrawal delays**: Withdrawing large sums may trigger additional verification or temporary holds while the entity assesses whether an SMR is required
3. **Source of funds requests**: For large deposits or withdrawals, brokers and exchanges may request documentation proving the source of funds (payslips, property settlement statements, etc.)
4. **Banking restrictions**: Australian banks have restricted crypto-related transactions — CBA blocked payments to some exchanges, Westpac imposed $10K monthly limits on crypto exchange transfers
5. **Travel Rule impact**: Crypto transfers between exchanges above $1,000 may require additional sender/receiver information, potentially slowing the process
6. **International transfers**: All international wire transfers are reported to AUSTRAC regardless of amount
7. **Data sharing with ATO**: AUSTRAC data is accessible to the ATO for tax compliance — this is why the ATO knows about your crypto holdings even if you don't report them

### Practical trader checklist (indicative)

| Friction point | What triggers it | Practical mitigation |
|---|---|---|
| Account onboarding delay | KYC / 100-point ID check | Have passport + driver's licence ready; expect hours-to-days |
| Large deposit/withdrawal hold | Threshold (TTR ≥ A$10k cash) or pattern flags | Keep proof of source-of-funds (payslips, settlement statements) |
| Crypto transfer delay | Travel Rule (≥ A$1,000) | Use exchanges that share originator/beneficiary data cleanly |
| Banking restrictions on crypto | Bank-level de-risking (e.g., CBA/Westpac limits) | Use bank channels the exchange supports; expect monthly caps |
| Inadvertent "structuring" risk | Splitting cash to stay under A$10k | **Never** split deliberately — structuring is a criminal offence even with clean funds |
| ATO visibility | AUSTRAC ↔ ATO data sharing | Report crypto gains; assume holdings are already visible |

These are indicative compliance frictions, not legal advice — see the disclaimer at the top of this page.

## Related

- [[austrac]]
- [[asic]]
- [[vasp-regulation]]
- [[regulation]]
- [[cryptocurrency-tax-australia]]
- [[wash-trading]]
- [[binance]]
- [[coinbase]]
- [[australian-regulatory-framework]]
- [[australian-crypto-regulation]]
- [[kyc]] — the customer-identification pillar of AML
- [[defi]] — the hardest case for applying AML controls
- [[nft]] — NFT-based value-washing risk
- [[sanctions]] — overlapping OFAC / financial-sanctions regime

## Sources

- Australian Government — Anti-Money Laundering and Counter-Terrorism Financing Act 2006
- AUSTRAC — AML/CTF compliance guides
- FATF — International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation
- AUSTRAC — Reporting obligations for reporting entities

General market knowledge; no specific wiki source ingested yet.
