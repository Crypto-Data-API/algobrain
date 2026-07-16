---
title: "Synapse"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["SYN"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://synapseprotocol.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[oi-confirmed-trend]]", "[[liquidation-cascade-fade]]"]
---

# Synapse

**Synapse** (SYN) is a cross-chain layer ∞ protocol powering frictionless interoperability between blockchains. It ranks **#427** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SYN |
| **Market Cap Rank** | #427 |
| **Market Cap** | $50.92M |
| **Current Price** | $0.2324 |
| **Categories** | Bridge Governance Tokens, Intent |
| **Website** | [https://synapseprotocol.com](https://synapseprotocol.com) |

---

## Overview

Synapse is a cross-chain layer ∞ protocol powering frictionless interoperability between blockchains. 
By providing decentralized, permissionless transactions between any L1, sidechain, or L2 ecosystem, Synapse powers integral blockchain activities such as asset transfers, swaps, and generalized messaging with cross-chain functionality - and in so doing enables new primitives based off of its cross-chain architecture.
At Synapse you can bridge and swap stable assets between chains and provide liquidity to fuel cross-chain swapping in pools with minimal impermanent loss.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 219.07M SYN |
| **Total Supply** | 250.00M SYN |
| **Max Supply** | 250.00M SYN |
| **Fully Diluted Valuation** | $58.11M |
| **Market Cap / FDV Ratio** | 0.88 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.92 (2021-10-24) |
| **Current vs ATH** | -95.29% |
| **All-Time Low** | $0.0274 (2026-06-11) |
| **Current vs ATL** | +745.45% |
| **24h Change** | -15.92% |
| **7d Change** | -35.04% |
| **30d Change** | +355.11% |
| **1y Change** | +79.80% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x0f2d719407fdbeff09d87557abb7232601fd9f29` |
| Base | `0x432036208d2717394d2614d6697c46df3ed69540` |
| Fantom | `0xe55e19fb4f2d85af758950957714292dac1e25b2` |
| Polygon Pos | `0xf8f9efc0db77d8881500bb06ff5d6abc3070e695` |
| Binance Smart Chain | `0xa4080f1778e69467e905b8d6f72f6e441f9e9484` |
| Arbitrum One | `0x080f6aed32fc474dd5717105dba5ea57268f46eb` |
| Optimistic Ethereum | `0x5a5fff6f753d7c11a56a52fe47a177a87e431655` |
| Avalanche | `0x1f1e7c893855525b303f99bdf5c3c05be09ca251` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SYN/USDT | N/A |
| Kraken | SYN/USD | N/A |
| KuCoin | SYN/USDT | N/A |
| Crypto.com Exchange | SYN/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X0F2D719407FDBEFF09D87557ABB7232601FD9F29/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://synapseprotocol.com](https://synapseprotocol.com) |
| **Twitter** | [@SynapseProtocol](https://twitter.com/SynapseProtocol) |
| **Telegram** | [synapseprotocol](https://t.me/synapseprotocol) (3,521 members) |
| **GitHub** | [https://github.com/synapsecns](https://github.com/synapsecns) |
| **Whitepaper** | [https://docs.hypercall.xyz/](https://docs.hypercall.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $20.53M |
| **Market Cap Rank** | #427 |
| **24h Range** | $0.2305 — $0.2764 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

SYN is tradable on **Binance** — both spot (SYN/USDT) and a **USD-margined perpetual**, which exposes funding rates, open interest, and liquidation flow. It is **not** listed on Hyperliquid, so Binance is the primary leveraged venue and the reference source for derivatives signals. With a small-cap ($50M) market cap and a thin ~$20M daily volume concentrated on a handful of CEXs, order books are shallow: leverage is available but slippage and liquidation risk scale quickly on size. Execution should favor limit orders, staggered entries, and conservative position sizing; the concentration of leveraged liquidity in a single venue means funding and OI on Binance drive the whole market, and any Binance outage or listing change would sharply degrade tradability.

### Applicable strategies

- [[funding-rate-harvest]] — a single dominant perp venue (Binance) makes SYN funding swings harvestable via delta-neutral spot-vs-perp positioning when rates run persistently one-sided.
- [[oi-confirmed-trend]] — SYN's +355% 30d move shows it trends hard; pairing price breaks with rising Binance open interest filters genuine continuation from thin-book noise.
- [[liquidation-cascade-fade]] — shallow books plus leveraged perps make SYN prone to sharp forced-liquidation wicks that mean-revert, offering fade entries after cascades exhaust.
- [[breakout-and-retest]] — low-float small-cap with violent expansions rewards trading confirmed range breakouts and retests rather than chasing extended candles.
- [[narrative-trading]] — as a cross-chain bridge/interop token, SYN reprices on interoperability and DeFi bridging narratives, giving tradable catalyst-driven moves.
- [[volatility-targeting]] — extreme swings (-16% 24h, +355% 30d) demand position sizing scaled inversely to realized volatility to keep risk bounded.

### Volatility & regime character

SYN is a small-cap DeFi infrastructure token (cross-chain bridge/interoperability) with high beta to the broader alt market and elevated idiosyncratic volatility. Its low float and modest liquidity produce reflexive, momentum-driven moves — parabolic rallies and equally sharp drawdowns (the +355% 30d against a -35% 7d illustrates the whipsaw). Directionally it tends to correlate with BTC/ETH risk-on regimes but amplifies both up and down moves, and it is highly sensitive to DeFi and bridging narrative rotations.

### Risk flags

- **Liquidity/venue concentration** — thin volume and leveraged trading concentrated on Binance; single-venue dependence heightens execution and gap risk.
- **Small-cap fragility** — a ~$50M cap and low daily turnover mean large orders move price materially and stops can slip.
- **Narrative dependence** — valuation hinges on cross-chain/bridge interoperability sentiment, which can reverse quickly.
- **Bridge/protocol risk** — as a bridge governance token, SYN carries smart-contract and cross-chain exploit exposure that can trigger abrupt repricing.
- **High MC/FDV proximity** — most supply is circulating (MC/FDV 0.88), limiting future unlock overhang but leaving little emission cushion for demand shocks.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SYNUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SYNUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SYN` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SYN` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SYNUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SYNUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SYN"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
