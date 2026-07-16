---
title: "NEAR Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto]
aliases: ["NEAR"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized (NEAR Foundation: Switzerland)"
website: "https://near.org/"
related: ["[[ai-agent-tokens]]", "[[artificial-intelligence]]", "[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[internet-computer]]", "[[layer-1-blockchains]]", "[[narrative-trading]]", "[[proof-of-stake]]", "[[sharding]]", "[[solana]]"]
---

# NEAR Protocol

**NEAR Protocol** (NEAR) is a sharded, [[proof-of-stake]] Layer 1 blockchain that has repositioned itself as "the blockchain for AI", combining chain abstraction, NEAR Intents (goal-driven cross-chain execution) and AI-agent infrastructure. For traders it is one of the primary large-cap vehicles for the AI-crypto narrative, with pending US spot-ETF filings and a 2025 halving of token inflation as live catalysts. Founded by Alexander Skidanov and Illia Polosukhin (a co-author of the "Attention Is All You Need" transformer paper), mainnet launched in 2020.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #34 |
| **Market Cap** | $2.78B |
| **Current Price** | $2.14 |
| **24h Volume** | $253.45M |
| **24h Change** | +0.93% |
| **7d Change** | +5.17% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: the snapshot lands inside a broad **extreme fear** regime ([[fear-and-greed-index|Fear & Greed]] = 22) and an "Established [[bear-market|Bear Market]]" backdrop. NEAR is mildly green on both the day (+0.93%) and the week (+5.17%), modest relative strength versus a tape where most of the AI/L1 cohort is flat-to-down — consistent with NEAR's role as a liquid expression of the AI-crypto narrative that periodically decouples from broad [[crypto-markets]] beta. Price remains ~89.5% below the January 2022 ATH of $20.44.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NEAR |
| **Market Cap** | $2.78B, rank #34 (2026-06-20) |
| **Sector** | Layer 1 (L1), AI infrastructure, chain abstraction |
| **Supply mechanics** | ~1.30B circulating, fully unlocked; max annual inflation cut from 5% to 2.5% in Q4 2025 ("Halving Upgrade") |
| **Consensus** | [[proof-of-stake|Proof of Stake]] with Nightshade [[sharding]] (9 shards, dynamic resharding) |
| **Website** | [https://near.org/](https://near.org/) |

---

## Overview

NEAR Protocol is a high-performance, AI-native platform built to power decentralized applications and intelligent agents. It provides infrastructure for AI to transact and operate across Web2 and Web3, combining three core elements: User-Owned AI; Intents and Chain Abstraction, which eliminate blockchain complexity for goal-driven transactions across chains; and a sharded blockchain architecture delivering low-cost, high-throughput execution. NEAR Intents shifts UX away from manual coordination — users describe what they want and the protocol routes execution across chains automatically.

---

## Technology & Consensus

NEAR's defining technical primitive is **Nightshade sharding** — an approach to [[sharding]] in which the blockchain is conceptually a single chain whose state and transaction processing are split across multiple shards, each maintained by a subset of validators. Rather than running separate shard chains, Nightshade has all validators produce a single block per slot containing "chunks" (one chunk per shard); a validator only needs to process the chunks for the shards it tracks, while the aggregate block records the whole network state.

| Component | Detail |
|---|---|
| **Consensus** | Thresholded Proof-of-Stake (Doomslug for near-instant finality, plus a Nightshade BFT finality layer) |
| **Sharding model** | Nightshade — single logical chain, state split into shards/chunks; dynamic resharding adds/removes shards with demand |
| **Shards (2026)** | Expanded from 6 to 9 in 2025 (+50% throughput); a public test using live core code hit ~1 million TPS |
| **Smart contracts** | WebAssembly (Wasm) runtime; contracts written in Rust and JavaScript/TypeScript |
| **Account model** | Human-readable named accounts (e.g. `alice.near`), access keys, account abstraction by design |
| **Finality** | Sub-second optimistic finality via Doomslug; full BFT finality in a few blocks |

**Chain abstraction & NEAR Intents.** NEAR's higher-layer differentiation is *chain abstraction*: chain-signatures (MPC-based) let NEAR accounts control addresses on other chains (Bitcoin, Ethereum, Solana), and **NEAR Intents** turn user goals ("swap X for Y at best price across any chain") into solver-routed cross-chain execution. This positions NEAR as coordination infrastructure rather than just another execution L1 — relevant for the AI-agent thesis where autonomous agents need to transact across many chains.

**Confidential Intents (March 2026)** added optional privacy for cross-chain execution via private shards and TEEs, shielding agent transactions from front-running bots — a structural overlap with the [[privacy-coins]] theme applied to agent workflows rather than payments.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 1,298,708,855 NEAR |
| **Total Supply** | 1,298,708,862 NEAR |
| **Max Supply** | None (uncapped; inflation-limited) |
| **Market Cap / FDV Ratio** | ~1.00 (fully unlocked) |

- **Inflation model**: NEAR uses a fixed *target* annual inflation that funds staking rewards and protocol treasury. The **Halving Upgrade (Q4 2025)** cut the maximum annual inflation ceiling from **5% to 2.5%**, materially reducing structural sell pressure given the token is effectively fully unlocked (circulating ≈ total).
- **Staking**: NEAR is staked to validators to secure the network and earn a share of issuance; staking yield scales inversely with total stake participation.
- **Fee burn**: a portion of transaction fees is burned (EIP-1559-style), providing a mild deflationary offset that grows with usage; high Intents/agent throughput would increase burn.
- **No vesting cliffs**: with circulating ≈ total supply, NEAR carries **no scheduled unlock overhang** — a structural contrast with [[sui|Sui]] (MC/FDV ~0.40) and many newer L1s.

---

## Ecosystem & Use Cases

- **AI agents & user-owned AI** — NEAR AI Cloud and Private Chat (2026) deliver cryptographically protected, user-owned AI inference; May 2026 added automatic PII anonymization for AI prompts. This anchors NEAR's "blockchain for AI" branding.
- **Chain abstraction / Intents** — the flagship 2026 product push; Intents aims to become a leading on-chain transaction venue by abstracting which chain a trade settles on.
- **DeFi** — NEAR hosts a mid-sized DeFi ecosystem (Ref Finance, Burrow lending) plus the **Aurora** EVM layer for Ethereum-compatible apps.
- **Consumer / social** — historically promoted for low-fee consumer apps; named-account UX lowers onboarding friction versus hex addresses.
- **Cross-chain hub** — chain-signatures let NEAR accounts custody and act on Bitcoin, Ethereum and Solana addresses, positioning NEAR as a coordination layer rather than a walled garden.

---

## Market Structure & Derivatives

- **Spot venues**: top-tier liquidity — [[binance|Binance]] (NEAR/USDT), [[kraken|Kraken]], Upbit (NEAR/KRW, a Korean-flow tell), [[coinbase|Coinbase]], Bitget, KuCoin. ~$253M reported 24h volume (2026-06-20).
- **Perps / funding / OI**: perpetuals on [[hyperliquid|Hyperliquid]] (NEAR-PERP) and all major futures venues (Binance, Bybit, OKX). As a high-beta AI/L1 name, NEAR perp funding tends to swing positive during AI-narrative bids and flip negative in risk-off legs of the bear market; open interest concentrates around ETF-decision and roadmap-announcement dates.
- **ETF pathway**: Bitwise filed for a spot NEAR ETF in May 2025; Grayscale filed for a spot NEAR ETF (GSNR) on 20 January 2026, with an SEC decision window pointing to ~September 2026. Unlike [[privacy-coins]] such as [[monero|Monero]] and [[zcash|Zcash]], NEAR has a credible US ETF path, which adds a discrete institutional-flow catalyst.

---

## Trading Playbook

- **Narrative basket**: core member of the **AI L1 / AI-agent basket** (with [[internet-computer|ICP]], TAO, FET/ASI, RENDER); also trades with the broader L1 basket. When the AI-crypto narrative bids, NEAR is one of the most liquid large-cap expressions — a natural long leg in [[narrative-trading]] pairs and a candidate short leg against stronger AI names on rotation. See [[ai-agent-tokens]].
- **Catalyst calendar**: SEC decisions on Bitwise/Grayscale spot ETFs (~Sept 2026), v2.13 dynamic resharding launch (June 2026), Intents volume growth, AI product announcements. These are discrete, schedulable events suited to event-driven positioning.
- **Structural tailwind**: fully unlocked supply means no vesting-cliff overhangs; post-halving inflation (2.5%) reduces structural sell pressure from staking emissions — a cleaner supply profile than unlock-heavy peers, useful in a bear tape where supply overhang dominates.
- **Regime note (2026-06-20)**: in an Established Bear Market with [[fear-and-greed-index|F&G]] at 22, NEAR's mild green is relative strength, not a trend signal — size accordingly and respect the ~89% drawdown from ATH as evidence of how violent the downside can be.

---

## History

- **2018** — Project founded by Alexander Skidanov and Illia Polosukhin (transformer-paper co-author); NEAR Foundation established in Switzerland.
- **2020** — Mainnet launch; phased decentralization ("MainNet: Community-Governed" phase).
- **2021–2022** — Bull-market run to an ATH of **$20.44 (2022-01-16)**; Aurora EVM and Octopus appchains expand the ecosystem.
- **2022–2023** — Bear market drawdown; the NEAR ecosystem fund (Proximity, etc.) episodes and broad alt-L1 derating.
- **2024–2025** — Strategic pivot to the **"blockchain for AI"** narrative; chain abstraction and NEAR Intents become the flagship roadmap.
- **2025** — Sharding scaled from 6 to 9 shards (+50% throughput); 1M-TPS public test; **Halving Upgrade** cuts max inflation from 5% to 2.5%.
- **Jan 2026** — Grayscale files for a spot NEAR ETF (GSNR).
- **2026** — Confidential Intents (Mar), NEAR AI Cloud / Private Chat, PII anonymization (May), v2.13 dynamic resharding + post-quantum signing (June).

---

## Competitive Positioning

| Project | Consensus / scaling | Supply model | Narrative niche | MC rank (2026-06-20) |
|---|---|---|---|---|
| **NEAR** | PoS + Nightshade sharding | Uncapped, 2.5% inflation cap, fully unlocked | AI agents + chain abstraction | #34 |
| [[internet-computer|ICP]] | Chain-key crypto, canisters | Uncapped, inflationary | AI / decentralized cloud | #59 |
| [[solana|Solana]] | PoH + PoS, monolithic | Uncapped, disinflationary | High-throughput L1, consumer/DeFi | top 10 |
| [[sui|Sui]] | Move, object model, PoS | 10B cap, MC/FDV ~0.40 (unlock overhang) | High-throughput L1, Move | #32 |
| [[aptos|Aptos]] | Move, BFT (AptosBFT) | Uncapped, unlock schedule | High-throughput L1, Move | mid-cap |

NEAR's edge vs. its AI-narrative peer [[internet-computer|ICP]] is a cleaner, fully-unlocked supply and a concrete ETF path; vs. monolithic L1s like [[solana|Solana]] it offers sharded horizontal scaling and chain abstraction, at the cost of a smaller DeFi/consumer ecosystem.

---

## Regulatory

- **Asset classification**: NEAR is a utility/staking token of a permissionless L1; the live ETF filings (Bitwise, Grayscale GSNR) imply issuers expect a commodity-style treatment, with SEC decisions pending ~September 2026. The US **CLARITY Act** process (market-structure legislation) is a sector-wide tailwind for utility-classified L1 tokens.
- **Staking-in-ETF question**: as with [[sui|Sui]] and other staking L1s, whether US spot ETFs may pass through staking rewards is an open regulatory item that affects effective yield and inflow demand.
- **Privacy features**: Confidential Intents introduces optional privacy at the agent-transaction layer; this is far narrower than [[monero|Monero]]/[[zcash|Zcash]]-style default privacy and is not expected to attract the same delisting risk, but it is a watch-item if privacy regulation broadens.

---

## Risks

- **Narrative dependence** — NEAR trades heavily on the AI-crypto theme; if the AI narrative cools, NEAR can derate faster than fundamentals-driven peers.
- **Competition** — crowded AI/L1 field ([[internet-computer|ICP]], TAO, [[solana|Solana]]) plus Move-chains ([[sui|Sui]], [[aptos|Aptos]]) competing for the same throughput-app developers.
- **Execution risk** — Intents/chain-abstraction adoption is still proving out; the value-capture link between Intents volume and NEAR token demand is not yet fully established.
- **Inflation** — uncapped supply with 2.5% inflation requires usage-driven fee burn to offset emissions; in low-usage regimes the token still inflates.
- **Macro/regime** — high-beta large-cap alt in an Established Bear Market; ~89% off ATH demonstrates downside severity.
- **ETF path is not guaranteed** — an SEC denial or delay (~Sept 2026) would remove a key institutional-flow catalyst.

---

## Developer Activity (April 2026 snapshot)

| Metric | Value |
|---|---|
| **GitHub Stars** | 2,586 |
| **GitHub Forks** | 771 |
| **Commits (4 weeks)** | 119 |
| **Contributors** | 211 |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://near.org/](https://near.org/) |
| **Twitter** | [@nearprotocol](https://twitter.com/nearprotocol) |
| **GitHub** | [https://github.com/nearprotocol/nearcore](https://github.com/nearprotocol/nearcore) |
| **Whitepaper** | [https://near.org/papers/the-official-near-white-paper/](https://near.org/papers/the-official-near-white-paper/) |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[internet-computer]] — AI/compute-narrative peer
- [[solana]] — monolithic high-throughput L1 peer
- [[sui]], [[aptos]] — Move-language L1 peers
- [[ai-agent-tokens]]
- [[artificial-intelligence]]
- [[hyperliquid]]
- [[bitcoin-etfs]]
- [[narrative-trading]]
- [[proof-of-stake]], [[sharding]], [[layer-1-blockchains]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- cryptodataapi.com / CoinGecko markets snapshot, 2026-06-20 (current Market Data block)
- [NEAR Protocol Outlines 2026 Roadmap — MEXC News](https://www.mexc.co/news/391794)
- [NEAR Protocol Jumps 28% on Privacy, AI, and Scaling Upgrades — Decrypt](https://decrypt.co/368737/near-protocol-jumps-28-on-privacy-ai-and-scaling-upgrades)
- [NEAR Protocol Overview in 2026 — ChangeNOW](https://changenow.io/blog/near-protocol-overview)
- [CoinMarketCap — NEAR Protocol](https://coinmarketcap.com/currencies/near-protocol/)
- [CoinGecko — NEAR Protocol](https://www.coingecko.com/en/coins/near)
- Web search verification, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.30B NEAR |
| **Total Supply** | 1.30B NEAR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $2.64B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $20.44 (2022-01-16) |
| **Current vs ATH** | -90.10% |
| **All-Time Low** | $0.5268 (2020-11-04) |
| **Current vs ATL** | +284.22% |
| **24h Change** | -0.86% |
| **7d Change** | +5.76% |
| **30d Change** | -18.84% |
| **1y Change** | -24.48% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | NEAR/USDT | N/A |
| Kraken | NEAR/USD | N/A |
| Bitget | NEAR/USDT | N/A |
| KuCoin | NEAR/USDT | N/A |
| Crypto.com Exchange | NEAR/USD | N/A |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 2,590 |
| **GitHub Forks** | 781 |
| **Commits (4 weeks)** | 103 |
| **Pull Requests Merged** | 8,632 |
| **Contributors** | 213 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $185.65M |
| **Market Cap Rank** | #34 |
| **24h Range** | $2.01 — $2.10 |
| **CoinGecko Sentiment** | 92% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
