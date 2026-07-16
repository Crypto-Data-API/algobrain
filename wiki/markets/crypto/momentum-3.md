---
title: "Momentum"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["MMT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.mmt.finance/"
related: ["[[crypto-markets]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[oi-confirmed-trend]]", "[[liquidation-cascade-fade]]"]
---

# Momentum

**Momentum** (MMT) is a Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Sui Ecosystem, Coinbase Ventures Portfolio, OKX Ventures Portfolio, Binance HODLer Airdrops, Binance Wallet IDO, CeFi project. It ranks **#770** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MMT |
| **Market Cap Rank** | #770 |
| **Market Cap** | $22.13M |
| **Current Price** | $0.10854 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Sui Ecosystem, Coinbase Ventures Portfolio, OKX Ventures Portfolio, Binance HODLer Airdrops, Binance Wallet IDO, CeFi |
| **Website** | [https://www.mmt.finance/](https://www.mmt.finance/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 204.10M MMT |
| **Total Supply** | 1.00B MMT |
| **Max Supply** | 1.00B MMT |
| **Fully Diluted Valuation** | $120.47M |
| **Market Cap / FDV Ratio** | 0.20 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.03 (2025-11-04) |
| **Current vs ATH** | -97.01% |
| **All-Time Low** | $0.1035 (2026-03-29) |
| **Current vs ATL** | +16.33% |
| **24h Change** | -1.10% |
| **7d Change** | +11.29% |
| **30d Change** | +1.00% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0x35169bc93e1fddfcf3a82a9eae726d349689ed59e4b065369af8789fe59f8608::mmt::MMT` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MMT/USDT | N/A |
| Upbit | MMT/KRW | N/A |
| Bitget | MMT/USDT | N/A |
| KuCoin | MMT/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.mmt.finance/](https://www.mmt.finance/) |
| **Twitter** | [@MMTFinance](https://twitter.com/MMTFinance) |
| **Telegram** | [mmtfinance](https://t.me/mmtfinance) (39,950 members) |
| **GitHub** | [https://github.com/mmt-finance/clmm-sdk](https://github.com/mmt-finance/clmm-sdk) |
| **Whitepaper** | [https://docs.mmt.finance/](https://docs.mmt.finance/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 15 |
| **GitHub Forks** | 8 |
| **Pull Requests Merged** | 74 |
| **Contributors** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.92M |
| **Market Cap Rank** | #770 |
| **24h Range** | $0.1204 — $0.1254 |
| **CoinGecko Sentiment** | 100% positive |
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

MMT is tradable on [[binance]] — both spot (MMT/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract, which exposes [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data. It is NOT listed on Hyperliquid, so Binance is the primary (and effectively sole) leveraged venue. This concentration means the perp funding, OI, and liquidation prints on Binance are the definitive derivatives signal for MMT — there is no deep alternative perp book to cross-check or arbitrage against. As a small-cap (~#557 by market cap) with modest 24h volume, the perp order book is thin: large leveraged size should be scaled in against limit orders, since aggressive market execution will slip and can itself trigger the cascades that fade strategies target. Spot liquidity across Binance, Upbit, Bitget, and KuCoin can be used to hedge or exit, but Binance perp is where leverage, funding, and forced-liquidation dynamics live.

### Applicable strategies

- [[funding-rate-harvest]] — the single-venue Binance perp lets a delta-neutral spot-long/perp-short position collect funding when MMT's perp trades at a premium during momentum-driven rallies.
- [[crowded-long-funding-fade]] — after sharp small-cap pumps, persistently positive funding flags over-leveraged longs on the only perp venue, setting up a mean-reversion fade.
- [[liquidation-cascade-fade]] — thin perp liquidity makes MMT prone to sharp forced-liquidation wicks; fading the overshoot after a Binance cascade prints is a repeatable small-cap edge.
- [[oi-confirmed-trend]] — pairing rising Binance open interest with directional price helps distinguish a genuine trend from a low-conviction squeeze in this low-float name.
- [[breakout-and-retest]] — MMT sits far below its ATH near prior lows; range breaks with a retest offer defined-risk entries on volatile small-cap moves.
- [[atr-trailing-stop]] — given wide intraday ranges, an ATR-based trailing stop sizes exits to realized volatility rather than fixed ticks.

### Volatility & regime character

MMT is a small-cap DeFi/DEX infrastructure token on the Sui ecosystem with high-beta, reflexive price action — trading ~97% below its 2025 ATH near its all-time low. As a low-float altcoin (market cap far below FDV, ~0.20 ratio), it exhibits sharp, liquidity-driven swings and elevated sensitivity to broad crypto risk-on/risk-off swings, typically amplifying BTC/ETH direction. Behavior is narrative- and ecosystem-dependent (Sui DeFi flows, airdrop/IDO history) rather than driven by independent fundamentals.

### Risk flags

- **Venue concentration:** Binance is the only leveraged venue and a dominant spot venue — an outage, delisting, or margin-parameter change is a single point of failure for derivatives exposure.
- **Liquidity:** thin spot and perp books mean high slippage and elevated liquidation-cascade risk; size conservatively.
- **Emissions/unlocks:** circulating supply (~204M) is a fraction of the 1B max supply, so future unlocks/emissions are a structural sell-pressure overhang; monitor the vesting schedule around large releases.
- **Narrative dependence:** valuation hinges on Sui-ecosystem DeFi momentum and airdrop-era attention; fading narratives can compress liquidity quickly.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=MMTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=MMTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=MMT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=MMT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=MMTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=MMTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=MMT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
