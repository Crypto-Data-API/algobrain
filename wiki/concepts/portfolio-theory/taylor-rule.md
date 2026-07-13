---
title: "Taylor Rule"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [macro, fundamental-analysis, interest-rates]
aliases: ["Taylor Rule", "taylor-rule", "Taylor Principle"]
domain: [portfolio-theory, fundamental-analysis]
prerequisites: ["[[monetary-policy]]", "[[inflation]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[monetary-policy]]", "[[interest-rates]]", "[[inflation]]", "[[federal-reserve]]", "[[recession]]", "[[stagflation]]", "[[top-down-macro-analysis]]", "[[yield-curve]]"]
---

The **Taylor Rule** is a monetary-policy formula, proposed by economist John B. Taylor in 1993, that prescribes how a central bank should set its short-term policy [[interest-rates|interest rate]] in response to deviations of [[inflation]] from its target and of output (or employment) from potential. It has become the standard benchmark against which actual [[federal-reserve|Fed]] policy is judged, and a widely-watched gauge of whether monetary policy is "too loose" or "too tight."

## The Formula

In its canonical form:

```
i = r* + π + 0.5(π − π*) + 0.5(y − y*)
```

where:
- **i** = the nominal target policy rate (e.g. the federal funds rate)
- **r\*** = the equilibrium ("neutral") real interest rate (Taylor's original paper assumed 2%)
- **π** = the current rate of inflation
- **π\*** = the inflation target (typically 2%)
- **(π − π\*)** = the inflation gap
- **(y − y\*)** = the output gap (percent deviation of real GDP from potential)

Taylor's original 1993 calibration used coefficients of **0.5** on both the inflation gap and the output gap. Substituting his assumptions (r\* = 2, π\* = 2):

```
i = 2 + π + 0.5(π − 2) + 0.5(output gap)
```

A key property is the **Taylor principle**: the coefficient on inflation in the *nominal* rate response must exceed 1 (here the total response to a 1-point rise in π is 1.5), so that the *real* rate rises when inflation rises. A real-rate response is what actually restrains demand; failing the Taylor principle (raising nominal rates less than one-for-one with inflation) lets real rates fall and inflation become self-reinforcing — a diagnosis some economists apply to the [[stagflation|stagflationary]] 1970s.

## Mechanics and Interpretation

- When inflation is **above target** or the economy is **above potential**, the rule prescribes a rate **above neutral** (contractionary).
- When inflation is **below target** or output is **below potential** (a [[recession|recession]] / negative output gap), it prescribes a rate **below neutral** (accommodative).
- The output gap is often replaced in practice by the **unemployment gap** (Okun's-law transformation), linking the rule to the Fed's dual mandate of stable prices and maximum [[unemployment|employment]].

Variants matter: the **"balanced-approach" rule** (Yellen-era) doubles the output-gap coefficient to 1.0; **inertial** versions add interest-rate smoothing; and the choice of inflation measure (core PCE vs. headline CPI) and of r\* substantially shifts the prescribed rate. Because r\* is unobservable and has likely fallen since the 1990s, modern estimates often use r\* closer to 0.5%.

## Trading and Portfolio Relevance

The Taylor Rule is a core input to [[top-down-macro-analysis|top-down macro analysis]] and rates trading:

- **Policy-gap signal** — when the actual funds rate sits far *below* the Taylor-implied rate, the market infers the Fed is "behind the curve," raising the odds of future hikes and steepening/inverting the [[yield-curve]]. The reverse signals room to cut.
- **Front-end positioning** — rates desks use Taylor-rule estimates (and the Atlanta Fed's published Taylor-rule utility) to fade or fade-into market-priced rate paths in SOFR/fed-funds futures.
- **Cross-asset read-through** — a hawkish Taylor gap pressures long-duration growth equities and supports the currency; a dovish gap is risk-on. It is one of the cleanest quantitative anchors for the "what are central banks doing?" question at Level 1 of the [[top-down-macro-analysis|macro framework]].
- **Limits** — the rule is a *benchmark*, not a commitment device. The Fed deviates deliberately (e.g. forward guidance, the 2020–2021 "average inflation targeting" overshoot), so the gap is a sentiment/expectations indicator rather than a forecast of the next move.

## Related

- [[monetary-policy]] — the broader policy framework the rule operationalizes
- [[interest-rates]] — the policy instrument it prescribes
- [[inflation]] — the primary input gap
- [[federal-reserve]] — the institution most often benchmarked against it
- [[recession]] — drives the output-gap term negative
- [[stagflation]] — the regime where the Taylor principle is most tested
- [[top-down-macro-analysis]] — where the rule fits in trade idea generation
- [[yield-curve]] — reflects expected future Taylor-implied paths

## Sources

- Taylor, J. B. (1993). *"Discretion versus Policy Rules in Practice."* *Carnegie-Rochester Conference Series on Public Policy* 39: 195–214.
- Taylor, J. B. (1999). *"A Historical Analysis of Monetary Policy Rules."* In *Monetary Policy Rules*, NBER/University of Chicago Press.
- Yellen, J. (2012). *"The Economic Outlook and the Conduct of Monetary Policy."* Federal Reserve speech (balanced-approach rule).
- Federal Reserve Bank of Atlanta — *Taylor Rule Utility* (interactive policy-rate calculator).
- Bernanke, B. (2015). *"The Taylor Rule: A Benchmark for Monetary Policy?"* Brookings Institution.
