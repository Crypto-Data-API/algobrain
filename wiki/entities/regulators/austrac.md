---
title: "AUSTRAC (Australian Transaction Reports and Analysis Centre)"
type: entity
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [regulation, australia, aml, crypto, compliance]
aliases: ["AUSTRAC", "Australian Transaction Reports and Analysis Centre"]
entity_type: regulator
founded: 1989
headquarters: "Canberra, Australia"
website: "https://austrac.gov.au"
related: ["[[asic]]", "[[apra]]", "[[aml-ctf]]", "[[vasp-regulation]]", "[[australian-investing]]", "[[binance]]", "[[coinbase]]", "[[cryptocurrency-tax-australia]]", "[[sec]]", "[[regulation]]", "[[australian-regulatory-framework]]", "[[australian-crypto-regulation]]"]
---

AUSTRAC is Australia's financial intelligence agency and anti-money laundering/counter-terrorism financing (AML/CTF) regulator. Established in 1989, it serves as the Australian equivalent of the US FinCEN (Financial Crimes Enforcement Network), monitoring financial transactions for money laundering, terrorism financing, and other financial crimes. Since April 2018, AUSTRAC's remit has expanded to include digital currency exchanges (DCEs), making it a critical regulator for Australian crypto investors and traders.

## Overview

AUSTRAC operates under two distinct mandates. First, it is Australia's **financial intelligence unit (FIU)** — it collects, analyses, and disseminates financial intelligence to law enforcement and national security agencies. Second, it is the **regulator** responsible for ensuring that businesses in the financial sector comply with the [[aml-ctf|Anti-Money Laundering and Counter-Terrorism Financing Act 2006]] (AML/CTF Act). These dual roles mean AUSTRAC both sets compliance standards and uses the resulting data to detect criminal activity.

AUSTRAC regulates a broad range of "reporting entities" including banks, credit unions, building societies, casinos, remittance (money transfer) providers, bullion dealers, and — since 2018 — digital currency exchanges. It does **not** regulate the cryptocurrency assets themselves (that falls to [[asic|ASIC]]) — AUSTRAC regulates the exchanges and intermediaries that facilitate crypto transactions.

## Key Legislation

The **Anti-Money Laundering and Counter-Terrorism Financing Act 2006** (AML/CTF Act) is the primary legislation governing AUSTRAC's regulatory functions. It was significantly amended in 2017 to bring digital currency exchanges under AUSTRAC's purview (effective April 2018). See [[aml-ctf]] for a comprehensive overview of the AML/CTF framework.

Additional legislation:
- **Financial Transaction Reports Act 1988** (FTR Act) — the original reporting framework, now largely superseded by the AML/CTF Act
- **Anti-Money Laundering and Counter-Terrorism Financing Rules Instrument 2007** — detailed compliance rules made under the AML/CTF Act

## Reporting Obligations

All reporting entities regulated by AUSTRAC must submit the following reports:

### Threshold Transaction Reports (TTR)
- **Trigger**: Any cash transaction of **AUD $10,000 or more** (or foreign currency equivalent)
- Physical cash only — electronic transfers are covered separately
- Must be reported within 10 business days

### Suspicious Matter Reports (SMR)
- **Trigger**: Any transaction or activity that the reporting entity suspects, on reasonable grounds, may be related to money laundering, terrorism financing, tax evasion, or other serious offences
- **No dollar threshold** — suspicion is the trigger, regardless of amount
- Must be reported within 24 hours (terrorism-related) or 3 business days (other)
- **Tipping off is a criminal offence** — the reporting entity must NOT inform the customer that an SMR has been filed

### International Funds Transfer Instructions (IFTI)
- **Trigger**: All electronic funds transfers into or out of Australia, regardless of amount
- Includes wire transfers, SWIFT payments, and cross-border crypto transfers under the Travel Rule
- Must be reported within 10 business days

## Customer Due Diligence (KYC)

AUSTRAC requires all reporting entities to verify the identity of their customers before providing services:

- **100-point identification check**: Combination of primary documents (passport, driver's licence) and secondary documents (utility bills, bank statements)
- **Ongoing monitoring**: Entities must monitor customer transactions on an ongoing basis for consistency with the customer's known profile
- **Enhanced Due Diligence (EDD)**: Required for high-risk customers including Politically Exposed Persons (PEPs), customers from high-risk jurisdictions (FATF grey/black list countries), and customers with complex or unusual transaction patterns
- **Record keeping**: All customer identification records and transaction records must be retained for **7 years**

## Notable Enforcement Actions

AUSTRAC has pursued some of the largest corporate penalties in Australian history:

### Commonwealth Bank of Australia — $700 Million (2018)
The largest fine in Australian corporate history at the time. CBA was found to have committed **53,750 breaches** of the AML/CTF Act, including:
- Failure to report over **$625 million** in suspicious transactions through its Intelligent Deposit Machines (IDMs)
- IDMs accepted anonymous cash deposits of up to $20,000 — criminals exploited this for money laundering
- Late or non-filing of TTRs and SMRs
- Inadequate customer due diligence

### Westpac — $1.3 Billion (2020)
Surpassed CBA as the largest Australian corporate penalty. Westpac was found to have committed approximately **23 million breaches** of the AML/CTF Act, including:
- Failure to report over 19.5 million International Funds Transfer Instructions (IFTIs) totalling over $11 billion
- Failure to assess money laundering and terrorism financing risks associated with correspondent banking relationships
- Transfers linked to **child exploitation** in Southeast Asia — the single most damaging allegation, which led to the CEO's resignation
- Inadequate customer due diligence on high-risk customers

### Crown Resorts — Investigation and Remediation
Crown Resorts was investigated by AUSTRAC (alongside state-level casino regulators and a Royal Commission in Victoria) for:
- Allowing junket operators linked to organised crime to use casino accounts for money laundering
- Inadequate AML/CTF controls at Crown Melbourne and Crown Perth
- Led to Crown losing its casino licence suitability in multiple states and ultimately being acquired by Blackstone

### SkyCity Adelaide — $67 Million (2024)
AUSTRAC took civil penalty action against SkyCity Adelaide for systematic failures in its AML/CTF compliance program, including:
- Failure to conduct appropriate customer due diligence
- Failure to monitor customers and report suspicious transactions
- Inadequate AML/CTF programs for the period 2016-2022

## Crypto Regulation

Since **April 2018**, all Digital Currency Exchanges (DCEs) operating in Australia — or providing services to Australians — must register with AUSTRAC. See [[vasp-regulation]] for the full DCE registration framework.

### What DCE Registration Requires
- Register with AUSTRAC as a digital currency exchange business
- Implement a full AML/CTF compliance program: KYC procedures, transaction monitoring, suspicious activity reporting
- Verify customer identity before allowing trading
- Report suspicious transactions (SMRs) and threshold transactions (TTRs)
- Comply with the Travel Rule for crypto transfers above $1,000 AUD

### What AUSTRAC Does NOT Do for Crypto
- Does not regulate the crypto assets themselves (that's [[asic]])
- Does not provide investor protection or compensation schemes
- Does not set rules about which tokens can be listed
- Does not regulate [[defi]] protocols (no central entity to register)

### Travel Rule
AUSTRAC is implementing the **FATF Travel Rule** (FATF Recommendation 16 applied to virtual assets), which requires crypto exchanges to share sender and receiver information for transfers exceeding **AUD $1,000**. This applies to transfers between exchanges (and between exchanges and unhosted wallets where the exchange is a party). The Travel Rule is a significant compliance burden for exchanges and may affect withdrawal processes for traders.

**What the Travel Rule means in practice (indicative):**

| Transfer type | Travel Rule implication |
|---------------|-------------------------|
| Exchange A -> Exchange B (both registered) | Originator/beneficiary data must accompany the transfer; both VASPs verify and retain it |
| Exchange -> self-hosted ("unhosted") wallet | The exchange may collect beneficiary details and apply enhanced checks; some platforms restrict or whitelist withdrawal addresses |
| Self-hosted wallet -> self-hosted wallet | Peer-to-peer transfers fall outside the rule (no [[vasp-regulation|VASP]] is a party) -- but the on/off-ramp back to an exchange is captured |
| Below the AUD $1,000 threshold | Reduced data requirements, though aggregation/structuring is still monitored |

This is the same conceptual mechanism long applied to wire transfers (the IFTI regime, see Reporting Obligations) now extended to virtual assets. The **sunrise problem** -- jurisdictions implementing the Travel Rule on different timelines, so a sending VASP may have no compliant counterparty to send data to -- is an ongoing operational friction across the global crypto industry, not unique to Australia.

### The 2024-2026 AML/CTF Reform ("Tranche 2")
Australia legislated a major expansion of the AML/CTF regime (commonly called **"Tranche 2"**) to bring previously excluded "gatekeeper" professions -- such as lawyers, accountants, real estate agents, and dealers in precious metals/stones -- under AUSTRAC's reporting net, with a phased commencement extending into 2026. The reform also modernises the digital-currency provisions. For traders, the practical signal is that AUSTRAC's perimeter is **widening, not narrowing**, and that crypto and high-value-asset flows face progressively more reporting, not less. (Status of specific commencement dates evolves; confirm current obligations with AUSTRAC directly.)

## AUSTRAC vs Other Financial Intelligence Units

| Feature | AUSTRAC (Australia) | FinCEN (US) | NCA (UK) | FINTRAC (Canada) |
|---------|-------------------|-------------|----------|-------------------|
| **Cash reporting threshold** | AUD $10,000 | USD $10,000 | No fixed threshold (SARs) | CAD $10,000 |
| **Crypto exchanges** | Registered since 2018 | Registered as MSBs | FCA registration | Registered as MSBs |
| **Travel Rule threshold** | AUD $1,000 (crypto) | USD $3,000 | Implementing | CAD $1,000 |
| **Largest penalty** | $1.3B (Westpac) | $2B+ (HSBC) | Various | Various |
| **Regulatory model** | FIU + regulator (combined) | FIU + regulator (combined) | FIU (NCA), regulator (FCA) | FIU + regulator (combined) |

## Structure and Leadership

- **CEO**: Appointed by the Attorney-General
- **Reports to**: Attorney-General's Department (not Treasury — reflecting its law enforcement orientation)
- **Staff**: ~400
- **Budget**: ~AUD $100 million
- **Offices**: Canberra (headquarters), Sydney, Melbourne
- **International cooperation**: Member of the Egmont Group of Financial Intelligence Units (164 member countries)

## Impact on Traders and Investors

> **Not financial, legal, or tax advice.** This section is general, indicative information about how AUSTRAC's regime tends to affect market participants. AML/CTF obligations and thresholds change; verify current requirements with AUSTRAC, [[asic|ASIC]], or a licensed adviser before acting.

For Australian traders and investors, AUSTRAC's regulation means:

1. **KYC is mandatory**: You must verify your identity with any regulated exchange or broker before trading
2. **Large cash transactions are reported**: Depositing or withdrawing $10,000+ in cash triggers automatic reporting
3. **Suspicious activity is monitored**: Unusual trading patterns (rapid in/out, structuring, trading inconsistent with your profile) may trigger an SMR
4. **Crypto exchanges must be registered**: Only trade on [[vasp-regulation|AUSTRAC-registered exchanges]] — unregistered platforms have no AML/CTF obligations and offer no regulatory protections
5. **Cross-border transfers are tracked**: All international money transfers (including crypto under the Travel Rule) are reported to AUSTRAC
6. **Data sharing with ATO**: AUSTRAC shares data with the ATO, which uses it for tax compliance — this is one reason the ATO's crypto data matching program is so effective (see [[cryptocurrency-tax-australia]])

### What a Trader Actually Experiences

| Activity | Likely AUSTRAC-driven friction | Underlying obligation |
|----------|-------------------------------|------------------------|
| Opening an exchange/broker account | Identity verification before first trade | Customer Due Diligence (KYC) |
| Depositing/withdrawing AUD $10,000+ in cash | Automatic threshold report filed | Threshold Transaction Report (TTR) |
| Sending crypto >AUD $1,000 to another exchange | Counterparty info collected/shared; possible delay | Travel Rule / IFTI |
| Cross-border bank or crypto transfer (any size) | Reported to AUSTRAC | International Funds Transfer Instruction (IFTI) |
| Rapid in/out, structuring near thresholds, atypical patterns | Possible account review or freeze; no notice given | Suspicious Matter Report (SMR); tipping-off prohibition |
| Trading on an unregistered offshore platform | No AML/CTF protections; ATO data-matching gaps; counterparty risk | Outside the registered-[[vasp-regulation|VASP]] perimeter |

The practical takeaways for a compliant trader: keep identity documents current, expect large or cross-border movements to be reported automatically (this is routine, not an accusation), avoid transaction patterns that resemble **structuring** (deliberately breaking amounts to stay under thresholds -- itself an offence), and prefer **AUSTRAC-registered** exchanges. See [[aml-ctf]] for the underlying framework and [[australian-crypto-regulation]] for the broader Australian picture.

## Related

- [[asic]]
- [[apra]]
- [[aml-ctf]]
- [[vasp-regulation]]
- [[australian-investing]]
- [[binance]]
- [[coinbase]]
- [[cryptocurrency-tax-australia]]
- [[sec]]
- [[regulation]]
- [[australian-regulatory-framework]]
- [[australian-crypto-regulation]]

## Sources

- AUSTRAC — Annual reports and compliance guides
- Australian Government — Anti-Money Laundering and Counter-Terrorism Financing Act 2006
- AUSTRAC — Digital currency exchange register
- Federal Court of Australia — Commonwealth of Australia v Commonwealth Bank of Australia (2018)
- Federal Court of Australia — AUSTRAC v Westpac Banking Corporation (2020)
