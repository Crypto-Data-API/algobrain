---
title: "Space and Time"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, defi, ai-trading]
aliases: ["SXT", "Space and Time", "SxT"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized"
website: "https://www.spaceandtime.io"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zero-knowledge-proof]]", "[[chainlink]]", "[[depin]]"]
---

# Space and Time

**Space and Time** (SXT) is a decentralized, **verifiable data warehouse** — a blockchain-anchored database that can prove the correctness of SQL query results using zero-knowledge cryptography. Its flagship technology, **Proof of SQL**, lets a smart contract trustlessly verify that a query was executed accurately over untampered data, allowing on-chain applications to consume large-scale off-chain and cross-chain data without trusting a centralized oracle or indexer. The project is backed by **Microsoft's venture fund M12** and has been closely associated with [[chainlink|Chainlink]] for oracle/data delivery. It ranks **#810** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* SXT trades around **$0.007967**, market cap **~$20.7M** (rank #810), **+1.24% over 24h** and **-5.60% over 7d**, against an Extreme-Fear market (Fear & Greed 22, BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SXT |
| **Market Cap Rank** | #810 |
| **Market Cap** | $20,674,260 |
| **Current Price** | $0.00796704 |
| **Categories** | Smart Contract Platform, Ethereum Ecosystem, Zero Knowledge (ZK), Base Ecosystem |
| **Website** | [https://www.spaceandtime.io](https://www.spaceandtime.io) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Space and Time is positioned as "the data blockchain securing on-chain finance." It indexes blockchain data and ingests off-chain/real-world data into a decentralized warehouse, then lets developers run analytical SQL queries whose results can be cryptographically proven and consumed on-chain. This addresses a core limitation of smart contracts: they cannot natively run complex queries over large datasets, and naively trusting an external indexer reintroduces an oracle-trust assumption.

**Proof of SQL** is the differentiator. It is a [[zero-knowledge-proof|zero-knowledge]] proof system that generates a succinct cryptographic proof that a SQL query was executed correctly over a specific, untampered table. A smart contract can verify that proof on-chain cheaply, so the result is trustless even though the heavy computation happened off-chain. Use cases include tokenized real-world assets (RWA), stablecoin reserves attestation, institutional/DeFi analytics, on-chain gaming, and feeding [[artificial-intelligence|AI]] agents verifiable data. The project's Microsoft M12 backing and [[chainlink|Chainlink]] integration (for delivering proven query results as oracle data) are central to its institutional-trust narrative.

The **SXT token** is an ERC-20 on [[ethereum|Ethereum]] (with a Base deployment) and is the network's native utility token: it is used for **staking** by validators/provers that secure the network and generate proofs, **payment** for data processing and queries, **access control**, and **incentives** for node operators and data contributors. As with [[depin|DePIN]] data networks generally, the demand-vs-emissions question is whether query/proof volume from real applications grows faster than token emissions to operators.

---

## Architecture — How It Works

Space and Time combines a **decentralized data warehouse** with a **zero-knowledge proof system** so that the output of a SQL query can be trusted on-chain without trusting the operator who ran it. The pipeline has three conceptual stages:

1. **Ingestion & indexing.** A decentralized network of operators indexes blockchain data (events, balances, transactions across multiple chains) and ingests off-chain / real-world data into tamper-evident tables. Tables are committed to a cryptographic commitment scheme so that any later query can be proven against a fixed, known dataset.
2. **Query execution.** Developers write ordinary **SQL** against the warehouse. Heavy analytical work — joins, aggregations, scans over large tables — runs off-chain where it is cheap, because doing this on-chain is impossible at any reasonable cost.
3. **Proof generation & on-chain verification (Proof of SQL).** The novel piece. **Proof of SQL** generates a *succinct cryptographic proof* that a specific SQL query was executed correctly over the committed table and was not altered. A smart contract verifies that proof cheaply on-chain. The result: a contract can consume the output of a complex query over a large off-chain dataset and be cryptographically certain it is correct — without re-running the query and without trusting a centralized indexer or oracle.

**Why this matters.** Smart contracts are deliberately limited — they cannot natively scan or join large datasets, and naively trusting an external indexer or analytics provider reintroduces exactly the oracle-trust assumption that decentralization is supposed to remove. Proof of SQL replaces *trust* with *verification*: instead of "trust the indexer," it is "verify the proof." This is the same trust-minimization philosophy as a [[zero-knowledge-proof|ZK]] rollup, applied to databases.

**Delivery via Chainlink.** Proven query results can be delivered on-chain through [[chainlink|Chainlink]] infrastructure, letting SxT function as a verifiable-data source feeding existing oracle pipelines — a key part of its enterprise/institutional go-to-market.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.60B SXT |
| **Total Supply** | 5.00B SXT |
| **Max Supply** | 5.00B SXT |
| **Fully Diluted Valuation** | $82.08M |
| **Market Cap / FDV Ratio** | 0.52 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1621 (2025-05-08) |
| **Current vs ATH** | -89.86% |
| **All-Time Low** | $0.0142 (2026-03-31) |
| **Current vs ATL** | +15.66% |
| **24h Change** | +1.24% |
| **7d Change** | -5.60% |
| **1y Change** | +0.00% |

> SXT is a relatively recent listing (ATH $0.1621 in May 2025) and trades ~95% below that peak. With ~52% of max supply circulating, future unlocks represent meaningful dilution risk.

---

## Value Accrual & Governance

SXT is the work-and-payment token of the network, with value accrual gated by *query/proof volume* rather than emissions:

- **Payment.** Applications pay SXT for data processing, queries, and proof generation — the core demand loop. If verifiable-data consumption grows, SXT throughput grows with it.
- **Staking.** Validators/provers stake SXT to participate in indexing and proof generation; staking secures the network and removes supply from the float, with rewards tying operator economics to honest service.
- **Access & incentives.** SXT mediates access control and incentivizes data contributors and node operators.
- **Governance.** As the native token, SXT is positioned to govern protocol parameters as the network decentralizes.

The central tension is the standard data-DePIN one: with only ~52% of max supply circulating, **unlock-driven dilution** can outrun real query revenue unless adoption of *provable* data scales meaningfully.

## Competitive Position

Space and Time competes with blockchain data/indexing and verifiable-compute providers. Its distinct angle is full **verifiable SQL over a managed warehouse** — not just availability of data, but cryptographic proof of query correctness — plus enterprise positioning via Microsoft M12 and [[chainlink|Chainlink]].

| Project | Token | Category | Verifiable? | Distinct angle |
|---|---|---|---|---|
| **Space and Time** | SXT | Verifiable data warehouse | **Yes (Proof of SQL)** | Provable SQL results consumable on-chain; M12 + Chainlink |
| **[[the-graph\|The Graph]]** | GRT | Blockchain indexing (subgraphs) | No (data availability, not proof) | Largest decentralized indexing network; broad subgraph ecosystem |
| **[[chainlink\|Chainlink]]** | LINK | Oracle / data services | Partial (DON consensus, not ZK-of-query) | Dominant oracle; also a SxT *partner* (delivery rail) |
| **Lagrange** | LA | ZK coprocessor | Yes (ZK proofs over chain state) | Proves computations over historical chain data |

SxT's edge is that it offers *provable* analytics where The Graph offers *available* data, and a managed SQL warehouse where ZK-coprocessors (Lagrange, Axiom, Brevis) typically prove narrower computations. The risk is that "provable" is a narrower market than "available," and that incumbents — including its own partner Chainlink — could absorb the use case.

## How & Where It Trades

- **Spot venues.** SXT is comparatively well-listed for its size: Binance, Kraken, Bitget, KuCoin, and Crypto.com on the CEX side, plus Uniswap V3 on [[ethereum|Ethereum]] (see Exchange Listings). The Binance listing gives it materially deeper liquidity than most sub-$25M peers.
- **Liquidity.** The Apr-2026 snapshot showed ~$5.47M 24h volume against a ~$20.7M cap — a high volume/cap ratio reflecting active CEX trading rather than a dormant token.
- **Float / unlock overhang.** With ~52% of max supply circulating (MC/FDV ≈ 0.52), scheduled unlocks are a structural dilution headwind — the gap between cap (~$20.7M) and FDV (~$82M) prices in significant future supply.

## Narrative, Category & Catalysts

SXT sits in the **ZK / verifiable-compute** and **on-chain-data infrastructure** narratives, with an unusually concrete enterprise angle (Microsoft M12 backing, Chainlink integration). Use cases that could drive demand: tokenized real-world-asset (RWA) data, stablecoin-reserve attestation, institutional/DeFi analytics, and feeding verifiable data to [[artificial-intelligence|AI]] agents. Catalysts: production deployments consuming Proof of SQL at scale, RWA/stablecoin attestation adoption, deeper Chainlink integration, and broad ZK-narrative rotations. The de-rating risk is that *provable* data remains a niche relative to raw indexing, leaving query revenue thin against the unlock schedule.

## History & Timeline

- **2022** — Space and Time founded; positions as a decentralized, verifiable data warehouse.
- **2025-05-08** — SXT all-time high of **$0.1621**, shortly after token launch.
- **2026-03-31** — SXT all-time low of **$0.0142**.
- **2026-06-21** — Trades ~$0.00797 (~95% below ATH); +1.24% 24h / -5.60% 7d against an Extreme-Fear market (per snapshot below).

## Risks

- **Demand realization** — verifiable databases are a young category; adoption depends on developers needing *provable* (not merely available) data, which is a narrower market than raw indexing.
- **ZK / cryptographic risk** — Proof of SQL is novel cryptography; a soundness bug would undermine the entire trust model.
- **Competition from incumbents** — [[chainlink|Chainlink]] (also a partner) and [[the-graph|The Graph]] are well-funded and could absorb the use case.
- **Tokenomics / dilution** — large gap between market cap (~$20.7M) and FDV (~$82M), with roughly half of supply still to unlock.
- **Liquidity / size** — small-cap with elevated volatility and slippage, despite better-than-peer CEX coverage.

## Trading Playbook

> *Educational context, not financial advice. SXT is a thin, high-beta small-cap.*

- **Regime awareness.** In the current **Established Bear Market / Extreme Fear** tape (Fear & Greed 21, BTC ~16% below its 200-day MA as of 2026-06-22), ZK/data-infra small-caps trade as high-beta narrative plays — outperforming in ZK risk-on rotations and bleeding in risk-off.
- **Liquidity is an advantage here.** Unlike most peers in this batch, the Binance listing and ~$5M 24h volume mean SXT is comparatively tradeable, with tighter spreads — though still small enough that size moves price.
- **Mind the unlocks.** The ~0.52 MC/FDV ratio means unlock events are a recurring overhang; align entries/exits with the emission calendar rather than ignoring it.
- **Bull case is fundamental.** The thesis requires *paid, provable* query volume — track production usage of Proof of SQL and RWA/attestation adoption, not just price and narrative.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe6bfd33f52d82ccb5b37e16d3dd81f9ffdabb195` |
| Base | `0xa2c22252cdc8b7cddee1b0b2e242818509fcf7b8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SXT/USDT | N/A |
| Kraken | SXT/USD | N/A |
| Bitget | SXT/USDT | N/A |
| KuCoin | SXT/USDT | N/A |
| Crypto.com Exchange | SXT/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XDAC17F958D2EE523A2206206994597C13D831EC7/0XE6BFD33F52D82CCB5B37E16D3DD81F9FFDABB195 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.spaceandtime.io](https://www.spaceandtime.io) |
| **Twitter** | [@spaceandtime](https://twitter.com/spaceandtime) |
| **Telegram** | [spaceandtimedb](https://t.me/spaceandtimedb) (8,654 members) |
| **Discord** | [https://discord.gg/spaceandtimedb](https://discord.gg/spaceandtimedb) |
| **GitHub** | [https://github.com/spaceandtimelabs/](https://github.com/spaceandtimelabs/) |
| **Whitepaper** | [https://spaceandtime.io/whitepaper](https://spaceandtime.io/whitepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.47M (Apr-2026 snapshot) |
| **Market Cap Rank** | #810 |
| **Current Price** | $0.00796704 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[zero-knowledge-proof]]
- [[chainlink]]
- [[the-graph]]
- [[depin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.
