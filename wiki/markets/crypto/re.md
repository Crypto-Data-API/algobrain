---
title: "RE"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, stablecoins, defi]
aliases: ["RE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://re.xyz/home"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-pair-arbitrage]]"]
---

# RE

**RE** (RE) is an internet-native marketplace for insurance capital. It connects eligible capital providers with fully collateralized reinsurance activity conducted through licensed insurance entities. It ranks **#294** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RE |
| **Market Cap Rank** | #294 |
| **Market Cap** | $82.34M |
| **Current Price** | $0.5166 |
| **Categories** | Insurance, Real World Assets (RWA), Stablecoin Issuer, RWA Protocol, Governance |
| **Website** | [https://re.xyz/home](https://re.xyz/home) |

---

## Overview

Re is an internet-native marketplace for insurance capital. It connects eligible capital providers with fully collateralized reinsurance activity conducted through licensed insurance entities. Blockchain infrastructure makes collateral, reserves, and selected operating data verifiable onchain. RE is the governance token of the Re Protocol. It governs protocol upgrades, technical permissions, committee formation, reporting standards, incentive policy, and governance procedures. Underwriting, claims, pricing, reserve decisions, and regulated operations remain with qualified professionals and licensed entities.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 159.60M RE |
| **Total Supply** | 1.00B RE |
| **Max Supply** | 1.00B RE |
| **Fully Diluted Valuation** | $515.94M |
| **Market Cap / FDV Ratio** | 0.16 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.08 (2026-06-20) |
| **Current vs ATH** | -52.35% |
| **All-Time Low** | $0.4002 (2026-06-18) |
| **Current vs ATL** | +28.33% |
| **24h Change** | +5.78% |
| **7d Change** | -13.05% |
| **30d Change** | +0.00% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x526526528f35ac738177003b8773b402b8df8143` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RE/USDT | N/A |
| Kraken | RE/USD | N/A |
| Upbit | RE/KRW | N/A |
| Crypto.com Exchange | RE/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X526526528F35AC738177003B8773B402B8DF8143/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://re.xyz/home](https://re.xyz/home) |
| **Twitter** | [@re](https://twitter.com/re) |
| **Telegram** | [re_protocol](https://t.me/re_protocol) (49,465 members) |
| **Discord** | [https://discord.gg/reprotocol](https://discord.gg/reprotocol) |
| **GitHub** | [https://github.com/re-protocol](https://github.com/re-protocol) |
| **Whitepaper** | [https://docs.re.xyz/](https://docs.re.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $63.62M |
| **Market Cap Rank** | #294 |
| **24h Range** | $0.4789 — $0.5172 |
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

RE trades as a USD-pegged stablecoin, with primary centralized liquidity on [[binance]] (RE/USDT). It is a PEG / cash-management instrument, NOT a directional asset — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage rather than momentum or trend. Because a stablecoin's fair value is anchored near 1.00, position sizing is governed by peg tightness and redemption confidence rather than volatility targeting; leverage is generally inappropriate except for tight, mean-reverting peg-arbitrage legs. Venue availability shapes execution: consolidated flow on Binance concentrates spot depth and keeps quoted spreads narrow during calm regimes, so large redemptions or arbitrage sizing should account for single-venue depth and the risk of thinning liquidity during depeg stress.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — buy RE below par during a depeg episode and capture the reversion as the peg is restored.
- [[stablecoin-pair-arbitrage]] — arbitrage RE against other USD stablecoins when its price diverges from 1.00 on Binance.
- [[stablecoin-yield]] — deploy RE into on-chain or venue yield venues as a cash-management leg while holding near par.
- [[mint-parity-arbitrage]] — exploit gaps between the secondary-market RE price and its mint/redeem parity through the issuer's collateral mechanism.
- [[delta-neutral-yield-farming]] — pair RE liquidity provision or lending with an offsetting hedge to harvest yield with minimal directional exposure.
- [[carry-trade]] — fund positions with RE's peg-stable value to capture rate/yield differentials across venues.

### Volatility & regime character

As a USD-pegged instrument, RE's regime character is defined by peg tightness rather than trend. In normal conditions price should oscillate in a narrow band around 1.00, with volatility clustering only around depeg events driven by redemption pressure, backing/collateral concerns, or venue-specific liquidity gaps. Regime shifts are discrete (pegged vs. depegged) rather than continuous, and the key qualitative inputs are the backing model, the transparency of reserves, and the reliability of redemption/mint mechanics that enforce parity.

### Risk flags

- **Depeg risk** — a break from 1.00 can be sharp and, depending on backing, may not fully revert; peg-reversion trades carry tail risk.
- **Reserve/backing transparency** — the strength of the peg depends on collateral quality and how verifiably reserves are disclosed; opacity raises depeg probability.
- **Redemption gating** — restrictions, delays, or eligibility limits on mint/redeem can trap arbitrage capital and widen secondary-market dislocations.
- **Regulatory** — stablecoin issuance and redemption are subject to evolving regulation that can affect availability, redeemability, and venue access.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=REUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=REUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=REUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=REUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
