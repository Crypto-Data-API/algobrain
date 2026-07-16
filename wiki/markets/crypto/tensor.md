---
title: "Tensor"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["TNSR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.tensor.foundation"
related: ["[[crypto-markets]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[basis-trading]]"]
---

# Tensor

**Tensor** (TNSR) is a cryptocurrency. It ranks **#1118** by market capitalization. The TNSR token governs the protocols underlying Tensor and Vector. 50% of protocol fees from both products accrue to the TNSR treasury.

Tensor launched in July 2022 and is the leading NFT marketplace on Solana, commanding 60-70% of Solana NFT market share.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TNSR |
| **Market Cap Rank** | #1118 |
| **Market Cap** | $10.84M |
| **Current Price** | $0.0324 |
| **Categories** | NFT, NFT Marketplace |
| **Website** | [https://www.tensor.foundation](https://www.tensor.foundation) |

---

## Overview

The TNSR token governs the protocols underlying Tensor and Vector. 50% of protocol fees from both products accrue to the TNSR treasury.

Tensor launched in July 2022 and is the leading NFT marketplace on Solana, commanding 60-70% of Solana NFT market share. It gained momentum by catering to NFTs traders instead of just collectors with real-time data, pro charting tools, and a fast terminal interface.

Vector is the leading social trading app in crypto. Within 3 months of launch, it grew to $7.5 billion of annualized volume and 20k daily active users, both of which are doubling every 1-2 weeks. It generates $75M/year in fees of which 50% goes directly to the TNSR treasury.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 334.61M TNSR |
| **Total Supply** | 1.00B TNSR |
| **Max Supply** | 1.00B TNSR |
| **Fully Diluted Valuation** | $32.39M |
| **Market Cap / FDV Ratio** | 0.33 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.23 (2024-04-08) |
| **Current vs ATH** | -98.55% |
| **All-Time Low** | $0.0274 (2026-06-10) |
| **Current vs ATL** | +18.23% |
| **24h Change** | -1.60% |
| **7d Change** | -2.67% |
| **30d Change** | +5.91% |
| **1y Change** | -77.93% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `TNSRxcUxoT9xBG3de7PiJyTDYu7kskLqcpddxnEJAS6` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TNSR/USDT | N/A |
| Kraken | TNSR/USD | N/A |
| Bitget | TNSR/USDT | N/A |
| KuCoin | TNSR/USDT | N/A |
| Crypto.com Exchange | TNSR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | TNSRXCUXOT9XBG3DE7PIJYTDYU7KSKLQCPDDXNEJAS6/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.tensor.foundation](https://www.tensor.foundation) |
| **Twitter** | [@tensorfdn](https://twitter.com/tensorfdn) |
| **Discord** | [https://discord.gg/tensor](https://discord.gg/tensor) |
| **GitHub** | [https://github.com/tensor-foundation](https://github.com/tensor-foundation) |
| **Whitepaper** | [https://docs.tensor.foundation](https://docs.tensor.foundation) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.29M |
| **Market Cap Rank** | #1118 |
| **24h Range** | $0.0322 — $0.0335 |
| **CoinGecko Sentiment** | 0% positive |
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

TNSR is a genuine two-venue derivatives market: it trades on **Binance** (TNSR/USDT spot plus a USD-margined perpetual) and on **Hyperliquid** (TNSR-PERP, offering roughly 40-50x max leverage). Having both a top-tier CEX and a leading on-chain perp venue gives the market meaningful depth for a rank ~1118 asset, and lets the spot leg on Binance be paired against either perp for carry and basis structures. Practically, the Binance perp typically carries the deepest book and tightest spreads, while the Hyperliquid perp adds transparent on-chain funding/OI and a second venue whose funding can diverge. Still, TNSR is a low-market-cap alt, so order-book depth thins quickly at size — scale into positions, lean on limit/passive execution, and split large orders across both venues to limit slippage and single-venue impact.

### Applicable strategies

- [[funding-rate-arbitrage]] — capture the funding spread between Binance and Hyperliquid TNSR perps by going long the cheaper-funded venue and short the richer one, delta-neutral.
- [[hl-vs-cex-funding-divergence]] — the smaller Hyperliquid TNSR book can print funding materially away from Binance, creating a direct cross-venue divergence trade.
- [[cash-and-carry]] — hold Binance spot TNSR against a short perp to harvest positive basis/funding on a low-cap alt that often trades in contango during hype phases.
- [[basis-trading]] — trade the spread between TNSR spot and perp mark as the low-float token's basis swings with narrative-driven demand.
- [[liquidation-cascade-fade]] — thin depth and high leverage make TNSR prone to sharp liquidation flushes; fade overshoots once OI and funding reset.
- [[breakout-and-retest]] — narrative catalysts (NFT/social-trading volume, Vector growth) can drive clean range breaks worth trading on the retest with defined risk.

### Volatility & regime character

TNSR is a **high-beta, low-float Solana-ecosystem alt** tied to the NFT-marketplace and social-trading narrative. With a low circulating float versus supply and modest market cap, it exhibits reflexive, momentum-driven moves and outsized realized volatility relative to majors. Directionally it carries strong positive beta to BTC/ETH and especially to SOL and broader Solana risk sentiment — it tends to amplify up-moves in bull phases and bleed harder in risk-off, with idiosyncratic spikes around Tensor/Vector product news.

### Risk flags

- **Liquidity & venue concentration** — small market cap and thin books mean high slippage at size and elevated dependence on Binance/Hyperliquid remaining active for TNSR.
- **Token unlocks / emissions** — circulating supply is only ~a third of max supply, so scheduled unlocks and emissions are a persistent overhang; monitor supply-event calendars.
- **Narrative dependence** — price is heavily levered to NFT-marketplace share and Vector/social-trading traction; fading narrative can compress valuation quickly.
- **Perp funding dislocations** — high leverage on a low-cap alt can drive extreme funding and crowded positioning, raising liquidation-cascade and squeeze risk on both venues.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=TNSR` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=TNSR` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=TNSR&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=TNSR&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=TNSR"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
