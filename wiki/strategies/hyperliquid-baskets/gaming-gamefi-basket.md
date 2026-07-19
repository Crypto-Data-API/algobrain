---
title: "Gaming / GameFi Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, gamefi, market-regime]
aliases: ["GameFi Basket", "Crypto Gaming Basket", "Web3 Gaming Basket", "Play-to-Earn Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral]
edge_mechanism: "GameFi tokens are driven by bull-market retail speculation and specific gaming-season narratives (major game launches, tournament events, platform milestones); the sector co-moves strongly during risk-on regimes and provides high-beta exposure to the crypto gaming cycle with concentrated within-sector dispersion driven by individual game-adoption metrics."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 15000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.50
breakeven_cost_bps: 40
kill_criteria: |
  - basket drawdown > 50% from peak on a rolling 6-month basis
  - gaming/metaverse narrative absent from top-20 crypto narratives for > 90 days
  - rolling 6-month Sharpe < -0.2 on minimum 10 trades
---

# Gaming / GameFi Basket (Hyperliquid Basket)

A sector basket of blockchain gaming and GameFi tokens with active Hyperliquid perpetuals. Captures the crypto gaming and metaverse narrative cycle — characteristically late-cycle, high-beta, and retail-driven. Deployed only in confirmed risk-on / alt-season regimes.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral** (see [[edge-taxonomy]]). Gaming tokens are pure narrative plays with minimal revenue; their price cycles are driven by anticipation of game launches, major gaming studio partnerships, and the broader "metaverse" or "web3 gaming" narrative. The predictable structure of these hype cycles (announcement → listing → play-to-earn launch → inflation-driven decline) creates tradeable momentum and exit patterns.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Immutable | IMX | Ethereum gaming L2; largest gaming-focused blockchain |
| Axie Infinity | AXS | Pioneered P2E; multi-cycle survivor |
| The Sandbox | SAND | Metaverse/gaming platform; established brand |
| Gala | GALA | Multi-game ecosystem; established GameFi presence |
| Illuvium | ILV | High-production-value RPG; open-world gaming narrative |
| Big Time | BIGTIME | MMORPG; high-profile gaming token launch |

**Constituent count:** 6. Minimum $2M daily HL perp volume required.

## Selection Rule

Constituents must: (1) have an active blockchain game or gaming platform (not just a gaming-adjacent infrastructure token); (2) ≥ $2M daily HL perp volume; (3) ≥ 6 months of trading history (avoid first-week listing pumps — route to exchange-listing-delisting basket instead).

## Weighting Scheme

**Equal-weight**. AXS and SAND are larger-cap; IMX has higher liquidity. Equal-weight maintains exposure to the higher-beta smaller constituents where the cycle alpha concentrates.

## Rebalance Cadence

Weekly. Event-driven out-of-cycle rebalance on major game launches or platform milestones.

## Regime Character

Strong in late-bull / alt-season when retail capital seeks highest-beta exposure. Historically weakest in prolonged bear markets where gaming-token inflation from play-to-earn mechanics creates structural sell pressure. Gaming tokens often lag the first wave of alt-season and lead the final euphoric leg — useful timing signal.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long gaming when sector ranks top momentum quintile in late alt-season
- [[cross-sectional-relative-value]] — long gaming leaders vs. short underperformers
- [[narrative-position-vol-targeting]] — gaming narrative exposure with vol-capped sizing
- [[alt-season-momentum-gate]] — gaming basket activated late in confirmed alt-season

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=IMX&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=AXS`
- `GET /api/v1/derivatives/open-interest?coin=AXS`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=AXS&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[alt-season-momentum-gate]] · [[meme-coin-cycle]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
