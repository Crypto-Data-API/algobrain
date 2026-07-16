---
title: "FC Barcelona Fan Token"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, altcoins, memecoins]
aliases: ["BAR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.socios.com/fcbarcelona/"
related: ["[[crypto-markets]]", "[[binance]]", "[[event-driven-trading]]", "[[breakout-trading]]"]
---

# FC Barcelona Fan Token

**FC Barcelona Fan Token** (BAR) is a Sports, Fan Token, Solana Ecosystem, Base Ecosystem, Binance Launchpad, Chiliz Ecosystem project. It ranks **#1275** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BAR |
| **Market Cap Rank** | #1275 |
| **Market Cap** | $8.05M |
| **Current Price** | $0.3101 |
| **Categories** | Sports, Fan Token, Binance Launchpad |
| **Website** | [https://www.socios.com/fcbarcelona/](https://www.socios.com/fcbarcelona/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 25.96M BAR |
| **Total Supply** | 39.96M BAR |
| **Max Supply** | 39.96M BAR |
| **Fully Diluted Valuation** | $12.39M |
| **Market Cap / FDV Ratio** | 0.65 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $72.55 (2021-04-21) |
| **Current vs ATH** | -99.57% |
| **All-Time Low** | $0.2585 (2026-06-23) |
| **Current vs ATL** | +21.30% |
| **24h Change** | +11.39% |
| **7d Change** | +14.90% |
| **30d Change** | +7.36% |
| **1y Change** | -72.83% |

---

## Platform & Chain Information

**Native Chain:** Chiliz

### Contract Addresses

| Chain | Address |
|---|---|
| Chiliz | `0x1589248b4b61ed472cc21ca1f2114d93ab6910d5` |
| Solana | `82DNsTK61ZrgCHP6pfP32Eubcsp9h38d64E6X9ETEBBe` |
| Base | `0x110a0fc65a0f78840f4b4a04a42e8c285e424553` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BAR/TRY | N/A |
| Upbit | BAR/BTC | N/A |
| Bitget | BAR/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.socios.com/fcbarcelona/](https://www.socios.com/fcbarcelona/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $13.37M |
| **Market Cap Rank** | #1275 |
| **24h Range** | $0.2761 — $0.3385 |
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

BAR is tradable on **Binance SPOT only** — there is no liquid perpetual venue, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding, basis, and liquidation-cascade strategies do NOT apply. With a small ~$8M cap and single-venue depth concentration, order books thin out quickly: large orders will slip, so position sizing must stay modest and execution should favor limit orders and VWAP-style slicing rather than aggressive market fills. The lack of a borrow/short leg means bearish exposure can only be expressed by exiting spot, and the absence of leverage caps both upside amplification and forced-liquidation risk.

### Applicable strategies

- [[breakout-trading]] — BAR trades in long quiet ranges near ATL then spikes on match/club catalysts; spot breakouts above range highs are the cleanest entries.
- [[breakout-and-retest]] — thin books produce false breaks, so waiting for a retest of the broken level filters noise before committing spot size.
- [[range-trading]] — between catalysts BAR oscillates in a defined band (e.g. recent $0.276–$0.339 24h range), suiting fade-the-edges spot rotation.
- [[rsi-mean-reversion]] — sharp fan-token pumps overextend fast; RSI extremes flag reversion points for spot re-entry or trimming.
- [[event-driven-trading]] — price is driven by discrete club events (fixtures, signings, silverware); positioning around scheduled catalysts is the core edge.
- [[dca-strategy]] — for spot-only accumulation near cyclical lows, averaging in smooths the wide swings without needing leverage.

### Volatility & regime character

BAR is a **small-cap fan token** (rank ~1232, ~$8M cap) with high idiosyncratic, reflexive volatility more akin to a sports-narrative asset than an infra/DeFi token. It is down ~99.6% from its 2021 ATH and trades near all-time lows, so realized volatility is event-clustered rather than continuous. Correlation to BTC/ETH is loose — moves are dominated by club-specific news and Chiliz/fan-token sector sentiment rather than broad crypto beta. Expect low baseline activity punctuated by sharp, mean-reverting spikes.

### Risk flags

- **Liquidity/venue concentration** — spot-only on Binance with a small cap; depth is shallow and a single-venue outage or delisting would sharply impair exit liquidity.
- **Narrative dependence** — value hinges on FC Barcelona sporting performance and fan engagement, not on protocol cash flows; sentiment can evaporate quickly.
- **Supply overhang** — circulating supply (~26M) is well below max (~40M); ~35% of tokens remain to enter circulation, a structural dilution risk.
- **Sector fragility** — the fan-token category has weak long-term price retention (deep drawdown from ATH), signaling persistent secular downside pressure.
- **Regulatory** — fan tokens have drawn scrutiny in some jurisdictions over securities/consumer-protection classification.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BARUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BARUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BARUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BARUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
