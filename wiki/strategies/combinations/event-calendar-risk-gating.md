---
title: "Event Calendar Risk Gating"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, event-driven, risk-management, market-making, funding-rate, volatility, grid-trading, perpetual-futures, quantitative, crypto, methodology]
aliases: ["Event-Pause Framework", "Binary-Event Pause Protocol", "Scheduled-Event De-sizing", "Calendar-Gated Strategy Pause"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, informational]
edge_mechanism: "Passive and mechanical strategies (grids, market-making, carry books, short-vol books) assume a continuous mean-reverting or carry-harvesting regime; scheduled binary events (major unlocks, protocol upgrades, macro data releases, regulatory decisions) temporarily suspend this regime assumption and introduce non-random, directional, vol-expansion risk that these strategies are structurally ill-equipped to survive; pausing or de-sizing around the event window is not an optional enhancement — it is loss prevention against a known structural break in the strategy's operating assumptions."

data_required: [event-calendar, dvol-history, funding-rates, open-interest, ohlcv-4h]
min_capital_usd: 10000
capacity_usd: 500000000

crowding_risk: low

expected_sharpe: 0.0
expected_max_drawdown: 0.05

breakeven_cost_bps: 0

decay_evidence: "This is a risk-management protocol, not a strategy that earns alpha. The 'edge' is purely in loss prevention. The framework cannot decay; events will always exist and passive strategies will always be vulnerable to them. The specific event-type list and parameter table may need updating as new event types emerge (e.g., crypto ETF approval decisions post-2024, Federal Reserve meeting days affecting crypto via macro correlation)."

kill_criteria: |
  - Not applicable — this is a risk-management framework. It cannot be "killed" independently; it is retired only if the underlying strategy it protects is retired.
  - Review trigger: if the event-pause causes strategy capital to be idle > 15% of trading days (the event calendar is too dense), reduce the number of event types covered or narrow the pause window.

related: ["[[event-vol-buying]]", "[[regime-gated-grid]]", "[[trend-aware-carry]]", "[[carry-with-tail-hedge]]", "[[post-panic-vol-selling]]", "[[funding-conditioned-vol-selling]]", "[[oi-aware-grid]]", "[[unlock-cascade-watch]]", "[[unlock-short-with-crowding-gate]]", "[[grid-trading]]", "[[funding-rate-arbitrage]]", "[[volatility-targeting]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Event Calendar Risk Gating

Event calendar risk gating is a **risk-management framework** that systematically pauses or de-sizes **mechanical/passive strategies** — grids, market-making books, funding carry books, and short-volatility books — around scheduled binary events. These strategies generate income by operating continuously in mean-reverting or low-volatility regimes; they are structurally unprepared for the regime-break that scheduled binary events (major token unlocks, protocol upgrades and forks, macro data releases, regulatory decision dates) temporarily impose. The framework provides a generic gating structure applicable to multiple passive strategy types, with per-strategy parameter guidance.

**This page covers THREE matrix cells:**
- **Grid / market-making × unlock/event calendar** — grids and market-making books paused around events
- **Funding carry × unlock/event calendar** — carry books de-sized around events
- **Vol selling × unlock/event calendar** — short-vol books paused around events

All three share the same underlying logic (passive strategies vulnerable to binary-event regime breaks) and differ only in the parameter calibration (how far to de-size, how long to pause, which events trigger which strategy type). Rather than writing three redundant pages, this page provides the unified framework with per-strategy tables.

**This is explicitly differentiated from [[event-vol-buying]]** — that page TRADES binary events: buy vol ahead of events that will expand IV. It is an active trade on the event. This page AVOIDS events: pause passive strategies that will lose money when binary events break the mean-reversion or carry regime. The two pages are complementary: one profits from the event (long vol); the other prevents losses from the event (pause passive strategies). They are not substitutes.

**This is differentiated from [[regime-gated-grid]]** — that page pauses the grid when a vol REGIME changes (trending regime detected via ADX, Bollinger-bandwidth, or similar lagging regime indicators). The trigger is a CURRENT MARKET STATE. This page pauses the grid based on a FUTURE CALENDAR EVENT (specific date in the event calendar). The regime gate fires after the regime has changed; the calendar gate fires before the event, in anticipation of the regime change. Both are necessary: the calendar gate prevents the event-day loss; the regime gate prevents losses in sustained trend regimes between events.

**This is differentiated from [[trend-aware-carry]]** — that page scales down the carry book when a strong directional trend is running (price ≥ 15% above SMA20, RSI ≥ 70, funding ≥ 0.05%/8h). The trigger is CURRENT MOMENTUM. This page pauses the carry book around specific CALENDAR DATES regardless of the current trend state. A carry book can be running smoothly in a quiet regime and encounter a sharp binary-event-driven move; the calendar gate prevents that.

**This is differentiated from [[post-panic-vol-selling]] and [[funding-conditioned-vol-selling]]** — those pages define ENTRY conditions for the short-vol book (when to start selling). This page defines PAUSE conditions: when to STOP the short-vol book ahead of events. The pause gate is applied on top of whichever short-vol entry strategy is active; the pause overrides the entry signal during event windows regardless of whether the entry signal would otherwise qualify.

## Edge source

Per [[edge-taxonomy]], **structural + informational**:

- **Structural** — passive strategies (grids, carry, short vol) are structurally profitable in range-bound, carry-persistent, and low-vol regimes. Binary events temporarily break ALL of these assumptions simultaneously: a fork event produces non-random price discontinuity (grid ladder penetration), funding disruption (carry collapse), and IV spike (short-vol loss). The structural incompatibility between passive strategies and binary events is predictable and preventable.
- **Informational** — the event calendar is publicly available information. The edge is using it systematically as a pre-trigger for risk reduction rather than reactively closing positions after the damage has occurred. Most passive-strategy practitioners monitor their positions but do not maintain a formal event calendar that gates strategy activity; this informational gap is the source of preventable losses.

## Why this edge exists

**The regime-break problem for passive strategies:**

Three passive strategy types and their binary-event failure modes:

**Grid / market-making:**
A grid earns income by capturing the bid-ask spread and range oscillation within defined price bands. The grid assumes that prices will oscillate within the grid range — a mean-reversion assumption. A binary event (a protocol upgrade that causes a −20% price gap in 5 minutes, a regulatory decision that causes a +30% spike) violates this assumption completely: the price gaps through the grid ladder, leaving the market-maker holding inventory at the wrong price with no mechanism for recovery.

**Funding carry:**
A funding carry book earns the funding rate differential between holding spot and shorting perps (or vice versa). The assumption is that funding rates are persistent. A binary event can cause: (a) a sudden funding rate reversal (if the event is bullish, funding can spike from +0.02% to +0.10%/8h within hours, causing a large mark-to-market loss on the short-perp leg before it can be unwound); or (b) a large price move that produces a P&L loss on the perp leg that dwarfs the funding income accumulated to date.

**Short-vol / short-volatility:**
A short-vol book earns the volatility risk premium (IV > RV on average). The assumption is that realized vol will stay below IV. A binary event directly inverts this assumption: binary events produce large realized vol spikes (−20% in one session) that exceed the IV at option sale time, converting a positive expected-value position into a large realized loss. The event-vol-buying page [[event-vol-buying]] profits from exactly the same IV-underpricing dynamic that kills the short-vol book.

**The calendar-gate solution:** by pausing these passive strategies in the defined window around binary events, the strategy avoids the single-session loss that can wipe out weeks of passive income. The cost of the pause is foregone income (typically 2–5 bps per day of pause); the benefit is the loss prevention from the binary event.

## Null hypothesis

Under the null, pausing passive strategies around scheduled events **does not improve net returns** compared to running continuously:
- The paused income foregone should be larger than the losses prevented, on average.
- Binary events should not produce larger-than-expected drawdowns in passive strategies that are not gated.

This hypothesis CAN be tested:
- (a) Run a historical grid backtest over 2020–2025 on BTC with and without a calendar pause (±2 days around halvings, major ETF decision dates, major regulatory events). Compare max drawdown events and their overlap with calendar events. Predict: top-5 grid drawdown events in each year overlap with calendar events.
- (b) Run a historical short-vol backtest with and without calendar pause around Bitcoin halving dates and major FOMC releases. Predict: calender-gated version shows 20–30% lower max drawdown with minimal impact on annual Sharpe.

## Event Type Taxonomy

**Tier 1 — HARD PAUSE (full strategy halt, all strategy types):**
Major events with historically demonstrated capacity to produce ≥ 10% price moves in ≤ 24 hours:
- BTC/ETH halving events (±3 days)
- US SEC/CFTC regulatory decisions on BTC/ETH spot ETF approvals or exchange enforcement actions (±1 day of announced decision date)
- Major protocol hard forks affecting BTC, ETH, or SOL (±2 days)
- Large token cliff unlocks ≥ 10% of circulating supply (±3 days) — extremely rare; most unlocks are 3–8%

**Tier 2 — PARTIAL PAUSE (50–75% size reduction, strategy-dependent):**
Events with moderate historical impact (5–10% price moves) or uncertain binary outcomes:
- BTC halving-related technical upgrades (Taproot activation, etc.) (±2 days)
- Token cliff unlocks 4–9% of circulating supply (±2 days)
- Major US Federal Reserve FOMC meetings (±1 day) — only for strategies in BTC/ETH where macro correlation is currently active
- Ethereum major EIP implementation dates (±2 days)
- Major exchange collapses or insolvency announcements (reactive; not pre-scheduled — handled by real-time OI/funding monitoring)

**Tier 3 — MONITORING ONLY (no automatic size change; enhanced monitoring):**
Events with moderate uncertainty but lower historical impact:
- Token cliff unlocks 2–4% of circulating supply (±1 day)
- Protocol minor upgrades (non-consensus-breaking)
- CPI/PPI/NFP macro data releases (only when BTC/ETH macro correlation is elevated)
- Token TGE events for new tokens in the same sector as held positions

## Per-Strategy Parameter Table

| Strategy | Tier 1 | Tier 2 | Tier 3 | Resume Condition |
|---|---|---|---|---|
| **Grid / market-making** | Full halt ±3 days | 60% size reduction ±2 days | Enhanced monitoring | DVOL drops ≥ 15 vol pts from event peak AND price re-enters grid range |
| **Funding carry book** | Full halt ±3 days | 50% size reduction ±2 days | Enhanced monitoring | Funding rate normalises to within ±30% of pre-event level |
| **Short-vol book** | Full halt ±3 days (close short options positions) | 75% size reduction ±2 days | Enhanced monitoring | DVOL drops ≥ 20 vol pts from event peak AND new RV ≤ prior IV at sale |

**"Full halt" for a short-vol book** means: close all short options positions before the event window opens (not just pause new entries). An existing short put sold at DVOL = 60 cannot be "paused" — it is live exposure to a vol spike. The position must be closed (bought back) before the event.

**"Full halt" for a grid** means: cancel all GTC grid orders, close any grid inventory to flat (or as close as feasible), and restart the grid after the resume condition is met.

**"Full halt" for a carry book** means: unwind the short-perp leg (close the hedge), leaving only the spot long. The spot long can be maintained through the event; the perp short is the primary risk vector (large directional moves produce asymmetric P&L on the short-perp leg that is not matched by the spot long's gains in a gap-up event).

## Rules

### Step 1: Event calendar maintenance

Maintain a rolling 90-day event calendar with the following data per event:
- Event name and type (Tier 1/2/3 from the taxonomy above)
- Event date (or date range for regulatory decision windows)
- Tokens directly affected
- Historical volatility impact estimate (if available)
- Data source (tokenunlocks.app, CoinGecko events, official protocol blogs, SEC EDGAR)

Update the calendar weekly. Assign each upcoming event to a Tier based on the taxonomy.

### Step 2: Pre-event notification window

**Tier 1 (±3 days):** Fire a strategy-halt notification 3 days before the event date.
- Day T − 3 to T − 1: Begin orderly wind-down of the affected strategy:
  - Grid: cancel open orders gradually (to avoid market-impact of simultaneous cancellation)
  - Carry: close short-perp leg over T − 3 to T − 1 (3-day window to unwind)
  - Short-vol: buy back short options over T − 3 to T − 1 (prioritise largest-delta positions first)
- Day T: strategy fully halted; no open positions except residual spot longs
- Day T + 1 to T + 3: monitor for post-event normalisation

**Tier 2 (±2 days):** Fire a partial-reduction notification 2 days before the event date.
- Reduce to target size over T − 2 to T − 1 (2-day window for gradual reduction)

**Tier 3:** Enhanced monitoring only. Check OI and funding every 2 hours. If OI rises ≥ 10% or DVOL rises ≥ 10 vol pts in the 24h before the event, escalate to Tier 2 actions.

### Step 3: Resume check

After a Tier 1 or Tier 2 pause, check the resume conditions from the per-strategy table before re-deploying:
- DVOL normalisation: `GET /api/v1/market-intelligence/dvol-history`
- Funding normalisation: `GET /api/v1/derivatives/funding-rates?coin=BTC`
- Price within grid range: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=12`

Do not resume until ALL conditions for the applicable strategy type are met. Premature resumption into a still-elevated-vol environment is the most common error in event-pause management.

### Step 4: Monitoring protocol

During an active pause window (strategy halted or reduced), continue monitoring:
- DVOL every 2 hours via `GET /api/v1/market-intelligence/dvol-history`
- OI and funding every 2 hours via `GET /api/v1/derivatives/open-interest?coin=BTC` and `GET /api/v1/derivatives/funding-rates?coin=BTC`
- Liquidation spikes via `GET /api/v1/market-intelligence/liquidations`

If any of these show rapid normalisation faster than expected, consider an early resume (subject to resume conditions being met).

## Implementation pseudocode

```python
# event_calendar_risk_gating.py
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional
from enum import Enum

class EventTier(Enum):
    TIER1 = 1   # Full halt ±3 days
    TIER2 = 2   # 50-75% reduction ±2 days
    TIER3 = 3   # Monitoring only

class StrategyType(Enum):
    GRID = "grid"
    CARRY = "carry"
    SHORT_VOL = "short_vol"

@dataclass
class CalendarEvent:
    name: str
    event_date: date
    tier: EventTier
    affected_coins: list[str]

# ---- pause windows ----
PAUSE_DAYS = {EventTier.TIER1: 3, EventTier.TIER2: 2, EventTier.TIER3: 0}

# ---- size reduction during partial pause ----
SIZE_REDUCTION = {
    (StrategyType.GRID, EventTier.TIER2): 0.40,      # retain 40% (60% reduction)
    (StrategyType.CARRY, EventTier.TIER2): 0.50,     # retain 50%
    (StrategyType.SHORT_VOL, EventTier.TIER2): 0.25, # retain 25% (75% reduction)
}

# ---- resume conditions (checked post-event) ----
GRID_DVOL_DROP_MIN       = 15.0   # DVOL must drop >= 15 vol pts from event peak
CARRY_FUNDING_NORMALISE  = 0.30   # funding within 30% of pre-event level
SHORTVOL_DVOL_DROP_MIN   = 20.0   # DVOL must drop >= 20 vol pts from event peak

def days_to_event(event: CalendarEvent, today: date) -> int:
    return (event.event_date - today).days

def is_in_pause_window(event: CalendarEvent, today: date) -> bool:
    delta = abs((today - event.event_date).days)
    return delta <= PAUSE_DAYS.get(event.tier, 0)

def get_pause_action(
    strategy_type: StrategyType,
    event: CalendarEvent,
    today: date,
) -> dict:
    if not is_in_pause_window(event, today):
        return {"action": "NORMAL", "event": event.name}

    if event.tier == EventTier.TIER1:
        return {
            "action": "FULL_HALT",
            "event": event.name,
            "tier": "TIER1",
            "strategy": strategy_type.value,
            "note": (f"Tier-1 event within {PAUSE_DAYS[EventTier.TIER1]} days: "
                     f"halt {strategy_type.value} completely"),
        }
    elif event.tier == EventTier.TIER2:
        retain_pct = SIZE_REDUCTION.get((strategy_type, EventTier.TIER2), 0.50)
        return {
            "action": "PARTIAL_PAUSE",
            "event": event.name,
            "tier": "TIER2",
            "strategy": strategy_type.value,
            "retain_pct": retain_pct,
            "reduce_pct": 1 - retain_pct,
            "note": (f"Tier-2 event within {PAUSE_DAYS[EventTier.TIER2]} days: "
                     f"reduce {strategy_type.value} to {retain_pct:.0%}"),
        }
    else:
        return {"action": "MONITORING", "event": event.name, "tier": "TIER3"}

def resume_check(
    strategy_type: StrategyType,
    dvol_current: float,
    dvol_event_peak: float,
    funding_pre_event: float,
    funding_current: float,
    price_in_grid_range: bool = True,
) -> tuple[bool, str]:
    if strategy_type == StrategyType.GRID:
        dvol_ok = (dvol_event_peak - dvol_current) >= GRID_DVOL_DROP_MIN
        range_ok = price_in_grid_range
        if dvol_ok and range_ok:
            return True, "grid resume: DVOL normalised and price in range"
        return False, (f"grid hold: DVOL drop={dvol_event_peak - dvol_current:.1f} "
                       f"(need {GRID_DVOL_DROP_MIN}), in_range={range_ok}")

    elif strategy_type == StrategyType.CARRY:
        if funding_pre_event == 0:
            return True, "carry resume: no pre-event baseline"
        funding_delta_pct = abs(funding_current - funding_pre_event) / abs(funding_pre_event)
        if funding_delta_pct <= CARRY_FUNDING_NORMALISE:
            return True, f"carry resume: funding within {funding_delta_pct:.1%} of pre-event"
        return False, f"carry hold: funding deviation {funding_delta_pct:.1%} > {CARRY_FUNDING_NORMALISE:.0%}"

    elif strategy_type == StrategyType.SHORT_VOL:
        dvol_ok = (dvol_event_peak - dvol_current) >= SHORTVOL_DVOL_DROP_MIN
        if dvol_ok:
            return True, "short-vol resume: DVOL normalised"
        return False, (f"short-vol hold: DVOL drop={dvol_event_peak - dvol_current:.1f} "
                       f"(need {SHORTVOL_DVOL_DROP_MIN})")

    return False, f"unknown strategy type: {strategy_type}"
```

The production system adds: an event calendar ingestion pipeline (weekly pull from tokenunlocks.app and CoinGecko events API); a daily alert that fires when any Tier 1 or Tier 2 event is within the pause window for an active strategy; an automated position-size adjustment for Tier 2 events (gradual reduction over the T − 2 to T − 1 window); and a resume-check monitor that runs every 2 hours post-event until resume conditions are met.

## Indicators / data used

- **Event calendar** — external source (tokenunlocks.app, Coinglass unlock calendar, protocol blog posts, SEC.gov for ETF decision dates, CME economic calendar for FOMC). NOT available via CryptoDataAPI.
- **DVOL** — `GET /api/v1/market-intelligence/dvol-history`; pre-event baseline, real-time monitoring during event window, and post-event resume check for grid and short-vol.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; pre-event baseline and post-event normalisation check for carry book resume.
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; pre-event build-up monitoring and post-event normalisation.
- **Liquidations** — `GET /api/v1/market-intelligence/liquidations`; real-time cascade detection during the event window.
- **4h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=12`; grid range check for resume condition.

## Example trades (one per strategy type)

### Grid example: BTC halving (Tier 1)

- **T − 3 (April 17, 2024):** Halving detected at T − 3. BTC grid (range $60,000–$72,000, 20 grid levels) has 8 open orders. Cancel all grid orders over T − 3 to T − 1. Close any inventory positions (net long 0.12 BTC from grid imbalance, sell at market $69,800).
- **T (April 19, 2024):** Grid fully halted. Halving event occurs. BTC moves from $64,000 to $60,900 (−4.9%) and recovers to $66,500 in 24 hours. Without the halt, the grid would have experienced ladder-through risk on the −4.9% move and recovery order re-fills.
- **T + 2 (April 21):** DVOL peaked at halving (72 vol pts), now at 58 (14-point drop). Grid range check: price at $66,500 is within grid range. DVOL drop = 14 pts (< 15 pts threshold). Hold.
- **T + 4 (April 23):** DVOL at 54 (18-point drop from event peak). Price at $65,200. Resume condition met. Restart grid with new centre at $65,200.

**Cost of pause:** 4 days × avg 2 bps/day grid income = 8 bps foregone income. **Loss avoided:** the grid would have experienced a ladder-through on the $64,000 → $60,900 move, requiring $4,860 in emergency inventory management at distorted spread widths — estimated $300–$600 in grid-specific losses on a $50,000 grid notional.

### Carry example: Large token unlock (Tier 2)

- **T − 2:** SOL cliff unlock (6% of supply) in 2 days. Carry book: short SOL perp / long spot at 1.5:1 ratio. Size: $20,000 notional. Tier 2 → 50% reduction.
- **T − 1:** Reduce short-perp leg from $20,000 to $10,000 (sell $10,000 perp long, reducing the short by closing half the basis). Retain $10,000 of the perp hedge.
- **T (unlock day):** SOL declines −13%. The retained $10,000 perp short gains: $10,000 × 0.13 = +$1,300. The spot long (not reduced) loses: $20,000 × 0.13 = −$2,600. Net P&L on the reduced carry position: −$1,300 (loss).
- **Without the Tier 2 reduction:** Full $20,000 perp short + $20,000 spot long. Perp short gains $2,600; spot long loses $2,600. Net P&L = −$0 (basis trade is neutral to directional move). However: funding disruption — SOL funding spikes during the unlock to −0.15%/8h (longs panic, shorts squeezed). The short-perp leg faces a $20,000 × 0.15% × 3 × 1 day = $90 carry drag. More importantly, the perp price dislocates from spot: at the trough, the perp is trading 2% below spot (basis blowout). The $20,000 perp hedge bought back at trough shows a $400 slippage loss on the basis blowout.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | N/A | This is a risk-management framework, not a standalone alpha strategy |
| Expected max drawdown reduction | 30–50% reduction in event-driven drawdowns | The primary metric; measured against the unpaused baseline |
| Income foregone per pause | 2–5 bps/day of strategy-specific income × pause duration | For a Tier 1 ±3-day halt, cost ≈ 12–30 bps total |
| Expected annual pause days | 15–30 days | Depends on the number of Tier 1/2 events in a year (typically 4–8 BTC/ETH-relevant events) |
| Sharpe improvement on underlying strategy | Varies; estimate +0.15–0.30 Sharpe points | Loss prevention produces a more consistent equity curve |

## Capacity limits

`capacity_usd: 500000000` — there is no practical capacity limit on a risk-management framework. Any book size that deploys these passive strategies can benefit from calendar gating. The figure reflects the size of books where this framework is most relevant; very small books (< $10K) may find the operational overhead disproportionate to the benefit.

## What kills this strategy

1. **Over-gating — too many events classified as Tier 1/2.** If the event taxonomy is too broad, the strategy pauses too frequently, reducing capital utilisation substantially. The cost of foregone passive income exceeds the loss prevention benefit. Regularly review the event taxonomy to ensure only genuinely high-impact events are in Tier 1/2.
2. **Calendar data latency — event date announced less than 3 days in advance.** Some events (exchange insolvency, flash regulatory decisions) are not in any calendar with ≥3 days notice. For these reactive events, real-time OI/funding monitoring serves as the substitute early-warning system. The calendar gate cannot prevent ALL event-driven losses — only scheduled ones.
3. **Resume too early — re-deploying before vol has normalised.** The most common implementation error: seeing that the event has passed and the price has stabilised, the trader re-deploys the passive strategy while DVOL is still elevated (e.g., DVOL only dropped 10 vol pts vs the 15-vol-pt resume threshold). A second vol event in the same window (common in regulatory-decision clusters) then hits the re-deployed strategy.
4. **Event scope creep — adding macro events that don't actually affect crypto.** As macro correlation between crypto and US equities has varied significantly (high in 2022, moderate in 2024, variable in 2025+), the relevance of FOMC meetings for crypto passive strategies is inconsistent. Including FOMC as a permanent Tier 2 event adds ~8 pause days per year without consistent benefit.

## Kill criteria

This page is a risk-management protocol, not a standalone strategy. It cannot be retired independently:
- If the underlying strategy (grid, carry, or short-vol) is retired, this page's guidance no longer applies.
- **Review trigger:** if the event-pause causes capital to be idle for > 15% of trading days, reduce the event-type coverage. The framework should protect against high-impact events, not create perpetual stand-down.

See [[when-to-retire-a-strategy]] and [[failure-modes]] for the broader framework.

## Advantages

- **Prevents the single-session loss that wipes weeks of passive income.** Grid strategies, carry books, and short-vol books earn 2–5 bps per day. A single binary-event loss can wipe 30–60 days of income in a 4-hour window. A 6-day halt (3 days before + 3 days after) that prevents this loss costs 12–30 bps (3–6 days of income) against saving 60–180 bps of potential loss. The expected value of the halt is strongly positive.
- **Does not require prediction of event outcomes.** The framework is not a bet on whether the halving will be bullish or bearish, whether the upgrade will succeed, or whether the regulatory decision will be positive or negative. It simply removes the passive strategy's exposure to the binary outcome. Uncertainty about the event direction is irrelevant.
- **Unified framework across multiple strategy types.** Rather than developing independent event-awareness protocols for each passive strategy, this framework provides a common event taxonomy and per-strategy parameter table. Practitioners running multiple passive strategies can maintain a single event calendar.
- **Complementary to all active combination strategies.** Active combination strategies (e.g., [[event-vol-buying]], [[unlock-short-with-crowding-gate]]) TRADE binary events. This page ensures the passive strategies that run alongside active strategies are not accidentally exposed to the same events. The two frameworks (trade the event, protect the passive book) operate independently on the same calendar.

## Disadvantages

- **Requires ongoing event calendar maintenance.** The framework is only as good as the event calendar. Outdated or incomplete calendar data (missed unlock dates, incorrect protocol upgrade dates) create gaps in coverage.
- **Carry book unwind costs are material in large positions.** Closing and re-opening a large short-perp position for a Tier 1 halt generates transaction costs (taker fees × 2 fills + bid-ask crossing) that can be significant. At 10 bps round trip on a $500,000 carry position, each halt-and-resume cycle costs $500 in transaction costs.
- **No protection against unscheduled events.** The calendar gate explicitly covers SCHEDULED events. Unscheduled events (exchange hacks, protocol emergency halts, flash news) are not covered and require real-time monitoring ([[leverage-stress-tail-hedge]], [[oi-aware-grid]]) as a separate layer.
- **Grid income foregone during halt is a permanent cost.** Unlike a stop-loss (which can re-enter after conditions normalise), the halt foregoes income that cannot be "made back." In a year with many Tier 1 events, the cumulative pause cost can reduce annual grid income by 3–8%.

## Sources

- [[event-vol-buying]] — the active-trading complement: buys vol ahead of binary events that this page pauses around. Together these two pages define the complete event-handling protocol for a crypto trading book: protect the passive strategies (this page), and monetise the vol expansion (that page).
- [[regime-gated-grid]] — the regime-based grid halt (lagging vol-regime indicator); this page adds the forward-looking calendar-based halt as a complementary layer.
- [[trend-aware-carry]] — the trend-based carry reduction; this page adds the event-calendar-based carry halt.
- [[oi-aware-grid]] — the OI-build-based grid halt; this page adds the calendar-based halt on top.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/dvol-history` — DVOL monitoring during event window; resume-condition check for grid and short-vol
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding monitoring during event window; resume-condition check for carry book
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI monitoring during event window; pre-event build-up detection
- `GET /api/v1/market-intelligence/liquidations` — real-time cascade detection during event window
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=12` — price-range check for grid resume condition

*Note: the event calendar itself (unlock dates, upgrade dates, regulatory decision dates) is not available via CryptoDataAPI. Source from tokenunlocks.app (unlock calendar), official protocol governance posts (upgrade dates), and regulatory filing dates (SEC EDGAR for US regulatory decisions).*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/dvol-history"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Monitor set** — `GET /api/v1/market-intelligence/dvol-history`, `GET /api/v1/derivatives/funding-rates?coin=BTC`, `GET /api/v1/derivatives/open-interest?coin=BTC` — the resume-condition dashboard during each event window
- **Cascade check** — `GET /api/v1/market-intelligence/liquidations` — real-time forced-flow detection while the book is gated down
- **Event feed** — `GET /api/v1/event/calendar?type=unlock&days=30` + `GET /api/v1/event/regime/score` — a native forward catalyst calendar (unlocks, macro prints, depeg risk) to cross-check the external calendar sources noted above
- **Backtest** — gate-window P&L replay from `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08); `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) preserves what the derivatives/vol dashboard actually showed on each historical date
- **Tips** — this overlay's failure mode is resuming too early: encode resume conditions as explicit data checks (DVOL back under threshold, funding normalised, price range held) and let the agent enforce the full waiting period

## Related

- [[event-vol-buying]] — the active-trading complement: buy vol when this page pauses passive strategies
- [[regime-gated-grid]] — regime-based grid halt (lagging indicator); this page adds the calendar-based (forward-looking) halt layer
- [[trend-aware-carry]] — trend-based carry reduction; this page adds the calendar-based halt layer
- [[carry-with-tail-hedge]] — permanent tail-hedge on the carry book; this page's halt prevents the event-day loss that the tail hedge is designed to monetise
- [[post-panic-vol-selling]] — short-vol entry after panic; this page ensures the short-vol book is not live during the event that creates the panic
- [[funding-conditioned-vol-selling]] — short-vol entry conditions; this page overrides the entry condition during event windows
- [[oi-aware-grid]] — OI-build grid halt; composable with this page (OI gate fires before events; calendar gate fires predictably on known dates)
- [[unlock-cascade-watch]] — unlock event risk management for directional positions; this page handles the PASSIVE strategy protection, that page handles directional position de-risking
- [[unlock-short-with-crowding-gate]] — the active unlock trade; this page manages passive strategy protection around the same events
- [[grid-trading]] — the canonical grid/market-making primitive
- [[funding-rate-arbitrage]] — the canonical funding carry primitive
- [[volatility-targeting]] — the vol-scaling framework; complements this page by sizing passive strategies by vol between events
- [[failure-modes]] — binary-event regime breaks, calendar maintenance failure, early resumption
- [[when-to-retire-a-strategy]] — kill vs pause framework
