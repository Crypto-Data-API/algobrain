---
title: "Post-Panic Vol Selling"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, volatility, derivatives, behavioral-finance, sentiment, mean-reversion, quantitative, crypto, bitcoin, ethereum]
aliases: ["Post-Event Short Vol", "Fear-Extreme Vol Selling", "Panic-Spike Premium Harvesting", "Stabilisation-Confirmed Vol Entry"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Panic events spike IV far above the realized volatility that subsequently delivers after the cascade completes; by entering short-vol only after a sentiment extreme is confirmed AND stabilization signals (rolling realized vol turning over, no fresh cascade in N hours) are present, the seller captures the mean-reversion of the panic premium paid by terrorized spot holders and leveraged longs seeking emergency tail protection — the counterparty who is buying puts at peak fear."

data_required: [dvol-history, realized-vol-calc, options-chain, funding-rates, liquidation-feed, fear-greed-index, ohlcv-daily]
min_capital_usd: 25000
capacity_usd: 100000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.35
breakeven_cost_bps: 60

decay_evidence: "Post-event vol selling is a structurally narrow subset of crypto-options-volatility-selling that targets the specific post-panic window. No peer-reviewed crypto study exists on this exact entry filter; the equity-market analog (selling puts after VIX spikes, documented in Whaley 2000 and Szado 2010 for equity markets) provides the conceptual basis. The edge may compress as more systematic vol-selling capital targets post-spike windows, but the combination of the sentiment-extreme filter with the stabilization-confirmation requirement is a tighter gate than raw DVOL-percentile entry."

kill_criteria: |
  - DVOL rises > 50% in a single session after entry (panic not over; exit immediately per standard vol-selling circuit breaker)
  - sleeve drawdown > 30% from high-water mark
  - realized vol exceeds DVOL for 20+ consecutive days (structural VRP inversion; post-panic IV not repricing quickly enough)
  - rolling 5-event post-panic P&L negative for all 5 consecutive events where entry qualification was met (panic premium is not mean-reverting post-stabilisation)
  - fear-and-greed ≤ 20 simultaneously with DVOL ≥ 90th percentile occurs but no stabilisation ever confirms within 48h, across 3 consecutive panic windows (stabilisation filter is structurally never met — recalibrate cascade-clear condition)

related: ["[[crypto-options-volatility-selling]]", "[[funding-conditioned-vol-selling]]", "[[event-vol-buying]]", "[[contrarian-extremes]]", "[[short-volatility-strategies]]", "[[onchain-capitulation-confluence]]", "[[leverage-stress-tail-hedge]]", "[[liquidation-cascade-fade]]", "[[deribit]]", "[[dvol]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[fear-and-greed-index]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Post-Panic Vol Selling

Post-panic vol selling enters a short-vol position (selling BTC/ETH options on [[deribit]], typically strangles or OTM puts) **after** a panic-spike event — defined as a concurrent sentiment extreme (Fear & Greed ≤ 20), elevated IV percentile (DVOL ≥ 85th percentile of its trailing year), and a rapid realized-vol spike — but only once **stabilization is confirmed**: realized vol is rolling over from its spike peak, no fresh liquidation cascade has occurred in the past 12 hours, and spot price has not made a new local low. The primitive edge is the [[variance-risk-premium|variance risk premium]] (IV exceeds subsequent realized vol); the overlay is the panic-sentiment + stabilization filter that concentrates entry to the specific post-event window where the fear premium in the vol surface is most extreme and most likely to mean-revert.

**This is explicitly differentiated from [[crypto-options-volatility-selling]]** — that page's entry gate is a DVOL-percentile filter (40th–90th percentile of the trailing year) applied continuously; it does not require a panic event or sentiment extreme as the trigger. The baseline vol-selling page enters when IV is statistically elevated relative to the trailing distribution at any time. This page enters **specifically after a panic event** when the sentiment extreme provides an additional signal that the IV elevation is fear-driven rather than structurally warranted.

**This is differentiated from [[funding-conditioned-vol-selling]]** — that page enters short-vol when elevated perp funding confirms a crowd of leveraged longs is driving IV richness (a pre-event, bullish-crowding context). This page enters short-vol **after a panic crash** when elevated fear confirms a crowd of terrified sellers is driving IV richness (a post-event, bearish-capitulation context). The trigger is the opposite sentiment regime: funding-conditioned vol selling is for overbought/crowded-long markets; post-panic vol selling is for oversold/maximum-fear markets. The two strategies should rarely fire simultaneously.

**This is differentiated from [[event-vol-buying]]** — that page buys vol ahead of scheduled binary catalysts when IV has not yet priced the event. This page sells vol **after** the panic event has fired, when IV has been driven above fair value by fear rather than by rational event-risk pricing. The two strategies are on opposite sides of the volatility life cycle.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — panic events produce a characteristic behavioral overshoot in the options market: spot holders rush to buy puts for emergency protection, leveraged longs buy calls hoping for a reversal, and market-makers widen spreads substantially. This demand spike drives IV to levels that historically exceed the realized volatility that subsequently delivers once the cascade completes. The behavioral excess is measurable through the Fear & Greed index and through the comparison between the DVOL spike and the concurrent 24h realized vol. Fear at extreme levels is historically associated with the *end* of the vol-expansion phase, not the beginning.
- **Structural** — the [[variance-risk-premium|VRP]] in crypto options is persistently positive (IV > RV on average, as documented for [[crypto-options-volatility-selling]]). Post-panic, this premium is at its widest point in the cycle: realized vol has already spiked, but IV has run even further due to the fear premium. As the panic resolves, IV mean-reverts toward realized vol faster than realized vol itself decays, creating a compression opportunity for the vol seller.
- **Risk-bearing** — the post-panic vol seller is absorbing the tail-protection demand of recently-burned market participants who are buying puts at peak panic prices. The counterparty (a terrified spot holder buying puts to protect against "the next leg down") is paying a large insurance premium for protection that is increasingly unlikely to be needed once stabilization is confirmed. The vol seller is compensated for bearing the residual tail risk.

## Why this edge exists

**Three mechanisms create the post-panic IV overshoot:**

1. **Emergency demand from forced hedgers drives IV above realized vol.** During and immediately after a cascade, spot holders, exchange custody desks, and institutional risk managers all rush to buy puts simultaneously. This demand spike is not proportional to the forward crash probability — it is proportional to the *psychological shock* of the event just experienced. The result is an IV level that prices in a much higher probability of a near-term repeat cascade than the stabilized realized-vol environment actually supports.

2. **Market-makers widen spreads and raise vol levels to manage inventory.** After absorbing panic-demand short options positions, market-makers have short-gamma books they need to hedge. They widen the vol surface by quoting higher IV to slow the incoming demand and to compensate for the delta-hedging costs they face in a volatile spot market. Once spot stabilises (smaller intraday moves, cascade flow drying up), this defensive vol widening reverses — providing the mean-reversion that the post-panic vol seller captures.

3. **The stabilization filter confirms the vol is orphaned.** The key insight of this strategy over plain post-event vol selling is the stabilization requirement. IV can remain elevated after a panic for two reasons: (a) the crash is genuinely not over (another wave coming), or (b) the crash is over and fear premium is simply slow to decay. The stabilization gate — no new cascade in 12 hours, realized vol turning over — distinguishes these cases. By requiring stabilization, the strategy enters only when IV is orphaned from its fear-driver: the cascade is over, but the vol surface has not yet repriced.

**Who is on the other side:** the spot holder buying emergency put protection at peak panic prices, paying up to 2–5× normal IV for the insurance; and the long-vol systematic fund that accumulated vol positions before/during the event and is slow to exit.

## Null hypothesis

Under the null, the panic-sentiment + stabilization gate carries **no incremental predictive power** over the DVOL-percentile gate alone:
- Short-vol positions entered when both Fear & Greed ≤ 20 AND DVOL ≥ 85th percentile AND stabilization confirmed should not produce higher P&L than positions entered on DVOL-percentile ≥ 85th percentile alone.
- Post-panic IV mean-reversion speed (days to return to 30-day-average DVOL) should not differ between panic-triggered entries and non-panic-triggered entries at the same DVOL level.
- The additional conditions (fear extreme + stabilisation) should not reduce drawdown below what the DVOL-only entry achieves, net of the fewer signals generated.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical crypto panic events (dates when BTC dropped ≥ 10% in 24h); measure DVOL before vs 5–10 days after; compare P&L of short strangles entered at DVOL peak with vs without the stabilization filter. Predict: stabilisation-filtered entries show higher win rates and lower entry-to-stop frequency.

## Rules

### Entry gate (all five conditions must be met simultaneously)

**Gate 1: Panic sentiment extreme**
- Fear & Greed index ≤ **20** (Extreme Fear) for at least **2 consecutive days**.
- Source: `/api/v1/sentiment/fear-greed-index` or alternative (alternative.me API; CryptoDataAPI provides the index).
- *Rationale:* persistent extreme fear (not just a one-day reading) confirms the panic is at its sentiment apex, not still escalating.

**Gate 2: IV is at a post-panic peak**
- DVOL ≥ **85th percentile** of its trailing 52-week DVOL distribution.
- DVOL has risen ≥ **20 vol points** from its level 5 days prior (the spike is recent and substantial).
- Source: `/api/v1/market-intelligence/dvol-history`.
- *Rationale:* the IV peak must be clearly elevated relative to history AND relative to recent levels; a DVOL that was already high before the panic does not qualify.

**Gate 3: Realized vol is rolling over**
- 24-hour realized vol (computed from 15-minute OHLCV) has declined vs its peak reading in the prior 48 hours.
- The peak 24h RV was ≥ **80 vol points** (confirming the event was a genuine shock, not routine vol).
- Source: computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200`.
- *Rationale:* realized vol rolling over from its spike peak means the cascade is dissipating; this is the key stabilization signal.

**Gate 4: No fresh cascade in 12 hours**
- Liquidation volume in the prior 12 hours is below **1.5× its 7-day rolling average**.
- Source: `/api/v1/market-intelligence/liquidations?coin=BTC`.
- *Rationale:* a fresh cascade would restart the fear cycle and invalidate the stabilization thesis. This gate ensures the entry is truly post-panic, not mid-panic.

**Gate 5: Price has not made a new 7-day local low in the prior 4 hours**
- BTC price has not set a new 168h low in the most recent 4-hour candle.
- Source: computed from `/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50`.
- *Rationale:* a new local low suggests the cascade leg is not complete; the strategy does not try to catch the absolute bottom, only enter once the selling pressure has demonstrably paused.

### Instrument selection

- **Primary instrument:** 25-delta BTC put (sell), nearest expiry with DTE ≥ 14 days but ≤ 35 days, on Deribit. Post-panic, the put wing is where the fear premium is richest (puts bid for emergency protection). Selling the put captures the widest fear-premium component.
- **Strangle alternative:** sell 25-delta put AND 15-delta call on the same expiry. The strangle captures both put-skew richness (post-panic puts) and the structural call premium; more delta-neutral.
- **Avoid front-week options:** high gamma in a still-elevated vol environment; residual cascade risk can snap the position.
- **Delta hedge:** delta-neutral within ±5 delta per unit notional; hedge daily unless spot moves > 3% intraday (hedge immediately).

### Position sizing and exit

- **Premium collected per event:** size to collect 1.5–2.5% of portfolio in option premium on the initial entry.
- **Maximum concurrent post-panic positions:** 1 (the post-panic window is regime-specific; stacking multiple events is self-contradictory).
- **Profit exit:** close when DVOL returns to within **5 vol points** of its 30-day trailing average (the fear premium has fully decayed).
- **Stop loss:** close if DVOL rises ≥ 15 vol points above entry level (a new panic wave is developing; exit immediately).
- **Time exit:** close at expiry −3 days if neither the profit target nor the stop has been triggered.

## Implementation pseudocode

```python
# post_panic_vol_selling.py

from dataclasses import dataclass
from typing import Optional

# ---- entry thresholds ----
FEAR_GREED_EXTREME       = 20      # Fear & Greed index <= 20
FEAR_DAYS_REQUIRED       = 2       # consecutive days at extreme fear
DVOL_PERCENTILE_MIN      = 85.0    # DVOL >= 85th percentile of trailing 52w
DVOL_SPIKE_MIN_VOLS      = 20.0    # DVOL rose >= 20 vol points from 5-day-ago level
RV_24H_PEAK_MIN          = 80.0    # 24h realized vol peaked at >= 80 vol points (real event)
LIQUIDATION_CLEAR_MULT   = 1.5     # liq volume < 1.5x 7d average (no fresh cascade)
NEW_LOW_LOOKBACK_HOURS   = 168     # no new 7-day low in past 4h

# ---- exit thresholds ----
DVOL_PROFIT_WITHIN_VOLS  = 5.0     # close when DVOL within 5 vol pts of 30d avg
DVOL_STOP_ABOVE_ENTRY    = 15.0    # stop: DVOL rises >= 15 vol pts above entry
DTE_TIME_EXIT            = 3       # close at expiry-3 days

@dataclass
class PanicState:
    fear_greed_today:     float  # current Fear & Greed index
    fear_greed_yesterday: float
    dvol_current:         float  # current DVOL
    dvol_5d_ago:          float  # DVOL 5 days prior (spike magnitude)
    dvol_30d_avg:         float  # 30-day trailing DVOL average
    dvol_percentile_52w:  float  # DVOL percentile in trailing 52 weeks
    rv_24h_peak_48h:      float  # peak 24h realized vol in prior 48h
    rv_24h_current:       float  # current 24h realized vol
    liq_12h:              float  # 12h liquidation volume
    liq_7d_avg:           float  # 7-day average liquidation volume
    new_low_in_4h:        bool   # True if price made new 168h low in last 4h candle

@dataclass
class ShortVolPosition:
    entry_dvol:       float
    current_dvol:     float
    dvol_30d_avg:     float
    dte:              int

def all_gates_pass(s: PanicState) -> tuple[bool, list[str]]:
    fails = []
    if not (s.fear_greed_today <= 20 and s.fear_greed_yesterday <= 20):
        fails.append(f"fear_greed not sustained: today={s.fear_greed_today}, yesterday={s.fear_greed_yesterday}")
    if s.dvol_percentile_52w < DVOL_PERCENTILE_MIN:
        fails.append(f"DVOL percentile {s.dvol_percentile_52w:.1f}% < {DVOL_PERCENTILE_MIN}%")
    if (s.dvol_current - s.dvol_5d_ago) < DVOL_SPIKE_MIN_VOLS:
        fails.append(f"DVOL spike {s.dvol_current - s.dvol_5d_ago:.1f} < {DVOL_SPIKE_MIN_VOLS} vol pts")
    if s.rv_24h_peak_48h < RV_24H_PEAK_MIN:
        fails.append(f"RV peak {s.rv_24h_peak_48h:.1f} < {RV_24H_PEAK_MIN} — event not large enough")
    if s.rv_24h_current >= s.rv_24h_peak_48h:
        fails.append(f"RV not rolling over: current {s.rv_24h_current:.1f} >= peak {s.rv_24h_peak_48h:.1f}")
    if s.liq_12h > s.liq_7d_avg * LIQUIDATION_CLEAR_MULT:
        fails.append(f"fresh cascade: 12h liq {s.liq_12h:.0f} > {LIQUIDATION_CLEAR_MULT}x 7d avg {s.liq_7d_avg:.0f}")
    if s.new_low_in_4h:
        fails.append("new 7-day low in last 4h candle — cascade not complete")
    return len(fails) == 0, fails

def entry_decision(s: PanicState, book: dict) -> dict:
    if book.get("drawdown", 0) > 0.30:
        return {"action": "FLAT", "reason": "sleeve drawdown kill"}
    if book.get("active_post_panic_position"):
        return {"action": "HOLD", "reason": "post-panic position already active"}
    ok, fails = all_gates_pass(s)
    if not ok:
        return {"action": "WAIT", "reason": "gates not met: " + "; ".join(fails)}
    premium_target = book["portfolio_capital"] * 0.020
    return {
        "action":           "SELL_25D_PUT",
        "instrument":       "25-delta BTC put, DTE 14-35 days",
        "premium_target":   premium_target,
        "entry_dvol":       s.dvol_current,
        "dvol_30d_avg":     s.dvol_30d_avg,
        "fear_greed":       s.fear_greed_today,
        "note": (f"all 5 panic gates pass: DVOL={s.dvol_current:.1f} "
                 f"(+{s.dvol_current - s.dvol_5d_ago:.1f} vs 5d ago), "
                 f"Fear&Greed={s.fear_greed_today}, RV rolling over {s.rv_24h_current:.1f} < peak {s.rv_24h_peak_48h:.1f}"),
    }

def exit_decision(pos: ShortVolPosition) -> Optional[dict]:
    # profit: DVOL back near 30d avg
    if (pos.current_dvol - pos.dvol_30d_avg) <= DVOL_PROFIT_WITHIN_VOLS:
        return {"action": "CLOSE_PROFIT",
                "reason": f"DVOL {pos.current_dvol:.1f} within {DVOL_PROFIT_WITHIN_VOLS} vol pts of 30d avg {pos.dvol_30d_avg:.1f}"}
    # stop: new panic wave
    if (pos.current_dvol - pos.entry_dvol) >= DVOL_STOP_ABOVE_ENTRY:
        return {"action": "CLOSE_STOP",
                "reason": f"DVOL +{pos.current_dvol - pos.entry_dvol:.1f} vol pts above entry — new panic wave; exit"}
    # time exit
    if pos.dte <= DTE_TIME_EXIT:
        return {"action": "CLOSE_TIME",
                "reason": f"expiry-{DTE_TIME_EXIT} days exit"}
    return None
```

The production system adds: a Deribit WebSocket feed for live DVOL and options pricing; an automated delta-hedge runner; a daily P&L attribution between theta decay (carry) and vega P&L (IV mean-reversion); and a pre-entry checklist verifying the cascade appears genuinely complete (no large pending liquidation clusters on the order book).

## Indicators / data used

- **Fear & Greed index** — `/api/v1/sentiment/fear-greed-index` (CryptoDataAPI sentiment layer) or alternative.me API. Consecutive ≤ 20 readings (Gate 1).
- **DVOL** — `/api/v1/market-intelligence/dvol-history`; current DVOL, 5-day-ago level, 30-day trailing average, and 52-week percentile (Gates 2, and profit-exit target).
- **Realized vol (24h and 48h peak)** — computed from `/api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200`; Yang-Zhang or close-to-close log-return vol over trailing 24h window. Gate 3 (rolling over).
- **Liquidations (12h)** — `/api/v1/market-intelligence/liquidations?coin=BTC`; 12h aggregated liquidation volume vs 7-day average. Gate 4 (no fresh cascade).
- **4h OHLCV** — `/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50`; check for new 168-hour low in the most recent candle. Gate 5.
- **Funding rates** — `/api/v1/derivatives/funding-rates?coin=BTC`; context check — if funding has inverted deeply negative (panic-driven mass shorting), that is a secondary warning that the vol entry may be premature.
- **Regime** — `/api/v1/regimes/current`; if `Structural_Shock`, defer entry even if all gates pass (ongoing systemic shock may produce multiple cascade waves).
- **OTM put pricing (Deribit)** — specific strike and delta options pricing NOT available via CryptoDataAPI; source from [[deribit]] directly (`GET /api/v2/public/get_order_book?instrument_name=BTC-{date}-{strike}-P`).

*Note: OTM put pricing for specific strikes/expiries requires Deribit API access, consistent with [[funding-conditioned-vol-selling]] and [[leverage-stress-tail-hedge]]. DVOL history and sentiment are available via CryptoDataAPI.*

## Example trade

**Setup (illustrative — post-cascade panic window):**

- Trigger event: BTC drops from $88,000 to $74,000 (−15.9%) in 36 hours following a large exchange-hack headline.
- **Gate 1:** Fear & Greed = 14 (day 1) and 17 (day 2). Both ≤ 20 — Gate 1 passes.
- **Gate 2:** DVOL = 92 vol points. DVOL 5 days ago = 58 vol points. Spike = +34 vol points (≥ 20 threshold). DVOL 52-week percentile = 93rd (≥ 85th threshold) — Gate 2 passes.
- **Gate 3:** 24h RV peak (48h prior) = 135 vol points. Current 24h RV = 104 vol points (rolling over — 135 → 104 in 12h) — Gate 3 passes.
- **Gate 4:** 12h liquidation volume = $240M. 7d avg = $210M/day. 12h liq = $240M vs daily avg = $210M; 12h rate annualised ≈ 0.48× daily (below 1.5× threshold) — Gate 4 passes.
- **Gate 5:** No new 168h low in last 4h candle; BTC is at $74,400 vs the 7-day low of $73,800 set 6 hours ago — Gate 5 passes.
- **Entry:** All 5 gates pass.
- **Instrument:** sell 25-delta BTC put, expiry 21 days out. Strike ≈ $63,000 (25-delta at $74,400 spot with DVOL = 92). Put premium = approximately 3.5% of spot = $2,604 collected per unit.
- **Portfolio:** $250,000. Premium target = 2% × $250,000 = $5,000. Units sold = $5,000 / $2,604 ≈ **1.92 units** (sell ~2 contracts).
- **Entry DVOL:** 92 vol points. DVOL 30-day average: 54 vol points. Target DVOL for profit exit: 54 + 5 = 59 vol points.

**Scenario A — IV mean-reverts as expected (most common post-panic):**
- Over the next 9 days, no new cascade occurs. BTC stabilises at $72,000–$78,000. DVOL declines: 92 → 78 → 65 → 59. When DVOL reaches 59 (within 5 vol points of 30d avg = 54), close the put.
- 25-delta put held 9 days: theta decay has eroded premium significantly + vega decline. Buy back at approximately 1.4% of spot = $1,037 per unit. Net gain: ($2,604 − $1,037) × 1.92 = **+$3,009 gross** on $5,000 premium collected = **+60.2% return on premium** / +1.2% of portfolio.

**Scenario B — second cascade wave (stop):**
- 3 days after entry, a second negative headline triggers a fresh cascade. BTC drops to $68,000. DVOL spikes from 92 to 111 (+19 vol points — approaching the +15 stop threshold from entry of 92; at +15 → 107; at 111 the stop triggers).
- Buy back at approximately 8.1% of spot = $5,508 per unit. Net loss: ($2,604 − $5,508) × 1.92 = **−$5,576 gross** on $5,000 premium = **−111% of premium collected** / −2.2% of portfolio.

**Expected value sketch (illustrative):** if 65% of post-panic entries reach the profit target (Scenario A) and 35% hit the stop (Scenario B), expected P&L per signal ≈ (0.65 × +$3,009) + (0.35 × −$5,576) = $1,956 − $1,952 ≈ **breakeven** at these win/loss parameters. The strategy's edge comes from a higher actual win rate (more historical panics stabilize than cascade again within 3 days) and a higher actual vega-decay capture vs stop size. Conservative until backtested.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Higher win rate vs raw DVOL-percentile entry; lower signal frequency; net Sharpe similar to or slightly above crypto-options-volatility-selling |
| Expected max drawdown | ~35% | Stop-loss at +15 DVOL points above entry; consecutive failed panic entries possible if cascade events cluster |
| Win rate (per signal) | ~60–70% (estimated) | Post-panic stabilization more likely than second-wave cascade; raw DVOL percentile has ~55% win rate; panic filter improves this estimate |
| Average win / average loss | ~1.2–1.5× (estimated) | Profit target (DVOL to 30d avg) is larger than entry overshoot; but stop is relatively tight at +15 DVOL points |
| Breakeven cost budget | 60 bps | Options are wide bid/ask instruments; Deribit fees 0.03% per fill × 2 fills = 6 bps; delta-hedge slippage ≈ 10–20 bps; total cost ≈ 30–40 bps; 60 bps budget is conservative |
| Signal frequency | Very low | Post-panic qualifying windows occur 3–7 times per year in BTC; less frequent than raw DVOL-percentile |

**Cost overlay:** the dominant cost is the stop-loss event (buying back the sold put at a higher price when DVOL spikes further). Theta decay works in the seller's favour day-by-day; the risk is a second cascade wave before DVOL has mean-reverted.

## Capacity limits

- **Per event:** Deribit BTC 25-delta put OI in the relevant expiry can support $5–20M in sold premium without meaningful market impact.
- **Aggregate:** `capacity_usd: 100000000` reflects the total short-vega capacity at this scale. At $100M AUM and 2% of portfolio per signal = $2M premium collected per event × 5 events/year = $10M annual premium — within Deribit's post-panic put supply.
- **Binding constraint:** the number of qualifying panic events per year (3–7), not market depth. The strategy cannot scale by lowering quality thresholds.

## What kills this strategy

1. **Cascade clustering (#3: Market-structure regime change).** In systemic events (LUNA collapse 2022, FTX collapse 2022), the "stabilization" period between cascade waves is short and the strategy is stopped repeatedly. The requirement for 12h cascade-clear and the DVOL-stop-loss limit exposure but do not eliminate it for multi-day systemic events.
2. **Options market efficiency post-panic (#4: Crowding).** If more systematic vol-sellers target the post-panic window, the fear premium decays faster — but also the entry prices are lower (the market has already partially absorbed the post-panic IV reset before the seller can enter). The two effects partially cancel.
3. **Persistent high vol after event (#5: Regime change).** After structurally significant events (exchange collapses, regulatory crises), IV can remain elevated for weeks rather than mean-reverting in days. The profit target (DVOL within 5 of 30d avg) may not be reached before expiry, and the time-exit captures less premium.
4. **VRP inversion (#2: Cost structure).** If a multi-month regime emerges where RV consistently exceeds IV (the underlying is moving more than options price), the vol-selling book generates systematic losses. The kill criterion (RV > DVOL for 20+ days) covers this.
5. **Liquidity in post-panic options market (#7: Operational).** After a large cascade, Deribit bid/ask spreads widen substantially. The actual entry price for the sold put may be significantly worse than the mid-market quote. Execution in the first hours post-panic may be substantially more expensive than under normal conditions — wait for liquidity to partially normalise before executing.

## Kill criteria

Pause on any of:

1. **DVOL rises > 50% in a single session after entry** — panic not over; exit immediately (standard vol-selling circuit breaker inherited from [[crypto-options-volatility-selling]]).
2. **Sleeve drawdown > 30% from high-water mark** — multiple failed post-panic entries; the stabilisation thesis is not delivering.
3. **Realized vol exceeds DVOL for 20+ consecutive days** — structural VRP inversion; the premium collected is negative in expectation.
4. **Rolling 5-event post-panic P&L negative for all 5 consecutive events** where all 5 entry gates were met — the panic premium is not mean-reverting post-stabilisation; strategy has stopped working.
5. **Fear & Greed ≤ 20 AND DVOL ≥ 85th percentile fires but stabilisation never confirms within 48h** for 3 consecutive panic windows — the stabilisation filter is structurally never being met; recalibrate the 12h cascade-clear condition.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Enters at the highest-value point in the VRP cycle** — post-panic IV is at its maximum distance from normal; the vol seller is at peak carry advantage and the mean-reversion pull is strongest.
- **Sentiment filter provides an orthogonal gate** — Fear & Greed extreme adds information beyond DVOL percentile alone; the emotional overshoot is a stronger signal that the vol is driven by fear rather than structural uncertainty.
- **Stabilisation confirmation reduces false entries** — requiring the cascade to be demonstrably over (no fresh cascade in 12h, RV rolling over, no new local low) avoids the most dangerous scenario: entering short-vol into an ongoing multi-wave collapse.
- **Lower entry frequency means better selectivity** — the tighter gates mean fewer signals, but higher win rate per signal vs the raw DVOL-percentile book.

## Disadvantages

- **Very low signal frequency** — qualifying events occur 3–7 times per year; the strategy generates minimal annual signals. Underperformance in low-volatility years is structural, not regime-specific.
- **Stop-loss in second cascade waves is painful** — when the stabilisation thesis is wrong (new wave comes), the stop at +15 DVOL points produces losses of 100%+ of premium collected in the position. The risk/reward per trade is not as asymmetric as long-vol strategies.
- **Execution friction post-panic is high** — bid/ask spreads are widest exactly when the entry signal fires. Actual fills may be 5–15 vol points inside the mid-price in the immediate post-panic window; waiting a few hours for liquidity to normalise is operationally sensible but may miss the peak fear premium.
- **Cannot scale by finding more signals** — the strategy requires genuine panic events; it cannot be scaled by relaxing the gates, which would revert it toward the baseline DVOL-percentile strategy without the differentiation.

## Sources

- [[crypto-options-volatility-selling]] — the canonical short-vol primitive; this page is a post-panic-targeted subset with tighter entry gates.
- [[contrarian-extremes]] — the sentiment-extreme entry logic in a directional (spot) context; the Fear & Greed ≤ 20 gate here is the options-vol adaptation of the same sentiment-extreme trigger.
- [[onchain-capitulation-confluence]] — the on-chain equivalent of the stabilization-confirmation requirement; uses on-chain signals + sentiment to confirm a capitulation bottom is in place. Conceptually adjacent.
- Whaley, R. E. (2000) — "The investor fear gauge." *Journal of Portfolio Management* 26(3): 12–17. Documents the VIX spike-and-mean-reversion pattern in equity markets; the conceptual analog for crypto post-panic DVOL mean-reversion.
- [[variance-risk-premium]] — the structural premium that the post-panic vol seller is harvesting; the VRP is at its widest in the post-panic window.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed-index` — Fear & Greed index; Gate 1 (consecutive extreme fear readings)
- `GET /api/v1/market-intelligence/dvol-history` — DVOL history; Gate 2 (percentile + spike magnitude) and profit-exit target
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200` — 15m OHLCV; compute 24h realized vol and Gate 3 (rolling over)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50` — 4h OHLCV; Gate 5 (no new 7-day low)
- `GET /api/v1/market-intelligence/liquidations?coin=BTC` — liquidation volume; Gate 4 (no fresh cascade)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding context check
- `GET /api/v1/regimes/current` — macro regime; defer entry in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-intelligence/dvol-history` — extended DVOL series for 52-week percentile calibration and post-panic backtest
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — daily OHLCV for longer-window realized-vol baseline

*Note: 25-delta put pricing for specific strikes and expiries is NOT currently documented as a CryptoDataAPI endpoint. Source from [[deribit]] API directly (`GET /api/v2/public/get_order_book`, `GET /api/v2/public/get_instruments`). DVOL index history is available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/dvol-history"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-market-data]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [fear & greed](https://cryptodataapi.com/fear-greed) · [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run all five gates end-to-end:

- **Gate stack** — `GET /api/v1/sentiment/fear-greed` (consecutive extreme-fear), `GET /api/v1/market-intelligence/dvol-history` (spike percentile), and `GET /api/v1/market-intelligence/liquidations?coin=BTC` (no fresh cascade) are polled together each hour post-panic
- **Signal** — 15m klines compute realised vol rolling over (Gate 3) — the actual entry trigger
- **Regime gate** — `GET /api/v1/regimes/current`; `Structural_Shock` defers entry no matter how stretched DVOL is
- **Backtest** — `GET /api/v1/market-intelligence/fear-greed-history` + DVOL history + `GET /api/v1/backtesting/klines` (1d back to 2017-08) replay the gates across past panics; the cascade-clear condition (Gate 4) replays only since 2026-03-30 via `GET /api/v1/backtesting/liquidations`
- **Tips** — the short-put execution itself lives on Deribit; CryptoDataAPI covers all five gates, so let the agent hold the full gate state and only call Deribit when armed

## Related

- [[crypto-options-volatility-selling]] — the canonical short-vol book with DVOL-percentile gate; this page is the panic-event-targeted subset
- [[funding-conditioned-vol-selling]] — short-vol when funding confirms leveraged-long crowding; this page is the opposite sentiment regime (post-crash fear, not pre-crash greed) — rarely active at the same time
- [[event-vol-buying]] — buys vol before scheduled catalysts; this page sells vol after panic events — the two are the buy-and-sell sides of post-event IV mis-pricing
- [[contrarian-extremes]] — directional (spot) contrarian entry at sentiment extremes; this page applies the same extreme-fear filter to the options surface
- [[leverage-stress-tail-hedge]] — accumulates long-vol *before* the panic event; this page enters short-vol *after* the event; the two strategies are temporal complements
- [[onchain-capitulation-confluence]] — requires on-chain + sentiment confirmation before a bullish entry; adjacent stabilisation-confirmation logic
- [[short-volatility-strategies]] — the broad short-vol category
- [[liquidation-cascade-fade]] — the spot/perp directional fade of the same cascade that this page sells vol around; adjacent tactical use case
- [[fear-and-greed-index]] — the sentiment indicator underlying Gate 1
- [[dvol]] — the DVOL index; primary IV baseline
- [[implied-volatility]] — the options surface concept
- [[variance-risk-premium]] — the VRP that post-panic IV overshoot represents
- [[deribit]] — the primary options execution venue
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — cascade clustering, VRP inversion, crowding
- [[when-to-retire-a-strategy]] — kill vs pause framework
