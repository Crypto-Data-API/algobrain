---
title: "Chromia"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, nft, altcoins]
aliases: ["CHR", "ChromaWay", "Chroma"]
entity_type: protocol
headquarters: "Sweden"
website: "https://chromia.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[real-world-assets]]"]
---

# Chromia

**Chromia** (CHR) is an open-source [[layer-1|Layer-1]] blockchain built around a **relational-database** architecture, conceived by the Swedish company **ChromaWay AB**. Unlike most blockchains that store data as key-value pairs or flat state, Chromia structures on-chain data the way a SQL database does, using its own SQL-like language called **Rell**. This makes it well suited to data-heavy applications — games, [[real-world-assets|real-world-asset (RWA)]] registries, and enterprise data systems — that need efficient querying and structured storage. The Chroma token (CHR) launched in May 2019.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* CHR trades at **$0.0163674**, ranked **#931** with a market cap of **~$15.96M**. It is up sharply over 24h (**+10.05%**) and **+3.99%** over the week — a notable outperformer in an otherwise weak market (BTC ~$64,180; Fear & Greed 22 / Extreme Fear), with the +10% move standing out against the broader cohort's softness.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CHR |
| **Market Cap Rank** | #931 |
| **Market Cap** | ~$15.96M |
| **Current Price** | $0.0163674 |
| **24h / 7d Change** | +10.05% / +3.99% |
| **Builder** | ChromaWay AB (Sweden) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Real World Assets (RWA), Modular Blockchain, NFT, AI, Chromia Ecosystem |
| **Website** | [https://chromia.com/](https://chromia.com/) |

---

## Overview

Chromia is an open-source public blockchain conceived by Swedish company ChromaWay AB. The technology is adapted from **Postchain**, ChromaWay's earlier enterprise consortium-blockchain product, giving the project an unusually long enterprise lineage for a public [[layer-1|L1]].

Chromia operates both as a standalone Layer-1 and as an EVM-compatible Layer-2 enhancement for BNB Smart Chain and Ethereum. It is designed to improve scalability, data handling, and fee flexibility for decentralized applications. Its defining feature is the **relational blockchain** architecture together with **Rell**, a custom language that reads and behaves much like SQL. This lets developers combine blockchain's security and immutability with the querying efficiency and structured storage of a relational database — a meaningful advantage for data-intensive dApps.

Each dApp on Chromia runs on its **own sidechain** rooted in the main chain, so applications scale independently and developers choose their own fee model. One app may charge users transaction fees in CHR (the conventional model), while another can stake enough CHR to reserve computation and offer its users **fee-less** transactions — a flexible cost structure aimed at consumer-grade UX.

Applications built on Chromia span gaming (the open-world farming game **My Neighbor Alice**), DeFi (the options platform **Hedget**), and real-world-asset use cases (the **LAC PropertyChain** land-registry initiative) — reflecting ChromaWay's roots in land registry and enterprise data.

---

## Architecture — How the Relational Blockchain Works

Chromia's defining bet is that most real applications are fundamentally about **structured, queryable data**, and that forcing that data into a flat key-value store (as most blockchains do) is the wrong abstraction. Its architecture follows from this:

- **Relational state model.** Every Chromia node runs a PostgreSQL database under the hood. On-chain state lives in actual relational tables with columns, types, indexes, and foreign keys — not opaque byte blobs. This makes complex queries (joins, filters, aggregations) cheap and native, which is a genuine advantage for data-heavy apps (game state, registries, social graphs, RWA records) that on key-value chains require expensive off-chain indexing layers.
- **Rell, the SQL-like language.** Smart contracts ("dapps") are written in **Rell**, a statically-typed language that reads like a blend of SQL and a modern application language. Developers declare entities (tables) and operations (state transitions) directly, and Rell compiles these into deterministic database mutations. This lowers the barrier for the large population of developers already fluent in SQL and relational modeling.
- **Per-dApp sidechains anchored to a system chain.** Each application runs on its **own dedicated blockchain** rather than sharing one global state machine. These app-chains are anchored back to a central system chain for cross-chain security and finality. The benefit is horizontal scalability (one busy app cannot congest another) and per-app customization of fee models and governance.
- **Deterministic consensus over the database.** Block-producing **providers** run nodes and reach BFT-style agreement on the ordered sequence of operations applied to the relational state, so every honest node's database converges to the same tables — preserving blockchain's determinism and verifiability while keeping a SQL data layer.
- **Dual deployment.** Chromia operates both as a standalone L1 and as an EVM-compatible enhancement layer for [[ethereum|Ethereum]] and BNB Smart Chain, letting projects bridge assets and users from larger ecosystems.

The trade-off is the same one every novel runtime faces: the relational model is a real differentiator, but Rell is a new language with a smaller talent pool than Solidity, EVM, or Move, and the per-app-chain model means tooling and liquidity are more fragmented than on a single monolithic chain.

---

## Mechanism & Token Role

- **Relational blockchain + Rell.** On-chain state is modeled as relational tables; Rell (SQL-like) is the developer language, lowering the barrier for data-heavy applications.
- **Per-dApp sidechains.** Apps run on dedicated sidechains anchored to the main chain, enabling independent scaling and customizable fee economics.
- **CHR as gas and staking.** CHR pays transaction fees and is [[staking|staked]] by app operators to reserve compute (enabling fee-less UX) and by node providers/validators securing the network.
- **Provider/validator incentives.** Block-producing providers earn CHR for running the infrastructure, aligning network security with token demand.
- **Governance.** CHR holders participate in protocol governance and ecosystem decisions.

---

## Competitive Position

Chromia's relational-database design is a genuine technical differentiator in a Layer-1 landscape crowded with EVM and Move-based chains. Its enterprise heritage (Postchain, land-registry pilots) and AI/data-infrastructure positioning give it a distinct "data-centric blockchain" narrative, and its RWA tagging aligns it with one of the stronger 2025–26 themes. The challenge is the same one all alt-L1s face: attracting developers and durable, high-usage applications away from dominant ecosystems, and converting an interesting architecture into sustained on-chain activity.

### Comparison vs Data-Focused & RWA L1s

Chromia is most usefully compared to other chains positioning on data, RWAs, and app-specific architecture rather than to general-purpose EVM L1s.

| Dimension | **Chromia (CHR)** | [[ethereum|Ethereum]] | Internet Computer (ICP) | TON / app-chain peers |
|---|---|---|---|---|
| Data model | Relational (PostgreSQL tables) | Key-value (Merkle Patricia trie) | Canister memory (key-value-ish) | Account / cell-based |
| Contract language | Rell (SQL-like) | Solidity / Vyper | Motoko / Rust | FunC / Tact |
| Scaling model | Per-dApp sidechains anchored to system chain | Rollups / L2s | Subnets | Sharded workchains |
| Fee flexibility | Per-app; can offer fee-less UX (app stakes CHR) | User pays gas in ETH | Reverse-gas (dev pays) | User pays gas |
| Native narrative | Data-centric, RWA, gaming, AI | General-purpose, DeFi base layer | Full-stack web on-chain | High-throughput consumer apps |
| Mkt-cap tier (2026-06-21) | ~$16M micro-cap | Top-2 | Mid-cap | Large |

Takeaway: Chromia's relational model and fee-less-UX option are differentiated and genuinely useful for data-heavy and consumer apps, but it must overcome a smaller developer talent pool (Rell vs Solidity) and the fragmentation of a per-app-chain model — while competing for the same RWA/AI/gaming mindshare as far larger, better-capitalized ecosystems.

### Value Accrual & Governance

CHR accrues value through four channels, all usage-gated: (1) **gas/fees** paid by apps and users that charge in CHR; (2) **app staking**, where dApp operators lock CHR to reserve compute and unlock fee-less UX for their users (a structural lock-up that scales with ecosystem activity); (3) **provider/validator rewards**, paid in CHR for running infrastructure, tying network security to token demand; and (4) **governance**, where CHR holders vote on protocol and ecosystem decisions. The fee-less-UX model is a double-edged sword: it can drive adoption by removing end-user friction, but it shifts the demand sink from per-transaction fees to upfront app staking, so CHR's value depends heavily on the number and scale of apps choosing to stake.

---

## Narrative, Category & Catalysts

Chromia sits at the intersection of several active themes: **[[real-world-assets|RWA]]** (its land-registry/Postchain heritage), **AI/data infrastructure** (positioning the relational chain as a data layer for AI agents), **gaming** (My Neighbor Alice and other titles), and **modular/app-chain** design. This multi-narrative tagging means CHR can catch sentiment-driven rallies when any of these themes rotates into favor — which helps explain its standout +10% 24h move on 2026-06-21 against a broadly weak market.

Catalysts to watch (speculative): a flagship app reaching durable, high-volume usage; concrete AI-data-layer partnerships or integrations; RWA tokenization deals leveraging ChromaWay's registry experience; mainnet/economy upgrades; or beta-driven flows if BTC reverses the current bear regime. Because CHR rides multiple narratives, its sharp moves are frequently sentiment- or catalyst-driven rather than fundamentals-driven — a point already noted in the Risks section.

---

## History / Timeline

| Date | Event |
|---|---|
| 2019-05 | Chroma (CHR) token launched following ChromaWay's enterprise/Postchain work |
| 2020-03-13 | All-time low of $0.00874003 during the COVID-crash liquidity event |
| 2021-11-20 | All-time high of $1.49 at the peak of the 2021 bull cycle |
| 2026-06-21 | CHR a standout mover, +10.05% on the day against an Extreme-Fear market |

> Dates above are from market-data snapshots and widely reported project history. Items without a verifiable date are stated as ranges or omitted rather than invented.

---

## Trading Playbook (current regime)

- **Regime read (2026-06-22).** Broad **Extreme Fear** (Fear & Greed 21), long-horizon **Established Bear**, BTC ~16% below its 200-day MA. CHR is a sub-$20M-cap, multi-narrative micro-cap — high beta, with rallies and drawdowns both amplified by thin liquidity.
- **What to watch.** BTC reclaiming its 200-day MA (precondition for broad alt rotation); CHR volume spikes (the +10% day shows how thin books magnify moves); rotation into RWA / AI-data / gaming narratives; concrete ecosystem catalysts (flagship-app usage, partnerships, upgrades).
- **Character of the asset.** CHR has a credible, differentiated tech stack but a long history of the technology outrunning adoption — it remains far below its 2021 ATH. In a bear tape, treat single-day outperformance as sentiment-driven and prone to reversal unless backed by sustained volume or a fundamental catalyst.
- **Bull-case trigger.** A durable BTC trend reversal plus genuine, sticky on-chain usage (or a marquee AI/RWA integration) that converts the relational-blockchain narrative into recurring CHR demand would be required to re-rate the token on fundamentals rather than beta.

---

## Risks

- **L1 competition.** Chromia competes for developers and users against far larger Layer-1 and Layer-2 ecosystems; relational tooling is novel but adds a learning curve (Rell).
- **Narrative dependence.** CHR rides AI, RWA, and gaming narratives; sharp moves (like the +10% 24h) can be sentiment- or catalyst-driven rather than fundamentals-driven.
- **Adoption concentration.** Ecosystem traction has historically leaned on a few flagship apps; breadth and durability of usage remain the key questions.
- **Low liquidity.** A sub-$16M cap makes CHR volatile and slippage-prone, amplifying both rallies and drawdowns.
- **Long drawdown.** The token remains far below its 2021 ATH despite a credible tech stack, underscoring the gap between technology and market adoption.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 955.33M CHR |
| **Total Supply** | 955.33M CHR |
| **Max Supply** | 978.06M CHR |
| **Fully Diluted Valuation** | $15.73M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.49 (2021-11-20) |
| **All-Time Low** | $0.00874003 (2020-03-13) |
| **24h Change** | +10.05% |
| **7d Change** | +3.99% |

> *Current price $0.0163674 is far below the 2021 ATH, but CHR was a standout mover on 2026-06-21 with a +10.05% 24h gain against a broadly weak, Extreme-Fear market.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8a2279d4a90b6fe1c4b30fa660cc9f926797baa2` |
| Binance Smart Chain | `0xf9cec8d50f6c8ad3fb6dccec577e05aa32b224fe` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CHR/USDT | N/A |
| Kraken | CHR/USD | N/A |
| Upbit | CHR/BTC | N/A |
| Bitget | CHR/USDT | N/A |
| KuCoin | CHR/USDT | N/A |
| Crypto.com Exchange | CHR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X8A2279D4A90B6FE1C4B30FA660CC9F926797BAA2/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

**How & where it trades.** CHR has reasonably broad CEX coverage for a micro-cap (Binance, Kraken, KuCoin, Bitget, Upbit, Crypto.com) plus on-chain liquidity via Uniswap V2 on Ethereum and BSC pools, reflecting its dual ERC-20/BEP-20 deployment. Spot is the dominant price-discovery venue; perpetual coverage exists on some derivatives venues but is shallow. At a sub-$16M cap, CHR is low-liquidity and slippage-prone — order books are thin enough that single-day moves of +10% (as on 2026-06-21) are common on modest flow.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://chromia.com/](https://chromia.com/) |
| **Twitter** | [@chromia](https://twitter.com/chromia) |
| **Reddit** | [https://www.reddit.com/r/Teamchromia/](https://www.reddit.com/r/Teamchromia/) |
| **Telegram** | [hellochromia](https://t.me/hellochromia) (18,249 members) |
| **Whitepaper** | [https://chromia.com/whitepaper-english.html](https://chromia.com/whitepaper-english.html) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.0163674 |
| **Market Cap Rank** | #931 |
| **24h Change** | +10.05% |
| **7d Change** | +3.99% |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[layer-1]]
- [[real-world-assets]]
- [[artificial-intelligence]]
- [[staking]]
- [[crypto-markets]]
- [[ethereum]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original snapshot data
- Market data 2026-06-21 via cryptodataapi.com / CoinGecko
- General market knowledge; no additional specific wiki source ingested yet.
