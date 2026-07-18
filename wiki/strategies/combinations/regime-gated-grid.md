---
title: "Regime-Gated Grid"
type: strategy
created: 2026-07-18
updated: 2026-07-18
status: good
tags: [combinations, meta-strategy, mean-reversion, grid-trading, regime-detection, market-microstructure, quantitative, crypto]
aliases: ["Regime-Filtered Grid", "Volatility-Gated Grid Bot", "Range-Regime Grid"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [structural, risk-bearing]
edge_mechanism: "In confirmed low-volatility, range-bound regimes the grid mechanically harvests bid-ask spread and oscillation; the regime gate removes the known catastrophic failure mode of inventory accumulation in trending markets by killing the grid at the first sign of a regime flip, leaving only the regime where the structural spread-capture edge actually works."

data_required: [ohlcv-1h, ohlcv-4h, adx-14, bollinger-bands-20, atr-14, funding-rates, volatility-regime]
min_capital_usd: 2000
capacity_usd: 10000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.15
breakeven_cost_bps: 10

decay_evidence: "Grid strategies on consumer bot platforms (3Commas, Pionex) have proliferated since 2020, compressing the edge in common pairs at common spacings. The regime gate partially counteracts this: it selects the least-crowded subset of regimes (confirmed range) and avoids the high-noise, high-bot-competition choppy markets where consumer grids are most active."

kill_criteria: |
  - strategy drawdown > 15% from high-water mark
  - regime gate is never satisfied for 60+ consecutive days (no viable range periods found)
  - average realized grid revenue per cycle < taker fee cost (all fills are taker, no maker fills) for 20 consecutive cycles
  - rolling 3-month Sharpe < 0 on minimum 50 completed grid cycles

related: ["[[grid-trading]]", "[[regime-adaptive-strategy]]", "[[regime-detection]]", "[[volatility-targeting]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[range-trading]]", "[[market-making]]", "[[adx]]", "[[bollinger-bands]]", "[[atr]]", "[[adverse-selection]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Regime-Gated Grid

A regime-gated grid is [[grid-trading]] with an **explicit regime classification layer** that activates the grid only in confirmed low-volatility, range-bound periods and issues a hard kill order the moment the regime flips to trend or high-volatility. The primitive edge is the grid's spread-capture and oscillation-harvest in range regimes; the overlay solves the grid's well-documented catastrophic failure mode — uncontrolled inventory accumulation in trending markets — by treating the regime signal as a *binary on/off switch*, not merely a positioning hint.

This is differentiated from [[grid-trading]] (the underlying primitive, which includes an ADX filter as a risk control), [[regime-adaptive-strategy]] (which swaps between multiple strategies based on regime), and [[volatility-targeting]] (which scales position size by volatility). The specific contribution of this page is the **architecture**: the regime gate is the first-order decision; the grid is only ever deployed inside a confirmed non-trending regime, and it is shut down before a breakout rather than caught by one.

## Edge source

Per [[edge-taxonomy]], **structural + risk-bearing**:

- **Structural** — in a confirmed range regime, the grid mechanically earns the bid-ask spread on every completed buy-then-sell cycle. This is the same flow as market-making in a constrained price band: passive liquidity earns the spread from price-insensitive takers. Regime confirmation selects for the periods where this spread is reliable and the flow is approximately balanced (as many buyers as sellers near the reference price).
- **Risk-bearing** — the grid operator absorbs two-sided inventory risk. In genuine range regimes this is a manageable warehouse risk for which the spread compensates. The regime gate makes the explicit judgment that the risk being borne (oscillation risk within the range) is well-priced by the grid spacing, and that the risk NOT being borne (breakout/trend risk) is where inventory quickly becomes a losing bet.

The strategy has no informational or analytical edge. The regime classification must be fast and accurate; everything else is mechanical.

## Why this edge exists

**The combination solves the grid's only structural failure mode.** An unfiltered grid in a trending market accumulates a losing one-sided inventory faster than the spread income from partial fills can cover. This is not a modeling problem — it is a mechanical consequence of the grid's symmetric quoting structure in an asymmetric flow environment. Every successful grid operator knows this; the only question is *how* to detect the transition.

The regime gate approach adds value over a simple ATR stop or drawdown kill for three reasons:

1. **Pre-emptive vs reactive.** A drawdown-based kill acts *after* the grid has already been damaged by a trend. A volatility-regime gate that monitors ADX, Bollinger Bandwidth, and HMM regime probabilities can signal an incipient trend before a grid level has been breached.
2. **No false re-entries.** A drawdown kill restarts the grid after the loss; if the trend continues, the restarted grid accumulates more losses. A regime gate keeps the grid off until the range regime is affirmatively re-confirmed.
3. **Selectivity increases return quality.** By running only in confirmed range regimes, the grid's realized win rate per cycle is higher — the oscillation that generates buy-then-sell cycles is more reliable in range than in chop.

**Who is on the other side:** taker-flow participants — retail momentum, spot rebalancers, liquidation flow, and other algos — who value immediacy more than the small price improvement from waiting. They lose the grid spacing in aggregate; the grid earns it.

## Null hypothesis

Under the null, the regime gate provides no incremental value: the average P&L per grid cycle is the same whether the gate fires or not. Specifically, grid cycles in confirmed range regimes should not have materially higher completion rates, lower inventory accumulation, or higher spread-per-cycle revenue than grid cycles entered on a random regime label. The null is directly testable by comparing grid performance conditioned on regime classification vs random activation on the same underlying. It is untested in this wiki.

## Rules

### Regime activation gate (grid ON only when ALL met)

1. **ADX(14) < 20** on the 4h chart — low directional momentum (adapted from [[grid-trading]]'s validated ADX filter).
2. **Bollinger Bandwidth** (20-period, 2-std) is in the **bottom 30th percentile** of its trailing 90-day history — volatility is compressed, consistent with range.
3. **Volatility regime** from `/api/v1/volatility/regime` is `compressed` or `mean_reverting` — not `expanding`, `vol_shock`, or `normal` trending up.
4. **HMM regime** from `/api/v1/quant/market`: probability of `range_low_vol` state > **40%** (the HMM is not strongly pricing a trend state).
5. **No active event risk**: `/api/v1/event/regime/score` < 50 (no major unlock, macro print, or catalyst within 48h that could catalyse a breakout).

### Grid construction

1. **Channel definition.** Define the current range: high and low of the trailing **48-hour** period on the 4h chart. Add 1% buffer on each side.
2. **Grid spacing.** Set grid levels at **0.5% intervals** within the channel. This is the minimum spacing; widen to 1.0% on assets with taker fees > 0.04% to stay above the breakeven cost.
3. **Number of levels.** Deploy N = (channel_width% / grid_spacing%) levels, maximum **12** per side (24 total). Maximum deployed notional = 25% of sleeve per asset.
4. **Order type.** Prefer limit orders (maker). On venues without reliable maker fills at grid levels (high-latency), accept taker up to 0.05% fee.

### Grid kill conditions (immediate close-all or cancel-all on ANY trigger)

1. **ADX(14) breaches 25** — directional momentum is building; kill immediately, do not wait for a level to be hit.
2. **Price breaks 1.5x ATR(14) from the channel midpoint** in a single 4h bar close — breakout in progress.
3. **Volatility regime flips to `expanding` or `vol_shock`** from the API — pre-emptive shutdown before the trend fully develops.
4. **Event risk score ≥ 70** — imminent catalyst that could invalidate the range.
5. **Funding spikes > 0.06%/8h** (>65% APY) — a strong directional crowd is entering; regime is likely flipping.
6. **Drawdown on the grid position > 8%** — emergency stop; inventory has accumulated beyond the spread-income recovery horizon.

### Post-kill re-entry gate

After a kill, the grid must remain **off** for a minimum of **24 hours**. Re-entry requires the full activation gate to be met again (all 5 conditions). This prevents premature re-entry during a whipsaw where ADX drops briefly before resuming the trend.

### Position sizing

- Total deployed notional per grid = max 25% of sleeve.
- Per-level order size = total notional / (number of active levels / 2).
- Maintain a 30% cash reserve within the grid sleeve for margin calls and emergency exits.

## Implementation pseudocode

```python
# regime_gated_grid.py — grid activation and kill controller
from dataclasses import dataclass
from typing import Optional

# ---- activation thresholds ----
ADX_MAX_ON     = 20.0    # ADX to allow grid on
ADX_KILL       = 25.0    # ADX to kill immediately
BB_WIDTH_PCT   = 30      # Bollinger Bandwidth percentile ceiling to allow on
VOL_REGIME_OK  = {"compressed", "mean_reverting"}
HMM_RANGE_PROB = 0.40    # minimum prob of range_low_vol state
EVENT_SCORE_OK = 50      # max event risk score
EVENT_SCORE_KILL = 70

BREAKOUT_ATR_MULT = 1.5  # price move to trigger kill
FUNDING_SPIKE     = 0.0006  # 0.06%/8h funding spike kill
GRID_DRAWDOWN_KILL = 0.08

GRID_SPACING_PCT  = 0.005   # 0.5% grid levels
MAX_LEVELS_EACH   = 12
MAX_NOTIONAL_PCT  = 0.25
CASH_RESERVE_PCT  = 0.30

@dataclass
class RegimeSnapshot:
    adx_14: float
    bb_width_percentile: float   # 0-100
    vol_regime: str
    hmm_range_low_vol_prob: float
    event_risk_score: float
    price: float
    atr_14: float
    funding_8h: float
    channel_mid: float

def gate_open(r: RegimeSnapshot) -> bool:
    return (r.adx_14 < ADX_MAX_ON
            and r.bb_width_percentile < BB_WIDTH_PCT
            and r.vol_regime in VOL_REGIME_OK
            and r.hmm_range_low_vol_prob > HMM_RANGE_PROB
            and r.event_risk_score < EVENT_SCORE_OK)

def kill_triggered(r: RegimeSnapshot, grid_drawdown: float) -> Optional[str]:
    if r.adx_14 >= ADX_KILL:
        return f"ADX {r.adx_14:.1f} >= {ADX_KILL}"
    if abs(r.price - r.channel_mid) > BREAKOUT_ATR_MULT * r.atr_14:
        return f"price breakout {abs(r.price - r.channel_mid):.2f} > {BREAKOUT_ATR_MULT}×ATR"
    if r.vol_regime in {"expanding", "vol_shock"}:
        return f"vol regime flipped to {r.vol_regime}"
    if r.event_risk_score >= EVENT_SCORE_KILL:
        return f"event risk {r.event_risk_score} >= {EVENT_SCORE_KILL}"
    if r.funding_8h > FUNDING_SPIKE:
        return f"funding spike {r.funding_8h*100:.4f}%/8h"
    if grid_drawdown > GRID_DRAWDOWN_KILL:
        return f"grid drawdown {grid_drawdown:.1%} > {GRID_DRAWDOWN_KILL:.1%}"
    return None

def manage_grid(r: RegimeSnapshot, grid_state: dict, book: dict) -> dict:
    kill_reason = kill_triggered(r, grid_state.get("drawdown", 0.0))
    if kill_reason:
        return {"action": "KILL_GRID", "reason": kill_reason,
                "reentry_lockout_hours": 24}

    if grid_state.get("active"):
        return {"action": "HOLD_GRID"}

    # Grid is OFF — check if we can activate
    if grid_state.get("lockout_remaining_hours", 0) > 0:
        return {"action": "WAIT", "reason": "post-kill lockout"}

    if gate_open(r):
        channel_h = r.channel_mid * (1 + 0.01)
        channel_l = r.channel_mid * (1 - 0.01)
        n_levels = min(int((channel_h - channel_l) / r.price / GRID_SPACING_PCT), MAX_LEVELS_EACH)
        total_notional = MAX_NOTIONAL_PCT * book["sleeve_capital"] * (1 - CASH_RESERVE_PCT)
        level_size = total_notional / n_levels
        return {
            "action": "ACTIVATE_GRID",
            "channel": [channel_l, channel_h],
            "grid_levels": n_levels * 2,
            "level_notional": level_size,
            "spacing_pct": GRID_SPACING_PCT,
        }
    return {"action": "WAIT", "reason": "regime gate not open"}
```

The production system adds: WebSocket price feed for real-time ADX/ATR updates; CryptoDataAPI polling at 15-min intervals for vol-regime and HMM state; limit-order management (cancel/replace at each level); gas-aware execution on DEX venues.

## Indicators / data used

- **ADX(14) on 4h** — directional strength gate and kill trigger
- **Bollinger Bandwidth (20, 2σ)** — range-compression confirmation
- **ATR(14) on 4h** — breakout detection for kill trigger
- **Volatility regime** (`/api/v1/volatility/regime`) — API-sourced vol-state label
- **HMM regime probabilities** (`/api/v1/quant/market`) — probabilistic regime classification
- **Event risk score** (`/api/v1/event/regime/score`) — catalyst calendar risk
- **Funding rate (8h)** (`/api/v1/derivatives/funding-rates`) — crowding/trend signal for kill

## Example trade

**Setup (illustrative):**

- Asset: ETH-PERP on Hyperliquid, 4h chart.
- ADX(14) = 14 (below 20 gate). Bollinger Bandwidth percentile = 18 (below 30 gate). Vol regime = `compressed`. HMM `range_low_vol` prob = 58%. Event risk = 22. Funding = +0.009%/8h. All 5 gate conditions met → **ACTIVATE**.
- Price midpoint: $3,400. Channel: $3,366–$3,434 (1% each side, 2% total). Grid spacing: 0.5% = ~$17. Levels: 2%/0.5% = 4 per side = 8 total. Sleeve capital $100,000. Deployed notional = 25% × 70% = $17,500. Level size = $17,500/8 ≈ $2,188 per level.
- Day 1: price oscillates between $3,370 and $3,425. Grid fills: 6 complete buy-sell cycles. Revenue per cycle: ~0.5% × $2,188 ≈ $10.94. Less taker (0.045% × 2 = 0.09%): $2.19. Net per cycle: ~$8.75. Day 1 gross: 6 × $8.75 = **$52.50**.
- Day 3: ETH reports macro-positive news. Price closes a 4h bar at $3,476 = $76 from mid = 0.89% = 1.45× ATR. ADX reading at next bar = 22.3 → **KILL triggered** (ADX ≥ 25 not yet, but breakout ATR ≥ 1.5× kill also not quite — the ADX kill at 22 provides a pre-emptive exit with no grid loss).
- 3-day gross revenue: ~$130. Taker fees on all fills: ~$40. Net: **~$90 on $17,500 deployed in 3 days** (~62% APY on the deployed notional, illustrative exceptional short window).

*(Illustrative only. Actual results depend on fill rates, fee structure, and regime accuracy.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Unfiltered grid Sharpe is ~0.5-0.8; regime selection expected to add ~0.3-0.5 |
| Expected max drawdown | ~15% | Dominated by the risk of a kill executing slightly late during a sharp breakout |
| Fill rate per level | 60-90% | Higher in deep-range regimes; lower in borderline regime classifications |
| Breakeven cost budget | 10 bps | Narrow; requires maker fills at key levels |
| Range regime duration | 2-10 days typical | Grid is on for short windows; inactive much of the time |
| Regime identification lag | 0-8 hours | The gap between regime flip and kill signal determines maximum inventory exposure |

**Realistic cost overlay:**
- Maker fees (Hyperliquid): ~0.02% per leg = ~4 bps round-trip per cycle.
- Taker bleed (partial taker fills): adds ~2-6 bps per cycle on average.
- Kill-event slippage: 1-5 bps to close all levels into a moving market.
- Gas (DEX venues): negligible on Hyperliquid L1.

The strategy is highly sensitive to fee tier. On venues where taker > 0.05%, the minimum grid spacing must widen to 1.0%+ to stay profitable, which reduces fill frequency.

## Capacity limits

- **Per asset on Hyperliquid**: ~$2-5M before the grid levels themselves become visible to predatory order-flow traders who can pick off the levels.
- **Cross-asset**: capacity scales with the number of eligible assets in confirmed range simultaneously (~3-5 assets at once during low-vol periods).
- **Hard ceiling**: grid strategies consume OI at each level; large grids on low-cap perps are limited by OI availability.

## What kills this strategy

1. **False regime signal (#5: The Regime Changed).** The gate fires (ADX < 20, vol compressed) but a sudden macro event (Fed announcement, a large liquidation cascade) creates a gap that the 4h ADX has not yet registered. The grid accumulates inventory on the wrong side before the kill triggers.
2. **Consumer-bot crowding (#4).** In popular pairs, thousands of retail grid bots operate at similar spacings. Their collective presence can make the "range" temporarily stable (they all absorb oscillations) but also means the edge per cycle is compressed and any single breakout wipes all of them simultaneously.
3. **Regime classifier latency (#7: Operational).** If the API polling cadence is 15 minutes but the vol regime flips in a 5-minute candle, there is a 10-minute gap where the grid is running in an invalid regime.
4. **Funding drain in low-vol regimes.** Positive funding in a low-vol range (not uncommon during accumulation periods) adds a steady carry cost to any long-side grid fills that are not immediately completed. The funding kill at 0.06%/8h limits this but does not eliminate it.
5. **Fee compression.** As Hyperliquid and other perp DEXes cut maker fees toward zero, the spread-capture logic becomes thinner and the strategy's margin of safety shrinks.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 15%** in any rolling 14-day window.
2. **Regime gate never satisfied** for 60+ consecutive days — persistent trending or high-vol environment.
3. **Average grid revenue per cycle < all-in taker cost** for 20 consecutive cycles — the edge has compressed to zero.
4. **Rolling 3-month Sharpe < 0** on minimum 50 completed grid cycles.

Re-deploy when gate conditions re-satisfy, drawdown has recovered, and per-cycle net revenue is positive on a forward-looking paper-trade for 5 consecutive days. See [[when-to-retire-a-strategy]].

## Advantages

- **Converts the grid's worst failure mode into an off-switch**: regime detection replaces the painful "emergency drawdown kill after the fact" with a pre-emptive shutdown before most of the damage occurs.
- **Predictable, short-duration risk windows**: the grid is only active during confirmed low-vol periods, so the operator can monitor it intensively for short windows rather than running it unattended.
- **Structurally transparent**: both layers (regime classification and grid mechanics) are observable in real time — no hidden state or model opaqueness.
- **Maker-fee efficient**: a patience-maximizing grid that only operates in range regimes earns most of its revenue from maker fills, minimising taker drag.

## Disadvantages

- **Low duty cycle**: the regime gate may be satisfied only 20-40% of calendar time, leaving significant capital sitting idle.
- **Gap risk at kill**: if price gaps on news while the grid is active, the kill executes into a moving market, producing the worst possible fills.
- **Regime false positives**: ADX and Bollinger Bandwidth are lagging indicators; regime flips are detected with a lag of 0-8 hours during which the grid runs in an invalid environment.
- **Consumer-bot competition**: in popular pairs on popular venues, grid spacings are crowded by retail bots who push the competitive edge toward zero even in range regimes.
- **Complexity trade-off**: the combination adds an API dependency (regime endpoints), a lockout logic, and multiple kill conditions that a simple single-strategy grid does not have. Each added component is a potential failure point.

## Sources

- Avellaneda, M. and Stoikov, S. (2008), *High-frequency trading in a limit order book*, Quantitative Finance. The theoretical basis for market-making spread capture as a function of inventory risk and volatility.
- Garman, M.B. (1976), *Market microstructure*, Journal of Financial Economics 3(3). The original dealer-spread model; grid trading is the discretized implementation.
- [[grid-trading]] — the underlying primitive, including the ADX-filtered variant deployed in this wiki.
- [[regime-adaptive-strategy]] — the broader meta-strategy framework from which this borrows the regime-gate concept.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (`compressed`, `expanding`, `vol_shock`, `mean_reverting`, `normal`) — primary grid activation gate
- `GET /api/v1/quant/market` — HMM 6-regime probabilities including `range_low_vol` — secondary gate
- `GET /api/v1/event/regime/score` — event risk composite 0-100 — pre-kill catalyst check
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — funding rate — grid kill trigger at spike
- `GET /api/v1/liquidity/depth` — per-coin order-book depth — confirms adequate liquidity to run maker grid

**Historical data:**
- `GET /api/v1/quant/history` — point-in-time HMM probabilities for backtest (Pro Plus tier)
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=200` — OHLCV for ADX/ATR/BB computation

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-derivatives]].

## Related

- [[grid-trading]] — the underlying primitive; this page is the regime-gate extension
- [[regime-adaptive-strategy]] — the broader regime-switching framework
- [[regime-detection]] — how regime classification works
- [[volatility-targeting]] — complementary vol-scaling overlay
- [[mean-reversion]] — the theoretical basis for range-bound oscillation capture
- [[bollinger-band-reversion]] — a signal-based cousin of range trading
- [[range-trading]] — the discretionary equivalent
- [[market-making]] — the microstructure theory underpinning grid spread capture
- [[adx]] — the directional strength indicator used in the gate
- [[atr]] — the volatility measure used in the breakout kill trigger
- [[adverse-selection]] — what happens to grid inventory when informed flow arrives
- [[edge-taxonomy]] — structural + risk-bearing classification
- [[failure-modes]] — regime-change and crowding risk
- [[when-to-retire-a-strategy]] — kill vs pause framework
