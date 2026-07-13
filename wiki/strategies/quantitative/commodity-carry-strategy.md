---
title: "Commodity Carry Strategy"
type: strategy
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [quantitative, commodities, futures, position-trading]
aliases: ["Commodity Carry", "Carry in Commodities", "Roll Yield Strategy"]
strategy_type: quantitative
timeframe: position
markets: [commodities, futures]
complexity: intermediate
backtest_status: walk-forward-validated
edge_source: [risk-bearing, structural]
edge_mechanism: "Harvests the risk premium embedded in backwardated commodity curves — producers systematically sell futures below expected spot to hedge, transferring risk to speculators"
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 15
crowding_risk: medium
data_required: [futures-continuous-contracts, futures-curve-data, ohlcv-daily]
capacity_usd: 5000000000
min_capital_usd: 500000
related: ["[[carry-anomaly]]", "[[commodity-momentum]]", "[[roll-yield]]", "[[backwardation]]", "[[contango]]", "[[hedging-pressure]]", "[[commodity-curve-rolls]]", "[[commodities]]"]
---

# Commodity Carry Strategy

Systematic carry in commodity futures -- go long commodities in [[backwardation]] (positive [[roll-yield]]), short those in [[contango]] (negative roll-yield). This strategy harvests the [[hedging-pressure]] premium that producers pay speculators for bearing commodity price risk. It is the commodity application of the broader [[carry-anomaly]] factor documented across asset classes, and the direct cousin of the FX [[carry-trade]] (Source: [[2026-04-14-commodities-research-framework]]).

Carry is the structural-risk-premium member of the commodity factor triad, sitting alongside [[commodity-momentum]] (behavioral trend) and [[commodity-value-strategy]] (behavioral reversal). Where value and momentum bet on price *direction*, carry harvests a premium embedded in the *shape* of the futures curve regardless of where spot goes. Its signal -- [[roll-yield]] -- is directly observable from the curve with no model estimation, which makes it the most transparent of the three. The trade-off is its risk profile: carry earns small steady premiums most of the time and suffers sharp left-tail losses when curves collapse together (2008, March 2020).

### At a Glance

| Dimension | This strategy |
|---|---|
| Factor family | Cross-sectional commodity carry (curve slope) |
| Edge type | Risk-bearing ([[hedging-pressure]]) + structural (index roll flow) |
| Signal | Annualized [[roll-yield]] (front vs deferred) |
| Holding period | 2-6 months |
| Turnover | ~150%/yr (middle of the three factors) |
| Return skew | Negative -- steady gains, sharp crisis losses |
| Correlation to [[commodity-momentum]] | ~0 (weakly correlated; good blend) |
| Cousin strategies | [[carry-trade]] (FX), bond carry, [[carry-anomaly]] |

## Edge Source

**Risk-bearing and structural edge.** The carry premium exists because commodity producers (miners, drillers, farmers) have a structural need to hedge future production by selling futures. They systematically accept a discount to expected future spot prices in exchange for revenue certainty. Speculators who take the other side of these hedges earn a compensation for bearing commodity price risk. The structural nature of producer hedging makes this premium persistent (Source: [[2026-04-14-commodities-research-framework]]).

## Why This Edge Exists

Keynes (1930) first articulated "normal [[backwardation]]" -- the idea that futures prices are biased below expected future spot prices because hedgers (predominantly producers) pay an implicit insurance premium. The mechanism: a copper miner with production coming in 6 months needs price certainty for budgeting, debt service, and capex planning. They sell futures at a discount to expected spot, transferring price risk to speculators. This discount is the carry premium.

The losers on the other side are the hedgers themselves -- but "losing" the carry premium is rational for them because it buys valuable insurance. They are not trying to maximize speculative returns; they are managing business risk. Some losses also come from passive commodity index investors who mechanically roll long positions from near-month to deferred, paying [[contango]] costs on a massive scale (estimated $5-10 billion annually in roll costs for GSCI/BCOM tracking funds) (Source: [[2026-04-14-commodities-research-framework]]).

### Who pays the carry premium

| Counterparty | Why they accept losing the premium | Persistence |
|---|---|---|
| Producers (miners, drillers, farmers) | Need revenue certainty for budgeting, debt service, [[capex-cycle\|capex]] -- buy insurance via selling futures below expected spot | Structural; persists as long as producers hedge |
| Passive index funds (GSCI/BCOM trackers) | Mechanically roll near-to-deferred each month, paying [[contango]] regardless of price | Persists while index AUM is large |
| Consumers locking in input costs | Pay up for deferred contracts to guarantee supply | Asymmetric; weaker than producer pressure |

The carry trader is the speculator who warehouses the price risk producers shed and harvests the roll-yield differential. This is the same economic structure as the FX [[carry-trade]] (borrow low-yield currency, lend high-yield) and bond carry -- which is precisely why all carry strategies tend to draw down together in risk-off episodes (see Disadvantages).

## Null Hypothesis

Under no-edge conditions, the slope of the commodity futures curve would contain no information about future returns. [[backwardation]] and [[contango]] would simply reflect storage costs and [[convenience-yield]], with no systematic profit opportunity from going long backwardated commodities and short contango commodities after adjusting for costs.

## Rules

### Signal Construction
1. For each commodity in the universe, compute the **annualized roll yield**:
   `Roll Yield = (Front Month Price - Second Month Price) / Second Month Price x (12 / months_between_contracts)`
2. Positive roll yield = [[backwardation]] (front > deferred). Negative = [[contango]] (front < deferred).
3. Rank all commodities by roll yield.

### Entry
1. **Long**: top quintile (most backwardated commodities).
2. **Short**: bottom quintile (most contango commodities).
3. Equal-weight within each quintile.

### Position Sizing
1. Target portfolio-level volatility of 10-15% annualized.
2. Use ex-ante volatility (60-day realized vol) for each commodity to adjust individual position sizes.
3. Cap single commodity exposure at 20% of gross.

### Rebalancing
Monthly rebalance. Recalculate roll yields and re-rank on each rebalance date.

### Exit
Positions exit when a commodity leaves the top/bottom quintile. Emergency exit if portfolio drawdown exceeds 20% intra-month.

## Implementation Pseudocode

```python
def commodity_carry(universe, target_vol=0.12):
    """Cross-sectional commodity carry strategy."""
    roll_yields = {}
    for commodity in universe:
        front = commodity.front_month_price
        second = commodity.second_month_price
        months_gap = commodity.months_between_contracts
        ry = (front - second) / second * (12 / months_gap)
        roll_yields[commodity] = ry

    # Rank by roll yield (most backwardated = highest carry)
    ranked = sorted(roll_yields, key=roll_yields.get, reverse=True)
    n = len(ranked)
    q = n // 5

    longs = ranked[:q]       # most backwardated
    shorts = ranked[-q:]     # most contango

    # Volatility-scale
    portfolio_vol = estimate_portfolio_vol(longs, shorts)
    scale = target_vol / portfolio_vol

    positions = {}
    for c in longs:
        positions[c] = +scale / q
    for c in shorts:
        positions[c] = -scale / q

    return positions
```

### Curve Shape Reference

| Curve state | Front vs deferred | Roll yield sign | Carry signal | Typical cause |
|---|---|---|---|---|
| [[backwardation]] | Front > deferred | Positive | **Long** (top quintile) | Low inventories, strong near-term demand, high [[convenience-yield]] |
| Flat | Front ≈ deferred | ~0 | Neutral / excluded | Balanced supply/demand |
| [[contango]] | Front < deferred | Negative | **Short** (bottom quintile) | Oversupply, high storage, weak spot demand |
| Super-contango | Front << deferred | Strongly negative | Strong short | Storage near capacity (e.g. WTI April 2020) |

The signal is *cross-sectional* (rank commodities against each other) rather than *time-series* (each commodity vs its own history). A commodity can be in mild contango and still be a long if everything else is in deeper contango.

## Indicators / Data Used

- **[[roll-yield]]** (front vs. second month spread, annualized) -- the primary signal
- **Full futures curve** -- deeper curve analysis via [[futures-curve-structure-analysis]]
- **[[convenience-yield]]** -- theoretical underpinning for backwardation
- **[[cot-report-analysis|COT report]]** -- confirms [[hedging-pressure]] direction
- **Inventory data** ([[eia]]-data for energy, LME warehouse stocks for metals, [[usda]] for agriculture) -- inventories drive curve shape
- **Ex-ante volatility** for position sizing
- **Seasonality calendars** -- needed to avoid mistaking predictable seasonal curve patterns (heating gas, harvest grains) for an information-bearing carry signal

## Example Trade

**Setup:** Monthly rebalance, January 2024. Universe of 25 commodity futures.

1. **Roll yield ranking:** Crude oil WTI (roll yield +8% annualized, backwardated -- strong demand, low inventories), copper (+5%), live cattle (+4%) top the ranking. Natural gas (-25% annualized, steep contango -- oversupply, mild winter), corn (-8%), zinc (-6%) at the bottom.
2. **Enter:** Long crude oil, copper, live cattle, sugar, soybean oil (top quintile). Short natural gas, corn, zinc, wheat, aluminum (bottom quintile).
3. **Position sizing:** Target 12% portfolio vol. Crude oil position scaled down (higher individual vol), corn scaled up (lower vol).
4. **February rebalance:** Crude oil stays backwardated, earning +0.7% from roll yield alone plus +3% from price appreciation. Natural gas contango deepens, short position earns +2% from price decline plus +2% from favorable roll. Portfolio return: +2.8% for the month.
5. **Cost overlay:** Futures commission ~$3/contract, slippage ~1-2 bps. Monthly cost impact: ~5 bps. Net return: +2.75%.

## Performance Characteristics

| Metric | Estimate |
|--------|----------|
| Annualized return | 5-9% |
| Annualized volatility | 10-14% |
| Sharpe ratio | 0.5-0.7 |
| Max drawdown | 20-30% |
| Win rate (monthly) | 55-60% |
| Average holding period | 2-6 months |
| Turnover | ~150% annualized |
| Transaction costs | 3-8 bps per trade (futures) |

Academic evidence: Szymanowska et al. (2014) found a significant carry premium in commodities. Koijen et al. (2018) documented carry as a pervasive factor across asset classes. Gorton, Hayashi & Rouwenhorst (2013) showed that commodities in [[backwardation]] (low inventories) earn substantially higher futures returns — roughly a 10-percentage-point annualized spread over [[contango]] commodities — over their 1969-2006 sample (Source: [[2026-04-14-commodities-research-framework]]).

**Critical risk note:** Commodity carry got destroyed in 2008 (commodity crash: correlation spike, backwardation disappeared across the board) and in March 2020 (COVID oil crash: WTI went negative, carry signals were maximally wrong). The strategy has left-tail risk -- it earns steady premiums most of the time but suffers sharp drawdowns during systemic commodity dislocations.

### Cost-Aware Reality Check

These figures are illustrative estimates, not a backtest of this exact implementation. The cost economics:

| Cost component | Magnitude (liquid futures) | Comment |
|---|---|---|
| Commission | ~$1-3 / contract | Negligible vs notional |
| Bid-ask / slippage | 1-2 bps per trade | Tight in energy/metals, wider in softs/livestock |
| Monthly rebalance turnover | ~150%/yr | Higher than value, lower than momentum |
| Total drag | comfortably under the 15 bps `breakeven_cost_bps` | Carry survives costs in liquid contracts |

The binding constraint on carry is *not* cost but **negative skew**: the strategy can absorb its trading costs easily yet still suffer years of P&L erased in a single dislocation week. Sizing must therefore be driven by tail risk, not by the smooth in-sample Sharpe.

### Left-Tail Episodes

| Episode | What happened to the curve | Why carry was wrong |
|---|---|---|
| 2008 commodity crash | Backwardation flattened/inverted across the board | Long backwardated legs all sold off together |
| March 2020 (COVID) | WTI front month went **negative**; storage filled | Carry signal maximally mispriced as physical storage broke |
| Correlated risk-off generally | Cross-commodity correlation spikes toward 1 | Long-short book stops being market-neutral |

## Capacity Limits

**High capacity.** Similar to [[commodity-momentum]] -- deep liquidity in major commodity futures accommodates $1-5 billion. The strategy's monthly rebalancing and relatively low turnover (~150% annualized) further support scalability. Capacity is limited primarily by the number of liquid commodity futures available (30-40 globally) and the depth of smaller markets (softs, livestock). At very large scale ($10B+), the strategy would need to restrict to the most liquid energy and metals contracts.

## What Kills This Strategy

1. **Systemic commodity crashes** -- when all commodities sell off together (2008, 2020), backwardation flattens or inverts, destroying the carry signal and causing simultaneous losses on longs.
2. **Structural shift in hedging behavior** -- if producers stop hedging (e.g., due to financial engineering or price insurance programs), the hedging pressure premium shrinks.
3. **Passive index flow reversal** -- if commodity index AUM declines dramatically, the "roll yield transfer" from passive to active investors diminishes.
4. **Storage economics disruption** -- new storage capacity or technology that eliminates the physical constraints driving [[contango]]/[[backwardation]] dynamics.
5. **Correlation spike** -- during risk-off events, the long-short carry portfolio may not be market-neutral as all commodity risk premiums compress together.

| Failure mode | Mechanism | Early warning | Defense |
|---|---|---|---|
| Systemic crash | All commodities sell off; backwardation flattens | Cross-commodity correlation rising | Hard drawdown stop (20% intra-month per Rules) |
| Hedging behavior shift | Producers stop hedging; premium shrinks | Roll-yield spread compresses structurally | Monitor [[cot-report-analysis\|COT]] hedger positioning |
| Index flow reversal | Passive AUM declines; roll transfer fades | Falling index OI | Reweight toward producer-hedged contracts |
| Storage disruption | New capacity removes [[contango]] driver | Curve shapes decouple from inventories | Cross-check with inventory data |
| Seasonality artifact | Predictable seasonal curve mistaken for signal | Signal concentrated in seasonal contracts | Seasonality-adjust the roll yield |

## Kill Criteria

- Rolling 12-month Sharpe ratio < 0 for two consecutive years
- Maximum drawdown exceeds 35%
- The carry spread (return of top quintile minus bottom quintile) is insignificant (t-stat < 1.5) over trailing 5-year window
- Roll yield signal loses predictive power for next-month returns (information coefficient < 0.02 over 3 years)

## Advantages

- **Strong economic rationale** -- grounded in Keynes's theory of normal backwardation and producer hedging economics
- **Well-documented academically** across multiple decades and commodity universes
- **Low correlation** to equity and bond markets -- genuine portfolio diversifier
- **Complementary to momentum** -- carry and momentum are weakly correlated in commodities, making a combined carry+momentum portfolio more efficient
- **Transparent signal** -- roll yield is directly observable, no complex model estimation required
- **Low turnover** -- curve structures are persistent, reducing trading costs

## Disadvantages

- **Left-tail risk** -- earns small, steady premiums but suffers sharp drawdowns during crises (negative skew)
- **Sensitive to curve data quality** -- inaccurate or stale futures prices can distort roll yield signals
- **Small cross-section** -- only 20-30 commodities, limiting statistical power
- **Curve shape can be driven by non-informational factors** (storage economics, seasonal patterns) rather than risk premiums
- **Performance concentration** -- a few commodities with extreme roll yields can dominate portfolio returns
- **Correlated with other carry strategies** (FX carry, bond carry) during risk-off events -- less diversifying than it appears

## Sources

- Keynes, J.M. (1930). *A Treatise on Money.* (Normal backwardation theory.)
- Szymanowska, M. et al. (2014). "An Anatomy of Commodity Futures Risk Premia." *Journal of Finance.*
- Koijen, R.S.J. et al. (2018). "Carry." *Journal of Financial Economics.*
- Gorton, G., Hayashi, F. & Rouwenhorst, K.G. (2013). "The Fundamentals of Commodity Futures Returns." *Review of Finance.*
- (Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[carry-anomaly]] -- the carry factor across all asset classes
- [[carry-trade]] -- the FX cousin sharing the same risk-off failure mode
- [[commodity-momentum]] -- complementary factor (low correlation to carry)
- [[commodity-value-strategy]] -- the third pillar of commodity factor investing
- [[roll-yield]] -- the mechanical component of carry
- [[backwardation]] -- positive carry environment
- [[contango]] -- negative carry environment
- [[hedging-pressure]] -- the economic theory behind the carry premium
- [[convenience-yield]] -- why low inventories drive backwardation
- [[commodity-curve-rolls]] -- practical roll mechanics
- [[futures-curve-structure-analysis]] -- deeper curve analytics
- [[commodities]] -- market overview
- [[edge-taxonomy]] -- risk-bearing / structural edge classification
