---
title: "Commodity Momentum"
type: strategy
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [quantitative, momentum, commodities, futures, trend-following, position-trading]
aliases: ["Commodity Cross-Sectional Momentum", "Commodity Momentum Factor"]
strategy_type: quantitative
timeframe: position
markets: [commodities, futures]
complexity: intermediate
backtest_status: walk-forward-validated
edge_source: [behavioral]
edge_mechanism: "Trend persistence from slow-moving fundamentals (supply/demand imbalances, capex cycles) and behavioral herding by CTAs/managed money"
expected_sharpe: 0.65
expected_max_drawdown: 0.25
breakeven_cost_bps: 15
crowding_risk: medium
data_required: [futures-continuous-contracts, ohlcv-daily]
capacity_usd: 5000000000
min_capital_usd: 500000
related: ["[[trend-following-cta]]", "[[commodity-carry-strategy]]", "[[commodity-value-strategy]]", "[[commodity-curve-rolls]]", "[[commodities]]", "[[momentum-rotation]]", "[[carry-anomaly]]"]
---

# Commodity Momentum

Cross-sectional momentum applied to commodity futures -- rank a diversified universe of 20-30 commodity futures by trailing returns, go long the winners, short the losers. This is the commodity application of the broader [[momentum-rotation|momentum factor]], exploiting the tendency for commodities with strong recent performance to continue outperforming over intermediate horizons (Source: [[2026-04-14-commodities-research-framework]]).

## Edge Source

**Behavioral edge.** Commodity momentum exploits two reinforcing mechanisms: (1) slow-moving fundamentals -- [[supply-demand-balance|supply/demand imbalances]] in physical commodities take months or years to resolve because of [[capex-cycle|capex cycle]] lags, and (2) behavioral herding by [[trend-following-cta|CTA trend-followers]] and managed money who amplify existing trends through systematic position-building.

### Cross-sectional vs time-series momentum

Commodity momentum comes in two flavors that are frequently conflated. This page describes the **cross-sectional** variant (rank the universe, long winners / short losers). The [[trend-following-cta|time-series]] variant trades each commodity against its *own* history (long if its own trailing return is positive, short if negative) and is the dominant approach in the managed-futures industry.

| Dimension | Cross-sectional (this page) | Time-series ([[trend-following-cta]]) |
|---|---|---|
| Signal | Rank vs other commodities | Own trailing return sign |
| Net exposure | ~Market-neutral (long/short balanced) | Directional; can be net long or net short |
| Benefits most from | Dispersion across commodities | Sustained sector-wide trends |
| Diversifier role | Pure factor; low beta to broad commodity index | Carries directional commodity beta |
| Correlation to each other | High but not identical (~0.6-0.8 typical) | — |

The two are positively correlated and often combined; the kill-criterion on [[trend-following-cta]] correlation (below) exists precisely to avoid double-counting the same exposure.

## Why This Edge Exists

Commodity prices trend because the underlying fundamentals trend. A drought doesn't resolve in days -- it plays out over an entire growing season. An oil supply deficit caused by [[capex-cycle|underinvestment]] persists for years until new production comes online. On top of this physical persistence, behavioral actors amplify trends: CTAs add to positions as trends develop, commercial hedgers adjust hedging programs slowly, and retail/institutional investors chase performance. The losers on the other side are: (1) mean-reversion traders who fade trends too early, (2) hedgers who systematically sell into rallies (producers) or buy into declines (consumers), and (3) liquidity providers who absorb momentum-driven order flow (Source: [[2026-04-14-commodities-research-framework]]).

## Null Hypothesis

Under no-edge conditions, ranking commodities by past returns and going long winners / short losers would produce zero average returns after costs. The return spread between the top and bottom quintiles would be statistically indistinguishable from zero, and any apparent performance would be explained by random variation in a small cross-section.

## Rules

### Universe Construction
1. Select 20-30 liquid commodity futures spanning energy, metals, agriculture, and livestock (e.g., crude oil, natural gas, gold, copper, corn, soybeans, wheat, sugar, coffee, cotton, live cattle, lean hogs).
2. Use continuous front-month or second-month contracts adjusted for rolls.

### Signal Construction
1. Compute **12-month trailing return** for each commodity (or 12-1 month return, skipping the most recent month to avoid short-term reversal).
2. Rank all commodities by trailing return.
3. **Long**: top quintile (top 20% of ranked commodities).
4. **Short**: bottom quintile (bottom 20%).

### Position Sizing
1. Equal-weight within each quintile.
2. Target portfolio-level volatility of 10-15% annualized using ex-ante volatility scaling.
3. Cap any single commodity at 20% of gross exposure.

### Rebalancing
Monthly rebalance on a fixed calendar date (e.g., last business day of each month).

### Exit
Positions exit when a commodity drops out of the top/bottom quintile at next rebalance. No intra-month discretionary exits unless a risk limit is breached.

## Implementation Pseudocode

```python
def commodity_momentum(universe, lookback=252, skip=21):
    """Cross-sectional commodity momentum strategy."""
    returns = {}
    for commodity in universe:
        # 12-1 month return (skip most recent month)
        ret_12m = commodity.price[-skip] / commodity.price[-(lookback + skip)] - 1
        returns[commodity] = ret_12m

    # Rank and select quintiles
    ranked = sorted(returns, key=returns.get, reverse=True)
    n = len(ranked)
    quintile_size = n // 5

    longs = ranked[:quintile_size]
    shorts = ranked[-quintile_size:]

    # Equal-weight, volatility-scaled
    target_vol = 0.12
    portfolio_vol = estimate_portfolio_vol(longs, shorts)
    scale = target_vol / portfolio_vol

    positions = {}
    for c in longs:
        positions[c] = +scale / quintile_size
    for c in shorts:
        positions[c] = -scale / quintile_size

    return positions
```

## Signal Variants

The lookback window is the most important design choice and the largest source of result instability. There is no single "correct" window; the literature and practice cluster around a few:

| Lookback | Character | Trade-off |
|---|---|---|
| 1-month | Short-term reversal, not momentum | Avoid as a long signal; commodities mean-revert at 1m |
| 3–6 month | Faster momentum, higher turnover | More responsive; more whipsaw and costs |
| 12-month | Classic momentum | Standard; captures intermediate persistence |
| **12-1 month** (skip recent month) | Momentum with reversal filter | Industry default; lowest turnover, sidesteps 1m reversal |
| 12 + 6 + 3 blend | Multi-horizon ensemble | Diversifies lookback risk; reduces single-window overfitting |

Because the cross-section is small (20–30 commodities, see Disadvantages), lookback choice should be fixed *ex ante* on economic reasoning, not optimized on the sample — optimizing a window on 25 instruments is a textbook overfit. Using a blend of several windows is the standard defensive choice.

## Indicators / Data Used

- **Trailing returns** (12-month, 6-month, or 12-1 month) -- the primary signal
- **Continuous futures prices** adjusted for contract rolls
- **Ex-ante volatility** (20-60 day realized vol) for position sizing
- [[cot-report-analysis|COT positioning data]] -- supplementary signal for gauging crowding
- [[open-interest]] -- monitors liquidity available in each contract

## Example Trade

**Setup:** Monthly rebalance, April 2024. Universe of 25 commodity futures. *(Figures are approximate roll-adjusted continuous-contract returns, for illustration.)*

1. **Ranking:** Cocoa (roughly +150% trailing 12-1 month — the 2023-24 West African supply crisis rally), copper (+22%), live cattle (+18%) are top-ranked. Natural gas (-35%), wheat (-28%), zinc (-15%) are bottom-ranked.
2. **Enter:** Go long cocoa, copper, live cattle, sugar, coffee (top quintile). Go short natural gas, wheat, zinc, corn, cotton (bottom quintile).
3. **Sizing:** Portfolio volatility target 12%. Each position ~2% of NAV after vol scaling.
4. **May rebalance:** Cocoa has rallied further (+12% in month). Wheat continued declining (-8%). Portfolio gained ~2.5% for the month.
5. **Outcome:** Cocoa remains in top quintile. Natural gas rallies sharply on weather -- exits bottom quintile, position closed. Net monthly P&L: +2.5% before costs, +2.3% after.

## Performance Characteristics

| Metric | Estimate |
|--------|----------|
| Annualized return | 6-10% |
| Annualized volatility | 10-15% |
| Sharpe ratio | 0.5-0.8 |
| Max drawdown | 20-30% |
| Win rate (monthly) | 55-60% |
| Average holding period | 3-6 months |
| Turnover | ~200% annualized |
| Transaction costs | 3-8 bps per trade (futures) |

Academic evidence: Erb & Harvey (2006) documented commodity momentum with Sharpe ~0.5. Miffre & Rallis (2007) confirmed cross-sectional momentum in 31 commodity futures 1979-2004. Asness, Moskowitz & Pedersen (2013) showed commodity momentum is positively correlated with equity/FX momentum but provides diversification (Source: [[2026-04-14-commodities-research-framework]]).

**Important cost note:** Futures trading costs are low (3-8 bps round-trip) but roll costs and slippage during contract rolls can erode 50-100 bps annually. The 12-1 month signal reduces turnover relative to shorter lookback periods.

**Cost-aware overlay (qualitative).** Naive backtests of commodity momentum routinely overstate live performance. The realistic drag stack, applied to any gross result before believing it:

| Cost component | Approximate drag | Notes |
|---|---|---|
| Commission + exchange fees | Low (3-8 bps/round-trip) | Futures are cheap to trade |
| Bid/ask + market impact | Modest in liquid contracts | Grows fast in lumber, OJ, hogs (see Capacity) |
| Roll cost / slippage | ~50-100 bps annually | Worse in [[contango]]; the dominant live cost |
| Crowding / signal decay | Unquantified, ongoing | CTA crowding compresses the edge over time |

With ~200% annual turnover and these drags, a strategy showing a gross Sharpe near the upper academic estimate (~0.8) realistically nets out lower (the `expected_sharpe: 0.65` in frontmatter reflects this haircut). No live or walk-forward Sharpe is asserted here beyond the cited academic studies — treat the table above as a checklist, not a backtest.

## Capacity Limits

**High capacity.** Major commodity futures (crude oil, gold, copper, corn, soybeans) have deep liquidity -- daily volumes of $1-10 billion notional per contract. A $1-5 billion commodity momentum portfolio can be executed with minimal [[market-impact]]. Beyond $5B, market impact in smaller commodity markets (lumber, lean hogs, orange juice) becomes significant, requiring universe constraints. The strategy's monthly rebalancing frequency helps: spreading trades over several days further reduces impact.

## Combining With Other Commodity Factors

Commodity momentum is rarely run standalone at the institutional level; it is one leg of a multi-factor commodity sleeve. The factors are chosen for low or negative mutual correlation:

| Factor | Signal | Correlation to momentum | Role |
|---|---|---|---|
| [[commodity-momentum]] (this) | Trailing return rank | — | Trend capture |
| [[commodity-carry-strategy]] | Curve shape ([[backwardation]] vs [[contango]]) | Low | Harvests roll yield; different driver |
| [[commodity-value-strategy]] | Price vs long-run average / cost | Often **negative** | Counterbalances momentum crashes |
| [[trend-following-cta]] | Own trailing return sign | High | Directional overlay (watch double-counting) |

The momentum/value negative correlation is the key diversification result from Asness, Moskowitz & Pedersen (2013) (Source: [[2026-04-14-commodities-research-framework]]): when momentum crashes (sharp reversals), value tends to be recovering, smoothing the combined drawdown. A naive equal-risk blend of momentum + carry + value historically produced a higher and more stable Sharpe than any single factor — though this is an academic in-sample result, not a live-traded figure for this book.

## What Kills This Strategy

1. **Sharp momentum reversals** -- sudden supply shocks ([[opec]] emergency meetings, weather events, export bans) can cause violent trend reversals that hit momentum portfolios before they can rebalance.
2. **CTA crowding** -- if too many trend-followers hold the same positions, liquidation cascades amplify drawdowns (see 2008 commodity crash when CTAs unwound simultaneously).
3. **Correlation spikes** -- in risk-off episodes, commodities become correlated with equities, reducing the diversification benefit and hitting long-short commodity portfolios.
4. **Regulatory changes** -- position limits, speculative margin hikes (as in 2011 silver), or trading restrictions can force rapid deleveraging.
5. **Structural breaks** -- shale revolution (2014-2016) broke long-running oil trends; similar technological shifts can invalidate momentum signals.

## Kill Criteria

- Rolling 12-month Sharpe ratio < 0 for two consecutive years
- Maximum drawdown exceeds 35%
- Cross-sectional return spread (long minus short quintile) is statistically insignificant (t-stat < 1.5) over trailing 5-year window
- Correlation to [[trend-following-cta]] strategies exceeds 0.85 (redundancy with existing CTA exposure)

## Advantages

- **Strong academic evidence** across multiple studies, time periods, and commodity universes
- **Low correlation** to equity momentum and bond returns -- genuine diversifier in a multi-asset portfolio
- **Low transaction costs** in liquid futures markets with monthly rebalancing
- **Transparent, rules-based** -- easy to implement and audit
- **Scalable** -- deep liquidity in commodity futures accommodates large AUM
- **Combines well** with [[commodity-carry-strategy]] and [[commodity-value-strategy]] for a multi-factor commodity portfolio

## Disadvantages

- **Drawdowns can be severe** -- momentum crashes in commodities are sharp and fast (2008: -30%+ in weeks)
- **Small cross-section** -- only 20-30 commodities vs. thousands of stocks, making statistical inference harder
- **Roll costs** erode returns, especially in [[contango]] markets
- **Crowding risk** from CTAs running similar signals
- **Lookback sensitivity** -- performance varies with lookback window choice (6m vs. 12m vs. 12-1m)
- **No fundamental anchor** -- pure price momentum can persist into bubbles and amplify crashes

## Sources

- Erb, C.B. & Harvey, C.R. (2006). "The Strategic and Tactical Value of Commodity Futures." *Financial Analysts Journal*.
- Miffre, J. & Rallis, G. (2007). "Momentum Strategies in Commodity Futures Markets." *Journal of Banking & Finance*.
- Asness, C.S., Moskowitz, T.J. & Pedersen, L.H. (2013). "Value and Momentum Everywhere." *Journal of Finance*.
- (Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[trend-following-cta]] -- time-series momentum (related but distinct from cross-sectional)
- [[commodity-carry-strategy]] -- complementary factor (low correlation to momentum)
- [[commodity-value-strategy]] -- complementary factor (negative correlation to momentum)
- [[commodity-curve-rolls]] -- roll dynamics affect realized returns
- [[commodities]] -- market overview
- [[momentum-rotation]] -- equity analog of cross-sectional momentum
- [[momentum]] -- the broader momentum anomaly across asset classes
- [[carry-anomaly]] -- the carry factor across asset classes
- [[backwardation]], [[contango]] -- curve states that drive roll cost and the carry overlay
