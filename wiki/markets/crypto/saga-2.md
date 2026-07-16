---
title: "Saga"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["SAGA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.saga.xyz/"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]"]
---

# Saga

**Saga** (SAGA) is a Artificial Intelligence (AI), Infrastructure, Smart Contract Platform, Binance Launchpool, Layer 1 (L1), Modular Blockchain, Gaming Blockchains, Appchains, Saga Ecosystem project. It ranks **#1527** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SAGA |
| **Market Cap Rank** | #1527 |
| **Market Cap** | $5.22M |
| **Current Price** | $0.0125 |
| **Categories** | Artificial Intelligence (AI), Infrastructure, Smart Contract Platform, Binance Launchpool, Layer 1 (L1), Modular Blockchain, Gaming Blockchains, Appchains |
| **Website** | [https://www.saga.xyz/](https://www.saga.xyz/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 416.51M SAGA |
| **Total Supply** | 1.10B SAGA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $13.85M |
| **Market Cap / FDV Ratio** | 0.38 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $7.60 (2024-04-09) |
| **Current vs ATH** | -99.84% |
| **All-Time Low** | $0.0118 (2026-06-10) |
| **Current vs ATL** | +6.25% |
| **24h Change** | -0.13% |
| **7d Change** | -2.38% |
| **30d Change** | -4.24% |
| **1y Change** | -95.77% |

---

## Platform & Chain Information

**Native Chain:** Saga

### Contract Addresses

| Chain | Address |
|---|---|
| Saga | `usaga` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SAGA/TRY | N/A |
| Kraken | SAGA/USD | N/A |
| Bitget | SAGA/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.saga.xyz/](https://www.saga.xyz/) |
| **Twitter** | [@Sagaxyz__](https://twitter.com/Sagaxyz__) |
| **Reddit** | [https://www.reddit.com/r/saga_xyz/](https://www.reddit.com/r/saga_xyz/) |
| **Telegram** | [sagaofficialchannel](https://t.me/sagaofficialchannel) (3,356 members) |
| **Discord** | [https://discord.gg/sagaxyz](https://discord.gg/sagaxyz) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.56M |
| **Market Cap Rank** | #1527 |
| **24h Range** | $0.0125 — $0.0128 |
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

SAGA trades on **two derivatives venues**: Binance (spot plus a USD-margined perpetual) and Hyperliquid (**SAGA-PERP**, offering roughly **40-50x** leverage). This dual-venue footprint gives SAGA deeper, more continuous liquidity than a single-listing microcap: aggregated order-book depth is spread across a centralized incumbent and an on-chain perp DEX, which tightens spreads and supports somewhat larger clip sizes than the ~$5M market cap alone would suggest. In practice, execution should still be sliced — book depth thins quickly beyond the top few levels at this cap, so large market orders will walk the book on either venue. The parallel Binance and Hyperliquid perps also create a natural rail for cross-venue and funding-based strategies, since price and funding can diverge between the CEX and the DEX.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — SAGA's simultaneous Binance and Hyperliquid perps let you harvest funding-rate gaps between the CEX and the DEX legs.
- [[funding-rate-harvest]] — a thin, sentiment-driven microcap perp tends to run persistently skewed funding you can collect delta-neutrally.
- [[cash-and-carry]] — pair Binance/Hyperliquid spot exposure against the perp to lock the basis when funding runs rich.
- [[liquidation-cascade-fade]] — low-float, high-leverage SAGA perps are prone to sharp liquidation wicks that mean-revert, offering fade entries.
- [[cross-exchange-arbitrage]] — the two-venue listing means transient price dislocations between Binance and Hyperliquid can be arbitraged.
- [[rsi-mean-reversion]] — a beaten-down, range-bound token near its all-time low frequently overshoots on short-term momentum, favoring reversion setups.

### Volatility & regime character

SAGA is a **high-beta infrastructure/Layer-1 altcoin** (a modular-blockchain / appchain and gaming-infra token) sitting deep in the long tail at rank ~1533. It carries the reflexivity typical of low-cap alts: illiquid, narrative-sensitive, and prone to outsized percentage swings on modest flow. Directionally it is highly correlated to BTC/ETH beta — it tends to amplify broad-market risk-on/risk-off moves — while adding idiosyncratic volatility from L1/AI-infra narrative cycles and its own thin float. Having fallen ~99%+ from its all-time high, it trades in a low-price, low-cap regime where volatility is dominated by leverage-driven liquidation dynamics rather than steady spot demand.

### Risk flags

- **Liquidity / venue concentration** — despite two venues, absolute depth is small; the perps concentrate most speculative flow, so a venue outage or delisting would sharply impair exit liquidity.
- **Token unlocks / emissions** — max supply is uncapped and circulating supply (~417M) is well below total (~1.10B), so ongoing emissions and unlocks add persistent sell-side pressure.
- **Narrative dependence** — as an infra/L1/AI-tagged token, price action leans heavily on rotating sector narratives rather than fundamentals; narrative fatigue can drive protracted drawdowns.
- **Perp funding dislocations** — high leverage (~40-50x) on a thin float makes funding and mark price prone to violent dislocations and liquidation cascades.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=SAGA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=SAGA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=SAGA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=SAGA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=SAGA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
