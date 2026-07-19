---
title: "Trend-Aware Carry"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, funding-rate, perpetual-futures, trend-following, risk-management, quantitative, crypto, bitcoin, derivatives]
aliases: ["Trend-Throttled Carry", "Carry Book Trend Gate", "Trend-Conditional Funding Carry", "Momentum-Filtered Carry"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, behavioral, analytical]
edge_mechanism: "Leveraged retail longs pay structural funding to the carry book; the trend overlay reduces or exits that book specifically when a strong directional trend makes the short-perp leg mechanically expensive — the counterparty is the carry operator who ignores trend context and absorbs the full basis-blowout and squeeze risk embedded in trending perp markets, while paying for insurance they did not need in calm regimes."

data_required: [funding-rates, ohlcv-daily, open-interest, perp-price, spot-price]
min_capital_usd: 25000
capacity_usd: 150000000
crowding_risk: high

expected_sharpe: 1.1
expected_max_drawdown: 0.12
breakeven_cost_bps: 20

decay_evidence: "Funding carry has compressed from 40%+ APY (2021) to 5–15% APY (2025) as Ethena/Resolv/Pendle industrialised the trade. The trend-throttle layer is not independently documented in the academic literature; it is an operational risk-management refinement grounded in the well-documented relationship between perp funding and price trend (BIS Working Paper 1087, Schmeling et al. 2023). The overlay does not generate independent alpha — it reduces the worst-regime losses of the carry primitive."

kill_criteria: |
  - carry book drawdown > 12% net of hedge P&L in rolling 30 days (with trend overlay active)
  - trend overlay fires >60% of trading days over 90 consecutive days (perpetually in throttle; the signal is uninformative — recalibrate thresholds or accept carry compression as structural)
  - annualised net carry after throttle period costs < 3% APY (carry no longer compensates for exchange/basis risk even without trend drag)
  - trend throttle exits consistently followed by carry recovery < the funding missed during the exit window, across 6 consecutive throttle events (overlay is generating false exits that cost more than the avoided drawdowns)
  - 7-day funding average turns negative on > 50% of held carry positions (carry primitive dead regardless of trend)

related: ["[[carry-with-tail-hedge]]", "[[funding-vs-basis-rotation]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[funding-filtered-momentum]]", "[[vol-targeted-trend-following]]", "[[trend-following-cta]]", "[[oi-confirmed-trend]]", "[[crowded-long-funding-fade]]", "[[funding-conditioned-vol-selling]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[open-interest]]", "[[basis-trading]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Trend-Aware Carry

Trend-aware carry is a **carry book** (short perp / long spot, collecting positive funding) that scales down or exits the short-perp leg when a strong directional trend is running against the carry structure — specifically, strong uptrends that compress or flip funding capture and mechanically widen the short-perp basis, or strong downtrends that raise depeg and venue-stress risk. The trend overlay acts as a **throttle on carry-book deployment**, not as a source of directional alpha; the carry book is the primitive that generates P&L, and the trend gate is the mechanism that idles or reduces that book in the regimes where its costs, basis blowout, and squeeze risk are highest.

This is explicitly differentiated from [[carry-with-tail-hedge]] — that page maintains the carry book at full deployment at all times and finances a permanent tail-hedge overlay sized as a fixed percentage of expected carry income. The tail hedge protects against the crash; it does not reduce book size in trending regimes. This page **scales down or exits the carry book itself** in response to trend signals, rather than budgeting for a hedge on a book that stays fully deployed.

This is differentiated from [[funding-vs-basis-rotation]] — that page allocates *between* two carry instruments (perp-funding carry vs dated-futures basis carry) depending on which annualised yield is higher. It is an allocation-layer decision between instruments. This page throttles the *overall size* of the carry book in response to a directional trend signal; no instrument rotation is performed.

This is differentiated from [[funding-filtered-momentum]] — that page gates momentum entries (directional trend trades) on funding-rate level. The relationship here is the inverse: this page gates the carry book on trend signal, not the momentum book on funding.

## Edge source

Per [[edge-taxonomy]], **structural + behavioral + analytical**:

- **Structural (primary)** — the carry book earns a contractual funding transfer from leveraged perp longs. The structural component of the edge is unchanged by the trend overlay; the overlay is a risk-management constraint on when to bear that structural risk.
- **Behavioral** — strong trending markets are associated with elevated leverage accumulation (high OI, compressed or flipped funding), which is also the regime in which the short-perp leg of a carry book suffers its highest mark-to-market losses and squeeze risk. The behavioral distortion is the carry operator who treats funding as independent of price trend — ignoring that the same crowded longs who are paying funding in calm markets become the engine of funding inversion and basis blowout during violent uptrends.
- **Analytical** — the improvement over plain carry is not a new edge source but a more accurate regime model: carry P&L is well-explained by the funding income stream *minus* the basis blowout and funding-inversion cost in trending regimes. A systematic trend signal that identifies these regimes in advance adds analytical value by reducing the drag without missing the normal carry accrual periods.

## Why this edge exists

**The carry book has regime-conditional P&L that naive carry operators ignore:**

1. **Strong uptrends compress then invert funding.** When BTC is in a strong uptrend — price above its 20-day high, trend strength confirmed by directional indicators — the perp premium widens substantially. Initially this *improves* the carry yield (the short-perp/long-spot book earns more). But at the extreme, as the crowd goes maximally long, the basis becomes so wide that a sudden momentum reversal or negative catalyst produces a rapid funding normalization — the "funding flush." The carry book's short-perp leg faces mark-to-market losses as the perp premium collapses, and the book may be forced to cover at the worst time. The strong-uptrend gate identifies this region before the flush.

2. **Strong downtrends raise depeg and venue risk.** In sharp downtrends, the carry book's long-spot / short-perp combination is nominally delta-neutral but exposed to venue risk (exchange solvency), oracle divergence, and the possibility that the perp-spot basis widens in the wrong direction (perp discount to spot is unusual but occurs during panic). The trend gate reduces the carry book in this regime to avoid the operational tail risk that is elevated in chaotic downtrends.

3. **Re-entry rules capture the resumed carry stream.** The carry book does not permanently exit — it waits for trend metrics to return to the neutral zone (price consolidation, trend indicators reverting) and re-enters at normal sizing. The P&L cost of the throttle is the missed carry during the trend exit window; this is smaller than the avoided basis-blowout loss that would have occurred if the carry book stayed deployed through the trend extreme.

**Who is on the other side:** the systematic carry operator (ETH staking carry stack, Ethena/Resolv delta-neutral vault) who maintains full exposure through trending markets without trend-conditional sizing, and absorbs the full funding-flush and basis-blowout losses that the trend-aware book avoided.

## Null hypothesis

Under the null, the trend overlay carries **no incremental value** over a fully-deployed carry book:
- The annualised return of carry × (1 − throttle_fraction) during trend windows should not exceed the annualised return of full carry deployment during the same windows.
- The drawdown reduction from trend-exits should not exceed the carry income forgone during exit periods (i.e., the overlay has zero net value — saved drawdowns = missed carry income).
- Trend-exit windows should not be associated with higher-than-average subsequent funding-flush events (trend signal predicts flush timing no better than random).

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical dates when the BTC trend score exceeded the strong-uptrend threshold; compare the forward 14-day carry P&L distribution (funding income minus basis move) of a trend-throttled book vs a fully-deployed book. Predict that throttled book shows smaller left tail with minimal reduction in median outcome.

## Rules

### Trend signal construction

**Primary trend gate (4h and daily):**
- **Trend score:** defined as BTC price relative to its 20-period SMA on the daily chart.
  - `trend_score_up = (close - SMA20_daily) / SMA20_daily` — normalised distance above SMA
  - `trend_score_dn = (SMA20_daily - close) / SMA20_daily` — normalised distance below SMA (only positive when below)
- **Strong uptrend threshold:** `trend_score_up ≥ 0.15` (price ≥ 15% above 20-day SMA) **AND** 4h RSI ≥ 70 **AND** funding 7-day average ≥ 0.05%/8h (elevated funding confirms perp premium stretched into the trend).
- **Strong downtrend threshold:** `trend_score_dn ≥ 0.12` (price ≥ 12% below 20-day SMA) **AND** 4h RSI ≤ 30.
- **Neutral zone:** neither threshold active; carry book at full deployment.

### Carry book deployment levels

| Regime | Carry-book size | Rationale |
|---|---|---|
| **Neutral** (no strong trend) | 100% of target notional | Full carry deployment; collect normal funding income |
| **Strong uptrend entering** | 60% of target notional | Reduce short-perp leg to 60%; retain partial carry income while limiting squeeze/flush exposure |
| **Strong uptrend sustained (7+ days)** | 30% of target notional | Further reduce if trend persists; funding may be peaking |
| **Strong downtrend** | 50% of target notional | Reduce for venue and depeg risk, but maintain half-size as downtrends often still pay positive funding from remaining longs |
| **Kill: funding inverts** | 0% (exit) | If 7-day funding average turns negative, the carry primitive has stopped working; exit regardless of trend |

### Re-entry conditions

1. **Trend score normalises:** both uptrend and downtrend conditions return to neutral zone AND 4h RSI is between 35–65.
2. **Funding confirms carry resumes:** 7-day average funding ≥ 0.02%/8h (carry income is positive and non-trivial).
3. **Re-enter in tranches:** return to 100% over 3 days — one-third per day — to avoid chasing a volatile re-entry.
4. **No re-entry during funding inversion:** if carry has inverted (negative funding), do not re-enter even if trend normalises; wait for funding to return positive for 3 consecutive 8h periods.

### Position mechanics

- **Carry book construction:** short BTC perp / long BTC spot, delta-neutral. (Identical to [[carry-with-tail-hedge]] and [[funding-rate-arbitrage]] for the base position mechanics.)
- **Trend throttle on the short-perp leg only:** reduce the perp short according to the regime table above; the spot leg is reduced proportionally. Avoid stranding unhedged spot exposure.
- **Cost of throttle:** the missed carry income during reduced deployment. At 10% APY and a 30% reduction for 14 days: 10% × 30% × (14/365) = approximately 11.5 bps of carry cost per throttle event. This is the hurdle the trend gate must clear in saved drawdowns to be net-additive.

## Implementation pseudocode

```python
# trend_aware_carry.py

from dataclasses import dataclass
from typing import Optional

# ---- trend thresholds ----
UPTREND_SMA_DIST        = 0.15    # price >= 15% above 20d SMA
UPTREND_RSI_MIN         = 70      # 4h RSI confirms overbought
UPTREND_FUNDING_MIN     = 0.050   # 7d avg funding >= 0.05%/8h (crowd stretched)
DOWNTREND_SMA_DIST      = 0.12    # price >= 12% below 20d SMA
DOWNTREND_RSI_MAX       = 30      # 4h RSI confirms oversold
SUSTAINED_UPTREND_DAYS  = 7       # days at strong-uptrend before further reduction

# ---- funding kill ----
FUNDING_KILL_THRESHOLD  = 0.0     # exit if 7d avg funding turns negative

# ---- carry-book deployment fractions ----
DEPLOY_NEUTRAL           = 1.00
DEPLOY_STRONG_UP         = 0.60
DEPLOY_STRONG_UP_SUSTAINED = 0.30
DEPLOY_STRONG_DN         = 0.50
DEPLOY_FUNDING_INVERT    = 0.00

@dataclass
class TrendState:
    close:               float
    sma20_daily:         float
    rsi_4h:              float
    funding_7d_avg_8h:   float  # 7-day average 8h funding rate
    days_in_strong_up:   int    # consecutive days above uptrend threshold

def trend_regime(s: TrendState) -> str:
    if s.funding_7d_avg_8h < FUNDING_KILL_THRESHOLD:
        return "FUNDING_INVERT"
    up_dist = (s.close - s.sma20_daily) / s.sma20_daily if s.sma20_daily > 0 else 0
    dn_dist = (s.sma20_daily - s.close) / s.sma20_daily if s.sma20_daily > 0 else 0
    strong_up = (up_dist >= UPTREND_SMA_DIST
                 and s.rsi_4h >= UPTREND_RSI_MIN
                 and s.funding_7d_avg_8h >= UPTREND_FUNDING_MIN)
    strong_dn = (dn_dist >= DOWNTREND_SMA_DIST and s.rsi_4h <= DOWNTREND_RSI_MAX)
    if strong_up and s.days_in_strong_up >= SUSTAINED_UPTREND_DAYS:
        return "STRONG_UP_SUSTAINED"
    if strong_up:
        return "STRONG_UP"
    if strong_dn:
        return "STRONG_DN"
    return "NEUTRAL"

def target_deployment(s: TrendState) -> tuple[float, str]:
    regime = trend_regime(s)
    deployment = {
        "NEUTRAL":              DEPLOY_NEUTRAL,
        "STRONG_UP":            DEPLOY_STRONG_UP,
        "STRONG_UP_SUSTAINED":  DEPLOY_STRONG_UP_SUSTAINED,
        "STRONG_DN":            DEPLOY_STRONG_DN,
        "FUNDING_INVERT":       DEPLOY_FUNDING_INVERT,
    }[regime]
    return deployment, regime

def carry_sizing(target_notional: float, s: TrendState) -> dict:
    deployment, regime = target_deployment(s)
    active_notional = target_notional * deployment
    return {
        "carry_notional":    active_notional,
        "deploy_fraction":   deployment,
        "regime":            regime,
        "short_perp_size":   active_notional,
        "long_spot_size":    active_notional,
        "carry_income_7d_bps": s.funding_7d_avg_8h * 3 * deployment,  # 3 funding periods/day × fraction
        "note": (f"regime={regime}, deploy={deployment:.0%}, "
                 f"SMA_dist={(s.close - s.sma20_daily)/s.sma20_daily:+.2%}, "
                 f"RSI4h={s.rsi_4h:.1f}, funding7d={s.funding_7d_avg_8h:.4f}")
    }

def reentry_check(s: TrendState, days_since_exit: int) -> dict:
    """Check whether a fully-exited carry book can re-enter."""
    if s.funding_7d_avg_8h < 0.0002:   # funding below 0.02%/8h — too thin
        return {"reenter": False, "reason": "funding too low for carry to be economic"}
    regime = trend_regime(s)
    if regime != "NEUTRAL":
        return {"reenter": False, "reason": f"trend still in regime={regime}"}
    tranche = min(days_since_exit, 3)   # re-enter at 1/3 per day over 3 days
    return {"reenter": True, "tranche_fraction": tranche / 3,
            "note": f"re-entering day {days_since_exit} of 3-day ramp"}
```

The production system adds: real-time funding rate monitor (polling `/api/v1/derivatives/funding-rates` every 8h); daily SMA and RSI calculation on OHLCV klines; an alert for when `days_in_strong_up` hits 7 (trigger second-reduction); and a P&L attribution separating carry income, mark-to-market basis move, and throttle-period opportunity cost.

## Indicators / data used

- **Daily OHLCV (close, SMA20)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30`; compute 20-period SMA and price distance.
- **4h OHLCV (RSI)** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50`; compute 14-period RSI.
- **Funding rate (7-day average)** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; 7-day trailing average of 8h funding periods.
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; context for confirming perp premium stretch alongside trend.
- **Perp and spot price (basis)** — perp mark price from the derivative venue; spot reference from klines. Track the perp premium separately to confirm basis is not inverting.
- **Regime context** — `GET /api/v1/regimes/current`; block re-entry in `Structural_Shock` regardless of trend normalisation.

## Example trade

**Setup (illustrative — strong uptrend throttle event):**

- BTC: $95,000. SMA20-daily = $80,000. SMA distance = (95,000 − 80,000) / 80,000 = **+18.75%** (above 15% threshold).
- 4h RSI = 74 (above 70 threshold).
- 7-day average 8h funding = 0.061%/8h (above 0.05% threshold).
- All three uptrend conditions pass → **STRONG_UP regime**.
- Current carry-book deployment = 100% ($500,000 notional short perp / long spot).
- Target deployment = 60% → reduce to $300,000 notional. Close $200,000 of short-perp / sell $200,000 of spot.

**During reduced deployment (days 1–7):**
- BTC continues trending from $95,000 to $102,000 (+7.4%).
- Perp premium widens further; funding spikes to 0.10%/8h for 3 days before normalising.
- At 60% deployment, the carry book earns 60% × the funding income from these 7 days, and the mark-to-market loss on the short-perp leg is reduced by 40% relative to full deployment.
- Carry income during throttle window: 0.08% avg × 3 periods/day × 7 days × $300,000 = **$504** collected.
- Basis blowout avoided (on the $200,000 not held): assume perp/spot premium widened +1.2% then normalised; unrealised mark-to-market loss avoided = $200,000 × 1.2% = **$2,400 loss avoided** (would have had to absorb if held at 100% — this is the cost saved by the throttle).

**Day 8 — trend sustained → STRONG_UP_SUSTAINED:** reduce further from 60% to 30%. Close additional $150,000 of short-perp / spot.

**Day 14 — trend normalises:** BTC consolidates at $98,000. SMA distance = +22.5% (SMA now $80,000 + growth). Wait for SMA to catch up. After 5 more days, SMA20 reaches $84,000 and distance falls to +16.7%; RSI drops to 58. After 2 more days, distance = +14.8% (below 15%) and RSI = 52 — neutral zone confirmed.
- Funding 7-day avg = 0.028%/8h (above 0.02% re-entry floor). Re-enter at +1/3 per day: $333K → $500K over 3 days.

**Round-trip P&L sketch:**
- Carry income during full deployment (pre-throttle, days −30 to 0): 0.03% avg × 3 × 30 × $500K = **$13,500**.
- Carry income during throttle (days 0–14 at reduced size): ~**$2,200** (at 60% then 30% average).
- Basis blowout avoided: **$2,400** (estimated).
- Carry income missed (cost of throttle vs full deployment): full would have earned ~$3,600; earned $2,200 → cost = **−$1,400**.
- Net benefit of throttle: $2,400 (avoided loss) − $1,400 (missed carry) = **+$1,000** net positive.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Higher than plain carry (~0.9) due to drawdown reduction; lower than carry-with-tail-hedge if hedges are well-timed |
| Expected max drawdown | ~12% | Trend throttle reduces the worst funding-flush drawdowns; remaining drawdown comes from delayed throttle response |
| Carry income reduction | ~8–15% | Throttle periods reduce total funding collected; carry at 60–100% of full deployment on average |
| Regime transition cost | 5–20 bps | Closing and reopening the short-perp/spot pair incurs trading costs; 2–4 transitions/year at 5 bps each = 10–20 bps annual drag |
| Breakeven cost budget | 20 bps | Tight; carry books are low-cost strategies; the throttle adds transition costs |

**Cost overlay:** unlike options-overlay strategies, the trend-aware carry has no theta or option-premium costs. The cost is purely in the form of (a) trading costs on transitions (5 bps per round-trip × 4–8 transitions/year ≈ 20–40 bps) and (b) the missed carry during throttle periods. The sum of these two cost types is the hurdle the trend gate must clear in saved drawdowns.

## Capacity limits

- **Binding constraint:** the carry book's capacity — not the trend overlay. At $500M+ notional, a single operator reducing their short-perp position by 40% moves the funding market itself, partly defeating the purpose of the throttle.
- `capacity_usd: 150000000` — the trend overlay does not add capacity; it is a sizing discipline on the underlying carry book, which is the binding constraint.
- **Transition liquidity:** closing $200M of BTC perp at a liquid venue (Binance, Hyperliquid) has minimal market impact; the carry book's scale is the relevant constraint.

## What kills this strategy

1. **Carry compression to zero (#2: Cost structure).** As Ethena/Resolv/Pendle and institutional carry operators crowd the trade, funding rates compress to near-zero. At 3% APY carry, the transaction costs of throttle transitions become a large fraction of the carry income; the strategy becomes uneconomic. The `kill_criteria` condition (net carry after throttle < 3% APY) addresses this.
2. **Trend signal generates false exits (#5: Regime change / miscalibration).** If the 15% SMA-distance threshold fires in every mild uptrend, the carry book spends too many days at 60% deployment, and the missed-carry cost exceeds the avoided-loss benefit. The kill condition tracking throttle events vs. subsequent actual funding flushes catches this.
3. **Funding persists at extreme levels through strong uptrend (#4: Crowding).** In some bull markets, funding stays elevated for months (2021: 0.10%+ consistently for 90+ days). The strategy at 30% deployment for 90 days misses large amounts of carry income. This is a feature not a bug for risk management, but is economically painful if the trend never produces a crash.
4. **Venue / exchange risk (#7: Operational).** The carry book's short-perp leg is concentrated on a perp venue. A venue failure during the re-entry phase (when the carry book is scaling back up) at the worst time is the main operational tail. Same as [[carry-with-tail-hedge]] and [[funding-rate-arbitrage]].
5. **Basis inversion during downtrend (#5: Regime change).** In extreme downtrends, perp can trade at a discount to spot (negative funding for extended periods). The `FUNDING_INVERT` kill exits the carry book entirely; if this happens during a delayed downtrend detection, the book absorbs a period of negative carry before the exit fires.

## Kill criteria

Pause on any of:

1. **Carry book drawdown > 12% net of hedge P&L in rolling 30 days** (with trend overlay active) — the overlay has not prevented a substantial drawdown.
2. **Trend overlay fires > 60% of trading days over 90 consecutive days** — perpetually throttled; thresholds are miscalibrated for the current market; recalibrate the SMA-distance threshold to a level that fires less frequently.
3. **Annualised net carry after throttle period costs < 3% APY** — carry primitive no longer compensates for exchange and basis risk; shut down the book regardless of overlay.
4. **Trend throttle exits consistently followed by carry recovery < funding missed during exit window** across 6 consecutive throttle events — overlay is destroying value; the trend exits are worse than staying deployed.
5. **7-day funding average turns negative on > 50% of held positions** — funding carry primitive dead; the underlying carry edge has disappeared.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Reduces the worst regime for the carry book** — strong trending regimes are where carry books suffer funding flushes and basis blowouts; the throttle directly targets the carry book's most dangerous operating environment.
- **No options premium cost** — unlike [[carry-with-tail-hedge]], this overlay costs nothing beyond trading costs for transitions; there is no annual premium budget.
- **Self-funding overlay** — the carry book funds its own risk management through funding income; no separate budget line is needed.
- **Interpretable signals** — the SMA distance, RSI, and funding conditions are transparent, verifiable, and have clear economic rationales; the overlay is not a black-box model.
- **Composable with carry-with-tail-hedge** — a practitioner can run both overlays simultaneously: the tail hedge (carry-with-tail-hedge) as permanent convexity protection, and the trend throttle (this page) as a regime-based sizing discipline. The two are not mutually exclusive.

## Disadvantages

- **Missed carry during throttle periods is real cost** — every day at 60% or 30% deployment is a day of forgone carry income. In a strong-trending, high-funding market, this can be a 30–60% reduction in annual carry income for that period.
- **Delayed signal response** — the SMA20-distance threshold lags the actual trend development by construction; the carry book may absorb the first part of a funding flush before the throttle fires, since the distance needs time to reach 15%.
- **Does not protect against instantaneous shocks** — a sudden exchange failure or oracle divergence event is not trend-based; the throttle is irrelevant to this class of risk. [[carry-with-tail-hedge]] is better suited to protect against instantaneous tails.
- **Threshold calibration sensitivity** — the 15% SMA-distance and 0.05% funding-threshold levels require periodic review as market structure evolves. Bull markets with different trend geometry (slower SMA drift, more funding spikes at lower distances) may require recalibration.
- **Not a hedge, a reduction** — even at 30% deployment in a strong-uptrend-sustained regime, the carry book retains a short-perp position that suffers if funding flushes. The throttle mitigates but does not eliminate the exposure.

## Sources

- [[carry-with-tail-hedge]] — the hedged carry variant; the comparison between the tail-hedge approach and the trend-throttle approach is the core design decision for carry operators.
- [[funding-rate-arbitrage]] — the plain carry primitive; the mechanics of the short-perp/long-spot carry book are fully described there.
- BIS Working Paper No. 1087 — Schmeling, Schrimpf, Todorov (2023): documents the relationship between elevated funding rates and subsequent cryptocurrency price corrections; the empirical basis for why strong-uptrend + high-funding is the regime where carry flush risk is highest.
- [[funding-conditioned-vol-selling]] — uses the same funding signal for a different overlay (vol-selling gate); the funding-as-crowd-proxy logic is shared.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30` — daily OHLCV; compute SMA20 and price-SMA distance (Gate 1 of trend score)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50` — 4h OHLCV; compute 14-period RSI (Gate 2)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding rates; 7-day average for Gate 3 and funding-kill condition
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI context; confirms perp-premium stretch alongside trend
- `GET /api/v1/regimes/current` — macro regime; blocks re-entry in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — long daily OHLCV for SMA calibration and throttle-event backtest
- `GET /api/v1/derivatives/binance/history?days=365` — extended funding and derivatives history for throttle-vs-flush-event analysis

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this carry book end-to-end:

- **Signal** — `GET /api/v1/derivatives/funding-rates?coin=BTC` 7-day average is the carry leg; the trend score comes from daily (SMA20) and 4h (RSI) klines
- **Throttle** — the funding-kill condition and the `GET /api/v1/derivatives/open-interest?coin=BTC` stretch check scale the carry book down as trend and positioning diverge
- **Regime gate** — `GET /api/v1/regimes/current` blocks re-entry in `Structural_Shock`
- **Backtest** — carry replay from `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05 — the deepest honest funding archive; Binance daily since 2026-03-30) joined to `GET /api/v1/backtesting/klines` (1d back to 2017-08) for the trend overlay
- **Tips** — accrue funding per settlement timestamp in the backtest; averaging it daily hides exactly the settlement-window spikes the throttle exists to catch

## Related

- [[carry-with-tail-hedge]] — permanent OTM put overlay on the same carry book; contrasts with this page's size-reduction approach
- [[funding-vs-basis-rotation]] — allocation between perp-carry and dated-futures carry; complements rather than competes with this page's trend throttle
- [[funding-rate-arbitrage]] — the plain carry primitive; provides the underlying mechanics
- [[cash-and-carry]] — the spot-futures basis carry variant; same structural logic, different instrument
- [[funding-filtered-momentum]] — the inverse relationship: momentum gated on funding level (vs. carry gated on trend here)
- [[vol-targeted-trend-following]] — trend strategy with volatility sizing; the analogous overlay applied to a different primitive (momentum)
- [[trend-following-cta]] — the canonical trend primitive; the source of the trend signal methodology used as the overlay here
- [[oi-confirmed-trend]] — OI as a trend-confirmation signal; the OI component can supplement the trend score
- [[crowded-long-funding-fade]] — fades the directional exposure when funding is stretched; this page reduces carry exposure in the same regime
- [[funding-conditioned-vol-selling]] — uses funding as a crowding proxy for vol entry; the same signal applied to a different primitive
- [[edge-taxonomy]] — structural + behavioral + analytical classification
- [[failure-modes]] — carry compression, false exits, sustained trending periods
- [[when-to-retire-a-strategy]] — kill vs pause framework
