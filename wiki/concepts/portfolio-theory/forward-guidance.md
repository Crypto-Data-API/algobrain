---
title: "Forward Guidance"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [macro, market-regime]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[federal-reserve]]", "[[interest-rates]]"]
difficulty: intermediate
aliases: ["Forward Guidance", "Central Bank Communication", "Date-Based Guidance", "State-Contingent Guidance"]
related: ["[[fomc]]", "[[federal-reserve]]", "[[interest-rates]]", "[[fed-funds-futures]]", "[[yield-curve]]", "[[quantitative-easing]]", "[[us-treasury-bonds]]", "[[macroeconomics]]"]
---

Forward guidance is a monetary-policy tool whereby a central bank communicates the likely future path of policy — interest rates and balance-sheet actions — in order to shape market expectations *today*, without necessarily changing current policy. Because long-term rates, equity discount factors, and the [[us-dollar|currency]] all depend on the *expected* future path of short rates, credible guidance lets a central bank ease or tighten financial conditions through words alone. It became a primary tool when policy rates hit the zero lower bound (ZLB) after 2008 and again in 2020.

## Overview

The transmission logic rests on the expectations hypothesis of the [[yield-curve|term structure]]: a long-term yield is roughly the average of expected future short rates plus a term premium. If the [[fomc|FOMC]] can convince markets that the policy rate will stay low for years, long-term yields fall *now*, easing financial conditions even with the policy rate already at zero. Guidance also reduces uncertainty (and therefore risk premia) by narrowing the distribution of plausible policy paths. Its entire potency depends on **credibility** — guidance that the market does not believe, or that the central bank later abandons, damages the tool for future use.

## Types of Forward Guidance

- **Delphic guidance** — a forecast of what the central bank *expects* to do given its economic outlook (e.g., the [[fomc|SEP "dot plot"]]). It is informational, not a commitment.
- **Odyssean guidance** — a binding-style *commitment* to a policy path, even if conditions later argue otherwise, in order to "tie itself to the mast" and move expectations (the term references Odysseus binding himself against the Sirens).
- **Time/date-based guidance** — ties policy to a calendar (e.g., the Fed's 2011 statement that rates would stay low "at least through mid-2013").
- **State-contingent / threshold guidance** — ties policy to economic outcomes (e.g., the 2012 "Evans rule": near-zero rates until unemployment fell below 6.5% or inflation rose above 2.5%). Generally more robust than date-based because it self-adjusts to the data.

| Type | Form | Example | Strength | Weakness |
|------|------|---------|----------|----------|
| Delphic | Forecast / expectation | [[fomc|SEP dot plot]] | Honest about uncertainty | Easy to dismiss; not a commitment |
| Odyssean | Commitment to a path | "Lower for longer" pledges | Maximally moves expectations | Costly to credibility if abandoned |
| Date-based | Calendar trigger | 2011 "through mid-2013" | Simple, unambiguous | Rigid; can be wrong as data changes |
| State-contingent | Economic threshold | 2012 "Evans rule" | Self-adjusts to data | Harder for markets to price precisely |

## Mechanics and Market Impact

Forward guidance moves markets mainly through the **front and belly of the curve** — 2-to-5-year Treasury yields and the [[fed-funds-futures|fed funds futures]] / SOFR strip that price the expected policy path. A "hawkish surprise" (guidance for higher-for-longer rates than priced) lifts those yields, strengthens the dollar, and pressures long-duration equities; a "dovish surprise" does the reverse. Traders read guidance through the gap between the [[fomc|dot plot]] / statement language and what the futures curve already implies — the move is to the *unexpected component*, not the level. The 2013 "taper tantrum," when mere discussion of slowing [[quantitative-easing|QE]] spiked 10-year yields ~100 bps in months, is the canonical example of guidance (mis)communication moving markets violently.

### Why Words Move Long Rates — A Worked Example

The expectations hypothesis says a long yield is roughly the average of expected future short rates plus a term premium. Suppose the 1-year rate is expected to be **5%, 5%, 1%, 1%, 1%** over the next five years (the market expects the Fed to cut sharply after two years). Ignoring the term premium, the fair 5-year yield is the average:

```
(5% + 5% + 1% + 1% + 1%) / 5 = 2.6%
```

Now the FOMC issues *dovish* guidance — it signals the cuts will come a year earlier, so expectations shift to **5%, 1%, 1%, 1%, 1%**:

```
(5% + 1% + 1% + 1% + 1%) / 5 = 1.8%
```

The 5-year yield falls ~80 bps *with no change to today's policy rate*. That repricing eases financial conditions immediately: lower discount rates lift equity valuations and cheapen mortgages and corporate borrowing. The reverse holds for a hawkish surprise. This is the entire mechanism — guidance changes the *path* embedded in the average, and the curve reprices today.

## Trading and Portfolio Relevance

- **Duration positioning.** Guidance is the primary driver of the front end; rates traders position the 2s/5s and eurodollar/SOFR curve around expected shifts in the guided path rather than the spot rate decision.
- **Equity factor tilt.** Dovish "lower-for-longer" guidance lengthens the effective discount horizon, favouring long-duration growth and unprofitable-tech equities; hawkish guidance favours value and short-duration cash-flow.
- **Vol and event risk.** Guidance *changes* (regime shifts in the communication framework) are larger vol events than routine rate moves — see [[fomc]] for how this distorts the options surface. Credibility breaks (guidance abandoned under pressure) produce the sharpest repricings.
- **Carry and FX.** Divergence in guidance across central banks drives the cross-currency rate differential and therefore the carry trade and major FX pairs.

## How Traders Use This

- **Trade the surprise, not the headline.** Before each [[fomc|FOMC]] meeting, derive the market-implied path from [[fed-funds-futures]] / SOFR and the OIS strip; the tradeable edge is the *gap* between that and the statement, dots, and press conference. A "hold" can be hawkish or dovish depending on what was priced.
- **Map the reaction across the curve.** Guidance hits the front and belly hardest; position 2s/5s steepeners or flatteners and SOFR-strip trades rather than betting on the spot decision.
- **Rotate equity factors on the signal.** Dovish "lower-for-longer" guidance favours long-duration [[growth-stocks|growth]] and unprofitable tech; hawkish guidance favours [[value-investing|value]] and short-duration cash-flow names. See [[equity-duration]].
- **Pre-position vol.** The press conference and dot-plot release are scheduled vol events; the [[options|options surface]] embeds an FOMC-day "kink." Framework *changes* (not routine moves) are the largest repricings — keep dry powder for them.
- **Watch credibility.** The most violent moves come when guidance is *abandoned* under pressure (a credibility break), as in 2013's taper tantrum — these are regime shifts, not noise.

## Common Pitfalls

- **Reacting to the level instead of the surprise.** If the market already prices a dovish path, dovish guidance can sell off ("buy the rumour, sell the news"). Always benchmark against what was priced.
- **Confusing Delphic with Odyssean.** A *forecast* (dot plot) is not a *commitment*; treating projections as promises leads to mispriced conviction. Dots shift meeting to meeting.
- **Ignoring credibility risk.** Guidance only works while believed; a central bank that repeatedly walks back its words loses the tool, and markets stop responding (or overreact to reversals).
- **Single-curve tunnel vision.** Guidance moves the front end, FX, and equity factors simultaneously; trading only the rate leg ignores correlated, sometimes larger, cross-asset moves.
- **Over-reading every Fed speaker.** Individual member speeches are noisy relative to the committee's consensus statement; the durable signal is the statement, the dots, and the chair.

## Related

- [[fomc]] — the committee that issues US guidance (statement, dots, press conference)
- [[federal-reserve]] — the institution
- [[interest-rates]] — the variable being guided
- [[fed-funds-futures]] — where the market-implied guided path is priced
- [[yield-curve]] — the transmission channel via the term structure
- [[quantitative-easing]] — the balance-sheet tool guidance often accompanies
- [[macroeconomics]] — the broader macro framework

## Sources

- Federal Reserve — *Monetary Policy: Forward Guidance* (federalreserve.gov), and FOMC statements 2011–2020 (date-based and threshold guidance examples).
- Campbell, J., Evans, C., Fisher, J., & Justiniano, A. (2012) "Macroeconomic Effects of FOMC Forward Guidance" — *Brookings Papers on Economic Activity*. Source of the Delphic/Odyssean distinction.
- Woodford, Michael (2012) "Methods of Policy Accommodation at the Interest-Rate Lower Bound" — Jackson Hole symposium. Theoretical foundation for ZLB guidance.
- Bernanke, Ben (2020) "The New Tools of Monetary Policy" — AEA Presidential Address, *American Economic Review*. Retrospective on guidance and QE effectiveness.
