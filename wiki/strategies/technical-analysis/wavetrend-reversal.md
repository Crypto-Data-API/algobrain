---
title: "WaveTrend Reversal"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [mean-reversion, momentum, technical-analysis, swing-trading, crypto]
aliases: ["WaveTrend Cross Strategy", "WT Oversold Cross", "WaveTrend Mean Reversion"]
strategy_type: technical
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[wavetrend-oscillator]]", "[[overbought-oversold]]", "[[rsi-divergence]]", "[[range-trading]]", "[[adx]]", "[[tradingview-community-scripts]]"]

edge_source: [behavioral]
edge_mechanism: "Short-horizon overreaction: when a swing extends far enough to push a doubly-smoothed CCI past its extreme band and the fast line then turns through its signal line, late momentum chasers and forced sellers have largely finished, and price tends to mean-revert toward its EMA baseline. Only valid when a higher-level trend filter says the market is ranging or trending in the trade's direction."
data_required: [ohlcv-4h, ohlcv-daily, trend-classifier]
min_capital_usd: 1000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.3
expected_max_drawdown: 0.2
breakeven_cost_bps: 15
kill_criteria: |
  - rolling 40-trade expectancy < 0 after costs
  - rolling 6-month net Sharpe < 0
  - more than 60% of losing trades occur while the trend filter reads against the trade (filter broken)
---

# WaveTrend Reversal

A swing mean-reversion strategy that buys oversold crosses and sells overbought crosses of LazyBear's [[wavetrend-oscillator|WaveTrend Oscillator]], using a trend classifier as a filter so it does not fade strong trends. It is the literal trading rule in the original script's description: buy when WT1 crosses above WT2 below the oversold band, and sell on the mirror condition. It was published on TradingView by **LazyBear** on 2014-05-27 (https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/). Labelled-entry forks such as thomcam's "WaveTrend [LazyBear] with Long/Short Labels" wrap it for alerts (Source: [[tradingview-community-scripts]]).

## Edge source

**Behavioral.** Short-horizon overreaction and exhaustion. The WT extreme band is a normalised measure of how far the typical price has run from its EMA baseline, and the cross is a confirmation that the run has stopped accelerating. See [[edge-taxonomy]] and [[overbought-oversold]].

## Why this edge exists

In crypto, short swings are amplified by leverage. Late breakout buyers and liquidation cascades push price beyond fair short-term levels, and once forced flow ends, price tends to retrace part of the move. The counterparties are the late chasers and liquidated positions. The edge fails badly when the move is not overreaction but a regime change (a trend), because oscillator extremes then persist. That is why the trend filter is mandatory rather than optional.

## Null hypothesis

With no edge, forward 6-24 bar returns after an oversold cross would match returns after random bars drawn from the same trend-filter state. The test uses matched random entries with identical exits and costs. Also check that the filter alone (trade randomly only when the filter allows) does not explain the result.

## Rules

**Entry (long; short is the mirror)**
1. On the closed 4h bar, WT1 crosses above WT2 while WT1 is below −53 (or below the asset's 10th-percentile WT1 level for high-vol alts).
2. Trend filter: the daily trend classifier is not bearish (ADX/DMI not RED, or the close is above the daily 100-EMA).
3. Optional confluence: bullish [[divergence]], meaning price makes a lower low while WT1 makes a higher low versus the prior oversold trough.
4. Enter at the next bar's open.

**Exit**
- Target: WT1 reaches +20 or the opposite (overbought) cross fires, whichever comes first
- Stop: below the swing low of the last 10 bars minus 0.5 × ATR(14)
- Time stop: 24 bars

**Position sizing**
- Risk 0.5% of equity to the stop. Halve size when the daily trend filter reads neutral (GREY).

## Implementation pseudocode

```python
for bar in closed_bars(symbol, "4h"):
    wt1, wt2 = wavetrend(bar_history, n1=10, n2=21)
    os_level = percentile(wt1_history, 10) if is_high_vol_alt else -53
    if position is None:
        cross_up = wt1[-1] > wt2[-1] and wt1[-2] <= wt2[-2]
        if cross_up and wt1[-1] < os_level and trend_state(symbol, "1d") != "RED":
            stop = min(low[-10:]) - 0.5 * atr14
            size = equity * 0.005 / (next_open - stop)
            if trend_state(symbol, "1d") == "GREY": size /= 2
            enter("long", size, at="next_open", stop=stop)
    else:
        if wt1[-1] >= 20 or overbought_cross(wt1, wt2) or position.age >= 24:
            exit(position, at="next_open")
```

## Indicators / data used

- [[wavetrend-oscillator]]: WT1/WT2 crosses and bands
- [[adx]] / CryptoDataAPI Signum RGG: the trend filter
- [[atr]]: stop buffer
- [[divergence]]: optional confluence

## Example trade

*Illustrative, not a backtest result.* ETHUSDT 4h in a sideways month. After a liquidation wick, WT1 bottoms at −68, then crosses WT2 at −58 on the bar close. The daily Signum RGG reads GREY (neutral), so the position is half size. Entry at the next open is $2,400. The 10-bar swing low is $2,310 and ATR is $45, so the stop is $2,287.50. Risk of 0.25% on a $100k book gives about 2.2 ETH. Six bars later WT1 reaches +22 and the position exits at $2,505. Gross is about +$233. A 10 bps round trip costs about $10, leaving about +$223 (about 0.9R). A short time-in-market keeps funding negligible.

## Performance characteristics

No independent, cost-adjusted backtest was found. Published community strategies built on WaveTrend report TradingView Strategy Tester results that generally use zero default commission, and they should be treated as pre-cost author claims (Source: [[tradingview-community-scripts]]). Structural expectations: a moderate-to-high hit rate (roughly 50-60%) with small winners, a negative skew from the occasional trend continuation through the stop, and strong dependence on the trend filter. On 1h and lower timeframes, turnover makes the strategy highly cost-sensitive. The frontmatter `breakeven_cost_bps` of 15 is a prior, so re-derive it from the backtest.

## Capacity limits

The entry comes after liquidation-driven dislocations, which is when books are thin. On BTC/ETH the capacity is in the tens of millions per signal at next-open fills. On alts it is in the low hundreds of thousands, and posting limit orders instead of crossing the spread matters.

## What kills this strategy

- **Trend regimes.** Oversold crosses in a bear trend (for example 2022) repeatedly fail. If the filter lags, drawdown clusters ([[failure-modes]]).
- **Crowding.** WT is one of the most-copied TradingView scripts, and the default-band crosses are widely watched.
- **Band drift.** Fixed ±53 bands misfire on assets whose volatility has changed.
- **Stacking with correlated confirmations.** Adding RSI or Stochastic oversold conditions adds little independent information, because they are all bounded momentum oscillators ([[overfitting]]).

## Kill criteria

Retire or pause (see [[when-to-retire-a-strategy]]) if any of these hold:
- The rolling 40-trade expectancy is negative after costs.
- The rolling 6-month net Sharpe is below 0.
- More than 60% of losses occur while the trend filter reads against the trade, which means the filter is not working.

## Advantages

- A simple, open-source, fully specified signal with few parameters.
- Frequent signals across a multi-asset universe allow statistical evaluation faster than a breakout strategy can.
- A short holding period, so funding carry is minor.

## Disadvantages

- Negative skew: small wins, occasional large trend losses.
- Heavily crowded default settings.
- Relies on a separate trend filter whose own lag drives much of the performance.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=200`: bars for WT1/WT2
- `GET /api/v1/indicators/signum-rgg/{symbol}`: ADX(14)+DMI RED/GREY/GREEN trend filter with 60-day history

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep archive for crosses, per-asset band calibration and the matched-random null test

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/signum-rgg/ETH"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-indicators]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal**: on each 4h close, compute WT1/WT2 from `GET /api/v1/market-data/klines` for the watchlist and flag crosses beyond the per-asset percentile bands
- **Trend gate**: `GET /api/v1/indicators/signum-rgg/{symbol}` blocks longs in RED and shorts in GREEN, and halves size in GREY
- **Backtest**: replay `GET /api/v1/backtesting/klines` with next-open fills and costs, split results by trend-filter state, and compare against matched random entries in the same state
- **Monitoring**: `GET /api/v1/regimes/current`. A shift to a trending macro regime label is the early warning for this strategy's main failure mode

## Related

- [[wavetrend-oscillator]]: the signal
- [[overbought-oversold]], [[rsi-divergence]]: related oscillator-reversal approaches
- [[range-trading]]: the regime where it works
- [[adx]]: the trend-filter logic
- [[tradingview-community-scripts]], [[external-strategy-sources]]: where the idea came from

## Sources

- LazyBear, "Indicator: WaveTrend Oscillator [WT]", TradingView, 2014-05-27. thomcam, "WaveTrend [LazyBear] with Long/Short Labels" (Source: [[tradingview-community-scripts]])
