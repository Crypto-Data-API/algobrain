---
title: "CryptoDataAPI — Derivatives"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, derivatives, funding-rates, open-interest, binance, hyperliquid, perpetual-futures]
aliases: ["CryptoDataAPI Derivatives", "CDA Derivatives", "Derivatives API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[funding-rate]]", "[[funding-rates]]", "[[open-interest]]", "[[funding-rate-arbitrage]]", "[[perpetual-futures]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-market-data]]"]
---

The Derivatives category of [[cryptodataapi]] serves [[perpetual-futures]] positioning data — [[funding-rates]], [[open-interest]], and account long/short ratio — sourced from Binance Futures plus a cross-exchange layer that merges Binance and Hyperliquid into one view. It is the wiki's primary API surface for reading leverage, crowding, and carry conditions in perp markets.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/derivatives/binance/funding-rates | Binance perp funding history | symbol (default BTCUSDT), limit | — |
| GET | /api/v1/derivatives/binance/open-interest | Binance OI + 30d trend | symbol | — |
| GET | /api/v1/derivatives/binance/long-short-ratio | Binance account L/S ratio | symbol | — |
| GET | /api/v1/derivatives/binance/summary | All-in-one Binance summary | symbol | — |
| GET | /api/v1/derivatives/binance/history | Daily derivatives data | days 1-90 | — |
| GET | /api/v1/derivatives/funding-rates | Cross-exchange funding (Binance + Hyperliquid) | coin (default BTC) | — |
| GET | /api/v1/derivatives/open-interest | Cross-exchange OI | coin (default BTC) | — |
| GET | /api/v1/derivatives/summary | Combined overview | coin (markdown format option) | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

## Live Data

Current-state reads: `/derivatives/binance/open-interest` (spot OI level plus 30-day trend), `/derivatives/binance/long-short-ratio`, `/derivatives/binance/summary`, and the cross-exchange `/derivatives/funding-rates`, `/derivatives/open-interest`, and `/derivatives/summary` — the last of which is the single-call snapshot for a coin's full positioning picture across both venues.

## Historical Data

`/derivatives/binance/history` returns daily derivatives data for 1-90 days, and `/derivatives/binance/funding-rates` is itself a funding history series (paged with `limit`). For deeper archives — funding back to 2020 — use the [[cryptodataapi-backtesting]] endpoint `/api/v1/backtesting/funding`.

## Trading Applications

- [[funding-rate-arbitrage]] — `/derivatives/funding-rates` puts Binance and Hyperliquid funding for the same coin in one response, making cross-venue carry spreads directly observable
- Crowding fades — extreme [[funding-rate]] readings combined with stretched account long/short ratio flag one-sided positioning (see [[crowded-long-funding-fade]])
- Trend confirmation — rising price with rising [[open-interest]] confirms fresh positioning; rising price on falling OI signals a short-covering move instead
- Leverage-flush detection — pair the 30-day OI trend with [[liquidation]] data from [[cryptodataapi-market-intelligence]] to spot deleveraging cascades
- Regime inputs — funding and OI feed the leverage components of the [[cryptodataapi-market-health]] and [[cryptodataapi-regimes]] families

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BTC"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-hyperliquid]] — Hyperliquid-native perp data (prices, candles, L2 book)
- [[cryptodataapi-market-intelligence]] — cross-exchange liquidations, funding, and OI for top coins
- [[cryptodataapi-backtesting]] — historical funding and liquidation archives for research
- [[cryptodataapi-market-data]] — Binance spot klines and tickers
- [[funding-rate]], [[open-interest]], [[perpetual-futures]] — concept pages

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
