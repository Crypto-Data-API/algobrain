---
title: "WTI-Brent Spread Trading"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [commodities, energy, mean-reversion, pairs-trading, futures, macro]
aliases: ["WTI/Brent Spread", "Brent-WTI Spread", "Trading with WTI BRENT Spread"]
strategy_type: quantitative
timeframe: swing
markets: [commodities]
complexity: intermediate
backtest_status: untested
edge_source: [structural, behavioral]
edge_mechanism: "WTI and Brent are near-identical light sweet crudes tied together by shipping and refining arbitrage; temporary dislocations from regional flows (Cushing storage, pipeline outages, export rules) revert as physical arbitrageurs move barrels."
data_required: [ohlcv-daily, futures-curve]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.2
breakeven_cost_bps: 10
decay_evidence: "The spread structurally shifted in 2011-2013 (Cushing glut, WTI at a $20+ discount) and again after the 2015 US crude export ban was lifted; mean-reversion models fitted before a regime break lose heavily through it."
kill_criteria: |
  - spread moves > 3 standard deviations from the regression fair value and stays there for 20 trading days (structural break)
  - rolling 12-month net Sharpe < 0
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[crude-oil]]", "[[pairs-trading]]", "[[geographic-spread-trading]]", "[[crack-spread]]", "[[cointegration]]"]
---

# WTI-Brent Spread Trading

**WTI-Brent spread trading** is a mean-reversion trade on the price difference between the two main crude oil benchmarks: West Texas Intermediate (delivered at Cushing, Oklahoma) and Brent (North Sea, seaborne). When the spread strays from a moving average or regression fair value, the trader buys the cheap benchmark and sells the rich one. [[quantconnect|QuantConnect]]'s Strategy Library implements it with WTI and Brent CFDs, following a Quantpedia description (Source: [[quantconnect-strategy-library]]). It is macro context for this wiki: oil shocks feed inflation and rates expectations that move crypto.

## Edge Source

**Structural** (physical arbitrage bounds the spread) and **behavioral** (regional flow overreaction), per [[edge-taxonomy]].

## Why This Edge Exists

WTI and Brent are similar crudes; the spread should reflect transport cost from the US Gulf to Europe plus quality differences. Short-term flows — Cushing inventory builds, pipeline outages, hurricane shut-ins, geopolitical risk in Brent-linked supply — push it away from that anchor. Physical traders, refiners and exporters respond by moving barrels, which pulls the spread back. The trader providing liquidity against the dislocation is paid for bearing the risk that the anchor itself has moved. See [[geographic-spread-trading]] for the general location-spread family.

## Null Hypothesis

If the spread is a random walk, crossings of its 20-day average carry no information and the strategy earns zero minus roll and trading costs. Testable: an ADF or [[cointegration]] test on WTI and Brent over the calibration window should reject a unit root in the spread; if it does not, there is nothing to trade.

## Rules

Source rules (QuantConnect port):

1. Data: daily WTI and Brent prices (the source uses OANDA CFDs).
2. Spread = WTI - Brent. Compute its 20-day simple moving average.
3. Fit a linear regression Brent = β·WTI + α on the last 252 days; refit monthly. Fair value of the spread = (1 - β)·WTI - α.
4. **Long spread** (long WTI 0.5, short Brent 0.5) when the spread is below its 20-day SMA; **short spread** when it is above.
5. **Exit** when the spread crosses the regression fair value.

Practical additions (not in the source): use exchange futures (CME WTI, ICE Brent) matched by delivery month, roll both legs together, and add a structural-break stop.

## Implementation Pseudocode

```python
# wti, brent: daily close series (front-month or continuous-adjusted)
spread = wti - brent
sma20 = spread.rolling(20).mean()

def monthly_fit(t):
    beta, alpha = np.polyfit(wti[t-252:t], brent[t-252:t], 1)
    return beta, alpha

for t in days:
    if t.is_month_start: beta, alpha = monthly_fit(t)
    fair = (1 - beta) * wti[t] - alpha
    if pos == 0:
        pos = +1 if spread[t] < sma20[t] else -1          # long or short the spread
    elif (pos > 0 and spread[t] >= fair) or (pos < 0 and spread[t] <= fair):
        pos = 0
    # cost: both legs' commissions + spread; roll cost on futures
```

## Indicators / Data Used

- Daily WTI and Brent prices; 20-day SMA of the spread
- One-year rolling regression for fair value
- Cushing inventories ([[eia]] weekly report), [[crude-oil]] curve structure ([[futures-curve-structure-analysis]])

## Example Trade

Illustrative: WTI 72.00, Brent 76.50, spread -4.50 against a 20-day average of -3.80 and a regression fair value of -3.60 after a surprise Cushing inventory build. Long WTI / short Brent. Two weeks later the build reverses and the spread is -3.55: exit at fair value for +0.95 per barrel before costs. On one CME/ICE pair (1,000 barrels each) that is about $950 gross, less ~$20 in commissions and fees.

## Performance Characteristics

- **Source claim**: none — the QuantConnect page cites the Quantpedia strategy but publishes no statistics (Source: [[quantconnect-strategy-library]]).
- The source trades CFDs on LEAN's zero-fee CFD default; real CFD financing and spreads are material over multi-week holds.
- Returns are small per trade and depend on the spread staying range-bound.

## Capacity Limits

Crude futures are among the deepest commodity markets; capacity is in the hundreds of millions for a spread trader. CFD implementations are limited by broker financing, not liquidity.

## What Kills This Strategy

- Structural breaks in the anchor: the 2011-2013 Cushing glut and the 2015 end of the US export ban each moved the "fair" spread by many dollars ([[failure-modes]]).
- Contract mismatch: WTI and Brent expire on different schedules; mis-rolled legs create fake signals.
- Geopolitical supply shocks that hit one benchmark only ([[geopolitical-risk-premium]]).

## Kill Criteria

Retire per [[when-to-retire-a-strategy]] if the spread stays more than 3σ from fair value for 20 trading days or rolling 12-month net Sharpe turns negative.

## Advantages

- Strong economic anchor (physical arbitrage).
- Market-neutral to the oil price level.
- Deep, liquid instruments.

## Disadvantages

- No published performance from the source.
- Exposed to regime shifts in logistics and regulation.
- Not tradeable with crypto-native data or venues.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not carry oil futures or CFDs, so this strategy needs an external commodity data source (see [[data-sources-overview]]). The crypto-side use is as a macro input: large oil spread dislocations often coincide with supply shocks that move rates expectations. To study that link, pair external oil data with BTC history from `GET /api/v1/backtesting/klines`.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

### AI agent workflow

With the [[cryptodataapi-mcp|CryptoDataAPI MCP]] for the crypto side:

- **Signal** — compute the WTI-Brent spread from an external feed; CryptoDataAPI supplies no oil prices
- **Regime gate** — when oil shocks hit, check `GET /api/v1/regimes/current` before adding crypto risk; oil-driven inflation scares tend to be risk-off
- **Backtest** — align oil spread z-scores with BTC daily returns from `/backtesting/klines` to measure whether large dislocations lead crypto drawdowns
- **Tips** — treat the spread as a macro stress indicator for crypto sizing, not as a crypto trade

## Variant / External Source: Quantpedia

[[quantpedia|Quantpedia]] #0100 is the origin card for this rule (20-day SMA fade of the WTI/Brent spread; source Evans, Dunis & Laws). It reports 1995-2004 pre-cost figures of 9.9% p.a., 11.3% volatility, Sharpe 0.88 and max drawdown −69%, and flags *slightly negative* out-of-sample performance (Source: [[quantpedia-strategy-encyclopedia]]).

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "Trading with WTI BRENT Spread", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[crude-oil]] · [[brent-crude]] · [[geographic-spread-trading]] · [[crack-spread]] · [[seasonal-spread-trading]]
- [[pairs-trading]] · [[cointegration]]
