---
title: "Trend-Aligned Premium Selling"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, volatility, derivatives, trend-following, mean-reversion, behavioral-finance, quantitative, crypto, bitcoin, ethereum]
aliases: ["Trend-Selective Wing Selling", "Directional Premium Seller", "Trend-Conditioned Vol Selling", "Wing-Selective Short Vol"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Options vol sellers who sell both wings symmetrically suffer systematic losses on the side that the trend is pressing into — the into-the-move options remain bid by directional flow and produce frequent delta losses; by selling only the wing the trend supports (puts in confirmed uptrends, calls in confirmed downtrends), the strategy harvests the structural VRP on the side where the trend-following crowd is reducing demand, while avoiding the systematic delta-drag of selling into the directional move."

data_required: [dvol-history, realized-vol-calc, options-chain, ohlcv-daily, funding-rates, open-interest]
min_capital_usd: 25000
capacity_usd: 100000000
crowding_risk: medium

expected_sharpe: 1.0
expected_max_drawdown: 0.30
breakeven_cost_bps: 60

decay_evidence: "Trend-conditional wing selection in crypto options is not documented in published research; the equity-market analog (covered call in uptrends, cash-secured put in downtrends as a mechanical rule) is well-known in retail strategy education but not rigorously tested as a systematic combination. As a niche refinement of the baseline DVOL-percentile vol-selling book, this overlay is likely less crowded than the raw short-vol approach, but the reduced signal frequency (must wait for a confirmed trend in addition to elevated IV) means the evidence base is thinner."

kill_criteria: |
  - DVOL rises > 50% in a single session (vol-shock circuit breaker; standard across all short-vol strategies)
  - sleeve drawdown > 30% from high-water mark
  - the into-the-trend wing produces systematic losses: rolling 10-entry wing P&L on the selected side is negative (trend is still pressing into the wing even after trend confirmation — the trend signal is not delivering protection)
  - realized vol exceeds DVOL for 20+ consecutive days (VRP inversion; structural problem with all vol selling)
  - trend regime is in "NEUTRAL" > 70% of potential entry days for 90 consecutive days (trend gate is perpetually blocking entries; IV is elevated but no confirmed trend — reconsider whether to accept neutral-regime entries at reduced size, or accept the low signal frequency)

related: ["[[crypto-options-volatility-selling]]", "[[funding-conditioned-vol-selling]]", "[[post-panic-vol-selling]]", "[[covered-call]]", "[[cash-secured-put]]", "[[options-premium-selling]]", "[[premium-selling-systematic]]", "[[vol-targeted-trend-following]]", "[[trend-following-cta]]", "[[deribit]]", "[[dvol]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[skew-trading]]", "[[funding-rate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Trend-Aligned Premium Selling

Trend-aligned premium selling is a short-vol strategy that sells options on [[deribit]] (BTC and ETH) where the **trend direction selects which wing to sell** — puts in confirmed uptrends, calls in confirmed downtrends — rather than selling both wings symmetrically as in a standard strangle or iron condor. The primitive edge is the [[variance-risk-premium|variance risk premium]] (IV exceeds subsequent realized vol on average); the overlay is the trend filter that selects **which side of the vol surface to sell**, avoiding the "into-the-move" wing where the trend is pressing against the short-option position and where delta losses and early assignment/exercise risk are highest.

**This is explicitly differentiated from [[crypto-options-volatility-selling]]** — that page sells symmetric strangles or iron condors (both wings) whenever the DVOL-percentile gate fires, regardless of market direction. The trend filter is not applied to wing selection. This page adds the trend gate specifically to **select the wing**, not to determine whether to sell. A neutral-regime market would still trigger [[crypto-options-volatility-selling]] if DVOL percentile is elevated; this page requires a confirmed trend to determine which wing.

**This is differentiated from [[funding-conditioned-vol-selling]]** — that page uses elevated perp funding as the conditioning signal for vol entry (a crowding-proxy trigger, most relevant in bull markets). The two strategies can be simultaneously active (elevated funding in an uptrend → funding-conditioned vol selling enters AND this page sells puts). But funding-conditioned vol selling does not select the wing based on trend; it uses a call-wing tilt when funding is extremely high (≥ 0.05%/8h) but does not explicitly forbid selling calls when the trend is up. This page's wing-selection rule is more absolute: in a confirmed uptrend, calls are **not sold** regardless of funding level.

**This is differentiated from [[post-panic-vol-selling]]** — that page enters short-vol after a panic crash, when sentiment is at an extreme and IV is at a post-event peak. The timing and trigger are completely different: post-panic vol selling is a post-event, fear-extreme entry; this page is a steady-state, trend-conditional entry for ongoing vol-selling books.

**This is differentiated from [[covered-call]]** — a covered call is the retail/spot-holding expression of call-selling in uptrends (long spot → sell call on top). This page sells puts AND uses a delta-hedged or standalone perp position, not a spot base. The covered-call page describes the mechanics of holding an underlying asset and writing covered calls; this page is a systematic, trend-gated premium-selling book without a mandatory spot or long-perp base.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — in a confirmed uptrend, calls are consistently bid by retail and institutional participants seeking directional leveraged upside exposure (call buying is the natural momentum-following behavior). This bid keeps call-side IV and call skew elevated, making calls expensive in realized-vol terms even when the overall DVOL is not at an extreme. Selling the put side in this environment — where put buyers are scarce and put-seller competition is low — captures the VRP on the structurally under-bid wing. The inverse applies in downtrends: put demand is bid by panic hedgers while call demand drops; selling calls in a downtrend captures the VRP on the under-bid upside wing.
- **Structural** — the crypto options vol surface has a pronounced **skew** driven by the directional positioning in the perp market. In uptrends, the surface tilts positively (call skew up, put skew relatively lower); in downtrends, the surface tilts negatively (put skew up, call skew relatively lower). The trend-aligned wing seller systematically sells the relatively cheaper wing, improving the VRP collected per unit of delta risk taken.
- **Risk-bearing** — the vol seller still underwrites crash risk (put seller) or squeeze risk (call seller). The wing selection does not eliminate risk; it selects the risk type that is better compensated given the current directional regime: in uptrends, the market is paying less for put insurance relative to the crash probability; in downtrends, the market is paying less for call (rally) insurance relative to the rebound probability.

## Why this edge exists

**Two mechanisms explain why the trend-aligned wing is systematically better compensated than the into-the-trend wing:**

1. **Trend following crowd bids the into-the-trend options.** In confirmed uptrends, the momentum crowd accumulates long exposure — in spot, perps, AND options. This momentum demand bids calls in uptrends and pushes their IV above the structurally-justified level. Selling calls in an uptrend means selling into a crowd that is actively buying them for directional exposure, accepting a rich premium but also accepting high delta P&L variability as the trend continues. Selling puts in the same uptrend means selling against the structurally under-bid wing: put demand is lower because the recent direction has been up, reducing spot holders' urgency to hedge downside.

2. **The delta profile of the trend-aligned wing decays faster.** A put seller in an uptrend watches the market move further from the put strike every day the trend continues — the put's delta naturally decreases (the option becomes less ITM risk). A call seller in an uptrend watches the market approach or test the call strike — the call's delta increases, requiring expensive delta hedging. The trend-aligned short wing has systematically better delta dynamics than the into-trend short wing.

3. **Into-the-trend wing has a reflexive feature.** During sustained trends, the option market periodically re-strikes the into-the-trend wing (new strikes at-the-money emerge as the market moves). Each re-striking eliminates the accumulated theta the into-trend wing seller earned, requiring the seller to establish a new position at a worse relative entry. The trend-aligned wing avoids this re-striking dynamic.

**Who is on the other side:** the directional momentum participant buying the into-the-trend options (calls in uptrends, puts in downtrends) who is overpaying for directional convexity; and the structured-product desk that sells the trend-aligned wing as cheap insurance without considering the relative under-pricing created by the directional-crowd demand imbalance.

## Null hypothesis

Under the null, the trend direction carries **no information about which wing is better compensated in the VRP**:
- The P&L of selling BTC puts in confirmed uptrends should not exceed the P&L of selling BTC calls in the same uptrend periods, conditional on DVOL percentile.
- Call skew (25-delta risk reversal) should not be systematically positive in uptrends relative to neutral regimes.
- The delta-drag cost of selling the into-the-trend wing (calls in uptrend, puts in downtrend) should not exceed the delta-drag cost of selling the trend-aligned wing across a representative historical sample.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical periods where BTC was in a confirmed uptrend (price > SMA20 by ≥ 10%, RSI 4h > 55); compare P&L of selling 25-delta puts vs 25-delta calls on Deribit in the same periods, delta-hedged. Predict: put-selling P&L significantly exceeds call-selling P&L during uptrend periods.

## Rules

### Trend regime classification

**Uptrend confirmation (sell puts):**
- BTC daily close ≥ **10% above 20-day SMA** — price structure confirming trend.
- 4h RSI ≥ **60** — momentum not overbought/reversal-pending but trending (not at RSI extreme where a reversal is more probable).
- Funding 7-day average ≥ **0.02%/8h** — perp market confirming directional bias (not required to be stretched, just positive).

**Downtrend confirmation (sell calls):**
- BTC daily close ≥ **8% below 20-day SMA** — price structure confirming trend.
- 4h RSI ≤ **45** — momentum trending down, not at oversold extreme.
- Funding 7-day average < **0.00%/8h** (≤ 0, negative) — perp market flipped to short-bias OR flat.

**Neutral regime (no wing sell):**
- Price within ±8% of 20-day SMA, OR RSI between 45–60, OR funding ambiguous (between 0% and 0.02%/8h).
- In neutral regime: no new wing-sell entries. Existing positions held per exit rules.
- *Rationale:* in directionless markets, both wings have similar risk/reward; the trend gate provides no differentiation, and entering both wings replicates the undifferentiated strangle.

### IV entry gate (all regime types)

**Gate: DVOL must be elevated.**
- DVOL ≥ **50th percentile** of its trailing 52-week distribution.
- IV−RV (DVOL minus 30-day realised vol) ≥ **+3 vol points** (VRP is positive — selling is justified on the fundamental VRP basis).

*Note: the DVOL percentile threshold here is lower (50th) than in [[crypto-options-volatility-selling]] (40th–90th) because the trend gate provides an additional quality filter; a 50th-percentile IV in a confirmed trend is more informative than a 50th-percentile IV in a directionless market.*

### Instrument selection

| Regime | Wing to sell | Instrument | Notes |
|---|---|---|---|
| **Uptrend** | Puts | 25-delta BTC put, DTE 14–35 days | Put wing is under-bid in uptrend; delta naturally decays away from strike as market rises |
| **Downtrend** | Calls | 25-delta BTC call, DTE 14–35 days | Call wing is under-bid in downtrend; delta decays as market falls away from call strike |
| **Neutral** | None | — | No new entries; hold existing through expiry or exit triggers |

**Alternative — spreads for capital efficiency:**
- **Bull put spread** (uptrend): sell 25-delta put, buy 10-delta put same expiry. Limits tail exposure; reduces premium collected but lowers maximum loss.
- **Bear call spread** (downtrend): sell 25-delta call, buy 10-delta call same expiry. Equivalent downtrend structure.

### Position sizing and risk

- **Premium collected per entry:** 1.5–2.5% of portfolio in premium per open position.
- **Maximum concurrent positions:** 2 (one per active expiry). Do not ladder more than 2 simultaneous open wing-sell positions.
- **Delta hedge:** delta-neutral within ±10 delta per unit notional; hedge when delta breaches this band. In uptrend with sold puts: delta drift is typically away from the short put (market rising → short put delta decreases naturally); hedge less frequently than in neutral. In downtrend with sold calls: similarly, delta drifts naturally away from sold call as market falls.
- **Vol-shock exit:** close immediately if DVOL rises > 50% in a single session. No exceptions.

### Exit conditions

1. **Profit target:** close when the position's value falls to **20% of premium collected** (the sold option has decayed 80% of its value; theta capture is largely complete; retain the last 20% only at elevated risk).
2. **Stop:** close if the sold option's value rises to **3× the premium collected** (the option has moved 3× against the position — substantial delta/vega loss).
3. **Trend reversal:** close the position if the trend regime flips — uptrend-to-neutral or uptrend-to-downtrend while holding a sold put. The overlay that justified the wing selection has reversed; exit and reassess.
4. **Time exit:** close at expiry −3 days (gamma risk becomes extreme in final 3 days).

## Implementation pseudocode

```python
# trend_aligned_premium_selling.py

from dataclasses import dataclass
from typing import Optional

# ---- trend thresholds ----
UPTREND_SMA_PCT          = 0.10     # close >= 10% above SMA20
UPTREND_RSI_MIN          = 60
UPTREND_FUNDING_MIN      = 0.0002  # 7d avg >= 0.02%/8h
DOWNTREND_SMA_PCT        = 0.08    # close >= 8% below SMA20
DOWNTREND_RSI_MAX        = 45
DOWNTREND_FUNDING_MAX    = 0.0     # funding <= 0

# ---- IV gate ----
DVOL_PERCENTILE_MIN      = 50.0    # DVOL >= 50th percentile
IV_MINUS_RV_MIN          = 3.0     # IV - RV >= +3 vol points

# ---- position management ----
MAX_CONCURRENT           = 2
PROFIT_DECAY_PCT         = 0.80    # close at 80% theta capture
STOP_MULT                = 3.0     # close at 3x premium collected
DTE_TIME_EXIT            = 3
VOL_SHOCK_PCT            = 0.50    # close if DVOL rises 50% in one session

@dataclass
class MarketState:
    close:               float
    sma20_daily:         float
    rsi_4h:              float
    funding_7d_avg_8h:   float
    dvol_current:        float
    dvol_52w_percentile: float
    realized_vol_30d:    float

@dataclass
class ShortWingPosition:
    wing:               str     # "put" or "call"
    entry_premium:      float
    current_value:      float
    trend_at_entry:     str     # "UPTREND" or "DOWNTREND"
    dte:                int

def trend_regime(s: MarketState) -> str:
    sma_dist = (s.close - s.sma20_daily) / s.sma20_daily if s.sma20_daily > 0 else 0
    if (sma_dist >= UPTREND_SMA_PCT
            and s.rsi_4h >= UPTREND_RSI_MIN
            and s.funding_7d_avg_8h >= UPTREND_FUNDING_MIN):
        return "UPTREND"
    if (sma_dist <= -DOWNTREND_SMA_PCT
            and s.rsi_4h <= DOWNTREND_RSI_MAX
            and s.funding_7d_avg_8h <= DOWNTREND_FUNDING_MAX):
        return "DOWNTREND"
    return "NEUTRAL"

def iv_gate_passes(s: MarketState) -> tuple[bool, str]:
    if s.dvol_52w_percentile < DVOL_PERCENTILE_MIN:
        return False, f"DVOL percentile {s.dvol_52w_percentile:.1f}% < {DVOL_PERCENTILE_MIN}%"
    iv_minus_rv = s.dvol_current - s.realized_vol_30d
    if iv_minus_rv < IV_MINUS_RV_MIN:
        return False, f"IV-RV={iv_minus_rv:.1f} < {IV_MINUS_RV_MIN} vol pts"
    return True, ""

def entry_decision(s: MarketState, book: dict) -> dict:
    if book.get("drawdown", 0) > 0.30:
        return {"action": "FLAT", "reason": "drawdown kill"}
    if book.get("active_positions", 0) >= MAX_CONCURRENT:
        return {"action": "HOLD", "reason": "max concurrent positions reached"}

    regime = trend_regime(s)
    if regime == "NEUTRAL":
        return {"action": "WAIT", "reason": "no confirmed trend — no wing selected"}

    iv_ok, iv_reason = iv_gate_passes(s)
    if not iv_ok:
        return {"action": "WAIT", "reason": f"IV gate: {iv_reason}"}

    wing = "put" if regime == "UPTREND" else "call"
    delta_target = 25
    premium_budget = book["portfolio_capital"] * 0.020
    return {
        "action":           f"SELL_{delta_target}D_{wing.upper()}",
        "wing":             wing,
        "regime":           regime,
        "delta_target":     delta_target,
        "dte_range":        "14-35 days",
        "premium_budget":   premium_budget,
        "entry_dvol":       s.dvol_current,
        "iv_minus_rv":      s.dvol_current - s.realized_vol_30d,
        "note": (f"trend={regime}, DVOL={s.dvol_current:.1f} ({s.dvol_52w_percentile:.0f}th pct), "
                 f"IV-RV={s.dvol_current - s.realized_vol_30d:+.1f}, sell {wing} wing"),
    }

def exit_decision(pos: ShortWingPosition, current_regime: str) -> Optional[dict]:
    # vol shock
    # (handled at book level, not position level — see book monitor)

    # profit: 80% theta capture
    if pos.current_value <= pos.entry_premium * (1 - PROFIT_DECAY_PCT):
        return {"action": "CLOSE_PROFIT",
                "reason": f"80% theta captured: value {pos.current_value:.4f} vs entry {pos.entry_premium:.4f}"}
    # stop: 3x premium
    if pos.current_value >= pos.entry_premium * STOP_MULT:
        return {"action": "CLOSE_STOP",
                "reason": f"3x stop: value {pos.current_value:.4f} = {pos.current_value/pos.entry_premium:.1f}x entry"}
    # trend reversal
    if current_regime != pos.trend_at_entry and current_regime != "NEUTRAL":
        return {"action": "CLOSE_TREND_REVERSAL",
                "reason": f"trend flipped from {pos.trend_at_entry} to {current_regime}"}
    if current_regime == "NEUTRAL" and pos.trend_at_entry in ("UPTREND", "DOWNTREND"):
        # neutral is tolerated for a short period; close if persists > 3 days
        pass  # handled by monitor with a counter
    # time exit
    if pos.dte <= DTE_TIME_EXIT:
        return {"action": "CLOSE_TIME", "reason": f"expiry-{DTE_TIME_EXIT}d exit"}
    return None
```

The production system adds: a Deribit WebSocket feed for live DVOL and option mid-prices; a daily delta-hedge runner for the selected wing positions; a trend-regime monitor polling every 4 hours (RSI and SMA on 4h and daily klines); and a P&L attribution separating theta (time decay), delta P&L (directional move), and vega P&L (IV change) per wing.

## Indicators / data used

- **Daily OHLCV (SMA20)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30`; 20-day SMA and price-distance for trend Gate 1.
- **4h OHLCV (RSI)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50`; 14-period RSI for trend Gate 2.
- **Funding rate (7-day average)** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; directional-bias confirmation for trend Gate 3.
- **DVOL** — `GET /api/v1/market-intelligence/dvol-history`; DVOL current level, 52-week percentile, and 30-day trailing average for IV gate and stop monitoring.
- **Realized vol (30-day)** — computed from `/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=60`; Yang-Zhang estimator for IV−RV gate.
- **Regime** — `GET /api/v1/regimes/current`; context for regime filtering (avoid entries in `Structural_Shock`).
- **Options pricing (Deribit)** — 25-delta put and call pricing requires [[deribit]] API access directly (`GET /api/v2/public/get_order_book?instrument_name=BTC-{date}-{strike}-{P/C}`).

*Note: specific options pricing (delta, IV, mid-price for chosen wings) requires Deribit API access, consistent with [[crypto-options-volatility-selling]], [[funding-conditioned-vol-selling]], and [[event-vol-buying]]. DVOL index and derivatives metrics are available via CryptoDataAPI.*

## Example trade

**Setup (illustrative — uptrend put-sell entry):**

- BTC: $72,000. SMA20-daily = $63,000. Distance = (+14.3% — above 10% threshold).
- 4h RSI = 64 (above 60 threshold).
- 7-day average 8h funding = 0.028%/8h (above 0.02% threshold). Uptrend confirmed.
- DVOL = 61 vol points. DVOL 52-week percentile = 68th (above 50th threshold).
- 30-day realized vol = 55%. IV−RV = 61 − 55 = +6 vol points (above +3 floor).
- **Regime: UPTREND.** **IV gate: passes.** → Sell 25-delta BTC put.
- **Instrument:** sell 25-delta BTC put, $64,000 strike, 21 days out. Premium collected ≈ 1.7% of spot = $1,224 per unit.
- **Portfolio:** $150,000. Premium budget = 2.0% × $150,000 = $3,000. Units sold = $3,000 / $1,224 ≈ **2.45 units**.

**Scenario A — uptrend continues; put decays (most likely in uptrend):**
- BTC continues to $78,000 over 14 days. The $64,000 put moves deeply OTM. Its delta approaches 0; value decays to 0.3% of spot = $234 per unit.
- Value = $234 / unit × 2.45 = $573 remaining. 80% decay threshold = $3,000 × (1 − 0.80) = $600. Close.
- **Net gain: $3,000 − $573 = +$2,427 / +1.62% of portfolio.**

**Scenario B — trend reversal; put moves toward strike:**
- At day 7, BTC breaks below SMA20 after a negative headline (now 6% below SMA20, which is below the 8% downtrend threshold but within neutral range). Regime switches to NEUTRAL.
- Trend reversal from UPTREND to NEUTRAL triggers the exit condition. Close the put at current value.
- BTC at $68,500. Put at $64,000 strike, 14 DTE, BTC down $3,500 from entry. Put value rises to approximately 2.8% of spot = $1,918 per unit. Total value = $1,918 × 2.45 = $4,699.
- **Net loss: $3,000 − $4,699 = −$1,699 / −1.13% of portfolio.** (Stop was at 3× entry = $9,000; this exit fired earlier due to trend reversal.)

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Higher win rate than symmetric strangle due to trend-aligned wing selection; modestly lower Sharpe than funding-conditioned-vol-selling (fewer entry signals) |
| Expected max drawdown | ~30% | Trend reversal exits limit losses relative to symmetric strangle in reversal regimes; vol-shock stop is the primary drawdown driver |
| Win rate (per entry) | ~65–75% (estimated) | Trend-aligned wing naturally decays when the trend continues; better than the ~55% win rate of symmetric strangles |
| Average win / average loss | ~1.5–2× (estimated) | Theta capture when the wing decays vs. stop-loss when a reversal brings the option toward the strike; asymmetric but not as extreme as long-vol |
| Breakeven cost budget | 60 bps | Consistent with [[crypto-options-volatility-selling]]; 30–40 bps in bid/ask and fees; 60 bps is conservative |
| Signal frequency | Moderate-low | Must have confirmed trend AND elevated IV simultaneously; fewer entries than symmetric strangle (which fires on IV-percentile alone) |

**Cost overlay:** theta decay (time value erosion as the sold wing moves further OTM in the trend) works strongly for the seller. Delta hedging costs are lower than for a symmetric strangle because delta drifts naturally away from the sold strike in a trending market. The dominant cost is the stop-loss event (trend reversal with insufficient exit speed).

## Capacity limits

- **Same as [[crypto-options-volatility-selling]]:** Deribit BTC 25-delta put and call market depth in the 14–35 DTE range. A $100M AUM strategy selling $2M notional per entry × 2 concurrent positions = $4M in open short premium — within Deribit's capacity.
- **Wing-specific liquidity:** put wings in uptrends and call wings in downtrends are typically the less-liquid side of the surface (the market has less demand for insurance on the trend-aligned side). Actual fills may be slightly wider than mid-market. Size accordingly.

## What kills this strategy

1. **Trend reversal into the sold wing (#5: Regime change).** The strategy's primary risk is that the market trend reverses sharply into the sold wing before the exit fires. A 20% sudden crash in an uptrend (sold puts) moves the put from deep OTM to near-the-money. The trend reversal exit and the 3× stop provide protection, but rapid reversals can gap through both.
2. **Persistent neutral regime (#5: Regime change).** If BTC spends most of a year in a directionless range (price bouncing around the SMA20, RSI between 45–60), the trend gate rarely fires and the strategy generates minimal signals. The DVOL may be elevated but the trend gate blocks entries.
3. **Vol-shock in the trend direction (#2: Cost structure).** An unexpected negative shock in an uptrend (spot ETF rejection, major exchange hack) produces both a trend reversal AND a vol spike simultaneously. The sold puts are near-the-money in a high-IV environment — a doubly adverse scenario. The vol-shock exit (DVOL +50% in one session) fires but at potentially adverse levels.
4. **Options market efficiency improving for trend-conditional wings (#4: Crowding).** If more systematic operators adopt trend-conditional wing selling, the put skew in uptrends and call skew in downtrends will compress, reducing the VRP differential between the two wings.
5. **Trend signal too slow (delta-drag during trend entry phase).** The SMA20-based trend signal lags the actual trend by construction; the strategy enters the sold-put position after the trend has already moved 10% above the SMA. If the trend is near its end when the gate fires, the position may be entered at the worst time.

## Kill criteria

Pause on any of:

1. **DVOL rises > 50% in a single session** — standard vol-shock circuit breaker; close all positions immediately.
2. **Sleeve drawdown > 30% from high-water mark** — the trend-aligned wing selection is not preventing losses.
3. **Rolling 10-entry wing P&L on the selected side is negative** — trend is pressing into the "correct" wing despite the alignment; the signal is not delivering the expected delta-drift benefit.
4. **Realized vol exceeds DVOL for 20+ consecutive days** — VRP inversion; the structural basis for vol selling is inverted.
5. **Trend regime is NEUTRAL > 70% of potential entry days for 90 consecutive days** — the trend gate is perpetually blocking entries; the strategy is idle; reconsider acceptance of neutral-regime entries at half-size or at higher DVOL percentile threshold.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Avoids the delta-drag of the into-trend wing** — selling puts in uptrends and calls in downtrends means the sold option's delta naturally decays as the market moves with the trend. This is the opposite of the systematic delta-drag that plagues symmetric-strangle sellers who hold the into-trend wing.
- **Higher win rate for the trend period** — in a trending market, the trend-aligned short wing expires worthless or near-worthless with higher probability than the symmetric strangle's into-trend wing, improving the overall win rate.
- **Clear exit trigger from trend reversal** — the trend gate provides a natural exit signal that the symmetric strangle lacks; a trend reversal closes the position before it fully moves against the seller.
- **Composable with existing vol-selling infrastructure** — this strategy can be run as an overlay on top of [[crypto-options-volatility-selling]]: when the baseline vol-selling book is in a confirmed trend, tilt toward the trend-aligned wing; in neutral, return to symmetric strangles. The overlay adds the wing-selection discipline without requiring a separate infrastructure.

## Disadvantages

- **Lower signal frequency** — requires both a confirmed trend AND elevated IV; many elevated-IV periods occur without a confirmed trend, and the strategy skips those.
- **Tail risk on sharp trend reversals** — in trend-reversal crashes (uptrend → sudden dump), the sold puts are closest to the money exactly when the vol is spiking and liquidity is thinning. The stop fires but at adverse prices.
- **Single-wing positions have less premium income** — selling only one wing (put or call) collects approximately 40–60% of the premium a symmetric strangle would collect at the same delta and DTE. The strategy has lower absolute income per period than the symmetric baseline.
- **Wing selection can be wrong** — in consolidating markets near the trend threshold (SMA distance between 8–12%), the trend regime can flip between uptrend and neutral rapidly, causing repeated entry-and-exit cycles that accumulate transaction costs without meaningful P&L.

## Sources

- [[crypto-options-volatility-selling]] — the canonical short-vol primitive; the DVOL-percentile gate and VRP harvest are directly inherited from this page; this page adds the trend-conditional wing selection as the overlay.
- [[funding-conditioned-vol-selling]] — the funding-conditioned vol-selling variant; the two can be composed: funding-conditioned entry selects *when* to sell, while this page's trend gate selects *which wing* to sell.
- [[covered-call]] and [[cash-secured-put]] — the retail/spot-holding expressions of the same trend-conditional wing-selling intuition; this page is the delta-hedged, systematic options-book equivalent.
- [[variance-risk-premium]] — the structural basis for all vol selling; trend alignment improves which wing of the VRP to harvest.
- [[skew-trading]] — the vol surface skew that the trend creates; this strategy exploits the trend-induced skew asymmetry.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30` — daily OHLCV; SMA20 and price distance for trend Gate 1
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50` — 4h OHLCV; 14-period RSI for trend Gate 2
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 7-day average funding for trend Gate 3
- `GET /api/v1/market-intelligence/dvol-history` — DVOL current, 52-week percentile, and 30-day trailing average for IV gate
- `GET /api/v1/regimes/current` — regime context; block entry in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — daily OHLCV for trend-regime classification across historical periods
- `GET /api/v1/market-intelligence/dvol-history` — extended DVOL series for 52-week percentile calibration and wing-P&L backtest by regime

*Note: 25-delta put and call pricing for specific strikes and expiries requires [[deribit]] API access directly. DVOL index, klines, and funding data are available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-intelligence/dvol-history"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

## Related

- [[crypto-options-volatility-selling]] — the canonical baseline short-vol book; this page is the trend-conditional wing-selective variant
- [[funding-conditioned-vol-selling]] — conditions vol entry on funding crowding; this page conditions wing selection on trend; the two can be layered
- [[post-panic-vol-selling]] — conditions vol entry on post-panic sentiment extreme; different timing and trigger from this page
- [[covered-call]] — the retail expression of selling calls in uptrends (long spot + short call); this page is the systematic, delta-hedged options-book version
- [[cash-secured-put]] — the retail expression of selling puts in downtrends or neutral; adjacent logic on the put-sell side
- [[options-premium-selling]] — the general systematic options-premium-selling category
- [[premium-selling-systematic]] — the systematic premium-selling methodology; this page is a trend-gated refinement
- [[vol-targeted-trend-following]] — the trend-following strategy with vol targeting; the trend signal source methodology is adjacent to what this page uses for wing selection
- [[trend-following-cta]] — the canonical trend-following primitive; the trend signal that gates this strategy's wing selection
- [[deribit]] — the primary options execution venue
- [[dvol]] — the DVOL index; IV gate and vol-shock trigger
- [[implied-volatility]] — the concept underlying the IV gate
- [[variance-risk-premium]] — the structural VRP that vol selling harvests
- [[skew-trading]] — the skew asymmetry that trend-aligned selling exploits
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — trend reversal, neutral regime, vol shock
- [[when-to-retire-a-strategy]] — kill vs pause framework
