---
title: "ATR Trailing Stop"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [technical-analysis, risk-management, trend-following, volatility, order-types]
aliases: ["ATR Trailing Stop", "Chandelier Exit", "Volatility Stop", "ATR Stop"]
related: ["[[average-true-range]]", "[[trailing-stop]]", "[[atr-position-sizing]]", "[[stop-loss]]", "[[trend-following-cta]]", "[[trend-following]]", "[[managing-winners]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, futures, forex, crypto]
complexity: intermediate
backtest_status: walk-forward-validated
edge_source: [behavioral, risk-bearing]
edge_mechanism: "An exit rule, not an entry edge. It monetizes the persistence of trends by staying in a position while it runs and exiting only when price retraces by a volatility-scaled amount, while behaviorally enforcing discipline against the disposition effect (cutting winners early, holding losers)."
data_required: [ohlcv-daily]
min_capital_usd: 5000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: 0.0
expected_max_drawdown: 0.0
breakeven_cost_bps: 0
---

An ATR trailing stop is an exit rule that places a stop a fixed multiple of the [[average-true-range|Average True Range (ATR)]] away from the most favorable price reached since entry, ratcheting in the direction of the trade but never against it. Because the stop distance scales with volatility, it gives a position "room to breathe" in volatile conditions while tightening automatically as volatility falls. The best-known formulation is Chuck LeBeau's **Chandelier Exit**, which hangs the stop a multiple of ATR below the highest high since entry (for longs). Like [[atr-position-sizing]], it is an overlay that shapes exits rather than a standalone return-generating signal.

## Edge source

This is a **risk-bearing** and **behavioral** technique from the [[edge-taxonomy]]. There is no entry alpha here; the value comes from (1) capturing the right tail of trending moves by not exiting on noise, and (2) overriding the human tendency to take profits too early and hold losers too long (the disposition effect). It is the canonical exit for [[trend-following-cta|trend-following]] systems, whose edge lives entirely in letting winners run.

## Why this edge exists

Trends, when they occur, tend to persist longer and further than intuition expects, but they are punctuated by sharp counter-trend retracements. A fixed-percentage or fixed-dollar stop fails in two ways: too tight and normal volatility knocks you out before the trend matures; too loose and you give back enormous open profit. ATR scaling solves this by setting the stop in *units of the instrument's own noise* — wide enough to survive ordinary pullbacks, tight enough to lock in gains once a move is mature and volatility contracts. Behaviorally, a pre-committed, mechanical trailing rule removes the discretionary moment where fear (sell now) or hope (it'll come back) destroys trend-following returns. The persistent counterparties are discretionary traders who exit winners on the first scary candle and average down on losers.

## Null hypothesis

Under the null, an ATR trailing stop applied to random entries should produce zero expected return net of costs — exits cannot create alpha where entries have none. The meaningful test is conditional: given a genuine trend signal, does the ATR trailing exit deliver **higher average winning-trade size and a better profit factor** than a fixed-percentage stop or a fixed-bar time exit on the same entries? If the ATR exit shows no improvement in capturing trend length over a naive fixed stop, the volatility scaling is adding no value.

## Rules

- **Volatility input**: ATR over a lookback (commonly 14 or 22 periods), Wilder-smoothed.
- **Multiple**: choose an ATR multiple — 2.5x to 3.5x is typical (LeBeau's Chandelier default is 3x ATR over 22 periods).
- **Long stop**: `stop = highest_high_since_entry − (multiple × ATR)`. The stop only ratchets up; it never moves down.
- **Short stop**: `stop = lowest_low_since_entry + (multiple × ATR)`; ratchets down only.
- **Exit**: close the position when price closes through (or trades through, per your fill convention) the trailing stop.
- **Initial stop**: at entry, the trailing stop doubles as the initial risk stop and feeds directly into [[atr-position-sizing]] (size the position so the distance to the initial stop equals the risk budget).
- **Optional tightening**: some implementations reduce the multiple as the trade ages or as a target is approached, trading some trend-capture for tighter profit lock-in.

## Implementation pseudocode

```python
def update_atr_trailing_stop(position, bar, atr, mult=3.0):
    if position.side == "long":
        position.high_water = max(position.high_water, bar.high)
        candidate = position.high_water - mult * atr
        position.stop = max(position.stop, candidate)   # ratchet up only
        if bar.close < position.stop:
            return "EXIT"
    else:  # short
        position.low_water = min(position.low_water, bar.low)
        candidate = position.low_water + mult * atr
        position.stop = min(position.stop, candidate)    # ratchet down only
        if bar.close > position.stop:
            return "EXIT"
    return "HOLD"
```

## Indicators / data used

- [[average-true-range|ATR]] (14- or 22-period, Wilder-smoothed)
- Running highest-high / lowest-low since entry (the "chandelier anchor")
- OHLCV bars on the trading timeframe
- The entry signal from the host strategy (this rule only governs exit)

## Example trade

Long a futures contract entered at $100 with a 22-day ATR of $2.00 and a 3x multiple. Initial stop = $100 − 3 × $2.00 = $94 (and the position is sized so $6/contract of risk equals the budget). Price rallies to a high of $130; ATR rises to $3.00. New stop = $130 − 3 × $3.00 = $121 — locking in $21 of the $30 open profit. Price then pulls back and closes at $120, below the $121 stop → exit at the next available fill, banking roughly $20–21 per contract. A fixed 5% stop ($95) would have either been hit on an early dip or, if survived, given back far more on the retracement.

## Performance characteristics

As an overlay, the ATR trailing stop has no standalone P&L; it modifies the host signal's trade distribution. Typical effects on a real trend signal: larger average winners, more giveback than a tight fixed stop (you always exit some distance below the peak), a lower win rate but a higher payoff ratio, and improved performance during sustained trends at the cost of more whipsaws in choppy regimes. The volatility scaling is robust because volatility is persistent and forecastable. Incremental costs are limited to the exit slippage when the stop is triggered, often on a fast move.

## Capacity limits

Capacity is set by the host strategy and the liquidity of the traded instrument, not by the stop rule. The mechanic scales to institutional size and is standard at large [[managed-futures]] funds. The only stop-specific concern is that exits cluster when many participants use similar ATR multiples off similar anchors, which can amplify slippage on the triggering move — a mild crowding effect in heavily systematic markets.

## What kills this strategy

- **Choppy, rangebound markets**: repeated whipsaws as price oscillates around the stop band — the dominant failure mode (see [[failure-modes]]).
- **Gap risk**: overnight or news gaps jump past the stop, so realized exit is well below the stop level.
- **Wrong multiple**: too tight → premature exits on noise; too loose → massive giveback of open profit.
- **Stale ATR in volatility expansions**: a sudden vol spike widens the true range after the fact, but the stop was computed on the prior, lower ATR.

## Kill criteria

- Whipsaw rate (stop hit and signal re-entry within N bars) exceeds a threshold over a rolling window → the multiple is too tight or the market regime is rangebound; widen or stand aside.
- Average giveback (peak open profit minus realized profit) exceeds 50% of average open profit → multiple too wide; tighten.
- On the host signal, the ATR trailing exit underperforms a fixed-fraction stop on profit factor over a rolling 12-month walk-forward → revert to the simpler exit.

## Advantages

- Adapts stop distance to current volatility automatically.
- Lets winners run while mechanically locking in profit — the core of trend-following.
- Enforces exit discipline, neutralizing the disposition effect.
- Doubles as the initial risk stop and integrates cleanly with [[atr-position-sizing]].

## Disadvantages

- No edge without a real entry signal.
- Whipsaws badly in rangebound markets.
- Always exits below the peak — guarantees some giveback.
- Vulnerable to gaps that jump the stop level.

## Getting the Data (CryptoDataAPI)

For crypto positions, [[cryptodataapi|CryptoDataAPI]] serves the OHLCV bars that drive the ATR and the chandelier anchor, plus regime and liquidity context for choosing the multiple.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` — OHLCV on the trading timeframe for ATR and the highest-high/lowest-low anchor
- `GET /api/v1/volatility/regime` — per-asset vol regime; a fresh `vol_shock` state warns the stop was computed on stale, lower ATR
- `GET /api/v1/liquidity/depth` — per-coin book depth/spread: thin books mean worse slippage when the stop triggers

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Binance spot 1h/4h/1d back to 2017-08) for testing multiples, whipsaw rates, and giveback across regimes

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Stop maintenance** — on each bar close, pull `GET /api/v1/market-data/klines` for the traded symbol, update ATR and the high/low water mark, ratchet the stop; the rule is pure arithmetic an agent can run 24/7 — crypto never closes, so the stop must be watched through weekends too.
- **Multiple selection** — `GET /api/v1/volatility/regime` per asset: widen the multiple in `expanding` conditions, tighten in `mean_reverting`; check `GET /api/v1/liquidity/depth` for the thin-book windows where exit slippage on the trigger is worst.
- **Regime gate** — `GET /api/v1/quant/market`: `range_low_vol`/`choppy_high_vol` states are the whipsaw regimes where ATR trailing exits underperform a simple fixed stop — widen the band or stand aside.
- **Backtest** — whipsaw-rate and giveback studies on `GET /api/v1/backtesting/klines` (Binance 1h/4h/1d since 2017-08); 1m bars exist only since 2026-03-30, so intrabar trigger simulation is limited to that window — use bar closes for fills elsewhere.
- **Tips** — snapshot all open positions' stop-breach checks from one `GET /api/v1/daily/prices` call (~2,500 pairs) instead of per-symbol polling between bar closes.

## Sources

- Chuck LeBeau — Chandelier Exit (ATR-anchored trailing stop), widely documented in trading-systems literature.
- J. Welles Wilder, *New Concepts in Technical Trading Systems* (1978) — origin of ATR (see [[j-welles-wilder]]).
- Curtis Faith, *Way of the Turtle* (2007) — N-based (ATR) exits in the Turtle system.

## Related

- [[average-true-range]]
- [[trailing-stop]]
- [[atr-position-sizing]]
- [[stop-loss]]
- [[trend-following-cta]]
- [[managing-winners]]
- [[trend-following]]
