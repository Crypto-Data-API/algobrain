---
title: "MultiversX"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["EGLD", "Elrond"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://multiversx.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bitcoin]]", "[[layer-1]]", "[[proof-of-stake]]"]
---

# MultiversX

**MultiversX** (ticker **EGLD**), formerly **Elrond**, is a [[layer-1]] blockchain that pursues horizontal scalability through full sharding — network, transaction, and state sharding combined into an "Adaptive State Sharding" design. It runs a Secure [[proof-of-stake]] (SPoS) consensus and markets itself as a high-throughput platform for DeFi, real-world assets, and the metaverse. EGLD ("Electronic Gold") is the native token used for fees, staking, and governance. The project rebranded from **Elrond** to **MultiversX** in late 2022 — the wiki slug `elrond-erd-2` and CoinGecko id preserve the legacy name.

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | EGLD |
| **Current Price** | $2.88 |
| **Market Cap** | $86,992,991 |
| **Market Cap Rank** | #295 |
| **24h Volume** | $3,737,760 |
| **24h Change** | -0.29% |
| **7d Change** | -2.46% |
| **All-Time High** | $545.64 (2021-11-23) — **-99.5%** |
| **All-Time Low** | $2.70 (2026-06-06) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Artificial Intelligence (AI), MultiversX Ecosystem, Binance Launchpad, Proof of Stake (PoS), Coinbase 50 Index |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** The 2026-06-21 snapshot falls within an *Established Bear Market*, [[fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (extreme fear)**. EGLD was roughly flat over 24h (-0.29%) and soft over the prior week (-2.46%), sits ~99.5% below its 2021 all-time high, and is trading only fractionally above its **all-time low of $2.70 set on 2026-06-06** — i.e., at effectively the lowest valuation in its history.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~30.18M EGLD |
| **Total Supply** | ~30.18M EGLD |
| **Max Supply** | Capped at 31.4M EGLD (declining issuance) |
| **Fully Diluted Valuation** | ~$86.0M |
| **Market Cap / FDV Ratio** | ~1.00 |

EGLD has a near-fully-circulating supply (MC/FDV ≈ 1.00) — there is no large insider unlock overhang. The protocol uses a **declining inflation** schedule capped around 31.4M EGLD, with transaction fees burned to offset issuance, so net inflation trends toward zero as usage grows. EGLD secures the network via Secure [[proof-of-stake]] staking — validators and delegators earn staking rewards (yield) for participating in consensus. The token also pays transaction fees, enables smart-contract deployment, and serves as a governance vote.

**Dilution note:** With circulating ≈ total supply and a hard cap near 31.4M EGLD, EGLD's supply profile is comparatively benign versus the airdrop/VC-heavy tokens in the small-cap cohort (e.g., [[movement]], [[plasma]]). The principal headwind is demand-side (adoption), not forced sell pressure from vesting.

---

## Market Structure & Derivatives

### Spot venues

| Exchange | Pair | Type |
|---|---|---|
| Binance | EGLD/USDT | CEX spot |
| Kraken | EGLD/USD | CEX spot |
| Upbit | EGLD/KRW | CEX spot (Korea) |
| Bitget | EGLD/USDT | CEX spot |
| KuCoin | EGLD/USDT | CEX spot |
| Crypto.com Exchange | EGLD/USD | CEX spot |
| xExchange (MultiversX DEX) | EGLD pairs | DEX / on-chain |

EGLD has broad CEX coverage including Binance, Kraken, and the Korean Upbit KRW pair (it was a Binance Launchpad IEO project), plus native on-chain liquidity via the MultiversX ecosystem DEX (xExchange). ~$3.74M 24h volume against an ~$87M cap is light turnover (~4% of cap), implying meaningful slippage on larger orders in the current extreme-fear regime.

**Derivatives.** No active perpetual/derivatives listing on [[hyperliquid]] is recorded in the current snapshot. EGLD perps have historically traded on major CEX futures venues but with modest open interest; [[funding-rate]] and OI are not a primary price driver. Confirm live perp depth on-venue before sizing.

---

## Technology & Consensus

MultiversX is a sharded [[layer-1]] using **Secure Proof-of-Stake (SPoS)** consensus. Its core technical claim is **Adaptive State Sharding**, which parallelizes the network across three dimensions:

- **Network sharding** — partitioning nodes into shards.
- **Transaction sharding** — distributing transactions across shards for parallel processing.
- **State sharding** — splitting the ledger state itself across shards.

The team reports throughput of up to ~100,000 transactions per second, ~6-second latency, and ~$0.002 transaction cost. The architecture is designed to scale capacity as more nodes join, while SPoS guarantees that all shards remain connected and secured.

---

## Use Case, Narrative & Category

MultiversX positions itself as a **high-throughput L1 for the "new internet"** — spanning DeFi, real-world assets, and the metaverse — and has more recently leaned into an **AI** narrative (AI Framework / agent tooling categories). It competes with [[ethereum]] and other scalable [[layer-1]] platforms on the strength of its sharding architecture and low fees.

---

## Valuation Framing (qualitative)

EGLD's valuation case rests almost entirely on **demand-side adoption** rather than supply mechanics: its near-fully-circulating, supply-capped tokenomics remove the dilution overhang that plagues newer launches, but its TVL, developer mindshare, and on-chain activity have lagged the larger scalable-L1 field for several cycles. Trading at a ~$87M cap and effectively at its all-time low, the market is pricing MultiversX as a high-throughput chain that has not converted its technical claims (sharding, ~100k TPS) into durable usage. A re-rating would likely require a verifiable inflection in active addresses / TVL or traction on the newer AI-agent narrative. Repeated repositioning (DeFi → metaverse → AI) is a double-edged signal: it shows adaptability but can read as a project searching for product-market fit.

---

## Peer Comparison

| Asset | Ticker | Mkt-cap rank | Scaling approach | Consensus | Supply | From ATH |
|---|---|---|---|---|---|---|
| **MultiversX** | EGLD | #295 | Adaptive State Sharding | SPoS ([[proof-of-stake]]) | Capped ~31.4M | -99.5% |
| [[ethereum]] | ETH | top 2 | Rollup-centric (L2s) | PoS | ~Net-flat | below ATH |
| [[solana]] | SOL | top 10 | Monolithic high-TPS | PoS (PoH) | Inflationary | below ATH |
| [[movement]] | MOVE | #467 | Move-language modular L2 | PoS | 10B cap, ~40% circ. | -99.2% |

EGLD is a mid-small-cap sharded L1 whose cleanest differentiator versus the cohort is its capped, fully-circulating supply — but it carries the weakest relative adoption profile of the group.

---

## Notable History

- Launched as **Elrond** in 2020; rebranded to **MultiversX** in late 2022, pivoting messaging toward the metaverse and broader Web3.
- Raised via a Binance Launchpad IEO.
- All-time high of **$545.64** on 2021-11-23; down ~99.5% from that peak. A fresh **all-time low of $2.70 was set on 2026-06-06** during the broad small-cap bear; EGLD trades only fractionally above it as of the 2026-06-21 snapshot.

---

## Risks

- **Adoption gap:** despite strong throughput claims, TVL and developer mindshare lag larger L1s.
- **Narrative drift:** repeated repositioning (DeFi → metaverse → AI) can dilute focus.
- **Light liquidity:** ~$3.74M daily volume (~4% of cap) increases slippage risk in the current extreme-fear regime.
- **At all-time lows:** EGLD is trading essentially at its ATL ($2.70, 2026-06-06), with no demonstrated price-trend support.
- **Bear-market beta:** as a small-cap alt (rank #295), EGLD is highly sensitive to the prevailing market downturn (F&G 23).

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[solana]]
- [[movement]]
- [[layer-1]]
- [[proof-of-stake]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
