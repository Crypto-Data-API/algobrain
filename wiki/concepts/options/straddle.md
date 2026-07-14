---
title: "Straddle"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, derivatives, volatility, indicators]
aliases: ["Straddle"]
related: ["[[long-straddle]]", "[[strangle]]", "[[iron-butterfly]]", "[[volatility-trading]]", "[[long-volatility-strategies]]", "[[short-volatility-strategies]]", "[[delta]]", "[[vega]]", "[[theta]]"]
domain: [options]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
---

A **straddle** is a two-legged options structure consisting of a call and a put on the same underlying, with the same strike price and the same expiration date. The position is a pure expression of a view on volatility relative to what the market has priced in: the long version profits if realized volatility exceeds the implied volatility paid; the short version profits if realized volatility comes in below the implied volatility received.

This page is the conceptual umbrella covering both directions of the structure. For the standalone strategy mechanics of the long variant, see [[long-straddle]]. For the same-strike cousin with different strikes, see [[strangle]]. For the spread version, see [[iron-butterfly]].

## Definition

A straddle is constructed from two simultaneous options trades on the same underlying:

- **One call** at strike K expiring at T
- **One put** at strike K expiring at T

Both legs use the **same strike (K)** and **same expiration (T)**. The strike is typically chosen at-the-money (ATM), meaning K is approximately equal to the current spot price S. This makes the structure roughly delta-neutral at inception — the +0.5 delta of the ATM call is offset by the -0.5 delta of the ATM put.

The total premium of the structure equals the sum of the call premium and put premium. Because both legs are ATM, the straddle premium is approximately equal to the market's expected absolute price move over the period (a result that follows from the Black-Scholes ATM approximation).

## Long Straddle vs Short Straddle

The two variants of a straddle are mirror images:

| Aspect | Long straddle | Short straddle |
|---|---|---|
| Position | Buy call + buy put | Sell call + sell put |
| Volatility view | Long volatility (expect realized > implied) | Short volatility (expect realized < implied) |
| Max loss | Premium paid | Theoretically unlimited |
| Max gain | Theoretically unlimited | Premium received |
| Breakeven (per side) | K +/- total premium | K +/- total premium |
| Profit zone | Outside the breakevens | Between the breakevens |
| Margin | Low (debit paid upfront) | High (undefined risk) |

The long straddle is a **defined-risk, undefined-reward** trade. The short straddle is the opposite — **defined-reward, undefined-risk** — and is usually capped in practice by margin requirements rather than by trader choice.

## Greek Profile

The Greeks of a straddle are a stacked combination of its two legs. The signs flip cleanly between the long and short variants:

| Greek | Long straddle | Short straddle | Comment |
|---|---|---|---|
| [[delta]] | ~0 at inception | ~0 at inception | ATM call's +0.5 cancels ATM put's -0.5 |
| Gamma | Positive | Negative | Largest at-the-money; concentrates as expiry approaches |
| [[vega]] | Positive | Negative | Both legs gain on IV rises (long); both lose (short) |
| [[theta]] | Negative | Positive | Both legs decay; long pays, short collects |
| Rho | Mixed | Mixed | Small in normal regimes |

The two profiles describe opposite trades on the same underlying engine. A long straddle is "I am paying theta in exchange for the right to harvest gamma if the underlying moves and to harvest vega if implied vol expands." A short straddle is the inverse: "I am collecting theta in exchange for taking on negative gamma and negative vega."

## When to Use Each Variant

### Long straddle

Use a long straddle when:

- A binary catalyst (earnings, FDA decision, central-bank meeting, M&A vote) is approaching and **implied vol underprices the realized move** historically delivered
- IV rank is low and there is a fundamental reason to expect a vol expansion (often pre-event, before crowd buying inflates premium)
- The trader has a directional uncertainty but high conviction in *magnitude* — they expect a big move but cannot predict the direction
- A position is needed to express a long-vol overlay on a portfolio (see [[long-volatility-strategies]])

The structural problem with the long straddle is timing: theta decay accelerates as expiration approaches, and IV often crushes after the catalyst event. Pre-event entry is typically too late if the crowd has already bid up the premium.

### Short straddle

Use a short straddle when:

- IV rank is elevated (often post-event) and likely to revert toward realized vol
- The underlying is range-bound with no expected catalyst
- The trader has portfolio margin and the discipline to manage the unbounded risk

Short straddles are the backbone of many systematic premium-selling programs but are catastrophically exposed to gap moves. They are typically run delta-hedged or as iron butterflies (see below) to bound the risk.

## Differences vs Strangle

A **[[strangle]]** is structurally similar but uses **different strikes** for the call and the put:

- **Long strangle** — buy OTM call (strike K_c > S) + buy OTM put (strike K_p < S)
- **Long straddle** — buy ATM call + buy ATM put (K_c = K_p = S)

The trade-offs:

| Dimension | Straddle | Strangle |
|---|---|---|
| Premium cost | Higher (ATM is most expensive) | Lower (OTM legs cheaper) |
| Breakeven distance | Smaller move needed | Larger move needed |
| Max gamma | Higher (concentrated at K) | Spread across two strikes |
| Implied move pricing | Exactly the ATM straddle = expected move | Approximation only |
| Probability of profit (long) | Lower | Higher distance, lower probability |

Practitioners often prefer strangles when they want cheaper exposure and are willing to demand a larger move; they prefer straddles when they want maximum gamma concentration at a known catalyst price.

## Differences vs Iron Butterfly

An **[[iron-butterfly]]** is a *spread version* of the short straddle. Where the short straddle is naked on both legs, the iron butterfly adds protective long wings:

- **Short straddle**: short ATM call + short ATM put (naked, undefined risk)
- **Iron butterfly**: short ATM call + short ATM put + long OTM call + long OTM put (defined risk, defined reward)

The iron butterfly caps the upside (max gain = net credit) and caps the downside (max loss = wing width minus credit). Margin requirements drop dramatically because the position is risk-defined. The trade-off is that the long wings cost premium, so the credit collected is smaller than for the naked short straddle.

For most retail traders and risk-budgeted books, the iron butterfly is the practical implementation of the "short straddle" view because the unbounded risk of the naked structure is rarely acceptable.

## Related

- [[long-straddle]] — the standalone long-variant strategy page
- [[strangle]] — same volatility view, different strikes
- [[iron-butterfly]] — risk-defined version of the short straddle
- [[volatility-trading]] — the parent discipline
- [[long-volatility-strategies]], [[short-volatility-strategies]] — the strategy buckets
- [[delta]], [[vega]], [[theta]] — the dominant Greeks for straddle structures
- [[implied-volatility]] — what the straddle premium prices
- [[volatility-risk-premium]] — why short straddles have a long-run edge in calm regimes

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — chapters on straddles, strangles, and butterfly spreads.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — Greek profile and volatility-based usage.
- CBOE educational materials on straddle vs strangle vs butterfly structures.
