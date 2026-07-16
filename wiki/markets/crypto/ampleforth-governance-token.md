---
title: "Ampleforth Governance"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, stablecoins, defi]
aliases: ["FORTH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.ampleforth.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-yield]]"]
---

# Ampleforth Governance

**Ampleforth Governance** (FORTH) is a cryptocurrency. It ranks **#2335** by market capitalization. FORTH is the native governance token that powers Ampleforth, a protocol that automatically adjusts the supply of its native token, AMPL, in response to demand.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FORTH |
| **Market Cap Rank** | #2335 |
| **Market Cap** | $1.81M |
| **Current Price** | $0.1689 |
| **Categories** | Stablecoin Issuer, Governance |
| **Website** | [https://www.ampleforth.org/](https://www.ampleforth.org/) |

---

## Overview

FORTH is the native governance token that powers Ampleforth, a protocol that automatically adjusts the supply of its native token, AMPL, in response to demand. FORTH holders can vote on proposed changes to the Ampleforth protocol or delegate their votes to representatives who vote on their behalf.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.70M FORTH |
| **Total Supply** | 15.30M FORTH |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $2.58M |
| **Market Cap / FDV Ratio** | 0.70 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $180.47 (2021-04-21) |
| **Current vs ATH** | -99.91% |
| **All-Time Low** | $0.1558 (2026-06-06) |
| **Current vs ATL** | +8.38% |
| **24h Change** | -3.76% |
| **7d Change** | -1.56% |
| **30d Change** | -3.26% |
| **1y Change** | -93.74% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x77fba179c79de5b7653f68b5039af940ada60ce0` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | FORTH/USD | N/A |
| KuCoin | FORTH/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X77FBA179C79DE5B7653F68B5039AF940ADA60CE0/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X77FBA179C79DE5B7653F68B5039AF940ADA60CE0/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.ampleforth.org/](https://www.ampleforth.org/) |
| **Twitter** | [@AmpleforthOrg](https://twitter.com/AmpleforthOrg) |
| **Telegram** | [Ampleforth](https://t.me/Ampleforth) (5,327 members) |
| **Discord** | [https://discord.gg/mptQ49m](https://discord.gg/mptQ49m) |
| **GitHub** | [https://github.com/ampleforth/Forth/](https://github.com/ampleforth/Forth/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 26 |
| **GitHub Forks** | 9 |
| **Pull Requests Merged** | 7 |
| **Contributors** | 2 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.06M |
| **Market Cap Rank** | #2335 |
| **24h Range** | $0.1669 — $0.1772 |
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

A USD-pegged stablecoin traded on [[binance]]. It is a PEG / cash-management instrument, NOT a directional asset — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. Because the instrument targets a fixed 1.00 anchor, leverage adds little directional edge and mostly amplifies tail depeg risk; liquidity is concentrated on the primary venue, so venue availability directly shapes execution quality, achievable size, and the tightness of any arbitrage loop. Size should be scaled to on-venue depth and the ability to redeem or exit at parity rather than to volatility targets.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — accumulate on downside deviations below 1.00 and exit on reversion to parity, treating each depeg as a mean-reversion trade.
- [[stablecoin-pair-arbitrage]] — arbitrage price differences between FORTH and other stablecoin pairs where quotes diverge from parity across books.
- [[mint-parity-arbitrage]] — exploit gaps between the secondary-market price and the parity redemption/mint value when the mechanism permits.
- [[stablecoin-yield]] — deploy idle balances into yield venues while holding the peg exposure as a cash-equivalent position.
- [[carry-trade]] — fund positions cheaply and hold the peg instrument to capture yield or spread differentials with limited directional risk.

### Volatility & regime character

As a peg instrument, the relevant regime signal is peg tightness rather than trend. Quiet regimes trade in a narrow band around the 1.00 anchor; stress regimes are marked by depeg episodes where the price gaps below parity before (potentially) reverting. Character depends on the backing model and redemption mechanics — how reserves are held and whether holders can redeem at parity on demand determines how quickly deviations self-correct.

### Risk flags

- **Depeg risk** — the core trading risk; the peg can break and reversion is not guaranteed.
- **Reserve/backing transparency** — quality and auditability of the backing determine confidence in parity.
- **Redemption gating** — redemptions may be paused, throttled, or restricted during stress, trapping positions off-peg.
- **Regulatory** — stablecoin-specific regulatory action can force redemption freezes or delistings.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=FORTHUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=FORTHUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=FORTHUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=FORTHUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
