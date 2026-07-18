---
title: "Funding-Skewed Grid"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, grid-trading, funding-rate, market-microstructure, perpetual-futures, quantitative, crypto, hyperliquid]
aliases: ["Carry-Skewed Grid", "Funding-Receiver Grid", "Inventory-Biased Grid"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, risk-bearing]
edge_mechanism: "A symmetric grid on perpetuals earns spread capture but carries no funding direction; by skewing the inventory allocation toward the funding-receiver side (more capital on the side that collects the 8h settlement), the grid earns both the oscillation-harvest premium and a structural carry — while the rebalancing logic keeps the skew aligned with the prevailing funding direction, ensuring the carry is positive throughout the grid's active life."

data_required: [ohlcv-1h, ohlcv-4h, funding-rates, open-interest, mark-price, perpetual-futures-depth, adx-14, atr-14]
min_capital_usd: 5000
capacity_usd: 15000000
crowding_risk: medium

expected_sharpe: 1.2
expected_max_drawdown: 0.15
breakeven_cost_bps: 10

decay_evidence: "No published study on funding-skewed grid strategies specifically. The grid spread-capture edge has documented slow decay as retail bot platforms proliferate (see regime-gated-grid wiki page). The carry component is the same as documented in BIS WP 1087 (Schmeling et al. 2023) and has compressed since 2024 but remains positive. The combination — earning both spread and carry — should decay more slowly than either alone in range regimes."

kill_criteria: |
  - strategy drawdown > 15% from high-water mark
  - grid revenue per cycle < taker fee cost for 25 consecutive cycles (spread edge gone)
  - funding rate averages < 0.005%/8h absolute across the universe for 30 consecutive days (carry contribution near zero)
  - rolling 3-month Sharpe < 0 on minimum 50 completed grid cycles
  - skew rebalancing frequency exceeds 3 full rebalances per 24h for 7 consecutive days (funding too volatile for stable skew)

related: ["[[grid-trading]]", "[[regime-gated-grid]]", "[[funding-rate-arbitrage]]", "[[funding-filtered-momentum]]", "[[hyperliquid-market-making]]", "[[carry-with-tail-hedge]]", "[[market-making]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[open-interest]]", "[[adx]]", "[[atr]]", "[[adverse-selection]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Funding-Skewed Grid

A funding-skewed grid is [[grid-trading]] on crypto perpetuals where the **inventory allocation is biased toward the funding-receiver side**: if funding is positive (longs pay shorts), the grid holds a net short skew — more capital at sell levels than buy levels — to collect the 8h funding settlement while still quoting on both sides. The grid rebalances its skew when funding flips direction. The primitive edge is the grid's oscillation-harvest in range regimes; the overlay is a structural carry income that improves the P&L on the inventory the grid is already absorbing.

This is differentiated from [[regime-gated-grid]] — that page solves the grid's regime-classification problem (when to run the grid at all). This page assumes the grid is already running in a valid regime and adds an intra-grid inventory optimisation: given that the grid will be holding inventory on both sides, skew it toward the side that earns carry. The regime gate and the funding skew are compatible overlays and can be stacked.

This is differentiated from [[funding-rate-arbitrage]] — that strategy takes a directional carry position (long spot, short perp) to earn funding without price exposure. This page does not create a direction-pure carry position; it merely tilts a market-making grid's inventory toward the carry-receiving side while retaining the market-making structure.

## Edge source

Per [[edge-taxonomy]], **structural + risk-bearing**:

- **Structural (primary)** — the grid's spread capture is structural: passive limit orders earn the bid-ask spread from takers who value immediacy over price. The funding carry is also structural: the perpetual contract settles the 8h funding payment regardless of price direction. Combining both structural income streams — spread capture and funding carry — in a single inventory reduces the P&L volatility of holding grid inventory while adding a consistent carry floor.
- **Risk-bearing (secondary)** — the grid operator bears inventory risk (being stuck long in a downtrend, or stuck short in an uptrend). The funding skew is compensation for bearing this inventory risk *in the direction that the funding mechanism also compensates*: when funding is positive, the grid holds a net short skew, being paid by the crowd of longs to absorb their risk. When funding is negative, the grid flips to net long, collecting carry from the crowded shorts. This aligns the grid's risk-bearing with the market's structural payment mechanism.

## Why this edge exists

**The combination solves the grid's zero-carry problem.** A symmetric grid is P&L-neutral with respect to funding direction: on average, it holds equal inventory on both sides, so the net funding receipt is approximately zero. This is a missed opportunity — the grid is absorbing market risk for free when it could be absorbing it for a positive carry. The skew corrects this by deliberately holding more inventory on the funding-receiver side.

Three mechanisms reinforce the combination:

1. **Carry income reduces the break-even per cycle.** A symmetric grid on BTC at 0.5% spacing must earn 0.5% per buy-then-sell cycle to justify the inventory risk. A grid with a net short skew at +0.05%/8h funding earns ~0.6% APY per $1 of net short inventory per day in carry alone — roughly equivalent to 12 completed 0.5%-grid cycles in a day. The carry does not replace the grid, but it meaningfully reduces the P&L dependence on oscillation frequency.

2. **Skew aligns with the crowding direction.** When funding is positive, the crowd is net long. The grid's short skew means the grid is on the other side of the crowd — providing liquidity to the over-long side and collecting their crowding premium. This is a structural reinforcement: the counterparty (the over-long retail participant) is both the source of the taker flow (grid spread income) AND the source of the funding payment (carry income).

3. **Skew rebalancing is a natural risk management rule.** When funding flips, the grid rebalances its skew — this is not just a carry optimisation but also a risk management action: by shifting inventory, the grid moves away from the side that is becoming the crowded loser (previously positive funding → longs were crowded → now funding has flipped → shorts are crowded). The rebalancing keeps the grid on the structural payment side.

**Who is on the other side:** the directional retail participant whose perp funding payments are the source of the carry income; and the taker-flow participant who sacrifices price improvement to cross the grid's spread.

## Null hypothesis

Under the null, funding direction carries no information about optimal grid inventory skew: the average P&L of a skewed grid should equal the average P&L of a symmetric grid on the same pairs in the same regime, after accounting for the minor notional difference in deployed capital. Specifically:
- The carry income from the funding skew should not improve Sharpe or drawdown statistics beyond the symmetric grid baseline.
- Skewed inventory should not fill at better rates or improve cycle completion vs symmetric allocation.

The null is currently not rejected in this wiki (`backtest_status: untested`). Testable prediction: compare skewed vs symmetric grid P&L in range regimes with funding > 0.02%/8h; the skewed version should show materially better risk-adjusted P&L due to carry income.

## Rules

### Grid activation gate (shared with [[regime-gated-grid]])

The grid must first satisfy a regime gate before activation:
1. **ADX(14) < 20** on the 4h chart — low directional momentum.
2. **Bollinger Bandwidth (20, 2σ)** in the bottom 30th percentile of its 90-day history.
3. **Volatility regime** (`/api/v1/volatility/regime`) = `compressed` or `mean_reverting`.
4. **No active event risk**: `/api/v1/event/regime/score` < 50.

*These are the same conditions as [[regime-gated-grid]]. When the regime-gated-grid and the funding-skewed-grid are both considered, prefer the funding-skewed version only when funding is non-trivial (absolute rate > 0.01%/8h); otherwise use the symmetric grid.*

### Funding skew computation

Define `funding_8h` as the current 8h funding rate. Positive = longs pay shorts; negative = shorts pay longs.

**Skew ratio** = the fraction of total grid capital allocated to the funding-receiver side relative to the other side:

| Funding level (absolute) | Skew factor | Effect |
|---|---|---|
| `|funding| < 0.01%/8h` | 1.0 (symmetric) | Carry near zero; run symmetric grid |
| `0.01% ≤ |funding| < 0.03%/8h` | 1.3 | Mild skew: 56.5% on receiver side |
| `0.03% ≤ |funding| < 0.05%/8h` | 1.5 | Moderate skew: 60% on receiver side |
| `|funding| ≥ 0.05%/8h` | 1.75 | Strong skew: 63.6% on receiver side |

**Direction**: if `funding_8h > 0` → skew toward SHORT (more sell levels than buy levels). If `funding_8h < 0` → skew toward LONG (more buy levels than sell levels).

**Implementation**: allocate capital per level proportionally. If skew factor = 1.5 and there are 8 levels per side, the skewed side gets 60% of total notional spread across 8 levels and the other side gets 40%. Level sizes differ but the total levels per side remain equal (preserving grid symmetry in quoting).

### Skew rebalancing

Rebalance the skew when:
1. **Funding crosses zero**: flip the skew direction. This is the primary rebalancing trigger. Do not flip during a single period; require 2 consecutive periods below/above zero to avoid flipping on noise.
2. **Funding magnitude band changes**: if funding moves from one skew-factor band to another and stays there for 2 consecutive 8h periods, adjust the capital allocation.
3. **Rebalance cap**: never rebalance more than once per 8h period (align with funding settlement periods).

**Kill conditions** (same as [[regime-gated-grid]] plus):
- Funding rate > 0.08%/8h (extreme positive funding → crowd is trend-following, not ranging; grid kill).
- ADX(14) ≥ 25; ATR breakout (1.5× ATR from channel midpoint); volatility regime flip to `expanding` or `vol_shock`.

### Position sizing

- Total grid notional: max 25% of sleeve capital per asset, with 30% cash reserve (same as regime-gated-grid).
- Skewed side gets `skew_factor / (1 + skew_factor)` of total notional.
- Symmetric side gets `1 / (1 + skew_factor)` of total notional.
- Maximum leverage: 2× on the skewed side (the net directional skew creates a structural position; leverage must be capped).
- Grid spacing: 0.5% minimum on major perps (BTC, ETH, SOL).

## Implementation pseudocode

```python
# funding_skewed_grid.py — grid with inventory skew toward funding receiver

from dataclasses import dataclass
from typing import Optional

# ---- thresholds ----
ADX_MAX_ON        = 20.0
ADX_KILL          = 25.0
BB_WIDTH_PCT      = 30
VOL_REGIME_OK     = {"compressed", "mean_reverting"}
EVENT_SCORE_OK    = 50
EVENT_SCORE_KILL  = 70
BREAKOUT_ATR_MULT = 1.5
FUNDING_KILL      = 0.0008   # 0.08%/8h: extreme funding → grid kill
GRID_DRAWDOWN_KILL = 0.08
GRID_SPACING_PCT  = 0.005
MAX_LEVELS_EACH   = 12
MAX_NOTIONAL_PCT  = 0.25
CASH_RESERVE_PCT  = 0.30
SKEW_FLIP_PERIODS = 2        # consecutive periods for flip confirmation

SKEW_TABLE = [
    (0.0001, 1.0),   # < 0.01%/8h → symmetric
    (0.0003, 1.3),   # 0.01-0.03% → mild skew
    (0.0005, 1.5),   # 0.03-0.05% → moderate skew
    (float('inf'), 1.75),  # ≥ 0.05% → strong skew
]

def get_skew_factor(funding_abs: float) -> float:
    for threshold, factor in SKEW_TABLE:
        if funding_abs < threshold:
            return factor
    return SKEW_TABLE[-1][1]

@dataclass
class GridSnapshot:
    adx_14: float
    bb_width_percentile: float
    vol_regime: str
    event_risk_score: float
    price: float
    atr_14: float
    funding_8h: float
    channel_mid: float
    funding_negative_streak: int   # periods with funding < 0
    funding_positive_streak: int   # periods with funding > 0

def gate_open(r: GridSnapshot) -> bool:
    return (r.adx_14 < ADX_MAX_ON
            and r.bb_width_percentile < BB_WIDTH_PCT
            and r.vol_regime in VOL_REGIME_OK
            and r.event_risk_score < EVENT_SCORE_OK
            and abs(r.funding_8h) < FUNDING_KILL)

def kill_triggered(r: GridSnapshot, grid_drawdown: float) -> Optional[str]:
    if r.adx_14 >= ADX_KILL:
        return f"ADX {r.adx_14:.1f} >= {ADX_KILL}"
    if abs(r.price - r.channel_mid) > BREAKOUT_ATR_MULT * r.atr_14:
        return "price breakout beyond ATR threshold"
    if r.vol_regime in {"expanding", "vol_shock"}:
        return f"vol regime flipped to {r.vol_regime}"
    if r.event_risk_score >= EVENT_SCORE_KILL:
        return f"event risk {r.event_risk_score}"
    if abs(r.funding_8h) >= FUNDING_KILL:
        return f"extreme funding {r.funding_8h*100:.4f}%/8h"
    if grid_drawdown > GRID_DRAWDOWN_KILL:
        return f"grid drawdown {grid_drawdown:.1%}"
    return None

def compute_skew(r: GridSnapshot, grid_state: dict) -> dict:
    """Returns skew allocation for both sides."""
    fund = r.funding_8h
    fund_abs = abs(fund)
    factor = get_skew_factor(fund_abs)

    # determine direction: who receives funding?
    # positive funding → shorts receive → skew toward short side
    # negative funding → longs receive → skew toward long side
    receiver_side = "short" if fund >= 0 else "long"

    # check if a flip is confirmed (direction change held for SKEW_FLIP_PERIODS)
    prev_receiver = grid_state.get("receiver_side", receiver_side)
    if prev_receiver != receiver_side:
        streak = (r.funding_negative_streak if fund < 0
                  else r.funding_positive_streak)
        if streak < SKEW_FLIP_PERIODS:
            receiver_side = prev_receiver   # not yet confirmed; hold previous skew
            factor = grid_state.get("skew_factor", 1.0)

    total = MAX_NOTIONAL_PCT * (1 - CASH_RESERVE_PCT)
    receiver_frac = factor / (1 + factor)
    other_frac    = 1 / (1 + factor)

    return {
        "receiver_side": receiver_side,
        "skew_factor": factor,
        "receiver_notional_pct": receiver_frac * total,
        "other_notional_pct": other_frac * total,
    }

def manage_grid(r: GridSnapshot, grid_state: dict, book: dict) -> dict:
    kill_reason = kill_triggered(r, grid_state.get("drawdown", 0.0))
    if kill_reason:
        return {"action": "KILL_GRID", "reason": kill_reason,
                "reentry_lockout_hours": 24}

    if grid_state.get("active"):
        # Update skew if needed
        skew = compute_skew(r, grid_state)
        if skew["skew_factor"] != grid_state.get("skew_factor"):
            return {"action": "REBALANCE_SKEW", "skew": skew}
        return {"action": "HOLD_GRID"}

    if grid_state.get("lockout_remaining_hours", 0) > 0:
        return {"action": "WAIT", "reason": "post-kill lockout"}

    if gate_open(r):
        skew = compute_skew(r, grid_state)
        channel_h = r.channel_mid * (1.01)
        channel_l = r.channel_mid * (0.99)
        n_levels = min(
            int((channel_h - channel_l) / r.price / GRID_SPACING_PCT),
            MAX_LEVELS_EACH
        )
        return {
            "action": "ACTIVATE_GRID",
            "channel": [channel_l, channel_h],
            "grid_levels": n_levels * 2,
            "spacing_pct": GRID_SPACING_PCT,
            "skew": skew,
        }
    return {"action": "WAIT", "reason": "regime gate not open"}
```

The production system adds: real-time funding polling at 8h intervals; skew rebalancer that issues cancel/replace for the level sizes on each side after a confirmed skew change; drawdown accounting per grid cycle; and daily carry income attribution (funding received vs spread captured) for strategy monitoring.

## Indicators / data used

- **ADX(14) on 4h** — regime gate and kill trigger (same as [[regime-gated-grid]]).
- **Bollinger Bandwidth (20, 2σ)** — range-compression gate.
- **ATR(14) on 4h** — breakout kill trigger.
- **Volatility regime** (`/api/v1/volatility/regime`) — vol state gate and kill.
- **Event risk score** (`/api/v1/event/regime/score`) — catalyst calendar risk.
- **[[funding-rate]] (8h)** — the primary skew-direction and skew-magnitude input; also serves as extreme-funding kill at 0.08%/8h.

## Example trade

**Setup (illustrative):**

- Asset: BTC-PERP on Hyperliquid, 4h chart.
- ADX(14) = 15. Bollinger Bandwidth percentile = 22. Vol regime = `compressed`. Event risk = 18. Gate: **ACTIVATE**.
- Price midpoint: $95,000. Channel: $93,950–$96,050 (1% each side). Grid spacing: 0.5% = ~$475. Levels: 4 per side = 8 total.
- Sleeve capital: $100,000. Total notional: 25% × 70% = $17,500.
- **Funding (8h): +0.038%/8h** (~42% APY). Absolute = 0.038% → skew factor **1.5** (moderate skew band).
- Skew direction: funding positive → shorts receive → skew toward SHORT side.
- Short-side notional: 1.5/2.5 × $17,500 = **$10,500** (60%). Long-side notional: 1/2.5 × $17,500 = **$7,000** (40%).
- 4 sell levels at $95,475/95,950/96,425/96,900: $10,500/4 = $2,625 per sell level.
- 4 buy levels at $94,525/94,050/93,575/93,100: $7,000/4 = $1,750 per buy level.

**Day 1:** BTC oscillates between $93,800 and $96,100. Grid fills: 3 complete sell-buy cycles (short $10,500 average → cover on oscillation). Spread per cycle at 0.5%: ~$13.13 per $2,625. Net 3 cycles (short side): $39.38. 1 complete buy-sell cycle (long side): ~$8.75.
**Carry income (day 1):** net short inventory average ~$3,000 × 0.038%/8h × 3 periods = **$3.42 carry**.
**Day 1 gross:** grid spread ~$48 + carry ~$3.42 = **$51.42** (vs symmetric grid ~$35, +47% improvement).

**Day 3:** ADX rises to 22.1. Kill triggered at ADX 22+ (pre-emptive, before the kill threshold of 25 — in practice the operator monitors and acts before the hard kill). Grid shut down.

3-day gross: ~$130 spread + ~$10 carry = **$140 on $17,500** (~107% APY annualised; illustrative exceptional short window).

*(Illustrative only. Actual results depend on fill rates, fee structure, and funding stability.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.2 | Symmetric regime-gated grid ~1.1; carry skew adds ~0.1-0.2 in range regimes with non-trivial funding |
| Expected max drawdown | ~15% | Same as regime-gated grid; the skew does not materially change the kill-trigger drawdown profile |
| Funding carry contribution | 5-30% of daily grid P&L | Depends on funding level; at 0.04%/8h with 60% skew, carry ≈ 25% of daily spread income |
| Breakeven cost budget | 10 bps | Narrow; requires maker fills; skew does not change the fee structure |
| Skew rebalance cost | ~4-8 bps per full rebalance | Cancel/replace on all levels; costs are small relative to carry income |

**Realistic cost overlay (Hyperliquid):**
- Maker fees: ~0.02% per leg = ~4 bps per cycle (unchanged from symmetric grid).
- Skew rebalancing: ~1-2 rebalances per funding-direction cycle; at $17,500 notional, ~$3-7 per rebalance.
- Carry income per day at 0.038%/8h with avg $3,000 net short: ~$3.42/day ≈ 20 bps on deployed notional.

## Capacity limits

- **Per asset on Hyperliquid majors**: ~$2-5M before grid levels become visible to predatory traders (same as [[regime-gated-grid]]).
- **Carry income does not scale linearly**: as the grid grows, the skew increases the net directional exposure; above ~$5M, the net short (or long) skew becomes large enough to be a meaningful directional position in its own right, changing the risk profile from grid-with-skew to carry-with-grid-income.
- The carry contribution is capped by the funding magnitude — at very low funding rates (< 0.01%/8h), the skew provides negligible carry and the strategy reverts to a symmetric grid.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Funding volatility (#5 / Operational).** If funding flips direction multiple times per day, the skew rebalancing costs accumulate without collecting stable carry. The cap of one rebalance per 8h period limits this, but highly volatile funding periods reduce the carry contribution to near-zero.
2. **Regime misclassification (#5).** The same failure mode as [[regime-gated-grid]]: the gate fires in a borderline range, the price breaks out, and the skewed inventory accumulates directional losses. The kill triggers and post-kill lockout contain this.
3. **Extreme funding kills the grid (#5).** At +0.08%/8h, the funding kill trigger fires and the grid shuts down. Paradoxically, the highest funding environments — where carry would be most attractive — are also the most likely to be trending (high funding often coincides with strong uptrends). The kill is correct: do not try to harvest extreme carry inside a trending market with a grid.
4. **Consumer-bot crowding (#4).** Popular pairs have many retail grids at similar spacings. The funding-skewed grid's competitive advantage is in the carry harvesting, not in the spread per cycle; if spread per cycle is compressed to near-zero by competitors, only the carry remains — and the strategy becomes structurally closer to a directional carry trade.
5. **Fee tier dependency (#7: Operational).** The grid's economics depend on maker fills. If the venue increases maker fees or the grid is forced to taker-fill frequently, the 10 bps breakeven budget is consumed by fees, leaving no margin for the carry skew to improve.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 15%** in any rolling 14-day window.
2. **Grid revenue per cycle < taker fee cost** for 25 consecutive cycles — spread edge is gone.
3. **Funding absolute average < 0.005%/8h** for 30 consecutive days — carry contribution near zero; strategy reverts to symmetric grid with overhead costs.
4. **Rolling 3-month Sharpe < 0** on minimum 50 completed cycles.
5. **Skew rebalancing > 3 full rebalances per 24h for 7 consecutive days** — funding is too volatile for a stable skew; the carry and rebalancing costs are inverting the edge.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Earns both spread and carry simultaneously**: the two income streams are largely independent — spread income depends on price oscillation frequency; carry income depends only on funding settlement. Combining them improves the P&L per unit of deployed capital in range regimes.
- **Aligns grid inventory with the structural payment mechanism**: the skew is not a speculative bet on funding direction — it is a passive adjustment to collect what the contract is already paying on the side the grid naturally holds.
- **Skew rebalancing is a risk management improvement**: the flip of the skew when funding changes direction keeps the grid away from the crowd-losing side, providing a secondary benefit beyond carry.
- **Stackable with [[regime-gated-grid]]**: the two strategies share the same regime gate architecture; the funding-skewed grid can be seen as a carry-enhanced version of the regime-gated grid, adding only the skew layer without changing the grid kill logic.
- **Self-calibrating skew**: the skew factor table is tied to funding levels, so the strategy automatically reduces skew when funding is trivial (near-zero) and increases it when carry is meaningful.

## Disadvantages

- **Net directional exposure from the skew**: a 60%/40% allocation creates a ~20% net directional bias. In a sudden breakout against the skew direction, the asymmetric inventory accumulates losses faster than a symmetric grid. The kill triggers limit this, but the skewed grid has higher directional sensitivity.
- **Rebalancing costs on funding flips**: each full skew reversal requires cancelling and replacing all levels, incurring fees and potential slippage. In environments where funding oscillates around zero, these costs can exceed the carry income.
- **Carry is small relative to spread at low funding**: at 0.01%/8h, the carry on a $3,000 net position is ~$0.90/day — less than 10% of typical daily spread income. The overlay only materially improves performance when funding is consistently 0.03%+/8h.
- **More complex than symmetric grid**: the skew logic, rebalancing trigger, and asymmetric level sizing add operational complexity. Each additional component is a potential failure point.
- **Hyperliquid-specific**: most of the analysis assumes Hyperliquid's fee structure and funding mechanism. On CEX perps with different maker-rebate structures, the economics change materially.

## Sources

- Avellaneda, M. and Stoikov, S. (2008), *High-frequency trading in a limit order book*, Quantitative Finance. Inventory-optimal quoting with drift: the theoretical basis for skewing quotes toward the funding-receiver side when there is a systematic directional carry.
- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (2023). Funding as a structural payment: the carry income the skew is designed to capture. https://www.bis.org/publ/work1087.pdf
- [[regime-gated-grid]] — the regime gate architecture shared by this strategy; activation and kill logic.
- [[grid-trading]] — the underlying primitive; grid spacing, level construction, and drawdown mechanics.
- [[hyperliquid-market-making]] — Hyperliquid-specific market-making mechanics and fee structure.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange 8h funding (Binance + Hyperliquid); primary skew-direction and skew-magnitude input
- `GET /api/v1/volatility/regime` — vol regime for grid activation gate
- `GET /api/v1/quant/market` — HMM regime probabilities for secondary gate
- `GET /api/v1/event/regime/score` — event risk composite for pre-kill check
- `GET /api/v1/liquidity/depth` — order-book depth to confirm adequate liquidity for grid maker fills

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for skew-calibration backtest
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI) for regime and carry analysis
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) for multi-regime skew performance
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — OHLCV for ADX, ATR, Bollinger Bandwidth computation

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

## Related

- [[grid-trading]] — the underlying primitive; this page is the carry-skew extension
- [[regime-gated-grid]] — the regime-gate layer this page builds upon; the two are stackable
- [[funding-rate-arbitrage]] — the pure carry primitive; shares the funding mechanism but not the grid structure
- [[hyperliquid-market-making]] — Hyperliquid-specific market making; overlapping execution context
- [[carry-with-tail-hedge]] — a carry-focused combination that tail-hedges rather than grid-trades
- [[funding-filtered-momentum]] — funding filter on momentum entries; shares the funding-as-overlay concept
- [[market-making]] — the microstructure theory underpinning grid spread capture
- [[funding-rate]] — the contract mechanism providing the carry income
- [[open-interest]] — secondary grid signal for regime confirmation
- [[perpetual-futures]] — the instrument carrying both the grid and the funding mechanism
- [[adx]] — the directional strength indicator used in the grid gate and kill
- [[atr]] — the volatility measure used in the breakout kill trigger
- [[adverse-selection]] — what happens to skewed inventory when informed flow arrives
- [[edge-taxonomy]] — structural + risk-bearing classification
- [[failure-modes]] — regime-change, volatility, and crowding risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
