---
title: "cat in a dogs world"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, memecoins, altcoins]
aliases: ["MEW"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://mew.xyz/"
related: ["[[crypto-markets]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[meme-coin-cycle]]"]
---

# cat in a dogs world

**cat in a dogs world** (MEW) is (MEW) on Solana It ranks **#619** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MEW |
| **Market Cap Rank** | #619 |
| **Market Cap** | $31.80M |
| **Current Price** | $0.000358 |
| **Categories** | Solana Ecosystem, Meme, Dog-Themed, Solana Meme, Cat-Themed, Binance Alpha Spotlight, IP Meme |
| **Website** | [https://mew.xyz/](https://mew.xyz/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

cat in a dogs world (MEW) on Solana

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 88.89B MEW |
| **Total Supply** | 88.89B MEW |
| **Max Supply** | 88.89B MEW |
| **Fully Diluted Valuation** | $50.84M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0129 (2024-11-17) |
| **Current vs ATH** | -95.58% |
| **All-Time Low** | $0.00051113 (2026-02-06) |
| **Current vs ATL** | +11.42% |
| **24h Change** | -3.29% |
| **7d Change** | +0.38% |
| **30d Change** | -1.20% |
| **1y Change** | -70.80% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `MEW1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | MEW/EUR | N/A |
| Upbit | MEW/KRW | N/A |
| Bitget | MEW/USDT | N/A |
| KuCoin | MEW/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | MEW-PERP | Perpetual |
| Orca | MEW1GQWJ3NEXG2QGERIKU7FAFJ79PHVQVREQUZSCPP5/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://mew.xyz/](https://mew.xyz/) |
| **Twitter** | [@mew](https://twitter.com/mew) |
| **Telegram** | [mewsworld](https://t.me/mewsworld) (20,302 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.60M |
| **Market Cap Rank** | #619 |
| **24h Range** | $0.00056881 — $0.00060072 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

MEW is tradable on **both Binance (spot + USD-margined perp) and Hyperliquid (MEW-PERP, up to ~40-50x leverage)**, alongside additional CEX spot listings (Kraken, Upbit, Bitget, KuCoin) and Solana DEX liquidity (Orca). This makes it a comparatively deep, liquid two-venue derivatives market for a small-cap memecoin, with meaningful order-book depth on both the centralized perp and Hyperliquid's on-chain book. The dual-venue availability enables cross-venue execution — routing size across Binance and Hyperliquid to reduce slippage, and exploiting funding/basis differences between the two perp markets. Position sizing should still respect that MEW is a rank ~621 memecoin: depth thins quickly beyond modest clip sizes, so scale in/out and avoid market orders that sweep the book during volatility.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — MEW trades as a perp on both Binance and Hyperliquid, so funding can diverge between the two venues, creating a delta-neutral harvest of the spread.
- [[funding-rate-harvest]] — as a reflexive memecoin, MEW perp funding frequently swings positive during hype legs; hedging spot against the perp captures that carry.
- [[crowded-long-funding-fade]] — retail crowds pile long into MEW rallies, pushing funding to extremes and setting up funding-driven mean-reversion fades.
- [[liquidation-cascade-fade]] — thin memecoin depth means clustered stops trigger sharp liquidation cascades that overshoot, offering rebound fades.
- [[meme-coin-cycle]] — MEW is a pure narrative/attention memecoin whose price follows the hype-and-fade meme rotation cycle.
- [[cash-and-carry]] — with liquid spot (Solana/CEX) and a perp on two venues, MEW supports a spot-long / perp-short carry when funding is richly positive.

### Volatility & regime character

MEW is a **high-beta Solana-ecosystem memecoin** driven by reflexive attention and social sentiment rather than fundamentals. It exhibits large, momentum-heavy swings, sharp drawdowns (~95% below ATH), and pronounced sensitivity to broad crypto risk-on/risk-off. Correlation to BTC/ETH is directional but amplified — it tends to rally harder in risk-on memecoin phases and sell off faster in de-risking, with additional idiosyncratic beta to SOL and the Solana meme sector.

### Risk flags

- **Liquidity / venue concentration** — despite two-venue perp access, absolute depth is small-cap; large orders move price and cascades are violent.
- **Narrative dependence** — value is almost entirely attention/meme-driven; loss of social momentum can produce durable, non-mean-reverting declines.
- **Perp funding dislocations** — memecoin funding can spike to extremes and flip rapidly, punishing one-sided carry and crowded positioning.
- **Memecoin reflexivity** — feedback loops between price, funding, and liquidations amplify moves in both directions and raise gap/slippage risk.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MEW` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MEW` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MEW&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MEW&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MEW"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
