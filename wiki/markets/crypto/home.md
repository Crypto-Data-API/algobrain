---
title: "HOME"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["HOME"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://defi.app"
related: ["[[crypto-markets]]", "[[base]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# HOME

**HOME** (HOME) is a cryptocurrency. It ranks **#242** by market capitalization. Crypto's "Everything App" that makes DeFi as easy as using an iPhone, combining instant cross-chain swaps, yield farming, and perps trading with zero gas fees, zero bridging and full self-custody.

Decentralized finance has massive potential, but several challenges have consistently held it back from broader adoption:
-Complex User Experience: The steep learning curve, confusing interfaces, and technical barriers make DeFi intimidating for newcomers.
-Fragmented Ecosystem: Managing assets across

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HOME |
| **Market Cap Rank** | #242 |
| **Market Cap** | $116.77M |
| **Current Price** | $0.030509 |
| **Categories** | Decentralized Finance (DeFi), BNB Chain Ecosystem, Solana Ecosystem, Base Ecosystem, Account Abstraction, Dex Aggregator, Base Native |
| **Website** | [https://defi.app](https://defi.app) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

Crypto's "Everything App" that makes DeFi as easy as using an iPhone, combining instant cross-chain swaps, yield farming, and perps trading with zero gas fees, zero bridging and full self-custody.

Decentralized finance has massive potential, but several challenges have consistently held it back from broader adoption:
-Complex User Experience: The steep learning curve, confusing interfaces, and technical barriers make DeFi intimidating for newcomers.
-Fragmented Ecosystem: Managing assets across multiple blockchains can feel disjointed and labor-intensive, with users needing to navigate different platforms and tools.
-Risk of User Errors: DeFi can be unforgiving—losing a seed phrase or making a small mistake can lead to significant financial losses.
-Issues with Centralized Exchanges: Centralized exchanges compromise control and security by holding custody of users' assets, which goes against the core principles of decentralization.

Defi App directly addresses these issues to make DeFi simple, safe, and accessible:
-Unified Platform: Defi App provides native account abstraction, allowing you to connect your wallets and manage all your assets without dealing with technical intricacies. There’s no need to navigate multiple tools or migrate assets across chains—everything you need is in one place.
-Cross-Chain Capabilities: Our platform supports seamless engagement across different blockchain networks. Swap tokens, leverage assets, or yield farm—Defi App breaks down chain boundaries, so you can take advantage of opportunities anywhere in DeFi.
-Gasless Transactions: Defi App sponsors gas fees, meaning you don’t need to hold specific gas tokens for every chain. This makes transactions easy and eliminates a common barrier that frustrates both new and experienced users.
-Intuitive Design: Defi App’s user-friendly interface ensures that anyone, from beginners to experts, can navigate DeFi confidently.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.44B HOME |
| **Total Supply** | 10.00B HOME |
| **Max Supply** | 10.00B HOME |
| **Fully Diluted Valuation** | $189.52M |
| **Market Cap / FDV Ratio** | 0.34 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0489 (2025-08-17) |
| **Current vs ATH** | -61.34% |
| **All-Time Low** | $0.0161 (2025-12-30) |
| **Current vs ATL** | +17.11% |
| **24h Change** | -0.50% |
| **7d Change** | -2.59% |
| **30d Change** | -16.83% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x4bfaa776991e85e5f8b1255461cbbd216cfc714f` |
| Binance Smart Chain | `0x4bfaa776991e85e5f8b1255461cbbd216cfc714f` |
| Solana | `J3umBWqhSjd13sag1E1aUojViWvPYA5dFNyqpKuX3WXj` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HOME/USDT | N/A |
| Bitget | HOME/USDT | N/A |
| KuCoin | HOME/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://defi.app](https://defi.app) |
| **Twitter** | [@defiapp](https://twitter.com/defiapp) |
| **Telegram** | [OfficialDefiApp](https://t.me/OfficialDefiApp) (6,640 members) |
| **Discord** | [https://discord.com/invite/defiapp](https://discord.com/invite/defiapp) |
| **GitHub** | [https://github.com/defi-app](https://github.com/defi-app) |
| **Whitepaper** | [https://docs.defi.app/knowledge-base](https://docs.defi.app/knowledge-base) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.15M |
| **Market Cap Rank** | #242 |
| **24h Range** | $0.0188 — $0.0192 |
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

HOME is tradable on **Binance** — both spot (HOME/USDT) and a **USD-margined perpetual**, which exposes funding rates, open interest, and liquidation flow. It is **not listed on Hyperliquid**, so Binance is the primary — and effectively sole — venue for leveraged HOME exposure. With a small market cap (rank ~432) and thin 24h spot volume, order books are shallow: leveraged size and liquidation events move price disproportionately, so position sizing must stay small relative to depth and use limit/scaled entries to avoid slippage. Venue concentration on Binance means the perp funding/basis and Binance spot are the reference prices for any HOME strategy; there is no deep second leveraged venue to cross-hedge against.

### Applicable strategies

- [[funding-rate-harvest]] — the isolated Binance perp lets you collect funding when HOME perp trades at a persistent premium/discount to spot while delta-hedging on Binance spot.
- [[cash-and-carry]] — long Binance spot HOME against short the USD-M perp to capture basis on a small-cap where perp demand can push a rich carry.
- [[liquidation-cascade-fade]] — thin books mean leveraged flushes overshoot; fade forced-liquidation spikes back toward spot value.
- [[crowded-long-funding-fade]] — narrative-driven long crowding in a small DeFi token often shows in elevated funding and OI; fade the crowded side into exhaustion.
- [[oi-price-exhaustion]] — rising open interest without follow-through in price flags trapped positioning ripe for a reversal on this low-float name.
- [[range-mean-reversion]] — outside catalysts, HOME oscillates in a low-liquidity range, favoring reversion at band extremes.

### Volatility & regime character

Small-cap DeFi "everything app" token (Base-native, multi-chain) with a modest float and low FDV. Price action is reflexive and high-beta to broader crypto risk sentiment, with amplified moves versus BTC/ETH due to thin liquidity. Directionality is largely driven by DeFi/narrative flows and Binance-listing liquidity rather than deep organic order flow; expect elevated realized volatility and sharp regime shifts around catalysts.

### Risk flags

- **Liquidity/venue concentration** — leveraged exposure lives almost entirely on Binance; a single-venue outage, delisting, or margin change is a concentrated risk with no deep fallback perp venue.
- **Emissions/unlocks** — circulating supply (~3.44B) is well below max supply (10.00B), so ongoing emissions and future unlocks create structural sell pressure and dilution.
- **Narrative dependence** — as a DeFi UX/aggregator play, valuation hinges on adoption narrative; sentiment reversals can drain liquidity fast.
- **Thin books** — low 24h volume makes slippage, stop-hunts, and liquidation cascades likely; size conservatively and expect wide effective spreads.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HOMEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HOMEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HOME` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HOME` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HOMEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HOMEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HOME"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
