---
title: "Zilliqa"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ZIL"]
entity_type: protocol
founded: 2019
headquarters: "Decentralized"
website: "https://www.zilliqa.com/"
related: ["[[bitcoin]]", "[[bnb]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[layer-2]]", "[[proof-of-stake]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Zilliqa

**Zilliqa** (ZIL) is a [[layer-1]] smart-contract blockchain built around **sharding**, designed to scale transaction throughput far beyond first-generation chains like [[bitcoin]] and [[ethereum]]. Launched in 2017 (mainnet 2019), it was one of the first public blockchains to ship network/transaction sharding in production, splitting validators into parallel groups to process transactions concurrently. ZIL is the native token.

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | ZIL |
| **Current Price** | $0.00312041 |
| **Market Cap** | $60,950,478 |
| **Market Cap Rank** | #392 |
| **24h Volume** | $5,841,053 |
| **24h Change** | +0.20% |
| **7d Change** | -1.70% |
| **Fully Diluted Valuation** | ~$65.5M |
| **Market Cap / FDV** | ~0.93 |
| **All-Time High** | $0.255376 (2021-05-06), ~-98.8% |
| **All-Time Low** | $0.00239616 |
| **Genesis Date** | 2019-01-31 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), BNB Chain Ecosystem, GMCI Layer 1 Index |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** The 2026-06-21 snapshot sits in an *Established Bear Market* with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **~23 (extreme fear)** and [[bitcoin]] dominance near 59%. ZIL was roughly flat over 24h (+0.2%) and modestly down on the week (-1.7%), and remains ~98.8% below its 2021 all-time high of $0.255376 while trading ~30% above its all-time low.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~19.51B ZIL |
| **Total Supply** | ~20.49B ZIL |
| **Max Supply** | 21.00B ZIL |
| **Fully Diluted Valuation** | ~$65.5M |
| **Market Cap / FDV Ratio** | ~0.93 |

ZIL has a hard cap of **21 billion** tokens and is near-fully circulating (MC/FDV ≈ 0.93), so **dilution overhang is small** — only ~7% of the capped supply remains to be issued. The network rewards stakers/validators with newly issued ZIL up to the cap, and ZIL holders can stake (including via seed nodes and staking partners) to earn yield while contributing to network security. ZIL pays for transaction fees and gas, and is used for governance participation. Notably ZIL shares its 21-billion cap symbolism with [[bitcoin]]'s 21-million cap, though the economics are unrelated.

---

## How & Where It Trades

### Spot venues

| Exchange | Pair |
|---|---|
| Binance | ZIL/USDT |
| Upbit | ZIL/KRW |
| Bitget | ZIL/USDT |
| KuCoin | ZIL/USDT |
| Crypto.com Exchange | ZIL/USD |

ZIL trades on major CEXs including Binance and the Korean Upbit KRW pair. A bridged BEP-20 representation also exists on [[bnb|BNB Chain]] (`0xb86abcb37c3a4b64f74f59301aff131a1becc787`). ~$5.8M in 24h volume at the snapshot is moderate for a small-cap (a turnover of ~9.6% of cap, healthier than several peers in this batch). No active perpetual/derivatives listing on [[hyperliquid]] is recorded in the current snapshot, so leveraged exposure is constrained.

---

## Technology & Consensus

Zilliqa is a [[layer-1]] chain whose defining feature is **sharding**:

- **Network & transaction sharding:** validators are partitioned into smaller groups (shards); transactions are distributed across shards so that consensus can be reached and transactions verified in parallel, raising throughput roughly linearly with the number of shards.
- **Practical Byzantine Fault Tolerance (pBFT)** is used within shards for finality, combined with proof-of-work historically used only for Sybil resistance / shard assignment; the network has moved toward staking-based participation over time.
- **Scilla:** Zilliqa uses its own smart-contract language, *Scilla*, designed with safety and formal-verification properties in mind.

The architecture is intended so that capacity scales as more nodes join, rather than congesting like non-sharded chains.

---

## Use Case, Narrative & Category

Zilliqa's narrative is **scalability via sharding** — a third-generation [[layer-1]] aiming to deliver high throughput, low fees, and predictable performance for dApps and DeFi. It competes with [[ethereum]] and other scalable smart-contract platforms, and has explored gaming and Web3 verticals. It carries a "Made in China" association and is indexed in GMCI Layer-1 baskets. The longer-term roadmap (Zilliqa 2.0) has targeted a move to a more conventional [[proof-of-stake]] account model with EVM compatibility, aiming to reduce friction for [[ethereum]] developers — though execution against far larger L1/[[layer-2]] ecosystems remains the central question.

---

## Valuation Framing (Qualitative)

- **Near-fully-diluted micro-cap:** with MC/FDV ≈ 0.93, ZIL's circulating cap (~$61M) is close to its FDV (~$65.5M), so unlike high-FDV tokens there is little hidden dilution — what you see is roughly what you get on the supply side.
- **First-mover-discount:** ZIL was an early production sharding chain, but the "scalability narrative" premium it once commanded has been arbitraged away as dozens of L1s and rollups now offer comparable or better throughput. The current cap prices ZIL as a legacy small-cap rather than a frontier scaling bet.
- **Deep ATH drawdown:** ~98.8% below the 2021 peak; the market is pricing minimal probability of recapturing prior relevance absent a successful Zilliqa 2.0 relaunch and renewed developer inflow.

---

## Peer Comparison

| Token | Category | Price | Market Cap | Rank | MC/FDV | Max Supply |
|---|---|---|---|---|---|---|
| **Zilliqa (ZIL)** | Sharded [[layer-1]] | $0.00312 | ~$61.0M | #392 | ~0.93 | 21.0B |
| [[qtum\|Qtum (QTUM)]] | UTXO+EVM [[layer-1]] | $0.7239 | ~$76.8M | #326 | ~0.98 | Uncapped |
| [[metal-blockchain\|Metal (METAL)]] | Avalanche-fork [[layer-1]] | $0.1247 | ~$63.3M | #379 | ~0.76 | 666.67M |
| [[proton\|XPR Network (XPR)]] | DPoS [[layer-1]] payments | $0.00225 | ~$64.3M | #375 | ~0.89 | Uncapped |

*All figures from the 2026-06-21 snapshot. The four are clustered tightly between ~$61M and ~$77M — a band of legacy small-cap [[layer-1]] smart-contract platforms. ZIL has the highest supply-side certainty (capped, high MC/FDV) but the lowest market-cap rank of the group.*

---

## Notable History

- Founded/ICO in 2017; mainnet genesis 2019-01-31.
- One of the earliest production deployments of sharding on a public blockchain.
- All-time high of **$0.255376** on 2021-05-06; price is down ~98.8% from that peak as of the 2026-06-21 snapshot.

---

## Risks

- **Competition & relevance:** sharding is now offered by many L1s and L2s; ZIL's early-mover edge has eroded.
- **Liquidity:** ~$5.8M daily volume on a sub-$0.01 micro-priced token amplifies volatility and slippage in the current extreme-fear regime.
- **Adoption gap:** TVL and developer mindshare lag larger ecosystems.
- **Bear-market beta:** as a small-cap alt (rank #392), ZIL is highly sensitive to the prevailing market downturn (Crypto [[fear-and-greed-index|Fear & Greed]] ~23, extreme fear).
- **Execution risk:** the Zilliqa 2.0 / EVM-compatibility transition is a multi-year migration whose success is not guaranteed.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Trading Profile

### Venues & liquidity

ZIL is tradable on [[binance]] as both **spot** (ZIL/USDT) and a **USD-margined perpetual**, exposing standard derivatives telemetry — [[funding-rate|funding]], [[open-interest]], and [[liquidations]]. It is **not** listed on [[hyperliquid]], so Binance is effectively the primary leveraged venue and the dominant price-discovery hub for ZIL futures. This single-venue concentration for leverage means funding, OI, and liquidation dynamics are best read directly off Binance rather than aggregated across DEX perps. With a sub-$0.01 nominal price and ~$5.8M spot 24h volume, the order book is thin: leveraged positions and larger clips should be sized conservatively, executed with limit/passive fills or [[vwap-trading|VWAP]] slicing, and stress-tested for slippage, since even moderate flow can move price and cascade liquidations.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on ZIL when the perpetual trades at a persistent premium/discount, hedged against spot to isolate the carry.
- [[cash-and-carry]] — pair long ZIL/USDT spot against a short Binance perp to lock the basis when funding/basis is favorable on this near-fully-diluted small-cap.
- [[liquidation-cascade-fade]] — thin liquidity and clustered leverage on the sole Binance venue make ZIL prone to sharp liquidation flushes that overshoot and mean-revert.
- [[oi-confirmed-trend]] — use Binance open-interest expansion to validate directional moves and filter low-conviction chop in a micro-cap that whipsaws easily.
- [[rsi-mean-reversion]] — extreme-fear regime and range-bound micro-cap behavior favor fading stretched RSI readings back toward the mean.
- [[breakout-and-retest]] — trade confirmed breaks of the tight consolidation range with a retest entry to reduce false-breakout risk on a low-float, headline-sensitive name.

### Volatility & regime character

ZIL is a **legacy small-cap [[layer-1]]** (rank ~#392) with high beta to broad crypto risk and strong correlation to [[bitcoin]]/[[ethereum]] direction. As a sub-$0.01 micro-priced infra token it exhibits sharp, reflexive moves on thin books, amplified in the current *Established Bear Market / extreme-fear* regime. It is not a memecoin but trades with small-cap reflexivity: sensitive to BTC dominance shifts, altseason rotation, and Zilliqa-specific catalysts (e.g., the Zilliqa 2.0 / EVM roadmap).

### Risk flags

- **Venue/liquidity concentration:** leveraged exposure hinges on a single venue (Binance); no Hyperliquid fallback, and thin spot depth magnifies slippage and cascade risk.
- **Small-cap beta:** highly sensitive to macro downturns and BTC-dominance regimes; deep ~98.8% ATH drawdown reflects structurally weak demand.
- **Narrative dependence:** valuation leans on the sharding / Zilliqa 2.0 relaunch narrative competing against far larger L1/L2 ecosystems.
- **Emissions:** near-fully-diluted (MC/FDV ≈ 0.93) limits dilution overhang, but residual staking issuance toward the 21B cap remains a mild supply drift.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ZILUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ZILUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ZIL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ZIL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ZILUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ZILUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ZIL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[layer-2]]
- [[proof-of-stake]]
- [[bnb]]
- [[qtum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZIL |
| **Market Cap Rank** | #393 |
| **Market Cap** | $57.95M |
| **Current Price** | $0.00296967 |
| **Genesis Date** | 2019-01-31 |
| **Hashing Algorithm** | Ethash |
| **Categories** | Smart Contract Platform, Made in China |
| **Website** | [https://www.zilliqa.com/](https://www.zilliqa.com/) |

---

## Overview

Zilliqa (ZIL) is a token developed in the year 2017. Zilliqa is mainly based on the concept of Sharding and primarily aims at improving the scalability of the cryptocurrency networks as in case of Bitcoin or Ethereum. The white paper mentions that the transactions speed would be approximately a thousand times more than that of Ethereum network. Ziliqa is fast, secured and decentralized. Zilliqa’s high throughput means that you can focus on developing your ideas without worrying about network congestion, high transaction fees or security which are the key issues with legacy blockchain platforms. Zilliqa network uses a concept called Sharding where the transactions are grouped into smaller groups and divided among the miners for the parallel transactional verification. Developing smaller groups for transactional verification means the Consensus can be reached faster and hence a higher number of transactions can be processed in a given time frame. The capacity of the network linearly increases in other cryptocurrencies as the number of people joins the network, but in this case, the capacity is increased at a higher variable rate than the number of members joining the network. By incorporating the Sharding Technology, it can completely revolutionize the smart contract functionality too. Ziliqa has few pros as it has a great new technology. Zilliqa is the first platform to use sharding technology. This puts it ahead of the rest of the market. It’s a completely new kind of blockchain designed to solve the problem of scalability. Third-generation platforms like Zilliqa could be the big winners in the future of cryptocurrency. Ziliqa has a strong community. The platform has a lot of fans. The Zilliqa ICO only happened because there was so much demand for it. The Zilliqa ICO also shows that the crypto community is ready to see blockchain technology move to the next phase of its development.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 19.51B ZIL |
| **Total Supply** | 20.52B ZIL |
| **Max Supply** | 21.00B ZIL |
| **Fully Diluted Valuation** | $60.93M |
| **Market Cap / FDV Ratio** | 0.95 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2554 (2021-05-06) |
| **Current vs ATH** | -98.84% |
| **All-Time Low** | $0.00239616 (2020-03-13) |
| **Current vs ATL** | +24.03% |
| **24h Change** | -0.74% |
| **7d Change** | -1.81% |
| **30d Change** | -9.79% |
| **1y Change** | -76.72% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xb86abcb37c3a4b64f74f59301aff131a1becc787` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZIL/USDT | N/A |
| Upbit | ZIL/KRW | N/A |
| Bitget | ZIL/USDT | N/A |
| KuCoin | ZIL/USDT | N/A |
| Crypto.com Exchange | ZIL/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.zilliqa.com/](https://www.zilliqa.com/) |
| **Twitter** | [@zilliqa](https://twitter.com/zilliqa) |
| **Reddit** | [https://www.reddit.com/r/zilliqa/](https://www.reddit.com/r/zilliqa/) |
| **Telegram** | [zilliqachat](https://t.me/zilliqachat) (11,112 members) |
| **GitHub** | [https://github.com/Zilliqa/Zilliqa](https://github.com/Zilliqa/Zilliqa) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,129 |
| **GitHub Forks** | 287 |
| **Commits (4 weeks)** | 12 |
| **Pull Requests Merged** | 3,032 |
| **Contributors** | 62 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.56M |
| **Market Cap Rank** | #393 |
| **24h Range** | $0.00295860 — $0.00304213 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
