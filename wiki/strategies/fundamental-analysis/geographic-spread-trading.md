---
title: "Geographic Spread Trading"
type: strategy
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, commodities, futures, arbitrage, pairs-trading]
aliases: ["Location Spread Trading", "Geographic Arbitrage", "Locational Basis Trading"]
strategy_type: fundamental
timeframe: swing
markets: [commodities, futures]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, informational]
edge_mechanism: "Exploits temporary transportation/logistics dislocations between geographically distinct pricing points — arbitrage is constrained by physical shipping time and infrastructure capacity"
expected_sharpe: 0.5
expected_max_drawdown: 0.20
breakeven_cost_bps: 25
crowding_risk: low
data_required: [futures-continuous-contracts, ohlcv-daily, shipping-rates, pipeline-capacity, trade-flow-data]
capacity_usd: 1000000000
min_capital_usd: 1000000
related: ["[[crude-oil]]", "[[copper]]", "[[basis-risk]]", "[[basis-trading]]", "[[commodities]]", "[[cme-group]]", "[[london-metal-exchange]]", "[[intercontinental-exchange]]"]
---

# Geographic Spread Trading

Trading the price differential between the same commodity at different physical locations or exchanges. Classic examples include the WTI-Brent crude oil spread (Cushing, Oklahoma vs. North Sea), the LME-SHFE copper spread (London vs. Shanghai), and the Permian Basin-Cushing crude spread (reflecting pipeline capacity). These geographic spreads mean-revert around transportation cost but can blow out during logistical disruptions, trade policy shifts, or regional supply/demand imbalances (Source: [[2026-04-14-commodities-research-framework]]).

## Edge Source

**Structural and informational edge.** Geographic spreads are constrained by physical realities -- shipping lanes, pipeline capacity, refinery locations, port throughput -- that create friction preventing instant arbitrage. The structural edge comes from the time lag between identifying a spread dislocation and the physical response (chartering a ship takes weeks, building pipeline capacity takes years). The informational edge comes from understanding the specific logistics, regulatory, and trade flow dynamics that drive each spread, which requires domain expertise beyond simple price analysis (Source: [[2026-04-14-commodities-research-framework]]).

### Major tradable geographic spreads

| Spread | Locations | Driven by | Liquidity |
|---|---|---|---|
| WTI–Brent | Cushing, OK vs North Sea | US export capacity, Cushing inventories, [[opec]] cuts | Very high |
| Brent–Dubai | North Sea vs Middle East/Asia | East-of-Suez demand, sour-vs-sweet quality | High |
| Permian (Midland)–Cushing | West Texas vs Cushing | Pipeline takeaway capacity | Medium |
| Bakken–Cushing | North Dakota vs Cushing | Rail vs pipeline; Dakota Access (2017) reshaped it | Medium |
| LME–SHFE copper | London vs Shanghai | Import arb, China demand, FX, trading-hours gap | Medium (constrained) |
| RBOB–Brent (crack-adjacent) | US Gulf vs Europe | Refinery runs, hurricane season | High |
| CBOT–Matif wheat | Chicago vs Paris | Export competitiveness, harvest timing | Lower |

The oil spreads anchor the strategy because their fair value (transportation + quality differential) is well-defined and the legs are deeply liquid. Cross-exchange metal and ag spreads offer wider dislocations but pay for it in execution friction (see Capacity Limits and Disadvantages).

### Fair-value decomposition

A geographic spread is not noise around zero; it has a structural anchor. Decompose it before deciding a level is "cheap" or "rich":

| Component | Source | Stability |
|---|---|---|
| Transportation cost | Tanker freight ([[baltic-exchange|Baltic]]/Clarksons), pipeline tariffs (FERC) | Slow-moving; the spread's gravitational center |
| Quality differential | API gravity, sulfur, grade specs | Stable unless contract specs change |
| Seasonal adjustment | Hurricane season, heating demand, harvest | Predictable, repeating |
| Transient dislocation | Maintenance, vessel scheduling, weather, inventory shocks | **The tradable component** — mean-reverts |
| Structural shift | New pipeline, export terminal, sanctions | **Not tradable as mean-reversion** — resets fair value |

The entire edge lives in distinguishing the fourth row (mean-reverting, tradable) from the fifth (a permanent re-rating that kills the trade). That discrimination is the informational edge and cannot be done on price percentiles alone.

## Why This Edge Exists

A barrel of crude oil in Cushing, Oklahoma is not the same asset as a barrel in Rotterdam. The price difference (the "locational basis") reflects: transportation cost (pipeline tariff, tanker freight), quality differentials (API gravity, sulfur content), regional supply/demand balance, and trade policy (export bans, tariffs, sanctions). When these spreads deviate from fair value (defined by transportation cost plus quality adjustment), physical arbitrageurs step in -- but they are constrained by capacity limits and time.

The losers on the other side include: (1) entities forced to trade at a specific location due to logistical constraints (a Midland, Texas refiner cannot choose to buy crude in Rotterdam), (2) passive participants who do not monitor spread dynamics, and (3) hedgers who roll positions at a single exchange without considering cross-exchange value. The edge exists because the arbitrage is **imperfect** -- limited by vessel availability, pipeline schedules, storage capacity, and regulatory barriers (Source: [[2026-04-14-commodities-research-framework]]).

## Null Hypothesis

Under no-edge conditions, geographic price differentials would always exactly equal transportation cost plus quality adjustment plus a random noise term. No systematic profit would be available from trading mean-reversion in the spread, because deviations would be instantly arbitraged by physical traders and the deviations observed in historical data would be purely random.

## Rules

### Spread Selection
1. Identify a commodity traded at two or more distinct pricing points with liquid futures or physical markets.
2. Determine the **fair value** of the spread: transportation cost + quality differential + seasonal adjustment.
3. Compute the spread: Price_A - Price_B.
4. Calculate the spread's historical distribution (mean, standard deviation, percentile range over 1-3 years).

### Entry
1. **Long the spread** (buy Location A, sell Location B) when the spread falls below the 10th percentile of its historical range (Location A is cheap relative to B).
2. **Short the spread** (sell Location A, buy Location B) when the spread rises above the 90th percentile (Location A is expensive relative to B).
3. Confirm with fundamental analysis: Is the dislocation driven by a temporary factor (weather, maintenance, ship scheduling) or a structural shift (new pipeline, trade policy change)?

### Exit
1. **Mean reversion exit**: close when spread returns to the 40th-60th percentile range.
2. **Stop-loss**: close if spread moves to the 2nd/98th percentile (thesis is wrong or structural shift underway).
3. **Time stop**: close after 60 days if no reversion (reassess fundamentals).

### Position Sizing
1. Size based on spread volatility, not outright price volatility. Target 1-2% portfolio risk per spread trade.
2. Margin requirements can be reduced via exchange-recognized spread margins (CME, ICE offer spread margin credits).

## Implementation Pseudocode

```python
def geographic_spread(spread_history, fair_value, current_spread):
    """Geographic spread mean-reversion strategy."""
    # Historical percentile calculation
    percentile = percentile_rank(spread_history[-756:], current_spread)  # 3-year window

    # Entry signals
    if percentile < 10:
        signal = "LONG_SPREAD"   # Location A is cheap
        entry_size = base_size * (10 - percentile) / 10  # scale into extremes
    elif percentile > 90:
        signal = "SHORT_SPREAD"  # Location A is expensive
        entry_size = base_size * (percentile - 90) / 10
    else:
        signal = "NO_TRADE"
        entry_size = 0

    # Exit logic
    if signal == "LONG_SPREAD" and percentile > 50:
        action = "CLOSE"
    elif signal == "SHORT_SPREAD" and percentile < 50:
        action = "CLOSE"

    # Stop-loss
    if percentile < 2 or percentile > 98:
        action = "STOP_LOSS"

    return signal, entry_size, action
```

## Indicators / Data Used

- **Spread price** (difference between two geographic pricing points)
- **Transportation cost** -- tanker freight rates (Baltic Exchange, Clarksons), pipeline tariffs (FERC filings), rail rates
- **Quality differentials** -- API gravity, sulfur content for crude; grade specifications for metals/agriculture
- **Regional inventory data** -- Cushing stocks ([[eia]]), LME warehouse stocks, SHFE warehouse stocks
- **Trade flow data** -- vessel tracking (AIS data), pipeline flow data, customs/import-export data
- **Seasonal patterns** -- hurricane season (Gulf Coast crude/product spreads), winter heating demand (product spreads)
- **Policy/regulatory changes** -- export bans, sanctions, tariff changes

## Example Trade

**WTI-Brent Spread, February 2024** *(illustrative trade using approximate early-2024 levels)*.

1. **Setup:** WTI-Brent spread at -$6/bbl (WTI trading $6 below Brent). Historical 3-year average: -$4/bbl. This is at the 15th percentile.
2. **Fundamental check:** US crude exports are running at record levels due to high European demand post-Russia sanctions. Cushing inventories are building slightly (bearish for WTI). Brent supported by OPEC cuts. But the spread is wider than transportation cost alone justifies.
3. **Wait for catalyst:** Cushing inventory draw reported in EIA weekly data. WTI-Brent narrows to -$5.50 temporarily, then widens again to -$6.50 (8th percentile).
4. **Enter:** Long WTI, short Brent. Position size: 100 contracts each side. Spread margin: ~$2,000/contract (vs. ~$8,000 for outright crude).
5. **March-April:** US refinery maintenance season ends, runs increase, drawing down Cushing stocks. WTI rallies relative to Brent. Spread narrows to -$3.50 (55th percentile).
6. **Exit:** Close both legs. Profit: $3.00/bbl x 1,000 barrels/contract x 100 contracts = **$300,000**. Holding period: 6 weeks.

## Performance Characteristics

| Metric | Estimate |
|--------|----------|
| Annualized return | 5-10% (varies widely by spread) |
| Annualized volatility | 8-15% |
| Sharpe ratio | 0.4-0.7 |
| Max drawdown | 15-25% |
| Win rate | 55-65% |
| Average holding period | 2-8 weeks |
| Transaction costs | 5-15 bps per leg (spread margin offsets reduce capital cost) |

Performance is highly dependent on which spreads are traded and the trader's domain expertise. The WTI-Brent spread has been one of the most actively traded geographic spreads globally, with daily volume in the hundreds of thousands of contracts. Less liquid spreads (LME-SHFE copper, regional gas hubs) offer wider dislocations but higher execution costs.

**Important:** Backtesting geographic spreads is difficult because historical spread data often does not capture intraday execution dynamics, settlement price vs. trade price differences, and the cost of legging into spread positions. The estimates in the table above are illustrative ranges that vary widely by spread and trader skill — they are **not** a backtested track record for this book.

**Cost-aware overlay (qualitative).** The realized edge survives only after the following frictions, which are heavier than in single-instrument futures momentum:

| Cost component | Relative size | Notes |
|---|---|---|
| Commission (two legs) | Moderate | Pay both legs each side; spread-margin credits help capital, not commission |
| Bid/ask on each leg | Moderate-high | Two markets to cross; worse on illiquid spreads (LME-SHFE, ag) |
| Legging risk | Episodic, large | One leg fills, the other moves — can erase the dislocation captured |
| FX + funding (cross-exchange) | Material on LME-SHFE | Currency conversion and margin drag across clearers |
| Data ($) | Fixed overhead | AIS vessel tracking, pipeline flow, physical intelligence are expensive |

The `breakeven_cost_bps: 25` and `expected_sharpe: 0.5` in frontmatter already embed a conservative haircut for these. The page asserts no live Sharpe beyond the `naive-backtested` status flag.

## Capacity Limits

**Moderate capacity.** The major oil spreads (WTI-Brent, Brent-Dubai, RBOB-Brent) have enormous liquidity -- $500M+ can be deployed. Cross-exchange metal spreads (LME-SHFE) are more constrained by differing trading hours, currency conversion, and regulatory limits on foreign participation. Agricultural geographic spreads (CBOT wheat vs. Matif wheat) have lower liquidity. Overall, a diversified geographic spread portfolio can accommodate $500M-$1B. Beyond this, the strategy faces diminishing opportunities and increased [[market-impact]] in less liquid spreads.

## What Kills This Strategy

1. **Structural infrastructure changes** -- new pipeline capacity (e.g., Dakota Access Pipeline in 2017 permanently narrowed the Bakken-Cushing spread), new export terminals, or trade route changes can permanently shift spread fair value.
2. **Trade policy shocks** -- sanctions, export bans, or tariff changes can cause spreads to gap to new levels with no mean-reversion (e.g., Russia-Europe gas spread post-2022 invasion).
3. **Exchange rule changes** -- delivery point modifications, contract specification changes, or position limit differences can alter spread dynamics.
4. **Correlation breakdown** -- if the two locations decouple fundamentally (e.g., due to sanctions fragmenting global commodity markets), the spread may not mean-revert.
5. **Execution risk** -- legging into cross-exchange spreads carries risk if one leg fills and the other does not.

## Kill Criteria

- Spread fair value (transportation cost) has shifted structurally and historical percentile ranges are no longer valid
- Consecutive 3 losing trades on the same spread despite correct fundamental analysis
- Cross-exchange execution costs (slippage, currency conversion, margin drag) erode more than 50% of theoretical P&L
- Regulatory changes prevent position-taking on one leg of the spread

## Advantages

- **Well-defined fair value** -- transportation cost provides a concrete anchor for spread valuation
- **Reduced directional risk** -- spread trading is hedged against broad commodity moves (long and short the same commodity)
- **Lower margin** -- exchanges offer spread margin credits, improving capital efficiency
- **Domain expertise creates edge** -- understanding physical flows, logistics, and infrastructure provides informational advantage
- **Actionable fundamental signals** -- inventory reports, vessel tracking, pipeline flow data provide clear catalysts
- **Relatively uncrowded** -- requires specialized knowledge, limiting competition from systematic traders

## Disadvantages

- **Requires deep domain expertise** -- understanding physical commodity flows, shipping, infrastructure, and regional market dynamics
- **Execution complexity** -- cross-exchange spreads require managing different clearing houses, currencies, and trading hours
- **Data costs** -- vessel tracking (AIS), pipeline flow data, and physical market intelligence are expensive
- **Structural break risk** -- infrastructure changes can permanently alter spread dynamics
- **Limited universe** -- only a handful of liquid geographic spreads are tradable at scale
- **Not purely systematic** -- significant discretionary judgment required for fundamental analysis

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[crude-oil]] -- the most actively traded geographic spread commodity
- [[copper]] -- LME-SHFE spread is a major cross-exchange trade
- [[basis-risk]] -- theoretical framework for location price differentials
- [[basis-trading]] -- related strategy focused on cash-futures basis
- [[commodities]] -- market overview
- [[cme-group]] -- primary exchange for WTI crude and US commodity futures
- [[london-metal-exchange]] -- primary exchange for base metals
- [[intercontinental-exchange]] -- primary exchange for Brent crude
- [[opec]] -- supply decisions that shift oil-spread fair value
- [[eia]] -- weekly inventory data (Cushing stocks) used as a catalyst
- [[baltic-exchange]] -- tanker freight rates that anchor transportation cost
- [[commodity-momentum]] -- complementary commodity strategy with a different (behavioral) edge
