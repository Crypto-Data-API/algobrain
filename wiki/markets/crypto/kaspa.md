---
title: "Kaspa"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto]
aliases: ["KAS", "Kaspa BlockDAG"]
entity_type: protocol
founded: 2021
headquarters: "Decentralized"
website: "https://kaspa.org/"
related: ["[[crypto-markets]]", "[[bitcoin]]", "[[hyperliquid]]", "[[monero]]", "[[litecoin]]"]
---

# Kaspa

**Kaspa** (KAS) is a [[proof-of-work|proof-of-work]] Layer 1 that replaces [[bitcoin|Bitcoin's]] linear chain with a **BlockDAG** (GHOSTDAG consensus), allowing parallel blocks and sub-second confirmation while keeping PoW security. Fair-launched in November 2021 with no pre-mine, no pre-sale and no allocations, it is the flagship of the "fair-launch PoW" narrative basket and one of the few large-cap PoW assets created after Bitcoin. For traders it is a mid-cap (top-100) asset with deep CEX coverage and a [[hyperliquid|Hyperliquid]] perp, whose price action is dominated by protocol-upgrade catalysts (Crescendo 2025, Toccata 2026).

---

## Market Data

| Field | Value |
|---|---|
| **Current Price** | $0.03039 |
| **Market Cap** | $835.14M |
| **Market Cap Rank** | #77 |
| **Fully Diluted Valuation** | $835.93M |
| **24h Volume** | $10.28M |
| **24h Range** | $0.02964 — $0.03044 |
| **24h Change** | +1.13% |
| **7d Change** | -3.65% |
| **Circulating Supply** | 27.50B KAS |
| **Total Supply** | 27.52B KAS |
| **Max Supply** | 28.70B KAS |
| **MC / FDV** | 1.00 |
| **All-Time High** | $0.2074 (2024-08-01) — currently -85.34% |
| **All-Time Low** | $0.00017105 (2022-05-26) — currently +17,678.18% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index at **23 (Extreme Fear)** in an **Established Bear Market**. KAS sits ~85% below its August 2024 ATH and lagged over the prior week (-3.65% / 7d) on thin ~$10M/day volume, with the market in a wait-and-see stance ahead of the **Toccata** hard fork.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KAS |
| **Rank tier** | Top 100 (#77 at the 2026-06-20 snapshot) |
| **Consensus** | [[proof-of-work\|Proof-of-work]] BlockDAG (GHOSTDAG); kHeavyHash mining |
| **Block rate** | 10 blocks/sec since the Crescendo hard fork (May 2025), up from 1/sec |
| **Supply mechanics** | Fair launch Nov 2021; no pre-mine; max supply ~28.7B KAS; emission halves yearly via smooth monthly reduction ("chromatic" schedule); ~95.8% of max supply already circulating |
| **Categories** | Layer 1, Proof of Work, Directed Acyclic Graph (DAG), Smart Contract Platform (in progress) |
| **Founders** | Yonatan Sompolinsky & Aviv Zohar (GHOSTDAG/PHANTOM authors) |
| **Website** | [https://kaspa.org/](https://kaspa.org/) |

---

## Overview

Kaspa was fair-launched in November 2021 with no pre-mine, zero pre-sale, and no coin allocations, and is 100 percent community-managed. Kaspa aims to be the world's global sequencer for traditional finance and decentralized crypto markets by utilizing proof-of-work and its BlockDAG consensus protocol, GHOSTDAG.

Being the world's fastest proof-of-work network, Kaspa combines five properties: (1) hard money principles, (2) [[bitcoin|Bitcoin]]'s ethos of security-first fundamentals, (3) decentralization from rapid block rate mining, (4) block speeds faster than any PoW or PoS network, and (5) smart contract development through based-rollups without fragmented liquidity. The Kaspa implementation includes Reachability to query the DAG's topology, block data pruning, SPV proofs, and subnetwork support intended to ease future layer-2 implementation. The underlying GHOSTDAG/PHANTOM protocol is described in the 2018 IACR paper by Yonatan Sompolinsky (a DAG-consensus researcher whose earlier GHOST work is cited in the Ethereum whitepaper) and Aviv Zohar.

---

## Protocol & Technology

Kaspa's core innovation is solving the **PoW throughput trilemma**: classic [[proof-of-work|PoW]] chains ([[bitcoin|Bitcoin]]) must keep block rates low to avoid orphaned/forked blocks, capping throughput. Kaspa removes that ceiling with a BlockDAG.

### BlockDAG vs blockchain
Instead of a single linear chain where only one block can be canonical per slot, Kaspa lets **multiple blocks be produced in parallel** and references all of them in a **Directed Acyclic Graph (DAG)**. No valid block is orphaned — blocks mined simultaneously are merged into the DAG rather than discarded. This is what allows 10 blocks/second while preserving PoW security.

### GHOSTDAG / PHANTOM consensus
- **GHOSTDAG** (a greedy implementation of the PHANTOM protocol) takes the DAG and produces a **total ordering** of all blocks and transactions.
- It distinguishes "well-connected" honest blocks (the **blue set**) from outliers (the **red set**) and orders accordingly, so the network reaches consensus on transaction order even with many concurrent blocks.
- Security inherits from PoW: rewriting history still requires out-hashing the honest majority, but throughput is decoupled from confirmation latency.

### kHeavyHash mining
Kaspa uses **kHeavyHash**, an optical-friendly PoW algorithm. It is ASIC-mineable (Bitmain/IceRiver KAS ASICs exist), and the hashrate is large and globally distributed. Optical-PoW research positions Kaspa for potential energy-efficient mining hardware.

### Crescendo and the smart-contract roadmap (Toccata)
- **Crescendo (May 2025)** raised block production from 1 to 10 blocks/sec — the largest throughput upgrade to date.
- **Toccata (targeted June 2026)** is slated to add **native tokens, covenants, and ZK verification** — the foundation for L1 programmability and Kaspa's "based rollup" smart-contract vision (settling L2 execution back to the DAG without fragmenting liquidity). This is the dominant near-term catalyst.
- Other features: **Reachability** (fast DAG topology queries), block-data **pruning**, SPV proofs, and subnetwork support for future L2s.

---

## Major News & Events (2025–2026)

- **May 2025 — Crescendo hard fork.** Successfully activated, raising block production from 1 to 10 blocks per second — the largest throughput upgrade in the network's history.
- **June 2025** — KAS traded around $0.09 with a ~$2.38B market cap; the price subsequently declined through the 2025–26 altcoin drawdown to roughly $0.03 by April 2026.
- **June 2026 — Toccata hard fork (pending).** Mainnet activation targeted for roughly June 5–20, 2026 per CoinMarketCap's June 2026 update. Toccata is slated to introduce native tokens, covenants, and ZK verification — the foundation for L1 programmability and Kaspa's "based rollup" smart-contract vision. This is the dominant near-term catalyst.

---

## Trading Relevance

- **Venues:** Spot on Kraken, KuCoin, Bitget, Gate, MEXC and most mid-tier CEXs (notably *not* Binance or Coinbase as of the 2026-06-20 snapshot — a major-listing catalyst remains outstanding). Perps: **KAS-PERP on [[hyperliquid|Hyperliquid]]** plus Binance/Bybit futures.
- **Narrative basket:** fair-launch PoW (with [[monero]], [[litecoin]]); "Bitcoin-but-faster" rotations; increasingly the L1-programmability story post-Toccata.
- **Catalysts:** Toccata activation and any slippage in its June 2026 window; smart-contract testnet milestones; tier-1 exchange listings; PoW-narrative rotations.
- **Structure:** ~95% of supply already mined means low future emission pressure, but miner sell flow is a persistent bid-side drag in low-price regimes. High retail-community concentration (strong sentiment, reflexive moves).
- **Risk:** -85% from the Aug 2024 ATH ($0.2074) at the 2026-06-20 snapshot; momentum traders treat KAS as a high-beta PoW proxy.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 27.50B KAS |
| **Total Supply** | 27.52B KAS |
| **Max Supply** | 28.70B KAS |
| **Fully Diluted Valuation** | $835.93M |
| **MC / FDV** | 1.00 |
| **Circulating / Max** | ~95.8% |

**Emissions / inflation.** Kaspa fair-launched in November 2021 with **no pre-mine, no pre-sale, and no allocations** — every KAS is mined. Emission follows a **"chromatic" schedule**: rather than abrupt Bitcoin-style halvings, the block reward decreases smoothly each month, halving once per year (the reward is divided by the 12th root of 2 monthly). With ~95.8% of max supply already mined, remaining annual issuance is small (~5% to go to 28.7B) and falling.

**Dilution flag.** MC/FDV of **1.00** means essentially **no dilution overhang** — almost all supply circulates. The relevant supply pressure is not unlocks but **miner sell flow**: in low-price regimes, miners selling rewards to cover electricity create a persistent bid-side drag. High retail-community concentration adds reflexivity (strong sentiment, sharp swings).

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **All-Time High** | $0.2074 (2024-08-01) |
| **Current vs ATH** | -85.34% |
| **All-Time Low** | $0.00017105 (2022-05-26) |
| **Current vs ATL** | +17,678.18% |
| **24h Change** | +1.13% |
| **7d Change** | -3.65% |

---

## Ecosystem & Use Cases

- **Hard money / fast settlement** — Kaspa's pitch is "Bitcoin-but-faster": PoW-secured value transfer with sub-second confirmations, positioning it as a global sequencer for value.
- **Smart contracts (post-Toccata)** — native tokens, covenants, and ZK verification target an L1-programmability layer and a "based rollup" model where L2 execution settles to the DAG without fragmenting liquidity.
- **Mining ecosystem** — kHeavyHash ASICs (IceRiver, Bitmain), large mining pools, and a strong solo/home-mining culture; mining is a core part of community identity.
- **Wallets / tooling** — Kasware, KDX, Tangem, Kaspad node software; community-built explorers and KRC-20 token experiments.
- **DePIN / DeFi (nascent)** — limited today; the smart-contract roadmap is the prerequisite for a real on-chain app ecosystem.

Compared with [[ethereum|Ethereum]] or [[solana|Solana]], Kaspa's on-chain app ecosystem is minimal — its value today is monetary/narrative, with programmability as the forward bet.

---

## Market Structure & Derivatives

| Layer | Detail |
|---|---|
| **Spot CEX** | Kraken (KAS/USD), KuCoin, Bitget, Gate, MEXC and most mid-tier CEXs. **Notably absent from Binance spot and Coinbase** as of the 2026-06-20 snapshot — a tier-1 listing remains an outstanding catalyst |
| **Perps** | KAS-PERP on [[hyperliquid|Hyperliquid]]; KAS futures on Binance and Bybit |
| **Funding / OI** | High-beta PoW proxy; funding swings with PoW-narrative rotations and around the Toccata window. Thin spot volume (~$10M/day) makes derivatives flow disproportionately price-setting |
| **Liquidity** | Thinner than top-50 majors; the missing Binance/Coinbase spot listings cap depth and US accessibility |

---

## Valuation Framework

KAS has no fees-to-token accrual (pure PoW), so valuation leans on **monetary and network metrics**:

- **Hashrate / network security** — rising hashrate signals miner conviction and security; also implies miner cost basis (a soft price floor).
- **Active addresses / transaction count** — on-chain usage of the value-transfer network.
- **Stock-to-flow / remaining emission** — with ~95.8% mined, KAS is approaching a fixed-supply asset; its scarcity narrative strengthens as issuance tapers.
- **Realized cap / MVRV** — momentum traders use these to gauge whether holders are in profit/loss across the -85% drawdown.
- **Relative value vs PoW peers** — compare MC against [[bitcoin|BTC]], [[litecoin|LTC]], [[monero|XMR]] as a "fair-launch PoW" basket ranking.

*(No invented values: the wiki holds no live hashrate/on-chain series; track via Kaspa explorers.)*

---

## Trading Playbook

**Bullish catalysts:** clean Toccata activation and smart-contract testnet milestones; a tier-1 (Binance/Coinbase) spot listing; PoW-narrative rotations; rising hashrate.

**Bearish catalysts:** Toccata slippage/delay in its June 2026 window; persistent miner sell flow in low-price regimes; thin liquidity amplifying drawdowns; broad alt capitulation.

**Setups:**
- **Catalyst trade (Toccata)** — the dominant near-term driver; buy-the-rumor into activation, manage the sell-the-news risk. The June 2026 window makes this live *now*.
- **Fair-launch PoW basket** — trade KAS alongside [[bitcoin|BTC]], [[litecoin|LTC]], [[monero|XMR]] on "Bitcoin-but-faster" rotations; KAS is the high-beta leg.
- **Listing-catalyst lottery** — the missing Binance/Coinbase spot listing is a binary upside catalyst; size for tail outcomes.
- **Mean-reversion in extreme fear** — at a Fear & Greed of 23 and -85% from ATH, washed-out PoW names can snap back; use [[risk-management|stops]].

---

## Competitive Positioning

| Project | Consensus | Throughput | Supply | vs Kaspa |
|---|---|---|---|---|
| **Kaspa** | [[proof-of-work\|PoW]] BlockDAG (GHOSTDAG) | 10 blocks/sec, sub-second | Fair-launch, ~28.7B cap | Fastest PoW; smart contracts pending |
| [[bitcoin\|Bitcoin]] | PoW (linear chain) | ~1 block / 10 min | 21M cap | The benchmark; KAS positions as faster PoW |
| [[litecoin\|Litecoin]] | PoW (Scrypt) | ~2.5 min blocks | 84M cap | Older "faster Bitcoin"; KAS is far faster |
| [[monero\|Monero]] | PoW (RandomX, privacy) | ~2 min blocks | Tail emission | Privacy focus; fellow fair-launch PoW |
| Other DAGs (Nano, etc.) | DAG, often feeless/non-PoW | Instant | Varies | KAS keeps PoW security; many DAGs do not |

Kaspa's edge: **PoW security + the highest throughput of any PoW network + a genuine fair launch**. Its gap vs smart-contract L1s ([[ethereum]], [[solana]]) is programmability — the entire Toccata bet.

---

## History

| Date | Event |
|---|---|
| **2018** | GHOSTDAG/PHANTOM paper (Sompolinsky & Zohar, IACR 2018/104) |
| **Nov 2021** | Fair launch — no pre-mine, pre-sale, or allocations |
| **2022-05-26** | All-time low $0.00017105 |
| **2024-08-01** | All-time high $0.2074 (~$5B cap region) |
| **May 2025** | Crescendo hard fork — 1 -> 10 blocks/sec |
| **June 2025** | ~$0.09 / ~$2.38B cap before the 2025-26 alt drawdown |
| **June 2026 (pending)** | Toccata hard fork — native tokens, covenants, ZK verification |
| **2026-06-20** | ~$0.0304, #77 by market cap, -85% from ATH |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1, BlockDAG)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Kraken | KAS/USD |
| Bitget | KAS/USDT |
| KuCoin | KAS/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | KAS-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kaspa.org/](https://kaspa.org/) |
| **Twitter** | [@KaspaCurrency](https://twitter.com/KaspaCurrency) |
| **Reddit** | [https://www.reddit.com/r/Kaspa](https://www.reddit.com/r/Kaspa) |
| **Telegram** | [kaspaenglish](https://t.me/kaspaenglish) (34,740 members, April 2026) |
| **Discord** | [https://discord.com/invite/kS3SK5F36R](https://discord.com/invite/kS3SK5F36R) |
| **GitHub** | [https://github.com/kaspanet/kaspad](https://github.com/kaspanet/kaspad) |
| **Whitepaper** | [PHANTOM/GHOSTDAG paper (IACR 2018/104)](https://eprint.iacr.org/2018/104.pdf) |

---

## Developer Activity (April 2026 snapshot)

| Metric | Value |
|---|---|
| **GitHub Stars** | 529 |
| **GitHub Forks** | 241 |
| **Pull Requests Merged** | 1,693 |
| **Contributors** | 31 |

---

## Risks

- **Execution / catalyst risk** — Toccata must ship on schedule and deliver working smart contracts; delays or bugs are a direct negative catalyst in the live June 2026 window.
- **No tier-1 spot listing** — absence from Binance and Coinbase spot caps liquidity, US access, and institutional flow.
- **Miner sell pressure** — in low-price regimes miners sell rewards to cover power costs, a persistent bid-side drag despite minimal unlock dilution.
- **Programmability gap** — with no meaningful on-chain app ecosystem yet, KAS's value rests on monetary narrative until Toccata proves out.
- **High beta / reflexivity** — strong but concentrated retail community drives sharp swings; -85% from ATH shows the downside.
- **Thin liquidity** — ~$10M/day spot makes the token sensitive to derivatives-driven flow and large orders.

---

## Related

- [[crypto-markets]]
- [[bitcoin]] — the PoW benchmark Kaspa positions against
- [[proof-of-work]] — the consensus family Kaspa belongs to
- [[monero]], [[litecoin]] — fellow large-cap PoW assets
- [[ethereum]], [[solana]] — smart-contract L1s Kaspa targets post-Toccata
- [[hyperliquid]] — KAS-PERP venue
- [[narrative-trading]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Market data 2026-06-20 — cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- PHANTOM/GHOSTDAG whitepaper — https://eprint.iacr.org/2018/104.pdf
- HelloSafe Kaspa profile (June 2025 price/market cap, Crescendo confirmation) — https://hellosafe.ae/investing/crypto/coins/kaspa
- CoinMarketCap Kaspa latest updates (Toccata fork window, June 2026) — https://coinmarketcap.com/cmc-ai/kaspa/latest-updates/
- Verified via Perplexity sonar, 2026-06-10.
