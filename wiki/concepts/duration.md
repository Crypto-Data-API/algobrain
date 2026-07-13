---
title: "Duration"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [bonds, risk-management, volatility, indicators]
aliases: ["Duration", "Macaulay Duration", "Modified Duration", "Effective Duration", "Bond Duration", "DV01"]
related: ["[[interest-rate-risk]]", "[[bonds]]", "[[bond-market]]", "[[us-treasury-bonds]]", "[[yield-curve]]", "[[convexity]]", "[[move-index]]", "[[fed-funds-rate]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[bonds]]"]
difficulty: intermediate
---

Duration is the primary measure of a fixed-income security's price sensitivity to changes in interest rates. Expressed in years, it answers the practical question: *if yields move by 1%, roughly how much does this bond's price move?* It is simultaneously a measure of the weighted-average time to receive a bond's cash flows (Macaulay duration) and a first-order sensitivity (modified/effective duration). Because it linearizes the price-yield relationship, duration is the building block for hedging, immunization, and the most-watched bond-portfolio risk metric in fixed income.

## Overview

A bond's price is the present value of its future coupons and principal, discounted at the prevailing yield. When yields rise, every future cash flow is discounted more heavily, so price falls — and vice versa. Duration quantifies *how fast* price moves for a given yield change.

There are several related but distinct definitions:

### Macaulay Duration

The weighted-average time (in years) until the bond's cash flows are received, weighting each cash flow by its present value as a fraction of total price:

```
Macaulay Duration = Σ [ t × PV(CFₜ) ] / Price
```

A 10-year zero-coupon bond has a Macaulay duration of exactly 10 years (its single cash flow arrives at maturity). A 10-year coupon bond has a *shorter* duration than 10 years, because interim coupons return capital earlier.

### Modified Duration

The sensitivity measure derived from Macaulay duration, giving the approximate percentage price change per 1% (100 bp) change in yield:

```
Modified Duration = Macaulay Duration / (1 + y/k)

ΔPrice% ≈ −ModifiedDuration × Δyield
```

where `y` is the yield and `k` the compounding frequency. Example: a bond with modified duration of 7 loses ≈ 7% if yields rise 100 bp, and gains ≈ 7% if yields fall 100 bp.

### Effective Duration

For bonds with embedded options (callables, putables, MBS), cash flows themselves change as rates move, so the analytic formula breaks down. Effective duration is computed numerically by repricing the bond under small up/down yield shocks:

```
Effective Duration = (P₋ − P₊) / (2 × P₀ × Δy)
```

This is the duration measure used for [[mortgage-backed-securities]] and any optionable instrument.

### DV01 (dollar duration)

The dollar price change for a 1 bp yield move (`DV01 = ModifiedDuration × Price × 0.0001`). Traders hedge in DV01 terms so that the dollar P&L of a long and a short leg offset — the core of [[swap-spread-arbitrage]] and other rates trades.

## Convexity — the second-order term

Duration is a *linear* approximation; the true price-yield curve is convex. For large yield moves, duration alone understates gains when rates fall and overstates losses when rates rise. The correction term is [[convexity]]:

```
ΔPrice% ≈ −ModifiedDuration × Δy + ½ × Convexity × (Δy)²
```

Positive convexity is a benefit to the holder; callable bonds and MBS exhibit *negative* convexity, which is precisely why they carry yield premia.

## What drives duration

- **Maturity** — longer maturity ⇒ longer duration.
- **Coupon** — higher coupon ⇒ shorter duration (more cash returned early). Zero-coupon bonds have the longest duration for a given maturity.
- **Yield level** — higher yields ⇒ shorter duration.
- **Embedded options** — calls shorten duration as rates fall (the bond gets called away).

## Trading relevance

- **Interest-rate hedging.** Duration is the metric you neutralize. Matching the DV01 of a long bond position with a short futures or [[interest-rate-swap]] position immunizes a portfolio against parallel yield-curve shifts — see [[interest-rate-risk]].
- **Immunization.** Pension funds and insurers match asset duration to liability duration so that a rate move changes both sides equally, locking in a funding ratio.
- **Barbell vs bullet.** A barbell (short + long bonds) and a bullet (intermediate bonds) can share the same duration but differ in convexity — a positioning lever used in [[barbell-portfolio]] and [[macro-relative-value]] trades.
- **Equity duration.** The concept extends to stocks: high-multiple growth names behave like long-duration assets because their value sits in distant cash flows, so they sell off hardest when discount rates rise. This is the link between rate moves and P/E compression.
- **Volatility of duration risk.** Aggregate Treasury-market rate volatility is tracked by the [[move-index|MOVE index]], the bond-market analogue of the VIX.
- **Bank balance-sheet risk.** Borrowing short and lending long is a duration mismatch; the 2023 US regional-bank failures (e.g. Silicon Valley Bank) were a duration-risk event — long-duration bond holdings cratered as the [[fed-funds-rate]] rose.

## Worked example

A 10-year Treasury with a 4% coupon, priced at par, has a modified duration of roughly 8.1 and convexity around 80. If the [[yield-curve|10-year yield]] rises 50 bp:

```
Duration term:  −8.1 × 0.0050      = −4.05%
Convexity term: +0.5 × 80 × 0.0050² = +0.10%
Estimated price change ≈ −3.95%
```

The convexity term cushions the loss slightly — and would *add* to the gain on a rate fall.

## Limitations

- Captures only **parallel** yield-curve shifts; non-parallel moves (steepening/flattening) need key-rate (partial) durations.
- Linear by construction — must be paired with convexity for large moves.
- For optionable bonds, only effective duration is meaningful, and it shifts as rates move.

## Related

- [[interest-rate-risk]] — the risk that duration measures
- [[convexity]] — the second-order correction to duration
- [[bonds]] · [[bond-market]] · [[us-treasury-bonds]] — the instruments
- [[yield-curve]] — the term structure duration is computed against
- [[move-index]] — implied volatility of rates
- [[barbell-portfolio]] — duration-equivalent, convexity-different construction

## Sources

- Fabozzi, *Bond Markets, Analysis, and Strategies* (standard fixed-income reference on Macaulay/modified/effective duration and convexity).
- Hull, *Options, Futures, and Other Derivatives* — duration and DV01 hedging (see [[book-options-futures-other-derivatives]]).
- CFA Institute curriculum, Fixed Income readings on duration and convexity.
