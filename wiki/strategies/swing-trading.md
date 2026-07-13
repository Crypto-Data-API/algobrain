---
title: "Swing Trading"
type: strategy
created: 2026-04-13
updated: 2026-06-20
status: excellent
tags: [swing-trading, technical-analysis, momentum, stocks, risk-management]
aliases: ["Swing Trader", "Swing Trade"]
strategy_type: technical
timeframe: swing
markets: [stocks, crypto, forex]
complexity: beginner
backtest_status: untested
edge_source: [behavioral]
edge_mechanism: "Captures multi-day continuation and overreaction swings created by investor under-reaction to news and overreaction at extremes; counterparties are impatient intraday traders selling winners early and slow-moving investors who reprice gradually."
data_required: [ohlcv-daily, earnings-calendar]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 30
related: ["[[day-trading]]", "[[position-trading]]", "[[trend-following]]", "[[support-resistance]]", "[[momentum]]", "[[risk-management]]", "[[day-trading-vs-swing-trading]]", "[[linda-raschke]]", "[[technical-analysis-overview]]"]
---

# Swing Trading

Swing trading is a style of trading that attempts to capture short-to-medium-term price moves over a holding period of **days to weeks** (typically 2-20 trading days). It sits between [[day-trading]] (positions closed within a single session) and [[position-trading]] (positions held for months). Swing traders use [[technical-analysis-overview|technical analysis]], [[support-resistance]] levels, momentum signals, and sometimes fundamental catalysts to identify entry and exit points. This page covers the style as a strategy family; the rules below describe the canonical pullback-in-uptrend implementation.

## Core Characteristics

| Dimension | Swing Trading |
|-----------|--------------|
| **Holding period** | 2-20 trading days (sometimes up to a few weeks) |
| **Positions overnight** | Yes — accepts overnight gap risk |
| **Analysis** | Primarily technical; some fundamental/catalyst-driven |
| **Time commitment** | Part-time compatible (check charts 1-2x daily) |
| **Capital required** | Moderate (no PDT rule concerns for US equities if holding >1 day) |
| **Key tools** | [[support-resistance]], [[moving-averages]], [[rsi]], [[macd]], [[volume-analysis]] |
| **Key risk** | Overnight gaps, weekend gaps, earnings surprises |

## Edge source

Per the [[edge-taxonomy]], swing trading is primarily a **behavioral** edge. The multi-day swing exists because prices adjust to new information and flows in steps, not jumps: investors under-react to news initially (anchoring, disposition effect), producing continuation over days-to-weeks, and overreact at short-term extremes, producing snap-backs from oversold pullbacks. The 2-20 day horizon is also a **structural niche**: it is too slow for HFT and intraday players to compete in, and too fast and too small for institutions to bother exploiting in size, leaving the timeframe relatively less arbitraged than either adjacent horizon. Note the candor required here: unlike the cross-sectional [[momentum]] premium, the *discretionary chart-pattern layer* of swing trading has weak academic support — the edge, where it exists, comes from disciplined exploitation of the documented continuation/reversion effects plus rigorous [[risk-management]], not from the patterns themselves.

## Why this edge exists

- **Who is on the other side**: (1) the disposition-effect crowd — holders who sell winners too early into the start of a trend leg, supplying stock to the swing trader on breakouts; (2) panicked or margin-constrained sellers who dump into multi-day pullbacks, supplying the discount at support; (3) slow-moving institutions whose multi-day/multi-week order execution (a fund building a position over two weeks) *creates* the very drift the swing trader rides; (4) impatient intraday traders who exit at the close and forgo the overnight and multi-day component of moves.
- **Why they keep losing (or keep paying)**: the disposition effect and loss-aversion are stable features of human behavior (documented since Shefrin & Statman 1985; Odean 1998) — retail systematically sells winners and holds losers. Institutional execution constraints are mandate-driven and cannot adapt. Intraday traders forgo overnight risk by *choice*; the overnight gap premium they leave on the table is compensation the swing trader collects for bearing gap risk.
- **Honest caveat**: this is a crowded, well-known timeframe. The behavioral effects are real but modest; most of the dispersion in swing-trader outcomes is explained by risk management and trade selection discipline, not by the existence of a large structural premium.

## Null hypothesis

Under no-edge conditions, daily equity returns at the 2-20 day horizon are approximately a random walk with a small positive drift. A swing trader entering on "setups" and exiting at 2:1 reward/risk targets would then show: win rate ≈ 33% (mechanically, from the 2:1 payoff geometry), expectancy ≈ 0 before costs, and *negative* expectancy after paying ~10-30 bps round-trip in spread/slippage/commissions, plus occasional gap-through-stop losses exceeding 1R. Crucially, a no-edge swing trader still produces winning streaks, beautiful-looking chart entries, and profitable quarters by chance. The discriminating test is whether expectancy per trade — (win% × avg win) − (loss% × avg loss) − costs — is reliably positive over 100+ trades, and whether returns survive comparison against a buy-and-hold or time-matched random-entry baseline with identical stop/target geometry.

## Rules

Canonical implementation: pullback-buying in established uptrends (the most-taught and most-documented swing setup; breakout and mean-reversion variants are listed under Common Swing Trading Strategies below).

**Entry**
1. **Identify a trend or range** — is the stock trending (trade pullbacks) or ranging (trade bounces off support/resistance)? For the canonical setup: uptrend defined as price above a rising 50-day [[moving-averages|moving average]], with the 50-day above the 150/200-day.
2. **Wait for a setup** — a 3-10 day pullback to [[support-resistance|support]], a rising moving average, or a trendline; a breakout above resistance; or a reversal candlestick at a key level. Avoid entries within 5 trading days of a scheduled earnings report.
3. **Trigger** — buy on a stop order above the high of the reversal/setup bar (confirmation), not blindly at the level.

**Exit**
4. **Stop-loss** — initial stop below the recent swing low (longs) or above the recent swing high (shorts); never arbitrary. Typical risk per share: 3-7% of price.
5. **Target the next swing** — take profit at the prior swing high, at a measured-move target, or scale out 1/2 at +2R and trail the rest below higher swing lows; exit fully if momentum weakens ([[rsi]] divergence, close below the trailing stop).
6. **Time stop** — if the trade has gone nowhere in 10 trading days, exit; the setup thesis has expired.

**Position sizing**
7. Risk **1-2% of account equity per trade** (position size = risk budget ÷ per-share stop distance); require a minimum reward/risk ratio of **2:1** at entry.
8. Maximum 4-6 concurrent positions; no more than 2 in the same sector/theme (gap and correlation control).

## Implementation pseudocode

```python
# Canonical pullback-in-uptrend swing system (long side)
for stock in liquid_universe:                      # e.g. >$1B mcap, >$10M ADV
    if not (price > sma50 > sma200 and sma50_rising):  continue
    if days_to_earnings(stock) < 5:                    continue
    if pullback_days(stock) < 3 or price > 1.02 * sma50: continue

    setup_bar = last_bar(stock)
    if is_bullish_reversal(setup_bar):             # hammer / engulfing / higher low
        entry  = setup_bar.high + tick
        stop   = swing_low(stock, lookback=10) - tick
        target = prior_swing_high(stock)
        if (target - entry) / (entry - stop) >= 2.0:
            shares = (0.01 * equity) / (entry - stop)   # 1% risk
            place_buy_stop(stock, entry, shares, stop)

# Daily management
for pos in open_positions:
    if pos.unrealized >= 2 * pos.risk:  scale_out(pos, 0.5); trail_stop(pos)
    if pos.bars_held >= 10 and pos.unrealized <= 0:  close(pos)   # time stop
    if earnings_tomorrow(pos):  close_or_resize(pos)
```

## Indicators / data used

- Daily (and weekly, for [[multi-timeframe-confluence]]) OHLCV bars
- [[moving-averages]] — 20/50/200-day for trend definition and pullback zones
- [[rsi]] — overbought/oversold and [[rsi-divergence|divergence]]
- [[macd]] — trend-following crossover confirmation on the daily timeframe
- [[volume-analysis]] — breakout confirmation, accumulation/distribution
- [[support-resistance]] levels and swing highs/lows
- [[atr]] — stop distance and gap-risk-adjusted sizing

## Example trade

A $50,000 account; stock XYZ ($25B cap, $40M ADV) in a confirmed uptrend (price > rising 50-day MA > 200-day MA). After a 4-day, 6% pullback, XYZ tags the 50-day at $48.50 and prints a bullish hammer. Next earnings: 6 weeks away. Buy stop at $49.20 (above the hammer high); initial stop $46.90 (below the swing low; $2.30/share risk); target the prior swing high at $54.00 — reward/risk 2.1:1. Sizing at 1% risk: $500 ÷ $2.30 ≈ 217 shares (round to 215). The order fills next morning; eight sessions later XYZ reaches $53.80, momentum stalls (RSI divergence on a lower-high attempt at $54), and the position is sold at $53.75 — +$4.55/share, ~2.0R, **+$978 gross** (+1.96% of account), less roughly $5-10 in commissions and ~5 bps of spread. Had XYZ instead gapped down through the stop to $45.80 on sector news, the loss would have been ~$731 (1.46% of account, not the planned 1.0%) — the gap-risk overshoot that sizing must anticipate.

## Performance characteristics

Honest, cost-corrected expectations for the style (no canonical backtest exists for "swing trading" as such — `backtest_status: untested` at the style level; specific rule sets must be validated individually):

- **Costs**: liquid US large-caps cost ~2-10 bps spread plus near-zero commissions per side; small-caps 20-50 bps. At 50-150 round-trips/year the strategy must clear ~30 bps round-trip ([[breakeven-cost|breakeven_cost_bps]]) — easy in large-caps, material in small-caps.
- **Realistic profile for a disciplined rule-based trader**: win rate 40-55% at ~1.5-2R average winners, expectancy +0.1 to +0.3R per trade, net Sharpe **0.3-0.7**, annual return mid-single to low-double digits on equity at 1%-risk sizing. Max drawdown expectation **20-30%** through a losing streak of 8-12R (frontmatter: 0.25).
- **Supporting evidence at the horizon**: intermediate-horizon continuation (Jegadeesh & Titman 1993) and short-term reversal effects are documented in academic literature, though both have weakened post-publication and the classic momentum horizon (3-12 months) is longer than the typical swing hold.
- **Base rates**: brokerage-data studies of self-directed traders (e.g., Barber & Odean) consistently show the *median* active retail trader underperforms after costs. Swing trading's part-time compatibility and lower trade frequency reduce, but do not remove, this headwind. The dispersion between disciplined and undisciplined practitioners is the dominant performance factor.
- **Regime sensitivity**: the long-side pullback playbook performs in trending bull regimes and bleeds in choppy/bear regimes; 2022-style grinding downtrends are the classic expectancy-killer for long-biased swing books.

### Regime fit

Swing expectancy is highly conditional on the prevailing [[market-regime]]. Matching the setup variant to the regime is most of the trade selection edge:

| [[market-regime\|Regime]] | Long-side pullback | Breakout | Mean-reversion | Net stance |
|---|---|---|---|---|
| Trending bull (low vol) | strong | strong | weak (snap-backs fail) | full risk, long bias |
| Choppy / range-bound | whipsaws | false breakouts | strongest | trade ranges, reduce size |
| Trending bear | bleeds badly | short-side only | dangerous (catching knives) | reduce/flat or short-side variant |
| High-vol / shock | gaps through stops | unreliable | wide stops needed | cut size, widen stops, fewer names |

The single most expensive mistake is running the long pullback playbook unchanged through a regime change into chop or a downtrend — the setup keeps *looking* valid bar-by-bar while expectancy has already gone negative. Regime awareness is the discretionary overlay that separates disciplined swing books from the median outcome described under Base rates above.

## Capacity limits

Effectively unconstrained at retail scale: a swing trader in large-cap US equities taking $50k-$500k positions is invisible in names trading $10M+ daily. Practical limits appear when single positions exceed ~1% of a stock's average daily volume — entries/exits start paying market impact beyond the modeled 30 bps. For a 5-position book concentrated in mid-caps that binds somewhere in the **$20-50M AUM** range (frontmatter: $50M); restricting to liquid large-caps stretches capacity several-fold but pushes the trader into the most efficiently priced names where the behavioral edge is thinnest. Swing trading is structurally a personal/small-fund strategy, not an institutional one — which is precisely why the niche persists.

## What kills this strategy

1. **Overnight/weekend gap risk** — earnings surprises, M&A, macro shocks gapping through stops; the 1% planned risk becomes 2-4% realized. The defining tail risk of the style.
2. **Regime change** — a trending market turning choppy converts every pullback entry into a whipsaw; long losing streaks (8-12R) arrive in clusters, not uniformly.
3. **Discipline decay** — widening stops, revenge-sizing after losses, holding losers through earnings "to get back to even." The dominant practical killer; the strategy's edge is thin enough that behavioral leaks fully consume it.
4. **Cost creep** — drifting into lower-liquidity names or overtrading until spread/slippage exceeds the per-trade expectancy.
5. **Correlation blindness** — five "different" positions that are all the same trade (e.g., all semiconductor longs) turning a 1%-per-trade book into a 5% single-event loss.
6. **Edge crowding/decay** — the standard setups (50-day pullback, flag breakouts) are universally taught; in heavily scanned large-caps the snap-back increasingly happens before the textbook trigger.

## Kill criteria

Numerical retirement conditions for a live swing book (see [[when-to-retire-a-strategy]]):

- **Stop trading and review** after a drawdown of **15%** from equity high-water mark; **retire or fully rebuild** the rule set at **25%** (the frontmatter expected_max_drawdown is the retirement boundary, not a budget).
- **Retire the setup** if rolling-100-trade expectancy is **below 0R after costs** — at ~1-3 trades/week that is a 12-24 month verdict window.
- **Retire** if rolling 12-month return underperforms a beta-matched buy-and-hold benchmark by more than 10 percentage points for **two consecutive years**.
- **Mechanical circuit-breaker**: 3 consecutive full-R losses in a week → halve size for 20 trades before resuming.

## Swing Trading vs Day Trading

| Dimension | Swing Trading | [[day-trading|Day Trading]] |
|-----------|--------------|------------|
| **Holding period** | Days to weeks | Minutes to hours (closed same day) |
| **Overnight risk** | Yes | No |
| **Time commitment** | Low-medium | High (full-time) |
| **Transaction costs** | Lower (fewer trades) | Higher (many trades) |
| **PDT rule (US)** | Usually not triggered | Applies if >3 day trades in 5 days |
| **Stress level** | Moderate | High |

See [[day-trading-vs-swing-trading]] for detailed comparison.

## Common Swing Trading Strategies

- **Pullback trading** — buy pullbacks to moving averages or trendlines in established uptrends (the canonical rule set above)
- **[[support-resistance-breakout|Breakout trading]]** — enter when price breaks above resistance or below support with volume confirmation
- **[[rsi-divergence|RSI divergence]]** — identify exhaustion in trending moves via divergence between price and RSI
- **[[macd-crossover|MACD crossover]]** — trend-following signals on the daily timeframe
- **Earnings gap strategies** — trade post-earnings momentum or mean-reversion over 2-5 day windows (related: post-earnings-announcement-drift)
- **[[multi-timeframe-confluence|Multi-timeframe confluence]]** — use weekly charts for direction, daily for entry

### Variant comparison

| Variant | Entry trigger | Best regime | Typical win rate | Primary failure mode |
|---|---|---|---|---|
| Pullback (canonical) | reversal bar at rising MA/support | trending bull | 45-55% | regime turns choppy → whipsaw |
| [[support-resistance-breakout\|Breakout]] | break of resistance on volume | trend initiation | 35-45% | false breakout / fakeout |
| [[rsi-divergence\|RSI divergence]] | price/RSI divergence at extreme | exhausting trend | 40-50% | divergence persists; trend continues |
| [[macd-crossover\|MACD crossover]] | signal-line cross on daily | clean trend | 40-50% | lag and chop produce late, whipsawed signals |
| Earnings gap | gap + follow-through (drift) or fade | post-event | varies | binary surprise; the gap *is* the risk |

Across all variants the [[risk-management]] discipline — pre-placed stop, 1-2% risk, minimum 2:1 reward/risk — matters more than the trigger; the variant only sets *when* to look, not whether the trade has positive expectancy.

## Key Practitioners

- [[linda-raschke]] — one of the most prominent swing traders; co-authored *Street Smarts* with Larry Connors
- Mark Minervini — SEPA (Specific Entry Point Analysis) methodology
- Alexander Elder — triple-screen trading system ([[multi-timeframe-confluence]])

## Risk Management for Swing Traders

- **Position sizing**: 1-2% max risk per trade
- **Stop placement**: below the swing low (longs) or above swing high (shorts); never arbitrary
- **Gap risk**: be aware that overnight gaps can jump your stop — size accordingly
- **Earnings dates**: either exit before earnings or size the position to survive a gap
- **Correlation**: avoid having multiple correlated positions (e.g., 5 tech stocks all long)

## Advantages

- Part-time compatible: end-of-day analysis and 1-2 chart checks daily suffice; no screen-watching.
- Lower transaction-cost drag than [[day-trading]] (tens of round-trips per year, not thousands), and no US PDT-rule constraint for accounts under $25k.
- Defined-risk structure: every trade carries a pre-placed stop and a minimum 2:1 reward/risk, making expectancy measurable and reviewable.
- Captures the overnight and multi-day components of moves that intraday traders forgo by construction.
- Low capital threshold ($5k workable) and trivially scalable up to small-fund size in liquid names.

## Disadvantages

- Bears overnight and weekend gap risk — the planned 1R loss is not a hard ceiling; gaps occasionally deliver 2-4R losses.
- Thin underlying edge: at this horizon the documented behavioral premia are modest, and after costs the median self-directed trader underperforms; outcomes depend overwhelmingly on discipline.
- Long-biased pullback playbooks bleed in choppy and bear regimes, and losing streaks cluster (8-12R drawdown sequences are normal, psychologically brutal at part-time engagement levels).
- Setups are universally taught and heavily scanned — crowding erodes the cleanest textbook triggers in liquid names.
- Style-level performance claims are unbacktestable as such; every specific rule set requires its own validation ([[backtesting]], [[overfitting-detection]]).

## Sources

- Raschke, Linda Bradford and Connors, Laurence A. *Street Smarts: High Probability Short-Term Trading Strategies* (1995).
- Minervini, Mark. *Trade Like a Stock Market Wizard* (2013) — SEPA methodology.
- Elder, Alexander. *Trading for a Living* (1993) — triple-screen system.
- Jegadeesh, Narasimhan and Titman, Sheridan. "Returns to Buying Winners and Selling Losers." *Journal of Finance* (1993) — intermediate-horizon continuation evidence.
- Barber, Brad and Odean, Terrance. "Trading Is Hazardous to Your Wealth." *Journal of Finance* (2000) — retail active-trading cost drag.
- Shefrin, Hersh and Statman, Meir. "The Disposition to Sell Winners Too Early and Ride Losers Too Long." *Journal of Finance* (1985).

## Related

- [[day-trading]] — shorter-term trading style
- [[position-trading]] — longer-term trading style
- [[support-resistance]] — key levels for entries and exits
- [[trend-following]] — related momentum approach
- [[momentum]] — the underlying continuation effect
- [[technical-analysis-overview]] — the analytical framework
- [[risk-management]] — managing trade risk
- [[day-trading-vs-swing-trading]] — detailed comparison
- [[edge-taxonomy]] — edge categorization framework
- [[failure-modes]] — generic strategy failure catalog
- [[market-regime]] — regime conditions that flip swing expectancy
- [[atr]] — volatility-adjusted stop and position sizing
- [[when-to-retire-a-strategy]] — kill-criteria framework
- [[backtesting]] / [[overfitting-detection]] — validating any specific rule set
