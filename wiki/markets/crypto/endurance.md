---
title: "Fusionist"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins]
aliases: ["ACE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://link3.to/fusionist_io"
related: ["[[crypto-markets]]", "[[bnb]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[basis-trading]]"]
---

# Fusionist

**Fusionist** (ACE) is a AAA game that we have developed independently.

The client utilizes the Unity engine, with the rendering segment employing the HDRP (High Definition Render Pipeline) to achieve AAA visual effects.

The networking segment adopts real-time synchronization technology (KCP + flatbuffer protocol), and all computation results are determined by the backend to ensure there's no possibility of cheating.

Additionally, we have developed a lightweight client using Unity WebGL technology, whi It ranks **#1329** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ACE |
| **Market Cap Rank** | #1329 |
| **Market Cap** | $7.29M |
| **Current Price** | $0.0696 |
| **Categories** | Gaming (GameFi), NFT, Binance Launchpool, RPG, Strategy Games |
| **Website** | [https://link3.to/fusionist_io](https://link3.to/fusionist_io) |

---

## Overview

Fusionist is a AAA game that we have developed independently.

The client utilizes the Unity engine, with the rendering segment employing the HDRP (High Definition Render Pipeline) to achieve AAA visual effects.

The networking segment adopts real-time synchronization technology (KCP + flatbuffer protocol), and all computation results are determined by the backend to ensure there's no possibility of cheating.

Additionally, we have developed a lightweight client using Unity WebGL technology, which can run on PCs or mobile devices, ensuring the maximization of user reachability.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 104.68M ACE |
| **Total Supply** | 146.31M ACE |
| **Max Supply** | 147.00M ACE |
| **Fully Diluted Valuation** | $10.19M |
| **Market Cap / FDV Ratio** | 0.72 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $16.73 (2023-12-21) |
| **Current vs ATH** | -99.58% |
| **All-Time Low** | $0.0682 (2026-07-13) |
| **Current vs ATL** | +2.07% |
| **24h Change** | -1.33% |
| **7d Change** | -4.75% |
| **30d Change** | -19.63% |
| **1y Change** | -87.63% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xc27a719105a987b4c34116223cae8bd8f4b5def4` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ACE/USDT | N/A |
| Bitget | ACE/USDT | N/A |
| KuCoin | KACE/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://link3.to/fusionist_io](https://link3.to/fusionist_io) |
| **Twitter** | [@fusionistio](https://twitter.com/fusionistio) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.18M |
| **Market Cap Rank** | #1329 |
| **24h Range** | $0.0689 — $0.0720 |
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

ACE trades on **both Binance and Hyperliquid**, giving it a genuine two-venue derivatives market rather than a single-exchange listing:

- **Binance** — spot (ACE/USDT) plus a USD-margined perpetual, providing the primary reference price and the deepest centralized liquidity.
- **Hyperliquid** — the on-chain `ACE-PERP` contract supports leverage up to roughly **40-50x**, with transparent on-chain order-book depth and funding.

The dual listing means execution can be split across CEX and DEX books, and cross-venue price/funding differences are directly observable and tradable. Because ACE is a small-cap (rank ~1325, thin dollar volume), the two-venue depth is helpful but still shallow in absolute terms — size positions conservatively, use limit orders, and expect slippage on market fills. The parallel Binance perp and Hyperliquid perp make CEX-vs-DEX funding and basis relationships the cleanest structural edge here.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — ACE runs simultaneously on the Binance perp and Hyperliquid `ACE-PERP`, so funding can diverge between the two venues and be harvested market-neutral.
- [[cash-and-carry]] — Binance spot plus a USD-margined perp lets you hold spot ACE against a short perp to capture positive funding/basis on a low-float token.
- [[basis-trading]] — persistent spot-vs-perp basis on a thin small-cap like ACE can be traded against, with both legs available on Binance.
- [[crowded-long-funding-fade]] — on a beaten-down GameFi token, speculative long crowding can push funding to extremes; fading over-heated funding is a defined-edge play.
- [[liquidation-cascade-fade]] — high leverage (40-50x) on a low-liquidity perp makes ACE prone to sharp liquidation wicks that mean-revert, offering fade opportunities.
- [[range-mean-reversion]] — deep in its post-ATH downtrend, ACE frequently chops in tight ranges where reversion between support and resistance can be scalped.

### Volatility & regime character

ACE is a **small-cap GameFi / NFT infrastructure token** with high-beta, reflexive price behavior. Sitting more than 99% below its 2023 all-time high and near all-time lows, it exhibits large percentage swings on modest flow. As a low-float alt it is strongly correlated to broad crypto risk appetite and tends to amplify BTC/ETH beta on the downside — outsized drawdowns in risk-off regimes and sharp, short-lived squeezes on relief rallies. Regime is currently distributional/downtrending, so trend-continuation and mean-reversion setups dominate over sustained momentum.

### Risk flags

- **Liquidity & venue concentration** — thin dollar volume; despite two venues, depth is limited and slippage/gap risk is elevated on size.
- **High-leverage cascade risk** — 40-50x Hyperliquid leverage on a shallow book invites violent liquidation-driven wicks in both directions.
- **Supply overhang** — circulating supply is well below max supply, so future emissions/unlocks can pressure price; monitor float expansion.
- **Narrative dependence** — as a GameFi/NFT token, price is heavily tied to gaming-sector sentiment and can stay illiquid through quiet narrative periods.
- **Perp funding dislocations** — small OI means funding can spike or invert quickly; crowded positioning can force painful funding payments before any mean reversion.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=ACE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=ACE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=ACE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=ACE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=ACE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
