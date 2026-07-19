---
title: "Multiple Timeframe Analysis"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [technical-analysis, indicators, day-trading, methodology]
aliases: ["Multiple Timeframe Analysis", "Multi-Timeframe Analysis", "MTF Analysis", "Triple Screen", "Top-Down Analysis"]
domain: [indicators]
prerequisites: ["[[indicators-ta-primer]]", "[[trend-following]]"]
difficulty: intermediate
related: ["[[indicators-ta-primer]]", "[[john-murphy]]", "[[technical-analysis-of-the-financial-markets]]", "[[trend-following]]", "[[rsi]]", "[[macd]]", "[[moving-averages]]", "[[support-resistance]]", "[[dow-theory]]", "[[bar-resolution-selection]]", "[[microstructure-noise-low-timeframe]]", "[[intrabar-fill-modeling]]", "[[lookahead-bias]]", "[[crypto-perp-backtesting-pitfalls]]", "[[overfitting]]", "[[hyperliquid]]"]
---

Multiple timeframe analysis is the practice of examining the same market across two or more timeframes to align trend direction, identify signals, and time entries with greater precision. [[john-murphy]] emphasizes this as one of the most important principles in [[indicators-ta-primer|technical analysis]]: a signal on a daily chart means more when confirmed by the weekly chart, and a signal on a weekly chart that contradicts the daily should give a trader pause. The concept is rooted in [[dow-theory]], which identified three simultaneous trends (primary, secondary, minor) operating across different time horizons. (Source: [[book-technical-analysis-of-the-financial-markets]])

## Murphy's Three-Timeframe Framework

Murphy recommends analyzing at least three timeframes before taking any trade. Each timeframe serves a distinct purpose:

### 1. Higher Timeframe -- Trend Identification

The higher timeframe establishes the dominant trend direction. This is the primary trend in Dow Theory terms -- the tide. A trader should never take a position that opposes the higher timeframe trend.

- **Swing traders**: Weekly chart
- **Day traders**: Daily chart
- **Scalpers**: 4H or 1H chart

Tools used: [[moving-averages]] (50-period and 200-period), trendlines, [[macd]] direction.

### 2. Middle Timeframe -- Signal Generation

The middle timeframe is where entry and exit signals are generated. This is the trader's primary working chart. Signals include [[moving-averages|moving average]] crossovers, [[chart-patterns|pattern]] breakouts, oscillator signals ([[rsi]], [[stochastic]]), and [[support-resistance|support/resistance]] breaks.

- **Swing traders**: Daily chart
- **Day traders**: 4H or 1H chart
- **Scalpers**: 15m or 5m chart

The rule: only take signals on the middle timeframe that align with the higher timeframe trend. A daily buy signal is only actionable if the weekly trend is up.

### 3. Lower Timeframe -- Entry Timing

The lower timeframe is used to fine-tune the exact entry point for better risk/reward. After the middle timeframe generates a signal in the direction of the higher timeframe trend, drop down to the lower timeframe to find the optimal entry -- typically a pullback to [[support-resistance|support]], a micro-pattern breakout, or an oscillator turning from oversold.

- **Swing traders**: 4H or 1H chart
- **Day traders**: 15m or 5m chart
- **Scalpers**: 1m chart

This layered approach improves the risk/reward ratio by providing tighter entries while maintaining conviction from the larger trend context. (Source: [[book-technical-analysis-of-the-financial-markets]])

## Elder's Triple Screen

Alexander Elder formalized a closely related three-screen method in *Trading for a Living* (1993) that operationalizes the same principle with specific indicator rules:

- **Screen 1 (weekly)**: Identify the primary trend using a trend-following indicator. Elder recommends weekly [[macd]] histogram slope -- rising histogram = bullish tide, falling histogram = bearish tide.
- **Screen 2 (daily)**: Identify pullbacks against the weekly trend using an oscillator. When the weekly is bullish, look for daily [[rsi]] or [[stochastic]] to reach oversold levels (below 30). When the weekly is bearish, look for daily oscillators to reach overbought levels (above 70).
- **Screen 3 (intraday)**: Time the entry using a trailing buy stop (for longs) or trailing sell stop (for shorts). Set the stop at the high/low of the prior bar and adjust daily until triggered.

Elder's system is more prescriptive than Murphy's general framework but embodies the same principle: use the higher timeframe for direction, the middle for opportunity, and the lower for execution.

## Practical Rules

### Alignment Rule
Never take a long signal on the middle timeframe if the higher timeframe is in a downtrend, and never take a short signal if the higher timeframe is in an uptrend. Conflicting signals across timeframes mean no clear edge -- stay out.

### Timeframe Ratio
The higher timeframe should be approximately 4-6x the middle timeframe. This ensures the timeframes capture genuinely different trend scales rather than overlapping noise:

| Trading Style | Higher | Middle | Lower |
|--------------|--------|--------|-------|
| Position/Swing | Weekly | Daily | 4H |
| Short-term Swing | Daily | 4H | 1H |
| Day Trading | 4H | 1H | 15m |
| Scalping | 1H | 15m | 5m |

Using timeframes that are too close together (e.g., 30m and 15m) provides little additional information. Using timeframes that are too far apart (e.g., monthly and 5m) creates too much ambiguity in the middle.

### Weight Hierarchy
Higher timeframe signals always carry more weight than lower timeframe signals. A weekly trend reversal overrides any number of bullish daily signals. A daily breakdown is more significant than an hourly bounce.

### Conflicting Signals Protocol
When timeframes disagree:
- **Higher bullish, middle bearish**: Treat as a pullback within the larger uptrend. Wait for the middle timeframe to realign (oscillator reaches oversold, price reaches support).
- **Higher bearish, middle bullish**: Treat as a bear market rally. Do not initiate new longs. The middle timeframe bounce will likely fail.
- **All three disagree**: No edge. Stand aside.

### Decision Matrix

Collapsing the three timeframes into a single action grid. The higher timeframe (HTF) sets the *only* direction you may trade; the middle (MTF) decides whether to act *now*; the lower (LTF) refines the trigger and stop:

| HTF trend | MTF signal | Verdict | Action |
|-----------|------------|---------|--------|
| Up | Bullish (pullback ending) | Aligned long | Drop to LTF; enter long on trigger |
| Up | Bearish | Pullback within uptrend | Wait for MTF oscillator to reset oversold; then look long |
| Up | Neutral / chop | No clean setup | Stand aside; monitor |
| Down | Bearish (bounce ending) | Aligned short | Drop to LTF; enter short on trigger |
| Down | Bullish | Bear-market rally | Do not initiate longs; fade only with caution |
| Down | Neutral / chop | No clean setup | Stand aside |
| Sideways | Either | No dominant tide | Range-trade extremes only, or stand aside |

The asymmetry is deliberate: **the HTF can veto an MTF signal, but an MTF signal can never override the HTF.** This is the [[#Weight Hierarchy|weight hierarchy]] expressed as a lookup table.

## Worked Example — Swing-Trade Equity Setup

*(Levels are illustrative, chosen to show the decision flow, not a live trade.)*

A swing trader runs a **Weekly → Daily → 4H** stack on a large-cap stock.

1. **Weekly (HTF — direction):** price is above a rising 200-week [[moving-averages|moving average]] and the weekly [[macd]] histogram is rising. **Tide: up. Long-only.**
2. **Daily (MTF — opportunity):** the stock pulls back three sessions into a [[support-resistance|support]] shelf and daily [[rsi]] dips to 32 (oversold). This is a *bullish pullback ending within an uptrend* — the "Up / pullback ending" row of the matrix. **Setup is live.**
3. **4H (LTF — timing):** the trader waits for the 4H to print a higher low and reclaim the prior 4H swing high before entering. The **stop sits below the daily support shelf**, not below a tight 4H wick, so normal noise does not stop it out. The reward target is the prior weekly swing high.

Had the weekly been *down*, the identical daily oversold RSI would have been read as a [[#Conflicting Signals Protocol|bear-market rally]] — no long. Same signal, opposite verdict, decided entirely by the HTF. This is the whole point of MTF analysis: the lower timeframe never gets to argue with the tide.

## Common Combinations by Market

### Equities (Swing Trading)
Weekly chart for trend direction (200-week MA, weekly MACD), daily chart for signals (daily RSI divergence, pattern breakouts), 4H chart for entry timing.

### Forex (Day Trading)
Daily chart for bias (is the pair trending up or down on the daily?), 4H for signal (flag breakout, MA crossover), 1H for entry (pullback to 1H support + RSI oversold).

### Crypto (Swing Trading)
Weekly for macro trend, daily for signals, 4H for entries. Crypto's 24/7 nature and higher volatility mean the lower timeframe often provides more precise entries than in traditional markets.

### Crypto Perpetuals (Intraday / Low-Timeframe)
For low-timeframe perp trading on a venue like [[hyperliquid|Hyperliquid]], a typical stack is **1h → 15m → 5m/1m**: the 1h sets directional bias and macro levels, the 15m locates the pullback and the swing low to anchor a stop, and the 5m/1m delivers the entry trigger. A worked long: 1h in an uptrend above a rising 50-MA (bias: long only) → price pulls back to a 15m support shelf and forms a swing low → on the 5m, price reclaims a short-term level and breaks the prior 5m swing high, **enter long with the stop below the 15m swing low** rather than below a tight 1m wick.

Because crypto trades **24/7**, the higher-timeframe context never resets at a session close: there is no overnight gap, opening auction, or daily settlement to flush positioning, so the 1h trend is continuous across the day. This makes HTF bias more persistent but removes the natural session boundary to reset risk against — traders impose their own (a rolling 24h anchor or a [[vwap-trading|session VWAP]] reset). The lower the entry resolution, the more the [[microstructure-noise-low-timeframe|bid-ask bounce]] dominates, which is precisely why MTF anchoring helps; see [[bar-resolution-selection]] for choosing the rungs.

## Multi-Timeframe Analysis in Systematic Backtests — the Look-Ahead Trap

The single most damaging pitfall when *coding* MTF logic is [[lookahead-bias|look-ahead bias]] — referencing a higher-timeframe bar that has **not yet closed** at the moment of the lower-timeframe decision.

A 1h bar only becomes *known information* at the **top of the next hour**. If a 5m signal fires at 10:35 and the code reads the 10:00–11:00 bar's **close**, it has leaked a value that will not exist until 11:00 — a 25-minute peek into the future. In a backtest this masquerades as a brilliant edge; live, it evaporates. It is one of the most common ways crypto-perp MTF backtests inflate results (see [[crypto-perp-backtesting-pitfalls]]).

**The fix — an as-of join on closed bars only.** Forward-fill every higher-timeframe feature using only bars whose *close* timestamp is strictly before the current lower-timeframe timestamp:

```
for each 5m bar at time t:
    htf_bias = last 1h bar with close_time < t   # NOT the in-progress hour
    # at 10:35, htf_bias comes from the 09:00-10:00 bar (closed at 10:00),
    #           never from the still-forming 10:00-11:00 bar
```

In pandas this is `merge_asof(..., direction="backward")` keyed on the **bar-close** timestamp. Aligning on bar-*open* is itself a subtle leak: a bar labelled 10:00 is not fully known until 11:00. Always align HTF features to the moment they could actually be observed. Resolving stop/take-profit sequencing inside the entry bar is a related problem — see [[intrabar-fill-modeling]]. Over-optimising the timeframe ratio (grid-searching for a "best" combination like 3m/11m/47m) is a textbook form of [[overfitting]]; choose round, economically sensible ratios *a priori*.

## Why Multiple Timeframes Work

The effectiveness of multiple timeframe analysis derives from a structural feature of markets: different participants operate on different timescales. Institutional portfolio managers, pension funds, and central banks drive weekly and monthly trends. Active fund managers and swing traders drive daily trends. Day traders and algorithmic systems drive intraday movements.

By aligning a trade with the higher timeframe, a trader positions alongside the dominant capital flow. The middle and lower timeframes are then used to enter that flow at the most favorable price. This is fundamentally different from trying to trade a 15-minute chart signal that opposes the weekly trend -- a trade that pits a small amount of capital against the dominant institutional flow.

## Common Pitfalls

- **Redundant timeframes.** Stacking 30m / 15m (a ratio near 2x) adds screen clutter without new information. Keep the HTF roughly 4–6x the MTF — see the [[#Timeframe Ratio|ratio rule]].
- **Letting the LTF override the HTF.** The most common discretionary error is talking oneself into a counter-tide trade because "the 5m looks great." The matrix exists precisely to prevent this.
- **Grid-searching the "best" ratio.** Optimising a timeframe combination (e.g. 3m/11m/47m) on historical data is textbook [[overfitting]]; choose round, economically sensible rungs *a priori*.
- **Look-ahead leakage in code.** Referencing a not-yet-closed HTF bar is the dominant systematic-backtest error — see the [[#Multi-Timeframe Analysis in Systematic Backtests — the Look-Ahead Trap|look-ahead trap]] and [[lookahead-bias]].
- **Analysis paralysis.** Adding a fourth or fifth timeframe usually produces contradictions, not clarity. Three is the canonical count for a reason.
- **Forgetting the markets differ.** A 24/7 crypto market has no session reset, so HTF context persists differently than in equities/FX — see the [[#Crypto Perpetuals (Intraday / Low-Timeframe)|crypto-perp]] note.

## Limitations

- Requires monitoring multiple charts, which increases complexity and screen time
- Timeframe selection is somewhat arbitrary -- there is no single "correct" combination
- In choppy, range-bound markets, all timeframes may give conflicting signals for extended periods
- Higher timeframe signals are slower, meaning entries based on weekly confirmation will always miss the first portion of a move
- Does not eliminate false signals -- it filters them, but aligned signals can still fail

## Related

- [[dow-theory]] -- the origin of the three-trend hierarchy that underlies MTF analysis
- [[john-murphy]] -- emphasizes multiple timeframe analysis as a core TA principle
- [[technical-analysis-of-the-financial-markets]] -- Claim #12: multiple timeframe analysis provides better context
- [[trend-following]] -- the strategy most enhanced by timeframe alignment
- [[rsi]] -- commonly used as the middle-timeframe oscillator
- [[macd]] -- Elder's preferred higher-timeframe trend indicator
- [[moving-averages]] -- the most common tool for identifying trend on higher timeframes
- [[support-resistance]] -- key levels used for lower-timeframe entry timing
- [[intermarket-analysis]] -- extends the confirmation principle across asset classes
- [[bar-resolution-selection]] -- choosing which resolutions to stack (1m/3m/5m/15m)
- [[microstructure-noise-low-timeframe]] -- why the lowest rung is the noisiest
- [[intrabar-fill-modeling]] -- resolving entry/exit sequencing inside the trigger bar
- [[crypto-perp-backtesting-pitfalls]] -- the alignment trap in a crypto-perp context

## Sources

- (Source: [[book-technical-analysis-of-the-financial-markets]]) -- Claim #12: multiple timeframe analysis provides better context than single-timeframe trading
- Murphy, J. (1999), *Technical Analysis of the Financial Markets*, New York Institute of Finance — the three-timeframe principle and Dow Theory trend hierarchy
- Elder, A. (1993), *Trading for a Living*, Wiley — the Triple Screen trading system (weekly trend, daily oscillator, intraday entry)
