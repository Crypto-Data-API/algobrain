---
title: "Disposition Effect"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [behavioral-finance, psychology, risk-management]
aliases: ["disposition bias", "Shefrin-Statman Disposition Effect", "Hold Losers Sell Winners"]
domain: [behavioral-finance]
difficulty: intermediate
prerequisites: ["[[prospect-theory]]", "[[loss-aversion]]"]
related: ["[[prospect-theory]]", "[[loss-aversion]]", "[[anchoring-bias]]", "[[behavioral-finance]]", "[[cognitive-biases]]", "[[overconfidence-bias]]", "[[confirmation-bias]]", "[[daniel-kahneman]]", "[[richard-thaler]]", "[[trading-psychology]]", "[[risk-management]]"]
---

The disposition effect is the well-documented tendency of investors to sell winning positions too early and hold losing positions too long. First formally described by Hersh Shefrin and Meir Statman in 1985, it is one of the most robust and costly behavioral biases in trading, driven by the interaction of [[prospect-theory|prospect theory's]] [[loss-aversion]] and reference-point dependence.

## The Evidence

### Odean (1998)

Terrance Odean's landmark study of 10,000 individual brokerage accounts found:

- Investors were **50% more likely to sell a winning position** than a losing one
- This pattern held across virtually all account sizes and experience levels
- The sold winners subsequently outperformed the held losers by an average of **3.4 percentage points** over the following 12 months
- The effect was not tax-motivated — it persisted even in December when tax-loss harvesting should dominate

### Additional Evidence

- The disposition effect has been replicated across US equities, Finnish stocks, Israeli IPOs, Chinese markets, Australian futures, and even cryptocurrency markets
- Professional traders show a weaker disposition effect than retail traders, but it is not eliminated by experience
- The effect is stronger for individual stocks than for index funds, suggesting that it is amplified by the salience of individual position P&L

## Why It Happens

### Prospect Theory Mechanism

[[prospect-theory]] explains the disposition effect through two features of the value function:

1. **Concavity in gains**: Once a position is in profit, the marginal happiness from additional gains decreases. A $500 gain doesn't feel much better than a $400 gain. This creates a desire to lock in the gain — to move from the risky "open position" to the certain "realized profit"

2. **Convexity in losses**: When a position is underwater, the marginal pain from additional losses decreases. Being down $500 doesn't feel much worse than being down $400. This creates risk-seeking behavior — a willingness to gamble on recovery rather than accept the certain pain of realization

3. **Reference point**: The purchase price serves as the reference that defines "gain" and "loss." This is pure [[anchoring-bias]] — the market does not care about your entry price

### Mental Accounting

[[richard-thaler|Thaler's]] mental accounting framework adds another layer: traders maintain a mental account for each position and resist "closing the account" at a loss. Closing a losing position feels like admitting a mistake and making the loss "real," even though the economic loss already exists.

## The Cost

The disposition effect is expensive in two ways:

1. **Selling winners cuts off trends**: Winning positions often have positive [[momentum]] — the fundamentals or technicals that caused the initial gain may still be operating. Selling too early sacrifices the tail of the distribution where the largest gains occur

2. **Holding losers compounds drawdowns**: Losing positions often continue losing because the factors causing the decline persist. Holding them ties up capital that could be redeployed to better opportunities and allows losses to grow

Combined, these effects can reduce annual returns by several percentage points.

## Counter-Strategies

### Mechanical Exit Rules

The most effective counter is removing discretion from exit decisions:
- **Trailing stops** — automatically sell when price retraces a defined percentage from its high, letting winners run while capping losses
- **Time-based exits** — close positions after a fixed holding period regardless of P&L
- **Target-based exits** — set price targets at trade entry and honor them
- **Condition-based exits** — define specific fundamental or technical conditions that must be met to hold

### Reframing the Question

Instead of "should I sell this position?", ask: **"If I had no position, would I buy this stock today at the current price?"** This reframe neutralizes the [[anchoring-bias|anchoring]] to entry price and the [[endowment-effect|endowment effect]].

### Portfolio-Level Thinking

Viewing the portfolio as a whole rather than position-by-position reduces the salience of individual position gains and losses. This is why systematic, rule-based strategies outperform discretionary approaches for most traders — they enforce portfolio-level discipline.

### Reducing Check Frequency

[[richard-thaler|Thaler's]] myopic loss aversion research suggests that checking positions less frequently reduces the emotional triggers that drive the disposition effect. Traders who check P&L daily make worse disposition-related decisions than those who check less often.

## Related

- [[prospect-theory]] — the theoretical foundation explaining the disposition effect
- [[loss-aversion]] — the core asymmetry that drives reluctance to sell losers
- [[anchoring-bias]] — fixation on entry price as the reference point
- [[confirmation-bias]] — supports holding losers by selectively processing information
- [[overconfidence-bias]] — overconfident traders believe losers will recover
- [[richard-thaler]] — mental accounting framework adds explanation
- [[daniel-kahneman]] — prospect theory co-developer
- [[trading-psychology]] — practical application of bias management
- [[risk-management]] — mechanical rules to counteract the disposition effect

## Sources

- Shefrin, H. & Statman, M. (1985) "The Disposition to Sell Winners Too Early and Ride Losers Too Long: Theory and Evidence," *Journal of Finance* 40(3):777-790 — the paper that named the effect.
- Odean, T. (1998) "Are Investors Reluctant to Realize Their Losses?" *Journal of Finance* 53(5):1775-1798 — the 10,000-account empirical study.
- Kahneman, D. & Tversky, A. (1979) "Prospect Theory" — the underlying value-function asymmetry.
- Thaler, R. (1985) "Mental Accounting and Consumer Choice," *Marketing Science* — the mental-accounting layer.
- [[book-thinking-fast-and-slow]] — accessible treatment of the prospect-theory mechanism.
