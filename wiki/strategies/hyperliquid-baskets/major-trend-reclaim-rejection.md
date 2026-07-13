---
title: "Major Trend Reclaim / Rejection (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, trend-following, technical-analysis, quantitative, swing-trading, momentum, breakout]
aliases: ["MA Reclaim Rejection Basket", "200 MA Reclaim Short Strategy", "Critical Level Reclaim Trade", "Structural Level Flip Strategy"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[macro-trend-regime]]", "[[oi-confirmed-trend]]", "[[trend-pullback-rally-fade]]", "[[defensive-majors]]", "[[breakout-and-retest]]", "[[failed-breakout-failed-breakdown]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[when-to-retire-a-strategy]]", "[[200-day-moving-average]]", "[[support]]", "[[resistance]]", "[[market-cap-level-trading]]"]
strategy_type: algorithmic
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Algorithmic and institutional participants cluster orders at the 200-day MA and major historical structure — a reclaim triggers forced short-covering and programmatic buy signals across many systems simultaneously, creating momentum disproportionate to the individual trade size; the basket front-runs this convergence."
data_required: [ohlcv, perp-funding, open-interest, liquidation-feed, order-book-depth]
min_capital_usd: 5000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.28
breakeven_cost_bps: 35
kill_criteria: |
  - Basket drawdown > 28% on rolling 6-month basis
  - Rolling 6-month Sharpe < -0.4
  - Win rate on reclaim/rejection setups < 40% over 20 consecutive signals
  - Any held position adverse > 20% from entry → cover (level has definitively failed)
  - Three consecutive false reclaims on BTC (reclaim + hold for 2 days + reversal) → suspend BTC signals and recalibrate level definitions
---

# Major Trend Reclaim / Rejection (Hyperliquid Basket)

The Major Trend Reclaim / Rejection basket focuses on **the most significant structural price levels in crypto** — the 200-day moving average, weekly EMAs, and major historical support/resistance zones — and trades **binary outcomes** at those levels. When price reclaims one of these levels (breaks above and holds for a confirmation period), the basket goes long, expecting an outsized upside continuation. When price tests a level but fails to hold (rejection), the basket goes short, expecting an outsized move back down. These are high-conviction, low-frequency setups that anticipate the largest moves in a cycle, because the most watched levels generate the most violent reactions.

*Part of the [[hyperliquid-baskets-overview|Alfred Hyperliquid basket library]].*

## Edge Source

**Behavioral** + **structural** (see [[edge-taxonomy]]).

- **Behavioral** — major moving averages and historical levels concentrate the attention and order placement of both systematic and discretionary participants. A [[200-day-moving-average|200-day MA]] reclaim is used as a regime signal by CTAs, risk-parity funds, and algo traders globally — their simultaneous buy signals create the cascade of forced buying that makes the level self-fulfilling. The basket front-runs this convergence by entering at the confirmation point rather than after the move.
- **Structural** — at critical levels, two structural forces converge: (a) covering pressure from participants who were short and must now exit, adding to buying momentum; (b) stop-loss activation from new positions on the wrong side of the level flip, which adds directional momentum. These mechanical flows are structural and predictable. Source: [[market-cap-level-trading]], [[support]], [[resistance]].

**Honest framing:** this is a well-known setup; the 200-day MA reclaim/rejection is among the most-watched signals in all of financial markets. The edge is not obscurity — it is that the self-fulfilling nature of the level creates predictable, tradeable momentum post-confirmation, and the signal's high profile means position sizing and confirmation discipline are critical to avoid false signals.

## Why This Edge Exists

1. **200-day MA is the global risk benchmark.** The 200-day MA is used by institutional risk managers, algorithmic CTAs ([[trend-following-cta]]), and retail platforms as a primary bull/bear regime signal. A reclaim triggers buy signals across dozens of independent systems simultaneously; this coordinated flow creates momentum beyond what any single trade justifies. Source: [[200-day-moving-average]].
2. **Historical structure has memory.** A major price level (e.g., the 2021 all-time high, the 2022 bear market low) concentrates unfilled limit orders from participants who missed the original move and are waiting for a retest. These orders provide structural support/resistance that re-activates at every re-test.
3. **Short-covering amplifies reclaims.** When price reclaims a major level, participants who were short below the level are trapped — they must cover, adding buy pressure. This mechanical covering is forced and inelastic to the price; it adds momentum regardless of the fundamental view.
4. **False reclaims are also tradeable.** When price briefly reclaims a level then fails (a [[failed-breakout-failed-breakdown|failed reclaim]]), the trapped longs who entered the reclaim must exit, and new shorts enter aggressively — the basket's rejection trade captures this double-sided technical conviction.
5. **Volume and OI confirm genuine reclaims.** A genuine reclaim is accompanied by expanding [[open-interest]] and above-average volume; a false reclaim occurs on thin volume and declining OI. This confirmation requirement filters out the most dangerous false signals.
6. **Counterparty:** (reclaim trade) shorts who must cover at the level; (rejection trade) longs who entered the breakout and are now trapped above the level as it becomes resistance.

## Null Hypothesis

Under no-edge conditions, the 200-day MA is a lagging indicator that identifies trends that have already occurred — trading at the level is no better than random entry, and the "cluster of orders" at the level is offset by the equal cluster of participants betting against it. False reclaims and false rejections occur as frequently as valid signals, and the level has no predictive power beyond coincidence with the underlying trend direction. In this case, the strategy's win rate converges to 50% and the edge is explained by the underlying macro trend rather than the level-specific signal.

**Disconfirming evidence to monitor:**
- BTC produces three consecutive "reclaim + hold 2 days + reversal" sequences (the level has become noise rather than signal).
- OI expands on the reclaim but immediately contracts within 24 hours (institutional participants entering at the level then exiting — no conviction behind the move).
- Win rate on reclaim/rejection signals drops below 40% over 20 consecutive signals.
- The 200-day MA has been "reclaimed" and "rejected" multiple times within a 30-day window (the level is in a chop zone, not a clear flip zone).

## Rules

**Defined levels (ranked by importance):**

| Level | Calculation | Asset scope | Signal strength |
|-------|-------------|-------------|-----------------|
| **200-day SMA** | 200-day simple MA of daily close | All assets; especially BTC/ETH | Highest |
| **Weekly 50 EMA** | 50-period weekly EMA | BTC, ETH, large caps | High |
| **Weekly 20 EMA** | 20-period weekly EMA | All large caps | Medium |
| **Major historical S/R** | Prior cycle ATH, bear market lows, annual pivot | BTC, ETH, SOL | High when fresh |
| **Monthly open/close** | Monthly OHLC pivots (prior month close as level) | BTC, ETH | Medium |

**Reclaim signal (long):**
1. Price closes above the target level on the daily timeframe.
2. Price holds above the level for a **confirmation period** of 1–2 daily closes (not a one-wick false break).
3. [[open-interest]] expands ≥ 5% on the confirmation close (capital commitment, not thin air).
4. Volume on the reclaim close is above the 20-day average.
5. [[funding-rate]] is not deeply positive (< +0.08%/8h) — a crowd already long into the reclaim means the covering is complete and the trade is crowded.
6. Entry: limit order just above the level on the first candle that re-tests the level from above (the retest confirms the flip from resistance to support). If no retest within 3 days, enter at market with 75% of the planned size.

**Rejection signal (short):**
1. Price tests the target level from below (approaches resistance).
2. Price closes back below the level after touching/briefly exceeding it.
3. [[open-interest]] expands ≥ 3% on the rejection bar (new shorts entering, not just covering).
4. Volume on the rejection close is above the 20-day average.
5. Funding is not deeply negative (< −0.08%/8h) — don't short into a crowded short environment.
6. Entry: limit order just below the level (confirming the rejection) or at the re-test of the level from below (level from support → resistance).

**Position sizing:**
- Reclaim long: 3–4% of book, 2–2.5x leverage, isolated margin.
- Rejection short: 2–3% of book, 2x leverage, isolated margin (lower size due to higher squeeze risk on shorts near critical levels).
- These are the largest single-asset positions in the Alfred system — justified by the high-conviction, low-frequency nature of the setups.

**Exit / take-profit:**
- Reclaim long: Target = next major structural level above (e.g., prior cycle ATH); ATR trailing stop at 1.5× 14-day ATR.
- Rejection short: Target = prior swing low or next major structural level below; ATR trailing stop at 1.5× 14-day ATR.
- Hard stop: close back below the level (reclaim fails) or close back above the level (rejection fails) on a daily close → exit immediately at market.

## Implementation Pseudocode

```python
LEVELS = {
    "BTC": [
        "200d_sma",
        "weekly_50_ema",
        "prior_cycle_ath",
        "bear_market_low_2022",
    ],
    "ETH": ["200d_sma", "weekly_50_ema", "prior_cycle_ath"],
    # ... extend for large caps
}
OI_RECLAIM_THRESHOLD   = 0.05
OI_REJECTION_THRESHOLD = 0.03
CONFIRM_CLOSES         = 2
LEVERAGE_LONG          = 2.5
LEVERAGE_SHORT         = 2.0
ATR_STOP_MULT          = 1.5

def major_trend_reclaim_rejection(state, book_size):
    legs = []

    for sym, level_ids in LEVELS.items():
        for level_id in level_ids:
            level_price = compute_level(sym, level_id)

            # --- Reclaim signal ---
            daily_close = state.daily_close(sym)
            oi_change   = oi_change_pct(sym, "1d")
            volume_ok   = volume_above_avg(sym, 20)
            funding     = perp_funding_8h(sym)

            consec_above = consecutive_closes_above(sym, level_price, CONFIRM_CLOSES)

            if (consec_above
                    and oi_change >= OI_RECLAIM_THRESHOLD
                    and volume_ok
                    and funding < 0.0008
                    and not already_in_position(sym, "long")):
                # Wait for re-test; if no re-test in 3 days, enter at market
                entry_price = level_price * 1.002  # just above level
                stop_price  = level_price * 0.985  # daily close below = invalid
                target      = next_major_level_above(sym, level_price)
                atr14 = compute_atr(sym, 14, "1d")
                stop_price  = max(stop_price, daily_close - ATR_STOP_MULT * atr14)
                legs.append(long_perp(sym,
                                       notional=book_size * 0.035,
                                       leverage=LEVERAGE_LONG,
                                       margin="isolated",
                                       entry_type="limit_retest",
                                       entry_price=entry_price,
                                       stop_price=stop_price,
                                       target_price=target))

            # --- Rejection signal ---
            consec_below = consecutive_closes_below(sym, level_price, CONFIRM_CLOSES)
            prior_was_above = price_was_above_level_recently(sym, level_price, lookback=3)

            if (consec_below
                    and prior_was_above
                    and oi_change >= OI_REJECTION_THRESHOLD
                    and volume_ok
                    and funding > -0.0008
                    and not already_in_position(sym, "short")):
                entry_price = level_price * 0.998  # just below level
                stop_price  = level_price * 1.015  # daily close above = invalid
                atr14 = compute_atr(sym, 14, "1d")
                stop_price  = min(stop_price, daily_close + ATR_STOP_MULT * atr14)
                target      = next_major_level_below(sym, level_price)
                legs.append(short_perp(sym,
                                        notional=book_size * 0.025,
                                        leverage=LEVERAGE_SHORT,
                                        margin="isolated",
                                        entry_type="limit_retest",
                                        entry_price=entry_price,
                                        stop_price=stop_price,
                                        target_price=target))

    # --- Hard stop: level re-broken on daily close ---
    for leg in legs:
        if leg.direction == "long" and state.daily_close(leg.symbol) < leg.level_price:
            leg.action = "close_market"  # reclaim has failed
        if leg.direction == "short" and state.daily_close(leg.symbol) > leg.level_price:
            leg.action = "close_market"  # rejection has failed

    # --- Kill switches ---
    if state.basket_drawdown_6m > 0.28 or state.rolling_6m_sharpe < -0.4:
        return []

    return legs
```

## Indicators / Data Used

- **[[200-day-moving-average]]** — the primary level for BTC and ETH signals; the most widely-watched technical level in traditional and crypto finance.
- **[[exponential-moving-average]]** — weekly 20 and 50 EMAs as supplementary structural levels; faster-moving than the 200-day and more sensitive to medium-term trend changes.
- **[[support]] / [[resistance]]** — historical price levels (prior cycle ATHs, bear-market lows, annual pivots) that function as structural S/R on re-tests.
- **[[market-cap-level-trading]]** — the broader framework for trading at psychologically and structurally significant levels in high-market-cap assets.
- **[[open-interest]]** — the confirmation signal for genuine capital commitment at the reclaim/rejection. Source: [[coinglass]], [[hypurrscan]].
- **[[funding-rate]]** — sentiment guard preventing entries into already-crowded positions. Source: [[hyperliquid-funding-rate-microstructure]].
- **[[average-true-range]] / [[atr-trailing-stop]]** — stop placement and trailing exits.
- **Volume** — above-20-day-average volume on the signal bar confirms genuine institutional participation.

## Example Trade

**Illustrative — not a backtest.** BTC 200-day MA reclaim.

**Setup:** BTC has traded below its 200-day MA ($62,000) for 6 weeks during a correction. It rallies back to $62,000, closes above on Day 1 ($63,200), and again on Day 2 ($64,100). OI expands 6.8% over the two confirmation days. Volume is 1.4× the 20-day average. Funding: +0.03%/8h (mild positive — not crowded). On Day 3, BTC re-tests $62,500 (the newly-reclaimed 200-day MA from above).

| Parameter | Value |
|-----------|-------|
| Entry (limit at re-test) | $62,600 |
| Stop (close below 200 MA) | $61,000 |
| Target 1 (50% at prior swing high) | $72,000 |
| Notional | $3,500 (3.5% of $100K book) |
| Leverage | 2.5x |
| R/R ratio (stop: $1,600 / target: $9,400) | ~5.9:1 |

**Scenario A (confirmed reclaim):** BTC trends to $72,000 over 3 weeks. Take 50% at $72,000 (+15%), trail ATR stop on remainder to $68,000. Net: ~**+$2,100 on $3,500 notional**.

**Scenario B (false reclaim):** BTC closes back below $62,000 (200 MA) on Day 4. Hard stop triggers at market (approx $61,500). Loss: **−$315 on $3,500 notional** (−9%). Book impact: −0.32%.

**Rejection example (brief):** BTC tests $75,000 resistance (prior ATH area), closes below on high volume with OI expanding 4%. Rejection short entered at $74,500. Stop: $76,200 (daily close above). Target: $68,000. Same high-conviction, lower-frequency structure.

*All figures illustrative. Not a backtest.*

## Performance Characteristics

- **Return shape:** low frequency, high conviction — typically 2–6 signals per quarter across the full universe. Large wins when the reclaim/rejection holds (the outsized moves this strategy targets are the 15–40% range); losses when the signal is false (the hard stop at daily close below/above the level limits loss to 8–15% on the position, depending on the stop distance).
- **Expected Sharpe (illustrative estimate):** ~0.6–0.9 in trending regimes with clean structural levels; approaches 0 in choppy markets where levels are repeatedly reclaimed and broken (whipsaw).
- **Win rate:** lower signal frequency means the win rate estimate is uncertain at current stage (`untested`). A win rate of 40–55% with 3:1 average R/R produces a positive expectancy system.
- **Max drawdown estimate:** ~25–28% in a sequence of false reclaims (the market is in a distribution zone where the 200-day MA is continually crossed both ways). Each false signal loses 8–12% on the position, which is 0.3–0.5% of total book — a sequence of 5–8 such losses before a real trend produces the estimated max drawdown.
- **Realistic round-trip cost:** ~30–40 bps per trade (limit entries at re-test levels; market exits on hard stops). Low trade frequency reduces total annual cost.

## Capacity Limits

BTC and ETH perps on Hyperliquid absorb the largest positions of any asset on the venue — hundreds of millions in notional. At Alfred's current scale the position sizes (3–4% of book) are microscopic relative to venue depth. At institutional scale ($50M+ per trade), block entries near major levels require TWAP or iceberg execution to avoid telegraphing the size. Strategy-level capacity: **$200M** across a BTC/ETH-dominant universe, constrained only by execution impact near the target level rather than market depth in aggregate.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Distribution zone / whipsaw.** When a major level is in a consolidation zone (price oscillates above and below the 200-day MA repeatedly), every "reclaim" is followed by a "rejection" and vice versa. The confirmation requirement (2 closes) reduces but does not eliminate this — a 2-day hold followed by a reversal is the classic distribution pattern. Source: [[wyckoff-method]].
2. **False confirmation volume.** Liquidation cascades can generate above-average volume and OI expansion on a fake reclaim (shorts are force-covered at the level, volume spikes, OI expands from new long entries — all the "right" signals — then price reverses on the next candle when the forced covering is complete). Source: [[long-liquidation]], [[liquidation-cascade-fade]].
3. **Macro override.** A [[policy-shock-regime|policy shock]] can invalidate a technical level in minutes — a regulatory ban, exchange insolvency, or sovereign selling can push BTC through the 200-day MA on a single day despite every technical signal suggesting support. The hard stop (daily close below the level) catches this, but the gap may skip the stop.
4. **Over-watched level.** The 200-day MA is so widely watched that front-running is common — price may squeeze just above the level to fill reclaim buyers, then reverse sharply, producing a wick reclaim rather than a genuine structural flip. The 2-close confirmation requirement mitigates this.
5. **Funding cost on long holds.** If the reclaim is genuine but choppy (price grinds slowly higher), the funding cost at 2.5x leverage accumulates over weeks. At 0.05%/8h (+170% APR annualised), a 30-day hold costs ~14% of the leveraged notional in funding alone.
6. **Rejection squeeze (JELLY class).** For minor large-cap rejection shorts (non-BTC/ETH), a coordinated bid near the resistance level can squeeze the short before the rejection confirms. Less relevant on BTC/ETH perps given depth; more relevant if the basket expands to mid-caps. Source: [[2025-03-jellyjelly-hlp-attack]].

## Kill Criteria

See [[when-to-retire-a-strategy]]. Specific conditions:

- **Basket drawdown > 28%** from rolling 6-month peak → flatten and reassess.
- **Rolling 6-month Sharpe < −0.4** → full review; default to flatten.
- **Win rate < 40% over 20 consecutive signals** → level definitions need recalibration; suspend.
- **Any held position adverse > 20% from entry** → cover; the level has definitively failed (a close back through the level is already the hard stop).
- **Three consecutive false BTC 200-day MA reclaims** (reclaim + 2-day hold + reversal) → BTC signals suspended; BTC is in a chop zone around the level, not a clean flip; recalibrate the confirmation requirement.

## Advantages

- **Highest R/R ratio in the basket library.** Entering near the major level with a stop just beyond it (1–2% below/above) targets moves of 10–25%+ — R/R of 5:1 to 10:1 on the best setups.
- **Self-fulfilling at scale.** The 200-day MA is watched by enough independent systems that the reclaim genuinely creates the move it signals; this is one of the few cases where technical analysis has a structural foundation rather than just coincidental correlation.
- **Low frequency = low cost.** 2–6 signals per quarter means total transaction cost is small relative to other higher-frequency baskets.
- **Clear binary invalidation.** The hard stop (close back through the level) is objective and leaves no ambiguity about when the trade has failed.
- **Complementary to other baskets.** A BTC 200-day MA reclaim typically initiates an OI-confirmed trend and generates Trend Pullback / Rally Fade setups on the subsequent retracement — the baskets chain together into a coherent trade sequence.

## Disadvantages

- **Low signal frequency** — periods of 4–8 weeks with no signals are common; the strategy requires patience and must coexist with higher-frequency baskets to maintain book utilisation.
- **Whipsaw in distribution zones** — the hardest market conditions for this strategy are exactly when the 200-day MA is most discussed, because markets consolidating around it produce the most false signals.
- **False reclaim / distribution pattern.** The institutional version of this strategy (buying the 200-day MA reclaim) is old enough that sophisticated participants deliberately create false reclaims to trap buyers.
- **Funding cost on extended holds.** Positions held for weeks accumulate funding cost at 2.5x leverage; the target move must be large enough to absorb this.
- **Binary outcome.** Unlike mean-reversion strategies that provide gradual entry and exit opportunities, this strategy's value is concentrated in a few large wins per year — a bad streak of false signals with no winners can create a long drawdown period psychologically and numerically.

## Hyperliquid Execution Notes

- **Funding carry direction:** Long positions post-reclaim typically face mildly positive funding (longs pay) as the market transitions to a bull phase and retail leverage builds. The re-test entry reduces the carry cost during the period before the trend firmly establishes. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** At 2.5x leverage, liquidation requires a ~40% adverse move on the full position. A stop placed 2% below the 200-day MA with a 2.5x leverage exits at well below the liquidation point. However, extreme cascade events can gap past stops — size positions such that a 20% gap does not liquidate. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** non-negotiable. A failed reclaim on ETH must not affect the BTC or other legs; each level signal runs in its own isolated margin account.
- **JELLY-style thin-alt squeeze risk:** Minimally relevant for BTC/ETH-focused signals given the depth of those perps. If the universe expands to mid-cap "major level" trades (e.g., SOL weekly EMA reclaim), apply the same JELLY volume guard: skip any perp with < $20M/24h volume for rejection shorts. Source: [[2025-03-jellyjelly-hlp-attack]].
- **Oracle and ADL interaction:** Near major levels, HL's oracle (index-weighted price) and the mark price can temporarily diverge during thin-hours tests of the level. Confirm that the daily close used in the signal logic references the oracle close, not a spot mark spike. Source: [[hyperliquid-oracle-mechanics]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Major Trend Reclaim / Rejection as a technical-structural basket targeting the most significant structural levels.
- [[technical-structural-regime]] — the regime page covering MA levels, range breakouts, and exhaustion signals that this basket is native to.
- [[macro-trend-regime]] — the higher-timeframe backdrop that sets the directional bias for reclaim vs rejection signals.
- [[200-day-moving-average]] — the primary level; its role as a universal regime signal across all asset classes.
- [[market-cap-level-trading]] — framework for understanding why market-cap-weighted assets respond strongly to their major structural levels.
- [[support]], [[resistance]] — foundational concepts; the "flip" of support to resistance (and vice versa) is the core mechanism.
- [[hyperliquid-funding-rate-microstructure]] — funding dynamics during level tests and post-reclaim momentum.
- [[hyperliquid-liquidation-engine]] — liquidation mechanics driving position sizing at these critical levels.
- [[hyperliquid-oracle-mechanics]] — oracle price vs mark price behaviour during thin-hour level tests.
- [[2025-03-jellyjelly-hlp-attack]] — thin-perp squeeze precedent, relevant if the basket expands to mid-caps.
- [[wyckoff-method]] — distribution/accumulation patterns that produce false reclaims; the primary structural failure mode for this strategy.

## Related

[[hyperliquid]] · [[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[perpetual-futures]] · [[market-regime]] · [[liquidation]] · [[oi-confirmed-trend]] · [[trend-pullback-rally-fade]] · [[breakout-and-retest]] · [[failed-breakout-failed-breakdown]] · [[defensive-majors]] · [[technical-structural-regime]] · [[macro-trend-regime]] · [[200-day-moving-average]] · [[exponential-moving-average]] · [[support]] · [[resistance]] · [[market-cap-level-trading]] · [[open-interest]] · [[funding-rate]] · [[atr-trailing-stop]] · [[average-true-range]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-oracle-mechanics]] · [[2025-03-jellyjelly-hlp-attack]] · [[wyckoff-method]] · [[liquidation-cascade-fade]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
