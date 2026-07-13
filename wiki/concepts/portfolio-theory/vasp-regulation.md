---
title: "VASP Regulation & DCE Registration (Australia)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [regulation, australia, crypto, compliance, defi]
aliases: ["VASP", "Virtual Asset Service Provider", "DCE Registration", "Digital Currency Exchange Registration"]
related: ["[[austrac]]", "[[asic]]", "[[aml-ctf]]", "[[binance]]", "[[coinbase]]", "[[defi]]", "[[regulation]]", "[[cryptocurrency-tax-australia]]", "[[changpeng-zhao]]", "[[australian-crypto-regulation]]", "[[afsl]]", "[[australian-regulatory-framework]]"]
domain: [regulation]
difficulty: intermediate
---

A Virtual Asset Service Provider (VASP) is the [FATF](https://www.fatf-gafi.org)'s global term for any business that provides cryptocurrency exchange, transfer, custody, or related services. In Australia, the equivalent legal concept is the **Digital Currency Exchange (DCE)** — a regulated designation under the [[aml-ctf|AML/CTF Act 2006]]. Since **April 2018**, all DCEs operating in Australia or providing services to Australian customers must register with [[austrac|AUSTRAC]] and implement full AML/CTF compliance programs. This registration requirement was the first major step in bringing Australia's crypto industry under formal regulatory oversight.

> **Not legal or financial advice.** This page is an encyclopedic summary for traders, not a compliance manual. All thresholds, fees, and dates are **indicative** and change frequently as legislation evolves (Australia's AML/CTF "Tranche 2" reforms and Treasury's crypto-asset framework are both in flux as of 2026). Verify current obligations against primary sources ([[austrac|AUSTRAC]], [[asic|ASIC]], the relevant statute) or a qualified adviser before acting.

## What "Virtual Asset" and "VASP" Mean (FATF Definitions)

The FATF — the inter-governmental financial-crime standard-setter — coined the global vocabulary that national regimes (including Australia's DCE rules) implement:

| Term | FATF definition (paraphrased) | Practical scope |
|------|-------------------------------|-----------------|
| **Virtual Asset (VA)** | A digital representation of value that can be traded or transferred and used for payment/investment | Most cryptocurrencies, stablecoins, many tokens; **excludes** fiat, CBDCs, and (often) closed-loop in-game points |
| **VASP** | A business conducting VA exchange, transfer, safekeeping/administration, or issuance/participation in financial services for VA offerings | Exchanges, brokers, custodians, some issuers |
| **Obliged entity** | Any business caught by AML/CTF law for the above | Must run KYC/CDD, monitoring, reporting |

The five FATF-listed VASP activities: (1) VA↔fiat exchange; (2) VA↔VA exchange; (3) VA transfer; (4) custody/administration of VA or instruments enabling control; (5) participation in/provision of financial services related to a VA issuance/sale. A business doing **any one** of these as a business is in scope.

## Overview

Australia's approach to crypto exchange regulation is registration-based rather than licence-based. DCE registration with AUSTRAC is a **lower bar** than obtaining an Australian Financial Services Licence ([[afsl|AFSL]]) from [[asic|ASIC]], but still imposes significant obligations around customer identification, transaction monitoring, and suspicious activity reporting. The distinction matters: AUSTRAC registration focuses on preventing financial crime, while AFSL regulation (which may be extended to crypto in the future) focuses on consumer protection, disclosure, and product suitability.

The practical effect for Australian traders is straightforward: only trade on AUSTRAC-registered exchanges. Unregistered platforms operating illegally in Australia carry heightened risk — no AML/CTF protections, no regulatory recourse, and potential legal exposure for the user.

## Who Must Register

Under the AML/CTF Act, a **Digital Currency Exchange (DCE)** is any business that exchanges:
- Digital currency for **fiat currency** (AUD or foreign currency)
- Fiat currency for **digital currency**
- One digital currency for **another digital currency**

This definition captures a broad range of business models:

| Business Type | Must Register? | Notes |
|---------------|---------------|-------|
| **Centralised exchanges** (Binance, CoinSpot) | Yes | Primary target of registration |
| **OTC desks** (over-the-counter crypto brokers) | Yes | Provide exchange services |
| **Crypto ATM operators** | Yes | Exchange cash for crypto |
| **Crypto brokers** (aggregators, white-label) | Yes | Facilitate exchange on behalf of customers |
| **Peer-to-peer platforms** (facilitating P2P trades) | Likely yes | If the platform facilitates the exchange |
| **Individual P2P traders** | Possibly | If conducted as a business (regular, systematic) |
| **[[defi]] protocols** (Uniswap, Aave) | Currently no | No central entity to register — regulatory gap |
| **NFT marketplaces** | Currently not explicitly | AUSTRAC has flagged potential future inclusion |
| **Wallet providers** (non-custodial) | No | Do not facilitate exchange |
| **Blockchain analytics firms** | No | Do not facilitate exchange |

## Registration Requirements

### Application Process
1. Submit an application to AUSTRAC with:
   - Business details (entity name, ABN/ACN, contact information)
   - Key personnel details (directors, beneficial owners, compliance officers)
   - Description of the exchange services to be provided
   - Overview of proposed AML/CTF compliance arrangements
2. AUSTRAC assesses the application — primarily checking that the applicant has the capacity to comply
3. If approved, the business is added to the AUSTRAC DCE register (publicly searchable)
4. Registration is ongoing — there is no expiry date, but AUSTRAC can cancel registration for non-compliance

### Ongoing Obligations
Once registered, DCEs must:
- Implement and maintain a full **AML/CTF program** (see [[aml-ctf]])
- Conduct **KYC/CDD** on all customers before allowing trading
- Monitor transactions for suspicious activity and file **SMRs** as required
- File **TTRs** for cash transactions of AUD $10,000 or more
- Comply with the **Travel Rule** for crypto transfers exceeding AUD $1,000
- Retain all records for **7 years**
- Appoint an **AML/CTF compliance officer**
- Provide staff training on AML/CTF obligations
- Submit to AUSTRAC examinations and audits

### Registration vs Licence

| Feature | AUSTRAC DCE Registration | [[afsl|ASIC AFSL]] |
|---------|------------------------|---------------------|
| **Issued by** | AUSTRAC | ASIC |
| **Focus** | AML/CTF compliance | Consumer protection, product regulation |
| **Application fee** | Free | ~$2,000-4,000 |
| **Ongoing cost** | Compliance costs ($50K-$200K+/year) | Compliance costs ($50K-$200K+/year) + ASIC levies |
| **Capital requirements** | No explicit minimum | Yes — varies by licence type |
| **Client money rules** | Basic (AML/CTF Act) | Strict segregation (Corporations Act) |
| **Investor protection** | None (not AUSTRAC's mandate) | AFCA access, DDO, compensation arrangements |
| **Product disclosure** | Not required | PDS, TMD, FSG required |
| **Bar to entry** | Lower | Higher |

## The FATF Travel Rule (Mechanics)

The single most operationally demanding VASP obligation worldwide is the **Travel Rule** — FATF Recommendation 16, extended to virtual assets in 2019. It requires that for VA transfers above a threshold, the **originating VASP** collect and transmit identifying information to the **beneficiary VASP**, mirroring the wire-transfer "travel" of payer/payee data in TradFi.

### What information must travel

| Party | Required data (typical) |
|-------|-------------------------|
| **Originator (sender)** | Name; account/wallet identifier used; address, national ID number, customer ID, or date+place of birth |
| **Beneficiary (recipient)** | Name; account/wallet identifier used |

The originating VASP must **transmit immediately and securely**, screen against sanctions lists, and keep the data; the beneficiary VASP must receive it and run its own checks.

### Thresholds (indicative — verify locally)

| Jurisdiction | Travel Rule threshold (indicative) |
|--------------|-------------------------------------|
| FATF recommendation | USD/EUR **1,000** |
| Australia | AUD **1,000** |
| United States (FinCEN) | USD **3,000** (a 2020 proposal to lower to $250 for cross-border was not finalised) |
| European Union (TFR / MiCA-adjacent) | **No de minimis** — applies to all CASP-to-CASP transfers |

Below threshold, reduced data (names + wallet identifiers) is typically still required, with full verification on suspicion.

### The core problems the Travel Rule creates

- **No native messaging layer.** Blockchains move value, not KYC data. VASPs must bolt on a separate secure channel. Competing protocols/standards emerged — IVMS101 (the agreed data format), plus solutions like TRP, OpenVASP, Sygna, Notabene, TRISA — and **interoperability between them is imperfect**.
- **The "sunrise problem."** Because jurisdictions adopted the rule at different times, a compliant VASP often transacts with a counterparty VASP in a jurisdiction with no rule yet — there is no one to send the data to.
- **The counterparty / VASP-discovery problem.** A receiving address is just a string; the sender often **cannot tell** whether it belongs to another VASP, a different customer, or a self-hosted (unhosted) wallet.
- **Unhosted (self-custody) wallets.** Transfers to/from private wallets have no beneficiary VASP to receive the data. Regimes diverge: some require the VASP to collect counterparty info and/or verify wallet ownership (e.g. "Satoshi test" / signature proof); the EU's TFR imposes additional checks above EUR 1,000 to self-hosted wallets.

The Travel Rule is the clearest example of why VASP compliance is **operationally** harder than its TradFi analogue, even though the legal concept is borrowed directly from wire-transfer rules.

## Major Registered DCEs in Australia

As of 2026, the major AUSTRAC-registered digital currency exchanges operating in Australia include:

| Exchange | AUSTRAC Status | Notes |
|----------|---------------|-------|
| **[[binance]] Australia** | Registered | Faced banking access issues in 2023; lost multiple banking partnerships; restricted AUD deposit/withdrawal options |
| **[[coinbase]] Australia** | Registered | Expanded Australian operations; acquired Swyftx user base |
| **CoinSpot** | Registered | One of Australia's oldest and largest domestic exchanges; founded 2013 |
| **Independent Reserve** | Registered | Australian-founded; strong institutional focus; SMSF-friendly |
| **BTC Markets** | Registered | Longest-running Australian crypto exchange; founded 2013 |
| **CoinJar** | Registered | Australian-founded; now dual-headquartered in Melbourne and London |
| **Digital Surge** | Registered | Brisbane-based; briefly entered administration in 2022 (FTX exposure) but restructured |
| **Swyftx** | Registered | Australian-founded; merged with stake in 2023 (Swyftx brand retained for crypto) |

## Binance Australia: A Case Study

[[binance]] Australia illustrates the challenges of crypto exchange regulation in Australia:

- **Registered with AUSTRAC** as a DCE
- In **June 2023**, Binance Australia's third-party payment provider (Cuscal, via Zepto) terminated services, cutting off AUD bank transfers
- Multiple Australian banks progressively restricted or blocked payments to Binance
- [[changpeng-zhao]] (CZ) pleaded guilty in the US in November 2023 to AML violations, resulting in Binance paying $4.3 billion in penalties globally
- Binance Australia continued operating with reduced AUD payment options (credit/debit card, PayID through alternative providers)
- The episode highlighted that **AUSTRAC registration alone does not guarantee banking access** — banks make independent risk assessments about which crypto platforms they will service

## The DeFi Regulatory Gap

Decentralised finance ([[defi]]) protocols present a fundamental challenge to the DCE registration framework:

- DeFi protocols like Uniswap, Aave, and Curve operate as autonomous smart contracts on blockchains — there is **no central entity** to register with AUSTRAC
- No individual or company controls the protocol once deployed (in theory)
- Users interact directly with the smart contract — no intermediary performs KYC or monitors transactions
- AUSTRAC has acknowledged this gap but has not yet published a framework for regulating DeFi
- The global regulatory community (via FATF) is grappling with the same issue — some jurisdictions are considering regulating DeFi front-ends (the websites that provide user interfaces to protocols) even if the underlying smart contracts remain unregulated
- Australian traders using DeFi protocols operate in a **regulatory grey zone** — the activity is not prohibited, but there are no consumer protections, no AFCA access, and no recourse if funds are lost

## NFT and Emerging Asset Regulation

- NFT platforms are not currently explicitly required to register as DCEs
- However, AUSTRAC has indicated that NFT marketplaces **may** fall under DCE registration requirements if they facilitate the exchange of digital currency (e.g., crypto-to-NFT trades could be characterised as digital currency exchange)
- The ATO already treats NFTs as CGT assets (see [[cryptocurrency-tax-australia]])
- If NFT marketplaces are brought under AUSTRAC regulation, expect KYC requirements and transaction reporting to be imposed

## International Comparison

| Jurisdiction | Regulatory Approach | Authority | Key Features |
|-------------|-------------------|-----------|--------------|
| **Australia** | DCE registration (AML/CTF) | [[austrac]] | AML/CTF-focused; no product regulation; relatively low bar |
| **United States** | MSB registration + state licences | FinCEN + state regulators | Patchwork: federal MSB registration + 50 state money transmitter licences + potential SEC/[[cftc]] oversight |
| **European Union** | MiCA (Markets in Crypto-Assets) | National competent authorities | Comprehensive: licensing, conduct rules, stablecoin regulation, market abuse rules. Effective 2024-2025 |
| **United Kingdom** | FCA registration | FCA | AML/CTF registration + marketing restrictions; evolving toward comprehensive framework |
| **Singapore** | MAS Payment Services Act licence | MAS | Licence-based; covers DPT (digital payment token) services; stringent requirements |
| **Japan** | FSA registration | JFSA | Strict: mandatory cold storage, client money segregation, regular audits |
| **Hong Kong** | SFC licensing | SFC | Licence required for VA trading platforms; mandatory insurance |

Australia's current framework is comparatively **light-touch** — focusing primarily on AML/CTF rather than comprehensive product regulation. The proposed Treasury reforms (Token Mapping and potential AFSL extension) would move Australia closer to the EU's MiCA model.

## Proposed Reforms: Token Mapping and Beyond

The Australian Treasury has been consulting on reforms to bring crypto assets under a more comprehensive regulatory framework:

### Token Mapping (2023 Consultation)
- Proposed classifying crypto tokens into categories:
  - **Payment tokens**: Tokens used primarily as a medium of exchange (e.g., [[bitcoin]], [[stablecoins]])
  - **Utility tokens**: Tokens providing access to a product or service
  - **Asset tokens**: Tokens representing rights similar to financial products (e.g., security tokens)
  - **Stablecoins**: Tokens pegged to fiat currency or other assets
- Different categories would receive different regulatory treatment
- Payment tokens and stablecoins would likely receive the most immediate regulatory attention

### Potential AFSL Extension
- Treasury has indicated that some crypto products (particularly those resembling financial products) may eventually require an [[afsl|AFSL]] or a new equivalent licence
- This would bring crypto under [[asic]] regulation **in addition to** AUSTRAC registration
- Would impose consumer protection obligations: PDSs, target market determinations, dispute resolution, compensation arrangements
- Timeline uncertain — multiple rounds of consultation still ongoing as of 2026

## Impact on Traders

For Australian crypto traders and investors, the DCE registration framework means:

1. **Only trade on registered exchanges**: Check the AUSTRAC DCE register before depositing funds
2. **KYC is mandatory**: No anonymous trading on registered Australian exchanges
3. **Expect banking friction**: Some banks restrict crypto-related transfers — have backup payment methods
4. **Large transactions may be delayed**: Withdrawals above certain thresholds may trigger additional verification
5. **DeFi = no protection**: If you use DeFi protocols, understand that you are outside the regulated framework
6. **Data flows to ATO**: Registered exchanges provide transaction data to the ATO for tax compliance
7. **Unregistered platforms = legal risk**: Using an unregistered exchange may expose you to legal risk (though enforcement has focused on the exchanges, not users)

## Common Pitfalls

For both operators considering VASP/DCE status and traders relying on regulated venues, the recurring mistakes are:

| Pitfall | Why it bites | Mitigation |
|---------|--------------|------------|
| **Assuming registration = solvency/safety** | Registration covers AML/CTF, *not* prudential soundness, reserves, or custody quality. FTX entities were nominally compliant in several places | Treat registration as a floor, not a guarantee; assess custody and reserves separately |
| **"Registration ≠ banking access"** | A registered DCE can still lose fiat rails (see the [[binance\|Binance]] Australia case) | Keep backup on/off-ramps and venues |
| **Geographic / "offshore" arbitrage** | Serving a country's customers usually triggers that country's rules **regardless of where the entity sits**; "we're offshore" is not a defence | Geo-fence properly; obtain local registration where customers are |
| **Travel Rule "sunrise" gaps** | Sending to a non-compliant-jurisdiction VASP can leave data un-receivable, creating audit exposure | Use counterparty-VASP discovery tooling; document good-faith effort |
| **Misclassifying self-hosted-wallet transfers** | Withdrawals to private wallets carry extra obligations in some regimes (EU TFR) | Apply correct unhosted-wallet procedures per jurisdiction |
| **Token-by-token classification error** | Whether an asset is a "virtual asset," a "financial product," or both changes the regulator (AUSTRAC vs [[asic\|ASIC]] vs SEC/[[cftc\|CFTC]]) | Map each token; expect dual regulation under reform |
| **Treating DeFi as exempt forever** | The DeFi gap is a *current* gap, not a permanent carve-out; front-end and developer liability is being explored globally | Don't build a business model that only works if DeFi stays unregulated |
| **Ignoring record-retention** | Many regimes require multi-year (e.g. 7-year) retention; gaps surface in audits years later | Retain KYC, transaction, and Travel Rule records from day one |
| **Sanctions screening as an afterthought** | Sanctions obligations are separate from and stricter than AML and apply even below thresholds | Screen addresses and parties continuously |

## Related

- [[austrac]]
- [[asic]]
- [[aml-ctf]]
- [[binance]]
- [[coinbase]]
- [[defi]]
- [[regulation]]
- [[cryptocurrency-tax-australia]]
- [[changpeng-zhao]]
- [[australian-crypto-regulation]]
- [[afsl]]
- [[australian-regulatory-framework]]
- [[cftc]]
- [[bitcoin]]
- [[stablecoins]]

## Sources

- AUSTRAC — Digital currency exchange register
- Australian Government — Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (as amended 2017)
- Australian Treasury — Token Mapping consultation paper (2023)
- FATF — Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs (2021)
- FATF Recommendation 16 ("Travel Rule") and the Interpretive Note extending it to virtual asset transfers (2019)
- IVMS101 data standard (interVASP Messaging Standards) for Travel Rule payloads
- EU Transfer of Funds Regulation (TFR) and MiCA framework (general reference)
- General market knowledge; thresholds and dates are indicative and not legal advice.
