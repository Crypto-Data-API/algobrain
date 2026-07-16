---
title: "Ankr Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, depin, perpetual-futures, funding-rate, open-interest, derivatives, defi, altcoins]
aliases: ["ANKR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.ankr.com/"
related: ["[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[momentum-investing]]"]
---

# Ankr Network

**Ankr Network** (ticker **ANKR**) is the token of a Web3 decentralized infrastructure provider that delivers RPC endpoints, node hosting, and liquid-staking services across [[ethereum|Ethereum]] and dozens of other chains. The ANKR token is a multi-chain ERC-20-style asset originally launched on Ethereum, now bridged to BNB Chain, Polygon, Arbitrum, Optimism, Avalanche, Fantom, Linea, Scroll, Base/Blast and other ecosystems. Ankr is one of the older [[depin|DePIN]]-adjacent node-infrastructure names, frequently used by developers who need reliable read/write access to multiple blockchains without running their own nodes.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ANKR |
| **Current Price** | $0.00370604 |
| **Market Cap** | $37.06M |
| **Market Cap Rank** | #555 |
| **24h Volume** | $6.93M |
| **24h Change** | +0.11% |
| **7d Change** | -4.62% |
| **Fully Diluted Valuation** | $37.06M |
| **All-Time High** | $0.213513 (2021-04-16) |
| **All-Time Low** | $0.00070728 (2020-03-13) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market is in an **Established Bear Market** with the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] at **≈23 (extreme fear)** as of 2026-06-21. ANKR is roughly flat on the day (+0.1%) and down ~4.6% on the week. Its ~$6.9M of daily turnover against a $37.1M cap means liquidity is thin and slippage-prone for larger orders; the token trades ~98% below its 2021 cycle high of $0.2135.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.00B ANKR |
| **Total Supply** | 10.00B ANKR |
| **Max Supply** | 10.00B ANKR |
| **Market Cap / FDV** | 1.00 |

ANKR has a **fully circulating supply** — circulating equals total equals max at 10B tokens, so market cap and FDV are identical and there is **no future unlock/dilution overhang**. This is a meaningful contrast with the newer AI/DePIN launches (see [[cysic]], [[gensyn]]) whose low circulating-to-total ratios imply heavy forward emissions. The flat supply also means ANKR's price is driven by demand and network usage rather than emission mechanics.

---

## How & Where It Trades

**Centralized spot venues:**

| Exchange | Pair |
|---|---|
| Binance | ANKR/USDT |
| Kraken | ANKR/USD |
| Upbit | ANKR/KRW |
| Bitget | ANKR/USDT |
| KuCoin | ANKR/USDT |
| Crypto.com Exchange | ANKR/USD |

**Decentralized venues:** Uniswap V2/V3 and Sushiswap on Ethereum (ANKR/WETH).

**Derivatives:** ANKR has perpetual-futures listings on major derivatives venues (Binance Futures and others have historically carried ANKR perps), though it is **not** a flagship [[hyperliquid|Hyperliquid]] market and open interest is small relative to large caps. Given the modest spot float, funding and OI are not significant price drivers; treat ANKR primarily as a spot instrument.

### Contract Addresses (selected)

| Chain | Address |
|---|---|
| Ethereum | `0x8290333cef9e6d528dd5618fb97a76f268f3edd4` |
| BNB Chain | `0xf307910a4c7bbc79691fd374889b36d8531b08e3` |
| Polygon PoS | `0x101a023270368c0d50bffb62780f4afd4ea79c35` |
| Arbitrum One | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |
| Optimism | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |

---

## Use Case, Narrative & Category

Ankr operates a **decentralized node and RPC infrastructure network** — a [[depin|DePIN]]-style category where independent operators run blockchain nodes and Ankr aggregates them into load-balanced public/private RPC endpoints. Core products:

- **RPC / API services** — multi-chain endpoints for dapps and wallets
- **Node hosting / Validator services** — staking infrastructure and node deployment
- **Liquid staking** — Ankr issues liquid staking tokens; ANKR is the governance token for these systems
- **Rollups-as-a-Service (RaaS)** — appchain/rollup deployment tooling

CoinGecko categorizes ANKR under DePIN, Liquid Staking Governance Tokens, Rollups-as-a-Service, and numerous chain-ecosystem tags. The investment narrative is "picks-and-shovels infrastructure for Web3" — Ankr earns where developers need reliable chain access. It is backed by Pantera Capital and YZi Labs (formerly Binance Labs).

---

## Peer Comparison — Web3 Infrastructure / RPC & Node Tokens

| Project | Token | Niche | Supply structure |
|---|---|---|---|
| **Ankr** | ANKR | Multi-chain RPC, node hosting, liquid staking, RaaS | Fully circulating (10B, cap = FDV); no dilution overhang |
| [[the-graph\|The Graph]] | GRT | Decentralized [[indexing]] / data queries | Fully diluted (cap ≈ FDV); ~3% issuance |
| Pocket Network | POKT | Decentralized RPC relay network | DePIN RPC competitor |
| Alchemy / Infura / QuickNode | (private) | Centralized RPC + dev APIs | Ankr's commercial competition |

Versus centralized RPC giants (Alchemy, Infura), Ankr's pitch is **decentralized, multi-chain, no-vendor-lock-in** access; versus [[the-graph|The Graph]] it sits one layer lower (raw RPC/node access rather than indexed/queryable data). Both share the infra-token problem: heavy product commoditization and weak token fee-capture.

---

## Valuation Framing (qualitative)

- **No dilution, low-cap infra token:** with supply fully circulating (cap = FDV ≈ $37M), ANKR has no unlock overhang — a structural positive versus locked peers like [[spark-2|SPK]] and [[huma-finance|HUMA]]. The flip side is no emission-driven incentive flywheel to bootstrap fresh demand.
- **Commoditized revenue base:** RPC/node access is a low-margin, heavily competed product (Alchemy, Infura, public RPCs), capping the fee-capture story that would justify a re-rate.
- **Narrative beta, not fundamentals:** ANKR re-rates mostly when retagged under a hot theme ([[depin|DePIN]], liquid staking, RaaS) rather than on usage metrics — a speculative, mean-reverting pattern.
- **Deep-cycle value vs value trap:** ~98% below ATH with a clean cap structure makes ANKR a deep-cycle bet on Web3 infra demand recovering; the risk is that RPC commoditization means demand never accrues to the token.

---

## Notable History

- **2021-04-16** — All-time high of $0.2135 during the bull-cycle peak.
- Expanded from an Ethereum-native token into a broad multi-chain footprint (12+ chains) as liquid staking and RaaS products launched.
- Like most 2021-era infrastructure tokens, ANKR has spent the subsequent cycle deeply below its ATH (~-98%), reflecting both broad altcoin drawdown and the commoditization of RPC services.

---

## Risks

- **Thin liquidity** — ~$6.9M daily volume on a ~$37M cap; large orders move price and exits can be costly in stressed markets.
- **Commoditized product** — RPC/node infrastructure is competitive (Alchemy, Infura, QuickNode, public RPCs); margin and differentiation pressure is structural.
- **Hype-cycle exposure** — ANKR is repeatedly retagged under whatever narrative is hot (DePIN, liquid staking, RaaS), which can drive speculative spikes that reverse hard, especially in an extreme-fear regime.
- **Bear-market beta** — as a low-cap altcoin it carries high beta to overall crypto risk-off moves; the current "Established Bear Market" backdrop is a headwind.
- **No unlock overhang** is a positive, but the flip side is no emissions-driven incentive flywheel to bootstrap new demand.

---

## Trading Profile

### Venues & liquidity

ANKR is tradable on **Binance** as both a **spot** market (ANKR/USDT) and a **USD-margined perpetual**, giving it funding, open interest and liquidation data — Binance is the **primary leveraged venue** for the name. It is **not** listed on [[hyperliquid|Hyperliquid]]. Because the perp is USD-M on a single dominant venue, execution and sizing are constrained: leveraged flow, funding and liquidation cascades all concentrate on Binance, so there is no cross-venue perp depth to disperse impact. Combined with a thin spot float (a low-cap token where daily turnover is small relative to cap), this means leverage should be modest, orders worked with limit/VWAP-style execution, and position sizes kept well inside available book depth to avoid slippage and liquidation-driven gaps.

### Applicable strategies

- [[funding-rate-harvest]] — the single-venue Binance USD-M perp lets a delta-neutral book collect funding on ANKR when the perp trades at a persistent premium/discount to spot.
- [[cash-and-carry]] — hold Binance spot ANKR against a short perp to capture basis/funding cleanly, exploiting the fact that spot and perp sit on the same venue.
- [[liquidation-cascade-fade]] — thin liquidity plus concentrated Binance leverage makes ANKR prone to sharp liquidation wicks that overshoot and mean-revert, offering fade entries.
- [[oi-confirmed-trend]] — Binance open-interest changes confirm whether an ANKR move is leverage-driven and sustainable versus a squeeze likely to reverse.
- [[narrative-trading]] — ANKR re-rates on DePIN / liquid-staking / RaaS narrative rotation rather than fundamentals, rewarding positioning around theme cycles.
- [[rsi-mean-reversion]] — as a range-bound, deep-below-ATH low-cap, ANKR frequently reverts from oscillator extremes within its trading band.

### Volatility & regime character

ANKR is a **small-cap DePIN / Web3-infrastructure altcoin** with high beta to broad crypto risk-on/risk-off moves and strong directional correlation to BTC/ETH. It is not a memecoin but exhibits reflexive, narrative-driven spikes (DePIN, liquid staking, RaaS retagging) that tend to mean-revert. With a fully circulating supply and no emission flywheel, price action is demand- and sentiment-led; in the current risk-off regime it behaves as a mean-reverting, range-bound low-cap punctuated by beta-driven trend legs.

### Risk flags

- **Liquidity / venue concentration** — thin spot turnover and leveraged flow concentrated on Binance; large orders move price and stressed exits are costly with no alternative perp venue for depth.
- **Narrative dependence** — re-rates on hot-theme retagging rather than usage; speculative spikes reverse hard, especially in extreme-fear conditions.
- **Commoditization / demand risk** — RPC/node access is a low-margin, heavily competed product, capping fundamental fee-capture that would anchor valuation.
- **High altcoin beta** — outsized drawdowns in broad crypto risk-off; leverage amplifies liquidation risk given single-venue concentration.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ANKRUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ANKRUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ANKR` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ANKR` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ANKRUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ANKRUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ANKR"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[depin]]
- [[the-graph]]
- [[indexing]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ANKR |
| **Market Cap Rank** | #550 |
| **Market Cap** | $36.23M |
| **Current Price** | $0.00362347 |
| **Categories** | Liquid Staking Governance Tokens, DePIN, Rollups-as-a-Service (RaaS), Liquid Staking, Made in USA, Governance |
| **Website** | [https://www.ankr.com/](https://www.ankr.com/) |

---

## Overview

Ankr is a Web3 decentralized infrastructure provider that helps developers, dapps, and stakers easily interact with multiple blockchains. It allows you to create DApps using API and RPC, staking on Ankr Earn, and use customized blockchain solutions for businesses.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.00B ANKR |
| **Total Supply** | 10.00B ANKR |
| **Max Supply** | 10.00B ANKR |
| **Fully Diluted Valuation** | $36.23M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2135 (2021-04-16) |
| **Current vs ATH** | -98.30% |
| **All-Time Low** | $0.00070728 (2020-03-13) |
| **Current vs ATL** | +411.96% |
| **24h Change** | +0.76% |
| **7d Change** | +2.73% |
| **30d Change** | -9.75% |
| **1y Change** | -79.10% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8290333cef9e6d528dd5618fb97a76f268f3edd4` |
| Polygon Zkevm | `0xdf474b7109b73b7d57926d43598d5934131136b2` |
| Linea | `0xa8ae6365383eb907e6b4b1b7e82a35752cc5ef8c` |
| Fantom | `0xdf474b7109b73b7d57926d43598d5934131136b2` |
| Mode | `0xdf474b7109b73b7d57926d43598d5934131136b2` |
| Polygon Pos | `0x101a023270368c0d50bffb62780f4afd4ea79c35` |
| Binance Smart Chain | `0xf307910a4c7bbc79691fd374889b36d8531b08e3` |
| Blast | `0x3580ac35bed2981d6bdd671a5982c2467d301241` |
| Arbitrum One | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |
| Optimistic Ethereum | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |
| Avalanche | `0xdf474b7109b73b7d57926d43598d5934131136b2` |
| Scroll | `0xdf474b7109b73b7d57926d43598d5934131136b2` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ANKR/USDT | N/A |
| Kraken | ANKR/USD | N/A |
| Upbit | ANKR/KRW | N/A |
| Bitget | ANKR/USDT | N/A |
| KuCoin | ANKR/USDT | N/A |
| Crypto.com Exchange | ANKR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X8290333CEF9E6D528DD5618FB97A76F268F3EDD4/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X8290333CEF9E6D528DD5618FB97A76F268F3EDD4/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.ankr.com/](https://www.ankr.com/) |
| **Twitter** | [@ankr](https://twitter.com/ankr) |
| **Reddit** | [https://www.reddit.com/r/Ankrofficial](https://www.reddit.com/r/Ankrofficial) |
| **Telegram** | [ankrnetwork](https://t.me/ankrnetwork) (16,905 members) |
| **Discord** | [https://discord.gg/GGzJ6A6fEg](https://discord.gg/GGzJ6A6fEg) |
| **GitHub** | [https://github.com/Ankr-network](https://github.com/Ankr-network) |
| **Whitepaper** | [https://ankr.com/ankr-whitepaper-2.0.pdf](https://ankr.com/ankr-whitepaper-2.0.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $15.90M |
| **Market Cap Rank** | #550 |
| **24h Range** | $0.00358675 — $0.00386740 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
