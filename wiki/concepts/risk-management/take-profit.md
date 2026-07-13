---
title: "Take Profit"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [risk-management, order-types, trading-psychology]
aliases: ["Profit Taking", "Take-Profit Order", "TP", "Profit Target"]
domain: [risk-management]
prerequisites: ["[[stop-loss]]", "[[order-types]]"]
difficulty: beginner
related: ["[[risk-management]]", "[[stop-loss]]", "[[position-sizing]]", "[[risk-reward-ratio]]", "[[trailing-stop]]", "[[managing-winners]]", "[[loss-aversion]]", "[[expectancy]]", "[[trading-journal]]"]
---

A **take-profit** (TP) is a predefined exit that closes a position once price reaches a target level, converting an unrealised gain into a realised one. It is the upside mirror of the [[stop-loss]]: where the stop bounds the loss on a wrong trade, the take-profit harvests the gain on a right one. Together the two define the [[risk-reward-ratio|risk/reward]] of every trade before it is entered, and removing the exit decision from the heat of the moment is the take-profit's main behavioural value.

## Overview and Mechanics

A take-profit can be implemented as a resting **limit order** placed at the target price (a take-profit order, or on many platforms a bracket/OCO order that pairs the TP with a stop). When price touches the limit, the order fills and the position is flat. The two halves of a **one-cancels-the-other (OCO)** bracket are linked: a fill on the stop cancels the take-profit, and a fill on the take-profit cancels the stop, so the trader is never left with a dangling order after the position closes.

Several common ways to set the target:

- **Fixed risk/reward multiple.** Set TP at a multiple of the stop distance. If the stop risks 1R (one unit of risk), a 2R target is placed twice as far from entry as the stop. The required [[expectancy|win rate]] to break even at reward:risk *b* is `1 / (1 + b)` — a 2:1 target only needs to win ~33% of the time to break even, a 3:1 target ~25%. This is the link between take-profit placement and the [[risk-reward-ratio]].
- **Technical level.** Place the TP just ahead of a structural barrier — prior swing high/low, a measured-move projection, a round number, a [[fibonacci-retracement]] extension, or a [[volume-profile]] node — where price is likely to stall and resting liquidity sits.
- **Volatility-scaled.** Set the target as a multiple of [[average-true-range|ATR]] so that the profit objective expands in fast markets and contracts in quiet ones.
- **Scaling out (partial take-profit).** Close a fraction of the position at a first target (often locking in enough to cover the trade's risk), then let the remainder run with a [[trailing-stop]]. This is the standard compromise between booking gains and capturing trends — see [[managing-winners]].
- **Time-based / discretionary.** Exit on a target *date* or on invalidation of the thesis rather than a price (common for [[options]] income books and event trades).

### Break-even win rate by reward:risk

The required win rate to break even at reward:risk *b* is `1 / (1 + b)`. This table is the core reason target placement and the [[risk-reward-ratio]] cannot be chosen in isolation from a strategy's hit rate:

| Reward:Risk (b) | Break-even win rate | Read |
|---|---|---|
| 1:1 | 50% | Must win more than half the time |
| 1.5:1 | 40% | Modest edge needed |
| 2:1 | 33% | A common swing-trade default |
| 3:1 | 25% | Trend-following territory |
| 5:1 | 17% | Few big winners pay for many losers |
| 0.5:1 (tight TP) | 67% | Mean-reversion / premium-selling: high hit rate required |

A target is only "good" if the strategy's actual win rate clears the break-even row for that reward:risk — otherwise the [[expectancy]] is negative no matter how disciplined the execution.

Two structural cautions:

- A take-profit *limit* may not fill if price gaps through it in an illiquid market, or may suffer adverse selection — the level that fills your TP is, by construction, a level the market was willing to trade through. A take-profit set too tight on a trending instrument systematically caps winners while stops cut losers, degrading [[expectancy]].
- For short-premium [[options]] books the analogous rule is closing at a fraction of max profit (e.g. 50% of credit), which raises the [[theta-realisation-ratio]] by avoiding the flat, slow-decaying tail of the position. See [[managing-winners]] and [[theta-targeting]].

## Worked Example: A 2R Trade with a Scale-Out

A trader buys a stock at **$100** and places a [[stop-loss]] at **$96**, risking **$4 per share (= 1R)**. With $200,000 of capital and a 1% risk budget ($2,000), [[position-sizing]] dictates **500 shares** (500 × $4 = $2,000 at risk).

| Plan element | Level | R-multiple | Action |
|---|---|---|---|
| Entry | $100 | 0R | Buy 500 |
| Stop-loss | $96 | −1R | OCO leg; cancels TP if hit |
| First target (TP1) | $104 | +1R | Sell 250; bank $1,000, now risk-free |
| Move stop to break-even | $100 | — | Remaining 250 shares cannot lose |
| Second target (TP2) | $108 | +2R | [[trailing-stop]] on final 250 |

After TP1, the trade is "free": the locked-in $1,000 covers the entire original risk, so the worst case on the remaining 250 shares is a flat outcome. If TP2 fills, total profit is $1,000 (TP1) + $2,000 (250 × $8) = **$3,000 = 1.5R blended** while never having risked more than 1R. This scale-out structure is the practical embodiment of "cut the downside, let part of the winner run" — the [[managing-winners]] discipline.

## Trading Relevance

In practice the take-profit is as much a psychology tool as an execution one. The dominant failure mode is the inverse of [[loss-aversion]]: traders cut winners too early to "lock in" a small gain (the disposition effect) while letting losers run in hope of a recovery — exactly backwards from positive expectancy. A pre-committed take-profit, written into the [[trading-journal]] at entry alongside the stop, removes the in-the-moment decision and lets the trader be judged on adherence rather than on the random outcome of a single trade.

The classic cautionary lesson is the bubble that never gets sold: investors who refuse to realise gains during a mania and watch them evaporate in the collapse (the [[poseidon-bubble|Poseidon nickel bubble]] of 1969-70 is a textbook Australian example). The discipline that prevents this is mechanical: set profit targets in advance, scale out into strength, and execute the plan without re-optimising for the upside that "might still come."

The right take-profit is not the one that maximises any single trade — it is the one that maximises long-run [[expectancy]] across many trades given the strategy's win rate and the instrument's behaviour. A trend-following system deliberately uses wide or trailing targets (few big winners pay for many small losers); a mean-reversion or premium-selling system uses tight, mechanical targets (many small winners, managed before the tail). Matching take-profit logic to the edge being harvested is the core skill.

## Pitfalls and Risks

- **Capping winners while stops cut losers.** A take-profit set too tight on a trending instrument truncates the right tail of the return distribution while the [[stop-loss]] still realizes the full left tail — a structural drag on [[expectancy]]. This is the most common silent killer of otherwise sound systems.
- **The disposition effect.** Cutting winners early to "lock in" a gain while holding losers in hope is exactly backwards from positive expectancy; a pre-committed TP counteracts this [[loss-aversion]]-driven bias.
- **Gap risk on limit fills.** A take-profit *limit* will not fill if price gaps through it (overnight, around earnings, or in an illiquid name); and any fill is by construction at a level the market was willing to trade through — mild adverse selection.
- **Re-optimising in the moment.** Moving the target further out because the trade "might still run" abandons the plan and re-introduces the discretion the TP was meant to remove. The mania-then-collapse pattern (e.g. the [[poseidon-bubble|Poseidon nickel bubble]]) is the macro version of refusing to take profit.
- **Mismatched logic.** Using mean-reversion-style tight targets on a trend system (or vice versa) guarantees the take-profit fights the edge instead of harvesting it.
- **Ignoring costs.** Very tight targets generate more round-trips; commissions, spread, and slippage can quietly turn a positive-expectancy backtest into a losing live record.

## Related

- [[stop-loss]] — the downside counterpart that bounds risk
- [[risk-reward-ratio]] — the ratio of target distance to stop distance
- [[trailing-stop]] — dynamic exit that lets winners run while protecting gains
- [[managing-winners]] — partial take-profit / scaling-out for options books
- [[position-sizing]] — determines how much each R is worth in dollars
- [[expectancy]] — why target placement must match win rate
- [[loss-aversion]] — the bias take-profit discipline counteracts
- [[trading-journal]] — where the target is recorded at entry and reviewed after
- [[theta-targeting]] — the income-book analogue of profit targeting

## Sources

- Van K. Tharp, *Trade Your Way to Financial Freedom* — expectancy, R-multiples, and exit design.
- Investopedia, "Take-Profit Order (TP)" — definition, OCO/bracket mechanics, and limit-order behaviour.
- General trading-desk and broker documentation on bracket/OCO order construction.
