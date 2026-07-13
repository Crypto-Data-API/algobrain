---
title: "Hedging"
type: concept
created: 2026-04-07
updated: 2026-04-20
status: good
tags: [risk-management, options, portfolio-theory]
aliases: ["Hedge", "Hedged Position", "Portfolio Hedging"]
related: ["[[delta-neutral]]", "[[options-greeks]]", "[[delta]]", "[[put-options]]", "[[covered-call]]", "[[collar]]", "[[pairs-trading]]", "[[risk-management]]", "[[options]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[protective-puts]]"]
domain: [risk-management, portfolio-theory]
difficulty: intermediate
---

**Hedging** is the practice of taking an offsetting position to reduce or eliminate specific risks in a portfolio. Rather than removing exposure entirely (which would also remove potential gains), hedging aims to limit downside while preserving acceptable upside. It is the financial equivalent of insurance -- you pay a cost (the hedge) to protect against a potentially larger loss.

## Overview

Hedging is a cornerstone of professional portfolio management. Every institutional investor, market maker, and sophisticated retail trader uses some form of hedging. The key insight is that different risks can be isolated and managed independently: a trader can hedge directional risk while retaining volatility exposure, or hedge market risk while retaining stock-specific exposure.

The cost of hedging is unavoidable. A perfect hedge eliminates both risk and reward. Practical hedging involves choosing which risks to retain (where the trader has an edge) and which to hedge away (where the trader has no edge or where the risk is unacceptable). As [[ed-thorp]] demonstrated, the ability to hedge precisely is what transforms speculation into systematic investing.

## How It Works

### Options-Based Hedging

Options are the most versatile hedging instruments because they provide asymmetric protection:

- **Protective puts**: Buying [[put-options]] against a long stock position creates a floor on losses. The stock can still rise, but losses below the put's strike price are limited. Cost: the put premium.
- **[[collar]]**: Buying a protective put and simultaneously selling a [[call-option|covered call]] to offset the cost. Limits both downside and upside, often for near-zero net cost. Used extensively by executives hedging concentrated stock positions.
- **Index puts**: Buying puts on a broad index (S&P 500, Nasdaq) to hedge a diversified portfolio against market-wide declines. The hedge is imperfect (basis risk) unless the portfolio closely tracks the index.
- **[[covered-call]]**: Selling calls against long stock reduces downside by the premium received but caps upside. A partial hedge -- more of an income/risk-reduction strategy than pure protection.

### Delta Hedging

[[delta-neutral]] hedging eliminates directional risk by balancing the delta of an options position with an offsetting position in the underlying:

1. Calculate the total delta of the options position
2. Buy or sell shares/futures to bring net delta to zero
3. As the underlying moves and delta shifts (due to [[gamma]]), rebalance periodically

This is the core hedging technique used by options market makers. The cost of delta hedging in practice comes from transaction costs and the gamma-theta tradeoff -- frequent rehedging captures gamma profits but is expensive to execute.

### Pairs and Statistical Hedging

- **[[pairs-trading]]**: Going long one stock and short a correlated stock, hedging sector or market risk while expressing a view on the relative performance of the two names.
- **Beta hedging**: Shorting an index or ETF in proportion to a portfolio's beta to isolate stock-specific (alpha) returns from market returns.
- **long-short-equity**: Running a portfolio with both long and short positions, adjusting the ratio to control net market exposure. Hedge funds use this approach to extract alpha regardless of market direction.

### Futures Hedging

- **Portfolio hedging with futures**: Selling index futures against a stock portfolio provides a quick, liquid, cost-effective hedge. The margin requirements are lower than buying puts, but the hedge is symmetric (you give up upside too).
- **Commodity hedging**: Producers and consumers of commodities (oil, grain, metals) use futures to lock in prices. Airlines hedge jet fuel costs; farmers hedge crop prices.
- **Currency hedging**: International investors use currency futures or forwards to neutralize exchange rate risk in foreign holdings.

## Cost of Hedging

Every hedge has a cost, which takes various forms:

- **Explicit cost**: Premium paid for options (puts, collars)
- **Opportunity cost**: Upside foregone (covered calls, futures hedges)
- **Basis risk**: The hedge may not perfectly offset the position being hedged (e.g., hedging a tech portfolio with S&P 500 puts)
- **Transaction costs**: Commissions, bid-ask spreads, and slippage on the hedging instruments
- **Drag on returns**: A permanently hedged portfolio will underperform an unhedged portfolio in rising markets

The art of hedging is determining when the cost of protection is justified by the risk being hedged. Many traders use a "tail risk hedging" approach -- maintaining cheap, far out-of-the-money puts that cost little in normal markets but provide significant protection in crashes.

## Trading Applications

- **Portfolio protection**: Long-only investors buy index puts or use collars to protect against drawdowns, particularly before known risk events (elections, earnings seasons, rate decisions).
- **Market making**: Market makers delta-hedge continuously to isolate the bid-ask spread profit from directional risk. Without hedging, market making would be indistinguishable from speculation.
- **Earnings hedging**: Traders hedge stock-specific risk around earnings by buying protective puts or selling covered calls, reducing the impact of the binary event.
- **Tail risk management**: Allocating a small percentage of portfolio value (e.g., 0.5-1% per year) to far OTM puts that pay off in crash scenarios. This approach is associated with Nassim Taleb's [[black-swan]] philosophy.
- **Concentrated position management**: Executives and founders with large holdings in a single stock use collars, prepaid forwards, and other structures to reduce concentration risk without triggering taxable sales.

## Hedging as Recovery

Hedging is not only a preventative tool — it is also one of the five pillars of the professional options recovery playbook. When a portfolio is losing due to directional exposure, adding hedging overlays ([[protective-puts]], [[collar|collars]], index puts) can stabilize the P&L without requiring the trader to close losing positions. This buys time for the original thesis to play out. See [[trade-repair-and-rolling]] for how hedging fits into the broader recovery framework alongside rolling, spread conversion, and position sizing. (Source: [[recovering-losing-options-positions]])

## Related

- [[delta-neutral]]
- [[options-greeks]]
- [[delta]]
- [[gamma-risk]] — understanding how gamma drives hedging urgency near expiration
- [[put-options]]
- [[protective-puts]] — the most common options-based hedge
- [[covered-call]]
- [[collar]]
- [[trade-repair-and-rolling]] — hedging as part of the professional recovery playbook
- [[pairs-trading]]
- [[risk-management]]
- [[options]]
- [[black-swan]]

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg covers options-based hedging mechanics and the delta hedging process in depth
- [[book-a-man-for-all-markets]] — Thorp's pioneering work in hedged strategies, from warrant hedging to statistical arbitrage, demonstrates the power of precise risk neutralization
- (Source: [[recovering-losing-options-positions]]) — Hedging overlays as part of the five-pillar professional recovery framework
