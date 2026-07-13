---
title: "Dispersion Trade"
type: strategy
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [volatility, derivatives, options, quantitative, correlation, arbitrage]
aliases: ["Correlation Trade", "Dispersion Trading", "Index vs Single-Name Vol"]
strategy_type: quantitative
timeframe: position
markets: [options, stocks]
complexity: advanced
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "Sell richly-priced index volatility and buy comparatively cheap single-name volatility (or vice versa) to harvest the implied-correlation premium — index options embed an over-estimate of how tightly components co-move, set by structural hedging demand for index protection."
data_required: [options-chain, implied-volatility-surface, index-constituents-weights, correlation-estimates]
min_capital_usd: 250000
capacity_usd: 10000000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.30
breakeven_cost_bps: 20
related: ["[[implied-volatility]]", "[[realized-volatility]]", "[[variance-swap]]", "[[correlation]]", "[[volatility-trading]]", "[[delta-hedging]]", "[[edge-taxonomy]]", "[[variance-risk-premium]]"]
---

# Dispersion Trade

A dispersion trade is a relative-value [[volatility-trading|volatility]] strategy that takes opposing positions in **index volatility** and **single-name (component) volatility** to express a view on **implied [[correlation]]**. The classic "short correlation" version *sells* index volatility (e.g., short index [[variance-swap]] or short index straddles) and *buys* a basket of single-stock volatility on the index's constituents. It profits when realized correlation among components turns out lower than the implied correlation baked into index option prices — equivalently, when the dispersion of individual stock moves is high relative to the index move.

## Edge source

Per [[edge-taxonomy]], dispersion trading is a **structural** edge with a **risk-bearing** component:

- **Structural** — persistent, mandate-driven demand for *index* downside protection (from institutions hedging portfolios) bids up index [[implied-volatility]] relative to the weighted volatility of its components. Since index variance is a function of component variances *and* their pairwise correlations, this rich index vol implies a correlation level that historically tends to exceed subsequent realized correlation. The dispersion trader sells the rich index leg and buys the cheaper single-name legs to capture that gap.
- **Risk-bearing** — the short-correlation trade loses badly when correlations spike to ~1 in a crash (everything sells off together). The premium is compensation for absorbing that systemic co-movement risk.

## Why this edge exists

- **Who is on the other side**: large institutions and funds that systematically buy index puts and index volatility to hedge equity books. Their hedging demand is price-insensitive and one-directional, structurally enriching index vol.
- **Why they keep paying**: they are buying portfolio insurance, not making a vol forecast. The implied-correlation premium they pay is the cost of that insurance, and the dispersion trader earns it for taking the other side.
- **Why it isn't free money**: the trade is short correlation, and correlation is *exactly* what blows out in a crisis. The accumulated premium is repaid — often in a single deleveraging episode — when stocks crash in lockstep and the short-index leg loses far more than the long single-name legs gain.

## Null hypothesis

If index options correctly priced the future correlation of components, then index implied variance would equal the correlation-weighted sum of component implied variances, and a market-neutral dispersion book would earn **zero** before costs. Under this null, the short-index / long-components structure has no edge — it merely repackages the same variance with no informational or structural advantage, and after the substantial transaction costs of trading dozens of single-name option books, expected P&L is negative. Any claimed edge must demonstrate that *implied* correlation systematically exceeds *realized* correlation by more than costs — and must survive the rare regimes where realized correlation exceeds implied.

## Rules

### Entry
1. **Estimate implied correlation.** From index implied variance and component implied variances (and index weights), back out the market's implied correlation. High implied correlation = attractive short-correlation (long-dispersion) entry.
2. **Construct the legs.** Short index volatility (index [[variance-swap]], or short ATM index straddle, delta-hedged) and long single-name volatility on the largest-weight constituents (long single-stock straddles or variance swaps), vega-weighted.
3. **Vega-neutralize.** Size the component vega to offset index vega so the book is roughly neutral to a parallel shift in volatility and isolates the correlation view.
4. **Filter on the correlation premium.** Only enter when implied correlation is elevated relative to its history *and* realized correlation has been trending lower.

### Exit
1. **Correlation mean-reverts** to your target → take profit.
2. **Vega/correlation stop** → if implied correlation rises further against you past a threshold, cut.
3. **Roll** near expiry to maintain the spread.
4. **Crisis exit** → on a volatility/correlation spike, de-risk fast; short-correlation books bleed worst exactly here.

### Position sizing
- Size to survive a correlation-to-1 stress event, not to the modeled carry. Stress the book against a simultaneous index vol spike and correlation jump before sizing.
- Manage the operational load: holding vol on many single names multiplies transaction costs and pin/expiry risk.

## Implementation pseudocode

```python
def dispersion_trade(index, components, weights):
    iv_index = implied_vol(index)
    iv_comp  = {c: implied_vol(c) for c in components}
    # implied correlation from variance identity
    comp_var = sum(weights[c]**2 * iv_comp[c]**2 for c in components)
    cross    = sum(weights[i]*weights[j]*iv_comp[i]*iv_comp[j]
                   for i in components for j in components if i != j)
    implied_corr = (iv_index**2 - comp_var) / cross
    if implied_corr < HIGH_CORR_THRESHOLD:
        return None                         # correlation not rich enough
    short_vol(index, vega=V)                 # short index straddle / var swap
    for c in components:                     # long component vol, vega-weighted
        long_vol(c, vega=V * weights[c])
    while holding:
        delta_hedge_all()                    # neutralize directional drift
        if implied_corr_now() > STOP_CORR:   # correlation spiking against us
            unwind_all(); break
```

## Indicators / data used
- **Index [[implied-volatility]]** vs. **constituent implied volatilities** (the IV surface).
- **Index constituent weights** — define the basket and hedge ratios.
- **Implied correlation** (CBOE-style implied correlation indices, or computed from the variance identity).
- **[[realized-volatility]] and realized correlation** — the payoff reference.
- **[[variance-risk-premium]]** context — dispersion is a cousin of the index variance-premium trade.

## Example trade

*Illustrative, round numbers — not a backtest.*

Suppose a major equity index shows 20% implied vol, while the vega-weighted average of its top constituents' implied vols is 25%, implying an unusually high implied correlation (say ~0.65). The trader sells index volatility (short index variance) and buys single-name volatility on the largest constituents, vega-matched.
- **If realized correlation comes in low** (stocks move idiosyncratically), the single-name legs realize more volatility than the index leg — the long components win more than the short index loses, and the book profits.
- **If a shock hits and correlation jumps toward 1**, everything moves together: the short-index leg loses heavily while the long single-name legs gain little, producing a large loss. This left-tail is the cost of the carry.

## Performance characteristics
- **Return profile**: frequent modest gains harvesting the correlation premium, with rare large losses when correlation spikes — short-correlation / short-tail in nature.
- **Cost sensitivity**: heavy. Trading and hedging many single-name option books incurs large cumulative bid-ask and rebalancing costs; this is the dominant drag.
- **Best conditions**: calm, idiosyncratic, stock-pickers' markets where single names move on their own news.
- **Worst conditions**: macro-driven, high-correlation selloffs where the index moves as one.

## Capacity limits
Capacity is bounded by liquidity in single-name options (far thinner than index options) and by the market impact of running large vega across dozens of names. Index variance markets are deep, but the long single-name basket is the binding constraint. Crowding is moderate but episodic — the trade is concentrated among a handful of vol desks and funds, and crowded short-correlation positioning has amplified historical vol/correlation blowups.

## What kills this strategy
- **Correlation-to-1 events** — systemic crashes where the short-index leg dominates losses (see [[failure-modes]]).
- **Transaction-cost bleed** from rebalancing many single-name books.
- **Liquidity gaps** in single-name options that prevent clean hedging or exit.
- **Crowding cascades** — synchronized unwinds of short-correlation books.

## Kill criteria
- Realized correlation rises above implied correlation at entry → the thesis is inverted; exit.
- Book drawdown exceeds ~2× the modeled carry → cut.
- Implied correlation jumps more than a set threshold (e.g., +0.15) against the position → de-risk.
- Single-name option liquidity deteriorates such that hedging slippage exceeds the carry → close.

## Advantages
- Market-neutral expression of a pure correlation/dispersion view.
- Harvests a structurally persistent implied-correlation premium.
- Diversifies a book away from simple directional or single-vol exposures.
- Rich analytical framework (variance identity) for sizing and monitoring.

## Disadvantages
- **Short-correlation tail** — large losses precisely in market crashes.
- **High operational and transaction cost** across many single-name legs.
- **Liquidity-constrained** on the single-name side.
- **Model-dependent** — implied-correlation estimates rely on weights and surface assumptions.
- **Crowding** amplifies unwind severity.

## Sources
General market knowledge; no specific wiki source ingested yet.

## Related
- [[variance-swap]] — common instrument for both legs
- [[implied-volatility]], [[realized-volatility]] — the priced vs. delivered vol
- [[correlation]] — the variable being traded
- [[variance-risk-premium]] — the related index-vol premium
- [[volatility-trading]], [[delta-hedging]] — adjacent methods
- [[edge-taxonomy]] — classification
