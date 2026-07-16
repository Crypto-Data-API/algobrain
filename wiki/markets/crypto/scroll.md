---
title: "Scroll"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins, ethereum]
aliases: ["SCR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://scroll.io/"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[basis-trading]]", "[[liquidation-cascade-fade]]"]
---

# Scroll

**Scroll** (SCR) is designed from the ground-up to maximize compatibility with Ethereum Virtual Machine. Thanks to bytecode-level compatibility with EVM, your existing applications and favorite tools are compatible with Scroll out-of-the-box. It ranks **#1619** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SCR |
| **Market Cap Rank** | #1619 |
| **Market Cap** | $4.66M |
| **Current Price** | $0.0245 |
| **Categories** | Smart Contract Platform, Binance Launchpool, Layer 2 (L2), Zero Knowledge (ZK) |
| **Website** | [https://scroll.io/](https://scroll.io/) |

---

## Overview

Scroll is designed from the ground-up to maximize compatibility with Ethereum Virtual Machine. Thanks to bytecode-level compatibility with EVM, your existing applications and favorite tools are compatible with Scroll out-of-the-box. Being the most popular virtual machine for blockchains, EVM enables new developers to easily pick up Solidity or Vyper through countless tutorials, open-source code, and online communities.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 190.00M SCR |
| **Total Supply** | 1.00B SCR |
| **Max Supply** | 1.00B SCR |
| **Fully Diluted Valuation** | $24.53M |
| **Market Cap / FDV Ratio** | 0.19 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.43 (2024-12-13) |
| **Current vs ATH** | -98.29% |
| **All-Time Low** | $0.0238 (2026-07-15) |
| **Current vs ATL** | +2.65% |
| **24h Change** | -3.85% |
| **7d Change** | -8.12% |
| **30d Change** | -27.49% |
| **1y Change** | -92.98% |

---

## Platform & Chain Information

**Native Chain:** Scroll

### Contract Addresses

| Chain | Address |
|---|---|
| Scroll | `0xd29687c813d741e2f938f4ac377128810e217b1b` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SCR/USDT | N/A |
| Upbit | SCR/BTC | N/A |
| KuCoin | SCR/USDT | N/A |
| Crypto.com Exchange | SCROLL/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://scroll.io/](https://scroll.io/) |
| **Twitter** | [@Scroll_ZKP](https://twitter.com/Scroll_ZKP) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.42M |
| **Market Cap Rank** | #1619 |
| **24h Range** | $0.0238 — $0.0261 |
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

SCR trades as a deep, liquid two-venue market. It is available on **Binance** (SCR/USDT spot plus a USD-margined perpetual) and on **Hyperliquid** (SCR-PERP, with leverage up to roughly 40-50x). The Binance spot leg supplies a reliable borrow/inventory source, while both venues run continuous perp order books, so cross-venue price discovery is tight. The dual-venue footprint means funding, basis, and OI can be compared directly across a centralized and a decentralized book, and it lets traders route or split size to minimize slippage. As a low-market-cap L2 token, order-book depth thins quickly away from mid, so position sizing should respect available depth on each venue rather than assuming headline 24h volume is all executable at once.

### Applicable strategies

- [[funding-rate-arbitrage]] — capture funding differentials by holding offsetting SCR-PERP legs while netting directional risk across Binance and Hyperliquid.
- [[hl-vs-cex-funding-divergence]] — trade the funding spread between Hyperliquid SCR-PERP and the Binance USD-margined perp when the two books drift apart.
- [[cash-and-carry]] — long Binance SCR spot against a short perp to harvest a positive basis on this two-venue name.
- [[basis-trading]] — exploit spot-vs-perp basis dislocations in a thin L2 token where perps can decouple from spot under flow.
- [[liquidation-cascade-fade]] — fade over-extended wicks after leverage flushes, which are amplified in a low-cap perp with shallow depth.
- [[breakout-and-retest]] — trade confirmed range breaks on the retest, useful for a beaten-down token pinned near its all-time low that can gap on narrative shifts.

### Volatility & regime character

SCR is a high-beta, low-market-cap Layer 2 / ZK-rollup infrastructure token. Price action is dominated by ETH-ecosystem and broad-alt beta: it tends to amplify ETH and BTC moves on the downside and is highly reflexive to L2/rollup and airdrop narratives. Realized volatility is elevated and asymmetric to the downside, as reflected in its deep drawdown from all-time high toward all-time low. Correlation to ETH beta is high, with idiosyncratic spikes around Scroll-specific catalysts.

### Risk flags

- **Liquidity / depth concentration** — a low-cap name with modest 24h volume; large orders can move the book on either venue and slippage risk is real.
- **Token unlocks / emissions** — circulating supply is a small fraction of total/max supply (low market-cap-to-FDV ratio), so scheduled unlocks and emissions are a persistent supply overhang.
- **Narrative dependence** — value is tied to L2/ZK-rollup and Ethereum-scaling narratives; sentiment rotation out of the sector can drive outsized moves.
- **Perp funding dislocations** — thin two-venue perp liquidity means funding can spike or invert sharply, punishing crowded leverage and creating cascade risk.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=SCR` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=SCR` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=SCR&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=SCR&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=SCR"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
