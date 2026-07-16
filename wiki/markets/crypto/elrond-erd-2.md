---
title: "MultiversX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["EGLD", "Elrond"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://multiversx.com/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[oi-confirmed-trend]]", "[[liquidation-cascade-fade]]"]
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

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EGLD |
| **Market Cap Rank** | #275 |
| **Market Cap** | $93.83M |
| **Current Price** | $3.09 |
| **Categories** | Artificial Intelligence (AI), Smart Contract Platform, Layer 1 (L1), Binance Launchpad, Proof of Stake (PoS), AI Framework |
| **Website** | [https://multiversx.com/](https://multiversx.com/) |

---

## Overview

What is MultiversX 

MultiversX is a blockchain protocol that offers true horizontal scalability by using all aspects of sharding (Network, Transaction &amp; State). The project describes itself as a technology ecosystem for the new internet, which includes decentralized finance, real world assets and the Metaverse. Its smart contracts execution platform is reportedly capable of up to 100,000 transactions per second, 6-second latency and a $0.002 transaction cost. MultiversX is governed and secured through the EGLD token. EGLD, or Electronic Gold, is MultiversX's native token. It acts as a store of value currency to pay for network usage. The coin also serves as a medium of exchange between platform users and validators. Users pay transaction fees in EGLD and validators participate in the consensus process. EGLD allows developers to deploy smart contracts, protocols, and dApps on the platform. It empowers participants to perform any network action. Through staking and validation rewards, as well as transaction fees, EGLD manages the MultiversX network. Plus, EGLD is endowed with the functionality of a governance token, so its holders can vote on network decisions. 

How does MultiversX Work 

According to the MultiversX crypto team, the project implements three types of parallelization: state, transactions, and network, using the parallel processing method to speed up the time and increase the number of transactions. MultiversX uses Adaptive State Sharding to scale while sharing infrastructure to support a growing number of applications/transactions on the ledger. A variation of the traditional PoS operational protocol guarantees the connection to the platform of all sections of the network, separated during sharding. Hence, the integrated environment is involved in the development of dApps, which are imitations of products and services. MultiversX combines three sharding methods to create its own unique adaptive one. It divides the network into four shards: three b...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 30.36M EGLD |
| **Total Supply** | 30.36M EGLD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $93.83M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $545.64 (2021-11-23) |
| **Current vs ATH** | -99.43% |
| **All-Time Low** | $2.43 (2026-06-26) |
| **Current vs ATL** | +27.16% |
| **24h Change** | -7.43% |
| **7d Change** | +0.13% |
| **30d Change** | +1.41% |
| **1y Change** | -80.70% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | EGLD/USDT | N/A |
| Kraken | EGLD/USD | N/A |
| Upbit | EGLD/KRW | N/A |
| Bitget | EGLD/USDT | N/A |
| KuCoin | EGLD/USDT | N/A |
| Crypto.com Exchange | EGLD/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://multiversx.com/](https://multiversx.com/) |
| **Twitter** | [@MultiversX](https://twitter.com/MultiversX) |
| **Reddit** | [https://www.reddit.com/r/elrondnetwork/](https://www.reddit.com/r/elrondnetwork/) |
| **Telegram** | [MultiversX](https://t.me/MultiversX) (32,810 members) |
| **Discord** | [https://discord.com/invite/multiversxbuilders](https://discord.com/invite/multiversxbuilders) |
| **GitHub** | [https://github.com/multiversx/mx-chain-go](https://github.com/multiversx/mx-chain-go) |
| **Whitepaper** | [https://assets-global.website-files.com/6597cc7be68d63ec0c8ce338/65b22e7c42f65345c285ccb8_multiversx-whitepaper.pdf](https://assets-global.website-files.com/6597cc7be68d63ec0c8ce338/65b22e7c42f65345c285ccb8_multiversx-whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.32M |
| **Market Cap Rank** | #275 |
| **24h Range** | $3.06 — $3.34 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

EGLD is tradable on [[binance]] as both **spot** (EGLD/USDT) and a **USD-margined perpetual** ([[perpetual-futures]]), which exposes [[funding-rate]], open interest, and liquidation data on the primary leveraged venue. It is **not** listed on [[hyperliquid]], so Binance is effectively the only deep leveraged venue — leveraged flow, funding signals, and cascade dynamics all concentrate there. This single-venue concentration means execution and sizing should account for thinner cross-venue perp depth than top-cap alts: modest 24h spot turnover (~4% of cap) plus one dominant perp book implies wider effective spreads and slippage on larger clips, and funding/OI reads are only as reliable as Binance's own book. Size positions to the Binance order book, and confirm live perp depth on-venue before committing size, since venue availability — not just spot liquidity — governs how much leverage can be deployed cleanly.

### Applicable strategies

- [[oi-confirmed-trend]] — with all EGLD perp leverage concentrated on Binance, rising open interest alongside directional price gives a cleaner single-venue confirmation of trend participation.
- [[liquidation-cascade-fade]] — thin, single-venue perp depth makes EGLD prone to over-extended liquidation wicks near its all-time low, offering fade entries once forced flow exhausts.
- [[funding-rate-harvest]] — a supply-capped, low-turnover alt can see funding drift persistently one-sided on Binance, letting a delta-neutral spot-vs-perp position collect the carry.
- [[cash-and-carry]] — Binance spot plus USD-M perp lets a trader lock the spot/perp basis on EGLD when the perp trades rich to spot, a clean market-neutral carry.
- [[range-mean-reversion]] — trading fractionally above its ATL with soft demand, EGLD tends to chop in a compressed range, favoring reversion entries at band extremes over trend chasing.
- [[breakout-and-retest]] — a low-float, capped-supply name basing near all-time lows can produce sharp breakouts on any adoption/narrative inflection; entering on the retest filters false starts.

### Volatility & regime character

EGLD is a **mid-small-cap sharded L1 / infra token** (rank ~276) with high beta to the broad crypto risk cycle and strong correlation to BTC/ETH direction — it sells off hard in bear regimes and offers little idiosyncratic support when trading near its all-time low. It is not a memecoin and lacks reflexive social-driven pumps; instead its moves are dominated by market beta and occasional narrative repricing (DeFi → metaverse → AI-agent). Realized volatility is elevated in absolute terms but its low turnover means moves can be gappy and liquidity-driven rather than smoothly trending.

### Risk flags

- **Venue/liquidity concentration:** leveraged trading concentrates on Binance with no Hyperliquid perp; light spot turnover (~4% of cap) amplifies slippage and gap risk.
- **Narrative dependence:** repeated repositioning (DeFi → metaverse → AI) means re-rating hinges on an unproven adoption/narrative catalyst rather than durable usage.
- **Trend-support absence:** trading essentially at its all-time low with no demonstrated price-trend floor increases downside-continuation risk.
- **Emissions:** supply is near-fully-circulating under a hard cap (~31.4M), so unlock overhang is minimal — but declining staking issuance is a mild structural sell source.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=EGLDUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=EGLDUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=EGLD` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=EGLD` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=EGLDUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=EGLDUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=EGLD"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---
