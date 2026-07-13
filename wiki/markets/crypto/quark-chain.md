---
title: "QuarkChain"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, sharding]
aliases: ["QKC", "Quark Chain"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://quarkchain.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[sharding]]"]
---

# QuarkChain

**QuarkChain** (QKC) is a sharded, high-throughput [[layer-1]] blockchain designed around a two-layer architecture: many parallel transaction-processing **shards** sit beneath a single **root chain** that finalizes and secures them. Its founding pitch (2017–2018) was that horizontal scaling via [[sharding]] could let the network process very high transaction volumes without sacrificing decentralization. The QKC token originated on QuarkChain's mainnet and is widely traded as an ERC-20 representation on [[ethereum]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* QKC trades at **$0.00221887**, ranked **#924** by market capitalization (~**$16.08M**), up **+2.98%** over 24h but down a sharp **-11.04%** over the past 7 days — a notable underperformance against an already weak market (Fear & Greed Index 22, "Extreme Fear"). The token remains ~99% below its June 2018 ICO-era peak near $0.34.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QKC |
| **Market Cap Rank** | #924 |
| **Market Cap** | ~$16.08M |
| **Current Price** | $0.00221887 |
| **24h Change** | +2.98% |
| **7d Change** | -11.04% (sharp drop) |
| **Architecture** | Sharded two-layer L1 (shards + root chain) |
| **Categories** | Infrastructure, Ethereum Ecosystem, Energi Ecosystem |
| **Website** | [https://quarkchain.io/](https://quarkchain.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

QuarkChain is a [[layer-1]] blockchain whose central design goal is scalability through [[sharding]]. The project, which began research in 2017 and published its whitepaper in early 2018, argued that monolithic chains face a hard ceiling on throughput and that splitting the ledger into many parallel shards — each processing its own subset of transactions — is the path to internet-scale capacity. The team historically promoted very high theoretical throughput targets (on the order of "1 million+ TPS"); such figures are marketing/architectural targets rather than verified sustained mainnet performance, and should be treated qualitatively.

QuarkChain's model emphasizes commodity hardware: instead of requiring expensive "super-full nodes," operators can run multiple cheaper nodes that together form a cluster acting as a super-full node, which is meant to keep participation accessible as throughput scales.

---

## Architecture and Consensus

- **Two-layer design** — The first layer is a set of **shards**: independent blockchains that each process transactions and smart contracts in parallel, increasing aggregate throughput as shards are added. The second layer is the **root chain**, which does not process individual transactions but confirms the shards' block headers, providing shared security and a single source of finality across all shards. See [[sharding]].
- **Cluster-based nodes** — Multiple inexpensive nodes can be combined into a cluster that collectively behaves as a full node for the whole network, lowering the hardware cost of participation versus monolithic full nodes.
- **Security model** — The root chain anchors the security of the shards; the design aims to make cross-shard double-spend attacks costly because reorganizing a shard requires overpowering the root chain's accumulated work/security. Historically QuarkChain used a hash-power-based ([[proof-of-work]]-style) security model on its root chain. This is the project's "Boson consensus" framing: each shard can in principle run its own consensus, while the root chain aggregates and finalizes via accumulated hash power.
- **Smart contracts** — QuarkChain supports EVM-style smart contracts on its shards, allowing dApp deployment across the multi-chain structure.
- **Cross-shard transactions** — Native cross-shard transfers let assets and calls move between shards in a single network, with the root chain providing the ordering/finality that makes those transfers safe. This was an early design answer to the problem rollup ecosystems now solve with shared sequencing and bridges.

### How it compares to the modern scaling stack

QuarkChain's 2018-era thesis was **execution sharding** — split the ledger horizontally and process shards in parallel. The industry's center of gravity later moved to a different decomposition: **modular blockchains** that separate execution (rollups), settlement, and **data availability** ([[ethereum]]'s "danksharding" roadmap, plus Celestia/EigenDA-style DA layers). In modern terms, Ethereum chose to shard *data* (so rollups can post cheap proofs) rather than *execution* directly. QuarkChain's native execution-sharding approach is architecturally coherent but competes against a rollup-centric world with vastly more developer mindshare, liquidity, and tooling — a core reason QKC reads as a legacy infrastructure token.

## Token Utility

QKC is the network's native asset, used to pay transaction fees (gas) across shards, to reward block producers/validators that secure the chain, and for cross-shard transfers. A large share of QKC liquidity exists as ERC-20 tokens on [[ethereum]] (and a wrapped form in the Energi ecosystem), so most trading activity occurs off the native chain. As with many sharded L1s, QKC's value accrual depends on real transaction demand across its shards rather than on speculative throughput claims.

---

## Comparison vs Scaling / L1 Peers

QuarkChain belongs to the "high-throughput, sharded/parallel L1" cohort that emerged 2017–2019. It is useful to contrast it with both its contemporaries and the rollup-era designs that displaced the narrative.

| Project | Ticker | Scaling approach | Era | Status vs QKC |
|---|---|---|---|---|
| **QuarkChain** | QKC | Execution sharding (shards + PoW root chain) | 2018 ICO-era | Legacy infra token, minimal recent dev activity |
| **Zilliqa** | ZIL | Network + transaction sharding (not execution-state sharding) | 2017–2019 | Same cohort; larger ecosystem, still active |
| **Harmony** | ONE | Effective Proof-of-Stake with full state sharding | 2019 | Same cohort; suffered a major bridge hack (2022) |
| **NEAR** | NEAR | Nightshade dynamic resharding (PoS) | 2020+ | Newer, better-funded, sustained development |
| **Ethereum (rollup-centric)** | ETH | Data-availability sharding + L2 rollups for execution | 2020s | The winning paradigm; QuarkChain competes against its entire L2 stack |

Takeaway: QuarkChain was an early and technically credible bet on execution sharding, but the cohort that "won" either pivoted (Ethereum to rollups + DA sharding) or out-resourced it (NEAR). QKC's challenge is not architecture — it is mindshare, liquidity, and ongoing development relative to peers.

---

## How & Where QKC Trades

- **Centralized exchanges carry the liquidity.** Unlike many sub-$20M tokens, QKC retains listings on major venues — **Binance (QKC/USDT)**, **Upbit (QKC/KRW)**, **Bitget**, and **KuCoin** — a legacy of its 2018 prominence. Korean-won liquidity via Upbit can make QKC sensitive to Korean retail flow and occasionally drives outsized, idiosyncratic moves versus the broader market.
- **DEX presence.** The bulk of on-chain liquidity is the **ERC-20 representation on [[ethereum]]**, tradeable on Uniswap-class venues, plus a wrapped form in the Energi ecosystem.
- **Derivatives.** QKC has had perpetual/futures listings on some exchanges historically, but open interest is thin; it is not a token where funding rates carry a strong, reliable signal.
- **Trading implications** — Better CEX liquidity than its market cap implies, but still a thin micro-cap: the ~$16M cap and ~$0.4M daily volume mean it can swing double digits on modest flow, and the 7d move into 2026-06-21 (**-11%**) illustrates how it underperforms when liquidity dries up.

---

## Narrative, Category & Catalysts

- **Category** — Legacy ICO-era **Layer-1 / scaling-infrastructure** token. Its narrative window (2018–2019 "sharding will scale crypto") has largely closed in favor of the rollup/modular thesis.
- **Catalysts (scarce)** — A renewed sharding/parallel-execution narrative; a concrete mainnet-usage or partnership milestone; or a broad small-cap "old coin" rotation in a risk-on regime. None is present as of 2026-06-22.
- **Headwind — development cadence.** Public repo activity is low (≈1 commit in the trailing 4 weeks per the snapshot below), reinforcing the "stalled-development" perception that weighs on any infra token.
- **Headwind — regime.** The market is in an Established Bear with Fear & Greed at **21 (Extreme Fear)**; dormant infra tokens with thin catalysts are precisely what bleeds in this environment.

---

## History & Timeline

Only dated, verifiable milestones are listed.

| Date | Event |
|---|---|
| 2017 | QuarkChain research begins; team forms around an execution-sharding scaling thesis |
| 2018 (early) | Whitepaper published; QuarkChain raises in an ICO during the 2018 token boom |
| 2018-06-05 | QKC all-time high of **$0.3388** |
| 2020-03-13 | QKC all-time low of **$0.00137714** (COVID "Black Thursday" crash) |
| 2026-06-21 | QKC ~$0.00222, ~99% below ATH, down 11% on the week into Extreme Fear |

---

## Risks

- **Acute recent weakness** — QKC fell **-11.04% over the trailing 7 days** into 2026-06-21, materially worse than the broad market; low-cap infrastructure tokens can sell off hard on thin liquidity.
- **Stalled-development perception** — QuarkChain is an ICO-era (2018) project; mindshare and developer activity for sharded-L1 narratives have largely shifted to newer designs (rollups, modular DA, and chains like the post-Merge [[ethereum]] roadmap). Catalysts are scarce.
- **Unverified performance claims** — Headline "1M+ TPS" figures are architectural targets; do not treat them as audited mainnet throughput.
- **Small-cap / liquidity risk** — at ~$16M market cap, QKC is thinly traded, with high volatility and slippage on size.
- **Smart-contract / bridge exposure** — the bulk of QKC liquidity is wrapped ERC-20 on [[ethereum]], inheriting bridge and contract risk.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.23B QKC |
| **Total Supply** | 10.00B QKC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.17M |
| **Market Cap / FDV Ratio** | 0.72 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3388 (2018-06-05) |
| **Current vs ATH** | -99.11% |
| **All-Time Low** | $0.00137714 (2020-03-13) |
| **Current vs ATL** | +120.03% |
| **24h Change** | -1.25% |
| **7d Change** | +0.14% |
| **30d Change** | -3.73% |
| **1y Change** | -47.51% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xea26c4ac16d4a5a106820bc8aee85fd0b7b2b664` |
| Energi | `0x02c6c53930b20bced86ddf64007bebcd923e1093` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | QKC/USDT | N/A |
| Upbit | QKC/KRW | N/A |
| Bitget | QKC/USDT | N/A |
| KuCoin | QKC/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://quarkchain.io/](https://quarkchain.io/) |
| **Twitter** | [@Quark_Chain](https://twitter.com/Quark_Chain) |
| **Reddit** | [https://www.reddit.com/r/quarkchainio/](https://www.reddit.com/r/quarkchainio/) |
| **Telegram** | [quarkchainio](https://t.me/quarkchainio) (5,515 members) |
| **Discord** | [https://discord.com/invite/h5rUa4Aq](https://discord.com/invite/h5rUa4Aq) |
| **GitHub** | [https://github.com/QuarkChain/pyquarkchain](https://github.com/QuarkChain/pyquarkchain) |
| **Whitepaper** | [https://quarkchain.io/QUARK%20CHAIN%20Public%20Version%200.3.5.pdf](https://quarkchain.io/QUARK%20CHAIN%20Public%20Version%200.3.5.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 223 |
| **GitHub Forks** | 113 |
| **Commits (4 weeks)** | 1 |
| **Pull Requests Merged** | 656 |
| **Contributors** | 21 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $383,526.00 (2026-04-09 snapshot) |
| **Market Cap Rank** | #924 (2026-06-21) |
| **Last Updated** | 2026-06-21 |
> *Older intraday range/volume figures reflect the 2026-04-09 snapshot and are retained for history; current price/rank/market cap are 2026-06-21 (see Key Facts).*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Playbook (Bear / Extreme-Fear Regime)

> Educational framing only — not investment advice. QKC is a thin, legacy-narrative micro-cap.

- **Regime first.** In an Established Bear with Fear & Greed at 21, a dormant infra token with low development activity has weak fundamental support; the base case is continued drift and underperformance versus majors (as the -11% week into 2026-06-21 showed).
- **Watch the Korean bid.** QKC's Upbit (KRW) listing means Korean retail flow can produce sharp, market-independent spikes; these are mean-reversion setups more often than trend starts. Treat sudden volume bursts on Upbit as a signal, not a fundamental shift.
- **Liquidity is better than peers but still thin.** Despite Tier-1 CEX listings, size carefully; the cap (~$16M) means real impact on larger orders. Use limit orders.
- **Invalidation / risk control.** There is no robust derivatives market to hedge; risk is controlled by position size. Structural support to watch is the 2020 ATL ($0.00138), far below current price.
- **What would change the thesis** — a genuine resurgence in execution-sharding/parallel-L1 narratives during a risk-on phase, or a concrete usage/partnership catalyst. Absent that, QKC trades as a beta-to-altcoin-risk-appetite vehicle, not a fundamentals story.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[sharding]]
- [[proof-of-work]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — initial market-data snapshot
- Market data 2026-06-21: cryptodataapi.com / CoinGecko (price, rank, market cap, 24h/7d change)
- Architecture (two-layer shard/root design, cluster nodes): general market knowledge; no specific wiki source ingested yet.
