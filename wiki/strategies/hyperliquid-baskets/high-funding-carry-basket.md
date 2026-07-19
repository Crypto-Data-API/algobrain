---
title: "High Funding Carry Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, funding-rate, risk-management, market-regime, derivatives]
aliases: ["Funding Carry Factor Basket", "High Positive Funding Basket", "Funding Rate Carry Basket", "Crowded Long Carry Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[funding-rate-harvest]]", "[[crowded-long-funding-fade]]", "[[pairs-with-funding-differential]]", "[[funding-rate-arbitrage]]", "[[hl-vs-cex-funding-divergence]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "Perps with persistently high positive funding rates have levered retail longs paying carry to shorts; by going short the highest-funding perps (earning carry) and hedging BTC-beta with a long on a low-funding major, the strategy earns the funding spread as a structural carry income while maintaining approximately market-neutral exposure to broad market direction."
data_required: [funding-rates, open-interest, ohlcv-daily, ohlcv-1h, long-short-ratio]
min_capital_usd: 20000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 20
kill_criteria: |
  - basket drawdown > 25% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 15 completed trades
  - funding rates on top-decile perps normalise to < 0.03%/8h for > 14 consecutive days (carry income collapses)
  - any position in the basket gaps > 25% against the carry direction in < 4h (squeeze precondition; exit immediately)
---

# High Funding Carry Basket (Hyperliquid Basket)

A factor basket — not a sector basket — that dynamically selects the **highest-funding-rate perpetuals on Hyperliquid** and goes short them (earning the positive funding as carry income), hedging BTC-beta with a proportional long in a low-funding major (BTC-PERP or ETH-PERP). The basket is reconstructed weekly from the current funding-rate leaderboard. It is a factor-exposure basket: what changes each week is which tokens are in it, not which sector.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Structural + risk-bearing** (see [[edge-taxonomy]]). Persistently high positive funding (above 0.05%/8h) on a perp signals crowded levered longs paying carry to shorts; the structural mechanism is that levered longs demand immediacy and do not carefully observe the carry cost. The strategy is paid to provide the hedge they need. See [[funding-rate-harvest]] for the pure long-funding-harvest design; this basket is the **short-leg expression** of that edge.

## Basket Construction (Factor-Based, Dynamic)

Rather than a fixed list of constituents, this basket is rebuilt weekly from the funding-rate leaderboard:

**Step 1: Rank all HL perps by 7-day average 8h funding rate (descending).**
- Source: `GET /api/v1/derivatives/funding-rates?coin=X` for all HL perps.

**Step 2: Select top 5–8 perps by funding rate, subject to:**
- 7-day average funding ≥ 0.05%/8h (annualised ≥ 54.75%) — below this, the carry is too small to cover costs.
- Daily perp volume ≥ $5M (thin perps have squeeze risk that overwhelms carry income).
- OI short-side ≥ 15% of total OI (if shorts are < 15%, a squeeze is imminent; skip this perp).
- No imminent major unlock or catalyst within 7 days (check event calendar).

**Step 3: Short selected perps, equal notional.**
**Step 4: Long BTC-PERP (or ETH-PERP) in offsetting notional to hedge BTC-beta.**
- Beta-hedge ratio: 1:1 notional for simplicity; optionally adjust by the perp's rolling 30-day BTC correlation.

**Typical constituents (illustrative; will vary each week):** High-funding perps are most commonly meme tokens, newly listed tokens, or momentum-driven altcoins with crowded long positioning. Examples from historical periods: PEPE, WIF, BONK, DOGE, specific AI tokens during hype cycles.

## Weighting Scheme

**Equal-weight short legs**; hedge long in BTC-PERP scaled to match total short-leg notional.

## Rebalance Cadence

**Weekly** — the entire basket is re-screened and rebuilt from the current funding-rate leaderboard. The highest-funding perps change week to week as sentiment rotates. Individual position exits also occur if: (a) funding on that position drops below 0.02%/8h (carry no longer sufficient), or (b) OI shorts drop below 10% (squeeze precondition).

## Regime Character

This basket earns when: high positive funding persists across multiple altcoin perps (crowded bull market or speculative frenzy in specific sectors). Earns least when: funding normalises after a market correction, or when the short squeeze on individual names triggers losses that exceed the accumulated carry income. The [[crowded-long-funding-fade]] basket uses this same signal but also takes a directional price-reversion bet; this basket is the pure-carry version.

## Strategies That Deploy This Basket

- [[funding-rate-harvest]] — the neutral carry version (long spot / short perp); this basket is the pure-perp-short carry version
- [[crowded-long-funding-fade]] — the directional extension; expects the crowded long to fade in price as well
- [[pairs-with-funding-differential]] — uses the funding signal as a pairs-entry gate; this basket is the standalone funding-carry expression
- [[cross-sectional-relative-value]] — the funding score is one component of the cross-sectional ranking; this basket is the pure-funding-factor slice

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=X` — for all HL perps; build leaderboard
- `GET /api/v1/derivatives/open-interest?coin=X` — OI for short-side check
- `GET /api/v1/derivatives/long-short-ratio?coin=X` — long/short ratio for squeeze precondition
- `GET /api/v1/event/calendar` — upcoming unlocks/catalysts that could break the carry trade

**Historical:**
- `GET /api/v1/backtesting/funding` — historical funding rates for all HL perps; used to calibrate the 0.05%/8h threshold

```bash
# Build funding-rate leaderboard for all HL perps
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

[[hyperliquid-baskets-overview]] · [[funding-rate-harvest]] · [[crowded-long-funding-fade]] · [[pairs-with-funding-differential]] · [[funding-rate-arbitrage]] · [[hl-vs-cex-funding-divergence]] · [[cross-sectional-relative-value]] · [[hyperliquid-funding-rate-microstructure]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
