---
title: "BounceBit"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["BB"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bouncebit.io/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# BounceBit

**BounceBit** (BB) is a CeDeFi infrastructure project and EVM-compatible Layer 1 blockchain focused on bringing tokenized real-world assets (RWAs) into crypto markets. It ranks **#1310** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BB |
| **Market Cap Rank** | #1310 |
| **Market Cap** | $7.53M |
| **Current Price** | $0.0184 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Restaking, Proof of Stake (PoS), Binance Megadrop |
| **Website** | [https://bouncebit.io/](https://bouncebit.io/) |

---

## Overview

BounceBit is a CeDeFi infrastructure project and EVM-compatible Layer 1 blockchain focused on bringing tokenized real-world assets (RWAs) into crypto markets. Through BounceBit Prime, the platform connects Franklin Templeton’s Benji and BlackRock’s BUIDL via Securitize with regulated custody and onchain execution, allowing yield-bearing institutional assets to be used as productive collateral across trading, treasury, and structured yield strategies.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 409.50M BB |
| **Total Supply** | 2.10B BB |
| **Max Supply** | 2.10B BB |
| **Fully Diluted Valuation** | $38.63M |
| **Market Cap / FDV Ratio** | 0.19 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.8658 (2024-06-06) |
| **Current vs ATH** | -97.88% |
| **All-Time Low** | $0.0180 (2026-07-14) |
| **Current vs ATL** | +2.22% |
| **24h Change** | -1.12% |
| **7d Change** | -1.25% |
| **30d Change** | -20.60% |
| **1y Change** | -83.18% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd459eceddafcc1d876a3be7290a2e16e801073a3` |
| Solana | `76SYfdi8jT84GqxuTqu7FuyA4GQbrto1pLDGQKsy8K12` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BB/TRY | N/A |
| Bitget | BB/USDT | N/A |
| KuCoin | BB/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bouncebit.io/](https://bouncebit.io/) |
| **Twitter** | [@bouncebit](https://twitter.com/bouncebit) |
| **Telegram** | [bouncebit_io](https://t.me/bouncebit_io) (19,366 members) |
| **Discord** | [https://discord.com/invite/bouncebit](https://discord.com/invite/bouncebit) |
| **GitHub** | [https://github.com/BounceBit-Labs](https://github.com/BounceBit-Labs) |
| **Whitepaper** | [https://docs.bouncebit.io/](https://docs.bouncebit.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.49M |
| **Market Cap Rank** | #1310 |
| **24h Range** | $0.0183 — $0.0190 |
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

BB is tradable on **Binance** — both **spot** and a **USD-margined perpetual** (BBUSDT), which exposes funding, open interest, and liquidation data. It is **not** listed on Hyperliquid, so **Binance is the primary leveraged venue**. Because leveraged flow is concentrated on a single perp venue with a low market cap (~#1311) and thin 24h volume, order books are shallow and the perp funding/OI signal is dominated by Binance positioning. Practically, this means execution should assume meaningful slippage on larger clips, position sizing must be conservative, and there is no cross-venue perp to hedge or arb the leveraged leg against — any spot/perp basis play must route through Binance itself. Liquidation cascades can be sharp given the concentrated leverage and shallow depth.

### Applicable strategies

- [[funding-rate-harvest]] — collect BB perp funding on Binance when the single-venue perp runs persistently one-sided against spot.
- [[crowded-long-funding-fade]] — low-cap restaking token prone to speculative long crowding; fade extended positive funding into mean reversion.
- [[cash-and-carry]] — hold Binance spot BB against a short BBUSDT perp to capture positive basis when funding is elevated.
- [[liquidation-cascade-fade]] — thin depth plus concentrated leverage produces overshoot liquidations; fade the flush and reclaim.
- [[oi-price-exhaustion]] — use Binance open-interest divergence versus price to flag exhausted moves in a low-liquidity name.
- [[token-unlock-supply-event]] — large locked supply (MC/FDV ~0.19) means scheduled unlocks are tradable supply overhangs.

### Volatility & regime character

BB is a small-cap CeDeFi / restaking infrastructure token with high realized volatility and strong reflexivity typical of low-float, low-liquidity alts. It trades as a high-beta play on BTC/ETH risk-on regimes but is heavily narrative-driven (RWA / CeDeFi / restaking, BounceBit Prime), so idiosyncratic catalysts can decouple it from majors. Directional moves tend to be exaggerated by thin books, and correlation to BTC/ETH tightens during broad market stress.

### Risk flags

- **Liquidity & venue concentration:** thin 24h volume and leverage concentrated on Binance's single perp — slippage and cascade risk are elevated.
- **Unlocks & emissions:** MC/FDV ratio ~0.19 implies substantial locked supply; unlock schedules are a persistent dilution/overhang risk.
- **Narrative dependence:** valuation hinges on the RWA/CeDeFi/restaking narrative and institutional integrations; sentiment shifts can drive outsized drawdowns.
- **Regulatory:** RWA and tokenized-securities exposure (via custody/Securitize partners) carries regulatory sensitivity that can affect the token.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BBUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=BBUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=BB` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BB` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BBUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BBUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BB"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
