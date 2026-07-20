---
title: "Jurik Moving Average (JMA)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto]
aliases: ["JMA", "Jurik MA", "Jurik Research Moving Average"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[z-score]]", "[[hurst-exponent]]", "[[overfitting]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[john-ehlers]]", "[[microstructure-noise-low-timeframe]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[bid-ask-spread]]", "[[false-signals]]", "[[standard-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: advanced
---

# Jurik Moving Average (JMA)

The Jurik Moving Average is a commercial adaptive smoothing filter sold by Jurik Research (Mark Jurik), marketed on the claim that it delivers very low lag, high smoothness, and minimal overshoot simultaneously — the three properties conventional filters are forced to trade against each other. In [[stretch-revert]] it is the baseline behind `jma_stretch_revert`, valued for noise rejection.

> **The JMA algorithm is proprietary and has never been publicly disclosed.** It is licensed as a compiled library. Everything below describes *published behavioural claims and exposed parameters*, not the algorithm. The many "JMA" implementations circulating in TradingView, MQL4/MQL5, and Python communities are **reverse-engineered approximations, they are not the real algorithm, and they do not agree with one another**. This page presents no formula, because presenting one would be a fabrication.

Alongside the [[laguerre-filter|Laguerre Filter]] and [[supersmoother-filter|SuperSmoother]] it is grouped with the signal-processing baselines — but unlike those two, both of which [[john-ehlers|John Ehlers]] published in full, JMA cannot be inspected, verified, or independently derived.

## Construction

**No formula is given here, and none should be.** The construction is a trade secret. Any code presented anywhere as "the JMA formula" is either a licensee's illegal disclosure or, far more commonly, somebody's approximation fitted to match the vendor's plotted output.

What *is* documented is the parameter interface the commercial library exposes:

| Parameter | Range | Documented effect |
|---|---|---|
| `period` / `length` | integer, typically 7 - 50 | Nominal lookback. Longer = smoother, slower. Behaves broadly like a period, but is not equivalent to an EMA period. |
| `phase` | roughly −100 to +100 | Explicitly trades **overshoot against lag**. Negative phase is described as more conservative — less overshoot, more lag. Positive phase is more aggressive — faster response, permitting overshoot on sharp moves. 0 is neutral. |
| `power` / smoothing strength | small integer, commonly 1 - 4 | Strength of the smoothing stage. Higher = smoother output. |

That interface is informative in itself. A `phase` control that explicitly buys responsiveness by *allowing overshoot* tells you the filter has a lag-cancelling component — the same family of behaviour as [[zero-lag-exponential-moving-average|ZLEMA]] and [[triple-exponential-moving-average|TEMA]], which reduce lag by subtracting an estimate of it and pay for it with overshoot. And a `power` control alongside a `period` control implies at least two separable smoothing stages. Both are inferences from the interface, not statements about the algorithm.

## What is publicly known

Sorted by how much weight each item can bear:

**Vendor claims (marketing material, not independently verified):**
- Very low lag relative to conventional filters of the same smoothness.
- High smoothness — the output line is visually much quieter than an EMA of comparable responsiveness.
- Minimal overshoot at default settings, despite the low lag.
- Adaptive behaviour — the filter is described as responding to market conditions rather than applying a fixed kernel.

**Independently observable:**
- The exposed parameter set above, and its documented directional effects.
- The plotted output for a given input series and parameter set, from the licensed library. This is the only ground truth available, and it is only available to licensees.

**Not known, and not knowable without a licence:**
- The recursion, the state variables, the adaptation rule, the number of stages, or the frequency response.
- Whether the adaptation is volatility-driven (like [[vidya|VIDYA]]), efficiency-ratio-driven (like [[kama|KAMA]]), fractal-dimension-driven (like [[frama|FRAMA]]), or something else entirely.
- Whether the "minimal overshoot at low lag" claim holds across regimes, since no one outside the vendor can characterise the filter analytically.

There is no peer-reviewed evaluation of JMA that this vault has reviewed. The vendor's comparative charts are vendor-produced.

## Reproducibility problem

This is the section that matters most, and it is a research-integrity issue rather than a technical one.

**A strategy whose baseline is a closed-source black box cannot be fully reproduced, audited, or independently backtested.** For `jma_stretch_revert` that has concrete consequences:

1. **The signal cannot be verified.** In [[stretch-revert]] every member's entry is `price - baseline` normalised into a [[z-score]]. If the baseline cannot be recomputed by an independent party, neither can the z-score, the entry, or the exit. A third party cannot check the trade log against the stated rules.
2. **Backtest-vs-live divergence is undiagnosable in the usual way.** When results disagree, the standard procedure is to recompute the indicator on both bar sets and compare. With a licensed binary you can do this only inside the vendor's environment, on the platforms it supports, at the versions you hold. If two platforms' JMA outputs differ, there is no reference implementation to adjudicate.
3. **Community implementations are not substitutes and using one silently is a correctness bug.** TradingView Pine, MQL5, and Python "JMA" ports disagree with each other and with the commercial library. A backtest run on a Pine approximation and a live bot run on a different port are running **two different strategies with the same name**. This is not a subtle difference — the lag profile *is* the strategy in this family, per [[stretch-revert]]'s own framing.
4. **It weakens the family's core robustness argument.** [[stretch-revert]] runs fourteen baselines specifically so that a reversion premium can be shown to survive a change of smoother — defence in depth against estimator-specific artifacts. That argument requires each estimator be *known*, so that a member's result can be attributed to its lag characteristics. A black box contributes a data point you cannot interpret: if `jma` performs well and its neighbours do not, you cannot say why, and you cannot rule out that its adaptation is implicitly fitting something.
5. **The [[overfitting]] surface is hidden.** `period`, `phase`, and `power` are three tunable knobs on an unknown number of internal ones. You can count your own search over the exposed three; you cannot count whatever the vendor fitted when choosing the internal constants, and you cannot know whether those constants were tuned on markets and eras that overlap your test set. A model selected on data you cannot see is not a model you can deflate for.
6. **Vendor risk.** Licensing, platform support, and pricing are third-party dependencies on a component the strategy cannot run without. An open filter has none of these.

**The honest position for this vault:** JMA is included in [[stretch-revert]] as an installed member, its behavioural claims are plausible, and no claim on this page asserts it works or does not. If `jma_stretch_revert` ever produces a result that matters, the correct response is not to promote it but to **check whether an open filter reproduces it**. If [[laguerre-filter|Laguerre]], [[supersmoother-filter|SuperSmoother]], [[alma|ALMA]], or [[hull-moving-average|HMA]] deliver the same result, the black box is unnecessary. If none do, the result rests on something unverifiable and should be treated as unproven rather than as a discovery.

**If code is shown anywhere in this vault labelled JMA, it is a community approximation, not JMA.** No such code is included here, deliberately.

## Lag and smoothing trade-off

Positioned by *claimed* behaviour, with the uncertainty stated:

| Baseline | Lag | Smoothness | Overshoot | Verifiable |
|---|---|---|---|---|
| SMA(20) | high, fixed ~9.5 bars | moderate, sinc sidelobes leak | none | yes |
| EMA(20) | ~9-10 bars | moderate | none | yes |
| [[supersmoother-filter\|SuperSmoother]](20) | ≈ EMA(20) | high, clean rolloff | none | yes |
| [[laguerre-filter\|Laguerre]] γ=0.6 | below EMA of matched smoothness | high | none | yes |
| ZLEMA / TEMA | near zero | low | significant | yes |
| **JMA** | **claimed very low** | **claimed high** | **claimed minimal; `phase` explicitly trades it** | **no** |

JMA is marketed as occupying the corner of that table nothing else reaches — ZLEMA's speed with SuperSmoother's cleanliness. That is exactly the claim that cannot be independently checked, and it is a strong claim: every open filter in the table trades along that frontier rather than sitting off it. Treat the position as *asserted*, not measured.

The `phase` parameter is the tell that the trade-off has not been abolished, only exposed as a dial. A filter that had genuinely escaped the lag/overshoot frontier would not need a knob to move along it.

## Use as a mean-reversion baseline

In [[stretch-revert]] the baseline defines the mean; the residual defines the stretch. JMA's role in the family is noise rejection — a quiet baseline so that `price - JMA` reflects displacement rather than jitter.

**Does it flag stretch early or late? Nominally early, because the claim is low lag.** Practically, a low-lag baseline hugs price, which *compresses* residuals and makes large z-scores rarer — the high-precision, low-recall profile [[stretch-revert]] attributes to ZLEMA and TEMA. If JMA is as fast as claimed while staying smooth, its residual series should be small in magnitude but clean, meaning it fires infrequently and mostly on real displacement. **This is a prediction from the claims, not an observation** — and it is a testable one, which is the right way to relate to a black box.

`phase` is the parameter that decides this directly, and it is the one that requires the most care:

- **Negative phase** (conservative, more lag, less overshoot) → larger residuals, more entries, and behaviour closer to a conventional smoother. Better recall, more [[false-signals]].
- **Positive phase** (aggressive, faster, permits overshoot) → smaller residuals and fewer entries, but with a specific hazard: an overshooting baseline can *cross past* price after a sharp move, briefly flipping the sign of the residual and producing an entry in the wrong direction, or inflating the residual sigma so the z-threshold silently drifts. For a reversion baseline, overshoot is worse than lag.

**Regimes that flatter it:** noisy ranges where a smooth-and-fast baseline genuinely helps, and where its infrequent firing avoids the chop-driven entries that catch laggier members.

**Regimes that expose it:**

- **Trends** — the family-wide killer. No baseline solves walking the bands; the regime gate does.
- **Sharp V-reversals**, where any overshoot-permitting filter can produce a residual whose sign misrepresents the displacement for a bar or two.
- **Volatility regime shifts**, where you cannot reason about how the adaptation responds, because the adaptation rule is unpublished. With [[kama|KAMA]] you can at least inspect the efficiency ratio; with JMA there is nothing to inspect.
- **[[microstructure-noise-low-timeframe|Microstructure noise on thin books]]** — the family's most expensive failure mode, where measured "stretch" is really [[bid-ask-spread|bid-ask]] bounce. SuperSmoother has an *auditable* argument for handling this (a Nyquist null plus a two-pole rolloff). JMA has a *claim*. When the question is whether the edge is real or is the spread, an auditable argument is worth considerably more than a marketing claim.

## Parameters and tuning

| Parameter | Typical | Effect |
|---|---|---|
| `period` / `length` | 7 - 50 | Nominal smoothing horizon |
| `phase` | −100 to +100, default 0 | Overshoot vs lag; **keep at or below 0 for a reversion baseline** |
| `power` | 1 - 4 | Smoothing strength |
| `entry_z` | 2.0 - 3.0 | Stretch threshold on the residual |
| `z_window` | 50 - 200 bars | Window for residual sigma |

**Overfitting warning, and it is worse here than for the open filters.** Three exposed knobs is already a large grid: 10 periods × 5 phase settings × 3 power values is 150 configurations of a single member, inside a family already testing fourteen members on one history. The best cell of a 150-point grid will look excellent in-sample whether or not any edge exists — this is the textbook multiple-comparisons problem [[stretch-revert]] flags for the family as a whole, concentrated in one member. See [[overfitting]].

The aggravating factor unique to JMA: **you cannot account for the vendor's own model-selection.** Deflating a Sharpe ratio requires knowing how many configurations were tried. You know your 150. You do not know how many internal constants were fitted before the library shipped, or on what data. **The true search count is unknown and unknowable, so the deflated Sharpe cannot be computed correctly — only bounded from below.**

Discipline:

- Leave `phase` at 0 or negative. Do not sweep it looking for P/L; overshoot is a structural hazard for a reversion baseline, not a tunable preference.
- Sweep `period` only, coarsely, and require a plateau rather than a peak.
- **Cross-check against an open filter.** Before believing any JMA-baselined result, run the identical rules with [[supersmoother-filter|SuperSmoother]] and [[laguerre-filter|Laguerre]]. Agreement is evidence about reversion; disagreement means the result depends on a component nobody can audit.

## Advantages

- **Strong behavioural claims** on the one axis this family cares about most: smoothness at low lag.
- **An explicit `phase` control** exposing the lag/overshoot trade-off as a deliberate choice rather than an emergent property — genuinely useful when the trade-off is understood.
- **Widely adopted** across commercial platforms, so a JMA-baselined strategy is at least comparable with other practitioners running the licensed library.
- **Adaptive by design**, in principle handling regime changes that fixed-coefficient filters like Laguerre and SuperSmoother do not.
- Its infrequent firing profile (if the low-lag claim holds) suits a fade that wants precision over recall.

## Limitations

- **Proprietary and undisclosed.** The single most important fact on this page. The algorithm cannot be inspected, verified, derived, or reasoned about analytically.
- **Not independently reproducible.** No third party can recompute the signal, so no third party can audit the strategy — see [Reproducibility problem](#reproducibility-problem).
- **Community implementations are incompatible with each other and with the real thing.** Using one is running a different, unnamed indicator.
- **Claims are vendor claims.** No peer-reviewed or independent evaluation has been reviewed in this vault.
- **Undeflatable search space.** The vendor's own fitting is unknown, so the overfitting correction cannot be computed properly.
- **Vendor dependency** — licensing, versioning, and platform support are external risks on a critical component.
- **Overshoot risk at positive `phase`** is specifically dangerous for a reversion baseline, where a sign-flipped residual is a wrong-direction entry.
- **Does not solve trend risk** — like every member of the family, it dies in trends, and the regime gate is what protects it.
- **Weakens the family's robustness argument** by contributing an uninterpretable data point to a comparison whose whole purpose is interpretability.

## Getting the Data (CryptoDataAPI)

The API supplies the price series; the filter itself must come from the licensed library. Nothing here computes JMA.

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes fed to the licensed JMA library and to the open cross-check filters
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread check before entry; the black box gives no auditable guarantee that a small residual is not just the spread
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry drag on held reversions
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into the stretch argues trend, not dislocation

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive; the same bars must feed the JMA baseline and every open comparison baseline
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels for regime-stratified scoring
- `GET /api/v1/volatility/regime/{symbol}` — vol state, since JMA's adaptation rule is unpublished and can only be characterised empirically

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] should treat this member as a black box to be *characterised empirically*, since it cannot be reasoned about analytically:

- **Never substitute a community port.** If the licensed library is unavailable, the correct action is to disable `jma_stretch_revert` and say so — not to swap in a TradingView or MQL approximation. A silent substitution changes the strategy while keeping the name.
- **Behavioural fingerprint** — over one `GET /api/v1/backtesting/klines` pull, measure the JMA output's realised lag (cross-correlation against price) and residual variance, and compare against [[supersmoother-filter|SuperSmoother]] and [[laguerre-filter|Laguerre]] on identical bars. This is the only way to test the "low lag *and* high smoothness" claim, and it produces a number rather than a marketing adjective.
- **Overshoot audit** — flag every bar where `sign(price - JMA)` flips within one bar of a large move. Non-trivial flip rates at `phase = 0` mean overshoot is present at the default setting, which would contradict the vendor claim and matters directly for a reversion baseline.
- **Open-filter cross-check before any promotion** — replay the identical [[stretch-revert]] rules with JMA and with two open baselines. Promote only what survives the substitution; a result that lives only under the black box is unverified, not validated.
- **Regime gate** — `GET /api/v1/quant/market`; the adaptation rule is unpublished, so it earns no benefit of the doubt in trending states and the gate must stand the member down like any other.
- **Record the version** — log the JMA library version and parameter triple with every signal. Without a reference implementation, version metadata is the only thing making a past result re-checkable at all.

## Related

[[stretch-revert]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[john-ehlers]] · [[moving-averages]] · [[adaptive-moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] · [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] · [[mean-reversion]] · [[bollinger-bands]] · [[z-score]] · [[standard-deviation]] · [[hurst-exponent]] · [[microstructure-noise-low-timeframe]] · [[bid-ask-spread]] · [[false-signals]] · [[overfitting]] · [[cryptodataapi-hyperliquid]] · [[cryptodataapi-mcp]]

## Sources

- Jurik Research (Mark Jurik) — vendor documentation for the commercial JMA library: the parameter interface (`period`, `phase`, `power`) and the low-lag / high-smoothness / minimal-overshoot behavioural claims. The algorithm itself is undisclosed; these are the vendor's own claims and are not independently verified.
- Open-filter comparisons on this page reference [[john-ehlers|Ehlers]]' published designs — "Time Warp – Without Space Travel" (2004) and *Cycle Analytics for Traders* (2013) — because those are inspectable and JMA is not. See [[laguerre-filter]] and [[supersmoother-filter]].
- Strategy framing, regime dependence, and failure modes are drawn from vault pages: [[stretch-revert]], [[mean-reversion]], [[moving-averages]], [[microstructure-noise-low-timeframe]], [[overfitting]].

**No independent or peer-reviewed evaluation of JMA has been reviewed in this vault, and no reproducible reference implementation exists.** No source-summary page exists for the Jurik Research material.
