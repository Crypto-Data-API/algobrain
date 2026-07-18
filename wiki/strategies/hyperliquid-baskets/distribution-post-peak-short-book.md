---
title: "Distribution / Post-Peak Short Book (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetual-futures, hyperliquid, technical-analysis, swing-trading, mean-reversion, risk-management, algorithmic, momentum]
aliases: ["Distribution Short Book", "Post-Peak Shorts", "Wyckoff Distribution Short", "Smart-Money Exit Fade"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[macro-trend-regime]]", "[[on-chain-regime]]", "[[derivatives-native-regime]]", "[[full-bear-short-book]]", "[[oi-price-exhaustion]]", "[[trend-pullback-rally-fade]]", "[[major-trend-reclaim-rejection]]", "[[wyckoff-method]]", "[[evening-star]]", "[[divergence]]", "[[resistance]]", "[[open-interest]]", "[[funding-rate]]", "[[rsi]]", "[[volume]]", "[[vwap]]", "[[atr]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "Late retail buyers absorb distribution from institutional / early-cycle holders who are selling into strength at resistance; the retail crowd anchors to the prior peak as a price target while the smart-money exit has already structurally weakened the book, leaving latecomers holding a deteriorating position as distribution resolves into a bear trend."
data_required: [ohlcv-daily, ohlcv-4h, open-interest, funding-rate, volume-profile, on-chain-exchange-flows, liquidation-feed]
min_capital_usd: 15000
capacity_usd: 75000000
crowding_risk: medium
expected_sharpe: 0.75
expected_max_drawdown: 0.25
breakeven_cost_bps: 45
kill_criteria: |
  - Rolling 6-month drawdown > 25% on the strategy book
  - 3 consecutive losing short entries on confirmed distribution setups (pattern no longer firing)
  - Bull market re-entry confirmed by higher high + OI expansion + funding reset → stand down and reassign capital
---

# Distribution / Post-Peak Short Book (Hyperliquid Basket)

> **Not investment advice** — this page documents the setup for the systematic trading framework. Distribution shorts are aggressive reversal plays entered against a recently bullish tape; position accordingly.

A selective short book targeting assets that have **already peaked** and are entering the distribution phase — where early-cycle or institutional holders sell into retail buying near all-time highs or major resistance. Unlike the [[full-bear-short-book]], which fires after a bear trend is established, this basket is a **precursor**: it enters earlier, when distribution signals are present but the crowd still holds a bullish narrative. The tradeoff is a higher false-positive rate in exchange for entering at structurally better prices.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral** + **informational** (see [[edge-taxonomy]]).

The primary edge is behavioral: the retail crowd anchors to a prior peak as a "fair value" target, continuing to buy into resistance while distribution is underway. The informational component is the ability to read distribution signals — volume at resistance without price progress, declining OI on sideways price action, RSI bearish divergence — before the breakdown is obvious to the crowd. Distribution patterns, particularly the [[wyckoff-method|Wyckoff distribution schematic]], encode the sequence of how professional selling unfolds in recognisable price/volume structure.

## Why This Edge Exists

Distribution is a structural feature of how large holders exit. A large seller cannot dump their entire position in one block without collapsing the price against themselves. Instead, they sell incrementally into retail buying at resistance, absorbing demand over days or weeks before the bid is exhausted. This creates a recognisable signature: high volume at resistance without price follow-through, price oscillating in a topping range, and gradually deteriorating momentum (RSI divergence, declining OI, funding staying elevated but eroding).

The edge exists because the crowd interprets high volume at resistance as "accumulation" (buyers winning) when it is actually supply being offloaded. Late entrants buy the top of the distribution range as a "dip," providing the exit liquidity that the distribution phase requires. By the time the breakdown is visible, the early-cycle holders are already flat.

On Hyperliquid perpetuals specifically, the [[funding-rate]] remains elevated (retail still paying longs) while OI stagnates or falls — a divergence that signals existing longs are closing (distribution) rather than new longs entering (accumulation). The on-chain exchange-inflow data ([[on-chain-regime]]) corroborates: coins moving to exchanges are a sell signal.

**Counterparty:** late retail buyers who anchor to the recent peak as a return target; leveraged long holders on Hyperliquid who entered during the final thrust and are now trapped above the distribution zone.

**Why more selective than [[full-bear-short-book]]:** The Full Bear book fires when the bear is already established; this basket fires *at the transition*. Earlier entry means better prices but more false positives — the distribution can fail and resolve upward (especially in strong bull regimes). Position size is therefore conservative until the breakdown confirms.

## Null Hypothesis

Under "no edge," high-volume resistance tests and RSI divergences are noise: the market is efficient at pricing distribution, funding rates and OI already encode the seller's exit, and any short entered on these signals nets to zero after slippage and funding costs. Distribution patterns are pattern-matched in hindsight and do not predict breakdown timing with better-than-random accuracy.

**Disconfirming evidence to monitor:**
- Repeated distribution signals followed by breakout continuation (pattern failing more than 40% of the time over a 20-trade sample).
- Funding never flipping negative even after price breaks lower — suggests the crowd is not positioned the way the distribution thesis requires.
- OI expanding despite sideways price (accumulation, not distribution — the opposite regime).
- [[wyckoff-method|Wyckoff]] spring / shakeout pattern firing (a distribution-pattern false positive that reverses sharply higher) appearing in more than 30% of setups.

## Rules

**Universe.** Hyperliquid perps with liquid order books (> $5M daily volume). Focus on assets that have:
1. Made a local or cycle high within the past 2–8 weeks.
2. Failed to make a new high on the subsequent attempt.
3. Are trading in a range or grinding lower, *not* in a clean downtrend (that is the [[full-bear-short-book]] universe).

**Entry conditions (all must hold):**
- Price has tested a major resistance level or all-time-high zone **≥ 2 times without closing above it** on the 4H or daily chart.
- RSI (14) on the daily is **bearish divergence**: lower high on RSI while price makes a higher high or equal high (see [[divergence]]).
- OI is **flat or declining** over the prior 5 days while price is flat or slightly positive — the signature of distribution rather than accumulation.
- A bearish candlestick pattern has formed at or near resistance: [[evening-star]], bearish engulfing, shooting star, or a Wyckoff [[wyckoff-method|UTAD (Upthrust After Distribution)]] signal.
- Funding rate is **positive but declining** — longs still paying, but enthusiasm fading.

**Position sizing:**
- Risk 0.5–1.0% of capital per entry.
- Size using [[atr]] (14) on the daily: position size = risk per trade / (1.5 × ATR). See [[atr-position-sizing]].
- Maximum 4 concurrent positions in this basket.

**Entry:**
- Enter short on the close of the confirming candle on the 4H chart, or on a retest of the breakdown level (price briefly retests the bottom of the distribution range from below after the initial break).
- Do not chase — if price is already more than 1 ATR below the distribution zone, skip the entry.

**Stop-loss:**
- Stop above the most recent swing high in the distribution zone (above the [[resistance]] level), typically 1.2–1.5 × ATR above entry.
- If price reclaims the distribution zone with a high-volume close, exit regardless of stop level.

**Take-profit / exit:**
- Primary target: the next major [[support]] level or the prior consolidation zone (typically 15–40% below the distribution zone).
- Scale out in thirds: 1/3 at first support, 1/3 at second support, trail the final third with a 2 × ATR trailing stop (see [[atr-trailing-stop]]).
- Mandatory exit: if [[on-chain-regime]] signals reverse (exchange outflows, whale accumulation), close the position.
- Exit if funding flips deeply negative (crowded short — squeeze risk rises; see Hyperliquid Execution Notes below).

## Implementation Pseudocode

```python
def distribution_short_book(universe, state, capital):
    positions = []
    MAX_CONCURRENT = 4
    RISK_PER_TRADE = 0.008 * capital  # 0.8% risk per entry

    for asset in universe:
        if len(positions) >= MAX_CONCURRENT:
            break

        p = get_price_data(asset, timeframe="4H", lookback=90)
        d = get_derivatives_data(asset)

        # --- Distribution pattern checks ---
        at_resistance = is_at_resistance(p, tolerance_pct=0.03)
        failed_breakout = count_resistance_tests(p, lookback=40) >= 2
        rsi_divergence = bearish_rsi_divergence(p, rsi_period=14)
        oi_declining = d.oi_5d_change < 0.01           # flat or falling OI
        funding_positive_declining = (
            d.funding_rate > 0 and d.funding_8d_slope < 0
        )
        bearish_candle = (
            is_evening_star(p) or
            is_bearish_engulfing(p) or
            is_wyckoff_utad(p)
        )

        if not all([
            at_resistance, failed_breakout, rsi_divergence,
            oi_declining, funding_positive_declining, bearish_candle
        ]):
            continue

        # --- Size by ATR ---
        atr = compute_atr(p, period=14)
        stop_distance = 1.5 * atr
        size = RISK_PER_TRADE / stop_distance
        entry = p.close[-1]
        stop = entry + stop_distance
        tp1 = entry - 1.5 * atr  # first support
        tp2 = entry - 3.0 * atr  # second support

        positions.append(
            short_perp(asset, size=size, entry=entry, stop=stop,
                       tp1=tp1, tp2=tp2, margin="isolated",
                       leverage=3, tag="distribution")
        )

    # --- Ongoing management ---
    for pos in state.open_distribution_positions:
        if state.on_chain_reversal_signal(pos.asset):
            close_position(pos, reason="on_chain_flip")
        if state.funding_rate(pos.asset) < -0.15 / 365:  # deeply negative
            close_position(pos, reason="crowded_short_risk")
        if price_reclaims_distribution_zone(pos.asset):
            close_position(pos, reason="pattern_failed")
        apply_atr_trailing_stop(pos, atr_multiple=2.0)

    return positions
```

## Indicators / Data Used

- **Price structure** — daily / 4H OHLCV for resistance identification, pattern recognition ([[evening-star]], [[wyckoff-method|Wyckoff UTAD]]).
- **RSI (14)** — bearish divergence on the daily chart; see [[rsi]] and [[relative-strength-index]].
- **Open Interest** — 5-day OI change on Hyperliquid; flat/declining OI on flat/rising price is the distribution fingerprint. Source: [[open-interest]], Hypurrscan ([[hypurrscan]]).
- **Funding rate** — positive but declining funding signals waning long enthusiasm. Source: [[funding-rate]], [[hyperliquid-funding-rate-microstructure]].
- **Volume profile** — high volume at resistance without price progress (distribution volume signature). See [[value-area]], [[vwap]].
- **ATR (14)** — daily ATR for stop placement and position sizing. See [[average-true-range]], [[atr]].
- **On-chain exchange flows** — exchange inflows (selling pressure building) from CryptoQuant ([[cryptoquant]]). A leading signal for the distribution thesis.
- **Wyckoff pattern recognition** — UTAD, Sign of Weakness, Last Point of Supply. See [[wyckoff-method]].

## Example Trade

**Illustrative — not a backtest. Figures are estimates to demonstrate setup logic.**

*Setup:* A mid-cap altcoin on Hyperliquid perps has rallied 3× over two months, peaked at $4.20 (all-time high), pulled back to $3.00, and then rallied back to $4.10 — failing to set a new high. OI is flat over the last week despite the rally. RSI shows a lower high (68 vs prior 78). An evening-star candlestick forms on the daily at $4.05. Funding is +0.04% per 8h, down from +0.09% at the peak.

| Parameter | Value |
|---|---|
| Asset | ALT-PERP (illustrative) |
| Setup date | Day 0 |
| Entry | $4.00 (close of evening-star day) |
| Stop | $4.35 (above the recent high; 1.5 × ATR) |
| Target 1 (⅓ exit) | $3.40 (prior consolidation zone) |
| Target 2 (⅓ exit) | $2.80 (50% retracement) |
| Target 3 (trailing) | Trail with 2× ATR stop |
| ATR (14, daily) | $0.23 |
| Position size | 0.8% risk / $0.35 stop ≈ notional sized accordingly |
| Leverage | 3× isolated |

*Illustrative outcome:* Price oscillates for 4 days near $3.90–4.10, then breaks down on heavy volume to $3.20 over 10 days. ⅓ covered at $3.40 (+15%), ⅓ covered at $2.90 (+27.5%), final third stopped out at $3.10 on a bounce (+22.5%). Weighted average return ≈ +22% on notional, net of funding paid and fees. Distribution thesis confirmed; asset reassigned to [[full-bear-short-book]] universe.

*Counter-example:* A "Wyckoff spring" shakeout briefly drops to $3.70, triggering weak hands, then reverses sharply to $4.50 — a new high. Stop at $4.35 hit for −8.75% on notional. Pattern failed; no position in the new uptrend.

## Performance Characteristics

**All figures are ILLUSTRATIVE ESTIMATES. No live or walk-forward track record exists.**

| Metric | Estimate |
|---|---|
| Win rate (per setup) | ~45–55% (distribution patterns have meaningful false-positive rate) |
| Average win / average loss | ~2.5:1 (wide targets vs tight stops) |
| Expected Sharpe (annual) | ~0.6–0.9 (regime-dependent; collapses in bull continuation) |
| Expected max drawdown | ~20–25% on the strategy book |
| Avg holding period | 5–20 days |
| Breakeven round-trip cost | ~45 bps (taker fee + slippage; funding usually neutral to slightly negative cost) |

Return profile is **lognormal with a negative skew on individual trades** (stops are tight, wins are wide) but the distribution-phase pattern means most trades resolve one way or the other within 1–2 weeks. In bull-continuation regimes, the false-positive rate rises significantly and the basket should be gated off.

**Regime dependence:** This basket performs best during [[technical-structural-regime|technical exhaustion]] periods inside a [[macro-trend-regime|distribution-to-bear transition]]. It is not designed for — and should be disabled in — confirmed bull markets where resistance tests resolve as [[breakout-trading|breakouts]].

## Capacity Limits

Capacity is bounded by Hyperliquid perp liquidity on mid-cap assets. On major assets (BTC, ETH, SOL), single-name capacity is effectively unlimited at this strategy's scale. On mid-cap alts, the strategy should not exceed ~1–3% of the asset's daily perp volume on entry to avoid moving the market and creating adverse fill quality. Strategy-level capacity: **$50–75M** across the basket before slippage on the distribution-zone entries meaningfully degrades execution. At scale, limit entries to the four most liquid names with confirmed distribution setups.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Bull-continuation false positives.** The most common failure: distribution-looking patterns that resolve as consolidation before a continuation move higher. Stop is hit; the asset reaches new highs. Frequency rises sharply in strong bull regimes — gate this basket off when [[macro-trend-regime]] is confirmed bullish.
2. **Premature entry before distribution completes.** Entering on the first failed breakout attempt instead of waiting for pattern confirmation results in being stopped out by the final push to the actual high.
3. **Short squeeze ([[2025-03-jellyjelly-hlp-attack|JELLY pattern]]).** A coordinated buy or listing-driven bid squeezes the perp higher into the stop zone. Use isolated margin and respect per-name caps.
4. **Funding flip (crowded short).** If the market joins the short after the initial breakdown, funding turns negative and the carry advantage disappears; continued crowding creates squeeze fuel. Monitor via [[hyperliquid-funding-rate-microstructure]].
5. **Regime mismatch.** Running distribution shorts during an institutional-accumulation phase ([[on-chain-regime]] showing exchange outflows) inverts the edge entirely.
6. **Overfitting to Wyckoff schematics.** Distribution patterns are visually compelling but subject to confirmation bias. Track the actual signal accuracy, not the theoretical schema. See [[overfitting-detection]].
7. **Catalyst override.** A positive macro catalyst (ETF approval, rate cut) can abort an in-progress distribution phase and squeeze shorts violently.

## Kill Criteria

Numeric conditions for retiring this basket (see [[when-to-retire-a-strategy]]):

- **Rolling 6-month drawdown > 25%** on the strategy book → flatten all positions and reassess.
- **3 consecutive confirmed-setup losses** → pause new entries; review pattern recognition logic.
- **Macro-trend regime flips to confirmed bull** (higher high + OI expansion + funding reset) → gate off entirely; redeploy capital to long-biased baskets.
- **Funding persistently < −0.10% per 8h** across core positions → crowded short; exit.
- **Any single position +30% adverse in < 24h on thin volume** → cover immediately (squeeze guard).
- **Rolling 6-month Sharpe < −0.5** → full review; default to flatten.

## Hyperliquid Execution Notes

- **Funding carry:** This basket usually carries a small negative funding cost (paying to be short when the market is still bullish) during the early distribution phase. The carry flips positive once the distribution resolves and longs start unwinding. Model this as a holding cost of ~0.03–0.08% per 8h in the early phase.
- **Single-mark-tick liquidation + ADL:** Hyperliquid can liquidate on a single mark-price tick; size positions to survive a 15–20% adverse move without liquidation trigger. 3× leverage on isolated margin is the ceiling for a multi-day hold. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** Always use isolated margin on this basket. Distribution-phase timing is uncertain; cross-margin would let a squeeze in one leg impair all positions.
- **JELLY thin-alt squeeze risk:** Avoid distribution shorts on low-float, low-OI perps where a coordinated bid can squeeze through the distribution zone and trigger liquidations. Confirm > $5M daily perp volume before entry. See [[2025-03-jellyjelly-hlp-attack]].
- **Oracle / mark-price divergence:** During volatile moves, the HL mark price can diverge from the index. Monitor via [[hyperliquid-oracle-mechanics]] — an adverse mark divergence can trigger premature liquidation on a position that is nominally in-the-money on the index.
- **Transparent OI:** Hyperliquid's on-chain OI and leverage distribution data is a real-time edge for reading crowding. If short OI is rapidly rising (crowd joining), exit before the squeeze, not after. Source: [[hyperliquid-vault-architecture]].

## Advantages

- **Better entry prices than the [[full-bear-short-book]]** — entered during distribution rather than after the breakdown, capturing the full decline rather than the middle third.
- **Behavioral edge is durable** — retail anchoring to prior peaks is a persistent bias unlikely to be arbitraged away, especially in crypto where narrative momentum is strong.
- **Defined risk** — tight stops above the distribution zone mean the risk-reward is asymmetric when the thesis is correct.
- **Multi-timeframe confirmation** — requires alignment of price pattern, OI trend, RSI divergence, and funding; reduces false positives vs single-signal approaches.
- **Complementary to the broader short book** — feeds confirmed breakdowns into the [[full-bear-short-book]], creating a natural pipeline from detection to sustained short.

## Disadvantages

- **Higher false-positive rate** than the [[full-bear-short-book]] — distribution can fail and resolve as continuation.
- **Timing uncertainty** — distribution phases can last weeks; the position pays funding while waiting.
- **Pattern subjectivity** — [[wyckoff-method|Wyckoff]] pattern recognition requires judgment; susceptible to confirmation bias without rigorous rules.
- **Regime sensitivity** — completely unprofitable in strong bull markets; requires reliable [[macro-trend-regime]] gating.
- **Holding duration mismatch** — a swing strategy on a venue optimised for faster trades; overnight funding costs accumulate.
- **Squeeze risk** — being short a distribution zone that fails and reverses sharply is the modal large loss event.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — 14-basket regime framework; distribution phase defined as the transition from Macro Bull to Full Bear (Source: basket #1, technical-structural overlay).
- [[wyckoff-method]] — Wyckoff distribution schematic, UTAD pattern, Sign of Weakness.
- [[evening-star]] — Bearish reversal candlestick pattern used as entry confirmation.
- [[divergence]] — RSI bearish divergence as distribution indicator.
- [[crypto-perp-backtesting-pitfalls]] — regime gating and look-ahead bias considerations for this strategy type.
- [[hyperliquid-funding-rate-microstructure]] — funding carry mechanics and crowding signals.
- [[hyperliquid-liquidation-engine]] — single-tick liquidation and ADL risks.
- [[2025-03-jellyjelly-hlp-attack]] — JELLY thin-alt squeeze precedent.

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[full-bear-short-book]] · [[oi-price-exhaustion]] · [[trend-pullback-rally-fade]] · [[major-trend-reclaim-rejection]] · [[wyckoff-method]] · [[evening-star]] · [[divergence]] · [[resistance]] · [[open-interest]] · [[funding-rate]] · [[perpetual-futures]] · [[rsi]] · [[vwap]] · [[atr]] · [[market-regime]] · [[technical-structural-regime]] · [[macro-trend-regime]] · [[on-chain-regime]] · [[derivatives-native-regime]] · [[breadth-and-momentum-divergence]] · [[breakout-and-retest]] · [[cross-sectional-relative-value]] · [[crowded-short-funding-fade]] · [[defensive-majors]] · [[hyperliquid]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[2025-03-jellyjelly-hlp-attack]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
