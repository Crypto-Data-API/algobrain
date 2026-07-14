---
title: "Range Trading"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [technical-analysis, mean-reversion, swing-trading, indicators, volatility]
aliases: ["Range Trading", "Channel Trading", "Range-Bound Trading", "Sideways Market Trading"]
related: ["[[mean-reversion]]", "[[support-resistance]]", "[[bollinger-bands]]", "[[rsi]]", "[[breakout-trading]]", "[[grid-trading]]", "[[market-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: technical
timeframe: intraday
markets: [forex, crypto, futures]
complexity: beginner
backtest_status: naive-backtested
edge_source: [behavioral, structural]
edge_mechanism: "Liquidity providers and dealers repeatedly buy near a defined floor and sell near a defined ceiling, fading retail momentum chasers; in a balanced (non-trending) regime price oscillates between these levels and the trader collects the round-trip."
data_required: [ohlcv-intraday, ohlcv-daily]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 15
---

Range trading buys near a well-defined [[support-resistance|support]] level and sells (or shorts) near a well-defined resistance level, betting that price will continue oscillating inside a horizontal channel rather than breaking out. It is the canonical [[mean-reversion]] strategy for *balanced* or *sideways* markets — periods when no trend dominates and price reverts to the middle of a band. The entire edge depends on correctly identifying that the market is range-bound (a [[market-regime]] judgment) and exiting fast when it is not. Range trading is the regime-complement of [[trend-following]] and [[breakout-trading]]: the same boundary that a range trader fades is the trigger a breakout trader buys, so the two strategies profit in opposite regimes and a complete book usually runs both with a regime switch between them.

> **Relationship to neighbouring strategies.** Range trading sits in a family of horizontal-channel methods. [[grid-trading]] mechanizes it by placing a ladder of bids and offers across the channel and removing the discretionary entry. [[bollinger-bands|Bollinger-band mean reversion]] uses a volatility-adaptive channel instead of static lines. [[pairs-trading]] applies the same fade-the-extreme logic to the *spread* between two correlated instruments rather than a single price. All share the same Achilles heel: a regime change that turns the oscillation into a one-way move.

## Edge source

Primarily **behavioral**, with a **structural** component (see [[edge-taxonomy]]). The behavioral side: round numbers, prior swing highs/lows, and overnight VWAP act as psychological anchors where order flow clusters, so price stalls and reverses there. The structural side: market makers and inventory-managing dealers passively provide liquidity at the edges of an established range, fading momentum and pushing price back toward the mean. The range trader piggybacks on these mean-reverting forces.

| Edge dimension | Present? | Mechanism in range trading |
|---|---|---|
| Behavioral | Primary | Anchoring on round numbers / prior swings; over-extrapolation of small moves by momentum chasers; reflexive clustering of resting orders at "obvious" levels |
| Structural | Secondary | Dealer / market-maker inventory management passively supplies liquidity at the band edges, mechanically mean-reverting price |
| Informational | No | The range trader has no superior information; the level is public |
| Analytical | Weak | Modest edge in *regime classification* (knowing when the range is valid) — the genuinely hard, value-adding inference |
| Latency | No | Daily/intraday horizon; no co-location advantage required |
| Risk-bearing | Partial | The trader is short the tail of a breakout — paid small premiums for insuring against moves that mostly do not happen, until one does |

## Why this edge exists

Who is on the other side? Mostly **momentum/[[breakout-trading|breakout]] traders and stop-loss orders** that fire at the range boundaries. When price pokes above resistance, breakout chasers pile in and stops trigger — but in a balanced regime there is no fundamental fuel behind the move, so dealers absorb the flow and price snaps back. The range trader is effectively selling insurance against breakouts that do not materialize. They keep losing because most boundary tests in a quiet market are *false* breakouts, and humans systematically over-extrapolate small moves (see [[behavioral-finance]]). The edge is real only while the regime stays balanced; it inverts violently the moment a genuine trend begins.

Why doesn't this edge get arbitraged away? Two reasons. First, the *cost* of being wrong is asymmetric and lumpy — the strategy's whole P&L distribution is negatively skewed (see [[skewness]]), so capital is reluctant to crowd in, which preserves the round-trip for the disciplined. Second, the edge is *conditional*: it only exists in the balanced regime, and the moment when fading is most tempting (a long, clean, oft-tested range) is precisely when the breakout is most dangerous because so many stops and crowded fades sit just beyond the boundary. The hard, non-commoditised part of the strategy is therefore not the entry rule but the regime filter — exactly the part most traders skip.

## Null hypothesis

Under no edge, price is a random walk and "support"/"resistance" are artifacts of hindsight. A range strategy would then: (a) win small repeatedly inside noise but (b) give all gains back on the eventual breakout, netting to roughly zero before costs and clearly negative after spread and commissions. The honest test is whether a *pre-registered* range definition (e.g., 20-day high/low channel that has held N touches) produces a positive expectancy net of costs out-of-sample — not whether you can draw two parallel lines on a chart after the fact.

## Rules

**Regime filter (gate):** Trade only when ADX < 20–25 (weak trend) and price has produced at least two confirmed touches of both boundaries. Skip entirely in strong-trend regimes.

**Define the range:** Support = recent confirmed swing low / lower Bollinger Band; Resistance = recent confirmed swing high / upper band. Require the channel width to exceed a multiple of ATR so the round-trip clears costs.

**Entry:**
- Long near support: price within ~0.25 ATR of support AND a reversal confirmation (RSI < 30 turning up, or a bullish reversal candle, or lower-band tag with a close back inside).
- Short near resistance: mirror image (RSI > 70 turning down, upper-band tag, bearish reversal candle).

**Exit:**
- Target: the opposite boundary, or the range midpoint for a faster, higher-hit-rate variant.
- Stop: a fixed fraction beyond the boundary (e.g., 0.5–1.0 ATR past support/resistance). A *decisive close* outside the range is the breakout signal — flip to flat or to a breakout play.

**Sizing:** Risk a fixed fraction (0.5–1% of equity) per trade based on the distance from entry to stop. Because stops are tight relative to the channel, position size can be larger than in trend strategies, but never override the per-trade risk cap. (See [[position-sizing]] and [[risk-management]].)

| Parameter | Typical setting | Rationale |
|---|---|---|
| Regime gate | ADX(14) < 20–25 | Stand aside in trending regimes — the single highest-value filter |
| Range definition | 20-bar high/low channel, ≥ 2 confirmed touches each side | Mechanical, pre-registered; avoids hindsight line-drawing |
| Minimum channel width | ≥ ~3 × ATR(14) | Ensures the round-trip clears spread + commission |
| Entry proximity | within ~0.25 ATR of boundary | Buy/sell only at the extreme, not mid-channel |
| Entry confirmation | RSI < 35 (long) / > 65 (short) turning, or reversal candle | Filters out boundary breaks already underway |
| Target | opposite boundary (full) or midpoint (fast, higher hit-rate) | Midpoint variant trades reward for hit-rate |
| Stop | 0.5–1.0 ATR beyond the boundary | A decisive *close* outside = regime change, exit |
| Per-trade risk | 0.5–1.0% of equity | Caps the drawdown from the inevitable breakout loss |

## Implementation pseudocode

```python
def range_trade(bar, state):
    atr = ATR(14)
    adx = ADX(14)
    if adx > 25:                      # regime gate: trend present -> stand aside
        return flatten()

    support, resistance = channel(lookback=20, min_touches=2)
    if support is None:               # no valid range
        return flatten()

    rsi = RSI(14)
    near = 0.25 * atr

    if position == 0:
        if bar.low <= support + near and rsi < 35 and reversal_up(bar):
            enter_long(stop=support - 0.75*atr, target=resistance)
        elif bar.high >= resistance - near and rsi > 65 and reversal_down(bar):
            enter_short(stop=resistance + 0.75*atr, target=support)
    else:
        # decisive close outside range = failed range -> exit
        if (position > 0 and bar.close < support - 0.5*atr) or \
           (position < 0 and bar.close > resistance + 0.5*atr):
            flatten()                 # breakout against us
        else:
            manage_target_and_stop(bar)
```

## Indicators / data used

- [[support-resistance]] levels (swing highs/lows, prior session ranges, round numbers)
- [[bollinger-bands]] as a dynamic channel proxy
- [[rsi]] (or stochastics) for overbought/oversold confirmation at boundaries
- ADX to filter out trending regimes (the single most important input)
- ATR for sizing, stop placement, and the minimum-width filter
- OHLCV intraday and daily bars

## Example trade

EUR/USD chops between 1.0800 (support) and 1.0900 (resistance) for two weeks, ADX = 16. Price tags 1.0810, RSI prints 28 and ticks up, and a bullish hammer closes at 1.0825. Enter long 1.0825, stop 1.0780 (45 pips), target 1.0890 (65 pips) — roughly 1.4:1 reward:risk. Price drifts back to 1.0888 over three days; exit at target. If instead price had closed at 1.0775, the stop fires for a 50-pip loss and the trader stands aside, because a decisive break of support warns the range is over.

## Performance characteristics

Range strategies typically show a **high hit rate (55–70%)** with **small average wins** and occasional larger losses on the breakout that ends the range — a left-skewed, "picking up nickels in front of a steamroller" profile (negative [[skewness]]). Realistic expectations net of a 1–3 pip / few-bps spread plus commission: Sharpe roughly 0.4–0.8 when the regime filter is disciplined, and meaningfully negative without it. The strategy's lifetime P&L is dominated by *how cleanly you exit when the range breaks*; most of the theoretical edge is destroyed by holding through false-breakout whipsaws and by trading ranges too narrow to clear costs.

> **Why naive backtests flatter this strategy.** Because the win rate is high, a curve-fit range bot looks superb until the first regime change. The honest read of performance must (a) include every false-breakout whipsaw, (b) apply realistic spread/commission on *both* legs, and (c) pre-register the range and regime rules out-of-sample. The figures above are qualitative ranges drawn from [[backtesting|practitioner backtests]] of the genre, **not** a verified backtest of a specific system; treat any quoted Sharpe with [[deflated-sharpe-ratio|deflation]] in mind.

| P&L characteristic | Range trading | Contrast: [[trend-following]] |
|---|---|---|
| Hit rate | High (55–70%) | Low (30–45%) |
| Skew of returns | Negative (small wins, rare big loss) | Positive (small losses, rare big win) |
| Best regime | Balanced / mean-reverting | Trending / directional |
| Worst event | Genuine breakout / regime change | Choppy, whipsawing range |
| Equity-curve feel | Smooth then a cliff | Grindy drawdowns then a jump |
| Cost sensitivity | High (many round-trips, tight targets) | Lower (fewer, larger trades) |

## Capacity limits

Capacity is moderate and venue-dependent. On deep FX majors and large-cap index futures it scales to several million dollars per name before quotes at the boundaries move against the trader. On thin altcoins or small-cap stocks the "range" is partly your own footprint, and capacity collapses to tens of thousands. As a rule, keep per-trade size below ~1–2% of the average dollar volume traded inside the channel.

## What kills this strategy

The dominant failure mode (see [[failure-modes]]) is **regime change**: the range that printed cleanly for weeks resolves into a trend, and the strategy keeps shorting resistance and buying support straight into a one-way move. Secondary killers: ranges too narrow to clear transaction costs; over-fitting boundary lines to noise; and crowding — when too many traders fade the same obvious level, the "stop run" through it becomes a self-fulfilling breakout.

| Failure mode | Trigger | Mitigation |
|---|---|---|
| Regime change to trend | Fundamental catalyst, breakout with volume | ADX gate; exit on decisive close beyond boundary |
| Whipsaw / false-break churn | Choppy boundary tests just past the line | Wider stop buffer; require close-back-inside confirmation |
| Costs exceed channel width | Narrow range, wide spread | Minimum-width filter (≥3 ATR); skip thin instruments |
| Over-fit boundaries | Lines drawn in hindsight | Mechanical, pre-registered channel rule; OOS / walk-forward test |
| Crowding-driven stop run | Too many fades at the same obvious level | Avoid the most-watched levels; size down; trail exits |
| Liquidity gap (overnight, news) | Stop jumps past placement | Cap event-window exposure; reduce size around scheduled news |

## Kill criteria

- Rolling 60-trade hit rate falls below 50% **and** expectancy turns negative net of costs.
- Drawdown exceeds 20% of allocated capital.
- More than 3 consecutive losses caused by holding through breakouts (regime filter is failing).
- ADX-filter back-test edge does not survive out-of-sample / walk-forward validation.

## Advantages

- Conceptually simple, beginner-accessible, works on any liquid instrument and timeframe.
- High win rate gives a smooth equity curve during the (frequent) balanced regimes.
- Clear, objective stop level (the range boundary) makes risk easy to define.
- Complements trend-following: the two profit in opposite regimes (see [[market-regime]]).

## Disadvantages

- Negatively skewed: many small wins, then a large loss when the range breaks.
- Critically dependent on correctly classifying the regime — the hardest part is not the entry.
- Easily over-fit; "support" and "resistance" are subjective without a mechanical rule.
- Costs eat narrow ranges alive; requires sufficient channel width to be viable.

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — support/resistance and trading ranges.
- Welles Wilder, *New Concepts in Technical Trading Systems* (1978) — ADX and ATR, the regime/volatility tools used here.
- Investopedia, "Range Trading" and "How to Trade in a Range-Bound Market."
- General market knowledge; no specific wiki source ingested yet. Performance figures above are illustrative practitioner ranges, not a verified backtest.

## Related

- [[mean-reversion]]
- [[support-resistance]]
- [[bollinger-bands]]
- [[rsi]]
- [[breakout-trading]]
- [[trend-following]]
- [[grid-trading]]
- [[pairs-trading]]
- [[market-regime]]
- [[position-sizing]]
- [[risk-management]]
- [[behavioral-finance]]
- [[skewness]]
- [[edge-taxonomy]]
- [[failure-modes]]
