---
title: "Breakout and Retest (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetual-futures, hyperliquid, technical-analysis, breakout, trend-following, swing-trading]
aliases: ["Breakout Retest", "Break and Retest", "Confirmed Breakout Entry", "Retest Confirmation Breakout"]
related: ["[[hyperliquid-baskets-overview]]", "[[technical-structural-regime]]", "[[volatility-regime-classification]]", "[[breakout-trading]]", "[[support]]", "[[resistance]]", "[[consolidation]]", "[[atr]]", "[[range-breakout-breakdown]]", "[[failed-breakout-failed-breakdown]]", "[[range-mean-reversion]]", "[[volatility-compression-breakout]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[hyperliquid]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[open-interest]]", "[[funding-rate]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]"]
strategy_type: technical
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [behavioral, structural]
edge_mechanism: "Retail traders anchored to the old range are slow to recognise the breakout as real; the retest shakes out weak longs (or shorts) who entered on the initial break, producing a second, higher-confidence entry precisely at the level where the structural edge — stop clusters now flipped to support — is strongest."
data_required: [ohlcv, atr, volume, open-interest, funding-rate]
min_capital_usd: 5000
capacity_usd: 25000000
crowding_risk: medium
expected_sharpe: 0.65
expected_max_drawdown: 0.20
breakeven_cost_bps: 35
kill_criteria: |
  - Rolling 6-month drawdown > 20% of strategy book
  - Rolling 12-month net Sharpe < 0 over ≥ 30 completed trades
  - Average confirmed-retest failure rate > 65% over last 40 signals (range regime dominant)
  - Realised round-trip slippage > 60 bps on three consecutive trades
---

# Breakout and Retest (Hyperliquid Basket)

A confirmation-first breakout strategy that enters a perpetual-futures position only **after** price has broken a well-defined [[support]] or [[resistance]] level **and** returned to successfully retest that level as a new zone of support (or resistance). The extra patience filters the majority of false breaks that destroy naive breakout entries, at the cost of occasionally missing fast-moving, no-pullback breakouts. Stop is placed just beyond the retested level; target is the measured move of the prior range projected from the breakout point.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

> **Not investment advice.** This page is a design document for a systematic trading basket. All performance figures are ILLUSTRATIVE ESTIMATES.

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]).

- **Behavioral**: The retest moment is a microcosm of the anchoring bias that powers all breakout strategies. Traders who missed the initial break now hesitate at the old resistance-turned-support, fearing a false breakout — exactly when the entry is cleanest. Weak-hand longs who bought the initial break exit on the pullback (confirming the retest low), handing strong hands an entry at better risk/reward.
- **Structural**: Stop-loss clusters that previously defended the resistance level now sit just below it, acting as a mechanical demand floor on the retest. If the retest holds, those defenders have flipped to buyers — a one-sided order-flow burst once the level proves itself.

## Why This Edge Exists

The counterparties are threefold: (1) anchored sellers who believe the breakout is false and add short near the old resistance during the retest, (2) weak-hand longs who bought the initial break and cut losses as price pulls back to "prove" them wrong, and (3) range-bound mean-reversion traders who still expect a return into the consolidation.

All three provide liquidity to the retest entry. They keep losing because the successful retest — price touching the old level without closing back inside the range — is statistically a stronger signal than the raw breakout alone. The behavioral bias (anchoring to the prior range) is persistent and well-documented in equity markets ([[breakout-trading]]); in perpetual-futures markets, where funding dynamics mean extended trends *pay* longs when the market leans directional, the edge is further amplified by the carry tailwind on winning positions.

**Why perpetuals specifically:** a retest that holds at the new support often coincides with funding shifting positive (longs accumulating), creating a situation where the trade earns carry *while* targeting the measured move. This is unusual — most trend entries pay carry or are funding-neutral.

## Null Hypothesis

Under a random walk, crossing an N-period high and then pulling back to it carries no incremental information versus entering on the initial break. The "retest" is just an ordinary intraday fluctuation that the random-walk model produces regularly. If true, a break-and-retest filter merely introduces *adverse selection* (missing the best clean-breakout trades) without improving the win rate on confirmed entries.

**Disconfirming evidence to monitor:**

- Retest success rate (holds vs. closes back inside the range) should materially exceed a naive base rate of ~50%. If not, the pattern is noise.
- Average P&L on retest entries should exceed average P&L on equivalent raw-breakout entries in the same universe. If the extra wait provides no edge improvement, the filter is worthless.
- Regime performance: if break-and-retest entries perform no better during [[technical-structural-regime|technical/structural regimes]] than in ranging or trending regimes, the regime-gating hypothesis is false.

## Rules

**Universe:** Hyperliquid perpetuals across major and mid-cap assets with sufficient daily volume (≥ $10M 24h volume) to absorb entries without material slippage.

**Step 1 — Identify the range:**
- Price must have traded in a bounded range for ≥ 5 bars (4h or daily timeframe) with clearly defined highs (resistance) and lows (support), tested ≥ 2× at each boundary.
- Range height must be ≥ 1× ATR(14) to make the measured-move target meaningful after costs.

**Step 2 — Confirm the breakout:**
- Price closes above resistance (long setup) or below support (short setup) on the reference timeframe (4h or daily).
- Optional volume/OI confirmation: open interest expands ≥ 10% on the breakout candle — indicates new positions entering, not short covering alone.

**Step 3 — Wait for the retest:**
- Price retraces back toward the broken level. The retest is valid if price touches or approaches the old level but **does not close back inside** the range.
- The retest must complete within 3–8 bars of the breakout candle on the reference timeframe. A retest taking longer than 8 bars risks full range re-entry (treat as failed breakout; see [[failed-breakout-failed-breakdown]]).

**Step 4 — Enter:**
- Enter long (or short) as price bounces from the retested level, ideally on the close of the first bullish (or bearish) candle off the retest low/high.
- **Leverage:** 2–4× isolated margin. Use lower end in compressed-volatility environments.
- **Stop:** close back inside the range by ≥ 0.25× ATR(14) — a definitive range re-entry.
- **Target:** measured move = range height projected from the breakout level. Minimum reward-to-risk 1.5:1.

**Step 5 — Manage:**
- Trail stop using [[atr-trailing-stop|2× ATR(14) trailing stop]] once the position is ≥ 1× ATR in profit.
- If funding flips sharply negative (longs paying > 0.05%/8h) before the target is reached, tighten stop or take partial profit.
- Cover on close back through the breakout level.

**Regime gate:** Only enter in [[technical-structural-regime|technical/structural]] or early-trending regimes. Suppress during confirmed ranging regimes where the competing [[range-mean-reversion]] basket is active — the two baskets should not both hold directional positions on the same asset simultaneously.

## Implementation Pseudocode

```python
def breakout_and_retest(universe, bars_4h, state):
    signals = []

    for asset in universe:
        b = bars_4h[asset]
        atr = ATR(b, period=14)
        volume_oi = state.open_interest[asset]

        # Step 1: Range detection
        rng = find_range(b, min_bars=5, min_touches=2)
        if rng is None:
            continue
        if rng.height < 1.0 * atr[-1]:
            continue  # range too small; costs consume measured move

        # Step 2: Breakout confirmation
        broke_up   = b[-1].close > rng.resistance and not state.in_range(asset)
        broke_down = b[-1].close < rng.support    and not state.in_range(asset)
        if not (broke_up or broke_down):
            continue

        breakout_bar = state.breakout_bar[asset]
        bars_since   = len(b) - breakout_bar

        if bars_since > 8:
            continue  # retest window expired

        # Step 3: Retest condition
        if broke_up:
            retest_touch = b[-1].low <= rng.resistance * 1.005  # within 0.5%
            close_inside = b[-1].close < rng.resistance
            if retest_touch and not close_inside:
                # Step 4: Entry
                stop   = rng.resistance - 0.25 * atr[-1]
                target = rng.resistance + rng.height  # measured move
                rr     = (target - b[-1].close) / (b[-1].close - stop)
                if rr >= 1.5:
                    size = position_size_atr(
                        equity=state.equity,
                        risk_pct=0.01,        # risk 1% of equity per trade
                        entry=b[-1].close,
                        stop=stop,
                        leverage=3,
                        margin="isolated"
                    )
                    signals.append(long_perp(asset, size, stop=stop,
                                            target=target))

        # Mirror logic for broke_down (shorts) ...

    # Regime gate: suppress if range-mean-reversion basket already
    # holds a position on this asset (avoid conflicting signals)
    signals = [s for s in signals
               if not state.range_mv_active(s.asset)]

    return signals
```

## Indicators / Data Used

- **[[atr|ATR(14)]]** — range height filter, stop distance, trailing exit, and position sizing via [[atr-position-sizing]]
- **OHLCV (4h or daily)** — range detection, breakout confirmation, retest identification
- **[[open-interest|Open Interest]]** — breakout-quality filter; OI expansion on the breakout bar confirms new positions entering
- **[[funding-rate|Funding rate]]** — carry monitor; used as a signal to tighten stops or take partial profit
- **[[support]] / [[resistance]] detection** — swing-high/low algorithm or N-period channel (e.g., [[donchian-channel-breakout]])
- **Volume** (optional) — corroborating filter; 1.5× 20-period average on breakout candle strengthens conviction

## Example Trade

**Illustrative only — not a backtest.**

| Field | Detail |
|-------|--------|
| Asset | SOL-PERP |
| Range | $140–$158 (6 days, tested 3× each side) |
| Breakout | Close above $158 with OI +12% |
| Retest | Price pulls back to $159, holds (low = $158.40), bullish close |
| Entry | $160 long, 3× isolated margin |
| Stop | $156.50 (below $158 support + 0.25× ATR) |
| Target | $176 ($158 + $18 measured move from range height) |
| Reward:Risk | ~4.7:1 |
| Outcome (illustrative) | Target reached in 4 days; +10% on notional, +30% on margin |

The retest consumed 2 candles; entry was 2 bars after the breakout candle. Funding remained mildly positive throughout (+0.02%/8h), adding ~0.12% carry to the position.

## Performance Characteristics

ILLUSTRATIVE ESTIMATES based on breakout-strategy literature and perp-specific considerations:

- **Win rate:** ~42–50% (higher than raw breakout entries by 5–10 percentage points due to the retest filter)
- **Payoff ratio:** ~1.8:1 average win / average loss on the measured-move target with ATR trailing stop
- **Expected Sharpe:** ~0.55–0.75 net of costs in trending/technical regimes; materially lower (potentially negative) in persistent ranging regimes
- **Max drawdown:** ~15–22% in extended choppy markets where retests repeatedly fail
- **Cost overlay:** 35–50 bps round-trip per trade (taker fees + slippage on entry + trailing stop exit). The measured-move target (typically 5–15% on crypto) absorbs this comfortably on winning trades.
- **Return shape:** lumpy — long flat periods during low-breakout environments, punctuated by multi-trade clusters when a trending regime fires. This basket's equity curve is positively correlated with the [[oi-confirmed-trend]] basket and inversely with [[range-mean-reversion]].

## Capacity Limits

Limited by the size of individual Hyperliquid perp order books at the retest moment. For BTC and ETH perps, single-trade capacity is effectively uncapped at this strategy's scale. For mid-cap perps ($10M–$100M daily volume), practical per-trade capacity is $500K–$2M before entry slippage at the retest bounce consumes meaningful edge. **Strategy-level capacity: ~$25M** across a diversified basket of 5–10 concurrent positions.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Extended choppy / ranging regime.** If markets stay range-bound, breakouts are quickly reversed before retests can complete, producing a bleed of false setups. This is the basket's dominant risk — it is regime-dependent on [[technical-structural-regime]] conditions. The [[range-mean-reversion]] basket thrives in exactly this environment.
2. **Retest-and-fail (trap).** The retested level appears to hold, the position is entered, and then price collapses back into the range — the textbook [[failed-breakout-failed-breakdown]] signal. The stop-loss at range re-entry contains the damage, but repeated trap setups destroy expectancy.
3. **No-pullback breakouts.** In strong momentum environments, price never pulls back for a retest. The basket misses the entire move while the [[range-breakout-breakdown]] basket (which enters on the initial break) captures it. These two baskets are explicitly complementary; run both when regime clarity is low.
4. **Stop-hunting on the retest.** On Hyperliquid, large players can momentarily push price through the retested level to trigger stops before snapping back — converting a valid retest into a failed-breakout loss. Use slightly wider stops (0.5× ATR from the level) to survive these wicks.
5. **Funding carry reversal.** If the position earns negative funding through a slow move to target, total return degrades. Monitor funding daily and tighten exits if carry turns persistently negative.
6. **Liquidation cascade contagion.** A market-wide deleveraging event ([[2025-10-crypto-liquidation-cascade]]) invalidates individual technical setups across the board; all open positions risk liquidation at leveraged prices. Isolated margin limits contagion to the individual position.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the full framework.

- Rolling 6-month drawdown > **20%** of strategy book → halt, full review
- Rolling 12-month net Sharpe < **0** over ≥ 30 completed trades → stop new entries
- Confirmed-retest failure rate > **65%** over last 40 signals → regime is ranging; redirect capital to [[range-mean-reversion]]
- Realised round-trip slippage > **60 bps** on three consecutive trades → execution edge eroded in current universe; pause and re-evaluate asset selection

## Advantages

- Retest filter materially reduces false-breakout exposure compared to naive breakout entries ([[range-breakout-breakdown]])
- Clean, objective entry and stop rules — stop is at range re-entry, target is measured move; no discretion required
- Stop-loss clusters at the retested level provide mechanical support, making the stop-placement zone self-reinforcing
- Compatible with [[atr-position-sizing]] for systematic risk management
- On Hyperliquid: isolated margin caps single-trade risk; positive-funding environments add carry tailwind to winning positions
- Complements [[range-breakout-breakdown]] (no-wait entry) — together, they cover both the immediate and delayed breakout entry paths

## Disadvantages

- Misses all fast, no-retest breakouts — a significant performance drag in strong momentum regimes where [[range-breakout-breakdown]] dominates
- Retest window (3–8 bars) requires active monitoring; entries can be time-sensitive
- Win rate still below 50%; psychologically demanding during losing streaks
- Regime-dependent: performs poorly in choppy markets and should be suppressed when [[range-mean-reversion]] is the dominant active basket
- Hyperliquid single-mark-tick liquidation and ADL risk means positions at 3–4× leverage can be forced-closed on brief wicks through the stop level during thin overnight hours

## Hyperliquid Execution Notes

- **Funding carry:** check the 8h funding rate before entry. Ideally the position earns carry (positive funding for longs, negative for shorts). If funding is adverse (> 0.05%/8h against the trade), adjust the target or reduce leverage — the carry erodes the measured-move edge over multi-day holds. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** Hyperliquid can liquidate on a single mark-price tick. Use isolated margin; size so that a 15% adverse move does not trigger liquidation. Never hold at > 5× on a swing position held overnight. Source: [[hyperliquid-liquidation-engine]].
- **JELLY thin-alt squeeze risk:** for assets outside the top 20 by OI, a coordinated spot-buy can spike the mark price and liquidate a short in minutes ([[2025-03-jellyjelly-hlp-attack]]). Skip perps with < $2M open interest or < $5M 24h volume; cap per-leg size at 0.5% of strategy book on thin names.
- **Slippage on the retest bounce:** the retest entry is a *limit-order* opportunity — price is returning to a known level. Place limit orders at the retested level rather than chasing with market orders; this recovers 15–25 bps per trade versus taker entry.
- **OI and leverage distribution:** use [[hyperliquid-vault-architecture|HL's public OI data]] to monitor crowding before sizing. If OI at the breakout direction is already at cycle highs relative to book depth, reduce size — a crowded directional bet on a thin book is squeeze fuel.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket regime framework that contextualises this basket within the trading system
- [[breakout-trading]] — foundational breakout strategy page; retest approach documented in "False Breakout Filtering" section
- [[technical-structural-regime]] — primary regime for this basket; defines the range/breakout/consolidation conditions
- [[volatility-regime-classification]] — secondary regime overlay; compressed-vol environments precede the cleanest breakouts
- [[hyperliquid-funding-rate-microstructure]], [[hyperliquid-liquidation-engine]] — venue-specific mechanics for execution and risk management
- [[2025-03-jellyjelly-hlp-attack]] — thin-alt squeeze precedent informing position-size caps

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[range-breakout-breakdown]] · [[failed-breakout-failed-breakdown]] · [[range-mean-reversion]] · [[volatility-compression-breakout]] · [[breakout-trading]] · [[support]] · [[resistance]] · [[consolidation]] · [[atr]] · [[atr-trailing-stop]] · [[atr-position-sizing]] · [[open-interest]] · [[funding-rate]] · [[perpetual-futures]] · [[market-regime]] · [[technical-structural-regime]] · [[volatility-regime-classification]] · [[oi-confirmed-trend]] · [[breadth-and-momentum-divergence]] · [[cross-sectional-relative-value]] · [[crowded-short-funding-fade]] · [[defensive-majors]] · [[distribution-post-peak-short-book]] · [[hyperliquid]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[2025-03-jellyjelly-hlp-attack]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
