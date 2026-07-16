---
title: "YZY"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins]
aliases: ["YZY"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://money.yeezy.com/"
related: ["[[crypto-markets]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# YZY

**YZY** (YZY) is a Solana Ecosystem, Meme, Celebrity-Themed project. It ranks **#526** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | YZY |
| **Market Cap Rank** | #526 |
| **Market Cap** | $38.95M |
| **Current Price** | $0.299875 |
| **Categories** | Solana Ecosystem, Meme, Celebrity-Themed |
| **Website** | [https://money.yeezy.com/](https://money.yeezy.com/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 130.00M YZY |
| **Total Supply** | 1,000.00M YZY |
| **Max Supply** | 1.00B YZY |
| **Fully Diluted Valuation** | $328.93M |
| **Market Cap / FDV Ratio** | 0.13 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.95 (2025-08-21) |
| **Current vs ATH** | -88.86% |
| **All-Time Low** | $0.1884 (2025-10-10) |
| **Current vs ATL** | +74.33% |
| **24h Change** | -0.22% |
| **7d Change** | +0.24% |
| **30d Change** | +1.16% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `DrZ26cKJDksVRWib3DVVsjo9eeXccc7hKhDJviiYEEZY` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | YZY/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | YZY-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://money.yeezy.com/](https://money.yeezy.com/) |
| **Twitter** | [@yzy_mny](https://twitter.com/yzy_mny) |
| **Telegram** | [YZY_MNY](https://t.me/YZY_MNY) (2,066 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.15M |
| **Market Cap Rank** | #526 |
| **24h Range** | $0.3271 — $0.3307 |
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

YZY is a **PERP-FIRST** asset: flow concentrates on the **[[hyperliquid|Hyperliquid]] YZY-PERP** contract (leverage up to ~40–50x). It is **not listed on Binance**, and spot access is limited/offshore (thin CEX/DEX spot venues), so the HL perp is the primary price-discovery and liquidity venue. Book depth is shallow relative to majors, so size must scale to available depth — large market orders slip and can self-trigger moves. The lack of a deep, on-shore spot leg means true cash-and-carry hedging is hard to execute cleanly; most positioning is directional or funding/basis plays against the perp itself. Prefer limit/passive execution, size conservatively, and expect wider effective spreads and gap risk around low-liquidity hours.

### Applicable strategies

- [[funding-rate-harvest]] — a low-cap, retail-driven perp where funding can run persistently one-sided; harvest the carry when funding is rich and stable.
- [[crowded-long-funding-fade]] — celebrity/meme narrative attracts crowded longs; fade extreme positive funding and OI buildup for mean-reversion.
- [[liquidation-cascade-fade]] — thin depth plus high leverage means liquidation wicks overshoot; fade the flush and buy the exhaustion.
- [[oi-price-exhaustion]] — watch for rising price on stalling/falling OI (or vice versa) to flag reflexive exhaustion in this single-venue perp.
- [[narrative-trading]] — price is dominated by the Yeezy/celebrity-meme storyline; trade catalyst-driven attention spikes and fades.
- [[volatility-breakout]] — range-bound drift punctuated by sharp expansion; trade confirmed breaks out of compression on the HL perp.

### Volatility & regime character

High-beta **memecoin / celebrity-themed** token with strong reflexivity — price is narrative- and attention-driven rather than fundamentals-driven. Expect memecoin-style behavior: long low-volume drift interrupted by violent, leverage-fueled expansions. Directionally correlated to broad crypto risk-on/risk-off (BTC/ETH beta) during market-wide moves, but idiosyncratic narrative flow frequently dominates, producing high dispersion versus majors.

### Risk flags

- **Venue concentration** — liquidity is concentrated on a single perp venue (Hyperliquid); no Binance listing and thin spot means fragile depth and execution risk.
- **Token unlocks / emissions** — low circulating vs. total/max supply (MC/FDV ratio ~0.13) implies substantial future unlock/dilution overhang; monitor supply events.
- **Narrative dependence** — value is tied to the Yeezy/celebrity meme narrative; sentiment reversals can be abrupt and severe.
- **Perp funding dislocations** — one-sided crowded positioning on a thin single-venue perp can drive funding to extremes and trigger liquidation cascades.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=YZY` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=YZY` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=YZY&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=YZY&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=YZY"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
