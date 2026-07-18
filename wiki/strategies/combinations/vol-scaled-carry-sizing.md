---
title: "Vol-Scaled Carry Sizing"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, funding-rate, perpetual-futures, volatility, risk-management, position-sizing, quantitative, crypto, derivatives]
aliases: ["Volatility-Scaled Carry", "Risk-Budgeted Carry Book", "Vol-Targeted Carry", "Carry P&L Vol Scaling", "Basis Vol Scaling"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, analytical, behavioral]
edge_mechanism: "Carry books (funding carry and basis/cash-and-carry) accumulate maximum notional exactly when realized P&L volatility is highest — which is precisely when the funding rate is most elevated and the short-squeeze / basis-blowout risk is at its greatest; vol-scaling the carry book to a constant daily-risk budget forces the book to shrink during its most dangerous regimes and expand when carry is quiet and harvesting is lowest-risk, correcting the systematic timing error of fixed-notional carry deployment."

data_required: [funding-rates, ohlcv-daily, perp-price, spot-price, open-interest, realized-vol-calc, basis-history]
min_capital_usd: 25000
capacity_usd: 150000000
crowding_risk: high

expected_sharpe: 1.3
expected_max_drawdown: 0.10
breakeven_cost_bps: 20

decay_evidence: "Vol-targeting applied to carry books is established in the CTA literature (Hurst, Ooi & Pedersen 2012; AQR risk parity research). The specific application to crypto funding carry using the carry P&L stream's realized volatility (rather than spot or perp price vol) as the sizing input is not yet published but follows directly from the same logic: the carry P&L stream has its own realized volatility, and that is the right risk denominator for carry sizing. The carry primitive itself has compressed from ~40% APY (2021) to ~5–15% APY (2025) as Ethena/Resolv/Pendle industrialised the trade; the vol-scaling overlay does not address carry compression but does reduce the left-tail losses that make the compressed carry uneconomic after a single blowout event."

kill_criteria: |
  - carry book drawdown > 10% net of hedge P&L in rolling 30 days (with vol-scaling active)
  - vol-scaling results in average daily notional < 20% of target capital for 60+ consecutive days (carry vol so high the book is effectively shut; the carry primitive itself may be dead — check kill criteria on carry-with-tail-hedge)
  - annualised net carry after vol-scaling adjustments < 3% APY (carry no longer compensates for exchange/basis risk)
  - realized carry P&L vol exceeds 3× target daily-risk budget for 30+ consecutive days (sizing model is failing to normalize risk — recalibrate vol lookback)
  - 7-day funding average turns negative on > 50% of held carry positions (carry primitive dead regardless of sizing)

related: ["[[carry-with-tail-hedge]]", "[[trend-aware-carry]]", "[[funding-vs-basis-rotation]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[vol-targeted-trend-following]]", "[[vol-balanced-pairs]]", "[[narrative-position-vol-targeting]]", "[[volatility-targeting]]", "[[basis-trading]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[open-interest]]", "[[realized-volatility]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Vol-Scaled Carry Sizing

Vol-scaled carry sizing is a **risk-budget framework for carry books** — both [[funding-rate-arbitrage|funding carry]] (short perp / long spot, collecting positive funding) and [[cash-and-carry|basis/cash-and-carry]] (long spot / short dated futures, collecting the basis premium) — that sizes total book notional to a **constant realized P&L volatility target** rather than a fixed capital allocation. The primitive edge is the carry income from either structure; the sizing overlay corrects the classic carry failure mode: the book is at maximum notional exactly when P&L volatility (and thus drawdown risk) is highest — creating the maximum position precisely at the worst time.

**This page covers TWO matrix cells:**
- **Funding carry × vol targeting** — funding carry book sized to a daily-risk P&L budget using realized vol of the carry P&L stream
- **Basis / cash-and-carry × vol targeting** — basis carry book sized to the same framework; the basis P&L stream has its own realized vol, distinct from funding P&L vol

Both cells share the same sizing framework and differ only in the carry P&L stream used to compute realized volatility. Rather than writing two thin pages, this unified framework covers both structures with per-structure calibration guidance. The critical insight that applies to both: **use the carry P&L stream's realized volatility, not spot price volatility, as the sizing denominator.** Spot or perp price vol is the wrong denominator for carry sizing — it is not what the carry book earns and loses from.

**Footnote (matrix):** One sizing framework governs both carry structures. The funding carry book and the basis/C&C book can run simultaneously, each independently vol-scaled; they are not mutually exclusive.

**This is explicitly differentiated from [[carry-with-tail-hedge]]** — that page maintains the carry book at a fixed deployment level (subject to a funding-entry threshold) and budgets a fixed percentage of expected carry income toward an OTM put overlay. The book size is fixed; the protection is variable. This page adjusts the **book size itself** in response to carry P&L volatility — no fixed tail hedge is assumed, though the two frameworks are composable.

**This is differentiated from [[trend-aware-carry]]** — that page throttles the carry book when a directional trend signal fires (price ≥ 15% above SMA20, RSI ≥ 70, funding ≥ 0.05%/8h). The trigger is a directional momentum signal. This page scales the carry book based on the **realized volatility of the carry P&L stream itself**, regardless of price trend direction. A carry book can be in a quiet regime, with no directional trend, and still experience elevated P&L volatility from basis blowouts, funding rate noise, or settlement timing effects — this page addresses that regime.

**This is differentiated from [[vol-targeted-trend-following]]** — that page applies vol-targeting to a directional trend/momentum book: scale notional so the portfolio contribution of the trend book is constant. This page applies vol-targeting to a **carry book** (delta-neutral), where the P&L driver is funding income and basis convergence, not directional price movement. The math is identical; the P&L stream is entirely different.

**This is differentiated from [[funding-vs-basis-rotation]]** — that page decides *which* carry instrument to hold (perp-funding carry vs dated-futures basis carry) based on which annualised yield is higher. It is an allocation-layer decision between carry instruments. This page does not change the instrument allocation; it scales the size of whichever carry instrument is active.

## Edge source

Per [[edge-taxonomy]], **structural + analytical + behavioral**:

- **Structural** — carry books (both funding and basis) earn structural income: the funding transfer mechanism (funding carry) and the futures basis convergence (basis/C&C) are contractual cash flows driven by the market's structural leverage demand. The edge from the carry primitive is structural; the vol-scaling overlay is an enhancement to survival of that structural edge.
- **Analytical** — the vol-scaling calculation (carry P&L vol → target notional) is an explicit quantitative correction to a systematic error in naive fixed-notional carry deployment. It requires computing the realized vol of the carry P&L stream — a calculation most fixed-notional carry operators do not perform — and acting on it to adjust position size. This analytical discipline is the overlay's contribution.
- **Behavioral** — most carry operators deploy a fixed capital allocation to the carry book: "10% of portfolio in carry." This creates a systematic timing error: when funding is highest (most attractive), the fixed notional is too high relative to the elevated P&L volatility; when funding is lowest (least attractive), the fixed notional is appropriate but the carry income barely covers overhead. Vol-scaling forces the book smaller when P&L vol is high (when the carry is most attractive but also most dangerous) and larger when P&L vol is low (when the carry is quieter but safer). This counter-behavioral adjustment corrects the fixed-notional crowd's systematic oversizing into high-carry / high-risk windows.

## Why this edge exists

**The fixed-notional carry timing error:**

Fixed-notional carry deployment creates a systematic mismatch between position size and risk level:

**In high-funding regimes (funding ≥ 0.04–0.10%/8h):**
- The carry book earns the most income (high annualised yield)
- BUT: high funding signals crowded leveraged longs, elevated squeeze risk, high P&L volatility from basis blowouts and mark-to-market moves on the short-perp leg
- Fixed notional → maximum size at maximum risk
- A single basis blowout or funding spike can produce a multi-month income drawdown in days

**In low-funding regimes (funding 0.01–0.02%/8h):**
- The carry book earns modest income (low annualised yield)
- The P&L volatility is lower: crowding is absent, basis is stable
- Fixed notional → same size at lower risk
- The carry book could safely run larger in this regime without increasing drawdown probability

**The vol-scaling correction:**

Targeting a constant daily-risk P&L budget:
- In high-carry / high-vol regimes: the model forces notional **down**, reducing exposure exactly when the carry is most crowded and most likely to blowout
- In low-carry / low-vol regimes: the model can run the book at **full or above-target notional** (if the daily-risk budget allows), harvesting the safer, quieter carry more efficiently

This is the same structural reason [[vol-targeted-trend-following]] outperforms fixed-notional CTA: vol-scaling forces position sizing to track the risk environment rather than the P&L opportunity.

**Why carry P&L vol, not spot vol:**

The basis/C&C book's P&L is driven by:
- Basis convergence rate and basis volatility (NOT spot price vol)
- Funding rate changes (NOT spot price moves in isolation)
- Roll costs and timing

Using spot price volatility as the sizing denominator would scale down the carry book during directional BTC moves — which may or may not coincide with elevated carry P&L risk. A large BTC spot move can be benign for a delta-neutral carry book if the basis is stable. Conversely, a flat BTC price period can produce extreme carry P&L volatility if funding rates oscillate or the basis blows out. The correct denominator is always the P&L stream's own volatility.

## Null hypothesis

Under the null, vol-scaling the carry book **does not improve net returns** relative to fixed-notional carry deployment:
- Carry income foregone (by shrinking the book during high-vol regimes) should exceed the losses avoided, on average.
- Fixed-notional carry should produce the same or better risk-adjusted return as vol-scaled carry on a historical BTC carry dataset.

Currently not rejected (`backtest_status: untested`). Testable predictions:
- (a) Backtest BTC funding carry (2020–2025) with fixed 10% notional allocation vs vol-scaled (target: $500 daily risk on $100K capital). Predict: vol-scaled version produces 15–30% lower max drawdown during high-funding episodes (March 2021, November 2021, March 2024) with ≤ 10% reduction in total carry income over the full period.
- (b) The same backtest for the BTC basis/C&C structure using quarterly futures. Predict: vol-scaled version produces more stable equity curve through roll periods and basis-blowout windows.

## Rules

### Step 1: Define the carry P&L stream

**For funding carry (short perp / long spot):**

The daily carry P&L is:
```
carry_pnl_day = funding_rate × notional_perp × 3_periods_per_day
               + mark_to_market_change_on_short_perp (delta neutral offset by spot long)
               - exchange_fees
```

In practice, track the daily net P&L of the carry book as a single time series, separate from any directional book P&L. Use this series for vol calculation.

**For basis/cash-and-carry (long spot / short dated futures):**

The daily carry P&L is:
```
carry_pnl_day = daily_basis_change × notional_futures (convergence step)
               + any roll income/cost on the futures leg
               - exchange_fees
```

The basis/C&C P&L stream is typically smoother than funding carry P&L (no 8-hourly settlement spikes), but basis blowouts around expiry dates create volatile episodes. Track as a separate daily time series.

### Step 2: Compute carry P&L volatility

**Lookback:** 20-day realized volatility of the carry P&L stream.

```
carry_vol = std(carry_pnl_daily_20d) × sqrt(365)
```

This produces the annualised volatility of the daily carry P&L expressed in dollar terms (e.g., "carry P&L has been running at 2.1% annualised volatility on $100K notional").

Minimum lookback: 10 trading days (discard estimates on < 10 days of data). If the carry book has been active for < 10 days, default to the regime estimate from **Step 2a**.

**Step 2a (cold-start and warm-start estimate):** In the absence of sufficient carry P&L history, use the following proxy estimates:
- Funding carry: proxy carry vol = 20-day realized spot vol × 0.15 (carry vol is typically 10–20% of spot vol in calm regimes; 30–40% of spot vol during high-carry / high-OI regimes). Recalibrate once ≥ 10 days of actual carry P&L are available.
- Basis/C&C: proxy carry vol = 20-day realized basis vol (from historical quarterly futures basis data).

### Step 3: Target notional calculation

**Daily risk budget:** Set a fixed dollar daily-risk budget (e.g., $500/day for a $100,000 portfolio = 0.50% per day).

**Target notional:**
```
target_notional = daily_risk_budget / (carry_vol_annualised / sqrt(365))
               = daily_risk_budget / carry_vol_daily
```

Where `carry_vol_daily = carry_vol_annualised / sqrt(365)`.

**Example:**
- Portfolio: $100,000
- Daily risk budget: $500 (0.50%/day)
- 20-day carry P&L vol: 2.0% annualised → 2.0% / sqrt(365) = 0.105% daily vol per dollar of notional
- Target notional: $500 / 0.00105 = $476,190 ← this is the total carry book size

Wait — that calculation yields 4.76× leverage, which is too high. The correct formulation normalises by the notional:

**Correct calculation:**

Define `carry_vol_pct_daily = std(carry_pnl_pct_20d)` where returns are expressed as % of notional.

```
target_notional = (daily_risk_budget / portfolio_capital) / carry_vol_pct_daily × portfolio_capital
               = daily_risk_budget / carry_vol_pct_daily
```

**Worked example:**
- Portfolio: $100,000
- Daily risk budget: $500 (0.50% of portfolio per day)
- 20-day carry P&L: shows std of 0.18% of notional per day
- Target notional: $500 / 0.0018 = $277,778 → 2.78× leverage on carry book

This is consistent with typical carry books (1–3× leverage). In high-vol carry regimes (carry P&L std = 0.40%/day): target notional = $500 / 0.0040 = $125,000 → 1.25× leverage. In low-vol regimes (std = 0.12%/day): target notional = $500 / 0.0012 = $416,667 → 4.17× leverage (capped by exchange margin constraints — see Step 4).

### Step 4: Notional bounds and adjustment timing

**Minimum notional:** 0.5× target capital (carry book must be at least half-deployed to be economically meaningful). If vol-scaling would call for < 0.5× capital, clip to 0.5× and log the regime as "high-vol carry — clipped."

**Maximum notional:** 4× target capital for funding carry (exchange margin constraint); 3× for basis/C&C (expiry liquidity constraint). These caps prevent the vol-scaling from over-deploying in ultra-quiet regimes.

**Rebalancing frequency:** Recompute target notional **weekly** (every 7 days). Do not rebalance more frequently — daily recomputation creates excessive transaction costs from constant perp-leg adjustments.

**Rebalance threshold:** Only execute a notional adjustment if the new target differs from the current notional by **≥ 15%**. Below that threshold, the round-trip cost (perp fees + slippage) exceeds the risk-reduction benefit.

### Step 5: Interaction with directional overlays

If [[trend-aware-carry]] is also deployed:
- The trend overlay takes precedence: if the trend gate calls for a 60% reduction, apply that reduction to the current vol-scaled notional, not to the fixed capital target.
- Combined effect: vol-scaling adjusts the base notional; the trend overlay applies a further percentage reduction on top when directional risk is elevated.

If [[carry-with-tail-hedge]] is deployed:
- Compute the tail-hedge budget as a percentage of the **expected vol-scaled carry income**, not the fixed-notional carry income. When vol-scaling reduces the book, the hedge budget shrinks proportionally.

## Implementation pseudocode

```python
# vol_scaled_carry_sizing.py
from dataclasses import dataclass
from typing import Literal
import numpy as np

CarryType = Literal["funding", "basis"]

# ---- sizing parameters ----
DAILY_RISK_BUDGET_PCT = 0.0050   # 0.50% of portfolio per day
VOL_LOOKBACK         = 20        # 20-day carry P&L vol lookback
MIN_NOTIONAL_MULT    = 0.50      # floor: 0.5× portfolio capital
MAX_NOTIONAL_MULT_FUNDING = 4.0  # ceiling: 4× portfolio capital (funding carry)
MAX_NOTIONAL_MULT_BASIS   = 3.0  # ceiling: 3× portfolio capital (basis/C&C)
REBALANCE_THRESHOLD  = 0.15      # only rebalance if target differs by >= 15%

# ---- cold-start proxy (before 10 days of carry P&L history) ----
PROXY_CARRY_VOL_FACTOR_FUNDING = 0.15   # carry vol ≈ 15% of spot vol (calm regime)
PROXY_CARRY_VOL_FACTOR_BASIS   = 0.08   # basis vol ≈ 8% of spot vol

@dataclass
class CarryBook:
    carry_type: CarryType
    portfolio_capital: float
    current_notional: float
    carry_pnl_pct_history: list[float]   # daily carry P&L as pct of notional
    spot_vol_20d: float                  # fallback for cold-start only

def compute_carry_vol_daily(book: CarryBook) -> float:
    """Compute daily carry P&L volatility (% of notional)."""
    n = len(book.carry_pnl_pct_history)
    if n >= VOL_LOOKBACK:
        arr = np.array(book.carry_pnl_pct_history[-VOL_LOOKBACK:])
        return float(arr.std())
    elif n >= 10:
        # partial history — use what we have
        arr = np.array(book.carry_pnl_pct_history)
        return float(arr.std())
    else:
        # cold-start: use spot vol proxy
        proxy_factor = (PROXY_CARRY_VOL_FACTOR_FUNDING
                        if book.carry_type == "funding"
                        else PROXY_CARRY_VOL_FACTOR_BASIS)
        spot_vol_daily = book.spot_vol_20d / np.sqrt(365)
        return spot_vol_daily * proxy_factor

def target_notional(book: CarryBook) -> float:
    """Return the vol-scaled target notional for the carry book."""
    carry_vol_daily = compute_carry_vol_daily(book)
    if carry_vol_daily <= 0:
        return book.portfolio_capital * 1.0  # fallback: no scaling

    daily_risk_budget_dollar = book.portfolio_capital * DAILY_RISK_BUDGET_PCT
    raw_target = daily_risk_budget_dollar / carry_vol_daily

    # apply floor and ceiling
    max_mult = (MAX_NOTIONAL_MULT_FUNDING if book.carry_type == "funding"
                else MAX_NOTIONAL_MULT_BASIS)
    clipped = max(
        book.portfolio_capital * MIN_NOTIONAL_MULT,
        min(raw_target, book.portfolio_capital * max_mult)
    )
    return clipped

def rebalance_decision(book: CarryBook) -> dict:
    """Return rebalance action if threshold crossed."""
    new_target = target_notional(book)
    pct_change = abs(new_target - book.current_notional) / book.current_notional

    carry_vol_daily = compute_carry_vol_daily(book)
    regime_label = ("HIGH-VOL" if carry_vol_daily > 0.003
                    else "LOW-VOL" if carry_vol_daily < 0.0015
                    else "NORMAL")

    if pct_change < REBALANCE_THRESHOLD:
        return {
            "action": "HOLD",
            "current_notional": round(book.current_notional, 0),
            "new_target": round(new_target, 0),
            "pct_change": round(pct_change, 3),
            "regime": regime_label,
            "note": f"change {pct_change:.1%} < threshold {REBALANCE_THRESHOLD:.0%}; no rebalance",
        }

    direction = "REDUCE" if new_target < book.current_notional else "INCREASE"
    return {
        "action": f"REBALANCE_{direction}",
        "current_notional": round(book.current_notional, 0),
        "new_target": round(new_target, 0),
        "pct_change": round(pct_change, 3),
        "regime": regime_label,
        "carry_vol_daily_pct": round(carry_vol_daily * 100, 3),
        "note": (f"{direction}: from ${book.current_notional:,.0f} to ${new_target:,.0f} "
                 f"({pct_change:.1%} change); carry vol daily = {carry_vol_daily:.3%}; "
                 f"regime = {regime_label}"),
    }
```

The production system adds: a weekly scheduler that triggers the rebalance decision every Sunday evening (before Monday's funding settlements); an alert when the regime label shifts from NORMAL to HIGH-VOL (flag for manual review of whether to apply [[trend-aware-carry]] override simultaneously); a carry P&L logger that records each 8-hour funding settlement and each daily mark-to-market for accurate vol estimation; and a monthly audit comparing the vol-scaled equity curve to the hypothetical fixed-notional baseline.

## Indicators / data used

**For both carry structures:**
- **Carry P&L time series** — computed internally from position tracking. Not available via a direct API endpoint; built from the funding rate settlement log and the perp/spot mark-to-market record.
- **Daily OHLCV (BTC/ETH spot and perp)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22`; used for the cold-start spot-vol proxy.

**For funding carry:**
- **8h funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; primary income driver; also used to flag high-carry / high-risk regimes (funding ≥ 0.04%/8h = HIGH-VOL carry regime signal).
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; correlated with carry P&L vol (high OI = elevated basis blowout risk). When OI/market-cap rises above 2.5%, treat as an independent HIGH-VOL signal even if the 20-day carry vol estimate has not yet risen.

**For basis/cash-and-carry:**
- **Binance quarterly futures mark price / spot price** — `GET /api/v1/derivatives/binance/summary?coin=BTC`; the basis (futures − spot) computed from this data; daily basis changes are the primary P&L driver and thus the primary vol input.
- **Funding rates (for basis convergence rate monitoring)** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; the perp funding rate influences the quarterly futures basis (cash-and-carry arbitrage pressure).

**Regime context:**
- `GET /api/v1/regimes/current` — if `Structural_Shock` regime, reduce carry book to minimum notional regardless of vol estimate (carry primitive fails in systemic stress; do not wait for the carry P&L vol estimate to update).

## Example trade

**Setup: BTC funding carry book, vol-scaling in action across two regimes**

*Portfolio: $100,000. Daily risk budget: $500 (0.50%).*

**Regime 1 — Low-carry, low-vol (Q4 2024 analog):**
- 20-day carry P&L std: 0.12% of notional per day
- Target notional: $500 / 0.0012 = $416,667 (4.17× leverage — capped at 4.00× = $400,000)
- Carry book: short $200,000 BTC perp / long $200,000 BTC spot (delta-neutral)
- Funding rate: +0.015%/8h = +0.045%/day on $200,000 = $90/day income
- Weekly carry income at vol-scaled sizing: $90 × 7 = $630

**Regime 2 — High-carry, high-vol (late bull analog, March 2024):**
- 20-day carry P&L std: 0.38% of notional per day (basis blowouts + funding spikes)
- Target notional: $500 / 0.0038 = $131,579 (1.32× leverage)
- Carry book: short $65,789 BTC perp / long $65,789 BTC spot
- Funding rate: +0.075%/8h = +0.225%/day on $65,789 = $148/day income
- Weekly carry income at vol-scaled sizing: $148 × 7 = $1,036

**Comparison — fixed-notional $200,000 in Regime 2:**
- Funding rate: +0.225%/day on $200,000 = $450/day income → $3,150/week
- But: during a basis blowout event (−2.5% mark-to-market loss on the short-perp leg), fixed notional loses: $200,000 × 2.5% = −$5,000 in a single session
- Vol-scaled: $65,789 × 2.5% = −$1,645 in the same event

The vol-scaled version earns $2,114 less in carry income during Regime 2's active week. It also avoids $3,355 more of the basis-blowout loss. The tradeoff: $2,114 forgone income vs $3,355 avoided loss → the vol-scaling provides positive expected value if basis-blowout events occur with ≥ 63% of the frequency implied by this single-event example.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.3 | Higher than fixed-notional carry (est. Sharpe ~0.8–1.0) due to reduced blowout drawdowns |
| Expected max drawdown | ~10% | Carry book shrinks during highest-risk carry regimes, preventing the multi-month income wipeout |
| Carry income reduction vs fixed-notional | 15–25% of gross carry foregone | The cost of risk management; accepted to preserve the equity curve |
| Average book utilisation | 60–80% of fixed-notional equivalent | Book runs smaller on average; the improvement comes from tail-loss reduction |
| Breakeven cost per rebalance | 20 bps round-trip | Perp fee (taker 0.04% × 2) + slippage; 15% threshold prevents excessive rebalancing |

## Capacity limits

`capacity_usd: 150,000,000` — there is no fundamental capacity constraint on a sizing framework. The carry book's capacity is determined by the underlying carry primitive ([[carry-with-tail-hedge]] and [[trend-aware-carry]] both set capacity at $20M–$150M for delta-neutral carry). The vol-scaling overlay is invisible to the market; it adjusts notional within whatever execution footprint the carry book already has. Very large carry books (≥ $500M) face their own liquidity constraints on the perp-leg unwind; vol-scaling adjustments must be executed gradually to avoid impact.

## What kills this strategy

1. **Carry P&L vol estimation lag (#3: Market-structure change).** The 20-day lookback is slow to respond to sudden regime shifts. A funding rate spike from 0.02% to 0.10%/8h can occur over 48 hours; the vol estimate requires 10+ days to incorporate the new regime. During that lag, the carry book is oversized relative to the new high-vol regime. The OI monitor (Step 3: when OI/market-cap ≥ 2.5%, treat as HIGH-VOL) provides an independent, faster-acting override.
2. **Carry compression destroying the P&L signal (#3).** As funding carry compresses toward 5% APY (2025 levels), the daily carry P&L becomes too small relative to mark-to-market noise from the perp leg. At very low carry rates, the "carry P&L stream" is dominated by daily perp mark-to-market noise, producing an artificially high vol estimate that keeps the book small even in genuinely low-risk regimes. Detection: if 20-day annualised carry yield < 4% while carry vol is > 1% daily, the vol signal is noise-dominated; switch to the OI/funding-rate direct proxy.
3. **Rebalancing costs consume the vol-targeting benefit (#7: Operational).** At small portfolio sizes (< $25K), the 20 bps round-trip rebalancing cost represents a larger fraction of carry income. The 15% threshold prevents excessive rebalancing, but in volatile regimes where the target swings frequently, even weekly rebalancing can cost 1–2% of annual carry income. Below $25K, the overhead may exceed the benefit; a simpler step-function (2 levels: "normal" and "high-vol at 50% notional") is preferable.
4. **Over-reliance on the cold-start proxy (#6: Complexity).** The spot-vol proxy is a rough approximation. If the carry book starts in a period where spot vol is high but carry P&L vol is actually low (e.g., BTC is volatile but the basis/funding is stable), the proxy will keep the book undersized needlessly. Accumulate 10 days of actual carry P&L history as quickly as possible and retire the proxy estimate.
5. **Correlation between carry vol and carry income (#1: Primitive degradation).** In the carry compression scenario (funding persistently low), the vol-scaling optimization breaks down: there is nothing meaningful to scale against. The vol-targeting framework requires the carry primitive to be generating sufficient income to justify management overhead. If annualised carry < 3% APY, retire the carry book — vol-scaling cannot resurrect a dead carry primitive.

## Kill criteria

Pause on any of:

1. **Carry book drawdown > 10%** net of hedge P&L in rolling 30 days — vol-scaling failed to prevent a drawdown event; review the carry vol estimate and the OI override trigger.
2. **Average vol-scaled daily notional < 20% of target capital for 60+ days** — carry P&L volatility so high the framework is effectively shutting down the carry book; the carry primitive may be dead (check carry income vs threshold).
3. **Annualised net carry after vol-scaling < 3% APY** — carry no longer compensates for exchange, basis, and counterparty risk; retire the carry primitive.
4. **Realized carry P&L vol > 3× target daily-risk budget for 30+ consecutive days** — the sizing model is failing; recalibrate the vol lookback or reduce the daily-risk budget target.
5. **7-day funding average negative on > 50% of carry positions** — carry primitive dead regardless of sizing framework.

See [[when-to-retire-a-strategy]] and [[failure-modes]] for the broader framework.

## Advantages

- **Corrects the classic carry timing error at no additional data cost.** The carry P&L history is a by-product of running the carry book; no additional data source is required. The vol-scaling calculation requires only that daily P&L is tracked, which any serious carry operator should already be doing.
- **Composable with all existing carry overlays.** Vol-scaled carry is the base book that [[carry-with-tail-hedge]], [[trend-aware-carry]], [[funding-vs-basis-rotation]], and [[event-calendar-risk-gating]] all layer on top of. It changes the base notional; the overlays apply their respective adjustments on top. No conflict between layers.
- **Unified framework for both funding and basis carry.** The same vol-scaling math governs both carry structures; operators running both simultaneously can use the same code base with per-structure P&L streams as inputs.
- **Prevents the single blowout that wipes months of carry income.** At typical carry rates (5–15% APY), a single basis-blowout event of 3–5% mark-to-market loss destroys 3–12 months of carry income at fixed notional. Vol-scaling reduces the carry book before these high-risk periods, limiting the worst-case loss to 2–3 months of carry income rather than a full-year wipeout.

## Disadvantages

- **Reduces carry income during the highest-yield periods.** The highest-funding periods (funding ≥ 0.05–0.10%/8h) are also when carry vol is highest, forcing the book smaller. Vol-scaling gives up the highest annualised carry rates to reduce blowout risk. Operators seeking maximum carry income in bull markets will underperform fixed-notional carry during peak periods.
- **Cold-start estimation error.** Without 10+ days of carry P&L history, the spot-vol proxy is approximate. New carry books or carry books returning from a pause start with a rough size estimate that may be significantly wrong. The 10-day warm-up period during which sizing is less accurate is a real operational gap.
- **Requires accurate carry P&L accounting.** The framework depends on daily carry P&L being accurately tracked, separate from any directional position P&L. Systems that blend carry income with directional P&L (e.g., a portfolio-level PnL sheet) will produce corrupted vol estimates. Operational discipline in P&L attribution is a prerequisite.
- **Weekly rebalancing creates execution overhead.** Each rebalance requires adjusting the perp-leg size (and potentially the spot-leg hedge). At 20 bps round-trip cost, a carry book that rebalances 20 times per year (above the 15% threshold) spends 400 bps/year on rebalancing — a meaningful fraction of compressed carry income.

## Sources

- [[carry-with-tail-hedge]] — the tail-hedge overlay on a carry book; the vol-scaling framework is the base-book sizing that determines the hedge budget for this page.
- [[trend-aware-carry]] — the trend-throttle overlay; composable with vol-scaling as a secondary notional reduction layer.
- [[vol-targeted-trend-following]] — the vol-targeting framework applied to the trend book; the math in that page directly translates to carry book sizing with carry P&L vol as the denominator.
- [[vol-balanced-pairs]] — the intra-spread vol-balanced sizing for pairs; the same risk-budget logic applies at a different level of the portfolio hierarchy.
- [[volatility-targeting]] — the portfolio-level vol-targeting concept; foundational for understanding daily-risk-budget sizing.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding settlements; primary input for funding carry P&L stream (income leg); also used to flag HIGH-VOL regime independently of the vol estimate when funding ≥ 0.04%/8h
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — ETH funding carry P&L input (if running ETH carry book)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI monitoring; independent HIGH-VOL override when OI/market-cap ≥ 2.5%
- `GET /api/v1/derivatives/binance/summary?coin=BTC` — quarterly futures mark price for basis/C&C P&L computation (futures − spot = basis; daily basis changes = primary P&L driver)
- `GET /api/v1/regimes/current` — regime context; `Structural_Shock` → reduce to minimum notional immediately

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=22` — 22-day daily OHLCV; cold-start spot vol proxy calculation
- `GET /api/v1/derivatives/binance/history?days=30` — historical funding and OI data for carry P&L backfilling and vol estimate calibration

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

## Related

- [[carry-with-tail-hedge]] — tail-hedge overlay on a carry book; composable on top of vol-scaled base notional
- [[trend-aware-carry]] — trend throttle on the carry book; applies a percentage reduction on top of the vol-scaled notional
- [[funding-vs-basis-rotation]] — allocation between funding carry and basis/C&C; the rotation decision is independent of the vol-scaling within each structure
- [[funding-rate-arbitrage]] — the canonical funding carry primitive
- [[cash-and-carry]] — the canonical basis/C&C primitive
- [[vol-targeted-trend-following]] — vol-targeting on the trend book; same math applied to a directional P&L stream
- [[vol-balanced-pairs]] — vol-balanced leg sizing for pairs; the same risk-budget logic at the intra-spread level
- [[narrative-position-vol-targeting]] — vol-targeting on the narrative sub-book; the same sizing logic in a high-vol context
- [[volatility-targeting]] — portfolio-level vol-targeting framework; foundational reference
- [[event-calendar-risk-gating]] — binary-event pause framework; composable with vol-scaling (event pause overrides vol-scaling during event windows)
- [[realized-volatility]] — the computation method for the carry P&L vol denominator
- [[funding-rate]] — the income driver for funding carry
- [[basis-trading]] — the income driver for basis/C&C carry
- [[open-interest]] — the independent HIGH-VOL override signal
- [[edge-taxonomy]] — structural + analytical + behavioral classification
- [[failure-modes]] — carry compression, vol estimation lag, rebalancing cost
- [[when-to-retire-a-strategy]] — kill vs pause framework
