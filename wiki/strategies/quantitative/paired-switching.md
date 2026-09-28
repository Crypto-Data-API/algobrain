---
title: "Paired Switching"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [momentum, quantitative, position-trading, diversification, crypto, bitcoin, macro]
aliases: ["Paired Switching Strategy", "Two-Asset Relative Momentum Switch"]
strategy_type: quantitative
timeframe: position
markets: [crypto, bonds, commodities]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Relative performance between two weakly or negatively correlated assets persists over quarters because capital rotates slowly between risk-on and defensive assets; holding the recent winner harvests that persistence."
data_required: [ohlcv-daily]
min_capital_usd: 500
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: 0.5
expected_max_drawdown: 0.5
breakeven_cost_bps: 100
decay_evidence: "QuantConnect's port publishes no statistics (pending review). The relative-momentum premise is the same as dual-momentum rotation, which has weakened since its popularization in the 2010s."
kill_criteria: |
  - trailing 3-year return below the 50/50 static mix of the same two assets
  - more than 4 consecutive losing switches
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[momentum-rotation]]", "[[relative-strength]]", "[[time-series-momentum]]", "[[crypto-beta-rotation]]"]
---

# Paired Switching

**Paired switching** holds 100% of one of two assets and, each quarter, switches to whichever had the higher return over the previous 90 days. The two assets are chosen to be negatively (or weakly) correlated, so the portfolio rotates between a risk-on and a defensive holding. The idea comes from Quantpedia and is implemented in [[quantconnect|QuantConnect]]'s Strategy Library; this page adapts it to crypto-versus-defensive pairs (Source: [[quantconnect-strategy-library]]).

## Edge Source

**Behavioral** (relative momentum from slow capital rotation) and **risk-bearing** (full concentration, no hedging), per [[edge-taxonomy]].

## Why This Edge Exists

Intermediate-term relative momentum across asset classes is documented ([[time-series-momentum]], [[momentum-rotation]]): risk-on and risk-off regimes last months, and allocators rebalance quarterly or slower. A two-asset switch is the simplest way to own the leader. The other side is the rebalancer who mechanically sells the winner back to a static weight, and investors who buy the laggard on valuation. Using negatively correlated assets matters: when one is in a drawdown, the other is more likely to be rising, so the switch is into something that is actually working.

## Null Hypothesis

If 90-day relative returns have no persistence, the switch picks the next-quarter winner 50% of the time and its return equals the average of the two assets minus switching costs. Testable: compare against a 50/50 quarterly-rebalanced mix of the same pair and against random quarterly picks; the strategy must beat both after costs.

## Rules

1. Choose two assets with low or negative return correlation. Crypto adaptations (not from the source):
   - **BTC vs a stablecoin/T-bill yield proxy** — the classic risk-on/cash switch
   - **BTC vs gold** — digital vs physical store of value (use tokenized gold or futures)
   - **ETH vs BTC** — not negatively correlated, but a well-known relative-strength rotation
2. At each quarter end, compute each asset's return over the last 90 days.
3. Hold 100% of the asset with the higher return until the next quarter.
4. No stop, no leverage (source rule). Optional crypto safety rule: if both returns are negative, hold the cash leg.

## Implementation Pseudocode

```python
LOOKBACK, REBAL = 90, "Q"                     # days; quarter-end rebalance
for date in quarter_ends:
    r_a = close_a[date] / close_a[date - LOOKBACK] - 1
    r_b = close_b[date] / close_b[date - LOOKBACK] - 1
    target = "A" if r_a > r_b else "B"
    if target != holding:
        pay_cost(fee + spread)                 # one switch = sell + buy
        holding = target
    # optional: if max(r_a, r_b) < 0 -> hold cash leg
```

## Indicators / Data Used

- 90-day total return of each asset ([[relative-strength]])
- Stablecoin yield or T-bill rate if one leg is cash ([[stablecoin-yield]])

## Example Trade

Illustrative: at 2026-03-31, BTC's 90-day return is -18% and the stablecoin-yield leg earned +1.1%. The strategy moves to the cash leg. At 2026-06-30, BTC's trailing 90-day return is +24% versus +1.1%; the strategy moves back into BTC. One round trip per regime change; costs ~10-20 bps each on spot.

## Performance Characteristics

- **Source claim**: none — QuantConnect's entry is marked pending review and publishes no backtest statistics (Source: [[quantconnect-strategy-library]]).
- Expect the return profile of a coarse [[trend-following]] overlay: it misses the first part of each rally and the first part of each crash, and suffers in V-shaped reversals within a quarter.
- **Cost overlay**: at most 4 switches a year, so trading costs are negligible; the real cost is whipsaw.

## Capacity Limits

Effectively unlimited for BTC/gold/cash; quarterly spot switches of nine figures are feasible.

## What Kills This Strategy

- Sharp intra-quarter reversals (e.g., crypto crashes that start and end between rebalance dates).
- Correlation regime change: if both assets fall together (2022 BTC and bonds), switching does not help.
- Single-lookback fragility — the 90-day and quarter-end choices are arbitrary; see [[overfitting]] and [[failure-modes]].

## Kill Criteria

Retire per [[when-to-retire-a-strategy]] if the trailing 3-year return trails the static 50/50 mix of the same two assets.

## Advantages

- Extremely simple, low-turnover, and tax-light.
- Transparent; no model to break.
- Pairs naturally with a cash leg for crypto drawdown avoidance.

## Disadvantages

- 100% concentration in one asset.
- Quarterly rebalance reacts slowly to crypto-speed crashes.
- No published evidence from the source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` — 90-day return for the crypto leg

**Historical data:**
- `GET /api/v1/backtesting/klines` — daily archive for quarter-end backtests (the non-crypto leg needs another source)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100"
```

Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Signal** — at each quarter end, compute the 90-day BTC (or ETH) return from daily `/market-data/klines` and compare to the other leg
- **Regime gate** — optionally consult `GET /api/v1/regimes/current` before switching into the crypto leg; a bear regime reading argues for waiting on the defensive side
- **Backtest** — `/backtesting/klines` daily since 2017 gives ~35 quarterly decisions; that is a small sample, so report the confidence interval, not just the mean
- **Tips** — test several lookbacks (60/90/120) and rebalance dates; if results flip sign across them, the edge is noise

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "Paired Switching", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[momentum-rotation]] · [[crypto-beta-rotation]] · [[relative-strength]] · [[time-series-momentum]]
