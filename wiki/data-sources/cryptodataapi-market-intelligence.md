---
title: "CryptoDataAPI — Market Intelligence"
type: source
created: 2026-07-13
updated: 2026-09-28
status: good
tags: [data-provider, crypto, api, etf-flows, liquidations, options, cycle-indicators, coinbase-premium, market-intelligence]
aliases: ["CryptoDataAPI Market Intelligence", "CDA Market Intelligence", "Market Intelligence API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[spot-etf-flows]]", "[[max-pain]]", "[[liquidation]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-news]]"]
---

The Market Intelligence category of [[cryptodataapi]] aggregates the institutional and structural signals that sit above raw price: BTC cycle indicators, spot-ETF AUM and flows, cross-exchange liquidations, options [[max-pain]], exchange BTC balances, the Coinbase premium, taker buy/sell ratio, and long-run Fear & Greed and stablecoin histories. Most endpoints carry historical series, making this the wiki's one-stop source for cycle- and flow-level context.

> [!warning] `/grayscale/*` and `/borrow-interest` retired from the live API (verified 2026-09-04)
> `/market-intelligence/grayscale/holdings`, `/market-intelligence/grayscale/premium`, and `/market-intelligence/borrow-interest` are **no longer in the live OpenAPI spec** (`curl https://cryptodataapi.com/api`) and the `/api/v1/changelog` feed carries no rename entry for them (10-release retention window, so a rename further back is unrecoverable from the API). There is **no documented replacement** for any of the three — Grayscale-specific holdings/premium data and the Binance margin-borrow-rate proxy are simply gone from this category. For a leverage-cost proxy, use perp funding (`/derivatives/funding-rates`, [[cryptodataapi-derivatives]]) instead of the borrow rate. Rows kept below (struck through) for path-history context; do not call them.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/market-intelligence/btc/cycle-indicators | All 8 BTC cycle indicators, historical | — | — |
| GET | /api/v1/market-intelligence/btc/cycle-indicators/{indicator} | Single indicator by name, historical | indicator | — |
| GET | /api/v1/market-intelligence/etf/btc/aum | BTC ETF AUM, reconstructed estimate from cumulative flows (settled days only since 2026-09-25) | — | — |
| GET | /api/v1/market-intelligence/etf/{asset}/flows | BTC/ETH/SOL ETF net flow per settled US trade date; default = latest settled day (XRP unsupported — 400) | asset, days (1-1000, default 1) | — |
| GET | /api/v1/market-intelligence/liquidations | Cross-exchange liquidations — trailing 1h/4h/12h/24h levels per coin (top coins, default HL) | symbol, exchange, limit | Free = BTC only; Pro/Pro Plus = full universe |
| GET | /api/v1/market-intelligence/options | BTC options (OI, volume, max pain) | — | — |
| GET | /api/v1/market-intelligence/exchange-balance | Exchange BTC balance + flow | — | — |
| GET | /api/v1/market-intelligence/coinbase-premium | Coinbase premium index, historical | — | — |
| GET | /api/v1/market-intelligence/funding-rates | Cross-exchange funding (top coins, default HL) | — | — |
| GET | /api/v1/market-intelligence/open-interest | Cross-exchange OI (top coins, default HL) | — | — |
| ~~GET~~ | ~~/api/v1/market-intelligence/grayscale/holdings~~ | **RETIRED** (verified 2026-09-04) — Grayscale fund holdings; no replacement | — | — |
| ~~GET~~ | ~~/api/v1/market-intelligence/grayscale/premium~~ | **RETIRED** (verified 2026-09-04) — Grayscale BTC premium/discount (through Jan 2024); no replacement | — | — |
| GET | /api/v1/market-intelligence/taker-buy-sell | Taker buy/sell ratio by exchange, 4h window, per-coin (Binance + Hyperliquid legs) | — | — |
| GET | /api/v1/market-intelligence/liquidations/by-exchange | Liquidations by venue, BTC only, 4h — streamed-venue subset only | — | — |
| GET | /api/v1/market-intelligence/squeeze-alerts | Coins with one-sided, abnormal forced-liquidation flow right now (`direction`, `severity`, `triggered`, `suppressed_by`) | symbol, window_s, min_severity, include_quiet, limit | Free = BTC only; Pro/Pro Plus = full universe |
| ~~GET~~ | ~~/api/v1/market-intelligence/borrow-interest~~ | **RETIRED** (verified 2026-09-04) — margin borrow rate, BTC/Binance, 4h; no replacement, use perp funding as a leverage-cost proxy instead | — | — |
| GET | /api/v1/market-intelligence/fear-greed-history | Fear & Greed timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/stablecoin-history | Stablecoin mcap timeseries, historical | — | — |
| GET | /api/v1/market-intelligence/squeeze-alerts | One-sided, abnormal forced-liquidation flow — cascade tripwire | symbol, window_s, min_severity, include_quiet, limit | Pro (free tier scoped to BTC) |
| GET | /api/v1/market-intelligence/status | Collector status + rate usage | — | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

## Live Data

`/etf/btc/aum` is explicitly live; `/liquidations`, `/options`, `/exchange-balance`, `/funding-rates`, `/open-interest`, `/taker-buy-sell` (4h window), and `/liquidations/by-exchange` (4h) report current or recent-window state. `/status` shows collector health and rate usage. (`/grayscale/holdings` and `/borrow-interest` are retired — see warning above.)

**`/etf/btc/aum` is a reconstructed estimate, not a bare total.** It has no `aum_usd` field. It derives AUM by accumulating flows over time and returns `aum_usd_from_flows`, `btc_held_from_flows`, `btc_price_usd`, `cumulative_net_flow_usd`, `price_appreciation_usd`, `as_of`, `since`, `flow_days`, plus `method`, `source`, `excludes`, and `caveats` metadata fields describing the reconstruction. The `_from_flows` suffix is deliberate: GBTC's conversion from a closed-end trust to an ETF carried over a pre-existing BTC stake that never shows up as a tracked inflow, so the figure understates the true complex by roughly that seed amount. `cumulative_net_flow_usd` is a *different* quantity from AUM — the gap between the two is `price_appreciation_usd` (the return on assets already held, not new money).

**`/etf/{asset}/flows` supports BTC, ETH, and SOL only.** `xrp` now returns a `400` (previously it 503'd) — no free source publishes XRP spot-ETF flow data, so the API does not serve it. SOL flow coverage was dead from 2026-07-24 and came back live on 2026-08-22.

**BREAKING — `/etf/{asset}/flows` now returns settled trade-date values (changed 2026-09-25).** Before this release the route read Farside's newest row *while issuers were still reporting* and stamped it with the fetch time, so on most weekdays it served a **partial sum**. Farside fills a day fund by fund, with IBIT and FBTC last, so the missing part was usually the largest. Example: for the 2026-09-23 BTC trade date it served +$32.4M (MSBT alone), while the settled Total is +$346.9M. Only Friday figures read on the Saturday were correct. The rebuilt response:

- `flows` holds **settled days only, oldest first**. Each row carries `trade_date` (YYYY-MM-DD, the US trading day), `time` (now 00:00 UTC of `trade_date`, *not* the fetch time), `flow_usd` / `total_value` (the Farside Total in USD), `status: "final"` and `source` (`farside`, or `sosovalue` for a day Farside had not settled or could not be fetched)
- The default is the **latest settled day**, so `flows[0]` and `flows[-1]` both still read it. New `?days=N` (1-1000) returns the last N settled days, with history back to 2024-01-11 for BTC, 2024-07-23 for ETH and 2025-10-28 for SOL
- `latest` is the newest settled row. `in_progress` is the day still being reported (`status: "partial"`, plus `funds_reported` / `funds_total`), or `null`. **Never add `in_progress` to totals**, because it is a partial sum by construction
- Also new: `count` (rows in `flows`), `units` (`"USD"`), `sources` (`primary: farside.co.uk`, `backup: sosovalue.com`) and `source_health` (per-feed `last_ok` and `consecutive_failures`)
- SOL no longer reports `0.0` for a day with no reports yet. A Farside `-` now means **no value, not zero**

Live check on 2026-09-28: `?days=3` for BTC returned 2026-09-23 +$346.9M, 2026-09-24 +$190.7M and 2026-09-25 +$134.5M, all `status: "final"`, `source: "farside"`, with `in_progress: null` over the weekend.

**`/etf/btc/aum` sums settled days only (changed 2026-09-25).** It used to include the day still reporting. Its daily closes are now paged, so it keeps working once the flow history passes 1000 days.

**Archived ETF values before 2026-09-25 are partial on most weekdays.** `coinglass_etf_flows` snapshots (`/backtesting/snapshots`) and daily-snapshot ETF values are point-in-time copies of what the API served, so they hold the partial figure described above, and they are not being rewritten. For settled flow history, use `/etf/{asset}/flows?days=N`. Snapshots from 2026-09-25 onward carry `trade_date`, `status` and `source`. See [[cryptodataapi-backtesting]].

**`/taker-buy-sell` gained a Hyperliquid leg (2026-09-09).** Previously the endpoint carried only a `Binance` leg (BTC only, from Binance's public taker-volume endpoint). It now adds a `Hyperliquid` exchange leg — `buy_ratio` as a percent (0-100) of taker volume that was buying, notional-weighted over the trailing 4h — for every HL perp with fills, sourced from the collector's own trade tape (see `/hyperliquid/trade-flow` on [[cryptodataapi-hyperliquid]]). A coin only HL lists gets its own top-level entry whose aggregate is the HL figure. **An absent Hyperliquid leg means the tape is still warming (or the pull is not configured) — never that HL had zero trades for that coin.**

**`/liquidations` rows are trailing-window levels, not flows (changed 2026-09-23).** Each row's `liquidation_usd_*`, `long_liquidation_usd_*` and `short_liquidation_usd_*` fields (1h/4h/12h/24h) are trailing-window **levels**. **Never sum or difference successive polls**, because that double-counts. The response now says so in a top-level `grain` block (`kind: rolling_window`, `is_cumulative: true`, `sum_ok: false`), which uses the same vocabulary as the `/backtesting/*` readers. For incremental liquidation flow per closed bucket, use `/backtesting/hl-liquidation-bars` (Pro) on [[cryptodataapi-backtesting]]. The same release made two per-row fields real. They were CoinGlass-era leftovers that always read `0` / `null`, so a row with millions liquidated looked empty to anything that counted rows:

- `count` is the number of liquidation events in the 24h window. The new top-level `row_count_meaning: "liquidation_events_24h"` states this
- `source` names the venues those events came from, `+`-joined (for example `"bybit+hyperliquid+okx"`). It is `null` only when no event in the window carries a venue tag. AsterDEX-native rows keep `source: "asterdex"`

The response also carries `as_of`, `coverage` (venues, the Binance exclusion, windows) and `baseline`, which defines the per-row `liq_1h_vs_7d_median` ratio. Tier gating is unchanged (free = BTC). Live check on 2026-09-28: BTC showed `count: 3314`, `source: "bybit+hyperliquid+okx"` and $19.7M liquidated over 24h.

**`/liquidations/by-exchange` coverage caveat** (shared with `/liquidations`): rows only cover the streamed venue subset — OKX, Bybit, and Hyperliquid — because Binance geo-blocks its liquidation stream. Totals therefore run *under* a true all-exchange number. The endpoint was returning `503` on every call from 2026-07-24 until fixed 2026-08-22; a `503` today should only mean a cold start (first minutes after a deploy, before the trailing 4h window has venue-tagged events).

**`/squeeze-alerts` names the side being liquidated, not the price direction** — `direction: short_squeeze` means shorts are being forced to buy (upward pressure) and `long_flush` means longs are being forced to sell, so the label is correct before price confirms it. It shares the same venue coverage as `/liquidations/by-exchange` (OKX, Bybit, and Hyperliquid only — Binance geo-blocks its liquidation stream from this API's infrastructure) and hides rows that fail to trigger by default; pass `include_quiet=true` to see a suppressed row alongside the `suppressed_by` gate that blocked it. Free tier is scoped to BTC only; Pro and Pro Plus cover the full universe.

## Historical Data

Historical series come from `/btc/cycle-indicators` (all 8 indicators, or one via `{indicator}`), `/etf/{asset}/flows?days=N` (BTC/ETH/SOL, up to 1000 settled trade days — the only source of settled history, see the 2026-09-25 note above), `/coinbase-premium`, `/fear-greed-history`, and `/stablecoin-history`. (`/grayscale/premium`, formerly the source for Jan-2024-and-earlier Grayscale discount history, is retired — see warning above.) For liquidation records back through the archive, use `/api/v1/backtesting/liquidations` on [[cryptodataapi-backtesting]].

## Trading Applications

- [[spot-etf-flows]] — daily settled BTC/ETH/SOL ETF flow series (no XRP), keyed by US `trade_date`, plus the reconstructed live BTC AUM estimate quantify the institutional bid that has driven post-2024 cycles
- [[max-pain]] — `/options` returns BTC options OI, volume, and the max-pain strike for expiry-pinning and dealer-positioning analysis
- [[liquidation]] cascades — cross-exchange and per-venue liquidation feeds identify forced-flow events and stop-hunt zones, subject to the streamed-venue coverage caveat above; `/squeeze-alerts` adds a real-time cascade tripwire on top, ahead of the 15-45 minute lag on [[cryptodataapi-news]]
- Cycle timing — the 8 BTC cycle indicators plus Coinbase premium (US institutional spot demand vs offshore) and exchange BTC balance frame where we sit in the [[bitcoin-cycle-regime]] map
- Demand quality — taker buy/sell ratio separates aggressive spot demand from leverage-driven rallies, complementing [[cryptodataapi-derivatives]] funding data (the margin borrow-interest endpoint that used to sit alongside it is retired — see warning above)

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/etf/btc/flows?days=30"
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
- https://cryptodataapi.com/api (live OpenAPI JSON; `/market-intelligence/taker-buy-sell` description confirming the Hyperliquid exchange leg added 2026-09-09, fetched 2026-09-17)
- https://cryptodataapi.com/api (live OpenAPI JSON; rebuilt `/market-intelligence/etf/{asset}/flows` — `ETFFlowsResponse` `asset`/`units`/`latest`/`in_progress`/`count`/`flows`/`sources`/`source_health`, `days` param 1-1000 — and `/market-intelligence/liquidations` `grain`/`row_count_meaning`/`count`/`source`, confirmed against the spec and live calls, fetched 2026-09-28)
- https://cryptodataapi.com/api/v1/changelog (releases 2026-09-23 and 2026-09-25, fetched 2026-09-28)
