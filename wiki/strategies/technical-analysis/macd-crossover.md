---
title: MACD Crossover Strategy
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: review
tags:
  - momentum
  - macd
  - trend-following
  - crossover
  - gerald-appel
  - crypto
strategy_type: momentum
timeframe: swing
markets:
  - crypto
  - forex
complexity: beginner
backtest_status: untested
related:
  - "[[rsi-divergence]]"
  - "[[rate-of-change]]"
  - "[[moving-average-crossover]]"
  - "[[trend-following]]"
  - "[[perpetual-futures]]"
  - "[[funding-rate]]"

# Edge characterization
edge_source: [behavioral, analytical]
edge_mechanism: "Behavioral: MACD crossovers identify early-stage momentum shifts when the crowd is still committed to the prior trend, capturing the lag between price reality and participant position adjustment. Analytical: the signal-line smoothing filters noise and confirms that the momentum shift is sustained rather than a single-candle spike. In crypto, momentum persistence is amplified by leveraged perp funding dynamics — a regime of strongly positive funding perpetuates upside momentum; negative funding perpetuates downside — making MACD crossovers in the direction of the funding trend higher-probability setups."

# Data and infrastructure requirements
data_required: [ohlcv, funding-rates]
min_capital_usd: 1000
capacity_usd: 500000000
crowding_risk: low

# Performance expectations
expected_sharpe: 0.3
expected_max_drawdown: 0.30
breakeven_cost_bps: 15

# Kill criteria
kill_criteria: |
  - false-signal rate exceeds 65% over rolling 20 signals → add trend filter (200 EMA) or shift to longer timeframe
  - rolling 90-day P&L negative with > 15 completed trades → pause; market is range-bound or parameters need revision
  - funding rate > 0.1% per 8h and MACD signals short → skip short signals; funding strongly penalizes shorts
gates:
  - id: bullish_cross_below_zero
    role: entry
    rule: "Long when MACD(12,26,9) crosses above its signal line while both are below zero, on closed daily candles"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
    note: "MACD = EMA12 - EMA26 of closes, signal = EMA9 of MACD; 200 bars lets the EMAs settle. Drop the forming bar named by forming_bar_timestamp. The page's example uses Binance spot (/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d)."
  - id: bearish_cross_above_zero
    role: entry
    rule: "Short when MACD crosses below its signal line while both are above zero"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
  - id: histogram_expanding
    role: entry
    rule: "Confirm with the MACD histogram expanding in the trade's direction"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    note: "Histogram = MACD - signal; expanding = its absolute value growing bar over bar on the trade's side."
  - id: trend_filter_200_ema
    role: filter
    rule: "Take bullish crossovers only in uptrends and bearish ones only in downtrends, using a moving average such as the 200 EMA on the higher timeframe"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=400
    field: candles[].close
    note: "The rule leaves the average and timeframe open ('e.g. 200 EMA on the higher timeframe'); the AI workflow takes the 200 EMA from the same daily series. The served 200-day SMA is ma.above_200 on /api/v1/indicators/technical/{symbol}."
  - id: funding_short_veto
    role: filter
    rule: "Skip a short signal when funding is above 0.1% per 8 hours"
    runnable: true
    endpoint: /api/v1/derivatives/funding-rates?coin={coin}
    field: binance.current_rate
    replay: /api/v1/backtesting/funding?symbol={coin}&start={start}
    replay_field: data[].funding_rate
    note: "Binance funding is per 8 hours: skip when current_rate is above 0.001. The replay is Hyperliquid hourly funding; multiply by 8."
  - id: funding_alignment
    role: filter
    rule: "Check funding before every entry: crossovers in the direction of the funding trend are higher-probability; a long against deeply negative funding fights structural short pressure"
    runnable: partial
    endpoint: /api/v1/derivatives/funding-rates?coin={coin}
    field: binance.current_rate
    note: "Only the 0.1% short veto has a number; 'deeply negative' and the funding trend are left to the desk."
  - id: trend_regime_only
    role: filter
    rule: "Take crossovers only in strong_trend_bull or strong_trend_bear; stand down in choppy_high_vol"
    runnable: true
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's AI-agent workflow. The coin's own read is /api/v1/quant/coins/{symbol}."
  - id: enough_history
    role: universe
    rule: "Respect insufficient-history flags on recently listed perps before trusting a 26-period EMA"
    runnable: true
    endpoint: /api/v1/quant/coins/{coin}
    field: meta.insufficient_history
  - id: signal_line_exit
    role: exit
    rule: "Close when MACD crosses its signal line against the trade"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
  - id: zero_line_exit
    role: exit
    rule: "Exit immediately if the MACD line crosses zero against the position"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
  - id: swing_stop
    role: stop
    rule: "Stop below the most recent swing low for longs (above the recent swing high for shorts)"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30
    field: candles[].low
    note: "The page does not define a swing low (a pivot with N higher lows either side is the usual reading)."
  - id: target_2r_or_trail
    role: exit
    rule: "Take profit at 2:1 reward-to-risk, or trail the stop using the signal line"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: kill_criteria
    role: stop
    rule: "If more than 65% of the last 20 signals fail to move 1R within 10 bars, add the 200 EMA filter or lengthen the timeframe; pause on a negative rolling 90-day P&L over more than 15 trades"
    runnable: true
    input: position
---

# MACD Crossover Strategy

## Edge source

**Behavioral (primary)**: MACD crossovers identify early-stage momentum shifts before the crowd has adjusted its positioning. When the fast EMA crosses the slow EMA, most participants are still positioned for the prior trend and face the decision to hold or close; the crossover anticipates the forced position adjustment that comes as the new trend is confirmed. The signal line (9-period EMA of the MACD) smooths out noise and confirms that the shift is multi-day, not a single-bar spike.

**Analytical (secondary)**: In crypto, momentum is amplified by perp funding dynamics. Sustained positive funding (longs paying shorts) reflects levered positioning in the direction of the trend; this funding acts as a headwind to reversal and a tailwind to continuation. A MACD crossover aligned with the funding trend is a higher-probability continuation signal than a crossover against it. Conversely, a bearish MACD crossover during strongly positive funding is lower-probability because the funding creates an economic incentive for buyers to stay long.

**Note on edge decay**: MACD's default parameters (12, 26, 9) are universally known and widely used; any raw MACD edge is heavily arbitraged in liquid BTC/ETH markets. The residual edge in crypto comes from: (1) applying MACD on lower-traded assets or timeframes where fewer algorithms operate; (2) combining with trend and funding filters; (3) using the histogram as a momentum confirmation tool rather than the crossover itself.

## Null hypothesis

Under the null, MACD crossovers are lagging indicators that signal past momentum, not future continuation. Because the signal fires after the move has already begun, a random-walk price series produces a significant number of valid-looking MACD crossovers that fail because the underlying move was noise. The counter-argument is that momentum persistence is real in crypto (particularly in trending perp markets where funding amplifies trend continuation) and that the combination of MACD + trend filter + funding direction can reject the null over multi-year crypto data. A program that cannot demonstrate positive P&L over at least 2–3 years across multiple regimes cannot reject the null.

## Overview

The MACD (Moving Average Convergence Divergence) crossover strategy trades signals generated when the MACD line crosses the signal line. Developed by **Gerald Appel** in the late 1970s, the MACD remains one of the most widely used [[momentum]] indicators in [[technical-analysis]]. The strategy exploits shifts in short-term momentum relative to longer-term momentum, capturing trend transitions early. The [[macd-histogram]] confirms momentum strength and direction, providing additional conviction for entries.

## Rules

### Entry Rules
1. **Bullish Entry:** Go long when the MACD line crosses **above** the signal line while both lines are **below the zero line**. This signals momentum shifting from bearish to bullish early in a potential uptrend.
2. **Bearish Entry:** Go short when the MACD line crosses **below** the signal line while both lines are **above the zero line**. This captures the transition from bullish to bearish momentum.
3. **Confirmation:** The [[macd-histogram]] should be expanding (bars growing) in the direction of the trade to confirm momentum is building, not fading.
4. **Trend Filter:** Use a [[moving-average]] (e.g., 200 EMA) on the higher timeframe to ensure trades align with the dominant trend direction. Only take bullish crossovers in uptrends and bearish crossovers in downtrends.

### Exit Rules
1. **Signal Exit:** Close the position when the MACD line crosses back in the opposite direction of the trade.
2. **Zero-Line Exit:** If the MACD line crosses the zero line against your position, exit immediately as the trend has shifted.
3. **Stop Loss:** Place stops below the most recent [[swing-low]] for longs or above the recent [[swing-high]] for shorts.
4. **Profit Target:** Use a 2:1 reward-to-risk ratio, or trail the stop using the signal line as a dynamic exit.

## Indicators Used

| Indicator | Default Settings | Purpose |
|-----------|-----------------|---------|
| [[macd]] | 12, 26, 9 (EMA) | Primary signal generation |
| [[macd-histogram]] | Derived from MACD | Momentum strength confirmation |
| [[moving-average]] (200 EMA) | 200-period | Trend direction filter |
| [[volume]] | N/A | Confirm conviction on crossover |

## Example Trade

**Setup:** BTC/USD daily chart. Price is trading above the 200 EMA (uptrend confirmed). The MACD line is at -150 and the signal line is at -120, both below zero. The MACD histogram bars are shrinking (becoming less negative).

**Entry:** MACD line crosses above the signal line at price $42,500. Histogram turns positive. Enter long.

**Management:** Stop loss placed below the recent swing low at $40,800. Risk = $1,700 per unit. Target set at $45,900 (2:1 R/R).

**Exit:** Price reaches target at $45,900. Alternative exit: MACD line crosses back below signal line at $44,600, closing the trade for a partial profit.

## Performance Characteristics

- **Win Rate:** Typically 40-55% depending on market conditions and filters applied
- **Best Conditions:** Trending markets with clear directional moves
- **Worst Conditions:** Choppy, range-bound markets produce frequent whipsaws
- **Average Holding Period:** 5-20 days on daily charts (swing timeframe)
- **Frequency:** 2-4 signals per month per instrument on daily charts

## Advantages

- Simple to learn and execute, ideal for beginners entering [[technical-analysis]]
- Works across all liquid markets (stocks, [[crypto]], [[forex]])
- Combines trend and momentum in a single indicator
- The histogram provides early warning of crossover signals
- Widely supported by every charting platform

## Disadvantages

- **Lagging indicator** -- crossovers occur after the move has already begun
- Generates many [[false-signals]] in sideways or choppy markets
- Default settings (12, 26, 9) may not suit all instruments or timeframes
- Can miss fast-moving breakouts due to signal delay
- Should not be used in isolation; always combine with [[support-resistance]] or [[volume-analysis]]

## Capacity limits

MACD-based momentum trading in BTC/ETH perps has essentially no capacity constraint at the fund level — perp markets are multi-billion in open interest. The constraint is **signal frequency**: on a daily chart, 2–4 signals per month per instrument means a systematic program needs many instruments to generate adequate turnover. Altcoin perps add signal diversity but introduce correlation (in risk-off, all alts correlate to BTC beta) and liquidity risk on exits.

## What kills this strategy

1. **Range-bound crypto markets**: extended consolidations produce a high density of false MACD crossovers with no follow-through; without a trend filter, the strategy churns through small losses.
2. **Funding headwinds**: if MACD signals a long while funding is deeply negative (shorts earning premium), the lagger's trade fights against structural short pressure; funding should be checked before every entry.
3. **Overnight gaps and cascade moves**: crypto's 24/7 nature means a MACD crossover on a daily chart fires at the daily close; the actual market has already moved 8–12 hours past the signal. Fast-moving breakouts triggered by macro events (FOMC, CPI, on-chain liquidations) can gap through the signal price before entry.
4. **Widely programmed default settings**: in BTC/ETH, the (12, 26, 9) MACD is programmed into every retail bot; its signals are anticipated and faded by larger players. Parameter customization per timeframe/instrument is required for any residual edge.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- False-signal rate (price fails to move > 1R in the signal direction within 10 bars) exceeds 65% over rolling 20 signals → add 200-period EMA trend filter or shift to a longer timeframe.
- Rolling 90-day P&L negative with > 15 completed trades → pause; re-examine whether a trend filter or funding overlay is needed.
- Any day where funding rate > 0.1% per 8h and MACD signals short → skip that short signal; funding strongly penalizes perp shorts and reduces edge.

## Getting the Data (CryptoDataAPI)

Everything the system needs is OHLCV-based with a funding-rate overlay for crypto perp alignment.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` — daily OHLCV for MACD calculation
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding rate (directional bias filter)

**Historical data:**
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — history for parameter optimization and backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-data]] and [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` → compute MACD(12,26,9) on closed daily candles; the 200-EMA trend filter comes from the same series (or `GET /api/v1/market-data/btc-price-history`, which ships the 200D MA pre-computed for BTC).
- **Funding filter** — `GET /api/v1/derivatives/funding-rates?coin=BTC` before every entry; skip shorts when funding > 0.1%/8h per the kill criteria.
- **Regime gate** — `GET /api/v1/quant/market` — take crossovers only in `strong_trend_bull`/`strong_trend_bear`; stand down in `choppy_high_vol`, where whipsaws dominate.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) for parameter sweeps; pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time regime states to avoid [[lookahead-bias]].
- **Tips** — batch the universe via `GET /api/v1/quant/coins/risk` rather than looping per symbol; respect `insufficient_history` flags on recently listed perps before trusting a 26-period EMA.

## Related

- [[rsi-divergence]] — oscillator-based momentum signal with divergence detection
- [[rate-of-change]] — simpler, un-smoothed momentum companion
- [[moving-average-crossover]] — the raw MA version of the same trend-shift signal
- [[trend-following]] — the broader systematic trend philosophy
- [[perpetual-futures]] — the primary crypto instrument for this strategy
- [[funding-rate]] — the crypto momentum amplifier and directional filter
