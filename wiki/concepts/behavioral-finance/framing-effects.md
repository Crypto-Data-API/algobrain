---
title: "Framing Effects"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [behavioral-finance, psychology, risk-management]
aliases: ["Framing Effects", "Framing Effect", "Framing Bias"]
domain: [behavioral-finance]
prerequisites: ["[[prospect-theory]]", "[[loss-aversion]]"]
difficulty: beginner
related: ["[[prospect-theory]]", "[[loss-aversion]]", "[[cognitive-bias]]", "[[cognitive-biases]]", "[[behavioral-finance]]", "[[anchoring-bias]]", "[[disposition-effect]]", "[[daniel-kahneman]]", "[[trading-psychology]]"]
---

A framing effect is the [[cognitive-bias|cognitive bias]] whereby people reach different decisions about the *same* underlying choice depending on how it is described — most notably, whether an outcome is presented as a gain or as a loss. It is a direct consequence of [[prospect-theory]]: because the value function is concave for gains and convex (steeper) for losses, identical economic propositions trigger risk-averse behavior when framed positively and risk-seeking behavior when framed negatively. Framing is, in effect, [[loss-aversion]] weaponized by wording.

## Overview

Framing was demonstrated by [[daniel-kahneman]] and Amos Tversky in their classic "Asian disease problem" (Tversky & Kahneman, 1981). Subjects chose between two programs to combat a disease expected to kill 600 people:

- **Gain frame:** Program A "saves 200 people"; Program B "1/3 chance of saving 600, 2/3 chance of saving none." Most people chose the certain gain (A) — they were *risk-averse*.
- **Loss frame:** Program C "400 people die"; Program D "1/3 chance nobody dies, 2/3 chance 600 die." Most people chose the gamble (D) — they were *risk-seeking*.

Programs A/C and B/D are mathematically identical. Only the wording — survivors vs deaths — changed, yet preferences reversed. This is the canonical proof that human choice is not invariant to description, violating a core axiom of rational expected-utility theory.

| | Gain frame ("saved") | Loss frame ("die") | Underlying maths |
|---|---|---|---|
| **Certain option** | A: save 200 — *most chose* | C: 400 die | 200 live / 400 die (identical) |
| **Gamble option** | B: 1/3 save 600, 2/3 save 0 | D: 1/3 none die, 2/3 all die — *most chose* | EV = 200 live (identical) |
| **Revealed attitude** | Risk-averse | Risk-seeking | Should be the same! |

The mechanism is the **reference point**. People do not evaluate final wealth states in the abstract; they evaluate *changes* relative to a reference point that the frame implicitly sets. Move the reference point and the same outcome flips from "gain" to "loss," and with it the risk attitude flips too. The gain frame anchors on "0 saved" so any survivors are a gain (and people lock in the sure gain); the loss frame anchors on "0 deaths" so any deaths are a loss (and people gamble to avoid the sure loss).

### Common Frames in Markets

| Same underlying fact | "Gain" / positive frame | "Loss" / negative frame |
|---|---|---|
| A trade at break-even after costs | "up 12% from where I started" | "down 5% from the peak" |
| A negative-skew options strategy | "80% win rate" | "loses more than it makes when it loses" |
| Exchange pricing | maker *rebate* | absence of a *fee* |
| Brokerage cost model | "commission-free" | spread + payment-for-order-flow cost |
| A held losing position | "long-term hold" | "down 30%, should I cut?" |

Each row is the *identical* economic object; only the framing differs, and the framing reliably shifts behavior.

## Trading Relevance

Framing effects are pervasive and costly in trading because P&L is inherently a gain/loss quantity and the reference point (usually the entry price) is arbitrary and psychologically sticky.

- **The disposition effect is framing in action.** A position above entry is framed as a "gain," inducing risk-aversion and premature selling; below entry it is framed as a "loss," inducing risk-seeking and holding-and-hoping. See [[disposition-effect]]. The entry price is just an [[anchoring-bias|anchor]] — the market is indifferent to it.
- **Reference-point manipulation changes behavior.** The same account down 5% on the year feels very different framed as "down 5% from the peak" versus "up 12% from where I started." Brokers, fund marketers, and traders themselves exploit this — e.g. quoting performance from a flattering start date.
- **Probability framing in options and bets.** "80% win rate" sells a [[short-strangle]] far better than its equivalent "expected to lose more than it makes when it loses," even when both describe the same negative-skew payoff. Framing a strategy by hit rate rather than by expectancy or geometric return drives systematic over-allocation to negatively-skewed strategies (see [[dopamine-loop]]).
- **Surcharge vs discount, fee vs rebate.** Microstructure and product design lean on framing: a maker *rebate* feels better than the equivalent absence of a *fee*; "commission-free" framing (see [[democratization-of-markets]]) obscures spread and payment-for-order-flow costs.
- **Defensive use.** The standard debiasing reframe — "If I held no position, would I buy this at today's price?" — works precisely by stripping away the entry-price frame and forcing a decision based on forward expected value rather than realized-vs-unrealized status. Evaluating decisions at the **portfolio level** rather than position-by-position also reduces frame-dependent salience.

Because framing operates automatically (System 1), the reliable counter is to standardize the frame in advance: define decisions in terms of forward expected value and risk, fix evaluation windows and reference points in a written plan, and let mechanical rules execute so the in-the-moment frame cannot bend the choice.

### Worked Example: Two Ways to See the Same Position

A trader bought 1,000 shares at $50 ($50,000 cost). The stock is now $44.

- **Loss frame (entry anchor):** "I'm down $6,000 (12%). If I sell I lock in the loss; if I hold, it could come back to $50." → induces holding-and-hoping (risk-seeking in the loss domain).
- **Forward frame (no anchor):** "I have $44,000 of capital tied up in this name. With no position, would I buy 1,000 shares at $44 today given the current setup?" → if the answer is no, the rational move is to redeploy the $44,000 elsewhere, regardless of the $50 entry.

The market does not know or care about the $50 entry — it is a sticky [[anchoring-bias|anchor]] supplied by the frame, not information. The forward frame strips it out and converts the decision back into a clean expected-value choice.

## Common Pitfalls

- **Believing you are immune.** Framing affects experts and professionals; awareness alone does not remove it. The fix is structural (fixed frames, written rules), not willpower.
- **Letting marketing set your reference point.** Performance "since inception," "from the bottom," or "best year" framing is chosen to flatter. Re-anchor to a neutral benchmark and a fixed evaluation window.
- **Hit-rate seduction.** A high win-rate frame ("wins 9 of 10 trades") systematically over-sells negative-skew strategies. Always re-frame to **expectancy** (average win × win rate − average loss × loss rate) and geometric return.
- **Position-by-position evaluation.** Looking at each open trade in isolation maximizes frame salience. Evaluate at the **portfolio level** to dilute it.
- **Inconsistent frames across decisions.** Using a gain frame to justify taking profits and a loss frame to justify holding losers is exactly the [[disposition-effect]] — the cure is one consistent, pre-committed frame for both.

## Related

- [[prospect-theory]] — the value function that produces gain/loss asymmetry
- [[loss-aversion]] — the steeper loss limb that drives the reversal
- [[disposition-effect]] — framing applied to open positions
- [[anchoring-bias]] — the entry price as the sticky reference point
- [[cognitive-biases]] — the broader family of decision errors
- [[dopamine-loop]] — hit-rate framing and strategy over-allocation
- [[trading-psychology]] — practical debiasing

## Sources

- Tversky, A. & Kahneman, D. (1981) "The Framing of Decisions and the Psychology of Choice," *Science* 211:453-458 — the Asian disease problem.
- Kahneman, D. & Tversky, A. (1979) "Prospect Theory: An Analysis of Decision under Risk," *Econometrica* 47:263-291.
- [[book-thinking-fast-and-slow]] — Kahneman's accessible treatment of framing and reference dependence.
