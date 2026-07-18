---
title: "Funding-Conditioned Vol Selling"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, volatility, funding-rate, derivatives, perpetual-futures, quantitative, crypto, behavioral-finance]
aliases: ["Funding-Gated Vol Selling", "Crowding-Confirmed Short Vol", "Leverage-Proxy Vol Entry"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Elevated perp funding flags a crowd of leveraged retail longs whose demand for lottery-ticket calls and panic puts simultaneously inflates implied vol and skew above fair value; by entering short-vol only when funding is elevated AND IV exceeds realised vol by a threshold, the strategy sells options when the crowding-driven IV premium is confirmed at its richest and avoids the DVOL-percentile regime where vol is expensive for structural reasons unrelated to leverage."

data_required: [funding-rates, options-chain, dvol-history, realized-vol-calc, ohlcv-daily, open-interest]
min_capital_usd: 25000
capacity_usd: 200000000
crowding_risk: medium

expected_sharpe: 1.0
expected_max_drawdown: 0.35
breakeven_cost_bps: 60

decay_evidence: "DVOL-gated vol selling has compressed as covered-call ETFs and on-chain vaults (Ribbon/Aevo, Deribit auction flow) industrialised systematic call-writing (see crypto-options-volatility-selling). The funding conditioning layer targets the *subset* of the VRP that is leverage-crowd driven — a narrower, less-crowded niche that may decay more slowly than the raw DVOL-percentile filter, but which also produces fewer entry signals."

kill_criteria: |
  - DVOL rises > 50% in a single session (vol-shock circuit breaker; same as the underlying vol-selling primitive)
  - sleeve drawdown > 30% from high-water mark
  - realized vol exceeds DVOL for 20+ consecutive days (structural VRP inversion)
  - funding AND DVOL-percentile signals both qualify but vol selling P&L is negative on 15+ consecutive signal entries (crowding has absorbed the combined-signal alpha)
  - signal frequency < 1 entry per 60 days for 6 months (both conditions rarely coincide — reconsider the threshold calibration)

related: ["[[crypto-options-volatility-selling]]", "[[skew-trading]]", "[[options-premium-selling]]", "[[funding-filtered-momentum]]", "[[funding-flush-reversal]]", "[[crowded-long-funding-fade]]", "[[deribit]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[dvol]]", "[[variance-risk-premium]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Funding-Conditioned Vol Selling

Funding-conditioned vol selling is [[crypto-options-volatility-selling]] — the systematic sale of BTC/ETH options on [[deribit]] — where entry requires **two simultaneous signals**: the perp funding rate is elevated (≥ 0.03%/8h), confirming that a crowd of leveraged retail longs is driving the implied-vol richness, **and** DVOL exceeds trailing 30-day realized volatility by a minimum threshold. Funding is used as a **crowding proxy** that identifies when the structural source of IV-premium richness (leveraged retail demand for call exposure and put protection) is actively present, not just when DVOL happens to be percentile-elevated for other reasons.

This is differentiated from [[crypto-options-volatility-selling]] — that page's canonical entry gate is a DVOL-percentile filter (40th–90th percentile of trailing year). This page uses **funding rate as the conditioning signal** and explains why funding adds information *beyond* the DVOL percentile: DVOL can be in the 60th percentile because the market is nervously range-bound with genuine macro uncertainty (non-crowding), or because a crowd of leveraged longs is bidding calls while perp holders are paying 0.05%/8h funding. These two regimes have the same DVOL level but different VRP textures — the second has a *leverage-crowd premium* that is predictably mean-reverting because the crowd's funding cost is bounded and their crowding eventually triggers a flush. Funding identifies which regime is driving the vol elevation, enabling a more selective subset of entries with higher expected VRP per signal.

This is differentiated from [[crowded-long-funding-fade]] — that page trades the *price* of the perp itself (fading momentum when funding is stretched). This page trades the *options surface*, using funding as a signal to enter short vol, not to fade the underlying.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing** — the same triple that drives [[crypto-options-volatility-selling]], with a tighter behavioral identification:

- **Behavioral (primary)** — elevated perp funding is the market's direct revealed preference: leveraged retail longs are paying their counterparts ~0.03-0.10%/8h (33-110% APY) to hold leveraged long perp positions. This same behavioural impulse — overconfidence, leverage preference, lottery-ticket demand — also *inflates* the options surface: the same crowd buys OTM calls as leveraged lottery tickets and buys puts post-dip as emotional insurance. When funding is high, the options surface inherits the crowd's behavioural premium on top of the base VRP. Funding-conditioned entry captures the *intersection* of the crowding signal and the IV-RV gap.
- **Structural** — the perp mechanism creates a structural carry payment that bounds the crowd's willingness to hold leveraged longs. At 0.05%/8h, the crowd pays ~55% APY to be long perp. This carry cost eventually forces crowded longs to reduce exposure, creating the cascade / flush / mean-reversion event that is also the vol-selling book's best outcome: mean-reversion of the crowding premium.
- **Risk-bearing** — the seller still underwrites the crypto tail (2020-03, LUNA, FTX, 2025-10-10). The funding signal does not reduce tail exposure — it improves *selection* of when to absorb that tail risk relative to compensation received.

## Why this edge exists

**Funding adds information beyond DVOL percentile** through three mechanisms:

1. **Regime identification within the DVOL distribution.** DVOL at the 65th percentile can correspond to two distinct regimes: (A) perp funding neutral/negative, market under genuine macro uncertainty, options surface reflecting hedging demand — lower expected VRP, harder entry; (B) perp funding elevated, leveraged longs crowded, call skew bid by the same crowd — higher expected VRP, the crowding premium is an identifiable, mean-reverting component. The DVOL percentile is the same in both; funding discriminates between them.

2. **Call skew richness is mechanically linked to funding.** The [[crypto-options-volatility-selling]] page documents this explicitly: "when funding is richly positive and call skew is bid, weight the short toward the call wing." High perp funding → crowded longs → bid for call convexity → 25-delta call RR elevated above the structural skew level. This gives a mechanistic reason to prefer call-wing entry when funding is elevated: the crowding premium has a clear source (leveraged long demand) and a clear resolution mechanism (the crowd exits or is flushed).

3. **Funding predicts the crowding unwind, not just the crowding.** The key insight: elevated funding does not just tell you *that* the crowd is in — it tells you the crowd is *paying an unsustainable rate to stay in*. At 0.05%/8h, a leveraged long holding a $50K perp position pays ~$200/day in funding. This creates a natural reversal pressure: crowded vol richness has a timer on it that DVOL percentile alone does not capture.

**Who is on the other side:** the leveraged retail participant who is simultaneously bidding options premiums (call wings and puts) as expressions of their leveraged bullish conviction, while paying funding on their perp exposure. The vol seller captures both the options surface richness that the crowd created and the mean-reversion of the crowding premium as they eventually exit.

## Null hypothesis

Under the null, perp funding carries no information about forward options P&L *conditional on DVOL percentile*. Specifically:
- The average P&L of delta-hedged short strangles entered when both funding ≥ 0.03%/8h AND IV−RV > 5 vol points should not exceed the P&L of entries made when only the DVOL-percentile gate fires.
- The IV−RV premium on entries meeting the funding condition should not decay faster than entries without the funding condition in the subsequent 10-35 DTE window.
- Call-wing skew should not mean-revert faster after funding-conditioned entries than after DVOL-only entries.

Currently not rejected (`backtest_status: untested`). Testable prediction: partition all historical DVOL-gate signal periods by concurrent perp funding level (quartile); compute average subsequent 30-day IV−RV path and short-strangle P&L per quartile. Prediction: highest funding quartile should show the largest positive IV−RV spread at entry AND the fastest mean-reversion — i.e., the premium is richest and most reliably mean-reverting when the crowd is most crowded.

## Rules

### Entry conditions

All three must be simultaneously satisfied:

1. **Perp funding gate:** 8h funding on BTC (or the target underlying) ≥ **0.03%/8h** (~33% APY). This confirms an actively crowded leveraged-long position in the perp market. The threshold is one standard-deviation-above-average for Hyperliquid/Binance BTC in normal bull regimes — elevated but not at extreme-spike levels where the crowd is about to be flushed immediately.
2. **DVOL-percentile gate (same as [[crypto-options-volatility-selling]]):** DVOL between the **40th and 90th percentile** of the trailing 1-year distribution. Below 40th: premium too thin regardless of funding. Above 90th: likely entering into an active vol shock — sit out or wait for the spike to roll.
3. **VRP confirmation:** DVOL − 30-day realized vol ≥ **5 vol points**. The IV−RV spread must be open above the noise floor regardless of funding; funding identifies *why* it is open, not whether it is open.

**Skew application (funding-specific adjustment):** when funding ≥ 0.05%/8h, the call skew is disproportionately bid by the leveraged long crowd. In this sub-regime, tilt the structure to **overweight the call wing**: sell a call spread or a call-heavy strangle, since the call-side richness is the direct expression of the crowd's leverage demand. Standard DVOL-gated entries without the funding signal should not assume this directional skew.

### Structure, sizing, and delta hedging

Follow the same framework as [[crypto-options-volatility-selling]]:
- **Structure:** iron condor (preferred for defined-risk) or short strangle at 15-25 delta on BTC/ETH Deribit options, 21-45 DTE.
- **Sizing:** short vega ≤ 1% of NAV per 1 vol point of DVOL.
- **Delta hedge:** band + schedule (±0.5% NAV-equiv delta); switch to continuous on DVOL +25% intraday.
- **Exit:** 50% of max credit, or 10-14 DTE time stop, or vol-shock kill.

### Kill conditions (shared with underlying vol-selling primitive)

- DVOL +50% in a single session → flatten all short vega.
- Position delta > 2× entry delta.
- Sleeve drawdown > 30%.

The additional funding-specific kill: if funding drops below 0.01%/8h during the trade hold (the crowding premise has dissolved), evaluate whether to close early — the rationale for the call-skew tilt has expired.

## Implementation pseudocode

```python
# funding_conditioned_vol_selling.py
# Extends crypto-options-volatility-selling entry logic with a funding gate

# ---- entry thresholds (new, funding-specific) ----
MIN_FUNDING_8H          = 0.0003    # 0.03%/8h: crowding gate
CALL_WING_FUNDING       = 0.0005    # 0.05%/8h: tilt to call-overweight
FUNDING_EXIT_THRESHOLD  = 0.0001    # below 0.01%/8h mid-hold: consider early exit

# ---- thresholds shared with underlying vol-selling primitive ----
MIN_DVOL_PCTL           = 0.40
MAX_DVOL_PCTL           = 0.90
MIN_VRP_POINTS          = 5.0
TARGET_DTE              = 35
SHORT_DELTA             = 0.20
VEGA_PER_VOLPT          = 0.01
DVOL_SHOCK_KILL         = 0.50
TIME_STOP_DTE           = 12
PROFIT_TARGET           = 0.50

def funding_gate_passes(funding_8h: float) -> bool:
    return funding_8h >= MIN_FUNDING_8H

def call_wing_tilt(funding_8h: float) -> str:
    """Returns skew tilt direction for structure selection."""
    if funding_8h >= CALL_WING_FUNDING:
        return "call_overweight"    # leveraged longs are overbidding calls
    return "balanced"

def try_open_funding_conditioned(book, mkt):
    # standard DVOL + VRP gates (same as crypto-options-volatility-selling)
    if not (MIN_DVOL_PCTL <= mkt.dvol_pctl <= MAX_DVOL_PCTL):
        return None  # DVOL out of range
    if (mkt.dvol - mkt.rv30) < MIN_VRP_POINTS:
        return None  # VRP too thin
    if book.short_vega_per_volpt() >= VEGA_PER_VOLPT * book.nav:
        return None  # vega budget exhausted

    # ADDITIONAL GATE: funding must be elevated (crowding confirmed)
    if not funding_gate_passes(mkt.funding_8h):
        return None  # DVOL gate fires but funding is flat → skip this signal

    exp = select_expiry(mkt.chain, TARGET_DTE)
    call_k = strike_at_delta(exp, +SHORT_DELTA)
    put_k  = strike_at_delta(exp, -SHORT_DELTA)
    tilt   = call_wing_tilt(mkt.funding_8h)

    # iron condor with funding-adjusted skew tilt
    return sell_iron_condor(exp, call_k, put_k, protect_delta=0.10,
                            skew_tilt=tilt,
                            size=vega_sized(book, exp),
                            entry_note=f"funding={mkt.funding_8h*100:.3f}%/8h, "
                                       f"dvol_pctl={mkt.dvol_pctl:.2f}, "
                                       f"vrp={mkt.dvol - mkt.rv30:.1f}vol_pts")

def check_mid_hold_exit(pos, mkt):
    """Early exit if the funding crowding premise dissolves."""
    if pos.entry_note.startswith("funding=") and mkt.funding_8h < FUNDING_EXIT_THRESHOLD:
        # crowding has cleared — the rationale for the call-skew tilt is gone
        # consider closing early if the position is still profitable
        if pos.pnl >= 0.25 * pos.max_credit:
            return {"action": "CLOSE_EARLY",
                    "reason": "funding crowding premise dissolved; locking partial profit"}
    return None
```

The production system adds: DVOL and realized-vol computation from Deribit / [[greeks-live]]; perp funding polling from CryptoDataAPI; the full delta-hedging cadence from the underlying primitive; and a per-entry attribution separating the "funding premium" component from the baseline VRP.

## Indicators / data used

- **[[funding-rate]] (8h)** — the primary conditioning signal; must be ≥ 0.03%/8h at entry.
- **[[dvol]] (BTC/ETH DVOL index)** — the standard DVOL-percentile gate from Deribit / [[greeks-live]].
- **[[realized-volatility]] (30-day)** — computed from BTC/ETH klines; the IV−RV spread denominator.
- **25-delta [[risk-reversal]] and call skew** — confirms the call-wing richness expected from elevated funding.
- **[[open-interest]] per strike** — dealer-positioning context; OI walls inform strike selection.
- **[[gamma-exposure|GEX]]** — dealer-gamma context for entry timing (avoid selling into a short-gamma cascade environment).

Note: DVOL and the options surface come from Deribit and [[greeks-live]]. CryptoDataAPI provides the funding signal and complementary options-OI / vol-regime context (see Getting the Data below).

## Example trade

**Setup (illustrative):**

- Asset: BTC. ETH-based example omitted for brevity; applies symmetrically.
- BTC spot: $98,000. BTC DVOL: 62 (67th percentile of trailing year). 30-day RV: 44. VRP = **18 vol points** — gate 3 passes.
- Perp funding (8h): **+0.048%/8h** (~52.6% APY) — gate 1 passes. This is Hyperliquid BTC-PERP, confirming a crowd of leveraged longs paying heavy funding.
- DVOL percentile: 67% — gate 2 passes (40th-90th).
- Skew tilt: funding 0.048% ≥ 0.05% threshold? No (just below) — use balanced structure (or call-tilt at operator discretion).

**Trade:** sell 35-DTE iron condor, BTC, USDC-margined (Deribit):
- Short 20-delta call @ $108,000 / long 10-delta call @ $115,000 (protective wing).
- Short 20-delta put @ $88,000 / long 10-delta put @ $82,000 (protective wing).
- Net credit ≈ $1,400 per 1-BTC condor; max loss capped at ~$5,600 by long wings.
- Size: 1%-NAV-per-vol-point vega (if NAV = $200K, short vega ≤ $200K × 0.01 × 62 = assume ~$120K vega notional; position sized accordingly).

**Path A (base case, ~65%):** Over 3 weeks, BTC oscillates $94,000–$103,000. DVOL decays to 52 as the leveraged longs gradually reduce exposure (funding drops back to 0.01%/8h by week 2). The condor decays to ~$600 at 15 DTE. Close at 50% profit: **+$700 per condor**. The funding-regime entry coincided with faster-than-average DVOL mean-reversion: the crowding premium unwound as expected.

**Path B (moderate stress, ~25%):** BTC drops 8% to $90,200 over 5 days. DVOL spikes from 62 to 84 (+35% — below the 50% kill). Put wing marks against; delta hedge kicks in. Position marks −$800. Funding flushes to 0.005%/8h (crowding cleared in the dump). Mid-hold exit logic triggers: partial profit lock if applicable, or hold to 12 DTE time stop. Exits at −$200 net (protective wing capped the loss).

**Path C (shock, ~10%):** BTC gaps −20%. DVOL 62 → 130 (+110%). Vol-shock kill triggers at session open. Defined-risk condor: max loss ~$5,600/BTC. Delta hedge offsets part of spot move.

**Differentiation observable in example:** in Path A, the accelerated DVOL mean-reversion (from 62 to 52 in 3 weeks) is consistent with the crowding-premium unwinding as leveraged longs reduce exposure. In a non-funding-conditioned entry at the same DVOL percentile, the DVOL path might have been flatter — the premium taking longer to decay, increasing the risk of a time-stop exit at lower profit.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Base vol-selling Sharpe ~0.9 (same gate structure); funding conditioning adds selectivity estimated at +0.1 Sharpe by filtering to faster-decaying premium regimes |
| Expected max drawdown | ~35% | Same tail structure as underlying vol-selling; defined-risk condor caps per-position loss |
| Signal frequency | Reduced vs pure DVOL gate | Both conditions must fire simultaneously; estimated 40-60% fewer entries vs DVOL-only gate in typical years |
| IV−RV spread at entry | Expected higher than DVOL-only average | Prediction: funding-coincident entries have higher IV−RV spreads by 2-5 vol points |
| DVOL mean-reversion speed | Expected faster | Crowding-premium component mean-reverts faster than generic IV elevation |
| Breakeven cost budget | 60 bps | Same as underlying; Deribit options costs unchanged |

**What the funding filter buys (qualitative):** it filters out the DVOL-percentile-gate entries where vol is elevated for macro-uncertainty reasons (not crowding), where mean-reversion may be slower and less reliable. The cost is signal frequency; the benefit is quality of the entries that pass.

## Capacity limits

- **Deribit market depth:** same as [[crypto-options-volatility-selling]] — individual desk ceiling ~$50-300M notional. The funding-conditioned strategy has *fewer* entries, so it actually uses less of the available liquidity — potentially better execution quality per position.
- **Crowding of the filter:** if the funding conditioning becomes a widely adopted entry filter, sophisticated desks and systematic programs will simultaneously seek to enter short vol when funding is elevated, crowding the entry. This narrows bid-ask at entry time and compresses the premium. The strategy's edge degrades when the funding-conditioned vol-entry is too widely known.

## What kills this strategy

1. **All the same failure modes as [[crypto-options-volatility-selling]] (#6, #7):** vol-shock, single-venue Deribit dependency, coin-margined settlement wrong-way risk, margin spiral.
2. **Crowding of the combined signal (#4):** the DVOL-percentile gate is already widely watched. Adding the funding gate creates a secondary filter, but if desks widely adopt the rule "sell vol when funding AND DVOL both signal," simultaneous entry narrows the spread and reduces the premium available at the point of entry.
3. **Decorrelation of funding and vol premium (#5):** the strategy's thesis requires that funding *actually causes* or *reliably coincides with* vol surface richness. If the perp market and the options market decouple (e.g., large options dealers hedge on spot rather than perp, breaking the perp-options surface link), the funding signal loses its predictive value for the options entry.
4. **Funding compression (#5):** if perp funding compresses permanently toward zero (Ethena/Resolv saturation), the funding gate fires rarely, and the strategy has very few entries — it may become practically inactive.
5. **Inverse relationship in bear markets:** in risk-off regimes, funding can be negative (shorts crowded, not longs) while DVOL is elevated (crash-driven). The funding gate blocks entries in this regime — which is correct (funding signals a *different* type of crowding), but the operator must understand that the strategy will not trade during deep bear volatility spikes.

## Kill criteria

Pause on any of:

1. **DVOL +50% in a single session** → flatten all positions immediately (vol-shock circuit breaker).
2. **Sleeve drawdown > 30%** from high-water mark.
3. **Realized vol > DVOL for 20+ consecutive days** — structural VRP inversion; no premium to sell.
4. **Combined-signal entries generate negative P&L on 15+ consecutive signals** — both conditions fire but the entry no longer works; crowding has absorbed the signal.
5. **Signal frequency < 1 entry per 60 days for 6 consecutive months** — the two conditions rarely coincide in the current regime; recalibrate funding threshold.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Improves signal quality over pure DVOL gate:** filters to the subset of vol-selling opportunities where a specific, identifiable mechanism (leveraged retail crowding) is driving the IV elevation — a more interpretable and testable edge than raw percentile filtering.
- **Provides a call-skew entry logic:** the funding signal gives a mechanistic reason to tilt the condor toward the call wing when funding is high, rather than treating the skew as a black box.
- **Naturally self-limiting signal frequency:** the double gate reduces position count, keeping vega utilisation lower and margin headroom higher — operationally beneficial for a defined-risk book.
- **Shareable data rail with perp-funding strategies:** the same funding endpoint feeds [[funding-filtered-momentum]], [[funding-flush-reversal]], and [[funding-skewed-grid]] — the data infrastructure is not incremental.
- **Interpretable kill conditions:** if the crowding premise dissolves mid-hold (funding drops), the mid-hold exit rule provides a principled way to reduce exposure rather than relying entirely on the standard time/profit stops.

## Disadvantages

- **Fewer entries:** the double gate reduces signal frequency by an estimated 40-60%. In years where vol-selling would have been consistently profitable, this strategy sits out more frequently.
- **Deribit and DVOL data dependency:** the options surface and DVOL index come from Deribit; CryptoDataAPI does not document a specific DVOL timeseries endpoint — the DVOL feed must be sourced from Deribit's own API or [[greeks-live]]. This requires maintaining separate data subscriptions.
- **Tail risk unchanged:** the funding gate does not reduce exposure to black-Thursday-style shocks. The call-skew tilt in high-funding regimes can actually increase *put* exposure — in a crash, the crowded long-perp regime triggers a rapid deleveraging, exactly the scenario the put wing gets tested by.
- **Threshold sensitivity:** the 0.03%/8h funding gate is a calibrated design choice, not a statistically validated threshold. Different thresholds shift the trade-off between frequency and quality; overfitting the threshold to historical data is a real risk.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (BIS, 2023). Documents the structural link between perp funding and leveraged retail demand; the crowding mechanism this strategy uses as its conditioning signal. https://www.bis.org/publ/work1087.pdf
- [[crypto-options-volatility-selling]] — the underlying vol-selling primitive; all structural framing, sizing, and kill logic from that page is inherited by this strategy.
- Deribit Insights research on DVOL and the crypto variance risk premium — BTC IV−RV spreads structurally wider than SPX; the funding/skew linkage is documented in the strategy's "why it exists" section of the underlying primitive.

## Getting the Data (CryptoDataAPI)

**DVOL and the options surface** come from [[deribit]] and [[greeks-live]]. CryptoDataAPI provides the funding signal and complementary options-flow, vol-regime, and GEX context:

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding rate; the primary conditioning gate
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and max-pain strike
- `GET /api/v1/volatility/regime` — vol regime classification (compressed / expanding / vol_shock) for kill-trigger monitoring
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure for dealer-gamma context at entry
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for conditioning-gate backtest
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for multi-regime RV backtesting

Note: DVOL itself (Deribit's implied-vol index) and the live options surface must be sourced from Deribit's API or [[greeks-live]]; CryptoDataAPI does not currently document a DVOL timeseries endpoint. The options-OI and max-pain endpoint (`/market-intelligence/options`) covers dealer positioning context.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]].

## Related

- [[crypto-options-volatility-selling]] — the underlying vol-selling primitive; this page adds the funding conditioning layer on top
- [[skew-trading]] — using the options skew structure to extract relative-value premium; complements the call-tilt rule here
- [[options-premium-selling]] — the broader options income strategy family
- [[dvol]] — the Deribit Volatility Index used in the DVOL-percentile gate
- [[variance-risk-premium]] — the premium being harvested
- [[deribit]] — the venue; DVOL and surface source
- [[greeks-live]] — the analytics/RFQ workbench
- [[funding-filtered-momentum]] — funding as a filter on momentum entries; shares the funding data rail
- [[funding-flush-reversal]] — funding-confirmed dip-buy; a different expression of funding-as-crowding-signal
- [[crowded-long-funding-fade]] — fades perp price momentum when funding is stretched; same crowding premise applied to the perp itself
- [[implied-volatility]], [[realized-volatility]] — the vol inputs
- [[funding-rate]] — the contract mechanism providing the conditioning signal
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — vol shock, crowding, premise decorrelation risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
