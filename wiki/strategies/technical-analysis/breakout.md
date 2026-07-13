---
title: "Breakout"
type: strategy
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [technical-analysis, breakout, momentum, trend-following, stocks, crypto]
aliases: ["Breakout Pattern", "Price Breakout", "Range Breakout"]
strategy_type: technical
timeframe: swing
markets: [stocks, crypto, forex, futures]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Traders anchored to a defended price level are slow to re-rate when it breaks; clustered stop-loss orders just beyond the level provide forced counterparties that accelerate the move."
crowding_risk: medium
data_required: [ohlcv-daily, volume]
min_capital_usd: 2000
capacity_usd: 20000000
related: ["[[edge-taxonomy]]", "[[support]]", "[[resistance]]", "[[support-resistance]]", "[[volume]]", "[[average-true-range]]", "[[momentum]]", "[[trend-following]]", "[[breakout-trading]]", "[[consolidation]]", "[[position-sizing]]", "[[false-breakout]]"]
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
