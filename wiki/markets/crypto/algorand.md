---
title: "Algorand"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["ALGO"]
entity_type: protocol
founded: 2017
headquarters: "Boston, USA (Algorand Foundation: Singapore)"
website: "https://algorand.co/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[l1-l2-rotation]]", "[[real-world-assets]]", "[[solana]]"]
---

# Algorand

**Algorand** (ALGO) is a Pure [[proof-of-stake|Proof-of-Stake]] Layer-1 founded by Turing Award cryptographer Silvio Micali (2017, mainnet 2019), known for instant finality, no forks, and native Python support. Long criticized as a "ghost chain" despite strong tech, it pivoted in 2025 toward [[real-world-assets|real-world assets]], payments and on-chain staking rewards. As of 2026-06-20 it sits in the **top-80 market-cap tier** (~$841M) — one of the deepest drawdowns from ATH (-97%) among majors, making it a classic deep-value/L1-rotation candidate.

---

## Market Data

| Field | Value |
|---|---|
| **Current Price** | $0.09422 |
| **Market Cap** | $841.48M |
| **Market Cap Rank** | #76 |
| **Fully Diluted Valuation** | $841.48M |
| **24h Volume** | $28.61M |
| **24h Range** | $0.09089 — $0.09691 |
| **24h Change** | +1.54% |
| **7d Change** | +6.37% |
| **Circulating Supply** | 8.93B ALGO |
| **Total Supply** | 8.93B ALGO |
| **Max Supply** | 10.00B ALGO |
| **MC / FDV** | 1.00 |
| **All-Time High** | $3.56 (2019-06-20) — currently -97.35% |
| **All-Time Low** | $0.0801 (2026-03-29) — currently +17.69% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index at **23 (Extreme Fear)** in an **Established Bear Market**. ALGO trades just ~18% above its fresh March 2026 all-time low and -97% from its 2019 ATH — a textbook late-cycle, deeply-based legacy L1, modestly green over the prior week (+6.4% / 7d).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ALGO |
| **Market Cap Rank** | #76 (2026-06-20) |
| **Market Cap** | $841.48M (2026-06-20) |
| **Consensus** | Pure [[proof-of-stake\|Proof-of-Stake]] (PPoS); instant finality, no slashing |
| **Supply mechanics** | 10B max supply, ~8.93B circulating (MC/FDV ≈ 1.0 — emissions largely done) |
| **Founder** | Silvio Micali (Turing Award cryptographer, MIT) |
| **Categories** | Smart Contract Platform, Layer 1, Real World Assets (RWA), Proof of Stake, Made in USA |
| **Website** | [https://algorand.co/](https://algorand.co/) |

---

## Overview

Algorand is a scalable, secure, and decentralized digital currency and smart contract platform. Its protocol uses a variation of [[proof-of-stake|Proof-of-Stake]] called Pure PoS (PPoS) to secure the network and reach consensus on block production. Developers can build decentralized applications (dApps) using familiar programming languages, including Python, which Algorand supports natively. Its infrastructure enables various use cases, including payment systems, digital identity solutions, supply-chain tracking, and financial services. The protocol's architecture allows for tokenization of assets and the development of smart contracts, while its technical specifications support both retail users seeking basic transaction capabilities and enterprises requiring more complex blockchain solutions.

---

## Protocol & Technology

Algorand's design goal is to solve the blockchain trilemma (security, scalability, decentralization) without forks or slashing, via a cryptographically clean [[proof-of-stake|PoS]] variant.

### Pure Proof-of-Stake (PPoS)
- Every ALGO holder is implicitly eligible to participate; there is **no minimum stake to secure the network** and **no slashing**.
- Each round, a small committee of proposers/voters is selected via a **Verifiable Random Function (VRF)** — a private, self-selecting lottery weighted by stake. Validators learn they are chosen only after the fact, which prevents an adversary from targeting them in advance.
- **Instant finality, no forks** — a block is final the moment it is committed (single round, ~2.8s block time / sub-3s finality); there are no reorgs or orphaned chains, unlike [[proof-of-work|PoW]] or longest-chain PoS.
- Security holds as long as a supermajority of stake is honest; the VRF + Byzantine Agreement (Algorand BA*) protocol provides the consensus.

### AVM and developer experience
- The **Algorand Virtual Machine (AVM)** runs smart contracts written in **TEAL**, with high-level languages **PyTeal / Algorand Python** — native Python support is a key developer draw.
- **Algorand Standard Assets (ASAs)** make token and RWA issuance a first-class, layer-1 primitive (no smart contract required to mint).
- **Atomic transfers** group multiple transactions that all succeed or all fail — useful for DEX swaps, escrow, and RWA settlement.
- **AlgoKit** (4.0 in the 2026 roadmap) provides composable contract libraries, SDKs, and AI-assisted tooling.

### Staking rewards (2025)
Protocol v4.0 introduced on-chain staking rewards: wallets staking ≥30,000 ALGO can earn block rewards by running a node or delegating; proposers earn 50% of transaction fees plus a Foundation-funded bonus (started 10 ALGO/block, decaying 1%/million blocks). This created a native yield sink and more than doubled validator participation.

## Major News & Events (2025–2026)

- **2025-01 — Protocol v4.0 + staking rewards**: wallets staking ≥30,000 ALGO can earn block rewards by running a node or delegating; block proposers earn 50% of transaction fees plus a Foundation-funded bonus (started at 10 ALGO/block, decaying 1% per million blocks). Validator participation more than doubled and the Foundation's share of total stake fell from 63% to 21% — a major decentralization shift.
- **2025 — "2025+" roadmap**: refocus on real-world use — RWA tokenization, payments, and enterprise rails. **Intermezzo** launched: a custodial API solution (built on HashiCorp Vault) abstracting key management for businesses; powers WorldChess's on-chain loyalty program.
- **2026 roadmap**: full rollout of **AlgoKit 4.0** (composable contract libraries, new SDKs, AI-assisted tooling), **Rocca** self-custody wallet (Web2-style, open-source/white-label), and "Project King Safety" economic-incentive recalibration.
- **Price**: all-time low printed 2026-03-29 ($0.0801); as of 2026-06-20 ALGO trades ~$0.0942 (~+18% above ATL), still -97% from its 2019 ATH.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 8.93B ALGO |
| **Total Supply** | 8.93B ALGO |
| **Max Supply** | 10.00B ALGO |
| **Fully Diluted Valuation** | $841.48M |
| **MC / FDV** | 1.00 |
| **Circulating / Max** | ~89.3% |

**Emissions / inflation.** ALGO had a 10B fixed max supply set at genesis, distributed via auctions, community/ecosystem incentives, and Foundation allocations. With ~8.93B already circulating (total = circulating, so no locked treasury overhang in the FDV sense) and emissions essentially complete, **MC/FDV ≈ 1.0 means negligible dilution**. The 2025 staking-rewards program redirects a portion of fees + a decaying Foundation bonus to validators, creating a native yield sink that absorbs supply.

**Decentralization shift.** The 2025 staking launch cut the Foundation's share of total stake from **63% to 21%**, a material decentralization improvement and a structural positive for the network's credibility.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **All-Time High** | $3.56 (2019-06-20) |
| **Current vs ATH** | -97.35% |
| **All-Time Low** | $0.0801 (2026-03-29) |
| **Current vs ATL** | +17.69% |
| **24h Change** | +1.54% |
| **7d Change** | +6.37% |

---

## Ecosystem & Use Cases

- **Real-world assets (RWA) / tokenization** — ASAs make on-chain issuance of bonds, funds, carbon credits, and stablecoins straightforward; the centerpiece of the 2025+ strategy.
- **Payments / enterprise rails** — **Intermezzo** (custodial API on HashiCorp Vault) abstracts key management for businesses; powers WorldChess's on-chain loyalty program.
- **Stablecoins** — native USDC and USDT issuance on Algorand; fast, cheap settlement suits payments.
- **DeFi (modest)** — DEXs (Tinyman, Pact), lending (Folks Finance), and liquid staking, though TVL is far below [[ethereum]]/[[solana]].
- **Digital identity, supply chain, CBDC pilots** — Algorand has historically targeted government/enterprise pilots (e.g. central-bank and national-ID experiments).
- **Tooling** — AlgoKit 4.0, the Rocca self-custody wallet, and AI-assisted dev tooling are the 2026 developer-acquisition push.

The persistent critique: strong technology and enterprise pipeline, but consumer/app traction ("ghost chain") has lagged the headline tech.

---

## Market Structure & Derivatives

| Layer | Detail |
|---|---|
| **Spot CEX** | Binance (ALGO/USDT), Kraken (ALGO/USD), **Upbit (ALGO/KRW — Korean retail flow matters for ALGO)**, Bitget, KuCoin, Crypto.com — deep, long-listed liquidity |
| **Spot DEX** | Tinyman, Pact (on Algorand) |
| **Perps** | ALGO-PERP on [[hyperliquid|Hyperliquid]]; ALGO futures on Binance, Bybit, OKX |
| **Funding / OI** | Mature derivatives; funding generally muted in the bear, useful for momentum/funding trades. Korean spot flow (Upbit) can drive idiosyncratic moves |
| **Staking yield** | Native ~on-chain staking rewards (post-2025 v4.0) provide a yield alternative to derivatives carry |

---

## Valuation Framework

ALGO valuation leans on **network usage and the RWA pivot**, not cash flow:

- **On-chain RWA value / tokenized assets** — the clearest fundamental for the 2025+ thesis; growth in tokenized funds/bonds on Algorand.
- **TVL and DEX volume** — DeFi traction vs [[ethereum]]/[[solana]]; the gap is the "ghost chain" discount.
- **Active addresses / transactions** — payments and app usage; stablecoin transfer volume is a useful proxy.
- **Staking participation / Foundation stake share** — decentralization and yield-sink health (Foundation share fell 63% -> 21%).
- **MC vs peer L1s** — relative value against other smart-contract L1s on a TVL- or fee-normalized basis; ALGO typically trades at a steep discount.

*(No invented values: the wiki holds no live TVL/RWA series; track via DefiLlama / Algorand dashboards.)*

---

## Trading Playbook

**Bullish catalysts:** AlgoKit 4.0 / Rocca wallet shipping; RWA/payments partnership announcements; Project King Safety economics; an L1-quality-curve rotation reaching legacy alts; Korean (Upbit) flow.

**Bearish catalysts:** continued ghost-chain perception (TVL/app revenue lagging); RWA narrative stalling; broad alt capitulation; a fresh ATL breakdown below $0.08.

**Setups:**
- **Deep-value / late-cycle L1 rotation** — ALGO is a high-beta laggard that historically rallies late when capital rotates down the [[l1-l2-rotation|L1 quality curve]]; -97% from ATH and just above ATL gives asymmetric base-building potential.
- **RWA basket beta** — trade ALGO alongside other [[real-world-assets|RWA]] names on tokenization headlines.
- **Range/mean-reversion** — deep, based price with native staking yield suits accumulate-and-stake or range trades; use [[risk-management|stops]] below the $0.0801 ATL.

---

## Competitive Positioning

| L1 | Consensus | Finality | Dev language | vs Algorand |
|---|---|---|---|---|
| **Algorand** | Pure [[proof-of-stake\|PoS]] (VRF + BA*) | Instant, no forks | Python (PyTeal/TEAL) | Clean PoS, RWA focus; weak app traction |
| [[ethereum\|Ethereum]] | PoS (Casper/Gasper) | ~12.8 min | Solidity | Dominant ecosystem/TVL; ALGO far cheaper/faster, far less liquidity |
| [[solana\|Solana]] | PoH + PoS | sub-second (probabilistic) | Rust | Higher throughput + thriving apps; ALGO lacks the ecosystem |
| Avalanche | PoS (Snowman) | sub-2s | Solidity | Subnet model vs Algorand's single chain |
| Cardano | PoS (Ouroboros) | probabilistic | Plutus/Haskell | Both academic-rigor L1s with app-traction critiques |

Algorand's edge: **instant finality, no slashing, native RWA primitives (ASAs), and academic-grade consensus**. Its weakness: ecosystem/TVL and app revenue trail the leading L1s, the core of the persistent valuation discount.

---

## History

| Date | Event |
|---|---|
| **2017** | Founded by Silvio Micali (MIT); Algorand Foundation established |
| **2019-06** | Mainnet launch; ALGO ATH $3.56 (2019-06-20) |
| **2019–2024** | Enterprise/CBDC pilots; "ghost chain" critique despite strong tech |
| **2025-01** | Protocol v4.0 + staking rewards; Foundation stake share 63% -> 21% |
| **2025** | "2025+" roadmap — RWA, payments, Intermezzo enterprise API |
| **2026-03-29** | All-time low $0.0801 |
| **2026** | AlgoKit 4.0, Rocca wallet, Project King Safety on the roadmap |
| **2026-06-20** | ~$0.0942, #76 by market cap, -97% from ATH |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | ALGO/USDT |
| Kraken | ALGO/USD |
| Upbit | ALGO/KRW |
| Bitget | ALGO/USDT |
| KuCoin | ALGO/USDT |
| Crypto.com Exchange | ALGO/USDT |

### Decentralized Exchanges / Perps

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ALGO-PERP | Perpetual |

---

## Trading Relevance

- **Narrative baskets**: legacy alt-L1 ([[l1-l2-rotation]]) and [[real-world-assets|RWA]]. ALGO is a high-beta laggard that historically rallies late-cycle when capital rotates down the L1 quality curve.
- **Structural setup**: emissions essentially complete (MC/FDV = 1.0), so no unlock overhang; the 2025 staking-rewards launch created a new native yield sink for supply.
- **Venues**: deep spot across Binance/Kraken/Upbit (Korean flow matters for ALGO); ALGO-PERP on [[hyperliquid]] for funding and momentum trades.
- **Catalysts**: AlgoKit 4.0 / Rocca wallet shipping in 2026, RWA/payments partnership announcements, Project King Safety economics changes.
- **Risks**: persistent ghost-chain perception — TVL and app revenue remain far below [[solana]] and [[ethereum]]; -97% from ATH reflects a long-term downtrend that has only recently based.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://algorand.co/](https://algorand.co/) |
| **Twitter** | [@algorand](https://twitter.com/algorand) |
| **Reddit** | [https://www.reddit.com/r/AlgorandOfficial/](https://www.reddit.com/r/AlgorandOfficial/) |
| **Telegram** | [algorand](https://t.me/algorand) |
| **Discord** | [https://discord.gg/QBYp7Y2](https://discord.gg/QBYp7Y2) |
| **GitHub** | [https://github.com/algorand/go-algorand](https://github.com/algorand/go-algorand) |
| **Whitepaper** | [https://www.algorand.com/technology/white-papers](https://www.algorand.com/technology/white-papers) |

---

## Developer Activity

| Metric | Value (2026-04-09 snapshot) |
|---|---|
| **GitHub Stars** | 1,426 |
| **GitHub Forks** | 525 |
| **Commits (4 weeks)** | 13 |
| **Pull Requests Merged** | 3,906 |
| **Contributors** | 115 |

---

## Trading Characteristics

| Characteristic | Detail (2026-06-20) |
|---|---|
| **24h Volume** | $28.61M |
| **Market Cap Rank** | #76 |
| **24h Range** | $0.09089 — $0.09691 |
| **CoinGecko Sentiment** | 88% positive (April 2026 reading) |

---

## Risks

- **Ghost-chain perception** — TVL and app revenue remain far below [[solana]] and [[ethereum]]; the core driver of ALGO's deep discount.
- **Demand realization (RWA)** — the 2025+ RWA/payments pivot is the thesis; if tokenization volume does not materialize, valuation rests on legacy beta.
- **Structural downtrend** — -97% from ATH and just ~18% above a fresh 2026-03-29 ATL; price has only recently based.
- **Competition** — leading L1s ([[ethereum]], [[solana]]) and newer entrants dominate developer mindshare.
- **Korean-flow concentration** — heavy Upbit volume can drive idiosyncratic, sentiment-led swings.
- **Liquidity contraction** — volume has thinned (~$29M/day) versus prior cycles.

---

## See Also / Related

- [[crypto-markets]]
- [[l1-l2-rotation]] — the rotation basket ALGO trades in
- [[real-world-assets]] — its 2025+ strategic narrative
- [[ethereum]], [[solana]] — competing smart-contract platforms
- [[hyperliquid]] — perp venue

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Market data 2026-06-20 — cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- Algorand, "Algorand's 2025+ roadmap: Building for real-world use" — https://algorand.co/blog/algorands-2025-roadmap-building-for-real-world-use
- Algorand, "2025 on Algorand: Roadmap progress" — https://algorand.co/blog/2025-on-algorand-roadmap-progress
- Messari, "Algorand Q3 2025 Brief" — https://messari.io/report/algorand-q3-2025-brief
- Web verification (WebSearch + Perplexity), 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.97B ALGO |
| **Total Supply** | 8.97B ALGO |
| **Max Supply** | 10.00B ALGO |
| **Fully Diluted Valuation** | $746.26M |
| **Market Cap / FDV Ratio** | 1.00 |

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
