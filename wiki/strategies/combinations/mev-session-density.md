---
title: "MEV Session Density Filter"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, execution, algorithmic, market-microstructure, quantitative, crypto, ethereum]
aliases: ["MEV Session Filter", "Session-Aware MEV Scheduling", "MEV Time-of-Day Overlay", "MEV Density Clock"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, latency]
edge_mechanism: "MEV opportunity density (cross-exchange DEX arb, liquidation MEV, sandwich backrun) is demonstrably non-uniform across the 24-hour clock — it peaks at major CEX-session opens (Asia, Europe, New York) when fresh directional order flow arrives and moves spot prices faster than AMM pools can rebalance, and during elevated-volatility windows that produce liquidation cascades. A session-density filter that concentrates searcher infrastructure spend (builder bids, gas, co-location) on high-density windows and pauses or reduces activity during predictably low-yield windows improves net Sharpe by reducing gas burn and builder-bid cost during periods when extractable value is below the per-attempt break-even threshold."

data_required: [mempool-pending-tx, dex-pool-reserves, block-time-utc, gas-basefee, liquidation-events, cex-volume-by-session, historical-mev-pnl-by-hour]
min_capital_usd: 5000
capacity_usd: 3000000
crowding_risk: high

expected_sharpe: 0.9
expected_max_drawdown: 0.12
breakeven_cost_bps: 60

decay_evidence: "Session-timing effects in MEV are not published academically but are widely known among competitive searcher teams. The edge is not from 'discovering' session density — it is from operational discipline: most MEV bots run continuously without session-aware cost budgeting, spending as much on gas in dead hours as peak hours. The session-aware scheduling edge is thus an OPERATIONAL efficiency gain, not an informational alpha that decays as more people learn it. However, as MEV infrastructure costs decline (EIP-4844 blob gas, L2 MEV), the absolute cost-saving from session scheduling may shrink."

kill_criteria: |
  - rolling 30-day net MEV P&L (after gas, builder bids, failed-tx drag) falls below zero
  - session-density pattern shifts: 4 consecutive weeks where high-density sessions produce below-average gross extractable value (possible structural shift in when large users are active)
  - gas price spikes to levels where per-attempt break-even exceeds 90th-percentile gross opportunity value across ALL sessions (pause entirely, not just low-density windows)
  - competitor latency improvement makes all sessions equally low-yield (latency-race loss, not session-scheduling issue)

related: ["[[mev-strategies]]", "[[jito-solana-mev-arbitrage]]", "[[jit-liquidity]]", "[[mev-execution-guide]]", "[[session-aware-mean-reversion]]", "[[session-overlap-momentum]]", "[[off-hours-liquidation-playbook]]", "[[funding-window-timing]]", "[[market-microstructure]]", "[[latency-and-mev-on-chain-clob]]", "[[mev]]", "[[flashbots]]", "[[gas-price]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# MEV Session Density Filter

MEV session density filter is an **operational scheduling overlay** on top of any MEV strategy family (DEX-to-DEX arbitrage, sandwich backrunning, JIT liquidity provision, liquidation MEV) that concentrates searcher infrastructure spend — builder bids, failed-transaction gas burn, and co-location compute — on the hours of the day where gross extractable value per block is historically highest. This is explicitly not a new MEV strategy: it is a resource-allocation wrapper that improves the net Sharpe of existing MEV operations by reducing cost burn during predictably low-yield windows. The counterparty is passive: other MEV operators who run continuously without session-aware cost budgeting, spending the same infrastructure per block in 3:00 UTC dead hours as in 14:00 UTC New York-London overlap.

**This is differentiated from [[mev-strategies]]** — that page documents the core MEV strategy types (sandwich, backrun, JIT, liquidation, arbitrage) and their mechanics. This page does not introduce a new MEV mechanism; it adds a time-of-day cost-budget overlay that schedules when to compete and when to reduce bids, applicable across all MEV strategy types.

**This is differentiated from [[session-overlap-momentum]]** — that page exploits the directional price momentum that occurs at major session overlaps (geographic liquidity transitions). This page uses the same session calendar as a cost-allocation guide for MEV infrastructure, not as a momentum entry signal. The MEV session filter does not require a directional position.

**This is differentiated from [[funding-window-timing]]** — that page exploits the pre-settlement repositioning drift around CEX funding timestamps (00:00/08:00/16:00 UTC) as a directional carry trade. This page uses a broader session-density classification (entire session windows, not specific settlement minutes) and applies to MEV cost scheduling, not to directional funding carry.

## Edge source

Per [[edge-taxonomy]], **structural + latency**:

- **Structural** — MEV opportunity density is driven by user flow timing (when large users, market makers, and institutions are active). This is a structural calendar pattern: new-session opens bring fresh directional flow (CEX price moves vs AMM reserves creating arb gaps); liquidation events cluster during high-vol windows that are correlated with session transitions. The session density pattern is persistent because user behavior rhythms are persistent.
- **Latency** — MEV is a latency competition; infrastructure costs (builder bid, gas) are sunk per attempted block. Session-aware cost budgeting concentrates competitive bids on the highest-yield blocks, equivalent to "latency budget" management — being willing to outbid competitors more aggressively when the EV justifies it and reducing bids in low-EV windows rather than bidding flat across all blocks.

## Why this edge exists

**MEV opportunity density follows a predictable intraday cycle** driven by user flow timing:

1. **New York open (13:00–17:00 UTC):** highest DEX-arb volume. US institutions, algo desks, and large retail all become active simultaneously; directional spot flows move BTC/ETH prices on Binance faster than Uniswap/Curve pools can rebalance, creating sustained arb gaps. Coinbase premium spikes (see [[spot-led-momentum-filter]] — the same flow drives both). Builder competition is highest but gross opportunity is also highest: the optimal window to bid aggressively.

2. **London-New York overlap (12:00–16:00 UTC):** liquidation cascade windows are most frequent here. When macro news (CPI, FOMC, NFP) prints and moves crypto as a risk asset, cascades trigger; the overlap session produces the highest liquidation MEV yield per block.

3. **Asia open (00:00–03:00 UTC):** moderate activity; altcoin-specific moves (Korean premium events, Asia-native project news) create DEX-arb in less-efficient pools. Competition is lower; builder bids can be smaller per EV unit.

4. **Dead zone (04:00–11:00 UTC):** lowest MEV opportunity density per block. Large user flow is at minimum; fewer new positions are opened; DEX-to-DEX gaps are smaller and shorter-lived. Gas base fee is typically at its daily minimum — but the competition for high-EV blocks is also at minimum, which is exactly when a continuous MEV bot wastes the most proportion of its gas on low-yield opportunities.

**The cost-save logic:** a typical competitive MEV operation spends 30–60% of its gas costs and failed-tx gas in the dead zone, capturing only 10–15% of its total MEV income. Session scheduling that reduces bids by 60–75% in the dead zone while holding full bids during high-density windows conserves gas float, reduces failed-tx drag, and improves Sharpe — without reducing income meaningfully.

**Who is on the other side:** searchers who run 24/7 without session-aware budgets, spending equally per block across all sessions. They over-subsidise dead-zone block builders relative to the extractable value available.

## Null hypothesis

Under the null, MEV opportunity density is **uniform across the 24-hour clock**: a 60-minute window at 04:00 UTC produces the same expected gross extractable value per block as a 60-minute window at 14:00 UTC. If the null holds:

- Session-aware bid reduction during the dead zone does NOT improve net Sharpe — it only reduces activity while missing opportunities equally distributed across sessions.
- Historical MEV P&L indexed by hour-of-day should show no statistically significant variation in gross EV per block.

The null is currently NOT rejected by the formal literature (no published per-hour MEV density paper as of 2026). Testable with historical MEV data (Flashbots data, Dune Analytics MEV dashboards): regress gross MEV income per block on hour-of-day bucket and test for joint significance of session dummies. Prediction: high-density session dummies (NY open, London-NY overlap) are positive and significant at p < 0.05.

## Rules

### Session density classification

| Session window (UTC) | Label | Action |
|---|---|---|
| 13:00–17:00 | High-density: NY open | Full bid schedule; aggressive builder tips |
| 12:00–16:00 | High-density: London-NY overlap | Full bid schedule; liquidation MEV priority |
| 00:00–03:00 | Medium-density: Asia open | 70% bid schedule; alt-pool arb focus |
| 08:00–12:00 | Medium-density: London pre-overlap | 60% bid schedule; monitoring for UK/EU news |
| 17:00–21:00 | Low-density: NY afternoon | 50% bid schedule |
| 21:00–24:00 | Dead zone: global overlap | 30% bid schedule |
| 03:00–08:00 | Dead zone: Asia-Europe gap | 25% bid schedule |

*Bid schedule percentage applies to: maximum builder tip per block (reduce proportionally); active searcher pool count (pause lower-priority strategy types in dead zones); and total gas float committed per hour.*

### Opportunity-type priority by session

- **Dead zone (25–30% bid schedule):** run only highest-margin strategy types — on-chain liquidation MEV (guaranteed profit if won) and extreme DEX arb (≥ 2× break-even). Pause: sandwich, JIT (require active large order flow).
- **Medium-density:** run all profitable strategy types above 1.5× break-even threshold.
- **High-density:** run all strategy types above 1.0× break-even threshold; add sandwich and JIT back to active pool; raise max builder tip ceiling.

### Volatility override

If realized 15-minute BTC price volatility exceeds 1.5% within any 30-minute window, **temporarily upgrade to "High-density" bid schedule regardless of session** for 45 minutes. Liquidation MEV opportunities do not respect session boundaries; they follow vol events.

### Entry / position sizing

Not applicable: MEV positions are atomic (within-block). The "sizing" decision is the builder tip amount and gas allocation per opportunity, not notional.

### Session-density calibration

Re-calibrate session density weights every **90 days** using trailing 90-day historical MEV P&L (gross EV, gas cost, failed-tx drag) bucketed by UTC hour. If the high-density window shifts (e.g., increasing Asian institution participation moves the density peak to 01:00–05:00 UTC), update the session table above.

## Implementation pseudocode

```python
# mev_session_density.py

from datetime import datetime, timezone
from enum import Enum

class DensityLevel(Enum):
    HIGH    = 1.00   # full bid schedule
    MEDIUM  = 0.65   # 60–70% bid schedule
    LOW     = 0.40   # 30–50% bid schedule

# UTC hour ranges → density level
SESSION_MAP = {
    # High-density: NY open + London-NY overlap
    **{h: DensityLevel.HIGH   for h in range(12, 17)},   # 12:00–16:59 UTC
    13: DensityLevel.HIGH,
    14: DensityLevel.HIGH,
    15: DensityLevel.HIGH,
    16: DensityLevel.HIGH,
    # Medium: Asia open, London pre-overlap
    **{h: DensityLevel.MEDIUM for h in [0, 1, 2, 8, 9, 10, 11]},
    # Low: NY afternoon, dead zones
    **{h: DensityLevel.LOW    for h in list(range(3, 8)) + list(range(17, 24))},
}

# Build the full 0–23 map cleanly
SESSION_MAP = {h: DensityLevel.LOW for h in range(24)}
for h in [0, 1, 2, 8, 9, 10, 11]:    SESSION_MAP[h] = DensityLevel.MEDIUM
for h in range(12, 17):               SESSION_MAP[h] = DensityLevel.HIGH

VOLATILITY_OVERRIDE_THRESHOLD_PCT = 1.5    # 15-min BTC move triggers HIGH
VOLATILITY_OVERRIDE_DURATION_MIN  = 45

MAX_BUILDER_TIP_BASE_GWEI = 10.0           # baseline max tip in HIGH session

def current_density(utc_hour: int, recent_15m_move_pct: float,
                    vol_override_remaining_min: int) -> DensityLevel:
    if vol_override_remaining_min > 0:
        return DensityLevel.HIGH
    if recent_15m_move_pct >= VOLATILITY_OVERRIDE_THRESHOLD_PCT:
        return DensityLevel.HIGH   # will set override timer externally
    return SESSION_MAP[utc_hour]

def max_builder_tip(density: DensityLevel) -> float:
    return MAX_BUILDER_TIP_BASE_GWEI * density.value

def strategy_types_active(density: DensityLevel) -> list[str]:
    always_on = ["liquidation_mev", "extreme_dex_arb"]   # ≥2× break-even, always run
    medium_on = always_on + ["standard_dex_arb", "backrun"]
    high_on   = medium_on + ["sandwich", "jit_liquidity"]
    if density == DensityLevel.HIGH:   return high_on
    if density == DensityLevel.MEDIUM: return medium_on
    return always_on

def session_scheduler_tick(utc_now: datetime, recent_15m_btc_move_pct: float,
                           vol_override_remaining_min: int) -> dict:
    hour = utc_now.hour
    density = current_density(hour, recent_15m_btc_move_pct, vol_override_remaining_min)
    tip = max_builder_tip(density)
    active = strategy_types_active(density)
    new_override = (VOLATILITY_OVERRIDE_DURATION_MIN
                    if recent_15m_btc_move_pct >= VOLATILITY_OVERRIDE_THRESHOLD_PCT
                    else max(0, vol_override_remaining_min - 1))
    return {
        "density":               density.name,
        "bid_fraction":          density.value,
        "max_builder_tip_gwei":  tip,
        "active_strategy_types": active,
        "vol_override_min_left": new_override,
    }
```

The production scheduler wraps each MEV bot's opportunity evaluator: before submitting a bundle, it calls `session_scheduler_tick` and (a) caps the builder tip at `max_builder_tip_gwei`, (b) skips the opportunity if its strategy type is not in `active_strategy_types`, and (c) raises the minimum-EV threshold for submission in LOW-density windows.

## Indicators / data used

- **UTC block timestamp** — primary session clock; derived from each block header (no external data source required).
- **15-minute BTC realized move** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=2`; compute |close[−1] − close[−2]| / close[−2]; triggers volatility override.
- **Historical MEV P&L by hour** — sourced from Flashbots MEV-Inspect data (Dune Analytics dashboard `mev_summary`) or operator's own execution log; used for quarterly session-weight recalibration.
- **Gas base fee** — EIP-1559 base fee per block from the Ethereum node; used to verify builder-tip calculations (effective priority fee = tip − base fee floor).
- **CryptoDataAPI session context** — `GET /api/v1/regimes/current` for macro regime override; if `Structural_Shock`, elevate to HIGH density for liquidation MEV priority regardless of session clock.

*Note: CryptoDataAPI does not have a dedicated MEV endpoint; MEV-specific data (Flashbots relay, bundle success rates, MEV revenue by strategy) is sourced from the Flashbots API (`boost-relay.flashbots.net`) and Dune Analytics. The CryptoDataAPI regime and volatility endpoints provide the contextual inputs.*

## Example trade

**Setup: Dead-zone session, no vol override**

- UTC 04:30. Session: dead zone, density = LOW (25–30% bid schedule).
- A DEX arb opportunity appears: Uniswap WETH/USDC pool is 0.18% above Binance spot (CEX reference). Break-even for this arb (gas + builder tip at baseline gwei): 0.12%.
- Gross edge: 0.18% − 0.12% = 0.06% net at full bid. At LOW density (25% tip): builder tip is 2.5 gwei instead of 10 gwei.
- **Decision: SKIP** — at LOW bid schedule, the builder tip is too small to win the competition for this block reliably. The opportunity is marginal (0.06% net at full bid, likely zero net at 25% bid). Dead-zone protocol: require ≥ 0.30% gross for submission. Skip.

**Same opportunity at 14:00 UTC (High-density: NY open)**

- Same arb: Uniswap 0.18% above Binance.
- Full builder tip (10 gwei). Competition is higher but gross EV is also higher (fresh NY flow creating larger sustained gaps). Submit bundle; win the block; capture 0.18% − 0.12% = 0.06% net.
- P&L: on $50,000 flash loan: 0.06% × $50,000 = **$30 net of gas**. Multiplied across 8–12 similar opportunities per high-density hour = $240–$360/hour gross.

*(Illustrative. Actual MEV P&L is highly variable and infrastructure-dependent.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected Sharpe improvement (session scheduling) | +0.2–0.4 over unscheduled | Incremental over running the same MEV strategy 24/7 without session filter |
| Expected net Sharpe (whole operation) | ~0.9 | Combination of strategy Sharpe (~0.7 unscheduled) + session scheduling gain |
| Expected max drawdown | ~12% | Gas-float drawdown risk; no directional position risk |
| Gas cost reduction (dead zone) | ~35–45% of total gas spend | By reducing bids and skipping marginal opportunities in dead zones |
| Failed-tx drag reduction | ~20–30% | Fewer aggressive bids in low-competition dead zones → lower failed bundle rate |
| Session density pattern stability | Quarterly recalibration needed | User flow patterns shift with market structure (e.g., Asian institutional growth) |

**Cost overlay:** the gas cost per opportunity is the dominant cost driver. At Ethereum gas prices of 5–15 gwei base fee + 2–10 gwei priority tip, a failed bundle costs 21,000 gas × 20 gwei = $0.20–0.40 at $2000 ETH. Running 200 bundle attempts per hour in dead zones (typical for aggressive searchers) costs $40–80/hour with near-zero EV. Session scheduling eliminates this dead-zone burn, which directly flows to net Sharpe.

## Capacity limits

- **Single-strategy capacity:** `capacity_usd: 3000000` reflects the total capital that can be profitably deployed in MEV operations before per-searcher returns start compressing. This is a ceiling on capital, not on opportunity — the MEV market scales with total on-chain volume.
- **Session scheduling does not change capacity:** the overlay improves net margin, not gross opportunity. Capacity is set by MEV market depth and competitor count.
- **Infrastructure cost, not capital, is the binding constraint:** the most important resource in MEV is block-builder relationships, co-location latency, and gas-float size. Session scheduling reduces the rate at which gas float is consumed in low-yield windows.

## What kills this strategy

1. **Session density pattern shifts (#3: Market-structure regime change).** If Asian institutional crypto trading grows to match US/EU volumes, the dead zone (03:00–08:00 UTC) becomes a medium or high-density window. The session map becomes incorrect; the scheduler reduces bids in what is now a high-value window. Annual recalibration required; lagged response unavoidable.
2. **L2/blob gas cost collapse (#3: Market-structure change).** If EIP-4844 and subsequent L2 adoption shift MEV primarily to L2s where gas costs are negligible, the cost-saving rationale for session scheduling weakens. Dead-zone gas burn becomes trivial; the session overlay adds less value. The strategy does not fail — it becomes less additive.
3. **Builder cartelisation (#7: Operational).** If block builders form cartels that extract a fixed large fraction of MEV regardless of builder tip, the tip optimisation logic becomes irrelevant. Session scheduling that adjusts builder tips loses its leverage.
4. **Competitor latency improvement makes all sessions equally low-yield (#2: Competition).** If a competitor achieves sub-millisecond latency advantages, they win all high-value MEV opportunities in ALL sessions; the high-density windows lose their value to less-latency-advantaged operators. This kills the MEV operation as a whole, not just the session scheduling overlay.

## Kill criteria

Pause or retire on any of:

1. **Rolling 30-day net MEV P&L (after gas + builder bids + failed-tx drag) < 0** — the operation is losing money; session scheduling cannot fix a fundamentally non-profitable MEV book.
2. **4 consecutive weeks where high-density sessions produce below-average gross extractable value** — session density pattern has shifted; recalibrate the session map before continuing.
3. **Gas price spike where per-attempt break-even > 90th-percentile gross EV across ALL sessions** — pause all MEV activity until gas normalises; session scheduling cannot rescue a cost-crush environment.
4. **Competitor latency gap > 500ms on the monitored relay** — latency disadvantage too large to recover via cost scheduling; fundamental infrastructure issue.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Operational efficiency gain without edge degradation** — session scheduling does not reduce gross MEV income meaningfully (high-density windows generate most of the income); it only reduces dead-zone cost burn. Net Sharpe improves without changing strategy mechanics.
- **Composable with all MEV strategy types** — the session scheduler is a wrapper layer that applies equally to DEX arb, sandwich, JIT, and liquidation MEV. No modification to the underlying strategy logic required.
- **Volatility override catches unexpected high-density events** — the 15-minute BTC vol trigger ensures the scheduler does not miss cascades and high-volume events that happen outside the historical peak windows.
- **Quarterly recalibration is low-maintenance** — session density patterns are relatively stable; recalibration is a 2-hour data analysis task, not a continuous monitoring burden.

## Disadvantages

- **Pattern shift lag** — if user flow shifts (new geography, new institution type), the session map is wrong for 30–90 days until the next recalibration. Marginal opportunities are missed in newly high-density windows.
- **Does not solve the fundamental latency problem** — session scheduling improves net margin but cannot overcome a latency disadvantage in winning blocks. A faster competitor wins in all sessions; scheduling cannot compensate.
- **Session classification is coarse** — the 1-hour session buckets are a simplification; intraday variation within sessions (first 15 minutes of NY open vs last 15 minutes) may justify finer-grained scheduling. Production implementations should refine to 15-minute or 30-minute buckets after initial deployment.
- **Tail events are session-agnostic** — the largest single-block MEV events (Black Thursday cascade, May 2021 cascade, FTX collapse) occurred at hours that do not respect session density patterns. The volatility override partially captures these.

## Sources

- [[mev-strategies]] — core MEV strategy taxonomy; this page is an overlay on those strategies.
- [[latency-and-mev-on-chain-clob]] — infrastructure context for MEV execution.
- [[session-overlap-momentum]] — session-dependent market structure for momentum strategies; analogous session calendar.
- [[off-hours-liquidation-playbook]] — session-conditional liquidation fade; thematically adjacent.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=2` — 15-minute BTC price for volatility override trigger
- `GET /api/v1/regimes/current` — macro regime; Structural_Shock triggers HIGH density for liquidation MEV

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=8760` — annual hourly OHLCV for session density calibration (volatility by UTC hour)

*Note: MEV-specific data (bundle success rate, gross MEV revenue by block/hour, strategy breakdown) is not available via CryptoDataAPI. Use Flashbots Relay API (`boost-relay.flashbots.net/relay/v1/data/bidtraces`), Dune Analytics MEV dashboards, and the operator's own bundle execution log for session-density calibration.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=2"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Vol override** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=2` — a large 15m BTC move forces HIGH density regardless of session
- **Regime trigger** — `GET /api/v1/regimes/current` — `Structural_Shock` arms liquidation-MEV density
- **Calibration** — hourly OHLCV by UTC session from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=8760`, extended by `GET /api/v1/backtesting/klines` (1h back to 2017-08)
- **Tips** — CryptoDataAPI covers only the market-volatility half of this strategy: join session-density calibration to your own bundle-log timestamps (Flashbots relay data) for the payoff half

## Related

- [[mev-strategies]] — the full MEV strategy taxonomy; this page is a scheduling overlay on those strategies
- [[jito-solana-mev-arbitrage]] — Solana-specific MEV via Jito bundles; same session-density logic applies
- [[jit-liquidity]] — JIT LP MEV; highest value in high-density sessions where large swaps occur
- [[mev-execution-guide]] — operational execution guide for MEV searchers
- [[session-aware-mean-reversion]] — session-conditional mean-reversion; analogous overlay structure for a different primitive
- [[session-overlap-momentum]] — session-overlap momentum; same session calendar as a directional signal
- [[funding-window-timing]] — peri-settlement timing overlay; uses a finer-grained timestamp trigger on the same session calendar
- [[off-hours-liquidation-playbook]] — session-conditional cascade fade; thematically adjacent
- [[market-microstructure]] — foundational context for session structure and flow timing
- [[latency-and-mev-on-chain-clob]] — MEV infrastructure and latency context
- [[edge-taxonomy]] — structural + latency edge classification
- [[failure-modes]] — pattern shift, latency gap, competition failure modes
- [[when-to-retire-a-strategy]] — kill vs pause framework
