---
title: "Commodity Momentum with Term Structure"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [commodities, futures, momentum, quantitative, funding-rate, perpetual-futures, crypto]
aliases: ["Momentum Effect Combined with Term Structure in Commodities", "Roll-Return Momentum Double Sort", "Carry-Momentum Double Sort"]
strategy_type: quantitative
timeframe: position
markets: [commodities, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Backwardated contracts pay hedgers' insurance premium (roll yield) and recent winners keep winning as speculators under-react; requiring both signals isolates contracts where the carry premium and trend agree, and the short side where both are negative."
data_required: [futures-curve, ohlcv-daily, funding-rates]
min_capital_usd: 50000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 0.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 30
decay_evidence: "The academic double-sort (Fuertes, Miffre and Rallis, 2010) predates the widespread adoption of commodity carry and momentum in CTA and alternative-risk-premia products; QuantConnect's port publishes no statistics."
kill_criteria: |
  - rolling 24-month net Sharpe < 0
  - drawdown > 25% from high-water mark
  - roll-return and momentum ranks become negatively correlated for 12 months (signals fighting each other)
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[commodity-carry-strategy]]", "[[commodity-momentum]]", "[[roll-yield]]", "[[funding-filtered-momentum]]", "[[trend-aware-carry]]", "[[momentum-value-combination]]"]
---

# Commodity Momentum with Term Structure

**Commodity momentum with term structure** is a double sort: first rank commodity futures by roll return (how backwardated their curve is), then, within the most backwardated and most contangoed groups, rank by recent momentum. It buys the backwardated winners and shorts the contangoed losers. [[quantconnect|QuantConnect]]'s Strategy Library implements it on 22 commodity futures from a Quantpedia description (Source: [[quantconnect-strategy-library]]). In crypto, perp funding and dated-futures basis play the role of roll return, which makes the same double sort testable on a perp universe.

## Edge Source

**Risk-bearing** (the carry/roll premium hedgers pay) plus **behavioral** (momentum from under-reaction), per [[edge-taxonomy]]. It combines the single-factor pages [[commodity-carry-strategy]] and [[commodity-momentum]].

## Why This Edge Exists

Backwardation signals scarce inventory and producers paying to hedge ([[backwardation]], [[roll-yield]]); long positions in those contracts earn the roll. Momentum captures slow diffusion of supply-demand news. Each signal alone suffers when the other disagrees — a backwardated contract in a collapsing trend, or a winner in deep [[contango]] where the roll bleeds the position. The double sort holds only the agreement cases. The counterparties are commercial hedgers paying for insurance and index investors rolling mechanically regardless of curve shape.

## Null Hypothesis

If neither roll return nor momentum predicts returns, the High-Winner minus Low-Loser portfolio earns zero before costs and its returns are uncorrelated with the sort variables. Testable: compare against portfolios formed by random double sorts, and against each single-factor portfolio — the combination must add return beyond the better single factor.

## Rules

### Source rules (commodities)
1. Universe: 22 commodity futures.
2. Monthly, compute each contract's annualized roll return: (P_near - P_next) × 365 / days between expiries.
3. Split the universe into tertiles by roll return; drop the middle.
4. Split the top (High) and bottom (Low) tertiles in half by 21-day momentum (mean daily return).
5. **Long** High-roll Winners, **short** Low-roll Losers, equal weight, hold one month.

### Crypto adaptation (not from the source)
- Replace roll return with the negative of annualized perp funding (or annualized dated-futures basis): coins with negative funding are "backwardated" for a long holder, since longs are paid.
- Universe: top 30-50 perps by open interest, point-in-time.
- Momentum: 21- to 30-day return, skipping the last day to avoid short-term reversal.
- Long low-funding winners, short high-funding losers; BTC-beta neutralize; weekly or monthly rebalance.

## Implementation Pseudocode

```python
def monthly_portfolio(universe, date):
    rr  = {c: roll_return(c, date) for c in universe}        # crypto: -annualized funding
    mom = {c: mean_daily_return(c, date, 21) for c in universe}
    ranked = sorted(universe, key=rr.get)
    k = len(ranked) // 3
    low, high = ranked[:k], ranked[-k:]
    def split(group):
        g = sorted(group, key=mom.get)
        h = len(g) // 2
        return g[:h], g[h:]                                   # losers, winners
    _, high_winners = split(high)
    low_losers, _   = split(low)
    w = {c: 0.5 / len(high_winners) for c in high_winners}
    w |= {c: -0.5 / len(low_losers) for c in low_losers}
    return w          # execute next day; subtract fees, roll costs / funding
```

## Indicators / Data Used

- Futures curve (front and next contract) for [[roll-yield]]; crypto: [[funding-rate]] or basis
- 21-day momentum ([[time-series-momentum]], [[commodity-momentum]])
- Volatility for optional risk-parity weighting

## Example Trade

Illustrative (commodities): in a monthly sort, crude oil and copper sit in the backwardated tertile with positive 21-day returns (High-Winners); natural gas and wheat sit in the contango tertile with negative momentum (Low-Losers). Long 25% each in crude and copper, short 25% each in natural gas and wheat. The book earns roll on the longs, positive roll on the shorts (selling contango), and trend on both.

Illustrative (crypto): SOL funding is -8% annualized with a +15% 30-day return (long it and get paid funding); a mid-cap alt has +60% annualized funding and a -20% 30-day return (short it and collect funding). BTC-beta neutralized, rebalanced weekly.

## Performance Characteristics

- **Source claim**: none — the QuantConnect entry is marked pending review with no statistics (Source: [[quantconnect-strategy-library]]). The underlying academic study reported that combining the two signals improved on either alone for 1979-2007 commodity futures (claim as summarized by Quantpedia; not verified here).
- With only 22 contracts, each leg holds ~3-4 names — high idiosyncratic risk.
- **Cost overlay**: monthly rebalance, ~50% turnover, 2-5 bps per side on liquid futures — modest. Crypto perps: 5-10 bps per side plus the funding actually paid on any leg where the sign flips.

## Capacity Limits

Commodity futures: hundreds of millions, limited by the least liquid agricultural contracts. Crypto: limited by short-leg depth in mid-cap perps, typically low tens of millions.

## What Kills This Strategy

- Momentum crashes at trend reversals, when the Low-Losers rally hard ([[failure-modes]]).
- Curve regime changes (e.g., 2020 oil contango) that flip roll signs faster than the monthly sort.
- Crypto: funding signs flip within days; a monthly funding sort can be stale by the second week.
- Small universe → concentration; see [[overfitting]].

## Kill Criteria

Retire per [[when-to-retire-a-strategy]] on the frontmatter conditions.

## Advantages

- Two documented premia combined, with a clear economic story for each.
- Market-neutral construction.
- Natural crypto analog using funding data.

## Disadvantages

- No published statistics from the source port.
- Few names per leg.
- Requires curve data (commodities) or funding history (crypto) in addition to prices.

## Getting the Data (CryptoDataAPI)

**Live data (crypto adaptation):**
- `GET /api/v1/derivatives/funding-rates` — current funding across perps (the roll-return proxy)
- `GET /api/v1/derivatives/open-interest` — to define the liquid universe
- `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=40` — momentum lookback

**Historical data:**
- `GET /api/v1/backtesting/funding` — funding history for the term-structure sort
- `GET /api/v1/backtesting/klines` — price archive for momentum

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates"
```

Commodity futures curves are not served by CryptoDataAPI. Full catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-backtesting]].

### AI agent workflow

On the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Signal** — rank the perp universe by average funding over the last 7 days from `/derivatives/funding-rates`, then split each funding tertile by 30-day momentum from daily klines
- **Regime gate** — pause the long leg when `GET /api/v1/volatility/regime` shows a vol shock; momentum crashes cluster there
- **Backtest** — join `/backtesting/funding` with `/backtesting/klines` on a point-in-time universe from `/backtesting/daily-snapshots/{date}`; average funding over the holding period, not a single print
- **Tips** — compare against [[funding-filtered-momentum]] and [[trend-aware-carry]]; if the double sort adds nothing over them, keep the simpler one

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "Momentum Effect Combined with Term Structure in Commodities", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[commodity-carry-strategy]] · [[commodity-momentum]] · [[roll-yield]] · [[backwardation]] · [[contango]]
- [[funding-filtered-momentum]] · [[trend-aware-carry]] · [[momentum-value-combination]]
