---
title: "Crypto Beta Rotation"
type: strategy
created: 2026-07-14
updated: 2026-07-19
status: good
tags: [quantitative, crypto, bitcoin, market-regime, regime-detection, correlation, risk-management, macro]
aliases: ["Crypto Risk-On/Off Rotation", "Crypto Macro Regime Rotation", "Crypto Beta Hedging Overlay", "DXY Nasdaq Crypto Rotation", "Risk-Regime De-Beta"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested

# Edge characterization
edge_source: [structural, behavioral, analytical]
edge_mechanism: "When crypto's rolling correlation to Nasdaq/equities is high, Bitcoin trades as a high-beta risk asset whose direction is set by the macro tape, not by the halving clock or on-chain flows; a strengthening DXY plus a risk-off correlation regime carries negative expected crypto returns, so systematically cutting or hedging crypto-directional beta in those windows sidesteps the macro-driven drawdowns that recency-anchored holders sit through."

# Data and infrastructure requirements
data_required: [btc-nasdaq-correlation, dxy-trend, macro-sentiment, funding-rates, vol-regime-score, policy-regime]
min_capital_usd: 10000
capacity_usd: 500000000
crowding_risk: low

# Performance expectations (as a risk overlay, net of hedge cost)
expected_sharpe: 0.8
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

# Decay history
decay_evidence: "The crypto-macro correlation is itself regime-dependent and non-stationary: BTC-Nasdaq 30-day correlation ran near zero through much of 2019-2020 and again in idiosyncratic 2023 stretches, then spiked to ~0.6-0.7 in the 2022 tightening cycle and the Aug-2024 yen unwind. The edge exists only while crypto trades as macro beta; in decoupled, crypto-idiosyncratic regimes the overlay adds cost without benefit — so the signal must gate itself on the correlation regime being active."

# Lifecycle (naive-backtested; not deployed)
capital_allocation: "risk overlay on a crypto-directional book; scales target beta 0.0-1.0 by risk-regime"
kill_criteria: |
  - BTC-Nasdaq correlation collapses toward zero for 20+ days (overlay adds cost, no benefit)
  - overlay underperforms static exposure over a rolling 6 months (whipsaw)
  - hedge instrument basis/cost exceeds the modeled risk-off drawdown avoided
  - macro-regime data feed disruption
last_review: 2026-07-14
next_review: 2026-08-14

related: ["[[crypto-macro-correlation-regime]]", "[[macro-trend-regime]]", "[[bitcoin-cycle-regime]]", "[[dxy]]", "[[correlation]]", "[[vix]]", "[[gold]]", "[[regime-detection]]", "[[momentum-rotation]]", "[[macro-relative-value]]", "[[yen-carry-trade]]", "[[tail-risk-hedging]]", "[[funding-rate]]", "[[bitcoin]]", "[[ethereum]]", "[[position-sizing]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi]]"]
---

# Crypto Beta Rotation

Crypto Beta Rotation is a **risk-regime overlay** that dials crypto-directional exposure up and down according to whether the macro tape is risk-on or risk-off. Its premise: when crypto's rolling correlation to the Nasdaq is high, [[bitcoin|BTC]] trades as a **high-beta risk asset** whose direction is set by rates, the dollar, and equity risk appetite — not by the [[bitcoin-halving|halving]] clock or on-chain flows. In those macro-driven windows a strengthening [[dxy|DXY]] and a risk-off [[crypto-macro-correlation-regime|correlation regime]] carry negative expected crypto returns, so the strategy **reduces or hedges crypto beta**; when the regime is risk-on (or crypto has decoupled into an idiosyncratic regime), it restores full exposure. It is not a standalone alpha source — it is a **de-beta / hedging overlay** on top of a crypto-directional book, using macro and correlation-regime signals to avoid the worst macro drawdowns.

This sits directly on top of the wiki's [[crypto-macro-correlation-regime|Macro Correlation regime (Basket #6)]], which can *override* the [[bitcoin-cycle-regime|BTC cycle]] when crypto trades as tech beta.

## Edge Source

Per [[edge-taxonomy]], the overlay draws on three edges:

- **Structural (primary).** In macro-correlated regimes, crypto is a leveraged risk-asset proxy: it responds mechanically to global liquidity, real yields, and the dollar. A strengthening DXY tightens dollar liquidity and is structurally headwind for risk assets including crypto; rising real yields raise the discount rate on long-duration speculative assets. These are structural macro linkages, not opinions — when the correlation regime is "on," crypto's beta to them is real and measurable.
- **Behavioral.** Crypto holders are recency-anchored and narrative-driven; they under-weight macro and sit through risk-off drawdowns waiting for the "next leg up." The overlay is the disciplined counter-party that cuts beta when the macro regime turns, capturing the gap between the crowd's price-anchoring and the macro reality.
- **Analytical.** The edge is in *measuring the regime* — the rolling BTC-Nasdaq correlation, the DXY trend, the vol-stress and policy-risk composites — and acting on the *conditional* expected return, rather than holding a static beta through all environments.

The overlay does **not** claim a directional forecasting edge on crypto in general — in decoupled, idiosyncratic regimes it deliberately does nothing. Its edge is *conditional*: it only fires when crypto is behaving as macro beta, which is precisely when de-risking pays.

## Why This Edge Exists

1. **Crypto's correlation to equities is high but time-varying — and the transitions are tradeable.** BTC-Nasdaq 30-day rolling correlation has swung from ~0 (2019-2020, idiosyncratic 2023 stretches) to ~0.6-0.7 (2022 rate-hike cycle, Aug-2024 yen-carry unwind). When correlation is high, the macro tape dominates crypto's direction; the overlay exploits the *conditional* predictability of risk-off drawdowns in those windows.
2. **The dollar is a genuine crypto headwind in tight-liquidity regimes.** DXY strength coincides with dollar-liquidity tightening; crypto, sitting at the far end of the risk curve, is among the first assets sold. The DXY *trend* (not level) is a durable risk-on/off gauge that leads crypto weakness in macro regimes.
3. **Holders systematically fail to de-risk.** The dominant crypto participant is long-biased and narrative-driven; de-risking into a risk-off macro turn is behaviourally rare among holders, leaving the drawdown-avoidance edge under-exploited. The overlay is a discipline the crowd lacks.

## Null Hypothesis

Under no-edge conditions, crypto's forward return is independent of the macro regime — DXY trend, BTC-Nasdaq correlation, and vol-stress carry no conditional information — so a beta-rotation overlay would just add transaction cost and whipsaw versus static full exposure. In that world:

- Conditioning target beta on the risk-regime would not improve risk-adjusted returns.
- Cutting exposure in "risk-off" windows would miss as many rallies as drawdowns (regime signal is noise).
- The overlay's Sharpe would be *below* static buy-and-hold after hedge costs.

Empirically, in *macro-correlated* regimes the null is rejected: risk-off signals (DXY breakout + high correlation + vol-stress) preceded negative crypto returns often enough that de-risking improved drawdown and risk-adjusted return. **But** in *decoupled* regimes the null holds — the overlay adds cost with no benefit, and forcing it on during idiosyncratic 2023-style stretches would have whipsawed. This is why the strategy's first gate is *"is the correlation regime even active?"* — it disables itself when crypto is not trading as macro beta. The naive-backtest caveat is real: the regime signal is non-stationary and the sample of clean risk-off events is small.

## Rules

### Regime signals (composite)

- **BTC-Nasdaq rolling correlation (30-day):** the master gate. Overlay is **active** only when correlation ≥ ~0.4 (crypto is trading as macro beta). Below that, hold static exposure (overlay off).
- **[[dxy|DXY]] trend:** risk-off tilt when DXY is above its 50-day MA and rising (dollar strengthening). Proxied via EUR/USD + macro-sentiment where a direct DXY feed is unavailable (see *Getting the Data*).
- **Vol-stress composite:** rising crypto vol-stress score and/or a [[vix|VIX]] spike corroborate risk-off.
- **Policy/rates tilt:** hawkish rate calendar / rising real yields add to the risk-off score; dovish subtracts.
- **Crypto-internal risk appetite:** [[funding-rate]] and liquidity-fragility as confirming internal tells (collapsing funding + rising fragility = risk-off underway).

### Target-beta mapping

Combine the signals into a **risk-regime score** and map it to a target crypto beta for the book:

| Regime | Correlation | DXY trend | Vol-stress | Target crypto beta | Action |
|---|---|---|---|---|---|
| **Risk-on (macro)** | ≥0.4 | falling / below MA | low | 1.0 | Full exposure |
| **Neutral (macro)** | ≥0.4 | flat | moderate | 0.5-0.7 | Trim |
| **Risk-off (macro)** | ≥0.4 | rising / above MA | high | 0.0-0.3 + hedge | Cut hard, add hedge |
| **Decoupled (idiosyncratic)** | <0.4 | any | any | hold static | Overlay OFF — defer to [[bitcoin-cycle-regime]] |

### Implementation of the de-beta

- **Cut exposure** by reducing spot/perp longs (cheapest), or
- **Hedge** by shorting BTC/ETH perp against the core, or shorting a crypto-beta proxy, or buying downside via [[tail-risk-hedging|puts]] when vol is not yet spiked.
- Prefer *reducing* over *hedging* when the book is small and the hedge basis/funding cost is high; prefer *hedging* when the operator wants to retain the underlying (tax, custody, staking) and only neutralise beta.

### Sizing / cadence

- **Rebalance the target beta** on a daily-to-weekly cadence (regime signals are daily; avoid intraday churn — the overlay's enemy is whipsaw).
- **Hysteresis band:** require the risk-regime score to move a full band (not a marginal tick) before changing target beta, to suppress whipsaw.
- **Cap hedge cost:** if the funding/basis/premium cost of the hedge over the expected risk-off window exceeds the modeled drawdown avoided, *reduce* instead of hedge, or stand down.

## Implementation Pseudocode

```python
# crypto_beta_rotation.py — risk-regime overlay dialing crypto beta 0..1
# Status: naive-backtested. Regime signals from CryptoDataAPI macro/vol/policy + external DXY/Nasdaq.

CORR_GATE   = 0.40   # overlay active only when BTC-Nasdaq corr >= this
BANDS       = {"RISK_ON": 1.0, "NEUTRAL": 0.6, "RISK_OFF": 0.15}

def risk_regime(sig):
    if sig.btc_nasdaq_corr_30d < CORR_GATE:
        return "DECOUPLED"                       # overlay off -> defer to cycle/flow books
    score = 0
    score += 1 if (sig.dxy > sig.dxy_ma50 and sig.dxy_rising) else -1   # dollar
    score += 1 if sig.vol_stress_score > 60 else 0                      # crypto vol stress
    score += 1 if sig.vix_spike else 0                                  # equity vol
    score += 1 if sig.policy_tilt_hawkish else -1 if sig.policy_tilt_dovish else 0
    score += 1 if (sig.funding_collapsing and sig.liquidity_fragile) else 0
    if score >= 3:   return "RISK_OFF"
    if score <= -1:  return "RISK_ON"
    return "NEUTRAL"

def target_beta(sig, book):
    regime = risk_regime(sig)
    if regime == "DECOUPLED":
        return book.static_target_beta           # hand back to non-macro books
    return BANDS[regime]

def rebalance(book, sig):
    tgt = target_beta(sig, book)
    # hysteresis: only move if a full band away from current
    if abs(tgt - book.current_beta) < 0.25:
        return hold("within hysteresis band")
    if tgt < book.current_beta:
        # de-beta: reduce longs, or hedge if retaining underlying is preferred
        if book.prefer_retain and hedge_cost_ok(sig, tgt):
            return short_perp_hedge(book, to_beta=tgt)      # budget funding/basis
        return reduce_longs(book, to_beta=tgt)
    return add_longs(book, to_beta=tgt)                     # restore exposure risk-on
```

## Indicators / Data Used

- **BTC-Nasdaq rolling correlation (30-day)** — the master gate; whether crypto is trading as macro beta at all. Computed from crypto price + external Nasdaq series.
- **[[dxy|DXY]] trend** — the dollar-liquidity risk-on/off gauge; proxied via EUR/USD + macro-sentiment where a direct DXY feed is unavailable.
- **Macro sentiment (EUR/USD, [[gold]], yields)** — the dollar and real-rate backdrop from [[cryptodataapi-sentiment|CryptoDataAPI macro sentiment]].
- **Vol-stress composite / [[vix|VIX]]** — crypto and equity fear corroboration.
- **Policy / rate-calendar tilt** — hawkish-vs-dovish macro overlay.
- **[[funding-rate]] + liquidity fragility** — crypto-internal risk-appetite tells that confirm a macro risk-off is transmitting into crypto positioning.
- **[[crypto-macro-correlation-regime]] / [[macro-trend-regime]]** — the wiki's own regime labels the overlay is an expression of.

Note: Nasdaq and a pure DXY index are external macro series; [[cryptodataapi]] supplies EUR/USD + gold + yields (macro sentiment), the vol-stress and policy composites, funding, and liquidity-regime — the crypto-side and macro-proxy inputs (see *Getting the Data*).

## Example Trade

**Setup (illustrative risk-off turn, macro-correlated regime).** BTC-Nasdaq 30-day correlation is **0.62** (overlay active). DXY has broken above its 50-day MA and is rising; the macro-sentiment feed shows yields ticking up and EUR/USD weakening (dollar strength). Crypto vol-stress score is 68 and rising; equity VIX has spiked; [[funding-rate|funding]] is collapsing from positive toward zero and liquidity fragility is climbing. Risk-regime score = +4 → **RISK_OFF**.

- **Current book beta:** 1.0 (fully long a BTC/ETH core).
- **Action:** target beta → 0.15. The operator wants to retain the underlying (staking + AU CGT clock), so instead of selling, **short BTC/ETH perp** against ~85% of the core to neutralise beta. Funding is near zero, so the hedge carry is cheap (`hedge_cost_ok` passes).
- **Outcome (risk-off plays out):** crypto sells off ~15% over the following two weeks with the equity tape; the perp hedge offsets ~85% of the drawdown, so the book draws down ~2-3% instead of ~15%. When the risk-regime score falls back below the RISK_OFF band (DXY rolls over, correlation eases, vol-stress recedes), the hedge is lifted and beta restored to 1.0.

**Counter-example (whipsaw cost).** A one-day DXY spike and VIX blip push the score into RISK_OFF, the hedge goes on, and the macro scare reverses within 48 hours. The overlay pays the round-trip hedge cost and misses ~1-2% of a bounce before restoring beta. This is the modal cost of the strategy — small, frequent whipsaw — and is why the **hysteresis band and the correlation gate** exist: to keep whipsaw below the drawdown-avoidance benefit.

## Performance Characteristics

Realistic picture as a *risk overlay* on a crypto-directional book (naive-backtested; the regime signal is non-stationary — treat with caution):

| Metric | Estimate | Note |
|---|---|---|
| Drawdown reduction vs static beta | Meaningful in macro-correlated risk-off (e.g. 2022, Aug-2024) | The overlay's whole purpose; largest benefit in the worst months |
| Sharpe uplift vs static | +0.1 to +0.3 (overlay Sharpe ~0.8) | From avoiding the fat left tail, partly offset by whipsaw |
| Whipsaw cost | Small, frequent | Hedge round-trips on false risk-off signals; the dominant drag |
| Hit rate on risk-off calls | Modest (~55-60%) | The value is asymmetric — the *wins* (avoided drawdowns) are large |
| Correlation to BTC | 1.0 risk-on, →0 or negative risk-off | By construction — it dials beta |

**Cost overlay — this is a hedging overlay, so cost is hedge carry + whipsaw, not a naive backtest:**

| Friction | Magnitude | Note |
|---|---|---|
| Perp hedge funding | ±5-15% APY on hedged notional | A short-perp hedge often *collects* positive funding in a still-long-heavy market (a tailwind); can be a drag if funding is negative |
| Spot/perp round-trip | 4-10 bps per rebalance on BTC/ETH | Kept low by the hysteresis band and daily-weekly cadence |
| Put-hedge premium (if used) | Vol-dependent | Expensive once vol has spiked; prefer perp hedge or reduction after the spike |
| Whipsaw drag | The main cost | False risk-off signals; suppressed by the correlation gate + hysteresis |
| Basis/tracking error | Small on BTC/ETH perp vs spot | Larger if hedging with an imperfect crypto-beta proxy |

The honest framing: in *macro-correlated* regimes the overlay earns its keep by cutting the fat left tail; in *decoupled* regimes it is pure cost, which is why the correlation gate disables it. `breakeven_cost_bps: 25` reflects that the trade is only worth running when the avoided drawdown exceeds the hedge + whipsaw cost.

## Capacity Limits

- High capacity — the overlay trades BTC/ETH spot/perp, the deepest crypto markets, in size-agnostic proportion to the book it sits on. An operator can run the overlay on **hundreds of millions** of crypto-directional exposure before hedge-execution impact matters; reflected in `capacity_usd: 500000000`.
- The binding constraint is not liquidity but **hedge basis at size** — a very large perp hedge can move funding against the operator, and put-hedging at scale moves the [[implied-volatility|IV]] surface. Both are manageable at individual/small-fund scale.
- Because it is an *overlay*, its capacity is effectively the capacity of the underlying directional book plus the depth of the hedge instrument (BTC/ETH perp), both large.

## What Kills This Strategy

Mapped to [[failure-modes]]:

1. **Correlation decoupling (Failure Mode #5: The Regime Changed).** The dominant risk. When BTC-Nasdaq correlation collapses toward zero (2019-2020, idiosyncratic 2023), crypto stops trading as macro beta and the overlay's signals become noise — it hedges risk-off calls that never transmit into crypto, paying cost for no benefit. The correlation gate mitigates this but the transitions are the danger.
2. **Non-stationary regime signal (Failure Mode #4/#5).** The crypto-macro relationship is unstable; a DXY/correlation rule fit on 2022 may misfire in a different macro structure. The overlay must be treated as a prior, re-validated across regimes.
3. **Whipsaw (Failure Mode: over-trading).** Choppy macro (frequent false risk-off/on flips) grinds the overlay through repeated hedge round-trips. Hysteresis and the daily-weekly cadence suppress but do not eliminate this.
4. **Hedge-cost blowout.** In a negative-funding or high-put-premium environment, the hedge costs more than the drawdown it avoids; the overlay must prefer *reducing* to *hedging* in those windows.
5. **Signal-latency shocks (Failure Mode #6).** A macro gap can move crypto before the daily regime signals confirm risk-off; the overlay is a step behind the fastest shocks (a genuine limitation shared with [[etf-flow-directional]]).
6. **Data-feed disruption.** The overlay depends on external Nasdaq/DXY series and the macro-sentiment/vol/policy composites; a feed outage blinds the regime classifier.

## Kill Criteria

Paused or disabled on any of:

1. **BTC-Nasdaq correlation < ~0.2 for 20+ days** → crypto is decoupled; disable the overlay and defer to the [[bitcoin-cycle-regime]]/[[etf-flow-directional]] books (the correlation gate does this automatically; a sustained breach is the sleeve-level kill).
2. **Overlay underperforms static exposure over a rolling 6 months** → whipsaw is dominating the drawdown-avoidance benefit; suspend and re-fit.
3. **Hedge instrument basis/cost exceeds the modeled risk-off drawdown avoided** → switch to reduction-only or stand down.
4. **Macro-regime data-feed disruption** → hold static exposure until the feed is restored (do not act on stale signals).
5. **Rolling drawdown-reduction benefit turns negative across two consecutive risk-off events** → the regime linkage has broken; retire until re-validated.

Re-engage: correlation regime active again (≥0.4), overlay back to improving risk-adjusted return in walk-forward, and hedge cost below the avoided-drawdown budget. See [[when-to-retire-a-strategy]].

## Instrument Structures

Crypto beta rotation deploys across all structure types, moving between them as the macro-correlation regime shifts.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Single-asset** | The defensive mode: reduce crypto exposure to BTC and ETH only (the highest-liquidity, lowest-idiosyncratic-risk tokens) when the macro-correlation regime activates. BTC-PERP and ETH-PERP carry the book when hedging. |
| **Basket** | The risk-on mode: when correlation is low and the alt-season gate is active, the book deploys across multiple sector baskets (e.g., [[l1-blockchains-basket]], [[ai-tokens-basket]], [[defi-bluechip-basket]]) for diversified crypto beta exposure. Baskets provide the cross-sectional breadth needed to capture alt-season returns. |
| Pair | Not the primary deployment, but beta rotation can be expressed as a BTC/ETH pair spread — long ETH-PERP (higher beta, alt-correlated), short BTC-PERP (lower beta, macro-correlated) when rotating into risk-on mode. |
| Cross-venue | Not deployed. The strategy operates within a single venue (Hyperliquid) for simplicity; cross-venue execution is a tactical add-on, not a structural feature. |

The mechanics change between structures: in single-asset (defensive) mode, position sizing uses [[atr-position-sizing]] at the BTC/ETH level; in basket (risk-on) mode, sizing is per-basket-notional with equal-weight across active baskets, scaled down by the vol-regime overlay from [[volatility-targeting]].

## Advantages

- **Targets the fat left tail** — cuts crypto's worst macro-driven drawdowns (2022, Aug-2024) that buy-and-hold sits through; asymmetric payoff (large avoided losses).
- **Self-disabling** — the correlation gate turns the overlay off when crypto decouples, so it does not fight idiosyncratic regimes.
- **Retains the underlying if desired** — hedging (rather than selling) preserves custody, staking, and the AU >12-month CGT clock on the core.
- **High capacity, cheap instruments** — BTC/ETH spot/perp; low transaction cost, large capacity.
- **Composable overlay** — sits cleanly on top of directional, cycle, or flow books; a portfolio-level risk dial rather than a competing alpha.
- **Grounded in the wiki's regime map** — a direct expression of [[crypto-macro-correlation-regime|Basket #6]] and [[macro-trend-regime]].

## Disadvantages

- **Non-stationary, regime-dependent edge** — only works while crypto trades as macro beta; the correlation itself is unstable and the transitions are hard.
- **Whipsaw drag** — false risk-off signals cost hedge round-trips; the main ongoing cost.
- **Naive-backtested on a small event sample** — few clean macro risk-off episodes; parameter confidence is limited.
- **Signal latency** — a step behind the fastest macro gaps; the daily regime signal lags intraday shocks.
- **Not standalone alpha** — an overlay that improves an existing book's risk profile; it does not generate return on its own in risk-on or decoupled regimes (it just holds full beta).
- **External data dependence** — needs Nasdaq/DXY series plus the macro/vol/policy composites; feed outages blind it.

## Sources

- [[crypto-macro-correlation-regime]] — the wiki's Macro Correlation regime (Basket #6); the framing this strategy operationalises, including how high correlation *overrides* the [[bitcoin-cycle-regime|BTC cycle]].
- [[macro-trend-regime]] — the broad risk-on/off backdrop the overlay reads.
- [[dxy]] — the dollar index as a crypto risk-on/off gauge and its inverse relationship to crypto.
- BIS Bulletin No. 90, "The market turbulence and carry trade unwind of August 2024" — the canonical recent macro-correlated crypto drawdown (BTC fell with the equity tape on the yen-carry unwind); cross-referenced on [[yen-carry-trade]] and [[liquidation-cascade-fade]].
- General macro-finance literature on time-varying risk-asset correlations and the dollar as a global-liquidity/risk gauge.

## Getting the Data (CryptoDataAPI)

Nasdaq and a pure DXY index are external macro series; [[cryptodataapi]] supplies the macro-proxy (EUR/USD + gold + yields), the vol-stress and policy composites, funding, and liquidity-regime — the crypto-side regime inputs.

**Live data:**
- `GET /api/v1/sentiment/macro` — EUR/USD (DXY proxy), gold, and yields (the dollar / real-rate backdrop)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/policy/regime` — policy risk + signed tilt + rate calendar (hawkish/dovish overlay)
- `GET /api/v1/quant/market` — whole-market HMM regime + probability buckets (risk-on/off context)
- `GET /api/v1/regimes/current` — current long-horizon 10-state market regime
- `GET /api/v1/liquidity/regime` — liquidity fragility score (risk-off transmission tell)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — crypto-internal risk appetite

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — Fear & Greed timeseries (risk-appetite backtest input)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — BTC series for the BTC-Nasdaq correlation computation

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/macro"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-sentiment]]; regime and vol-stress detail on [[cryptodataapi]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [fear & greed](https://cryptodataapi.com/fear-greed) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this overlay end-to-end:

- **Signal** — `GET /api/v1/sentiment/macro` for the EUR/USD (DXY proxy), gold, and yields backdrop; `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d` supplies the BTC leg of the 30-day BTC-Nasdaq correlation (the Nasdaq series stays external)
- **Regime gate** — combine `GET /api/v1/quant/market`, `GET /api/v1/volatility/regime/score`, and `GET /api/v1/policy/regime` into the risk-regime score; `GET /api/v1/liquidity/regime` confirms risk-off is transmitting into crypto books
- **Backtest** — `GET /api/v1/backtesting/klines` (BTC daily to 2017-08) plus `GET /api/v1/quant/regimes/history` (hourly HMM probabilities since 2020, Pro Plus) for regime-conditioned overlay tests; full point-in-time `/daily` payloads via `GET /api/v1/backtesting/daily-snapshots` only since 2026-03-02
- **Tips** — poll the cached `GET /api/v1/daily` bundle hourly (it packages macro, health, and derivatives in one call — the overlay's whole input set); enforce the hysteresis band agent-side by acting only when the regime score persists across ≥2 consecutive readings

## Related

- [[crypto-macro-correlation-regime]] — the Basket #6 regime this strategy operationalises
- [[macro-trend-regime]] — the risk-on/off backdrop
- [[bitcoin-cycle-regime]] — the cycle book the overlay defers to when crypto decouples
- [[dxy]] — the dollar gauge; core risk-on/off signal
- [[correlation]] — the master gate variable
- [[vix]], [[gold]] — macro fear and safe-haven corroboration
- [[regime-detection]], [[momentum-rotation]] — the regime-rotation strategy family
- [[macro-relative-value]], [[yen-carry-trade]] — adjacent macro-driven crypto trades
- [[tail-risk-hedging]] — the put-hedge implementation option
- [[funding-rate]] — crypto-internal risk-appetite confirmation
- [[bitcoin]], [[ethereum]] — the assets whose beta is dialed
- [[position-sizing]] — the target-beta risk-budget layer
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
