---
title: "Options Relative-Value × Event Calendar"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options-structures, derivatives, volatility, event-driven, term-structure, crypto, deribit, quantitative]
aliases: ["Options RV Event Calendar", "Term-Structure Event Positioning", "Calendar Event Vol-of-Vol Premium", "Event-Anchored Options RV"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, behavioral]
edge_mechanism: "Scheduled high-vol events (halvings, ETF/regulatory decisions, FOMC, major protocol upgrades) predictably compress forward implied volatility in the near-dated expiry: market makers build a 'vol-of-vol premium' into the near-term implied vol surface, creating a systematic richness in front-month vs back-month IV ratio (term-structure steepening into the event). The event-calendar overlay selects WHEN to enter term-structure mean-reversion trades — buying back-dated IV vs selling near-dated IV into events (collecting the term-structure richness), and flattening or reversing after event resolution. The counterparty is the systematic vol seller who has no event awareness, or the retail hedger who buys near-dated options at peak event premium without fading the post-event IV collapse."

data_required: [deribit-options-chain, dvol-btc, dvol-eth, implied-vol-by-expiry, event-calendar, realized-vol-30d, skew-rr25, term-structure-slope]
min_capital_usd: 25000
capacity_usd: 30000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.25
breakeven_cost_bps: 35

decay_evidence: "The event-vol richness in near-dated crypto options is well-documented qualitatively but no peer-reviewed study has quantified it for crypto options specifically. The BTC halving vol premium (IV spike into halving, collapse post-event) is observable in historical Deribit data (April 2024 halving: DVOL peaked at ~85 ahead of the event, fell to ~50 post-event; March 2020 halving: similar pattern). The pattern is durable because retail hedgers systematically overpay for near-dated event insurance; the post-event IV collapse is nearly mechanical as the event uncertainty resolves. Compression risk: as institutional options market-makers become more sophisticated, the pre-event richness may partially normalise."

kill_criteria: |
  - rolling 6-month net Sharpe < 0 on all event-calendar options RV trades combined
  - 3 consecutive major events (halving, ETF decision, FOMC) where near-dated IV does NOT spike into the event relative to the back-dated expiry (event-vol premium has normalised; counterparty sophistication has increased)
  - Deribit options liquidity in the target expiries below minimum threshold (bid-ask spread > 3 vol pts on the near expiry) — execution costs exceed the term-structure dislocation
  - Maximum loss on any single event trade exceeds 12% of the options sleeve (position sizing failure; reassess)

related: ["[[calendar-spread-arbitrage]]", "[[skew-trading]]", "[[crypto-options-dispersion]]", "[[event-vol-buying]]", "[[event-calendar-risk-gating]]", "[[post-panic-vol-selling]]", "[[complacency-vol-buying]]", "[[long-options-trend-expression]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[term-structure]]", "[[deribit]]", "[[dvol]]", "[[variance-risk-premium]]", "[[options-greeks]]", "[[vega]]", "[[theta]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Options Relative-Value × Event Calendar

Options relative-value event calendar positions the **term structure of implied volatility** around scheduled high-impact events — Bitcoin halvings, ETF approval/rejection decisions, FOMC meetings during macro-crypto correlation periods, and major Ethereum hard forks. It exploits the systematic richness in near-dated implied volatility that builds into known catalysts (market participants and retail hedgers bid up near-expiry options, steepening the IV term structure) by buying the back-dated expiry (cheap, calm IV) against selling the near-dated expiry (rich, event-premium IV), collecting the convergence as the event resolves and the near-dated IV collapses back toward the back-dated level. The counterparty is the event-insurance buyer: retail traders and systematic vol sellers who buy near-dated hedges at event-premium prices without a corresponding position in the back-dated expiry.

**This is differentiated from [[calendar-spread-arbitrage]]** — that page trades the futures/perp dated-basis term structure (long near-dated futures, short far-dated, or vice versa), capturing financing-rate dislocations in the futures curve. This page trades the options IMPLIED VOLATILITY term structure — near-dated IV vs back-dated IV — using calendar spreads in options, not futures. Distinct instrument, distinct mechanism: the futures spread captures carry; this page captures event-premium richness in the vol surface.

**This is differentiated from [[event-vol-buying]]** — that page buys ATM straddles or OTM strangles ahead of events to profit from the IV spike. This page sells near-dated IV and buys back-dated IV — it profits from the POST-EVENT IV collapse, not from the IV spike itself. The two pages are timed inversely: event-vol-buying profits from the vol spike into the event; this page profits from the mean-reversion of the term structure after the event. The two strategies are not directly competing; they can be run sequentially (buy straddle ahead of event; roll to calendar spread just before event for the post-event collapse trade).

**This is differentiated from [[post-panic-vol-selling]]** — that page sells outright vega (net short options) after a fear extreme stabilises. This page is a vol-surface relative-value trade (long back-dated vega, short near-dated vega); the net vega is near-zero or slightly long (the calendar spread). Not a directional vol short.

**This is differentiated from [[event-calendar-risk-gating]]** — that page PAUSES passive mechanical strategies (grids, carry books, vol selling) around events to avoid being caught by the event's directionality. This page ACTIVELY TRADES the event premium in the vol surface. The event calendar is the source of edge here, not a risk to avoid.

## Edge source

Per [[edge-taxonomy]], **structural + behavioral**:

- **Structural (primary)** — The options term structure in crypto has a systematic event-premium pattern: near-dated IV expiry dates that bracket a known high-vol event carry a predictable richness relative to the back-dated expiry whose DTE extends through and beyond the event. After the event resolves, the near-dated IV snaps back toward the (calmer) back-dated level — a mechanical convergence driven by the removal of event uncertainty from the near expiry.
- **Behavioral** — Retail hedgers and event-driven options buyers systematically overpay for near-dated options immediately before high-profile events. The "must hedge before the halving / ETF decision" framing drives demand for near-dated instruments without a corresponding analysis of relative value vs. the back-dated expiry. This behavioral overpayment is the richness that the calendar spread harvests.

## Why this edge exists

**The event-premium mechanism:**

1. **Pre-event buildup (T − 14 to T − 2 days):** the market begins pricing the event's binary uncertainty into the near-dated expiry (the one closest to the event date). Front-month IV rises, back-month IV stays relatively stable. Term structure steepens: near-dated IV − back-dated IV spreads widen from the typical flat/mild-contango shape to an inverted or steep-contango shape depending on event direction.

2. **Event resolution (T + 0 to T + 1 days):** the binary uncertainty resolves (halving happens; ETF is approved or rejected). Near-dated IV collapses sharply as the uncertainty is removed — a mechanical mean-reversion of the term structure back toward its typical shape.

3. **Post-event normalisation (T + 1 to T + 5 days):** the IV spread between near and back-dated returns to baseline. The calendar spread (long back-dated, short near-dated) profits from this convergence.

**The structural argument for persistence:** crypto options market makers consistently build the event premium into near-dated expiries because they face real delta-hedging uncertainty around the event; they mark up near-dated IV to compensate. This markup is not arbitraged away by pure vol sellers (who go net short vega — they cannot fully exploit the near-vs-back dislocation without delta risk). The calendar spread structure (market-neutral to the event direction, long back-dated, short near-dated) is the cleanest way to harvest this premium.

**Who is on the other side:** the retail options buyer who purchases a 2-week BTC put/call immediately before a halving at 85 DVOL, and a systematic vol seller who continuously sells near-dated options without regard for calendar structure (they are short the same near-dated premium the calendar spread is also short — but without the back-dated long that neutralises the event-direction risk).

## Null hypothesis

Under the null, crypto implied volatility exhibits **no systematic event-premium pattern** in the near-dated expiry: the IV spread between near-dated and back-dated expiries does not widen predictably ahead of halvings, ETF decisions, or FOMC during correlation periods. If the null holds:

- Average (near-dated IV − back-dated IV) T − 14 to T − 2 days before major events should not differ significantly from the same metric during non-event periods.
- Calendar spreads entered 7–14 days before events should not show systematically positive realised P&L relative to calendar spreads entered during random non-event windows.

Testable using Deribit historical options chain data (via `api.deribit.com/api/v2/public/get_historical_volatility` and the options chain history): compare T − 14 to T − 2 term-structure slope (near-month IV / back-month IV) around halving dates (May 2020, April 2024), ETF decision dates (Jan 2024, May 2024), and FOMC dates with elevated BTC-SPX correlation vs non-event periods.

Currently not rejected (untested on this exact structure). The directional evidence (DVOL peaked ~85 pre-halving April 2024 and fell to ~50 post-halving) supports the hypothesis.

## Rules

### Event calendar and entry schedule

**Tier 1 events (largest expected vol premium, enter T − 14 days before):**
- BTC halvings
- SEC ETF approval / rejection binary decisions
- Ethereum major hard forks (EIP with consensus changes)

**Tier 2 events (moderate expected vol premium, enter T − 7 days before):**
- FOMC meetings when 30d BTC-SPX correlation ≥ 0.65
- Crypto regulatory decisions (DOJ enforcement, CFTC category decisions)
- Major protocol upgrade activations (Ethereum PoS merge-equivalent scale)

**Tier 3 events (minor vol premium, enter T − 3 to T − 5 days before):**
- Large token unlocks (≥ 5% of supply) on top-10 assets
- CME BTC/ETH options expiry (last Friday of month — creates near-dated gamma demand)
- Macro data releases (CPI, NFP) when BTC-SPX correlation ≥ 0.70

### Entry structure

**Pre-event entry (collect the term-structure richness):**
- **Leg A (long):** Buy the back-dated call/put (matching delta-hedge) at DTE 45–60 days, bracketing through and beyond the event date.
- **Leg B (short):** Sell the near-dated call/put at DTE 14–21 days, expiring 5–7 days AFTER the event date (captures the full event premium; expires while event uncertainty remains priced in, then rapidly decays post-event).
- **Delta neutrality:** immediately delta-hedge the net delta of the combined calendar position using the perpetual future (BTC/ETH perp on Deribit). Recalculate delta daily.
- **Strike selection:** at-the-money (ATM) for both legs; for put calendars (bearish event bias — ETF rejection, regulatory concern) bias toward 5% OTM puts on the near leg.

### Exit structure

- **Primary exit (T + 1 to T + 3 days post-event):** close the calendar spread as soon as near-dated IV normalises toward the back-dated IV level (IV spread collapses from event-premium level to baseline ± 2 vol pts). Typically achievable within 48–72 hours post-event.
- **Maximum hold:** close the entire position no later than T + 5 days (residual time-decay risk from the short near-dated leg dominates at this point).
- **Stop loss:** close if the near-dated IV spikes a further 20+ vol pts above the entry level (event outcome is more extreme than expected; the long back-dated leg partially hedges but vega loss on the position as a whole may be material). Stop at −10% of options sleeve.

### Position sizing

- Options sleeve: 5–12% of portfolio notional per Tier 1 event; 3–7% for Tier 2; 1–3% for Tier 3.
- Maximum concurrent event positions: 2 (events should not overlap in the same instrument). If two events bracket the same DTE expiry, wait for the first to resolve before entering the second.
- Maximum total options sleeve: 20% of portfolio.

## Implementation pseudocode

```python
# options_rv_event_calendar.py
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

@dataclass
class EventCalendarEntry:
    event_name:     str
    event_date:     date
    tier:           int       # 1, 2, or 3
    asset:          str       # "BTC" or "ETH"

@dataclass
class CalendarSpreadPosition:
    entry_date:           date
    event_date:           date
    asset:                str
    near_expiry:          date    # DTE 14–21d from entry
    back_expiry:          date    # DTE 45–60d from entry
    near_iv_at_entry:     float   # vol pts
    back_iv_at_entry:     float   # vol pts
    iv_spread_at_entry:   float   # near - back (should be positive = near is rich)
    delta_hedge_qty:      float   # perp units to hedge net delta
    notional_usd:         float
    options_type:         str     # "call" or "put"

TIER_ENTRY_DAYS_BEFORE = {1: 14, 2: 7, 3: 4}
TIER_SLEEVE_FRACTION   = {1: 0.08, 2: 0.05, 3: 0.02}
IV_SPREAD_MIN_ENTRY    = 5.0   # minimum near-back IV spread (vol pts) to justify trade
IV_SPREAD_EXIT_TARGET  = 2.0   # exit when spread compresses to near-baseline
MAX_HOLD_DAYS_POST_EVT = 5
STOP_LOSS_VOL_SPIKE    = 20.0  # close if near-dated IV spikes +20 vol pts from entry

def should_enter(event: EventCalendarEntry, today: date,
                 near_iv: float, back_iv: float) -> Optional[dict]:
    days_to_event = (event.event_date - today).days
    entry_window = TIER_ENTRY_DAYS_BEFORE[event.tier]
    if not (entry_window - 2 <= days_to_event <= entry_window + 1):
        return None  # not in entry window
    iv_spread = near_iv - back_iv
    if iv_spread < IV_SPREAD_MIN_ENTRY:
        return None  # insufficient term-structure richness; no trade
    return {
        "action":       "ENTER_CALENDAR_SPREAD",
        "near_expiry":  today + timedelta(days=days_to_event + 7),
        "back_expiry":  today + timedelta(days=55),
        "iv_spread":    iv_spread,
        "near_iv":      near_iv,
        "back_iv":      back_iv,
    }

def should_exit(pos: CalendarSpreadPosition, today: date,
                near_iv: float, back_iv: float) -> Optional[str]:
    days_post_event = (today - pos.event_date).days
    current_spread = near_iv - back_iv
    # Primary exit: IV spread converged to baseline
    if days_post_event >= 1 and current_spread <= IV_SPREAD_EXIT_TARGET:
        return f"IV_SPREAD_CONVERGED: spread {current_spread:.1f} <= {IV_SPREAD_EXIT_TARGET}"
    # Time exit: maximum hold
    if days_post_event >= MAX_HOLD_DAYS_POST_EVT:
        return f"TIME_EXIT: {days_post_event}d post-event"
    # Stop loss: near-dated IV spiked further
    if near_iv - pos.near_iv_at_entry >= STOP_LOSS_VOL_SPIKE:
        return (f"STOP_LOSS: near IV {near_iv:.1f} vs entry {pos.near_iv_at_entry:.1f}, "
                f"+{near_iv - pos.near_iv_at_entry:.1f} vol pts")
    return None
```

The production system polls Deribit's options chain every 30 minutes to update near and back-dated IV estimates; the delta hedge is recalculated on the same interval and re-executed via the Deribit BTC perpetual when net delta moves > 0.10.

## Indicators / data used

- **Deribit IV by expiry** — Deribit API: `GET /api/v2/public/get_historical_volatility?currency=BTC` (historical) and options chain for per-expiry IV; primary input for term-structure measurement. *Not in CryptoDataAPI — sourced directly from Deribit API.*
- **DVOL (BTC/ETH 30-day IV index)** — `GET /api/v1/volatility/dvol?coin=BTC`; context metric to assess whether the overall vol surface is elevated pre-event.
- **BTC-SPX 30-day correlation** — `GET /api/v1/volatility/correlation?assets=BTC,SPX&days=30` (if available) or computed from daily OHLCV; Tier 2 gate for FOMC events.
- **Event calendar** — maintained manually by the operator; key dates: halving (block-height countdown), ETF decision (SEC calendar), FOMC meeting dates (Federal Reserve calendar), major token unlock schedules (Messari, TokenUnlocks).
- **Realized vol** — `GET /api/v1/volatility/realized?coin=BTC&days=30`; secondary context for assessing whether the pre-event DVOL spike is justified or excessive.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; used to assess cost of delta hedging via perp (high funding = expensive delta hedge in one direction).

## Example trade

**Setup: BTC halving (Tier 1 event, T − 14 entry)**

*Illustrative numbers based on April 2024 BTC halving pattern.*

- T − 14: April 6, 2024. Halving expected April 20, 2024 (block ~840,000).
- Near-dated IV (April 26 expiry, DTE 20): **DVOL proxy = 72 vol pts.**
- Back-dated IV (May 31 expiry, DTE 55): **58 vol pts.**
- IV spread: 72 − 58 = **14 vol pts** (well above the 5-vol-pt minimum).
- Entry: buy May 31 ATM call ($70,000 strike at spot $70,500); sell April 26 ATM call ($70,000 strike). Portfolio $200,000; Tier 1 sleeve = 8% = $16,000 notional.
- Delta-hedge: net delta of calendar spread ≈ +0.08 (back-dated call delta > near-dated call delta at same strike). Sell 0.08 BTC perp to neutralise.

*T + 2 (April 22, 2024 — 2 days post-halving):*
- Near-dated IV (April 26): **48 vol pts** (collapsed post-halving; event uncertainty resolved).
- Back-dated IV (May 31): **55 vol pts** (slight decline; broader sentiment normalised but not collapsed).
- IV spread: 48 − 55 = **−7 vol pts** (spread has converged and flipped; near is now CHEAP vs back).
- **Exit triggered:** IV spread ≤ 2 vol pt target (it is actually negative = over-converged). Close calendar spread.
- P&L: sold near-dated call at 72 vol pts entry; close-buy at 48 → +24 vol pts × vega(near). Bought back-dated call at 58 vol pts; close-sell at 55 → −3 vol pts × vega(back). Net options P&L (illustrative): on $16,000 notional ≈ **+$1,920** (12% of sleeve, 0.96% of portfolio). Delta hedge P&L depends on BTC move (approx. flat if BTC returned to near-entry level).

*(Illustrative. April 2024 BTC halving did produce a DVOL spike and post-event collapse consistent with this setup. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Event-calendar structure provides selectivity; limited to ~4–8 major events/year |
| Expected max drawdown | ~25% | From a severe event with unexpected outcome (ETF rejection when position structured for approval) |
| Win rate (per trade) | ~60–70% (estimated) | Pre-event IV richness is systematic but not certain; some events do not produce the anticipated term-structure steepening |
| Average hold duration | 5–21 days | From entry to post-event IV normalisation |
| Breakeven cost | 35 bps | Deribit maker fees on both legs + delta-hedge perp cost (mark to market on each hedge rebalance) |
| Trades per year | 4–10 | Tier 1: ~2/year (halvings every 4 years + ETF decisions); Tier 2: 4–8 additional events |

**Cost overlay:** Deribit options maker fee is 0.03% of underlying per contract. For a $16K notional position, round-trip options cost ≈ 0.06% × $16K × 2 legs = $19. Delta-hedge perp cost ≈ 2–5 bps per rebalance × 3–5 rebalances = $24–$48 total. Total cost per trade ≈ $43–$67 on a $16K position = 0.3–0.4% = well within the 35 bps breakeven on the typical 12–24 vol-pt convergence.

## Capacity limits

- **Per trade:** `capacity_usd: 30000000` reflects Deribit ATM options depth; above $5M per expiry, the position moves the market. Practical per-trade sizing is $500K–$2M for a solo operator.
- **Strategy-level:** event frequency limits total capital deployment; 4–10 trades/year × $500K–$2M per trade = $2M–$20M annual deployment capacity.
- **Market structure:** as more participants target the same event-vol premium, the pre-event IV richness may compress. Currently a limited-capacity strategy.

## What kills this strategy

1. **Event outcome is more extreme than the vol surface anticipated (#3: Market-structure change).** An ETF is rejected on unprecedented legal grounds or a halving triggers an extreme price move; near-dated IV spikes a further 30–40 vol pts rather than collapsing. The long back-dated leg partially offsets the loss, but the stop-loss condition fires. Manageable with position sizing (< 12% sleeve per trade) but not avoidable.
2. **Events become perfectly anticipated and the term-structure premium normalises (#3: Market-structure change).** If institutional vol market-makers stop marking up near-dated expiries before halvings (because every event "doesn't move the market"), the IV spread at entry narrows below the 5-vol-pt minimum and no trade is generated. The strategy goes idle.
3. **Deribit liquidity thin in target expiries (#7: Operational).** Options market depth is concentrated in the nearest weekly/monthly expiry. Calendar spreads using non-standard expiry dates (e.g., 7 days post-halving) may face bid-ask spreads of 3–5 vol pts, erasing the spread edge.
4. **Delta hedge cost in high-funding environment (#7: Operational).** If perp funding is extremely elevated (> 0.08%/8h), delta-hedging the net delta via perp is expensive; the carry cost of the hedge over 5–14 days can exceed the vol-surface P&L. Enter calendar spreads in elevated-funding environments only when IV spread > 10 vol pts.

## Kill criteria

Pause or retire on any of:

1. **Rolling 6-month net Sharpe < 0** on all event-calendar options RV trades.
2. **3 consecutive major events where near-dated IV does NOT spike ≥ 5 vol pts above back-dated IV** — event-vol premium has normalised; the edge has degraded.
3. **Deribit bid-ask spread in target expiry > 3 vol pts** — execution costs exceed the typical IV spread; strategy is not executable at a profit.
4. **Single event trade loss > 12% of options sleeve** — position sizing discipline failure; reassess entry criteria.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Structural event-calendar selectivity** — the event calendar provides a clear, advance-known schedule for when to be active. No continuous monitoring required between events; the strategy is idle (capital in AAVE or stablecoin yield) between trades.
- **Near-market-neutral to event outcome** — the calendar spread's net vega is small (positive); the delta is continuously hedged. The position profits from vol-surface convergence, not from correctly predicting event direction.
- **High conviction per trade** — the IV spread (near-dated richness) is a directly observable and quantifiable entry criterion. Trades are only taken when the quantitative threshold is met (≥ 5 vol pts IV spread).
- **Complementary to [[event-vol-buying]]** — event-vol-buying profits from the pre-event IV spike; this page profits from the post-event IV collapse. The two strategies can be run in sequence on the same event.

## Disadvantages

- **Very low frequency** — 4–10 trades per year. Capital must be efficiently deployed in alternative uses (stablecoin yield) between events; strategy cannot be the sole income source.
- **Deribit concentration risk** — BTC/ETH options on Deribit are the only liquid crypto options market at scale. Any Deribit operational failure (exchange halt, margin call cascade) directly impacts this strategy. No liquid alternative venue exists for BTC/ETH options calendar spreads.
- **Delta hedge rebalancing friction** — vega P&L depends on IV movement but the daily delta hedge rebalancing creates ongoing perp trading costs. In low-vol post-event windows, the delta hedge churn is small but non-zero.
- **Event outcome tail risk** — extreme event outcomes (unexpected regulatory shock, technical failure at halving) can cause near-dated IV to spike further rather than collapse, generating losses despite the calendar spread structure. The long back-dated leg partially offsets but does not fully cancel the loss.

## Sources

- [[calendar-spread-arbitrage]] — the futures term-structure analog; this page is the options-IV analog
- [[event-vol-buying]] — the complementary strategy (pre-event vol buying); differentiated as the entry half vs this page's exit/collapse half
- [[skew-trading]] — adjacent options RV strategy; same Deribit infrastructure, different surface dimension
- [[event-calendar-risk-gating]] — the inverse strategy (pausing passive books around events); contrasts with this page (actively trading the event premium)
- [[implied-volatility]] — foundational concept for understanding IV term structure

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/dvol?coin=BTC` — DVOL 30-day index; context for overall vol level pre-event
- `GET /api/v1/volatility/dvol?coin=ETH` — ETH DVOL for ETH event trades
- `GET /api/v1/volatility/realized?coin=BTC&days=30` — realised vol comparison to assess DVOL richness
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — delta-hedge cost check (elevated funding = expensive perp hedge)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30` — recent daily OHLCV for BTC-SPX correlation computation

**Historical data:**
- `GET /api/v1/volatility/dvol?coin=BTC&historical=true&days=730` — 2-year DVOL history for event-vol-premium backtesting

*Note: per-expiry Deribit implied volatility (the core input for the calendar spread entry and exit) is NOT available via CryptoDataAPI. Access Deribit's public API directly: `GET https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option` for live options chain, and `GET https://www.deribit.com/api/v2/public/get_historical_volatility?currency=BTC` for historical DVOL. The Deribit API is public (no auth required for read-only endpoints).*

```bash
# CryptoDataAPI for context metrics:
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/volatility/dvol?coin=BTC"

# Deribit for per-expiry IV (no auth needed):
curl "https://www.deribit.com/api/v2/public/get_historical_volatility?currency=BTC"
```

Auth: CryptoDataAPI requires `X-API-Key` header. Deribit public endpoints require no auth. Full endpoint catalog: [[cryptodataapi-volatility]], [[cryptodataapi-market-data]].

## Related

- [[calendar-spread-arbitrage]] — futures term-structure analog; same calendar overlay, different instrument
- [[skew-trading]] — adjacent options RV on vol surface skew dimension; same Deribit infrastructure
- [[crypto-options-dispersion]] — cross-asset IV dispersion; another options RV trade
- [[event-vol-buying]] — buys straddles ahead of events (pre-event IV spike); this page harvests post-event IV collapse; sequential use on same event
- [[event-calendar-risk-gating]] — the inverse: pauses passive books around events instead of trading them
- [[post-panic-vol-selling]] — directional vol short after panic; differentiated as directional vs this page's surface-neutral calendar structure
- [[complacency-vol-buying]] — sentiment-driven vol buying; differentiated from event-calendar timing
- [[long-options-trend-expression]] — trend-gated long vol; differentiated as directional trend-expression vs this page's event-anchored surface RV
- [[implied-volatility]] — IV foundational concept
- [[volatility-surface]] — vol surface geometry context
- [[term-structure]] — term-structure concept
- [[deribit]] — the primary execution venue
- [[edge-taxonomy]] — structural + behavioral edge classification
- [[failure-modes]] — event tail risk, liquidity concentration, delta-hedge friction
- [[when-to-retire-a-strategy]] — kill vs pause framework
