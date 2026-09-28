---
title: "Dynamic Breakout II"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [breakout, technical-analysis, trend-following, volatility, forex, crypto]
aliases: ["Dynamic Breakout 2", "Adaptive Lookback Breakout"]
strategy_type: technical
timeframe: swing
markets: [forex, crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Trends that break out of both a volatility band and a multi-week high/low tend to persist because slow money reallocates over weeks; the lookback lengthens in volatile markets so noise has to clear a higher bar."
data_required: [ohlcv-daily]
min_capital_usd: 2000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.3
expected_max_drawdown: 0.25
breakeven_cost_bps: 40
decay_evidence: "QuantConnect's EURUSD port (2010-2016) reported only ~2.3%/yr and Sharpe 0.31; GBPUSD lost money over the same window. No evidence of a durable edge beyond generic trend-following."
kill_criteria: |
  - rolling 12-month net Sharpe < 0
  - drawdown > 25% from high-water mark
  - average holding period collapses below 3 days (whipsaw regime) for 3 months
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[donchian-channel-breakout]]", "[[bollinger-bands]]", "[[turtle-trading]]", "[[dual-thrust]]", "[[volatility-breakout]]"]
---

# Dynamic Breakout II

**Dynamic Breakout II** is a daily breakout system whose lookback window grows and shrinks with volatility: entries require price to clear both a 2σ [[bollinger-bands|Bollinger Band]] and the N-day high or low, where N adapts between 20 and 60 days. The exit is a cross of the N-day moving average. [[quantconnect|QuantConnect]]'s Strategy Library ports it to EURUSD and GBPUSD; this page adapts it to crypto majors (Source: [[quantconnect-strategy-library]]).

## Edge Source

**Behavioral** (under-reaction and slow reallocation after a regime break) plus **risk-bearing** (holding through whipsaws), as in all [[trend-following]] per [[edge-taxonomy]].

## Why This Edge Exists

Fixed-lookback channels ([[donchian-channel-breakout]], [[turtle-trading]]) break too easily when volatility jumps and too slowly when it falls. Scaling N with volatility makes the breakout threshold roughly volatility-invariant: in a quiet market a 20-day high is meaningful; in a volatile one only a 50-60-day high is. Requiring a Bollinger close as well filters single-bar spikes. The counterparties are mean-reversion traders fading the breakout and hedgers who sell into strength.

## Null Hypothesis

Under a random walk, the conditional return after a joint Bollinger + N-day breakout equals the unconditional drift, and the SMA exit captures nothing. Testable: shuffle daily returns (block bootstrap to keep volatility clustering) and compare the strategy's Sharpe distribution to the real one.

## Rules

### Adaptive lookback
- Start N = 20.
- Daily: σ_today and σ_yesterday = standard deviation of the last 30 closes. `deltavol = (σ_today - σ_yesterday) / σ_today`; `N = round(N × (1 + deltavol))`, clipped to [20, 60].

### Entry
- **Long**: yesterday's close > upper Bollinger Band (N-day, k = 2) **and** current price > highest high of the last N days.
- **Short**: yesterday's close < lower band **and** current price < lowest low of the last N days.

### Exit
- Long exits when price < N-day SMA of closes; short exits when price > N-day SMA.

### Position Sizing
- Not specified in the source. Crypto adaptation: volatility-target each position ([[volatility-targeting]]) to e.g. 20% annualized, since BTC's volatility is 5-8× EURUSD's.

## Implementation Pseudocode

```python
N = 20
for t in days[31:]:
    s_now  = close[t-30:t].std()
    s_prev = close[t-31:t-1].std()
    N = int(np.clip(round(N * (1 + (s_now - s_prev) / s_now)), 20, 60))
    window = close[t-N:t]
    mid, sd = window.mean(), window.std()           # source uses an EMA mid; SMA shown for clarity
    upper, lower = mid + 2 * sd, mid - 2 * sd
    hi, lo = high[t-N:t].max(), low[t-N:t].min()
    if pos == 0:
        if close[t-1] > upper and price[t] > hi: pos = +1
        elif close[t-1] < lower and price[t] < lo: pos = -1
    elif pos > 0 and price[t] < mid: pos = 0
    elif pos < 0 and price[t] > mid: pos = 0
    # size = target_vol / realized_vol; subtract fees + slippage + funding
```

## Indicators / Data Used

- [[bollinger-bands]] with a variable window
- Rolling N-day high/low ([[donchian-channel-breakout]])
- 30-day close volatility for lookback adaptation
- Perp [[funding-rate]] as carry cost when held via perpetuals

## Example Trade

Illustrative: ETH trades in a quiet range with N at 22. A weekly close above the upper band at 3,050 is followed by a break of the 22-day high at 3,080; the system buys at 3,085. Volatility rises over the next week, pushing N to 30, which moves the SMA exit lower and further from price. ETH runs to 3,600, then fades; the exit triggers at 3,390 when price closes under the 30-day SMA. Gross +9.9%, minus ~20 bps round-trip costs and ~2 weeks of funding.

## Performance Characteristics

- **Source claim** (QuantConnect, 2010-2016, pre-cost): EURUSD ~2.3% annual return, Sharpe 0.31, max drawdown ~14% (May-December 2015). GBPUSD produced negative returns and ~19% drawdown (Source: [[quantconnect-strategy-library]]).
- The source ran FX with LEAN's default zero-fee model for Forex, so spread costs are omitted. Low turnover (few trades per year per instrument) limits the damage, but expect the net figure to be lower.
- Crypto expectation: trend systems historically fit crypto better than FX majors because crypto trends are larger ([[time-series-momentum]]), but no wiki backtest exists.

## Capacity Limits

Daily signals on majors — capacity is large (tens of millions on BTC/ETH perps). Alt-coin versions are limited by depth at breakout levels.

## What Kills This Strategy

- Choppy, range-bound regimes (whipsaws through band + high).
- The lookback formula is path-dependent and can ratchet to 60 and stay there, making the system slow exactly when a new trend starts.
- Overfitting the 20/60/30/2σ constants ([[overfitting]]); see [[failure-modes]].

## Kill Criteria

Retire per [[when-to-retire-a-strategy]] on the frontmatter conditions (rolling 12-month net Sharpe < 0 or drawdown > 25%).

## Advantages

- Volatility-aware threshold without a separate regime model.
- Double confirmation reduces single-bar false breaks.
- Low turnover.

## Disadvantages

- Weak published results, and the second test instrument lost money.
- Adaptive rule adds path dependence that is hard to reason about.
- Moving-average exit gives back a large part of each trend.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=100` — daily bars for bands, channel and volatility
- `GET /api/v1/volatility/regime` — per-asset volatility regime as a cross-check on the lookback

**Historical data:**
- `GET /api/v1/backtesting/klines` — daily OHLCV archive for the adaptive-lookback backtest
- `GET /api/v1/backtesting/funding` — funding history for perp holding costs

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=100"
```

Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

On the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Signal** — pull 100 daily klines per major, recompute N, bands and channel once per UTC day
- **Regime gate** — cross-check the adaptive N against `/volatility/regime`; skip entries in a vol-shock regime where band breaks are liquidation noise
- **Backtest** — `/backtesting/klines` daily since 2017 covers several crypto trend and chop cycles; include funding from `/backtesting/funding`
- **Tips** — log N each day; if it sits at the 60 cap for months, the adaptation has stopped doing anything

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "The Dynamic Breakout II Strategy", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[dual-thrust]] · [[donchian-channel-breakout]] · [[turtle-trading]] · [[volatility-breakout]]
- [[bollinger-bands]] · [[volatility-targeting]]
