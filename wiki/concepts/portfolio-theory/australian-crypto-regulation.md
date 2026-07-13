---
title: "Australian Crypto Regulation"
type: concept
created: 2026-04-07
updated: 2026-06-20
status: excellent
tags: [regulation, australia, crypto, defi, compliance]
aliases: ["Australian Crypto Regulation", "Crypto Law Australia"]
related: ["[[vasp-regulation]]", "[[austrac]]", "[[asic]]", "[[aml-ctf]]", "[[cryptocurrency-tax-australia]]", "[[binance]]", "[[defi]]", "[[stablecoins]]", "[[staking]]", "[[nft]]", "[[bitcoin]]", "[[ethereum]]", "[[coinbase]]", "[[changpeng-zhao]]", "[[regulation]]", "[[afsl]]", "[[australian-regulatory-framework]]"]
domain: [regulation]
difficulty: intermediate
---

Australia does not have a single, comprehensive crypto-specific law. Instead, cryptocurrency regulation is distributed across multiple existing frameworks — [[austrac|AUSTRAC]] for AML/CTF and exchange registration, [[asic|ASIC]] for financial products, the ATO for tax, [[apra|APRA]] for banking exposure, and the RBA for payments and stablecoin policy. This patchwork approach means crypto is legal and widely used in Australia, but the regulatory landscape is fragmented and evolving. Treasury consultations on Token Mapping and potential licensing reform signal a move toward a more comprehensive framework, but as of 2026, the multi-regulator model remains the reality.

> **Not legal or financial advice.** This page is general educational information about Australia's crypto regulatory landscape. The framework is actively changing — Treasury reforms, ASIC enforcement, AUSTRAC rules, and banking policies can shift quickly, and reporting/transaction thresholds quoted here are **indicative**. Confirm current obligations with the relevant regulator ([AUSTRAC](https://www.austrac.gov.au), [ASIC](https://asic.gov.au), [RBA](https://www.rba.gov.au), [ATO](https://www.ato.gov.au)) and qualified legal/financial advice before acting. For tax specifics see [[cryptocurrency-tax-australia]].

## At a Glance

| Question | Short answer |
|----------|--------------|
| Is crypto legal in Australia? | Yes — buying, holding, and trading crypto is legal. |
| Is there one crypto law? | No — a multi-regulator patchwork ([[austrac]], [[asic]], ATO, [[apra]], RBA, Treasury). |
| Do exchanges need approval? | Yes — AUSTRAC **registration** as a Digital Currency Exchange (a lower bar than an [[afsl]]). |
| Are crypto products financial products? | Sometimes — yield, leverage, and pooled products often are, triggering [[asic]] / AFSL rules. |
| Is DeFi regulated? | Largely not — a recognised gap with no investor protections. |
| Are stablecoins regulated? | Proposed (stored-value facility model) — not yet a settled regime. See [[stablecoin-regulation]]. |
| Biggest practical risk for traders? | Debanking (losing bank access) and dealing with unlicensed products. |

## Overview

Australia has approximately **4-5 million** crypto holders (roughly 20-25% of adults), making it one of the highest per-capita crypto adoption countries in the developed world. The regulatory approach has been pragmatic — bringing crypto exchanges under AML/CTF regulation early (2018) and applying existing financial services law to crypto products case-by-case, while consulting on broader reforms. The result is a framework that is functional but incomplete, with several significant grey areas — particularly around [[defi]], [[stablecoins]], and NFTs.

## Regulatory Map: Who Regulates What

| Regulator | What They Regulate | Key Framework |
|-----------|-------------------|---------------|
| **[[austrac|AUSTRAC]]** | Digital currency exchanges (DCEs) — AML/CTF, KYC, transaction reporting | AML/CTF Act 2006 (amended 2017) |
| **[[asic|ASIC]]** | Crypto products that qualify as financial products (managed investment schemes, derivatives, securities) | Corporations Act 2001 |
| **ATO** | Tax treatment of crypto (CGT asset, income, GST) | ITAA 1997 |
| **[[apra|APRA]]** | Banks' exposure to crypto assets; prudential treatment | Banking Act 1959, Basel framework |
| **RBA** | Payment systems, stablecoin regulation, CBDC research | Payment Systems (Regulation) Act 1998 |
| **Treasury** | Policy development, Token Mapping, proposed licensing reform | Various consultation papers |

### Practical Example: Regulatory Touchpoints for Buying Bitcoin

When an Australian buys [[bitcoin]] through a registered exchange:
1. **AUSTRAC**: Exchange must be registered, must have KYC'd the buyer, monitors for suspicious transactions
2. **ATO**: Purchase establishes cost base; any future disposal is a CGT event (see [[cryptocurrency-tax-australia]])
3. **APRA**: The bank used to transfer AUD is APRA-supervised and may impose restrictions on crypto-related transfers
4. **ASIC**: If the "purchase" is actually a structured product (e.g., a crypto ETF, a yield product, a tokenised security), ASIC's product regulation applies
5. **RBA**: The payment system used for the AUD transfer is ultimately overseen by the RBA

## AUSTRAC: Exchange Registration (Since 2018)

The centrepiece of Australia's current crypto regulation. See [[vasp-regulation]] for full details.

- All digital currency exchanges must register with AUSTRAC as DCEs
- Implement full AML/CTF programs: KYC, transaction monitoring, suspicious activity reporting
- Comply with the Travel Rule for crypto transfers above the prescribed threshold (indicatively around $1,000 AUD — confirm the current figure with AUSTRAC)
- Report threshold cash transactions (indicatively $10,000+) and suspicious matters
- This is a **registration** (not a licence) — the bar is lower than an [[afsl|AFSL]]
- Major registered exchanges: [[binance]] Australia, [[coinbase]] Australia, CoinSpot, Independent Reserve, BTC Markets, CoinJar, Digital Surge

## ASIC: Crypto as Financial Products

ASIC does not regulate cryptocurrency per se — it regulates **financial products**, and has taken the position that many crypto-related products fall within existing financial product definitions. ASIC's approach has been case-by-case enforcement rather than comprehensive rulemaking.

### Key ASIC Positions

**When crypto IS a financial product:**
- **Managed investment scheme (MIS)**: If a crypto product pools investor funds and a third party manages them for returns, it likely constitutes an MIS and requires an AFSL. This was the basis for ASIC's actions against crypto yield products
- **Derivative**: If a crypto product derives its value from an underlying crypto asset (e.g., crypto CFDs, crypto futures, crypto options), it is a derivative and requires an AFSL
- **Security**: If a crypto token confers rights similar to a share or debenture (e.g., profit-sharing, governance rights, debt obligations), it may be a security
- **Non-cash payment facility**: If a token functions as a payment mechanism

**When crypto is NOT a financial product (currently):**
- Buying and selling cryptocurrency itself (BTC, ETH) on an exchange — this is simply buying and selling a CGT asset, not a financial product
- Holding crypto in a personal wallet
- Using crypto for payments (subject to CGT implications)

### ASIC Enforcement Actions

| Year | Target | Issue | Outcome |
|------|--------|-------|---------|
| **2022** | **Finder Wallet (Finder Earn)** | ASIC alleged Finder's crypto yield product was a managed investment scheme offered without an AFSL | ASIC commenced proceedings; Finder discontinued the product |
| **2022** | **Block Earner (crypto yield)** | Similar to Finder — ASIC alleged Block Earner's "Crypto Earner" and "Gold Earner" products were financial products offered without an AFSL | Federal Court found in ASIC's favour in 2024 — products were MIS interests and derivatives |
| **2023** | **Bit Trade (Kraken Australia)** | ASIC alleged Bit Trade's margin extension product was a credit facility/derivative offered without proper AFSL authorisation and TMD | Proceedings ongoing; significant implications for crypto margin trading in Australia |
| **2023** | **Various finfluencers** | ASIC pursued social media personalities providing specific crypto investment recommendations without an AFSL | Fines and banning orders |
| **2022-ongoing** | **ICO/token sale warnings** | ASIC issued multiple warnings about unregistered token sales that may constitute securities offerings | Consumer alerts; some referrals to enforcement |

**The clear message**: If a crypto product looks like a financial product, ASIC will regulate it as one — regardless of the technology involved.

## ATO: Crypto Taxation

The ATO treats all cryptocurrency as a **CGT asset** (not as currency). See [[cryptocurrency-tax-australia]] for comprehensive coverage.

Key points:
- Every disposal (sell, swap, spend, gift) is a CGT event
- [[capital-gains-tax-discount|50% CGT discount]] applies for holdings >12 months
- [[staking]] rewards and yield farming rewards are ordinary income (taxed at marginal rate)
- No wash sale rule — tax-loss harvesting is highly effective (see [[tax-loss-harvesting-australia]])
- ATO actively data-matches with all AUSTRAC-registered exchanges — 350,000+ compliance letters sent
- Crypto is a priority compliance area for the ATO

## Banking Access (Debanking)

One of the most significant practical challenges for Australian crypto traders has been **debanking** — major banks restricting or blocking crypto-related transactions:

| Bank | Restriction |
|------|------------|
| **Commonwealth Bank (CBA)** | Blocked payments to certain crypto exchanges; trialled and then abandoned crypto features within the CommBank app |
| **Westpac** | Imposed a monthly cap (reported as around **$10,000**, indicative) on transfers to crypto exchanges; blocks payments to some platforms |
| **NAB** | Various restrictions on crypto exchange transfers; enhanced monitoring |
| **ANZ** | Intermittent restrictions; enhanced monitoring of crypto-related transactions |

### Why Banks Restrict Crypto
- AML/CTF compliance risk — banks are concerned about being held responsible if customer funds are linked to money laundering through crypto
- Scam prevention — banks report significant fraud losses related to crypto investment scams
- Regulatory risk — APRA expects banks to manage their exposure to crypto-related risks
- Reputational risk — association with volatile and sometimes fraudulent crypto activities

### Workarounds Used by Traders
- Use smaller banks or neobanks (some have fewer restrictions)
- Use PayID or OSKO for instant transfers (sometimes not blocked when traditional bank transfers are)
- Use credit/debit cards (higher fees but often not blocked)
- Use P2P trading platforms (though these carry their own risks)
- Maintain accounts at multiple banks

### Debanking Reform
The Australian government has acknowledged debanking as a systemic issue (affecting not just crypto, but also money remitters, charities operating in certain regions, and other lawful businesses). Treasury has consulted on reforms that would:
- Require banks to provide reasons for debanking decisions
- Establish a dispute resolution mechanism for debanking
- Potentially require banks to continue providing basic banking services to lawful businesses

## Stablecoin Regulation

[[stablecoins|Stablecoins]] are receiving specific regulatory attention in Australia:

- **RBA consultation**: The RBA and Treasury have consulted on regulating stablecoins as **stored-value facilities** under the Payment Systems (Regulation) Act
- **Proposed framework**: Stablecoin issuers may need to hold a licence, maintain 1:1 reserves in high-quality liquid assets, submit to regular audits, and meet capital requirements
- **Rationale**: Stablecoins that achieve significant adoption as payment instruments could pose systemic risk if the issuer fails — regulation aims to ensure the "stable" part is genuine
- **Impact on traders**: If stablecoin regulation is implemented, expect stricter compliance from stablecoin-related services but also greater confidence in the backing of regulated stablecoins
- USDT (Tether), USDC (Circle), and other major stablecoins used heavily by Australian crypto traders could be affected

## eAUD (Central Bank Digital Currency)

The RBA has been researching and piloting a potential Australian CBDC:

- **2023 Pilot**: RBA conducted a limited pilot of the eAUD with **16 use cases** tested across payments, settlement, and tokenisation
- **Participants**: Selected financial institutions, fintechs, and researchers
- **Architecture**: Token-based (not account-based); issued by the RBA; intermediated by banks and payment providers
- **No commitment to full rollout**: RBA has characterised the pilot as research — no decision to issue a CBDC has been made
- **Potential implications**: If implemented, an eAUD could compete with private stablecoins, provide a government-backed digital payment option, and potentially enable programmable money (automated compliance, conditional payments)
- **Privacy concerns**: A CBDC could enable unprecedented government visibility into transactions — the design of privacy features is a key policy question

## DeFi Regulatory Gap

[[defi|DeFi]] protocols operating on public blockchains present a fundamental challenge for Australia's regulatory framework:

- **No central entity**: DeFi protocols are smart contracts deployed on blockchains — there is no company, director, or compliance officer to regulate
- **AUSTRAC**: Cannot require registration of a smart contract — no entity to register
- **ASIC**: Has flagged that DeFi arrangements may constitute financial products (e.g., a DeFi lending protocol could be a managed investment scheme) depending on the degree of centralisation and the rights conferred — but no formal enforcement against a DeFi protocol to date
- **Practical reality**: Australian users interact with DeFi freely — no regulator has attempted to prevent access
- **Risk**: DeFi users have no investor protections, no AFCA access, no compensation schemes, and no recourse if smart contracts are exploited or funds are lost
- **Global trend**: The FATF has recommended that countries find ways to regulate DeFi, but no jurisdiction has implemented a comprehensive DeFi regulatory framework

## NFT Regulation

[[nft|NFTs]] are not specifically regulated in Australia:

- The ATO treats NFTs as CGT assets (see [[cryptocurrency-tax-australia]])
- ASIC has indicated that some NFTs may qualify as financial products if they confer rights similar to securities or managed investment scheme interests (e.g., fractionalised NFTs representing investment interests)
- AUSTRAC has not formally required NFT marketplace registration, but has flagged potential future inclusion if NFT platforms facilitate digital currency exchange
- Most NFTs (art, collectibles, gaming items) are unlikely to be classified as financial products under current law — but "financial NFTs" (tokenised shares, profit-sharing tokens) almost certainly would be

## International Comparison

| Feature | Australia | US | UK | EU (MiCA) | Singapore |
|---------|-----------|----|----|-----------|-----------|
| **Comprehensive crypto law** | No (multi-regulator) | No (multi-regulator) | Developing | Yes (MiCA 2024-25) | Yes (PSA 2019) |
| **Exchange registration/licence** | AUSTRAC registration | FinCEN MSB + state MTL | FCA registration | MiCA CASP licence | MAS DPT licence |
| **Stablecoin regulation** | Proposed | Proposed | Proposed | Yes (MiCA Title III) | Yes (under PSA) |
| **DeFi regulation** | No | Evolving (SEC enforcement) | No | Limited | No |
| **NFT regulation** | No | Case-by-case SEC | No | Partial (MiCA Art. 4) | No specific |
| **Crypto tax clarity** | Good (ATO guidance) | Good (IRS guidance) | Developing | Varies by country | Good (IRAS) |
| **Banking access** | Restricted (debanking) | Restricted (Operation Chokepoint) | Mixed | Generally available | Generally available |
| **CBDC progress** | Pilot (eAUD) | Research (no pilot) | Research | ECB digital euro pilot | Retail CBDC pilot |

## Proposed Treasury Reforms

### Token Mapping (2023 Consultation)
Treasury proposed categorising crypto tokens to determine appropriate regulatory treatment:
- **Payment tokens** (e.g., [[bitcoin]], [[stablecoins]]): Focus on payment regulation, stablecoin backing requirements
- **Utility tokens** (e.g., access tokens): Lighter regulation if genuinely functional
- **Asset tokens** (e.g., tokenised securities): Full financial product regulation
- **Mixed tokens**: Classification based on primary function

### Potential New Licensing Framework
- Some crypto products may eventually require an [[afsl]] or a new purpose-built licence
- Would bring crypto under ASIC regulation alongside AUSTRAC registration
- Would impose consumer protections: PDSs, TMDs, compensation arrangements, AFCA membership
- **Timeline**: Multiple rounds of consultation ongoing; no legislation introduced as of early 2026

### Custody Regulation
- Treasury has also consulted on regulating crypto custody services
- Custodians holding crypto on behalf of others may need to meet capital requirements, segregation rules, and insurance obligations
- This would address the risk highlighted by collapses like FTX (where customer assets were not properly segregated)

## Investor Due-Diligence Checklist

Before putting money on a crypto platform or into a crypto product in Australia:

- [ ] **Check the AUSTRAC DCE register** — confirm the exchange is a registered Digital Currency Exchange.
- [ ] **Identify the legal entity and jurisdiction** — who actually holds your funds, and where are they incorporated?
- [ ] **Ask whether the product is a financial product** — yield, leverage, lending, or pooled returns usually require an [[afsl]]; check ASIC's register for the licence.
- [ ] **Look for a PDS / TMD** — regulated financial products carry a Product Disclosure Statement and Target Market Determination; their absence on a "yield" product is a red flag.
- [ ] **Confirm custody arrangements** — are assets segregated, and is there independent proof of reserves? (FTX-style commingling is the key risk.)
- [ ] **Plan for debanking** — maintain accounts at more than one bank and have alternative payment rails (PayID/OSKO, card) ready.
- [ ] **Recognise DeFi has no safety net** — no [[afsl]], no AFCA, no compensation scheme; you bear smart-contract and counterparty risk in full.
- [ ] **Keep tax records from day one** — ATO data-matches with registered exchanges (see [[cryptocurrency-tax-australia]]).

### Red Flags of an Unregulated / High-Risk Offering

| Red flag | Why it matters |
|----------|----------------|
| "Guaranteed" or fixed high yields | Likely an unlicensed managed investment scheme (cf. Finder, Block Earner) |
| No AUSTRAC registration | Platform operating outside Australia's AML/CTF perimeter |
| No PDS/TMD for an investment product | Suggests the provider is avoiding financial-product obligations |
| Leverage/margin without an AFSL | Possible unlicensed derivative/credit facility (cf. Bit Trade/Kraken) |
| Finfluencer "advice" with affiliate links | Personal advice without a licence — an ASIC enforcement target |
| Pressure to move fast / offshore-only support | Classic scam pattern; harder recourse |

## Regulatory Reform Trajectory

Australia's direction of travel is from a *patchwork* toward a *purpose-built* regime, though timelines remain uncertain:

| Stage | Status (indicative, as of 2026) |
|-------|---------------------------------|
| AML/CTF exchange registration | **In force** since 2018 ([[austrac]]) |
| Case-by-case financial-product enforcement | **Ongoing** ([[asic]]) |
| Token Mapping consultation | **Consulted** (2023) — categorisation framework |
| Crypto custody regulation | **Consulted** — segregation/capital/insurance proposals |
| Licensing framework for exchanges/products | **Proposed** — no legislation enacted yet |
| Stablecoin (stored-value facility) rules | **Proposed** — see [[stablecoin-regulation]] |
| Debanking reform | **Acknowledged** — reasons/dispute-resolution proposals |
| eAUD CBDC | **Pilot completed** — no rollout decision |

## Impact on Traders and Investors

1. **Use registered exchanges only**: Check the AUSTRAC DCE register — unregistered platforms offer no regulatory protection
2. **Watch for financial product classification**: If a crypto product offers yields, leverage, or investment returns, it may need an AFSL — if the provider doesn't have one, you may be dealing with an unregulated product
3. **Prepare for banking restrictions**: Have multiple payment methods available for moving AUD to/from crypto exchanges
4. **Maintain records**: ATO data matching means your crypto activity is visible — keep comprehensive transaction records (see [[cryptocurrency-tax-australia]])
5. **DeFi = unprotected**: Using DeFi protocols means accepting full responsibility — no regulatory safety net
6. **Stay current**: Australian crypto regulation is actively evolving — Treasury reforms, ASIC enforcement actions, and banking access rules can change the landscape rapidly
7. **Consider SMSF implications**: If holding crypto in an [[smsf]], ensure the investment strategy permits it and use a compliant exchange with SMSF account support

## Related

- [[vasp-regulation]]
- [[austrac]]
- [[asic]]
- [[aml-ctf]]
- [[cryptocurrency-tax-australia]]
- [[binance]]
- [[defi]]
- [[stablecoins]]
- [[stablecoin-regulation]]
- [[staking]]
- [[nft]]
- [[bitcoin]]
- [[ethereum]]
- [[coinbase]]
- [[changpeng-zhao]]
- [[regulation]]
- [[afsl]]
- [[australian-regulatory-framework]]
- [[apra]]
- [[cbdc]]

## Sources

- AUSTRAC — Digital currency exchange provider registration
- ASIC — Information Sheet 225: Crypto-assets
- ATO — Tax treatment of crypto assets
- Australian Treasury — Token Mapping consultation paper (2023)
- RBA — Central Bank Digital Currency Research
- RBA — Australian CBDC Pilot Project Report (2023)
