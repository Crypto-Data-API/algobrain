---
title: "Event Vol Buying"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, volatility, derivatives, event-driven, behavioral-finance, quantitative, crypto, bitcoin, ethereum]
aliases: ["Scheduled-Event Straddle", "Catalyst IV Buying", "Event Straddle Strategy", "Pre-Catalyst Long Vol"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, informational, structural]
edge_mechanism: "Option market-makers and systematic vol sellers misprice scheduled crypto catalysts by treating upcoming protocol upgrades, regulatory decisions, halvings, and major unlocks as business-as-usual — implied vol does not step up until days to hours before the event; buying straddles when the event-date calendar is public knowledge but IV has not yet priced the catalyst captures the behavioural underreaction of the vol surface to known, dated, binary-outcome events."

data_required: [options-chain, dvol-history, realized-vol-calc, event-calendar, ohlcv-daily, implied-vol-surface]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium

expected_sharpe: 0.7
expected_max_drawdown: 0.40
breakeven_cost_bps: 80

decay_evidence: "Event vol buying in traditional markets is well-documented (earnings IV under-priced in equity options); the crypto equivalent has been studied anecdotally for Bitcoin halvings and ETF decisions. Increased institutional options market depth (Deribit, Paradigm block trades, crypto options ETFs from 2024+) has somewhat improved pricing efficiency around known events, suggesting the edge may have partially compressed relative to pre-2022 conditions. No published peer-reviewed crypto study on pre-catalyst straddle performance specifically."

kill_criteria: |
  - strategy drawdown > 35% (position-trading with wide draw tolerance; IV can reset without event occurring)
  - rolling 4-event realized P&L negative for 3 consecutive events with IV premium paid > 5 vol points each (market is pricing events correctly; the IV under-pricing edge is gone)
  - average IV expansion into event (entry IV to peak IV achieved) < 3 vol points across 5 consecutive events (no IV bid materialising; events are being priced early)
  - post-event realized move < 50% of entry ATM straddle breakeven for 4 of 5 consecutive events (events are not generating the realized vol needed to recover premium)

related: ["[[funding-conditioned-vol-selling]]", "[[crypto-options-volatility-selling]]", "[[long-straddle]]", "[[straddle-strangle]]", "[[long-volatility-strategies]]", "[[long-vol-overlay]]", "[[event-driven-trading]]", "[[unlock-aware-momentum]]", "[[unlock-short-with-crowding-gate]]", "[[macro-event-pump]]", "[[volatility-trading]]", "[[deribit]]", "[[dvol]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[bitcoin-halving]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Event Vol Buying

Event vol buying is a [[long-straddle|straddle]] or [[straddle-strangle|strangle]] strategy on BTC and ETH options (primarily on [[deribit]]) that enters long-vol positions specifically ahead of **scheduled binary-outcome catalysts** — protocol upgrades, ETF/regulatory decision dates, Bitcoin halvings, and major token unlocks — when implied volatility has not yet priced the upcoming event. The primitive edge is long vol (benefiting from realized vol exceeding implied vol or from an IV increase before expiry); the overlay is the event calendar — concentrating long-vol deployment to the pre-catalyst window where the IV surface systematically under-prices known, dated, binary-outcome events, and exiting into the event or on an IV pop rather than running the position through event-decay.

This is the **long-side, event-calendar counterpart** to [[funding-conditioned-vol-selling]] — that page sells vol when leverage-crowd demand has made IV artificially rich; this page buys vol when event-calendar under-pricing has made IV artificially cheap. The two strategies are structurally opposed in vol exposure but both exploit the same information inefficiency from different directions: the vol surface deviating from fair value.

This is differentiated from [[long-straddle]] — the general long-straddle framework covers the mechanics of the position (buying ATM call + put, delta-hedging through expiry). This page adds the **event-calendar selection filter**: it does not hold long vol generically but specifically targets the pre-event window on identified catalyst dates, with entry timing, exit discipline, and event-type selection criteria that the generic straddle page does not specify.

This is differentiated from [[long-volatility-strategies]] — that page covers the broad category of long-vol instruments and their use cases. This page is a narrow, event-specific implementation: defined catalyst types, defined entry windows, defined IV threshold for entry (IV has not yet moved), and defined exit triggers.

This is differentiated from [[unlock-aware-momentum]] (B2) — that page gates momentum entries around unlock events to avoid supply-driven headwinds. This page trades the *volatility* of the move around scheduled catalysts, not the directional momentum; the straddle profits from a large move in either direction, while unlock-aware momentum avoids being caught on the wrong side of a directional move.

This is differentiated from [[macro-event-pump]] — that page trades the directional price move anticipation around macro catalyst narratives. This page is explicitly direction-agnostic: the straddle benefits from any large realized move (or from IV expansion before the event), regardless of direction.

## Edge source

Per [[edge-taxonomy]], **behavioral + informational + structural**:

- **Behavioral (primary)** — options market-makers and systematic short-vol participants tend to under-price upcoming scheduled binary events in crypto because (a) the vol surface is primarily calibrated to recent realized vol (GARCH/historical vol anchoring) rather than event-specific forward vol, and (b) the sellers' risk models penalize the cost of maintaining elevated IV for weeks until an event that might deliver only modest realized vol. The underreaction is greatest 2–4 weeks before a known event, when the event is certain but market participants have not yet begun bidding up the term structure.
- **Informational** — the event calendar is *public knowledge*: Bitcoin halving dates are deterministic (block-height), ETF decision deadlines are published by regulators, Ethereum upgrade timelines are communicated via core developer calls months in advance. The asymmetry is that the market *knows* the date but has not yet *priced* the outcome variance. This is the crypto options equivalent of the earnings pre-announcement IV under-pricing documented in equity research (Patell & Wolfson 1979, Amin & Lee 1997).
- **Structural** — the [[variance-risk-premium]] is persistently positive in crypto options (IV > RV on average), meaning systematic vol buying is a losing strategy unconditionally. The event-calendar overlay flips the expected value locally: around binary-outcome catalyst dates, the event-specific forward vol has historically been higher than the prevailing pre-event IV implied by the vol surface — the VRP is locally negative or near-zero, making the entry viable.

## Why this edge exists

**Three specific mechanisms create the pre-event IV under-pricing:**

1. **Market-maker gamma exposure management incentivizes low pre-event IV.** Market-makers who are short gamma in short-dated options benefit from low IV (slower decay of sold options). In the 2–4 week window before a catalyst, it is in their short-term interest to maintain lower IV, since they are also sellers of near-term event vol; they only aggressively bid up the vol when the event window is imminent. This creates a window of artificially subdued IV for the buyer.

2. **Historical vol anchoring misses discrete event jumps.** Black-Scholes and GARCH-calibrated models extrapolate from recent daily returns to infer implied vol. A scheduled binary-outcome event (hard fork, SEC decision) creates a discrete jump component that is absent from the trailing daily return series. The model, anchored on recent quiet-period realized vol, systematically underestimates the event-day variance, which shows up as under-priced IV in the corresponding expiry bucket.

3. **Crowded vol sellers depress the surface before events.** Systematic [[crypto-options-volatility-selling]] strategies (covered call vaults, Ribbon/Aevo, structured product desks) supply premium year-round including before major events. Their steady selling pressure keeps IV lower than event-specific supply/demand alone would produce, creating a sustained entry window for the long-vol buyer.

**Who is on the other side:** the systematic vol seller (covered call vault, structured product desk) who does not distinguish between ordinary calendar days and days with known binary-outcome catalysts approaching on the horizon; and the market-maker who is short gamma and incentivized to keep pre-event IV subdued.

## Null hypothesis

Under the null, the event calendar carries **no incremental predictive power** over the level of IV at entry:
- Entry into a straddle 2–4 weeks before a scheduled catalyst at a given IV level should produce the same distribution of P&L as an equivalent straddle entered at the same IV level with no scheduled catalyst.
- The IV expansion into the event (pre-event IV drift) should not be systematically positive relative to average IV drift over the same time window.
- Post-event realized moves should not systematically exceed the entry straddle breakeven (IV at entry × strike × √(days/365) × 0.68).

Currently not rejected (`backtest_status: untested`). Testable prediction: for all identifiable scheduled crypto catalyst dates (halvings, SEC decision deadlines, major Ethereum upgrades), measure: (1) IV 3 weeks before the event vs 1 day before; (2) post-event realized move vs entry straddle breakeven. Predict that IV drift from 3-weeks-out to 1-day-before is systematically positive, and that post-event realized moves exceed entry breakeven on a majority of events.

## Rules

### Qualifying event types

| Event type | Rationale | Typical advance notice |
|---|---|---|
| **Bitcoin halving** | Block-height deterministic; date knowable months ahead; historically large realized volatility | 6–12 months |
| **SEC ETF decision deadline** | Published regulatory calendar; binary outcome (approve/deny); historically large IV expansion | 1–3 months |
| **Major Ethereum upgrade (hard fork)** | Core developer timeline communicated via ACD calls and EIPs; large protocol change = tail risk | 2–4 months |
| **Token TGE / major unlock** | Vesting schedule is public; binary supply shock with uncertain price direction | 1–4 weeks |
| **Regulatory hearing/vote (known date)** | Congressional hearings, MiCA deadlines, specific jurisdictional votes; directionally uncertain | 2–6 weeks |

*Do NOT enter on undated events (e.g. "market expects a spot ETF soon") — the strategy requires a specific dated catalyst to anchor the entry timing and exit.*

### Entry conditions

1. **Identified catalyst date ≥ 10 days away, ≤ 35 days away.** This window captures the pre-event IV under-pricing phase. Entering > 35 days out risks excessive time decay; entering < 10 days out risks paying into the IV spike itself.
2. **IV has not yet moved for the event.** The ATM implied vol on the expiry nearest to (and after) the catalyst date is within **10% of its trailing 30-day average DVOL** — the event has not yet been priced. If DVOL is already 20%+ above its 30-day trailing average, the under-pricing window has closed; skip entry.
3. **IV−RV spread is not negative.** Current ATM IV minus 30-day realized vol ≥ **−5 vol points**. If RV is already running materially above IV, the straddle is expensive in realized-vol terms even without the event bid; skip.
4. **No regime kill.** The current market regime from `/api/v1/regimes/current` is not `Structural_Shock` — in a systemic shock, event-specific IV pricing is overwhelmed by broad panic vol, and position management becomes unreliable.

### Instrument selection

- **ATM straddle on Deribit:** buy ATM call + ATM put on the expiry immediately after the catalyst date (or the nearest weekly/monthly expiry ≥ 3 days after the catalyst). Delta is approximately zero at entry; delta-hedge daily if desired or hold unhedged for a pure vol exposure.
- **OTM strangle alternative (cheaper, lower delta sensitivity):** buy 10-delta put + 10-delta call on the same expiry; costs less premium but requires a larger realized move to be profitable. Use for events with wide outcome uncertainty (regulatory votes) where the move could be very large in either direction.
- **Strike selection rule:** ATM straddle preferred for events with high binary certainty; OTM strangle preferred for events where the expected move is either very large (> 10% typical) or uncertain in magnitude.

### Exit conditions

1. **Pre-event IV expansion exit:** if ATM IV on the catalyst expiry rises ≥ **20 vol points** from entry — the event has been priced in; close the straddle and take the vega P&L before event theta begins compounding.
2. **Post-event realized move exit:** hold through the event if IV has not spiked pre-event; close no later than **48 hours after the catalyst** (theta decay becomes dominant once the event has passed).
3. **Maximum hold to expiry −3 days:** do not hold through final expiry weekend; gamma and theta decay become extreme.
4. **Stop loss:** position value falls to **40% of premium paid** (i.e., lose 60% of the initial option cost). Close and reassess.

### Position sizing

- **Premium outlay per event:** 1–2% of total portfolio in option premium per event straddle.
- **Maximum concurrent events:** 2 (total ≤ 4% of portfolio in option premium at any time).
- **Never size into deteriorating IV:** if IV starts rising during the entry window, do not chase — enter the planned notional or skip.

## Implementation pseudocode

```python
# event_vol_buying.py

from dataclasses import dataclass
from typing import Optional
from datetime import date, timedelta

# ---- thresholds ----
MIN_DAYS_TO_EVENT        = 10
MAX_DAYS_TO_EVENT        = 35
IV_ALREADY_MOVED_PCT     = 0.10    # if ATM IV > 1.10× 30d avg DVOL, skip entry
IV_MINUS_RV_FLOOR        = -5.0    # IV − RV must be ≥ −5 vol points
IV_EXPANSION_EXIT_VOLS   = 20.0    # close on +20 vol-point IV expansion from entry
POST_EVENT_HOLD_HOURS    = 48
PREMIUM_STOP_PCT         = 0.60    # stop if premium value falls to 40% of paid (lose 60%)
MAX_PREMIUM_PCT          = 0.02    # 2% of portfolio per event
MAX_CONCURRENT_EVENTS    = 2

@dataclass
class EventCatalyst:
    event_id:         str
    event_date:       date
    event_type:       str   # "halving", "sec_etf", "eth_upgrade", "unlock", "regulatory_vote"
    asset:            str   # "BTC", "ETH", etc.
    confirmed_dated:  bool  # event MUST have a specific date confirmed

@dataclass
class VolState:
    atm_iv_current:      float   # current ATM IV on catalyst expiry (vol points, e.g. 60 = 60%)
    dvol_30d_avg:        float   # trailing 30-day average DVOL
    realized_vol_30d:    float   # trailing 30-day realized vol (same units)

@dataclass
class StradlePosition:
    entry_premium:       float   # total premium paid per unit
    entry_iv:            float   # ATM IV at entry
    current_premium:     float
    current_iv:          float
    days_to_event:       int
    days_held:           int

def entry_qualifies(catalyst: EventCatalyst, vs: VolState, today: date,
                    regime: str, active_events: int) -> tuple[bool, str]:
    if not catalyst.confirmed_dated:
        return False, "event date not confirmed (unscheduled)"
    days = (catalyst.event_date - today).days
    if not (MIN_DAYS_TO_EVENT <= days <= MAX_DAYS_TO_EVENT):
        return False, f"days_to_event={days} outside [{MIN_DAYS_TO_EVENT}, {MAX_DAYS_TO_EVENT}]"
    if vs.atm_iv_current > vs.dvol_30d_avg * (1 + IV_ALREADY_MOVED_PCT):
        return False, (f"IV already moved: {vs.atm_iv_current:.1f} vs 30d avg "
                       f"{vs.dvol_30d_avg:.1f} (+{IV_ALREADY_MOVED_PCT*100:.0f}% threshold)")
    if (vs.atm_iv_current - vs.realized_vol_30d) < IV_MINUS_RV_FLOOR:
        return False, (f"IV−RV={vs.atm_iv_current - vs.realized_vol_30d:.1f} < floor {IV_MINUS_RV_FLOOR}")
    if regime == "Structural_Shock":
        return False, "regime kill: Structural_Shock"
    if active_events >= MAX_CONCURRENT_EVENTS:
        return False, f"max concurrent events ({MAX_CONCURRENT_EVENTS}) already active"
    return True, ""

def entry_decision(catalyst: EventCatalyst, vs: VolState, today: date,
                   regime: str, book: dict) -> dict:
    active = book.get("active_event_positions", 0)
    ok, reason = entry_qualifies(catalyst, vs, today, regime, active)
    if not ok:
        return {"action": "WAIT", "event": catalyst.event_id, "reason": reason}
    premium_budget = book["portfolio_capital"] * MAX_PREMIUM_PCT
    strike_type = ("atm_straddle" if catalyst.event_type in ("halving", "sec_etf", "eth_upgrade")
                   else "otm_strangle")
    return {
        "action":        "BUY_STRADDLE",
        "event":         catalyst.event_id,
        "event_date":    str(catalyst.event_date),
        "asset":         catalyst.asset,
        "strike_type":   strike_type,
        "premium_budget": premium_budget,
        "entry_iv":      vs.atm_iv_current,
        "dvol_30d_avg":  vs.dvol_30d_avg,
        "days_to_event": (catalyst.event_date - today).days,
        "note": f"IV {vs.atm_iv_current:.1f} vs 30d avg {vs.dvol_30d_avg:.1f} — not yet priced",
    }

def exit_decision(pos: StradlePosition) -> Optional[dict]:
    # IV expansion exit (vega profit)
    if (pos.current_iv - pos.entry_iv) >= IV_EXPANSION_EXIT_VOLS:
        return {"action": "CLOSE", "reason": f"IV expanded +{pos.current_iv - pos.entry_iv:.1f} vol pts from entry"}
    # stop loss
    if pos.current_premium < pos.entry_premium * (1 - PREMIUM_STOP_PCT):
        return {"action": "CLOSE", "reason": f"premium stop: {pos.current_premium:.4f} < 40% of {pos.entry_premium:.4f}"}
    # post-event time exit
    if pos.days_to_event < 0 and abs(pos.days_to_event) >= POST_EVENT_HOLD_HOURS // 24:
        return {"action": "CLOSE", "reason": f"48h post-event exit: theta dominant post-catalyst"}
    # near-expiry
    if pos.days_to_event <= -pos.days_held + 3 and pos.days_to_event < -3:
        return {"action": "CLOSE", "reason": "within 3 days of expiry — theta/gamma extreme"}
    return None
```

The production system adds: Deribit WebSocket feeds for live IV monitoring on the catalyst expiry bucket; a daily delta-hedge runner for ATM straddles; a P&L attribution separating delta P&L (realized move) from vega P&L (IV expansion); and a pre-event checklist that verifies the event date is still confirmed (event dates sometimes slip — e.g. ETF deadlines can be extended).

## Indicators / data used

- **ATM implied volatility (Deribit)** — the primary entry gate; requires the options chain on the Deribit API for the catalyst expiry. CryptoDataAPI does not document a verified options IV endpoint; source from [[deribit]] directly (`GET /api/v2/public/get_order_book?instrument_name=BTC-{date}-{strike}-C`) or Deribit's implied-vol history endpoint.
- **DVOL (Deribit Bitcoin/Ethereum Volatility Index)** — `/api/v1/market-intelligence/dvol-history` (CryptoDataAPI) or Deribit's `deribit_price_index` DVOL timeseries. Used for the 30-day trailing average IV level as the "not yet priced" baseline.
- **Realized vol (30-day)** — computed from daily OHLCV: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=60`. Yang-Zhang estimator or close-to-close log-return vol.
- **Event calendar** — public sources: Bitcoin block height countdown (bitcoin.clarkmoody.com), SEC EDGAR decision deadlines (public EDGAR calendar), Ethereum core developer blog (ethresear.ch, ethereum.org/en/history/). No CryptoDataAPI endpoint for event calendar; maintain a manual or scraped event log.
- **Regime classification** — `GET /api/v1/regimes/current` — blocks entry in `Structural_Shock` regime.
- **Options chain** — Deribit is the primary venue for BTC and ETH options with sufficient open interest in the relevant expiry. See [[deribit]] for API access.

*Note: Options IV data for specific expiries and strikes is not currently available via a documented CryptoDataAPI endpoint. Use Deribit API directly (as in [[funding-conditioned-vol-selling]]). DVOL history (the index-level vol) is available via CryptoDataAPI and serves as the baseline IV comparison.*

## Example trade

**Setup (illustrative — pre-halving BTC straddle):**

- Catalyst: Bitcoin halving at block 1,050,000, estimated date approximately 28 days from today.
- Current BTC price: $68,000.
- **Vol check:** ATM IV on the nearest expiry after the halving date = 52 vol points. DVOL 30-day average = 48 vol points. 52/48 = 1.08× — still within 10% of the 30-day average (below the 1.10× threshold); IV has not yet moved for the event.
- **IV−RV check:** Realized vol 30-day = 47%. IV−RV = 52 − 47 = +5 points (above the −5 floor). Entry is justified.
- **Instrument:** ATM straddle on Deribit; buy $68,000-strike call and $68,000-strike put, both for the expiry ~30 days out (halving + 2 days). Combined ATM straddle price: ~5.8% of spot = $3,944 per BTC unit.
- **Portfolio:** $100,000. Premium budget: 1.5% = $1,500. Notional exposure: $1,500 / $3,944 × $68,000 ≈ **$25,832 of BTC notional** (0.38 units of the straddle). Premium paid: ~$1,500.

**Scenario 1 — IV expansion before event (vega profit):**
- Over the next 14 days, market begins pricing the halving. ATM IV rises from 52 to 73 vol points (+21 — exceeds the 20 vol-point exit threshold).
- Close the straddle at 73 vol points. Vega gain per BTC unit: ~(73-52) vol pts × vega ≈ approximately +2.8% of notional. On $25,832 notional: **+$723 gross**.
- Net of Deribit fees (~0.03% per fill × 4 fills ≈ $31): **+$692 net on $1,500 premium = +46% return on premium deployed** / +0.69% of portfolio.

**Scenario 2 — hold through event, large realized move:**
- IV does not spike pre-event. On halving day, BTC moves +9.2% to $74,256. ATM straddle breakeven (at entry): $68,000 × 5.8% = ±$3,944 (±5.8%). Actual move +9.2% = $6,256. Move exceeds breakeven by $2,312 per BTC unit.
- On $1,500 premium (0.38 units): **+$878 gross**, minus 48h post-event exit (theta decay of ~0.5%): **+$750 net on $1,500 = +50%** / +0.75% of portfolio.

**Stop-loss scenario:** BTC stays flat; no IV expansion occurs. Straddle premium decays via theta. At 60% loss trigger: position value falls to $600 (from $1,500 entry). Close. Loss: −$900 / −0.9% of portfolio.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.7 | Low signal frequency (4–6 qualifying events per year); high variance on each event's outcome |
| Expected max drawdown | ~40% | Multiple consecutive stop-loss events possible if several catalysts disappoint; wide position-level stop (60% of premium) preserves optionality but generates sequential losses |
| Win rate (per event) | ~55–65% (rough estimate) | Pre-catalyst IV expansion is expected more often than not; post-event realized move outcome is binary |
| Average win / average loss | ~2–4× | IV expansion wins can be large (+50–100% of premium); stop losses are capped at 60% of premium — asymmetric payout |
| Breakeven cost budget | 80 bps | Options are wider bid/ask instruments; Deribit fee (0.03% per fill) × 4 fills = 12 bps in fees; the primary cost is theta decay, not commissions |
| Signal frequency | Very low | Approximately 4–8 qualifying events per year across BTC/ETH; far fewer than general long-vol strategies |

**Cost structure:** the dominant cost is theta decay (time value erosion), not transaction costs. A 28-day straddle entered 28 days before expiry will decay approximately 3–5% of its value per day in the final week. Entry 10–35 days out means roughly 30–50% of the premium will be consumed by theta if neither IV expansion nor realized move occurs. The stop at 60% of premium prevents full decay.

## Capacity limits

- **Per event:** Deribit BTC options at the $68K ATM strike have typical open interest of $200M+ in the front expiry. A $2–5M straddle entry is achievable without meaningful market impact.
- **Aggregate strategy:** `capacity_usd: 20000000` reflects the total annual premium budget, not the underlying notional. At 1–2% of portfolio per event × 5–8 events/year × $20M AUM = $200–400K total annual premium, which is well within Deribit's market depth.
- **Binding constraint:** the number of qualifying catalyst events per year (typically 4–8), not market depth. The strategy cannot be scaled by finding more events — the discipline requires specific dated binary catalysts.

## What kills this strategy

1. **Event date slippage.** If a catalyst date shifts (SEC extends review period, Ethereum upgrade delayed by a critical bug, halving block estimate moves by weeks), the pre-event positioning window changes and the existing straddle may be in the wrong expiry bucket. Pre-trade and mid-trade monitoring of event date confirmation is operationally required.
2. **Options market efficiency improving (#4: Crowding).** As more systematic long-vol players target the same catalyst dates, the pre-event IV under-pricing window compresses. The entry condition (ATM IV within 10% of 30-day trailing DVOL) would stop triggering if IV is now always 15–20% elevated before any catalyst — the market has learned to price events earlier.
3. **Event is a non-event (#2: Cost structure failure).** Scheduled catalysts sometimes produce near-zero realized vol (BTC's 2024 halving: price was largely pre-priced months ahead via ETF narratives). A sequence of well-priced-but-small-outcome events produces consecutive stop losses that can erode 30–40% of strategy equity.
4. **Deribit counterparty/regulatory risk (Operational #7).** This strategy is entirely dependent on Deribit as the crypto options venue. A Deribit operational failure, regulatory shutdown, or forced relocation mid-position is a hard risk. Diversifying to OKX options or CME BTC options reduces this, though liquidity and expiry alignment may differ.
5. **IV jump before entry window.** If the market starts pricing the event > 35 days out (the entry condition blocks entry because IV is already 15%+ above the 30-day average), the buyer misses the pre-event IV expansion entirely. The strategy has no mechanism to capture the ultra-early IV bid.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 35%** (option premium erosion on multiple consecutive events).
2. **Rolling 4-event realized P&L negative** with IV premium paid > 5 vol points per event — the "IV under-pricing" is not resolving; the market is pricing events fairly.
3. **Average IV expansion into event < 3 vol points** across 5 consecutive events — no pre-event vol bid materialising; the structural under-pricing has closed.
4. **Post-event realized move < 50% of entry straddle breakeven** for 4 of 5 consecutive events — events consistently disappoint realized vol requirements; recalibrate event type selection or minimum IV discount at entry.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Asymmetric payout profile:** unlike mean-reversion or carry strategies, long-vol entries have an asymmetric P&L — the maximum loss is the premium paid (capped), while wins can be several multiples of premium if IV expansion is large or the event move is extreme.
- **Direction-agnostic:** a straddle profits from a large move in either direction. The event calendar provides timing, not directional conviction — the strategy does not require a view on whether the catalyst is positive or negative.
- **Low ongoing maintenance:** once entered, the position requires monitoring (IV level, delta-hedge if applicable) but no active discretionary intervention unless the stop-loss or IV expansion exit is triggered.
- **Tail-risk hedge bonus:** being long vol ahead of major events provides an implicit hedge against tail scenarios not priced into the catalyst analysis. An unexpected negative surprise (exploit, hack, or harsh regulatory decision) produces a large vol spike that benefits the long-vol position.
- **Calendar-driven edge quantification:** the strategy has testable, falsifiable entry criteria. The hypothesis (pre-event IV is under-priced) can be tested on the historical record of catalyst events, providing a falsifiable foundation.

## Disadvantages

- **Very low signal frequency:** qualifying events occur roughly 4–8 times per year across BTC and ETH. The strategy is inactive during most of the year, generating no P&L while consuming account space.
- **Theta decay is the primary enemy:** long vol positions decay continuously; if the event is priced slowly or not at all, and the event itself is a non-event, the premium erodes to the stop-loss level purely via time. This requires disciplined stop-loss execution, which is psychologically difficult when the event date is still 2–3 weeks away.
- **Deribit dependency:** BTC/ETH options with sufficient liquidity for this strategy are predominantly on Deribit. Any disruption to Deribit's operations directly impairs the strategy. CME BTC options are an alternative but with higher trading costs and fewer expiry choices.
- **Event date uncertainty:** catalyst dates are not always precisely known (halving block estimates have a ±week uncertainty; SEC deadlines can be extended). Entering 10–35 days out requires a credible date estimate, which may itself be uncertain for regulatory decisions.
- **No carry income:** unlike [[funding-conditioned-vol-selling]] or [[carry-with-tail-hedge]], this strategy pays premium and receives no carry. The P&L is entirely dependent on realized vol exceeding implied vol or on a pre-event IV expansion — there is no carry buffer against a quiet period.

## Sources

- [[funding-conditioned-vol-selling]] — the structural counterpart; the same vol-surface inefficiency from the selling side, with the levy-crowd premium as the explanation for why IV deviates from fair value. This page's IV-buying logic is the long-side of the same inefficiency.
- [[long-straddle]] — the mechanics of the ATM straddle position; delta, gamma, vega, theta profiles.
- [[deribit]] — the primary execution venue; API endpoints for options chain access.
- Patell, J. M. & Wolfson, M. A. (1979) — "Anticipated information releases reflected in call option prices." *Journal of Accounting and Economics* 1(2): 117–140. Classic study on pre-earnings IV under-pricing in equity options — the conceptual analogue for crypto catalyst IV under-pricing.
- Amin, K. & Lee, C. M. C. (1997) — "Option trading, price discovery, and earnings news dissemination." *Contemporary Accounting Research* 14(2): 153–192. Further evidence on event-driven IV anomalies.
- [[variance-risk-premium]] — the VRP framework; this strategy exploits the local inversion of the VRP around catalyst events.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/dvol-history` — DVOL (Deribit Volatility Index) history for BTC and ETH; primary baseline for the "IV not yet moved" gate (compare current ATM IV to 30-day DVOL average)
- `GET /api/v1/regimes/current` — macro regime classification; blocks entry in `Structural_Shock`
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=60` — daily OHLCV for realized-vol computation

**Historical data:**
- `GET /api/v1/market-intelligence/dvol-history` — historical DVOL for backtest of the "IV not yet moved" gate across past catalyst events
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — long OHLCV history for realized-vol baseline estimation

*Note: options chain data (individual strikes, expiry-specific IV) is NOT currently documented as a CryptoDataAPI endpoint. Source directly from [[deribit]] API (`GET /api/v2/public/get_order_book`, `GET /api/v2/public/get_instruments`) or equivalent. DVOL index via CryptoDataAPI provides the macro IV baseline only; the specific straddle pricing and ATM IV for the catalyst expiry bucket must come from Deribit.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/dvol-history"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-market-data]].

**Live dashboards:** [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **IV gate** — `GET /api/v1/market-intelligence/dvol-history` — current IV vs the 30-day DVOL average: the "IV not yet moved" entry condition
- **Catalyst feed** — `GET /api/v1/event/calendar?days=30` + `GET /api/v1/event/regime/score` — candidate catalysts with directional bias to buy vol into
- **Regime gate** — `GET /api/v1/regimes/current` — no entries in `Structural_Shock` (vol has already repriced)
- **Backtest** — replay the IV gate across past catalysts with the same DVOL series; realized-vol outcomes from `GET /api/v1/backtesting/klines` (daily back to 2017-08); straddle-level pricing history stays on Deribit
- **Tips** — cheapness is relative: score IV against both the 30d DVOL average and realized vol computed from klines before paying for the straddle

## Related

- [[funding-conditioned-vol-selling]] — the structural counterpart: sells vol when leverage-crowd demand inflates IV; this page buys vol when event-calendar under-pricing deflates it
- [[long-straddle]] — the mechanics of the ATM straddle; this page adds the event-calendar entry gate
- [[straddle-strangle]] — straddle vs strangle selection; OTM strangle is the preferred instrument for wide-outcome-range events
- [[long-volatility-strategies]] — the broader long-vol category; this page is the event-targeted subset
- [[long-vol-overlay]] — long-vol as a portfolio hedge; this page is an alpha-seeking rather than hedge-oriented deployment of long vol
- [[event-driven-trading]] — the broader event-driven framework; this page applies it to vol buying rather than directional positioning
- [[unlock-aware-momentum]] — momentum gating around unlock events; this page trades vol around the same catalysts, direction-agnostically
- [[unlock-short-with-crowding-gate]] — directional supply-event short; contrast with the direction-agnostic vol approach here
- [[macro-event-pump]] — directional narrative pump trades; this page avoids a directional view entirely
- [[volatility-trading]] — the general volatility trading strategy page
- [[deribit]] — the primary options execution venue
- [[dvol]] — the DVOL index measuring crypto implied vol; used as the IV baseline
- [[implied-volatility]] — the concept underlying the entry gate
- [[variance-risk-premium]] — the VRP framework; event-calendar entry exploits local VRP inversion
- [[bitcoin-halving]] — the most well-known scheduled crypto catalyst
- [[edge-taxonomy]] — behavioral + informational + structural classification
- [[failure-modes]] — event date slippage, options market efficiency, non-event risk
- [[when-to-retire-a-strategy]] — kill vs pause framework
