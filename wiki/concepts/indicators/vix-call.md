---
title: "VIX Call (Option)"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, volatility, vix, derivatives, indicators]
aliases: ["VIX Call", "VIX Call Option"]
related: ["[[vix]]", "[[vix-calls]]", "[[vix-futures]]", "[[vix-term-structure]]", "[[implied-volatility]]", "[[long-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[volatility-of-volatility]]", "[[options-greeks]]", "[[tail-risk-hedging]]", "[[long-put]]", "[[options-risk-budgeting]]"]
domain: [volatility, derivatives, indicators]
prerequisites: ["[[vix]]", "[[vix-futures]]", "[[options-greeks]]", "[[implied-volatility]]"]
difficulty: advanced
---

A **VIX call** is a single listed call option on the [[vix|CBOE Volatility Index (VIX)]]: a cash-settled, European-style derivative whose terminal payoff is `max(VRO - K, 0) × $100`, where VRO is the [[vix-soq|special opening quotation]] of the VIX on expiration morning and K is the strike. This page describes what a VIX call **is** as an instrument -- its contract specification, pricing model, and Greek behaviour. The strategy of buying VIX calls as a portfolio hedge is covered separately in [[vix-calls]].

The single most important fact about a VIX call is that **its underlying is not the spot VIX**. Spot VIX is not tradeable -- it is a 30-day forward implied vol synthesised from a strip of [[spx-options|SPX options]]. The economic underlying of a VIX call is the matching [[vix-futures|VIX futures contract]] expiring on the same date. Every Greek and every pricing intuition for VIX calls flows from this fact.

## Overview

VIX options were launched by the [[cboe|CBOE]] on 24 February 2006 and are now among the most heavily traded volatility instruments in the world. Average daily volume in VIX options exceeds 700,000 contracts; open interest routinely exceeds 13M contracts. They are used by:

- **Tail-risk hedgers** seeking convex protection against equity-crash regimes (see [[tail-risk-hedging]] and [[vix-calls]]).
- **Volatility-of-volatility traders** ([[volatility-of-volatility|vol-of-vol]]) trading the IV of VIX itself.
- **Term-structure traders** trading [[vix-term-structure]] via calendar/diagonal spreads.
- **Macro funds** expressing views on regime change.

A VIX call differs from an equity call in three fundamental ways: the underlying is a futures (not spot), settlement is cash (not deliverable shares), and the Greeks are non-standard because the underlying itself has term structure dynamics.

### VIX call vs. other tail-hedge instruments

| Instrument | Economic underlying | Payoff vs. equity crash | Carry in calm regime | Best for |
|---|---|---|---|---|
| **VIX call** | [[vix-futures\|VIX future]] of matching expiry | Convex, fast, large in a vol spike | Negative (roll-down + theta) | Acute, fast crash convexity |
| [[long-put\|SPX/SPY long put]] | Index spot | Convex, direct, decays with skew | Negative (theta + skew premium) | Direct portfolio floor |
| [[vix-futures\|Long VIX future]] | Itself (linear) | Linear, no convexity | Negative (contango roll) | Cheap directional vol view |
| [[put-spread-collar\|Put-spread collar]] | Index spot | Capped convexity, financed | Near-zero (call sale funds put) | Cost-conscious standing hedge |
| [[tail-risk-hedging\|Variance/vol swap]] | Realised variance | Direct realised-vol exposure | Negative (variance risk premium) | Institutional, OTC |

The VIX call's distinguishing trait is its **convexity per dollar of premium** in a fast spike: because vol-of-vol is high and VIX gaps in stress, an OTM VIX call can multiply several-fold in days. The cost is the steepest negative carry of any instrument in the table during quiet markets.

## Contract Specifications

| Field | Value |
|---|---|
| Underlying | VIX Index (cash-settled against VRO) |
| Exchange | [[cboe|Cboe Options Exchange]] |
| Symbol root | VIX (also weekly: VIXW) |
| Style | European (no early exercise) |
| Settlement | Cash, $100 multiplier |
| Standard expirations | Monthly, Wednesday closest to 30 days before the third Friday of the following calendar month |
| Weeklys (VIXW) | Wednesday weekly expirations |
| Trading hours | Regular: 9:30am-4:15pm ET; Global Trading Hours session 3:00am-9:15am ET |
| Last trading day | Tuesday before the Wednesday expiration |
| Settlement value | VRO -- a [[vix-soq|Special Opening Quotation]] of the VIX calculated at 9:30am ET on expiration Wednesday using opening prices of constituent SPX options |
| Strike intervals | $0.50 below 15, $1.00 above 15 |
| Tick size | $0.05 below $3.00; $0.10 above |
| Position limits | None (removed 2017) |

The Wednesday expiration is unusual and matters: a VIX call you hold "to expiration" stops trading at the close of the Tuesday before, then settles against an opening calculation Wednesday morning. The opening SPX option auction can produce a VRO that diverges materially from the prior-day spot VIX -- often by several points in a stress regime. This is the most-cited operational risk in the VIX-options product.

(Source: [[cboe-vix-options-specs]])

## Pricing & Greeks

### Pricing model

A VIX call cannot be priced using Black-Scholes on the spot VIX. Spot VIX is non-tradeable; you cannot construct a hedge that replicates the call's payoff using spot VIX. Instead, the standard approach is:

1. Identify the **VIX futures contract** that expires on the same date as the option (e.g. the May 2026 VIX option settles against the May 2026 VIX future).
2. Treat the futures price F as the underlying for a Black-76-style model.
3. Add a [[volatility-of-volatility|vol-of-vol]] surface to capture the IV of the futures itself.

This produces the canonical pricing identity:

```
VIX call price = Black76(F = VIX_future, K = strike, T, σ_volvol, r) × discount
```

where σ_volvol is the implied vol of VIX futures, *not* the spot VIX. As of 2025, σ_volvol on front-month VIX is typically 80-130% (yes, vol-of-vol is high -- VIX futures themselves move 5-15% on a typical day).

This is why a VIX call quoted at strike 25 with spot VIX at 14 can still be expensive: the matching futures might be at 19 (in [[contango]]), so the option is only 6 points out of the money on the actual underlying, not 11 points as the spot reading suggests.

### Greeks behave unusually

Because the underlying is a futures with term structure, VIX option Greeks are non-standard:

- **Delta** is measured against the futures price F, not spot VIX. A VIX call with "delta 0.40" gains $40 per $1 move in VIX *futures*, not in spot VIX. In a contango regime, spot VIX may rise 1 point while the relevant futures rises only 0.3 point -- the call gains 0.4 × 0.3 × $100 = $12, not $40.
- **Gamma** is high relative to equity options because vol-of-vol is high. A 1-point move in F can shift delta by 10-15%.
- **Vega** measures sensitivity to changes in vol-of-vol -- the IV of VIX futures, not the IV of SPX. A VIX call gains money when **realised volatility of the VIX itself** rises, not when SPX vol rises (though the two are correlated).
- **Theta** is high in absolute terms because vol-of-vol is high; a 30-DTE VIX call decays much faster than a 30-DTE SPX call of equivalent moneyness.
- **Rho** is small (the multiplier and short tenor make rate sensitivity minor).
- **The non-standard Greek**: roll/decay through the futures curve. Even with constant spot VIX, the relevant futures contract converges toward spot as expiration approaches (in a normal contango regime, F drops). This *roll-down* is a hidden negative carry that does not appear in standard Greek decomposition. See [[vix-roll-yield]].

### Greek interpretation cheat-sheet

| Greek | What it measures (for a VIX call) | Practical reading |
|---|---|---|
| Delta | Sensitivity to the matching **VIX future**, not spot VIX | "0.40 delta" = ~$40 per $1 move in *the future*; spot may move more or less |
| Gamma | How fast delta changes as F moves | High vs. equities — vol-of-vol amplifies; deltas reprice quickly in a spike |
| Vega | Sensitivity to **vol-of-vol** (IV of VIX futures) | Gains when the VIX itself becomes more volatile, not when SPX vol rises |
| Theta | Time decay | High in absolute terms; a 30-DTE VIX call bleeds faster than a 30-DTE SPX call |
| Rho | Rate sensitivity | Negligible (short tenor, small multiplier) |
| Roll/carry | Futures convergence toward spot through time | Hidden negative carry in [[contango]]; **not** in standard Greek output — see [[vix-roll-yield]] |

The critical takeaway: there is no single number that tells you "how much this call moves if VIX moves 1 point," because *which* VIX (spot vs. the relevant future) matters and the two decouple. Always quote and risk-manage against the future.

### The term-structure trap

The defining feature of VIX call pricing is the [[vix-term-structure|term-structure trap]]:

1. Spot VIX is at 14. The trader buys a VIX 25 call expiring in 60 days for $1.20.
2. Spot VIX rises to 18 over the next month -- a 29% increase.
3. The call has *not* moved much, perhaps to $1.40, because the relevant futures contract has only risen from 19 to 20 (futures in a flattening contango).
4. The trader expected a much larger response and is surprised.

The cure for this trap is to **always price VIX options against the futures, not spot**. A trader who watches spot VIX as their primary signal will systematically misjudge the position.

## Settlement Mechanics (VRO / SOQ)

VIX options settle to a Special Opening Quotation (the VRO ticker), computed using the *opening* prices of SPX options on expiration Wednesday morning. The settlement procedure:

1. At market open Wednesday (9:30am ET), an opening auction is run for the SPX options that feed the VIX calculation.
2. The opening prices of those SPX options are used in the standard VIX formula to produce a single VIX value: the VRO.
3. VIX calls settle to `max(VRO - K, 0) × $100` per contract.

The risk is that the opening SPX auction can produce a VRO that differs materially from prior-day spot VIX -- particularly during overnight news. Empirical examples include 2018-02-06 (post-volmageddon), 2020-03-09 (COVID-era opening prints), and the August 2024 yen carry-unwind morning. Traders have observed VRO prints 4-8 points away from prior-day spot VIX in such regimes. A trader holding deep-OTM VIX calls into expiration is making an explicit bet on the *VRO morning* and can be either rewarded or burned dramatically by the auction print. Best practice is to close VIX calls before the Tuesday close rather than carry to settlement.

(Source: [[cboe-vix-soq-methodology]])

## Use Cases

- **Tail-risk hedging** of long-equity portfolios -- the dominant use. See [[vix-calls]] for the full strategy.
- **Vol-of-vol arbitrage** -- relative-value trades between VIX option IV and a model fair value derived from realised VIX volatility.
- **Term-structure trades** -- calendar spreads (long back-month VIX call vs. short front-month VIX call) to express views on the slope of the [[vix-term-structure]].
- **Macro speculation** on regime change -- e.g., buying long-dated VIX calls before a major macro inflection point.
- **Hedging short-vol books** -- a [[short-strangle]] or [[iron-condor]] book on SPX is structurally short [[vega]]; a small position in OTM VIX calls converts the negative-skew profile to a less-negative one.

## Risks

- **Term-structure trap** -- buying based on spot VIX rather than the relevant futures, leading to consistent underperformance versus expectation.
- **VRO settlement gap** -- expiration Wednesday SOQ can differ materially from prior spot VIX.
- **Negative carry** -- in a normal contango regime, a continuously held VIX call program loses 5-15% per month to time decay and roll.
- **Mean reversion of VIX** -- a vol spike that the call captures may revert to baseline before the holder can monetise; speed of reaction matters.
- **Bid-ask spreads on OTM strikes** -- can be 10%+ of mid in calm regimes.
- **Liquidity asymmetry** -- VIX call liquidity dries up *fast* in stress regimes when everyone wants to buy and few want to sell. The product is most expensive when most needed.
- **No early exercise** -- the European style means a deep ITM call cannot be exercised early to lock in gains; it must be sold or carried.
- **Non-deliverable** -- cash settlement, no opportunity to take delivery of the underlying.

## Worked Example

**Setup**: 2026-04-15. Spot VIX = 14.5. May 2026 VIX futures (expiring 21 May) = 17.8. Trader buys 10x May VIX 22 calls at $0.85 each.

| Field | Value |
|---|---|
| Premium paid | 10 × $0.85 × $100 = $850 |
| Underlying | May VIX futures @ 17.8 (NOT spot 14.5) |
| Effective moneyness | (22 - 17.8) / 17.8 = 23.6% OTM on futures |
| Strike vs spot | (22 - 14.5) / 14.5 = 51.7% OTM on spot |
| DTE | 36 days |
| Per-contract delta (vs futures) | ~0.22 |
| Per-contract vega | ~$5 per vol-of-vol point |

**Outcome A -- Vol spike**: SPX falls 8% over a week. Spot VIX rises to 28; May VIX futures rise to 25.5. Calls now ~$4.20 each -- 10 × ($4.20 - $0.85) × $100 = +$3,350. The futures move (17.8 → 25.5 = +7.7) was much smaller than the spot move (14.5 → 28 = +13.5), but the call still profited because the futures did move past the strike.

**Outcome B -- Calm regime**: Spot VIX drifts to 13. May VIX futures drift down to 16 (roll-down toward spot). Calls now ~$0.20 each -- 10 × ($0.20 - $0.85) × $100 = -$650. Loss is large despite spot VIX barely moving, because (a) the futures dropped due to roll-down, and (b) theta + vol-of-vol decline dominated.

This example demonstrates the term-structure trap: in Outcome A, spot VIX nearly doubled but the call only quadrupled (not the 10-20x naive intuition would suggest); in Outcome B, spot VIX barely moved but the call lost three-quarters of its value to carry. VIX calls are about the futures, always.

*(All numbers above are illustrative, chosen to show the mechanics; they are not a backtest.)*

## Common Pitfalls

| Pitfall | Why it happens | Mitigation |
|---|---|---|
| Watching spot VIX as the signal | Spot is the headline number; the future is the underlying | Track the matching [[vix-futures\|future]] and [[vix-term-structure\|curve slope]] |
| Sizing to "spot doubling" intuition | Naive 1:1 spot-to-call mental model | Size to delta-vs-future and expected futures move |
| Carrying to the Wednesday SOQ | Assuming settlement ≈ prior spot | Close by Tuesday close unless the VRO bet is intentional |
| Continuous standing hedge with no budget | Negative carry compounds 5-15%/mo in [[contango]] | Run as a *budgeted* sleeve; ladder/roll deliberately ([[vix-roll-yield]]) |
| Buying convexity *after* the spike | Liquidity dries up and IV explodes when most wanted | Establish the hedge in calm regimes; pre-commit a budget |
| Confusing VIX vega with SPX vega | Vega here is vol-of-vol, not SPX IV | Separate the two in any multi-Greek budget ([[options-risk-budgeting]]) |

## Related

- [[vix]] -- the underlying index
- [[vix-calls]] -- the *strategy* of buying VIX calls (distinct from this concept page)
- [[vix-futures]] -- the actual economic underlying of VIX options
- [[vix-term-structure]] -- contango/backwardation drives VIX option pricing
- [[vix-soq]] -- the settlement mechanism
- [[volatility-of-volatility]] -- the IV input for VIX option pricing
- [[implied-volatility]] -- the broader volatility concept
- [[options-greeks]] -- standard Greeks (which behave non-standardly here)
- [[long-volatility-strategies]] -- sleeve-level use of VIX calls
- [[long-vol-vs-short-vol]] -- the structural framework
- [[tail-risk-hedging]] -- the primary use case
- [[long-put]] -- the alternative tail-hedge instrument
- [[options-risk-budgeting]] -- how a VIX call slots into a multi-Greek budget
- [[contango]] / [[backwardation]] -- the term-structure regimes

## Sources

- [[cboe-vix-options-specs]] -- product specification, last updated 2024.
- [[cboe-vix-soq-methodology]] -- settlement procedure documentation.
- [[book-trading-vix-derivatives]] (Russell Rhoads) -- canonical reference on VIX options pricing and term structure.
- [[book-option-volatility-and-pricing]] (Natenberg) -- general framework for futures-based option pricing.
- [[book-dynamic-hedging]] (Taleb) -- convexity and the role of vol-of-vol.
