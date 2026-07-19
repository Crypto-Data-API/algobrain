---
title: "Options Relative-Value × Funding Filter"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options-structures, derivatives, volatility, funding-rate, perpetual-futures, quantitative, crypto, deribit, behavioral-finance]
aliases: ["Options RV Funding Gate", "Funding-Confirmed Skew Trading", "Perp-Funding Skew Signal", "Funding-Gated Vol Surface Entry"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, behavioral, informational]
edge_mechanism: "Stretched positive perp funding rates reflect an overcrowded leveraged-long crowd whose demand for call options simultaneously bids up call skew (puts become cheap relative to calls); conversely, stretched negative funding reflects an overcrowded short crowd that has bid put skew to richness (calls become cheap). The funding rate is a real-time revealed proxy for the derivative crowd's directional conviction — when that conviction is extreme, it distorts the vol surface away from its RV-implied fair value in a predictable direction, creating an exploitable skew RV dislocation. Negative funding → rich puts / cheap calls → buy calls (or sell risk-reversal short). Positive funding → rich calls / cheap puts → buy puts (or sell risk-reversal long). The counterparty is the leveraged derivative crowd that is both causing the skew dislocation (via their option demand) and the likely mean-reverting when their crowded position unwinds."

data_required: [funding-rates, long-short-ratio, open-interest, deribit-options-chain, dvol-btc, dvol-eth, skew-rr25, realized-vol-30d, implied-vol-by-strike]
min_capital_usd: 25000
capacity_usd: 25000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.25
breakeven_cost_bps: 50

decay_evidence: "The funding → skew relationship is grounded in the supply/demand of option instruments by the derivative crowd: crowded longs buy calls (for upside convexity), which elevates call skew; crowded shorts buy puts (for downside protection), which elevates put skew. This is a structural micro-market mechanism, not a statistical anomaly. Compression risk: as more options market makers and vol-arb desks operate in crypto options, the window between the funding signal and the skew adjustment narrows. The edge likely requires at least a 6–12 hour lag between funding extreme and skew response to be profitable net of Deribit bid-ask spreads. Available evidence from options-market-maker desks suggests this lag exists in BTC/ETH options as of 2025."

kill_criteria: |
  - rolling 6-month Sharpe < 0 on all funding-filtered options RV trades combined
  - Funding-to-skew correlation (measured as 5-day lagged correlation between 8h funding z-score and RR25 z-score) drops below 0.20 for 3 consecutive months (the funding → skew mechanism has broken down)
  - 3 consecutive trades where the skew re-rated in the funding direction rather than mean-reverting (crowded longs are bidding calls higher rather than the position being squeezed out; trend-following mode in derivatives is active — pause until correlation restores)
  - Deribit bid-ask spread on RR25 options > 3 vol pts consistently (execution costs exceed the skew dislocation being traded; pause)

related: ["[[skew-trading]]", "[[funding-conditioned-vol-selling]]", "[[options-rv-event-calendar]]", "[[calendar-spread-arbitrage]]", "[[funding-filtered-momentum]]", "[[narrative-crowding-exit]]", "[[low-leverage-vol-selling]]", "[[complacency-vol-buying]]", "[[crowded-long-funding-fade]]", "[[smart-money-vs-crowd-divergence]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[risk-reversal]]", "[[deribit]]", "[[dvol]]", "[[funding-rate]]", "[[open-interest]]", "[[options-greeks]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi]]"]
---

# Options Relative-Value × Funding Filter

Options relative-value funding filter uses the perp **funding rate as a leading indicator for skew richness** on the Deribit vol surface: stretched positive funding (leveraged longs crowded) predicts call skew richness and put skew cheapness; stretched negative funding (leveraged shorts crowded) predicts put skew richness and call skew cheapness. The strategy enters options RV positions — buying the cheap wing and selling the rich wing via risk reversals or wing spreads — when the funding signal confirms the expected skew dislocation is both large enough to be tradeable and attributable to crowd positioning rather than structural demand. The counterparty is the derivative crowd that is both causing the skew dislocation (by buying options for convexity on their crowded position) and the likely source of mean-reversion when their position unwinds.

**This is differentiated from [[skew-trading]]** — that page enters skew trades purely based on statistical dislocation of the 25-delta risk reversal (RR25) from its historical mean, without reference to the current perp funding state. This page uses the funding rate as the PRIMARY signal that tells you *why* the skew is dislocated and *whether* the dislocation is attributable to crowd positioning (thus likely to mean-revert when the crowd unwinds) vs. structural demand (thus less likely to mean-revert). The funding filter adds directional conviction to a pure statistical skew-deviation signal.

**This is differentiated from [[funding-conditioned-vol-selling]]** — that page sells net vega (net short options: the short-vol primitive) when elevated funding confirms that crowded longs are inflating IV level. This page trades *vol surface relative value* — it is not net short vol; it buys the cheap wing and sells the rich wing, maintaining near-zero net vega. The two pages are complementary: [[funding-conditioned-vol-selling]] sells the IV level richness when funding is high; this page trades the skew *shape* richness when funding is extreme in either direction.

**This is differentiated from [[options-rv-event-calendar]]** — that page conditions term-structure RV entries on the *forward event calendar* (scheduled catalysts create predictable near-dated IV richness). This page conditions skew RV entries on the *current funding state* (crowded derivative positioning creates predictable wing richness). Different signal source (calendar vs real-time funding), different vol-surface dimension (term-structure vs skew), different duration (event-window vs funding-regime).

**This is differentiated from [[funding-filtered-momentum]]** — that page uses the funding rate to gate *directional price-momentum entries* in perps/spot: enter a long only when funding confirms the crowd is not yet crowded. This page uses the funding rate to gate *options RV entries* in the vol surface: enter a skew trade when the funding confirms the crowd's option demand has created a skew dislocation. Completely different instrument and mechanism.

## Edge source

Per [[edge-taxonomy]], **structural + behavioral + informational**:

- **Structural (primary)** — The perp funding rate and the options vol surface are imperfectly integrated markets despite both being derivative instruments on the same underlying. A crowded long in perps systematically generates call option demand (leveraged longs buy calls for additional upside convexity or to cap their insurance cost) without a countervailing supply of calls from the vol surface's market-maker book. This supply-demand imbalance in the call wing is not immediately corrected because options market makers and perp speculators are different market participants with different information sets and different clearing mechanisms. The structural friction between these two derivative markets creates a predictable lag between the funding extreme and the full skew adjustment.
- **Behavioral** — The leveraged derivative crowd is emotionally driven: at positive funding extremes, the crowd buys calls because they fear missing additional upside (FOMO call buying); at negative funding extremes, the crowd buys puts because they fear further downside (panic put buying). Both behaviours are well-documented in crypto options market data (call skew is persistently elevated during bull-market FOMO phases; put skew is elevated during panic phases). The behavioral predictability of this demand creates a mean-reverting skew pattern that the options RV trade exploits.
- **Informational** — The funding rate is published in real time and is a direct revealed measure of the derivative crowd's current net positioning. It is not a lagging price indicator; it reflects actual current positioning costs. This makes it a more timely and direct signal for skew dislocation than historical price-based momentum or sentiment surveys.

## Why this edge exists

**The funding → skew transmission mechanism:**

1. **Funding builds positive (longs crowded):** Leveraged long holders in perps want additional upside exposure and buy calls on Deribit (or have protection from puts they've sold). Demand for OTM calls rises → call wing implied vol rises → RR25 (call vol minus put vol) rises toward positive or inflates further positive. Simultaneously, puts may become relatively cheap as the crowded-long crowd is not buying protective puts.

2. **Funding peaks and begins to mean-revert:** The crowded-long position becomes the consensus trade; late entrants are squeezed; some longs take profit. Funding starts to fall from its peak. The call option demand that drove call-skew richness starts to moderate.

3. **Skew mean-reverts toward fair value:** As the long crowd unwinds, call demand falls, and the RR25 returns toward its historical mean. The skew-RV trade (long put, short call, or short RR25 risk-reversal) profits from this convergence.

**The reverse works for negative funding:** crowded shorts buy puts for protection, inflating put skew; when the crowded-short position mean-reverts (short squeeze or funding normalisation), put skew compresses back to fair value.

**Quantitative relationship:** Based on CryptoDataAPI funding data and qualitative options-desk observation:
- BTC RR25 (25-delta call vol − 25-delta put vol) tends to be +5 to +10 vol pts above its rolling mean when 7-day avg funding ≥ +0.040%/8h (crowded longs bid calls significantly)
- BTC RR25 tends to be −5 to −10 vol pts below its rolling mean when 7-day avg funding ≤ −0.015%/8h (crowded shorts bid puts significantly)

These are approximate ranges observed qualitatively; precise calibration requires Deribit historical options data (not available via CryptoDataAPI — Deribit API or commercial vol surface feeds required).

**Who is on the other side:** the derivative crowd that buys calls in crowded-long phases (they are the source of call skew richness; the RV trade sells those expensive calls back to them via risk reversal) and the derivative crowd that buys puts in crowded-short phases (they are the source of put skew richness; the RV trade sells those expensive puts back to them).

## Null hypothesis

Under the null, the funding rate at the time of options RV entry adds **no incremental predictive power** to the subsequent direction of skew mean-reversion:

- RR25 entries made when funding is at extreme levels (≥ +0.040%/8h or ≤ −0.015%/8h) should NOT produce higher subsequent 5-day skew mean-reversion returns than entries made at neutral funding.
- The funding gate should not reduce loss frequency or increase win rate materially relative to entering all skew dislocation signals regardless of the current funding state.

Testable: for all historical RR25 z-score ≥ 1.5 signals (call-skew rich), separate by 7-day avg funding at signal date into (a) funding ≥ +0.030%/8h (crowd long) and (b) funding neutral (−0.010% to +0.020%/8h). Compare 5-day forward change in RR25. Prediction: group (a) has higher subsequent mean-reversion in RR25 (skew compresses) because the crowd's call demand is the cause of the richness.

Currently untested. Adjacent evidence: the academic options literature documents that retail demand for calls in bullish market phases systematically elevates call skew in equity markets (Bollen & Whaley 2004); crypto options are expected to exhibit a stronger version of this effect due to higher retail participation and leverage.

## Rules

### Entry gate: Positive-funding skew trade (call-rich, put-cheap)

**Entry conditions (all must hold):**
1. **Funding extreme (positive):** 8h funding ≥ **+0.035%/8h** AND 7-day avg funding ≥ **+0.025%/8h** (sustained crowded-long environment).
   - Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
2. **Call skew confirmed rich:** BTC RR25 (25Δ call IV − 25Δ put IV) ≥ **+5 vol pts above its 20-day rolling mean** (call wing is statistically elevated, not just slightly positive).
   - Source: Deribit API (`/api/v2/public/get_volatility_index_data`) or commercial vol surface feed. *Not available via CryptoDataAPI.*
3. **OI confirmation (crowd actually positioned):** OI ≥ 70th percentile of 30-day distribution AND L/S ratio ≥ 1.15 (longs are paying and are the majority).
   - Source: `GET /api/v1/derivatives/open-interest?coin=BTC`, `GET /api/v1/derivatives/binance/long-short-ratio`.
4. **No near-term event risk:** Event Risk score `GET /api/v1/event/regime/score` < 40 (no scheduled catalyst that could cause directional IV spike that would override the crowd-skew signal).

**Trade structure:**
- **Primary:** Buy 25Δ put (DTE 21–35), sell 25Δ call (DTE 21–35) = sell the risk reversal (long put vs short call, premium-neutral or slight debit). Maximum loss on short call capped with 15Δ call purchase (convert to call spread: sell 25Δ call, buy 15Δ call).
- **Alternative (if call skew < 4 vol pts rich):** sell 25Δ call alone (but keep delta-hedged); forgo the put leg.
- **Delta-hedge:** delta-neutral at inception; re-hedge when delta moves > 0.10 (roughly when underlying price moves 3–5%).

### Entry gate: Negative-funding skew trade (put-rich, call-cheap)

**Entry conditions (all must hold):**
1. **Funding extreme (negative):** 8h funding ≤ **−0.015%/8h** AND 7-day avg funding ≤ **−0.010%/8h** (sustained crowded-short environment).
   - Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
2. **Put skew confirmed rich:** BTC RR25 ≤ **−5 vol pts below its 20-day rolling mean** (put wing elevated).
   - Source: Deribit API or commercial vol surface feed.
3. **OI confirmation:** L/S ratio ≤ 0.85 (shorts are the majority position).
   - Source: `GET /api/v1/derivatives/binance/long-short-ratio`.
4. **No near-term event risk:** Event Risk score < 40.

**Trade structure:** buy 25Δ call (cheap), sell 25Δ put (rich) = buy the risk reversal (long call vs short put). Cap downside on short put with 15Δ put purchase.

### Exit rules (both trade directions)

1. **Primary exit (skew mean-reversion):** close the risk reversal when RR25 returns to within 1 vol pt of its 20-day rolling mean (the dislocation has compressed; edge captured).
2. **Funding normalisation exit:** close if the 7-day avg funding crosses back to neutral (|funding| < +0.015%/8h on positive trade; |funding| < −0.005%/8h on negative trade) — the crowd that was driving the skew dislocation has unwound.
3. **Time exit:** close after **21 days** if neither skew-mean-reversion nor funding-normalisation has triggered (approaching DTE; theta cost accumulates; do not carry through expiry if the thesis has not played out).
4. **Stop:** close if RR25 moves further in the dislocation direction by **+3 vol pts from entry** (the skew is getting richer before mean-reverting — the crowd position is strengthening, not unwinding; exit before further loss accumulates).

## Implementation pseudocode

```python
# options_rv_funding_filter.py

from dataclasses import dataclass
from typing import Optional

# Entry thresholds — positive funding (call-rich trade)
FUND_POS_8H_MIN    = 0.00035   # 8h funding ≥ +0.035% → crowded long
FUND_POS_7D_MIN    = 0.00025   # 7d avg funding ≥ +0.025%
SKEW_RICH_VOL_PTS  = 5.0       # RR25 ≥ +5 vol pts above 20d mean
OI_PERCENTILE_MIN  = 70        # OI ≥ 70th pct
LS_LONG_MIN        = 1.15      # L/S ≥ 1.15 for positive-funding trade
EVENT_RISK_MAX     = 40        # event risk score < 40

# Entry thresholds — negative funding (put-rich trade)
FUND_NEG_8H_MAX    = -0.00015  # 8h funding ≤ −0.015% → crowded short
FUND_NEG_7D_MAX    = -0.00010  # 7d avg funding ≤ −0.010%
SKEW_CHEAP_VOL_PTS = -5.0      # RR25 ≤ −5 vol pts below 20d mean
LS_SHORT_MAX       = 0.85      # L/S ≤ 0.85 for negative-funding trade

# Exit thresholds
SKEW_REVERSION_TARGET = 1.0    # exit when RR25 within 1 vol pt of 20d mean
FUND_NEUTRAL_CROSS    = 0.00015 # funding normalised to < +0.015%/8h (positive trade)
MAX_HOLD_DAYS         = 21
SKEW_ADVERSE_STOP     = 3.0    # stop if RR25 moves 3 vol pts further dislocated

@dataclass
class DerivativeState:
    funding_8h:       float     # current 8h funding rate
    funding_7d_avg:   float     # 7-day average 8h funding rate
    oi_percentile:    float     # OI vs 30d distribution (0–100)
    long_short_ratio: float
    event_risk_score: float     # CryptoDataAPI event risk 0–100

@dataclass
class SkewState:
    rr25_current:   float       # current 25Δ risk reversal (call vol − put vol)
    rr25_20d_mean:  float       # 20-day rolling mean of RR25
    rr25_disloc:    float       # = rr25_current − rr25_20d_mean

@dataclass
class Position:
    trade_type:    str          # 'sell_rr' (call-rich) or 'buy_rr' (put-rich)
    entry_rr25:    float
    entry_date_idx: int
    current_date_idx: int

def gate_positive_funding_trade(d: DerivativeState, s: SkewState) -> tuple[bool, list[str]]:
    fails = []
    if d.funding_8h < FUND_POS_8H_MIN:
        fails.append(f"funding {d.funding_8h:.5f} < {FUND_POS_8H_MIN}")
    if d.funding_7d_avg < FUND_POS_7D_MIN:
        fails.append(f"7d avg funding {d.funding_7d_avg:.5f} < {FUND_POS_7D_MIN}")
    if s.rr25_disloc < SKEW_RICH_VOL_PTS:
        fails.append(f"RR25 disloc {s.rr25_disloc:.1f} vol pts < {SKEW_RICH_VOL_PTS} threshold")
    if d.oi_percentile < OI_PERCENTILE_MIN:
        fails.append(f"OI {d.oi_percentile:.0f}th pct < {OI_PERCENTILE_MIN}th")
    if d.long_short_ratio < LS_LONG_MIN:
        fails.append(f"L/S {d.long_short_ratio:.2f} < {LS_LONG_MIN}")
    if d.event_risk_score >= EVENT_RISK_MAX:
        fails.append(f"event risk {d.event_risk_score:.0f} ≥ {EVENT_RISK_MAX}")
    return len(fails) == 0, fails

def gate_negative_funding_trade(d: DerivativeState, s: SkewState) -> tuple[bool, list[str]]:
    fails = []
    if d.funding_8h > FUND_NEG_8H_MAX:
        fails.append(f"funding {d.funding_8h:.5f} > {FUND_NEG_8H_MAX}")
    if d.funding_7d_avg > FUND_NEG_7D_MAX:
        fails.append(f"7d avg funding {d.funding_7d_avg:.5f} > {FUND_NEG_7D_MAX}")
    if s.rr25_disloc > SKEW_CHEAP_VOL_PTS:
        fails.append(f"RR25 disloc {s.rr25_disloc:.1f} vol pts > {SKEW_CHEAP_VOL_PTS} threshold")
    if d.long_short_ratio > LS_SHORT_MAX:
        fails.append(f"L/S {d.long_short_ratio:.2f} > {LS_SHORT_MAX}")
    if d.event_risk_score >= EVENT_RISK_MAX:
        fails.append(f"event risk {d.event_risk_score:.0f} ≥ {EVENT_RISK_MAX}")
    return len(fails) == 0, fails

def exit_decision(pos: Position, s: SkewState, d: DerivativeState) -> Optional[dict]:
    days = pos.current_date_idx - pos.entry_date_idx
    # Mean-reversion target
    if abs(s.rr25_disloc) <= SKEW_REVERSION_TARGET:
        return {'action': 'EXIT_PROFIT',
                'reason': f"RR25 within {SKEW_REVERSION_TARGET} vol pts of mean"}
    # Funding normalisation
    if pos.trade_type == 'sell_rr' and d.funding_8h < FUND_NEUTRAL_CROSS:
        return {'action': 'EXIT_FUNDING_NORM',
                'reason': f"funding {d.funding_8h:.5f} crossed below {FUND_NEUTRAL_CROSS}"}
    # Time exit
    if days >= MAX_HOLD_DAYS:
        return {'action': 'EXIT_TIME', 'reason': f"{MAX_HOLD_DAYS}d time limit"}
    # Adverse stop
    if pos.trade_type == 'sell_rr':
        adverse = s.rr25_disloc - (pos.entry_rr25 - s.rr25_20d_mean)
        if adverse >= SKEW_ADVERSE_STOP:
            return {'action': 'STOP',
                    'reason': f"RR25 moved {adverse:.1f} vol pts further rich (crowd strengthening)"}
    return None
```

## Indicators / data used

- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — primary entry signal; 8h current and 7-day avg. Source: [[cryptodataapi-derivatives]].
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC` — OI percentile check (Gate 3). Source: [[cryptodataapi-derivatives]].
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio` — crowd positioning confirmation (Gate 3). Source: [[cryptodataapi-derivatives]].
- **Event risk score** — `GET /api/v1/event/regime/score` — event risk gate (Gate 4); exclude entries when event risk elevated. Source: [[cryptodataapi-regimes]].
- **RR25 (25Δ risk reversal)** — *Not available via CryptoDataAPI.* Requires Deribit API (`/api/v2/public/get_order_book` or `/get_volatility_index_data`) or a commercial crypto vol surface feed (e.g., Kaiko, Tardis.dev). This is a hard dependency — the skew dislocation signal cannot be constructed from CryptoDataAPI endpoints alone.
- **DVOL** — *Available qualitatively via Deribit (`GET /api/v2/public/get_volatility_index_data` with `index_name=btc_usdv`).* Not available via CryptoDataAPI. Use DVOL level as a secondary gate (avoid entering skew trades when DVOL is > 80th percentile — the broad IV spike may overwhelm skew-specific signals).

*Important note: this strategy requires Deribit API access or a commercial vol surface data feed for the skew (RR25) signal. CryptoDataAPI provides the funding, OI, L/S, and event risk components of the gate, but the options surface data itself (RR25 by expiry and strike) is sourced from Deribit directly.*

## Example trade

**Setup (illustrative — crowded-long skew trade)**

- BTC trading at $82,000. 8h funding = +0.048%/8h (extremely crowded long). 7d avg funding = +0.038%/8h. Gate 1: PASS.
- BTC RR25 (DTE 28, Oct expiry): call 25Δ IV = 68 vol pts, put 25Δ IV = 58 vol pts. RR25 = +10 vol pts. 20-day mean RR25 = +3 vol pts. Dislocation = +7 vol pts above mean. Gate 2: PASS (+7 ≥ +5 threshold).
- OI: 72nd percentile. L/S ratio: 1.22. Gate 3: PASS.
- Event risk score: 18. Gate 4: PASS.
- All gates pass. Sleeve: $100,000 options capital.

**Trade: Sell risk reversal (call-rich, positive funding trade)**
- Sell 25Δ BTC call ($89,000 strike), buy 25Δ BTC put ($75,000 strike), DTE 28. Delta-hedged at inception.
- Approximate premium: approximately flat (near-zero net premium at these skew levels for RR25 around +10 vol pts).
- Contingent cap on short call: buy 15Δ call ($95,000 strike) as spread cap.

**Day 8:**
- Funding has declined to +0.022%/8h (crowd partially unwound). RR25 now +5 vol pts (moved from +10 to +5 — 5 vol pts mean-reversion). Not yet at SKEW_REVERSION_TARGET of 1 vol pt.

**Day 12:**
- Funding = +0.014%/8h (below FUND_NEUTRAL_CROSS of +0.015%). **Funding normalisation exit triggered.**
- RR25 = +4 vol pts (dislocation = +1 vol pt from 20d mean of +3 = almost back).
- Close risk reversal. Estimated P&L: 3–5 vol pts of skew compression on a $100K sleeve ≈ $2,500–$4,500 (approximate, depends on vega notional of the position).

*(Illustrative. Deribit options bid/ask spreads and delta hedging costs would reduce these estimates materially. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Funding extreme provides additional signal clarity over pure skew-stat entries |
| Expected max drawdown | ~25% | Adverse skew move (crowd continues bidding the rich wing) + delta hedging slippage |
| Signal frequency | 8–15 per year (estimated) | Funding extremes at the threshold levels occur multiple times per year |
| Average hold duration | 5–21 days | Until skew mean-reversion or funding normalisation (often earlier than 21 days) |
| Breakeven cost | 50 bps | Deribit taker fee ~3bps per leg × 3–4 legs (entry + exit of each wing) + delta hedge × 3 re-hedges |
| Options data dependency | Deribit API required | CryptoDataAPI does not provide vol surface / RR25 data |

**Cost overlay:** Deribit bid-ask spreads on BTC 25Δ options are typically 1–3 vol pts per side; a round-trip through a 2-leg risk reversal costs 4–12 vol pts in total spread costs. The target skew dislocation of ≥ 5 vol pts must therefore be significantly above this threshold to be profitable net of spreads. Entries are only triggered when dislocation ≥ 5 vol pts AND the funding signal provides directional conviction that the dislocation will mean-revert rather than persist.

## Capacity limits

- `capacity_usd: 25000000` — BTC options on Deribit have reasonable depth at the 25Δ strike for positions up to ~$25M notional. Above this, the risk reversal itself begins to move the skew, creating adverse self-selection.
- **ETH version:** ETH options are available with similar RR25 dynamics but lower OI. Scale ETH book to ~30% of BTC capacity ($7.5M notional).

## What kills this strategy

1. **Call skew remains rich for longer than expected (#2: Regime change).** In extreme bull markets (e.g., late 2020, early 2021), funding can remain at +0.10%/8h+ for weeks while call skew continues to expand rather than mean-revert. The trend-following derivative crowd may be correct; entering a sell-risk-reversal early in a bull run creates substantial losses. The 21-day time exit and +3 vol pt adverse stop are critical mitigants.
2. **Delta hedging failure (#6: Data / execution).** The risk reversal requires continuous delta hedging. Large gap moves (> 5–10% overnight) create hedge slippage that can turn a correctly-directional skew trade into a net loss due to hedging costs. Mitigate: keep position sizes small enough that hedge rebalances do not create meaningful market impact.
3. **Deribit bid-ask spreads wider than assumed (#6: Data / execution).** In low-liquidity windows (weekends, holiday periods) or during vol spikes, BTC 25Δ option spreads can widen to 5–8 vol pts, making the round-trip cost exceed the skew dislocation. Gate 4 (event risk) partially protects against this; monitor real-time Deribit bid-ask before execution.
4. **Funding-to-skew correlation breaks down (#2: Regime change).** In a market where most retail participation has shifted to non-Deribit venues (e.g., if a major competitor to Deribit emerges), the funding → skew transmission mechanism may weaken. The kill criterion (correlation drops below 0.20 for 3 months) detects this.

## Kill criteria

Pause or retire on any of:

1. **Rolling 6-month Sharpe < 0** on all funding-filtered options RV trades.
2. **Funding-to-skew lag correlation < 0.20 for 3 consecutive months** — the mechanism is broken; the derivative crowd is no longer generating predictable skew demand at funding extremes.
3. **3 consecutive adverse stops** — stop-loss triggers 3 times in a row (the skew is trending, not mean-reverting; the crowd is being right, not wrong).
4. **Deribit bid-ask spread on RR25 > 3 vol pts for > 50% of entries** — execution costs systematically exceed the skew dislocation; the trade is uneconomic.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Higher conviction than pure skew-stat signals** — knowing WHY the skew is dislocated (crowd positioning) rather than just THAT it is dislocated provides directional confidence and helps avoid entering into skew dislocations caused by structural demand (e.g., corporate treasury hedging demand) that are less likely to mean-revert.
- **Directional adaptability** — works in both directions: sell call skew richness when funding is positive (crowded longs), buy call skew cheapness when funding is negative (crowded shorts). The same framework applies to both regimes.
- **Near-zero net vega** — the risk-reversal structure is nearly vega-neutral (long put vs short call; the vega of each leg approximately cancels), meaning the strategy does not take a directional bet on whether IV will rise or fall in aggregate.
- **Composable with [[skew-trading]]** — the funding filter can serve as a pre-filter for all skew-trading entries: only enter statistical skew signals from [[skew-trading]] when the funding confirmation is also present.

## Disadvantages

- **Requires Deribit API access** — the RR25 skew signal is not available via CryptoDataAPI and requires direct Deribit API integration or a commercial crypto options data feed.
- **Delta hedging operational complexity** — the risk reversal position requires continuous delta hedging, adding operational overhead compared to a directional perp trade. Hedging failures during fast markets are a real execution risk.
- **BTC/ETH only** — Deribit lists liquid options only on BTC and ETH; the strategy cannot be applied to other crypto assets where skew signals might also be valuable.
- **Low signal frequency** — funding extremes at the threshold levels occur only 8–15 times per year; the strategy is inactive for extended periods.

## Sources

- Bollen, N.P.B. & Whaley, R.E. (2004). "Does net buying pressure affect the shape of implied volatility functions?" *Journal of Finance*. Documents retail demand driving skew shape in equity options markets.
- [[skew-trading]] — the pure skew-deviation strategy; this page adds the funding confirmation layer.
- [[funding-conditioned-vol-selling]] — the net-short-vol strategy gated on funding; this page is the vol-neutral RV analog.

## Getting the Data (CryptoDataAPI)

**Live data (available via CryptoDataAPI):**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — Gate 1: 8h funding rate and 7-day average
- `GET /api/v1/derivatives/open-interest?coin=BTC` — Gate 3: OI percentile check
- `GET /api/v1/derivatives/binance/long-short-ratio` — Gate 3: L/S ratio confirmation
- `GET /api/v1/event/regime/score` — Gate 4: event risk score (exclude when > 40)

**Historical data (available via CryptoDataAPI):**
- `GET /api/v1/derivatives/funding-rates?coin=BTC&historical=true&days=365` — annual funding history for gate threshold calibration

**Deribit API (required — not available via CryptoDataAPI):**
- `GET /api/v2/public/get_order_book` with `instrument_name=BTC-DDMMMYY-STRIKE-C/P` — live options bid/ask for RR25 construction
- `GET /api/v2/public/get_volatility_index_data?currency=BTC&resolution=3600` — DVOL timeseries for vol-regime context

*Note: CryptoDataAPI does not provide Deribit options chain data (implied vol by strike/expiry, RR25). This strategy requires Deribit API access (free, public endpoints) or a commercial crypto vol surface provider (Kaiko, Tardis.dev, Amberdata). The CryptoDataAPI endpoints listed above cover the derivative-positioning gates; the vol surface signal must be sourced from Deribit.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run every gate of this strategy end-to-end:

- **Gate** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (Gate 1), `GET /api/v1/derivatives/open-interest?coin=BTC` (Gate 3 percentile), and `GET /api/v1/derivatives/binance/long-short-ratio` run before any vol-surface read
- **Event filter** — `GET /api/v1/event/regime/score`; skip entries when the event-risk composite exceeds 40
- **Signal** — the RR25 skew signal itself comes from Deribit's public API; CryptoDataAPI supplies every positioning gate around it
- **Backtest** — funding-gate replay from `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30) — deeper than the 365-day REST window — with point-in-time regime state from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — poll the cached `GET /api/v1/daily` bundle hourly for the gate inputs instead of hitting four endpoints per cycle

## Related

- [[skew-trading]] — pure statistical skew-deviation trading; this page adds the funding gate as a conviction filter
- [[funding-conditioned-vol-selling]] — net-short-vol strategy gated on funding; this page's vol-neutral RV complement
- [[options-rv-event-calendar]] — event-calendar-gated vol term-structure RV; different vol-surface dimension
- [[funding-filtered-momentum]] — funding gate applied to price momentum (perp/spot); different instrument
- [[narrative-crowding-exit]] — exit discipline for crowded narrative longs; the same funding-crowding signal applied to exit rather than options-RV entry
- [[crowded-long-funding-fade]] — directional short into crowded longs; this page trades the vol surface consequence of the crowd, not the directional price consequence
- [[calendar-spread-arbitrage]] — the term-structure RV page; composable with this skew RV page as different vol-surface dimensions
- [[complacency-vol-buying]] — buy puts when greed + cheap IV; partially overlapping but different instrument structure
- [[risk-reversal]] — the options structure used in this strategy
- [[implied-volatility]] — the vol surface concept underlying this page
- [[deribit]] — the options exchange for execution
- [[dvol]] — Deribit's implied vol index for BTC/ETH
- [[funding-rate]] — the derivative positioning signal (Gate 1)
- [[edge-taxonomy]] — structural + behavioral + informational edge classification
