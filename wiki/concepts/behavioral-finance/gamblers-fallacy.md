---
title: "Gambler's Fallacy"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [behavioral-finance, risk-management]
aliases: ["gambler's fallacy", "gamblers fallacy", "Monte Carlo fallacy", "it's due to bounce"]
domain: [behavioral-finance]
prerequisites: ["[[behavioral-finance]]"]
difficulty: beginner
related: ["[[recency-bias]]", "[[mean-reversion]]", "[[loss-aversion]]", "[[overconfidence-bias]]", "[[disposition-effect]]", "[[narrative-fallacy]]", "[[trading-psychology]]", "[[cognitive-biases]]", "[[risk-management]]", "[[position-sizing]]"]
---

The gambler's fallacy is the mistaken belief that, in a sequence of independent events, a streak in one direction makes the opposite outcome "due." In trading it is the voice that says *"it has fallen five days in a row, so it has to bounce now"* — and it answers a frequent trader question: *"why do I keep assuming a falling stock is about to turn just because it's dropped a lot?"* The fallacy treats independent or weakly-related price moves as if a hidden law of averages must rebalance them in the short run.

## The Core Idea

For genuinely independent events — a fair coin, a roulette wheel — past outcomes carry **no** information about the next one. A fair coin that has landed heads five times in a row still has a 50% chance of heads on the sixth flip; the coin has no memory. The gambler's fallacy is the intuition that tails is now "owed." (It is named the *Monte Carlo fallacy* after a famous 1913 roulette run where the ball landed black many times in a row and players lost fortunes betting that red was due.)

Markets are *not* perfectly independent — there are real mean-reverting and trending dynamics. But the fallacy is the *unjustified* assumption that a streak alone, with no analysis of cause, guarantees a reversal. A stock that has fallen for a reason can keep falling; "it's down a lot" is not by itself a thesis.

## How It Shows Up in Trading

- **"It's due to bounce" averaging down.** Adding to a falling position purely because the decline has been long or steep, with no fresh catalyst — see [[disposition-effect]] and [[sunk-cost-fallacy]].
- **Counter-trend knife-catching.** Repeatedly trying to pick the bottom of a downtrend because each new low feels like it "must" be the last.
- **Streak-based sizing.** Believing a string of losing trades means a winner is now overdue, and sizing up the next trade to "make it back" — a dangerous mix with [[loss-aversion]] and revenge trading.
- **Fading randomness.** Betting against a run in a series that is effectively random (e.g. very short-term noise), expecting an inevitable correction that has no mechanism behind it.
- **The hot-hand flip side.** The same flawed reasoning can run the other way (expecting a winning streak to continue); the common root is over-reading short sequences of independent or noisy outcomes.

## Why It Happens

The fallacy stems from a faulty mental model of randomness. People expect short sequences to "look random" — to balance out quickly — and a long one-sided streak violates that expectation, so the mind predicts a corrective swing to restore balance. Kahneman and Tversky described this as a belief in the **"law of small numbers"**: treating small samples as if they must mirror the long-run distribution. In reality, the law of large numbers only guarantees balance over *very* large samples, and it does so by *dilution*, not by compensating reversals. The streak does not get "paid back"; it just gets swamped by future data.

## A Hypothetical Example

*This example is illustrative, not a real event.* A trader, "Alex," is watching a stock that has closed lower five sessions running on a deteriorating fundamental story. Alex reasons "nothing falls six days in a row — it's due for a green day," and buys a full position with no catalyst, purely on the streak. The stock falls three more sessions as the bad news keeps developing. The error was treating "five down days" as evidence of an imminent reversal when the moves were driven by ongoing news, not by a law of averages. A move worth fading needs a *reason* to revert — oversold extremes confirmed by a real [[mean-reversion]] edge, a catalyst, support that has historically held — not merely the length of the streak.

## How to Counter It

- **Demand a mechanism, not a streak.** Before fading a move, name *why* it should reverse (catalyst, valuation, structural [[mean-reversion]] edge). "It's down a lot" is not a reason.
- **Treat each trade as independent for sizing.** A losing streak does not make the next trade more likely to win; keep [[position-sizing]] constant and rule-based rather than "due"-based.
- **Distinguish independent noise from real autocorrelation.** Some series mean-revert and some trend; know which regime you are in instead of assuming balance must restore itself.
- **Pre-define entries and stops.** A planned [[stop-loss]] prevents a "it's due to turn" thesis from turning a small loss into a large one.
- **Backtest the streak idea.** If "buy after N down days" had an edge, it would show up in the data; usually it does not, which exposes the fallacy.
- **Keep a [[trading-journal]].** Logging "due to bounce" trades and their outcomes builds evidence against the instinct.

## Gambler's Fallacy vs Recency Bias

These two biases are mirror images and people slip between them depending on framing. The gambler's fallacy expects a **reversal** of a streak ("it's due to turn"), whereas [[recency-bias]] expects **continuation** of it ("the trend will keep going"). Both are over-readings of a short sequence; the antidote to both is the same — analyse the underlying process and the base rates rather than the raw streak.

## Related

- [[recency-bias]] — the continuation-expecting mirror of this reversal-expecting fallacy
- [[mean-reversion]] — the real dynamic the fallacy is a naive caricature of
- [[loss-aversion]] — feeds streak-based revenge sizing
- [[disposition-effect]] and [[sunk-cost-fallacy]] — reinforce "due to bounce" holding
- [[narrative-fallacy]] — inventing a story for why the streak "must" end
- [[trading-psychology]] and [[cognitive-biases]] — the broader context
- [[risk-management]] — rule-based sizing immune to "due" reasoning

## Sources

- Tversky, A. & Kahneman, D. (1971). "Belief in the Law of Small Numbers." *Psychological Bulletin* 76(2), 105-110 — the small-sample misconception behind the fallacy.
- Kahneman, D. & Tversky, A. (1972). "Subjective Probability: A Judgment of Representativeness." *Cognitive Psychology* — representativeness and expectations of local randomness.
- Clotfelter, C. & Cook, P. (1993). "The Gambler's Fallacy in Lottery Play." *Management Science* — field evidence of the bias in real betting behaviour.
