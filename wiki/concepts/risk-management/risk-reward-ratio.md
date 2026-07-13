---
title: "Risk-Reward Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [risk-management, day-trading, swing-trading]
aliases: ["Risk/Reward Ratio", "Reward-to-Risk Ratio", "R:R", "RRR", "R-multiple"]
domain: [risk-management]
prerequisites: ["[[stop-loss]]", "[[take-profit]]", "[[position-sizing]]"]
difficulty: beginner
related:
  - "[[stop-loss]]"
  - "[[take-profit]]"
  - "[[position-sizing]]"
  - "[[expectancy]]"
  - "[[win-rate]]"
  - "[[risk-of-ruin]]"
  - "[[kelly-criterion]]"
  - "[[maximum-drawdown]]"
---

# Risk-Reward Ratio

The **risk-reward ratio** (often written R:R, or expressed as a reward-to-risk multiple) compares how much a trader stands to lose if a trade goes wrong against how much they stand to gain if it goes right. It is one of the first questions an ALFRED user asks before placing a trade: *"If I'm wrong, what's the damage, and is the potential upside worth it?"*

## Definition

For a single trade, the ratio is built from three prices: the entry, the [[stop-loss|stop-loss]] (where you admit you are wrong), and the [[take-profit|profit target]] (where you plan to exit a winner).

```
Risk   = | Entry price − Stop-loss price |
Reward = | Take-profit price − Entry price |

Reward-to-risk ratio = Reward / Risk
```

A trade risking $1 to make $3 has a **3:1** reward-to-risk ratio (sometimes written as a risk-reward of 1:3). The "R" in **R-multiple** refers to one unit of risk: if you risk $200 on a trade and it returns $600, that is a **+3R** outcome; a full stop-out is **−1R**. Thinking in R-multiples lets you compare trades of different dollar sizes on one scale.

## Why It Matters

The risk-reward ratio is meaningless on its own — it only becomes useful when paired with how *often* you win. Profitability is governed by **[[expectancy]]**, which combines both:

```
Expectancy (per trade, in R) = (Win% × Avg win in R) − (Loss% × Avg loss in R)
```

This produces the single most important rule of thumb in trading risk:

> A high reward-to-risk ratio lets you be wrong most of the time and still make money; a low one demands a high [[win-rate|win rate]] to survive.

### The breakeven win-rate table

For a fixed reward-to-risk ratio (ignoring costs), the win rate you need just to break even is:

```
Breakeven win% = 1 / (1 + Reward-to-risk)
```

| Reward-to-risk | Breakeven win rate | Interpretation |
|---|---|---|
| 1:1 | 50% | Must win more than half your trades |
| 2:1 | 33% | Can be wrong 2 of 3 times and break even |
| 3:1 | 25% | Can be wrong 3 of 4 times and break even |
| 0.5:1 | 67% | Needs a very high hit rate to work |

This is why trend-following systems with low win rates (often 30-40%) can still be highly profitable — their winners are large multiples of their losers. It is also why "high win-rate" strategies that take small profits and hold losers (a poor risk-reward) can quietly bleed an account: a single loss erases many wins.

## Worked Example (hypothetical)

Suppose an ALFRED user is looking at a stock trading at **$100**:

- **Entry:** $100
- **Stop-loss:** $95 (risk = $5 per share)
- **Take-profit:** $115 (reward = $15 per share)
- **Reward-to-risk ratio:** 15 / 5 = **3:1**

If they size the position so the $5 risk equals 1% of a $50,000 account (see [[position-sizing]]), a winning trade is **+3R = +3%** of the account and a losing trade is **−1R = −1%**. With a modest 40% win rate over 100 such trades:

```
Expectancy = (0.40 × 3R) − (0.60 × 1R) = 1.2R − 0.6R = +0.6R per trade
```

That is a positive edge despite losing 6 trades out of every 10 — the entire result comes from the favourable reward-to-risk ratio. (These numbers are illustrative, not a forecast.)

## Practical Rules of Thumb

- **Set the stop first, the target second.** Decide where you are wrong based on the chart or thesis, *then* see whether the realistic target offers an acceptable multiple. Do not widen your stop to make the ratio look good.
- **Many discretionary traders require a minimum of ~2:1** before taking a trade, so that a roughly even win rate produces positive [[expectancy]].
- **Account for costs.** Spreads, commissions, and [[slippage]] shrink real reward and widen real risk. A "2:1" trade can become 1.5:1 after costs on a small move.
- **Be honest about target probability.** A 10:1 trade is worthless if the target is almost never reached. The ratio must be weighed against the *probability* of each outcome, not admired in isolation.
- **Use it with position sizing, not instead of it.** The ratio shapes the *quality* of a trade; [[position-sizing]] controls the *size* of the loss. Together they determine [[risk-of-ruin]].

## Limitations

- **It ignores probability.** A favourable ratio with a tiny chance of hitting the target is a bad trade. Risk-reward must always be combined with an estimated [[win-rate]].
- **Stops are not guaranteed.** Gaps, halts, and illiquidity mean the realized loss can exceed the planned 1R (slippage beyond the stop), so the *real* downside can be worse than the ratio implies. See [[maximum-drawdown]] and [[tail-risk]].
- **Static targets misrepresent dynamic exits.** Trailing stops, partial profit-taking, and scaling out produce a *distribution* of R-multiples, not a single clean ratio.
- **Cherry-picking the ratio.** Moving the stop closer to flatter the ratio simply raises the probability of being stopped out by noise — a worse trade dressed up as a better one.

## Related

- [[stop-loss]] — defines the "risk" leg of the ratio
- [[take-profit]] — defines the "reward" leg of the ratio
- [[position-sizing]] — converts 1R of risk into a dollar amount and account percentage
- [[expectancy]] — combines risk-reward with win rate to measure the real edge
- [[win-rate]] — the hit rate the ratio must be paired with
- [[risk-of-ruin]] — the probability of blowing up, driven by ratio, win rate, and sizing
- [[kelly-criterion]] — optimal bet sizing given win rate and reward-to-risk
- [[maximum-drawdown]] — what a string of −1R losses does to the equity curve
