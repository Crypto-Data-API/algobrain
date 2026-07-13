---
title: "Prospect Theory"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [behavioral-finance, risk-management, psychology]
aliases: ["loss aversion theory"]
domain: [behavioral-finance]
difficulty: intermediate
related: ["[[behavioral-finance]]", "[[loss-aversion]]", "[[risk-management]]", "[[daniel-kahneman]]", "[[book-thinking-fast-and-slow]]"]
---

Prospect theory is the descriptive model of decision-making under risk developed by **Daniel Kahneman** and **Amos Tversky** in 1979 and elaborated in *Thinking, Fast and Slow* (Source: [[book-thinking-fast-and-slow]]). It replaces the rational expected-utility framework of classical economics with a model that better fits how humans actually choose under uncertainty. Kahneman received the 2002 Nobel Prize in Economic Sciences for this work; Tversky had died in 1996. Prospect theory is the most empirically influential model in [[behavioral-finance]] and is essential context for any trader who wants to understand their own and others' decision biases.

## The Core Departures from Expected Utility

Classical expected utility theory says people choose between gambles by computing the probability-weighted average of outcomes' utilities, where utility is a smooth concave function of wealth. Prospect theory observes that real choices systematically violate this in three ways:

### 1. Reference Dependence

People do not evaluate outcomes in terms of final wealth — they evaluate them as **gains and losses relative to a reference point**. The reference point is usually the status quo, but it can be a recent peak, a purchase price, or an expectation. The same final wealth can feel like a gain or a loss depending on the frame.

### 2. Loss Aversion

**Losses loom roughly twice as large as equivalent gains.** Kahneman and Tversky's data suggested a coefficient of about 2.0 — the pain of losing $100 is about as intense as the pleasure of gaining $200. This asymmetry has nothing to do with marginal utility; it is a feature of how the mind weights outcomes.

### 3. Diminishing Sensitivity (S-shaped Value Function)

The value function in prospect theory is:
- **Concave in the gain domain** — risk-averse for gains
- **Convex in the loss domain** — risk-seeking for losses
- **Steeper for losses than for gains** — embodying loss aversion

The concrete implication: people prefer a sure $50 gain over a 50/50 shot at $100, but prefer a 50/50 shot at losing $100 over a sure $50 loss.

### 4. Probability Weighting

People do not use raw probabilities — they apply a **non-linear probability weighting function** that overweights small probabilities and underweights moderate to high ones. This explains the simultaneous popularity of lottery tickets (small chance of large gain) and insurance (small chance of large loss).

## Implications for Trading

### The Disposition Effect

Traders sell winners too early and hold losers too long. This is loss aversion plus diminishing sensitivity in action: a small gain feels worth locking in (concave gain region), while a paper loss feels worth gambling to recover (convex loss region). The disposition effect is one of the most robust empirical findings in behavioral finance and a primary reason that trading discipline must be rule-based rather than discretionary.

### Reference Point Anchoring

Many traders anchor on entry price as the reference point and treat the position as "winning" or "losing" relative to it. The market does not care about your entry. Position size, stop placement, and exit decisions should be based on current information, not on path-dependent emotional accounting.

### Risk-Seeking After Losses

Traders down on the day or month often increase position sizes or take lower-quality trades trying to "get back" — the convex loss-region behavior. This is the mechanism behind many blowup events in proprietary trading and is precisely why trading firms enforce drawdown-based position size cuts and circuit breakers.

### Skewed Bets

The probability-weighting overweighting of small probabilities is consistent with persistent demand for lottery-like assets (deep OTM options, penny stocks, certain crypto tokens) at prices that imply negative expected value. Sophisticated traders harvest this by selling lottery exposure (tail-risk insurance) or by avoiding the long side of skewed bets entirely.

### Designing Around Yourself

The most useful trading takeaway from prospect theory is humility about your own decision process. You will not stop being loss-averse or reference-dependent through willpower. The defenses are structural:

- **Pre-committed stop losses** placed at trade entry
- **Position-size discipline** independent of recent P&L
- **Mark-to-market accounting** that forces you to confront paper losses immediately
- **Outcome-blind process review** — judge decisions by quality at the time, not by results

## Related

- [[behavioral-finance]]
- [[loss-aversion]]
- [[disposition-effect]]
- [[risk-management]]
- [[cognitive-biases]]
- [[daniel-kahneman]]

## Sources

- (Source: [[book-thinking-fast-and-slow]]) — Kahneman's accessible exposition of prospect theory and its experimental foundations
