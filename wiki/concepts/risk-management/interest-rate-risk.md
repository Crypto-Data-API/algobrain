---
title: "Interest Rate Risk"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [risk-management, bonds, derivatives]
aliases: ["Interest Rate Risk", "interest-rate-risk", "rate risk", "Rate Risk", "duration risk"]
domain: [risk-management]
prerequisites: ["[[bonds]]", "[[duration]]"]
difficulty: intermediate
related: ["[[fed-funds-rate]]", "[[yield-curve]]", "[[duration]]", "[[bonds]]", "[[us-treasury-bonds]]", "[[interest-rate-swap]]", "[[value-at-risk]]"]
---

# Interest Rate Risk

Interest rate risk is the potential for investment losses arising from changes in interest rates. It most directly affects [[bonds]] and other fixed-income securities -- when rates rise, existing bond prices fall because their fixed coupons become less attractive relative to newly issued bonds at higher rates. The sensitivity of a bond's price to rate changes is measured by its [[duration]]; longer-duration bonds carry substantially more interest rate risk.

## Measuring Rate Sensitivity

The price-yield relationship is captured by two standard measures:

```
Modified duration:  %ΔPrice ≈ -ModDuration x Δyield
DV01 (dollar value of a basis point) = ModDuration x Price x 0.0001
```

- **[[duration|Duration]]** approximates the percentage price change for a 1% (100 bp) parallel shift in yields. A bond with modified duration of 7 loses roughly 7% if yields rise 1%.
- **DV01 / PV01** expresses the same sensitivity in dollars per 1 bp move — the workhorse metric for hedging a fixed-income book.
- **[[convexity|Convexity]]** is the second-order correction: duration alone overstates losses and understates gains for large moves, so long-convexity positions are favorable.

### Worked Example — The Duration Approximation

The first-order price change for a yield move is:

```
ΔP/P ≈ −ModDuration × Δy
```

**Example.** A 10-year Treasury with a modified duration of 8.5, priced at $100, when yields rise from 4.0% to 4.5% (Δy = +0.50% = +50 bp):

```
ΔP/P ≈ −8.5 × 0.0050 = −0.0425  → −4.25%
New price ≈ $100 × (1 − 0.0425) = $95.75
```

A 50 bp rise costs about 4.25% of the bond's value. On a $1,000,000 position, that is roughly a $42,500 mark-to-market loss. Equivalently, the **DV01** = ModDuration × Price × 0.0001 = 8.5 × $1,000,000 × 0.0001 = **$850 per basis point**, so 50 bp × $850 ≈ $42,500 — the two methods agree.

### Adding the Convexity Correction

For larger moves the linear estimate is too pessimistic on losses and too stingy on gains. The second-order formula adds a [[convexity|convexity]] term:

```
ΔP/P ≈ (−ModDuration × Δy) + (½ × Convexity × Δy²)
```

With Convexity = 90 and the same +50 bp move:

```
ΔP/P ≈ (−8.5 × 0.0050) + (0.5 × 90 × 0.0050²)
     ≈ −0.0425 + 0.001125
     ≈ −0.0414  → −4.14% (slightly less bad than duration alone implied)
```

Convexity always helps the holder of a positively-convex bond — it cushions losses when yields rise and adds to gains when yields fall. This asymmetry is why long-convexity positions (e.g. long options or long non-callable bonds) are prized, while callable bonds and mortgage-backed securities carry *negative* convexity that hurts holders in both directions.

The 2022–2023 episode showed the danger concretely: as the Fed raised the [[fed-funds-rate]] sharply, long-duration Treasuries fell ~30%+, and the unhedged duration mismatch in held-to-maturity bond portfolios was the proximate cause of the Silicon Valley Bank collapse in March 2023.

## Types of Interest Rate Risk

- **Price (market) risk** — the mark-to-market loss when rates rise, the focus above.
- **Reinvestment risk** — the risk that coupons and maturing principal must be reinvested at lower rates when rates fall (the mirror image of price risk).
- **[[yield-curve|Yield-curve]] / shape risk** — non-parallel shifts (steepening, flattening, twists) that [[duration]] alone, which assumes parallel moves, fails to capture. Managed with key-rate durations.
- **Basis risk** — the hedge instrument (e.g. Treasury futures) and the hedged asset (e.g. a corporate bond) do not move one-for-one, leaving residual exposure.
- **Optionality / negative-convexity risk** — embedded calls, prepayment (MBS), and caps/floors cause duration to shift adversely as rates move ("duration drift").

### Duration Sensitivity at a Glance

Approximate price change for a +100 bp parallel rise in yields (duration ≈ −% loss):

| Instrument (typical) | Modified duration | Approx. loss on +100 bp | Approx. gain on −100 bp |
|----------------------|-------------------|--------------------------|--------------------------|
| 3-month T-bill | ~0.25 | ~−0.25% | ~+0.25% |
| 2-year Treasury | ~1.9 | ~−1.9% | ~+1.9% |
| 10-year Treasury | ~8.5 | ~−8.5% | ~+8.5% (more, with convexity) |
| 30-year Treasury | ~19 | ~−19% | ~+19%+ |
| Long zero-coupon bond | ≈ maturity | very large | very large |

The takeaway: rate risk scales almost linearly with duration, and zero-coupon / long-maturity instruments carry the most. Shortening duration is the most direct lever to cut interest-rate risk.

## Equities and Cross-Asset Channels

Beyond fixed income, interest rate risk affects equities through multiple channels: higher rates increase companies' cost of capital, reduce the present value of future cash flows (especially damaging to growth stocks with earnings far in the future), and make risk-free alternatives like [[us-treasury-bonds|Treasuries]] more competitive with equities. Sectors such as utilities, REITs, and financials are particularly rate-sensitive.

## How Traders Hedge and Use It

Portfolio managers hedge interest rate risk through [[duration]] management (shortening duration when rates are expected to rise), [[interest-rate-swap|interest rate swaps]], Treasury futures, and diversification across asset classes with differing rate sensitivities. Common techniques:

- **DV01-matched futures hedge.** Match the DV01 of a long bond position with an offsetting short in liquid Treasury futures, neutralising parallel-shift risk while retaining the spread or [[carry-trade|carry]] view. *Hedge ratio = (portfolio DV01) ÷ (futures DV01).* If a portfolio has DV01 of $42,500 and the chosen future has DV01 of $85/contract, sell ≈ 500 contracts.
- **Duration targeting.** Run the book to a chosen duration (e.g. shorten to 2 ahead of a hiking cycle, extend to 10 to lock in yield before cuts) using cash bonds or futures.
- **Key-rate / curve hedges.** Hedge each bucket of the [[yield-curve]] separately (key-rate durations) to immunise against twists and steepeners, not just parallel moves.
- **Swaps and swaptions.** [[interest-rate-swap|Swaps]] convert fixed to floating (or vice versa); swaptions and caps/floors buy [[convexity]] and cap tail losses.
- **Immunisation / liability matching.** Pension and insurance books match asset and liability duration so a rate move hits both sides equally.

Traders monitor the [[yield-curve]] and central-bank policy ([[fed-funds-rate]], [[forward-guidance]]) because rate expectations drive not just bond prices but equity valuations, currency carry, and the discount rate underlying every risk asset (see [[us-debt]] for the supply side that also pushes yields).

## Common Pitfalls

- **Trusting duration for large moves.** Duration is a linear approximation; for big shocks you must add the [[convexity]] term or you will mis-size hedges. The error grows with the square of the yield move.
- **Assuming parallel shifts.** A single-number duration hedge leaves you exposed to steepeners, flatteners, and twists — the curve rarely moves in parallel. Use key-rate durations for real books.
- **Ignoring negative convexity.** Callable bonds and MBS *shorten* duration as rates fall (they get called/prepaid) and *extend* as rates rise — the worst of both worlds, and a classic source of hedging blow-ups.
- **Held-to-maturity accounting lulls.** Not marking duration risk to market (as in SVB's HTM book in 2023) hides the loss until a forced sale crystallises it — the risk is real even when unrealised.
- **Reinvestment blind spot.** Locking in a high coupon feels safe, but if rates fall, reinvesting coupons and principal at lower rates erodes the realised return — duration immunisation balances price and reinvestment risk at the horizon.
- **Stale hedge ratios.** DV01s drift as yields and time-to-maturity change; a hedge set and forgotten slowly de-matches. Re-balance the hedge as the book's DV01 moves.

## Related

- [[duration]] — the primary sensitivity measure
- [[convexity]] — the second-order correction
- [[bonds]], [[us-treasury-bonds]] — the instruments most exposed
- [[yield-curve]] — where shape risk lives
- [[fed-funds-rate]], [[forward-guidance]] — the policy drivers of rate moves
- [[interest-rate-swap]] — the core OTC hedging instrument
- [[value-at-risk]] — portfolio-level risk aggregation
- [[us-debt]] — Treasury supply as a structural driver of yields

## Sources

- Frank Fabozzi, *Bond Markets, Analysis, and Strategies* — standard reference on duration, convexity, and rate-risk measurement
- Federal Reserve / FDIC post-mortems on the 2023 Silicon Valley Bank failure — duration mismatch and unrealized bond losses
- CFA Institute curriculum, Fixed Income — duration, DV01, key-rate duration, and yield-curve risk
