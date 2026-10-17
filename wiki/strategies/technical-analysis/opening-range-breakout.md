---
title: Opening Range Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: review
tags:
  - breakout
  - opening-range
  - intraday
  - toby-crabel
  - orb
  - crypto
strategy_type: breakout
timeframe: intraday
markets:
  - crypto
  - futures
complexity: intermediate
backtest_status: untested
related:
  - "[[volatility-breakout]]"
  - "[[support-resistance-breakout]]"
  - "[[vwap-trading]]"
  - "[[scalping]]"
  - "[[perpetual-futures]]"
  - "[[funding-rate]]"

# Edge characterization
edge_source: [behavioral, structural]
edge_mechanism: "Behavioral: participants psychologically anchor to the high/low of an early reference window; a break of that window triggers systematic stops and breakout-chasing entries, producing a sustained directional move. Structural: in crypto, the 08:00 UTC Deribit settlement creates a genuine daily 'pseudo-open' concentrating institutional flow into the post-settle window; additionally, FOMC/CPI macro prints create identifiable US-session opens that concentrate flow exactly as a traditional equity open would."

# Data and infrastructure requirements
data_required: [ohlcv, funding-rates, liquidations]
min_capital_usd: 1000
capacity_usd: 100000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.4
expected_max_drawdown: 0.25
breakeven_cost_bps: 20

# Kill criteria
kill_criteria: |
  - false-breakout rate > 60% over rolling 20 signals → add volume filter or widen reference window
  - rolling 30-day P&L negative → pause; crypto's 24/7 market may not produce a statistically reliable "open"
  - vol-shock regime or active liquidation cascade → no new ORB entries; the cascade dominates any ORB range
gates:
  - id: opening_range_high
    role: entry
    rule: "Opening-range high = the highest 1m high from 08:00 to 08:30 UTC (08:15 for the aggressive 15-minute range)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&start={start}&end={end}
    field: candles[].high
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}
    replay_field: klines[].h
    note: "Anchored at 08:00 UTC, the page's own crypto open (the Deribit settlement). On FOMC/CPI days the page moves it to the US cash open (us_macro_day_window). 00:00 UTC, the daily candle open, is the other common anchor; the anchor is the desk's choice. Live: start = 08:00, end = 08:29 UTC (end is inclusive). Replay: end = 08:30 UTC (exclusive). Hyperliquid serves only about 4 days of 1m bars; coverage.local_first says how far the archive reaches."
  - id: opening_range_low
    role: entry
    rule: "Opening-range low = the lowest 1m low from 08:00 to 08:30 UTC (08:15 for the aggressive range)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&start={start}&end={end}
    field: candles[].low
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}
    replay_field: klines[].l
    note: "Same window and anchor as opening_range_high."
  - id: us_macro_day_window
    role: entry
    rule: "On an FOMC or CPI day, take the range from the US cash open instead: 14:30-15:00 UTC per the page"
    runnable: true
    endpoint: /api/v1/event/calendar?type=macro_print&window_days=1
    field: items[].macro_class
    note: "A row with days_until 0 and macro_class FOMC or CPI makes today a macro day. The page's 14:30 UTC is the NYSE open in US winter; while the US is on daylight time the open is 13:30 UTC. The calendar is forward-only, so a backtest needs the desk's list of past print dates."
  - id: weekend_skip
    role: filter
    rule: "Skip Saturday and Sunday (UTC) sessions"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&start={start}&end={end}
    field: candles[].timestamp
    note: "Read the UTC weekday from the first opening-range bar's timestamp (ms). The page allows 'stricter filters' instead of a skip, but its agent workflow skips weekends."
  - id: range_window_volume
    role: filter
    rule: "The range only counts when 08:00-08:30 UTC volume exceeds the trailing 24h average for a 30-minute span (24h volume / 48)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&start={start}
    field: candles[].volume
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}&limit=1500
    replay_field: klines[].v
    note: "start = 24 hours before 08:30 UTC. The edge section asks for 'meaningfully above'; 1x is the floor the page's agent workflow uses, and the desk may raise it."
  - id: range_width_min
    role: filter
    rule: "Skip when the opening-range width (high - low) is below 0.3x the daily ATR(14)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30&atr=14
    field: candles[].atr
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}&atr=14
    replay_field: candles[].atr
    note: "Use the last closed daily bar's atr; drop the forming bar named by forming_bar_timestamp."
  - id: range_not_manipulated
    role: filter
    rule: "Skip when the range high or low sits at an obviously manipulated pre-settlement level"
    runnable: false
    note: "No Deribit settlement or index print is served, and spotting a pinned level is a chart judgement."
  - id: long_breakout
    role: entry
    rule: "Long when price trades above the opening-range high plus a 1-2 tick buffer, after 08:30 UTC (either this or short_breakdown)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&limit=3
    field: candles[].high
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}
    replay_field: klines[].h
    note: "A resting buy-stop at the level does the same job. Tick size is the coin's Hyperliquid price precision."
  - id: short_breakdown
    role: entry
    rule: "Short when price trades below the opening-range low minus a 1-2 tick buffer, after 08:30 UTC (either this or long_breakout)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&limit=3
    field: candles[].low
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}
    replay_field: klines[].l
  - id: breakout_volume
    role: entry
    rule: "The breakout 1m bar's volume is above the trailing 24h average 1m volume (the page's 24h hourly average, per minute)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1m&start={start}
    field: candles[].volume
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&start={start}&end={end}&limit=1500
    replay_field: klines[].v
    note: "start = 24 hours before the breakout bar; the baseline is the mean of the bars before it. The kill criteria raise this to 2x when false breakouts exceed 60%."
  - id: gap_up_long_only
    role: filter
    rule: "When the 08:00 UTC price is more than 1% above the prior daily close, take only the long breakout"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=2
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Crypto has no overnight gap. Our reading: the prior close is the last completed daily bar (closed 00:00 UTC), compared with the first opening-range bar's open. The 1% threshold is the equity version's."
  - id: gap_down_short_only
    role: filter
    rule: "When the 08:00 UTC price is more than 1% below the prior daily close, take only the short breakdown"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=2
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Same reading of the prior close as gap_up_long_only."
  - id: funding_long_bias
    role: filter
    rule: "Take the long breakout only when current funding is positive (above 0)"
    runnable: true
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=1
    field: current_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1h&start={start}
    replay_field: data[].funding_rate_mean
    note: "The page's crypto adaptation replaces the VWAP bias with the funding sign."
  - id: funding_short_bias
    role: filter
    rule: "Take the short breakdown only when current funding is negative (below 0)"
    runnable: true
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=1
    field: current_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1h&start={start}
    replay_field: data[].funding_rate_mean
  - id: vol_shock_skip
    role: filter
    rule: "No new entries while the volatility regime score is above 75"
    runnable: true
    endpoint: /api/v1/volatility/regime/score
    field: composite_score
    note: "A market-wide 0-100 composite. The coin's own label is regime on /api/v1/volatility/regime/{symbol} (vol_shock). No history of the composite is served for replay."
  - id: cascade_skip
    role: filter
    rule: "No new entries while a liquidation cascade is running through the reference window"
    runnable: partial
    endpoint: /api/v1/backtesting/hl-liquidation-bars?coin={coin}&interval=5m&start={start}
    field: data[].total_usd
    note: "Hyperliquid's own liquidation tape; bars with no liquidations are omitted. The page sets no cascade threshold. One reading is a 5m bar at 3x or more the trailing-24h mean (start = 24h ago, mean = sum / 288), as post-liquidation-rebound uses; the cutoff is the desk's."
  - id: one_trade_per_day
    role: entry
    rule: "One trade per session: after the first breakout triggers, do not re-enter that day, even if stopped out"
    runnable: true
    input: position
  - id: target_range_multiple
    role: exit
    rule: "Take profit 1.5x the opening-range width beyond the entry fill, 2x at most (either this or target_daily_atr)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
    note: "Width = opening_range_high - opening_range_low."
  - id: target_daily_atr
    role: exit
    rule: "Take profit 1x the daily ATR(14) beyond the entry fill (either this or target_range_multiple)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30&atr=14
    field: candles[].atr
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}&atr=14
    replay_field: candles[].atr
    note: "Use the last closed daily bar's atr."
  - id: time_exit
    role: exit
    rule: "Close 4-6 hours after the breakout entry, and always before the next 08:00 UTC settlement"
    runnable: true
    input: position
    note: "This replaces the equity version's 'close by 15:30', following the page's crypto adaptation."
  - id: stop_opposite_side
    role: stop
    rule: "Stop at the opposite side of the opening range: a long exits below the range low, a short above the range high"
    runnable: true
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
    note: "Levels from opening_range_high and opening_range_low. Hyperliquid stop orders trigger on the mark price."
  - id: trail_to_breakeven
    role: stop
    rule: "Once price has moved 1x the opening-range width in favour, move the stop to the entry price"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: trail_half_profit
    role: stop
    rule: "After the breakeven move, trail the stop to lock in 50% of the peak open profit"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: atr_trailing_stop
    role: stop
    rule: "Crypto adaptation: use an ATR trailing stop in place of the equity time exit"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30&atr=14
    field: candles[].atr
    note: "The page names neither the ATR multiple nor its timeframe. The daily ATR(14) is the only ATR the page uses; the multiple is the desk's."
---

# Opening Range Breakout Strategy

## Edge source

**Behavioral (primary)**: Participants psychologically anchor to the high and low printed in an early reference window. Stops cluster around these levels because traders who entered during the reference window place protective stops just outside it. When the boundary breaks with conviction, the cascade of triggered stops plus breakout-chasing entries from participants waiting for a "confirmed direction" creates a sustained directional move. This clustering dynamic is consistent across session types and markets.

**Structural (crypto adaptation)**: Crypto trades 24/7 with no traditional market open. However, there are two identifiable "pseudo-open" windows where institutional order flow concentrates:
1. **08:00 UTC Deribit settlement window** — BTC/ETH options settle to the Deribit index at 08:00 UTC; institutional hedgers, vol desks, and market makers adjust positions around this time, creating genuine elevated flow and an identifiable intraday reference level analogous to an equity open.
2. **US session open (14:30–15:00 UTC)** — FOMC, CPI, and macro events with NYSE/CME relevance concentrate US-institutional crypto flow at the US market open; this is the most reliable "session open" for BTC/ETH on macro days.

For non-macro days, the ORB concept is weaker in crypto: without a genuine open, any 15-minute window can look like an ORB setup in hindsight. Validate that volume in the reference window is meaningfully above the 24-hour hourly average before treating it as an "opening range."

## Null hypothesis

On a 24/7 crypto market, the "opening range" is an arbitrary window with no mechanical reason to concentrate flow on non-event days. Under the null, an ORB constructed from a randomly chosen 15-minute window would perform no better than any other 15-minute window — meaning the strategy's apparent edge comes entirely from the specific windows that *do* concentrate flow (08:00 UTC, US macro events). The null is harder to reject for intraday crypto ORB than for equity ORBs, which benefit from a genuine market-open mechanism. Practitioners should only run ORB signals anchored to the 08:00 UTC Deribit settle or a defined macro event, not from an arbitrary "I'm logging in now" reference window.

## Overview

The Opening Range Breakout (ORB) strategy marks the **high and low of the first 15-30 minutes** of the trading session, then trades the breakout of that range. Popularized by **Toby Crabel** in his 1990 book *Day Trading with Short-Term Price Patterns and Opening Range Breakout*, this method capitalizes on the fact that the opening range often sets the tone for the entire session. The first 15-30 minutes concentrate institutional order flow, earnings reactions, and overnight gap resolution. A decisive break of this range with [[volume]] typically leads to a sustained intraday move. The strategy uses [[atr]] for profit targets and works best on high-volume days with clear directional bias.

## Rules

### Entry Rules
1. **Define the Opening Range:** Mark the high and low of the first 15 minutes (aggressive) or 30 minutes (conservative) after the market open.
2. **Long Entry:** Buy when price breaks **above** the opening range high by a small buffer (e.g., 1-2 ticks). Confirm with above-average [[volume]] on the breakout candle.
3. **Short Entry:** Sell when price breaks **below** the opening range low by 1-2 ticks with volume confirmation.
4. **Gap Filter:** On large gap-up days (>1% above prior close), favor long-side ORB trades. On large gap-down days, favor short-side. Avoid trading ORB into the gap (fading gaps requires a different approach).
5. **One Trade Per Day:** After the first breakout triggers, do not re-enter if stopped out. The cleanest ORB signals happen once.

### Exit Rules
1. **ATR Target:** Set the profit target at 1.5-2x the opening range width, or use 1x [[atr]](14) of the daily chart.
2. **Time Stop:** Close all positions by 15:30 (30 minutes before market close) regardless of profit/loss. The ORB is a morning momentum play.
3. **Stop Loss:** Place the stop at the **opposite side of the opening range**. If long above the high, stop is at the opening range low (and vice versa).
4. **Trailing Stop:** Once price moves 1x the opening range width in your favor, trail the stop to breakeven, then to 50% of open profit.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| Opening Range (High/Low) | First 15 or 30 min | Define breakout levels |
| [[volume]] | Intraday bars | Confirm breakout conviction |
| [[atr]] | 14-period (daily) | Target calculation and position sizing |
| [[vwap]] | Session | Directional bias confirmation |
| [[moving-average]] (9 EMA) | 5-min chart | Intraday trend direction |

## Example Trade

**Setup:** SPY opens at $520.50 after a strong overnight futures session. The first 15 minutes print a high of $521.30 and a low of $520.10. Opening range width = $1.20. Volume in the first 15 minutes is 30% above the 20-day average.

**Entry:** At 9:50 AM, SPY breaks above $521.30 on heavy volume. Enter long at $521.35. The [[vwap]] is at $520.80, confirming bullish bias (price above VWAP).

**Management:** Stop loss at $520.10 (opening range low). Risk = $1.25. Target = $521.35 + (1.5 x $1.20) = $523.15. R/R = 1.44:1.

**Exit:** SPY rallies to $523.15 by 11:30 AM. Target hit, close position. Alternatively, trail stop to breakeven at $521.35 once price passes $522.55 (1x range width).

## Performance Characteristics

- **Win Rate:** 50-60% on high-volume days; drops to 35-45% on low-volume/choppy days
- **Best Conditions:** High-volume days, earnings catalysts, gap days, trending market environments
- **Worst Conditions:** Low-volume holiday sessions, FOMC announcement days (pre-announcement chop), narrow opening ranges
- **Average Holding Period:** 30 minutes to 4 hours
- **Key Filter:** Opening range width matters -- very narrow ranges (<0.3x daily ATR) produce more false breakouts

## Advantages

- Clear, objective rules with defined entry, stop, and target levels
- Captures the most liquid and volatile part of the trading day
- Works well on stocks and [[futures]] with regular session opens
- Can be combined with [[vwap-trading]] for additional confluence
- Simple enough for intermediate traders; no complex indicators required

## Disadvantages

- Crypto's 24/7 nature means there is no true opening session; the strategy requires discipline to apply only to the 08:00 UTC Deribit settle window or a defined macro event
- False breakouts (fakeouts) are common, especially outside event windows
- Requires real-time monitoring and fast execution
- Stop loss can be wide if the opening range is large, requiring smaller position sizes
- Only provides 1 trade per session window -- not suitable for high-frequency traders
- Does not work well when the ORB window contains a scheduled macro event that causes pre-event chop

## Crypto-specific adaptation

**Original (equity) version**: marks the 15–30 minutes after NYSE open (9:30–10:00 ET), uses [[vwap]] as bias confirmation, exits by 15:30 ET (30 min before close).

**Crypto adaptation**:
- Use **08:00–08:30 UTC** as the reference window (Deribit settle concentrates flow); or **14:30–15:00 UTC** on US macro days (FOMC/CPI).
- Replace VWAP session bias with **[[funding-rate|perp funding]]** direction — positive funding = long bias on breakout; negative funding = short bias.
- No hard time-exit; close within the first 4–6 hours of the breakout (equivalent to US afternoon), or before the *next* 08:00 UTC settle.
- Volume baseline: compare the breakout candle to the 24-hour hourly average, not a session average.
- **No 15:30 ET close rule**: crypto has no close; use an ATR trailing stop instead of a time-exit.
- On weekends, the 08:00 UTC window exists but volume is thin — apply stricter filters or skip entirely.

*TradFi context (historical reference only)*: the original equity ORB (Toby Crabel, 1990; SPY/ES example above) is well-documented on NYSE/CME instruments and remains a foundational intraday strategy; the crypto adaptation preserves the mechanism but replaces the session-open anchor with crypto's nearest equivalent.

## Capacity limits

Intraday BTC/ETH perp ORB trades can comfortably scale to $5–50M per position. Off BTC/ETH and off the two reference windows, liquidity degrades quickly — alt perps on the 08:00 UTC window are workable to $500K–$2M.

## What kills this strategy

1. **No genuine open**: running ORB on arbitrary 15-minute windows in crypto produces noise; without a real flow-concentration event (Deribit settle or macro), the "range" has no behavioral anchor.
2. **Liquidation cascade during the reference window**: if a cascade fires during the 08:00 UTC window, the resulting range may be enormous and the breakout trade has too-wide a stop to be viable.
3. **Pre-settle manipulation**: large players sometimes drive BTC into a Deribit settlement range; the post-settle breakout can be a reversal of this manipulation, not a genuine directional move. Verify that the reference-window high/low is not settled at an obviously manipulated level.
4. **Funding penalty**: a short ORB trade in strongly positive-funding (annualized 30%+) costs meaningful carry for an intraday hold; the breakout move must exceed the funding drag to be worthwhile.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- False-breakout rate (price re-enters opening range within 3 candles) exceeds 60% over rolling 20 signals → add a volume filter (breakout candle > 2× 24h hourly average) or widen the reference window to 30 minutes.
- Rolling 30-day P&L negative → pause; the chosen reference window may not be concentrating sufficient flow. Verify the window is tied to 08:00 UTC or a macro event.
- Vol-shock regime (CryptoDataAPI vol-regime-score > 75) or active liquidation cascade → no new ORB entries for that session; the cascade signal dominates any range structure.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=50` — 15-minute OHLCV for reference-window identification
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (directional bias filter)
- `GET /api/v1/market-intelligence/liquidations` — cascade early warning
- `GET /api/v1/volatility/regime` — vol-regime filter (skip ORB in vol_shock regime)

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep archive for backtesting the 08:00 UTC window vs other windows

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=50"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=50` at 08:30 UTC to fix the 08:00-08:30 Deribit-settle reference range (or the 14:30-15:00 window on US macro days); require window volume above the 24h hourly average before the range counts.
- **Bias** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — positive funding arms the long-side ORB, negative the short side.
- **Regime gate** — `GET /api/v1/volatility/regime` + `GET /api/v1/market-intelligence/liquidations` — no entries in `vol_shock` or while a cascade is running through the reference window (the range it prints is untradeable).
- **Backtest** — `GET /api/v1/backtesting/klines`: 1m klines exist only since 2026-03-30, which is exactly what window-level ORB replays need — treat the deeper 1h archive (back to 2017-08) as coarse hour-of-day evidence, not ORB validation.
- **Tips** — `GET /api/v1/event/calendar` tells you in advance which days carry the macro prints that make the US-open variant fire; skip weekends, where the 08:00 UTC window rarely passes the volume filter.

## Related

- [[volatility-breakout]] — ATR-based breakout from contraction setups
- [[support-resistance-breakout]] — horizontal breakout with retest entries
- [[vwap-trading]] — session-anchored VWAP (equity session equivalent)
- [[scalping]] — the intraday fast-execution context
- [[perpetual-futures]] — primary crypto instrument for this strategy
- [[funding-rate]] — directional bias filter on perp positions
- [[deribit]] — 08:00 UTC settlement creates the crypto "pseudo-open"
