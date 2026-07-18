---
title: "Vol-Targeted Trend Following"
type: strategy
created: 2026-07-18
updated: 2026-07-18
status: good
tags: [combinations, meta-strategy, trend-following, momentum, volatility, risk-management, position-sizing, quantitative, crypto, perpetual-futures]
aliases: ["Volatility-Scaled Trend Following", "Risk-Parity Trend Crypto", "Vol-Normalised Momentum", "Crypto CTA with Vol Targeting"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, analytical, risk-bearing]
edge_mechanism: "Crypto trend following captures momentum persistence driven by underreaction and anchoring; volatility targeting adds a systematic risk-management overlay that reduces position sizes when realized vol is elevated (preventing over-exposure to whipsaws in high-vol regimes) and increases them when vol is compressed (capturing the full move in low-vol breakouts), improving the Sharpe and drawdown profile relative to fixed-notional trend following."

data_required: [ohlcv-daily, ohlcv-4h, funding-rates, realized-volatility-20d, atr-14, vol-regime-score]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: medium

expected_sharpe: 1.0
expected_max_drawdown: 0.20
breakeven_cost_bps: 30

decay_evidence: "Crypto momentum has shown evidence of decay as systematic perp-DEX strategies proliferate (2023-2025). Vol targeting itself is well-documented in traditional CTA literature; no published crypto-specific study on the incremental value of vol targeting over naive crypto momentum. The overlay's benefit (Sharpe improvement) is expected to persist as long as crypto vol clustering persists — a structural feature of crypto markets."

kill_criteria: |
  - strategy drawdown > 20% from high-water mark
  - rolling 6-month Sharpe < 0 on minimum 20 signals
  - vol-targeting model produces average position size < 20% of maximum for 60+ days (signal collapse from persistently extreme volatility)
  - momentum signal win rate < 40% over 30 consecutive trades (edge decay in base signal)

related: ["[[trend-following-cta]]", "[[volatility-targeting]]", "[[funding-filtered-momentum]]", "[[momentum-rotation]]", "[[breakout-trading]]", "[[atr-position-sizing]]", "[[vol-targeted-trend-following]]", "[[garch-volatility]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Vol-Targeted Trend Following

Vol-targeted trend following runs a [[trend-following-cta|momentum/trend signal]] on crypto perpetuals with **volatility-targeted position sizing**: each position's notional is scaled inversely to the asset's current realized volatility, so the strategy targets a constant *risk contribution* per signal rather than a constant *notional* per signal. In high-vol regimes (crypto crashes, weekend gap events, funding-spike periods), position sizes automatically shrink; in low-vol breakout periods, sizes expand — without any discretionary override.

**How this differs from related strategies:**

- **[[trend-following-cta]]** — the classic multi-asset CTA momentum strategy, primarily focused on commodity/FX/bond futures. Includes vol-based position sizing in one section, but does not treat it as the central innovation and is not crypto-native.
- **[[volatility-targeting]]** (combinations page) — generic vol-targeting across a multi-strategy portfolio; treats vol targeting as a portfolio-level risk budgeting tool. This page focuses on vol targeting as an asset-level sizing input *within* a single momentum strategy, and adds crypto-specific considerations: funding drag, weekend gaps, and realized-vol lookback selection.
- **[[funding-filtered-momentum]]** — filters entries by funding rate. This page layers a *sizing* overlay (vol targeting) on top of the momentum signal rather than a filter. The two can be combined (funding filter + vol-targeted sizing).
- This page is the **crypto-native, buildable implementation** of vol-targeted trend following. It treats the combination as a first-class hybrid strategy with its own edge characterization, not as a variation note inside a generic momentum page.

## Edge source

Per [[edge-taxonomy]], this is primarily **behavioral + analytical**:

- **Behavioral** — momentum in crypto is driven by underreaction and anchoring: participants slow to update their views on trend direction, creating continuation after news and on-chain flow events. This is the same mechanism documented in Jegadeesh and Titman (1993) and Moskowitz, Ooi, Pedersen (2012) for equities and futures, replicated in crypto by Cong, He, Li, and Wang (2022, *Crypto Factor Zoo*) and others. The behavioral mechanism does not depend on vol targeting; vol targeting improves its harvest.
- **Analytical** — vol targeting is a systematic modeling choice: the insight that *risk* should be equalized across signals rather than *notional*. The analytical edge is correctly identifying that crypto volatility is highly clustered (GARCH-like persistence), so that today's volatility is the best predictor of tomorrow's volatility. A fixed-notional approach over/under-weights signals in a predictable way that a vol-targeted approach avoids.
- **Risk-bearing (minor)** — in compressed-vol regimes, the strategy takes larger positions because vol is low; it is implicitly providing liquidity in low-activity periods and being paid via trend continuation when the vol eventually expands.

## Why this edge exists

**The core problem of fixed-notional trend following in crypto:**

Crypto volatility is highly regime-dependent. During a major catalyst event (macro shock, exchange failure, halving breakout), 30-day realized vol on BTC can spike from 30% to 120% in days. A fixed-notional trend follower who sized positions for 30% vol is suddenly running 4× the intended risk at the worst possible moment — when momentum whipsaws are most violent and drawdowns are hardest to recover.

**What vol targeting solves:**

1. **Risk normalization across regimes.** By scaling position size to target a constant daily P&L volatility (e.g. 1% per day), the strategy naturally reduces exposure before a high-vol event materialises, not after. Because vol clusters, yesterday's elevated vol predicts today's elevated vol; the sizing adjustment is predictive, not reactive.
2. **Improved drawdown profile without sacrificing expected return.** Academic CTA research (Roncalli and Weisang 2016; Hurst, Ooi, Pedersen 2017; Man AHL research) consistently shows that vol targeting improves risk-adjusted returns of trend-following strategies across asset classes. The expected return is approximately preserved (trend signal governs direction and entry) while variance is reduced.
3. **Crypto-specific benefit: weekend gap protection.** Crypto markets trade 24/7, but volatility spikes disproportionately on weekend evenings (low liquidity, thin books, news not priced by active market makers). A vol-targeted sizer that uses intraday realized vol (not just daily close-to-close) implicitly reduces size before weekend sessions.

**Who is on the other side:** trend chasers using fixed lot sizes who are forced to exit (stop-loss or margin call) in high-vol periods, creating the very whipsaws that a vol-targeted approach protects against. By not being overleveraged into high-vol periods, the vol-targeted operator survives while over-leveraged participants liquidate.

## Null hypothesis

Under the null, vol targeting adds no marginal value: a vol-targeted trend strategy should have the same Sharpe as a fixed-notional trend strategy on the same signals, with the difference being only presentation (lower notional peaks, same risk-adjusted performance). The null is directly testable by comparing the two on the same signal set.

The null is rejected if the vol-targeted strategy shows materially higher Sharpe *and* materially lower max drawdown than the fixed-notional version on the same universe and period. Prior evidence from CTA research strongly supports rejection. In crypto-specific testing, the null is expected to be rejected due to the particularly pronounced vol clustering in crypto (higher GARCH persistence than equities).

The null is accepted if crypto momentum itself has no edge — vol targeting cannot improve a random signal. Testing the momentum signal in isolation is a prerequisite.

## Rules

### Momentum signal (choose one and apply consistently)

- **Option A (breakout):** Enter long when price breaks above the 20-day Donchian channel high on a 4h bar close. Enter short when price breaks below the 20-day Donchian channel low. Exit when the opposite channel is breached.
- **Option B (EMA crossover):** Enter long when EMA(12) crosses above EMA(26) on daily bars. Enter short when EMA(12) crosses below EMA(26). Exit on the opposite crossover.
- **Option C (time-series momentum):** Enter long if the 20-day price return is positive and accelerating (20d return > 5d return). Enter short if negative and accelerating. Exit on the sign reversal.

The specific momentum signal matters less than consistency and a coherent entry/exit framework. The vol overlay works with any.

### Volatility calculation

1. **Realized vol (20-day close-to-close):** `σ = StdDev(daily_log_returns, 20) × sqrt(365)` (annualised). In crypto, use sqrt(365), not sqrt(252) — crypto trades 7 days/week.
2. **Intraday realized vol (optional, for weekend-gap protection):** use a Parkinson or Yang-Zhang estimator on 4h OHLCV data instead of close-to-close.
3. **Minimum lookback.** Use a minimum of 15 days to compute vol; below this the estimate is unreliable.
4. **Vol cap.** Cap realized vol at 200% annualized to prevent position sizes from going to zero during extreme events (the trade should shrink but not completely disappear).

### Vol-targeted position sizing

```
target_daily_vol = 0.01  # target 1% per-day portfolio vol contribution per position
notional = (target_daily_vol × sleeve_capital) / (σ_daily × price)

where σ_daily = σ_annualised / sqrt(365)
```

Example: sleeve = $100,000, target = 1%/day, ETH σ_annual = 80%, ETH price = $3,000.
σ_daily = 80% / sqrt(365) = 4.19%. Notional = (1% × $100,000) / (4.19% × $3,000) = $1,000 / $125.7 = **7.96 ETH notional** ≈ $23,880.

If ETH vol spikes to 150%: notional shrinks to $1,000 / (7.85% × $3,000) = $4.25 ETH ≈ $12,740. The position is automatically halved without any discretionary decision.

### Sizing constraints

- **Minimum position size.** Do not enter if vol-targeted notional < 2% of sleeve (signal is real but vol is so high that the position is too small to matter; wait for vol to normalise).
- **Maximum position size.** Cap at 15% of sleeve per position (prevents low-vol from producing excessive concentration).
- **Funding drag guard.** Before entering a long perp, check that 8h funding ≤ 0.06%/8h (~65% APY). If funding exceeds this, the funding drag over an expected 10-day hold period (~2%) erodes the vol-targeted sizing benefit. Apply funding gate from [[funding-filtered-momentum]] as an optional complement.
- **Concurrent positions.** Maximum 5 assets to keep the book manageable.

### Exit conditions

1. **Momentum signal reverses** (channel breach in opposite direction, or EMA crossover).
2. **Vol-scale exit.** If realized vol more than doubles from entry vol within 3 days (e.g. entered with 40% vol, now 90%), the position is sized as if for the new vol; if the resulting required size reduction is > 50%, execute the reduction at the next daily bar close.
3. **Drawdown stop.** Close any position where the individual loss exceeds 3× the daily vol contribution at entry. Example: vol-targeted daily contribution = $1,000; close if position drawdown > $3,000.
4. **Funding stop.** Close longs if funding exceeds 0.08%/8h for 3 consecutive 8h periods; the carry cost is now dominating the vol-targeted P&L.

## Implementation pseudocode

```python
# vol_targeted_trend.py — decision loop with vol-scaled sizing
import math
from dataclasses import dataclass

TARGET_DAILY_VOL    = 0.01   # 1% daily vol contribution per position
MIN_NOTIONAL_PCT    = 0.02   # skip if vol-sized notional < 2% of sleeve
MAX_NOTIONAL_PCT    = 0.15   # cap at 15% of sleeve
MAX_CONCURRENT      = 5
FUNDING_GATE_LONG   = 0.0006  # 0.06%/8h: block longs above this
FUNDING_EXIT_LONG   = 0.0008  # 0.08%/8h × 3 periods: exit longs
DRAWDOWN_KILL       = 0.20
VOL_CAP_ANNUAL      = 2.00   # cap realized vol at 200%
DAYS_IN_YEAR_CRYPTO = 365
DRAWDOWN_PER_POS_MULT = 3.0  # exit if loss > 3× daily vol contribution

@dataclass
class Signal:
    asset: str
    price: float
    donchian_high_20d: float; donchian_low_20d: float
    ema_fast: float; ema_slow: float
    realized_vol_annual: float    # annualised realized vol (20-day)
    funding_8h: float
    days_since_entry: int = 0

def vol_daily(s: Signal) -> float:
    capped = min(s.realized_vol_annual, VOL_CAP_ANNUAL)
    return capped / math.sqrt(DAYS_IN_YEAR_CRYPTO)

def vol_sized_notional(s: Signal, sleeve: float) -> float:
    raw = (TARGET_DAILY_VOL * sleeve) / (vol_daily(s) * s.price) * s.price
    return max(min(raw, MAX_NOTIONAL_PCT * sleeve), MIN_NOTIONAL_PCT * sleeve)

def momentum_long(s: Signal) -> bool:
    return s.price > s.donchian_high_20d and s.ema_fast > s.ema_slow

def momentum_short(s: Signal) -> bool:
    return s.price < s.donchian_low_20d and s.ema_fast < s.ema_slow

def decide(s: Signal, book: dict) -> dict:
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    pos = book["positions"].get(s.asset)
    sleeve = book["sleeve_capital"]

    if pos is not None:
        side = pos["side"]
        # funding exit for longs
        if side == "long" and s.funding_8h > FUNDING_EXIT_LONG:
            return {"action": "EXIT", "asset": s.asset, "reason": "funding too high for long"}
        # momentum reversal
        if side == "long" and not momentum_long(s):
            return {"action": "EXIT", "asset": s.asset, "reason": "momentum reversed"}
        if side == "short" and not momentum_short(s):
            return {"action": "EXIT", "asset": s.asset, "reason": "momentum reversed"}
        # drawdown stop
        max_loss = DRAWDOWN_PER_POS_MULT * TARGET_DAILY_VOL * sleeve
        if pos.get("unrealized_pnl", 0) < -max_loss:
            return {"action": "EXIT", "asset": s.asset, "reason": "individual position drawdown stop"}
        # vol-scale adjustment
        new_notional = vol_sized_notional(s, sleeve)
        current_notional = pos.get("notional", 0)
        if abs(new_notional - current_notional) / current_notional > 0.5:
            return {"action": "RESIZE", "asset": s.asset, "new_notional": new_notional,
                    "reason": f"vol changed: resize to {new_notional:.0f}"}
        return {"action": "HOLD", "asset": s.asset}

    # ---- entries ----
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}

    notional = vol_sized_notional(s, sleeve)
    if notional < MIN_NOTIONAL_PCT * sleeve:
        return {"action": "WAIT", "reason": "vol too high — position too small to justify entry"}

    if momentum_long(s) and s.funding_8h <= FUNDING_GATE_LONG:
        return {"action": "LONG", "asset": s.asset, "notional": notional,
                "reason": f"trend confirmed, vol-sized notional={notional:.0f}"}
    if momentum_short(s):
        return {"action": "SHORT", "asset": s.asset, "notional": notional,
                "reason": f"downtrend confirmed, vol-sized notional={notional:.0f}"}

    return {"action": "WAIT", "reason": "no signal"}
```

The production system adds: daily vol recalculation from OHLCV (can use the CryptoDataAPI klines endpoint), regime check, Hyperliquid or Binance order routing, and daily P&L attribution between momentum P&L and vol-sizing benefit.

## Indicators / data used

- **Price momentum** — Donchian 20d or EMA(12/26) on daily bars
- **Realized volatility (20-day close-to-close, annualised)** — the primary position-sizing denominator
- **ATR(14)** — optional alternative vol estimator for sizing; consistent with [[atr-position-sizing]]
- **Funding rate (8h)** — optional funding gate for long entries (from [[funding-filtered-momentum]])
- **Vol regime classification** (`/api/v1/volatility/regime`) — macro-level vol environment check

## Example trade

**Setup (illustrative):**

- Asset: BTC-PERP on Hyperliquid. Sleeve: $100,000.
- EMA(12) crosses above EMA(26) on daily bar. Donchian(20d) high broken. Momentum confirmed.
- 20d realized vol: 65% annualised. σ_daily = 65%/√365 = 3.40%.
- Funding (8h): +0.015% < 0.06% gate → PASS.
- Vol-sized notional: (1% × $100,000) / (3.40% × $91,000 BTC price) = $1,000 / $3,094 ≈ 0.323 BTC × $91,000 = **$29,380 notional**.

**Entry:** Long BTC-PERP at $91,000, $29,380 notional ≈ 0.323 BTC.

**Day 5:** BTC rallies to $97,500. Realized vol has compressed to 45%: new sizing = (1% × $100,000) / (2.35% × $97,500) = $1,000 / $2,291 ≈ 0.436 BTC × $97,500 = **$42,516**. RESIZE triggered (42% increase > not > 50%... just below threshold). Hold current size.

**Day 12:** BTC at $94,000. EMA(12) crosses below EMA(26) on daily bar. Momentum reversed → EXIT.

**Net P&L:** ($94,000 − $91,000) / $91,000 × $29,380 = +3.3% × $29,380 = **+$969**. Less Hyperliquid taker fees (2 × 0.045% × average notional ~$32,000) ≈ $29. Less funding drag (0.015% × 36 periods × $29,380) ≈ $159. **Net: ~$781 on $29,380 = ~2.7% in 12 days**.

*(Illustrative only. Actual results will differ.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Unfiltered crypto momentum Sharpe ~0.5-0.7; vol targeting adds ~0.2-0.4 |
| Expected max drawdown | ~20% | Lower than fixed-notional momentum (~30%+) due to automatic size reduction in high-vol periods |
| Vol contribution stability | ±20% of target per day | Goal is 1%/day; realistic band given vol estimation lag |
| Win rate (per signal) | ~45-55% | Trend following: low win rate, right-skewed P&L |
| Breakeven cost budget | 30 bps | Standard perp taker/maker round-trip |
| Funding drag (per position) | variable | 0-120 bps per 10-day hold depending on funding regime |

**The Sharpe improvement of vol targeting (from CTA literature, extrapolated to crypto):**
Hurst, Ooi, Pedersen (AQR, 2017) document ~0.2-0.4 Sharpe improvement from vol targeting in diversified futures CTA strategies. Crypto-specific amplification is expected due to higher vol clustering (GARCH persistence coefficient > 0.9 in BTC, vs ~0.85 in equities). The estimate of 1.0 expected Sharpe (vs ~0.65 for unfiltered momentum) assumes this improvement transfers to the crypto-native implementation.

## Capacity limits

- **Per asset on Hyperliquid**: ~$20-50M (same as momentum; vol targeting does not change capacity).
- **Cross-asset (5 positions)**: ~$100M combined.
- **Binding constraint at scale**: vol targeting naturally reduces positions during low-liquidity/high-vol periods, which is when the market depth is also lowest — this is a feature, not a bug, but means the strategy self-regulates exposure to liquidity-thin regimes.

## What kills this strategy

1. **Base momentum signal has no edge (#4).** Vol targeting cannot rescue a zero-alpha signal. If crypto momentum has decayed (as systematic strategies proliferate on Hyperliquid), the vol overlay improves the Sharpe of a noisy signal but cannot manufacture alpha from nothing.
2. **Vol estimation breakdown (#5).** The 20-day realized vol assumes the recent past is predictive of near-future vol. In gap-and-reversal events (a sudden geopolitical shock, an exchange hack), yesterday's vol is a bad predictor. The vol cap at 200% prevents the worst misestimation, but gaps can still create immediate large losses before the sizer adjusts.
3. **Funding drain in high-vol trend periods (#5).** The best momentum periods in crypto (parabolic bull runs) are also periods of high positive funding. A large long position entering a BTC bull run at 80% annualised vol would be sized at ~half of a low-vol equivalent and is paying 40-100%+ APY in funding. The combination of reduced sizing *and* high funding cost compresses returns in exactly the scenario where unfiltered momentum looks best.
4. **Crowding (#4).** As vol-targeted momentum strategies proliferate (they are standard among quant funds), the entry signals become crowded: everyone reduces simultaneously in high-vol, and everyone sizes up simultaneously in low-vol, making the vol-targeting effect self-defeating at scale.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 20%** from high-water mark.
2. **Rolling 6-month Sharpe < 0** on minimum 20 signals.
3. **Average position size < 20% of maximum for 60+ days** — vol is persistently so extreme that the sizer produces negligible exposure (signal quality effectively zero in the sizing context).
4. **Win rate < 40% over 30 consecutive trades** — the base momentum signal has no edge.

See [[when-to-retire-a-strategy]].

## Advantages

- **Automatic risk adjustment across crypto vol regimes.** The sizer responds to the well-documented persistence of crypto volatility (GARCH-like clustering) without requiring discretionary judgment.
- **Improves Sharpe without changing the signal.** Vol targeting is a pure sizing improvement; the momentum signal itself is unchanged and need not be re-researched.
- **Weekend gap protection.** Intraday vol estimators naturally pick up the weekend-night liquidity gap in crypto, reducing size before the most dangerous low-liquidity periods.
- **Stackable.** Works with the [[funding-filtered-momentum]] gate (add funding filter to entry conditions) and with a regime gate (from [[regime-gated-grid]]'s activation logic applied here as a strategy-level on/off).
- **Well-documented in CTA literature.** Multiple academic and practitioner sources support the core mechanism (Roncalli and Weisang 2016; Man AHL white papers; AQR's Hurst et al 2017), reducing the reverse-engineering risk.

## Disadvantages

- **Reduces sizing in the best trends.** Crypto's strongest bull runs (2021, BTC 2024-2025) are often also its highest-vol periods. A vol-targeted strategy will be smaller in those periods than a fixed-notional strategy, underperforming on a raw return basis even if Sharpe is better.
- **Requires daily vol monitoring.** The sizer must recompute realized vol and resize daily; this is an operational dependency that a simple fixed-notional strategy does not have.
- **Vol estimation lag.** 20-day realized vol lags instantaneous vol; in a fast-moving market the sizer may be running at yesterday's vol for 1-2 days after a regime shift.
- **Funding interaction.** High-vol periods in crypto are often high-funding periods; the combination of reduced vol-targeting size and high funding drag can double-compress returns in bullish high-vol regimes.

## Sources

- Moskowitz, T., Ooi, Y., Pedersen, L. (2012), *Time series momentum*, Journal of Financial Economics 104(2). Foundational momentum evidence; the base signal.
- Hurst, B., Ooi, Y., Pedersen, L. (AQR, 2017), *A Century of Evidence on Trend-Following Investing*. Documents 100+ years of momentum Sharpe; vol targeting is standard in AQR's implementation.
- Man AHL Research papers on volatility-targeting in CTA strategies (various, 2014-2020). Practical implementation guidance.
- Roncalli, T. and Weisang, G. (2016), *Risk Parity Portfolios with Risk Factors*, Quantitative Finance. Vol targeting as risk-factor equalization.
- Cong, L., He, Z., Li, J., Wang, W. (2022), *Crypto Factor Zoo*, Columbia/Chicago Booth. Documents momentum and other factor premia in crypto. Available at SSRN.
- [[trend-following-cta]] — the foundational trend-following primitive this page extends to a crypto-native implementation.
- [[volatility-targeting]] — the portfolio-level vol-targeting framework; this page is the asset-level version.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (`compressed`, `expanding`, `vol_shock`) — macro vol environment gate
- `GET /api/v1/volatility/regime/score` — market-wide vol stress composite 0-100 — global sizing throttle
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding gate for long entries
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI trend confirmation

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d` — deep historical klines for walk-forward vol estimates
- `GET /api/v1/backtesting/funding` — funding history for funding-drag cost overlay in backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

## Related

- [[trend-following-cta]] — the underlying momentum primitive
- [[volatility-targeting]] — portfolio-level vol-targeting across multiple strategies
- [[funding-filtered-momentum]] — stackable funding-gate overlay on the same momentum signal
- [[atr-position-sizing]] — ATR-based position sizing; related to vol-targeting
- [[garch-volatility]] — the GARCH model underpinning vol clustering in crypto
- [[momentum-rotation]] — cross-sectional momentum; combinable with vol targeting
- [[breakout-trading]] — the entry-signal methodology used in Option A rules
- [[regime-adaptive-strategy]] — the broader regime-switching framework this can plug into
- [[perpetual-futures]] — the instrument; funding drag is the key cost difference from equities
- [[funding-rate]] — the funding mechanism that adds a crypto-specific cost layer
- [[edge-taxonomy]] — behavioral + analytical edge classification
- [[failure-modes]] — crowding and signal-decay risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
