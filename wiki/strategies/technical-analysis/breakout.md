---
title: "Breakout"
type: strategy
created: 2026-06-22
updated: 2026-10-17
status: good
tags: [technical-analysis, breakout, momentum, trend-following, crypto]
aliases: ["Breakout Pattern", "Price Breakout", "Range Breakout"]
strategy_type: technical
timeframe: swing
markets: [crypto, forex, futures]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Traders anchored to a defended price level are slow to re-rate when it breaks; clustered stop-loss orders just beyond the level provide forced counterparties that accelerate the move."
crowding_risk: medium
data_required: [ohlcv-daily, volume]
min_capital_usd: 2000
capacity_usd: 20000000
related: ["[[edge-taxonomy]]", "[[support]]", "[[resistance]]", "[[support-resistance]]", "[[volume]]", "[[average-true-range]]", "[[momentum]]", "[[trend-following]]", "[[breakout-trading]]", "[[consolidation]]", "[[position-sizing]]", "[[false-breakout]]"]
gates:
  - id: consolidation_range
    role: entry
    rule: "A consolidation of at least 4 weeks whose high-low range is at most 10% (resistance = range high, support = range low)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=60
    field: candles[].high
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].h
    note: "From the pseudocode (min_weeks=4, max_range_pct=0.10). Over closed daily bars before today, find a run of at least 28 bars whose max high / min low - 1 is at most 0.10. Drop the forming bar named by forming_bar_timestamp."
  - id: level_touches
    role: filter
    rule: "The level is tested at least 2-3 times before the break"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=60
    field: candles[].high
    note: "Count bars whose high (low) comes within a tolerance of resistance (support). The page does not define a touch, so the tolerance is the desk's call."
  - id: close_beyond_level
    role: entry
    rule: "Enter when a daily bar closes beyond the level: long above resistance, short below support (a close, not a wick)"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=3
    field: candles[].close
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
    note: "Use the last closed bar only."
  - id: breakout_volume_1_5x
    role: entry
    rule: "Breakout bar volume at least about 1.5x its 20-day average"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=22
    field: candles[].volume
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].v
    note: "Average the 20 closed bars before the breakout bar. Hyperliquid perp volume; the page's example uses Binance spot (/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d), which works the same way."
  - id: retest_entry
    role: entry
    rule: "Alternative: enter on the retest, when price pulls back to the broken level and holds"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=10
    field: candles[].low
    note: "The return to the level is mechanical; 'holds' is not defined on the page."
  - id: trend_aligned_filter
    role: filter
    rule: "Optional: trade only with-trend breaks, using the 200-day moving average"
    runnable: true
    endpoint: /api/v1/indicators/technical/{coin}
    field: ma.above_200
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}&end={end}
    replay_field: klines[].c
    note: "Longs only when above_200 is true, shorts only when false. Replay: recompute the 200-day SMA from closes."
  - id: no_fresh_listings
    role: universe
    rule: "Skip freshly listed coins: they print fake N-day highs with no real range behind them"
    runnable: true
    endpoint: /api/v1/quant/coins/{coin}
    field: meta.insufficient_history
    note: "From the page's AI-agent tips; skip when insufficient_history or new_listing is true (new_listing is on each row of /api/v1/quant/coins)."
  - id: chop_suppression
    role: filter
    rule: "Suppress entries while choppy_high_vol dominates the market regime"
    runnable: true
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "Skip while the committed label is choppy_high_vol."
  - id: coiled_watchlist
    role: filter
    rule: "A compressed vol regime marks the coiled ranges worth watching"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "A watchlist aid from the page's AI workflow, not a hard entry condition."
  - id: stop_back_inside
    role: stop
    rule: "Stop 1.0 ATR(14) back inside the range (rules allow 0.5-1x ATR beyond the level); a close back inside invalidates the break"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30&atr=14
    field: candles[].atr
  - id: measured_move_target
    role: exit
    rule: "Target = the range height projected from the breakout level"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: atr_trailing_stop
    role: stop
    rule: "Or trail: exit on a close below the highest close minus 2 ATR(14)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=30&atr=14
    field: candles[].close
  - id: risk_per_trade
    role: sizing
    rule: "Size so the stop distance risks at most 1-2% of equity (the pseudocode uses 1%)"
    runnable: true
    input: position
  - id: participation_context
    role: filter
    rule: "Grade the break with open interest and liquidation context: participation and stop clusters behind it"
    runnable: partial
    endpoint: /api/v1/liquidity/oi-divergence
    field: rows[].oi_change_4h_pct
    note: "The page names the data but gives no rule. Same-side liquidations are alerts[].direction on /api/v1/market-intelligence/squeeze-alerts?symbol={coin} (short_squeeze for an upside break)."
  - id: kill_criteria
    role: stop
    rule: "Halt on a 25% drawdown, 12 consecutive losers, win rate under 30% with payoff under 1.5 over 50 trades, or realized slippage over 50 bps round-trip across 20 trades"
    runnable: true
    input: position
---

# Breakout

A **breakout** is the event of price moving decisively beyond a well-defined level — typically a [[resistance]] ceiling, a [[support]] floor, the boundary of a [[consolidation]] range, or a chart-pattern line — usually accompanied by a surge in [[volume]]. The breakout strategy enters in the direction of the break on the thesis that the prior balance between buyers and sellers has resolved, initiating a new directional move. This page is the concise canonical entry on the breakout *concept and trade*; for the deeper treatment of specific patterns, filters, and the historical channel-breakout lineage, see [[breakout-trading]].

## Edge source

Breakout trading exploits a **behavioral** edge with a **structural** component (see [[edge-taxonomy]]). Behaviorally, participants anchor to a level that has repeatedly held and are slow to accept that conditions have changed once it gives way. Structurally, the *predictable placement of stop-loss orders* just beyond an obvious level creates a pocket of forced, one-sided order flow: when the level breaks, those stops fire as market orders, mechanically pushing price further in the break direction and giving the breakout trader forced counterparties.

## Why this edge exists

The counterparties are **range traders on the wrong side** and **anchored sidelined traders.** Range traders who sold near resistance (betting on a reversal) are forced to cover as the level breaks, buying into the move. Sidelined traders anchored to the old range chase once the new trend becomes visible. The edge persists because markets spend most of their time (~70-80%) range-bound, so the transition to trending repeatedly catches participants flat-footed; and because anchoring and the disposition effect are durable human biases — range sellers add to losers above resistance ("even better price") before capitulating, and that capitulation is the breakout's fuel. It is partly a [[limits-to-arbitrage]] story too: the move can overshoot before any "fair value" trader can fade it.

## Null hypothesis

Under a random walk, crossing an N-period high carries no information — a random walk makes new extremes routinely without any regime change, so expected post-breakout drift is zero and net of costs the system loses. The proper test compares breakout entries against (a) random-timed entries paired with the *same* [[average-true-range|ATR]] exit, and (b) the identical rules run on shuffled / simulated random-walk series. Breakout rules will still generate "trades" on random data; any claimed edge must beat that baseline after [[slippage|costs]]. Much of the apparent edge in naive backtests is anchoring-on-volume confirmation that fails out-of-sample.

## Rules

**Entry:**
- Define a clear level: a [[support]]/[[resistance]] line tested ≥ 2-3 times, or a [[consolidation]] range boundary
- Enter when price **closes** beyond the level (long above resistance, short below support) on volume ≥ ~1.5x the 20-day average — a close, not just an intraday wick
- Alternative: enter on the **retest** — wait for price to break, pull back to the broken level (now flipped support/resistance), and hold. Higher win rate, but misses fast movers

**Exit:**
- **Target:** the *measured move* — project the range height from the breakout point — or a trailing [[average-true-range|ATR]] stop (e.g., 2x ATR from the highest close)
- **Stop:** just back inside the range (a close back inside invalidates the break), typically 0.5-1x ATR beyond the level

**Position sizing:**
- Size so the stop distance is ≤ 1-2% of total equity (see [[position-sizing]])

## Implementation pseudocode

```python
for symbol in universe:
    bars = daily_ohlcv(symbol)
    rng  = find_consolidation(bars, min_weeks=4, max_range_pct=0.10, min_touches=2)
    if rng is None:
        continue

    atr     = ATR(bars, 14)
    vol_avg = SMA(bars.volume, 20)
    close, vol = bars[-1].close, bars[-1].volume

    if no_position(symbol):
        if close > rng.resistance and vol >= 1.5 * vol_avg:      # confirmed long break
            stop   = rng.resistance - 1.0 * atr                  # back-inside-range stop
            target = rng.resistance + rng.height                 # measured move
            size   = (0.01 * equity) / (close - stop)            # risk 1%
            buy(symbol, size, stop=stop, target=target)
        elif close < rng.support and vol >= 1.5 * vol_avg:       # confirmed short break
            sell_short(symbol, ...)                               # mirror logic
    else:
        trail_stop(symbol, highest_close - 2 * atr)
        if close < position.stop or close >= position.target:
            close_position(symbol)
```

## Indicators / data used

- Daily OHLCV (price-action based; intraday optional for execution)
- [[volume]] and its 20-day average — the primary confirmation filter
- [[average-true-range|ATR]] (14) — stop placement, trailing exits, volatility-compression filtering
- [[support-resistance]] levels / N-day high-low channels for systematic detection
- Optional higher-timeframe trend filter (e.g., 200-day MA) to trade only with-trend breaks
- No fundamental data required

## Example trade

*Illustrative, round numbers only — not a real trade or backtest.*

A stock trades between \$48 ([[support]]) and \$52 ([[resistance]]) for six weeks, volume drying up through the range. In week seven it closes at \$53.20 on 2x average volume. The trader buys at \$53.20, stops at \$51.50 (back inside the range), and targets \$56 (the \$4 range height projected from \$52). Risk \$1.70/share, reward \$2.80 → ~1.65:1 reward-to-risk. If price instead closes back below \$52 within a couple of sessions, the trade is cut as a [[false-breakout]].

## Performance characteristics

- **Win rate:** low — typically 35-45% for swing breakouts after volume/close filtering (raw, unfiltered level breaches fail far more often)
- **Payoff:** the edge is in the winners — average win ~1.5-2.5x average loss with trailing stops; a 40% win rate at 2:1 yields roughly +0.2R per trade before costs
- **Cost overlay:** breakouts demand liquidity exactly when spreads widen and price is moving. Realistic [[slippage]] ~10-30 bps/side in liquid markets (much worse in small caps / crypto alts). Tolerable on a 3-5% target; fatal on tight intraday breaks
- **Equity curve:** long flat-to-down stretches in chop (death by a thousand stop-outs) punctuated by occasional large trend captures — the classic [[trend-following]] shape
- Realistic standalone expectation: net Sharpe ~0.4-0.6, max drawdown 20-30%

## Capacity limits

For discretionary or small systematic accounts in large-cap stocks, major FX, or BTC/ETH, capacity is not a constraint. The limit arises because breakout entries are *concentrated in time* — everyone's buy-stops fire in the same minutes — so adding size into that burst worsens fills disproportionately. A diversified swing-breakout program realistically caps around \$20M before entry [[market-impact]] erodes the thin per-trade expectancy; large CTAs run breakout-family systems at far greater scale only by using longer lookbacks, slower entries, and deep futures markets. In small caps and thin crypto pairs, per-trade capacity can be tens of thousands of dollars. See [[strategy-capacity]].

## What kills this strategy

- **Extended choppy regimes** — quarters of range-bound chop bleed the account through false-breakout stop-outs (the most common death; see [[failure-modes]])
- **Stop-hunting** — in thin markets, participants push price through obvious levels to trigger stops, then reverse, turning the structural edge into a structural cost
- **Volatility collapse** — when ranges compress, measured-move targets shrink while costs stay fixed, pushing expectancy below breakeven
- **Crowding on obvious levels** — round numbers and 52-week highs attract so many breakout orders that fills degrade and immediate reversals rise
- **Gap risk** — overnight gaps through stops turn a 1R loss into 2-3R
- **Discipline failure** — the sub-50% win rate is psychologically punishing; quitting after a normal losing streak is how most actually exit

## Kill criteria

- Drawdown > 25% from equity high-water mark → halt, full review
- Rolling 12-month net Sharpe < 0 over ≥ 40 trades → stop new entries
- Win rate < 30% **and** payoff < 1.5 over the last 50 trades → negative expectancy, halt
- Realized [[slippage]] > 50 bps round-trip over 20 consecutive trades → execution edge gone in this universe, change instruments or halt
- 12 consecutive losing trades (< 1% likely at a true 40% win rate) → assume regime break, halt

## Advantages

- Clear, objective, chart-visible entry and exit rules
- Captures the *start* of trends with favorable reward-to-risk when correct
- Works across markets and timeframes
- Long, well-documented history (Donchian, Turtles) — failure modes are well mapped

## Disadvantages

- High [[false-breakout]] rate — many raw breakouts fail (often cited 50-70% depending on definition)
- Requires patience through long consolidation phases
- Costs erode profitability in chop where repeated false breaks trigger stops
- Hard to backtest rigorously — "breakout" definitions are somewhat subjective
- Low win rate is psychologically difficult to sustain

## Sources

- Covel, M. (2007). *The Complete TurtleTrader* — Dennis/Eckhardt channel-breakout experiment
- Faith, C. (2007). *Way of the Turtle* — original Turtle rules and their post-1980s decay
- O'Neil, W. (1988). *How to Make Money in Stocks* — cup-and-handle / flat-base breakouts (CAN SLIM)
- Bulkowski, T. (2005). *Encyclopedia of Chart Patterns*, 2nd ed. — empirical pattern failure rates
- Schwager, J. (1989). *Market Wizards* — Donchian-lineage breakout context

General market knowledge; no specific wiki source ingested yet.

## Getting the Data (CryptoDataAPI)

Everything the trade needs is OHLCV with volume, plus derivatives context to grade the break.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — OHLCV with volume for level detection, the 1.5x volume filter, and ATR stops
- `GET /api/v1/indicators/technical` — pre-computed SMA/BB/RSI structure state for universe-wide base screening
- `GET /api/v1/derivatives/open-interest?coin=BTC` and `GET /api/v1/market-intelligence/liquidations` — participation and stop-cluster context behind the break

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for testing breakout rules against the random-entry baselines in the null hypothesis above

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest) · [technical structure](https://cryptodataapi.com/technical-structure)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — N-day high/low channels and volume ratios computed from `GET /api/v1/market-data/klines`; a close beyond the level on ≥1.5x average volume is the trigger
- **Regime gate** — `GET /api/v1/quant/market`: suppress entries while `choppy_high_vol` dominates; `GET /api/v1/volatility/regime` reading `compressed` marks the coiled ranges worth watching
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09); run the shuffled-series null test the page prescribes, and validate the regime filter with `/api/v1/quant/regimes/history` (hourly since 2020, Pro Plus)
- **Tips** — respect `insufficient_history`/`new_listing` flags — freshly listed coins print fake "N-day highs" with no real range behind them; the retest entry fills better than chasing the break candle in thin pairs.

## Related

- [[breakout-trading]] — the deeper companion page (patterns, filters, history)
- [[support]] / [[resistance]] / [[support-resistance]] — the levels that define breakouts
- [[consolidation]] — the precondition
- [[volume]] — key confirmation
- [[average-true-range]] — stops and volatility filtering
- [[false-breakout]] — the primary failure mode
- [[momentum]] / [[trend-following]] — the broader strategy family
- [[edge-taxonomy]] — behavioral + structural edge classification
- [[position-sizing]] — risk-per-trade sizing
- [[failure-modes]] — how breakouts die
