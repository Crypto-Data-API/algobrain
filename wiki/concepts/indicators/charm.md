---
title: "Charm"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [options, derivatives, risk-management, volatility]
aliases: ["Charm", "Delta Decay", "Delta Bleed", "DdeltaDtime", "DcharmDtime"]
domain: [risk-management, derivatives]
prerequisites: ["[[options-greeks]]", "[[delta]]", "[[theta]]", "[[gamma]]"]
difficulty: advanced
related: ["[[second-order-greeks]]", "[[vanna]]", "[[vomma]]", "[[volga]]", "[[delta]]", "[[theta]]", "[[gamma]]", "[[delta-neutral]]", "[[gamma-explosion]]", "[[0dte-trading]]", "[[dealer-gamma-hedging]]", "[[portfolio-greeks-aggregation]]", "[[options-stress-testing]]", "[[max-pain]]"]
---

**Charm** is a second-order option Greek that measures how an option's [[delta]] changes as time passes — equivalently, how its [[theta]] changes when the underlying moves. Often called **delta decay** or **delta bleed**, charm quantifies the "drift" a position's delta experiences overnight even when the underlying price does not move at all. It is the reason a book that is hedged perfectly [[delta-neutral]] at the close is no longer neutral at the next open, and it becomes one of the dominant risks of holding short-dated options through expiration.

## Definition

Charm is the cross-partial derivative of the option value `V` with respect to spot `S` and time `t`:

```
Charm = ∂Δ/∂t = -∂Θ/∂S = -∂²V/∂S∂t
```

Because the mixed partials commute (Schwarz's theorem), charm has two equivalent readings:

1. **How much delta drifts per unit of time** (the hedger's view — "how much delta do I gain or lose overnight?").
2. **How much [[theta]] changes per 1-point move in spot** (the time-decay view — "how does my decay rate shift as the underlying moves?").

It sits in the [[second-order-greeks|second-order Greek]] lattice alongside [[gamma]] (∂Δ/∂S), [[vanna]] (∂Δ/∂σ), [[vomma]] (∂Vega/∂σ), speed, and color. Charm is conventionally quoted as **delta change per day** (dividing the annualised derivative by 365) so a desk can read it directly as "deltas drifting per calendar day."

## Where Charm Is Largest

- **Out-of-the-money (OTM) options** *lose* delta over time — charm bleeds their delta toward zero because, as expiry nears, an OTM option's probability of finishing in the money shrinks. An OTM call's delta drifts down from, say, 0.30 toward 0; an OTM put's delta drifts up from −0.30 toward 0.
- **In-the-money (ITM) options** *gain* delta magnitude over time, charm pushing delta toward ±1.0 as the option behaves more and more like the underlying.
- **At-the-money (ATM) options** have relatively small charm far from expiry — delta hovers near 0.50 — but charm becomes erratic and large in the final days as the ATM delta becomes razor-sensitive to tiny moves.
- **Near expiration** charm effects accelerate dramatically (they inherit the same `t → 0` divergence as [[gamma-explosion|gamma]]), which is why [[0dte-trading|0DTE]] and expiration-week positions require near-constant rehedging.
- Charm also depends on **moneyness and the weekend/calendar effect**: theta and therefore charm are often booked across non-trading days, so a Friday-to-Monday hold can deliver three days of delta drift at once.

## Why Charm Matters

Charm is the bridge between time decay and directional risk. A few practical consequences:

1. **Overnight delta drift.** A desk that squares its delta at the close will arrive to a non-zero delta at the open purely from the passage of time, before the underlying ticks. Charm is the budgeted estimate of that drift, so the morning re-hedge size can be anticipated rather than discovered.
2. **Calendar and diagonal spreads.** These positions deliberately hold legs with different expiries; the near-leg and far-leg charm differ, so the spread's delta evolves day to day even with a frozen tape. Charm is a core P&L driver of the structure.
3. **Pin risk and dealer hedging.** Into a large monthly or quarterly expiration, charm on the aggregate dealer book forces predictable, mechanical re-hedging of stock/futures as OTM strikes bleed delta toward zero — one of the flows that can pin price toward heavily-traded strikes (see [[max-pain]] and [[dealer-gamma-hedging]]).
4. **Hedging cost accounting.** Institutional desks keep an explicit **charm budget** so the expected cost of overnight re-hedging is reflected in risk limits rather than appearing as "unexplained" P&L (see [[portfolio-greeks-aggregation]] and [[options-stress-testing]]).

## Worked Example

*(Illustrative numbers chosen to show the mechanism, not from a live book.)*

A trader is long 100 OTM calls struck at 110 (spot 100, 5 days to expiry). Each call has delta ≈ 0.30, so the position reads **+30 deltas**, and the trader has sold 30 units of the underlying to sit delta-neutral. Suppose the charm on each call is **−0.04 deltas per day** (OTM calls bleed delta as expiry nears).

Overnight, with **spot unchanged at 100**, time advances one day. Each call's delta drifts from 0.30 to roughly 0.26. The position delta falls from +30 to about **+26** — the book has *lost ~4 deltas* purely from the clock. The trader's short hedge of −30 is now oversized, leaving the book **−4 deltas short** at the open. To re-neutralise they must *buy back* ~4 units of the underlying before doing anything else. The closer to expiry, the larger this nightly bleed becomes — by the final session a comparable OTM book can shed a multiple of that each day, which is why short-dated option hedgers re-mark and re-hedge every morning as a matter of routine.

## Trading Implications

- **"Delta-neutral at the close" is not "delta-neutral at the open."** Charm guarantees drift overnight. Re-mark and re-hedge at the open rather than assuming yesterday's hedge still holds.
- **Wing inventory bleeds; core inventory builds.** Books heavy in OTM strikes ([[iron-condor|iron condors]], [[short-strangle|short strangles]]) see their directional exposure bleed toward zero, while ITM-heavy books see delta migrate toward ±1.
- **Short-dated positions are charm-dominated.** As `t → 0`, vega and [[vomma]] collapse while charm, speed, and color explode. Near expiry the real second-order risk is delta/gamma drift, not volatility convexity.
- **Calendar traders trade charm differentials** between the near and far legs, deliberately.
- **Risk limits.** Desks set charm budgets alongside delta, gamma, [[vanna]] and [[vomma]] limits so overnight drift is a planned hedging cost, not a surprise.

## False Signals and Pitfalls

- **Treating delta-neutral as risk-free overnight.** The single most common mistake — charm bleeds the hedge even on a frozen tape.
- **Vega-hedging a near-expiry position.** Spending money on vega/vomma protection in the last days ignores the dominant risk, which is charm- and speed-driven delta/gamma drift. See [[gamma-explosion]].
- **Ignoring the weekend.** Theta and charm accrue across non-trading days; a Friday hold can deliver a weekend's worth of delta drift in one step, surprising traders who only model trading days.
- **Sign confusion across moneyness.** Charm drains delta for OTM options but *adds* magnitude for ITM options — a mixed book can net to a small aggregate charm that hides large offsetting drifts on each side.

## Related

- [[second-order-greeks]] — the family charm belongs to
- [[vanna]] — delta's sensitivity to volatility (the sibling cross-Greek)
- [[vomma]] / [[volga]] — vega's convexity
- [[delta]] / [[theta]] — the first-order Greeks charm connects
- [[gamma]] — delta's sensitivity to spot (the other delta derivative)
- [[delta-neutral]] — the hedge state charm steadily erodes
- [[gamma-explosion]] — why charm/speed/color explode near expiry
- [[0dte-trading]] — extreme charm effects in the final session
- [[dealer-gamma-hedging]] — how charm-driven re-hedging becomes market flow
- [[max-pain]] — expiration pinning that charm flows reinforce

## Sources

- Sheldon Natenberg, *Option Volatility and Pricing* — practitioner treatment of higher-order Greeks and dealer hedging (see [[book-option-volatility-and-pricing]]).
- John Hull, *Options, Futures, and Other Derivatives* — the mathematical definition of second-order partial derivatives of option value (see [[book-options-futures-other-derivatives]]).
