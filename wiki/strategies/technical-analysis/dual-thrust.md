---
title: "Dual Thrust"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [breakout, technical-analysis, day-trading, trend-following, crypto, futures, bitcoin]
aliases: ["Dual Thrust Trading Algorithm", "Dual Thrust Breakout"]
strategy_type: technical
timeframe: intraday
markets: [crypto, futures, forex]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "When price travels a volatility-scaled distance from the session open, late participants and stopped-out range traders chase it; the breakout trader buys the move early and is paid by the continuation, while absorbing the frequent false breaks."
data_required: [ohlcv-daily, ohlcv-1h]
min_capital_usd: 1000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.3
expected_max_drawdown: 0.35
breakeven_cost_bps: 15
decay_evidence: "QuantConnect's own port on SPY (2004-01 to 2017-08) reported Sharpe -0.17 and 41.1% max drawdown; the rule is widely known in Chinese futures CTA circles, so any open-range breakout edge is heavily crowded."
kill_criteria: |
  - rolling 6-month net Sharpe < 0
  - drawdown > 30% from high-water mark
  - false-break rate (reversal through the opposite trigger within one day) > 60% over 50 trades
related: ["[[quantconnect]]", "[[quantconnect-strategy-library]]", "[[opening-range-breakout]]", "[[donchian-channel-breakout]]", "[[breakout-trading]]", "[[volatility-breakout]]", "[[dynamic-breakout-ii]]"]
---

# Dual Thrust

**Dual Thrust** is a day-level breakout system attributed to Michael Chalek: it builds a price range from the last N days' highs, lows and closes, then buys when price rises a fraction K1 of that range above today's open and sells when it falls K2 of the range below. It is an always-in reversal system (a long signal closes any short and vice versa). The version below follows [[quantconnect|QuantConnect]]'s Strategy Library port and adapts it to 24/7 crypto markets (Source: [[quantconnect-strategy-library]]).

## Edge Source

Per [[edge-taxonomy]]: **behavioral** (momentum ignition — traders chase moves once price clears an obvious daily band) and **risk-bearing** (the system eats many small whipsaw losses in exchange for occasional large trend days). There is no informational edge; the rule is public and old.

## Why This Edge Exists

A daily open is a reference point. When price travels more than half of the recent daily range away from it, the move usually has a flow behind it — liquidations, news, a large taker — and a fraction of those days extend into trend days. The people on the other side are intraday mean-reverters fading the move and short-dated option sellers hedging late. In crypto, leverage makes trend days more common than in equity indices: a band break often triggers [[liquidations]] that feed the move ([[liquidation-cascade-arbitrage]]). The counter-force is that the same rule on a choppy, mean-reverting market just buys highs and sells lows, which is what QuantConnect's SPY test showed.

## Null Hypothesis

If intraday price paths are a driftless random walk, crossing open ± K·range tells you nothing about the rest of the day: expected gross P&L per trade is zero and net P&L equals minus costs times turnover. Testable prediction: compare the distribution of close-minus-trigger returns after triggers against the same statistic at random times of day with matched volatility. No significant difference means no edge.

## Rules

### Range
- Over the last N completed daily bars (N = 4 in the source): HH = highest high, LC = lowest close, HC = highest close, LL = lowest low.
- `range = max(HH - LC, HC - LL)`.

### Entry
- **Crypto adaptation**: define "open" as the 00:00 UTC daily open (crypto has no session close; pick one convention and keep it).
- Buy trigger = open + K1 × range; sell trigger = open - K2 × range. Source default K1 = K2 = 0.5. Setting K1 < K2 biases toward longs; K1 > K2 toward shorts.
- Price crosses buy trigger: close any short, go long. Price crosses sell trigger: close any long, go short.

### Exit
- Reversal on the opposite trigger (source rule).
- Optional crypto additions (not in the source): flatten at the daily roll, and a hard stop at 1 × range from entry.

### Position Sizing
- Volatility-scaled: size so that a move of 1 × range equals a fixed fraction (e.g., 1%) of equity ([[atr-position-sizing]]). Leverage on perps should stay low; the strategy is wrong often.

## Implementation Pseudocode

```python
# daily: pandas DataFrame of completed daily bars (UTC); intraday: 1h bars
N, K1, K2 = 4, 0.5, 0.5

def daily_triggers(daily):
    hh = daily.high.rolling(N).max().shift(1)   # use only completed days
    ll = daily.low.rolling(N).min().shift(1)
    hc = daily.close.rolling(N).max().shift(1)
    lc = daily.close.rolling(N).min().shift(1)
    rng = pd.concat([hh - lc, hc - ll], axis=1).max(axis=1)
    return daily.open + K1 * rng, daily.open - K2 * rng

pos = 0
for bar in intraday:                      # iterate hourly bars
    up, dn = triggers[bar.date]
    if bar.high >= up and pos <= 0:       # breakout up
        pos = +1                          # reverse / enter long at up (+ slippage)
    elif bar.low <= dn and pos >= 0:      # breakout down
        pos = -1
    # cost = |delta pos| * (taker_fee + half_spread + slippage); funding if on perps
```

## Indicators / Data Used

- Daily OHLC for the range; 1h (or finer) bars for trigger detection.
- Optional regime filter: [[regime-detection]] or ADX-style trend state to switch the system off in chop (not in the source).
- Perp funding for carry cost on held positions ([[funding-rate]]).

## Example Trade

Illustrative (not a backtest): BTC's last four daily bars give HH = 64,000, LL = 60,000, HC = 63,500, LC = 60,800. Range = max(3,200, 3,500) = 3,500. Today's UTC open is 62,000, so the buy trigger is 63,750 and the sell trigger 60,250. At 14:00 UTC BTC trades through 63,750 on a liquidation wave; the system goes long. BTC closes the day at 65,100 and the next day opens at 65,000 with a new range. The trade stays long until price hits the new sell trigger. Cost overlay: ~5 bps taker fee + ~3 bps slippage per side on a liquid perp, plus funding while held.

## Performance Characteristics

- **Source claim** (QuantConnect, SPY daily, 2004-01 to 2017-08, pre-cost): Sharpe -0.17, max drawdown 41.1%. The article notes it works better in trending markets and gives false signals in volatile, mean-reverting ones (Source: [[quantconnect-strategy-library]]).
- No crypto backtest exists in the wiki. Expect a low hit rate (35-45%) with right-skewed winners, typical of breakout systems ([[breakout-trading]]).
- **Cost overlay**: an always-in reversal system flips often. At 1-2 flips per day, round-trip costs of ~15 bps can consume the whole gross edge; test with explicit fees because the LEAN default for crypto was zero-fee.

## Capacity Limits

Trades only at obvious price levels on majors, so capacity is set by liquidity at the trigger. On BTC/ETH perps, tens of millions of dollars are feasible; on alts, slippage at trigger levels (where stops cluster) dominates well below $1M.

## What Kills This Strategy

- **Regime**: range-bound, mean-reverting markets turn it into a systematic buy-high/sell-low machine ([[failure-modes]]).
- **Crowding**: triggers sit exactly where stop orders cluster, so fills are worse than the bar data suggest.
- **Cost drag**: frequent reversals.
- **Overfitting K1/K2/N**: the four parameters invite curve-fitting ([[overfitting]]).

## Kill Criteria

See frontmatter; retire per [[when-to-retire-a-strategy]] if rolling 6-month net Sharpe < 0 or the false-break rate exceeds 60% over 50 trades.

## Advantages

- Four parameters, trivially implementable in Python or [[pine-script]].
- Adapts to volatility through the range term.
- Symmetric and asset-agnostic.

## Disadvantages

- Negative published result on its best-known port.
- Always in the market, so carries funding and gap risk continuously.
- Crypto "open" is arbitrary; results depend on the chosen UTC anchor.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=10` — completed daily bars for the range
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=48` — intraday bars for trigger detection

**Historical data:**
- `GET /api/v1/backtesting/klines` — full Binance spot OHLCV archive for backtesting triggers
- `GET /api/v1/backtesting/funding` — historical funding for the perp carry leg

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=10"
```

Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

An agent on the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this:

- **Signal** — compute the 4-day range once per UTC day from daily `/market-data/klines`, then poll 1h klines for trigger crosses
- **Regime gate** — skip new entries when `GET /api/v1/volatility/regime` flags a mean-reverting state; breakouts need expanding volatility
- **Backtest** — replay `/backtesting/klines` at 1h with an explicit fee and slippage model, and add `/backtesting/funding` for perp holding cost
- **Execution** — pre-place stop-limit orders at both triggers instead of market orders after the cross; triggers sit at crowded stop levels

## Sources

- (Source: [[quantconnect-strategy-library]]) — QuantConnect Strategy Library, "Dual Thrust Trading Algorithm", accessed 2026-09-28

## Related

- [[quantconnect]] · [[external-strategy-sources]]
- [[opening-range-breakout]] · [[donchian-channel-breakout]] · [[volatility-breakout]] · [[breakout-trading]]
- [[dynamic-breakout-ii]] — the volatility-adaptive breakout from the same library
