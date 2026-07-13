---
title: "CryptoDataAPI"
type: source
created: 2026-07-13
updated: 2026-07-13
status: excellent
tags: [data-provider, crypto, api, derivatives, on-chain, market-regime, hyperliquid, backtesting, sentiment]
aliases: ["CryptoDataApi", "Crypto Data API", "cryptodataapi.com", "CDA"]
source_type: data
source_url: "https://cryptodataapi.com"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi-market-data]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-hyperliquid-traders]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-indicators]]", "[[cryptodataapi-dex]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-strategy-baskets]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-nft]]", "[[coinglass]]", "[[glassnode]]", "[[hyperliquid-api-and-sdk]]", "[[data-sources-overview]]"]
---

CryptoDataAPI ([cryptodataapi.com](https://cryptodataapi.com), Australia) is the **canonical data layer for this wiki**: a single REST API with 190+ endpoints spanning live crypto market data, derivatives positioning, Hyperliquid perp and trader intelligence, multi-family market-regime classification, on-chain flows, sentiment, DEX/memecoin screening, NFTs, and a point-in-time backtesting archive going back to 2020. Where a wiki page describes data an endpoint serves, the page carries a **"Getting the Data (CryptoDataAPI)"** section with the live and historical access patterns.

## Access

- **Base URL**: `https://cryptodataapi.com`
- **Auth**: `X-API-Key` header on every request (create a key via `POST /api/v1/auth/keys`; rotate via `POST /api/v1/auth/keys/rotate`)
- **Docs**: https://cryptodataapi.com/api/docs

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

### Plans & rate limits

| Tier | Requests | Burst | Unlocks |
|------|----------|-------|---------|
| Free | 50/day | 5/min | Core live endpoints |
| Pro | 10,000/day | 30/min | Per-coin quant matrices, trader profiles, copy signals, DEX promoted feed |
| Pro Plus | Unlimited | 60/min | Point-in-time quant history, Parquet regime archive (2020+), whale history, refresh triggers |

## Category map

| Category | Page | What it covers |
|----------|------|----------------|
| Coins | [[cryptodataapi-coins]] | 500+ aggregated asset profiles, search, categories, top-N |
| Market Data | [[cryptodataapi-market-data]] | Binance spot klines/tickers, BTC price history + 200D MA, volume, daily bulk snapshots |
| Derivatives | [[cryptodataapi-derivatives]] | Funding rates, open interest, long/short ratio — Binance + cross-exchange |
| Hyperliquid | [[cryptodataapi-hyperliquid]] | Perp prices, funding, OI, OHLCV candles, L2 order book |
| Hyperliquid Traders | [[cryptodataapi-hyperliquid-traders]] | Leaderboard, wallet positions/signals, trader profiles, copy-trading signals, watchlists |
| Market & Quant Regimes | [[cryptodataapi-regimes]] | 10-state market regimes, HMM quant probabilities (6 regimes), volatility/liquidity/meme/event/security/policy regimes |
| Market Intelligence | [[cryptodataapi-market-intelligence]] | BTC cycle indicators, ETF flows, liquidations, options max-pain, exchange balance, Coinbase premium, taker buy/sell |
| On-Chain | [[cryptodataapi-on-chain]] | Stablecoin reserves & dry powder, exchange flows, miner reserves, hash ribbon, MVRV dormancy, whale scores |
| Sentiment & Macro | [[cryptodataapi-sentiment]] | Fear & Greed, stablecoin supply/flows, macro (EUR/USD, gold, yields) |
| Market Health | [[cryptodataapi-market-health]] | Dual-score market health (11 components), altcoin breadth |
| Indicators | [[cryptodataapi-indicators]] | Signum RGG (ADX/DMI), technical price-structure state (SMA/BB/RSI) |
| DEX & Memecoins | [[cryptodataapi-dex]] | Trending pools, new launches, token security/rug reports, promotion-spend signal |
| Strategy Baskets | [[cryptodataapi-strategy-baskets]] | 50 meta-baskets across 6 thematic groups |
| Backtesting | [[cryptodataapi-backtesting]] | Historical klines/funding/liquidations, point-in-time daily snapshots, Parquet archives since 2020 |
| NFTs | [[cryptodataapi-nft]] | Market overview, collections, volume, correlations |

## Why it is the wiki's canonical layer

- **Live + historical in one surface** — most signal families expose both a current endpoint and a history/backtesting endpoint, so strategy pages can cite one provider for research and production
- **Regime-native** — the regime endpoints map directly onto this wiki's [[crypto-market-regime-taxonomy|14-basket regime taxonomy]] and [[regime-strategy-playbook]]
- **Point-in-time discipline** — the [[cryptodataapi-backtesting|backtesting archive]] provides dated snapshots and Parquet downloads, addressing [[lookahead-bias]] and [[point-in-time-data]] requirements
- **Webhooks** — `GET/POST /api/v1/webhooks` for push-based alerting into trading systems

## Related

- [[coinglass]] — browser-first derivatives aggregator; CryptoDataAPI is the API-first counterpart
- [[glassnode]], [[cryptoquant]] — on-chain analytics alternatives
- [[hyperliquid-api-and-sdk]] — trading (order placement) on Hyperliquid; CryptoDataAPI covers the intelligence layer
- [[data-sources-overview]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
