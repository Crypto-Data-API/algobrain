---
title: "Win Rate"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [risk-management, quantitative, backtesting]
aliases: ["Win Rate", "Win Percentage", "Hit Rate", "Strike Rate", "Batting Average", "Probability of Profit"]
domain: [risk-management]
prerequisites: ["[[expected-value]]", "[[risk-reward-ratio]]"]
difficulty: beginner
related: ["[[expected-value]]", "[[risk-reward-ratio]]", "[[expectancy]]", "[[risk-of-ruin]]", "[[kelly-criterion]]", "[[position-sizing]]", "[[probability-of-profit]]"]
---

Win rate is the proportion of trades that close profitably, expressed as a percentage of all closed trades. It is one of the two numbers — alongside the average win-to-average-loss ratio (the [[risk-reward-ratio]]) — that together determine whether a strategy has positive [[expected-value]]. On its own, win rate says almost nothing about profitability: a system that wins 90% of the time can still lose money, and a system that wins 30% of the time can be highly profitable.

## Calculation

**Win Rate = Number of Winning Trades / Total Number of Closed Trades**

A trade is normally counted as a "win" if it closes above its entry net of costs, though some traders count scratch trades (closed at breakeven) separately. Win rate is sometimes called the **hit rate**, **strike rate**, or **batting average**; in the options context the forward-looking equivalent is the [[probability-of-profit]] implied by the position's payoff and the underlying's distribution.

## Why win rate alone is misleading

Win rate is only half of the [[expectancy]] equation. The full relationship is:

**Expectancy per trade = (Win Rate × Average Win) − (Loss Rate × Average Loss)**

This makes the trade-off explicit. A trend-following system might win only 35% of the time but let winners run to 4× the size of its losers, producing a strongly positive expectancy. A premium-selling or mean-reversion system might win 80% of the time while occasionally taking a loss many times the size of a typical win — positive on average until a tail event wipes out months of small gains. The headline win rate hides which of these you are looking at.

A useful framing is the **breakeven win rate** for a given payoff ratio. If the average win equals the average loss (1:1), you need to win more than 50% of the time to be profitable. If the average win is twice the average loss (2:1), the breakeven win rate falls to roughly 33%. The general formula is:

**Breakeven Win Rate = 1 / (1 + Reward-to-Risk Ratio)**

The table below shows the win rate a strategy must exceed just to break even (before costs) at various payoff ratios. Anything above the threshold is profitable; anything below it loses money no matter how "high" the win rate feels:

| Reward-to-risk (avg win : avg loss) | Breakeven win rate |
|---|---|
| 0.5 : 1 | 66.7% |
| 1 : 1 | 50.0% |
| 1.5 : 1 | 40.0% |
| 2 : 1 | 33.3% |
| 3 : 1 | 25.0% |
| 5 : 1 | 16.7% |

Two lessons fall out of this table. First, a small edge in payoff dramatically lowers the win rate you need — which is why [[trend-following]] and [[breakout]] systems can thrive on sub-40% win rates. Second, a high-win-rate style that risks more than it makes per trade (a payoff below 1:1, common in option-selling and fading strategies) needs a *very* high win rate and is quietly fragile: a single outsized loss can undo a long string of wins.

## The win-rate / payoff trade-off

Strategies sit on a spectrum:

- **High win rate, low payoff** — selling options, fading extremes, scalping. Frequent small wins, rare large losses. Emotionally comfortable but exposed to [[tail-risk]] and gap risk.
- **Low win rate, high payoff** — trend following, breakout trading, buying convex payoffs. Many small losses punctuated by occasional large wins. Statistically robust but psychologically taxing through long losing streaks.

Neither is inherently better; both can have identical expectancy. What matters for survival is how the two interact with [[position-sizing]] and [[risk-of-ruin]]: a high-win-rate system invites over-betting because losses feel rare, while a low-win-rate system requires the discipline to endure drawdowns without abandoning the edge.

## Example

A swing trader places 100 trades. 45 are winners averaging +$600; 55 are losers averaging −$400.

- Win rate = 45 / 100 = **45%**
- Reward-to-risk = 600 / 400 = 1.5
- Breakeven win rate = 1 / (1 + 1.5) = 40%
- Expectancy = (0.45 × 600) − (0.55 × 400) = 270 − 220 = **+$50 per trade**

The 45% win rate beats the 40% breakeven, so the system is profitable despite losing more often than the average beginner would tolerate.

## Pitfalls and statistical caveats

- **Small samples lie.** A win rate computed over 20 trades carries a wide confidence interval; the [[law-of-large-numbers]] means the observed rate only converges to the true rate over hundreds of trades.
- **Survivorship and cherry-picking.** Closing winners early and "giving losers room" inflates win rate while quietly destroying expectancy — a classic [[behavioral-finance]] failure mode (the disposition effect).
- **Open trades and unrealised losses** can mask a falling true win rate if only closed trades are counted.
- **Costs matter.** A pre-cost win rate above breakeven can flip negative once spread, commission, and slippage are deducted; win rate should always be computed net of costs, consistent with how [[expectancy]] is measured.

## Related

[[expected-value]] · [[expectancy]] · [[risk-reward-ratio]] · [[risk-of-ruin]] · [[kelly-criterion]] · [[position-sizing]] · [[probability-of-profit]] · [[law-of-large-numbers]]
