---
title: "Triple Screen Trading System"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [technical-analysis, swing-trading, trend-following, momentum, indicators]
aliases: ["Triple Screen System", "Triple Screen", "Elder Triple Screen"]
related: ["[[macd-crossover]]", "[[moving-average-crossover]]", "[[multi-timeframe-confluence]]", "[[trend-following]]", "[[mean-reversion]]", "[[stochastic-oscillator]]", "[[edge-taxonomy]]", "[[technical-analysis-overview]]", "[[indicators-overview]]", "[[macd]]", "[[stochastic]]", "[[williams-percent-r]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, futures, forex, crypto]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [behavioral]
edge_mechanism: "Forces traders to trade in the direction of the higher-timeframe trend and enter only on a pullback, exploiting the persistent behavioral tendency of crowds to fade trends and chase breakouts at exactly the wrong moments."
data_required: [ohlcv-daily, ohlcv-intraday]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: low
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 25
---

The Triple Screen Trading System is a multi-timeframe filtering method developed by Dr. Alexander Elder and popularised in his 1993 book *Trading for a Living*. It combines three sequential "screens" — a higher-timeframe trend filter, an intermediate-timeframe oscillator for timing, and a lower-timeframe entry trigger — so that every trade is taken with the larger trend (the "tide"), entered against a short-term counter-move (the "wave"), and triggered precisely (the "ripple"). The system is a structured discipline rather than a single indicator, designed to resolve the contradiction that trend and oscillator indicators often give opposite signals on the same chart.

## The Three Screens at a Glance

| Screen | Elder's metaphor | Timeframe | Question it answers | Typical tool |
|---|---|---|---|---|
| **1 — Tide** | The market tide | One order higher (e.g. weekly) | *Which direction am I allowed to trade?* | [[macd\|MACD]]-Histogram slope, or 13/26 EMA |
| **2 — Wave** | The wave against the tide | Primary (e.g. daily) | *Is there a counter-trend pullback to enter into?* | Force Index, [[stochastic\|Stochastic]], [[williams-percent-r\|Williams %R]], Elder-Ray |
| **3 — Ripple** | The ripple | Primary, intrabar | *Has the pullback actually turned?* | Trailing buy/sell-stop above/below prior bar |

The genius of the design is the **division of labour**: the trend tool decides *direction* on a slow timeframe where it is reliable, and the oscillator decides *timing* on a faster timeframe where it is useful — so the two never contradict each other on the same chart. This is the concrete application of [[multi-timeframe-confluence]].

## Edge source

The edge is primarily **behavioral** (see [[edge-taxonomy]]). The system does not exploit a structural inefficiency or private information; it exploits the disciplined application of a rule set that most discretionary traders fail to follow. Specifically it enforces two behaviors that are psychologically hard: (1) only trading in the direction of the dominant trend, and (2) waiting for a pullback rather than chasing. The counterparties are momentum-chasers who buy breakouts at local extremes and counter-trend traders who fight the dominant move.

## Why this edge exists

Trends persist longer than most traders expect because of anchoring, herding, and slow information diffusion among under-attentive participants. Retail traders systematically (a) chase strength after a move is extended, getting poor fills, and (b) try to pick tops and bottoms against strong trends, repeatedly stopping out. Triple Screen mechanically removes both errors: the first screen bans counter-trend trades, and the second screen forces entry only when a short-term oscillator shows a counter-trend overshoot (i.e. a discount inside an uptrend). The other side of the trade is the panicked seller in an uptrend pullback (or the euphoric buyer in a downtrend bounce). Because the discipline is uncomfortable, the behavior does not get arbitraged away.

## Null hypothesis

Under the null, multi-timeframe filtering adds no value: pullback entries within a higher-timeframe trend would have the same expected return as random entries, and the win rate / payoff would match a naive single-timeframe MACD or moving-average system after costs. To reject the null, the system must show that conditioning entries on (trend agreement + intermediate oscillator extreme) produces a statistically better reward-to-risk than entering on the trend signal alone — across instruments and regimes, net of slippage. If a coin-flip entry filtered only by the long-term trend matches Triple Screen, the second and third screens add nothing.

## Rules

**Screen 1 — Market Tide (long-term trend filter).** Choose your primary trading timeframe, then move one order of magnitude higher (e.g. trade daily → trend on weekly). Apply a trend indicator: Elder uses the slope of the weekly MACD-Histogram (or a 13-/26-week EMA). 
- If the higher-timeframe trend is up → only **long** trades are permitted on the lower screens.
- If down → only **short** trades permitted.
- If flat/ambiguous → stand aside.

**Screen 2 — Market Wave (intermediate oscillator, timing).** Drop to the primary timeframe (daily). Apply an oscillator such as Force Index, Stochastic, Williams %R, or Elder-Ray.
- In a weekly uptrend, **buy** when the daily oscillator is oversold (a pullback).
- In a weekly downtrend, **short** when the daily oscillator is overbought (a bounce).

**Screen 3 — Entry (the ripple / trigger).** Use a trailing buy/sell-stop for precise entry.
- Long: place a buy-stop one tick above the high of the prior bar; entry triggers only if price turns back up, confirming the pullback is ending.
- Short: place a sell-stop one tick below the prior bar's low.
- If not filled, lower (long) or raise (short) the stop each bar to chase the entry while the screens remain aligned.

**Exit / stops.** Initial stop below the most recent swing low (long). Elder recommends a money-management stop and scaling out: take partial profit when the oscillator reaches the opposite extreme, trail the remainder with the trend.

**Sizing.** Risk a fixed fraction (Elder's "2% rule") of equity per trade based on the distance to the protective stop.

## Implementation pseudocode

```python
# Timeframes: HTF (e.g. weekly), MTF (e.g. daily), trigger uses MTF bars
def triple_screen(htf_bars, mtf_bars):
    # Screen 1: long-term trend via MACD histogram slope on HTF
    macd_hist = macd_histogram(htf_bars.close)
    trend_up   = macd_hist[-1] > macd_hist[-2]    # rising histogram
    trend_down = macd_hist[-1] < macd_hist[-2]

    # Screen 2: intermediate oscillator on MTF
    osc = force_index(mtf_bars, period=2)   # or stochastic / Williams %R
    oversold   = osc[-1] < 0                 # pullback in uptrend
    overbought = osc[-1] > 0                 # bounce in downtrend

    prev = mtf_bars[-1]
    if trend_up and oversold:
        # Screen 3: buy-stop above prior bar high
        return Order(side="buy", entry_stop=prev.high + tick,
                     protective_stop=recent_swing_low(mtf_bars),
                     risk_pct=0.02)
    if trend_down and overbought:
        return Order(side="sell", entry_stop=prev.low - tick,
                     protective_stop=recent_swing_high(mtf_bars),
                     risk_pct=0.02)
    return None   # no trade — screens disagree or trend flat
```

## Indicators / data used

- Weekly (or HTF) **MACD-Histogram** or EMA slope for the trend filter.
- Daily (or MTF) oscillator: **Force Index (2-period)**, **Stochastic**, **Williams %R**, or **Elder-Ray** (bull/bear power).
- OHLC bars on two aligned timeframes (one order of magnitude apart).
- No fundamental or alternative data required.

### Second-screen oscillator choices

The system is deliberately **indicator-agnostic** on Screen 2 — any well-behaved oscillator works as long as it cleanly flags counter-trend overshoots. Elder's own preference is the 2-period Force Index.

| Oscillator | Concept page | Signal in an uptrend (buy) | Character |
|---|---|---|---|
| **Force Index (2)** | — | Force Index dips below zero | Elder's favourite; combines price + volume, very responsive |
| **Stochastic** | [[stochastic]] | %K oversold (<20-30) | Smooth, classic; can stick at extremes in strong trends |
| **Williams %R** | [[williams-percent-r]] | %R below -80 | Mirror of stochastic; fast |
| **Elder-Ray** | — | Bear Power turns up from negative | Elder's own bull/bear-power measure |
| **RSI** | [[rsi]] | RSI dips toward oversold | Common substitute; slower than Force Index |

See the [[indicators-overview]] hub for how each oscillator is calculated and its individual failure modes.

## Example trade

Weekly chart of an equity shows the MACD-Histogram rising for three weeks → uptrend, longs only. On the daily chart the 2-period Force Index turns negative as price pulls back 4% over two sessions toward the rising 22-day EMA. A buy-stop is placed one tick above the prior day's high at $50.20. The next session price turns up and fills at $50.22. Protective stop goes under the swing low at $48.40 (risk ≈ $1.82, ~3.6%). With a $50,000 account risking 2% ($1,000), position size ≈ 549 shares. Price resumes the weekly uptrend; half is sold at $54 when the daily Force Index spikes positive, the rest trailed and exited at $56 — a roughly 2.5:1 reward-to-risk outcome on the held portion.

## Performance characteristics

Triple Screen is a discretionary framework, so published edge statistics are sparse and depend heavily on the chosen oscillator, instrument, and trend definition. Realistically it behaves like a trend-aligned pullback system: moderate win rate (45–55%), positive expectancy driven by reward-to-risk > 1.5 on winners, and clustered losses in choppy/range-bound regimes where the weekly trend whipsaws. Expect a net Sharpe in the 0.4–0.8 range on liquid instruments after realistic costs, with deep drawdowns (20–30%) during trendless periods. It underperforms strongly in mean-reverting, range-bound markets, where the trend screen produces false directional bias. Round-trip costs (commission + ~1 tick slippage on stop entries) materially erode results on lower-priced or less liquid names — keep per-trade frictions well under ~25 bps.

| Regime | Triple Screen behaviour | Why |
|---|---|---|
| **Strong trend** | Best — pullback entries get carried by the dominant move | The trend screen is reliable; pullbacks resolve in the trend's direction |
| **Trend with deep pullbacks** | Good — the system's sweet spot | Screen 2 catches the discount; Screen 3 confirms the turn |
| **Range-bound / choppy** | Worst — repeated whipsaw losses | Weekly trend flips, producing false long-then-short bias |
| **Sharp reversal** | Poor on the turn, then re-aligns | Lagging trend filter keeps signalling the old direction until it flips |

The performance distribution is the classic trend-aligned pullback shape: many small losses and scratch trades in chop, a minority of large winners in sustained trends. As with all behavioral chart edges (see [[edge-taxonomy]]), the realistic expectation is a modest, cost-sensitive edge that depends far more on discipline than on indicator tuning.

## Capacity limits

Capacity is set by the liquidity of the chosen instruments and the use of stop-entry orders. On large-cap equities, index futures, and major FX, the approach scales to tens of millions before stop entries start moving the market on the trigger bar. On small caps or thin crypto pairs, capacity is far smaller because buy-stops above prior highs are exactly where liquidity thins out. As a discretionary swing method it is naturally low-frequency, which raises capacity but also makes statistical validation slow.

## What kills this strategy

- **Range-bound / choppy regimes:** the weekly trend filter flips repeatedly, generating long-then-short whipsaws (most common failure — see [[failure-modes]]).
- **Trend definition ambiguity:** a flat MACD-Histogram gives no clean signal; discretion creeps in and discipline erodes.
- **Slippage on stop entries:** in fast markets buy-stops fill far above the prior high, destroying the reward-to-risk math.
- **Over-optimisation:** tuning oscillator periods to historical data is classic curve-fitting; the system is meant to be robust, not optimised.
- **Behavioral leakage:** the entire edge is discipline; a trader who overrides the screens "just this once" forfeits it.

## Kill criteria

- Rolling 12-month win rate falls below 40% **and** average reward-to-risk drops below 1.3.
- Maximum drawdown exceeds 30% of allocated capital.
- More than 6 consecutive whipsaw losses attributable to weekly-trend reversals.
- Realised average slippage on stop entries exceeds 1.5x the modeled assumption.

## Advantages

- Resolves the trend-vs-oscillator contradiction by assigning each a role on its own timeframe.
- Enforces trading with the trend and entering on weakness — structurally good risk/reward.
- Indicator-agnostic and works across stocks, futures, FX, and crypto.
- Built-in money management (Elder's 2% and 6% rules) discourages over-leverage.

## Disadvantages

- Discretionary and subjective at the edges (what counts as "trend"?), hard to backtest rigorously.
- Performs poorly in range-bound markets — no built-in regime switch.
- Stop-entry slippage can quietly destroy the reward-to-risk advantage.
- Low trade frequency makes statistical validation and confidence slow to accumulate.

## Sources

- Alexander Elder, *Trading for a Living* (Wiley, 1993) — original description of the Triple Screen Trading System.
- Alexander Elder, *The New Trading for a Living* (Wiley, 2014) — updated treatment with Force Index and Impulse System.
- John J. Murphy, *Technical Analysis of the Financial Markets* — multiple-timeframe analysis context.

## Related

- [[multi-timeframe-confluence]] — the general principle the system formalises
- [[macd-crossover]] — the trend-screen indicator
- [[moving-average-crossover]] — alternative trend filter
- [[stochastic-oscillator]] — alternative second-screen oscillator
- [[trend-following]] — broader strategy family
- [[mean-reversion]] — the pullback-entry component within the trend
- [[macd]] — the trend-screen indicator (concept page)
- [[stochastic]], [[williams-percent-r]] — second-screen oscillator options
- [[technical-analysis-overview]] — the TA strategy hub this method belongs to
- [[indicators-overview]] — concept hub for the indicators used in each screen
- [[edge-taxonomy]] — behavioral edge classification
- [[failure-modes]] — whipsaw and over-optimisation risks
