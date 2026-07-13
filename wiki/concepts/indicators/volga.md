---
title: "Volga"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, risk-management, indicators, volatility, greeks]
aliases: ["Volga", "Vomma", "Vol Gamma", "Vol Convexity"]
related: ["[[vega]]", "[[gamma]]", "[[options-greeks]]", "[[second-order-greeks]]", "[[vol-of-vol]]", "[[options-risk-budgeting]]", "[[vega-budgeting]]", "[[implied-volatility]]", "[[volatility-spike]]", "[[short-strangle]]", "[[iron-condor]]", "[[straddle-strangle]]", "[[vanna]]", "[[skew]]", "[[volatility-surface]]", "[[volmageddon]]", "[[vix-august-2024-spike]]"]
domain: [risk-management, derivatives]
prerequisites: ["[[vega]]", "[[options-greeks]]", "[[implied-volatility]]"]
difficulty: advanced
---

**Volga** (also called **vomma**) is the second derivative of an option's price with respect to [[implied-volatility]] — i.e., the rate at which [[vega]] itself changes as IV changes. It is the *vol-of-vol Greek*: a long-volga position is convex in vol (gains from any large IV move, up or down), while a short-volga position is concave (loses on big IV moves either direction). [[straddle-strangle|Strangles]], [[iron-condor|condors]], and other short-OTM-premium structures are systematically *short volga* at their wings, which is why they get crushed not just by direction but by [[vol-of-vol|vol-of-vol]] explosions in events like [[volmageddon]] and the [[vix-august-2024-spike|August 2024 VIX spike]].

## Overview

[[vega]] tells you how option price changes per 1-vol-point change in IV. But vega itself is a function of IV — it's not a fixed sensitivity. **Volga** measures the curvature: how vega responds to vol moves.

Geometrically, plot option price on the y-axis against IV on the x-axis. Vega is the slope of that curve. Volga is the curvature.

- **Positive volga (long volga)**: the curve is convex. As IV rises, vega grows; as IV falls, vega shrinks. The position gains on *any* large vol move (in either direction), because the convex curve always lies above its tangent line. This is the volatility analog of [[gamma]] in spot.
- **Negative volga (short volga)**: the curve is concave. Vega shrinks as IV moves either way from the current point. The position loses on *any* large vol move. This is the volatility analog of short gamma.

Volga is one of the [[second-order-greeks]] (along with [[vanna]], [[charm]], speed, color). For most retail books it is invisible until a [[volatility-spike|vol spike]] suddenly produces large unexplained losses on positions that were "vega-budgeted" correctly. The vega budget was right; the volga budget was missing.

### Greek-of-Greek map

Volga sits in a tidy lattice of derivatives. Knowing where it lives makes the analogy to spot risk intuitive:

| | First derivative | Second derivative |
|---|---|---|
| w.r.t. **spot** S | [[delta]] | [[gamma]] |
| w.r.t. **vol** σ | [[vega]] | **volga** (∂vega/∂σ) |
| cross spot × vol | — | [[vanna]] (∂vega/∂S = ∂delta/∂σ) |

Read across the vol row: **volga is to vega what gamma is to delta.** A long-gamma position profits from spot moving in either direction; a long-volga position profits from IV moving in either direction. Short-gamma blows up on a big spot move; short-volga blows up on a big IV move. The retail short-premium book is usually both short gamma *and* short volga — the two punish it simultaneously in a [[volatility-spike|spike]].

## Definition / Formula

Volga is defined as:

```
Volga = ∂²C/∂σ² = ∂Vega/∂σ
```

Under [[black-scholes|Black-Scholes]] for a European option, the closed-form expression is:

```
Volga = Vega × (d₁ × d₂) / σ
```

where

```
d₁ = (ln(S/K) + (r + 0.5σ²)T) / (σ√T)
d₂ = d₁ − σ√T
```

and Vega = S × N'(d₁) × √T (the standard BSM vega).

### Sign and shape

Volga is positive when d₁ × d₂ > 0 — i.e., when both d₁ and d₂ have the same sign. This happens for **OTM and deep-ITM options**. Volga crosses zero near the at-the-money strike (where d₁ ≈ 0 or d₂ ≈ 0).

Equivalently:

| Moneyness | d₁ × d₂ | Volga | Interpretation |
|---|---|---|---|
| Far OTM (calls or puts) | positive (both negative for OTM puts; both positive for OTM calls) | **positive** | Vega grows as IV rises |
| ATM | near 0 | **near zero** | Vega is flat in IV near ATM |
| Far ITM | positive | **positive** | Same convex behavior as far OTM (put-call parity) |

Volga is also higher for longer-dated options (more time × √T factor) and scales roughly linearly with vega.

### Per-position sign convention

- **Long an option** (call or put): long volga at the wings, near-zero volga at ATM.
- **Short an option**: short volga at the wings, near-zero at ATM.
- **Long straddle** (long ATM call + long ATM put): near-zero volga at the strike, but long-volga *exposure to the wings* if IV moves significantly.
- **Long strangle**: long volga (long both OTM legs).
- **Short strangle / short iron condor**: **short volga** at both wings — the canonical retail short-volga book.
- **Long calendar spread** (long far-dated ATM, short near-dated ATM): mixed, but typically slightly long-volga because the long far-dated leg has higher absolute volga.

### Structure-level volga cheat sheet

| Structure | Net volga | Vega sign | What hurts it |
|---|---|---|---|
| Long single OTM option | Long | Long | IV staying flat (theta bleed) |
| [[short-strangle]] | **Short** | Short | IV spike (vega + volga both bite) |
| [[iron-condor]] | **Short** (smaller than strangle) | Short | IV spike; wings cap loss but not volga path |
| Long straddle | ≈ Zero at strike, long at wings | Long | Quiet, range-bound tape |
| Long strangle | Long | Long | Realized vol below implied |
| Long calendar (ATM) | Slightly long | Long | Front-month IV collapse / spot drift |
| Far-OTM long wings (tail hedge) | **Strongly long** | Long | Carry (theta) in calm regimes |

The pattern: **selling OTM premium is structurally short volga; buying OTM premium is structurally long volga.** The wings carry the volga, not the body.

### Measuring volga in practice

Black-Scholes prices volga at zero conceptually (constant vol), yet the BSM *formula* still yields a non-zero `Vega × d₁d₂ / σ` value because it differentiates the BSM price w.r.t. its IV input. Practitioners get volga two ways:

| Method | How | Notes |
|---|---|---|
| Closed form | `Vega × d₁ × d₂ / σ` per leg, then sum | Fast; assumes flat-vol bumps, ignores [[skew]] dynamics |
| Numerical bump | Re-price at IV ± Δσ; volga ≈ (Vega₊ − Vega₋) / (2Δσ) | Captures whatever model you use ([[stochastic-volatility|SABR]], Heston) |
| Scenario grid | Tabulate P&L over a matrix of IV shifts | What desks actually risk-manage on; surfaces the (ΔIV)² convexity directly |

For a wing-heavy short-premium book, the scenario grid is the only honest method — it shows the quadratic loss term that linear vega caps miss entirely.

## Why It Matters (for risk-budgeted books)

Inside [[options-risk-budgeting]], vega is one of the six binding caps. But a vega cap alone is insufficient for books with material OTM exposure. The reason:

1. **Vega is a snapshot sensitivity at one IV level.** A short strangle with vega = -$500 (per vol-point) at IV = 15% has a *different* vega when IV jumps to 30%. Specifically, vega magnitude *grows* if volga is positive — i.e., for the wings of the strangle. The trader's "vega budget" of -$500 turns into -$900 mid-spike. The realized loss is much larger than vega × ΔIV would predict.

2. **Volga tracks vol-of-vol risk.** [[vol-of-vol]] (typically measured by [[vvix|VVIX]]) is the volatility of implied volatility. Books short volga have a payoff equivalent to selling a vol option. When VVIX rises, the implied price of vol-of-vol rises, and short-volga positions lose mark-to-market even before any IV move. Long-volga positions gain. This is invisible to vega-only attribution.

3. **Convex left tail.** OTM put short-sellers are short volga at the put wing. In a [[volatility-spike|spike]], IV at the put wing typically rises far more than ATM IV (the [[skew|skew]] steepens). Volga × (ΔIV at the wing)² is a quadratic loss term that compounds the linear vega loss. This explains why short put strikes blow up by 5-10x their nominal vega exposure in stress.

4. **Vega-neutral does not mean vol-neutral.** A book with net vega = 0 (long ATM vega, short OTM vega) can still be heavily short volga. A 5-vol IV spike that disproportionately repricesthe wings (skew steepening) flatters the long ATM leg by little, while crushing the short OTM legs. Net P&L is negative even though "vega is hedged."

5. **Pricing the wings correctly requires a volga model.** The [[stochastic-volatility|stochastic-vol]] family of models (Heston, SABR, Bergomi) explicitly prices vol-of-vol — i.e., volga and vanna. Black-Scholes assumes vol is constant and prices volga at zero. Sellers using BSM-implied IV are systematically *underpricing* the wings. Sophisticated desks add a volga adjustment to BSM prices for OTM options.

For these reasons, professional vol books track a separate **volga budget** alongside the vega budget. Typical institutional caps: ±10% of total notional vega per vol point of IV move. Retail books almost never measure volga, which is part of why they get destroyed in vol spikes.

## Worked Example

A trader sells one SPX 30-DTE iron condor:
- Sell 10 SPX 4900P, sell 10 SPX 5100C
- Buy 10 SPX 4850P, buy 10 SPX 5150C
- SPX = 5000, IV-ATM = 15%, vol-points are flat across strikes for simplicity

Approximate Greeks at trade inception:

| Leg | Vega | Volga (per vol-pt²) |
|---|---|---|
| -10 × 4900P | -$300 | -$22 |
| -10 × 5100C | -$320 | -$24 |
| +10 × 4850P | +$200 | +$15 |
| +10 × 5150C | +$215 | +$16 |
| **Net** | **-$205** | **-$15** |

The book is short ~$200 of vega and short ~$15 of volga (per vol-pt²).

### Scenario 1 — IV rises modestly

IV rises uniformly from 15% to 18% (+3 vol points).

Vega P&L = -$205 × 3 = **-$615**
Volga P&L = 0.5 × Volga × (ΔIV)² = 0.5 × (-15) × 3² = **-$67.50**

Total ≈ **-$683**. Most of the loss is vega; volga adds ~10%.

### Scenario 2 — IV spikes sharply (vol event)

IV rises uniformly from 15% to 35% (+20 vol points).

Vega P&L = -$205 × 20 = **-$4,100** (linear extrapolation)
Volga P&L = 0.5 × (-15) × 20² = **-$3,000**

Total ≈ **-$7,100**.

But this still understates the real loss because:
1. The skew typically steepens — the put wing IV rises more than ATM (e.g., +30 vol points at 4900P, +20 at 5100C). The volga loss on the put leg becomes **0.5 × 22 × 30² × 1 ≈ $9,900** for that single leg.
2. Volga itself grows as IV rises (third derivative — *ultima*).
3. Spot has likely fallen alongside the IV jump, dragging the book deeper into the short put — gamma loss compounds.

A position that on paper had a vega-budget of $1,000/vol-pt × 3 vol-pts = $3,000 worst-case loss can produce $10,000-$15,000 of actual loss in a real [[volatility-spike|vol spike]] when volga (and skew dynamics, and gamma) all bite simultaneously.

### Scenario 3 — Long-volga hedge

A trader who wants to neutralize the volga adds a long position at far-OTM strikes. For instance, buying 5 SPX 4500P (deep OTM) and 5 SPX 5500C (deep OTM):

| Leg | Vega | Volga |
|---|---|---|
| +5 × 4500P | +$50 | +$25 |
| +5 × 5500C | +$45 | +$22 |
| **Hedge** | **+$95** | **+$47** |

After hedge: net vega = -$110, net volga = +$32. The book is now mildly *long* volga — a vol spike now produces a quadratic *gain* from the volga term that offsets the linear vega loss. Cost: the long wings have negative theta (~-$15/day), trading some carry for tail-protection. This is a textbook **wing hedge** and is the structural basis of [[long-vol|tail-hedge]] sleeves.

## Common Misuse / Pitfalls

1. **Treating volga as zero because BSM treats it as zero.** Black-Scholes assumes vol is deterministic and constant — there is no vol-of-vol. So BSM-derived risk reports often miss volga entirely. Real markets price volga implicitly via the [[volatility-surface|vol smile]]. Use a vol-aware model (SABR, Heston, Bergomi) or at minimum compute volga from numerical re-pricing under IV bumps.

2. **Confusing volga with vega convexity at ATM.** Volga is *near zero* at ATM. The largest volga sits in the wings. Traders looking at ATM options miss the volga entirely — and ATM-only vega caps fail to flag wing risk.

3. **Linear vega-cap thinking.** A book sized to "lose $X per vol point of IV move" using linear vega ignores the (ΔIV)² term. For 5-point IV moves and modest volga, error is small (~10%). For 15-30-point spikes, the linear estimate can understate true loss by 2-3×.

4. **Forgetting the cross terms.** A real spike is rarely IV-only. Spot moves, skew steepens, term structure inverts. The full P&L decomposition includes [[vanna]] (delta-IV cross), [[charm]] (delta-time), and skew dynamics. Volga is necessary, not sufficient.

5. **Asymmetric volga in skewed surfaces.** OTM puts and OTM calls in equity index markets have different volga magnitudes because the surface is skewed (puts at higher IV than calls, more steeply). Volga at the put wing is typically larger and more reactive than volga at the call wing. A symmetric strangle is therefore *not* symmetric in volga risk.

6. **Volga decays with time.** Long-volga positions in long-dated wings cost theta (the wings are long premium). Holding long volga as a permanent hedge incurs carry. Tail-hedge sleeves accept this carry as the cost of stability — see [[options-risk-budgeting#allocating-across-strategies-sleeves]].

7. **Volga vs vol-of-vol pricing confusion.** Volga is a *position Greek* (your sensitivity). [[vol-of-vol]] is a *market parameter* (the volatility of IV). They are linked but distinct: position volga × vol-of-vol² ≈ daily P&L variance from the volga term. High vol-of-vol regimes (VVIX > 120) demand tighter volga caps; the volga number itself doesn't change with VVIX, but its expected P&L impact does.

## Related

- [[vega]] — first-order vol Greek that volga derives from
- [[gamma]] — spot analog of volga (second derivative in spot vs in vol)
- [[options-greeks]] — primer
- [[second-order-greeks]] — full family of higher-order Greeks; volga is one
- [[vol-of-vol]] — market parameter; volga is the position-level counterpart
- [[vvix]] — headline measure of vol-of-vol
- [[options-risk-budgeting]] — risk framework that should include a volga budget for any wing-heavy book
- [[vega-budgeting]] — companion budget at first order
- [[short-strangle]] — canonical short-volga structure
- [[iron-condor]] — same
- [[straddle-strangle]] — strangle is long-volga; straddle is near-zero
- [[vanna]] — cross spot-IV second-order Greek
- [[skew]] — vol surface dynamics that interact with volga
- [[volatility-surface]] — full surface; volga is a slice of it
- [[volmageddon]] — Feb 2018 vol-of-vol explosion that destroyed short-volga books
- [[vix-august-2024-spike]] — Aug 2024 VIX spike, similar dynamics

## Sources

- [[book-options-futures-other-derivatives]] — Hull's derivation of the BSM second-order Greeks including volga
- [[book-option-volatility-and-pricing]] — Natenberg on portfolio-level wing risk and the empirical role of volga
- [[book-dynamic-hedging]] — Taleb on the convexity of vol-of-vol and why short-volga positions must be sized to scenario-loss, not vega
- [[book-stochastic-volatility-modeling]] — Bergomi's *Stochastic Volatility Modeling* (2015) for the formal vol-of-vol pricing framework that motivates volga as a hedgeable risk
