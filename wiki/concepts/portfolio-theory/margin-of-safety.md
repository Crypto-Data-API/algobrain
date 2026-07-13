---
title: Margin of Safety
type: concept
created: 2026-04-06
updated: 2026-07-01
status: good
tags:
  - fundamental-analysis
  - portfolio-theory
  - valuation
  - risk-management
aliases:
  - margin-of-safety
  - "Margin of Safety"
domain: [portfolio-theory]
prerequisites: ["[[fundamental-analysis]]", "[[value-investing]]"]
difficulty: beginner
related:
  - "[[benjamin-graham]]"
  - "[[value-investing]]"
  - "[[warren-buffett]]"
  - "[[discounted-cash-flow]]"
  - "[[economic-moat]]"
  - "[[risk-management]]"
---

# Margin of Safety

**Margin of safety** is a principle introduced by [[benjamin-graham]] that advocates buying securities at a significant discount to their intrinsic value. The gap between price and value provides a buffer against errors in analysis or unforeseen events.

This concept is foundational to [[value-investing]] and was later championed by [[warren-buffett]] and [[charlie-munger]].

## The Core Idea

Graham articulated the margin of safety in [[the-intelligent-investor]] (1949) as the central concept of investment. The logic is straightforward: if you estimate a stock's intrinsic value at $100 and buy it at $70, you have a 30% margin of safety. Even if your valuation is somewhat wrong -- perhaps the true value is only $85 -- you still purchased below fair value. The margin of safety protects against analytical errors, unexpected downturns, and the inherent unpredictability of business.

## How to Calculate

The basic formula is:

**Margin of Safety = (Intrinsic Value - Market Price) / Intrinsic Value**

If intrinsic value is $50 and market price is $35, the margin of safety is 30%. Graham typically looked for margins of at least 33%, and preferably 50% for riskier situations. The challenge lies in estimating intrinsic value itself, which requires [[fundamental-analysis]] through discounted cash flow models, asset-based valuation, or earnings power analysis.

## Buffett's Interpretation

[[warren-buffett]] extended Graham's framework. While Graham focused on statistical cheapness (buying stocks below net current asset value), Buffett -- influenced by [[charlie-munger]] -- broadened the concept to include qualitative factors. A company with a durable competitive moat, excellent management, and strong pricing power inherently provides a margin of safety even at a higher price-to-earnings multiple, because its future earnings are more predictable.

Buffett famously summarized the idea: "In the short run, the market is a voting machine, but in the long run, it is a weighing machine." The margin of safety allows investors to survive the voting machine's irrationality while waiting for the weighing machine to recognize true value.

## Practical Application

In practice, margin of safety applies beyond individual stock selection. It informs position sizing (larger margin = larger position), portfolio construction (avoiding concentrated bets where margins are thin), and risk management (selling when prices exceed intrinsic value and margin disappears).

## Worked Example (Illustrative)

The numbers below are hypothetical and exist only to show the arithmetic — they are not a recommendation or a real valuation.

Assume an analyst runs a [[discounted-cash-flow|DCF]] on a stable consumer-staples company and arrives at an intrinsic value of **$100/share**. To respect the uncertainty in that estimate, they build the position around scenarios rather than a single point:

| Scenario | Estimated intrinsic value | Probability |
|----------|--------------------------|-------------|
| Bear (margins compress) | $70 | 25% |
| Base | $100 | 50% |
| Bull (share gains) | $125 | 25% |

The probability-weighted value is 0.25×70 + 0.50×100 + 0.25×125 = **$98.75**, and — crucially — even the *bear* case is $70.

- **Buy at $70:** margin of safety = (100 − 70) / 100 = **30%**. The price already sits at the pessimistic estimate, so the analyst is being paid to take a bet whose downside is largely priced in. Graham's classic threshold (≥33%) is nearly met.
- **Buy at $95:** margin of safety = **5%**. A 5% error in the DCF erases the entire cushion. This is "paying up for quality" — defensible only if the business is exceptionally predictable (Buffett's extension), reckless otherwise.
- **Buy at $110:** margin of safety is **negative**. You are paying more than even the bull case is worth and relying on someone else paying still more — speculation, not investing.

The lesson: the margin of safety is a buffer against *being wrong about intrinsic value*, not merely a discount to a number you assume is correct.

## Limitations and Pitfalls

- **Garbage in, garbage out.** The whole framework rests on an intrinsic-value estimate. If the DCF assumptions (growth, discount rate, terminal value) are wrong, a large "margin" is illusory. The discount protects against *modest* error, not a broken thesis.
- **[[value-trap|Value traps]].** A stock that looks 40% cheap can be cheap *because* the business is permanently impaired (eroding [[economic-moat|moat]], structural decline, accounting issues). The margin of safety only works if intrinsic value is stable; a melting ice cube has no floor.
- **Opportunity cost and dead money.** Deeply discounted stocks can stay discounted for years. The buffer protects capital but does not guarantee a timely return — the market may take a long time to act as a "weighing machine."
- **Hard to apply to growth and intangibles.** Graham's statistical cheapness was built for asset-heavy, predictable businesses. For high-growth or intangible-heavy firms, intrinsic value is so sensitive to assumptions that a precise margin of safety is difficult to define — part of why Buffett shifted toward qualitative moat analysis.
- **Behaviorally hard to use.** Margins of safety are widest exactly when sentiment is most negative (recessions, crashes), which is when [[loss-aversion]] and [[herding]] make buying psychologically hardest. The concept is simple; the discipline is not.

## Related

- [[benjamin-graham]]
- [[the-intelligent-investor]]
- [[value-investing]]
- [[warren-buffett]]
- [[charlie-munger]]
- [[fundamental-analysis]]
- [[discounted-cash-flow]]
- [[economic-moat]]
- [[value-trap]]
- [[risk-management]]

## Sources

- Graham, B. (1949). *The Intelligent Investor*, esp. Ch. 20 "Margin of Safety as the Central Concept of Investment."
- Graham, B. and Dodd, D. (1934). *Security Analysis*.
- Berkshire Hathaway shareholder letters (Warren Buffett) — the qualitative extension of the margin-of-safety concept to durable competitive advantage.
