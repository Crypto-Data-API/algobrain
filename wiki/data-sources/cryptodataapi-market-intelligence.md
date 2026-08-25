---
title: "CryptoDataAPI — Market Intelligence"
type: source
created: 2026-07-13
updated: 2026-08-25
status: good
tags: [data-provider, crypto, api, etf-flows, liquidations, options, cycle-indicators, coinbase-premium, market-intelligence]
aliases: ["CryptoDataAPI Market Intelligence", "CDA Market Intelligence", "Market Intelligence API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[spot-etf-flows]]", "[[max-pain]]", "[[liquidation]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-news]]"]
---

The Market Intelligence category of [[cryptodataapi]] aggregates the institutional and structural signals that sit above raw price: BTC cycle indicators, spot-ETF AUM and flows, cross-exchange liquidations, options [[max-pain]], exchange BTC balances, the Coinbase premium, Grayscale holdings, taker buy/sell ratio, margin borrow interest, and long-run Fear & Greed and stablecoin histories. Most endpoints carry historical series, making this the wiki's one-stop source for cycle- and flow-level context.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/market-intelligence/btc/cycle-indicators | All 8 BTC cycle indicators, historical | — | — |
| GET | /api/v1/market-intelligence/btc/cycle-indicators/{indicator} | Single indicator by name, historical | indicator | — |
| GET | /api/v1/market-intelligence/etf/btc/aum | BTC ETF AUM, reconstructed estimate from cumulative flows | — | — |
| GET | /api/v1/market-intelligence/etf/{asset}/flows | BTC/ETH/SOL ETF flows, historical (XRP unsupported — 400) | asset | — |
| GET | /api/v1/market-intelligence/liquidations | Cross-exchange liquidations (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/options | BTC options (OI, volume, max pain) | — | — |
| GET | /api/v1/market-intelligence/exchange-balance | Exchange BTC balance + flow | — | — |
| GET | /api/v1/market-intelligence/coinbase-premium | Coinbase premium index, historical | — | — |
| GET | /api/v1/market-intelligence/funding-rates | Cross-exchange funding (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/open-interest | Cross-exchange OI (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/grayscale/holdings | Grayscale fund holdings | — | — |
| GET | /api/v1/market-intelligence/grayscale/premium | Grayscale BTC premium/discount (through Jan 2024) | — | — |
| GET | /api/v1/market-intelligence/taker-buy-sell | Taker buy/sell ratio by exchange, 4h window, per-coin | — | — |
| GET | /api/v1/market-intelligence/liquidations/by-exchange | Liquidations by venue, BTC only, 4h — streamed-venue subset only | — | — |
| GET | /api/v1/market-intelligence/borrow-interest | Margin borrow rate, BTC/Binance, 4h | — | — |
| GET | /api/v1/market-intelligence/fear-greed-history | Fear & Greed timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/stablecoin-history | Stablecoin mcap timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/squeeze-alerts | One-sided, abnormal forced-liquidation flow — cascade tripwire | symbol, window_s, min_severity, include_quiet, limit | Pro (free tier scoped to BTC) |
| GET | /api/v1/market-intelligence/status | Collector status + rate usage | — | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

## Live Data

`/etf/btc/aum` is explicitly live; `/liquidations`, `/options`, `/exchange-balance`, `/funding-rates`, `/open-interest`, `/grayscale/holdings`, `/taker-buy-sell` (4h window), `/liquidations/by-exchange` (4h), and `/borrow-interest` (4h) report current or recent-window state. `/status` shows collector health and rate usage.

**`/etf/btc/aum` is a reconstructed estimate, not a bare total.** It has no `aum_usd` field. It derives AUM by accumulating flows over time and returns `aum_usd_from_flows`, `btc_held_from_flows`, `btc_price_usd`, `cumulative_net_flow_usd`, `price_appreciation_usd`, `as_of`, `since`, `flow_days`, plus `method`, `source`, `excludes`, and `caveats` metadata fields describing the reconstruction. The `_from_flows` suffix is deliberate: GBTC's conversion from a closed-end trust to an ETF carried over a pre-existing BTC stake that never shows up as a tracked inflow, so the figure understates the true complex by roughly that seed amount. `cumulative_net_flow_usd` is a *different* quantity from AUM — the gap between the two is `price_appreciation_usd` (the return on assets already held, not new money).

**`/etf/{asset}/flows` supports BTC, ETH, and SOL only.** `xrp` now returns a `400` (previously it 503'd) — no free source publishes XRP spot-ETF flow data, so the API does not serve it. SOL flow coverage was dead from 2026-07-24 and came back live on 2026-08-22.

**`/liquidations/by-exchange` coverage caveat** (shared with `/liquidations`): rows only cover the streamed venue subset — OKX, Bybit, and Hyperliquid — because Binance geo-blocks its liquidation stream. Totals therefore run *under* a true all-exchange number. The endpoint was returning `503` on every call from 2026-07-24 until fixed 2026-08-22; a `503` today should only mean a cold start (first minutes after a deploy, before the trailing 4h window has venue-tagged events).

**`/squeeze-alerts` (new) is a cascade tripwire, not a news feed** — explicitly the answer to news being 15-45 minutes behind a breaking story (see [[cryptodataapi-news]]). It flags coins whose forced-liquidation flow is one-sided and abnormal right now: `direction` (`short_squeeze` / `long_flush` / `balanced`), `severity` (0-1), `triggered`, `asymmetry`, `side_ratio`, `spike_ratio`, `oi_change_pct`, `oi_state`, and `suppressed_by` (which gate blocked an alert — `no_spike_baseline`, `spike_ratio`, `asymmetry`, `severity`, `min_notional`, `baseline_too_young`). **`direction` names the side being liquidated, not the price direction** — a short liquidation is forced buying, so `short_squeeze` means upward price pressure. Severity is built ~80% from ratios (`spike_ratio` against the coin's trailing-24h mean, and `asymmetry`) rather than absolute dollar notionals, because notionals are the quantity most distorted by the same streamed-venue coverage gap noted above. `oi_state` (`covering` / `fresh_longs` / `capitulating` / `fresh_shorts` / `unclear`) is `null` until OI history has at least two samples — it distinguishes shorts covering into the squeeze from fresh longs piling on. Check `window_uptime_h`: `spike_ratio` understates on a recently reconnected feed.

## Historical Data

Historical series come from `/btc/cycle-indicators` (all 8 indicators, or one via `{indicator}`), `/etf/{asset}/flows` (BTC/ETH/SOL), `/coinbase-premium`, `/grayscale/premium` (data through Jan 2024), `/fear-greed-history`, and `/stablecoin-history`. For liquidation records back through the archive, use `/api/v1/backtesting/liquidations` on [[cryptodataapi-backtesting]].

## Trading Applications

- [[spot-etf-flows]] — daily BTC/ETH/SOL ETF flow series (no XRP) plus the reconstructed live BTC AUM estimate quantify the institutional bid that has driven post-2024 cycles
- [[max-pain]] — `/options` returns BTC options OI, volume, and the max-pain strike for expiry-pinning and dealer-positioning analysis
- [[liquidation]] cascades — cross-exchange and per-venue liquidation feeds identify forced-flow events and stop-hunt zones, subject to the streamed-venue coverage caveat above; `/squeeze-alerts` adds a real-time cascade tripwire on top, ahead of the 15-45 minute lag on [[cryptodataapi-news]]
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
- [[cryptodataapi-news]] — catalyst tape and news pressure/tilt features; `/squeeze-alerts` is the same-second complement to its 15-45min lag
- [[spot-etf-flows]], [[max-pain]], [[liquidation]] — concept pages

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
