---
title: "Commodity Value Strategy"
type: strategy
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [quantitative, commodities, futures, mean-reversion, fundamental-analysis, position-trading]
aliases: ["Commodity Value", "Commodity Value Factor", "Commodity Mean-Reversion"]
strategy_type: quantitative
timeframe: position
markets: [commodities, futures]
complexity: advanced
backtest_status: naive-backtested
edge_source: [behavioral]
edge_mechanism: "Mean-reversion exploits overreaction to recent supply/demand shocks — commodities that have fallen the most relative to long-run fundamentals tend to revert as supply/demand rebalances"
expected_sharpe: 0.4
expected_max_drawdown: 0.30
breakeven_cost_bps: 15
crowding_risk: low
data_required: [futures-continuous-contracts, ohlcv-daily, fundamentals-commodity]
capacity_usd: 3000000000
min_capital_usd: 500000
related: ["[[commodity-momentum]]", "[[commodity-carry-strategy]]", "[[supply-demand-balance]]", "[[capex-cycle]]", "[[commodity-super-cycle]]", "[[commodities]]"]
---

# Commodity Value Strategy

Mean-reversion in commodity prices relative to long-run fundamentals -- buy commodities that have fallen the most over 3-5 years (or are cheapest relative to marginal production cost), short those that have risen the most. This is the commodity analog of the equity value factor, exploiting behavioral overreaction to recent supply/demand shocks and the physical anchoring of commodity prices to production cost (Source: [[2026-04-14-commodities-research-framework]]).

Commodity value is the slow, contrarian member of the commodity factor triad alongside [[commodity-momentum]] (fast trend) and [[commodity-carry-strategy]] (curve-shape risk premium). Its defining feature is a strong negative correlation with momentum: where momentum rides recent trends, value bets on their exhaustion. It is rarely run alone — its standalone Sharpe is the weakest of the three — but it materially improves a multi-factor commodity book by diversifying the timing of when each leg pays off. It sits within the broader [[mean-reversion]] family and shares its DNA with equity contrarian-investing.

### At a Glance

| Dimension | This strategy |
|---|---|
| Factor family | Cross-sectional commodity value (long-term reversal) |
| Edge type | Behavioral (overreaction) + physical (production-cost anchor) |
| Signal | Negative of 3-5yr return, or price / 5yr-average ratio |
| Holding period | 6-18 months (slowest of the three factors) |
| Turnover | ~80%/yr (lowest of the three factors) |
| Correlation to [[commodity-momentum]] | ~ -0.5 (the headline diversification benefit) |
| Best paired with | [[commodity-momentum]] + [[commodity-carry-strategy]] |
| Standalone verdict | Marginal alone; valuable as a portfolio component |

## Edge Source

**Behavioral edge.** Commodity value exploits the tendency of market participants to extrapolate recent price moves too far into the future. When a commodity crashes, producers cut [[capex-cycle|capex]], but the market overshoots to the downside because participants anchor on recent bearish conditions. Conversely, when prices surge, the market overshoots to the upside despite the inevitable supply response. The reversion is anchored by a physical reality that equities lack: commodities are ultimately tethered to marginal production cost.

## Why This Edge Exists

Commodities have a fundamental anchor that most financial assets do not -- the marginal cost of production. When copper prices fall far below the all-in sustaining cost of the marginal mine, mines shut down, supply contracts, and prices eventually recover. When prices surge far above production cost, investment floods in, new supply comes online (after a lag of 3-10 years), and prices eventually fall. The losers on the other side are: (1) momentum traders who ride trends past fundamental value, (2) hedgers who lock in extreme prices (producers sell at the bottom, consumers buy at the top), and (3) speculators who extrapolate recent conditions linearly without accounting for the [[capex-cycle|supply response]] (Source: [[2026-04-14-commodities-research-framework]]).

The academic basis comes from Asness, Moskowitz & Pedersen (2013) "Value and Momentum Everywhere," which documented a value factor in commodities (measured as 5-year reversal) that is significant and negatively correlated with momentum -- making the combination particularly attractive.

### Why value and momentum are physical opposites in commodities

| Phase of the [[capex-cycle]] | What value sees | What [[commodity-momentum]] sees | Who wins |
|---|---|---|---|
| Price collapse, capex being cut | "Cheap" -- high value signal, starts buying | Still short the downtrend | Momentum (early), value too early |
| Bottoming, supply finally contracts | Holding long, supply response building | Trend flat/whipsawing | Value begins to pay |
| Recovery, prices rising | Trimming as signal mean-reverts | Long the new uptrend | Both, then momentum dominates |
| Blow-off / [[commodity-super-cycle]] top | "Expensive" -- short the winners | Long the parabola | Momentum (until the top) |

The two factors are out of phase by construction: value is early and contrarian, momentum is late and trend-confirming. This phase offset is the mechanical reason the realized correlation runs around -0.5 and why the combination has a meaningfully higher Sharpe than either leg.

## Null Hypothesis

Under no-edge conditions, commodities that have fallen the most over 3-5 years would have no systematic tendency to outperform those that have risen the most. Past long-term price changes would contain no information about future returns, and any apparent mean-reversion would be explained by time-varying risk or data mining across a small universe.

## Rules

### Signal Construction
1. For each commodity, compute the **5-year cumulative return** (or 3-year, depending on variant).
2. **Value signal** = negative of 5-year return. Commodities with the largest price declines over 5 years have the highest value signal (they are "cheapest").
3. **Alternative signal**: ratio of current price to trailing 5-year average price. Low ratio = high value.
4. Rank all commodities by value signal.

### Entry
1. **Long**: top quintile (commodities with largest 5-year declines -- "cheapest").
2. **Short**: bottom quintile (commodities with largest 5-year increases -- "most expensive").
3. Equal-weight within each quintile.

### Position Sizing
1. Target portfolio-level volatility of 10-12% annualized.
2. Use ex-ante volatility scaling for individual positions.
3. Cap single commodity exposure at 20% of gross.

### Rebalancing
Monthly rebalance. The 5-year lookback ensures signals change slowly, resulting in low turnover.

### Exit
Positions exit when a commodity leaves the top/bottom quintile. Given the slow-moving signal, holding periods are typically 6-18 months.

## Implementation Pseudocode

```python
def commodity_value(universe, lookback_years=5):
    """Cross-sectional commodity value strategy."""
    value_signals = {}
    lookback_days = lookback_years * 252

    for commodity in universe:
        # 5-year return (negative = high value)
        if len(commodity.prices) >= lookback_days:
            ret_5y = commodity.price[-1] / commodity.price[-lookback_days] - 1
            value_signals[commodity] = -ret_5y  # negate so biggest losers rank highest
        else:
            continue

    # Rank by value signal
    ranked = sorted(value_signals, key=value_signals.get, reverse=True)
    n = len(ranked)
    q = n // 5

    longs = ranked[:q]       # biggest 5-year losers (cheapest)
    shorts = ranked[-q:]     # biggest 5-year winners (most expensive)

    # Volatility-scale
    target_vol = 0.10
    portfolio_vol = estimate_portfolio_vol(longs, shorts)
    scale = target_vol / portfolio_vol

    positions = {}
    for c in longs:
        positions[c] = +scale / q
    for c in shorts:
        positions[c] = -scale / q

    return positions
```

### How to Define "Value" in Commodities

There is no book-to-market for crude oil, so practitioners use proxies. Each has a different trade-off between economic cleanliness and data availability:

| Value definition | Construction | Strength | Weakness |
|---|---|---|---|
| 5yr reversal (primary) | Negative of 5-year cumulative return | Cleanest data, used in AMP 2013 | Pure price-based, no fundamental anchor |
| Price / 5yr average | Current spot vs trailing 5yr mean | Intuitive, robust to single year | Same anchoring critique |
| Price / marginal cost | Spot vs all-in sustaining cost of marginal producer | Most economically grounded | Cost data proprietary (Wood Mackenzie, IEA), hard to systematize |
| Stocks-to-use ratio | Inventory relative to consumption (ags, energy) | Direct supply/demand signal | Only available for storable commodities; reporting lags |
| Real (inflation-adjusted) price | Nominal price deflated by CPI | Controls for monetary debasement | Sensitive to deflator choice |

Most quant implementations blend the price-based metrics (which are systematizable) and use the fundamental ones (production cost, [[supply-demand-balance]]) as validation overlays rather than hard signals.

## Indicators / Data Used

- **5-year trailing return** (primary signal)
- **Price-to-5-year-average ratio** (alternative signal)
- **Marginal cost of production** estimates (from mining company reports, IEA, Wood Mackenzie) -- used for fundamental validation but difficult to systematize
- **[[supply-demand-balance]]** data -- USDA WASDE, EIA, IEA reports confirm whether supply response is underway
- **[[capex-cycle]]** data -- mining/E&P spending trends confirm whether investment cycle has turned
- **Ex-ante volatility** for position sizing
- **Roll-adjusted continuous-contract series** -- value must be measured on the same return series actually tradeable, including [[contango]] / [[roll-yield]] drag, not on spot prices (see worked example caveat)

## Example Trade

**Setup:** Monthly rebalance, January 2024. Universe of 25 commodity futures. *(Figures are approximate roll-adjusted continuous-contract returns — they include [[contango]] roll drag, so they can be far more negative than spot price changes.)*

1. **5-year return ranking:** Natural gas has fallen ~70% over 5 years on a roll-adjusted basis (persistent contango drag plus the post-2022 price collapse — high value signal). Wheat has fallen ~40% (chronic roll drag plus the retracement of the 2022 spike). Zinc has fallen ~30%. Meanwhile, cocoa has risen ~85%, gold has risen ~60%, copper has risen ~40%.
2. **Enter:** Long natural gas, wheat, zinc, cotton, sugar (top value quintile). Short cocoa, gold, copper, crude oil, coffee (bottom value quintile).
3. **Sizing:** Target 10% portfolio vol. Natural gas position is small (extremely high individual vol despite high value signal).
4. **Over next 6 months:** Natural gas mean-reverts partially (+15%) as production cuts take effect. Cocoa continues rallying (+30%) -- the short hurts. Wheat stabilizes. Net portfolio return: -1% for the period.
5. **12-month outcome:** Value positions eventually pay off as supply responses materialize. Natural gas +25%, wheat +10%. Cocoa finally corrects -20%. Full-year return: +5% after a rocky path.

**Key lesson:** Commodity value has long horizons and requires patience. It frequently underperforms momentum in the short term but provides diversification and improves multi-factor portfolios.

## Performance Characteristics

| Metric | Estimate |
|--------|----------|
| Annualized return | 3-6% |
| Annualized volatility | 10-14% |
| Sharpe ratio | 0.3-0.5 |
| Max drawdown | 25-35% |
| Win rate (monthly) | 50-55% |
| Average holding period | 6-18 months |
| Turnover | ~80% annualized |
| Transaction costs | 3-8 bps per trade (futures) |

As a standalone strategy, commodity value has the weakest Sharpe among the three commodity factors (momentum, carry, value). Its primary virtue is **diversification**: the correlation between commodity value and commodity momentum is approximately -0.5, meaning a value+momentum combination has significantly higher Sharpe (~0.8-1.0) than either factor alone (Source: [[2026-04-14-commodities-research-framework]]).

**Caveat:** Defining "value" in commodities is harder than in equities. There is no book-to-market ratio for crude oil. The 5-year reversal signal is a proxy that works empirically but lacks the clean economic logic of equity value metrics. Some researchers use production cost ratios or stocks-to-use ratios instead.

### Cost-Aware Reality Check

The figures above are illustrative estimates, not a backtest of this exact implementation. The economic logic of the cost overlay matters more than any point estimate:

| Cost component | Magnitude (liquid futures) | Why value tolerates it |
|---|---|---|
| Commission | ~$1-3 / contract | Trivial relative to position size |
| Bid-ask / slippage | 1-5 bps per trade | Low turnover (~80%/yr) means few trades |
| Roll cost | Embedded in the signal itself | Captured in roll-adjusted returns, not an add-on |
| Total drag | well under the 15 bps `breakeven_cost_bps` | Slow signal is the key cost advantage |

Because turnover is the lowest of the three commodity factors, value is the most cost-robust of the three on a per-unit-of-gross-edge basis -- its problem is that the gross edge itself is thin, not that costs eat it. Contrast with [[statistical-arbitrage]], where high turnover makes cost the binding constraint.

### Combining with Momentum and Carry

The strategy's reason to exist is the multi-factor combination. A schematic of how the three commodity factors complement each other:

| Factor | Edge type | Turnover | Standalone Sharpe (illustrative) | Pairwise correlation |
|---|---|---|---|---|
| [[commodity-momentum]] | Behavioral (trend) | High (~250%) | Highest of the three | -0.5 vs value, ~0 vs carry |
| [[commodity-carry-strategy]] | Risk-bearing / structural | Medium (~150%) | Middle | ~0 vs momentum |
| Commodity value (this page) | Behavioral (reversal) | Low (~80%) | Lowest | -0.5 vs momentum |

Because value is strongly negatively correlated with momentum and roughly uncorrelated with carry, an equal-risk blend of all three has materially higher Sharpe than any single factor (the framework source cites combined Sharpe ~0.8-1.0 vs value's ~0.3-0.5 alone). Value's role is to cushion the momentum drawdowns that occur at trend reversals.

## Capacity Limits

**Moderate to high capacity.** Similar to other commodity factor strategies: $1-3 billion can be deployed in liquid futures with minimal market impact. Lower capacity than momentum or carry because the value signal concentrates positions in commodities that have fallen significantly -- these markets may have reduced liquidity (fewer participants, lower open interest in distressed commodities). Capacity improves when combined with momentum and carry in a multi-factor framework.

## What Kills This Strategy

1. **Structural breaks in production cost** -- if a technological innovation permanently lowers production cost (e.g., shale revolution for natural gas), the "cheap" commodity may never mean-revert to its old price level. The value signal misidentifies a structural shift as a temporary dislocation.
2. **Extended momentum regimes** -- during [[commodity-super-cycle|commodity super cycles]], momentum can dominate for years, causing persistent losses for the short side of the value portfolio.
3. **Supply destruction** -- if enough producers go bankrupt during a price decline, supply may not recover even when prices are "cheap," leading to extended periods at distressed levels.
4. **Data limitations** -- accurate production cost data is proprietary and expensive, forcing reliance on cruder price-based proxies.
5. **Small cross-section** -- with only 20-30 commodities, a few positions can dominate portfolio returns.

| Failure mode | Mechanism | Early warning | Defense |
|---|---|---|---|
| Structural cost break | Technology permanently lowers production cost (shale gas) | Cheap commodity never reverts over 3+ years | Overlay production-cost trend; cap conviction |
| Extended momentum regime | [[commodity-super-cycle]] runs for years | Short side bleeds, value-momentum corr turns positive | Run value only inside a multi-factor blend |
| Supply destruction | Producers go bankrupt; supply does not recover at "cheap" prices | Inventories stay high despite low price | Confirm with [[supply-demand-balance]] data |
| Data limitation | Reliance on price proxies vs true cost | Signal disagrees with stocks-to-use | Triangulate multiple value definitions |
| Concentration | Few extreme positions dominate | Single commodity > 20% of gross | Cap single-name exposure (per Rules) |

## Kill Criteria

- Rolling 24-month Sharpe ratio < -0.3 (value factor delivering significantly negative returns)
- Maximum drawdown exceeds 40%
- The value-momentum correlation turns positive (losing the diversification benefit that justifies running value as a standalone signal)
- 5-year reversal signal shows zero predictive power (information coefficient < 0.01) over trailing 10-year window

## Advantages

- **Negative correlation to momentum** -- the primary reason to run this strategy; combined value+momentum has Sharpe ~0.8-1.0
- **Grounded in physical economics** -- production cost provides a fundamental anchor absent in most financial factor strategies
- **Very low turnover** -- the 5-year signal changes slowly, minimizing transaction costs
- **Benefits from patience** -- rewards investors with long horizons willing to hold through periods of underperformance
- **Contrarian positioning** -- buys commodities when others are selling, avoiding crowded trades
- **Academic support** across multiple studies (Asness, Moskowitz & Pedersen 2013)

## Disadvantages

- **Weak standalone performance** -- Sharpe of 0.3-0.5 is marginal; difficult to justify without momentum/carry diversification
- **Ambiguous value definition** -- no consensus on how to measure "value" in commodities
- **Long holding periods** -- capital is tied up for 6-18+ months with uncertain outcomes
- **Can be wrong for years** -- mean-reversion can take much longer than expected (natural gas was "cheap" from 2019-2024)
- **Structural break vulnerability** -- technology and policy changes can permanently shift price levels
- **Requires conviction** -- psychologically difficult to buy commodities in freefall

## Sources

- Asness, C.S., Moskowitz, T.J. & Pedersen, L.H. (2013). "Value and Momentum Everywhere." *Journal of Finance.*
- Erb, C.B. & Harvey, C.R. (2006). "The Strategic and Tactical Value of Commodity Futures." *Financial Analysts Journal.*
- (Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[commodity-momentum]] -- complementary factor (negatively correlated with value)
- [[commodity-carry-strategy]] -- the third pillar of commodity factor investing
- [[supply-demand-balance]] -- fundamental driver of mean-reversion
- [[capex-cycle]] -- the investment cycle that creates value opportunities
- [[commodity-super-cycle]] -- long-duration cycles that can overwhelm value signals
- [[commodities]] -- market overview
- [[mean-reversion]] -- the statistical principle underlying the signal
- [[contango]] / [[roll-yield]] -- roll mechanics that distort raw value measurement
- [[edge-taxonomy]] -- behavioral edge classification
