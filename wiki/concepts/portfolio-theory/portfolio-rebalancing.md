---
title: "Portfolio Rebalancing"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [portfolio-theory, risk-management]
aliases: ["Rebalancing"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[portfolio-construction]]", "[[diversification]]"]
difficulty: beginner
related: ["[[portfolio-construction]]", "[[diversification]]", "[[risk-management]]", "[[modern-portfolio-theory]]", "[[asset-allocation]]"]
---

Portfolio rebalancing is the process of periodically realigning portfolio weights back to a target allocation by selling assets that have grown beyond their target weight and buying assets that have fallen below it. It enforces a systematic "buy low, sell high" discipline and prevents unintended risk concentration.

## Why Rebalance?

Without rebalancing, a portfolio naturally drifts as different assets produce different returns. Consider a simple 60/40 stocks/bonds portfolio:
- After a strong equity year, it might drift to 70/30
- The portfolio now has more equity [[risk-management|risk]] than intended
- If stocks decline, the unrebalanced portfolio suffers larger losses

Rebalancing restores the intended risk profile and has been shown to modestly improve risk-adjusted returns over long periods by systematically trimming winners and adding to losers.

## Rebalancing Methods

### Calendar Rebalancing
Rebalance at fixed time intervals regardless of drift:
- **Monthly**: More responsive but higher [[transaction-costs|transaction costs]] and tax events
- **Quarterly**: Common institutional frequency -- balances responsiveness with costs
- **Annually**: Simplest approach, suitable for long-term investors

### Threshold Rebalancing
Rebalance only when an asset's weight drifts beyond a specified band:
- **Narrow band** (e.g., +/- 3%): More frequent rebalancing, tighter tracking
- **Wide band** (e.g., +/- 10%): Less frequent, lower costs, more drift tolerance
- **Advantage**: Only trades when necessary, avoiding unnecessary turnover in quiet markets

### Threshold + Calendar (Hybrid)
Check at fixed intervals but only rebalance if drift exceeds the threshold. Combines the discipline of calendar-based checks with the cost efficiency of threshold-based execution.

### Tactical Rebalancing
Adjust target weights based on market views before rebalancing:
- Overweight assets expected to outperform
- Underweight assets expected to underperform
- Blends strategic asset allocation with active management
- Requires conviction in market timing -- evidence suggests most investors are better served by mechanical rebalancing

## Rebalancing Costs

Rebalancing is not free. Costs include:
1. **[[transaction-costs|Transaction costs]]**: [[fees|Trading fees]], bid-ask spreads, and [[slippage]]
2. **Tax drag**: Selling appreciated assets triggers capital gains taxes (in taxable accounts)
3. **Opportunity cost**: Selling winners too early may sacrifice momentum gains

### Tax-Efficient Rebalancing Techniques
- **Direct new contributions** to underweight assets instead of selling overweight ones
- **Rebalance within tax-advantaged accounts** (IRA, 401k) to avoid taxable events
- **Tax-loss harvesting**: Sell underperforming assets to realize losses, then rebalance with the proceeds
- **Asset location**: Hold tax-inefficient assets in tax-advantaged accounts, reducing the tax cost of rebalancing

## Academic Evidence

Research supports rebalancing as a risk management tool but with nuanced conclusions:
- Rebalancing **reduces portfolio risk** (standard deviation and max drawdown) relative to buy-and-hold
- The **return benefit** is modest and period-dependent -- in strong trending markets, buy-and-hold outperforms (because rebalancing trims the winning asset)
- **Frequency matters less than expected**: Monthly, quarterly, and annual rebalancing produce similar long-term results, with quarterly being a common sweet spot
- The "rebalancing bonus" (excess return from mean-reverting asset classes) is real but small (estimated 0.1-0.5% annually)

## Application to Trading Strategies

- **[[risk-parity]]**: Requires frequent rebalancing to maintain equal risk contribution across assets
- **[[portfolio-construction|ITPM portfolio management]]**: Rebalancing option positions to maintain target Greeks and portfolio exposure
- **Crypto portfolios**: High [[volatility]] causes rapid drift, requiring more frequent rebalancing -- but high [[fees]] on some networks offset the benefit
- **Factor portfolios**: Periodic rebalancing to maintain target factor exposures (value, momentum, quality)

## Related

- [[portfolio-construction]] -- Designing the target allocation that rebalancing maintains
- [[diversification]] -- Rebalancing preserves the diversification benefit across asset classes
- [[risk-management]] -- Rebalancing as a risk control mechanism
- [[modern-portfolio-theory]] -- Theoretical basis for optimal portfolio weights

## Sources

- Portfolio rebalancing is a core topic in [[modern-portfolio-theory|MPT]] and investment management literature
