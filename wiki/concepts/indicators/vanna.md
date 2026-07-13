---
title: "Vanna"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [options, derivatives, risk-management, volatility]
aliases: ["Vanna", "DdeltaDvol", "DvegaDspot", "Delta-Vol Cross Greek"]
domain: [risk-management, derivatives]
prerequisites: ["[[options-greeks]]", "[[delta]]", "[[vega]]", "[[implied-volatility]]"]
difficulty: advanced
related: ["[[second-order-greeks]]", "[[vomma]]", "[[volga]]", "[[charm]]", "[[delta]]", "[[vega]]", "[[gamma]]", "[[implied-volatility]]", "[[dealer-gamma-hedging]]", "[[gamma-pnl]]", "[[volatility-spike]]", "[[gamma-explosion]]", "[[portfolio-greeks-aggregation]]", "[[options-stress-testing]]", "[[spotgamma]]"]
---

**Vanna** is a second-order option Greek that measures how an option's [[delta]] changes when [[implied-volatility]] changes — or, equivalently by the symmetry of mixed partial derivatives, how its [[vega]] changes when the underlying price moves. It is the single most important "cross Greek" for understanding why a position that looks directionally neutral can suddenly develop directional exposure during a volatility shock, and it is the engine behind the dealer "vanna flows" that amplify equity-index moves around [[volatility-spike|volatility spikes]] and monthly options expiration.

## Definition

Vanna is the mixed partial derivative of the option value `V` with respect to spot `S` and volatility `σ`:

```
Vanna = ∂Δ/∂σ = ∂Vega/∂S = ∂²V/∂S∂σ
```

Because the two cross-partials are equal (Schwarz's theorem), vanna has two equivalent readings:

1. **How much delta moves per 1-point change in implied vol** (the risk-manager's view).
2. **How much vega moves per 1-point change in spot** (the volatility-trader's view).

It sits in the [[second-order-greeks|second-order Greek]] lattice alongside [[gamma]] (∂Δ/∂S), [[charm]] (∂Δ/∂t), [[vomma]] (∂Vega/∂σ), speed, and color.

## Where Vanna Is Largest

- **Out-of-the-money (OTM) options** carry the most vanna in absolute terms. A wing option's delta is highly sensitive to the level of [[implied-volatility]]: raising IV fattens the distribution and pushes more probability mass across the strike.
- **At-the-money (ATM) options** have vanna near zero — their ~0.50 delta is relatively stable as IV changes.
- **Sign flips across ATM.** OTM calls have positive vanna (delta rises as IV rises); OTM puts have negative vanna (delta becomes *more negative* as IV rises). This asymmetry is why a single aggregate vanna number can hide directional risk.
- Vanna magnitude in the wings tends to **sharpen as expiration approaches** (the peak narrows), unlike [[vomma]], which fades as vega collapses toward expiry.

## Why Vanna Matters: Dealer Vanna Flows

Vanna's market significance comes from the hedging behaviour of options dealers and market makers (see [[dealer-gamma-hedging]]). When dealers are net short OTM index puts — a common structural position because investors persistently buy downside protection — the desk carries large **negative vanna**.

The mechanism that links this to spot:

1. A volatility shock raises index IV (often *while* spot falls — IV and spot are negatively correlated for equity indices).
2. Negative vanna means the short-put book's delta becomes more negative as IV rises.
3. To stay delta-hedged, dealers must **sell** the underlying (or futures) into a falling, more-volatile market.
4. That selling pushes spot lower, which can feed back into higher IV — a self-reinforcing **vanna flow**.

The same mechanism runs in reverse on the way up: as IV *falls* after a scare (vol crush), the negative-vanna book sheds negative delta, forcing dealers to **buy**, mechanically supporting rallies. This "vol-down, dealers-buy" dynamic is a documented driver of the slow grind higher that often follows a volatility event and into monthly OPEX. Services such as [[spotgamma|SpotGamma]] and similar dealer-positioning analytics estimate aggregate vanna exposure to anticipate these flows.

## Worked Example

*(Illustrative numbers chosen to show the mechanism, not from a live book.)*

A market maker is short 1,000 index puts at the 25-delta strike (spot 5,000, 20 days to expiry, IV 16%) and has bought futures to be delta-neutral. The desk reads delta ≈ 0.

Overnight a headline lifts index IV from 16% to 22% with **no change in spot**. Because OTM puts have negative vanna, each put's delta moves from −0.25 to roughly −0.32. Being short 1,000 puts, the book's delta swings from +250 to +320 — it is now **+70 deltas long** purely from a volatility move, spot unchanged. To re-neutralise, the desk must *sell* 70 deltas of futures into a market that just got more volatile. Multiply across every dealer running short-wing inventory and the aggregate hedging is the vanna flow that pushes spot in the direction the vol move implied.

## Trading Implications

- **"Delta-neutral" is not vol-neutral.** A book hedged flat at current spot and IV can develop real directional risk the instant IV moves. Stress the book under *joint* spot-and-IV shocks, not one variable at a time.
- **Wing inventory is vanna inventory.** [[iron-condor|Iron condors]], [[short-strangle|short strangles]], and other wing-heavy structures load up vanna even when ATM [[gamma]] looks flat.
- **Calendar and skew trades** are deliberate vanna/[[vomma]] expressions, since the cross-Greek dominates their P&L during regime changes.
- **Risk limits.** Institutional desks set explicit vanna limits alongside delta, gamma, and vega to cap "unexplained P&L" — the residual after first-order attribution is usually vanna during a vol regime shift (see [[portfolio-greeks-aggregation]] and [[options-stress-testing]]).

## Related

- [[second-order-greeks]] — the family vanna belongs to
- [[vomma]] / [[volga]] — vega's convexity; the sibling vol-of-vol Greek
- [[charm]] — delta's drift through time
- [[delta]] / [[vega]] — the first-order Greeks vanna connects
- [[dealer-gamma-hedging]] — how dealer hedging converts vanna into market flow
- [[gamma-explosion]] / [[volatility-spike]] — when vanna dominates P&L
- [[spotgamma]] — dealer-positioning analytics that track aggregate vanna

## Sources

- Sheldon Natenberg, *Option Volatility and Pricing* — practitioner treatment of higher-order Greeks and dealer hedging (see [[book-option-volatility-and-pricing]]).
- John Hull, *Options, Futures, and Other Derivatives* — the mathematical definition of second-order partial derivatives of option value (see [[book-options-futures-other-derivatives]]).
