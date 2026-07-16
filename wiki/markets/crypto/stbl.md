---
title: "STBL"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins, stablecoins]
aliases: ["STBL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.stbl.com/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# STBL

**STBL** (STBL) is a decentralized, non-custodial platform built to redefine stablecoin utility by combining yield, transparency, and real-world asset (RWA) backing. It ranks **#919** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | STBL |
| **Market Cap Rank** | #919 |
| **Market Cap** | $16.13M |
| **Current Price** | $0.0323 |
| **Categories** | Decentralized Finance (DeFi), BNB Chain Ecosystem, Real World Assets (RWA), Stablecoin Issuer, Binance Alpha Spotlight |
| **Website** | [https://www.stbl.com/](https://www.stbl.com/) |

---

## Overview

STBL is a decentralized, non-custodial platform built to redefine stablecoin utility by combining yield, transparency, and real-world asset (RWA) backing. At its core, STBL is a mechanism to mint stablecoins — namely USST and YLD — with unique advantages that stand out in the DeFi ecosystem: yield without staking, no lockups, and RWA-powered growth.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 500.00M STBL |
| **Total Supply** | 10.00B STBL |
| **Max Supply** | 10.00B STBL |
| **Fully Diluted Valuation** | $322.54M |
| **Market Cap / FDV Ratio** | 0.05 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5992 (2025-09-24) |
| **Current vs ATH** | -94.63% |
| **All-Time Low** | $0.0269 (2025-09-16) |
| **Current vs ATL** | +19.67% |
| **24h Change** | -3.08% |
| **7d Change** | +1.49% |
| **30d Change** | -10.64% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x8dedf84656fa932157e27c060d8613824e7979e3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | STBL/USD | N/A |
| KuCoin | STBL/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | STBL-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.stbl.com/](https://www.stbl.com/) |
| **Twitter** | [@stbl_official](https://twitter.com/stbl_official) |
| **Telegram** | [Stbl_Official](https://t.me/Stbl_Official) (29,099 members) |
| **Whitepaper** | [https://docs.stbl.com/](https://docs.stbl.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.82M |
| **Market Cap Rank** | #919 |
| **24h Range** | $0.0321 — $0.0341 |
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

STBL is a **PERP-FIRST** asset: it trades as **STBL-PERP on [[hyperliquid|Hyperliquid]]** (leverage up to ~40-50x) but is **NOT listed on Binance**. Spot access is limited and offshore (e.g. Kraken, KuCoin, plus BSC DEX pools), so the deepest and most continuous price discovery lives on the HL perp. Practical consequences: order-book depth on STBL-PERP is thin relative to majors, so slippage rises quickly on size — scale in with limit orders, keep clip sizes small, and treat the HL mark/funding as the reference price. Because there is no Binance venue to arbitrage against, cross-venue basis and funding dislocations can persist longer than on large caps, and thin spot liquidity means perp funding does most of the work anchoring the mark.

### Applicable strategies

- [[funding-rate-harvest]] — a low-cap perp-first token like STBL frequently carries elevated/persistent funding on the HL perp that can be systematically collected while delta-neutral.
- [[crowded-long-funding-fade]] — thin float plus RWA/stablecoin narrative pumps can crowd longs into deeply positive funding, setting up funding-paid fade entries.
- [[liquidation-cascade-fade]] — high leverage (~40-50x) on a thin book makes STBL-PERP prone to sharp liquidation flushes that overshoot and mean-revert.
- [[oi-confirmed-trend]] — with flow concentrated on one venue, HL open-interest changes cleanly confirm or reject directional moves in STBL.
- [[range-mean-reversion]] — outside of narrative catalysts STBL chops in a low-price band, favoring bounded mean-reversion around HL ranges.
- [[token-unlock-supply-event]] — a low circulating/FDV ratio (large locked supply vs. float) makes scheduled unlocks a tradable, calendar-driven supply catalyst.

### Volatility & regime character

STBL is a **low-cap DeFi / RWA stablecoin-issuer token** (not a stablecoin itself — the STBL governance/utility token is fully volatile). It behaves as a **high-beta altcoin**: it amplifies BTC/ETH risk-on/risk-off swings, but its sharpest moves are idiosyncratic and narrative-driven (RWA, yield-bearing stablecoin, Binance Alpha spotlight) rather than tightly correlated to majors. Expect reflexive, low-liquidity price action with outsized wicks around catalysts and quiet, range-bound drift otherwise.

### Risk flags

- **Venue concentration:** derivatives flow is single-venue (Hyperliquid) with no Binance perp — venue outages, delistings, or HL parameter changes directly hit tradability.
- **Thin liquidity / slippage:** low spot volume and shallow book depth make large orders and stops expensive to execute.
- **Token unlocks / emissions:** market cap is a small fraction of FDV (large locked supply), so future unlocks are a meaningful overhang.
- **Narrative dependence:** price hinges on the RWA/yield-stablecoin story and spotlight programs; narrative fade can drain liquidity fast.
- **Perp funding dislocations:** with limited spot to arbitrage against, funding can spike and stay dislocated, amplifying carry and liquidation risk.
- **Product depeg/regulatory:** STBL issues stablecoins (USST/YLD); any depeg or stablecoin-regulatory action on the underlying product can spill into the token.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=STBL` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=STBL` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=STBL&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=STBL&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=STBL"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
