---
title: "OI-Aware Grid"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, grid-trading, open-interest, market-microstructure, perpetual-futures, quantitative, risk-management, crypto]
aliases: ["OI-Gated Grid", "Open-Interest Filtered Grid", "Leverage-Aware Grid Bot", "OI-Build Grid Pause"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [structural, risk-bearing]
edge_mechanism: "Grids generate income from oscillation in range-bound, low-leverage regimes; when OI builds rapidly — signalling that fresh directional leverage is entering the market and creating breakout fuel — the grid is paused or de-sized before the trend runs through it; the OI-build signal identifies the regime transition earlier than realized-vol measures because OI accumulates before the breakout occurs, giving the grid a leading-indicator gate rather than a lagging one."

data_required: [ohlcv-1h, ohlcv-4h, open-interest, funding-rates, atr-14, vol-regime-score]
min_capital_usd: 2000
capacity_usd: 15000000
crowding_risk: medium

expected_sharpe: 1.2
expected_max_drawdown: 0.12
breakeven_cost_bps: 12

decay_evidence: "Grid strategies on consumer platforms (3Commas, Pionex, Hyperliquid grid bots) have proliferated since 2020; OI-based overlays are not yet widely adopted by retail grid operators. The OI-build signal's leading-indicator property relative to vol-regime flips is a structural feature of how leverage builds pre-breakout; this property is unlikely to decay until a large share of grid operators adopt OI monitoring, which is not yet the case."

kill_criteria: |
  - grid sleeve drawdown > 12% from high-water mark
  - OI-build pause fires within 24h of grid activation in 4 of 5 consecutive activations (the OI signal is triggering too frequently; recalibrate the build-rate threshold)
  - 3 consecutive grid runs end at a loss after the grid was running (not at an OI-pause exit): the underlying range-bound regime assumption is wrong, not just the pause timing
  - grid income annualised < 15% before fees for 60 consecutive calendar days while active: the oscillation amplitude is insufficient to cover spread costs; widen grid spacing
  - OI-build signal fires but no breakout occurs within 48h for 5+ consecutive signals: the OI-build is not predicting breakouts; recalibrate or disable the OI pause

related: ["[[regime-gated-grid]]", "[[funding-skewed-grid]]", "[[grid-trading]]", "[[oi-confirmed-trend]]", "[[oi-flush-reversion]]", "[[leverage-stress-tail-hedge]]", "[[open-interest]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[market-microstructure]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# OI-Aware Grid

OI-aware grid is a **grid trading strategy that pauses or de-sizes when open interest is building rapidly**, and resumes at full size when OI stabilises back into the range-bound regime. A standard grid earns from oscillation; its failure mode is a breakout run — a strong directional move that accumulates inventory on one side and produces large losses. Rapid OI accumulation is a **leading indicator** of that breakout risk: new leverage is entering the market, signalling that directional participants are positioning for a large move before the vol regime has flipped and before ADX has risen. By acting on OI build-rate rather than on realized vol or trend indicators, the grid can exit or de-size before the breakout occurs rather than after.

**This is explicitly differentiated from [[regime-gated-grid]]** — that page pauses the grid when a volatility-regime indicator (ADX, Bollinger bandwidth, ATR) signals a range-to-trend flip. Vol-regime indicators are **lagging**: they measure volatility after it has already manifested in price. The OI-build signal is **leading**: OI accumulates as fresh directional leverage enters the market, typically 4–24 hours before the breakout fires and vol indicators register the regime change. The two gates are complementary; this page adds the earlier-acting gate on top of or instead of the lagging vol-regime gate.

**This is differentiated from [[funding-skewed-grid]]** — that page biases the grid's inventory allocation toward the funding-receiver side to earn both spread and carry simultaneously. It does not address the breakout-survival problem. This page makes no inventory bias; it focuses entirely on the pause/resume decision based on OI build-rate.

**This is differentiated from [[oi-confirmed-trend]]** — that page uses OI confirmation as a filter for entering trend/momentum positions (OI rising + price rising = fresh longs confirming trend strength). This page uses OI build-rate as a signal to EXIT (pause) the grid before a breakout — the same OI-rise signal, but as a defensive trigger for a range-bound strategy rather than an entry trigger for a trend strategy.

## Edge source

Per [[edge-taxonomy]], **structural + risk-bearing**:

- **Structural (primary)** — OI build-rate is a structural leading indicator of breakout risk. When OI grows faster than the typical oscillation-regime rate, directional participants are adding leverage to trade a perceived breakout. The grid is exposed to this risk structurally: grids accumulate inventory against the breakout direction. Acting on the OI signal before the breakout fires prevents the grid from being fully loaded with one-sided inventory at the worst possible moment.
- **Risk-bearing** — the grid earns income by bearing the risk of price oscillation — market-makers' spread. The OI gate narrows the set of regimes in which that risk-bearing is compensated (range-bound) vs uncompensated (breakout). By concentrating the risk-bearing in the compensated regime and pausing during uncompensated regimes, the strategy improves the Sharpe of the grid component.

## Why this edge exists

**Three mechanisms make OI build-rate a better grid-pause signal than lagging vol indicators:**

1. **OI builds before the breakout, vol indicators fire after.** When a large directional participant (fund, whale, algo) decides to buy a breakout, they begin accumulating a perp position over hours or days before the actual price move occurs. This position-building registers as OI growth before spot price moves. A vol-regime indicator (ADX, Bollinger squeeze) registers the regime change only after the breakout has compressed a candle range or made a new high. The OI signal typically fires 4–24 hours earlier, allowing the grid to exit before the full inventory accumulation on the losing side.

2. **OI growth rate distinguishes oscillation from accumulation.** In a healthy range-bound regime, OI oscillates with the price: longs enter at lows, shorts enter at highs, and OI stays flat on a rolling 24-hour basis. When OI consistently grows independent of short-term price oscillation, the market is not oscillating — it is building a directional book. The growth *rate* (not level) is the signal; absolute OI level is less informative than the rate of change.

3. **The grid pause cost is low.** Pausing a grid for 24–48 hours costs the opportunity cost of missed oscillation income. In most qualifying breakout preconditions, the grid would have lost multiple grid spacings to the directional move anyway. The pause reduces income marginally while avoiding a large inventory accumulation loss. The asymmetry favours pausing liberally.

**Who is on the other side:** directional momentum traders, trend-following algorithms, and informed breakout participants who are building the OI that preconditions the move. The grid's normal counterparty is the oscillating crowd; the pause shifts the grid to avoid the directional crowd.

## Null hypothesis

Under the null, OI build-rate carries **no incremental predictive power** for grid breakout events beyond what a vol-regime indicator (ADX, Bollinger bandwidth) already captures:
- Grids paused on OI build-rate should not produce higher net income than grids paused on vol-regime flip alone.
- OI build-rate should not predict imminent breakouts (price move ≥ 2× grid spacing within 24h) with higher accuracy than a baseline ATR-expansion measure.
- The grid income lost during OI-build pauses should not be recovered by avoiding breakout losses at a ratio > 1:1.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical grid-killing breakout events in BTC/ETH perps; check whether a ≥ 5% OI 12h growth rate signal preceded each breakout by 4–24 hours and was absent in the prior range-bound period. Predict: OI build-rate fires with a 6–18 hour median lead time before breakouts and has a false-positive rate of ≤ 30% (only 30% of OI-build signals produce no breakout).

## Rules

### Grid activation gate (grid runs when ALL conditions pass)

**Condition 1: OI is NOT building rapidly**
- 12-hour rolling OI change is < **+5%** (OI growing less than 5% in the most recent 12 hours).
- 24-hour rolling OI change is < **+8%**.
- Source: `GET /api/v1/derivatives/open-interest?coin=BTC`.
- *Rationale:* sustained OI growth above these thresholds signals directional accumulation, not oscillation-regime noise.

**Condition 2: Funding is not extreme in either direction**
- 8h funding rate is between **−0.03%** and **+0.05%** (not in a funding-flush or hyper-crowded regime).
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
- *Rationale:* funding extremes signal regime instability — either a deleveraging flush (negative) or an overcrowded breakout setup (very positive). Both regimes are hostile to grids.

**Condition 3: Realized volatility in range-bound territory**
- ATR(14) on 1h candles is ≤ **1.2%** of spot (price oscillation is within the grid's design range).
- ADX(14) on 4h candles is ≤ **25** (confirmed absence of a strong trend).
- Source: computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=50` and `interval=4h&limit=30`.

### Grid pause trigger (any condition triggers a pause)

**Pause Trigger A: Rapid OI build**
- 12h OI change ≥ **+5%** (rapid OI accumulation signalling directional entry).
- OR 24h OI change ≥ **+8%** (sustained OI build over a full day).

**Pause Trigger B: Extreme funding**
- 8h funding ≥ **+0.06%** (hyper-crowded long regime — breakout fuel high).
- OR 8h funding ≤ **−0.03%** (funding flush — cascade risk elevated).

**Pause Trigger C: Vol regime flip**
- ATR(14, 1h) rises above **1.5%** of spot (oscillation amplitude exceeding grid design).
- OR ADX(14, 4h) rises above **30** (confirmed trend forming).

### Grid resume conditions (all must pass for resume)

After a pause, the grid resumes when:
1. 12h OI change is below +3% for **6 consecutive hours** (OI has stabilised).
2. Funding is back within [−0.02%, +0.04%].
3. ATR(14, 1h) ≤ 1.1% and ADX ≤ 25 for the most recent 4h candle.
- *Minimum pause duration:* 12 hours (never resume immediately after a pause trigger; allow the directional move to complete).

### Grid parameters (default)

- **Grid range:** ±3–5% from current mid-price (set at activation; widen slightly if vol has recently been elevated).
- **Grid spacing:** 0.4–0.6% between levels (set to capture the typical oscillation in BTC/ETH range-bound regimes).
- **Inventory cap:** maximum 15% of portfolio in one-sided inventory (close the grid and exit positions if inventory exceeds this cap on either side).
- **Per-level capital:** allocate uniformly across levels; total capital-at-risk in the grid ≤ 20% of portfolio.

## Implementation pseudocode

```python
# oi_aware_grid.py

from dataclasses import dataclass
from typing import Optional
from enum import Enum

class GridState(Enum):
    INACTIVE = "INACTIVE"
    RUNNING  = "RUNNING"
    PAUSED   = "PAUSED"

# ---- activation thresholds ----
OI_12H_CHANGE_RUN_MAX    = 0.05    # 12h OI change < +5%  to run
OI_24H_CHANGE_RUN_MAX    = 0.08    # 24h OI change < +8%  to run
FUNDING_RUN_MIN          = -0.0003 # funding > -0.03%/8h to run
FUNDING_RUN_MAX          = +0.0005 # funding < +0.05%/8h to run
ATR_RUN_MAX_PCT          = 0.012   # ATR(14,1h) <= 1.2% of spot
ADX_RUN_MAX              = 25.0    # ADX(14,4h) <= 25

# ---- pause thresholds ----
OI_12H_PAUSE_MIN         = 0.05    # 12h OI >= +5% → pause
OI_24H_PAUSE_MIN         = 0.08    # 24h OI >= +8% → pause
FUNDING_PAUSE_HIGH       = +0.0006 # funding >= +0.06%/8h → pause
FUNDING_PAUSE_LOW        = -0.0003 # funding <= -0.03%/8h → pause
ATR_PAUSE_MIN_PCT        = 0.015   # ATR >= 1.5% → pause
ADX_PAUSE_MIN            = 30.0    # ADX >= 30 → pause

# ---- resume thresholds ----
OI_12H_RESUME_MAX        = 0.03    # 12h OI < +3% for 6h
RESUME_STABLE_HOURS      = 6
MIN_PAUSE_DURATION_HOURS = 12

@dataclass
class MarketSnapshot:
    spot_price:        float
    oi_12h_change:     float   # fractional (0.05 = +5%)
    oi_24h_change:     float
    funding_8h:        float   # fractional per 8h (-0.0003 = -0.03%)
    atr_1h_pct:        float   # ATR(14) / spot price (0.012 = 1.2%)
    adx_4h:            float   # ADX(14) on 4h

@dataclass
class GridBook:
    state:             GridState
    pause_trigger:     Optional[str]
    hours_paused:      int
    oi_stable_hours:   int      # consecutive hours OI < resume threshold

def should_pause(s: MarketSnapshot, current_state: GridState) -> tuple[bool, str]:
    if current_state != GridState.RUNNING:
        return False, ""
    if s.oi_12h_change >= OI_12H_PAUSE_MIN:
        return True, f"OI 12h build +{s.oi_12h_change:.1%} >= threshold {OI_12H_PAUSE_MIN:.0%}"
    if s.oi_24h_change >= OI_24H_PAUSE_MIN:
        return True, f"OI 24h build +{s.oi_24h_change:.1%} >= threshold {OI_24H_PAUSE_MIN:.0%}"
    if s.funding_8h >= FUNDING_PAUSE_HIGH:
        return True, f"funding {s.funding_8h:.4%}/8h >= pause threshold {FUNDING_PAUSE_HIGH:.4%}"
    if s.funding_8h <= FUNDING_PAUSE_LOW:
        return True, f"funding {s.funding_8h:.4%}/8h <= flush threshold {FUNDING_PAUSE_LOW:.4%}"
    if s.atr_1h_pct >= ATR_PAUSE_MIN_PCT:
        return True, f"ATR(1h) {s.atr_1h_pct:.2%} >= breakout threshold {ATR_PAUSE_MIN_PCT:.2%}"
    if s.adx_4h >= ADX_PAUSE_MIN:
        return True, f"ADX(4h) {s.adx_4h:.1f} >= trend threshold {ADX_PAUSE_MIN}"
    return False, ""

def can_activate(s: MarketSnapshot) -> tuple[bool, list[str]]:
    fails = []
    if s.oi_12h_change >= OI_12H_CHANGE_RUN_MAX:
        fails.append(f"OI 12h build +{s.oi_12h_change:.1%} — OI accumulating, wait")
    if s.oi_24h_change >= OI_24H_CHANGE_RUN_MAX:
        fails.append(f"OI 24h build +{s.oi_24h_change:.1%} — sustained accumulation, wait")
    if not (FUNDING_RUN_MIN <= s.funding_8h <= FUNDING_RUN_MAX):
        fails.append(f"funding {s.funding_8h:.4%}/8h outside run range [{FUNDING_RUN_MIN:.4%}, {FUNDING_RUN_MAX:.4%}]")
    if s.atr_1h_pct > ATR_RUN_MAX_PCT:
        fails.append(f"ATR(1h) {s.atr_1h_pct:.2%} > {ATR_RUN_MAX_PCT:.2%} — too volatile for grid")
    if s.adx_4h > ADX_RUN_MAX:
        fails.append(f"ADX(4h) {s.adx_4h:.1f} > {ADX_RUN_MAX} — trend detected, grid inactive")
    return len(fails) == 0, fails

def step(book: GridBook, s: MarketSnapshot) -> dict:
    """One decision step called each hour."""
    if book.state == GridState.RUNNING:
        pause, reason = should_pause(s, book.state)
        if pause:
            return {"action": "PAUSE", "reason": reason,
                    "note": "close all open grid orders; hold existing inventory; wait min 12h"}
        return {"action": "CONTINUE", "note": "all grid-run conditions active; grid operating normally"}

    if book.state == GridState.PAUSED:
        if book.hours_paused < MIN_PAUSE_DURATION_HOURS:
            return {"action": "HOLD_PAUSE",
                    "note": f"min pause duration not reached: {book.hours_paused}h/{MIN_PAUSE_DURATION_HOURS}h"}
        # Check resume conditions
        oi_stable = s.oi_12h_change < OI_12H_RESUME_MAX
        book.oi_stable_hours = book.oi_stable_hours + 1 if oi_stable else 0
        ok, fails = can_activate(s)
        if ok and book.oi_stable_hours >= RESUME_STABLE_HOURS:
            return {"action": "RESUME",
                    "note": f"all resume conditions met; OI stable {book.oi_stable_hours}h; reactivate grid"}
        return {"action": "HOLD_PAUSE",
                "note": f"resume blocked: OI stable hours={book.oi_stable_hours}/{RESUME_STABLE_HOURS}; {'; '.join(fails)}"}

    # INACTIVE: check for activation
    ok, fails = can_activate(s)
    if ok:
        return {"action": "ACTIVATE", "note": "all activation conditions met; deploy grid"}
    return {"action": "WAIT", "note": "; ".join(fails)}
```

The production system adds: a real-time OI monitor on a 15-minute polling cycle (OI can build rapidly); an automatic order-cancellation trigger when the pause fires; a daily inventory-reset check to flatten one-sided grid accumulation before it reaches the 15% cap; and a P&L attribution split between grid-spread income and OI-pause opportunity cost to evaluate the gate's net contribution.

## Indicators / data used

- **Open interest (12h and 24h change rate)** — `GET /api/v1/derivatives/open-interest?coin=BTC`; the primary gate signal. 12h and 24h rolling change rates are the pause/resume threshold. Both the cross-exchange endpoint and `GET /api/v1/derivatives/binance/open-interest` (Binance-specific with 30d trend) are useful.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; auxiliary gate for funding extremes (secondary pause trigger, and confirms OI-build direction).
- **1h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=50`; compute ATR(14) on 1h candles for vol-regime gate.
- **4h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=30`; compute ADX(14) on 4h candles for trend-regime gate.
- **Regime** — `GET /api/v1/regimes/current`; if `Trending_Momentum` or `Structural_Shock`, override to forced pause regardless of OI reading.
- **Liquidations** — `GET /api/v1/market-intelligence/liquidations?coin=BTC`; spike in liquidation volume confirms that a pause was warranted (directional move accompanied by forced exits); use retrospectively for gate calibration.

## Example trade

**Setup (illustrative — OI-build pause prevents grid run-over):**

- BTC is trading at $72,000 in a range $70,500–$73,500 (4.3% band). Grid is active: 10 levels at 0.5% spacing, ±2.5% from mid.
- Day 1–3: OI oscillates between $20.0B and $20.8B. 12h OI change < 2%. Grid earns normally; 6 fills at $360 net income (0.5% × $72,000 × 0.1 BTC per level × 6 fills, approximate).
- **Day 4, 08:00:** OI jumps from $20.8B to $22.1B in 12 hours (+6.3%, above 5% pause threshold).

**OI-build pause fires:**
- Grid is paused immediately. All open limit orders are cancelled. Current inventory: flat (no accumulated one-sided position at the time of pause).
- Hours paused: the grid waits.

**Day 4, 14:00:** BTC breaks above $73,500 and runs to $77,000 (+5.6% in 6 hours). Without the pause, the grid would have accumulated short inventory at each level from $73,500 upward — approximately 8 short contracts at average $74,000 × 0.1 BTC/level = $59,200 notional short at $77,000 close = **−$2,366 loss**.

**With the pause:** zero inventory. The breakout runs without the grid. Grid income foregone during the 18-hour pause: approximately $120 in missed fills (2 oscillations that occurred during the pause at lower levels). **Net saving: $2,366 − $120 = +$2,246** vs running the grid without the OI gate.

**Day 5, 12:00:** BTC has retraced to $75,000 and is oscillating in a new range $73,800–$76,200. OI stabilises: 12h OI change = +1.8%, stable for 6 hours. ADX = 22, ATR = 1.0%. All resume conditions pass.

**Grid resumes** at new mid $75,000 with grid range $72,750–$77,250 (±3% for the new range).

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.2 | Higher than raw grid from avoiding breakout losses; OI pause reduces loss frequency in trending regimes |
| Expected max drawdown | ~12% | Primary risk is inventory accumulation before OI signal fires; OI is leading but not instantaneous |
| Grid income (range-bound) | 30–60% annualised (estimated, pre-fee) | Subject to grid spacing, fill frequency, and funding on inventory |
| Breakeven cost budget | 12 bps | Maker fees on grid fills typically 2–4 bps; taker fees when closing during pause 5–8 bps; total ≈ 8–12 bps |
| OI pause frequency | 5–15 times per year | OI build signals qualifying at +5%/12h in BTC perps |
| Pause duration (median) | 24–72 hours | Time for OI to stabilise post-breakout or breakout to resolve |

**Cost overlay:** the dominant cost of the OI overlay is the income foregone during pauses. This opportunity cost must be offset by the breakout losses avoided. The asymmetry is favourable: a typical grid breakout loss (full inventory run-over at max size) exceeds 30 days of grid income; a typical pause costs 1–3 days of income.

## Capacity limits

- **Per pair:** BTC/ETH perp grid at $1–5M total capital per pair is well within Binance and Hyperliquid depth for the grid spacings described. Above $15M, individual limit orders at each grid level become large enough to influence the order book.
- **Aggregate:** `capacity_usd: 15000000` reflects the capacity constraint on the OTM grid levels (orders near the range boundary are in thinner book depth). The OI-pause constraint does not add an independent capacity limit.
- **Multi-pair extension:** the OI-build signal should be monitored per pair; BTC OI building does not necessarily mean ETH/SOL OI is building (though correlation is high in correlated breakouts).

## What kills this strategy

1. **Fast OI build without observable lead time (#3: Market-structure regime change).** In some breakout events, OI builds simultaneously with the price move (HFT-driven or news-driven breakouts). The OI signal fires at the same time as the breakout rather than in advance. The grid may have partially accumulated inventory before the signal fires.
2. **OI-build without a subsequent breakout (#4: Crowding).** If the OI build-rate threshold is too sensitive, many false-positive pauses occur: OI builds, the grid is paused, but no breakout follows — the market mean-reverts within the range. The grid forfeits income during false-positive pauses. The kill criterion (OI signal fires 5+ times with no breakout within 48h) covers this.
3. **Rapid breakout during grid resume (#7: Operational).** If the grid resumes before OI has fully stabilised (after minimum pause duration but while OI is still moderately elevated), a second breakout leg can catch the newly-resumed grid. The 12-hour minimum pause and 6-hour OI-stability requirement are intended to prevent this.
4. **Fees and funding compressing grid income (#2: Cost structure).** In low-oscillation periods, the grid generates fewer fills and the income may not cover funding payments on inventory. The kill criterion (grid income < 15% annualised for 60 days) covers this.

## Kill criteria

Pause on any of:

1. **Grid sleeve drawdown > 12%** from high-water mark — the grid is accumulating inventory losses faster than oscillation income is covering them; pause and review grid parameters.
2. **OI-build pause fires within 24h of grid activation in 4 of 5 consecutive activations** — the activation window is too narrow or the pause threshold is too low; recalibrate.
3. **3 consecutive grid runs end at a loss** (not at OI-pause exit) — the range-bound regime assumption is incorrect; the underlying market is trending; pause the strategy entirely.
4. **Grid income annualised < 15% for 60 consecutive days while active** — oscillation amplitude is insufficient to cover costs; widen grid spacing or switch to a pair with higher intraday oscillation.
5. **OI-build signal fires 5+ consecutive times with no breakout within 48h each time** — the OI-build-to-breakout predictive relationship has broken down; recalibrate the build-rate threshold.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Leading indicator vs lagging vol gate** — OI build-rate fires hours before a vol-regime flip; the grid can exit before the breakout rather than after, which is the key advantage over [[regime-gated-grid]].
- **Compatible with the vol-regime gate** — the two gates are complementary; running both (OI pause = leading; ADX/ATR pause = lagging confirmation) provides defence-in-depth against breakouts.
- **Low implementation complexity** — the OI rate-of-change calculation is a simple rolling percentage; no complex signal processing required. Suitable for a grid operator who already monitors funding and vol.
- **Grid income is preserved in range-bound regimes** — the OI gate is inactive the vast majority of the time; the grid earns normally and only pauses when the structural precondition for a breakout is objectively elevated.

## Disadvantages

- **Does not prevent all breakout losses** — OI can build and break out within a single 1h candle (correlated exchange flow, news event). In these cases, the 12h rolling OI signal does not fire in advance. The grid is not protected against instantaneous news-driven breakouts.
- **False-positive pauses reduce income** — every OI-build signal that precedes a failed breakout (market returns to range) costs 1–3 days of grid income. If the threshold is set too sensitively, the opportunity cost of pauses may exceed the losses avoided.
- **OI data latency on some venues** — cross-exchange OI aggregation from CryptoDataAPI has a polling latency. In production, pair with direct Binance or Hyperliquid OI WebSocket feeds for lower-latency monitoring.
- **Inventory at pause time** — when the pause triggers, the grid may already have partially accumulated inventory from the early phase of the OI build. Exiting that inventory at market creates additional cost not captured in the normal grid P&L.

## Sources

- [[grid-trading]] — the canonical grid/market-making primitive; provides the underlying spread-capture mechanism and the failure-mode taxonomy that the OI overlay addresses.
- [[regime-gated-grid]] — the lagging vol-regime gate; this page's leading OI-gate is explicitly designed as the earlier-acting complement.
- [[oi-confirmed-trend]] — OI-rise as a trend-confirmation signal; the same OI metric used here as a pause trigger for range strategies is a confirmation signal for trend strategies.
- [[oi-flush-reversion]] — OI decline as a mean-reversion entry signal; the inverse of the OI-build-rate pause trigger.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/open-interest?coin=BTC` — primary gate: 12h and 24h OI change rate; cross-exchange view (Binance + Hyperliquid)
- `GET /api/v1/derivatives/binance/open-interest` — Binance-specific OI with 30-day trend; useful for distinguishing Binance-driven vs Hyperliquid-driven OI build
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — auxiliary pause gate (funding extremes); also confirms OI-build direction
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=50` — compute ATR(14, 1h) for vol-regime gate
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=30` — compute ADX(14, 4h) for trend-regime gate
- `GET /api/v1/market-intelligence/liquidations?coin=BTC` — post-hoc confirmation that OI build preceded a breakout cascade
- `GET /api/v1/regimes/current` — regime override: forced pause if `Trending_Momentum` or `Structural_Shock`

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=90` — daily OI and funding history for OI-build-rate threshold calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500` — extended 1h kline history for ATR and ADX calibration across multiple range-to-trend regime transitions

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-market-intelligence]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this grid end-to-end:

- **Gate** — `GET /api/v1/derivatives/open-interest?coin=BTC` (12h/24h OI change rate) is the pause trigger; `GET /api/v1/derivatives/binance/open-interest` separates Binance-driven from Hyperliquid-driven builds
- **Signal** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=50` (ATR) and `interval=4h&limit=30` (ADX) keep the vol/trend gates current between grid re-centres
- **Regime gate** — `GET /api/v1/regimes/current` forces a full pause in trending or shock regimes; `GET /api/v1/derivatives/funding-rates?coin=BTC` adds the funding-extreme pause
- **Backtest** — simulate grid fills on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h back to 2017-08); the OI leg is shallower — `/derivatives/binance/history` covers ~90 days over REST and the Binance daily archive in `GET /api/v1/backtesting/funding` (which includes OI) starts 2026-03-30, so calibrate OI thresholds on rolling recent windows, not multi-year fits
- **Tips** — append `?format=markdown` on summary reads for cleaner agent context; respect `Cache-Control` headers rather than re-polling OI every minute
- **Prompt library** — the "Open Interest Divergence Scanner" prompt (Free tier, [prompt library](https://cryptodataapi.com/prompts)) supplies the OI-quadrant read that arms or disarms this grid

## Related

- [[regime-gated-grid]] — the lagging vol-regime gate for the same grid primitive; this page is the leading OI-gate complement
- [[funding-skewed-grid]] — funding-receiver inventory bias for the same grid primitive; orthogonal to this page (no conflict; can run together)
- [[grid-trading]] — the canonical grid/market-making primitive
- [[oi-confirmed-trend]] — OI-rise as a trend-entry signal; the same OI metric as a different gate direction
- [[oi-flush-reversion]] — OI decline as a mean-reversion entry; the inverse OI signal
- [[leverage-stress-tail-hedge]] — accumulates puts when OI/market-cap is elevated; adjacent use of the OI signal for a different strategy
- [[open-interest]] — the OI metric and its interpretation
- [[funding-rate]] — the secondary pause gate
- [[perpetual-futures]] — the perp market where the grid operates
- [[market-microstructure]] — grid strategies and their structural assumptions
- [[edge-taxonomy]] — structural + risk-bearing classification
- [[failure-modes]] — fast OI build, false-positive pauses, inventory at pause time
- [[when-to-retire-a-strategy]] — kill vs pause framework
