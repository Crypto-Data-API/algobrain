---
title: "New Listing Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, event-driven, altcoins, market-regime, derivatives]
aliases: ["New Perp Listing Basket", "Fresh Listing Event Basket", "HL New Listing Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[exchange-listing-delisting]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[meme-coin-cycle]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[hyperliquid-oracle-mechanics]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [informational, structural]
edge_mechanism: "Newly listed Hyperliquid perpetuals exhibit a predictable 3–14 day post-listing price pattern: an initial euphoria pump (liquidity vacuum + unhedged demand) followed by a mean-reversion; the information edge is detecting the listing before it is fully priced (monitoring HL meta feed) and entering the reversion rather than the pump, or fading the euphoria with size limits appropriate for thin oracle conditions."
data_required: [ohlcv-1h, funding-rates, open-interest, mark-price, hyperliquid-meta]
min_capital_usd: 5000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 50
kill_criteria: |
  - basket drawdown > 35% from peak on a rolling 3-month basis
  - rolling 3-month Sharpe < 0 on minimum 8 completed new-listing trades
  - any single new-listing position triggers the JELLY-pattern squeeze guard (price up > 30% in < 1h on thin volume → immediate exit)
---

# New Listing Basket (Hyperliquid Basket)

An event-driven basket that trades the **post-listing price pattern** of newly added Hyperliquid perpetuals. Rather than chasing the initial listing pump (which is dominated by insider flows and oracle risk), the basket targets the 2–10 day post-euphoria mean reversion on thin new listings, or selectively participates in the long side of high-quality new listings backed by strong fundamental narratives during confirmed bull regimes.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

**Critical risk note:** new HL listings carry elevated [[hyperliquid-oracle-mechanics|oracle risk]] (thin oracle referencing a single pool), JELLY-pattern short squeeze risk (see [[2025-03-jellyjelly-hlp-attack]]), and thin-book liquidation risk. This basket requires the most conservative position sizing in the basket library.

## Edge Source

**Informational + structural** (see [[edge-taxonomy]]). The information edge is detecting new HL listings via the `/api/v1/hyperliquid/meta` feed before the price is fully established. The structural edge is the predictable post-listing pattern: initial euphoria → peak funding → reversion as early buyers take profit.

## Basket Construction (Event-Driven, Dynamic)

This basket has no fixed constituents. It is populated by **newly listed HL perps** meeting all of:

1. Listed on HL within the prior **7 days** (from `GET /api/v1/hyperliquid/meta` change feed).
2. Daily perp volume ≥ **$1M** (below this, oracle risk is too high for any systematic entry).
3. Mark price is within **±20%** of the first-day closing price (avoid entering after a ≥ 20% pump or dump — too late for the post-listing pattern).
4. Not a known meme-coin micro-cap (route those to [[meme-coin-cycle]] instead).

**Maximum 3 concurrent new-listing positions.** Each held for no more than **14 days** from listing date; exit regardless of P&L at day 14.

**Entry signal:** 8h funding rate on the new listing > 0.15%/8h (crowded longs paying carry; reversion candidate) AND price has already moved > 15% from listing-day close. Enter short at market, isolated margin.

**Exit:** funding normalises to < 0.05%/8h, OR price reverts to within 5% of listing-day close, OR 14-day time stop, OR position drawdown > 20%.

**Hard guard:** if price moves > 30% against the position in < 4h on thin volume → immediate exit at market (JELLY-pattern squeeze guard). See [[2025-03-jellyjelly-hlp-attack]].

## Weighting Scheme

**Fixed small notional per trade: 0.5% of book maximum per new listing.** Do not scale up based on conviction — the oracle and squeeze risks are irreducible at the position level. Thin listings can move 100% in minutes; leverage ≤ 2× for any new-listing position.

## Rebalance Cadence

**Continuous monitoring** of `GET /api/v1/hyperliquid/meta` for new listings. Each new qualifying listing is evaluated within 24–48 hours of listing date for entry. Exits are event-driven (signal, time stop, or guard trigger).

## Regime Character

Active in bull-market periods when HL is regularly listing new perps (listing pace tends to accelerate in bull markets). More risky in bear markets where new listings fail to generate even initial interest and reversion patterns are weaker. The basket should be sized at minimum in bear markets (0.25% of book per trade instead of 0.5%).

## Strategies That Deploy This Basket

- [[exchange-listing-delisting]] — the cross-exchange listing event strategy; this basket is the HL-specific new-perp listing version
- [[meme-coin-cycle]] — new meme listings during meme season go to that basket; this basket handles non-meme new listings
- [[cross-sectional-relative-value]] — new listings that survive 30+ days may eventually be added to the sector classification for this basket

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/meta` — monitor for new HL perp listings (change detection required)
- `GET /api/v1/hyperliquid/candles?coin=X&interval=1h&limit=48` — first 48h of new listing price action
- `GET /api/v1/derivatives/funding-rates?coin=X` — funding rate on new listing (entry signal)
- `GET /api/v1/hyperliquid/l2-book?coin=X` — L2 book depth on new listing (oracle/squeeze risk assessment)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/meta"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[exchange-listing-delisting]] · [[meme-coin-cycle]] · [[2025-03-jellyjelly-hlp-attack]] · [[hyperliquid-oracle-mechanics]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]] · [[when-to-retire-a-strategy]]
