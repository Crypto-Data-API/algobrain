---
title: "Ole Peters"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [person, risk-management, portfolio-theory, behavioral-finance]
aliases: ["Ole B. Peters", "O. Peters"]
entity_type: person
website: "https://ergodicityeconomics.com"
related: ["[[ergodicity]]", "[[ergodicity-economics]]", "[[geometric-mean]]", "[[kelly-criterion]]", "[[murray-gell-mann]]", "[[nassim-taleb]]", "[[fat-tails]]", "[[negative-skew]]", "[[long-vol-vs-short-vol]]", "[[gaussian-assumption]]"]
---

Ole Peters is a theoretical physicist and the principal developer of **[[ergodicity-economics|ergodicity economics]]** -- a research program that re-derives the foundations of decision theory under non-ergodic wealth dynamics. He is a Fellow at the London Mathematical Laboratory (LML) and an External Professor at the Santa Fe Institute. His most cited work, *"The ergodicity problem in economics"* (*Nature Physics*, 2019), argues that 250 years of economics has been computing the wrong average for wealth dynamics, and that maximizing the **time-average growth rate** -- rather than the expected value -- reproduces real-world risk preferences without invoking psychological biases.

## Background

Peters trained as a physicist (Imperial College London, PhD), with a research background in non-equilibrium statistical mechanics and stochastic processes. He moved into economics through his collaboration with Nobel laureate physicist **Murray Gell-Mann** at the Santa Fe Institute, where the two co-developed the formal framework for evaluating gambles using dynamics rather than ensemble averages.

Peters is based at the **London Mathematical Laboratory (LML)**, an independent research institute. He runs the LML's ergodicity-economics research stream, including the regularly updated lecture notes (with Alexander Adamou) that serve as the program's de facto curriculum. He is also affiliated with the Santa Fe Institute as an External Professor and has held visiting positions at Imperial College London.

He is not an academic economist by training, which is part of the point: the ergodicity-economics critique came from outside the discipline and was initially ignored by it. The program has since gained traction with practitioners ([[nassim-taleb|Taleb]], [[mark-spitznagel|Spitznagel]], several systematic-fund risk teams) ahead of mainstream academic economics.

## Key Ideas

The core program (see [[ergodicity-economics]] for full treatment) rests on a few simple observations whose consequences cascade through decision theory:

1. **Wealth dynamics are typically multiplicative.** Returns compound; one period's wealth is the previous period's wealth times `(1 + r)`.
2. **Multiplicative dynamics are non-ergodic.** The ensemble average grows at the arithmetic mean rate; the time average grows at the geometric mean rate. They are different numbers.
3. **A single investor's wealth follows the time average.** No real investor experiences the ensemble average -- that would require running parallel universes.
4. **Maximize the time-average growth rate**, not expected value or expected utility.
5. **Risk aversion, insurance, and diversification fall out as theorems**, not behavioral biases. Standard economics' "anomalies" are mostly the correct response to non-ergodicity.
6. **Leverage has an optimum**, not a maximum: above the optimum, expected log-growth turns negative even though arithmetic expected return is still positive.

The mathematical centerpiece is the demonstration that for a multiplicative process with i.i.d. returns of arithmetic mean μ and variance σ², the time-average growth rate is approximately:

```
g ≈ μ - 0.5 * σ^2
```

The variance drag (`0.5 σ^2`) is the formal mechanism by which compounding strategies with high volatility silently lose. This same identity is the foundation of the [[kelly-criterion|Kelly criterion]] and is why fractional Kelly outperforms full Kelly in practice.

## Notable Papers

- **Peters, Ole (2019). "The ergodicity problem in economics."** *Nature Physics* 15, 1216-1221. The flagship paper of the program. Appearing in *Nature Physics* (rather than an economics journal) is itself part of the disciplinary story. The paper compresses two decades of work into a perspective article and is the standard citation.

- **Peters, Ole and Gell-Mann, Murray (2016). "Evaluating gambles using dynamics."** *Chaos* 26, 023103. The technical foundation: how to evaluate a gamble by computing the time-average growth rate it induces, rather than its ensemble expected value.

- **Peters, Ole and Klein, William (2013). "Ergodicity breaking in geometric Brownian motion."** *Physical Review Letters* 110, 100603. Demonstrates rigorously that geometric Brownian motion -- the standard model of asset prices in [[black-scholes|Black-Scholes]] -- is non-ergodic, and quantifies the divergence between ensemble and time averages.

- **Peters, Ole and Adamou, Alexander (2018). "The time interpretation of expected utility theory."** LML working paper. Argues that Bernoulli's logarithmic utility resolution to the St. Petersburg paradox is numerically correct but conceptually misattributed: the log function describes the *correct average* of multiplicative dynamics, not a psychological preference.

- **Adamou, Alexander and Peters, Ole (2016). "Dynamics of inequality."** *Significance* 13(3), 8-13. Applies the framework to wealth inequality dynamics, deriving the well-documented "rich-get-richer" effect from non-ergodic multiplicative dynamics rather than from political or behavioral causes.

- **LML Ergodicity Economics lecture notes** (Peters and Adamou, continuously updated). The standard practitioner-accessible curriculum, freely available via the LML website.

## Influence

Within the practitioner community, Peters's work has had outsized influence on the design of risk-management frameworks for non-ergodic strategies:

- **[[nassim-taleb|Nassim Taleb]]** explicitly cites and integrates Peters's work in *Skin in the Game* (2018), particularly Chapter 19. Taleb's earlier ergodicity discussions in *Fooled by Randomness* and *The Black Swan* are now usually paired with the Peters-Gell-Mann formalism.
- **[[mark-spitznagel|Mark Spitznagel]]**'s argument for [[long-vol-vs-short-vol|long-vol overlays]] in *Safe Haven* (2021) -- that a small allocation to a convex tail hedge raises the geometric return of a combined book despite the hedge's negative arithmetic expectation -- is exactly the time-average vs. ensemble-average distinction in trading dress.
- **Risk teams at quantitative funds** increasingly use time-average growth rate (rather than Sharpe ratio or expected return) as a position-sizing criterion. The fractional-Kelly tradition was already there; ergodicity economics provides the formal underpinning.
- **Behavioral economics** has been reluctant to engage. Peters's claim that "prospect theory's anomalies are mostly artifacts of computing the wrong average" is a direct challenge to a Nobel-winning research program (Kahneman and Tversky). The two communities largely talk past each other; Peters's program has made more headway in finance than in academic behavioral economics.

His public-facing presence at **ergodicityeconomics.com** -- an active blog with worked examples, lectures, and software -- has been a significant accelerator. Peters writes accessibly, and the site has become an entry point for practitioners encountering the ideas for the first time.

## The Coin-Flip Demonstration

Peters's signature pedagogical example -- now widely cited -- is the multiplicative coin-flip game in which heads multiplies wealth by 1.5 and tails multiplies wealth by 0.6 (see [[ergodicity-economics]] for full worked example). The game has positive arithmetic expected return (+5% per round) but negative time-average growth rate (-5.3% per round). Played long enough, every individual trajectory ends near zero, while the cross-sectional ensemble mean grows. The example is the simplest demonstration of non-ergodicity in a way that maps directly onto leveraged trading strategies.

## Related

- [[ergodicity]] -- the underlying principle
- [[ergodicity-economics]] -- the research program he developed
- [[geometric-mean]] -- the metric his work elevates over arithmetic mean
- [[kelly-criterion]] -- a special case of his framework
- [[murray-gell-mann]] -- collaborator on the formal foundations
- [[nassim-taleb]] -- popularizer and integrator of Peters's program
- [[mark-spitznagel]] -- practitioner whose tail-hedge argument relies on the same logic
- [[long-vol-vs-short-vol]] -- direct trading-context application
- [[gaussian-assumption]] -- the failed model the program replaces

## Sources

- Peters, Ole (2019) "The ergodicity problem in economics" -- *Nature Physics* 15, 1216-1221.
- Peters, Ole and Gell-Mann, Murray (2016) "Evaluating gambles using dynamics" -- *Chaos* 26, 023103.
- Peters, Ole and Klein, William (2013) "Ergodicity breaking in geometric Brownian motion" -- *Physical Review Letters* 110, 100603.
- Peters, Ole and Adamou, Alexander -- LML Ergodicity Economics lecture notes (continuously updated, londonmathematicallaboratory.org).
- Taleb, Nassim. *Skin in the Game* (2018), Ch. 19 -- discussion of Peters's program in popular form.
- ergodicityeconomics.com -- Peters's own site, including the canonical coin-flip demonstration and worked examples.
- Affiliations (London Mathematical Laboratory; Santa Fe Institute External Professor) re-checked via Perplexity (sonar), 2026-06-10 -- no reported changes as of June 2026; the LML ergodicity-economics lecture notes and blog remain the active outlets.
