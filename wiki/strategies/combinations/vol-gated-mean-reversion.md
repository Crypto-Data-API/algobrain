---
title: "Vol-Gated Mean Reversion"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, mean-reversion, volatility, risk-management, position-sizing, quantitative, derivatives, crypto, behavioral-finance]
aliases: ["Vol-Conditioned Reversion", "Vol-Aware Mean Reversion", "Selective Vol-Scaled Reversion", "Conditional Vol Reversion"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, analytical]
edge_mechanism: "Mean-reversion edge is empirically strongest at the moments of highest realized volatility — exactly the moments that naive vol targeting would de-size most aggressively; the correct response is not to scale down uniformly on vol but to apply a signal-quality gate: distinguish high-vol that is high-quality reversion setup (panic overshoot, funding flush, OI flush — mean-reverting driver) from high-vol that is a structural regime break (trending cascade, funding inversion continuation — non-mean-reverting driver), and SIZE DOWN only the latter; the analytical challenge is that both look like high-vol in the raw data."

data_required: [ohlcv-1h, ohlcv-4h, funding-rates, open-interest, atr-14, realized-vol-calc, long-short-ratio]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.16
breakeven_cost_bps: 30

decay_evidence: "The tension between mean-reversion signal quality and volatility is documented in the empirical options and equity literature (Lettau & Ludvigson 2002 on conditional mean reversion; DeMiguel et al. 2009 on regime-conditioning). The specific application to crypto mean-reversion with derivative-market conditioning to distinguish 'good high-vol' from 'bad high-vol' is not in the published literature; it follows directly from the structural logic of funding-flush-reversal and oi-flush-reversion already documented in this wiki."

kill_criteria: |
  - strategy drawdown > 16% from high-water mark
  - rolling 6-month Sharpe < 0 on minimum 20 completed trades
  - reversion entries during HIGH-VOL-GOOD regime produce ≤ 45% win rate across 20+ trades (the good-vol gate is not predicting reversion quality correctly; recalibrate or collapse to standard vol targeting)
  - reversion entries during NORMAL vol regime produce ≤ 45% win rate across 20+ trades (the base reversion signal is degraded; check pair selection or signal type)
  - the HIGH-VOL-GOOD gate fires on fewer than 15% of all HIGH-VOL periods (gate is too restrictive; recalibrate funding/OI thresholds)

related: ["[[mean-reversion]]", "[[session-aware-mean-reversion]]", "[[funding-flush-reversal]]", "[[oi-flush-reversion]]", "[[put-protected-dip-buying]]", "[[vol-targeted-trend-following]]", "[[volatility-targeting]]", "[[narrative-position-vol-targeting]]", "[[regime-adaptive-strategy]]", "[[pullback-trading]]", "[[contrarian-extremes]]", "[[funding-rate]]", "[[open-interest]]", "[[atr]]", "[[realized-volatility]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Vol-Gated Mean Reversion

Vol-gated mean reversion is a **mean-reversion strategy that replaces naive volatility-targeting (scale down positions in high-vol) with a conditional volatility framework**: it distinguishes high-volatility periods that indicate a high-quality reversion setup (panic overshoot, forced liquidation overshoot, funding/OI flush — mean-reverting by mechanism) from high-volatility periods that indicate a structural regime break (cascade continuation, funding inversion, trend acceleration — non-mean-reverting by mechanism). Position sizing responds differently to these two types of high-vol: the strategy sizes UP the first type and DOWN the second. The result is the opposite of naive vol targeting in the reversion-favourable high-vol regime.

**The fundamental tension this page resolves:** mean-reversion edge is empirically largest at moments of highest volatility — panics, forced liquidations, funding flushes. A naive vol-targeting rule (`notional = daily_risk_budget / realized_vol`) would halve or quarter the position size at precisely these highest-expected-value moments. Yet some high-vol events are not reversion setups — they are trending cascades where fading is catastrophically wrong. The solution is not to target vol uniformly but to condition the sizing on the TYPE of high vol.

**This is explicitly differentiated from [[vol-targeted-trend-following]]** — that page applies vol scaling to a directional trend book: lower notional when vol is high, higher when vol is low, targeting constant portfolio daily risk. The direction of the position follows the trend. This page applies vol-conditioned sizing to a COUNTER-TREND book: sizes UP in the high-vol moments with reversion-favourable characteristics, DOWN in the high-vol moments that indicate continuation. The two pages are structural complements — one is for trend books, one is for reversion books.

**This is differentiated from [[session-aware-mean-reversion]]** — that page adjusts reversion parameters by trading session (entry thresholds, take-profit targets scaled to session liquidity). It does not address vol regime. This page addresses the vol regime split; the session timing adjustment can be applied on top.

**This is differentiated from [[funding-flush-reversal]]** and **[[oi-flush-reversion]]** — those pages define specific reversion entry conditions based on funding/OI extremes. They address WHEN the setup occurs. This page addresses HOW MUCH to size those entries — the position sizing discipline that those pages implicitly assume but do not formalise. This page's HIGH-VOL-GOOD regime is precisely the regime in which those entry signals fire; the sizing framework here applies on top.

**This is differentiated from [[pullback-trading]]** — that page enters mean-reversion trades WITHIN an intact trend (higher-timeframe trend intact, entry at pullback). The reversion is short-timeframe within a longer-timeframe trend. This page applies to mean-reversion entries that are COUNTER to the short-term price move, in regimes where reversion is mechanically favoured (funding/OI flush).

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + analytical**:

- **Behavioral (primary)** — the high-quality reversion setups (panic overshoots, forced liquidations, funding flushes) arise because leveraged participants are forced to exit at market prices regardless of fundamental value. The sellers are not information-motivated; they are liquidity-motivated. The counterparty who provides liquidity during the flush earns the liquidity premium and the mean-reversion from fair value. Naive vol targeting reduces position size into these setups, leaving the liquidity premium on the table; the conditional vol framework captures it by sizing UP specifically in this category of forced-liquidation overshoot.
- **Structural** — the crypto perpetuals market creates predictable reversion mechanics: when funding is deeply negative (shorts crowded and paying longs), any price recovery triggers forced short-covering, creating a mechanical mean-reversion catalyst. When OI collapses (a flush), the forced selling has exhausted itself and structural supply overhang is resolved. These are structural reversion catalysts; they are NOT present in trending cascades where funding is normal and OI is building (cascade continuation setup). The structural distinction between these two high-vol types is the core of the conditional framework.
- **Analytical** — the classification of high-vol into "reversion-favourable" vs "continuation-risk" requires simultaneously monitoring funding rate, OI direction, and the vol signal — three independent data streams. This analytical multi-factor conditioning is the overlay's contribution. Practitioners who size purely on price vol miss the structural-catalyst dimension.

## Why this edge exists

**The vol targeting failure mode for reversion:**

A standard vol-targeting framework:
- Low vol (BTC 20-day RV < 30%): target notional = $500 / 0.82% daily = $61,000
- High vol (BTC 20-day RV > 60%): target notional = $500 / 1.64% daily = $30,500

This makes sense for a trend-following book: trend entries in high-vol are riskier and the book should be smaller. But for a mean-reversion book:

**High-vol + funding flush scenario (BTC drops 18% in 36 hours):**
- 20-day RV spikes to 80%
- Funding turns deeply negative: −0.04%/8h (shorts crowded, paying longs)
- OI drops 22% in 24h (leveraged longs flushed)
- This is a HIGH-QUALITY reversion setup: forced selling has exhausted the supply overhang, structural buyers (funding-receiving longs) have strong incentives to enter, and the price overshoot is mechanical, not information-driven

Standard vol targeting says: HALVE the position (RV doubled, so target notional halves)
Conditional vol framework says: SIZE UP — this is the highest-quality reversion entry in the cycle

**High-vol + cascade continuation scenario (BTC drops 8% and is accelerating):**
- 20-day RV rising rapidly (cascade underway but not complete)
- Funding is normal to slightly positive (carry crowd has not been flushed yet)
- OI is RISING (fresh short selling entering, not covering)
- This is a POOR reversion setup: the cascade has structural continuation fuel; fading now means standing in front of a moving train

Standard vol targeting says: REDUCE the position (same as flush scenario)
Conditional vol framework says: SIZE DOWN further — this is a continuation risk, not a reversion setup

The two scenarios look identical from the raw vol signal but are opposite from the reversion-quality perspective.

## Null hypothesis

If reversion entries carry no edge, the conditional multipliers (1.25x flush-confirmed, 0.30x cascade-continuation, 0.10x extreme) merely reweight noise: returns should be statistically indistinguishable from the unconditioned reversion book run at the same average leverage. The vol-state classifier adds value only if flush-confirmed high-vol entries outperform unconditional high-vol entries out-of-sample; if the performance gap disappears once entries are matched by drawdown depth, the gate is proxying entry quality, not adding independent information.

## Rules

### Step 1: Vol regime classification

**Measure realized vol (20-day annualised):**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22` — compute 20-day RV.

**Three vol regimes:**
- **NORMAL-VOL:** 20-day RV < 45% annualised (or ATR(14, 1d) < $1,800 for BTC).
- **HIGH-VOL:** 20-day RV ≥ 45% and < 100%.
- **EXTREME-VOL:** 20-day RV ≥ 100% (cascade or crisis; most mean-reversion strategies paused entirely).

### Step 2: Reversion quality gate (for HIGH-VOL periods only)

In HIGH-VOL periods, classify the vol as GOOD or BAD based on derivative-market signals on the SAME asset:

**HIGH-VOL-GOOD (reversion-favourable — size at or above normal):**
All of the following:
- Funding rate ≤ −0.015%/8h (longs being paid; shorts crowded and paying — flush / overshoot signature) OR 7-day average funding ≤ −0.005%/8h (sustained funding negative)
- OI change over past 24h: ≤ −8% (forced liquidation has cleared supply overhang) OR 48h OI change ≤ −12%
- L/S ratio ≤ 0.85 (retail is bearish — contrarian signal in the reversion context)
- Price is at or below a significant support level (200h EMA, prior weekly low) OR RSI(14, 1h) ≤ 22 (oversold)

**HIGH-VOL-BAD (continuation risk — size down aggressively):**
Any of the following:
- Funding rate ≥ +0.010%/8h AND OI is rising (longs crowded and paying, OI building = fresh directional leverage = cascade fuel)
- OI 24h change ≥ +10% (fresh leverage entering in a high-vol regime = potential cascade)
- Funding unchanged or positive despite a large price decline (the decline is not flushing crowded longs — something more structural is happening)

**UNCLASSIFIED HIGH-VOL:** Conditions present but not meeting either GOOD or BAD criteria → apply standard vol-targeting sizing (reduce position proportionally to vol increase).

### Step 3: Position sizing by regime

| Regime | Sizing rule | Rationale |
|---|---|---|
| **NORMAL-VOL** | Standard sizing: `notional = daily_risk_budget / (RV_daily)` | No special adjustment needed |
| **HIGH-VOL-GOOD** | Full or 1.25× standard notional (capped at max position limit) | Reversion setup confirmed by derivative signals; the vol is from forced selling, not informed selling |
| **HIGH-VOL-BAD** | 25–40% of standard notional OR no new entries | Continuation risk; the reversion signal is unreliable |
| **UNCLASSIFIED HIGH-VOL** | 50–60% of standard notional | Ambiguous; reduce exposure but don't refuse entry |
| **EXTREME-VOL** | 0–20% of standard notional, limit entries to the highest-conviction setups (funding flush + OI flush simultaneously) | Crisis; most mean-reversion entries are continuation traps in these conditions |

**Daily risk budget:** the overall portfolio risk budget for the reversion book (e.g., $500/day on a $100,000 portfolio = 0.50%/day). Standard notional = `$500 / RV_daily`.

### Step 4: Entry conditions

The vol-gated sizing is a wrapper around the underlying mean-reversion entry signal. The page is agnostic about which specific mean-reversion signal is used; common choices from the wiki:
- **[[funding-flush-reversal]]:** funding extreme → reversion long after flush
- **[[oi-flush-reversion]]:** OI collapse → reversion long as forced selling clears
- **[[session-aware-mean-reversion]]:** session-conditioned RSI/VWAP reversion
- **RSI oversold (RSI(14, 1h) ≤ 20):** generic technical mean-reversion

Each of these signals fires most frequently and with highest expected value in the HIGH-VOL-GOOD regime — the regime where this page's conditional framework calls for full sizing. The combination of the mean-reversion signal (WHEN to enter) and the vol-gated sizing (HOW MUCH to enter) is the combination strategy.

### Step 5: Exit conditions

Standard mean-reversion exits:
1. **Profit target:** price recovers to 50–70% of the initial move (RSI normalises, price returns above 200h EMA, or spread z-score normalises to 0.5σ for spread-based reversion).
2. **Stop-loss:** 2.0× the daily risk budget in losses (not a vol-adjusted stop — a fixed dollar stop to limit the downside when the reversion thesis is wrong).
3. **Regime change mid-trade:** if HIGH-VOL-GOOD reclassifies to HIGH-VOL-BAD mid-trade (funding turns positive + OI starts building mid-decline), exit the reversion trade immediately.

## Implementation pseudocode

```python
# vol_gated_mean_reversion.py
from dataclasses import dataclass
from typing import Literal
import numpy as np

VolRegime = Literal["NORMAL", "HIGH_GOOD", "HIGH_BAD", "HIGH_UNCLASSIFIED", "EXTREME"]

# ---- vol thresholds ----
NORMAL_VOL_MAX       = 0.45    # annualised RV; below = NORMAL-VOL
EXTREME_VOL_MIN      = 1.00    # annualised RV; above = EXTREME-VOL

# ---- HIGH-VOL-GOOD conditions ----
FUNDING_FLUSH_MIN    = -0.00015   # -0.015%/8h (longs paid; shorts flush)
FUNDING_AVG_FLUSH    = -0.00005   # 7d avg -0.005%/8h
OI_FLUSH_24H         = -0.08      # -8% in 24h
OI_FLUSH_48H         = -0.12      # -12% in 48h
LS_BEARISH           = 0.85       # L/S <= 0.85 (retail bearish = contrarian signal)
RSI_OVERSOLD         = 22         # RSI(14, 1h) <= 22

# ---- HIGH-VOL-BAD conditions ----
FUNDING_CROWDED_MIN  = 0.00010    # +0.010%/8h (longs crowded and paying)
OI_BUILD_24H         = 0.10       # +10% in 24h (fresh leverage entering)

# ---- sizing multipliers ----
SIZE_MULT = {
    "NORMAL":           1.00,
    "HIGH_GOOD":        1.25,
    "HIGH_BAD":         0.30,
    "HIGH_UNCLASSIFIED": 0.55,
    "EXTREME":          0.10,
}

@dataclass
class MarketCondition:
    rv_20d_annual: float          # 20-day annualised realized vol
    funding_8h: float             # current 8h funding rate (decimal)
    funding_7d_avg: float         # 7-day average 8h funding rate
    oi_change_24h: float          # fractional OI change (24h)
    oi_change_48h: float          # fractional OI change (48h)
    ls_ratio: float               # long/short ratio
    rsi_1h: float                 # RSI(14) on 1h chart

def classify_vol_regime(c: MarketCondition) -> tuple[VolRegime, str]:
    """Classify the current vol regime for mean-reversion sizing."""
    if c.rv_20d_annual >= EXTREME_VOL_MIN:
        return "EXTREME", f"extreme vol: RV={c.rv_20d_annual:.0%}"

    if c.rv_20d_annual < NORMAL_VOL_MAX:
        return "NORMAL", f"normal vol: RV={c.rv_20d_annual:.0%}"

    # HIGH-VOL: check GOOD vs BAD
    good_score = 0
    bad_score = 0

    if c.funding_8h <= FUNDING_FLUSH_MIN or c.funding_7d_avg <= FUNDING_AVG_FLUSH:
        good_score += 1
    if c.oi_change_24h <= OI_FLUSH_24H or c.oi_change_48h <= OI_FLUSH_48H:
        good_score += 1
    if c.ls_ratio <= LS_BEARISH:
        good_score += 0.5
    if c.rsi_1h <= RSI_OVERSOLD:
        good_score += 0.5

    if c.funding_8h >= FUNDING_CROWDED_MIN and c.oi_change_24h >= OI_BUILD_24H:
        bad_score += 2
    elif c.funding_8h >= FUNDING_CROWDED_MIN:
        bad_score += 1
    elif c.oi_change_24h >= OI_BUILD_24H:
        bad_score += 1

    if bad_score >= 2:
        return "HIGH_BAD", f"continuation risk: funding={c.funding_8h:.4%}, OI24h={c.oi_change_24h:.1%}"
    if good_score >= 2:
        return "HIGH_GOOD", f"reversion setup: flush confirmed (score={good_score:.1f})"
    return "HIGH_UNCLASSIFIED", f"ambiguous high-vol: good_score={good_score:.1f}, bad_score={bad_score}"

def compute_target_notional(
    c: MarketCondition,
    daily_risk_budget: float,
    max_notional: float,
) -> dict:
    regime, reason = classify_vol_regime(c)
    size_mult = SIZE_MULT[regime]

    rv_daily = c.rv_20d_annual / np.sqrt(365)
    if rv_daily <= 0:
        return {"regime": regime, "notional": daily_risk_budget, "note": "rv=0, use budget as notional"}

    base_notional = daily_risk_budget / rv_daily
    target = min(base_notional * size_mult, max_notional)

    return {
        "regime": regime,
        "regime_reason": reason,
        "size_multiplier": size_mult,
        "base_notional": round(base_notional, 0),
        "target_notional": round(target, 0),
        "rv_daily_pct": round(rv_daily * 100, 3),
        "note": f"{regime} × {size_mult:.2f} = ${target:,.0f}",
    }
```

The production system adds: a real-time vol-regime classification that runs at each potential mean-reversion entry signal; a log of regime classifications and subsequent trade outcomes for ongoing threshold calibration; an alert when HIGH-VOL-GOOD is active (the most important regime for reversion entry); and a monthly audit comparing the win rate and average P&L by regime classification to verify the conditional framework is adding value over naive vol targeting.

## Indicators / data used

- **20-day realized volatility** — computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22`; primary vol regime input.
- **8h funding rate** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; key distinguisher between HIGH-VOL-GOOD (flush, negative funding) and HIGH-VOL-BAD (crowded longs, positive funding).
- **7-day average funding** — computed from the same funding-rates endpoint over the past 21 8h periods.
- **Open interest (24h and 48h change)** — `GET /api/v1/derivatives/open-interest?coin=BTC`; OI flush confirmation for HIGH-VOL-GOOD; OI build warning for HIGH-VOL-BAD.
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio?coin=BTC`; contrarian sentiment confirmation in the HIGH-VOL-GOOD regime.
- **1h OHLCV (for RSI)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=16`; RSI(14, 1h) oversold check for HIGH-VOL-GOOD supplementary confirmation.
- **Regime context** — `GET /api/v1/regimes/current`; if `Structural_Shock`, no reversion entries regardless of vol regime classification.

## Example trade

**Setup: BTC 20-day RV = 72% (HIGH-VOL). Classification determines sizing.**

*Portfolio: $100,000. Daily risk budget: $500 (0.50%). Max reversion notional: $30,000.*

**Signal fired: BTC drops 15% over 48h. RSI(14, 1h) = 18 (oversold).**

**Scenario A — HIGH-VOL-GOOD:**
- Funding: −0.028%/8h (shorts paying; flush signature)
- 48h OI change: −16% (forced selling cleared)
- L/S: 0.78 (retail heavily bearish)
- Vol regime: HIGH-VOL-GOOD (good_score = 3.0)
- RV daily: 72%/√365 = 3.77%
- Base notional: $500 / 3.77% = $13,263. × 1.25 = **$16,579 position size**
- Entry: long BTC perp at $55,000. Stop: $500 × 2 = $1,000 loss limit → stop at $54,940 (0.11% below entry, wide for a position of this size — the daily vol budget is the limit, not a price-based stop)
- Over 3 days, BTC recovers to $58,500. Funding normalises to +0.01%/8h.
- Exit at RSI ≥ 50 and funding positive: **+6.4% on $16,579 = +$1,061 gross. Less 30 bps = −$50. Net: +$1,011 / +1.0% of portfolio.**

**Scenario B — HIGH-VOL-BAD (same price signal, different derivatives):**
- Same −15% decline. But: funding = +0.015%/8h AND 24h OI change = +14% (fresh shorts entering; cascade may continue)
- Vol regime: HIGH-VOL-BAD (bad_score = 2)
- Base notional: $13,263. × 0.30 = **$3,979 position size** (or NO entry if confidence is low)
- Entry small if any: risk is limited; position held with 2× tighter stop

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Higher than naive vol-targeted reversion; primarily from capturing full-sized HIGH-VOL-GOOD entries that naive vol targeting would have undersized |
| Expected max drawdown | ~16% | Aggressive HIGH-VOL-GOOD sizing carries drawdown risk from the subset of flush signals that turn into continuations; the stop-loss budget limits single-trade losses |
| Win rate in HIGH-VOL-GOOD | ~60–65% (target) | The regime classification should substantially outperform the unconditional reversion win rate |
| Win rate in HIGH-VOL-BAD | ~40–45% (expected) | These entries are expected to underperform; small sizing limits damage |
| Breakeven cost | 30 bps | Taker fills in high-vol periods; slippage on stop exits |

## Capacity limits

`capacity_usd: 20,000,000` — limited by the liquidity of the mean-reversion entry at the flush signal. Reversion entries in HIGH-VOL-GOOD regimes are typically in distressed market conditions where bid-ask is wide. Above $20M notional, market-impact on entry and exit dominates the per-trade P&L. Below $10,000, operational overhead is disproportionate.

## What kills this strategy

1. **HIGH-VOL-GOOD misclassification (#6: Complexity).** The classification scores (funding flush + OI flush + L/S extreme) may fire on the first wave of a multi-wave decline. A genuine cascade has multiple legs; the first OI flush does not guarantee the decline is over. The RSI oversold gate adds a price-level confirmation, but a deeply trending market can stay oversold for extended periods. The stop-loss budget ($1,000 = 2× daily risk) is the practical limit on per-trade loss when misclassification occurs.
2. **Cascade continuation after apparent flush (#3: Market-structure change).** The most dangerous scenario: OI drops sharply (flush signal), funding turns negative (confirms flush), but the cascade was triggered by a structural event (exchange insolvency, regulatory action, large protocol failure) that removes a permanent flow of buyers. The flush is real, but there is no mean-reversion catalyst to bring buyers back. The regime kill (`Structural_Shock` in `GET /api/v1/regimes/current`) partially addresses this, but classification lag is a risk.
3. **Funding signal noise in low-liquidity periods (#7: Operational).** Overnight or weekend sessions can produce negative funding not from a genuine flush but from reduced funding-payer participation. The 7-day average funding gate (> −0.005%/8h) reduces but does not eliminate false HIGH-VOL-GOOD signals in thin markets.
4. **Correlation between the classification criteria and the mean-reversion signal.** If the underlying mean-reversion entry signal (e.g., [[funding-flush-reversal]]) uses the same funding data as the vol-regime classification, the two layers are correlated. This is intended — both layers are conditioning on the same underlying mechanics — but it means the classification does not add truly independent information on top of the entry signal. The value is in the sizing discipline, not in generating a fundamentally new signal.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 16%** — review whether losses are concentrated in HIGH-VOL-GOOD entries (misclassification risk) or HIGH-VOL-BAD entries (sizing not small enough).
2. **Rolling 6-month Sharpe < 0** on minimum 20 trades — the base reversion signal is degraded; assess the underlying entry strategy.
3. **HIGH-VOL-GOOD win rate ≤ 45% across 20+ trades** — the regime classification is not adding information; collapse to naive vol targeting or adjust the classification thresholds.
4. **HIGH-VOL-GOOD gate fires on fewer than 15% of HIGH-VOL periods** — the gate is too restrictive; the strategy is effectively always in HIGH-VOL-BAD during high-vol periods, which means it is barely trading during the highest-expected-value windows.

See [[when-to-retire-a-strategy]] and [[failure-modes]] for the broader framework.

## Advantages

- **Captures the highest-expected-value reversion entries at appropriate size.** Panic and flush-driven reversion setups are the highest-expected-value entries in the mean-reversion category. Naive vol targeting systematically undersizes them. This conditional framework ensures the full risk budget is deployed when the mechanical basis for reversion is strongest.
- **Protects against the worst reversion entries (continuation traps).** By sizing down aggressively in HIGH-VOL-BAD regimes, the strategy avoids the trap of fading a continuation cascade. The systematic discipline replaces the discretionary judgment "is this a real flush or a falling knife?" with a measurable multi-factor gate.
- **Compatible with all reversion entry signals.** The vol-gated sizing is signal-agnostic: it applies on top of [[funding-flush-reversal]], [[oi-flush-reversion]], [[session-aware-mean-reversion]], or any other reversion entry mechanism. The sizing overlay enhances any reversion entry without replacing it.
- **Converts the mean-reversion book's inherent negative-skew into a better-shaped distribution.** Naive reversion has positive skew on small wins and negative skew on large losses (continuation traps). This framework captures more of the large-win setups (HIGH-VOL-GOOD with full sizing) while limiting the large losses (HIGH-VOL-BAD with small sizing), improving the distribution shape.

## Disadvantages

- **Classification complexity.** Three simultaneous inputs (funding, OI, L/S) with thresholds require real-time monitoring and reliable data. A data outage during a high-vol event — exactly when the classification matters most — prevents the sizing adjustment. Fallback: treat as UNCLASSIFIED (50% sizing) on any data gaps.
- **Classification cannot prevent all misclassifications.** The flush signal is not a guarantee of mean-reversion. Some flush signals precede further declines. The stop-loss budget provides the safety net, but the strategy will have a subset of HIGH-VOL-GOOD entries that lose.
- **Oversizing in HIGH-VOL-GOOD increases single-trade loss if wrong.** The 1.25× size in HIGH-VOL-GOOD regimes means a failed reversion trade loses 1.25× more than a NORMAL-VOL trade. The 2× daily risk budget stop-loss limits this, but the stop is wider in dollar terms than a NORMAL-VOL entry (same budget, larger notional = wider stop in price terms).
- **Not universally applicable across all mean-reversion assets.** The classification criteria (funding, OI, L/S) are specific to crypto perpetuals. For spot-only mean reversion or mean reversion on assets without funding/OI markets (small altcoins without liquid perps), this classification is not available and the strategy defaults to naive vol targeting.

## Sources

- [[funding-flush-reversal]] — the canonical funding-based reversion entry signal; this page provides the sizing framework that entry signal uses in high-vol conditions.
- [[oi-flush-reversion]] — the OI-based reversion entry signal; the OI classification gate in this page directly references the same OI dynamics.
- [[vol-targeted-trend-following]] — the vol-targeting framework for trend books; this page applies the same daily-risk-budget logic to a reversion book with a conditional multiplier by vol type.
- [[session-aware-mean-reversion]] — session-conditional reversion parameter adjustment; composable with this page's vol-regime sizing as complementary dimensions (session timing + vol regime conditioning).
- [[put-protected-dip-buying]] — the tail-protected version of the HIGH-VOL-GOOD reversion entry (adds an OTM put as a contractual floor); the vol-gated sizing in this page is an alternative approach that manages downside through position sizing rather than a purchased option.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22` — 20-day daily OHLCV for realized vol computation (vol regime classification input)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding rate; key HIGH-VOL-GOOD vs HIGH-VOL-BAD distinguisher
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI 24h and 48h change; flush confirmation (GOOD) or build warning (BAD)
- `GET /api/v1/derivatives/binance/long-short-ratio?coin=BTC` — L/S ratio; contrarian positioning confirmation in HIGH-VOL-GOOD
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=16` — 1h OHLCV for RSI(14, 1h) oversold check
- `GET /api/v1/regimes/current` — regime context; `Structural_Shock` → no reversion entries

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — annual daily closes for vol regime calibration and backtesting HIGH-VOL-GOOD gate thresholds
- `GET /api/v1/derivatives/binance/history?days=90` — historical funding and OI for classification threshold calibration

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — daily klines classify the vol regime (20-day realised vol) and 1h klines run the RSI oversold trigger
- **Gate** — `GET /api/v1/derivatives/funding-rates?coin=BTC`, `GET /api/v1/derivatives/open-interest?coin=BTC` (flush vs build), and the long/short ratio separate HIGH-VOL-GOOD (flush — fade it) from HIGH-VOL-BAD (build — stand aside)
- **Regime gate** — `GET /api/v1/regimes/current`; no reversion entries in `Structural_Shock`
- **Backtest** — vol-regime replay on `GET /api/v1/backtesting/klines` (1d/1h back to 2017-08); the GOOD/BAD classification replays via `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30) — before 2023 only the price leg is testable
- **Tips** — the GOOD/BAD split is the edge; log the classification at every entry so live hit-rates per class can be compared against the backtest split

## Related

- [[mean-reversion]] — the canonical mean-reversion primitive
- [[session-aware-mean-reversion]] — session-conditional reversion parameters; composable with this page's vol-regime sizing
- [[funding-flush-reversal]] — the funding-flush reversion entry signal; this page provides the conditional sizing framework for those entries
- [[oi-flush-reversion]] — the OI-flush reversion entry signal; the OI gate in this page directly enhances those entries
- [[put-protected-dip-buying]] — tail-protected reversion with an OTM put; structural alternative to vol-gated sizing for protecting the downside
- [[pullback-trading]] — HTF-trend-gated reversion (with-trend entries); different regime from this page's counter-trend flush entries
- [[vol-targeted-trend-following]] — vol targeting on the trend book; structural complement (trend book + reversion book with different vol-response logic)
- [[volatility-targeting]] — portfolio-level vol targeting; the framework this page extends and conditionalises
- [[narrative-position-vol-targeting]] — vol targeting on high-vol narrative positions; the same daily-risk-budget sizing in a different context
- [[regime-adaptive-strategy]] — broader regime-switching framework; this page's HIGH/NORMAL/EXTREME regimes are a specialised reversion sub-classification
- [[contrarian-extremes]] — sentiment-extreme reversion; related approach using sentiment rather than funding/OI for flush confirmation
- [[funding-rate]] — the core flush-signal input
- [[open-interest]] — the OI flush/build input
- [[realized-volatility]] — the vol regime input
- [[edge-taxonomy]] — behavioral + structural + analytical classification
- [[failure-modes]] — misclassification, cascade continuation, data latency
- [[when-to-retire-a-strategy]] — kill vs pause framework
