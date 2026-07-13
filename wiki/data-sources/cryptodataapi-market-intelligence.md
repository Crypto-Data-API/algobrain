---
title: "CryptoDataAPI — Market Intelligence"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, etf-flows, liquidations, options, cycle-indicators, coinbase-premium, market-intelligence]
aliases: ["CryptoDataAPI Market Intelligence", "CDA Market Intelligence", "Market Intelligence API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[spot-etf-flows]]", "[[max-pain]]", "[[liquidation]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-backtesting]]"]
---

The Market Intelligence category of [[cryptodataapi]] aggregates the institutional and structural signals that sit above raw price: BTC cycle indicators, spot-ETF AUM and flows, cross-exchange liquidations, options [[max-pain]], exchange BTC balances, the Coinbase premium, Grayscale holdings, taker buy/sell ratio, margin borrow interest, and long-run Fear & Greed and stablecoin histories. Most endpoints carry historical series, making this the wiki's one-stop source for cycle- and flow-level context.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/market-intelligence/btc/cycle-indicators | All 8 BTC cycle indicators, historical | — | — |
| GET | /api/v1/market-intelligence/btc/cycle-indicators/{indicator} | Single indicator by name, historical | indicator | — |
| GET | /api/v1/market-intelligence/etf/btc/aum | BTC ETF total AUM, live | — | — |
| GET | /api/v1/market-intelligence/etf/{asset}/flows | BTC/ETH/SOL/XRP ETF flows, historical | asset | — |
| GET | /api/v1/market-intelligence/liquidations | Cross-exchange liquidations (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/options | BTC options (OI, volume, max pain) | — | — |
| GET | /api/v1/market-intelligence/exchange-balance | Exchange BTC balance + flow | — | — |
| GET | /api/v1/market-intelligence/coinbase-premium | Coinbase premium index, historical | — | — |
| GET | /api/v1/market-intelligence/funding-rates | Cross-exchange funding (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/open-interest | Cross-exchange OI (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/grayscale/holdings | Grayscale fund holdings | — | — |
| GET | /api/v1/market-intelligence/grayscale/premium | Grayscale BTC premium/discount (through Jan 2024) | — | — |
| GET | /api/v1/market-intelligence/taker-buy-sell | Taker buy/sell ratio by exchange, 4h window, per-coin | — | — |
| GET | /api/v1/market-intelligence/liquidations/by-exchange | Liquidations by venue, BTC only, 4h | — | — |
| GET | /api/v1/market-intelligence/borrow-interest | Margin borrow rate, BTC/Binance, 4h | — | — |
| GET | /api/v1/market-intelligence/fear-greed-history | Fear & Greed timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/stablecoin-history | Stablecoin mcap timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/status | Collector status + rate usage | — | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

## Live Data

`/etf/btc/aum` is explicitly live; `/liquidations`, `/options`, `/exchange-balance`, `/funding-rates`, `/open-interest`, `/grayscale/holdings`, `/taker-buy-sell` (4h window), `/liquidations/by-exchange` (4h), and `/borrow-interest` (4h) report current or recent-window state. `/status` shows collector health and rate usage.

## Historical Data

Historical series come from `/btc/cycle-indicators` (all 8 indicators, or one via `{indicator}`), `/etf/{asset}/flows`, `/coinbase-premium`, `/grayscale/premium` (data through Jan 2024), `/fear-greed-history`, and `/stablecoin-history`. For liquidation records back through the archive, use `/api/v1/backtesting/liquidations` on [[cryptodataapi-backtesting]].

## Trading Applications

- [[spot-etf-flows]] — daily BTC/ETH/SOL/XRP ETF flow series plus live BTC AUM quantify the institutional bid that has driven post-2024 cycles
- [[max-pain]] — `/options` returns BTC options OI, volume, and the max-pain strike for expiry-pinning and dealer-positioning analysis
- [[liquidation]] cascades — cross-exchange and per-venue liquidation feeds identify forced-flow events and stop-hunt zones
- Cycle timing — the 8 BTC cycle indicators plus Coinbase premium (US institutional spot demand vs offshore) and exchange BTC balance frame where we sit in the [[bitcoin-cycle-regime]] map
- Demand quality — taker buy/sell ratio and borrow interest separate aggressive spot demand from leverage-driven rallies, complementing [[cryptodataapi-derivatives]] funding data

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/etf/btc/flows"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-derivatives]] — deeper funding/OI/long-short detail per symbol
- [[cryptodataapi-on-chain]] — exchange flows, miner reserves, and MVRV
- [[cryptodataapi-sentiment]] — live Fear & Greed and stablecoin flow snapshots
- [[cryptodataapi-backtesting]] — liquidation and snapshot archives
- [[spot-etf-flows]], [[max-pain]], [[liquidation]] — concept pages

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
