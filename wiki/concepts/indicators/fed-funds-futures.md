---
title: "Fed Funds Futures"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [futures, indicators, bonds]
aliases: ["Fed Funds Futures", "Federal Funds Futures", "30-Day Fed Funds Futures", "ZQ", "FedWatch"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[fed-funds-rate]]", "[[futures]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[fed-funds-rate]]", "[[fomc]]", "[[forward-guidance]]", "[[federal-reserve]]", "[[monetary-policy]]", "[[yield-curve]]", "[[interest-rate-options]]", "[[treasury-bonds]]", "[[sofr]]", "[[nowcasting]]", "[[interest-rates]]", "[[economic-indicators]]"]
---

**Fed funds futures** are exchange-traded contracts on the average daily [[fed-funds-rate|federal funds rate]] over a calendar month. Listed on the CME (ticker **ZQ**), they are the market's purest, most-watched gauge of where traders expect US [[monetary-policy]] to go: the prices embed a probability-weighted forecast of upcoming [[fomc|FOMC]] decisions, and they are the raw material behind the widely-cited **CME FedWatch** rate-move probabilities. They are stock-market relevant because the implied policy path drives the [[risk-free-rate|risk-free]] discount rate underlying every equity valuation.

## Contract Mechanics

- **Underlying:** the simple arithmetic average of the daily effective federal funds rate (EFFR), as published by the Federal Reserve Bank of New York, over the contract's delivery month.
- **Quotation:** price = **100 − (average daily fed funds rate for the month)**. A contract priced at 94.75 implies an average rate of **5.25%** for that month.
- **Notional:** based on $5,000,000 face value of 30-day fed funds, so a **1 basis point** change in the implied rate is worth about **$41.67** per contract ($5,000,000 × 0.0001 × 30/360).
- **Settlement:** cash-settled at month end against the realised monthly average EFFR — there is no physical delivery.
- **Listing:** consecutive months are listed far enough out to cover the next several FOMC meetings, so each meeting's expected outcome can be read off the relevant contract(s).

Because the contract settles to a *monthly average*, a contract whose month contains an FOMC meeting prices a *blend* of the rate before and after the decision — a fact that matters when extracting probabilities (below).

## Reading Market Expectations

The implied average rate for a month is simply `100 − price`. Comparing the implied rate across consecutive contracts shows the path the market expects policy to follow. For a meeting that falls mid-month, the implied move is backed out by accounting for how many days of the month sit at the old rate versus the new rate.

### Extracting a hike/cut probability (FedWatch logic)

The CME FedWatch tool formalises this. In simplified form, for a meeting and a current target midpoint:

```
Implied rate after meeting = (month-average implied rate, adjusted for the
                              days before vs after the meeting date)

P(rate change) = (Implied rate after meeting − Current rate)
                 ÷ (Size of the assumed change, e.g. 0.25%)
```

**Worked example (illustrative):** the current target midpoint is 5.00%. The fed funds future for a month containing an FOMC meeting near the start of the month implies a post-meeting average rate of roughly 4.94%. That 6 bp of "average" easing, scaled against a full 25 bp cut, implies a market-assigned probability of about **24%** that the Fed cuts 25 bp at that meeting, and ~76% that it holds. (Real FedWatch math is more careful about the exact meeting date and day-count, but the intuition is this proportion.)

The headline insight matches the [[fed-funds-rate]] page: **what is already priced is in the market**. Edge around an FOMC meeting comes from a differentiated view of the *path* versus what the futures already imply, not from the direction of the move itself.

## Uses

- **Gauging expectations.** The fastest read on whether a hike, cut, or hold is "priced in," and by how much — used by traders, the financial press, and even Fed officials as a measure of market sentiment versus the [[fomc|FOMC]] "dot plot."
- **Hedging.** Banks, money-market funds, and corporates hedge short-term funding costs against policy moves.
- **Expressing a rate view.** A trader who believes the Fed will cut faster than the market expects can buy fed funds futures (price rises as the implied rate falls); a more-hawkish-than-consensus view is expressed by selling.
- **Cross-checking other gauges.** Fed funds futures, overnight index swaps (OIS), and [[sofr|SOFR]] futures all imply a policy path; divergences between them flag funding-market stress or technical dislocations.

## Relationship to SOFR Futures

Since the post-2021 transition away from LIBOR, **[[sofr|SOFR]] futures** have become the deeper market for expressing views further out the curve, and 3-month SOFR futures now carry the bulk of rate-path open interest. Fed funds futures remain the cleanest instrument for the *very front end* — the next one or two FOMC meetings — because they reference the policy rate directly rather than a secured repo benchmark. The two are closely linked but not identical; the small, variable SOFR-EFFR spread is itself a watched funding indicator.

## Common Pitfalls

- **Confusing the contract with the rate.** Fed funds *futures* are a tradeable forecast; the [[fed-funds-rate|fed funds rate]] itself is the policy target the [[federal-reserve|Fed]] sets. This page is the former.
- **Ignoring the monthly-average settlement.** A meeting late in the month barely moves that month's contract, since most days still sit at the old rate. Use the *next* month's contract for the post-meeting rate.
- **Reading probabilities as forecasts.** Implied probabilities are risk-neutral, not real-world; they bake in a (usually small) risk premium and can be distorted near quarter-end funding pressures.
- **Treating it as a long-end signal.** Fed funds futures price the *short-rate path*; long [[treasury-bonds|Treasury]] yields are driven more by growth, inflation, and term premium and can move the opposite way.

## Related

- [[fed-funds-rate]] — the underlying policy rate this contract references
- [[fomc]] / [[forward-guidance]] — the decisions and communication the price anticipates
- [[federal-reserve]] / [[monetary-policy]] — the policymaker and toolkit
- [[sofr]] — the secured benchmark and its futures complement
- [[yield-curve]] — shaped by the expected short-rate path
- [[interest-rate-options]] — options layered on rate futures for convexity
- [[nowcasting]] — combining futures-implied paths with incoming data

## Sources

- CME Group — 30-Day Federal Funds futures (ZQ) contract specifications and the CME FedWatch Tool methodology (cmegroup.com).
- Federal Reserve Bank of New York — effective federal funds rate (EFFR) publication and reference-rate methodology, the contract's settlement basis.
