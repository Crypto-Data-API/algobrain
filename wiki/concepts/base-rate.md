---
title: "Base Rate"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [behavioral-finance, risk-management, backtesting]
aliases: ["Base Rate", "Base Rate Neglect", "Base Rate Fallacy", "Prior Probability"]
domain: [behavioral-finance]
prerequisites: ["[[probability]]", "[[expected-value]]"]
difficulty: intermediate
related: ["[[base-rate-neglect]]", "[[bayesian-inference]]", "[[expected-value]]", "[[probability]]", "[[representativeness-heuristic]]", "[[overconfidence-bias]]", "[[edge-taxonomy]]", "[[backtesting]]", "[[overfitting]]", "[[kelly-criterion]]", "[[confluence]]", "[[win-rate]]"]
---

A **base rate** is the unconditional, prior probability of an event in a reference population — the frequency of an outcome before any case-specific evidence is considered. In trading and forecasting, the base rate is the realistic odds of a setup working out *on average across many instances*, and the systematic failure to use it — **base-rate neglect** — is one of the most consequential cognitive biases in markets.

## The Concept

If 5% of all earnings-momentum signals historically led to a profitable trade after costs, then 5% is the base rate. When a trader evaluates a new signal, the rational estimate starts from that 5% prior and is updated by genuinely diagnostic, signal-specific evidence — the logic of [[bayesian-inference|Bayes' theorem]]:

```
P(win | evidence) = P(evidence | win) · P(win) / P(evidence)
```

Here P(win) is the base rate. People — including experienced traders — chronically discard it, anchoring instead on the vividness or plausibility of the specific story (the [[representativeness-heuristic|representativeness heuristic]]). This was the core finding of Kahneman and Tversky's research: when a description "sounds like" a category, subjects judge probability by similarity and ignore how common the category actually is.

### The Classic Illustration

The textbook example: a disease affects 1 in 1,000 people; a test is 95% accurate. A person tests positive — what is the chance they have the disease? Most people answer ~95%; the correct answer is about **2%**, because the rare base rate (0.1%) means false positives vastly outnumber true positives. The intuition that ignores the base rate is off by a factor of ~50.

Working it through on a population of 100,000 makes the trap concrete:

| Group | Count | Test result | Result count |
|-------|-------|-------------|--------------|
| Truly have disease (0.1%) | 100 | 95% test positive | **95** true positives |
| Truly healthy (99.9%) | 99,900 | 5% test positive (false alarm) | **4,995** false positives |
| **Total positives** | | | **5,090** |

P(disease | positive) = 95 / 5,090 ≈ **1.9%**. The test is "95% accurate," yet a positive result barely moves the odds — because the base rate is so low that the flood of false positives swamps the handful of true ones.

### A Trading-Flavoured Version

Apply the identical structure to a setup: a chart screen flags "high-probability breakouts," and historically only **10%** of flagged names actually follow through (the [[base-rate-neglect|base rate]]). The screen catches 80% of the real winners but also misfires on 20% of the eventual failures. Out of 1,000 flags:

| Group | Count | Flagged by screen | Flagged count |
|-------|-------|-------------------|---------------|
| Real follow-throughs (10%) | 100 | 80% caught | **80** |
| Failures (90%) | 900 | 20% misfire | **180** |
| **Total flags** | | | **260** |

P(follow-through | flagged) = 80 / 260 ≈ **31%** — better than the 10% base rate, but nowhere near the "high-probability" the label implies. The low base rate caps how good even a decent filter can be.

## Trading Relevance

Base-rate neglect shows up everywhere in markets and is a direct source of negative expected value:

- **Pattern recognition.** A chart pattern that "looks like" a breakout is traded as a high-probability event even though the base rate of breakouts following through after costs may be barely 50/50. Vivid setups override the unconditional odds.
- **Stock-picking narratives.** "This is the next Nvidia" ignores the base rate that the vast majority of small caps underperform and most "next-X" candidates fail. The reference-class outside view (how have similar companies/IPOs/turnarounds actually performed?) is the corrective.
- **Backtest evaluation.** When evaluating a strategy, the base rate of *published backtests that survive out-of-sample* is low; an impressive-looking equity curve should be discounted toward that grim prior (see [[backtesting]] and overfitting). This is reference-class forecasting applied to one's own research.
- **Forecasting and "expert" calls.** Pundit and analyst hit rates cluster near chance; the base rate of accurate macro calls is the right starting point, not the confidence with which a call is delivered (compounded by [[overconfidence-bias]]).
- **Position sizing.** Honest base rates feed directly into [[expected-value]] and the [[kelly-criterion]]; inflating perceived win probability above the true base rate leads to systematic over-sizing and elevated risk of ruin.

The professional discipline is to **take the outside view first**: identify the reference class, anchor on its base rate, and require strong, genuinely diagnostic evidence before deviating from it. An [[edge-taxonomy|edge]] is precisely a justified, evidence-backed departure from the base rate — not a story that ignores it.

## Illustrative Base Rates Traders Should Anchor On

These are *reference-class priors* to start from — directional reminders, not precise universal statistics. Verify with your own data before sizing.

| Reference class | Naïve / "story" estimate | Why the realistic base rate is lower |
|-----------------|--------------------------|--------------------------------------|
| A chart-pattern breakout following through | "It's obviously breaking out" | Many breaks are [[false breakout|false breakouts]]; net of costs the edge is often modest |
| "The next Nvidia" small-cap | "This 10×s" | The vast majority of small caps lag the index over time |
| A backtest surviving out-of-sample | "Look at this equity curve" | Most published/optimised backtests decay or fail live ([[overfitting]]) |
| A pundit's confident macro call | "They sound certain" | Aggregate expert hit-rates cluster near chance |
| An active fund beating its index over a decade | "Star manager" | A minority of funds beat their benchmark over long horizons after fees |

The point is not the exact number but the *direction of the correction*: vivid, specific stories almost always need to be discounted toward a humbler prior.

## How Traders Use It

- **Reference-class forecasting (the outside view).** Before judging a specific trade, ask: "Of all setups like this, how often do they actually work after costs?" Anchor there, then adjust for genuinely diagnostic specifics.
- **Calibrating [[win-rate|win rate]] inputs.** Feed *honest* base rates — not hopes — into [[expected-value]] and the [[kelly-criterion]]. Inflating perceived probability is the fastest route to systematic over-sizing and elevated risk of ruin.
- **Discounting your own research.** Treat an impressive backtest as a sample from a population of mostly-failing backtests; demand walk-forward and out-of-sample evidence before believing it.
- **Pre-mortem on narratives.** When a thesis "sounds like" a category (the [[representativeness-heuristic|representativeness heuristic]]), explicitly write down the base rate for that category as a counterweight.
- **Confluence with priors.** [[confluence|Confluence]] should *shift* you off the base rate via independent evidence — it never licenses ignoring the prior entirely.

## Common Pitfalls

- **Base-rate neglect.** The headline error — judging by vividness/similarity and discarding the prior (see [[base-rate-neglect]]).
- **The inside view.** Forecasting a specific case purely from its own details ("this turnaround is different") while ignoring how the reference class has historically performed.
- **Overconfidence compounding neglect.** [[overconfidence-bias]] makes traders both ignore the base rate *and* over-bet the deviation.
- **Cherry-picking the reference class.** Choosing a flattering comparison group ("compared to the best year ever...") to manufacture a higher prior. The class must be honestly representative.
- **Confusing test accuracy with predictive value.** As the disease and breakout examples show, a "95% accurate" signal can still be wrong most of the time when the base rate is low — accuracy ≠ P(true | positive).
- **Static priors.** Base rates can shift as regimes change; anchor on them but update with [[bayesian-inference|Bayesian]] discipline rather than treating them as permanent.

## Related

- [[base-rate-neglect]] — the bias of ignoring the prior probability
- [[bayesian-inference]] — the formal machinery for updating a base rate with evidence
- [[representativeness-heuristic]] — the mental shortcut that causes neglect
- [[probability]] — the foundation the base rate sits on
- [[expected-value]] / [[kelly-criterion]] — where honest base rates feed sizing
- [[win-rate]] — the trade-level statistic a base rate calibrates
- [[overconfidence-bias]] — compounds base-rate neglect
- [[edge-taxonomy]] — an edge is a justified departure from the base rate
- [[confluence]] — independent evidence that should *shift* the prior
- [[backtesting]] / [[overfitting]] — applying base rates to one's own research claims

## Sources

- Kahneman, D. & Tversky, A. (1973), "On the Psychology of Prediction," *Psychological Review* — base-rate neglect and representativeness.
- Daniel Kahneman, *Thinking, Fast and Slow* (2011) — inside vs outside view, reference-class forecasting.
- Bar-Hillel, M. (1980), "The Base-Rate Fallacy in Probability Judgments," *Acta Psychologica*.
- Philip Tetlock, *Superforecasting* (2015) — the discipline of anchoring forecasts on base rates.
