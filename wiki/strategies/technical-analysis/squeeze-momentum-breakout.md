---
title: "Squeeze Momentum Breakout"
type: strategy
created: 2026-09-28
updated: 2026-10-17
status: draft
tags: [breakout, volatility, momentum, technical-analysis, crypto, perpetual-futures]
aliases: ["Squeeze Momentum Strategy", "TTM Squeeze Breakout", "SQZMOM Strategy", "Squeeze Fire Strategy"]
strategy_type: technical
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[squeeze-momentum-indicator]]", "[[volatility-breakout]]", "[[bollinger-bands]]", "[[keltner-channels]]", "[[volatility-clustering]]", "[[funding-rate]]", "[[tradingview-community-scripts]]"]

edge_source: [analytical, behavioral]
edge_mechanism: "Volatility clusters: after a sustained BB-inside-KC compression, realised volatility tends to expand, and the first release bar in the direction of regression momentum catches the start of that expansion. The other side is range-traders and short-vol sellers still positioned for continued calm, plus stop-clusters that form at the edges of a tight range."
data_required: [ohlcv-4h, ohlcv-daily, funding-rates, volatility-regime]
min_capital_usd: 1000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 0.4
expected_max_drawdown: 0.25
breakeven_cost_bps: 25
kill_criteria: |
  - rolling 30-signal hit rate < 35% with average win/loss < 1.8
  - rolling 12-month net Sharpe < 0
  - fires per year on BTC 4h fall below 4 (setup too rare to evaluate)
gates:
  - id: squeeze_run_6
    role: entry
    rule: "Squeeze on (Bollinger Bands 20/2.0 inside Keltner Channels 20/1.5) for at least 6 consecutive closed 4h bars"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&limit=80
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&start={start}
    replay_field: candles[].close
    note: "Compute BB and KC from the bars' high, low and close (LazyBear's KC uses a 20-bar SMA with 1.5x the 20-bar mean true range). No squeeze series is served. Drop the forming bar named by forming_bar_timestamp."
  - id: fire_bar
    role: entry
    rule: "The fire bar is the first closed bar where the squeeze is off; enter at the next bar's open, never at the fire bar's close"
    runnable: true
    input: derived
    inputs: [squeeze_run_6]
  - id: histogram_direction
    role: entry
    rule: "Long if the momentum histogram is above zero and rising on the fire bar; short if below zero and falling; skip if sign and slope disagree"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&limit=80
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&start={start}
    replay_field: candles[].close
    note: "LazyBear histogram: 20-bar linear regression of close minus the mean of (the midpoint of the 20-bar highest high and lowest low) and the 20-bar SMA of close. Computed by the bot."
  - id: funding_top_decile_skip
    role: filter
    rule: "Optional: skip longs when perp funding is in the top decile of its 90-day range (shorts in the bottom decile)"
    runnable: true
    endpoint: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=4h&start={start}
    field: data[].funding_rate_mean
    note: "start = 90 days ago (the window cap is 93 days). Rank /hyperliquid/funding-rates current_rate against the 90 days of bar means. Funding history begins 2026-03-30."
  - id: vol_regime_gate
    role: filter
    rule: "Optional: skip if the asset is already in a high-vol regime; the regime should read compressed before the fire"
    runnable: partial
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "The served regime is computed on daily bars, while the setup is 4h. 'High vol' is not a served label: vol_shock is the clear case, and whether expanding also counts is the desk's call."
  - id: momentum_fade_exit
    role: exit
    rule: "Exit at the next open after the second consecutive histogram bar that moves toward zero"
    runnable: true
    input: derived
    inputs: [histogram_direction]
  - id: initial_stop_1_5atr
    role: stop
    rule: "Initial stop 1.5x ATR(14) beyond the entry price"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&limit=40&atr=14
    field: candles[].atr
    note: "ATR of the fire bar (the last closed 4h bar)."
  - id: chandelier_trail
    role: stop
    rule: "Then trail with a 2.5x ATR chandelier: highest high since entry minus 2.5x ATR(14) for longs (lowest low plus 2.5x ATR for shorts)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=4h&limit=40&atr=14
    field: candles[].atr
  - id: time_stop_20_bars
    role: exit
    rule: "Close after 20 bars if neither exit has triggered"
    runnable: true
    input: position
  - id: risk_per_trade
    role: sizing
    rule: "Risk 0.5-1% of equity per trade to the initial stop (0.75% in the pseudocode)"
    runnable: true
    input: position
  - id: leverage_cap_3x
    role: sizing
    rule: "Cap leverage at 3x on perps"
    runnable: true
    input: position
  - id: kill_hit_rate
    role: filter
    rule: "Pause when the rolling 30-signal hit rate is below 35% while the average win/loss ratio is below 1.8"
    runnable: true
    input: position
  - id: kill_sharpe
    role: filter
    rule: "Pause when the rolling 12-month net Sharpe is below 0"
    runnable: true
    input: position
  - id: kill_fire_frequency
    role: filter
    rule: "Pause when fires per year on BTC 4h fall below 4"
    runnable: true
    input: derived
    inputs: [fire_bar]
    note: "Count fire bars on BTC over the trailing year; the 4h replay reaches back about 800 days."
  - id: kill_live_vs_backtest
    role: filter
    rule: "Pause when live and backtest fire outcomes diverge by more than 2 standard errors over 20 signals (a repainting backtest)"
    runnable: true
    input: position
---

# Squeeze Momentum Breakout

A volatility-expansion strategy built on the [[squeeze-momentum-indicator|Squeeze Momentum Indicator]]. It waits for a run of squeeze bars ([[bollinger-bands|Bollinger Bands]] inside [[keltner-channels|Keltner Channels]]), then enters on the first bar where the squeeze releases, in the direction of the linear-regression momentum histogram. It exits when momentum fades or an ATR stop is hit. This is the most common strategy wrapper around LazyBear's open-source script on TradingView. Community versions include "Squeeze Momentum Indicator Strategy [LazyBear + PineIndicators]" (https://www.tradingview.com/script/G40dtEbK-Squeeze-Momentum-Indicator-Strategy-LazyBear-PineIndicators/) and "Strategy based on Squeeze Momentum Indicator [LazyBear]" by 03.freeman (https://www.tradingview.com/script/qp9BoNyS-Strategy-based-on-Squeeze-Momentum-Indicator-LazyBear/) (Source: [[tradingview-community-scripts]]).

## Edge source

**Analytical (primary).** Crypto realised volatility clusters and mean-reverts ([[volatility-clustering]]). A BB-inside-KC state is an objective, scannable definition of "volatility below its own ATR envelope", and the release bar marks the transition.

**Behavioral (secondary).** Range-traders keep fading the edges of a tight range, and short-premium or grid bots keep selling volatility until the range breaks. Their stops and liquidations add fuel in the break direction. See [[edge-taxonomy]].

## Why this edge exists

A compression is when range-bound strategies look best, so capital crowds into them. When the range breaks, those positions are forced to exit the same way, and on leveraged perps forced exits become liquidations. The squeeze trader is on the other side of that exit flow. The weakness is direction: the squeeze is directionless and the histogram lags, so many fires resolve into a short false break before the real move, often the opposite way.

## Null hypothesis

Under no edge, the forward 10-bar return after a squeeze fire, signed by histogram direction, would be indistinguishable from the forward return after a random bar with the same histogram sign. Realised volatility after a fire would equal unconditional volatility. The test compares fire-bar outcomes against matched random entries with the same ATR stop and holding rule, after costs. A result that only beats random before fees fails.

## Rules

**Entry**
1. Squeeze state on (BB 20/2.0 inside KC 20/1.5) for **at least 6 consecutive closed bars**.
2. The first closed bar where the squeeze is off is the fire bar.
3. **Long** if the histogram is above zero and rising on the fire bar. **Short** if it is below zero and falling. Skip if the sign and slope disagree.
4. Optional filters: skip longs when the perp [[funding-rate]] is in the top decile of its 90-day range (and the reverse for shorts). Skip if the asset is already in a high-vol regime.
5. Enter at the next bar's open (never at the fire bar's close).

**Exit**
- Momentum fade: exit at the close of the second consecutive histogram bar that moves toward zero (dark green for longs, dark red for shorts), or
- Initial stop: 1.5 × ATR(14) beyond entry, then trail with a 2.5 × ATR [[chandelier-exit|chandelier]]
- Time stop: close after 20 bars if neither has triggered

**Position sizing**
- Risk 0.5-1% of equity per trade to the initial stop. Cap leverage at 3× on perps.

## Implementation pseudocode

```python
for bar in closed_bars(symbol, "4h"):
    sqz_run = sqz_run + 1 if bar.sqz_on else 0
    if position is None:
        fired = (not bar.sqz_on) and prev.sqz_on and prev_run >= 6
        if fired:
            side = "long" if bar.mom > 0 and bar.mom > prev.mom else \
                   "short" if bar.mom < 0 and bar.mom < prev.mom else None
            if side and funding_ok(side) and vol_regime(symbol) != "high":
                stop = next_open -/+ 1.5 * atr14
                size = equity * 0.0075 / abs(next_open - stop)
                enter(side, size, at="next_open", stop=stop)
    else:
        trail_chandelier(position, mult=2.5)
        if momentum_faded(bars, 2) or position.age >= 20:
            exit(position, at="next_open")
    prev, prev_run = bar, sqz_run
```

## Indicators / data used

- [[squeeze-momentum-indicator]]: squeeze state plus the regression-momentum histogram
- [[atr]]: stop distance and chandelier trail
- [[funding-rate]]: crowding filter on perps
- CryptoDataAPI klines, funding and volatility regime (see below)

## Example trade

*Illustrative, not a backtest result.* BTCUSDT 4h. After eight black-cross squeeze bars in a roughly 3% range, the fire bar closes with the histogram above zero and rising. Entry at the next open, $60,000. ATR(14) is $900, so the stop is $58,650 (1.5 × ATR). Risking 0.75% of a $100k book gives about 0.56 BTC. Price expands to $63,800 over 9 bars, and the chandelier trail sits at $61,550. Two dark-green histogram bars follow, and the position exits at the next open, $63,100. Gross gain is about $1,740. After a 10 bps round trip on about $34k notional ($34), plus funding over 36 hours of roughly $15-30, net is about $1,680 (about 2.3R).

## Performance characteristics

No independent, cost-adjusted backtest was found. Community strategy scripts publish TradingView Strategy Tester results that typically use zero default commission, a single symbol and an arbitrary date window. Treat any such figure as a pre-cost author claim, not evidence (Source: [[tradingview-community-scripts]]). Structural expectations: a low hit rate (roughly 35-45%) with larger winners, returns concentrated in a few large expansions per year, and long flat or bleeding periods during trending markets that never compress. Apply a round-trip cost of 10-20 bps plus funding on perps before evaluating. The frontmatter `expected_sharpe` of 0.4 is a placeholder prior, not a measurement.

## Capacity limits

On BTC/ETH 4h, fills at the next open absorb seven-figure notional with little impact, so capacity is in the tens of millions. On alts, the squeeze-fire bar is exactly when liquidity thins and spreads widen. Mid-cap alt capacity is in the low hundreds of thousands per signal before slippage dominates.

## What kills this strategy

- **Crowding.** The script is among the most-viewed on TradingView. Default-setting fires are widely watched, and front-running produces fake breaks ([[failure-modes]]).
- **Regime shift to persistent trend.** No compressions means no trades, while fixed costs of monitoring continue.
- **Regime shift to persistent chop.** Many fires with no follow-through, the classic false-breakout bleed.
- **Lookahead in ported code.** MTF variants using `request.security` with lookahead make historical fires look better than live ones ([[lookahead-bias]]).

## Kill criteria

Retire or pause (see [[when-to-retire-a-strategy]]) if any of these hold:
- The rolling 30-signal hit rate falls below 35% while the average win/loss ratio is below 1.8.
- The rolling 12-month net Sharpe falls below 0.
- Live-versus-backtest fire outcomes diverge by more than 2 standard errors over 20 signals, which suggests the backtest was repainting.

## Advantages

- An objective, fully mechanical setup, easy to port from open-source Pine to Python.
- A defined-risk entry right after compression, when ATR-scaled stops are tight.
- Works across assets and timeframes, which allows portfolio-level diversification of fires.

## Disadvantages

- The squeeze is directionless and the lagging histogram decides direction, so many losers come from false first moves.
- Returns come from rare events, so there are long flat periods.
- Heavily crowded default parameters.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200`: bars for BB, KC and the histogram
- `GET /api/v1/derivatives/funding-rates?coin=BTC`: cross-venue funding for the crowding filter
- `GET /api/v1/volatility/regime`: per-asset volatility regime for the pre-fire compression check

**Historical data:**
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive): kline history for fire detection
- `GET /api/v1/backtesting/funding`: historical funding for the filter and carry cost

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal**: poll `GET /api/v1/market-data/klines` on the 4h close for a watchlist. Detect squeeze runs of 6 or more bars and the release bar, and read histogram sign and slope on the closed bar
- **Regime gate**: `GET /api/v1/volatility/regime` should read compressed before the fire. Skip fires in assets already tagged high-vol
- **Crowding filter**: `GET /api/v1/derivatives/funding-rates?coin=...` blocks longs into top-decile positive funding and shorts into deeply negative funding
- **Backtest**: `GET /api/v1/backtesting/klines` plus `GET /api/v1/backtesting/funding` to replay fires with next-open entries, fees and funding. Compare against matched random entries (the null hypothesis)
- **Execution**: on Hyperliquid, pull `GET /api/v1/hyperliquid/candles` for the perp's own bars. Fire-bar liquidity is thin on alts, so use limit orders near the open

## Related

- [[squeeze-momentum-indicator]]: the signal
- [[volatility-breakout]]: NR7 and BB-squeeze sibling strategy
- [[bollinger-bands]], [[keltner-channels]]: the compression components
- [[volatility-clustering]]: the mechanism
- [[chandelier-exit]]: the trailing exit
- [[tradingview-community-scripts]], [[external-strategy-sources]]: where the idea came from

## Sources

- LazyBear, "Squeeze Momentum Indicator [LazyBear]", TradingView, 2014-07-04. PineIndicators and 03.freeman, community strategy wrappers (Source: [[tradingview-community-scripts]])
