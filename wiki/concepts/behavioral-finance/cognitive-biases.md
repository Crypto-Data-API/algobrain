---
title: "Cognitive Biases"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [behavioral-finance, psychology, risk-management]
aliases: ["Cognitive Biases", "Cognitive Bias", "Decision Biases", "Heuristics and Biases"]
domain: [behavioral-finance]
prerequisites: ["[[behavioral-finance]]"]
difficulty: beginner
related: ["[[behavioral-finance]]", "[[loss-aversion]]", "[[confirmation-bias]]", "[[anchoring-bias]]", "[[overconfidence-bias]]", "[[disposition-effect]]", "[[prospect-theory]]", "[[framing-effects]]", "[[trading-psychology]]", "[[herding]]", "[[recency-bias]]"]
---

Cognitive biases are systematic, predictable errors in human judgment that arise from the brain's reliance on mental shortcuts (heuristics) to process information quickly under uncertainty. In trading they are the root cause of most discretionary mistakes: they cause investors to misweight evidence, mis-estimate probabilities, and let emotion override their plan. Because they are systematic rather than random, they both endanger the undisciplined trader and create exploitable inefficiencies in aggregate market behavior.

## Overview

The modern study of cognitive biases originates with the "heuristics and biases" research program of [[daniel-kahneman]] and Amos Tversky in the 1970s, later popularized in Kahneman's *Thinking, Fast and Slow* (Source: [[book-thinking-fast-and-slow]]). Kahneman frames the mind as two systems: **System 1** (fast, automatic, intuitive, emotional) and **System 2** (slow, deliberate, analytical, effortful). Biases arise when System 1 produces a quick answer that System 2 fails to check. Markets are an adversarial environment that punishes System-1 errors with real money, which is why bias management is a core trading skill rather than an academic curiosity.

A heuristic is not inherently bad — shortcuts are evolutionarily efficient and usually adequate. A bias is the *systematic* error a heuristic produces in a context (like probabilistic financial decisions) for which the shortcut was never optimized.

## Categories of Bias Relevant to Trading

### Biases of belief and information processing
- **[[confirmation-bias]]** — seeking and over-weighting evidence that supports an existing position; ignoring disconfirming data.
- **[[anchoring-bias]]** — fixating on a reference value (entry price, a round number, an analyst target) and adjusting insufficiently from it.
- **[[recency-bias]]** — over-weighting recent outcomes; assuming the last few trades or the current regime will persist.
- **Hindsight bias** — believing, after the fact, that an outcome was predictable ("I knew that crash was coming"), which corrupts the feedback loop and inflates confidence.
- **Narrative fallacy** — constructing a coherent causal story from what is mostly noise, then trading the story.

### Biases of probability and risk
- **[[loss-aversion]]** — losses hurt roughly twice as much as equivalent gains feel good (the asymmetry at the heart of [[prospect-theory]]).
- **[[framing-effects]]** — the same decision is evaluated differently depending on whether it is framed as a gain or a loss.
- **Availability heuristic** — judging probability by how easily examples come to mind, so vivid recent events (a crash, a viral squeeze) are over-weighted.
- **Gambler's fallacy** — expecting reversion in independent random sequences ("red is due"); its mirror is the **hot-hand fallacy**.
- **Probability neglect / base-rate neglect** — ignoring the underlying base rate in favor of salient case-specific detail.

### Biases of self-assessment and action
- **[[overconfidence-bias]]** — overestimating the accuracy of one's forecasts and the size of one's edge; drives over-leverage and over-trading.
- **[[disposition-effect]]** — selling winners too early and holding losers too long (a behavioral consequence of loss aversion and anchoring).
- **Endowment effect** — over-valuing an asset simply because you own it.
- **Sunk-cost fallacy** — continuing a losing position to justify capital already committed.
- **[[herding]]** — deferring to the crowd rather than independent analysis, producing bubbles and panics.
- **Self-attribution bias** — crediting wins to skill and blaming losses on bad luck, which prevents learning.

## Trading Relevance

Cognitive biases matter to traders in two opposite directions:

1. **As hazards to defend against.** Nearly every classic trading mistake maps to one or more biases: revenge trading (loss aversion + self-attribution), refusing to cut a loser (disposition effect + sunk cost), chasing a parabolic move (herding + FOMO + recency), or over-sizing after a hot streak (overconfidence). The defense is structural, not willpower-based: written rules, pre-committed stops and targets, position-sizing limits, mechanical/[[algorithmic-trading|algorithmic]] execution, a [[trading-journal]], and reduced screen-checking frequency. Because biases operate through System 1, the only reliable counter is to make the correct action automatic *before* the emotional trigger fires.

2. **As exploitable edges.** Because biases are systematic across the crowd, they create persistent market patterns that strategies harvest. The [[momentum]] and [[post-earnings-announcement-drift]] effects are partly driven by under-reaction and the disposition effect; [[mean-reversion]] and [[contrarian-extremes|contrarian]] strategies exploit herding and over-reaction at sentiment extremes; [[volatility-risk-premium|short-vol]] premiums persist partly because of loss aversion to tail events. Quantitative and systematic traders deliberately remove their own biases from execution while positioning to collect the premium left behind by everyone else's.

A practical principle from Kahneman: it is extremely hard to debias your own in-the-moment judgment, but much easier to design an environment and a process that prevents the bias from acting. Good [[risk-management]] is, in large part, applied bias management.

## Related

- [[behavioral-finance]] — the field that studies these biases in markets
- [[prospect-theory]] — the formal model behind loss aversion and framing
- [[loss-aversion]], [[confirmation-bias]], [[anchoring-bias]], [[overconfidence-bias]], [[disposition-effect]], [[framing-effects]] — individual biases
- [[trading-psychology]] — practical management and discipline
- [[herding]] — crowd-driven bias and its market effects
- [[risk-management]] — structural defenses against bias

## Sources

- [[book-thinking-fast-and-slow]] — Kahneman's synthesis of the heuristics-and-biases program, System 1 / System 2, and the major biases.
- Tversky, A. & Kahneman, D. (1974) "Judgment under Uncertainty: Heuristics and Biases," *Science* 185:1124-1131 — foundational paper.
- Nickerson, R. (1998) "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises," *Review of General Psychology* — on the most damaging trading bias.
