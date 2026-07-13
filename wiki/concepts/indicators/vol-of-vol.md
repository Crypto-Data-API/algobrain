---
title: "Vol of Vol"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, indicators, risk-management]
aliases: ["VVIX", "Vol of Vol", "Volatility of Volatility", "Vol-of-Vol"]
related: ["[[vix]]", "[[vvix]]", "[[volatility]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volga]]", "[[vanna]]", "[[options-greeks]]", "[[second-order-greeks]]", "[[options-risk-budgeting]]", "[[vega-budgeting]]", "[[volatility-spike]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[covid-19-crash]]", "[[volatility-surface]]", "[[skew]]", "[[short-strangle]]", "[[iron-condor]]", "[[stochastic-volatility]]"]
domain: [risk-management, derivatives]
prerequisites: ["[[implied-volatility]]", "[[vix]]", "[[options-greeks]]"]
difficulty: advanced
---

**Vol of vol** (VoV) is the volatility of [[implied-volatility]] itself — how much IV moves around, conditional on its current level. The headline market measure is [[vvix|VVIX]], the [[cboe|CBOE]]'s "VIX of VIX" index, which is computed from the prices of [[vix|VIX]] options using the same model-free variance formula that produces the VIX itself. Vol-of-vol is the empirical driver of [[volga]] and [[vanna]] P&L, the parameter that determines how badly OTM short-premium positions blow up in vol spikes, and the most reliable early warning signal for regime change in equity options markets. Empirically, VVIX averages around 80-100 in calm regimes and spikes to 150-220+ in crises like [[volmageddon]] (Feb 2018), the [[covid-19-crash|COVID crash]] (March 2020), and the [[vix-august-2024-spike|August 2024 yen-carry unwind]].

## Overview

Implied volatility is the market's forward expectation of realized vol. It is itself a price — a price that moves. The volatility of that price is vol-of-vol.

There are three related concepts to keep distinct:

1. **Realized vol of IV** — the historical standard deviation of changes in the [[vix|VIX]] (or of ATM IV for any underlying). Backward-looking.
2. **Implied vol-of-vol** — the level of vol-of-vol implied by the prices of [[vix|VIX]] options. Forward-looking. [[vvix|VVIX]] is the standardized measure of this.
3. **Vol-of-vol parameter** — in stochastic-volatility models (Heston's "ξ", SABR's "ν", Bergomi's "ω"), the parameter governing how much the volatility process moves. Calibrated to the option market.

When traders say "vol-of-vol is high," they usually mean *implied* — i.e., VVIX is elevated. VVIX is the lingua franca because it's a single transparent number published live by the [[cboe|CBOE]].

Vol-of-vol matters because it is the *market price of [[volga]] risk*. A book short volga (e.g., short OTM strangle) is implicitly short a bet on vol-of-vol. If realized vol-of-vol exceeds implied vol-of-vol over the holding period, the book loses; if vol-of-vol stays calm, it earns the premium. The [[variance-risk-premium|VRP]] for VIX options is generally positive (sellers of VIX options earn a premium for bearing tail risk), but the tail-loss episodes are large enough to wipe out years of premium.

## Definition / Formula

### VVIX (CBOE methodology)

VVIX is computed by [[cboe|CBOE]] using the same model-free variance formula as VIX, but applied to the prices of options *on* VIX futures rather than options on SPX. The formula (simplified) is:

```
VVIX² = (2/T) × Σᵢ (ΔKᵢ / Kᵢ²) × e^(rT) × Q(Kᵢ) − (1/T) × (F/K₀ − 1)²
```

where Q(Kᵢ) is the mid-quote price of out-of-the-money VIX options at strike Kᵢ, K₀ is the at-the-money strike, F is the VIX forward, and T is time-to-expiration (typically 30 days). The result is annualized like VIX.

VVIX represents the *expected 30-day volatility of VIX* expressed in annualized vol points. A VVIX of 100 means the market expects VIX itself to have an annualized vol of 100% over the next 30 days — a startlingly high number when you think about it (VIX is a vol index, so 100% vol-of-vol means VIX could double or halve over a month with non-trivial probability).

Reference: CBOE *VVIX White Paper* (2012), updated for VIX option methodology changes.

### Stochastic-vol parameter

In a Heston model:

```
dvₜ = κ(θ − vₜ) dt + ξ × √vₜ × dWₜ
```

ξ is the vol-of-vol parameter. Calibrated to the surface, ξ for SPX typically lives in the 0.5-1.5 range; rises to 2.0+ in stress.

In SABR:

```
dαₜ = ν × αₜ × dWₜ
```

ν is the vol-of-vol. Calibrated per expiration.

These parametric forms are useful for modeling and pricing exotics; for trading risk, VVIX is the operational measure.

### Vol-of-vol and volga: the link

The cleanest way to understand why vol-of-vol matters at the position level is through [[volga]] (the second derivative of option value with respect to [[implied-volatility|IV]], also called "vomma"). Volga is to vega what gamma is to delta: it is the *convexity* of an option's value in volatility space. The realised P&L attributable to volga over a holding period is approximately:

```
Volga P&L ≈ ½ × Volga × (ΔIV)²
```

Vol-of-vol is precisely what governs the size of `(ΔIV)²`. A long-volga position (long wings, long OTM options) *benefits* from large IV moves in either direction — it is implicitly **long vol-of-vol**. A short-volga position (short strangle, [[iron-condor]]) is **short vol-of-vol** and loses convexly when IV jumps. VVIX is therefore the market's price for the volga exposure: high VVIX means the market is paying up for convexity, and short-volga premium is correspondingly richer (and more dangerous). See [[volga]] for the position-level Greeks and [[vanna]] for the cross spot-IV term that co-moves with vol-of-vol in equity skew.

### Vol-of-vol vs. the three "vols"

| Quantity | What it measures | Forward/backward | Operational gauge |
|---|---|---|---|
| Realized volatility | How much the *underlying* has moved | Backward | [[realized-volatility\|RV]] (rolling stdev of returns) |
| Implied volatility | Market's forecast of future RV | Forward | [[vix\|VIX]] (for SPX), ATM IV |
| Vol-of-vol (realized) | How much *IV itself* has moved | Backward | Rolling stdev of VIX changes |
| Vol-of-vol (implied) | Market's forecast of future vol-of-vol | Forward | [[vvix\|VVIX]] |

Reading down the column: VVIX is to VIX exactly as VIX is to SPX. It is the next derivative up the volatility hierarchy.

## Why It Matters (for risk-budgeted books)

Inside [[options-risk-budgeting]], vol-of-vol is the *level adjuster* for the vega cap and the *binding parameter* for the volga cap:

1. **Vega cap should scale inversely with vol-of-vol.** A book sized to absorb a 5-vol-point IV move when VVIX is 80 should be sized to absorb a 15-vol-point move when VVIX is 150. Failing to scale = blow-up risk. The simplest rule: vega-cap × √(VVIX_baseline / VVIX_current) when VVIX exceeds a threshold.

2. **Volga P&L scales with VoV²**. The variance of vega's P&L over a horizon ≈ Vega² × (vol-of-vol)² × T. Doubling VVIX quadruples expected variance of vega P&L. Books unaware of this discover it during spikes. See [[volga]] for the position-level mechanics.

3. **Wing pricing uses VoV.** OTM option prices in stochastic-vol models contain a VoV-dependent premium (the "smile premium"). When VoV rises, the wings re-price upward — even if the ATM IV is unchanged. Short-OTM positions take mark-to-market hits driven entirely by VoV, not direction.

4. **Regime detection.** VVIX is a leading indicator. Empirically it rises *before* VIX in some episodes — vol traders position for a regime change first, dragging VVIX up, then realized vol arrives and VIX follows. Examples: VVIX rose from ~85 to ~115 in the days before [[volmageddon|Feb 5 2018]]; VVIX hit ~225 a day before VIX peaked in March 2020. Not a perfect leading indicator (some spikes co-move) but useful as a confirmation.

5. **Tail-hedge cost.** Buying tail hedges (long OTM puts, long [[vix|VIX]] calls) costs more in high-VoV regimes because the wings (long-volga instruments) are bid up. The optimal hedger buys insurance when VoV is *low* (cheap), not when it has already spiked — but most hedgers buy reactively. See [[tail-hedging]] for cost-aware timing.

6. **Liquidity proxy.** VoV correlates with bid-ask spreads in options, especially in the wings. High VVIX = wide spreads = expensive exits. Books planning to flatten in stress need to assume worse fills than backtests show.

## VVIX Regime Decision Table

A practitioner cheat-sheet for translating the joint VIX / VVIX reading into a posture. Levels are illustrative round numbers, not trading advice.

| VIX | VVIX | Joint reading | Typical short-premium posture | Tail-hedge posture |
|---|---|---|---|---|
| Low (12-16) | Low (<85) | Calm and stable | Harvest premium near full size | Buy hedges — cheap convexity |
| Low (12-16) | High (>110) | Calm spot, nervous vol traders | Trim size; a jump is being priced | Accumulate — wings still cheap |
| Mid (18-24) | Mid (95-130) | Normal stress | Half size; widen strikes | Hold existing hedges |
| High (28-40) | Mid (130-160) | High but *stable* vol | Selective selling into rich IV | Begin monetizing hedges |
| High (28-40) | High (>170) | High *and* uncertain vol | Stand aside — no-crush risk | Hold; do not chase new hedges (expensive) |
| Spike (>40) | Spike (>200) | Crisis | Flat / defensive only | Monetize into the spike |

The two diagonal cells — *calm spot but high VVIX*, and *high spot but mid VVIX* — are the most information-rich. The first ("decoupling") often precedes a jump; the second signals that the *level* of vol, not the *uncertainty*, is now the dominant risk.

## Worked Example

### VVIX historical reference levels

Approximate historical VVIX levels by regime (close-of-day):

| Regime | VVIX range | Date examples |
|---|---|---|
| Deep calm | 65-80 | mid-2017, late 2019 |
| Normal | 80-100 | most of post-2010 |
| Mild stress | 100-130 | Q4 2018, mid-2022 |
| Acute stress | 130-180 | Aug 2015, Brexit Jun 2016, Q4 2018 lows, late 2022 |
| Crisis | 180-225+ | [[volmageddon|Feb 5 2018]], [[covid-19-crash|March 2020]], [[vix-august-2024-spike|Aug 5 2024]] |

VVIX peaked around 225 on Feb 6 2018 (Volmageddon, where short-vol ETPs imploded — see [[xiv-collapse]]) and around 207 on March 16 2020 during the COVID crash. The August 5 2024 yen-carry unwind drove VVIX to ~190 intraday alongside a record 1-day VIX spike.

### Position implication — short strangle in two regimes

A trader sells the same SPX 30-DTE 1-sigma short strangle in two different regimes:

**Regime A (calm):** SPX = 5,000, VIX = 14, VVIX = 85, IV-strangle ≈ 12%.
- Net vega = -$200, net volga = -$15, premium collected = $1,200
- Expected daily IV move (1σ) ≈ VVIX × VIX × √(1/252) / 100 ≈ 85% × 14 × 0.063 ≈ **0.75 vol points/day**
- Expected daily vega P&L variance ≈ 200 × 0.75 ≈ ±$150

**Regime B (stress):** SPX = 5,000, VIX = 28, VVIX = 150, IV-strangle ≈ 26%.
- Same nominal vega = -$200 (pretend strikes are re-fitted to 1-sigma at the new vol)
- Expected daily IV move ≈ 150% × 28 × 0.063 ≈ **2.65 vol points/day**
- Expected daily vega P&L variance ≈ 200 × 2.65 ≈ ±$530

Same nominal vega exposure. **3.5× the expected daily P&L variance** because vol-of-vol scaled with VIX × VVIX. A vega cap that ignores VVIX systematically undersizes risk in stress regimes — which is exactly when discipline matters most.

### How VVIX moves vs VIX

Empirically, VVIX is correlated with VIX (when VIX rises, VVIX usually rises too) but not 1-for-1. The relationship has these stylized facts:

1. **VVIX leads VIX by 0-2 days at regime turns.** Sophisticated vol traders position before realized vol arrives.
2. **VVIX/VIX ratio compresses in spikes.** In calm regimes, VVIX/VIX is ~5-7. In acute stress, it can compress to 4 (VIX rising faster than VVIX) — a sign that the *level* of vol is now the dominant risk, not the *uncertainty* about vol.
3. **VVIX leads in normalization.** After spikes, VVIX often falls before VIX — vol traders bid offers as VIX comes off, and market makers reduce VoV pricing first.
4. **Decoupling = regime shift.** When VVIX rises and VIX doesn't, traders are positioning for a tail event that hasn't arrived yet. Often a leading signal of an upcoming jump.

### Pricing a VIX call using VoV

A 30-DTE VIX 25-strike call when VIX = 18 and VVIX = 110: under a Black-Scholes-style model on VIX directly, the call price ≈ VIX × N(d₁) − 25 × e^(-rT) × N(d₂) using σ = VVIX/100 = 1.10 as the volatility input. The high VVIX makes this OTM call genuinely expensive — much more expensive than the same strike in a 75-VVIX regime would be. This is why hedgers prefer to buy tail hedges in calm regimes.

## Common Misuse / Pitfalls

1. **Confusing VIX and VVIX.** VIX is the price (level) of equity vol; VVIX is the price of equity-vol-vol. A "high VIX" environment can have low VVIX (vol is high but stable) or high VVIX (vol is high *and* uncertain). The two together describe the regime.

2. **Treating VVIX as a vol number.** VVIX of 100 is *not* a 100% probability of a vol spike. It is the implied annualized vol of the VIX index. Convert appropriately for risk calculations.

3. **Assuming VoV is constant.** Vol-of-vol clusters and trends just like vol does. A model with a fixed ξ or ν calibrated last quarter is wrong this quarter. Recalibrate frequently — daily for serious vol books.

4. **Ignoring VoV in scenario analysis.** A scenario grid that varies spot and vol but holds VoV fixed underestimates wing P&L in stress. Real spikes have spot drops + IV jumps + skew steepening + VoV explosions all simultaneously. Multi-factor stress should jointly shock all four.

5. **Using VVIX without regime context.** VVIX = 100 is normal; the same number after VIX has fallen from 30 to 14 might mean vol traders expect a relapse. Always read VVIX alongside VIX level and trend.

6. **Mistiming tail hedges.** Buying VIX calls when VVIX is 200 is buying insurance on a burning house. The optimal hedger buys when VoV is *low* — when premiums are cheap and the book has time. Most retail hedgers do the opposite, which is why their tail hedges have negative expectancy.

7. **Asset-class-specific VoV measures don't exist for most underlyings.** VVIX exists for SPX. Other markets (currencies, commodities, single-name equities) have no published VoV index. Traders must build their own from the vol surface (the convexity of the smile encodes VoV). Sloppy substitution of SPX VVIX for other-asset VoV is a common error.

8. **VVIX has microstructure quirks.** VIX options have wide bid-ask spreads and limited liquidity at the wings, especially in stress. Reported VVIX in stress can lag actual market prices and contain stale-quote artifacts. Treat VVIX moves of >10% in 5 minutes with suspicion.

## Related

- [[vix]] — the underlying that VVIX is computed on
- [[vvix]] — dedicated page on the VVIX index itself
- [[volatility]] — first-order concept
- [[implied-volatility]] — the variable that vol-of-vol governs
- [[realized-volatility]] — counterpart; vol-of-vol of realized series differs from implied
- [[volga]] — position-level Greek that prices vol-of-vol
- [[vanna]] — cross spot-IV Greek; also touches vol-of-vol
- [[options-greeks]] — primer
- [[second-order-greeks]] — family containing volga and vanna
- [[options-risk-budgeting]] — framework that uses VoV to scale vega caps
- [[vega-budgeting]] — companion budget that should be VoV-adjusted
- [[volatility-spike]] — events driven by VoV explosions
- [[volmageddon]] — Feb 2018; classic VoV-driven blowup
- [[vix-august-2024-spike]] — Aug 2024; another VoV-driven episode
- [[covid-19-crash]] — March 2020; VoV peaked above 200
- [[volatility-surface]] — surface curvature encodes VoV
- [[skew]] — surface tilt; partly driven by VoV asymmetry
- [[short-strangle]] — short-volga structure exposed to VoV
- [[iron-condor]] — same
- [[stochastic-volatility]] — model family that prices VoV explicitly

## Sources

- [[cboe-vvix-white-paper]] — CBOE official methodology document for the VVIX index
- [[book-options-futures-other-derivatives]] — Hull on stochastic volatility models and the role of vol-of-vol parameters
- [[book-option-volatility-and-pricing]] — Natenberg's qualitative treatment of vol-of-vol and its trading implications
- [[book-dynamic-hedging]] — Taleb on convexity of vol-of-vol and why position sizing must scale with VoV
- [[book-stochastic-volatility-modeling]] — Bergomi's *Stochastic Volatility Modeling* (2015), the most rigorous modern treatment of vol-of-vol pricing and calibration
