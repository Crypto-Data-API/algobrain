---
title: "SuperRare"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, nft, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["RARE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://superrare.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[oi-confirmed-trend]]"]
---

# SuperRare

**SuperRare** (RARE) is a NFT, Ethereum Ecosystem project. It ranks **#1135** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RARE |
| **Market Cap Rank** | #1135 |
| **Market Cap** | $10.54M |
| **Current Price** | $0.0128 |
| **Categories** | NFT |
| **Website** | [https://superrare.com/](https://superrare.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 820.51M RARE |
| **Total Supply** | 1.00B RARE |
| **Max Supply** | 1.00B RARE |
| **Fully Diluted Valuation** | $12.84M |
| **Market Cap / FDV Ratio** | 0.82 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.64 (2021-10-11) |
| **Current vs ATH** | -99.65% |
| **All-Time Low** | $0.0117 (2026-06-25) |
| **Current vs ATL** | +10.06% |
| **24h Change** | -0.22% |
| **7d Change** | +4.96% |
| **30d Change** | -5.14% |
| **1y Change** | -78.09% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xba5bde662c17e2adff1075610382b9b691296350` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RARE/TRY | N/A |
| Kraken | RARE/USD | N/A |
| Bitget | RARE/USDT | N/A |
| Crypto.com Exchange | RARE/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XBA5BDE662C17E2ADFF1075610382B9B691296350/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0X7FC66500C84A76AD7E9C93437BFC5AC33E2DDAE9/0XBA5BDE662C17E2ADFF1075610382B9B691296350 | Spot |
| Uniswap V2 (Ethereum) | 0XBA5BDE662C17E2ADFF1075610382B9B691296350/0XA7925AA2A6E4575AB0C74D169F3BC3E03D4C319A | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://superrare.com/](https://superrare.com/) |
| **Twitter** | [@SuperRare](https://twitter.com/SuperRare) |
| **Reddit** | [https://www.reddit.com/r/SuperRare/](https://www.reddit.com/r/SuperRare/) |
| **Telegram** | [SuperRare](https://t.me/SuperRare) (1,811 members) |
| **Discord** | [https://discord.com/invite/5DwpdyJR6t](https://discord.com/invite/5DwpdyJR6t) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.40M |
| **Market Cap Rank** | #1135 |
| **24h Range** | $0.0128 — $0.0132 |
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

RARE is tradable on **Binance** — both spot and a USD-margined perpetual, which exposes funding, open interest, and liquidation data for the token. It is **not** listed on Hyperliquid, so Binance is the primary leveraged venue. With a sub-$11M market cap and thin 24h volume, order books are shallow; leverage is available via the Binance USD-M perp, but crowded positioning can move price sharply. Practically, this means position sizing should stay small relative to visible depth, execution favors limit/VWAP-style fills over aggressive market orders, and slippage risk rises quickly on size. Venue concentration on a single leveraged exchange also means funding and liquidation dynamics on Binance dominate the derivatives picture.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin RARE books make forced-liquidation flushes on the Binance perp overshoot, offering fades back toward fair value.
- [[funding-rate-harvest]] — a low-float, low-cap token with a single perp venue often runs persistent funding skews that a delta-neutral harvest can collect.
- [[crowded-long-funding-fade]] — sentiment-driven long crowding pushes funding positive; fading stretched longs when funding spikes suits RARE's reflexive moves.
- [[oi-confirmed-trend]] — pairing Binance open-interest changes with price filters low-conviction chop from genuine trend legs in an illiquid name.
- [[cash-and-carry]] — when the Binance perp trades at a premium to spot, a long-spot/short-perp carry captures basis with defined risk.
- [[rsi-mean-reversion]] — RARE's tight, low-price range and mean-reverting drift make oscillator-based reversion viable between breakouts.

### Volatility & regime character

RARE is a micro-cap NFT/infrastructure token (~rank 1134) with high beta to broad crypto risk sentiment and strong correlation to BTC/ETH direction. Trading near all-time lows and roughly 99% below its 2021 ATH, it exhibits reflexive, sentiment-driven swings typical of low-float altcoins: quiet drift punctuated by sharp NFT-narrative or listing-driven spikes. Liquidity is thin, so realized volatility clusters and gaps are common; regime shifts tend to track the risk-on/risk-off state of majors rather than idiosyncratic fundamentals.

### Risk flags

- **Liquidity & venue concentration** — low market cap and single dominant leveraged venue (Binance) mean shallow depth, wide effective spreads, and elevated slippage/liquidation risk on size.
- **Emissions/supply** — circulating supply is ~82% of max; remaining ~180M RARE issuance could add sell pressure.
- **Narrative dependence** — as an NFT-ecosystem token, price is highly sensitive to the health of the NFT/creator narrative, which can evaporate quickly.
- **Reflexivity** — thin books amplify both up and down moves, making stops prone to being run and funding prone to whipsaw.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=RAREUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=RAREUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=RARE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=RARE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=RAREUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=RAREUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=RARE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
