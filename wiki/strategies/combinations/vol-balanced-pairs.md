---
title: "Vol-Balanced Pairs"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, pairs-trading, arbitrage, volatility, risk-management, position-sizing, quantitative, statistics, crypto]
aliases: ["Volatility-Neutral Pairs", "Vol-Scaled Spread Trading", "Risk-Budget Pairs", "Vol-Weighted Stat Arb"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, analytical, structural]
edge_mechanism: "Retail stat-arb implementations enter pairs in dollar-equal or contract-equal sizes, allowing the higher-volatility leg to dominate realized P&L regardless of which leg is 'right'; vol-balanced sizing ensures the spread's risk contribution is symmetric — the spread earns mean-reversion profit when the structural relationship reasserts, while dollar-neutral sizing produces a spread that is structurally long the high-vol leg's risk and produces P&L dominated by the directional drift of the volatile leg rather than the spread itself."

data_required: [ohlcv-daily, ohlcv-4h, realized-vol-calc, funding-rates, open-interest, rolling-correlation, cointegration-p-value]
min_capital_usd: 25000
capacity_usd: 30000000
crowding_risk: low

expected_sharpe: 1.0
expected_max_drawdown: 0.18
breakeven_cost_bps: 25

decay_evidence: "Vol-balanced position sizing in equity pairs is documented in Gatev, Goetzmann & Rouwenhorst (2006) and the risk-parity literature. The specific application to crypto perp pairs — where the high-vol leg can have 3–5× the annualised volatility of the low-vol leg — is not systematically studied. Vol-targeting as a position-sizing layer is established in the CTA literature; applying it at the spread level rather than at the portfolio level is the specific novel element here."

kill_criteria: |
  - strategy drawdown > 18% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 12 completed spread cycles
  - spread z-score and vol ratio become anti-correlated for 45+ consecutive days (vol-balancing is not helping — one leg's vol is structurally elevated)
  - cointegration p-value deteriorates beyond 0.15 on a 90-day rolling window (structural anchor broken)

related: ["[[pairs-trading]]", "[[correlation-regime-pairs]]", "[[pairs-with-funding-differential]]", "[[vol-targeted-trend-following]]", "[[volatility-targeting]]", "[[narrative-position-vol-targeting]]", "[[unlock-pair-hedge]]", "[[stat-arb]]", "[[cointegration]]", "[[z-score]]", "[[realized-volatility]]", "[[funding-rate]]", "[[open-interest]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Vol-Balanced Pairs

Vol-balanced pairs is a [[pairs-trading|stat-arb/pairs]] strategy that applies **per-leg volatility scaling to a cointegrated spread** so that each side of the trade contributes equal realized risk to the position — not equal dollar notional. The primitive edge is the same as standard pairs trading: cointegrated crypto assets temporarily diverge in relative price and converge back. The vol-targeting overlay corrects the most common implementation flaw: entering legs in equal dollar size when the two legs have materially different realized volatility, which allows the high-vol leg's directional drift to dominate P&L instead of the spread's mean-reversion.

**This is explicitly differentiated from [[correlation-regime-pairs]]** — that page gates entry on whether the cointegrating relationship is currently intact (rolling correlation floor, cointegration test significance, spread half-life within bounds). It does not address how the two legs are sized relative to each other. This page assumes the cointegrating relationship is intact (the regime gate from [[correlation-regime-pairs]] can and should be applied as a pre-filter) and then addresses the sizing of the two legs so that neither dominates P&L.

**This is differentiated from [[pairs-with-funding-differential]]** — that page requires a funding differential between the two perp legs to agree with the spread direction, earning carry while holding the spread. The overlay is a carry filter (which leg is being paid vs which is paying). This page sizes the legs by vol rather than filtering by carry. The two overlays are composable: a spread can satisfy both the funding-differential alignment and the vol-balance requirement simultaneously, but they are independent filters and independent sizing decisions.

**This is differentiated from [[vol-targeted-trend-following]]** — that page applies volatility-based position sizing to a directional trend book: scale down the futures position when realized vol is high, scale up when low, targeting a constant daily-risk dollar amount. The instrument is a single directional perp; the sizing is a risk-budget constraint on that position. This page sizes the two LEGS OF A SPREAD relative to each other, so the spread itself is risk-balanced rather than each leg being independently sized against a portfolio budget. The mechanism is the same (vol-scaling) but the application is different (intra-spread balance vs portfolio-level position size).

**This is differentiated from [[unlock-pair-hedge]]** — that page constructs a beta-hedged long-short pair specifically for the token-unlock event window, using a fixed hedge ratio = 1/beta to strip sector correlation. The hedge ratio there is driven by BTC beta, not by relative realized volatility. This page's vol-neutral ratio is driven by the ratio of the two legs' realized volatilities and applies universally to any cointegrated pair, not only in the unlock event context.

## Edge source

Per [[edge-taxonomy]], **behavioral + analytical + structural**:

- **Behavioral (primary)** — retail stat-arb implementations are dollar-neutral by default (equal notional both sides). When BTC/ETH pairs are traded in dollar-equal sizes and ETH has 1.5–2× the annualised vol of BTC, the P&L from the ETH leg swamps the BTC leg. The "pair" degrades to a leveraged ETH position with a BTC hedge that is too small. Practitioners who are anchored to dollar-neutral sizing systematically expose themselves to this volatility imbalance; the vol-balanced implementation exploits the convergence that dollar-neutral practitioners cannot cleanly isolate.
- **Analytical** — computing per-leg realized volatility (20-day annualised) and adjusting notional so that the expected daily P&L contribution from each leg is equal is an explicit analytical calculation. This is the same logic used in risk-parity portfolio construction; applying it at the spread level is the analytical edge.
- **Structural** — cointegrated crypto assets share structural anchors (BTC beta, shared CEX liquidity, correlated ETF flows) that create genuine mean-reversion in the spread. The structural anchor ensures the convergence signal is not spurious; the vol-balancing ensures the position is sized to capture it cleanly.

## Why this edge exists

**The dollar-neutrality problem in crypto pairs:**

Consider a BTC/ETH cointegrated pair. BTC 20-day realized vol = 45% annualised; ETH 20-day realized vol = 65% annualised. If the pair is entered in $10,000 BTC long / $10,000 ETH short (dollar-neutral), the ETH short leg has 65/45 = 1.44× the risk contribution of the BTC long leg.

This means:
1. If ETH rallies 10% (against the short position) while BTC is flat, the position loses $1,000 on the ETH leg with zero offset from BTC. The P&L is dominated by ETH's directional move, not the spread.
2. The spread z-score may be only 1.5 standard deviations extended, but the ETH leg's vol means the position will hit a dollar-equivalent stop before the spread has time to mean-revert.

**The vol-balanced fix:**

Vol-neutral sizing: `notional_btc / notional_eth = vol_eth / vol_btc = 65 / 45 = 1.44`. Enter $14,400 BTC / $10,000 ETH (scaling the lower-vol leg up). Now both legs contribute $450 per day (at 1% daily move on each) to realized P&L — the spread's mean-reversion can assert itself without being drowned by the larger leg's directional noise.

**Who is on the other side:** primarily other stat-arb participants using dollar-neutral sizing, and momentum traders who are directionally positioned in the high-vol asset. When the spread mean-reverts, the momentum crowd is wrong-footed; the dollar-neutral stat-arb crowd was unable to hold the position through the period of convergence because their volatility exposure was unbalanced.

**Why the edge persists:** vol balancing requires real-time vol monitoring and willingness to hold unequal notional positions. Most retail pairs traders and many systematic shops default to dollar-neutral or contract-neutral as a simplifying assumption. This systematic underweighting of the lower-vol leg is the persistent implementation error that creates the exploitable wedge.

## Null hypothesis

Under the null, vol-balancing the spread adds **no incremental value** relative to dollar-neutral sizing:
- Vol-balanced pairs should not produce higher risk-adjusted returns than dollar-neutral pairs on the same cointegrated set.
- The annualised Sharpe of vol-balanced implementation should not be statistically different from dollar-neutral on the same spread entry signals.

Currently not rejected (`backtest_status: untested`). Testable predictions:
- (a) Backtest the BTC/ETH spread (2021–2025) with dollar-neutral sizing vs vol-balanced sizing (20d rolling vol ratio). Predict: vol-balanced produces 15–25% higher Sharpe due to reduced directional bleed from the ETH leg in its higher-vol periods.
- (b) Compare maximum drawdown on the same spread signal set. Predict: vol-balanced drawdown is 15–20% smaller than dollar-neutral drawdown in periods where the ETH/BTC vol ratio exceeds 1.5.

## Rules

### Step 1: Pair selection and cointegration gate

**Pair eligibility (pre-filter before any position):**
- Rolling 60-day correlation ≥ **0.70** (structural co-movement intact).
- Engle-Granger cointegration test p-value ≤ **0.05** on 90-day daily closes (cointegration confirmed).
- Spread half-life (estimated from OU process) between **3 and 25 days** (mean-reverts quickly enough to trade; not so fast that execution is infeasible).
- Source: computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` (both legs).

*Note: this pre-filter is identical to [[correlation-regime-pairs]]'s regime gate. Traders already running that strategy can use its regime-pass as the eligibility check for this page's vol-sizing layer.*

**Canonical pairs (crypto):**
- BTC/ETH (most liquid, most studied)
- BTC or ETH vs major L1s: SOL, BNB, ADA, AVAX
- Sector pairs: competing L2s (ARB/OP), competing DeFi protocols in the same category

### Step 2: Vol-balanced position sizing

**Per-leg volatility (20-day realized):**
- Compute 20-day annualised realized vol for each leg: `vol_i = std(daily_returns_20d) × sqrt(365)`.
- Source: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22` (both legs).

**Vol-neutral ratio:**
`ratio = vol_high_leg / vol_low_leg`

**Notional allocation:**
- Fix total notional `N` (e.g., 10% of portfolio for the full spread).
- Low-vol leg notional = `N × vol_high / (vol_high + vol_low)`.
- High-vol leg notional = `N × vol_low / (vol_high + vol_low)`.
- Both legs contribute equal daily-risk dollars at current realized vol.

**Example:** BTC (vol = 45%), ETH (vol = 65%), total notional $20,000:
- BTC (low-vol leg, long): `$20,000 × 65 / (65 + 45) = $11,818`.
- ETH (high-vol leg, short): `$20,000 × 45 / (65 + 45) = $8,182`.

**Re-sizing trigger:** recalculate vol ratio weekly. If either leg's 20-day vol changes by ≥ 15% relative, adjust notional at next spread entry (do not re-size mid-trade to avoid churning).

### Step 3: Spread entry

**Z-score entry:** enter when the spread z-score (based on 30-day rolling mean/std of the log-spread) reaches ≥ **2.0 standard deviations** in either direction.
- Long the under-performing leg (z-score low) with the vol-balanced notional.
- Short the over-performing leg (z-score high) with the vol-balanced notional.

**Optional funding alignment gate (from [[pairs-with-funding-differential]]):** additionally require that the funding differential agrees with the spread direction (the overvalued leg's perp has higher positive funding — you are paid to be short). This is an optional filter that reduces signal frequency but increases average entry quality.

### Step 4: Exit

1. **Primary:** close when spread z-score mean-reverts to ≤ **0.5 standard deviations** (convergence achieved).
2. **Stop-loss:** close if spread z-score widens to ≥ **3.5 standard deviations** (divergence accelerating; thesis invalidated).
3. **Regime invalidation:** immediately flatten if rolling 60-day correlation drops below **0.55** or cointegration p-value exceeds **0.10** (structural anchor has broken mid-trade).
4. **Time exit:** close after **21 days** if neither convergence nor stop-loss is hit (theta-equivalent; prevents indefinite carry on a stalled spread).

### Position sizing constraints

- Maximum single spread notional: 10–12% of portfolio.
- Maximum concurrent spreads: 3 (to limit correlation between positions in the same correlated asset universe).
- Leverage: maximum 2× on each leg (combined max 4× notional, but vol-balanced so each leg is sized conservatively).

## Implementation pseudocode

```python
# vol_balanced_pairs.py
from dataclasses import dataclass
from typing import Optional
import numpy as np

# ---- pair eligibility ----
CORR_MIN            = 0.70    # rolling 60d correlation floor
COINT_P_MAX         = 0.05    # Engle-Granger p-value <= 0.05
HALFLIFE_MIN        = 3       # OU half-life >= 3 days
HALFLIFE_MAX        = 25      # OU half-life <= 25 days

# ---- vol sizing ----
VOL_LOOKBACK        = 20      # 20-day realized vol for sizing
VOL_REBALANCE_PCT   = 0.15    # re-size if leg vol changes >= 15%

# ---- spread entry / exit ----
ZSCORE_ENTRY        = 2.0     # enter at 2σ spread dislocation
ZSCORE_EXIT         = 0.5     # exit at 0.5σ convergence
ZSCORE_STOP         = 3.5     # stop at 3.5σ divergence (position broken)
CORR_STOP           = 0.55    # flatten if rolling correlation drops below
COINT_STOP          = 0.10    # flatten if cointegration p-value rises above
MAX_HOLD_DAYS       = 21

@dataclass
class PairState:
    symbol_a: str
    symbol_b: str
    price_a: float
    price_b: float
    returns_a_20d: list[float]
    returns_b_20d: list[float]
    log_spread_30d: list[float]
    rolling_corr_60d: float
    coint_p_value: float
    halflife_days: float

def compute_vol(returns: list[float]) -> float:
    return float(np.std(returns) * np.sqrt(365))

def compute_zscore(log_spread_series: list[float]) -> float:
    arr = np.array(log_spread_series)
    return (arr[-1] - arr.mean()) / arr.std()

def vol_balanced_notional(total_notional: float, vol_a: float, vol_b: float) -> tuple[float, float]:
    """Return (notional_a, notional_b) so each leg contributes equal daily-risk."""
    n_a = total_notional * vol_b / (vol_a + vol_b)
    n_b = total_notional * vol_a / (vol_a + vol_b)
    return n_a, n_b

def pair_eligible(s: PairState) -> tuple[bool, str]:
    if s.rolling_corr_60d < CORR_MIN:
        return False, f"correlation {s.rolling_corr_60d:.2f} < {CORR_MIN}"
    if s.coint_p_value > COINT_P_MAX:
        return False, f"cointegration p={s.coint_p_value:.3f} > {COINT_P_MAX}"
    if not (HALFLIFE_MIN <= s.halflife_days <= HALFLIFE_MAX):
        return False, f"half-life {s.halflife_days:.1f}d outside [{HALFLIFE_MIN}, {HALFLIFE_MAX}]"
    return True, "pair eligible"

def entry_decision(s: PairState, portfolio_capital: float, book: dict) -> dict:
    eligible, elig_msg = pair_eligible(s)
    if not eligible:
        return {"action": "WAIT", "reason": f"pair not eligible: {elig_msg}"}
    if book.get("active_spread"):
        return {"action": "HOLD", "reason": "spread already active"}

    zscore = compute_zscore(s.log_spread_30d)
    if abs(zscore) < ZSCORE_ENTRY:
        return {"action": "WAIT", "reason": f"z-score {zscore:.2f} not at entry threshold"}

    vol_a = compute_vol(s.returns_a_20d)
    vol_b = compute_vol(s.returns_b_20d)
    total_notional = portfolio_capital * 0.10
    n_a, n_b = vol_balanced_notional(total_notional, vol_a, vol_b)

    if zscore > ZSCORE_ENTRY:
        # A over-performed B: short A, long B
        direction_a, direction_b = "SHORT", "LONG"
    else:
        # B over-performed A: short B, long A
        direction_a, direction_b = "LONG", "SHORT"

    return {
        "action": "ENTER_SPREAD",
        "leg_a": {"symbol": s.symbol_a, "direction": direction_a, "notional": round(n_a, 0)},
        "leg_b": {"symbol": s.symbol_b, "direction": direction_b, "notional": round(n_b, 0)},
        "zscore_at_entry": round(zscore, 2),
        "vol_ratio": round(vol_a / vol_b, 2),
        "note": (f"vol-balanced: {s.symbol_a} vol={vol_a:.1%}, "
                 f"{s.symbol_b} vol={vol_b:.1%}, ratio={vol_a/vol_b:.2f}; "
                 f"z-score={zscore:.2f}"),
    }

def exit_decision(
    s: PairState,
    days_held: int,
) -> Optional[dict]:
    zscore = compute_zscore(s.log_spread_30d)

    # Convergence target
    if abs(zscore) <= ZSCORE_EXIT:
        return {"action": "CLOSE_TARGET",
                "reason": f"spread converged: z-score={zscore:.2f} ≤ {ZSCORE_EXIT}"}
    # Stop-loss
    if abs(zscore) >= ZSCORE_STOP:
        return {"action": "CLOSE_STOP",
                "reason": f"spread widened: z-score={zscore:.2f} ≥ {ZSCORE_STOP}"}
    # Regime invalidation
    if s.rolling_corr_60d < CORR_STOP:
        return {"action": "CLOSE_REGIME",
                "reason": f"correlation collapsed to {s.rolling_corr_60d:.2f} — structural anchor broken"}
    if s.coint_p_value > COINT_STOP:
        return {"action": "CLOSE_REGIME",
                "reason": f"cointegration lost: p={s.coint_p_value:.3f} > {COINT_STOP}"}
    # Time exit
    if days_held >= MAX_HOLD_DAYS:
        return {"action": "CLOSE_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

The production system adds: a daily vol-ratio monitor that flags when either leg's 20-day vol changes ≥ 15% (re-size trigger); a regime monitor that polls rolling correlation and cointegration state; an alert when spread z-score reaches entry/stop thresholds; and a post-trade log recording the vol ratio at entry, the convergence speed, and whether the vol-balancing improved or hurt relative to the hypothetical dollar-neutral outcome.

## Indicators / data used

- **Daily OHLCV (both legs)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`; rolling correlation, log-spread z-score, cointegration test, 20-day realized vol, OU half-life estimation.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (and ETH); optional funding-differential alignment gate (adapts [[pairs-with-funding-differential]] filter as an optional add-on).
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; supplemental check: if OI is rapidly growing on the overvalued leg, the short may face squeeze risk — reduce position size.
- **Regime** — `GET /api/v1/regimes/current`; if `Structural_Shock`, all pairs flat — correlation anchors break under systemic stress.
- **Spread z-score** — computed in-strategy from OHLCV data; not a standalone endpoint.
- **20-day realized vol** — computed from daily returns of each leg (OHLCV endpoint above).

## Example trade

**Setup (illustrative — BTC/ETH spread dislocation):**

- BTC 20-day realized vol = 48% annualised. ETH 20-day realized vol = 72% annualised.
- Vol ratio (ETH/BTC) = 72/48 = 1.50.
- Rolling 60d correlation = 0.82 (above floor). Cointegration p-value = 0.03 (significant). OU half-life = 8.5 days. Pair eligible.
- Log-spread z-score: +2.3 (ETH has over-performed BTC over 8 days — ETH expensive relative to BTC).

**Sizing:** Portfolio $100,000. Total spread notional = 10% = $10,000.
- BTC (long, low-vol leg): `$10,000 × 72 / (48 + 72) = $6,000`.
- ETH (short, high-vol leg): `$10,000 × 48 / (48 + 72) = $4,000`.
- Each leg contributes `$6,000 × 48% / 365 ≈ $7.87` and `$4,000 × 72% / 365 ≈ $7.89` in expected daily P&L — symmetrically balanced.

Compare to dollar-neutral: $5,000 BTC long / $5,000 ETH short. ETH leg contributes `$5,000 × 72% / 365 ≈ $9.86` vs BTC leg's `$5,000 × 48% / 365 ≈ $6.58`. The ETH leg dominates by 50% — the "pairs trade" is effectively a bet on ETH vs BTC direction.

**Entry:** Long BTC perp at $66,500 ($6,000 notional ≈ 0.0902 BTC). Short ETH perp at $3,450 ($4,000 notional ≈ 1.159 ETH).

**Scenario A — spread converges:**
- Over 9 days, ETH underperforms BTC (ETH −6%, BTC +2%). Z-score falls from +2.3 to +0.4.
- BTC leg: +$120 (+2.0%). ETH leg: −$240 but short, so +$240 gain.
- Gross P&L: $120 + $240 = $360. Less 25 bps: −$25. Net P&L: **+$335** / +0.34% of portfolio.
- Funding income (ETH short, positive funding): $4,000 × 0.02%/8h × 3 periods/day × 9 days = +$21.60. **Total net: +$357**.

**Scenario B — dollar-neutral comparison (same signal, same setup):**
- Same BTC +2% / ETH −6% outcome but $5,000/$5,000 dollar-neutral sizing.
- BTC leg: +$100. ETH leg (short): +$300 gain.
- Gross P&L: $400. Less 25 bps: −$25. Net: +$375.
- In this specific scenario, dollar-neutral performed slightly better (+$375 vs +$357) because the high-vol leg was the one that moved in the "right" direction.

**Key insight on scenario B:** vol-balancing slightly reduces the per-trade P&L in scenarios where the high-vol leg's directional move AGREES with the spread direction. But it provides substantial loss reduction in scenarios where the high-vol leg DISAGREES — e.g., if ETH rallied 8% while BTC was flat: dollar-neutral loses $400 on the ETH short vs vol-balanced's $320 loss. Over many trades, the reduction in left-tail losses improves the Sharpe despite modest per-trade P&L reduction.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Higher than dollar-neutral pairs due to reduced directional bleed from the high-vol leg; confirmed by risk-parity pairs literature in equities |
| Expected max drawdown | ~18% | Vol-balanced sizing prevents the single-leg blowout that dominates dollar-neutral pair drawdowns |
| Win rate | ~60–65% (estimated) | Same pair entry signal as dollar-neutral; vol-balancing improves the hit rate by reducing false exits at volatility-driven z-score extremes |
| Average hold duration | 6–14 days | OU half-life of 3–25 days bounds the expected convergence period |
| Breakeven cost budget | 25 bps | Two-leg round trip (perp taker × 4 fills); funding income partially offsets in favourable-differential setups |

**Cost overlay:** the most significant cost is trading spread at z-score entry/exit levels plus perp taker fees. At 5 bps per fill × 4 fills (entry and exit for both legs) = 20 bps plus slippage = 25 bps total round-trip estimate. The vol-balanced strategy generates slightly more notional (higher-notional lower-vol leg) than dollar-neutral, which increases absolute cost slightly but the Sharpe improvement more than compensates.

## Capacity limits

- **Per spread:** $6,000–$12,000 per leg in BTC/ETH perps is well within Binance/Bybit perp capacity.
- **Aggregate:** `capacity_usd: 30000000` reflects the constraint from available cointegrated pairs in crypto. At $30M book, running 3 concurrent spreads at 10% each = $9M notional — within depth for major pairs (BTC, ETH). Minor L1 pairs hit liquidity limits at lower notional.
- **Binding constraint:** number of genuinely cointegrated pairs with sufficient liquidity; BTC/ETH is the only pair where this strategy runs at scale above $5M.

## What kills this strategy

1. **Structural decoupling of the pair (#1: Primitive degradation).** The most common failure: two assets that were cointegrated for 12 months experience a structural narrative break (ETH gains institutional ETF flows that BTC does not; SOL has a network outage while BNB continues operating normally). The pair's cointegration breaks permanently. The regime-stop (correlation < 0.55) catches this, but typically after significant drawdown has occurred.
2. **Vol-balancing overweights the low-vol leg during a low-vol regime that breaks explosively (#3: Market-structure change).** A period of compressed BTC vol (BTC 20-day vol = 30%) causes the vol-balanced position to overweight BTC significantly. If BTC then has a 15% flash crash, the overweight creates a larger-than-expected loss on the long BTC leg than the dollar-neutral position would have.
3. **Crowding of BTC/ETH pairs trading (#4: Crowding).** The BTC/ETH spread is the most visible cointegrated pair in crypto. As more systematic stat-arb capital monitors this spread, z-score extremes revert faster, reducing the tradeable window and compressing the per-entry P&L.
4. **Funding squeeze on the short high-vol leg (#7: Operational).** If the strategy is short the high-vol leg at the same time as a short-squeeze develops (funding spikes, OI increases rapidly), the short must be maintained at increasing cost. The vol-balancing does not protect against a carry blowout on the short leg — the optional funding-differential gate (from [[pairs-with-funding-differential]]) addresses this if activated.
5. **Correlation spike in a systemic crash (#3).** In a broad crypto deleveraging, all assets become highly correlated in the downward direction. The spread collapses as both legs fall together. The regime-stop (based on 60-day rolling correlation and cointegration) may not fire quickly enough if the regime shift is very rapid.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 18%** from high-water mark — vol-balanced sizing did not prevent a structural decoupling loss; recalibrate pair selection and cointegration standards.
2. **Rolling 6-month Sharpe < 0** on a minimum 12 completed spread cycles — the strategy is not producing positive risk-adjusted returns; the pair selection or vol-ratio computation needs review.
3. **Spread z-score and vol ratio anti-correlated for 45+ days** — the vol-balancing is actively hurting (the high-vol leg is consistently moving in the convergence direction, penalising the approach that down-sizes it). Recalibrate.
4. **Cointegration p-value of the primary pair deteriorates beyond 0.15 on a 90-day rolling window** — the structural anchor has broken; suspend the pair until re-established.

See [[when-to-retire-a-strategy]] for the broader framework.

## Instrument Structures

Vol-balanced pairs deploys on the **pair** structure with a modified position-sizing scheme that replaces dollar-neutral sizing with volatility-neutral sizing.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The only deployment structure. Two perp legs, long and short, with notional sized to equalise *volatility contribution* rather than dollar notional. The long leg and short leg target equal realised-vol contribution, so the spread P&L reflects the spread's own dynamics rather than being dominated by the more-volatile leg's directional drift. |
| Single-asset | Not deployed. Vol-balancing is a spread-level construction — both legs are held simultaneously. |
| Basket | Not deployed in base form. Vol-balancing can in principle be extended to a basket-vs-basket spread (one leg is a sector basket), but that extension lives in [[statistical-arbitrage]] and [[cross-sectional-relative-value]]. |
| Cross-venue | Not deployed. Vol-balancing is an intra-venue construction. |

Mechanical change from [[pairs-trading]]: `notional_A / notional_B ≠ beta` (the cointegration hedge ratio). Instead: `notional_A / notional_B = vol_B / vol_A` (inverse-vol ratio), where vol is the 20-day realised annualised volatility of each leg. In practice this means the lower-volatility leg receives larger notional and the higher-volatility leg receives smaller notional — correcting the systematic dollar-neutral bias toward the high-vol leg.

## Advantages

- **Eliminates the dollar-neutrality implementation flaw.** The most common failure mode in crypto pairs trading — where the high-vol leg dominates directional P&L — is eliminated by construction. The spread P&L reflects the mean-reversion signal, not the directional drift of the larger-vol asset.
- **Composable with existing pairs overlays.** The vol-balancing sizing is a layer on top of pair selection and spread entry; it is fully composable with the funding-differential filter ([[pairs-with-funding-differential]]), the regime-gate ([[correlation-regime-pairs]]), and the unlock event hedge ([[unlock-pair-hedge]]). Running all four layers simultaneously produces the highest-quality-filtered pairs entry available in this wiki's framework.
- **No additional data requirements.** Realized vol is computed from the same daily OHLCV data that cointegration tests and z-score calculations already require. The vol-balancing overlay has zero marginal data cost.
- **Symmetric risk contribution simplifies risk management.** With each leg contributing equal daily-risk, the position's risk is cleanly captured by the total notional and a single vol figure (the spread vol, not the individual leg vols). Portfolio risk management and drawdown attribution are simpler.

## Disadvantages

- **Reduces P&L when the high-vol leg is the "right" leg.** By down-sizing the high-vol leg, the strategy captures less upside in scenarios where the high-vol leg generates the mean-reversion P&L. Over a diversified set of trades this is neutral or positive (by construction), but in any individual scenario that goes "right" for the high-vol leg, vol-balanced will underperform dollar-neutral.
- **Vol ratio can change quickly in crypto.** Crypto realized volatility can double or halve in 1–2 weeks in a high-vol regime. A vol ratio computed on 20-day returns can be stale by the time a trade is entered. Weekly recalibration (as specified in the rules) helps but does not eliminate lag.
- **Requires accurate real-time vol calculation.** The strategy depends on computing 20-day rolling realized vol for both legs from OHLCV data. A bad data point, price gap, or exchange maintenance event can corrupt the vol estimate and produce a severely wrong-sized entry.
- **Low signal frequency.** Like all stat-arb strategies, the combination of cointegration requirements, z-score threshold, and (optionally) funding-differential alignment produces relatively few high-quality entries. Diversification requires monitoring multiple pairs simultaneously.

## Sources

- [[correlation-regime-pairs]] — the cointegration-regime gate that this page's pair-eligibility check adapts; the structural pre-filter that pairs-vol-balanced inherits.
- [[pairs-with-funding-differential]] — the carry-alignment overlay; this page's optional funding-differential gate is directly adapted from that page's entry rules.
- [[vol-targeted-trend-following]] — the portfolio-level vol-targeting framework that this page adapts at the intra-spread level.
- [[narrative-position-vol-targeting]] — the vol-targeting layer applied to the high-vol-dispersion narrative sub-book; the same sizing logic in a different context confirms the approach.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — daily OHLCV for both legs; rolling correlation, cointegration test, log-spread z-score, OU half-life estimation
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — ETH (or second-leg) daily OHLCV for the same calculations
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding rate for optional funding-differential gate
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — ETH/second-leg funding rate for differential calculation
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI growth check to flag short-squeeze risk on the high-vol leg
- `GET /api/v1/regimes/current` — regime check; flatten all spreads in Structural_Shock regime

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — annual daily closes for cointegration calibration and spread z-score history
- `GET /api/v1/derivatives/binance/history?days=90` — funding and OI history for optional funding-differential gate calibration

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this pairs book end-to-end:

- **Signal** — daily klines for both legs feed correlation, cointegration, z-score, and OU half-life; leg weights are inverse-vol balanced
- **Sizing** — `GET /api/v1/quant/coins/risk` returns per-coin vol-target multipliers in one batch call — a direct cross-check on locally computed leg weights
- **Filter** — the funding differential (`GET /api/v1/derivatives/funding-rates?coin={LEG}`) and short-leg OI growth (`GET /api/v1/derivatives/open-interest?coin={LEG}`) guard the carry and squeeze dimensions
- **Regime gate** — `GET /api/v1/regimes/current`; flatten all spreads in `Structural_Shock`
- **Backtest** — spread and vol-weighting replay on `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08); pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time regime states at rebalance dates
- **Tips** — re-estimate vol weights on a fixed weekly schedule, not on every poll — intraday vol-chasing turns a pairs book into a churn machine

## Related

- [[pairs-trading]] — the canonical stat-arb/pairs primitive; this page is the vol-balanced sizing variant
- [[correlation-regime-pairs]] — cointegration-regime gate; use as the pre-filter before this page's sizing layer
- [[pairs-with-funding-differential]] — carry-alignment filter for pairs entries; composable with vol-balanced sizing
- [[vol-targeted-trend-following]] — vol-targeting at the portfolio level; this page adapts the same logic at the intra-spread level
- [[volatility-targeting]] — the portfolio-level vol-targeting concept; foundational for understanding risk-budget sizing
- [[narrative-position-vol-targeting]] — vol-targeting in the high-vol narrative sub-book; the same sizing logic in a different context
- [[unlock-pair-hedge]] — beta-hedged unlock pairs; the hedge ratio there uses beta, not vol; composable with this page in event windows
- [[stat-arb]] — the statistical arbitrage concept page
- [[cointegration]] — the statistical relationship that provides the mean-reversion anchor
- [[z-score]] — the spread standardisation metric used for entry/exit
- [[realized-volatility]] — the input to the vol-balanced sizing calculation
- [[funding-rate]] — the optional carry-alignment input
- [[open-interest]] — the squeeze-risk context check
- [[edge-taxonomy]] — behavioral + analytical + structural classification
- [[failure-modes]] — decoupling, vol regime change, crowding, carry blowout
- [[when-to-retire-a-strategy]] — kill vs pause framework
