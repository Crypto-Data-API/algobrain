---
title: "Volatility Term Structure"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [volatility, indicators, options, term-structure, vix]
aliases: ["IV Term Structure", "Vol Curve", "Volatility Curve"]
related: ["[[volatility-regime]]", "[[volatility-regime-classification]]", "[[volatility-regime-switching]]", "[[volatility-risk-premium-decay]]", "[[implied-volatility]]", "[[vix]]", "[[vix-futures]]", "[[contango]]", "[[backwardation]]", "[[variance-risk-premium]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[long-vol-vs-short-vol]]", "[[volmageddon]]", "[[covid-crash]]", "[[vix-august-2024-spike]]"]
domain: [volatility, indicators, options]
prerequisites: ["[[implied-volatility]]", "[[vix]]"]
difficulty: intermediate
---

The **volatility term structure** is the curve formed by [[implied-volatility|implied volatilities]] (or VIX-style variance indices) plotted against time-to-expiration. Its shape — typically upward-sloping ("contango") in calm markets and inverted ("backwardation") in stressed markets — is one of the most reliable real-time indicators of [[volatility-regime|vol regime]] and the carry available to short-vol vs long-vol positions. Term structure is what makes [[vix-futures|VIX futures]] a non-trivial product: the futures roll, not the spot level, drives most of the long-run P&L of vol ETPs and explains why naive long-VIX exposure decays.

## Overview

For a single underlying, implied volatility is a *surface* indexed by both expiration and strike. Holding strike fixed (typically at-the-money or at the [[forward-price|forward]]) and varying expiration produces the **ATM term structure** — the IV curve as a function of DTE.

For the broad equity market, the [[cboe|CBOE]] publishes a family of constant-maturity variance indices that pin down the term structure at canonical horizons:

- **VIX1D** — 1-day expected variance of SPX (introduced 2023, capturing 0DTE flow).
- **VIX9D** — 9-day expected variance.
- **VIX** — 30-day expected variance (the canonical index).
- **VIX3M** — 3-month (~63 trading-day) expected variance.
- **VIX6M** — 6-month expected variance.
- **VIX1Y** — 1-year expected variance.

Each is computed from a strip of out-of-the-money SPX options spanning the relevant maturity, using the variance-swap fair-strike formula codified by Demeterfi-Derman-Kamal-Zou (1999). [[whaley-2000|Whaley (2000)]] is the canonical reference for the original VIX construction; the 2003 methodology revision moved from the original Black-Scholes-implied calculation to the variance-swap formula used today.

Plotting these together at a single point in time gives the term structure curve. ~80% of trading days, the curve slopes upward — VIX < VIX3M < VIX6M. The remaining ~20% of days exhibit kinks, flatness, or inversion.

## Definition / Formal Description

### Constant-maturity vs raw-month indices

The VIX-family indices are **constant-maturity** — they are interpolations across two adjacent expiration cycles to pin a fixed forward window (e.g., always exactly 30 days for VIX). This contrasts with **raw-month** [[vix-futures|VIX futures]] (VX1, VX2, …, VX9), which expire on specific dates and whose effective maturity *decays* day by day as expiration approaches.

The constant-maturity construction matters for two reasons:

1. **VIX itself is non-tradable.** You cannot trade spot VIX — only futures, options, and ETPs. The futures and ETPs replicate exposure that *converges* to spot VIX at their own expiration but rolls along the term structure in between.
2. **Term-structure ratios use constant-maturity indices for stability.** VIX/VIX3M is a clean ratio because both legs are pinned to fixed forward horizons; it doesn't drift mechanically as time passes.

### Contango and backwardation

| Shape | Definition | Frequency | Regime signal |
|-------|-----------|-----------|---------------|
| Steep contango | VIX/VIX3M < 0.85 | ~25% | Calm |
| Mild contango | 0.85–0.95 | ~50% | Normal |
| Flat | 0.95–1.00 | ~15% | Elevated/transitioning |
| Backwardation | > 1.00 | ~10% | Stressed |
| Deep backwardation | > 1.20 | ~2% | Crisis |

(Approximate frequencies for VIX/VIX3M since the latter's introduction in 2008.)

The structural reason contango dominates: the variance risk premium is positive on average, so long-dated implieds are bid up by the market's willingness to pay for uncertainty insurance; near-dated implieds reflect more recent realized vol, which is typically lower than the implied long-run mean. See [[variance-risk-premium]] and [[volatility-risk-premium-decay]].

### Roll yield mechanics

For a [[vix-futures|VIX futures]] holder, the contract converges to spot VIX at its expiration. If spot VIX stays constant and the curve is in contango, a futures position that began trading above spot must *fall* toward spot — the long pays roll yield, the short collects it. Roughly:

```
Daily roll yield (long) ≈ -(F_t - F_{t-1})  if curve is stable
                       ≈ -(F - S) / DTE     in steady state
```

A 5% steady-state contango on the VX1/spot pair gives a long-VIX1 holder a roll cost of roughly 0.17%/day, or ~5%/month. Compounded over a calendar year, a holder of front-month long VIX exposure gives back ~50–60% in roll yield in average years, ~80%+ in calm years. This is why long-VXX/UVIX/VIXY ETPs lose 80–95% of their value over multi-year periods absent a vol shock — the ETP rolls the curve every day.

The mirror image: short-vol ETPs (XIV, SVXY pre-2018) collected this roll yield as profit. The same mechanic that printed money for XIV from 2012–2018 vaporized it in 12 hours during the [[volmageddon|February 5, 2018 spike]] when the curve flipped to backwardation and the daily-rebalanced short position had to *cover* into the spike.

## Empirical Evidence / Examples

### How the curve shifts during shocks

The signature of a vol shock is a **front-loaded shift**: short-dated IV rises far more than long-dated IV, kinking and then inverting the curve.

- **Day 0 (calm)** — VIX 13, VIX3M 16, VIX6M 18. Steep contango. Ratio VIX/VIX3M ≈ 0.81.
- **Day 1 (shock)** — VIX 28, VIX3M 22, VIX6M 21. Sharp kink; front month massively repriced. Ratio 1.27 (deep backwardation).
- **Day 5 (post-peak)** — VIX 24, VIX3M 23, VIX6M 22. Backwardation flattening as front-month vol mean-reverts toward back month.
- **Day 20 (mean-reverted)** — VIX 18, VIX3M 19, VIX6M 19. Back to mild contango. The shock is fully priced into history; back-month vol barely moved.

This is why the **VIX/VIX3M ratio crossing 1.00** is one of the most reliable single-shot regime-change signals — see [[volatility-regime-classification]]. A steepening of front-month vol *without* corresponding back-month movement is exactly what regime-shifting vol-of-vol shocks look like.

### Specific historical episodes

- **[[volmageddon|Feb 5, 2018]].** VIX moved from 17 to 37 in a single session. VIX/VIX3M jumped from ~0.85 to ~1.40 — among the deepest backwardations ever recorded outside true crises. Term structure inverted for ~6 sessions before returning to contango.
- **[[covid-crash|March 2020]].** VIX peaked at 82.69 (March 16). VIX/VIX3M held above 1.10 for roughly 8 weeks — the longest sustained backwardation since the 2008 GFC. Long-vol ETPs that had bled for years finally paid off, multiplying ~5–10x in 4 weeks.
- **[[vix-august-2024-spike|August 5, 2024]].** Intraday VIX > 65, a single-day move comparable to Volmageddon and COVID. But the curve inverted and re-normalized within 4–5 sessions; back-month implieds barely moved. The shock was a JPY-carry-unwind compounded with a weak NFP, not a sustained regime change. Sub-stripe behavior: VIX1D, in its first major crisis test since launch, hit ~80 on the open, demonstrating the front-end's sensitivity to event-day flow.

### Single-name term structures

For single equities, the term structure has a characteristic *event hump* on the chart: the cycle that spans a known catalyst (earnings, FOMC, FDA decision) prices in a higher IV than the cycles immediately bracketing it. This is the operational reason for earnings IV crush — the post-event IV collapses back to the regime-appropriate level, often 30–60% lower than pre-event.

## Implications for Strategy

1. **Term structure is the fastest regime indicator available.** Daily ratio of VIX/VIX3M updates intraday; HMM-based regime classifiers update over weeks. See [[volatility-regime-switching]].
2. **Carry direction depends on curve shape.** In contango, *short-vol carries* (you collect roll yield) and *long-vol bleeds*. In backwardation, the reverse — long-vol *can* carry positively as the curve flattens.
3. **Calendar spreads are term-structure trades.** Selling a near-dated option and buying a longer-dated option of the same strike is a long-vega bet on the *back-month* IV staying high relative to the *front-month* IV. The curve shape at entry determines the payoff.
4. **Short-vol products require term-structure awareness.** A vol seller who ignores the curve and sells the same DTE in all regimes is structurally trading the curve shape's mean-reversion as well as the variance risk premium — and the curve mean-reverts violently against short-vol when it inverts.
5. **VIX1D and 0DTE.** Since VIX1D's introduction (2023), the front-end of the term structure has become a tradeable concept down to 1 day. The variance risk premium at the 1-day horizon behaves differently from the 30-day horizon — see [[volatility-risk-premium-decay]].
6. **Cross-checking single-name term structure against index term structure** reveals whether a single-name move is idiosyncratic (single-name IV up, index IV flat) or systemic (both moving together). Useful for sizing single-name short premium.

## Common Mistakes

1. **Confusing constant-maturity indices with raw-month futures.** VIX is *not* what you trade in the VX1 contract. The futures price reflects expected VIX *at the futures' expiration*, not today's spot VIX.
2. **Assuming a steep curve will mean-revert quickly.** Steep contango can persist for months in calm regimes — see 2017, 2019, mid-2024. The reversion comes when regime breaks.
3. **Treating one-day backwardation as regime change.** Brief, single-session inversions around known events (FOMC, NFP) often revert. Wait for *sustained* backwardation (3+ sessions) before treating as regime signal.
4. **Holding long-VIX ETPs as long-term hedges.** The roll cost in calm regimes (50–80%/year) eats the budget faster than payoffs replenish it. Use short-dated SPX puts or VIX call spreads instead — see [[long-vol-vs-short-vol]].
5. **Ignoring the kink shape.** A flat term structure with a *kink* at month 2 (the cycle that contains an event) is structurally different from a uniformly flat curve. The kink is event vol; the rest of the curve is regime vol.
6. **Mixing index term structures with single-name term structures.** A single name's term structure is dominated by the next earnings event; an index term structure is dominated by the next macro catalyst. They reflect different forces and should be analyzed separately.

## Related

- [[volatility-regime]] — the broader concept that term structure helps classify
- [[volatility-regime-classification]] — operational framework using VIX/VIX3M as a primary input
- [[volatility-regime-switching]] — formal models of regime change; term-structure inversion is a leading observable
- [[volatility-risk-premium-decay]] — why the curve shape changes inside long calm regimes
- [[implied-volatility]] — the underlying observable
- [[vix]] — the 30-day constant-maturity benchmark
- [[vix-futures]] — the tradeable instruments along the curve
- [[contango]] / [[backwardation]] — the two canonical curve shapes
- [[variance-risk-premium]] — the structural force that gives the curve its average upward slope
- [[theta-targeting]] / [[vega-budgeting]] — sizing inputs that should be regime-conditional via term structure
- [[long-vol-vs-short-vol]] — the trade-off the curve mediates
- [[calendar-spread]] / [[diagonal-spread]] — explicit term-structure trades
- [[volmageddon]], [[covid-crash]], [[vix-august-2024-spike]] — case studies in curve inversion

## Sources

- Whaley, R. (2000). *The Investor Fear Gauge*. Journal of Portfolio Management 26(3). The canonical VIX reference.
- Demeterfi, K., Derman, E., Kamal, M., Zou, J. (1999). *More Than You Ever Wanted to Know About Volatility Swaps*. Goldman Sachs Quantitative Strategies. The variance-swap fair-strike formula underlying the VIX 2003 revision.
- CBOE. *VIX White Paper* (current methodology; revisions 2003, 2014). Constant-maturity calculation and strip selection.
- CBOE. *VIX1D, VIX9D, VIX3M, VIX6M, VIX1Y* methodology documents. The constant-maturity index family.
- Carr, P. and Wu, L. (2006). *A Tale of Two Indices*. Journal of Derivatives 13(3). Comparison of VIX and VXO and the variance-swap interpretation.
- Whaley, R. (2008). *Understanding VIX*. The Journal of Portfolio Management 35(1). Updated coverage of the term-structure properties.
- Carr, P. and Wu, L. (2009). *Variance Risk Premiums*. Review of Financial Studies 22(3). Term-structure-conditional variance risk premium evidence.
