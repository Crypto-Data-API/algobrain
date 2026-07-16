---
title: "Celer Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["CELR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.celer.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Celer Network

**Celer Network** (CELR) is a Arbitrum Ecosystem, Ethereum Ecosystem, Bridge Governance Tokens, Binance Launchpad, Cross-chain Communication, Pantera Capital Portfolio, Energi Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio project. It ranks **#998** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CELR |
| **Market Cap Rank** | #998 |
| **Market Cap** | $13.48M |
| **Current Price** | $0.00238642 |
| **Categories** | Arbitrum Ecosystem, Ethereum Ecosystem, Bridge Governance Tokens, Binance Launchpad, Cross-chain Communication, Pantera Capital Portfolio, Energi Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio |
| **Website** | [https://www.celer.network/](https://www.celer.network/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 5.65B CELR |
| **Total Supply** | 10.00B CELR |
| **Max Supply** | 10.00B CELR |
| **Fully Diluted Valuation** | $23.87M |
| **Market Cap / FDV Ratio** | 0.56 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1948 (2021-09-26) |
| **Current vs ATH** | -98.77% |
| **All-Time Low** | $0.00095575 (2020-03-13) |
| **Current vs ATL** | +149.77% |
| **24h Change** | -5.37% |
| **7d Change** | -2.70% |
| **30d Change** | -7.96% |
| **1y Change** | -67.98% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4f9254c83eb525f9fcf346490bbb3ed28a81c667` |
| Energi | `0x1833e138fadf220eb951a8590b8ba9058785ddde` |
| Arbitrum One | `0x3a8b787f78d775aecfeea15706d4221b40f345ab` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CELR/USDT | N/A |
| Kraken | CELR/USD | N/A |
| Bitget | CELR/USDT | N/A |
| KuCoin | CELR/USDT | N/A |
| Crypto.com Exchange | CELR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X4F9254C83EB525F9FCF346490BBB3ED28A81C667/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X4F9254C83EB525F9FCF346490BBB3ED28A81C667/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.celer.network/](https://www.celer.network/) |
| **Twitter** | [@CelerNetwork](https://twitter.com/CelerNetwork) |
| **Reddit** | [https://www.reddit.com/r/celernetwork/](https://www.reddit.com/r/celernetwork/) |
| **Telegram** | [celernetwork](https://t.me/celernetwork) (8,318 members) |
| **Discord** | [https://discordapp.com/invite/Trhab5w](https://discordapp.com/invite/Trhab5w) |
| **GitHub** | [https://github.com/celer-network/sgn-v2-contracts](https://github.com/celer-network/sgn-v2-contracts) |
| **Whitepaper** | [https://im-docs.celer.network/developer/celer-im-overview](https://im-docs.celer.network/developer/celer-im-overview) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 140 |
| **GitHub Forks** | 104 |
| **Pull Requests Merged** | 237 |
| **Contributors** | 18 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.06M |
| **Market Cap Rank** | #998 |
| **24h Range** | $0.00238206 — $0.00254962 |
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

CELR is tradable on **Binance** as both **spot** (CELR/USDT) and a **USD-margined perpetual** contract, giving access to funding, open interest, and liquidation data. It is **not** listed on Hyperliquid, so **Binance is the primary leveraged venue** and effectively the reference market for any derivatives-based approach. With a sub-$15M cap and thin (~$2M) 24h spot volume, order books are shallow: available leverage is capped and tightens further in stress, so realistic position sizing must assume meaningful slippage and reduced max leverage. Concentration on a single perp venue means funding, OI, and liquidation signals all originate from Binance — execution should lean on limit/VWAP-style entries and scaled sizing rather than large market orders.

### Applicable strategies

- [[funding-rate-harvest]] — single-venue Binance USD-M perp lets a delta-neutral spot-vs-perp position collect funding when the small-cap perp trades at a persistent premium/discount.
- [[oi-confirmed-trend]] — pairing Binance open-interest changes with price filters out low-conviction moves on a thin, easily-spoofed CELR book.
- [[liquidation-cascade-fade]] — low liquidity and leverage clustering make CELR prone to sharp liquidation flushes that overshoot and mean-revert, offering fade entries.
- [[rsi-mean-reversion]] — the deeply drawn-down, range-bound micro-cap frequently prints oversold/overbought extremes that snap back, suiting oscillator reversion.
- [[breakout-and-retest]] — narrative or Binance-listing-driven volume spikes produce clean breakouts from long bases; retest entries manage the false-breakout risk of a low-float token.
- [[narrative-trading]] — as a cross-chain / bridge (interoperability) infrastructure token, CELR re-rates in bursts on interop and L2 narratives rather than steady trends.

### Volatility & regime character

CELR is a **small/micro-cap infrastructure token** (cross-chain messaging / bridging) with high beta to BTC and ETH and to broader alt risk-on/risk-off swings. Sitting ~99% below its 2021 ATH, it behaves reflexively: long stretches of illiquid drift punctuated by sharp, sentiment-driven spikes. It is not a memecoin, but its low float and thin liquidity give it memecoin-like reflexivity on the upside. Absent an idiosyncratic catalyst, it largely tracks ETH-ecosystem and interoperability-sector beta.

### Risk flags

- **Liquidity & venue concentration** — thin spot volume and Binance as the sole meaningful leveraged venue amplify slippage and single-venue outage/delisting risk.
- **Emissions/supply overhang** — circulating supply is ~57% of a 10B max; the remaining unissued supply is a structural sell-pressure risk.
- **Narrative dependence** — price is driven by episodic interop/bridge narratives; outside catalysts, liquidity and interest fade.
- **Stale-data / relevance risk** — the asset drifts in and out of the CoinGecko top 1000, so cached figures can be stale and listing status can change.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CELRUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CELRUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=CELR` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=CELR` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CELRUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CELRUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=CELR"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
