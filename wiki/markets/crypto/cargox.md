---
title: "CargoX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["CXO", "CargoX"]
entity_type: protocol
founded: 2018
headquarters: "Slovenia"
website: "https://cargox.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[polygon]]", "[[real-world-assets]]", "[[smart-contracts]]", "[[tokenization]]", "[[web3]]"]
---

# CargoX

**CargoX** (CXO) is a blockchain-based **document-transfer and ownership platform**, best known for its **Smart Bill of Lading (Smart B/L)** for the shipping and logistics industry. The platform uses public blockchain to let users issue, transfer, and verify ownership of digital documents securely and instantly, replacing slow, courier-based paper processes. **CXO** is the network's native utility token used to pay for document transactions on the platform.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, CXO trades at **$0.151383**, ranked **#719** by market capitalization with a market cap of roughly **$25.29M**. The token is up **+2.03%** over 24 hours and roughly flat over the week at **-1.13%**, resilient relative to the broader risk-off market (Crypto Fear & Greed Index 21, "Extreme Fear"; Bitcoin ~$64,508).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CXO |
| **Market Cap Rank** | #719 |
| **Market Cap** | $25.29M |
| **Current Price** | $0.151383 |
| **24h Change** | +2.03% |
| **7d Change** | -1.13% |
| **Genesis Date** | 2018-01-18 |
| **Categories** | Infrastructure, Logistics / Supply Chain, Polygon Ecosystem, Ethereum Ecosystem |
| **Website** | [https://cargox.io/](https://cargox.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

CargoX (founded 2018, Slovenia) provides a **blockchain document-transfer platform** that lets users upload documents and securely transfer their **ownership** — not just the file, but verifiable title to it. Its flagship use case is the **Smart Bill of Lading (Smart B/L)**, a digital, blockchain-backed replacement for the paper bill of lading that is central to international shipping. By digitizing B/Ls and other trade documents, CargoX aims to cut the time, cost, and fraud risk of physically couriering paper title documents between exporters, carriers, banks, and importers.

The platform has also been adopted in government/customs contexts for trusted document exchange (for example, single-window-style trade document submission systems), extending the model beyond shipping into broader regulated document workflows.

### How the platform works (deep dive)

CargoX is best understood as a **trade-document rail** rather than a generic file store. The architecture layers three things on top of a public blockchain:

1. **Document anchoring.** A document (a bill of lading, certificate of origin, packing list, etc.) is hashed; the cryptographic fingerprint and metadata are recorded on-chain while the document payload itself is held off-chain (encrypted), so sensitive trade data does not sit in plaintext on a public ledger. The on-chain record is what proves a given document version existed at a given time and who holds title to it.
2. **Ownership as a transferable token.** The defining feature of a bill of lading is that it is a **document of title** — whoever lawfully holds it controls the underlying cargo. CargoX represents that holdership as an on-chain right that can be transferred between parties (shipper → carrier → bank → consignee) in seconds, mirroring the legal "endorsement and delivery" of a paper B/L but without physical courier movement. This is the function that distinguishes a *Smart B/L* from a mere scanned PDF.
3. **The Platform / Public Blockchain Document Transaction Protocol (BDTP).** CargoX's branded protocol governs issuance, transfer, access control, and verification of documents. End users interact through a web application; enterprises and government systems integrate via APIs. [[smart-contracts]] enforce the transfer-of-ownership logic, and the network inherits settlement security from the underlying public chains rather than running a dedicated [[layer-1]].

A key design choice is **legal alignment with MLETR** (the UNCITRAL Model Law on Electronic Transferable Records), the framework that gives an electronic bill of lading the same legal force as paper. CargoX positions its Smart B/L as MLETR-compatible, which matters because trade finance and carriage contracts only accept an eBL if it is legally equivalent to the paper instrument it replaces.

### Token role (CXO)

**CXO** is the platform's utility token: it is used to **pay for document transactions** (issuance and ownership transfer) on the CargoX network. The token is an ERC-20-style asset originally deployed on [[ethereum]] with a [[polygon|Polygon]] PoS deployment as well, leveraging [[smart-contracts]] for the transfer-of-ownership logic and inheriting security from those public chains rather than running a dedicated [[layer-1]]. Because CXO is the metering unit for document operations, demand for the token is, in principle, a function of platform throughput — but in practice fees are frequently abstracted away from enterprise/government end users (who pay in fiat or via prepaid arrangements), which weakens the direct link between document volume and on-chain CXO demand.

### Value accrual & governance

CXO is a pure **utility/payment token**, not a fee-share or staking-yield instrument. There is no native staking, validator economics, or burn mechanism documented for CXO comparable to a [[layer-1]] gas token — value accrual depends entirely on the token being the required medium for paying platform fees. Supply is uncapped ("Unlimited" max), so there is no hard scarcity narrative; the circulating-to-FDV ratio (~0.78) implies a meaningful tranche of tokens is held outside circulation. Governance over the protocol is centralized with the CargoX company rather than a token-holder DAO, consistent with its enterprise/B2B positioning.

### Competitive position

CargoX operates at the intersection of [[web3]] and trade-document digitization, an area also targeted by industry consortia and the broader push toward electronic bills of lading (eBL) under frameworks such as the MLETR. Its edge is an early, production-grade Smart B/L product and government deployments; its challenge is that large incumbents and bank-backed trade-finance networks also pursue eBL standards, and adoption depends on enterprise/regulatory uptake rather than retail crypto demand.

| Project / Standard | Approach | Chain / Tech | Token | Differentiator vs CargoX |
|---|---|---|---|---|
| **CargoX (CXO)** | Public-blockchain Smart B/L & document title transfer | [[ethereum]] + [[polygon]] | CXO (utility/payment) | Early production eBL; government/customs deployments |
| **TradeLens** (defunct) | Permissioned shipping data platform (Maersk/IBM) | Hyperledger Fabric | none | Was consortium-led; **shut down in 2023** for lack of industry-wide adoption |
| **Bolero / essDOCS / WaveBL** | Established eBL providers for trade finance | Mostly permissioned / private DLT | none | Bank- and carrier-backed incumbents; no public token |
| **IQAX / GSBN** | Carrier consortium blockchain (CMA CGM, COSCO, etc.) | Permissioned consortium chain | none | Backed by major liner carriers; closed network |

The strategic contrast is **public token network vs. permissioned consortium**: CargoX is one of the few eBL plays with a public, tradeable token, but the bulk of trade-finance volume flows through bank/carrier consortia that have no token and no need for one. The 2023 wind-down of TradeLens — the highest-profile consortium effort — illustrates how hard adoption is even for well-capitalized incumbents.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 167.16M CXO |
| **Total Supply** | 215.12M CXO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.66M |
| **Market Cap / FDV Ratio** | 0.78 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5233 (2023-11-08) |
| **Current vs ATH** | -72.68% |
| **All-Time Low** | $0.00003988 (2020-01-01) |
| **Current vs ATL** | +358428.16% |
| **24h Change** | +2.03% |
| **7d Change** | -1.13% |
| **1y Change** | -30.07% |

CXO remains well below its 2023 all-time high (~$0.52), consistent with weak demand for "real-world utility" infrastructure tokens whose value accrual depends on enterprise adoption rather than speculative flows.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb6ee9668771a79be7967ee29a63d4184f8097143` |
| Polygon Pos | `0xf2ae0038696774d65e67892c9d301c5f2cbbda58` |

---

## How & Where It Trades

| Venue type | Detail |
|---|---|
| **Spot DEX** | Primary on-chain liquidity is on [[uniswap|Uniswap]] V2/V3 (CXO/WETH) on [[ethereum]], with corresponding liquidity on [[polygon]] |
| **Spot CEX** | CXO has historically appeared on mid-tier centralized venues; depth is thin and listing set varies |
| **Derivatives** | No meaningful, liquid perp/futures market — CXO is effectively spot-only |
| **Liquidity profile** | Very thin: the snapshot 24h volume of ~$2,249 against a ~$25M cap implies a microscopic float actually changes hands daily |

The defining trading reality for CXO is **illiquidity**. With reported 24h volume in the low thousands of dollars, even a four-figure order can move price several percent. This is a token that trades on its narrative (trade-document digitization / eBL adoption) far more than on flow, and any position must assume meaningful slippage and gap risk on both entry and exit (see [[slippage]], [[liquidity]]).

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XB6EE9668771A79BE7967EE29A63D4184F8097143/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0XB6EE9668771A79BE7967EE29A63D4184F8097143/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Narrative, Category & Catalysts

CXO sits in the **real-world-asset / trade-digitization** corner of crypto — the slow-burn "blockchain for enterprise" thesis rather than a fast-moving DeFi or memecoin narrative. Its category overlaps with [[real-world-assets|RWA]] and [[tokenization]], and it is tagged across Infrastructure, Logistics/Supply Chain, [[polygon|Polygon Ecosystem]], and [[ethereum|Ethereum Ecosystem]].

Potential catalysts (and why they are double-edged):

- **eBL mandates & MLETR adoption.** As more jurisdictions enact MLETR-aligned law (e.g., the UK's Electronic Trade Documents Act took effect in 2023), legally valid electronic bills of lading become possible at scale. This is the single largest structural tailwind for any eBL provider — but it benefits permissioned bank/carrier networks too, not just CargoX.
- **Government / customs deployments.** CargoX's adoption in single-window trade-document systems is its most concrete real-world traction; expansion of such deployments is the most credible source of fundamental demand.
- **Trade-finance digitization cycles.** Periodic industry pushes to digitize trade finance (post-COVID supply-chain shocks accelerated interest) lift the category.

The persistent counter-narrative is that **fee abstraction breaks the token thesis**: even if document volume grows, end users rarely touch CXO directly, so platform success need not translate into token demand.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cargox.io/](https://cargox.io/) |
| **Twitter** | [@CargoXio ](https://twitter.com/CargoXio ) |
| **Reddit** | [https://www.reddit.com/r/CargoXio/](https://www.reddit.com/r/CargoXio/) |
| **Whitepaper** | [https://cargox.io/CargoX-Whitepaper.pdf](https://cargox.io/CargoX-Whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2,248.62 |
| **Market Cap Rank** | #712 |
| **24h Range** | $0.1425 — $0.1482 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## History & Timeline

Only well-established, dated milestones are listed; granular product dates are omitted where they cannot be verified.

| Date | Event |
|---|---|
| **2018** | CargoX founded in Slovenia; CXO genesis date **2018-01-18**; token sale conducted in 2018 (genesis on CoinGecko: 2018-08-28 era for trading) |
| **2020-01-01** | All-time low era for CXO (~$0.00003988) during the deep bear market |
| **2023-11-08** | CXO all-time high of **$0.5233** during the late-2023 RWA/utility-token interest cycle |
| **2026-06-22** | Trades ~$0.151 (rank #719, ~$25.3M cap), ~73% below ATH, amid an Extreme-Fear macro regime |

(Founding, ATH/ATL, and genesis dates are sourced from the CoinGecko snapshot; no narrative product-announcement dates are asserted without a source.)

---

## Trading Playbook (context: Extreme-Fear bear regime, 2026-06-22)

> *Not investment advice. CXO is a thin-liquidity micro-cap; sizing and slippage dominate any thesis.*

- **Regime read.** The macro tape is an established bear market (Fear & Greed 21, BTC ~16% below its 200-day MA). Low-cap RWA/infrastructure tokens with negligible volume are the highest-beta, lowest-liquidity end of the risk curve and typically bleed or gap in risk-off conditions.
- **Liquidity first.** With ~$2k/day of volume, position size must be tiny relative to the order book. Treat fills as the binding constraint; use limit orders, expect partial fills, and never assume you can exit at the marked price (see [[slippage]], [[liquidity]]).
- **Thesis is fundamental, not technical.** CXO is a multi-year adoption bet on eBL/trade-document digitization, not a momentum trade. There is no liquid derivatives market to hedge with, so any exposure is unhedged spot.
- **Catalyst-driven only.** The rational entry case is anticipation of concrete adoption (new government deployment, major carrier/bank integration, MLETR-mandate expansion) — not chart patterns on a near-zero-volume token.
- **Risk controls.** Define a hard invalidation (e.g., loss of platform traction, broken token-demand link) and size for total loss. In Extreme Fear, prefer waiting for regime confirmation over catching a falling micro-cap (see [[risk-management]], [[when-to-retire-a-strategy]]).

---

## Risks

- **Adoption-dependent value:** CXO's utility is tied to document-transaction volume; enterprise/government sales cycles are long and value accrual to the token is uncertain.
- **Standards competition:** The shift to electronic bills of lading (eBL) is contested by bank consortia and other vendors; CargoX is one of several approaches to MLETR-aligned digital trade documents.
- **Token-vs-product disconnect:** A working B/L product does not guarantee that on-chain CXO demand scales with it, especially if fees are abstracted away from end users.
- **Small-cap liquidity:** Rank #719 (~$25.3M); thin order books mean slippage and gap risk (see [[risk-management]]).
- **Macro/regime sensitivity:** Operates in an "Extreme Fear" market (Fear & Greed 21 as of 2026-06-22).

> *Not investment advice. Figures are point-in-time and crypto markets are highly volatile.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[smart-contracts]]
- [[web3]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). General market knowledge; no additional specific wiki source ingested yet.

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XB6EE9668771A79BE7967EE29A63D4184F8097143/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0XB6EE9668771A79BE7967EE29A63D4184F8097143/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---
