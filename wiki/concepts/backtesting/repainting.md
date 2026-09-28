---
title: "Repainting"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [backtesting, indicators, validation, methodology]
aliases: ["Repaint", "Repainting Indicator", "Non-Repainting"]
domain: [backtesting, technical-analysis]
prerequisites: ["[[lookahead-bias]]"]
difficulty: intermediate
related: ["[[lookahead-bias]]", "[[pine-script]]", "[[tradingview-platform]]", "[[external-strategy-sources]]", "[[overfitting-detection]]", "[[crypto-forward-testing]]", "[[cryptodataapi-backtesting]]"]
---

# Repainting

**Repainting** is when an indicator or strategy shows different values on *historical* bars than it showed *in real time* on those same bars. The chart history is redrawn with information that was not available when the bar was live. It is the form [[lookahead-bias]] takes in charting platforms, and the most common reason a [[tradingview-platform|TradingView]] community script looks brilliant in the Strategy Tester and fails live.

## How Repainting Happens

TradingView's Pine Script documentation groups the causes roughly as follows (Source: [[tradingview-community-scripts]]):

1. **Higher-timeframe data fetched with lookahead.** In [[pine-script|Pine]], `request.security()` with `lookahead=barmerge.lookahead_on`, or without offsetting the series by `[1]`, returns the *final* higher-timeframe close on every intra-period historical bar. For example, a 4h script "knows" the daily close at 04:00. This is the single largest source of repainting in public scripts.
2. **Unconfirmed-bar signals.** A signal computed on the live bar can flash on and off before the bar closes. History only records the final state, so the backtest sees signals that a live trader might have acted on and then watched disappear, and it never records the false triggers.
3. **Future-referencing indicators.** ZigZag, fractals, pivots and "Buy/Sell" swing markers need `N` bars *after* a point to confirm it. They are drawn back at the pivot bar, so historically they look perfectly timed.
4. **Intrabar execution settings.** `calc_on_every_tick`, `calc_on_order_fills` and bar-magnifier settings make historical fills behave differently from real-time fills.
5. **Non-standard chart types.** Backtesting on Heikin-Ashi, Renko or Kagi candles fills orders at synthetic prices that never traded.
6. **Data revisions.** Rarer in crypto, but vendor back-fills and symbol remaps can change history after the fact.

## A Diagnostic Test

The simplest test is the **replay or forward comparison**. Record the script's signals live, bar by bar, for a period (or use TradingView's Bar Replay), then reload the chart and compare the historical signals with what you recorded. Any difference is repainting. In code review, look for:

- `request.security(` calls on a higher timeframe without `[1]` plus `lookahead_on`, or without `barstate.isconfirmed` gating
- `ta.pivothigh` / `ta.pivotlow` / zigzag logic used for *entries*
- `calc_on_every_tick=true` in the `strategy()` declaration
- Signals not gated on `barstate.isconfirmed`

## Why It Matters for Strategy Research

Repainted equity curves are *systematically* optimistic, because the error always falls in the strategy's favour: the script is effectively reading the answer. No amount of fee overlay fixes it. The only fix is to rebuild the logic on data that is strictly point-in-time. That is why the [[external-strategy-sources|external-source funnel]] requires every borrowed script to be **ported to your own backtester** before its results count. Porting forces each rule to state exactly which closed bar it reads.

## Getting the Data (CryptoDataAPI)

Rebuilding a script without repainting needs candles that were final at the time they are read:

- `GET /api/v1/backtesting/klines`: closed historical OHLCV bars. Compute higher-timeframe values only from *completed* higher-timeframe bars, then align them forward to the lower timeframe.
- `GET /api/v1/backtesting/daily-snapshots/{date}`: the point-in-time market state as of each date, for signals that combine price with other fields. See [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=4h"
```

## Sources

- (Source: [[tradingview-community-scripts]])

## Related

- [[lookahead-bias]]: the general class of error this belongs to
- [[pine-script]], [[tradingview-platform]]
- [[external-strategy-sources]]: the vetting funnel for borrowed strategies
- [[crypto-forward-testing]]: the live check that catches what the code review missed
