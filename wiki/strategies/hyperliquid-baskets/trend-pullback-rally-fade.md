---
title: "Trend Pullback / Rally Fade (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, trend-following, mean-reversion, technical-analysis, quantitative, swing-trading]
aliases: ["Pullback Long in Uptrend", "Rally Fade in Downtrend", "Counter-Trend Reentry Basket", "Trend Continuation Pullback"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[macro-trend-regime]]", "[[oi-confirmed-trend]]", "[[major-trend-reclaim-rejection]]", "[[defensive-majors]]", "[[breakout-and-retest]]", "[[range-mean-reversion]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[when-to-retire-a-strategy]]", "[[fibonacci-retracement]]", "[[vwap]]", "[[exponential-moving-average]]"]
strategy_type: algorithmic
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: pilot
edge_source: [behavioral]
edge_mechanism: "Trend-following participants who missed the primary move chase strength; their late entries at trend extremes push price away from value, creating the pullback that disciplined traders fade back into the trend — the late-chaser is the counterparty, systematically entering at worse prices."
data_required: [ohlcv, perp-funding, open-interest, vwap-intraday, fibonacci-levels]
min_capital_usd: 5000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.9
expected_max_drawdown: 0.22
breakeven_cost_bps: 30
kill_criteria: |
  - Basket drawdown > 22% on rolling 6-month basis
  - Rolling 6-month Sharpe < -0.4
  - Win rate on pullback entries drops below 45% over 25 consecutive signals
  - Any held position moves adversely > 25% from entry → cover (exceeded ATR stop buffer)
  - Macro trend regime flips direction → close all positions immediately
deploy_date: 2026-06-10
capital_allocation: "$2,375 maximum allocation capacity as of 2026-06-16"
last_review: 2026-06-16
next_review: 2026-07-16
---

# Trend Pullback / Rally Fade (Hyperliquid Basket)

> **Live status (2026-06-16 dashboard snapshot):** Active basket with $2,375 maximum allocation capacity, matching OI-Confirmed Trend. Trades with the primary trend by entering on counter-trend retracements.

The Trend Pullback / Rally Fade basket trades **with the primary trend by entering on counter-trend moves**. In an uptrend, it buys weakness — entering long positions when price pulls back to a key level (Fibonacci retracement, EMA support, session VWAP) and pullback momentum fades. In a downtrend, it sells strength — entering short positions when price rallies to a key level and rally momentum fades. The critical distinction from pure momentum strategies: this basket **buys weakness in bull trends and sells strength in bear trends**, always trading with the higher-timeframe structure but entering at better prices by waiting for the counter-move to exhaust.

*Part of the [[hyperliquid-baskets-overview|Alfred Hyperliquid basket library]].*

## Edge Source

**Behavioral** (see [[edge-taxonomy]]).

- **Behavioral (chaser capitulation):** When a trend move fires, late-entering trend followers and momentum chasers pile into the move near its exhaustion point — chasing price away from fair value. When this momentum fades (price stalls, RSI diverges, volume drops), those chasing participants are trapped and the pullback accelerates. The basket enters as the chasing momentum exhausts, at a far better price than the original breakout entry.
- **Behavioral (panic exit):** In uptrends, price pullbacks are amplified by stop-triggered exits and margin calls from over-leveraged longs who entered the breakout. These forced exits push price through genuine value levels temporarily, creating the entry opportunity for the basket.

**Honest framing:** This is one of the most widely practised patterns in systematic trading. The edge comes from disciplined execution (waiting for the right level, confirming exhaustion, not early-picking the bottom/top) rather than an obscure or novel signal. The advantage at Hyperliquid scale is the combination with real-time OI, funding data, and the structural clarity of the primary trend.

## Why This Edge Exists

1. **Trend chasers create the pullback.** Momentum is real but overshoots. When a large directional move fires, late participants pile in near the top (or bottom), creating the extension that must subsequently mean-revert back toward the trend's equilibrium. The pullback is the *return to trend*, and it arrives because of over-extension, not despite the trend.
2. **Key levels are self-fulfilling at scale.** [[fibonacci-retracement|Fibonacci levels]] (0.5, 0.618), the [[exponential-moving-average|daily EMA]] (20/50-period), and [[vwap|VWAP]] are watched by enough market participants that they concentrate orders — bids accumulate at 0.618 in an uptrend because multiple systematic and discretionary traders place limits there. This concentration makes the level *work* even without a fundamental reason.
3. **Funding normalises at pullback lows.** In an uptrend, funding can reach extreme positive values at the top of a leg (over-levered longs), then normalise or turn briefly negative during the pullback. The basket enters as funding neutralises — the cost-to-carry reset means a long entered at the pullback low faces zero carry headwind initially.
4. **Lower entry price improves risk/reward.** Entering at the 0.618 retracement of a 15% move means the stop (at the 0.786 level or swing low) is smaller and the target (trend resumption to new high) is larger. The same trend that would have triggered a tight stop on a breakout entry has a healthy 3:1 R/R on a pullback entry.
5. **Counterparty:** over-levered breakout chasers whose stops are below the 0.5 retracement; panic sellers in uptrends who exit at the worst point; late short-sellers in downtrends who chase the rally and are trapped when it fades.

## Null Hypothesis

Under no-edge conditions, entries at Fibonacci/EMA/VWAP levels in an uptrend are no better than random entries within the trend — the trend resumes from any point, and the "level" is a post-hoc rationalisation. The pullback is the beginning of a trend reversal (not a retracement), and entries at "support" become entries in a bear market. The primary trend detection is wrong.

**Disconfirming evidence to monitor:**
- Primary trend frequently reverses after entries (pullback = trend change, not retracement). If trend-reversal rate exceeds 30%, the trend-detection filter needs recalibration.
- Key levels (Fibonacci, EMA, VWAP) are consistently overshot and then recovered — entry is correct but the stop is too tight and fires before the trade works.
- Win rate on pullback entries drops below 45% over 25 consecutive signals.
- Regime shifts during an open position: the macro trend flips direction while the basket is long in an "uptrend" that just ended.

## Rules

**Universe.** All liquid Hyperliquid perps with > $15M/24h volume. In a bull [[macro-trend-regime]]: bias toward longs on pullbacks. In a bear macro trend: bias toward shorts on rallies. Both directions can run simultaneously on different assets.

**Primary trend identification (must confirm before entry):**
1. Price is above the 50-period daily EMA (long bias) OR below the 50-period daily EMA (short bias). [[exponential-moving-average]]
2. A valid swing structure exists: series of higher highs + higher lows (long) or lower highs + lower lows (short).
3. [[oi-confirmed-trend]] signal has fired on this asset within the last 5 days (optional but preferred confirmation).

**Pullback entry signal (long):**
1. Price pulls back from the most recent swing high.
2. Retracement touches the 0.5–0.618 Fibonacci level of the most recent swing leg OR reaches the 20/50-period daily EMA OR reaches the prior session VWAP.
3. Momentum exhaustion: RSI (14) on the 4-hour falls to 40–50 range and begins to recover (oversold within uptrend). [[relative-strength-index]]
4. OI stable or mildly declining during the pullback (passive covering, not fresh shorts building) — if OI is rising sharply during the pullback, the pullback may be a new short trend, not a retracement.
5. Entry: limit order at the level; do not chase if level missed.

**Rally fade entry signal (short):**
1. Price rallies from the most recent swing low in a downtrend.
2. Rally reaches the 0.5–0.618 Fibonacci retracement of the prior down leg OR the 20/50-period EMA from below OR the prior session VWAP.
3. Momentum exhaustion: RSI (14) on the 4-hour reaches 50–60 and begins to roll (overbought within downtrend).
4. OI stable or mildly declining during the rally (passive short-covering, not fresh longs building).
5. Entry: limit order at the level.

**Position sizing:**
- Base size: 2% of book per signal.
- Scale to 3% if confirmation is strong (OI-Confirmed Trend has fired on the same asset within 5 days AND regime is clearly trending).
- Leverage: 2x isolated margin. Never exceed 3x on this basket.
- Stop: 0.786 Fibonacci level (the "level has failed" invalidation), or 2× ATR from entry, whichever is tighter.

**Exit / take-profit:**
- Target 1 (50% of position): prior swing high (long) or prior swing low (short) — the trend resumption level.
- Target 2 (remaining 50%): ATR trailing stop, recomputed each 4-hour close.
- If price reclaims the entry level without triggering Target 1 after 5 days → exit (thesis invalid, trend is choppy not trending).

## Implementation Pseudocode

```python
FIBO_LEVELS   = [0.50, 0.618]
RSI_LONG_ZONE = (40, 50)
RSI_SHORT_ZONE= (50, 60)
LEVERAGE      = 2.0
STOP_FIBO     = 0.786
ATR_STOP_MULT = 2.0
MAX_HOLD_DAYS = 10

def trend_pullback_rally_fade(state, book_size):
    legs = []
    for sym in state.universe:
        if hl_24h_volume(sym) < 15_000_000:
            continue

        trend = get_primary_trend(sym)       # "up" / "down" / "none"
        if trend == "none":
            continue

        swing_high, swing_low = get_recent_swing(sym)
        fib_levels_long  = [swing_low + f * (swing_high - swing_low) for f in [0.50, 0.618]]
        fib_levels_short = [swing_high - f * (swing_high - swing_low) for f in [0.50, 0.618]]
        ema50     = compute_ema(sym, 50, "1d")
        vwap_sess = compute_vwap(sym, "session")
        rsi4h     = compute_rsi(sym, 14, "4h")
        oi_trend  = oi_change_pct(sym, "4h")
        atr14     = compute_atr(sym, 14, "1d")

        # --- Long: pullback in uptrend ---
        if trend == "up":
            at_level = (any(abs(state.price(sym) - fl) < 0.005 * state.price(sym)
                            for fl in fib_levels_long)
                        or abs(state.price(sym) - ema50) < 0.005 * state.price(sym)
                        or abs(state.price(sym) - vwap_sess) < 0.005 * state.price(sym))
            exhaustion = RSI_LONG_ZONE[0] <= rsi4h <= RSI_LONG_ZONE[1] and rsi_is_recovering(sym)
            oi_ok = oi_trend <= 0.01   # OI not rising sharply (avoid fresh-short trend)
            if at_level and exhaustion and oi_ok:
                stop = max(swing_low - 0.005 * swing_low,
                           state.price(sym) - ATR_STOP_MULT * atr14)
                size_mult = 1.5 if oi_confirmed_trend_recently(sym) else 1.0
                legs.append(long_perp(sym,
                                       notional=book_size * 0.02 * size_mult,
                                       leverage=LEVERAGE,
                                       margin="isolated",
                                       stop_price=stop,
                                       target_price=swing_high))

        # --- Short: rally fade in downtrend ---
        elif trend == "down":
            at_level = (any(abs(state.price(sym) - fl) < 0.005 * state.price(sym)
                            for fl in fib_levels_short)
                        or abs(state.price(sym) - ema50) < 0.005 * state.price(sym)
                        or abs(state.price(sym) - vwap_sess) < 0.005 * state.price(sym))
            exhaustion = RSI_SHORT_ZONE[0] <= rsi4h <= RSI_SHORT_ZONE[1] and rsi_is_rolling(sym)
            oi_ok = oi_trend <= 0.01
            if at_level and exhaustion and oi_ok:
                stop = min(swing_high + 0.005 * swing_high,
                           state.price(sym) + ATR_STOP_MULT * atr14)
                legs.append(short_perp(sym,
                                        notional=book_size * 0.02,
                                        leverage=LEVERAGE,
                                        margin="isolated",
                                        stop_price=stop,
                                        target_price=swing_low))

    # --- Time exit: 10 days without target hit ---
    for leg in legs:
        if leg.hold_days >= MAX_HOLD_DAYS and not leg.target_hit:
            leg.action = "close"

    # --- Kill switches ---
    if state.basket_drawdown_6m > 0.22 or state.rolling_6m_sharpe < -0.4:
        return []

    return legs
```

## Indicators / Data Used

- **[[fibonacci-retracement]]** — 0.5 and 0.618 retracement levels of the most recent swing leg; the primary entry zone. The 0.786 level is the stop-invalidation level.
- **[[exponential-moving-average]]** — 20- and 50-period daily EMA as dynamic support/resistance levels within the trend. Source: [[technical-structural-regime]].
- **[[vwap]] / [[vwap-trading]]** — session VWAP as an intraday mean-reversion anchor; price below VWAP mid-session in an uptrend is a potential pullback entry zone.
- **[[relative-strength-index|RSI]]** — 14-period RSI on the 4-hour chart; used as a momentum exhaustion indicator within the trend (40–50 zone in uptrend, 50–60 in downtrend).
- **[[open-interest]]** — OI behaviour during the pullback/rally distinguishes retracement (OI stable/declining) from new-trend-initiation (OI rising).
- **[[funding-rate]]** — funding normalisation during the pullback is a supportive signal; funding extremes during entry are a warning. Source: [[hyperliquid-funding-rate-microstructure]].
- **[[atr-trailing-stop]] / [[average-true-range]]** — 2× ATR stop as the hard invalidation level, and ATR trailing stop for the second half of the position.
- **[[oi-confirmed-trend]]** — sibling basket; a recent OI-confirmed signal on the same asset is optional but preferred confirmation of the primary trend.

## Example Trade

**Illustrative — not a backtest.** Pullback long on ETH-PERP in a bull trend.

Setup: ETH has trended from $2,200 to $2,850 over 3 weeks (the primary up-swing). It then retraces. The 0.618 Fibonacci level of the swing ($2,200 to $2,850) is at $2,446. The 50-day EMA is at $2,430. VWAP on the retracement day is $2,455. RSI-4h has fallen to 44 and is showing a bullish divergence. OI has declined 4% during the pullback (shorts not materially adding — a covering pullback).

| Parameter | Value |
|-----------|-------|
| Confluence zone | $2,430–$2,460 (0.618 Fib + 50 EMA + VWAP) |
| Entry (limit order) | $2,448 |
| Stop (0.786 Fib = $2,197 × adjustment) | $2,340 (approx 2× ATR) |
| Target 1 (50% of position) | $2,850 (prior high) |
| ATR trailing stop target 2 | dynamic |
| Notional | $2,000 (2% of $100K book) |
| Leverage | 2x |

**Scenario A:** ETH resumes trend, reaches $2,850 over 8 days. Take 50% at $2,850 (+16.5%), trail stop on remainder to $2,720, exits at $2,720 (+11%). Net: ~**+$520 on $2,000 notional**.

**Scenario B:** ETH violates $2,340 stop (level failed). Loss: **−$216 on $2,000 notional** (−10.8%). Book impact: −0.22%.

*All figures illustrative. Not a backtest.*

## Performance Characteristics

- **Return shape:** moderate frequency with positive asymmetry when the trend correctly identified — targets are larger than stops because entry is near the low of the retracement, not at the trend's peak. Skew is positive when trend identification is accurate.
- **Expected Sharpe (illustrative estimate):** ~0.8–1.1 in clearly trending regimes; falls sharply in choppy markets where trends reverse after pullbacks (each pullback becomes a reversal).
- **Regime sensitivity:** highest in [[macro-trend-regime]] early-to-mid bull or early-to-mid bear phases; degraded in late-trend distribution and in range-bound [[technical-structural-regime]] regimes.
- **Max drawdown estimate:** ~20–22% in a sequence of failed pullbacks in a market that has transitioned from trend to chop without the macro regime gate catching it.
- **Realistic round-trip cost:** ~25–35 bps per trade (limit entries reduce taker cost; stops and targets can be taker). Funding varies by direction and regime.
- **Funding carry:** typically mildly positive on long entries in bull trends (positive funding means longs pay, but at entry near pullback lows, the funding reset is often near zero). On short entries in bear trends, funding depends on the regime phase (see [[full-bear-short-book]]).

## Capacity Limits

The entry pattern is a limit order at a specific level — not scalable by definition to unlimited size, since very large limit orders at key levels become visible to other market participants and can be front-run. At Alfred's current scale ($2,375), no constraint. At $5M+ per trade, the order should be broken into 3–5 limit tranches across the entry zone. Strategy-level capacity: **$100M** across a diversified universe of 20+ assets.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Trend misidentification — the primary risk.** The strategy assumes a trending market; if the "trend" is actually the later stage of a distribution topping pattern ([[wyckoff-method]]), every pullback is a lower high and the basket accumulates losses at each "buy the dip" entry. The trend confirmation rules (EMA structure, swing structure) mitigate but don't eliminate this.
2. **Level overshoot.** Fibonacci and EMA levels are zones, not exact prices. In high-volatility regimes, price overshoots the 0.618 level to touch 0.786 before recovering. A stop placed at 0.786 may fire on a genuine retracement. Mitigant: use the wider 2× ATR stop rather than the tight Fibonacci invalidation.
3. **Range-bound regime.** In a choppy, sideways market, every swing generates a Fibonacci level, but no trend is present to resume. The basket generates multiple signals, all of which fail at the 50% level. Source: [[range-mean-reversion]] basket — the wrong basket for this environment.
4. **Macro regime flip during hold.** The position is in a pullback long when the trend reverses; the "pullback" becomes a new bear leg and the position is caught holding a losing trade in a new downtrend.
5. **Key level crowding.** Fibonacci and VWAP levels are so widely watched that institutional participants sometimes deliberately run stops below them before reversing; the stop at the 0.786 level gets hit, then price reverses and the trade would have worked.
6. **Funding cost erosion.** In a protracted uptrend with high retail leverage, funding rates can stay persistently positive (0.05–0.10%/8h) even at pullback lows — the carry cost eats into the risk/reward even when the trade direction is correct.

## Kill Criteria

See [[when-to-retire-a-strategy]]. Specific conditions:

- **Basket drawdown > 22%** from rolling 6-month peak → flatten and reassess.
- **Rolling 6-month Sharpe < −0.4** → full review; default to flatten.
- **Win rate on pullback entries < 45% over 25 consecutive signals** → regime has shifted to chop; suspend.
- **Any held position adverse > 25% from entry** → cover; exceeded the stop buffer (likely a trend reversal, not a pullback).
- **Macro trend regime flips direction** → close all open positions within the session.

## Advantages

- **Better entry prices than pure momentum** — entering at the pullback rather than the breakout reduces the stop distance and improves R/R on every trade.
- **Multiple entry opportunities per trend** — a trending asset provides multiple pullbacks over weeks; the basket can compound into the same trend via successive entries.
- **Defined levels = defined risk** — Fibonacci, EMA, and VWAP levels provide objectively defined entry zones and stops, reducing discretionary override.
- **Funding reset at entry** — entering at pullback lows (in uptrends) typically coincides with funding normalisation, so the early holding period often has minimal carry cost.
- **Synergy with OI-Confirmed Trend** — the two baskets complement each other: OI-Confirmed enters on the initial move; Trend Pullback enters on the retracement, achieving a lower average cost basis for the same directional view.

## Disadvantages

- **Requires confirmed trend context** — useless in sideways/choppy markets; the strategy must wait for the macro regime to align, which means periods of low activity.
- **Level overshoot risk** — key levels are zones; the stop placement around 0.786 is an educated estimate, not a guarantee of protection.
- **Timing dependence** — waiting for the "perfect level" means missing trades where the pullback was shallow and the trend resumes from the 0.382 level instead of 0.618.
- **Lag on trend reversal** — if the trend reverses sharply (black-swan, [[policy-shock-regime]]) while the basket is positioned, the stop may gap through on a fast move.
- **Behavioural pressure** — buying into a falling market (during pullbacks) is psychologically difficult; the signal looks wrong at entry, right at confirmation, which creates temptation to override.

## Hyperliquid Execution Notes

- **Funding carry direction:** Long entries in uptrends typically experience positive funding (longs pay); however, at pullback lows funding often normalises or briefly turns negative, providing a near-zero carry period at the ideal entry point. Monitor `predictedFundings` and prefer entries when funding is < +0.05%/8h. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** At 2x leverage, a 50% adverse move reaches liquidation. The 2× ATR stop (typically 15–20% in crypto) is well within this buffer. However, a sudden gap move (exchange hack, cascade event) can skip the stop and approach liquidation — size positions so that even a gap to 30% adverse does not liquidate. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** each leg runs independently. A failed pullback on ETH does not affect the SOL or BTC legs.
- **JELLY-style thin-alt squeeze risk:** For mid-cap pullback longs, confirm > $15M/24h volume gate. A thin-perp long cannot be squeezed in the same way as a short (the long-squeeze is a cascade liquidation, not a coordinated pump), but position sizing discipline applies. Source: [[2025-03-jellyjelly-hlp-attack]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Trend Pullback / Rally Fade as a technical-structural basket in the trend-continuation family.
- [[technical-structural-regime]] — the regime this basket is native to; Fibonacci, EMA, VWAP signals all fall under the technical overlay.
- [[macro-trend-regime]] — the higher-timeframe backdrop that validates trend direction.
- [[fibonacci-retracement]] — the primary entry-level framework.
- [[vwap-trading]], [[vwap]] — VWAP as a mean-reversion anchor for intraday pullback entries.
- [[exponential-moving-average]] — dynamic support/resistance levels within the trend.
- [[hyperliquid-funding-rate-microstructure]] — funding dynamics at pullback lows.

## Related

[[hyperliquid-baskets-overview]] · [[oi-confirmed-trend]] · [[major-trend-reclaim-rejection]] · [[breakout-and-retest]] · [[range-mean-reversion]] · [[defensive-majors]] · [[technical-structural-regime]] · [[macro-trend-regime]] · [[fibonacci-retracement]] · [[vwap]] · [[vwap-trading]] · [[exponential-moving-average]] · [[relative-strength-index]] · [[open-interest]] · [[funding-rate]] · [[atr-trailing-stop]] · [[average-true-range]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[2025-03-jellyjelly-hlp-attack]] · [[wyckoff-method]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
