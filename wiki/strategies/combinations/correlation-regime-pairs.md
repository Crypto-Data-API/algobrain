---
title: "Correlation-Regime Pairs"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, pairs-trading, arbitrage, regime-detection, mean-reversion, quantitative, crypto, derivatives, correlation]
aliases: ["Regime-Gated Stat Arb", "Cointegration-Regime Pairs", "Correlation-Conditional Spread Trading"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, analytical, structural]
edge_mechanism: "Retail and directional momentum traders push co-moving crypto pairs into temporary spread dislocations during periods when the cointegrating relationship is intact; by requiring a rolling correlation floor, cointegration test significance, and spread half-life within bounds before entering — and flattening immediately on correlation breakdown rather than averaging into a structurally broken spread — the strategy earns only the reversion that is supported by a live structural anchor, not the phantom reversion of a decoupled pair."

data_required: [ohlcv-1h, ohlcv-daily, funding-rates, open-interest, rolling-correlation, cointegration-p-value, spread-half-life]
min_capital_usd: 20000
capacity_usd: 30000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

decay_evidence: "Crypto pairs-trading has decayed slowly since 2020 as more stat-arb capital has entered the space, tightening spreads on canonical pairs (BTC/ETH, major L1s). The regime-conditioning layer — requiring live cointegration and correlation stability — has no published dedicated study, but research on regime-conditioned pairs in equities (Do & Faff 2012, Rad et al. 2016) shows that conditioning on spread half-life and cointegration stability reduces the frequency of trap-trades during decoupling events."

kill_criteria: |
  - strategy drawdown > 20% from high-water mark
  - rolling 6-month net Sharpe < 0 on a minimum of 15 completed pairs cycles
  - cointegration p-value of all primary pairs deteriorates beyond 0.15 on a 90-day rolling window for 60+ consecutive days (structural anchor persistently absent)
  - rolling correlation of primary pairs falls below floor on 80%+ of trading days over a 30-day window (regime gate is blocking all entries; pairs may be permanently decoupled)
  - realized spread half-life > 2× the modeled half-life on a 40-trade sample (OU model is mis-calibrated; revert to pure z-score or pause)

related: ["[[pairs-trading]]", "[[pairs-with-funding-differential]]", "[[stat-arb]]", "[[ornstein-uhlenbeck]]", "[[cointegration]]", "[[regime-detection]]", "[[regime-adaptive-strategy]]", "[[hl-vs-cex-funding-divergence]]", "[[statistical-arbitrage]]", "[[vol-regime-detection]]", "[[spread-trading]]", "[[augmented-dickey-fuller]]", "[[mean-reversion]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Correlation-Regime Pairs

Correlation-regime pairs is a [[pairs-trading|stat-arb/pairs]] strategy that runs spread entries **only while the pair's cointegrating relationship is demonstrably active**: rolling correlation above a calibrated floor (typically ≥ 0.70 on a 30-day window), the Engle-Granger or Johansen cointegration test still passing at p < 0.10, and the [[ornstein-uhlenbeck|spread half-life]] within an acceptable bound (≥ 3 days and ≤ 45 days for a swing book). On any breakdown of these conditions — correlation falling, test failing, half-life blowing out — the strategy flattens all open pairs positions immediately rather than averaging into a spread that may be structurally broken. The primitive edge is stat-arb reversion; the overlay is a continuous regime gate that licenses deployment only while the structural anchor behind the spread is empirically intact.

This is explicitly differentiated from [[pairs-with-funding-differential]] (B2 page) — that strategy gates spread entries on whether the funding differential between perp legs agrees with the spread direction, earning carry alongside mean-reversion. This page focuses instead on the **cointegration regime itself** as the entry gate: it asks whether the structural relationship that makes the spread mean-reverting is currently alive, not whether entry timing is funded-side-favourable. A pair can be cointegrated but have an unfavourable funding differential (pairs-with-funding-differential would pass on it); a pair can have a favourable funding differential but a degraded cointegration regime (this page would pass on it). The two pages are complementary filters and can be layered.

This is differentiated from [[regime-adaptive-strategy]] — that page selects which strategy family to deploy based on the macro market regime (trending, ranging, volatile). This page operates *within* the pairs/stat-arb family and gates on the pair's own internal statistical regime (cointegration stability, correlation stability), not on the broad market regime.

This is differentiated from [[ornstein-uhlenbeck]] — that page provides the modeling framework (OU process parameters: speed, mean, vol; half-life estimation). This page is an operational combination strategy that uses the OU half-life as one component of a multi-factor regime gate, combined with correlation and cointegration tests, and specifies the full entry/exit/flatten logic.

## Edge source

Per [[edge-taxonomy]], **behavioral + analytical + structural**:

- **Behavioral (primary)** — directional retail and momentum traders drive temporary dislocations in correlated crypto pairs via leverage, narrative rotation, and short-term sentiment. In crypto, pairs that share BTC/ETH beta or sector exposure (e.g. two L1s, two DEX tokens) tend to co-move structurally, so price divergences driven by these transient behavioural flows are mean-reverting. The counterparty is the momentum trader who broke the spread by chasing a narrative on one leg.
- **Analytical (secondary)** — the regime gate — rolling correlation, cointegration test, OU half-life — is an analytical overlay that identifies which dislocations are likely to revert vs. which represent genuine structural change. Most pair breakdowns in crypto are temporary (narrative rotation); a minority are permanent (one asset gains structural superiority via a protocol upgrade, regulation-driven delisting, or capital structure change). The analytical layer discriminates these cases.
- **Structural** — when cointegration holds, there is a structural anchor (shared BTC beta, shared liquidity pool, shared sector narrative) that forces convergence regardless of short-term flow. Being on the right side of that anchor — long the depressed leg, short the inflated leg — earns a structural bid as the anchor pulls the spread back.

## Why this edge exists

**Three failure modes of naive pairs trading that the regime gate removes:**

1. **Trap-trade into permanent decoupling.** Crypto pairs frequently exhibit *structural breaks* — when ETH transitions from PoW to PoS, or a major L1 suffers an exploit, the relationship with its previous correlation partners permanently shifts. Naive z-score-based pairs trading enters the spread just as it is breaking down, averaging into a trade that never reverts. The cointegration regime gate detects this: the p-value of the cointegration test rises as the structural anchor weakens, blocking entry before the full decoupling occurs.

2. **Half-life blowout.** The [[ornstein-uhlenbeck]] model's mean-reversion speed (θ) can shift dramatically when regime conditions change. A pair that normally reverts in 5 days may suddenly exhibit a half-life of 60+ days following a sector rotation. Entering on a 2σ z-score with a 60-day half-life requires holding the spread for weeks while paying funding costs and carrying directional risk — the carry cost alone can erase the expected P&L. The half-life gate (≤ 45 days) blocks these slow-reversion entries.

3. **Correlation collapse with residual z-score signal.** Rolling correlation can fall sharply (from 0.85 to 0.40) while the z-score is still at a 2σ extreme — the spread is wide in z-score terms but the asset pair is no longer co-moving, so the spread can widen further indefinitely. The correlation floor blocks entries when the pairs relationship is empirically absent, even if the historical parameters suggest an extreme.

**Who is on the other side:** the momentum or narrative trader who pushed one leg relative to the other on transient sentiment, and who will eventually rotate back to the beta-correlated equilibrium when the narrative fades.

## Null hypothesis

Under the null, correlation regime state and cointegration test results at the time of entry carry **no incremental predictive power** over a naive z-score-based pairs entry. Specifically:
- Average forward 10-day spread return (toward zero) should be equal for z-score entries made when the regime gate passes vs. when it fails.
- Win rate (spread reaching within 0.5σ of zero within 15 days) should not differ between gated and ungated z-score entries.
- Maximum adverse excursion (spread widening further before reverting) should not be lower for regime-gated entries.

Currently not rejected (`backtest_status: untested`). Testable prediction: on a multi-year BTC/ETH and major L1-pair dataset, classify all 2σ+ spread entries by regime state (correlation ≥ 0.70, cointegration p < 0.10, half-life 3–45 days). Predict that gated entries show meaningfully higher win rate and lower max adverse excursion than ungated entries.

## Rules

### Regime gate — must ALL pass before any spread entry

**Gate 1: Rolling correlation floor**
- Compute 30-day rolling Pearson correlation of log-returns for the two legs.
- Required: correlation ≥ **0.70**.
- Re-check daily; if correlation falls below 0.60 while a spread position is open → immediate flatten of all legs.

**Gate 2: Cointegration test significance**
- Run Engle-Granger two-step cointegration test on a rolling 90-day window of daily close prices.
- Required: ADF test on the residual with p-value ≤ **0.10** (spread is stationary at 10% significance).
- Alternative: Johansen trace test on 90-day window; require at least 1 cointegrating vector at 5% significance.
- Re-run weekly; if test fails for 5 consecutive daily checks → immediate flatten of open positions.

**Gate 3: Half-life within bounds**
- Fit the [[ornstein-uhlenbeck]] model to the 60-day spread: estimate θ (reversion speed); compute half-life = ln(2) / θ.
- Required: half-life **≥ 3 days AND ≤ 45 days**.
  - Half-life < 3 days: spread reverts too quickly; execution costs eat the signal.
  - Half-life > 45 days: spread reverts too slowly; funding costs and directional risk accumulate beyond the breakeven budget.

### Spread entry (z-score signal)

1. **Compute spread:** using the cointegration hedge ratio (β from Engle-Granger OLS) as the leg ratio. Z-score of the spread vs its 60-day rolling mean and std.
2. **Entry threshold:** z-score ≥ **+2.0σ** (short the overperformer, long the underperformer) or ≤ **−2.0σ** (reverse). Do not enter above ±3.5σ without confirmation of no regime break.
3. **All three regime gates must pass** on the entry day.
4. **Funding gate (optional, from [[pairs-with-funding-differential]]):** if funding differential between legs agrees with spread direction (funding on the short leg is higher → earn carry), prefer this entry. If funding disagrees, require a stronger z-score threshold (±2.5σ).

### Position sizing

- **Spread notional per pair:** 2.5% of the strategy sleeve per active pair (leg-adjusted notional by hedge ratio).
- **Maximum concurrent pairs:** 4 (total 10% of sleeve at full deployment).
- Each leg sized to be delta-neutral on the spread level (use hedge ratio β from the cointegration OLS).

### Exit conditions

1. **Profit target:** z-score reverts to within **±0.5σ** of zero — close both legs.
2. **Regime breakdown exit:** any gate fails during the hold → close both legs immediately, at market, no waiting for z-score target.
3. **Hard stop:** spread widens to **±3.5σ** and has been open for ≥ 3 days with no sign of reversion → close. (Do not average in; a spread at ±3.5σ after 3 days is likely a regime-breaking event.)
4. **Time stop:** close if spread has not reverted within **30 calendar days**.

## Implementation pseudocode

```python
# correlation_regime_pairs.py

from dataclasses import dataclass, field
from typing import Optional
import numpy as np
from scipy import stats

# ---- thresholds ----
CORR_FLOOR           = 0.70   # 30-day rolling correlation minimum
CORR_BREAK_FLOOR     = 0.60   # immediate flatten threshold
COINT_P_MAX          = 0.10   # max ADF p-value on residual
COINT_FAIL_DAYS      = 5      # consecutive days of test failure → flatten
HALFLIFE_MIN_DAYS    = 3.0    # minimum OU half-life
HALFLIFE_MAX_DAYS    = 45.0   # maximum OU half-life
ZSCORE_ENTRY         = 2.0    # z-score entry threshold
ZSCORE_WIDE_ENTRY    = 2.5    # z-score entry if funding disagrees
ZSCORE_STOP          = 3.5    # hard stop widening
ZSCORE_EXIT          = 0.5    # z-score exit target
TIME_STOP_DAYS       = 30
SIZE_PCT_PER_PAIR    = 0.025  # 2.5% of sleeve per pair
MAX_CONCURRENT_PAIRS = 4

@dataclass
class PairRegimeState:
    corr_30d: float               # 30-day rolling Pearson correlation of log-returns
    coint_p_value: float          # ADF p-value on cointegration residual
    coint_fail_streak: int        # consecutive days coint test has failed
    ou_halflife_days: float       # OU process half-life (ln(2)/theta)
    spread_zscore: float          # current spread z-score
    hedge_ratio: float            # OLS beta for leg sizing
    funding_diff_agrees: bool     # True if funding differential supports spread direction

def regime_gate_passes(s: PairRegimeState) -> tuple[bool, str]:
    """Returns (passes, reason_if_fails)."""
    if s.corr_30d < CORR_FLOOR:
        return False, f"correlation {s.corr_30d:.2f} below floor {CORR_FLOOR}"
    if s.coint_p_value > COINT_P_MAX:
        return False, f"cointegration p={s.coint_p_value:.3f} not significant"
    if s.coint_fail_streak >= COINT_FAIL_DAYS:
        return False, f"cointegration test failed {s.coint_fail_streak} consecutive days"
    if not (HALFLIFE_MIN_DAYS <= s.ou_halflife_days <= HALFLIFE_MAX_DAYS):
        return False, f"OU half-life {s.ou_halflife_days:.1f}d outside [{HALFLIFE_MIN_DAYS}, {HALFLIFE_MAX_DAYS}]"
    return True, ""

def regime_breakdown_requires_flatten(s: PairRegimeState) -> bool:
    """Hard flatten triggers (use in mid-hold monitoring)."""
    return (s.corr_30d < CORR_BREAK_FLOOR or
            s.coint_fail_streak >= COINT_FAIL_DAYS)

def entry_decision(s: PairRegimeState, book: dict, pair_id: str) -> dict:
    if book.get("drawdown", 0) > 0.20:
        return {"action": "FLAT", "reason": "drawdown kill"}

    gate_ok, gate_reason = regime_gate_passes(s)
    if not gate_ok:
        return {"action": "WAIT", "pair": pair_id, "reason": gate_reason}

    n_active = book.get("active_pairs", 0)
    if n_active >= MAX_CONCURRENT_PAIRS:
        return {"action": "WAIT", "pair": pair_id, "reason": "max concurrent pairs reached"}

    threshold = ZSCORE_ENTRY if s.funding_diff_agrees else ZSCORE_WIDE_ENTRY
    if abs(s.spread_zscore) < threshold:
        return {"action": "WAIT", "pair": pair_id,
                "reason": f"|z|={abs(s.spread_zscore):.2f} < threshold {threshold}"}

    direction = "SHORT_A_LONG_B" if s.spread_zscore > 0 else "LONG_A_SHORT_B"
    notional_per_leg = book["sleeve_capital"] * SIZE_PCT_PER_PAIR

    return {
        "action":         "ENTER_SPREAD",
        "pair":           pair_id,
        "direction":      direction,
        "notional":       notional_per_leg,
        "hedge_ratio":    s.hedge_ratio,
        "zscore":         s.spread_zscore,
        "ou_halflife":    s.ou_halflife_days,
        "regime_ok":      True,
        "note": (f"z={s.spread_zscore:.2f}, corr={s.corr_30d:.2f}, "
                 f"coint_p={s.coint_p_value:.3f}, hl={s.ou_halflife_days:.1f}d"),
    }

def exit_decision(pos: dict, s: PairRegimeState, days_held: int) -> Optional[dict]:
    if regime_breakdown_requires_flatten(s):
        return {"action": "FLATTEN_MARKET",
                "reason": f"regime breakdown: corr={s.corr_30d:.2f} or coint fail {s.coint_fail_streak}d"}
    if abs(s.spread_zscore) >= ZSCORE_STOP and days_held >= 3:
        return {"action": "FLATTEN_MARKET",
                "reason": f"hard stop: spread widened to z={s.spread_zscore:.2f} after {days_held}d"}
    if abs(s.spread_zscore) <= ZSCORE_EXIT:
        return {"action": "CLOSE_TARGET", "reason": f"z-score reverted to {s.spread_zscore:.2f}"}
    if days_held >= TIME_STOP_DAYS:
        return {"action": "CLOSE_TIME", "reason": f"30-day time stop"}
    return None
```

The production system adds: daily re-estimation of the cointegration OLS and ADF test via a rolling 90-day window; real-time spread tracking via WebSocket klines for the two legs; a PIT (point-in-time) discipline for the hedge ratio (never re-fit during a live trade); and a pre-trade audit that checks book depth on both legs to ensure no market-impact at entry.

## Indicators / data used

- **OHLCV (1h and daily)** — `/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=200` for spread construction and regime estimation; daily for ADF test input.
- **Rolling Pearson correlation (30-day)** — computed from the 1h or daily klines. No dedicated CDA endpoint; compute from klines response.
- **Cointegration test p-value** — Engle-Granger ADF on residuals, or Johansen trace; computed from the 90-day daily klines. No CDA endpoint; compute from klines.
- **OU half-life** — AR(1) fit on the spread: `ln(2) / abs(log(b))` where b is the AR(1) coefficient. Sourced from the [[ornstein-uhlenbeck]] model fitted to the spread series from klines.
- **Funding rates (for optional gate)** — `/api/v1/derivatives/funding-rates?coin=BTC` and equivalent for the counterpart leg; used as the optional funding-differential confirmation.
- **Open interest** — `/api/v1/derivatives/open-interest?coin=BTC` — OI context to identify regime shifts (OI collapsing as correlation breaks is an additional warning signal).
- **Regime classification** — `/api/v1/regimes/current` — macro regime check; avoid entering new pairs in `Structural_Shock`.

## Example trade

**Setup (illustrative — BTC/ETH pairs spread):**

- Date: a typical crypto mid-bull period.
- **Regime check:** 30-day rolling BTC/ETH log-return correlation = 0.78 (passes ≥ 0.70). Cointegration ADF p-value on 90-day residuals = 0.042 (passes ≤ 0.10). OU half-life estimated at 8.4 days (passes 3–45 day range).
- **Spread z-score:** ETH has outperformed BTC by +4.2% over 3 days. Spread z-score = +2.3σ (ETH expensive relative to BTC on the cointegrating relationship; short ETH / long BTC).
- **Funding gate (optional):** ETH perp funding = 0.055%/8h; BTC perp funding = 0.030%/8h. Funding differential: long BTC (cheaper) and short ETH (higher funding received). Differential agrees with spread direction. Use standard 2.0σ threshold.
- **Sleeve:** $100,000. Size per pair: 2.5% = $2,500 per leg.
- **Hedge ratio (β):** OLS coefficient from 90-day regression = 0.72 (ETH moves 0.72× BTC per unit). Short ETH notional = $2,500; long BTC notional = $2,500 × 0.72 ≈ $1,800.

**Entry (Day 1):**
- Short ETH-PERP at $3,420. $2,500 notional = 0.731 ETH.
- Long BTC-PERP at $62,400. $1,800 notional = 0.0288 BTC.
- Total notional: $4,300 (5% of sleeve across both legs combined).

**Hold (9 days):** spread reverts as ETH underperforms. By Day 9:
- ETH-PERP at $3,290 (−3.8% from entry). PnL on short ETH leg: +$96.
- BTC-PERP at $63,100 (+1.1% from entry). PnL on long BTC leg: +$20.
- Z-score reverts to +0.3σ — triggers profit-target exit.
- Funding collected (short ETH × 9 days × ~3 funding periods/day × 0.055%/period): ~$37.
- Gross P&L: +$96 + $20 + $37 = **+$153** on $4,300 deployed (+3.6%).
- Transaction costs (4 fills × 5 bps taker): ~$9.
- **Net P&L: +$144** (+3.4% on deployed notional, +0.14% on $100K sleeve).

**Regime-breakdown scenario:** if on Day 4 the 30-day correlation dropped to 0.55 (below 0.60 hard flatten level):
- Immediate market exit both legs at Day 4 price.
- Partial loss scenario: spread only partially reverted → small net gain or scratch trade. The key benefit: avoided sitting in a 30-day hold on a permanently decoupled pair.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Regime gating reduces trade frequency but improves per-trade quality; blended including carry on favourably funded pairs |
| Expected max drawdown | ~20% | The hard stop at 3.5σ + time stop + regime flatten bounds the loss on any single pair cycle |
| Win rate (per spread cycle) | ~60–70% | Regime-gated pairs historically have fewer trap-trades than naive z-score entries; exact crypto estimate untested |
| Average win / average loss | ~1.5–2.5× | Mean-reversion trades: wins are bounded at the z-score target; losses bounded by hard stop and regime flatten |
| Breakeven cost budget | 25 bps | Both legs are perp takers on entry/exit (4 fills per cycle); 25 bps is tight but achievable on BTC/ETH |
| Signal frequency | Low-medium | Approximately 2–5 qualifying regime windows per pair per quarter; max 4 concurrent pairs at a time |

**Cost overlay (per cycle, round trip):**
- Entry: 4 fills (2 legs × 2 sides) × 5 bps taker = 20 bps.
- Funding drag if funding differential disagrees: 0.03–0.05%/8h on the paying leg × hold days.
- Net spread P&L must exceed ~25 bps to cover costs; achievable on 2σ+ entries with 8–12 day hold periods.

## Capacity limits

- **Per pair:** BTC/ETH in perpetuals — $100M+; capacity is not the binding constraint on major pairs.
- **Binding constraint:** not execution but *signal quality decay as AUM scales*. At large book sizes, the strategy's own spread entries become visible to other stat-arb participants, narrowing the spread before the full entry is complete. The `capacity_usd: 30000000` estimate reflects the threshold beyond which market impact begins to matter on the second and third tier of pairs (mid-cap L1s, DEX tokens).
- **Pair universe breadth:** the regime gate restricts deployable pairs at any time to those currently cointegrated — typically 2–6 pairs from a universe of 10–15 crypto candidates. Capacity is ultimately limited by the number of regime-qualified pairs available simultaneously.

## What kills this strategy

1. **Crypto structural breaks accelerating (Regime change #5).** In bear markets and risk-off events, historical correlations collapse across the crypto universe simultaneously — the very regime gate fails en masse, leaving no pairs to trade. If structural break frequency increases (more exploits, regulatory shutdowns, protocol failures), the regime gate blocks all entries and the strategy becomes inactive.
2. **Cointegration crowding (#4).** As more systematic stat-arb capital targets the same BTC/ETH and L1 spread relationships, the spreads are absorbed faster, requiring faster execution (sub-day half-lives) that falls below the minimum half-life gate.
3. **Data quality on cointegration tests (Operational #7).** The ADF test on 90-day windows is sensitive to the look-back period and lag selection. Using the wrong lag selection criterion (AIC vs BIC) or look-back can systematically mis-classify pairs as cointegrated or not. A PIT (point-in-time) discipline is required — hedge ratio must be estimated from data available at entry time, not in-sample.
4. **Funding cost swamps spread P&L on slow-reversion pairs (#2: Cost structure).** Even within the 3–45 day half-life range, a pair with a 40-day half-life paying 0.04%/8h on one leg accumulates ~60 bps/month of funding drag — a significant fraction of the expected reversion P&L on a 2σ spread entry.
5. **Correlation breakdown timing lag.** Rolling 30-day correlation is a lagged indicator; by the time it falls from 0.80 to 0.60, the spread may have already widened 50% further than the entry z-score. The hard flatten at 0.60 is a circuit breaker but it is reactive, not anticipatory.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 20%** in any rolling 60-day window.
2. **Rolling 6-month net Sharpe < 0** on a minimum of 15 completed pairs cycles.
3. **Cointegration p-value on all primary pairs > 0.15 on rolling 90-day window for 60+ consecutive days** — structural anchors persistently absent; recalibrate pair universe.
4. **Rolling 30-day correlation below 0.60 floor on 80%+ of trading days over any 30-day window** — broad correlation collapse (likely macro regime event); pause entirely.
5. **Realized half-life > 2× modeled half-life on 40+ consecutive trades** — OU model is systematically mis-estimating reversion speed; recalibrate.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Avoids trap-trades into decoupling events:** the most expensive failure mode in pairs trading (entering a structurally breaking spread and holding through permanent divergence) is directly addressed by the regime gate. This is the primary value-add over naive z-score entry.
- **Composable with funding filter:** the optional funding-differential gate from [[pairs-with-funding-differential]] can be layered on top; running both gates simultaneously selects only the highest-conviction entries (regime intact AND funding agrees).
- **Interpretable failure mode:** if a trade fails, the post-mortem is clear — either the regime gate degraded mid-trade (flatten trigger worked or lagged) or the entry was a valid regime but the spread reverted slower than modeled. Both are diagnosable and recalibratable.
- **Pair universe is flexible:** while BTC/ETH is the canonical pair, the regime gate can be applied to any crypto pair with sufficient liquidity — L1 competitors, DEX governance tokens, correlated staking derivatives. The same gate logic applies.
- **Operates in all macro regimes (when correlation holds):** unlike momentum strategies, pairs mean-reversion can work in both bull and bear macro environments as long as the intra-crypto correlation structure is intact.

## Disadvantages

- **Gate reduces signal frequency substantially:** requiring rolling correlation ≥ 0.70 and passing cointegration tests restricts entry opportunities to roughly 30–50% of z-score extremes in practice. This is the cost of the improved precision.
- **Lagged gate on correlation:** a 30-day rolling correlation is slow to react to sudden decoupling (single-day narrative shocks). The 0.60 hard flatten threshold addresses this, but a fast gap-down event (exchange exploit, governance attack on one leg) can generate large mark-to-market losses before the flatten triggers.
- **Cointegration test reliability on short windows:** a 90-day cointegration test in crypto markets with high structural instability has moderate statistical power. False negatives (trading a structurally broken pair that happens to pass the 90-day window) are possible.
- **Execution complexity:** four fills per cycle (2 legs × 2 sides) plus continuous regime monitoring and daily re-estimation of the ADF and OU model require meaningful operational infrastructure.
- **Cannot scale beyond major pairs:** the regime gate restricts the liquid, reliably cointegrated universe to a small number of pairs (primarily BTC/ETH and major L1s). Extending to mid-caps introduces data quality and liquidity execution risks.

## Sources

- [[pairs-trading]] — the canonical stat-arb/pairs primitive; all structural framing from that page applies.
- [[ornstein-uhlenbeck]] — the OU process model for estimating spread half-life; the half-life gate in this strategy is directly derived from the OU parameter θ.
- [[pairs-with-funding-differential]] — the related combination that adds a funding-differential overlay on top of the z-score entry; composable with the regime gate in this page.
- Do, B. & Faff, R. (2012) — "Are Pairs Trading Profits Robust to Trading Costs?" *Journal of Financial Research*. Documents that conditioning on spread stability reduces the frequency of unprofitable pairs cycles, supporting the regime-gate logic.
- Rad, H., Low, R. K. Y., & Faff, R. (2016) — "The profitability of pairs trading strategies: distance, cointegration and copula methods." *Quantitative Finance*. Shows cointegration-based methods outperform naive distance approaches in out-of-sample periods — the basis for preferring a cointegration gate over a pure z-score threshold.
- [[ornstein-uhlenbeck#Sources]] — Avellaneda & Lee (2010), Chan (2013) — OU process calibration for spread trading.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=720` — 30 days of 1h klines for both legs; primary input for rolling correlation and spread z-score computation
- `GET /api/v1/derivatives/funding-rates?coin=BTC` and `?coin=ETH` — 8h funding rates for both legs; optional funding-differential confirmation gate
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI monitoring for regime context
- `GET /api/v1/regimes/current` — macro regime classification; block entries in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=200` — 90+ days of daily klines for cointegration ADF test estimation on both legs
- `GET /api/v1/derivatives/binance/history?days=90` — historical funding and OI for the funding-differential gate in the backtest

Note: rolling Pearson correlation, ADF cointegration test, and OU half-life estimation are **computed from the klines data** — no dedicated CryptoDataAPI endpoint exists for these derived statistics. Implement in Python (scipy.stats, statsmodels.tsa.stattools) using the klines as input.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

## Instrument Structures

Correlation-regime pairs deploys exclusively on the **pair** structure, adding a live regime gate that validates the pair's statistical relationship before entry.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The only deployment structure. Long the underperformer, short the outperformer via perps, dollar-neutral by OLS hedge ratio. The regime gate (correlation ≥ 0.70, cointegration p ≤ 0.10, OU half-life 3–45 days) is evaluated at the pair level, not at a portfolio level. |
| Single-asset | Not deployed. The regime gate explicitly excludes directional single-leg trades — if correlation breaks, the position is closed, not converted to a single-leg directional bet. |
| Basket | Not deployed in the base strategy. The pair is always exactly two assets. The [[statistical-arbitrage]] page covers basket-leg extensions. |
| Cross-venue | Not deployed here. The cross-venue analogue is [[hl-vs-cex-funding-divergence]], which is a composable layer rather than a replacement for the within-venue pair. |

Regime-gate mechanics change how the pair structure behaves relative to naive [[pairs-trading]]: entry is blocked unless all three gates pass on the day of entry; an open position is flattened immediately if correlation drops below 0.60 (a harder threshold than the entry gate), regardless of z-score. The pair structure's mechanics are otherwise identical.

## Related

- [[pairs-trading]] — the underlying stat-arb primitive; this page adds a three-factor regime gate on top
- [[pairs-with-funding-differential]] — the complementary combination that adds funding-carry confirmation to the spread entry; composable with this page's regime gate
- [[stat-arb]] — the broader statistical-arbitrage strategy family
- [[ornstein-uhlenbeck]] — the OU process model; half-life estimation for the Gate 3 threshold
- [[cointegration]] — the Engle-Granger / Johansen cointegration framework; Gate 2 methodology
- [[regime-detection]] — regime identification methods; the pair's internal regime (this page) vs the macro regime
- [[vol-regime-detection]] — vol-regime as a complement to the correlation regime gate
- [[regime-adaptive-strategy]] — macro regime gating for strategy selection; operates at a higher level than this page's pair-level gate
- [[hl-vs-cex-funding-divergence]] — cross-venue spread between the same asset; different from the same-asset-pair approach here
- [[statistical-arbitrage]] — the theoretical framework for convergence trading
- [[spread-trading]] — general spread mechanics; bid/ask management for multi-leg entries
- [[mean-reversion]] — the reversion mechanics underlying the spread entry signal
- [[perpetual-futures]] — the instrument for expressing pairs trades in crypto
- [[edge-taxonomy]] — behavioral + analytical + structural classification
- [[failure-modes]] — structural break, crowding, data-quality, cost risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
