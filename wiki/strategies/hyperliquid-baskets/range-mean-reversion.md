---
title: "Range Mean Reversion (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, technical-analysis, mean-reversion, swing-trading, intraday]
aliases: ["Range Fade", "Range Boundary Fade", "Range Oscillator", "Mean Reversion Range"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[volatility-regime-classification]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[rsi-mean-reversion]]", "[[bollinger-bands]]", "[[rsi]]", "[[relative-strength-index]]", "[[grid-trading]]", "[[range-trading]]", "[[support]]", "[[resistance]]", "[[atr]]", "[[average-true-range]]", "[[open-interest]]", "[[funding-rate]]", "[[breakout-and-retest]]", "[[range-breakout-breakdown]]", "[[failed-breakout-failed-breakdown]]", "[[volatility-compression-breakout]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[hyperliquid]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[atr-position-sizing]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: pilot
edge_source: [behavioral, structural]
edge_mechanism: "In a bounded range, market participants anchored to the prior equilibrium zone bid the lower boundary and offer the upper boundary, creating a persistent mean-reversion pull; the strategy earns by systematically selling this over-extension and buying the under-extension, until the range breaks — which is exactly when the range-breakout-breakdown basket takes over."
data_required: [ohlcv, atr, bollinger-bands, rsi, open-interest, funding-rate, order-book-depth]
min_capital_usd: 3000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.75
expected_max_drawdown: 0.18
breakeven_cost_bps: 30
kill_criteria: |
  - Rolling 6-month drawdown > 18% of strategy book
  - Rolling 90-day net Sharpe < 0 over ≥ 25 completed trades
  - Two consecutive range breakouts (confirmed by range-breakout-breakdown basket signal) on same asset while holding a range-fade position — regime has shifted; flatten and exit
  - Realised round-trip slippage > 55 bps on three consecutive trades
---

# Range Mean Reversion (Hyperliquid Basket)

Buys at the lower boundary and sells (or shorts) at the upper boundary of an established range, on the assumption that the range will hold until price evidence proves otherwise. Statistical measures — [[bollinger-bands|Bollinger Band]] extremes, [[rsi|RSI]] divergence, z-score from range mean — time entries at over-extensions near the boundaries, capturing the mean-reversion pull back to the midpoint or the opposite boundary.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

> **Live status (2026-06-16 dashboard snapshot):** This is the **most capital-efficient active basket** — **81.1% of allocated capital deployed** across 3 long and 1 short position simultaneously.

> **Not investment advice.** This page is a design document for a systematic trading basket. All performance figures are ILLUSTRATIVE ESTIMATES unless marked as live.

> **Critical regime dependency:** this basket is destroyed when a range breaks. That event is exactly what [[range-breakout-breakdown]] trades. The two baskets must be coordinated: when [[range-breakout-breakdown]] fires a signal on an asset, all [[range-mean-reversion]] positions on that asset should be exited immediately.

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]).

- **Behavioral**: Traders anchor to the prior range equilibrium (the midpoint and boundaries become reference points). At the lower boundary, buyers who "missed the entry" at the midpoint finally capitulate and buy; at the upper boundary, sellers who held through the rally lock in profits. Both groups enforce the range.
- **Structural**: [[liquidity]] pools at the range boundaries. Market makers post resting limit orders at known levels; these orders act as absorbing liquidity, dampening excursions beyond the range. As long as no new information shifts the equilibrium, these limits re-fill the book at the boundaries after each touch.

## Why This Edge Exists

The counterparties at range boundaries are momentum traders and late-FOMO participants who chase price into the boundary — buying near the high expecting a breakout, selling near the low expecting a breakdown. They are systematically wrong in a ranging environment because they are predicting a regime change (trend) in a regime designed to revert (range).

The profit mechanism is symmetric: sell the over-extension at the upper boundary (target: midpoint or lower boundary); buy the under-extension at the lower boundary (target: midpoint or upper boundary). Each completed oscillation generates P&L roughly equal to half the range height minus transaction costs.

**Perpetual-futures specific dynamics:** in a ranging market, funding tends to remain near zero or oscillate mildly — neither persistent positives nor negatives accumulate, meaning carry is roughly neutral. This is distinct from [[funding-rate-harvest]] (which earns from rate extremes) and [[range-breakout-breakdown]] (which earns carry on the breakout direction). The primary alpha source here is price mean-reversion, not funding carry.

**Why 81.1% capital utilisation:** in a ranging regime, multiple assets simultaneously exhibit similar consolidation structures, allowing the basket to deploy across 3+ concurrent positions. This is the regime where this basket earns its keep — the live data reflects a period of broad market consolidation.

## Null Hypothesis

Under a random walk with no mean-reversion, prices at the range boundary carry no predictive information about future direction. The probability of the next move being toward the midpoint (vs. continuing to and through the boundary) is exactly 50% — no better than a coin flip. A range-fade strategy's win rate and payoff ratio would combine to exactly offset transaction costs, producing zero or negative net expectancy.

**Disconfirming evidence to monitor:**

- If boundary touches that result in mean-reversion occur at a rate statistically indistinguishable from 50%, the range structure carries no real information.
- If drawdowns at the boundary (adverse excursions before mean-reversion) are consistently larger than the ATR implied by range height, the boundaries are being systematically overshot — reduce leverage.
- When [[range-breakout-breakdown]] signals are firing frequently (many confirmed breakouts), this basket's win rate will be depressed — not a regime for mean-reversion.

## Rules

**Universe:** Hyperliquid perpetuals with $10M+ 24h volume. Bias toward assets in confirmed consolidation with declining or stable volume (volume expansion is an early breakout warning).

**Step 1 — Range identification:**
- Asset must have traded in a bounded range for ≥ 8 bars (4h timeframe), with at least 3 tests of each boundary.
- Range height: 2× ATR(14) ≤ range height ≤ 8× ATR(14). Narrow ranges don't pay after costs; extremely wide ranges imply no structural level.
- Volume declining or stable during consolidation — volume expansion signals an impending breakout and should trigger standby mode (do not enter new range-fade positions; alert the [[range-breakout-breakdown]] basket).

**Step 2 — Entry trigger (upper boundary / short setup):**
- Price touches or approaches the upper boundary (within 0.3× ATR).
- [[bollinger-bands|Bollinger Band]] (20, 2): price closes outside or at the upper BB, or BB width is narrow (compression).
- [[rsi|RSI(14)]] ≥ 70 (overbought) on the reference timeframe.
- At least 2 of 3 statistical criteria must be satisfied for entry.
- **Entry:** limit order at the upper boundary or at the close of the trigger bar.

**Step 2 — Entry trigger (lower boundary / long setup):**
- Mirror: price at lower boundary, price at or below lower BB, RSI(14) ≤ 30 (oversold).
- At least 2 of 3 criteria satisfied.

**Step 3 — Position:**
- **Leverage:** 1–3× isolated margin. Lower leverage in [[volatility-regime-classification|high-volatility]] environments or when the range is narrower than 3× ATR.
- **Stop:** close beyond the range boundary by ≥ 0.5× ATR(14) — a definitive breakout signal. **This stop must be respected without exception.** A position that hits this stop has been caught by a genuine breakout; averaging down into a trend is catastrophically wrong.
- **Target (primary):** range midpoint.
- **Target (extended):** opposite boundary if midpoint is reached with RSI still moderate (40–60) and no breakout warnings.
- **Multiple positions:** up to 3–4 simultaneous range-fade positions on different assets at different boundary states. Do not open multiple positions on the same asset at the same boundary touch — scale in only once per bounce.

**Step 4 — Exit conditions:**
- Target reached → close or scale out half.
- Stop triggered (close beyond boundary) → close immediately; flag asset for [[range-breakout-breakdown]] monitoring.
- Volume spike on the boundary touch (> 2× 20-period average) → do not enter or close any existing position. Volume expansion at a boundary is a breakout warning, not a mean-reversion entry.
- [[funding-rate|Funding rate]] turns persistently directional (> 0.05%/8h in one direction for 3+ consecutive periods) → tighten stops; the carry signal suggests a trend is forming.
- [[range-breakout-breakdown]] signals on the asset → **exit immediately**, do not wait for stop. The baskets coordinate on this point.

## Implementation Pseudocode

```python
def range_mean_reversion(universe, bars_4h, state):
    signals = []
    MAX_CONCURRENT = 4

    for asset in universe:
        if len(state.open_positions("range_mv", asset)) > 0:
            continue  # one position per asset in this basket

        b   = bars_4h[asset]
        atr = ATR(b, period=14)
        bb  = BollingerBands(b.close, period=20, std=2)
        rsi = RSI(b.close, period=14)
        vol = b.volume
        vol_ma = SMA(vol, period=20)

        # Hard exit: breakout-breakdown basket fired on this asset
        if state.range_breakout_signal(asset):
            state.close_all("range_mv", asset, reason="breakout_confirmed")
            continue

        # Step 1: range identification
        rng = find_range(b[-30:], min_bars=8, min_touches=3)
        if rng is None:
            continue
        if not (2.0 * atr[-1] <= rng.height <= 8.0 * atr[-1]):
            continue
        if vol[-1] > 1.8 * vol_ma[-1]:
            continue  # volume expansion: breakout warning, stand aside

        # Step 2: entry triggers
        at_upper = b[-1].close >= rng.resistance - 0.3 * atr[-1]
        at_lower = b[-1].close <= rng.support    + 0.3 * atr[-1]

        upper_criteria = [
            b[-1].close >= bb.upper[-1],
            rsi[-1] >= 70,
            b[-1].close >= rng.resistance - 0.1 * atr[-1]
        ]
        lower_criteria = [
            b[-1].close <= bb.lower[-1],
            rsi[-1] <= 30,
            b[-1].close <= rng.support + 0.1 * atr[-1]
        ]

        if at_upper and sum(upper_criteria) >= 2:
            # Short at upper boundary → target midpoint
            stop   = rng.resistance + 0.5 * atr[-1]
            target = rng.midpoint()
            rr     = (b[-1].close - target) / (stop - b[-1].close)
            if rr >= 1.2:  # accept slightly lower RR in a confirmed range
                size = position_size_atr(
                    equity=state.equity,
                    risk_pct=0.010,
                    entry=b[-1].close,
                    stop=stop,
                    leverage=2,
                    margin="isolated"
                )
                if len(state.all_open("range_mv")) < MAX_CONCURRENT:
                    signals.append(short_perp(asset, size, stop=stop,
                                             target=target,
                                             basket="range_mv"))

        elif at_lower and sum(lower_criteria) >= 2:
            # Long at lower boundary → target midpoint
            stop   = rng.support - 0.5 * atr[-1]
            target = rng.midpoint()
            rr     = (target - b[-1].close) / (b[-1].close - stop)
            if rr >= 1.2:
                size = position_size_atr(
                    equity=state.equity,
                    risk_pct=0.010,
                    entry=b[-1].close,
                    stop=stop,
                    leverage=2,
                    margin="isolated"
                )
                if len(state.all_open("range_mv")) < MAX_CONCURRENT:
                    signals.append(long_perp(asset, size, stop=stop,
                                            target=target,
                                            basket="range_mv"))

    return signals
```

## Indicators / Data Used

- **[[bollinger-bands|Bollinger Bands (20, 2)]]** — primary entry trigger; price touching the outer bands at a range boundary is the highest-quality setup
- **[[rsi|RSI(14)]]** — confirmation of over-extension (≥ 70 overbought / ≤ 30 oversold) at the boundary; RSI divergence at the boundary (price makes a new range high but RSI does not) is the strongest variant
- **[[atr|ATR(14)]]** — range height validation, stop distance, [[atr-position-sizing]], volatility-regime assessment
- **OHLCV (4h)** — range detection, boundary identification, volume expansion monitoring
- **Volume** — volume decline during consolidation confirms range; volume expansion at boundary touch signals breakout risk — do not enter
- **[[open-interest|Open Interest]]** — OI stability during consolidation confirms the range; OI expansion at a boundary touch is a breakout warning
- **[[funding-rate|Funding rate]]** — directional funding signals a trend is forming; used as an exit trigger when it turns persistently one-sided

## Example Trade

**Illustrative only — not a backtest.**

| Field | Detail |
|-------|--------|
| Asset | DOT-PERP |
| Range | $6.80 (support) – $7.60 (resistance), 12 bars on 4h |
| Setup | Price touches $7.55 (resistance area); RSI = 74, BB upper band = $7.58; 2 of 3 criteria met |
| Entry | Short at $7.54, 2× isolated margin |
| Stop | $7.98 (0.5× ATR above resistance) |
| Target | $7.20 (range midpoint) |
| Reward:Risk | ~1.9:1 |
| Outcome (illustrative) | Midpoint reached in 14h; +4.5% on notional, +9.0% on margin |

Funding remained near zero throughout (+0.01%/8h). RSI declined from 74 to 48 as price reverted. Volume was stable — no breakout signal.

## Performance Characteristics

ILLUSTRATIVE ESTIMATES informed by live pilot data (partial) and mean-reversion strategy literature:

- **Win rate:** ~55–65% (higher than trend-following strategies; the confirmed-range structure provides a high base rate for mean-reversion)
- **Payoff ratio:** ~1.3–1.8:1 (target is the midpoint, not the full range — accepting a lower payoff in exchange for a higher win rate)
- **Expected Sharpe:** ~0.65–0.85 net in confirmed ranging regimes; **sharply negative** the moment a range breaks (the fatal flaw)
- **Max drawdown:** ~12–20% in the expected regime; up to 40%+ if a simultaneous multi-asset trend break catches the basket holding multiple boundary positions
- **Cost overlay:** 30–45 bps round-trip per trade. Range-fade entries are frequently at limit prices (resting at the boundary), which reduces taker costs — this is one of the few baskets where limit-order entry is the norm, recovering 10–20 bps versus market entry.
- **Return profile:** smooth equity curve during ranging regimes, with high trade frequency (the basin runs 3–4 concurrent positions). Can hold for 8–48h per trade. Equity curve inverts sharply during breakout regimes — the primary reason for hard coordination with [[range-breakout-breakdown]].
- **Correlation note:** strongly negatively correlated with [[range-breakout-breakdown]] and mildly negatively correlated with [[breakout-and-retest]] — the baskets diversify each other naturally.

## Capacity Limits

Constrained by the depth of order books at range boundaries on Hyperliquid. Limit-order entries at the boundary are filled at the best prices available — meaning capacity is limited by the resting depth at the boundary level, not by market-impact concerns during entry. For BTC and ETH perps, single-position capacity is $2M+ before partial fills become an issue. For mid-cap perps ($10M–$50M daily volume), practical per-position capacity is $50K–$300K. **Strategy-level capacity: ~$20M** across 4 concurrent positions — consistent with the live 81.1% utilisation pattern across major and mid-cap assets.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **The range breaks.** This is the primary, existential failure mode and it is inevitable — every range eventually breaks. The question is whether the stop-loss at the boundary is respected and the position is exited cleanly, or whether the trader averages down into a trend. **Never average down on a stop trigger.** The [[range-breakout-breakdown]] basket immediately takes the other side of this event; coordinate the two baskets via a shared asset-position tracker.
2. **Simultaneous multi-asset breakout.** A market-wide trending event (macro shock, catalyst cascade) breaks multiple ranges simultaneously, hitting stops across all concurrent range-fade positions at once. This is the scenario that produces the 40%+ drawdown tail. Reduce overall basket exposure during elevated macro-event risk ([[policy-shock-regime]], [[event-catalyst-regime]]).
3. **Whipsaw at the boundary.** Price repeatedly touches the boundary, triggering the entry, and then slowly drifts through it (not a decisive breakout, not a clean reversion). Multiple small losses accumulate as the basket enters and is stopped out at the boundary repeatedly. This typically signals a range that is failing gradually rather than decisively; volume expansion monitoring is the early-warning indicator.
4. **Grid-trading convergence.** In an environment where many algorithms are running similar range-fade logic ([[grid-trading]], [[bollinger-band-reversion]]), the boundary trades become crowded and mean-reversion returns compress. Crowding risk is assessed as medium — the setup is well-known.
5. **Funding adverse while waiting at boundary.** If a position is held for multiple 8h periods while waiting for mean-reversion, adverse funding erodes the target P&L. A target of range midpoint (typically 3–5% on crypto alts) can be consumed by 10+ 8h periods of 0.05% adverse funding. Monitor carry actively.
6. **JELLY thin-alt squeeze.** Holding a short position at the upper boundary of a thin alt's range exposes the position to a coordinated squeeze ([[2025-03-jellyjelly-hlp-attack]]). Stick to assets with sufficient OI and volume.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the full framework.

- Rolling 6-month drawdown > **18%** of strategy book → halt, full review (lower threshold than breakout baskets because the strategy should have a smoother equity curve — a large drawdown implies a regime error, not a normal losing streak)
- Rolling 90-day net Sharpe < **0** over ≥ 25 completed trades → stop new entries
- Two consecutive range breakouts on the same asset while holding a range-fade position → this asset is no longer a range; exit all positions, remove from universe
- Realised round-trip slippage > **55 bps** on three consecutive trades → execution edge eroded; pause and re-evaluate liquidity thresholds

## Advantages

- Higher win rate than directional breakout strategies — confirmed ranges provide a structural edge that manifests more consistently than trend initiation signals
- Limit-order entries at range boundaries reduce taker costs; often the only basket where resting limit orders are the primary entry mode
- High capital utilisation in ranging regimes (live: 81.1%) — the basket can run 3–4 concurrent positions efficiently
- Smooth equity curve during the target regime — more consistent than breakout baskets, which have lumpy return profiles
- Naturally complements [[range-breakout-breakdown]]: when this basket's stop triggers (a breakout confirmed), the other basket enters in the same direction — the two baskets are portfolio complements that cover all range-resolution outcomes
- Hyperliquid venue: isolated margin, public OI data, funding-near-zero environments during ranging = low carry cost

## Disadvantages

- Existential regime dependency: destroyed when a range breaks. Every open position is one breakout signal away from a full stop-loss. There is no graceful degradation — the loss is sharp and immediate when the regime shifts.
- Must be coordinated with [[range-breakout-breakdown]] to avoid holding a losing range-fade position while the breakout basket would profit from the same asset — requires shared state between the two baskets.
- In fast-moving markets, limit orders at the boundary may not fill (price blows through), causing the basket to miss the entry while still monitoring an "active" range that has already broken.
- Win rate and payoff ratio at the lower boundary of acceptability for the extended target (opposite boundary) — the probability of traversing the full range without stopping out is materially lower than the probability of reaching the midpoint.
- Requires frequent monitoring (4h–8h updates) to detect volume expansions and OI shifts at boundaries — cannot be run fully passively on daily checks.

## Hyperliquid Execution Notes

- **Funding carry:** in a true ranging regime, funding oscillates near zero. If funding starts trending persistently positive (longs paying) or negative (shorts paying), it signals that directional positioning is building — tighten stops and reduce new entries. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** range-fade positions held at 2× leverage with stops 0.5× ATR beyond the boundary should survive normal intrabar wicks. However, during a cascade event, the mark price can gap through the stop level without a fill at the stop price — isolated margin contains the maximum loss to the margin per position. Source: [[hyperliquid-liquidation-engine]].
- **JELLY squeeze risk (short at upper boundary):** maintain the $5M OI minimum floor for any short boundary fade. A thin alt squeezed from $7.50 to $12.00 in 30 minutes catches a short boundary fade at the worst possible time ([[2025-03-jellyjelly-hlp-attack]]). Favour BTC, ETH, and high-OI mid-caps for the short leg.
- **Limit-order entry advantage:** unlike breakout baskets that require taker fills, boundary-fade entries can be placed as limit orders resting at the boundary level. This recovers 10–20 bps per entry and is the primary cost advantage of this basket versus intraday breakout entries. Place limits at the boundary ± 0.1× ATR; cancel if the boundary is breached without a fill.
- **OI monitoring at boundary touches:** use Hyperliquid's public OI data to assess whether a boundary touch accompanies OI expansion (breakout risk — stand aside) or OI stability/contraction (mean-reversion setup — proceed). This is a 30-second check that materially improves signal quality.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket framework; this basket is the primary [[technical-structural-regime]] mean-reversion strategy
- [[bollinger-band-reversion]], [[rsi-mean-reversion]] — the underlying statistical approaches used for entry timing
- [[range-trading]], [[grid-trading]] — related mean-reversion-in-range frameworks; this basket differs by using statistical extremes for entry rather than fixed grid levels
- [[technical-structural-regime]], [[volatility-regime-classification]] — the two regime overlays where this basket is most active
- [[hyperliquid-funding-rate-microstructure]], [[hyperliquid-liquidation-engine]] — venue execution and risk
- [[2025-03-jellyjelly-hlp-attack]] — squeeze case study for short boundary positions

## Related

[[range-breakout-breakdown]] · [[breakout-and-retest]] · [[failed-breakout-failed-breakdown]] · [[volatility-compression-breakout]] · [[mean-reversion]] · [[bollinger-band-reversion]] · [[rsi-mean-reversion]] · [[bollinger-bands]] · [[rsi]] · [[relative-strength-index]] · [[grid-trading]] · [[range-trading]] · [[support]] · [[resistance]] · [[atr]] · [[average-true-range]] · [[atr-position-sizing]] · [[open-interest]] · [[funding-rate]] · [[funding-rate-harvest]] · [[oi-confirmed-trend]] · [[perpetual-futures]] · [[liquidation]] · [[technical-structural-regime]] · [[volatility-regime-classification]] · [[liquidity-depth-regime]] · [[market-regime]] · [[trading-strategy-baskets]] · [[hyperliquid]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[2025-03-jellyjelly-hlp-attack]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
