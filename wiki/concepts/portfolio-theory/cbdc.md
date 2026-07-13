---
title: "Central Bank Digital Currency (CBDC)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, regulation, central-banking, monetary-policy]
aliases: ["CBDC", "Central Bank Digital Currency", "Central Bank Digital Currencies"]
related: ["[[stablecoins]]", "[[regulation]]", "[[stablecoin-regulation]]", "[[usdc]]", "[[usdt]]", "[[australian-crypto-regulation]]", "[[central-bank]]", "[[monetary-policy]]", "[[ecb]]", "[[bitcoin]]", "[[defi]]", "[[fomc]]"]
domain: [regulation, monetary-policy]
difficulty: intermediate
---

A Central Bank Digital Currency (CBDC) is digital money issued directly by a nation's [[central-bank]], denominated in the national currency and serving as legal tender. Unlike [[stablecoins]] (which are private money backed by reserves), a CBDC is **government money** in digital form -- it carries the same sovereign backing as physical banknotes and coins. A CBDC is a *direct liability of the central bank* (like cash and bank reserves), whereas a commercial bank deposit is a liability of a private bank and a stablecoin is a liability of a private issuer. This single distinction — *whose liability is it?* — drives almost every difference in risk, privacy, and policy power discussed below, and connects CBDCs to the core of [[monetary-policy]] and the money-creation hierarchy.

## Overview

As of 2025-2026, over **130 countries** representing 98% of global GDP are exploring CBDCs, according to the Atlantic Council's CBDC tracker. Several have launched, many are piloting, and others remain in research phases. CBDCs represent the most significant potential change to monetary systems since the end of the gold standard.

The core question CBDCs answer is simple: should central banks issue money directly to citizens in digital form, or should digital money remain the domain of private sector intermediaries (banks, payment companies, stablecoin issuers)?

## Mechanics: How a CBDC Is Built

A CBDC is defined by a small set of architectural choices, each with large policy and market consequences. The design space is more important than the marketing.

| Design axis | Options | Trade-off |
|---|---|---|
| **Distribution model** | Direct (central bank holds every account) vs. Two-tier / intermediated (banks distribute, central bank issues) | Direct maximises control but disintermediates banks and overloads the central bank operationally; two-tier preserves the banking system and is the near-universal choice (China e-CNY, digital euro proposal) |
| **Ledger technology** | Centralised database vs. distributed ledger (DLT/blockchain) vs. hybrid | DLT enables programmability and atomic settlement but adds complexity; most retail designs use centralised or permissioned ledgers, not public blockchains |
| **Access record** | Account-based (tied to verified identity) vs. token-based (bearer-like, held in a wallet) | Account-based eases AML but kills cash-like anonymity; token-based can support offline, cash-like use |
| **Remuneration** | Non-interest-bearing vs. interest-bearing | An interest-bearing CBDC competes directly with bank deposits and amplifies disintermediation risk; most retail designs propose *no* interest plus holding caps |
| **Holding limits** | Capped (e.g. the proposed digital-euro EUR 3,000 cap) vs. uncapped | Caps are the primary tool to prevent a "digital bank run" out of deposits into central-bank money |
| **Offline capability** | Offline-capable vs. online-only | Offline support enables resilience and cash-like privacy for small payments but is hard to secure against double-spending |
| **Programmability** | None vs. limited (smart-contract conditions) | Programmability enables targeted stimulus and conditional payments — and is the core of the surveillance and autonomy concerns below |

The **disintermediation problem** is the central design tension: if households can hold unlimited, risk-free central-bank money digitally, they may pull deposits out of commercial banks, especially in a crisis (an accelerated bank run). This shrinks the deposit base banks lend against and complicates [[monetary-policy]] transmission. Holding caps, zero remuneration, and a two-tier model are the standard mitigations, and they explain why most serious retail-CBDC proposals look deliberately *unattractive as a store of value* — they are designed to be a means of payment, not a savings vehicle.

## Types of CBDCs

### Retail CBDC

Designed for the **general public** -- individuals and businesses use it for everyday transactions.

Two primary models:

| Model | Description | Examples |
|-------|-----------|---------|
| **Account-based** | Citizens hold accounts directly at the central bank or through intermediary banks | Nigeria eNaira, digital euro (proposed) |
| **Token-based** | Digital tokens held in wallets, transferable like digital cash | China e-CNY, Bahamas Sand Dollar |

Retail CBDCs are the most discussed and controversial type, as they fundamentally change the relationship between central banks and citizens.

### Wholesale CBDC

Designed for **interbank settlement** -- used only by banks and financial institutions to settle transactions between themselves.

- Less controversial than retail CBDCs (banks already hold digital reserves at the central bank)
- Focus on improving settlement speed, reducing costs, and enabling atomic settlement (delivery vs payment)
- Multiple wholesale CBDC projects: Project mBridge (BIS/China/UAE/Thailand), Project Helvetia (Switzerland), Project Jasper (Canada)
- May enable cross-border settlement without correspondent banking chains (currently slow and expensive)

## Motivations for CBDCs

Governments cite several motivations for developing CBDCs:

1. **Financial inclusion**: Reach unbanked populations (estimated 1.4 billion globally) who lack access to bank accounts but may have mobile phones
2. **Payment efficiency**: Reduce settlement times and costs, especially for cross-border transactions
3. **Reducing cash-handling costs**: Physical cash is expensive to produce, transport, secure, and process
4. **Competing with private stablecoins**: Maintain monetary sovereignty as private stablecoins like [[usdt|USDT]] and [[usdc|USDC]] gain adoption -- especially in emerging markets where stablecoins are replacing local currencies
5. **Monetary policy transmission**: CBDCs could enable more direct monetary policy tools -- applying interest rates directly to digital money, implementing targeted stimulus payments
6. **AML/CFT compliance**: Digital money is more traceable than cash, potentially improving [[aml-ctf|anti-money laundering]] enforcement
7. **Modernising payment infrastructure**: Many countries' payment systems run on decades-old technology

## Privacy and Surveillance Concerns

CBDCs are the most controversial aspect of digital money because they could enable **unprecedented government surveillance of financial transactions**:

### Surveillance Risks

- **Transaction monitoring**: Unlike cash (anonymous) or crypto (pseudonymous), CBDCs could give governments a complete, real-time record of every transaction by every citizen
- **Programmable money**: CBDCs could be programmed with restrictions:
  - **Spending restrictions**: Government could limit what money can be spent on (e.g., no gambling, no alcohol, only approved merchants)
  - **Expiry dates**: Money could expire if not spent within a timeframe (a form of forced stimulus)
  - **Negative interest rates**: Central banks could apply negative rates directly to CBDC holdings, effectively charging people for holding money -- impossible with physical cash
  - **Freezing**: Government could instantly freeze any individual's CBDC holdings without a court order or banking intermediary
- **Social credit integration**: In authoritarian regimes, CBDCs could be integrated with social credit or compliance systems -- spending rights linked to behaviour

### Privacy Frameworks

Aware of these concerns, many CBDC projects propose privacy-preserving designs:

- **Tiered privacy**: Small/offline transactions are anonymous (like cash), while larger/online transactions require identification. The digital euro proposal uses this model
- **Intermediary model**: The central bank sees aggregated data but not individual transactions -- intermediary banks handle customer relationships (China's e-CNY uses this "two-tier" model)
- **Zero-knowledge proofs**: Cryptographic techniques that can prove compliance (e.g., transaction is below threshold) without revealing transaction details. Still largely theoretical for CBDCs

### The Opposition Argument

The primary argument against CBDCs is that they represent a **fundamental shift in the power dynamic between citizens and the state**. Cash provides a degree of financial privacy and autonomy -- CBDCs could eliminate this entirely. This is not a theoretical concern: China's e-CNY already has programmable features, and several countries have explored spending restrictions.

In the United States, opposition has been bipartisan but particularly strong from libertarian-leaning lawmakers. The House passed an anti-CBDC bill in 2024, and the US is widely expected to **regulate stablecoins rather than launch a CBDC**.

Crypto advocates argue this is precisely why decentralised alternatives like [[bitcoin|Bitcoin]] and [[dai|DAI]] matter -- they provide financial autonomy that neither CBDCs nor regulated stablecoins can offer.

## Global CBDC Landscape

### Launched

| Country | CBDC | Launch Year | Status |
|---------|------|------------|--------|
| **Bahamas** | Sand Dollar | 2020 | First national CBDC. Limited adoption in a small economy (~400K population) |
| **Jamaica** | JAM-DEX | 2022 | Legal tender, distributed through commercial banks |
| **Nigeria** | eNaira | 2021 | One of the first African CBDCs. Adoption has been limited despite government incentives |
| **Eastern Caribbean** | DCash | 2021 | Multi-country CBDC across Eastern Caribbean Currency Union states |

### Major Pilots

#### China: e-CNY (Digital Yuan)

The most advanced major-economy CBDC globally:

- **Scale**: 260 million+ pilot wallets, $250 billion+ in cumulative transactions
- **Coverage**: Active in 26 cities including Beijing, Shanghai, Shenzhen, and Guangzhou
- **Two-tier model**: PBoC (People's Bank of China) issues e-CNY to commercial banks, which distribute to the public. The PBoC does not hold individual accounts directly
- **Programmable features**: Being tested for targeted subsidies, transport payments, and consumption vouchers
- **2022 Winter Olympics**: e-CNY was available for use by athletes and visitors
- **Strategic motivation**: China views e-CNY as a tool for:
  - **Internationalising the yuan**: Reducing reliance on US dollar payment systems (SWIFT)
  - **Competing with Alipay/WeChat Pay**: Ensuring the state maintains control over payment infrastructure (Alipay and WeChat Pay handle ~90% of China's mobile payments)
  - **Capital controls**: Maintaining visibility and control over cross-border flows
  - **Monetary sovereignty**: Countering the threat of USD-denominated stablecoins

#### India: e-Rupee (e-Rs)

- **Pilot launched**: December 2022
- **Two tracks**: Wholesale CBDC (interbank settlement) and retail CBDC (public use)
- **RBI approach**: Cautious rollout through commercial banks
- **Motivation**: The RBI is historically hostile to private crypto and stablecoins, viewing the e-Rupee as a government-controlled alternative
- **Adoption**: Limited pilot participation, scaling gradually

#### Brazil: Drex

- **Central Bank of Brazil** developing Drex as a wholesale-focused CBDC
- **Use cases**: Tokenised asset settlement, programmable payments, DeFi-like financial products on a regulated platform
- **Approach**: More innovative than most CBDCs -- exploring tokenisation and smart contract functionality
- **Timeline**: Pilot phase ongoing, gradual expansion planned

#### European Union: Digital Euro

- **ECB** (European Central Bank) in "preparation phase" (2023-2025)
- **Scope**: Would be legal tender across all 20 eurozone countries -- potentially 350 million+ users
- **Privacy framework**:
  - Offline small payments would be anonymous (like cash)
  - Online payments visible to intermediary banks but **not** to the ECB
  - Balance limits (proposed: EUR 3,000) to prevent bank disintermediation
- **Likely launch**: 2027-2028 at earliest, requires European Parliament and Council approval
- **Coexistence**: Designed to complement cash and private payment methods, not replace them

#### Russia: Digital Ruble

- Pilot launched 2023 with 13 banks
- Motivations include sanctions circumvention and reducing dependence on Western payment infrastructure
- International settlement potential being explored with friendly nations

### Research and Development Phase

| Country/Region | Project | Status |
|---------------|---------|--------|
| **United States** | Project Hamilton (Fed/MIT) | Research completed. Fed Chair Powell: would require Congressional authorisation. Political opposition strong. US likely to regulate stablecoins rather than launch CBDC |
| **United Kingdom** | Digital Pound ("Britcoin") | BoE consultation completed. Design phase. Potential launch 2025-2028 |
| **Australia** | eAUD | RBA completed limited pilot (2023) testing 16 use cases including offline payments, tokenised assets, and carbon credit settlements. No commitment to full launch. See [[australian-crypto-regulation]] |
| **Canada** | Project Jasper | Research phase. Bank of Canada actively studying but no commitment to launch |
| **Sweden** | e-Krona | Riksbank pilot. Sweden is one of the world's most cashless economies, making CBDC more relevant |
| **Japan** | Digital Yen | BoJ completed technical experiments. Cautious approach. No launch timeline |
| **South Korea** | Digital Won | BoK pilot completed. Wholesale focus |

### Discontinued

- **Ecuador**: Was one of the first countries to launch a digital currency (Dinero Electronico, 2014). Discontinued in 2018 due to low adoption and public distrust
- **Senegal**: eCFA project discontinued

## CBDC vs Stablecoin vs Bank Deposit vs Cash

| Dimension | CBDC | [[stablecoins|Stablecoin]] | Bank Deposit | Physical Cash |
|-----------|------|------------|-------------|---------------|
| **Issuer** | Central bank | Private company | Commercial bank | Central bank |
| **Legal tender** | Yes | No | No | Yes |
| **Deposit insurance** | N/A (sovereign) | None | Yes (limited) | N/A |
| **Programmable** | Potentially | Yes (smart contracts) | Limited | No |
| **Privacy** | Low-Medium (varies) | Medium (pseudonymous) | Low (bank records) | High (anonymous) |
| **Interest-bearing** | Potentially | Some (see [[stablecoin-yields]]) | Yes | No |
| **Censorship resistance** | None | Varies (DAI high, USDC low) | None | High |
| **24/7 availability** | Yes | Yes | No (banking hours for some) | Yes |
| **Cross-border** | Limited (bilateral) | Yes (global) | Yes (slow, expensive) | Limited |
| **Smart contract composability** | Limited | Yes ([[defi]]) | No | No |
| **Counterparty risk** | Sovereign (lowest) | Issuer risk | Bank risk | None (physical) |

## Impact on Crypto Markets

CBDCs could affect crypto markets in several ways:

1. **Stablecoin competition**: CBDCs could reduce demand for stablecoins in payments use cases -- why use USDC when you can use a government-backed digital dollar? However, stablecoins offer advantages CBDCs likely will not: composability with [[defi|DeFi]], censorship resistance, and 24/7 global availability
2. **Coexistence**: The most likely outcome is coexistence -- CBDCs for regulated payments and settlement, stablecoins for DeFi and crypto-native use cases
3. **Securities settlement**: CBDCs could enable real-time settlement of securities trades (currently T+1 in most markets), reducing counterparty risk
4. **Cash obsolescence**: In economies that launch CBDCs and reduce cash usage, [[bitcoin|Bitcoin]] and privacy coins may see increased demand from citizens seeking financial privacy
5. **Monetary policy**: CBDCs with programmable features could make monetary policy more powerful and direct -- positive for economic stability but concerning for individual financial autonomy

## Trader and Market-Structure Relevance

For a trader, CBDCs matter less as something to *trade* and more as a structural force on the assets that are traded:

- **Stablecoin issuers as a thesis** — the regulatory choice between "launch a CBDC" and "regulate stablecoins" directly affects the addressable market for [[usdc|USDC]], [[usdt|USDT]], and the firms behind them. A US tilt toward regulated stablecoins (rather than a retail CBDC) is broadly constructive for compliant private stablecoins and the rails built on them.
- **Bank deposit franchises** — a widely adopted, interest-competitive retail CBDC is a structural negative for commercial-bank net interest margins (deposit flight). This feeds into how one might think about bank equities and the [[ecb|ECB]]/Fed reaction functions. The standard mitigations (caps, no interest) exist precisely to neutralise this.
- **Settlement and collateral** — *wholesale* CBDCs and tokenised central-bank money (e.g. Project mBridge, Brazil's Drex) point toward atomic, real-time settlement of securities and FX. Shorter settlement cycles reduce counterparty and funding risk in the plumbing every trader relies on; see [[counterparty-risk]].
- **FX and reserve-currency dynamics** — China's e-CNY is explicitly aimed at yuan internationalisation and reducing reliance on USD payment rails (SWIFT). Multilateral wholesale-CBDC bridges are a slow-moving but real input to long-horizon FX and [[forex]] views.
- **Macro liquidity and the privacy bid for hard assets** — programmable, expirable, or negative-yielding CBDC features (if ever deployed) strengthen the structural case some investors make for [[bitcoin|Bitcoin]], gold, and privacy assets as opt-out stores of value. This is a *narrative* driver, not a backtested edge, and should be treated as such.

None of these is a short-horizon trading signal; CBDC development is a multi-year regulatory and infrastructure process. The trading-relevant edge, if any, is in correctly anticipating *regulatory direction* (CBDC vs. stablecoin) and *settlement-infrastructure change*, not in front-running a launch date.

## Common Misconceptions and Pitfalls

1. **"A CBDC is just a government stablecoin."** No — a stablecoin is a *private liability* backed by reserves and carries issuer/redemption risk; a CBDC is a *direct central-bank liability* with no credit risk. They sit in different rows of the money hierarchy. See the comparison table above.
2. **"A CBDC means the end of cash."** Most published designs (digital euro, digital pound) explicitly position the CBDC as a *complement* to cash, with cash legally protected. Whether that holds in practice is a political question, not a technical inevitability.
3. **"A retail CBDC will pay interest and replace my savings account."** The opposite is the design intent: caps and zero remuneration are deliberately built in to *prevent* it competing with deposits.
4. **"CBDC = blockchain."** Many CBDC designs use centralised or permissioned ledgers, not public blockchains. The technology choice is independent of the "central-bank money" property.
5. **"All CBDCs are equally surveilling."** Privacy ranges from China's intermediated-but-state-visible e-CNY to the tiered-anonymity digital-euro proposal. The privacy outcome is a design choice, not an inherent property — which is exactly why the design debate matters.
6. **"It's a tradable asset class."** A CBDC is national-currency money at par; there is no FX or basis trade *in the CBDC itself* against its own fiat. The tradable consequences are second-order (bank equities, stablecoin issuers, settlement infrastructure, FX regimes).

## Related

- [[stablecoins]] -- Private-sector stablecoins
- [[stablecoin-regulation]] -- Stablecoin regulatory frameworks by country
- [[regulation]] -- General crypto regulation
- [[usdc]] -- Most regulated major stablecoin
- [[usdt]] -- Largest stablecoin
- [[bitcoin]] -- Decentralised alternative to both CBDCs and stablecoins
- [[australian-crypto-regulation]] -- Australian eAUD CBDC pilot
- [[aml-ctf]] -- Anti-money laundering frameworks
- [[defi]] -- DeFi ecosystem (unlikely to use CBDCs)
- [[central-bank]] -- the issuer of CBDCs
- [[monetary-policy]] -- the policy framework CBDCs could reshape
- [[ecb]] -- the central bank developing the digital euro
- [[fomc]] -- the US Federal Reserve, which has declined to launch a retail CBDC
- [[counterparty-risk]] -- reduced by atomic CBDC-based settlement

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
