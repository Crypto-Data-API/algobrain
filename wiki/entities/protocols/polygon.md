---
title: "Polygon"
type: entity
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [crypto, ethereum, defi]
entity_type: protocol
founded: 2017
website: "https://polygon.technology"
aliases: ["MATIC", "POL", "Polygon-network", "Polygon PoS", "Matic Network"]
related: ["[[ethereum]]", "[[arbitrum]]", "[[defi]]", "[[blockchain]]", "[[polymarket]]", "[[aave]]", "[[uniswap]]", "[[polygon-ecosystem-token]]"]
---

# Polygon

**Polygon** is an [[ethereum|Ethereum]] scaling ecosystem, originally launched as Matic Network in 2017, that provides lower-cost, higher-throughput alternatives to Ethereum mainnet. Its native token **POL** (formerly MATIC; migration completed on mainnet in late 2024) is used for gas fees, staking, and governance. After years of pursuing multiple scaling tracks, Polygon decisively pivoted in 2025 toward **Polygon PoS as a payments and real-world-asset (RWA) chain** plus the **Agglayer** cross-chain settlement layer, announcing the sunset of its zkEVM rollup by 2026.

---

## Key Features

| Feature | Detail |
|---|---|
| **Primary Chain** | Polygon PoS -- an EVM-compatible proof-of-stake chain |
| **Token** | POL (migrated from MATIC; live on mainnet by October 2024) -- gas, staking, governance |
| **Finality** | ~5 seconds since Heimdall v2 (July 2025), down from 1-2 minutes |
| **Throughput** | ~1,000+ TPS after Bhilai hardfork; ~5,000 TPS capacity after Rio (Oct 2025); Gigagas roadmap targets 100,000 TPS |
| **Transaction Costs** | Fractions of a cent on Polygon PoS |
| **Settlement Layer** | Agglayer -- chain-agnostic cross-chain settlement (v0.3 live 2025-2026) |
| **Major Protocols** | [[aave]], [[uniswap]], QuickSwap, [[polymarket|Polymarket]] |
| **Partnerships** | Starbucks, Nike, Reddit (NFT avatars); stablecoin payment rails |

---

## Strategic Pivot: 2024-2026

- **POL migration**: the MATIC → POL token migration went live on mainnet by October 2024 ("Polygon 2.0"), making POL the gas/staking token of Polygon PoS and the staking asset for the broader Agglayer ecosystem.
- **zkEVM sunset (announced June 2025)**: Polygon announced it will retire its zkEVM rollup **by 2026**, ending its standalone ZK-rollup effort. Resources were redirected to Polygon PoS (stablecoin payments + RWA) and the Agglayer. POL rebounded ~20% around the strategic-shift news as markets read it as focus rather than retreat.
- **Heimdall v2 (July 2025)**: consensus-layer overhaul (Tendermint → CometBFT v0.38) cutting finality from 1-2 minutes to **~5 seconds** — critical for payment use-cases.
- **Bhilai hardfork (2025)**: raised throughput past 1,000 TPS and enabled gasless-UX features (EIP-7702-style account abstraction).
- **Rio upgrade (mainnet October 2025)**: block gas limit 45M → 60M, new block-producer model, stateless verification — positioning PoS for ~5,000 TPS, the first milestone of the **Gigagas roadmap to 100,000 TPS**.
- **Agglayer**: v0.3 live with an execution-proof mode; Polygon PoS connection to Agglayer scheduled; X Layer (OKX) among connected chains. The Agglayer Breakout Program (active 2026) incubates new chains that airdrop to POL stakers.
- **Scale (June 2026, per Polygon)**: ~**$2.4 trillion** cumulative stablecoin settlement volume, **6.4 billion transactions**, **159 million unique wallets**, 99.99% uptime over five years.

---

## Polygon PoS vs zkEVM (historical)

- **Polygon PoS** is the original chain -- fast, cheap, widely adopted, but security is maintained by its own validator set rather than Ethereum directly
- **Polygon zkEVM** was a zero-knowledge rollup posting proofs to Ethereum with stronger security guarantees at the cost of higher fees; it never attracted significant TVL and is being **wound down by 2026**
- The "Polygon 2.0" ZK-centric vision was superseded in 2025 by the payments/RWA + Agglayer strategy

---

## Trading Relevance

- Polygon PoS is one of the most used chains for retail DeFi and stablecoin payment activity due to near-zero gas costs
- POL trades as a proxy for the **stablecoin-payments and RWA-settlement narrative** (post-pivot), no longer primarily an "Ethereum L2 beta" — a regime change relative to MATIC's historical trading pattern
- [[polymarket|Polymarket]], the leading prediction market, operates on Polygon, drawing attention and flow during major events (elections, macro); it is the single most important application driving Polygon mindshare
- POL staking yields are augmented by **Agglayer Breakout Program airdrops** to stakers — a carry component when valuing POL
- Polygon competes with [[arbitrum]], Base, and other L2s for DeFi TVL and with Tron/Solana for stablecoin payment volume
- Upgrade events (Heimdall v2, Rio, zkEVM sunset) have been tradeable catalysts for POL

---

## Related

- [[ethereum]] -- The L1 that Polygon scales and settles to
- [[arbitrum]] -- Primary L2 competitor
- [[polymarket]] -- Flagship application on Polygon
- [[polygon-ecosystem-token]] -- POL token market page
- [[defi]] -- DeFi protocols deployed on Polygon
- [[aave]] -- Major lending protocol on Polygon

---

## Sources

- Polygon blog — "Polygon Rewind" (2026-06-04; POL mainnet timeline, Agglayer milestones): https://polygon.technology/blog/polygon-rewind
- Polygon blog — "Polygon's Gigagas Roadmap to 100k TPS": https://polygon.technology/blog/polygons-gigagas-roadmap-to-100k-tps-move-your-money-faster-across-the-globe
- Polygon blog — "2025 in Review: A Year of Real Payments Usage on Polygon": https://polygon.technology/blog/2025-in-review-a-year-of-real-payments-usage-on-polygon
- CryptoRank — "Polygon to sunset zkEVM, bets future on cross-chain settlement and stablecoin payments" (June 2025): https://cryptorank.io/news/feed/c2e0b-polygon-to-sunset-zkevm-bets-future-on-cross-chain-settlement-and-stablecoin-payments
- Stakin — "Understanding Polygon's Bhilai and Heimdall Upgrades": https://stakin.com/blog/understanding-polygons-bhilai-and-heimdall-upgrades-finality-1000-tps-and-gasless-ux
- EtherWorld — "From Rio to GigaGas: Polygon's Path to 5,000 TPS & Beyond" (2025-09-17): https://etherworld.co/2025/09/17/from-rio-to-gigagas-polygons-path-to-5-000-tps-beyond/
- Messari — "State of Polygon Q3 2025": https://messari.io/report/state-of-polygon-q3-2025
- Agglayer — "Agglayer v0.3 is live": https://www.agglayer.dev/blogs/agglayer-v0-3-is-live
- BeInCrypto — Polygon cumulative settlement/transaction stats (June 2026): https://beincrypto.com/how-polygon-agglayer-held-through-defi-worst-week-since-ftx/
- Web verification via Perplexity/WebSearch, 2026-06-10.
