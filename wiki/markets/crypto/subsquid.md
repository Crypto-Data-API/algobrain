---
title: "SQD (Subsquid)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["SQD", "Subsquid"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sqd.dev"
related: ["[[arbitrum]]", "[[artificial-intelligence]]", "[[base]]", "[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[the-graph]]"]
---

# SQD (Subsquid)

**SQD** (formerly Subsquid, ticker **SQD**) is the token of the SQD Network, a decentralized **on-chain data lake and query engine** for blockchain indexing and analytics. It gives developers performant, permissionless access to historical and real-time chain data — the layer that powers dApp backends, explorers, and analytics without relying on centralized RPC/API providers (the role [[the-graph|The Graph]] plays for many teams). The token settles on [[arbitrum|Arbitrum One]], with bridged deployments on [[base|Base]] and BNB Chain.

SQD's pitch is a decentralized, cost-efficient alternative to monolithic indexing frameworks and to centralized infrastructure firms (large RPC and API providers). Its modular "data lake" architecture is designed for scalability across many chains, and it positions itself increasingly around AI/big-data access to on-chain data.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | SQD |
| **Price** | $0.04384954 |
| **Market Cap** | $47.70M |
| **Market Cap Rank** | #471 |
| **24h Volume** | $4.05M |
| **24h Change** | -4.34% |
| **7d Change** | +7.11% |
| **Fully Diluted Valuation** | ~$58.63M (at 1.337B max supply) |
| **Market Cap / FDV** | ~0.81 |
| **All-Time High** | $0.284777 |
| **All-Time Low** | $0.0228513 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Backdrop: snapshot taken during an **Established Bear Market** with the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (Extreme Fear)**. SQD bucked the tape with **+7.1% over 7 days** despite a red day (-4.3%), on moderate ~$4.1M volume. It trades ~85% below its ATH but ~92% above its ATL.

---

## Technology & Protocol

SQD reframes blockchain indexing as a **decentralized data-lake problem** rather than a per-dApp indexing job:

- **Workers / data lake** — a permissionless set of node operators ("workers") store compressed, columnar slices of historical chain data across many networks, forming a distributed data lake.
- **Query engine / portal** — developers (and increasingly AI pipelines) query that lake through a gateway; queries are routed to the workers holding the relevant data and returned far faster and cheaper than re-scanning archive RPC nodes.
- **Squid SDK** — a developer framework for building custom indexers ("squids") that transform raw chain data into application-ready APIs, deployable to the SQD Network or self-hosted.
- **Two-sided market** — data consumers pay (in SQD) to query; workers stake SQD and earn rewards for serving data reliably.

This contrasts with both monolithic indexing frameworks and centralized incumbents (Alchemy, QuickNode, Infura), and overlaps with [[the-graph|The Graph]] in the decentralized-indexing market.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.09B SQD |
| **Total Supply** | ~1.337B SQD |
| **Max Supply** | 1.337B SQD |
| **Circulating / Max** | ~81.4% |
| **Market Cap / FDV** | ~0.81 |

Max supply is fixed at the symbolic **1,337,000,000 SQD** ("1337"). With ~81% already circulating, SQD has one of the **lower remaining-emission overhangs** in this cohort — MC/FDV of ~0.81 means relatively little forward dilution compared to peers like [[zama]] (~0.20) or [[kaito]] (~0.24). Token utility centers on the network's two-sided market: data consumers pay (in SQD) to query data, while node operators stake SQD and earn rewards for serving it, plus governance. The high circulating ratio makes SQD's valuation a more direct read on current demand than on future unlock schedules.

---

## Market Structure & Derivatives

- **Spot venues:** SQD trades on CEXs including KuCoin and Crypto.com, with DEX liquidity on [[arbitrum|Arbitrum One]], [[base|Base]], and BNB Chain. It came to market via a CoinList launchpad. Centralized depth is moderate.
- **Derivatives / perps:** SQD is **not** a major perpetual-futures listing — there is no liquid [[hyperliquid|Hyperliquid]] or top-CEX perp with meaningful open interest, so funding/OI data are not available. Exposure is effectively spot-only.
- **Liquidity note:** at rank #471 with ~$4.1M daily volume, treat it as a small-cap with real slippage on size.

---

## Use Case, Narrative & Category

SQD sits in the **on-chain-data / indexing infrastructure** category, overlapping with the [[artificial-intelligence|Artificial Intelligence (AI)]], Big Data, and Analytics narratives, and with Arbitrum/Base/BNB ecosystems. Its closest comparable is [[the-graph|The Graph (GRT)]] in the decentralized-indexing market.

The thesis: every dApp, wallet, explorer, and analytics product needs fast access to historical and live blockchain data, which is expensive and centralizing when served by big RPC/API vendors. SQD decentralizes that data layer with a "data lake + query engine" design, charging in token and rewarding operators for serving queries. The newer angle is feeding **AI agents and analytics** with structured on-chain data. Unlike hardware-[[depin|DePIN]], the "physical" contribution is compute/storage for indexing; the economic loop is query demand subsidizing the operator set.

---

## Valuation Framing

- **Query-revenue multiple** — value SQD on annualized, token-denominated query fees flowing to workers; the bull case requires developer usage to convert into paid queries at scale.
- **GRT relative comp** — as the #2-ish decentralized indexing name, SQD is often valued at a discount to [[the-graph|The Graph]]'s network value; convergence/divergence of that ratio is a key trade.
- **Low-float-adjusted read** — uniquely in this cohort, SQD's ~81% circulating ratio means valuation reflects current demand more than future dilution, so it is a cleaner read on fundamentals (for better or worse) than its low-float peers.

---

## Peer Comparison

| Token | Category | Mkt Cap | Rank | MC/FDV | 7d | Note |
|---|---|---|---|---|---|---|
| **SQD** | Data indexing / data lake | $48M | #471 | 0.81 | +7.1% | Highest float in cohort; spot-only |
| [[the-graph]] (GRT) | Data indexing | — | — | — | — | Closest comparable; subgraph incumbent |
| [[arkham]] (ARKM) | On-chain intel + CEX | $86M | #297 | 0.66 | +1.1% | Forensics, not raw indexing |
| [[zama]] (ZAMA) | FHE / confidential infra | $76M | #327 | 0.20 | +7.3% | Privacy infra; very low float |

---

## Notable History

- **All-Time High:** $0.284777 — current price is ~85% below ATH.
- **All-Time Low:** $0.0228513 — current price is ~92% above ATL.
- SQD rebranded from "Subsquid" to "SQD" alongside its network and token evolution. Like most 2024-2025-era infra tokens it is deep in drawdown, but its high circulating ratio means much of the supply-driven repricing is already behind it relative to lower-float peers.

---

## Risks

- **Competition risk:** decentralized indexing is contested ([[the-graph|The Graph]]) and centralized RPC/API providers (Alchemy, QuickNode, Infura) compete on reliability and ease.
- **Demand-monetization risk:** developer adoption must convert into paid, token-denominated queries to sustain operator rewards.
- **Drawdown/momentum:** ~85% below ATH; the +7% week is encouraging but small-cap rallies are fragile in Extreme Fear.
- **Liquidity risk:** small-cap with ~$4.1M daily volume and no perp market — limited venues to hedge or exit size.
- **Remaining emissions:** ~19% of supply still to unlock; minor but non-zero overhang.
- **Macro/sentiment risk:** Established Bear Market with Extreme Fear (F&G 23) is a headwind for infra/AI-narrative tokens.

---

## Related

- [[arbitrum]] — SQD's settlement chain
- [[base]] — bridged deployment
- [[the-graph]] — closest decentralized-indexing comparable
- [[depin]] — adjacent infrastructure-network narrative
- [[artificial-intelligence]] — AI/big-data data access angle
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## See Also

- [[crypto-markets]]
- [[arbitrum]]

---
