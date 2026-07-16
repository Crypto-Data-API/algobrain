---
title: "RHEA"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, defi, altcoins]
aliases: ["RHEA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://rhea.finance/"
related: ["[[crypto-markets]]", "[[binance]]", "[[breakout-trading]]", "[[dca-strategy]]"]
---

# RHEA

**RHEA** (RHEA) is a cryptocurrency. It ranks **#1548** by market capitalization. The current DeFi landscape is highly fragmented—yield opportunities are spread across multiple chains, protocols, and wallets, creating a steep learning curve for users. To access the most efficient strategies, users often need to navigate different ecosystems, bridge assets across chains, and manage multiple wallets, increasing complexity, cost, and risk.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RHEA |
| **Market Cap Rank** | #1548 |
| **Market Cap** | $5.15M |
| **Current Price** | $0.0130 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), BTCfi Protocol, Binance Alpha Spotlight |
| **Website** | [https://rhea.finance/](https://rhea.finance/) |

---

## Overview

The current DeFi landscape is highly fragmented—yield opportunities are spread across multiple chains, protocols, and wallets, creating a steep learning curve for users. To access the most efficient strategies, users often need to navigate different ecosystems, bridge assets across chains, and manage multiple wallets, increasing complexity, cost, and risk. This fragmentation makes it difficult for everyday users to participate in DeFi confidently and profitably.

RHEA addresses these issues by offering a unified, cross-chain platform that integrates the NEAR ecosystem's top DeFi primitives—Ref (DEX) and Burrow (lending)—with seamless BTC bridging via the Satoshi Bridge. Users can deploy capital and generate yield from a single Bitcoin wallet, eliminating operational friction while improving capital efficiency and access to higher yields. RHEA transforms a fragmented experience into a simple, streamlined, and cost-effective solution for earning yield across chains.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 397.43M RHEA |
| **Total Supply** | 999.57M RHEA |
| **Max Supply** | 1.00B RHEA |
| **Fully Diluted Valuation** | $12.95M |
| **Market Cap / FDV Ratio** | 0.40 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1133 (2025-08-02) |
| **Current vs ATH** | -88.55% |
| **All-Time Low** | $0.00867467 (2026-04-19) |
| **Current vs ATL** | +49.49% |
| **24h Change** | -0.48% |
| **7d Change** | -1.33% |
| **30d Change** | -18.10% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Near Protocol

### Contract Addresses

| Chain | Address |
|---|---|
| Near Protocol | `token.rhealab.near` |
| Binance Smart Chain | `0x4c067de26475e1cefee8b8d1f6e2266b33a2372e` |
| Solana | `8SMMso8Muv8d6i4WmMDthKt6TN1ysN6937sx3DKLXZqB` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Bitget | RHEA/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://rhea.finance/](https://rhea.finance/) |
| **Twitter** | [@rhea_finance](https://twitter.com/rhea_finance) |
| **Telegram** | [rhea_finance](https://t.me/rhea_finance) (34,740 members) |
| **Discord** | [https://discord.gg/rheafinance](https://discord.gg/rheafinance) |
| **GitHub** | [https://github.com/ref-finance](https://github.com/ref-finance) |
| **Whitepaper** | [https://guide.rhea.finance/rhea-finance-white-paper](https://guide.rhea.finance/rhea-finance-white-paper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $233,927.00 |
| **Market Cap Rank** | #1548 |
| **24h Range** | $0.0130 — $0.0132 |
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

RHEA is tradable on **Binance SPOT only** — no liquid perpetual venue exists, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding, basis, and liquidation strategies do **not** apply. With a micro-cap footprint and thin 24h volume, order books are shallow: large market orders will incur meaningful slippage. Execution should favor limit orders, staged entries/exits, and small clip sizes relative to visible depth. The absence of margin/perp venues means position sizing must be cash-funded and directional exposure cannot be hedged or amplified via derivatives, so risk is best managed through spot position size and stop discipline rather than leverage.

### Applicable strategies

- [[breakout-trading]] — thin-book micro-cap that can gap sharply on volume expansion; range breaks offer defined entries.
- [[breakout-and-retest]] — waiting for a breakout to retest confirms follow-through and reduces false-signal risk in low-liquidity conditions.
- [[atr-trailing-stop]] — volatility-scaled trailing exits protect gains and cap downside on a spot-only, no-hedge asset.
- [[dca-strategy]] — accumulating in small tranches smooths entry cost given shallow depth and sharp intraday swings.
- [[narrative-trading]] — as a NEAR-ecosystem DeFi/BTCfi token, price is sensitive to ecosystem and BTCfi narrative flow.
- [[range-trading]] — extended sideways drift between support/resistance suits fading extremes within a defined band.

### Volatility & regime character

Small-cap DeFi/BTCfi infrastructure token in the NEAR ecosystem with high idiosyncratic volatility. As a low-liquidity altcoin it exhibits strong high-beta behavior versus BTC/ETH in risk-on and risk-off swings, amplified by shallow books. Trades far below its all-time high, so regime is narrative- and liquidity-driven rather than trend-persistent, with reflexive moves on volume spikes.

### Risk flags

- **Liquidity/venue concentration** — spot-only, low 24h volume; slippage and exit risk are elevated, and venue availability could change.
- **Emissions/supply** — circulating supply is well below max supply (MC/FDV ~0.40), so future unlocks and emissions are a persistent dilution overhang.
- **Narrative dependence** — value is tied to NEAR-ecosystem and BTCfi DeFi narratives; sentiment shifts can drive outsized moves.
- **Regulatory** — as a DeFi/DEX-related token, evolving regulatory treatment of decentralized exchanges and yield products is a background risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=RHEAUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=RHEAUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=RHEAUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=RHEAUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
