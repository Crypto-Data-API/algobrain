---
title: "Post-Liquidation Rebound (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, liquidation, mean-reversion, behavioral-finance, market-microstructure, scalping, derivatives]
aliases: ["Flush Bounce", "Post-Cascade Mean Reversion", "Liquidation Exhaustion Entry", "Deleveraging Rebound"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[security-black-swan-regime]]", "[[liquidity-depth-regime]]", "[[liquidation-cascade-fade]]", "[[short-liquidation-squeeze]]", "[[long-liquidation-cascade]]", "[[crowded-short-funding-fade]]", "[[crowded-long-funding-fade]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-10-crypto-liquidation-cascade]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[liquidation]]", "[[long-liquidation]]", "[[open-interest]]", "[[leverage]]", "[[rsi]]", "[[relative-strength-index]]", "[[order-flow]]", "[[mean-reversion]]", "[[funding-rate]]", "[[coinglass]]", "[[atr-trailing-stop]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: quantitative
timeframe: scalp
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [behavioral, structural]
edge_mechanism: "Post-liquidation markets are cleaner — weak, over-levered hands have been flushed; the forced sellers have exhausted their supply; the remaining position holders are better-capitalised; price typically mean-reverts sharply from the liquidation extreme as the panic bid returns and the underlying asset reaches fair value again."
data_required: [perp-funding, open-interest, liquidation-feed, order-book-depth, mark-price, rsi]
min_capital_usd: 5000
capacity_usd: 8000000
crowding_risk: medium
expected_sharpe: 1.0
expected_max_drawdown: 0.28
breakeven_cost_bps: 35
kill_criteria: |
  - Win rate drops below 52% over trailing 25 completed trades
  - Three consecutive full stop-outs (each > 8% loss on position)
  - Average exit time approaches the 6-hour time stop (> 50% of trades time-stopping rather than target-hitting)
  - Drawdown > 25% on this basket over rolling 6 months
---

# Post-Liquidation Rebound (Hyperliquid Basket)

A [[mean-reversion]] strategy that enters **immediately after a significant liquidation event has flushed overleveraged positions from the market**. The logic: once a cascade of forced liquidations has completed, the market is structurally cleaner — weak hands are gone, the forced supply (or demand) that caused the overshoot has exhausted itself, and remaining position holders are better-capitalised. Price typically mean-reverts sharply from the liquidation extreme as patient capital re-enters and the asset reprices toward fair value. Entries are timed using liquidation volume spikes, [[rsi|RSI]] oversold/overbought readings at the flush point, and order-flow exhaustion signals.

*Part of the [[hyperliquid-baskets-overview|Alfred Hyperliquid basket library]].*

---

## Relationship to [[liquidation-cascade-fade]]

This basket is the **closest sibling to the existing [[liquidation-cascade-fade]] page** in the Alfred wiki. Both strategies:
- Enter in the direction opposite to the completed liquidation flush
- Target mean-reversion to the pre-cascade level
- Use liquidation volume spikes as the primary timing signal

**The key distinction:** [[liquidation-cascade-fade]] uses a precise **CVD exhaustion signal** (cumulative volume delta slope flattening) as the entry trigger and has a strict 4-hour time stop. This basket is broader and more regime-aware:
- Adds **RSI oversold/overbought confirmation** at the flush extreme
- Supports **both long (post-long-cascade) and short (post-short-squeeze) entries** — the fade is long-only
- Emphasises the **post-flush "clean market" structural improvement** as the core edge (not just the panic premium)
- Designed for Hyperliquid's specific context: hourly funding, mark-price liquidations, HLP recovery dynamics
- Has a longer maximum hold (6 hours vs 4 hours) to capture the multi-hour rebound rather than just the initial snap

Think of the cascade fade as the *precision* implementation and this basket as the *regime-aware, bidirectional* implementation. Where both signals fire simultaneously, the cascade fade's tighter CVD filter is preferred; this basket fills in when the CVD signal is ambiguous but RSI + liquidation volume are clear.

---

## Edge Source

**Behavioral** + **structural** (see [[edge-taxonomy]]).

- **Behavioral (primary).** Liquidation cascades produce acute panic: discretionary traders pull their bids (or offers in a short squeeze), social media amplifies the fear (or frenzy), and the marginal price-setter during the cascade is a forced liquidation engine — not a fundamental investor. Once the cascade ends, the panic has passed. Rational buyers (or sellers) re-enter, repricing the asset toward fair value. The post-flush entry exploits the *recency bias* of traders who continue avoiding the market long after the panic selling has ended.
- **Structural (secondary).** The structural improvement of the market is real and quantifiable:
  - **Open interest contracts sharply** — the overleveraged long (or short) book has been partially destroyed; the remaining book is healthier.
  - **Funding rate normalises** — the crowding signal that preceded the cascade (extreme positive or negative funding) has been partially or fully reversed by the forced position closures.
  - **Bid-ask spreads temporarily widen then tighten** as market makers re-enter after the cascade; the reentry of passive liquidity is itself a mean-reversion force.

---

## Why This Edge Exists

A post-cascade market has a specific microstructure that differs from a normal market:

1. **Forced supply is exhausted.** The liquidation engine has completed its orders. Every long (or short) below (or above) maintenance margin has been forced out. There are no more forced sellers (buyers) — only willing market participants remain.
2. **Surviving positions are stronger.** A long position that survived a 15% cascade has substantial margin buffer. These holders are not scared out by the next 3% move; they are a more stable base.
3. **Funding normalisation creates a buyer incentive.** If the cascade was a long liquidation (pushing price down), funding may have gone deeply negative during the cascade (as the perp dropped below oracle). Deeply negative funding means shorts are now paying longs — creating a structural incentive for new longs to enter and shorts to close. See [[hyperliquid-funding-rate-microstructure]].
4. **RSI oversold signal.** An [[rsi|RSI]] reading of 20–30 at the bottom of a cascade captures the quantified "this asset has fallen too far, too fast" condition that historically mean-reverts.
5. **Historical evidence.** The October 2025 cascade ([[2025-10-crypto-liquidation-cascade]]) saw BTC drop to specific levels and recover sharply within hours; the March 2025 JELLY squeeze ([[2025-03-jellyjelly-hlp-attack]]) saw the targeted pair force-settled — but the broader BTC/ETH market recovered within a day. The August 2024 yen carry unwind (documented in [[liquidation-cascade-fade]]) saw BTC recover from $49,000 to $54,000 within 2 hours of cascade exhaustion.

**Who is on the other side?** Late momentum-following traders who continue selling *after* the cascade has ended (chasing the move), and short-sellers who entered near the bottom expecting continuation — both are wrong in expectation once the forced supply is exhausted.

---

## Null Hypothesis

Under "no edge," liquidation cascades are not overshoots — they are fair value repricing events. In this null, post-cascade price should not systematically recover toward the pre-cascade level; the RSI-oversold and liquidation-volume-spike signals would not predict positive returns; mean reversion would not occur faster than expected by chance.

Empirically this null is *partially* rejected: post-cascade 4-hour returns are positively skewed in historical data across the 2022-2025 window (see [[liquidation-cascade-fade]] for detailed evidence). **However, the null is not rejected for regime-shift cascades** — LUNA, FTX, 3AC are canonical cases where the cascade correctly repriced the asset to a much lower equilibrium and no meaningful rebound occurred. The strategy's key empirical failure mode is regime-shift misclassification, identical to the cascade fade.

**Disconfirming evidence to monitor:**
- Average exit time approaches the 6-hour time stop (more than 50% of trades) — mean reversion is not occurring in the design window.
- Win rate below 52% over 25 trades — the post-flush clean-market thesis is not holding.
- Funding does not normalise after cascade (remains deeply one-sided for > 6 hours) — a structural regime shift rather than an overshoot.
- Open interest does *not* contract significantly after the cascade — the position book is not improving; new leveraged entries are immediately replacing the liquidated ones.

---

## Rules

**Universe:** Any Hyperliquid perp with a meaningful liquidation event. Unlike the other baskets (which have specific regime restrictions), this basket is event-driven and can activate on any pair where the flush signal fires — including mid-caps. However, size down significantly on thin pairs due to reversal-slippage risk.

**Entry criteria (post-long-cascade — enter long):**
1. **Liquidation volume spike:** 5-minute liquidation notional on the target pair ≥ 3× the trailing 24-hour mean (confirms a genuine cascade, not normal volatility). Source: [[coinglass]], native HL liquidation feed.
2. **Price drop:** Mark price has fallen ≥ 3% in the trailing 15 minutes.
3. **RSI oversold:** [[rsi|RSI]] (14-period, 15-minute candles) ≤ 28 at or near the liquidation spike time.
4. **CVD exhaustion (preferred):** Cumulative volume delta slope has flattened — aggressive selling is decelerating. (Same signal as [[liquidation-cascade-fade]] — use if tick-level CVD data is available.)
5. **Open interest contraction:** OI has fallen ≥ 5% from its pre-cascade level (confirms forced position closures are real, not phantom).
6. **No confirmed regime event:** No protocol collapse, de-peg, or major credit event is the cause of the cascade (would indicate bear regime, not overshoot).

**Entry criteria (post-short-squeeze — enter short):** Mirror the above: liquidation spike (shorts being closed), price rise ≥ 3% in 15 minutes, RSI ≥ 72 (overbought), CVD flattening on buy side, OI contraction. This direction is used after a short-squeeze cascade ([[short-liquidation-squeeze]] cascade completion).

**Entry execution:** Market entry, isolated margin, 2–3× leverage (more conservative than the cascade riders — this is a mean-reversion entry *after* an event, not during it; slightly less time-critical, more room to ladder).

**Exit — take profit:**
- Pre-cascade VWAP: the 15-minute volume-weighted average price captured in the 15-minute window *before* the liquidation spike fired. This is the "if the cascade fully reverses" target.
- If pre-cascade VWAP is not reachable within the time stop (event was too large), target: 61.8% Fibonacci retracement of the cascade move from peak to trough.

**Exit — stop:**
- Hard stop at −5% from entry (post-long-cascade long) or +5% (post-short-squeeze short).
- ATR trailing stop: once in profit, trail at 1.5× ATR. See [[atr-trailing-stop]].
- Time stop: 6 hours. If mean reversion hasn't occurred in 6 hours, the market has found a new equilibrium.

**Sizing:** 3–6% of basket equity per trade. Up to 2 concurrent positions (e.g., two different pairs can both flush simultaneously). Reduce to 2% if the cascade is on a thin-cap pair. Reduce to 1% if the macro context suggests possible bear-regime misclassification (de-peg risk, credit event news).

---

## Implementation Pseudocode

```python
# Post-Liquidation Rebound — basket module
# Event-driven; bidirectional; mean-reversion after cascade flush

LIQ_SPIKE_THRESHOLD   = 3.0     # x trailing 24h mean
PRICE_MOVE_MIN_PCT    = 0.03    # 3% move in 15 min
RSI_OVERSOLD          = 28      # long entry threshold
RSI_OVERBOUGHT        = 72      # short entry threshold (post-squeeze)
OI_CONTRACTION_MIN    = 0.05    # OI fell >= 5% from pre-cascade
CVD_FLATTEN_RATIO     = 0.3     # optional: CVD slope exhaustion
LEVERAGE              = 2.5
STOP_LOSS_PCT         = 0.05
TIME_STOP_HOURS       = 6
POSITION_SIZE         = 0.05

def evaluate_post_liquidation_rebound(pair, state, equity):
    liq_5m        = get_liquidation_notional(pair, minutes=5)
    liq_24h_mean  = get_rolling_mean_liquidation(pair, hours=24)
    price_now     = get_mark_price(pair)
    price_15m_ago = get_mark_price(pair, lag_minutes=15)
    rsi           = get_rsi(pair, period=14, timeframe='15m')
    oi_now        = get_open_interest(pair)
    oi_precascade = state.get_pre_cascade_oi(pair)    # snapshot taken at liq spike onset
    vwap_target   = state.get_pre_cascade_vwap(pair)  # 15m VWAP before spike

    liq_spike    = liq_5m >= LIQ_SPIKE_THRESHOLD * liq_24h_mean
    oi_contracted = (oi_precascade - oi_now) / oi_precascade >= OI_CONTRACTION_MIN

    # Post-long-cascade: enter long
    long_cascade_flush = (
        liq_spike and
        (price_15m_ago - price_now) / price_15m_ago >= PRICE_MOVE_MIN_PCT and
        rsi <= RSI_OVERSOLD and
        oi_contracted and
        not state.macro_bear_regime_event
    )

    # Post-short-squeeze: enter short
    short_squeeze_flush = (
        liq_spike and
        (price_now - price_15m_ago) / price_15m_ago >= PRICE_MOVE_MIN_PCT and
        rsi >= RSI_OVERBOUGHT and
        oi_contracted and
        not state.macro_bear_regime_event
    )

    if long_cascade_flush and not state.has_position(pair):
        notional  = equity * POSITION_SIZE * LEVERAGE
        stop_px   = price_now * (1 - STOP_LOSS_PCT)
        state.open_long(pair, notional, price_now, stop_px,
                        target_px=vwap_target,
                        deadline_hours=TIME_STOP_HOURS,
                        tag="post-long-cascade-rebound")

    elif short_squeeze_flush and not state.has_position(pair):
        notional  = equity * POSITION_SIZE * LEVERAGE
        stop_px   = price_now * (1 + STOP_LOSS_PCT)
        state.open_short(pair, notional, price_now, stop_px,
                         target_px=vwap_target,
                         deadline_hours=TIME_STOP_HOURS,
                         tag="post-short-squeeze-rebound")

    if state.has_position(pair):
        pos   = state.get_position(pair)
        price = get_mark_price(pair)

        if (pos.direction == 'long' and price >= pos.target_px) or \
           (pos.direction == 'short' and price <= pos.target_px):
            state.close_all(pair, tag="vwap-target")
        elif (pos.direction == 'long' and price <= pos.stop_px) or \
             (pos.direction == 'short' and price >= pos.stop_px):
            state.close_all(pair, tag="stop")
        elif state.hours_held(pair) >= TIME_STOP_HOURS:
            state.close_all(pair, tag="time-stop")
```

---

## Indicators / Data Used

- **Liquidation feed (volume spike)** — primary event trigger. Source: [[coinglass]] (`forceOrder` WebSocket), native HL liquidation stream, [[hypurrscan]].
- **[[rsi|RSI]] (14-period, 15-minute)** — oversold/overbought confirmation at the flush extreme. Specifically looks for RSI ≤ 28 (long entry) or ≥ 72 (short entry) — tighter than the standard 30/70 to avoid triggering in high-momentum trending markets.
- **CVD exhaustion** — optional but preferred when tick-level data is available. Same signal as [[liquidation-cascade-fade]]'s primary filter.
- **[[open-interest]] contraction** — confirms the cascade was real (forced liquidations reduced OI) vs a volume spike from large voluntary trades.
- **Pre-cascade VWAP** — the take-profit target. Must be captured at the moment the liquidation spike is first detected; use a snapshot at the start of the 5-minute liquidation window.
- **[[funding-rate]] post-cascade** — after a long liquidation cascade, funding often flips negative (perp dropped below oracle). If negative funding is now present, the long entry also collects carry — a structural bonus that improves the risk/reward.

---

## Example Trade

**Illustrative only — not a backtest.**

Reference: loosely inspired by the pattern documented in the [[liquidation-cascade-fade]] August 2024 trade example.

Scenario: BTC/USDC-PERP on Hyperliquid. Macro catalyst (yield spike) triggers a cascade. BTC falls 8% in 20 minutes; $600M in long liquidations in 5 minutes (3.8× daily mean). RSI on 15m candles touches 24. OI falls 9% from pre-cascade level. No confirmed credit event or protocol issue — this reads as a macro overshoot.

| Step | Detail |
|---|---|
| **Cascade detected** | 5-min liq notional = 3.8× 24h mean @ BTC $95,400 |
| **RSI confirmation** | RSI 15m = 24 (oversold) |
| **OI check** | OI fell 9% from $4.2B to $3.8B — real liquidations |
| **Pre-cascade VWAP** | $103,500 (captured 15min before spike onset) |
| **Entry** | Long BTC perp @ $95,600, 2.5× leverage, isolated margin |
| **Stop** | $90,820 (−5%) |
| **Post-cascade funding** | Flips to −0.02%/h (shorts now paying — bonus carry for long) |
| **Recovery** | BTC recovers to $101,800 in 3.5 hours (partial VWAP mean-reversion) |
| **Exit** | Time stop nears; exit at $101,800 (+6.5%) at h+3.5 |
| **Net P&L** | +6.5% on notional × 2.5× = +16.3% on margin, plus minor funding carry |

*Illustrative, not a backtest. Reflects a plausible macro-overshoot cascade. The canonical [[liquidation-cascade-fade]] documented a similar ~22% on position notional trade on the 2024-08-05 BoJ event — this basket would have fired the same signal.*

---

## Performance Characteristics

- **Return shape:** Mean-reversion profile — many small-to-medium wins, occasional large losses when bear-regime misclassification occurs. Closely mirrors [[liquidation-cascade-fade]]'s documented 62–70% win rate when CVD filter is applied.
- **Expected Sharpe:** ~1.0 (similar to cascade fade at 1.0–1.4, but slightly lower as this basket is broader and the RSI filter alone is weaker than the CVD + RSI combination).
- **Expected max drawdown:** ~28% — driven by regime-shift cascade losses (LUNA/FTX class events). Without regime-shift events, the drawdown profile is much more benign.
- **Correlation to [[liquidation-cascade-fade]]:** Very high when both fire simultaneously on the same event. The two baskets should not both be active on the same pair at the same time — treat them as alternative implementations of the same mean-reversion signal, with this basket as the regime-aware fallback when CVD data is unavailable.
- **Synergies:** Pairs naturally with [[long-liquidation-cascade]] (which exits *just before* this basket enters) and [[short-liquidation-squeeze]] (exits just before a short-entry version of this basket). Ideally, the cascade-rider basket exits and the rebound basket enters on the same event in sequence.

---

## Capacity Limits

Bounded by the same factors as [[liquidation-cascade-fade]]: approximately **$1–3M notional per cascade event** on BTC/ETH before the entry materially moves price. The post-cascade entry window is thin (the bid is reforming; any large market buy creates its own mini-squeeze). Aggregate basket capacity **$8M** across multiple concurrent pairs. On thin mid-caps, $200K–$500K per event.

---

## What Kills This Strategy

See [[failure-modes]]:

1. **Regime-shift misclassification.** The strategy's worst cases: LUNA (May 2022), FTX (November 2022), 3AC (June 2022) — cascades that correctly repriced assets permanently lower. The CVD filter and the 6-hour time stop limit but do not eliminate this risk. The macro context check is the primary guard.
2. **Slow reversion (time stop).** If the cascade is large enough that the market needs days rather than hours to recover, the 6-hour time stop exits at a loss even though the trade would have been correct given more time. This is the tradeoff for keeping the strategy focused on short-term reversion.
3. **Funding doesn't normalise.** If the cascade was genuine (not an overshoot), funding may remain extreme for hours or days — signalling continued imbalance rather than a clean flush. Monitor this as a hold/exit signal.
4. **Liquidity withdrawal post-cascade.** On thin pairs, the bid may remain absent for hours after a cascade, making mean-reversion extremely slow. The time stop handles this but at the cost of a loss.
5. **Multiple cascades in sequence.** In a genuine bear regime, a cascade is followed by another cascade, and the entry into the first rebound is caught by the second cascade. The −5% stop and the regime-event check are the primary mitigants.

---

## Kill Criteria

Per [[when-to-retire-a-strategy]]:

- **Win rate < 52%** over trailing 25 completed trades — post-flush signal is not reliably predicting mean reversion.
- **Three consecutive full stop-outs** (> 8% per position) — setup is systematically entering before the cascade is complete, or into genuine bear regimes.
- **> 50% of trades time-stopping** (6-hour stop) — mean reversion is taking longer than the design window; the 6-hour window is too short for the current regime.
- **Drawdown > 25%** on this basket over rolling 6 months.

---

## Advantages

- **Clean market post-flush.** The structural improvement (overleveraged positions removed, OI contracted, funding normalised) provides a genuine fundamental basis for mean reversion, not just a sentiment bet.
- **Bidirectional.** Can trade both post-long-cascade (long) and post-short-squeeze (short) — broader activation surface than the long-only [[liquidation-cascade-fade]].
- **Funding bonus.** Post-cascade funding often moves in the rebound direction (negative after long cascade = collect carry with long; positive after short squeeze = collect carry with short).
- **Natural pair with cascade-rider baskets.** Sequentially complements [[long-liquidation-cascade]] and [[short-liquidation-squeeze]] — where they exit, this basket enters.
- **Multiple confirming signals.** RSI + liquidation spike + OI contraction + CVD (optional) — multiple signals reduce false positives compared to pure CVD or pure RSI strategies.

---

## Disadvantages

- **Bear-regime risk is the same as [[liquidation-cascade-fade]]** — the strategy cannot reliably distinguish overshoot from genuine repricing.
- **Competition from other mean-reversion strategies.** The post-cascade entry point is also targeted by the cascade fade, arbitrage bots, and discretionary dip-buyers — the profit window may be crowded.
- **RSI is lagging.** RSI on 15-minute candles reaches oversold *after* the sharpest part of the decline; the entry may miss the best ticks of the rebound.
- **Thin entry window.** The optimal entry is a few minutes after cascade exhaustion — too early and the cascade is still going; too late and the rebound has already moved.
- **Event rarity.** Genuine cascade events triggering 3× daily liquidation volume are not daily occurrences on most pairs; this basket may see fewer setups than the carry-based baskets.

---

## Hyperliquid Execution Notes

**Mark-price recovery pattern.** Post-cascade, Hyperliquid's mark price (TWAP of oracle) lags the actual last-trade price recovery. This means the mark may remain depressed for 1–3 oracle update cycles even after the cascade ends — the perceived funding is still extreme, but spot is already recovering. Monitor both mark price and spot price during entry.

**Funding flip as confirmation.** On Hyperliquid's hourly settlement, if the cascade completed in the first 30 minutes of an hour, the *next* hour's `predictedFundings` will already show normalising or flipped funding. This is a uniquely powerful confirmation signal — it means the hourly mechanism has detected the shift and new incentives are already propagating. Use `predictedFundings` API to check this before entry. Source: [[hyperliquid-funding-rate-microstructure]].

**Isolated margin and leverage constraint.** At 2.5× leverage with a −5% stop, each failed trade loses 12.5% of margin (2.5 × 5%). After a cascade event, markets are volatile — do not increase leverage to "make back" a recent loss. The 2.5× cap is conservative by design.

**ADL awareness.** If Hyperliquid's insurance fund was depleted *by the cascade itself* (the cascade overwhelmed the fund), ADL may fire on profitable positions in the opposite direction. Entering long in a post-cascade window when ADL risk is elevated (check Hyperliquid's insurance fund level post-cascade via [[hyperliquid-liquidation-engine]]) warrants extra caution.

**[[2025-03-jellyjelly-hlp-attack]] note.** The JELLY squeeze is a short-squeeze case where the cascade was *orchestrated* rather than organic. A post-squeeze rebound entry would have been extremely profitable if it could have been executed — but the governance delist/force-settlement prevented normal price recovery. This is the primary tail risk for the short entry (post-squeeze direction): the squeeze may end via governance intervention rather than organic reversal, making the short entry (expecting continued decline post-squeeze-exhaustion) correct in theory but unexecutable in practice. Reduce exposure on pairs with known thin-book dynamics.

**Sibling baskets and sequencing:** [[long-liquidation-cascade]] → cascade fires → [this basket enters long] → mean reversion completes → exit. [[short-liquidation-squeeze]] → squeeze fires → [this basket enters short (rare)] → mean reversion completes → exit. See also [[liquidation-cascade-fade]] for the tighter CVD-based implementation.

---

## Sources

- [[liquidation-cascade-fade]] — the closely related existing strategy; methodology, empirical evidence, and historical examples.
- [[hyperliquid-liquidation-engine]] — mark-price liquidation, post-cascade insurance fund state, ADL.
- [[hyperliquid-funding-rate-microstructure]] — funding flip post-cascade; `predictedFundings` as confirmation signal.
- [[2025-10-crypto-liquidation-cascade]] — large-scale cascade event with documented recovery timing.
- [[2025-03-jellyjelly-hlp-attack]] — governance intervention after squeeze; execution risk for short direction.
- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — basket design and regime mapping.
- [[coinglass]] — liquidation volume data.
- [[edge-taxonomy]], [[failure-modes]] — classification frameworks.

---

## Related

[[hyperliquid]] · [[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[perpetual-futures]] · [[market-regime]] · [[liquidation-cascade-fade]] · [[short-liquidation-squeeze]] · [[long-liquidation-cascade]] · [[crowded-short-funding-fade]] · [[crowded-long-funding-fade]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[2025-10-crypto-liquidation-cascade]] · [[2025-03-jellyjelly-hlp-attack]] · [[liquidation]] · [[long-liquidation]] · [[open-interest]] · [[leverage]] · [[rsi]] · [[relative-strength-index]] · [[mean-reversion]] · [[order-flow]] · [[funding-rate]] · [[atr-trailing-stop]] · [[coinglass]] · [[derivatives-native-regime]] · [[security-black-swan-regime]] · [[liquidity-depth-regime]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
