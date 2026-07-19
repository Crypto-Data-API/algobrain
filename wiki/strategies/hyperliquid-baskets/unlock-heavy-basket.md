---
title: "Unlock-Heavy Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, event-driven, altcoins, derivatives, open-interest]
aliases: ["Unlock Risk Basket", "Token Unlock Short Basket", "High-Unlock Exposure Basket", "Supply-Event Risk Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[token-unlock-supply-event]]", "[[unlock-pair-hedge]]", "[[unlock-short-with-crowding-gate]]", "[[unlock-aware-momentum]]", "[[unlock-cascade-watch]]", "[[mythos-release-window-exploit-short]]", "[[cross-sectional-relative-value]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [informational, structural]
edge_mechanism: "Tokens with imminent large cliff-unlocks (≥ 5% of circulating supply releasing within 7–14 days) face a predictable supply-shock headwind that is observable in advance via unlock calendars; the basket systematically shorts the highest-unlock-concentration tokens in the 7–14 days before unlock execution, where historical average token price underperformance vs. sector peers has been −5% to −15% in the pre-unlock window."
data_required: [token-unlock-schedule, ohlcv-daily, ohlcv-4h, funding-rates, open-interest, circulating-supply, perp-price]
min_capital_usd: 10000
capacity_usd: 10000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.30
breakeven_cost_bps: 45
kill_criteria: |
  - basket drawdown > 30% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed unlock trades
  - unlock front-running becomes fully priced in (realised pre-unlock alpha < 1% average over 20 consecutive trades)
---

# Unlock-Heavy Basket (Hyperliquid Basket)

An event-driven basket that **systematically shorts Hyperliquid perpetuals of tokens with imminent large cliff unlocks**, exploiting the predictable supply-shock headwind in the 7–14 day pre-unlock window. The basket is short-only by design — it does not hold long positions in unlock-event tokens. Each position is time-limited to the unlock event window.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Informational + structural** (see [[edge-taxonomy]]). The unlock schedule is publicly observable in advance via token unlock calendars (Token Unlocks, Coinglass, project vesting schedules). The price impact is structural — large unlocks increase circulating supply and create selling pressure from vested recipients. The information edge is systematic pre-screening of the calendar rather than reacting after unlock announcement.

## Basket Construction (Event-Driven, Dynamic)

Rebuilt **daily** from the unlock calendar screen:

**Step 1: Screen upcoming unlocks (7–14 days ahead):**
- Unlock size ≥ **5% of current circulating supply** in a single cliff event.
- Unlock recipient is **insiders, investors, or team** (not community/staking rewards — those are distributed gradually and have less concentrated selling pressure).
- Token has an active HL perp with ≥ **$3M daily volume** (thin perps add squeeze risk without improving the short thesis).

**Step 2: Short qualification check:**
- HL perp funding rate < **0.10%/8h** (if funding is very high positive, the short will pay excessive carry; wait for funding normalisation or skip this token).
- OI short-side ≥ **15%** of total OI (if shorts are already crowded < 15%, front-running squeeze risk; skip).
- No ongoing governance proposal that could short-squeeze the position (check unlock-cascade-watch monitoring).

**Step 3: Enter short on qualifying tokens.**
- Position size: **0.5–1.0%** of book per token (smaller than typical baskets — unlock front-running is crowded).
- Leverage: **2× maximum**, isolated margin.
- Entry window: **T−14 to T−7 days before unlock** (the historical sweet spot; prices tend to decline most in the final 7 days before unlock).

**Step 4: Exit.**
- Target exit by **T−1 day before unlock** (do not hold through the unlock date itself — unexpected project buybacks or ecosystem announcements can reverse the short).
- Stop: price moves > 15% against the short → exit immediately (unlock may be delayed or cancelled).
- Time stop: exit by T−1 regardless of P&L.

**Maximum 4 concurrent unlock-short positions.**

## Weighting Scheme

**Equal-weight** across active positions. Each token is sized at the same notional (0.5–1.0% of book) regardless of unlock size — larger unlocks do not necessarily produce larger price impacts (institutional buyers sometimes absorb large unlocks in OTC markets before the on-chain execution).

## Rebalance Cadence

**Daily screening** of unlock calendar. New positions opened as qualifying events enter the T−14 to T−7 window. Exits are event-driven (time stop at T−1, price stop, or P&L target at −10% average pre-unlock move).

## Regime Character

Active in all market regimes — unlock pressure is a supply shock independent of macro direction. However, in strong bull markets, buyers absorb unlocks more quickly and the pre-unlock price decline is smaller (sometimes reverses post-unlock as pent-up demand enters). In bear or range markets, unlocks tend to produce larger and more sustained price declines. Size down in confirmed bull market regimes.

## Strategies That Deploy This Basket

- [[token-unlock-supply-event]] — the canonical unlock event strategy; this basket is the systematic HL-perp-short implementation
- [[unlock-pair-hedge]] — the beta-hedged version (short unlock token, long sector peer); this basket is the pure-short version
- [[unlock-short-with-crowding-gate]] — adds a crowding check before shorting; closely related
- [[unlock-aware-momentum]] — avoids momentum entries in tokens with upcoming unlocks; complementary
- [[unlock-cascade-watch]] — monitors post-unlock cascade dynamics; provides exit signal context

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/event/calendar` — token unlock calendar (upcoming unlocks with size and recipient type)
- `GET /api/v1/hyperliquid/candles?coin=X&interval=4h&limit=84` — 14-day 4h klines for pre-unlock price trend
- `GET /api/v1/derivatives/funding-rates?coin=X` — funding check before short entry
- `GET /api/v1/derivatives/open-interest?coin=X` — OI short-side crowding check
- `GET /api/v1/derivatives/long-short-ratio?coin=X` — long/short ratio for squeeze risk assessment

**Historical:**
- `GET /api/v1/backtesting/klines` — historical unlock-window price performance analysis

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

## Related

[[hyperliquid-baskets-overview]] · [[token-unlock-supply-event]] · [[unlock-pair-hedge]] · [[unlock-short-with-crowding-gate]] · [[unlock-aware-momentum]] · [[unlock-cascade-watch]] · [[cross-sectional-relative-value]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]] · [[when-to-retire-a-strategy]]
