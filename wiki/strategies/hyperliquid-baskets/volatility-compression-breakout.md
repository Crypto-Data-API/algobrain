---
title: "Volatility-Compression Breakout (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, technical-analysis, breakout, volatility, swing-trading, quantitative]
aliases: ["Vol Compression Breakout", "Squeeze Breakout", "Coiled Spring Breakout", "Low-Vol Expansion Trade"]
related: ["[[hyperliquid-baskets-overview]]", "[[volatility-regime-classification]]", "[[technical-structural-regime]]", "[[bollinger-bands]]", "[[atr]]", "[[average-true-range]]", "[[garch-volatility]]", "[[volatility-carry]]", "[[breakout-trading]]", "[[breakout-and-retest]]", "[[range-breakout-breakdown]]", "[[failed-breakout-failed-breakdown]]", "[[range-mean-reversion]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[hyperliquid]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-oracle-mechanics]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[open-interest]]", "[[funding-rate]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]", "[[overfitting-detection]]", "[[crypto-perp-backtesting-pitfalls]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, behavioral]
edge_mechanism: "Prolonged volatility compression concentrates stop-loss and breakout orders at a narrow price zone; when compression resolves, the burst of mechanical order flow is disproportionate to the range size, and a pre-positioned participant captures the initial expansion move before market makers can reprice the vol surface."
data_required: [ohlcv, atr, bollinger-bands, bollinger-band-width, historical-volatility-percentile, open-interest, funding-rate, volume]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.60
expected_max_drawdown: 0.25
breakeven_cost_bps: 40
kill_criteria: |
  - Rolling 6-month drawdown > 25% of strategy book
  - Rolling 12-month net Sharpe < 0 over ≥ 20 completed trades
  - Compression signals that fail to expand (price stays compressed > 10 bars post-signal) > 70% of last 30 signals
  - Average realised volatility expansion post-entry < 50% of ATR(14) at entry over 20 completed trades
---

# Volatility-Compression Breakout (Hyperliquid Basket)

Monitors [[bollinger-bands|Bollinger Band width]], [[atr|ATR]], and historical volatility percentiles to identify periods of **abnormally low volatility** — compression. After prolonged compression, volatility typically expands sharply in one direction. This basket **pre-positions** before the directional break (or enters on an early breakout trigger), targeting the explosive directional move when compression resolves. The setup is often described as a coiled spring: the longer and tighter the compression, the more potential energy stored, and the larger the expected expansion.

*Part of the [[hyperliquid-baskets-overview|Alfred Hyperliquid basket library]].*

> **Not investment advice.** This page is a design document for a systematic trading basket. All performance figures are ILLUSTRATIVE ESTIMATES.

## Edge Source

**Structural + behavioral** (see [[edge-taxonomy]]).

- **Structural**: [[volatility-regime-classification|Volatility regimes]] are mean-reverting. Realised volatility compressed below the historical 10th percentile is a structural anomaly — it represents a temporary equilibrium that cannot persist indefinitely because it implies reduced uncertainty, which attracts leveraged positioning that ultimately resolves through directional price discovery. This mean-reversion in volatility is the structural edge; the basket is long the expansion.
- **Behavioral**: During compression, many systematic strategies de-leverage or pause (stops are too tight, ATR-based position sizes are too large, range-fade strategies dominate). This creates a positioning imbalance — directional participants are undersized going into the expansion. When compression resolves and stops are clustered in a narrow zone, the resulting cascade is larger than the compressed ATR would predict.

## Why This Edge Exists

The counterparties are market participants who **sell volatility** during the compression: range-fade strategies (like [[range-mean-reversion]]) that collect the short edge of each oscillation, options market-makers who write near-term vol at compressed levels, and mean-reversion algorithms that interpret low volatility as "safe" and take on larger positions at leverage. All of them are wrong at the moment of expansion.

The compression-to-expansion dynamic is mechanically reproducible because compression accumulates resting orders at a narrow price zone. A large directed order — news, a whale accumulating, an options expiry cascade — encounters shallow absorbing liquidity in the compressed zone and moves price disproportionately. Market-maker hedging flows amplify the move (their delta exposure changes rapidly as vol expands), and systematic programs that were dormant during compression fire their trend/breakout entries simultaneously.

**Key distinction from [[range-breakout-breakdown]]:** that basket enters on a level break in a pre-defined range, targeting the measured move from the range height. This basket enters based on **volatility percentile**, not range geometry — it fires even when there is no obvious horizontal range, merely compressed ATR. It is a regime-detection trade, not a pattern-matching trade. The two are complementary: a horizontal range coincides with volume compression in most cases, so the [[range-breakout-breakdown]] entry often occurs *inside* a volatility-compression setup; this basket may pre-position *before* the range boundaries are definitively broken.

## Null Hypothesis

Under a null hypothesis, periods of low historical volatility carry no predictive information about the direction or timing of subsequent expansion. Vol compression is simply a random draw from the vol distribution; the next period's vol is equally likely to be compressed or expanded regardless of the prior state. A strategy that systematically pre-positions at vol extremes would earn no return before costs — in fact, it would **lose** (due to adverse carry on pre-positioned delta and the cost of being too early) relative to entering only after the directional break is confirmed.

**Disconfirming evidence to monitor:**

- If the average holding time before meaningful expansion exceeds 20 bars, the "coiled spring" is slow to resolve and carry costs / opportunity costs erode the edge.
- If directional accuracy of the expansion move (does price go the predicted direction vs. the pre-position direction?) is no better than 50%, the pre-positioning component is noise — better to wait for the first breakout bar and enter directionally, like [[range-breakout-breakdown]].
- If vol-expansion after compression is not significantly larger than vol-expansion from a random-state starting point, the compression signal is not a useful predictor of magnitude.

**Key risk to the thesis:** volatility-expansion prediction has a well-documented overfitting problem in backtests — see [[overfitting-detection]] and [[crypto-perp-backtesting-pitfalls]]. Compression signals are visually compelling in hindsight but harder to trade in real time because the direction is unknown at compression time.

## Rules

**Universe:** Hyperliquid perpetuals with $15M+ 24h volume. Sufficient history required for reliable percentile calculations (at least 30 bars of ATR data on the reference timeframe).

**Step 1 — Compression detection:**
- **Bollinger Band Width (BBW):** `BBW = (Upper BB - Lower BB) / Middle BB`. Signal fires when BBW reaches its lowest level in the past 20 bars (local minimum), especially when BBW is also at or below the 15th percentile of its 90-bar historical distribution. This is the "Bollinger Band Squeeze" (John Bollinger).
- **ATR percentile:** ATR(14) on the 4h timeframe is at or below the 10th percentile of its 90-bar rolling distribution.
- **Volume contraction:** 5-period average volume is declining and below the 90-bar 25th percentile. Volume compression often precedes price-volatility compression.
- **Require at least 2 of 3 criteria satisfied for 2+ consecutive bars** — avoids single-bar noise triggers.

**Step 2 — Direction assessment (optional but preferred):**
The compression signal is direction-agnostic. Use the following to bias the pre-position:
- Trend context: if price is above the [[exponential-moving-average|EMA(50)]] and [[200-day-moving-average|200-day MA]], lean long.
- OI skew: if [[open-interest|OI]] is growing while compression holds, the dominant positioning direction (visible in HL's public data) biases the likely expansion direction.
- [[funding-rate|Funding rate]] sign: persistent positive funding suggests long bias (market leaning long, squeeze is down; genuine trend is up). Use as a tiebreaker, not a primary signal.
- If direction is ambiguous, use a **straddle-equivalent approach**: pre-position a smaller size long + a smaller size short, and size up the direction that breaks first.

**Step 3 — Pre-position or breakout entry:**

*Pre-position (preferred when direction is assessable):*
- Enter a directional small position (50% of target size) at the compression signal.
- Leverage: 1.5–2× isolated margin.
- Stop: 1.0× ATR(14) from entry (wider than standard, to survive normal compression noise).

*Breakout entry (direction-confirming):*
- On the first bar that closes outside the 20-period BB (or breaks the 20-bar high/low), enter with full target size.
- Stop: 0.5× ATR(14) below/above the breakout bar close.
- This approach has higher conviction and lower holding cost, but worse average entry price vs. the pre-position.

*Combined:*
- Pre-position at compression signal; add to full size on the directional breakout bar (size = 50% + 50%). Average entry between compression signal and breakout close.

**Step 4 — Target and management:**
- **Target:** 1.5–3× ATR(14) from entry (the typical vol-expansion magnitude from compression), or a visible structural level (prior swing high/low).
- Switch to [[atr-trailing-stop|ATR trailing stop]] (2× ATR) once position is 1× ATR in profit.
- If compression persists > 10 bars after the signal without expansion, tighten the pre-position stop to 0.5× ATR — the setup is staling; energy may dissipate rather than expand.
- If the opposing direction breaks first (pre-positioned wrong direction), close the pre-position stop-loss immediately; reverse into the breaking direction with the breakout-entry rules.

**Regime gate:** specifically suited to [[volatility-regime-classification|low-volatility compression states]] within [[technical-structural-regime|technical/structural]] consolidation. Suppress when [[volatility-regime-classification|volatility is already expanded]] (entering after vol has expanded is chasing, not positioning into expansion). This basket should also suppress when [[range-mean-reversion]] is at full deployment — the two share the "range structure is intact" precondition but trade opposite regime transitions.

## Implementation Pseudocode

```python
def vol_compression_breakout(universe, bars_4h, state):
    signals = []

    for asset in universe:
        b    = bars_4h[asset]
        atr  = ATR(b, period=14)
        bb   = BollingerBands(b.close, period=20, std=2)
        vol  = b.volume
        ema50 = EMA(b.close, period=50)

        # Step 1: compression detection
        bbw       = (bb.upper - bb.lower) / bb.middle
        bbw_pct   = percentile_rank(bbw, lookback=90)  # 0–100
        atr_pct   = percentile_rank(atr, lookback=90)
        vol_5avg  = SMA(vol[-5:], period=5)
        vol_pct   = percentile_rank(vol_5avg, lookback=90)

        compressing_bbw = bbw[-1] <= min(bbw[-20:]) and bbw_pct[-1] < 15
        compressing_atr = atr_pct[-1] < 10
        compressing_vol = vol_pct[-1] < 25 and vol_5avg[-1] < vol_5avg[-6]

        criteria = sum([compressing_bbw, compressing_atr, compressing_vol])
        if criteria < 2:
            continue  # not enough compression

        # Require compression for 2+ consecutive bars
        if not state.compression_confirmed(asset, min_bars=2):
            state.mark_compression(asset)
            continue

        # Hard suppress: vol already expanded
        if atr_pct[-1] > 60:
            continue

        # Step 2: direction bias
        trend_up = b[-1].close > ema50[-1]
        funding  = state.funding_rate(asset)[-1]
        oi_skew  = state.oi_directional_skew(asset)  # +1 long-biased, -1 short-biased

        direction_score = (
            (1 if trend_up else -1) +
            (1 if funding > 0 else -1) +
            oi_skew
        )
        # +3 = strong long bias; -3 = strong short bias; 0 = neutral

        # Step 3a: pre-position
        if not state.has_preposition(asset, "vcb"):
            if direction_score >= 2:
                stop = b[-1].close - 1.0 * atr[-1]
                signals.append(long_perp(asset,
                    size=position_size_atr(state.equity, 0.005,
                                           b[-1].close, stop, 2, "isolated"),
                    stop=stop, tag="vcb_pre"))
            elif direction_score <= -2:
                stop = b[-1].close + 1.0 * atr[-1]
                signals.append(short_perp(asset,
                    size=position_size_atr(state.equity, 0.005,
                                           b[-1].close, stop, 2, "isolated"),
                    stop=stop, tag="vcb_pre"))

        # Step 3b: breakout entry (add or initiate)
        broke_up   = b[-1].close > bb.upper[-1]
        broke_down = b[-1].close < bb.lower[-1]

        if broke_up:
            stop   = b[-1].close - 0.5 * atr[-1]
            target = b[-1].close + 2.0 * atr[-1]  # 2× ATR expansion target
            rr     = (target - b[-1].close) / (b[-1].close - stop)
            if rr >= 1.5:
                signals.append(long_perp(asset,
                    size=position_size_atr(state.equity, 0.010,
                                           b[-1].close, stop, 2.5, "isolated"),
                    stop=stop, target=target,
                    trail=2.0 * atr[-1], tag="vcb_break"))

        elif broke_down:
            # mirror for short
            pass

        # Stale compression kill
        if state.compression_bars(asset) > 10:
            state.tighten_preposition_stop(asset, 0.5 * atr[-1])

    return signals
```

## Indicators / Data Used

- **[[bollinger-bands|Bollinger Band Width (20, 2)]]** — primary compression detector; local and percentile minimum signals the "Bollinger Squeeze"
- **[[atr|ATR(14)]]** — compression severity (percentile rank), stop distance, target sizing via [[atr-position-sizing]], trailing exit via [[atr-trailing-stop]]
- **Historical volatility percentile (90-bar rolling)** — normalises ATR and BBW across assets with different absolute price levels
- **Volume** — compression confirmation; volume contraction during price compression strengthens the coiled-spring setup
- **[[exponential-moving-average|EMA(50)]]** — trend direction bias for pre-positioning direction
- **[[open-interest|Open Interest]]** — directional OI skew as a tiebreaker for pre-position direction; OI expansion on the breakout bar confirms genuine new positioning
- **[[funding-rate|Funding rate]]** — directional tiebreaker; adverse carry monitoring during the hold
- **[[garch-volatility|GARCH-family volatility models]]** — optional; GARCH(1,1) conditional volatility provides a more rigorous compression signal than BBW for quantitative implementations. BBW remains the primary real-time signal due to its simplicity and real-time availability.

## Example Trade

**Illustrative only — not a backtest.**

| Field | Detail |
|-------|--------|
| Asset | NEAR-PERP |
| Compression | 6 bars (4h), BBW at 4-month low (8th percentile), ATR(14) at 9th percentile; volume declining |
| Direction bias | Price above EMA(50) +1; funding +0.015%/8h +1; OI neutral 0 → score +2 → long bias |
| Pre-position | Long at $4.82, 1.5× margin, stop at $4.68 (−1× ATR) |
| Breakout bar | 2 bars later: closes above upper BB at $4.98; OI +11% |
| Add to position | Full size added at $4.99, stop moved to $4.78 (below breakout bar low) |
| Target | $5.38 (2× ATR from breakout close) |
| Outcome (illustrative) | Target reached in 32h; +7.8% on notional, ~+13% blended margin (pre-position + breakout add) |

No mean-reversion occurred; the range-mean-reversion basket held no position on this asset (ATR was too compressed to qualify its range-entry criteria at normal leverage).

## Performance Characteristics

ILLUSTRATIVE ESTIMATES based on volatility-compression strategy literature and perp-market characteristics:

- **Win rate:** ~40–50% directional (lower than [[range-mean-reversion]] due to direction uncertainty; improved by the direction-bias scoring); pre-position component without direction scoring is closer to 35%
- **Payoff ratio:** ~2.5–4.0:1 — the defining feature of this basket. A vol-expansion from the 10th percentile to the median typically produces a move of 2–4× the compressed ATR, offering unusually large payoffs relative to the stop distance
- **Expected Sharpe:** ~0.50–0.70 net in environments with sufficient compression-expansion cycles; the return is lumpy and event-driven
- **Max drawdown:** ~20–28% — driven by sequences where compression signals fail to expand, bleeding pre-position carry and stop-out costs
- **Cost overlay:** 40–55 bps round-trip per trade. The pre-position component held before the breakout bar adds carry cost (funding-dependent, typically small) and one additional round-trip cost if the direction is wrong.
- **Return shape:** highly lumpy — long flat or small-loss periods during persistent compression (stale setup costs), punctuated by explosive winning trades when vol expands sharply. Very positive skew. This basket is the natural regime-aware companion to [[volatility-carry]] strategies, which earn in the flat periods this basket finds dry.
- **Regime timing quality:** this basket's key skill is detecting compression — the subsequent expansion is often inevitable; the question is when and in which direction. Early pre-positioning (compression only) has higher false-positive costs than waiting for the breakout bar (higher direction confidence, worse fill).

## Capacity Limits

Limited by the liquidity of the breakout bars themselves — the moment vol expands, the entry is a market-order taker fill in a fast-moving market. For BTC and ETH, single-position capacity is $3M+ before breakout-bar slippage matters. For mid-cap perps, the compressed state often coincides with thin order books (market makers reduce depth during slow periods), making the expansion entry more expensive. **Strategy-level capacity: ~$20M** across 4–6 concurrent compression setups — similar to [[range-breakout-breakdown]] but with higher slippage due to the volatility-expansion entry timing.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Compression that dissipates without expanding.** The market remains compressed for much longer than expected, then vol normalises without a directional explosion. Pre-positioned capital bleeds small carry costs; the stale-compression stop tightening eventually exits the position for a small loss. This is the most common outcome — not all compressions produce coiled-spring expansions.
2. **Expansion in the wrong direction.** The pre-position direction is wrong; the breakout fires the opposite way. The pre-position stop exits (loss); the breakout-entry rule can then enter the correct direction (the combined pre+breakout entry approach explicitly handles this).
3. **False breakout post-compression.** A compression followed by a brief expansion that immediately reverses — the basket enters on the breakout bar and is immediately stopped out. This is more damaging post-compression because the ATR stop is tighter. The [[failed-breakout-failed-breakdown]] basket would then enter counter to this move.
4. **Crowded compression signal.** Bollinger Squeezes are widely known and discussed in retail trading communities; crowded entries on the first breakout bar worsen fills and increase false-breakout rates. The OI expansion confirmation filter partially mitigates this.
5. **Liquidation cascade during the expansion.** A vol-expansion into a broad deleveraging event ([[2025-10-crypto-liquidation-cascade]]) catches the long pre-position on the wrong side of a forced liquidation wave. Isolated margin limits damage.
6. **JELLY squeeze risk (long → short reversal) on thin alts.** A coordinated buying spike on a thin perp can look exactly like a compression breakout to the upside; the basket enters long; the spike reverses for a loss. Filter: OI must expand on the breakout bar (not just price moving up).
7. **Overfitting in backtest selection.** The combination of BBW percentile + ATR percentile + volume contraction has many degrees of freedom — this is a well-known overfitting surface in technical strategy design. See [[overfitting-detection]] and [[crypto-perp-backtesting-pitfalls]]. The strategy is marked `naive-backtested` precisely because a rigorous walk-forward validation has not yet been completed.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the full framework.

- Rolling 6-month drawdown > **25%** of strategy book → halt, full review
- Rolling 12-month net Sharpe < **0** over ≥ 20 completed trades → stop new entries
- Compression signals that fail to expand (price stays compressed > 10 bars post-signal) > **70%** of last 30 signals → compression is not predictive in current market regime; pause the basket
- Average realised volatility expansion post-entry < **50% of ATR(14) at entry** over 20 completed trades → the "coiled spring" is not releasing meaningfully; recalibrate percentile thresholds

## Advantages

- Pre-positioned before the move — the best average entry price of any breakout basket when the direction is correctly assessed
- Naturally captures explosive moves that other baskets miss (those that enter on the confirmed breakout bar often get poor fills during the sharpest vol-expansion bars)
- Very positive skew — a single correct compression-expansion capture can dwarf many small losses
- Regime-detection based rather than pattern-matching — fires on true volatility anomalies rather than arbitrary range geometries
- [[bollinger-bands|Bollinger Band width]] squeeze is computable in real time on any timeframe; simple and auditable
- Can run simultaneously with [[range-mean-reversion]] on the same asset during the compression phase (they share the "quiet market" precondition), but should coordinate exit if this basket's breakout entry fires

## Disadvantages

- Direction uncertainty during the pre-position phase is the fundamental challenge — straddle-style pre-positioning doubles the trade cost and management complexity
- Stale compressions are expensive: hold the pre-position through 5–10 bars of slow drift, then it breaks in the wrong direction, doubling the loss
- Higher implementation complexity than the other four baskets — requires BBW percentile calculation, ATR percentile, volume percentile, and directional scoring in real time
- Naive backtests are unreliable for this strategy due to overfitting risk (see [[overfitting-detection]], [[crypto-perp-backtesting-pitfalls]]); performance expectations should be treated as rough estimates until walk-forward validation is complete
- Market-maker depth tends to be thinnest exactly when this basket wants to enter (during or just after compression) — slippage estimates must be wider than for range-fade baskets with limit-order entries
- Correlation with [[range-breakout-breakdown]]: both trade breakouts from consolidation. In many setups they fire simultaneously — coordinate to avoid double-sizing the same directional bet on the same asset

## Hyperliquid Execution Notes

- **Funding carry during compression:** in a compressed volatility environment, funding tends to be near zero or mildly oscillating — the position carries cheaply during the pre-position phase. If funding turns markedly negative during compression (shorts paying significantly), that directional signal strengthens the long pre-position case and vice versa. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation:** the wide pre-position stop (1× ATR) is intentional — compression bars can have deceptive wicks. Sizing based on the wider stop at 1.5–2× leverage ensures no liquidation on a normal wick through the stop level. Tighten to 0.5× ATR only after the breakout bar confirms direction. Source: [[hyperliquid-liquidation-engine]].
- **Oracle mechanics during compression:** Hyperliquid's mark price is an index average ([[hyperliquid-oracle-mechanics]]). During low-liquidity compression periods, the index may deviate briefly from individual exchange prices. Verify that BBW compression is reflected in the *mark price* series, not just one spot exchange, before treating it as a signal.
- **JELLY risk during the breakout bar:** the breakout bar in a thin-alt perp can be an engineered spike rather than genuine vol expansion. The OI expansion filter (OI must increase ≥ 8% on the breakout bar) is the primary guard — an engineered spike that doesn't attract new open interest is a stop-hunt, not vol expansion. Source: [[2025-03-jellyjelly-hlp-attack]].
- **ADL during sharp expansion:** an explosive vol-expansion move that goes strongly in the trade's favour can trigger ADL (auto-deleveraging) if the counterparty pool is thin — winners are force-closed at the mark price. Use isolated margin and monitor ADL queue position during fast-moving bars post-compression. Source: [[hyperliquid-liquidation-engine]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket regime framework; this basket is the primary [[volatility-regime-classification]] transition strategy
- [[bollinger-bands]] — Bollinger Band width (squeeze) methodology: John Bollinger's original specification of the BBW squeeze as a low-volatility precursor to expansion
- [[volatility-regime-classification]] — the regime overlay this basket is designed to trade; defines compression states and expansion triggers
- [[garch-volatility]] — GARCH-family conditional volatility models; the rigorous quantitative alternative to BBW for compression detection
- [[volatility-carry]] — complementary strategy that earns in the compressed-vol periods this basket considers dry; the two are natural portfolio complements
- [[breakout-trading]] — foundational breakout page; ATR filter and volume-compression criteria documented there
- [[overfitting-detection]], [[crypto-perp-backtesting-pitfalls]] — critical references for evaluating backtest validity of multi-parameter volatility strategies
- [[hyperliquid-funding-rate-microstructure]], [[hyperliquid-liquidation-engine]], [[hyperliquid-oracle-mechanics]] — venue execution
- [[2025-03-jellyjelly-hlp-attack]] — thin-alt squeeze case study for OI filter importance

## Related

[[range-breakout-breakdown]] · [[breakout-and-retest]] · [[failed-breakout-failed-breakdown]] · [[range-mean-reversion]] · [[breakout-trading]] · [[bollinger-bands]] · [[atr]] · [[average-true-range]] · [[atr-trailing-stop]] · [[atr-position-sizing]] · [[garch-volatility]] · [[volatility-carry]] · [[volatility-regime-classification]] · [[technical-structural-regime]] · [[exponential-moving-average]] · [[open-interest]] · [[funding-rate]] · [[overfitting-detection]] · [[crypto-perp-backtesting-pitfalls]] · [[hyperliquid]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-oracle-mechanics]] · [[2025-03-jellyjelly-hlp-attack]] · [[2025-10-crypto-liquidation-cascade]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
