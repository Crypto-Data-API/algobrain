---
title: "Range Breakout / Breakdown (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, technical-analysis, breakout, trend-following, intraday, swing-trading]
aliases: ["Range Breakout Breakdown", "Immediate Breakout Entry", "Level-Break Entry", "Range Break Momentum"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[volatility-regime-classification]]", "[[breakout-trading]]", "[[channel-breakout]]", "[[donchian-channel-breakout]]", "[[consolidation]]", "[[support]]", "[[resistance]]", "[[atr]]", "[[open-interest]]", "[[funding-rate]]", "[[breakout-and-retest]]", "[[failed-breakout-failed-breakdown]]", "[[range-mean-reversion]]", "[[volatility-compression-breakout]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[hyperliquid]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]"]
strategy_type: technical
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: pilot
edge_source: [behavioral, structural]
edge_mechanism: "Stop-loss clusters stacked beyond well-defined range boundaries create a burst of forced market orders when the level breaks; this mechanical order flow extends the move before market makers can restore liquidity, giving an early directional entry a positive-expectancy edge over a cost-adjusted random entry."
data_required: [ohlcv, atr, volume, open-interest, funding-rate, order-book-depth]
min_capital_usd: 3000
capacity_usd: 30000000
crowding_risk: medium
expected_sharpe: 0.70
expected_max_drawdown: 0.22
breakeven_cost_bps: 40
kill_criteria: |
  - Rolling 6-month drawdown > 22% of strategy book
  - Rolling 90-day net Sharpe < 0 over ≥ 20 completed trades
  - False-breakout (immediate reversal within 2 bars) rate > 60% over last 30 signals
  - Realised round-trip slippage > 70 bps on three consecutive trades
---

# Range Breakout / Breakdown (Hyperliquid Basket)

Enters a [[perpetual-futures]] position **the moment price breaks cleanly above a well-defined range high or below a well-defined range low**, without waiting for a retest. The thesis is that the stop-loss cascade and momentum surge triggered at the break are themselves the edge — the first mover captures the best fills before the move is priced in. Stop is placed just inside the range; target is the measured move from range height.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

> **Live status (2026-06-16 dashboard snapshot):** This is the **best-performing active basket** at **27.4% capital utilisation**, with both a long and a short position open simultaneously across different assets.

> **Not investment advice.** This page is a design document for a systematic trading basket. All performance figures are ILLUSTRATIVE ESTIMATES unless marked as live.

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]).

- **Behavioral**: Traders anchored to the prior range set stops just beyond boundary levels. When price breaks, those stops become market orders — forced, price-insensitive order flow that extends the move directionally. Range-bound mean-reversion traders simultaneously add to losing positions, compounding the fuel.
- **Structural**: Well-defined range boundaries are coordination points. Systematic [[channel-breakout]] programs (e.g., [[donchian-channel-breakout]] rules), volatility-expansion models, and momentum systems all fire at the same level break, creating a predictable burst of one-directional flow that temporarily overwhelms the opposing side's limit orders.

The key distinction from [[breakout-and-retest]]: this basket **does not wait for confirmation**. It accepts the higher false-breakout rate in exchange for better fills on genuine breakouts and full participation in no-pullback momentum moves.

## Why This Edge Exists

Stop-loss clusters above resistance and below support are a structural feature of any range with multiple boundary tests. Each retest deposits more stop orders at those levels; by the time the range has held 3–5 times, the cluster is large relative to local liquidity. When price finally breaks, the cascade of triggered stops is self-reinforcing: each stop fuels a tick that triggers the next stop. Market makers widen spreads and back away during this burst — temporarily reducing absorbing liquidity — which extends the move further.

The counterparties are: (1) stop-selling buyers who were long inside the range and are now forced out, (2) mean-reversion traders who add short at the breakout level expecting a reversal, and (3) passive market-makers who reduce exposure during the burst. All three sustain the directional move for long enough to make the early entry profitable after costs.

**Why perpetuals over spot:** funding dynamics reward early movers. In a genuine breakout, funding shifts in the breakout direction as new leveraged positions accumulate — early entries often earn carry on the winning leg during multi-day trend persistence.

## Null Hypothesis

Under a random walk, an N-period high breach has zero predictive power for future direction. Stop-cascade effects are real but brief, and the resulting gap is filled within hours in the average case. A breakout system's expected value before costs is zero; after costs it is negative. The "edge" is indistinguishable from buying high on a random walk.

**Disconfirming evidence to monitor:**

- If the basket's average holding time to target is less than the average time to stop-out, expectancy is positive; if similar, the pattern is noise.
- Post-breakout drift over 4–24 hours should be positive (for long breaks) net of the opening-bar volatility. If drift is random, the entry timing carries no information.
- The basket must outperform random-entry-same-exits on the same universe in backtest.

## Rules

**Universe:** Hyperliquid perpetuals; bias toward mid-to-large cap assets ($10M+ daily OI, $20M+ 24h volume). Thin-alt perps carry JELLY-style squeeze risk and should be sized conservatively or excluded.

**Step 1 — Range qualification:**
- Price bounded within a range for ≥ 4 bars (1h or 4h timeframe), with clearly defined high (resistance) and low (support), each tested ≥ 2×.
- Range height ≥ 1.0× ATR(14) and ≤ 6× ATR(14) — too-narrow ranges do not cover costs; too-wide ranges imply no structural compression.
- Declining or flat volume during the range increases breakout reliability (drying selling interest).

**Step 2 — Breakout trigger:**
- Price bar **closes** above resistance (long) or below support (short) on the reference timeframe.
- Do NOT enter on an intraday wick — require a full-candle close beyond the level.
- Optional: OI expansion ≥ 8% on the break candle confirms new directional positioning.

**Step 3 — Entry:**
- Enter at the open of the next bar after the breakout close (limit order at or near breakout level) or on the breakout close itself if the candle is forming in real time.
- **Leverage:** 2–3× isolated margin. Use lower end in [[volatility-regime-classification|high-volatility]] environments.
- **Stop:** Close back inside the range by ≥ 0.20× ATR(14). This is a definitive false-breakout signal.
- **Target:** Measured move = range height from breakout level. Minimum reward-to-risk 1.5:1.

**Step 4 — Manage:**
- Once position is ≥ 1× ATR in profit, switch to [[atr-trailing-stop|2× ATR trailing stop]] from highest close.
- If price immediately retests the breakout level (within 2 bars) without closing back inside the range, **hold** — this is the setup for [[breakout-and-retest]]. If it closes inside, the stop triggers.
- If the retest **fails** (price collapses back inside the range), the stop exits. Note: this is precisely the signal [[failed-breakout-failed-breakdown]] trades in the opposite direction.
- Monitor funding every 4h; if funding turns persistently adverse (> 0.06%/8h against the trade), tighten the trailing stop by 0.5× ATR.

**Regime gate:** Active in [[technical-structural-regime|technical/structural]] and trending regimes. Suppress or reduce size during confirmed ranging regimes where repeated false breakouts dominate (the [[range-mean-reversion]] basket is the regime alternative). The two baskets should not hold conflicting positions on the same asset.

## Implementation Pseudocode

```python
def range_breakout_breakdown(universe, bars_1h, state):
    signals = []

    for asset in universe:
        b = bars_1h[asset]
        atr = ATR(b, period=14)
        oi  = state.open_interest[asset]

        # Step 1: Range qualification
        rng = find_range(b, min_bars=4, min_touches=2)
        if rng is None:
            continue
        if not (1.0 * atr[-1] <= rng.height <= 6.0 * atr[-1]):
            continue

        prev_bar = b[-2]
        curr_bar = b[-1]

        # Step 2: Breakout trigger (close-based)
        broke_up   = (prev_bar.close <= rng.resistance and
                      curr_bar.close >  rng.resistance)
        broke_down = (prev_bar.close >= rng.support and
                      curr_bar.close <  rng.support)

        if not (broke_up or broke_down):
            continue

        # OI expansion filter (optional)
        oi_expanded = oi[-1] > oi[-2] * 1.08

        if broke_up:
            stop   = rng.resistance - 0.20 * atr[-1]
            target = rng.resistance + rng.height
            rr     = (target - curr_bar.close) / (curr_bar.close - stop)
            if rr >= 1.5 and oi_expanded:
                size = position_size_atr(
                    equity=state.equity,
                    risk_pct=0.012,       # risk 1.2% per trade
                    entry=curr_bar.close,
                    stop=stop,
                    leverage=2.5,
                    margin="isolated"
                )
                signals.append(long_perp(asset, size, stop=stop,
                                        target=target,
                                        trail=2.0 * atr[-1]))

        # Mirror for broke_down (short) ...

    # Regime gate: suppress if range-mean-reversion basket holds
    # a position on this asset (avoid conflicting directional bets)
    signals = [s for s in signals
               if not state.range_mv_active(s.asset)]

    return signals
```

## Indicators / Data Used

- **[[atr|ATR(14)]]** — range-qualification filter, stop distance, trailing exit, [[atr-position-sizing]]
- **OHLCV (1h or 4h)** — range detection, breakout-close confirmation
- **[[open-interest|Open Interest]]** — expansion filter to confirm new directional positioning (not merely stop-cascade short-covering)
- **[[funding-rate|Funding rate]]** — carry monitor; adverse funding tightens trailing stop
- **[[order-flow|Order book depth]]** — pre-entry check; avoid entry if the break-side book is empty (widen slippage estimate)
- **Volume** — declining volume during range, expansion on breakout bar is the textbook signal; not strictly required but corroborating

## Example Trade

**Illustrative only — not a backtest.**

| Field | Detail |
|-------|--------|
| Asset | AVAX-PERP |
| Range | $28.50 (support) – $31.00 (resistance), 6 bars on 4h (24h) |
| Breakout | 4h candle closes at $31.40 with OI +9.5% |
| Entry | $31.40 at close of breakout candle, 2.5× isolated margin |
| Stop | $30.75 (0.20× ATR below breakout level) |
| Target | $33.50 ($31.00 + $2.50 range height) |
| Reward:Risk | ~3.2:1 |
| Funding during hold | +0.025%/8h (earned carry) |
| Outcome (illustrative) | Target reached in 18h; +6.7% on notional, +16.8% on margin |

No retest occurred — price broke and continued. The [[breakout-and-retest]] basket had no entry opportunity; this basket captured the full move.

## Performance Characteristics

ILLUSTRATIVE ESTIMATES informed by live pilot data (partial):

- **Win rate:** ~38–46% (lower than [[breakout-and-retest]] by design; the higher false-breakout rate is accepted for better fills on genuine moves)
- **Payoff ratio:** ~2.0–2.5:1 on winning trades using the measured-move target and ATR trailing exit
- **Expected Sharpe:** ~0.60–0.80 net in active trending/technical regimes; negative in persistent ranging environments
- **Max drawdown:** ~18–25% in choppy markets with high false-breakout frequency
- **Cost overlay:** 40–55 bps round-trip (taker fees + elevated slippage at the breakout moment when spreads widen). This is higher than the retest-entry equivalent; factor it explicitly into target requirements.
- **Return profile:** similar to classic [[channel-breakout]] trend systems — many small stop-outs, few large winners. Positive skew; capital is compounded through clusters of trend captures.
- **Live basket note:** The basket currently runs both long and short legs simultaneously on different assets (27.4% capital utilisation as of 2026-06-16), consistent with a market environment where range structures are breaking in multiple directions.

## Capacity Limits

Constrained by the burst-of-liquidity dynamic at breakout moments. On BTC and ETH perps, single-trade capacity is $5M+ before slippage materially degrades fills. On mid-cap perps ($10M–$100M daily volume), practical per-trade capacity is $200K–$1M; beyond this, the entry itself becomes the spike that the [[failed-breakout-failed-breakdown]] basket then fades. **Strategy-level capacity: ~$30M** across a diversified basket of 6–12 concurrent positions, assuming BTC/ETH perps anchor the book with smaller allocations to mid-caps.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Choppy, false-breakout-heavy regime.** Extended periods where ranges repeatedly break and immediately reverse destroy expectancy. This is the basket's modal failure mode. The [[failed-breakout-failed-breakdown]] basket profits from exactly these failures — monitor its signal rate as a leading indicator that this basket should be suppressed.
2. **Stop-hunting on thin books.** On Hyperliquid, large participants can briefly push price through a range boundary to trigger breakout-system entries, then reverse — creating an immediate loss for breakout buyers and a profit for the stop-hunter. OI confirmation (OI did not expand on the "break") is the filter.
3. **Liquidation cascade contagion.** A market-wide deleveraging event sweeps through all correlated positions; breakout entries made in the prior 24h are caught inside the cascade ([[2025-10-crypto-liquidation-cascade]]). Isolated margin limits the damage to per-position size.
4. **Crowding on obvious levels.** Widely watched levels (round numbers, recent all-time highs, Fibonacci levels) attract so many systematic breakout orders that slippage on entry is severe and immediate reversals are common. Use lookback-defined range extremes rather than subjective chart levels.
5. **Funding carry reversal after entry.** A long breakout position that earns positive funding during entry can see funding flip negative as the market grows crowded — eroding hold returns without a price move against the position.
6. **JELLY-style squeeze on a short leg.** Coordinated spot-buying squeezes a thin perp through the breakout stop and into HLP ([[2025-03-jellyjelly-hlp-attack]]). Mitigant: isolated margin, per-leg size caps on low-OI assets.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the full framework.

- Rolling 6-month drawdown > **22%** of strategy book → halt, full review
- Rolling 90-day net Sharpe < **0** over ≥ 20 completed trades → stop new entries
- False-breakout rate (immediate reversal within 2 bars) > **60%** over last 30 signals → regime has shifted; redirect capital to [[range-mean-reversion]] or stand down
- Realised round-trip slippage > **70 bps** on three consecutive trades → entry execution edge is gone; pause and reassess asset selection or reference timeframe

## Advantages

- Captures the full move from the moment of breakout — superior average entry price versus the retest approach on genuine, no-pullback breakouts
- Systematic, objective rules (close-based breakout, ATR stop, measured-move target) — minimal discretion
- Compatible with [[donchian-channel-breakout]] and [[channel-breakout]] systematic frameworks; a well-tested strategy lineage (Donchian, Turtle Traders)
- Hyperliquid venue advantage: positive-carry environments on the breakout direction; isolated margin; transparent OI data for crowding checks
- Simultaneously holds long and short legs on uncorrelated assets — the basket is structurally market-neutral at the portfolio level even while each leg is directional

## Disadvantages

- Higher false-breakout rate than [[breakout-and-retest]] by design; requires a higher payoff ratio to compensate
- Entry slippage at the breakout candle is structural — spreads widen and market-maker depth retreats precisely when this basket wants to transact; taker costs are elevated
- Regime-sensitive: performs poorly in ranging environments and must be actively suppressed alongside [[range-mean-reversion]]
- The stop (0.20× ATR inside the range) is tight; in volatile markets, normal intrabar noise trips the stop before the move develops
- Adverse funding during a slow trend can convert a winning position into a marginal one; requires active monitoring

## Hyperliquid Execution Notes

- **Funding carry:** positive funding on a long breakout position earns carry while the measured move unfolds. Negative funding (longs paying > 0.05%/8h) tightens the effective target; adjust accordingly. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** use isolated margin and size for a 15–20% adverse move without liquidation at 2–3× leverage. The breakout entry is at an extreme — adverse wicks are common in the first 1–2 bars. Source: [[hyperliquid-liquidation-engine]].
- **JELLY thin-alt squeeze:** skip perps with < $3M OI or < $10M daily volume for the short leg. A coordinated spot-buy on a thin perp can squeeze a short through the stop and into HLP before a stop-loss executes. Source: [[2025-03-jellyjelly-hlp-attack]].
- **Slippage at the breakout candle:** use limit orders at the breakout level where possible (limit to open of next bar). Avoid market orders on the breakout close — spreads are typically at session-high widths in that candle.
- **OI transparency:** Hyperliquid's public OI and leverage data allow real-time crowding monitoring. If a position direction already dominates the OI distribution (> 60% of notional long or short), reduce size — the squeeze risk is elevated and the signal may already be crowded out.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket regime framework; this basket maps to the [[technical-structural-regime]] overlay
- [[breakout-trading]] — foundational page; false-breakout rates, stop mechanics, cost overlay
- [[channel-breakout]], [[donchian-channel-breakout]] — systematic channel-breakout lineage (Donchian, Turtle Traders)
- [[technical-structural-regime]] — primary regime context for range-detection and breakout timing
- [[volatility-regime-classification]] — secondary overlay; compressed-vol environments precede the highest-quality range breaks
- [[hyperliquid-funding-rate-microstructure]], [[hyperliquid-liquidation-engine]] — venue execution and risk
- [[2025-03-jellyjelly-hlp-attack]] — thin-alt squeeze case study

## Related

[[breakout-and-retest]] · [[failed-breakout-failed-breakdown]] · [[range-mean-reversion]] · [[volatility-compression-breakout]] · [[breakout-trading]] · [[channel-breakout]] · [[donchian-channel-breakout]] · [[consolidation]] · [[support]] · [[resistance]] · [[atr]] · [[atr-trailing-stop]] · [[atr-position-sizing]] · [[open-interest]] · [[funding-rate]] · [[technical-structural-regime]] · [[volatility-regime-classification]] · [[oi-confirmed-trend]] · [[hyperliquid]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[2025-03-jellyjelly-hlp-attack]] · [[2025-10-crypto-liquidation-cascade]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
