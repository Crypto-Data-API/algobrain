---
title: "When to Retire a Strategy"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, risk-management, strategy-lifecycle, kill-criteria]
aliases: ["Strategy Retirement", "Kill Criteria", "When to Stop Trading a Strategy"]
domain: [portfolio-theory, risk-management]
difficulty: intermediate
related: ["[[failure-modes]]", "[[multi-strategy-portfolio]]", "[[regime-detection]]", "[[strategy-development-overview]]", "[[edge-decay]]", "[[sharpe-ratio]]", "[[maximum-drawdown]]", "[[kelly-criterion]]", "[[live-journal]]", "[[research-checklist]]"]
---

# When to Retire a Strategy

The single hardest discipline in active management. Strategies you researched and built become emotionally meaningful; pulling the plug feels like admitting failure. The result is that most portfolios accumulate dead strategies that drag on performance for years — sometimes decades — beyond their natural sell-by date. The only defense is *pre-committing to numerical kill criteria* before the drawdown begins, while you still have the discipline to specify them honestly.

## The Asymmetry

Two errors are possible:

1. **Type I: Killing a strategy that would have recovered.** Cost: foregone returns from the strategy.
2. **Type II: Keeping a dead strategy alive.** Cost: continued drawdown plus opportunity cost of the capital.

Most traders worry mostly about Type I. Empirically, **Type II is much more costly** because dead strategies tend to *keep* dying — they don't suddenly mean-revert to profitability — and the opportunity cost compounds.

A useful prior: when in doubt, kill. The cost of incorrectly killing a strategy is bounded (you can always restart it if conditions improve); the cost of incorrectly continuing one is unbounded.

## Three Categories of Drawdown

When a strategy is losing money, distinguish three causes:

### 1. Normal Drawdown
Within the strategy's historical drawdown distribution. Should be expected. **Do not kill.** The strategy is performing exactly as advertised.

Test: is the current rolling drawdown within the 95th percentile of historical drawdowns of the same strategy on the same regime?

### 2. Tail Drawdown
Worse than historical but explainable by current conditions. The strategy is in an environment that historically would have produced this kind of loss, even if you haven't seen it in your sample. **Do not necessarily kill, but reduce size.**

Test: is the loss explainable by current regime indicators (high VIX, regime change, sector dislocation)? Is similar drawdown happening to other strategies in the same edge category?

### 3. Structural Drawdown
The drawdown isn't explainable by regime or normal noise. Something has changed about the underlying mechanism. **Kill or seriously consider killing.**

Test: are the kill criteria you wrote in advance now being met? Is there a specific dated event that explains the change?

## Pre-Committed Kill Criteria

Every strategy in production should have a written kill criterion *for each plausible failure mode*. Examples:

### For all strategies
- **Drawdown threshold:** kill if drawdown exceeds 1.5× the worst historical drawdown (or some fixed level like 25%)
- **Rolling Sharpe:** kill if rolling 6-month Sharpe < 0 for two consecutive months
- **Monthly hit rate:** kill if hit rate falls below 30% for three consecutive months

### For trend strategies
- **Trend strength:** pause if average ADX of universe < 15 for 90 days (no trends to follow)
- **Whipsaw losses:** kill if 30-day whipsaw count exceeds 2× historical average

### For mean-reversion strategies
- **Cointegration breaks:** kill pair if cointegration p-value > 0.10 for 30 days
- **Half-life increases:** review if estimated half-life doubles relative to research

### For carry strategies
- **Carry compression:** kill if expected carry < cost of capital
- **Vol spike:** pause if implied vol > 2× research-time vol

### For arbitrage strategies
- **Spread evaporation:** kill if average spread < execution cost
- **Venue change:** kill if venue makes a structural change to the underlying product

### For event-driven strategies
- **Event count:** pause if monthly event count is < 30% of historical average
- **Hit ratio on events:** kill if events outcome distribution shifts away from base rate

The kill criteria should be:
- **Numerical** — no "I'll know it when I see it"
- **Pre-committed** — written *before* deployment, not during the drawdown
- **Specific to the strategy's mechanism** — generic criteria miss the actual failure mode
- **Triggerable without judgment** — the rules apply themselves

### Kill-criteria summary table

The three universal signals — drawdown, rolling Sharpe, and edge decay — and the action each should trigger. Thresholds below are illustrative defaults; calibrate each to the strategy's own historical distribution.

| Signal | Watch metric | Pause trigger (reduce size) | Kill trigger | Notes |
|---|---|---|---|---|
| **Drawdown** | Current peak-to-trough | > 1.0× worst historical DD | > 1.5× worst historical DD, or a fixed hard floor (e.g. 25%) | See [[maximum-drawdown]]; recovery is asymmetric — a 50% DD needs a 100% gain |
| **Rolling Sharpe** | Rolling 6-month [[sharpe-ratio]] | < 0.3 for 1 month | < 0 for 2 consecutive months | Short windows are noisy; require *consecutive* breaches |
| **Edge decay** | Live vs research effect size | t-stat halves vs research | Live alpha indistinguishable from zero over 12 months | The hardest to detect; see below |
| **Hit rate** | Rolling win rate | Below research mean − 1σ | < 30% for 3 consecutive months | Combine with payoff ratio, not standalone |
| **Mechanism break** | Dated structural event | Suspected | Confirmed (venue, counterparty, regulation, crowding) | A confirmed mechanism break is an instant kill |

The pause column buys evidence-gathering time at reduced Type II exposure; the kill column is unconditional once breached.

## Detecting Edge Decay

Drawdown and rolling Sharpe catch *acute* failure. The more insidious death is **slow [[edge-decay|edge decay]]** — the inefficiency the strategy harvests gets crowded out, arbitraged away, or regulated out of existence, and the live alpha drifts toward zero without any single dramatic drawdown. Signals:

- **Live vs research t-statistic.** If the in-sample effect was significant at t ≈ 3 but the live realised effect is running at t ≈ 1, the edge has likely compressed. Re-estimate on the live sample alone.
- **Capacity crowding.** Rising correlation between the strategy's signal and known crowded factors; widening market impact per unit of size; the same trade appearing in competitor commentary. See [[failure-modes]].
- **Spread / premium compression.** For [[carry-anomaly|carry]], arbitrage, and premium-selling strategies, the harvested spread shrinking toward the cost of capital or execution cost is a direct decay reading.
- **Decay half-life.** Many published anomalies decay measurably after publication. A strategy built on a public, well-known edge should be assumed to be decaying and monitored more aggressively than one built on a proprietary mechanism.

Edge decay rarely triggers a sharp drawdown stop — which is exactly why it kills so many strategies silently. The defense is to monitor the *effect size*, not just the P&L.

## Drawdown and Rolling-Sharpe Mechanics

The two acute signals deserve precise definitions so the rules are genuinely triggerable without judgment:

- **Drawdown.** Peak-to-trough decline of the cumulative *geometric* equity curve (not the arithmetic-return series — recovery is multiplicative). A killed-at-25% rule means the cumulative equity has fallen 25% from its running maximum. Because recovery is asymmetric, the deeper the drawdown, the steeper the climb back: a 20% DD needs +25%, a 33% DD needs +50%, a 50% DD needs +100%. This asymmetry is why drawdown limits, not return targets, are the dominant kill lever. See [[maximum-drawdown]] and [[geometric-mean]].
- **Rolling Sharpe.** Computed over a fixed trailing window (commonly 6 or 12 months). Short windows are statistically noisy — a single bad month can drag a 6-month Sharpe negative even for a healthy strategy — so the rule requires *consecutive* breaches (e.g. "< 0 for two consecutive months") rather than a single reading. This is the standard guard against killing on noise (a Type I error) while still catching genuine deterioration.

A common combined rule used in pre-committed frameworks: **kill if drawdown > 1.5× worst historical AND rolling 6-month Sharpe < 0 for 2 months.** Requiring both reduces false positives; using either alone increases sensitivity at the cost of more Type I errors. The choice between AND and OR is itself a pre-commitment to make before deployment.

## The Pre-Mortem Habit

Before deploying any strategy, write a one-paragraph pre-mortem:

> "It is 12 months from now, and this strategy has been kicked off the book. What happened? Most likely: ___________. What would I have wanted to know in advance?"

The "most likely" cause becomes your primary kill criterion. The "would have wanted to know in advance" becomes your monitoring metric.

## Why Pre-Commitment Matters

Once a strategy starts losing, several psychological forces push you toward keeping it alive:

1. **Sunk cost fallacy** — "I spent so much time researching this"
2. **Loss aversion** — "I'll wait for break-even and then close it"
3. **Optimism bias** — "the regime is about to change"
4. **Identity protection** — "this is *my* strategy"
5. **Counterfactual self-deception** — "if I had bigger size, this drawdown would be a buying opportunity"

All of these are normal. None of them are valid reasons to keep a dead strategy alive. The only defense is **pre-committed numerical rules that don't require you to make the decision in the moment**.

It is much easier to write "kill if rolling 6-month Sharpe < 0 for 2 months" when you're not currently losing money. When you *are* currently losing money, every fiber of your being will look for reasons the rule doesn't apply.

## Distinguishing Drawdown from Death

A useful heuristic: **drawdowns recover; deaths don't**. If you can identify a *mechanism* that broke (a venue closed, a counterparty disappeared, a regulatory shift hit, the underlying inefficiency was crowded out), you have a death — not a drawdown. Kill it.

If you can't identify a mechanism and the drawdown is within historical norms for the strategy's regime, you have a drawdown. Hold.

Cases where this is hard:
- The mechanism *might* be broken but you're not sure
- The drawdown is worse than historical but you have a hypothesis for why
- A correlated strategy died — does that mean yours is also dead?

In these cases, the safe move is to *reduce size* rather than kill or hold. Cut allocation to 25-50% of normal until the picture clarifies. This buys you time to gather evidence without taking on full Type II risk.

## The Restart Question

A killed strategy can be restarted if conditions change. Restart criteria should also be pre-committed:

- **Restart if** the failure-mode condition that triggered the kill reverses
- **Restart if** a new edge mechanism appears that wasn't in the original research
- **Restart at reduced size** for the first 3-6 months after restart

Many traders treat strategies as binary: "running" or "dead." A more useful frame: strategies move between *active*, *paused*, *retired*, and *re-entered*. The tighter the lifecycle management, the smaller the cost of mistakes.

## A Decision Framework

When a strategy is in drawdown:

1. **Is the drawdown within historical norms?** If yes → hold, no action.
2. **Is the drawdown worse than historical but explainable by regime?** If yes → reduce size by 50%, monitor.
3. **Has any pre-committed kill criterion been triggered?** If yes → kill, no exceptions.
4. **Is there a specific dated event that explains the new regime?** If yes → assume structural change, kill.
5. **Are correlated strategies also dying?** If yes → assume category-wide failure, kill or reduce.
6. **None of the above and the drawdown is unexplained?** → reduce to 25%, gather evidence, set a specific timeline (e.g., "decide in 30 days").

This framework is *deliberately mechanical*. The point is to make the decision *cheap* and *fast*, so you don't have time to talk yourself out of it.

## Examples From the Wiki

- **[[ltcm-collapse-1998]]** — LTCM had no pre-committed kill criteria; their strategies were "obviously right" and they kept doubling down through the drawdown. Type II error, fatal.
- **[[quant-meltdown-2007]]** — funds with explicit drawdown stops kicked their strategies offline early in the week and survived; funds without explicit stops continued through Wednesday-Thursday and didn't.
- **[[flash-crash-2010]]** — algorithms with hardcoded "halt if x% deviation from theoretical" survived; those without didn't.

The pattern: explicit pre-committed rules > judgment under stress.

## Sources

- [[book-when-genius-failed]] — Lowenstein on LTCM's failure to kill
- [[book-the-quants]] — Patterson on which August 2007 funds killed and survived
- [[book-quantitative-trading-ernest-chan]] — Chan on practical kill criteria

## Related

- [[failure-modes]]
- [[multi-strategy-portfolio]]
- [[regime-detection]]
- [[strategy-development-overview]]
- [[research-checklist]]
- [[trading-journal]]
- [[live-journal]]
