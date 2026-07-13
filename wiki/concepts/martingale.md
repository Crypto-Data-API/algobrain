---
title: "Martingale"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [risk-management, behavioral-finance, leverage, quantitative]
aliases: ["Martingale Strategy", "Doubling Strategy", "Anti-Martingale", "Martingale (probability)", "Martingale Property"]
related: ["[[kelly-criterion]]", "[[gamblers-ruin]]", "[[position-sizing]]", "[[risk-of-ruin]]", "[[risk-management]]", "[[averaging-down]]", "[[grid-trading]]", "[[leverage]]", "[[anti-martingale]]", "[[efficient-market-hypothesis]]", "[[random-walk]]"]
domain: [risk-management, behavioral-finance]
prerequisites: ["[[probability]]", "[[position-sizing]]"]
difficulty: intermediate
---

"Martingale" carries **two distinct meanings** in trading, and conflating them causes confusion — this page covers both, clearly separated:

1. **The betting system** (the everyday trading meaning) — a position-sizing scheme that *doubles the stake after every loss*. A ruinous, negative-skew approach. Covered first below.
2. **The probability-theory property** (the quant/academic meaning) — a stochastic process whose expected next value, given all past information, equals its current value: $E[X_{t+1}\mid \mathcal{F}_t] = X_t$. A "fair game" with no predictable drift. This is the formal backbone of the [[efficient-market-hypothesis]] and risk-neutral option pricing. Covered in its own section below.

The betting system is *named after* the probability concept, but they are separate ideas: one is a (bad) money-management rule, the other is a deep mathematical statement about unpredictability.

---

The **martingale betting system** is a position-sizing scheme in which the stake is *doubled after every loss*, so that the first win recovers all prior losses plus a one-unit profit. Imported from 18th-century gambling, the martingale is the archetype of a strategy that produces many small, steady gains punctuated by a rare, account-destroying loss. It is one of the most important *negative* lessons in trading risk management: a high win-rate with a catastrophic tail is not an edge, and almost every blow-up of a "consistent" trader traces back to martingale-like behaviour.

## How the Betting Scheme Works

Bet 1 unit. If you lose, bet 2. Lose again, bet 4, then 8, 16, 32... On the first win at stake `2^n`, you recover the `2^n − 1` cumulative loss and net +1 unit. On a fair coin the win is "certain" eventually, which is the seductive illusion. The lethal flaw is the **geometric explosion of the required stake** against two hard constraints:

The table below makes the explosion concrete. After a loss streak of length `k`, the next bet is `2^k` and the cumulative amount already lost is `2^k − 1`. The right column is the probability of a fair coin (p = 0.5) producing a streak of at least that length — small per attempt, but near-certain over thousands of trades:

| Loss streak `k` | Next required bet | Cumulative loss so far | P(streak ≥ k) on fair coin |
|-----------------|-------------------|------------------------|----------------------------|
| 1 | 2 | 1 | 50% |
| 3 | 8 | 7 | 12.5% |
| 5 | 32 | 31 | 3.1% |
| 7 | 128 | 127 | 0.78% |
| 10 | 1,024 | 1,023 | 0.10% |
| 13 | 8,192 | 8,191 | 0.012% |
| 20 | 1,048,576 | 1,048,575 | ~1 in a million |

A 0.10% chance per attempt sounds safe — but over **10,000 trades** the probability of hitting *at least one* 10-loss streak is $1 - (1 - 0.001)^{10000} \approx 99.995\%$. The killing streak is not a tail risk; for an active martingale trader it is a near-certainty. With a starting bankroll of 1,000 units (table stake 1), the very first 10-streak demands a 1,024-unit bet you cannot place — and the account is gone.

The lethal flaw rests against two hard constraints:

- **Finite capital.** A run of just 10 losses requires a 1,024-unit bet and a cumulative 1,023 units already lost. Streaks far longer than intuition suggests occur with near-certainty over enough trials.
- **Table / margin limits.** Even with infinite nerve, exchanges and brokers cap leverage and position size, truncating the doubling exactly when you most "need" it to continue.

The expected value is, at best, zero (in a fair game) and negative once costs, spreads, or a house edge apply. The martingale does not change expectation — it only *reshapes the distribution* of outcomes into "win small, often; lose everything, rarely." This is precisely the [[risk-of-ruin|risk-of-ruin]] trap.

## Why It Masquerades as an Edge

A martingale trader shows a long, smooth equity curve with a >90% win rate — until the day a long adverse run hits the capital or margin wall and the entire account (plus more, if leveraged) is gone in one event. Backtests over short windows that happen not to contain the killing streak look spectacular, which is why martingale logic hides inside many "always-wins" retail systems: [[grid-trading]] bots, naive [[averaging-down]] / dollar-cost-into-a-falling-knife schemes, and "recovery" EAs. The structural tell is any rule that *increases* exposure as losses mount.

## The Anti-Martingale (the trading-relevant inversion)

The disciplined inversion — **anti-martingale** — does the opposite: *increase* size after wins (when the edge and capital are confirmed) and *decrease* size after losses (preserving capital through adverse runs). This is the philosophy behind:

- **[[kelly-criterion|Kelly sizing]]**, where the optimal bet is a *fraction of current bankroll* — so stakes shrink in absolute terms during drawdowns and grow during winning streaks, mechanically the anti-martingale.
- **[[volatility-targeting]] and pyramiding into winners**, the basis of most trend-following.
- **Fixed-fractional [[position-sizing]]** (risk a constant % of equity per trade), which can never blow up from sizing alone because the stake auto-deleverages as equity falls.

The anti-martingale embraces positive skew (many small losses, occasional large win) — the opposite, survivable shape.

## The Martingale Property (Probability Theory)

The *second, unrelated* meaning. In probability theory a stochastic process $\{X_t\}$ is a **martingale** with respect to an information set (filtration) $\mathcal{F}_t$ if its expected next value, conditional on everything known so far, equals its current value:

$$E[X_{t+1} \mid \mathcal{F}_t] = X_t$$

In words: the best forecast of tomorrow's value, given all of today's information, is simply today's value. The process has **no predictable drift** — it is the formal definition of a "fair game." Variants:

- **Submartingale**: $E[X_{t+1}\mid\mathcal{F}_t] \ge X_t$ — tends to rise (a favorable game; a stock with positive expected return).
- **Supermartingale**: $E[X_{t+1}\mid\mathcal{F}_t] \le X_t$ — tends to fall (an unfavorable game; a gambler facing a house edge).

### Link to the efficient-market hypothesis

The martingale property is the rigorous statement of the weak-form [[efficient-market-hypothesis]]. If a (discounted) price is a martingale, then no trading rule using only past prices can earn an above-risk-free expected return — because the expected change is zero by definition. This is subtly *weaker* and more accurate than the older "[[random-walk]]" claim: a random walk additionally assumes increments are i.i.d. (constant variance, independent), whereas a martingale only constrains the conditional *mean*. Real markets can be martingales (unforecastable mean) while still showing [[volatility-clustering]] (forecastable variance) — exactly what is observed. So the martingale model accommodates GARCH-style volatility dynamics that a strict random walk cannot.

### Link to option pricing

Under the **risk-neutral measure**, discounted asset prices are martingales — this is the first fundamental theorem of asset pricing and the reason an option's price equals the discounted risk-neutral expectation of its payoff. The Itô integral in [[stochastic-calculus]] is constructed precisely so that it is a martingale (non-anticipating, left-endpoint sampling), which is what makes arbitrage-free pricing via [[black-scholes]] and [[martingale|martingale-representation]] coherent. See [[stochastic-calculus]].

| Concept | Domain | One-line meaning |
|---------|--------|------------------|
| Martingale *betting system* | money management | Double after a loss → ruinous negative skew |
| Martingale *property* | probability | $E[X_{t+1}\mid\mathcal{F}_t]=X_t$ → fair game, no drift |
| Submartingale | probability | Expected to rise (positive-drift asset) |
| Supermartingale | probability | Expected to fall (house-edge game) |
| Anti-martingale | money management | Add after wins, cut after losses → survivable positive skew |

## Gambler's Ruin Connection

The martingale is the canonical case study for [[gamblers-ruin|gambler's ruin]]: a player with finite capital facing a fair-or-worse game and an opponent (the market/house) with effectively unlimited capital will, with probability approaching 1, eventually go bust. Doubling-up *accelerates* ruin rather than preventing it, because it maximises capital at risk exactly when a losing streak is in progress. The only robust defences are a real positive expectancy (an edge) plus sizing that survives the worst plausible streak — which is what [[kelly-criterion|Kelly]] and fixed-fractional methods provide and the martingale destroys.

## Trading Relevance — the Lessons

1. **Never increase exposure to "recover" losses.** Adding size to a losing position to lower the average price is martingale-flavoured; without an independent edge it converts a small loss into a ruin event.
2. **A high win rate is not an edge.** Expectancy (`win% × avg_win − loss% × avg_loss`) and the *tail* matter more than the hit rate. Martingale systems have great win rates and terrible expectancy after the tail is counted.
3. **Size as a fraction of equity, not a fixed nominal you "make back."** Fractional sizing guarantees you can always survive to trade again.
4. **Stress-test for the long adverse streak.** Compute [[risk-of-ruin]] over the worst run your strategy can plausibly face, not the average case.
5. **Prefer positive skew (anti-martingale).** Cut losers small, let winners run and add to them — the survivable distribution shape.

## Related

- [[kelly-criterion]] — optimal fractional sizing; the principled anti-martingale
- [[anti-martingale]] — the inverse, survivable sizing philosophy
- [[gamblers-ruin]] — why finite capital + doubling guarantees ruin
- [[risk-of-ruin]] — quantifying blow-up probability
- [[position-sizing]] / [[risk-management]] — fixed-fractional sizing that can't blow up
- [[averaging-down]] / [[grid-trading]] — common strategies that hide martingale risk
- [[leverage]] — what turns a martingale loss into a debt
- [[efficient-market-hypothesis]] — the martingale *property* is its rigorous statement
- [[random-walk]] — the stricter (i.i.d.) cousin of the martingale model
- [[stochastic-calculus]] — where the Itô integral is built to be a martingale, underpinning option pricing

## Sources

- Thorp, E. — *Beat the Dealer* / *The Kelly Capital Growth Investment Criterion* — the mathematics of bankroll sizing and why doubling-up fails.
- Kelly, J.L. (1956). *A New Interpretation of Information Rate*. *Bell System Technical Journal* — optimal growth-maximising fractional betting.
- Feller, W. — *An Introduction to Probability Theory and Its Applications* — the gambler's-ruin problem and martingale stopping times.
- Taleb, N.N. — *Fooled by Randomness* / *The Black Swan* — on win-small/lose-everything (negative-skew) payoff structures.
