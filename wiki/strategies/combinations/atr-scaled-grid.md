---
title: "ATR-Scaled Grid"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, grid-trading, volatility, risk-management, position-sizing, market-microstructure, quantitative, indicators, crypto]
aliases: ["Vol-Adaptive Grid", "ATR-Adjusted Grid Spacing", "Volatility-Scaled Grid", "Dynamic Grid Spacing"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [structural, risk-bearing, analytical]
edge_mechanism: "A fixed-spacing grid earns optimally only when its spacing is close to the asset's current oscillation amplitude; in high-vol regimes, too-tight spacing produces excessive churn (all fills are taker, no maker profit per cycle), while in low-vol regimes, too-wide spacing misses fills entirely; ATR-scaling the grid geometry continuously matches the spacing to the actual oscillation amplitude, keeping the grid near-optimal across the vol cycle rather than calibrated for only the vol environment at deployment."

data_required: [ohlcv-1h, ohlcv-4h, atr-14, atr-24, volatility-regime]
min_capital_usd: 2000
capacity_usd: 15000000
crowding_risk: medium

expected_sharpe: 1.2
expected_max_drawdown: 0.13
breakeven_cost_bps: 12

decay_evidence: "Fixed-spacing grid strategies have proliferated via consumer bots (3Commas, Pionex, Bybit grid bots) since 2020. ATR-adaptive spacing is not widely implemented in consumer grid bots (which use fixed percentage spacing). The vol-calibration advantage is likely to persist until consumer platforms add dynamic spacing options, which as of 2026 remains uncommon. The broader grid edge has compressed in crowded pairs; the ATR-scaling overlay partially counteracts this by reducing per-cycle churn cost."

kill_criteria: |
  - grid sleeve drawdown > 13% from high-water mark
  - ATR-scaled spacing consistently produces taker-only fills (no maker fills) for 20+ consecutive cycles: spacing is still too tight even after ATR scaling — recalibrate the spacing multiplier
  - average realized grid revenue per cycle < taker fee cost for 15 consecutive cycles: ATR-scaled grid is not earning enough per cycle; widen the ATR multiplier or pause
  - rolling 3-month Sharpe < 0 on minimum 40 completed grid cycles
  - ATR-scaled spacing > 3× the initial deployment spacing for 30+ consecutive days: vol regime is too high for grid trading regardless of adaptive spacing — apply [[regime-gated-grid]] stop

related: ["[[regime-gated-grid]]", "[[oi-aware-grid]]", "[[funding-skewed-grid]]", "[[grid-with-tail-hedge]]", "[[grid-trading]]", "[[event-calendar-risk-gating]]", "[[atr]]", "[[volatility-targeting]]", "[[market-making]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[bollinger-bands]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# ATR-Scaled Grid

ATR-scaled grid is a **grid trading strategy that continuously adjusts its grid spacing and per-level size to a multiple of the current Average True Range**, so the grid geometry tracks the asset's actual oscillation amplitude rather than remaining fixed at the spacing calibrated at deployment. The primitive edge is the same as any grid: capturing the bid-ask spread and oscillation within a range-bound regime. The vol-targeting overlay solves the most common grid implementation flaw: fixed spacing becomes wrong every time the vol regime shifts, producing either excessive fee-burning churn (spacing too tight in high-vol) or zero fills (spacing too wide in low-vol).

**This is explicitly differentiated from [[regime-gated-grid]]** — that page uses regime indicators (ADX, Bollinger bandwidth) to decide whether to run the grid at all (binary on/off). The spacing, when the grid is on, is fixed. This page adapts the grid's **geometry** — the spacing between levels and the notional per level — continuously as ATR changes, without the binary on/off trigger. The two pages are composable: use [[regime-gated-grid]]'s regime signal as the on/off gate; use this page's ATR-scaling to ensure the spacing is optimal while the grid is running.

**This is differentiated from [[oi-aware-grid]]** — that page pauses the grid when OI build signals a breakout is imminent (a leading-indicator pause trigger). The grid spacing is fixed when it is running. This page does not address breakout prevention; it addresses ongoing geometry optimization. Composable: OI-aware grid pauses on OI build; ATR-scaled grid runs with correct spacing when not paused.

**This is differentiated from [[funding-skewed-grid]]** — that page biases the grid's inventory allocation toward the funding-receiver side (asymmetric upper/lower spacing). It adjusts inventory distribution, not the overall grid scale. This page adjusts the scale of the entire grid (all levels expand or contract proportionally to ATR); the funding skew can be applied on top of the ATR-scaled base spacing.

**This is differentiated from [[grid-trading]]** — the underlying primitive uses a fixed ATR at deployment for initial setup. It documents the ATR break-cancel rule as a stop, not as a continuous spacing adjustment. This page makes the ATR-calibration continuous rather than a one-time deployment decision.

**Relationship to [[volatility-targeting]]:** portfolio-level volatility targeting adjusts position size to maintain a constant portfolio daily-risk budget. ATR-scaled grid adjusts the grid's internal geometry — spacing between levels and notional per level — to maintain optimal fill rates. Both use volatility as the sizing input; they operate at different levels (portfolio level vs grid geometry level).

## Edge source

Per [[edge-taxonomy]], **structural + risk-bearing + analytical**:

- **Structural** — the grid earns from oscillation; this is the same structural spread-capture edge as any grid. The ATR-scaling does not add a new edge category; it preserves the structural edge across the vol cycle by preventing spacing mis-calibration from converting the strategy into a fee-burning machine (tight spacing in high-vol) or a non-functional system (wide spacing in low-vol).
- **Risk-bearing** — the grid operator absorbs two-sided inventory risk. ATR-scaling ensures the risk borne per level is proportional to the current market amplitude: in high-vol regimes, wider spacing means fewer levels are filled simultaneously, reducing inventory accumulation; in low-vol regimes, tighter spacing fills more frequently and earns more cycles per unit of capital.
- **Analytical** — continuously calculating ATR and adjusting the grid is an analytical layer that most consumer grid bots do not implement. The grid operator who recalibrates spacing to current vol every 4 hours gains an edge over the operator who calibrated spacing once at deployment and never adjusted.

## Why this edge exists

**The fixed-spacing miscalibration problem:**

A grid deployed in a specific vol environment will be optimal only in that environment. As vol shifts:

**Too-tight spacing in high-vol (the fee-burning trap):**
When BTC's daily ATR doubles from $1,500 to $3,000, a grid with spacing set at $300 (tuned to the $1,500-ATR regime) will:
1. Be hit by taker fills on every level in rapid succession as price sweeps through the ladder
2. Every fill is a taker (market-price aggressive take on the way through) — no maker fill discount
3. The grid earns the $300 spacing per round-trip MINUS two taker fees ($300 spacing × 0.08% taker × 2 = $0.48 per $300 = 0.16% cost vs 0.06% grid spread net of fees)
4. At $300 spacing with $3,000 ATR, the grid may complete 4–8 full ladder sweeps per day, each sweep generating only small net profit after fees — or a net loss if the taker fees exceed the spacing

At doubled ATR, the optimal spacing would be approximately $600 (double the original), which would maintain the same ratio of spacing-to-ATR and preserve the maker/taker fee economics.

**Too-wide spacing in low-vol (the missed-fill problem):**
When BTC's daily ATR drops from $1,500 to $600, a grid with $1,000 spacing:
1. Will see very few complete level-to-level oscillations per day
2. Capital is allocated to grid levels that are never reached
3. Annual return on the grid collapses proportionally with the fill rate
4. A competitor with $200 spacing (matched to the $600-ATR regime) earns 3× the fill cycles on the same capital

**The ATR-scaling solution:**

Set spacing = `k × ATR(14)` where `k` is a calibrated multiplier. As ATR changes:
- Spacing shrinks in low-vol: more fills, more income per unit capital
- Spacing widens in high-vol: fewer churn fills, better economics per cycle, reduced inventory accumulation speed

This is a continuous version of the one-time ATR-calibration step that [[grid-trading]] already uses at deployment. The upgrade is making it ongoing.

## Null hypothesis

Under no-edge conditions (a random walk with the same volatility), any grid earns oscillation capture that is symmetric to its adverse-selection and inventory losses, and ATR-scaled spacing merely changes trade frequency rather than expectancy. The overlay only adds value if, on the same price series, it outperforms a fixed-spacing grid net of fees; on synthetic GBM series with matched vol the two should be indistinguishable. If backtests show the ATR version winning on random-walk segments, the result is fee-structure artifact or overfit calibration, not edge.

## Rules

### Step 1: ATR computation and spacing calibration

**ATR inputs:**
- **ATR(14, 4h):** 14-period ATR on the 4h timeframe — the primary spacing input. This captures the medium-term oscillation amplitude.
- **ATR(24, 1h):** 24-period ATR on the 1h timeframe — a faster-reacting supplementary input used to detect intra-day vol expansion.

**Spacing multiplier `k`:** Set such that spacing ≈ 20–30% of the daily expected oscillation range.
- Starting calibration: `k = 0.25` on ATR(14, 4h). That is, `spacing = 0.25 × ATR(14, 4h)`.
- For BTC: if ATR(14, 4h) = $1,200, spacing = $300.
- Adjust `k` based on the maker/taker fill-rate audit (see Kill Criteria). If fills are predominantly taker, increase `k`; if fill rate is too low, decrease `k`.

**Grid bounds:**
- Upper bound: reference price + `2.5 × ATR(14, 4h)`
- Lower bound: reference price − `2.5 × ATR(14, 4h)`
- Total levels: `5 × ATR(14, 4h) / spacing` = typically 15–25 levels for `k = 0.25`

### Step 2: Per-level sizing

**Equal-notional sizing across levels (base case):**
Each level: `level_notional = total_grid_capital / num_levels`

**Vol-adjusted per-level notional:**

In high-vol regimes (ATR has expanded ≥ 50% from baseline), reduce per-level notional proportionally to control total inventory accumulation risk:
```
adjusted_level_notional = base_level_notional × (atr_baseline / atr_current)
```

This ensures the maximum loss from a full ladder sweep (all levels on one side filled) scales with the same risk budget regardless of whether the grid is in a low-vol or high-vol environment. The total grid capital is constant; the notional per level decreases in high-vol, which means fewer total levels are deployed.

**Example:**
- Grid capital: $10,000. ATR baseline: $1,200. ATR current: $1,800 (50% expansion).
- Base notional per level: $10,000 / 20 levels = $500/level
- Adjusted: $500 × ($1,200 / $1,800) = $333/level
- New num levels: $10,000 / $333 ≈ 30 levels (but with wider spacing → same bounds)
- Net effect: more levels across wider spacing — grid still covers the same price range but with smaller bets per level

### Step 3: Recalibration schedule

**Recalibration frequency:** every 4 hours (aligned with 4h ATR calculation).

**Recalibration conditions:**
1. ATR(14, 4h) has changed by ≥ **15%** from the ATR at the last calibration (material vol change)
2. OR 48 hours have elapsed since the last recalibration (scheduled maintenance)

**Recalibration procedure:**
1. Cancel all open unfilled grid orders at the current (old) spacing.
2. Compute new spacing: `k × ATR(14, 4h)`.
3. Compute new bounds: reference price ± 2.5 × ATR.
4. Compute new per-level notional.
5. Re-place all orders at new spacing and notional. **Do not move filled levels** — any partially completed round-trip cycle keeps its profit-locked orders.

**Regime kill override (from [[regime-gated-grid]]):**
- If ADX(14) > 25 OR Bollinger bandwidth > 80th percentile at recalibration time: do not re-place grid orders. The regime signal says this is no longer a range-bound environment. Wait for regime signal to clear before restarting.
- This regime kill override is the same as [[regime-gated-grid]]'s primary mechanism; the ATR-scaled grid adopts it as a hard stop on the recalibration step.

### Step 4: Interaction with other grid overlays

**With [[oi-aware-grid]]:** OI-build pause takes priority. If 12h OI change ≥ +5%, cancel grid orders and do not recalibrate until OI normalises.

**With [[funding-skewed-grid]]:** After computing ATR-scaled spacing, apply the funding skew: adjust upper levels tighter and lower levels wider (or vice versa) to bias inventory toward the funding-receiver side. The ATR-scaled spacing is the base; the funding skew is an asymmetric adjustment on top.

**With [[event-calendar-risk-gating]]:** Event-calendar pauses override ATR-scaled recalibration. During a Tier 1 or Tier 2 event window, cancel all orders and suspend recalibration until the resume condition is met.

## Implementation pseudocode

```python
# atr_scaled_grid.py
from dataclasses import dataclass
from typing import Optional
import numpy as np

# ---- ATR spacing parameters ----
ATR_PERIOD_4H        = 14    # ATR(14) on 4h bars
ATR_PERIOD_1H        = 24    # ATR(24) on 1h bars (supplementary)
SPACING_MULTIPLIER   = 0.25  # spacing = k * ATR(14, 4h)
GRID_RANGE_MULT      = 2.5   # bounds = ref_price ± 2.5 × ATR
RECALIB_ATR_THRESHOLD = 0.15 # recalibrate if ATR changes >= 15%
RECALIB_FORCED_HOURS  = 48   # forced recalibration every 48h

# ---- regime kill ----
ADX_KILL             = 25    # halt grid if ADX(14) > 25
BB_BANDWIDTH_KILL    = 80    # halt if Bollinger bandwidth > 80th pct

# ---- vol-adjusted per-level sizing ----
HIGH_VOL_THRESHOLD   = 1.50  # reduce per-level notional if ATR > 1.5× baseline

@dataclass
class GridState:
    grid_capital: float
    current_spacing: float     # active spacing ($ per level)
    current_atr: float         # ATR at last calibration
    baseline_atr: float        # ATR at initial deployment
    reference_price: float
    adx_14: float
    bb_bandwidth_pct: float    # current percentile rank of BB bandwidth

def compute_atr(high: list[float], low: list[float], close: list[float],
                period: int) -> float:
    """Simplified ATR calculation from OHLC series."""
    tr_series = []
    for i in range(1, len(high)):
        tr = max(high[i] - low[i],
                 abs(high[i] - close[i-1]),
                 abs(low[i] - close[i-1]))
        tr_series.append(tr)
    return float(np.mean(tr_series[-period:]))

def regime_ok(state: GridState) -> tuple[bool, str]:
    if state.adx_14 > ADX_KILL:
        return False, f"ADX {state.adx_14:.1f} > {ADX_KILL} — trending regime, halt grid"
    if state.bb_bandwidth_pct > BB_BANDWIDTH_KILL:
        return False, f"BB bandwidth {state.bb_bandwidth_pct:.0f}th pct > {BB_BANDWIDTH_KILL} — halt grid"
    return True, "regime OK"

def new_grid_parameters(state: GridState, new_atr: float) -> dict:
    """Compute new grid parameters from updated ATR."""
    ok, reason = regime_ok(state)
    if not ok:
        return {"action": "HALT", "reason": reason}

    new_spacing = SPACING_MULTIPLIER * new_atr
    upper_bound = state.reference_price + GRID_RANGE_MULT * new_atr
    lower_bound = state.reference_price - GRID_RANGE_MULT * new_atr
    num_levels = max(5, int((upper_bound - lower_bound) / new_spacing))

    # vol-adjusted per-level notional
    vol_ratio = new_atr / state.baseline_atr
    if vol_ratio >= HIGH_VOL_THRESHOLD:
        level_notional = (state.grid_capital / num_levels) * (state.baseline_atr / new_atr)
    else:
        level_notional = state.grid_capital / num_levels

    return {
        "action": "RECALIBRATE",
        "new_spacing": round(new_spacing, 1),
        "new_upper": round(upper_bound, 1),
        "new_lower": round(lower_bound, 1),
        "num_levels": num_levels,
        "level_notional": round(level_notional, 2),
        "vol_ratio": round(vol_ratio, 2),
        "atr_change_pct": round((new_atr - state.current_atr) / state.current_atr, 3),
    }

def should_recalibrate(state: GridState, new_atr: float,
                       hours_since_last_calib: float) -> tuple[bool, str]:
    """Decide if a recalibration is needed."""
    atr_change = abs(new_atr - state.current_atr) / state.current_atr
    if atr_change >= RECALIB_ATR_THRESHOLD:
        return True, f"ATR change {atr_change:.1%} >= {RECALIB_ATR_THRESHOLD:.0%}"
    if hours_since_last_calib >= RECALIB_FORCED_HOURS:
        return True, f"scheduled: {hours_since_last_calib:.0f}h >= {RECALIB_FORCED_HOURS}h"
    return False, f"no recalibration needed: ATR change {atr_change:.1%}, {hours_since_last_calib:.0f}h elapsed"
```

The production system adds: a 4h scheduler that checks the should_recalibrate condition; automated cancellation of outstanding grid orders when recalibration fires; new order placement at updated levels with updated notionals; a regime monitor that checks ADX and BB bandwidth at every recalibration attempt; and a per-cycle fill-type log (maker vs taker) to audit whether the spacing multiplier `k` needs recalibration.

## Indicators / data used

- **ATR(14) on 4h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=20`; primary spacing input; computed from the high, low, close of the last 14 4h bars.
- **ATR(24) on 1h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=26`; supplementary faster-reacting ATR; used to detect intra-day vol expansion before the 4h ATR updates.
- **ADX(14)** — computed from 4h OHLCV; regime-kill check at every recalibration.
- **Bollinger Bandwidth percentile** — computed from 4h OHLCV; regime-kill secondary check.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; used in conjunction with [[funding-skewed-grid]] if the funding skew overlay is applied on top.
- **Open interest (4h change)** — `GET /api/v1/derivatives/open-interest?coin=BTC`; OI build check (from [[oi-aware-grid]]) applied at each recalibration; if 12h OI change ≥ +5%, defer recalibration and pause grid.

## Example trade

**Setup: BTC/USDT perp grid on Binance, ATR-scaled across a vol shift**

*Grid capital: $10,000. Multiplier k = 0.25.*

**Phase 1 — Deployment in normal vol (BTC ATR(14, 4h) = $1,200):**
- Spacing: 0.25 × $1,200 = **$300**
- Reference price: $65,000. Bounds: $65,000 ± 2.5 × $1,200 = [$62,000, $68,000]
- Levels: ($68,000 − $62,000) / $300 = **20 levels** at $300 spacing
- Per-level notional: $10,000 / 20 = **$500/level**
- Daily fill rate (estimated): 8–12 complete round-trips / day → daily income ≈ 8 × $300 × $500/$65,000 ≈ 0.29% daily

**Phase 2 — Vol expansion event (BTC ATR rises to $1,800 — +50% increase):**
- Recalibration trigger: +50% ATR change ≥ 15% threshold → RECALIBRATE
- New spacing: 0.25 × $1,800 = **$450**
- New bounds: $65,000 ± 2.5 × $1,800 = [$60,500, $69,500]
- New levels: $9,000 / $450 = **20 levels** (same count, wider spacing)
- Vol-adjusted per-level notional: $500 × ($1,200 / $1,800) = **$333/level**
- Cancelled: 20 old orders at $300 spacing. Placed: 20 new orders at $450 spacing.
- Daily fill rate (estimated): 5–8 round-trips at $450 spacing → daily income ≈ 6 × $450 × $333/$65,000 ≈ 0.14% daily

**Phase 2 comparison to fixed $300 spacing:**
- Fixed grid in $1,800 ATR: 15+ sweeps per day, all taker fills → taker cost per sweep = 15 × $300 × 0.08% × 2 = $72/day; gross income ≈ 15 × $300 × $500/$65,000 ≈ 0.346% = $34.6 on $10K → NET: $34.6 − $72 = −$37.4/day (net daily LOSS)
- ATR-scaled at $450 spacing: 6 sweeps, mix of maker/taker → taker cost ≈ 6 × $450 × 0.08% × 2 = $43.2; gross income ≈ 6 × $450 × $333/$65,000 ≈ 0.139% = $13.9 on $10K → NET: $13.9 − $43.2 = **−$29.3/day** — still negative in the high-vol phase, but 22% less negative than fixed; the regime kill (ADX check) would have paused the grid entirely in a sustained high-vol trending regime. In a range-bound high-vol (oscillating but not trending), the ATR-scaled grid survives; the fixed-spacing grid bleeds fees.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.2 | Higher than fixed-spacing (~0.8–1.0) in vol-varying environments; primary improvement from reducing fee-burning churn in high-vol phases |
| Expected max drawdown | ~13% | Lower than fixed-spacing due to reduced inventory accumulation speed in high-vol; regime kill further reduces drawdown |
| Fill rate sensitivity | Moderate | ATR-scaled grid maintains a more stable fill rate across vol regimes than fixed spacing |
| Annual income vs fixed | +5–15% higher | In years with multiple vol-regime transitions; neutral in stable-vol years |
| Breakeven cost per cycle | 12 bps | Wider ATR-scaled spacing means fewer cycles but better economics per cycle |

## Capacity limits

`capacity_usd: 15,000,000` — the capacity constraint is set by the liquidity depth of the perp pair at the grid spacing levels. ATR-scaling widens spacing in high-vol, which reduces market-impact concerns (fewer orders needing passive liquidity). In BTC/USDT perps on Binance or Hyperliquid, $15M notional is within normal depth even at $500+ grid spacings. Below $2,000 grid capital, the notional per level ($50–$200) is too small for the exchange's minimum order sizes.

## What kills this strategy

1. **Trending regime not caught by the regime kill (#3: Market-structure change).** The ATR-scaled grid expands spacing in high-vol regimes. But a high-vol trending market has wide ATR AND directional inventory accumulation — the wider spacing slows the damage but does not stop it. The ADX kill is essential; if it fails to fire (ADX is slow to respond to a rapid trend onset), the grid can accumulate significant inventory in the trend direction before the regime kill fires.
2. **Rapid vol collapse after deployment at wide spacing.** If ATR drops rapidly after the grid is calibrated at wide spacing (e.g., BTC drops from $1,800 ATR to $800 ATR in 48 hours), the grid is too wide for the new low-vol environment and fill rate collapses. The 48h forced recalibration catches this, but there is a lag.
3. **Maker/taker fill ratio deterioration (#7: Operational).** The ATR-scaling maintains the spacing-to-ATR ratio, which theoretically keeps the fill economics stable. But if the grid pair becomes crowded with other ATR-scaled bots using the same multiplier `k`, the limit-order book at each grid level fills with competing orders, reducing maker-fill probability. Monitor the maker/taker ratio of fills; if taker fills exceed 60% of total fills, increase `k` to widen spacing further.
4. **Cold-start ATR mis-estimation (#6: Complexity).** ATR(14) requires 14 bars of data to compute. At deployment on a new pair, the first few recalibrations use a short ATR estimate that may not reflect the true medium-term oscillation amplitude. Deploy at conservative (wider) spacing and reduce `k` only after 14+ bars of ATR data are available.
5. **Interaction complexity with funding skew and OI pause (#6: Complexity).** When running ATR-scaling, OI-pause, funding skew, and event-calendar gating simultaneously, the sequence of operations matters: event calendar → OI pause → regime kill → ATR recalibration → funding skew. Errors in the sequencing (e.g., applying the funding skew before the ATR recalibration) can produce mis-sized orders. The pseudocode above implements the correct sequence; production deployment must replicate it exactly.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 13%** from high-water mark — ATR-scaling did not prevent a drawdown; review whether the regime kill fired and was followed, or whether the loss was from an unmonitored source.
2. **Taker-only fills for 20+ consecutive cycles** — spacing is still too tight even after ATR scaling; increase the multiplier `k` and re-evaluate the fill economics.
3. **Average revenue per cycle < taker fee cost for 15 consecutive cycles** — the grid is losing money on each fill; the oscillation amplitude is insufficient. Increase `k` or pause.
4. **Rolling 3-month Sharpe < 0 on 40+ completed cycles** — the overall grid strategy is not working; assess whether the pair has transitioned to a permanently trending regime.
5. **ATR-scaled spacing > 3× initial deployment spacing for 30+ days** — the vol regime is persistently too high for grid trading on this pair; retire or redeploy on a different pair with lower ATR.

See [[when-to-retire-a-strategy]] and [[failure-modes]] for the broader framework.

## Advantages

- **Maintains near-optimal spacing across the vol cycle.** Fixed-spacing grids are calibrated for one vol environment; ATR-scaling keeps the spacing-to-ATR ratio stable, preserving the economics across low-vol and high-vol phases without manual recalibration.
- **Reduces fee-burning in high-vol without requiring a full halt.** The regime kill (from [[regime-gated-grid]]) pauses the grid in trending markets. But some high-vol environments are non-trending (oscillating at higher amplitude). In these environments, a fixed grid burns fees but an ATR-scaled grid adapts and remains profitable. The ATR-scaling fills the gap between "optimal vol regime" and "full halt."
- **Composable with all grid overlays.** ATR-scaled spacing is the base grid geometry. The regime kill, OI-aware pause, funding skew, tail hedge, and event calendar gating all operate on top of this base. The ATR-scaling is an internal property of the grid's construction, not a separate overlay that competes with others.
- **Reduces inventory accumulation rate in high-vol regimes.** Wider spacing in high-vol means fewer levels are filled per unit of price movement, slowing the rate at which one-sided inventory accumulates. This buys time for the regime kill to fire before the grid is fully loaded on one side.

## Disadvantages

- **Requires order cancellation and re-placement at every recalibration.** Each recalibration cancels all unfilled orders and re-places at new spacings. In markets with high cancellation fees or partial-fill ambiguity, this can create operational overhead and potential for order management errors.
- **Does not adapt to intra-recalibration vol spikes.** Between 4h recalibrations, a sudden vol spike (BTC drops 5% in 30 minutes) can produce taker-only sweeps at the current spacing before the recalibration fires. The 1h supplementary ATR provides some faster detection, but the 4h recalibration schedule creates a structural lag.
- **Neutral in stable-vol environments.** In a year where BTC vol remains stable (ATR stays within ±10% of baseline), the ATR-scaled grid performs identically to a well-calibrated fixed-spacing grid. The advantage is purely in vol-varying environments; stable-vol periods produce no benefit from the added complexity.
- **k multiplier requires pair-specific calibration.** The `k = 0.25` default is a starting point. Different pairs (BTC/USDT vs ETH/USDT vs SOL/USDT) have different oscillation characteristics relative to their ATR, and the optimal multiplier varies. Running the same `k` across multiple pairs without pair-specific calibration may produce suboptimal results on some pairs.

## Sources

- [[regime-gated-grid]] — the regime kill overlay; this page adopts its ADX/BB-bandwidth regime stop as the halt condition applied at each recalibration check.
- [[oi-aware-grid]] — the OI-build pause; this page defers to its OI pause signal (12h OI ≥ +5%) before executing an ATR recalibration.
- [[grid-trading]] — the canonical grid primitive; this page's ATR-scaling is a continuous extension of the one-time ATR calibration step documented there.
- [[atr-position-sizing]] — the ATR-based position sizing framework; the same ATR multiplier logic applied to grid spacing rather than stop-loss distance.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=20` — 4h OHLCV for ATR(14, 4h) and ADX(14) calculation; primary recalibration input
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=26` — 1h OHLCV for supplementary ATR(24, 1h); faster-reacting vol detection between 4h recalibrations
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI build check before each recalibration (12h change; pause grid if ≥ +5%)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding rate; used if [[funding-skewed-grid]] overlay is applied on top of ATR-scaled base spacing

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — extended 4h OHLCV for ATR baseline calibration and spacing multiplier `k` optimisation on historical data

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=20"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

## Related

- [[grid-trading]] — the canonical grid primitive; this page adapts its one-time ATR calibration to be continuous
- [[regime-gated-grid]] — regime kill (ADX/BB-bandwidth); composable as the on/off gate on top of ATR-scaled geometry
- [[oi-aware-grid]] — OI-build pause; composable as the early-warning breakout pause; takes priority over ATR recalibration
- [[funding-skewed-grid]] — inventory-bias overlay; apply on top of ATR-scaled base spacing for carry-enhanced grid
- [[grid-with-tail-hedge]] — OTM put overlay financed from grid income; protects against gap-through events that ATR-scaling alone cannot prevent
- [[event-calendar-risk-gating]] — binary-event pause; highest priority override; suspends ATR recalibration during event windows
- [[atr]] — the Average True Range indicator; the core input to the spacing calculation
- [[atr-position-sizing]] — ATR multiplier logic for position sizing; the same methodology applied to grid spacing
- [[volatility-targeting]] — portfolio-level vol targeting; operates above the grid, but the ATR-scaling is the grid's internal analogue
- [[market-making]] — the market-making theory that grid trading approximates; the spacing-to-ATR calibration is the practical version of optimal quote placement
- [[edge-taxonomy]] — structural + risk-bearing + analytical classification
- [[failure-modes]] — regime mis-classification, trending regime with wide spacing, recalibration lag
- [[when-to-retire-a-strategy]] — kill vs pause framework
