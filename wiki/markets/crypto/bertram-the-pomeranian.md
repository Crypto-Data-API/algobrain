---
title: "Bertram The Pomeranian"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, memecoins, altcoins]
aliases: ["BERT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.bert.global/"
related: ["[[crypto-markets]]", "[[solana]]", "[[binance]]", "[[momentum-investing]]", "[[atr-trailing-stop]]"]
---

# Bertram The Pomeranian

**Bertram The Pomeranian** (BERT) is a cryptocurrency. It ranks **#1164** by market capitalization. In a market dominated by hype and lack of substance, $BERT was born with one simple yet powerful mission: to transform a meme into a real force for good - helping dogs globally

Inspired by a real dog, Bertram the Pomeranian, with millions of fans globally, $BERT bridges the gap between Web2 and Web3 through AI, smart dog tags and real world impact

$BERT is no longer a meme, it is a global movement.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BERT |
| **Market Cap Rank** | #1164 |
| **Market Cap** | $9.97M |
| **Current Price** | $0.0102 |
| **Categories** | Meme, Dog-Themed, Solana Meme, IP Meme |
| **Website** | [https://www.bert.global/](https://www.bert.global/) |

---

## Overview

In a market dominated by hype and lack of substance, $BERT was born with one simple yet powerful mission: to transform a meme into a real force for good - helping dogs globally

Inspired by a real dog, Bertram the Pomeranian, with millions of fans globally, $BERT bridges the gap between Web2 and Web3 through AI, smart dog tags and real world impact

$BERT is no longer a meme, it is a global movement.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 976.87M BERT |
| **Total Supply** | 976.87M BERT |
| **Max Supply** | 979.95M BERT |
| **Fully Diluted Valuation** | $9.97M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1886 (2024-11-15) |
| **Current vs ATH** | -94.60% |
| **All-Time Low** | $0.00148588 (2024-11-13) |
| **Current vs ATL** | +585.72% |
| **24h Change** | -2.83% |
| **7d Change** | +3.30% |
| **30d Change** | -34.23% |
| **1y Change** | -73.90% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `HgBRWfYxEfvPhtqkaeymCQtHCrKE46qQ43pKe8HCpump` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | BERT/USD | N/A |
| KuCoin | BERT/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.bert.global/](https://www.bert.global/) |
| **Twitter** | [@bertcoincto](https://twitter.com/bertcoincto) |
| **Telegram** | [BERTCOINCTO](https://t.me/BERTCOINCTO) (2,222 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $868,264.00 |
| **Market Cap Rank** | #1164 |
| **24h Range** | $0.0102 — $0.0109 |
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

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With no perp market, there is no borrow/leverage rail and no easy way to express short exposure; positioning is effectively long-or-flat and any bearish view must be managed by exiting spot inventory. As a small-cap memecoin (rank ~1160) with thin 24h turnover, the order book is shallow: size positions conservatively, split entries/exits across time, and lean on limit orders to avoid slippage. Single-venue concentration means execution quality and any listing/delisting decision hinges entirely on that one book.

### Applicable strategies

- [[momentum-investing]] — memecoin trends run in sharp reflexive impulses; riding confirmed upside momentum captures the bulk of BERT's directional moves.
- [[breakout-trading]] — from a deeply drawn-down base (~-95% from ATH), a clean break above consolidation on volume is the primary long trigger for a spot-only name.
- [[volatility-breakout]] — high memecoin volatility makes ATR/range-expansion entries effective at catching the start of impulsive spot legs.
- [[narrative-trading]] — BERT is driven by its dog-meme/"real-world good" narrative; trading around narrative catalysts and social momentum aligns with what actually moves price.
- [[dca-strategy]] — for a thin small-cap where timing the exact bottom is unreliable, scaling in gradually manages entry risk without needing leverage.
- [[atr-trailing-stop]] — with wide swings and no ability to short, an ATR-based trailing stop locks in gains and enforces the long-or-flat exit discipline this asset requires.

### Volatility & regime character

Small-cap Solana memecoin with high beta and pronounced reflexivity: moves are sentiment- and narrative-led rather than fundamentally anchored, amplifying both rallies and drawdowns. Broad direction tends to correlate with BTC/ETH risk appetite, but idiosyncratic memecoin flows dominate the amplitude — BERT can decouple hard during meme-cycle rotations. Expect regime shifts between quiet, illiquid drift and violent volume-driven impulses.

### Risk flags

- Liquidity/venue concentration: spot-only on a single book means thin depth, wide spreads, and full exposure to one venue's listing/delisting risk.
- Narrative dependence: value is tied to meme momentum and community/social attention; fading narrative can drain liquidity quickly with no fundamental floor.
- Memecoin reflexivity: susceptible to sharp, sentiment-driven drawdowns and low-liquidity gaps.
- No hedge rail: absence of a perp market removes any leverage or short mechanism, so risk must be managed purely through spot sizing and exits.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BERTUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BERTUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BERTUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BERTUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
