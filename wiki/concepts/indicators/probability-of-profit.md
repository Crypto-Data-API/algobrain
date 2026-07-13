---
title: "Probability of Profit"
type: concept
created: 2026-05-03
updated: 2026-06-11
status: good
tags: [options, derivatives, indicators, risk-management]
aliases: ["PoP", "Probability of Profit", "Win Rate"]
domain: [risk-management, indicators]
prerequisites: ["[[options]]", "[[delta]]", "[[implied-volatility]]", "[[options-greeks]]"]
difficulty: intermediate
related: ["[[options]]", "[[delta]]", "[[theta]]", "[[implied-volatility]]", "[[iron-condors]]", "[[credit-spreads]]", "[[short-strangle]]", "[[options-greeks]]", "[[expected-value]]", "[[volatility-skew]]"]
---

Probability of Profit (PoP) is a model-derived statistical estimate of the likelihood that an [[options]] trade will close at or above its breakeven price by expiration. Brokers like tastytrade, thinkorswim, and Tradier display PoP next to every defined-risk options trade ticket; it is the single most-quoted "win rate" number in retail premium-selling and the metric that drives trade-selection rules of thumb such as "sell at 16-delta" or "target 70% PoP."

## How Brokers Compute PoP

Most retail platforms compute PoP from the same [[black-scholes]]/lognormal framework that prices the option itself. Given the current spot price, the strike, time to expiration, [[implied-volatility]], and the risk-free rate, the model produces a probability density for the underlying's terminal price. PoP is the integral of that density over the price region where the trade closes profitable (i.e., past breakeven). Because the inputs are the same as the pricing model, PoP is essentially a re-expression of the option's mid-price — it is *not* an independent forecast and contains no information beyond what the IV surface already encodes.

For a short put at strike K with credit C, breakeven is K - C, and PoP is the model-implied probability that the underlying finishes at or above K - C at expiry. For an [[iron-condors|iron condor]], PoP is the probability that the underlying finishes between the two breakeven points (short-call strike + credit, short-put strike - credit).

## PoP vs. Probability ITM vs. Probability of Touching

These three numbers are commonly confused on retail tickets, and the distinction matters:

| Metric | Question Answered | Typical Use |
|---|---|---|
| **Probability ITM (PITM)** | What's the chance the option finishes in the money at expiry? | Approximated by absolute [[delta]]; a 16-delta short put has ~16% PITM |
| **Probability of Touching (PoT)** | What's the chance the underlying touches the strike at any point before expiry? | Roughly **2× PITM** for OTM strikes; matters for stop-loss and early-management rules |
| **Probability of Profit (PoP)** | What's the chance the trade is profitable at expiry, given the credit received? | The credit shifts breakeven away from the strike, so PoP > (1 - PITM) for credit trades |

For a 16-delta short put sold for $1.50 credit on a $100 stock with strike $90:
- PITM ≈ 16% (chance stock finishes below $90)
- PoT ≈ 32% (chance stock touches $90 at some point)
- PoP ≈ 84% (chance stock finishes above breakeven of $88.50 — slightly *higher* than 1 − PITM because the credit pushes breakeven below the strike)

This is why retail premium-sellers fixate on the "sell-the-16-delta" rule: a short OTM put or call at 16-delta gives roughly 84% PoP at entry, which feels statistically comfortable even though the reward-to-risk is poor.

## Why Retail Targets 60-70% PoP

The tastytrade-style premium-selling literature popularized 60-70% PoP as the sweet spot for short [[credit-spreads|credit spreads]] and [[iron-condors]]. The reasoning:

- **Above 70% PoP**: Credits are tiny, so a single max-loss trade wipes out many wins. The risk-reward becomes lottery-ticket-like in the wrong direction.
- **Below 60% PoP**: Win rate drops below the psychological comfort zone and matches the credit closer to lottery-like upside (you're effectively buying directional exposure).
- **60-70% PoP zone**: Credits are meaningful (typically ~30-35% of spread width on credit spreads), wins are frequent enough to feel mechanical, and the trade can be repeated dozens of times per year for [[law-of-large-numbers|statistical convergence]].

## The PoP / Expected Value Trap

PoP is *not* the same as expected value (EV). A high-PoP trade can be negative-EV after costs. The math:

EV = (PoP × max profit) − ((1 − PoP) × max loss) − costs

Consider a $5-wide put credit spread sold for $1.00 credit:
- Max profit: $100 per contract
- Max loss: $400 per contract
- Broker-quoted PoP: 70%
- Expected value (gross): (0.70 × $100) − (0.30 × $400) = $70 − $120 = **−$50 per contract**

Even at a "comfortable" 70% PoP, this trade is a structural loser before commissions and slippage. The market — assuming no edge — prices PoP and credit such that EV ≈ 0 minus costs. Retail traders who chase high PoP without checking EV are paying the [[bid-ask-spread]] and exchange fees on a structurally fair bet.

The breakeven win-rate for this spread is credit / width = $1 / $5 = **20% loss rate** = 80% PoP required to be EV-positive. If the broker quotes 70% PoP, the trader needs an *informational edge* worth ~10% of win-rate to break even.

## Worked Example: Iron Condor PoP at Different Widths

SPY at $500, 45 DTE, IV ~15%. Trader sells an iron condor with short strikes at 16-delta on each side (call: $520, put: $480). PoP varies with the long-leg widths:

| Structure | Credit | Max Loss | PoP | Breakeven Win-Rate (no edge) | EV @ Quoted PoP |
|---|---|---|---|---|---|
| 5-wide condor (515/520, 480/485) | $1.50 | $350 | 76% | 70% (loss/(loss+win) = 350/500) | **+$30** |
| 10-wide condor (510/520, 480/470) | $3.00 | $700 | 73% | 70% | **+$21** |
| 20-wide condor (500/520, 480/460) | $5.50 | $1,450 | 68% | 72.5% | **−$90** |

The 20-wide structure has a *lower* PoP but a much larger absolute credit. The 5-wide structure is the highest-PoP version, but the credit is small and a single max loss wipes out 2-3 wins. The 10-wide is the conventional sweet spot — 73% PoP with sufficient credit that a single loss can be recovered with a few wins.

Note: the broker-quoted PoP assumes the lognormal model is correct. In reality, equity-index returns have fatter tails than lognormal predicts, so true PoP is typically *lower* than the displayed number — especially around earnings, FOMC, or other event windows.

## Limitations of PoP

- **Lognormal assumption**: Real return distributions have fat tails. Black-Monday-style moves are roughly 20+ standard deviations under the model, which the lognormal density says happens roughly never. They happen.
- **Ignores [[volatility-skew|skew]]**: PoP is symmetric in the model but real markets price downside puts richer than upside calls. Selling a 16-delta put is *not* statistically equivalent to selling a 16-delta call on SPX — the put-side has higher realized risk.
- **Assumes IV is correct**: If the option is mispriced (IV too low), the model-derived PoP is overstated. Selling cheap volatility before an event is the classic way to get the displayed PoP wrong.
- **No path dependency**: PoP is a terminal-value statistic. It says nothing about [[gamma-risk|gamma risk]] or [[max-adverse-excursion|drawdown]] along the way. A trade can be 84% PoP at entry and still have a 40% PoT, meaning the trade will *feel* like a loser at some point even if it ultimately wins.
- **Doesn't reflect early management**: Most retail traders close at 50% of max profit (a [[tastytrade-management|tastytrade rule]]), which raises realized win rate above the displayed PoP but lowers per-trade profit. PoP-as-displayed assumes hold-to-expiry.
- **Costs not included**: Commissions, exchange fees, bid-ask slippage, and assignment risk all shift the breakeven. A 70% PoP trade with $0.20 round-trip costs on a $1.00 credit needs effectively 75%+ realized win-rate to break even.

## How Pros Use PoP

Professional and semi-professional options traders treat PoP as a *sanity check*, not a decision rule:

1. Compute EV directly using the credit and max loss; verify it is positive *given an edge thesis*.
2. Cross-check displayed PoP against historical realized volatility — if the model uses 15% IV but realized vol is 22%, true PoP is far lower than displayed.
3. Adjust for skew: short puts on equity indices need a higher displayed PoP than short calls to match real-world equivalent risk.
4. Stress-test against fat-tail scenarios: what is the loss if the underlying gaps to the long strike overnight?

PoP is useful as a single-number summary for new traders and for comparing structures of similar type, but it should never be the sole input to a trade-go/no-go decision.

## Related

- [[options]] — overview of options contracts
- [[delta]] — approximates probability ITM, the input to PoP
- [[implied-volatility]] — the volatility input that drives PoP
- [[iron-condors]] — defined-risk structure where PoP is most commonly displayed
- [[credit-spreads]] — vertical structure with the same PoP/EV tradeoffs
- [[short-strangle]] — undefined-risk version with similar PoP framing
- [[options-greeks]] — the family of risk measures including delta
- [[volatility-skew]] — why model-PoP overstates true PoP on the put side
- [[expected-value]] — the proper decision metric that PoP feeds into

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
