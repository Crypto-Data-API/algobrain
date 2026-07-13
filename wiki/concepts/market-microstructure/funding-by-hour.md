---
title: "Funding By Hour"
type: concept
created: 2026-05-16
updated: 2026-07-13
status: good
tags: [crypto, derivatives, market-microstructure, arbitrage]
aliases: ["Funding Cycle", "Funding Schedule", "Intraday Funding"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[funding-rate]]", "[[perpetual-futures]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[funding-rate]]"
  - "[[funding-rate-arbitrage]]"
  - "[[crypto-trading-sessions]]"
  - "[[perpetual-futures]]"
  - "[[coinglass]]"
  - "[[hyperliquid]]"
  - "[[dydx]]"
---

# Funding By Hour

**Funding by hour** is the time-of-day rhythm of [[perpetual-futures]] funding payments — the predictable intraday cadence at which longs and shorts settle the cash flows that keep perp prices anchored to spot. While the [[funding-rate]] page covers the mechanism, this page covers *when* funding fires across venues, how the rate varies across [[crypto-trading-sessions]], and the workflows traders use to time entries and harvest cross-venue spreads.

## The 8-Hour Cycle

Most major centralized perp venues run discrete 8-hour funding windows. Funding is *quoted* continuously as the perp drifts above or below the spot index, but it is *paid* only at three timestamps per day. The canonical schedule on [[binance]], Bybit, and OKX is:

| Venue | Funding stamps (UTC) | Periods/day |
|-------|----------------------|-------------|
| [[binance]] USDⓈ-M perps | 00:00, 08:00, 16:00 | 3 |
| Bybit USDT perps | 00:00, 08:00, 16:00 | 3 |
| OKX USDT perps | 00:00, 08:00, 16:00 | 3 |

The mechanics: at each stamp, holders of the position at that exact second pay or receive the rate accumulated over the prior 8 hours. A trader who closes a long ten seconds before 16:00 UTC pays nothing for that window; a trader who opens at 15:59:59 and holds through the stamp pays the full 8-hour rate. This produces a small but real **funding-stamp arbitrage** for the alert: large positions are routinely flipped, hedged, or sized down in the minutes before a stamp to avoid paying, then re-entered immediately after (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

Conceptually, well-designed perps are far more liquid than dated futures and use these small, frequent funding payments — rather than expiry settlement — to keep prices aligned with [[spot-price]] (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## Cross-Venue Variation

DeFi perp venues run on a more continuous cadence:

| Venue | Funding cadence | Notes |
|-------|-----------------|-------|
| [[hyperliquid]] | Hourly | 24 payments/day; smaller per-stamp magnitude but more granular convergence |
| [[dydx]] | Hourly (event-driven on parts of the stack) | Sub-stamp granularity; cross-collateral makes hedging cheaper |
| [[binance]] / Bybit / OKX | 8-hourly | Discrete, predictable, and crowded by funding-rate arbs |

Because hourly funding on [[hyperliquid]] is roughly 1/8 the magnitude of an 8-hourly rate that would produce the same daily annualised number, traders comparing dashboards must normalise — a 0.001%/hour rate on Hyperliquid is comparable to roughly 0.008%/8h on a CEX, not to the raw 0.01% baseline most CEX dashboards display.

The asymmetric schedule also creates **cross-venue spread trades**: if Hyperliquid funding is paying long-side 0.001%/h while Binance is charging long-side 0.05%/8h, an arb can long on Hyperliquid and short on Binance for a net carry, subject to execution risk, collateral fragmentation, and auto-deleveraging risk (see [[perpetual-futures#Auto-Deleveraging-ADL]]).

## Cross-Session Patterns

Empirically, funding rates are not flat across the clock or the week (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]):

- **Midweek US hours**: funding tends to spike during high-conviction directional runs that coincide with [[crypto-trading-sessions|London-NY overlap]]. Speculative longs pile into perps as US desks and ETF flow drive spot; perp premium widens; longs pay shorts at the next stamp.
- **Weekends and off-peak Asia**: funding compresses toward the interest-rate baseline (~0.01%/8h on most CEXs) as speculative activity drops, market makers tighten quotes less aggressively, and the perp-spot basis narrows. Weekend funding is rarely the driver of major P&L.
- **Around macro releases (FOMC, CPI, payrolls)**: funding can flip violently as positioning unwinds; the 16:00 UTC stamp on Binance frequently catches the tail of US-session moves into the European close.

This rhythm is not a guarantee — funding regime depends on the broader market cycle (see the [[perpetual-futures#Funding-Rate-Regime-History|funding-rate regime history]]) — but the *intraday* pattern of "quiet weekends, midweek US-hours spikes" has held through both the 2024 ETF-era boom and the post-cascade compression (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## How Traders Use It

Three practical workflows dominate:

1. **Stamp-timed entry/exit.** A swing trader entering a short on a leveraged alt will prefer to open just *after* a funding stamp when funding is strongly positive, banking 8 hours of funding receipts before the next payment risk. Conversely, closing a long *before* the 16:00 UTC stamp during a midweek US rally avoids paying into a crowded book.
2. **Funding spread as a positioning signal.** When Binance funding diverges materially from Hyperliquid or Bybit for the same asset, the spread itself is informative: a venue with persistently higher long-pays-short funding has a crowded long book *on that venue*, often reflecting that exchange's regional retail base. Many traders use these spreads as a [[sentiment]] confirmation before fading.
3. **Arbitrage when funding diverges across venues or against spot.** This is the classic delta-neutral [[funding-rate-arbitrage]] play: long the venue where you receive funding, short the venue where you pay. Round-trip costs, [[slippage]], and auto-deleveraging risk (see [[perpetual-futures#Auto-Deleveraging-ADL]]) determine whether the carry survives. The trade is most attractive when one venue's funding is extreme during a specific regional session and least attractive when funding has been crowded out by basis traders.

## Practical Workflow

The standard real-time monitoring stack:

- **[[coinglass]] funding dashboards** — the canonical cross-exchange view. Funding is quoted per 8h for CEXs and per 1h for DeFi venues; the panel sorts by current rate, predicted next rate, and annualised-equivalent. Liquidation heatmaps on the same platform sit alongside, which matters because crowded funding regimes precede the liquidation cascades that thin sessions amplify.
- **CEX UI funding timers.** Binance, Bybit, and OKX all display a live countdown to the next stamp inside their perp trading interface. Active traders watch this clock the same way an equity trader watches the closing bell.
- **Custom alerts.** Quant desks build alerts on (a) funding crossing predefined thresholds, (b) cross-venue funding spread widening past N basis points, and (c) funding sign flips, which often coincide with regime changes.

For most discretionary traders, the operational rule is simple: know what time the next stamp is in your home venue's UTC clock, and never hold a leveraged position across a stamp without checking the predicted rate.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[funding-rate]] — mechanism, formula, and interpretation table
- [[funding-rate-arbitrage]] — the canonical delta-neutral carry trade
- [[crypto-trading-sessions]] — Asia/London/NY framework that drives funding's intraday pattern
- [[perpetual-futures]] — instrument context and ADL risk
- [[coinglass]] — primary dashboard for monitoring funding across venues
- [[hyperliquid]] — hourly funding venue
- [[dydx]] — event-driven funding venue
- [[binance]] — 8-hourly funding venue

## Sources

- (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]])
