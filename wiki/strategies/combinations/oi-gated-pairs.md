---
title: "OI-Gated Pairs"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, pairs-trading, arbitrage, open-interest, perpetual-futures, risk-management, quantitative, statistics, derivatives, crypto]
aliases: ["OI-Filtered Stat Arb", "Squeeze-Protected Pairs", "OI-Conditional Spread Trading", "Short-Squeeze Proof Pairs"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, informational]
edge_mechanism: "The most common short-term killer of a running stat-arb pair is a short squeeze on the overvalued leg being held short; the squeeze is mechanical — OI build on the short leg + crowded negative funding on that leg = forced short covering fuel accumulating in plain sight; the OI filter refuses entry (or forces exit) when that precondition is present on the short leg, protecting the spread from a non-economic forced-covering event that the cointegration model has no information about."

data_required: [ohlcv-daily, ohlcv-4h, funding-rates, open-interest, rolling-correlation, cointegration-p-value, long-short-ratio]
min_capital_usd: 25000
capacity_usd: 30000000
crowding_risk: low

expected_sharpe: 1.1
expected_max_drawdown: 0.16
breakeven_cost_bps: 25

decay_evidence: "OI-based squeeze-precondition monitoring is not widely adopted by systematic pairs traders, who typically focus only on price-based signals (z-score, correlation, cointegration). The squeeze-precondition pattern — OI build + crowded shorts + funding spike on the shorted leg — has been documented empirically in crypto pairs blowouts but is not yet part of standard stat-arb risk management outside of dedicated crypto desks."

kill_criteria: |
  - strategy drawdown > 16% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 12 completed spread cycles
  - OI gate fires and correctly predicts a ≥ 3σ adverse spread move in fewer than 30% of cases across 10+ gate activations (OI is not predicting squeeze risk on the short leg; recalibrate or disable)
  - cointegration p-value of primary pairs deteriorates beyond 0.15 on 90-day rolling window (structural anchor broken)
  - OI gate blocks > 70% of signal-eligible entry attempts over 90 days (OI is perpetually crowded on the short legs; recalibrate thresholds or reconsider pair selection)

related: ["[[pairs-trading]]", "[[correlation-regime-pairs]]", "[[pairs-with-funding-differential]]", "[[vol-balanced-pairs]]", "[[short-liquidation-squeeze]]", "[[leverage-stress-tail-hedge]]", "[[oi-confirmed-trend]]", "[[oi-flush-reversion]]", "[[crowded-long-funding-fade]]", "[[crowded-short-funding-fade]]", "[[open-interest]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[stat-arb]]", "[[cointegration]]", "[[z-score]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# OI-Gated Pairs

OI-gated pairs is a [[pairs-trading|stat-arb/pairs]] strategy that adds an **open-interest and funding filter on the short leg** as a prerequisite for entering — and as a live exit trigger during — any spread position where one leg is short. The primitive edge is spread mean-reversion between cointegrated crypto assets. The overlay targets the most common short-term killer of running pairs positions: a **short squeeze on the overvalued leg being held short**, driven by accumulated short crowding and the mechanical forced-covering that follows. The cointegration model tells you the spread should revert; the OI gate tells you whether the preconditions for a squeeze that would prevent that reversion are already building.

**This is explicitly differentiated from [[correlation-regime-pairs]]** — that page gates pair eligibility on the structural cointegrating relationship (rolling correlation, cointegration test significance, OU half-life). It filters out pairs that have decoupled. This page assumes the pair is structurally eligible and asks a different question: even if the cointegration is intact, is the short leg currently positioned for a mechanical squeeze that will temporarily overwhelm the structural reversion signal? The two gates address different risks and are composable: apply the regime-eligibility gate from [[correlation-regime-pairs]] first, then apply the OI squeeze-precondition gate from this page before entering.

**This is differentiated from [[pairs-with-funding-differential]]** — that page requires the funding differential to AGREE with the spread direction (you are paid carry while holding the spread). The funding filter there is a positive carry screen. This page's funding check on the short leg is a NEGATIVE squeeze-precondition screen: refuse entry if the short leg has crowded short positioning (negative funding, high OI) even if the spread direction is correct. The two filters check different aspects of funding: carry alignment (that page) vs squeeze fuel on the short leg (this page). Both are composable on the same pairs setup.

**This is differentiated from [[vol-balanced-pairs]]** — that page adjusts the relative notional of the two legs to equalise per-leg daily risk. It does not address the squeeze precondition. This page maintains the standard cointegration-based leg ratio but refuses or exits entries when squeeze fuel is present on the short leg. All three pages ([[correlation-regime-pairs]], [[vol-balanced-pairs]], this page) are composable layers on the same underlying pairs framework.

**This is differentiated from [[leverage-stress-tail-hedge]]** — that page buys OTM puts when the broad-market leverage stress composite is elevated (OI/market-cap ≥ 3%, funding ≥ 0.04%/8h). It is a portfolio-level tail-hedge triggered by aggregate market stress. This page targets the **single-leg short-squeeze precondition** within an active pairs trade — a token-specific OI + funding crowding on the shorted leg specifically, not a broad market stress signal. A pair can have a squeezeable short leg without the whole market being at tail-hedge stress levels.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + informational**:

- **Behavioral (primary)** — short-squeeze failures in pairs trades arise from a behavioral asymmetry: the crowd that is short the overvalued leg is often momentum-motivated (shorting what has rallied recently) or copying the pairs trade (crowded stat-arb). When the crowded short position builds (OI rises rapidly on the short leg, funding turns sharply negative on the shorted asset), the mechanical squeeze risk grows non-linearly. Pairs traders anchored to the cointegration signal ignore the derivative-market positioning signals; the OI gate exploits the information those traders discard.
- **Structural** — crypto perpetual futures have a mechanical squeeze architecture: when a short-leg OI spike coincides with funding turning sharply negative (shorts paying the long carry premium), large long positions are being paid to stay and shorts are being charged to stay. The funding cost accelerates short covering, which pushes mark price up, which triggers more liquidations. This cascade is **structurally built into perp markets** and is independent of any information about the asset's fair value. A pairs trade with a short on the crowded leg is holding against this structural forced-flow.
- **Informational** — OI and funding data are publicly available in real-time. The information advantage is using them systematically as a pre-entry and live-monitoring gate on the short leg, rather than discovering the squeeze is underway after the spread has moved 3 standard deviations against the position.

## Why this edge exists

**The short-leg squeeze: the classic pairs killer**

Consider a BTC/ETH cointegrated pair where ETH has over-performed. The standard pairs signal: short ETH (overvalued), long BTC (undervalued). The cointegration model says the spread should revert.

The pairs trade fails when the short leg gets squeezed:

1. Over the past 7 days, speculative shorts have been accumulating in ETH perps (momentum traders betting on ETH underperformance, plus crowded copies of the same pairs trade).
2. ETH perp OI has risen 18% in 7 days — above the entry threshold.
3. ETH funding is at −0.02%/8h: longs are being paid to hold, shorts are paying carry. The accumulated short position is expensive to maintain.
4. Any sustained bid in ETH — even unrelated to ETH fundamentals — triggers the first tier of forced short covering.
5. Forced covering pushes ETH mark price up, triggering stop-losses and liquidations on the ETH shorts.
6. The cascade drives ETH higher, widening the ETH/BTC spread from 2.3σ to 4.0σ before the structural reversion can assert.
7. The pairs trader hits the 3.5σ stop-loss, taking a loss, before the cointegration reversion occurs.

**The OI gate's role:** if the pairs trader had checked the OI condition before entering (or had a live exit trigger based on OI build on the short leg), they would have:
- Refused entry at 2.0σ because the squeeze precondition was already present
- Or exited the live position before the spread reached 3.0σ when the OI gate triggered mid-trade

**Why the edge persists:**
Most systematic pairs traders check only price-derived signals (z-score, correlation, cointegration). Derivative-market positioning data (funding, OI, long/short ratio) are not part of standard stat-arb entry logic at retail and many institutional levels. The information is public; the discipline to use it as a pre-entry gate is uncommon.

## Null hypothesis

Under the null, the OI gate **does not improve risk-adjusted returns** relative to unfiltered pairs trading:
- Pairs entries blocked by the OI gate should have the same distribution of outcomes as pairs entries that were allowed — the OI signal provides no information about spread outcome.
- The entries foregone by the OI gate should not have higher-than-average adverse outcomes; the gate is just reducing signal frequency without benefiting Sharpe.

Currently not rejected (`backtest_status: untested`). Testable predictions:
- (a) Backtest the ETH/BTC spread (2022–2025). Tag each potential entry with the OI gate status (blocked or allowed). Predict: entries blocked by the OI gate have a 25–40% higher rate of adverse spread moves ≥ 3.0σ within 10 days versus entries that passed the gate.
- (b) Compare Sharpe and max drawdown for OI-gated vs unfiltered on the same z-score entry threshold. Predict: OI-gated produces 15–25% higher Sharpe with 20–30% lower max drawdown.

## Rules

### Step 1: Pre-entry OI gate on the short leg

**Before entering any spread where one leg is short, check:**

| Gate | Condition | Action if triggered |
|---|---|---|
| OI build | Short-leg 7d OI change ≥ **+15%** | BLOCK ENTRY; wait until OI stabilises below +8% / 7d |
| OI spike | Short-leg 24h OI change ≥ **+8%** | BLOCK ENTRY; wait until 24h change < +4% |
| Funding squeeze fuel | Short-leg 8h funding ≤ **−0.015%** (longs being paid; shorts paying) AND short-leg L/S ≤ **0.80** (longs heavily outnumber shorts as a percentage) | BLOCK ENTRY; wait until funding > −0.005%/8h OR L/S > 0.90 |
| Funding spike | Short-leg 8h funding ≤ **−0.025%/8h** (extreme short-crowding regardless of OI level) | BLOCK ENTRY unconditionally |

*Note on L/S interpretation: L/S ≤ 0.80 means fewer longs than shorts by count, which in a market where the short IS the more crowded position, combined with negative funding (longs being paid = shorts being charged), confirms the squeeze precondition. The perp exchange's long/short ratio reflects the number of traders on each side weighted by position size.*

**All-clear conditions (entry allowed):**
- 7d OI change < +8% AND
- 24h OI change < +4% AND
- Funding > −0.005%/8h (not deeply negative; no severe short crowding on the short leg) AND
- L/S > 0.85 (crowd not uniformly positioned against the pairs short leg)

If the short leg passes all four conditions, proceed to the z-score entry check.

### Step 2: Standard pairs entry

Once the OI gate clears, use the standard pairs entry from [[correlation-regime-pairs]] and [[vol-balanced-pairs]]:

- **Pair eligibility:** rolling 60d correlation ≥ 0.70, cointegration p ≤ 0.05, OU half-life 3–25 days.
- **Entry z-score:** ≥ 2.0 standard deviations on the 30-day log-spread.
- **Optional funding alignment gate:** from [[pairs-with-funding-differential]] — if the spread direction also agrees with the funding differential (you are paid carry on the undervalued long leg), the entry quality is higher.

### Step 3: Live OI monitoring during the trade

Once in a spread position:

**Check OI on the short leg every 4 hours.**

**Escalating OI build trigger (mid-trade exit):**

| Condition | Action |
|---|---|
| Short-leg OI 4h change ≥ **+4%** (rapid intra-session build) | Reduce position to 50% immediately; full exit if the condition persists for 2 consecutive 4h periods |
| Short-leg funding crosses from positive to ≤ **−0.010%/8h** while OI is building | Exit full position immediately (squeeze ignition precondition met mid-trade) |
| Short-leg L/S drops to ≤ **0.75** (short crowding intensifying mid-trade) | Exit full position immediately |
| Short-leg OI 7d change exceeds **+20%** from any direction | Exit full position; do not re-enter until OI normalises |

**Normal exit conditions (unchanged from standard pairs):**
1. **Convergence:** z-score ≤ 0.5 standard deviations (close for profit).
2. **Stop-loss:** z-score ≥ 3.5 standard deviations (thesis invalidated).
3. **Regime break:** 60d correlation < 0.55 or cointegration p > 0.10 (structural anchor broken).
4. **Time exit:** 21 days without convergence.

### Step 4: After an OI-triggered exit

Do not re-enter the same spread until:
- Short-leg 7d OI change < +5% (OI growth has stabilised)
- AND short-leg funding > +0.00%/8h (short crowding has dissipated — longs are no longer being paid)
- AND at least 48 hours have passed since the OI trigger fired (allow the squeeze to complete before re-entering)

If the spread has widened further (z-score > 2.5) and the OI has normalised, the OI-triggered exit may have produced a re-entry at a more favourable z-score.

### Position sizing

Use [[vol-balanced-pairs]] leg sizing as the base: `notional_low-vol = total × vol_high / (vol_high + vol_low)`.

Apply an additional OI-risk scalar at entry:
- Short-leg 7d OI change in range +5% to +8% (near-threshold but allowed): size at 75% of normal notional (reduce exposure even before full gate triggers)
- Short-leg 7d OI change < +5%: full notional
- Short-leg 7d OI change ≥ +8% but < +15%: consider blocking; if entering, cap at 50% normal notional

## Implementation pseudocode

```python
# oi_gated_pairs.py
from dataclasses import dataclass
from typing import Optional
import numpy as np

# ---- OI gate thresholds ----
OI_7D_BLOCK         = 0.15   # block if short-leg 7d OI change >= 15%
OI_24H_BLOCK        = 0.08   # block if short-leg 24h OI change >= 8%
FUNDING_BLOCK       = -0.00015  # block if short-leg funding <= -0.015%/8h (as decimal)
FUNDING_EXTREME     = -0.00025  # block unconditionally if <= -0.025%/8h
LS_BLOCK            = 0.80   # block if long/short ratio <= 0.80
LS_EXIT_MID         = 0.75   # exit mid-trade if L/S drops to <= 0.75

# ---- mid-trade exit triggers ----
OI_4H_EXIT          = 0.04   # exit 50% if 4h OI change >= 4%
OI_7D_EXIT          = 0.20   # exit full if 7d OI change exceeds 20% from entry
FUNDING_EXIT        = -0.00010  # exit full if funding <= -0.010%/8h while OI is building

# ---- re-entry conditions after OI exit ----
REENTRY_OI_7D_MAX   = 0.05   # 7d OI change must be < 5% before re-entry
REENTRY_FUNDING_MIN = 0.0000 # funding must be > 0.00%/8h before re-entry
REENTRY_COOLDOWN_H  = 48     # minimum 48h cooldown after OI trigger

# ---- OI size scalar (near-threshold reduction) ----
OI_NEAR_THRESHOLD_MIN = 0.05  # reduce size when 7d OI change in [5%, 8%)
OI_NEAR_THRESHOLD_MAX = 0.08
NEAR_THRESHOLD_SIZE   = 0.75  # 75% of normal notional

@dataclass
class LegCondition:
    symbol: str
    oi_change_7d: float          # fractional (0.15 = 15%)
    oi_change_24h: float
    oi_change_4h: float
    funding_8h: float            # fractional per 8h period
    ls_ratio: float              # longs / shorts

def pre_entry_gate(short_leg: LegCondition) -> tuple[bool, str]:
    """Returns (allowed, reason). True = entry allowed."""
    if short_leg.funding_8h <= FUNDING_EXTREME:
        return False, (f"funding extreme: {short_leg.funding_8h:.4%}/8h <= "
                       f"{FUNDING_EXTREME:.4%} — unconditional block")
    if short_leg.oi_change_7d >= OI_7D_BLOCK:
        return False, (f"7d OI build: {short_leg.oi_change_7d:.1%} >= {OI_7D_BLOCK:.0%}")
    if short_leg.oi_change_24h >= OI_24H_BLOCK:
        return False, (f"24h OI spike: {short_leg.oi_change_24h:.1%} >= {OI_24H_BLOCK:.0%}")
    if short_leg.funding_8h <= FUNDING_BLOCK and short_leg.ls_ratio <= LS_BLOCK:
        return False, (f"squeeze fuel: funding={short_leg.funding_8h:.4%}/8h AND "
                       f"L/S={short_leg.ls_ratio:.2f} <= {LS_BLOCK}")
    return True, "OI gate clear — entry allowed"

def size_scalar(short_leg: LegCondition) -> float:
    """Return notional scalar (0.0–1.0) based on near-threshold OI."""
    if OI_NEAR_THRESHOLD_MIN <= short_leg.oi_change_7d < OI_NEAR_THRESHOLD_MAX:
        return NEAR_THRESHOLD_SIZE
    return 1.0

def mid_trade_monitor(
    short_leg: LegCondition,
    oi_change_7d_at_entry: float,
    hours_since_oi_trigger: Optional[float],
) -> dict:
    """Check live OI conditions; return action for current period."""
    oi_7d_since_entry = short_leg.oi_change_7d - oi_change_7d_at_entry

    # unconditional full exit conditions
    if short_leg.ls_ratio <= LS_EXIT_MID:
        return {"action": "EXIT_FULL",
                "reason": f"L/S={short_leg.ls_ratio:.2f} <= {LS_EXIT_MID} — short-crowd extreme"}
    if oi_7d_since_entry >= OI_7D_EXIT:
        return {"action": "EXIT_FULL",
                "reason": f"7d OI build since entry = {oi_7d_since_entry:.1%} >= {OI_7D_EXIT:.0%}"}
    # squeeze ignition
    if (short_leg.funding_8h <= FUNDING_EXIT and
            short_leg.oi_change_4h >= OI_4H_EXIT / 2):  # funding turning + OI building
        return {"action": "EXIT_FULL",
                "reason": (f"squeeze ignition: funding={short_leg.funding_8h:.4%}/8h AND "
                           f"4h OI change={short_leg.oi_change_4h:.1%}")}
    # partial reduction
    if short_leg.oi_change_4h >= OI_4H_EXIT:
        return {"action": "REDUCE_HALF",
                "reason": f"4h OI spike: {short_leg.oi_change_4h:.1%} >= {OI_4H_EXIT:.0%}"}
    return {"action": "HOLD", "reason": "OI conditions nominal"}

def reentry_allowed(
    short_leg: LegCondition,
    hours_since_exit: float,
) -> tuple[bool, str]:
    """Check if re-entry is allowed after an OI-triggered exit."""
    if hours_since_exit < REENTRY_COOLDOWN_H:
        return False, f"cooldown: {hours_since_exit:.0f}h < {REENTRY_COOLDOWN_H}h required"
    if short_leg.oi_change_7d >= REENTRY_OI_7D_MAX:
        return False, f"OI not normalised: 7d change = {short_leg.oi_change_7d:.1%}"
    if short_leg.funding_8h <= REENTRY_FUNDING_MIN:
        return False, f"funding not recovered: {short_leg.funding_8h:.4%}/8h"
    return True, "re-entry conditions met"
```

The production system adds: a real-time OI feed polling every 4 hours during active pairs positions (via the CryptoDataAPI derivatives endpoint); a pre-entry OI check that runs before every z-score entry signal fires; an automated position-size scalar at entry based on the near-threshold OI condition; an alert when any mid-trade OI exit trigger fires; and a post-trade log comparing OI conditions at entry vs outcome (spread convergence vs squeeze) to calibrate the gate thresholds over time.

## Indicators / data used

- **Open interest (both legs)** — `GET /api/v1/derivatives/open-interest?coin=BTC` and `?coin=ETH`; the primary squeeze-precondition signal; 7d change, 24h change, and 4h change are all computed from this feed.
- **Funding rates (short leg primarily)** — `GET /api/v1/derivatives/funding-rates?coin=BTC` and `?coin=ETH`; the funding direction on the short leg is the second dimension of the squeeze-precondition gate.
- **Long/short ratio (short leg)** — `GET /api/v1/derivatives/binance/long-short-ratio?coin=BTC`; confirms crowd positioning on the short leg; supplements the OI and funding signals.
- **Daily OHLCV (both legs)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`; rolling correlation, cointegration test, z-score calculation (standard pairs inputs).
- **4h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=42`; higher-frequency z-score monitoring and mid-trade OI check timing.
- **Regime context** — `GET /api/v1/regimes/current`; if `Structural_Shock` or `High_Leverage_Stress`, all pairs flat — no new entries regardless of OI gate status.

## Example trade

**Setup: ETH/BTC spread, OI gate blocking and then allowing an entry**

*Portfolio: $100,000. Target spread notional: $10,000.*

**Day 1 — Signal present, OI gate blocks:**
- ETH 30d log-spread z-score: +2.2 (ETH over-performed BTC; signal to short ETH)
- ETH (short leg) 7d OI change: +19% — **OI gate triggered**. Block entry.
- ETH funding: −0.012%/8h (shorts paying; squeeze fuel building)
- Decision: WAIT. The squeeze precondition is active on the short leg.

**Day 4 — OI stabilises:**
- ETH 30d z-score: +2.4 (spread has widened slightly further — better entry price)
- ETH 7d OI change: +7% (OI growth has stalled; still elevated but below the +15% block threshold)
- ETH 24h OI change: +1.2% (below +8% threshold)
- ETH funding: +0.003%/8h (no longer negative; shorts not paying carry)
- ETH L/S: 0.92 (balanced)
- OI gate: ALL CLEAR — entry allowed. 7d OI still near-threshold (+7%), apply 75% size scalar.

**Entry:**
- Vol-balanced sizing: BTC vol = 50%, ETH vol = 72%, ratio = 72/50 = 1.44.
- Normal notional: $10,000 → BTC long: $5,882, ETH short: $4,118
- Near-threshold OI scalar: 75% → BTC long: $4,412, ETH short: $3,088

**Day 11 — Convergence:**
- ETH has underperformed BTC over 7 days. Z-score falls from +2.4 to +0.3.
- OI throughout: stable (no mid-trade OI exit trigger fired).
- BTC leg: +3.2% → +$141. ETH short leg: −5.1% → +$157 gain on short.
- Gross P&L: $141 + $157 = $298. Less 25 bps round-trip: −$18. Net: **+$280** / +0.28% of portfolio.

**Comparison — if entered on Day 1 (no OI gate):**
- Day 1 entry: full notional ($5,882 BTC / $4,118 ETH), OI squeeze risk present
- Over days 2–4: ETH squeezed +7% (short-covering cascade driven by the OI crowding)
- Spread moves from +2.2σ to +3.8σ → stop-loss fires at 3.5σ
- Loss: BTC leg +1.2% (partial offset), ETH short leg −7.0% → net: −$288 − $83 = −$371 → large loss
- The OI gate prevented this sequence by blocking the entry on Day 1.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Higher than unfiltered pairs (~0.7–0.8) due to avoiding squeeze blowouts; same or better than [[correlation-regime-pairs]] alone |
| Expected max drawdown | ~16% | Squeeze-blowouts (which cause the largest pairs drawdowns) are the specific risk being filtered; max drawdown reduction estimated at 20–30% vs unfiltered |
| Signal frequency reduction | 15–30% fewer entries | OI gate blocks roughly 1-in-5 to 1-in-3 entry attempts; the blocked entries are disproportionately the ones that end in stop-outs |
| Average hold duration | 6–14 days | Unchanged from standard pairs (OU half-life bounds the convergence) |
| Breakeven cost budget | 25 bps | Standard two-leg perp round-trip; vol-balanced notional slightly increases absolute cost |

## Capacity limits

`capacity_usd: 30,000,000` — identical to [[vol-balanced-pairs]] and [[correlation-regime-pairs]] since all three address the same underlying pairs universe. The OI gate slightly reduces the total notional deployed at any given time (15–30% of entry signals blocked), but does not change the aggregate capacity ceiling. The binding constraint remains the number of genuinely cointegrated pairs with sufficient liquidity; BTC/ETH is the flagship pair above $5M per spread.

## What kills this strategy

1. **OI threshold mis-calibration (#6: Complexity).** If the OI block thresholds are too tight (e.g., blocking at +8% 7d change instead of +15%), the gate fires on normal OI fluctuations that do not predict squeezes, eliminating too many valid entries and reducing carry. If too loose (blocking only at +25%+), the gate misses the squeeze setups. Calibration requires historical data on ETH/BTC spread outcomes classified by OI conditions at entry. The thresholds in the Rules section are illustrative starting points; recalibrate on the specific pairs universe.
2. **OI build on the LONG leg (not the short leg) causing a different failure mode.** The OI gate focuses on the short leg's squeeze risk. An OI spike on the LONG leg (rapid accumulation of directional longs on the undervalued leg) is an unhandled risk: if the long leg's OI spikes and the underlying asset has a flash crash (long liquidation cascade), the pairs trade loses on both legs simultaneously. The [[leverage-stress-tail-hedge]] framework monitors this risk at the portfolio level; this page does not handle it at the single-pair level.
3. **Correlation between OI and cointegration breakdown (#3: Market-structure change).** In a sustained regime change (ETH permanently decouples from BTC due to ETF-specific flows), both OI on the spread-eligible pair and the cointegration break simultaneously. The OI gate may fire during the decoupling period (accurately signalling something is wrong), but the regime gate from [[correlation-regime-pairs]] is the primary defence against structural decoupling. The OI gate is designed for squeeze risk within an intact structural pair, not for detecting structural pair death.
4. **Squeeze on the long leg's shorted perp funding rate.** The gate monitors the asset being shorted. In some crowded pairs trades, the funding squeeze can develop on the *long* leg's perp (if the long leg becomes crowded long, causing negative funding on the asset being longed). This is a "carry cost" issue rather than a squeeze issue, but can erode the pair's profitability. [[pairs-with-funding-differential]] addresses this carry-alignment check; this page focuses on the squeeze risk.
5. **OI data latency.** CryptoDataAPI's OI endpoints are updated at regular intervals; in fast-moving markets, a 4h polling frequency may miss a rapid OI spike that occurs between polls. For pairs above $1M notional, consider increasing the mid-trade monitoring frequency to every 1h during active market hours.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 16%** from high-water mark — the OI gate did not prevent a major drawdown; review whether the gate fired and was ignored, or whether the loss was from an unmonitored source (long-leg cascade, structural decoupling).
2. **Rolling 6-month Sharpe < 0** on a minimum 12 completed spread cycles — the pairs signal itself may be degraded; assess whether cointegration is still intact.
3. **OI gate correctly predicts adverse spread in < 30% of activations across 10+ events** — the OI signal is not informative for this pairs universe; recalibrate or remove the gate.
4. **Cointegration p-value > 0.15 on 90-day rolling window** — the structural anchor is broken; suspend the pair.
5. **OI gate blocks > 70% of entries over 90 days** — the OI is perpetually crowded on the short legs; either the pairs universe has changed (all the good pairs are crowded long on the potentially-shorted side) or the thresholds need recalibration.

See [[when-to-retire-a-strategy]] and [[failure-modes]] for the broader framework.

## Instrument Structures

OI-gated pairs deploys on the **pair** structure with an additional pre-entry check that screens the open-interest composition of the short leg for squeeze-precondition signals.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The defining structure. Long the underperformer, short the overperformer via perps, dollar-neutral by hedge ratio — identical to [[pairs-trading]]. The OI gate operates as an entry-blocking filter on the short leg only. |
| Single-asset | Not deployed. The market-neutral construction is unchanged — if the OI gate rejects the short leg, the entire spread entry is skipped (not converted to a single-leg directional trade). |
| Basket | Not deployed. OI screening is per-perp; a basket of short legs would complicate the squeeze-precondition analysis. |
| Cross-venue | Not deployed in this strategy, though cross-venue OI aggregation (Hyperliquid + Binance OI on the same underlying) would improve the squeeze-precondition signal. |

The mechanical change from [[pairs-trading]]: before entering the short leg, OI on the short leg must satisfy: short OI ≥ 15% of total OI AND OI is not building faster than 20% per 24h on the short side. These checks confirm that a squeeze precondition is not accumulating. An existing position is exited early if the short leg's OI short-side falls below 10%.

## Advantages

- **Targets the #1 short-term failure mode of running pairs positions.** Spread squeezes — driven by OI build and crowded shorts on the short leg — are empirically the most common cause of stat-arb stop-losses in crypto. The gate addresses this specific, identifiable risk with measurable, observable data.
- **Improves entry timing by waiting for better z-scores.** When the OI gate blocks an entry at 2.0σ, the spread sometimes continues widening (driven by the squeeze) to 2.5σ or 3.0σ before OI normalises. The wait often produces a better entry price, partially offsetting the cost of foregone early entries.
- **Composable with all existing pairs layers.** The OI gate is applied after [[correlation-regime-pairs]]'s eligibility check, alongside [[vol-balanced-pairs]]'s leg sizing, and alongside [[pairs-with-funding-differential]]'s carry-alignment check. All four layers are independent and mutually reinforcing: use all four for the highest-quality pairs entries available in this wiki's framework.
- **Live monitoring creates an early-warning exit that standard stop-losses miss.** A standard 3.5σ stop-loss fires only after the damage is done. The mid-trade OI monitor fires earlier — when the squeeze is beginning, not after the 3.5σ dislocation. This earlier exit typically produces a smaller loss than waiting for the standard stop.

## Disadvantages

- **Reduces signal frequency substantially in high-OI environments.** In crowded bull markets where many assets have elevated OI, the gate blocks a larger fraction of entries. During peak bull-market phases (when cointegrated pairs are most active), the OI gate may block 30–50% of z-score entry signals, significantly reducing trade frequency and carry income.
- **Does not address squeeze risk on the long leg's perp.** The gate focuses on the asset being shorted. If the long leg becomes excessively crowded long (generating a squeeze risk on anyone shorting that asset), this page does not detect it directly. Use [[pairs-with-funding-differential]] as an additional carry-alignment check on both legs.
- **OI thresholds require pair-specific calibration.** The 15% and 8% OI build thresholds are starting points. Different pairs (ETH/BTC vs SOL/AVAX vs ARB/OP) have different structural OI dynamics and different squeeze amplitudes. The thresholds should be calibrated on at least 2 years of historical data for each pair before live deployment.
- **Cannot prevent all squeeze-driven losses.** A very rapid OI spike (from 0 to +10% in 4 hours) may trigger the mid-trade exit after the spread has already moved adversely. The gate reduces — but does not eliminate — squeeze risk. It is a probabilistic filter, not a perfect hedge.

## Sources

- [[correlation-regime-pairs]] — the cointegration-regime eligibility gate; this page's OI gate is applied on top of, not instead of, the eligibility gate.
- [[pairs-with-funding-differential]] — the carry-alignment filter; composable with this page's squeeze-precondition gate.
- [[vol-balanced-pairs]] — the per-leg vol-balanced sizing; this page's entries use vol-balanced notional as the base, with an additional OI-risk scalar applied on top.
- [[short-liquidation-squeeze]] — the short-squeeze mechanics on Hyperliquid; the squeeze precondition logic on this page is the pairs-context adaptation of the same structural dynamics documented there.
- [[leverage-stress-tail-hedge]] — the portfolio-level OI-stress tail hedge; the OI stress signals there overlap conceptually with the per-leg OI squeeze signal here, applied at different levels of granularity.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/open-interest?coin=BTC` — BTC short-leg OI; 7d change, 24h change, and 4h change computed from this feed
- `GET /api/v1/derivatives/open-interest?coin=ETH` — ETH short-leg OI (or whichever asset is the short leg)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — short-leg 8h funding rate; primary squeeze-fuel signal
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — ETH funding rate for short-leg check
- `GET /api/v1/derivatives/binance/long-short-ratio?coin=BTC` — L/S ratio for crowd-positioning confirmation
- `GET /api/v1/derivatives/binance/long-short-ratio?coin=ETH` — ETH L/S ratio
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=42` — 4h OHLCV for z-score monitoring and mid-trade OI check timing
- `GET /api/v1/regimes/current` — regime context; `Structural_Shock` → no new entries regardless of OI gate

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — daily OHLCV for rolling correlation, cointegration test, log-spread z-score calculation
- `GET /api/v1/derivatives/binance/history?days=90` — historical OI and funding for OI gate threshold calibration

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this pairs book end-to-end:

- **Signal** — daily klines for both legs (`GET /api/v1/market-data/klines?symbol={LEG}USDT&interval=1d&limit=90`) maintain the rolling correlation, cointegration state, and log-spread z-score
- **Gate** — before shorting the rich leg, `GET /api/v1/derivatives/open-interest?coin={LEG}` (7d/24h/4h OI change), `GET /api/v1/derivatives/funding-rates?coin={LEG}`, and the long/short ratio check squeeze fuel on the short side
- **Regime gate** — `GET /api/v1/regimes/current`; `Structural_Shock` blocks new spreads regardless of z-score
- **Backtest** — spread replay on `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08 spans several cointegration regimes); OI-gate replay is limited to `/derivatives/binance/history` (90d) and the Binance daily archive since 2026-03-30 — backtest the pairs logic deep, but validate the OI gate on recent data only
- **Tips** — batch both legs (and candidate substitutes) through `GET /api/v1/quant/coins/risk` in one call rather than sequential per-coin polls

## Related

- [[pairs-trading]] — the canonical stat-arb/pairs primitive
- [[correlation-regime-pairs]] — cointegration-regime eligibility gate; apply first, before this page's OI gate
- [[pairs-with-funding-differential]] — carry-alignment filter; composable with the OI squeeze gate
- [[vol-balanced-pairs]] — per-leg vol-balanced notional sizing; composable with this page's OI-risk scalar
- [[short-liquidation-squeeze]] — the short-squeeze mechanics this page defends against
- [[leverage-stress-tail-hedge]] — portfolio-level OI-stress tail hedge; the market-aggregate version of the per-leg signal here
- [[oi-confirmed-trend]] — OI confirmation as a trend-entry filter; the same OI signal used as an exit/block trigger here
- [[oi-flush-reversion]] — OI flush as a mean-reversion entry trigger; the same OI signal in a directional context
- [[crowded-short-funding-fade]] — market-wide crowded-short fade; overlaps conceptually but is a directional trade, not a pairs squeeze filter
- [[open-interest]] — the OI concept page
- [[funding-rate]] — the funding-rate concept page
- [[cointegration]] — the statistical anchor for pairs eligibility
- [[z-score]] — the spread-entry standardisation metric
- [[stat-arb]] — statistical arbitrage concept page
- [[edge-taxonomy]] — behavioral + structural + informational classification
- [[failure-modes]] — squeeze failure, threshold mis-calibration, structural decoupling
- [[when-to-retire-a-strategy]] — kill vs pause framework
