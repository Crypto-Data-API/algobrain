---
title: "Filecoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins, bitcoin, ethereum]
aliases: ["FIL", "Filecoin Network"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://filecoin.io/"
related: ["[[artificial-intelligence]]", "[[arweave]]", "[[bitcoin]]", "[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[narrative-trading]]"]
---

# Filecoin

**Filecoin** (FIL) is the largest decentralized storage network — a Layer 1 built by Protocol Labs (Juan Benet, also creator of IPFS) where storage providers worldwide rent disk space in an open market secured by cryptographic storage proofs. After raising a record ~$257M in its 2017 ICO and listing at extreme valuations (ATH $236.84, April 2021; -99.6% by April 2026), FIL has spent 2025–2026 re-architecting itself as an **"onchain cloud" for verifiable AI data**: the F3 fast-finality upgrade (450x faster finality), Proof of Data Possession, and the Filecoin Onchain Cloud platform. For traders it is the bellwether of the **[[depin|DePIN]] / decentralized-storage narrative basket** with deep CEX liquidity and a [[hyperliquid|Hyperliquid]] perp.

---

## Market Data

| Field | Value |
|---|---|
| **Current Price** | $0.7859 |
| **Market Cap** | $621.39M |
| **Market Cap Rank** | #90 |
| **Fully Diluted Valuation** | $1.54B |
| **24h Volume** | $57.15M |
| **24h Range** | $0.7646 — $0.8040 |
| **24h Change** | +2.30% |
| **7d Change** | +1.86% |
| **Circulating Supply** | 790.67M FIL |
| **Total Supply** | 1.96B FIL |
| **Max Supply** | Uncapped (emission tied to storage power) |
| **MC / FDV** | 0.40 |
| **All-Time High** | $236.84 (2021-04-01) — currently -99.67% |
| **All-Time Low** | $0.6776 (2026-06-06) — currently +15.98% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index at **23 (Extreme Fear)** in an **Established Bear Market**. FIL printed a fresh all-time low of $0.6776 on 2026-06-06 — one of the deepest ATH drawdowns (-99.67%) among major caps — and now trades just above it. The Onchain Cloud rollout has not yet translated into a sustained re-rating.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FIL |
| **Rank tier** | Top 100 (#90 at the 2026-06-20 snapshot) |
| **Sector** | [[depin|DePIN]] / decentralized storage / smart-contract L1 (FVM); GMCI DePIN and GMCI 30 index constituent |
| **Supply mechanics** | ~791M circulating vs 1.96B total (2026-06-20), MC/FDV 0.40 — long-running vesting/emission overhang from the 2017 raise, now largely fading; block rewards tied to storage power |
| **Finality** | <60 seconds since the F3 upgrade (was ~7.5 hours) — a 450x improvement |
| **Backers** | Sequoia, Pantera, [[blockchain-capital|Blockchain Capital]] portfolios; CoinList launchpad alumnus |
| **Founder** | Juan Benet (Protocol Labs; also created IPFS) |
| **Website** | [https://filecoin.io/](https://filecoin.io/) |

---

## Overview

The Filecoin network achieves economies of scale by allowing anyone worldwide to participate as storage providers. It makes storage resemble a commodity or utility by decoupling hard-drive space from additional services. On this global market the price of storage is driven by supply and demand rather than corporate pricing departments, and miners compete on reliability and price.

Storage is secured by Filecoin's proof system (Proof-of-Replication and Proof-of-Spacetime, extended in May 2025 with **Proof of Data Possession** for "warm" always-available storage). The Filecoin Virtual Machine (FVM, 2023) added smart contracts, enabling on-chain storage deals, payment rails, and DeFi around storage collateral.

---

## Protocol & Technology

Filecoin is a purpose-built Layer 1 whose consensus and economics revolve around **proving that real storage exists and stays live**.

### Storage proofs
- **Proof-of-Replication (PoRep)** — a storage provider proves it has created a unique physical copy of a client's data (sealing), preventing fake or deduplicated capacity.
- **Proof-of-Spacetime (PoSt)** — providers repeatedly prove, over time, that they are still storing the sealed data. Failure to respond is slashed.
- **Proof of Data Possession (PDP, May 2025)** — a lighter, continuous proof that data remains live and *retrievable* without the heavy sealing overhead, enabling "warm" always-available storage rather than cold archival.

### Consensus
Filecoin uses **Expected Consensus (EC)**, a Verifiable-Random-Function leader election weighted by a provider's proven **storage power** (Quality-Adjusted Power). More storage proven = higher block-production probability — so security is anchored to useful work (storage) rather than raw hash power like [[proof-of-work|PoW]] or pure stake like [[proof-of-stake|PoS]].

### F3 fast finality (April 2025)
The **F3 (Fast Finality via GossiPBFT)** upgrade cut finality from ~7.5 hours to under 60 seconds — a ~450x improvement — moving Filecoin from archival-only toward real-time, app-grade settlement.

### FVM and retrieval
- **Filecoin Virtual Machine (FVM, 2023)** — an EVM-compatible smart-contract layer enabling on-chain storage deals, programmable payments, collateral markets, and DeFi around storage. Solidity contracts deploy directly.
- **Retrieval markets** — historically Filecoin's weak spot (data was cheap to store, slow to retrieve). PDP + the Onchain Cloud's **Filecoin Beam** (incentivized retrieval) and **Saturn**-style CDN layers target fast retrieval.
- **IPFS** — Filecoin shares content-addressing (CIDs) with IPFS, its incentive layer; IPFS provides addressing/retrieval, Filecoin provides paid, proven persistence.

### Filecoin Onchain Cloud (FOC)
Announced Nov 2025, mainnet targeted Jan 2026: **Warm Storage**, **Filecoin Pay** (usage-based on-chain payments), **Filecoin Beam** (incentivized retrieval), and the **Synapse SDK** — repositioning FIL as a verifiable "onchain cloud" for AI data.

---

## Major News & Events (2025–2026)

- **April 2025 — F3 (Fast Finality) live.** Finality cut from ~7.5 hours to under 60 seconds (450x), shifting Filecoin from archival-only to a network capable of real-time applications (Filecoin Foundation).
- **May 2025 — Proof of Data Possession (PDP)** launched: continuous cryptographic proofs that data stays live and retrievable — the foundation for warm storage.
- **Nov 18, 2025 — Filecoin Onchain Cloud (FOC)** announced/live on testnet: Warm Storage, Filecoin Pay (usage-based on-chain payments), Filecoin Beam (incentivized retrieval), and the Synapse SDK; **mainnet planned January 2026** (filecoin.io blog).
- **Jan 2026 — FIL rallied to ~$1.58** around the Onchain Cloud mainnet window (MEXC blog), before fading with the broader alt market to ~$0.88 by April (ATL $0.7902 printed 2026-03-29).
- **2025–2026 — AI-data positioning.** Filecoin pitches verifiable storage for AI training datasets (integrity + provenance), the network's main demand narrative for 2026; the year is widely framed as the test of whether paid demand replaces incentive-driven storage.

---

## Trading Relevance

- **Narrative basket:** DePIN / decentralized storage — FIL is the large-cap proxy, trading alongside [[arweave|Arweave]] (AR), Render, Akash; it also catches beta from the broader [[artificial-intelligence|AI]]-infrastructure narrative.
- **Venues:** deep spot on Binance, Kraken, Bitget, KuCoin, Crypto.com (~$57M daily volume at the 2026-06-20 snapshot); **FIL-PERP on [[hyperliquid|Hyperliquid]]** and every major perp venue. Long listed-history makes it a staple of alt-basket momentum systems.
- **Catalysts:** Onchain Cloud mainnet adoption metrics (paid storage deals, Filecoin Pay volume), AI-dataset partnerships, F3-enabled real-time app launches, GMCI/DePIN index flows.
- **Structure:** MC/FDV 0.39 still implies future dilution, but the heaviest 2017-investor vesting is behind it — emission pressure is fading versus 2021–2023.
- **Risk:** one of the worst ATH drawdowns among majors (-99.6%); storage utilization vs paid demand remains the fundamental question; competitor basins (Arweave's permanent storage, centralized cloud pricing) cap pricing power.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 790.67M FIL |
| **Total Supply** | 1.96B FIL |
| **Max Supply** | Uncapped — emission tied to storage power; ~2B effective cap |
| **Fully Diluted Valuation** | $1.54B |
| **MC / FDV** | 0.40 |
| **Circulating / Total** | ~40.4% |

**Emissions / inflation.** Filecoin block rewards combine a fixed "Simple Minting" baseline with **"Baseline Minting"** that scales with network storage power — the protocol releases more FIL faster as proven storage grows, deliberately tying issuance to network utility. Storage providers must also post **pledge collateral** (locked FIL) to onboard sectors, which removes FIL from circulation and rises with onboarded capacity.

**Dilution flag.** MC/FDV of **0.40** means only ~40% of total supply circulates — a material dilution overhang. The bulk of the 2017-ICO investor and team vesting is now behind it, so emission pressure is *fading* versus 2021–2023, but new block rewards plus collateral dynamics keep supply elastic. The combination of heavy historical dilution and a -99.67% ATH drawdown explains FIL's persistently weak price.

---

## Ecosystem & Use Cases

- **Bulk / archival storage** — the original product: cheap, verifiable cold storage for large datasets (web archives, scientific data, NFT media, video).
- **Warm storage (PDP + Onchain Cloud)** — always-available, retrievable storage for live applications, the 2026 demand push.
- **AI training data** — verifiable, provenance-tracked storage for AI datasets (integrity + auditability) — the headline 2026 narrative.
- **FVM DeFi** — collateral markets, storage-deal financing, perpetual storage funds, and liquid-staking-style products around provider pledge collateral.
- **IPFS pinning at scale** — paid persistence layer behind content-addressed [[ethereum|Web3]] apps and NFT metadata.
- **Enterprise / public-sector archives** — partnerships for verifiable long-term records.

The central fundamental question for 2026: does **paid** demand (clients actually buying storage/retrieval) replace **incentive-driven** capacity (providers onboarding for block rewards)?

---

## Market Structure & Derivatives

| Layer | Detail |
|---|---|
| **Spot CEX** | Binance (FIL/USDT), Kraken (FIL/USD), Bitget, KuCoin, Crypto.com — long-listed, deep liquidity (~$57M/day at the 2026-06-20 snapshot) |
| **Perps** | FIL-PERP on [[hyperliquid|Hyperliquid]]; FIL futures on Binance, Bybit, OKX and most major venues |
| **Funding / OI** | Mature derivatives market; funding generally muted in the current bear, tilting negative on capitulation. As a long-listed major, FIL is a staple of alt-basket and DePIN momentum systems |
| **Index flows** | GMCI DePIN and GMCI 30 constituent — passive/index rebalances add mechanical flow |

---

## Valuation Framework

FIL valuation centers on **network-usage and storage economics** rather than cash flow:

- **Active deal storage / utilized capacity** — paid, actively-stored data versus raw committed capacity; the gap measures how much capacity is incentive-driven vs demand-driven.
- **Filecoin Pay volume** — on-chain payment throughput for storage/retrieval; a direct revenue proxy under the Onchain Cloud model.
- **Storage power (QAP) and provider count** — supply-side health and security.
- **Pledge collateral locked** — FIL removed from circulation; rises with onboarding, a structural supply sink.
- **FDV / utilized-storage TB** — a relative "price per useful terabyte" comparable against [[arweave|Arweave]] and centralized cloud ($/GB-month).

*(No invented values: the wiki holds no live deal/utilization series; track via Filecoin network dashboards / Starboard.)*

---

## Trading Playbook

**Bullish catalysts:** Onchain Cloud mainnet adoption (paid deals, Filecoin Pay volume); AI-dataset partnerships; F3-enabled real-time app launches; GMCI/DePIN index inflows; a [[depin|DePIN]] sector rotation led by [[render-token|Render]].

**Bearish catalysts:** weak paid-demand metrics (utilization stuck near incentive-only); centralized-cloud price competition; continued dilution headlines; broad alt capitulation dragging the DePIN basket.

**Setups:**
- **DePIN basket beta** — FIL is the large-cap storage proxy; trade alongside [[arweave|AR]], [[render-token|RENDER]], [[akash-network|AKT]].
- **ATL base trade** — fresh ATL on 2026-06-06 ($0.6776) makes FIL a deep-value mean-reversion candidate in extreme fear; the long listed history gives clean technicals. Use [[risk-management|stops]] below the ATL.
- **Catalyst-driven** — Onchain Cloud adoption prints are the cleanest fundamental trigger.

---

## Competitive Positioning

| Project | Storage model | Token | Pricing | vs Filecoin |
|---|---|---|---|---|
| **Filecoin** | Contract/term storage (pay-as-you-go), warm + cold | FIL | Market-set per GB-month | Largest network; FVM smart contracts; proof-heavy |
| [[arweave\|Arweave]] | Permanent storage (pay-once, store-forever) | AR | One-time endowment fee | Permanence vs Filecoin's renewable contracts; closest rival |
| [[render-token\|Render]] | GPU **compute** (not storage) | RENDER | Per render/compute job | Sibling [[depin]] basket member, different resource |
| [[akash-network\|Akash]] | Cloud **compute** | AKT | Reverse-auction compute | Compute not storage; DePIN basket peer |
| **Centralized** | AWS S3 / Glacier, Google Cloud Storage | — | $/GB-month | The real benchmark on price + retrieval speed |

Filecoin's edge: scale, FVM programmability, and proof-secured persistence. Its weakness vs [[arweave|Arweave]]: contract storage requires renewal/re-deal management where Arweave promises permanence; vs centralized cloud: retrieval speed and developer simplicity, which the Onchain Cloud aims to close.

---

## Risks

- **Dilution overhang** — MC/FDV 0.40; ongoing block-reward emission keeps supply elastic.
- **Demand realization** — paid demand may not replace incentive-driven capacity; the core 2026 thesis is unproven.
- **Worst-in-class drawdown** — -99.67% from ATH, fresh ATL on 2026-06-06; structurally weak price psychology.
- **Centralized-cloud competition** — AWS/GCP pricing and retrieval UX cap Filecoin's pricing power.
- **Competitor displacement** — [[arweave|Arweave]] for permanence; commoditization of decentralized storage.
- **Execution risk** — Onchain Cloud, PDP, and retrieval markets must ship and gain adoption to re-rate the token.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1 with FVM smart contracts)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | FIL/USDT |
| Kraken | FIL/USD |
| Bitget | FIL/USDT |
| KuCoin | FIL/USDT |
| Crypto.com Exchange | FIL/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | FIL-PERP | Perpetual |

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://filecoin.io/](https://filecoin.io/) |
| **Twitter** | [@Filecoin](https://twitter.com/Filecoin) |
| **GitHub** | [https://github.com/filecoin-project/lotus](https://github.com/filecoin-project/lotus) |
| **Docs** | [https://docs.filecoin.io/](https://docs.filecoin.io/) |

---

## Related

- [[arweave]] — closest competitor (permanent vs contract-based storage)
- [[artificial-intelligence]] / [[decentralized-ai]] — demand-side narrative
- [[hyperliquid]] — FIL-PERP venue
- [[blockchain-capital]] — early investor (BCAP portfolio)
- [[crypto-markets]], [[narrative-trading]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Market data 2026-06-20 — cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- Filecoin Foundation: "Fast, Secure, and Scalable: How F3 is Reshaping the Future of Onchain Storage" — https://fil.org/blog/fast-secure-and-scalable-how-f3-is-reshaping-the-future-of-onchain-storage
- Filecoin blog (2025-11-18): Introducing Filecoin Onchain Cloud — https://filecoin.io/blog/posts/introducing-filecoin-onchain-cloud-verifiable-developer-owned-infrastructure/
- Filecoin blog: Filecoin in 2025 — Year in Review — https://filecoin.io/blog/posts/filecoin-in-2025-year-in-review/
- MEXC blog (2026): Filecoin's Jan 2026 $1.58 rally & Onchain Cloud — https://blog.mexc.com/news/why-filecoins-jan-2026-1-58-rally-onchain-cloud-could-make-it-ai-infrastructures-12b-hidden-gem/
- Verified via Perplexity sonar + web search, 2026-06-10.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 799.30M FIL |
| **Total Supply** | 1.96B FIL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $1.52B |
| **Market Cap / FDV Ratio** | 0.41 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $236.84 (2021-04-01) |
| **Current vs ATH** | -99.67% |
| **All-Time Low** | $0.6776 (2026-06-06) |
| **Current vs ATL** | +14.62% |
| **24h Change** | -1.39% |
| **7d Change** | +0.14% |
| **30d Change** | -3.29% |
| **1y Change** | -70.46% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $55.19M |
| **Market Cap Rank** | #91 |
| **24h Range** | $0.7718 — $0.8028 |
| **CoinGecko Sentiment** | 60% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

**Venues & liquidity.** FIL trades on **both** [[binance|Binance]] (FIL/USDT spot plus a USD-margined perpetual) and [[hyperliquid|Hyperliquid]] (**FIL-PERP**, leverage up to ~40-50x). This is a deep, liquid two-venue market: long-listed CEX spot depth on Binance, Kraken, Bitget, KuCoin and Crypto.com sits alongside on-chain perp depth on Hyperliquid. Dual venue availability means tight spreads and reliable fills for size, and it opens direct CEX-vs-DEX execution — funding and mark can be compared across Binance and Hyperliquid, letting traders route the leg with the better price and size positions against the deeper book rather than being captive to a single venue.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — FIL-PERP on Hyperliquid and the Binance USD-margined perp both quote continuous funding, so funding can dislocate between the two venues on the same asset; harvest the spread.
- [[cash-and-carry]] — deep Binance spot plus a liquid perp lets you hold FIL spot against a short perp to capture basis/positive funding with low execution slippage.
- [[funding-rate-harvest]] — mature two-venue funding market on a mid-cap alt; collect funding while delta-hedged when the perp trades rich or cheap to spot.
- [[liquidation-cascade-fade]] — FIL's -99%+ ATH drawdown and thin conviction make it prone to leverage-driven capitulation wicks; fade forced-liquidation spikes back toward the range.
- [[mean-reversion]] — clean long listed-history technicals and a fresh ATL base make FIL a mean-reversion candidate off extreme-fear washouts.
- [[narrative-trading]] — FIL is the large-cap [[depin|DePIN]]/decentralized-storage proxy; trade the storage/AI-data narrative rotation and its BTC/ETH beta.

**Volatility & regime character.** FIL is a **high-beta mid-cap infrastructure altcoin** (DePIN / decentralized-storage L1), not a large-cap store-of-value or a memecoin. It carries strong positive beta to [[bitcoin]] and [[ethereum]] — it tends to amplify broad-market moves on the downside in bear regimes and lags on relief rallies — while also catching idiosyncratic beta from the DePIN and AI-infrastructure narrative baskets (trades alongside [[arweave|Arweave]], Render, Akash). Realized volatility is elevated and reflexive around narrative catalysts and index rebalances.

**Risk flags.**
- **Emission / dilution overhang** — MC/FDV ~0.40; ongoing baseline block-reward emission tied to storage power keeps supply elastic even though the heaviest 2017-ICO vesting is behind it.
- **Narrative dependence** — price hinges on the DePIN / AI-data storage thesis; weak paid-demand metrics or a basket rotation out of DePIN can drag FIL regardless of network health.
- **Structurally weak price psychology** — one of the worst ATH drawdowns among majors (-99%+) with a fresh ATL, which can extend downside momentum and trap mean-reversion entries.
- **Perp funding dislocations** — the two-venue perp market can see funding spikes and CEX-vs-DEX divergence during capitulation, a risk to naked longs/shorts but the raw material for the funding strategies above.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=FIL` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=FIL` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=FIL&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=FIL&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=FIL"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---
