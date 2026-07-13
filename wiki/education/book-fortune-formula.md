---
title: "Fortune's Formula — William Poundstone (2005)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, history, kelly-criterion, position-sizing, behavioral-finance]
source_type: book
source_author: "William Poundstone"
source_date: 2005
confidence: high
aliases: ["Fortune Formula", "Fortune's Formula", "Poundstone Kelly"]
related:
  - "[[kelly-criterion]]"
  - "[[position-sizing]]"
  - "[[edward-thorp]]"
  - "[[claude-shannon]]"
  - "[[information-theory]]"
  - "[[long-term-capital-management]]"
  - "[[risk-management]]"
  - "[[expected-utility]]"
---

## Overview

**Fortune's Formula: The Untold Story of the Scientific Betting System That Beat the Casinos and Wall Street** by William Poundstone, published in 2005, is the definitive popular history of the [[kelly-criterion]] — the optimal bet-sizing formula derived by Bell Labs scientist John Kelly in 1956 and applied by [[edward-thorp]] and [[claude-shannon]] to blackjack and the stock market with extraordinary results.

The book traces a 60-year arc: Shannon's information theory at Bell Labs → Kelly's reinterpretation of channel capacity as a betting formula → Thorp's deployment in Las Vegas blackjack and later in his hedge fund Princeton-Newport Partners → the broader adoption (and resistance) by Wall Street → and the conceptual collision with utility theory and the Markowitz framework that dominated academic finance.

## The Kelly Formula

Kelly's central result, in its simplest form for a binary bet:

```
f* = (bp - q) / b
```

Where `f*` = optimal fraction of bankroll to bet, `b` = odds, `p` = probability of winning, `q` = probability of losing.

The deeper claim: betting Kelly maximizes the long-run growth rate of the bankroll. Betting *more* than Kelly leads to ruin almost surely; betting *less* leaves growth on the table. The formula generalizes to multi-outcome bets, continuous distributions, and portfolios — though the multi-asset version requires solving an optimization that depends on the full joint distribution of returns.

For practical trading, "fractional Kelly" (typically 0.25× to 0.5× full Kelly) is preferred because:
- Edge estimates are noisy; full Kelly assumes perfect knowledge
- Drawdowns at full Kelly are gut-wrenching (50%+ pullbacks routine)
- The penalty for under-betting is roughly quadratic in distance from optimum, while the penalty for over-betting becomes linear and then catastrophic

## Key Takeaways

- **The Kelly criterion is a *growth-rate* optimum, not a utility optimum.** Maximizing long-run growth and maximizing expected utility are different objectives — though for log utility they coincide. This is the core academic dispute the book documents.
- **Position size, not signal selection, dominates long-run outcomes.** Two traders with identical signals but different sizing rules will end up in radically different places. Kelly is the mathematically privileged sizing rule for compounding capital.
- **Edward Thorp is the first quant.** Thorp built blackjack card-counting systems, ran a wildly successful market-neutral hedge fund (Princeton-Newport, 19% net for 19 years), and his methodology directly influenced [[long-term-capital-management|LTCM]], Renaissance, and modern statistical arbitrage.
- **Information theory is finance theory.** Shannon's framework — channel capacity, mutual information, entropy — maps directly onto trading: signal-to-noise ratio, information ratio, and the bound on growth from a given edge.
- **Claude Shannon was a serious investor.** Shannon's personal portfolio compounded at over 28% per year for several decades using a mix of growth stocks and a hand-coded rebalancing rule. The book documents his investing alongside his theoretical work.
- **Academia rejected Kelly for decades.** Paul Samuelson and the utility-theory establishment dismissed Kelly's work for being "wrong" by the standards of expected utility maximization. Thorp's empirical success eventually forced a partial reconciliation.
- **The mafia and the LTCM blow-up bookend the story.** Poundstone's narrative connects horse-race betting syndicates, casino countermeasures, and the leverage ratios that destroyed LTCM (which under-respected Kelly's lessons about position sizing under uncertainty).
- **Geometric mean > arithmetic mean for compounding.** A trade with 50% expected return and 50% volatility has a *negative* geometric mean. Kelly forces traders to think geometrically.

## Who Should Read This

Every trader. The Kelly criterion is the single most important concept in [[position-sizing]], and Poundstone's narrative makes the math intuitive without sacrificing rigor. Traders who size positions by gut, by fixed dollar amount, or by fixed fraction of equity will find Kelly mathematically compelling — and the historical case studies (Thorp, Shannon, the LTCM contrast) cement the lessons.

## How It Applies to AI Trading

Three direct applications:

1. **Bet sizing in systematic strategies.** Once a strategy has an edge estimate (mean and variance of expected returns), Kelly gives the optimal leverage. Most live systematic shops run fractional Kelly with periodic re-estimation.
2. **Strategy combination.** When combining N independent strategies, the Kelly framework gives optimal weights. This is a generalization of [[markowitz-portfolio-theory]] that explicitly maximizes geometric growth.
3. **Risk-of-ruin calculation.** Kelly's framework lets you compute exact ruin probabilities for any bet sizing rule. Many "blow-up" stories trace to bet sizes that exceeded Kelly by factors of 2-5x.

ML practitioners should pair Kelly with cross-validation to avoid the classic mistake of betting on in-sample edge that doesn't survive out-of-sample. The recommended workflow: estimate edge with walk-forward methodology, apply 0.25× Kelly on the *lower bound* of the estimate, then scale up only with live evidence.

## Rating

**9/10** — Engaging, rigorous, and historically rich. The narrative occasionally meanders (mafia subplots, casino lore) but the core material on Kelly and Thorp is essential. Read alongside Thorp's own *A Man For All Markets* for the practitioner's perspective.

## Sources

- Poundstone, William (2005). *Fortune's Formula: The Untold Story of the Scientific Betting System That Beat the Casinos and Wall Street*. Hill and Wang.

## Related

- [[kelly-criterion]] — The formula at the heart of the book
- [[position-sizing]] — Practical applications of Kelly
- [[edward-thorp]] — Protagonist and Kelly's most successful practitioner
- [[claude-shannon]] — Information theorist whose work inspired Kelly
- [[information-theory]] — The mathematical foundation
- [[long-term-capital-management]] — Counterexample of what happens without Kelly discipline
- [[risk-management]] — The broader context
- [[a-man-for-all-markets|A Man for All Markets (Thorp)]] — Thorp's own memoir
