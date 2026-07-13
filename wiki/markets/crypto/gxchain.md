---
title: "GXChain"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["GXC", "Gongxinbao", "GXB"]
entity_type: protocol
founded: 2017
headquarters: "Hangzhou, China (origin)"
website: "https://www.gxb.io/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[delegated-proof-of-stake]]", "[[smart-contracts]]"]
---

# GXChain

**GXChain** (GXC) is a [[layer-1]] public blockchain focused on the **data economy**, built by the team behind **Gongxinbao (GXB)**, a Chinese data-exchange company. Its core offering is a decentralized data-exchange marketplace plus identity/credit services (KYC, ID verification, multi-dimensional data), positioning it as data-economy infrastructure rather than a general-purpose app chain. GXChain ranks **#785** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot date GXC traded at **$0.299188** with a market cap of **$22,439,067** (rank #766), up **2.51%** over 24 hours and modestly higher over 7 days (**+1.58%**) — relatively stable versus peers despite the broad risk-off backdrop (Fear & Greed Index 21 / "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GXC |
| **Market Cap Rank** | #766 |
| **Market Cap** | $22,439,067 |
| **Current Price** | $0.299188 |
| **24h Change** | +2.51% |
| **7d Change** | +1.58% |
| **Genesis Date** | 2017-06-10 |
| **Consensus** | [[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]] + Proof of Credit Share (PoCS) |
| **Categories** | Big Data, Data Economy, [[layer-1|Layer 1]] |
| **Website** | [https://www.gxb.io/](https://www.gxb.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

GXChain, developed by the team behind **Gongxinbao (GXB)**, is a public [[layer-1]] blockchain built around decentralized **data exchange**. Its flagship product is a data marketplace marketed as the first of its kind — designed so that the exchange does not cache personal data, aiming to preserve privacy while letting parties trade verified data. The platform also targets data-copyright protection, anti-fraud measures and bilateral transactions. The GXB data exchange was commercialized in September 2017 and pitched at enterprises in network lending, automobile finance, consumer lending and banking.

Beyond a generic [[smart-contracts|smart-contract]] / blockchain-as-a-service offering, GXChain emphasizes data-economy services: **ID verification, multi-dimensional data, KYC, and quick login**. The chain also supports issuing new assets. An early flagship dApp dealt with personal credit management and credit verification.

### Consensus and architecture

GXChain combines two consensus ideas:

- **[[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]]** for ordering and recording transactions on the blockchain — a small set of elected delegates ("trustnodes") produce blocks, trading some decentralization for throughput. The architecture is in the BitShares/Graphene lineage, the same high-performance C++ engine used by EOS and BitShares, which is the source of GXChain's high-throughput claims.
- **Proof of Credit Share (PoCS)** — a project-specific mechanism intended to govern consensus around the data-exchange layer (credit/reputation weighting), so participants with more verifiable on-chain credit/contribution carry more weight in the data economy.

> **Data caveat:** Marketing materials have historically cited very high throughput figures (e.g. "~100,000 TPS"). Such peak-TPS claims are vendor-stated and should be treated as qualitative/marketing rather than independently verified production performance.

### Data-exchange design and BaaS layer

The distinguishing technical idea is a **privacy-preserving data marketplace**: the protocol is marketed as not caching personal data centrally — instead it brokers verified, point-to-point data transactions so a buyer can obtain a result (e.g. a credit or identity check) without the exchange itself warehousing the underlying records. On top of this, GXChain exposes a **blockchain-as-a-service (BaaS)** layer (developer toolkits, identity APIs such as "G-ID" / quick-login, KYC and multi-dimensional data services) and supports issuing new assets and [[smart-contracts|smart-contract]]-style applications. The thesis is that data — not generic DeFi — is the chain's native economic good.

### Value accrual

GXC accrues value as the **settlement and access token** of the data economy: it pays transaction/gas fees, settles purchases on the GXB data exchange, and is staked toward DPoS delegate election and PoCS credit weighting. Demand is therefore tied to real marketplace throughput and enterprise data-service usage rather than speculative TVL — a thesis that has struggled as the 2017-era "data-economy public chain" narrative lost ground to modern DePIN and general-purpose L1s.

### Origins and leadership

GXChain originated in China; **Minqiang Huang (Huang Minqiang)** is cited as founder/CEO with a background in data exchange, blockchain and fintech (former CTO roles in Chinese internet companies). Guojun Tu has been listed as co-founder / VP. As with most China-origin data and blockchain projects, the regulatory environment around personal data, credit scoring and crypto in China is a material consideration.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 75.00M GXC |
| **Total Supply** | 100.00M GXC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $31.25M |
| **Market Cap / FDV Ratio** | 0.75 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $10.61 (2018-01-13) |
| **Current vs ATH** | ~-97.2% |
| **All-Time Low** | $0.1898 (2020-03-13) |
| **24h Change** | +2.51% |
| **7d Change** | +1.58% |

GXC peaked in the January 2018 cycle and trades far below that level today. Its slightly positive 7-day performance (+1.58%) during an "Extreme Fear" market (Fear & Greed 21 on 2026-06-22) is comparatively resilient within this small-cap cohort, though that can also reflect very thin trading volume rather than genuine demand strength.

---

## Token Role

| Function | Description |
|---|---|
| **Gas / fees** | GXC pays for transactions and smart-contract execution on GXChain. |
| **Data-exchange settlement** | Used to pay for and settle data purchases on the GXB marketplace. |
| **Staking / governance** | Staked toward DPoS delegate election and network participation. |

Circulating supply is ~75M of a 100M total, giving a market-cap/FDV ratio around 0.75 — meaning roughly a quarter of the supply remains to be released, a dilution factor to watch.

---

## History

- **2016–2017** — **Gongxinbao (GXB)** is built in Hangzhou, China as a data-exchange business; founder/CEO **Minqiang Huang (Huang Minqiang)** brings a data-exchange, blockchain and fintech background, with **Guojun Tu** listed as co-founder/VP.
- **June 2017** — GXChain mainnet genesis (2017-06-10), built on the BitShares/Graphene C++ engine with [[delegated-proof-of-stake|DPoS]] consensus.
- **September 2017** — the GXB data exchange is commercialized, pitched at enterprises in network lending, auto finance, consumer lending and banking.
- **January 2018** — GXC reaches its ATH (~$10.61) during the broad altcoin peak.
- **2018–2020** — rebrand/expansion from "GXS/GXShares" branding toward "GXChain (GXC)"; addition of identity (G-ID), KYC, and BaaS tooling; the chain weathers the bear market and tightening Chinese crypto/data regulation.
- **2020–present** — trades as a small-cap with thin liquidity; the data-economy public-chain narrative has limited traction versus modern DePIN and general-purpose L1s.

---

## Governance

- **DPoS trustnodes:** GXC holders stake toward electing a limited set of block-producing delegates; the small validator set trades decentralization for throughput, a known DPoS trade-off shared with [[steem]]/[[hive]] and EOS.
- **PoCS credit weighting:** Governance and participation in the data layer are influenced by accumulated on-chain credit/reputation, not stake alone.
- **Founding-team / corporate steering:** As a China-origin project led by the Gongxinbao team, direction is concentrated; the surrounding regulatory environment for personal data, credit scoring and crypto in China is a material governance constraint.

---

## GXChain vs. Peer Data / Platform Chains

| Dimension | GXChain (GXC) | [[ardor]] (ARDR) | [[ethereum|Ethereum]] (ETH) | Ocean Protocol (OCEAN) |
|---|---|---|---|---|
| **Primary use** | Data exchange / data economy | Parent-child BaaS | General smart contracts | Data marketplace / tokenized data |
| **Consensus** | [[delegated-proof-of-stake|DPoS]] + PoCS | Forging [[proof-of-stake|PoS]] | PoS (post-Merge) | ERC-20 on Ethereum |
| **Engine** | BitShares/Graphene (C++) | Nxt-derived (Java) | EVM | EVM (token, not L1) |
| **Identity/KYC** | Native (G-ID, KYC, multi-dim data) | Account control / phasing | Via dApps | Limited |
| **Origin** | 2017, China | 2018 (Nxt 2013) | 2015 | 2017 |
| **Key risk** | China data/crypto regulation | Single-steward (Jelurida) | Fees/competition | Adoption |

GXChain's differentiation is a **native data-economy stack** (privacy-preserving exchange + identity/KYC services) rather than generic programmability. The persistent headwinds are **China-specific regulatory exposure** around personal data and credit scoring, and an aging narrative.

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1]] blockchain

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.gxb.io/](https://www.gxb.io/) |
| **Twitter** | [@GXChainGlobal](https://twitter.com/GXChainGlobal) |
| **Reddit** | [https://www.reddit.com/r/GXS/](https://www.reddit.com/r/GXS/) |
| **Telegram** | [GXChain_international](https://t.me/GXChain_international) (15,663 members) |
| **Discord** | [https://discord.gg/qHWZR5fJQa](https://discord.gg/qHWZR5fJQa) |
| **GitHub** | [https://github.com/gxchain/gxb-core](https://github.com/gxchain/gxb-core) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 226 |
| **GitHub Forks** | 77 |
| **Pull Requests Merged** | 115 |
| **Contributors** | 12 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.299188 |
| **Market Cap (2026-06-22)** | $22,439,067 |
| **Market Cap Rank** | #766 |
| **24h Change** | +2.51% |
| **7d Change** | +1.58% |
| **Last Updated** | 2026-06-22 |
| **Historical (2026-04-09)** | 24h volume $2,175.17; rank #775; 24h range $0.3121–$0.3372 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks & Considerations

- **Regulatory exposure** — a China-origin project centered on personal data and credit scoring sits in a heavily regulated area; Chinese policy on crypto and data privacy is restrictive and has shifted over time.
- **Liquidity** — extremely thin reported trading volume; small orders can move price disproportionately, and exit liquidity may be limited.
- **Marketing-stated performance** — high TPS and "first in the world" claims are vendor-stated; treat them as marketing rather than verified facts.
- **Aging narrative** — the data-economy public-chain thesis from 2017–2018 has limited traction versus modern data/DePIN and general-purpose L1 narratives.
- **Dilution** — ~25% of total supply not yet circulating.
- *Not investment advice — point-in-time data; micro-cap altcoin risk applies.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-stake]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
