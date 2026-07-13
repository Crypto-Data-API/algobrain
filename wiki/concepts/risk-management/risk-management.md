---
title: "Risk Management"
type: concept
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [risk-management, portfolio-theory, leverage, volatility, correlation]
aliases: ["Risk Mgmt"]
domain: [risk-management]
prerequisites: []
difficulty: beginner
related:
  - "[[risk-management-overview]]"
  - "[[leverage]]"
  - "[[position-sizing]]"
  - "[[stop-loss]]"
  - "[[value-at-risk]]"
  - "[[maximum-drawdown]]"
  - "[[sharpe-ratio]]"
  - "[[sortino-ratio]]"
  - "[[kelly-criterion]]"
  - "[[drawdown]]"
  - "[[hedging]]"
  - "[[derisking]]"
  - "[[correlation]]"
  - "[[diversification]]"
---

# Risk Management

**Risk management** is the practice of identifying, assessing, and controlling potential financial losses in trading. It is the single most important discipline a trader can develop -- without it, even the best strategy will eventually lead to ruin.

For the comprehensive guide covering position sizing, stop losses, risk/reward ratios, the mathematics of drawdowns, and practical risk frameworks, see the main article:

**Main article: [[risk-management-overview|Risk Management (Full Guide)]]**

## The First Principle: Survival Before Return

Every risk framework rests on one asymmetry: losses and the gains required to recover them are not symmetric. A drawdown of *x* percent requires a gain of *x / (1 - x)* to return to the prior peak. The cost of a loss accelerates non-linearly, which is why capping the *depth* of drawdowns matters far more than maximising the height of returns.

| Drawdown | Gain needed to recover | Practical reading |
|----------|------------------------|-------------------|
| 5%  | 5.3%   | Routine; recovered in weeks |
| 10% | 11.1%  | Normal pullback; recoverable |
| 20% | 25%    | Painful but survivable |
| 33% | 50%    | Serious; threatens discipline |
| 50% | 100%   | Must double to break even |
| 75% | 300%   | Near-terminal for most accounts |
| 90% | 900%   | Effectively unrecoverable |

The corollary is the core mandate of risk management: **stay in the game**. A trader who never risks ruin can compound an edge indefinitely; a trader who occasionally bets the account converts a positive-expectancy edge into eventual [[risk-of-ruin|ruin]] with probability approaching 1 over enough trials. This is why position sizing and drawdown control dominate strategy selection in determining long-run wealth (see [[ergodicity-economics]] and [[kelly-criterion]]).

## Types of Risk

### Market Risk

The risk of losses from adverse price movements. This is the most obvious risk in trading and includes:

- **Directional risk**: Exposure to price moving against your position
- **[[volatility]] risk**: Unexpected changes in the magnitude of price swings
- **Gap risk**: Price jumping past stop levels overnight or over weekends
- **[[tail-risk|Tail risk]]**: Extreme moves that exceed historical norms (see [[black-swan]])

### Credit and Counterparty Risk

The risk that the other party in a transaction fails to honor their obligation:

- **Broker insolvency**: Loss of funds if a broker fails (partially mitigated by SIPC insurance in the US)
- **[[counterparty-risk]]**: In OTC derivatives or DeFi, the counterparty may default
- **Exchange risk**: Centralized crypto exchanges can be hacked or collapse (see [[rug-pulls]])

### Liquidity Risk

The risk of being unable to exit a position at a reasonable price:

- **[[liquidity-risk]]**: Wide [[bid-ask-spread|bid-ask spreads]] or insufficient order book depth
- **Market impact**: Large orders moving the price against you (see [[market-impact]])
- **[[slippage]]**: Fills at worse prices than expected, especially during volatile periods

### Operational Risk

Risks from systems, processes, or human error:

- **Technology failures**: Platform outages, data feed disruptions, API errors
- **Order errors**: Incorrect position sizes, wrong direction, fat-finger trades
- **Infrastructure**: Power outages, internet failures during critical moments

### Model Risk

The risk that a trading model or strategy is flawed:

- **[[model-risk]]**: Strategies based on incorrect assumptions or [[overfitting-in-trading|overfitted]] parameters
- **Regime change**: Models trained on one market regime failing in another
- **[[crowding-risk]]**: Too many traders using the same strategy, eroding the edge

### Risk Type Summary

The risk categories above are not independent — a single crisis event activates several at once. The table maps each type to its primary mitigation and the wiki page that treats it in depth.

| Risk type | Manifests as | Primary mitigation | Page |
|-----------|--------------|--------------------|------|
| Market (directional) | Price moves against the position | [[position-sizing]], [[stop-loss]] | [[market-risk]] |
| Volatility | Magnitude of swings changes | [[vega-budgeting]], [[volatility-targeting]] | [[volatility]] |
| Gap / tail | Overnight or weekend jumps past stops | Defined-risk structures, [[tail-risk]] hedges | [[tail-risk]] |
| Liquidity | Cannot exit at a fair price | Trade liquid instruments, size to depth | [[liquidity-risk]] |
| Counterparty / credit | Broker, exchange, or OTC desk defaults | Diversify custody, SIPC/segregation | [[counterparty-risk]] |
| Operational | Outage, fat-finger, data error | Checklists, redundancy, hard limits | [[model-risk]] |
| Model / strategy | Edge was illusory or [[overfitting-in-trading\|overfit]] | Out-of-sample testing, [[deflated-sharpe-ratio]] | [[model-risk]] |
| Crowding | Edge decays as others copy it | Capacity awareness, decay monitoring | [[crowding-risk]] |

## Risk Metrics

### Value at Risk (VaR)

[[value-at-risk|Value at Risk (VaR)]] estimates the maximum expected loss over a given time period at a specified confidence level. For example, "1-day 95% VaR of $10,000" means there is a 95% probability that losses will not exceed $10,000 in a single day.

- Simple to communicate and widely used by institutions
- Limitations: does not describe the magnitude of losses beyond the VaR threshold
- See [[expected-shortfall|CVaR (Conditional VaR)]] for the expected loss in the tail beyond VaR

### Maximum Drawdown

[[maximum-drawdown|Maximum drawdown]] measures the largest peak-to-trough decline in portfolio value:

- Critical for assessing survivability: a 50% drawdown requires a 100% gain to recover
- Historical max drawdown understates future potential drawdown
- See [[drawdown-management]] for strategies to manage and recover from drawdowns

### Sharpe Ratio

The [[sharpe-ratio|Sharpe ratio]] measures risk-adjusted return: (Return - Risk-Free Rate) / Standard Deviation of Returns.

- Sharpe > 1.0 is generally considered acceptable; > 2.0 is strong
- Assumes normally distributed returns, which is often violated in practice
- See [[deflated-sharpe-ratio]] for adjustments accounting for multiple testing

### Sortino Ratio

The [[sortino-ratio|Sortino ratio]] is a modification of the Sharpe ratio that only penalizes downside volatility:

- More appropriate than Sharpe for strategies with asymmetric return profiles
- Better reflects the actual experience of a trader (upside volatility is welcome)

### Other Key Metrics

- **[[risk-of-ruin]]**: Probability of losing enough capital to be unable to continue trading
- **Profit factor**: Gross profit / Gross loss -- must exceed 1.0 to be profitable
- **Win rate vs payoff ratio**: A 30% win rate is fine if winners are 3x larger than losers
- **[[sharpe-sortino-calmar|Calmar ratio]]**: Annualized return / Max drawdown

## Position Sizing Methods

### Fixed Fractional

Risk a fixed percentage of account equity per trade (typically 1-2%):

```
Position Size = (Account Equity x Risk %) / (Entry Price - Stop Loss Price)
```

This is the most widely recommended approach for its simplicity and automatic deleveraging during drawdowns. See [[position-sizing]] for detailed implementation.

### Kelly Criterion

The [[kelly-criterion|Kelly criterion]] calculates the theoretically optimal bet size based on win probability and payoff ratio:

```
Kelly % = W - (1 - W) / R
```

Where W = win probability, R = win/loss ratio. In practice, traders use "half Kelly" or "quarter Kelly" because:

- Full Kelly assumes known, stable probabilities (rarely true in markets)
- Full Kelly produces extreme volatility and drawdowns
- Estimation errors in win rate or payoff can lead to over-betting

### Volatility Targeting

Size positions inversely to their [[volatility]]:

- High-volatility assets get smaller positions; low-volatility assets get larger positions
- Normalizes the dollar risk contribution of each position
- Used in [[risk-parity]] and many institutional systematic strategies
- See [[atr-position-sizing|ATR position sizing]] for a practical implementation

## Stop Loss Types

### Fixed Stop

A stop at a predetermined price level or percentage:

- Simple to implement and backtest
- Does not adapt to market conditions
- Risk of being stopped out by normal [[volatility]] before the trade thesis plays out

### Trailing Stop

A stop that moves with the price to lock in profits:

- Captures trends while protecting gains
- Can use fixed distance, ATR-based distance, or percentage-based distance
- Risk: in choppy markets, trailing stops get triggered frequently

### Volatility-Based Stop

Stop distance set as a multiple of [[volatility]] (typically ATR):

- Adapts to current market conditions automatically
- Wide stops in volatile markets, tight stops in calm markets
- Example: stop at 2x ATR(14) below entry

### Time-Based Stop

Exit a trade after a specified period regardless of P&L:

- Prevents capital from being tied up in stagnant positions
- Useful for event-driven strategies with a defined thesis window
- Common in options trading where [[theta]] decay is a factor

See [[stop-loss]] for a comprehensive treatment of stop loss strategies.

## Portfolio-Level Risk

### Correlation and Diversification

Individual position risk is only part of the picture. Portfolio-level risk depends on how positions interact:

- **[[correlation]]**: Highly correlated positions compound risk -- ten "different" stocks in the same sector may behave as one large position
- **[[diversification]]**: Genuine risk reduction requires assets with low or negative [[correlation]]
- **[[strategy-correlation-matrix]]**: When running multiple strategies, their return correlation determines overall portfolio risk

### Sector and Factor Exposure

- Concentrated sector exposure creates hidden risk (e.g., "diversified" portfolio of all tech stocks)
- Factor tilts (value, momentum, size) create systematic risk that diversification across stocks does not eliminate
- Use [[beta]]-weighted analysis to understand market exposure

### Risk Budgeting

Allocate risk rather than capital:

- Assign each strategy or position a "risk budget" (e.g., maximum contribution to portfolio VaR)
- [[risk-parity]]: Equalize risk contribution across positions
- Institutional approach: separate alpha risk from beta risk

### Correlation Spikes in Crises

During market crises, [[correlation]] between assets tends to spike toward +1, reducing the benefit of [[diversification]] precisely when it is needed most. Risk management must account for this through:

- Stress testing with historical crisis scenarios
- [[tail-risk]] hedging (out-of-the-money puts, [[vix]] calls)
- Cash reserves as the ultimate hedge (see [[cash-as-asset]])
- [[derisking]] protocols triggered by volatility or drawdown thresholds

## Worked Example: Sizing a Single Trade

*The numbers below are illustrative, not real market data.*

Suppose a trader holds a hypothetical $50,000 account and wants to buy a stock at $100 with a thesis-invalidation stop at $92. They apply a 1% per-trade risk rule (see [[fixed-fractional-position-sizing]]):

1. **Dollar risk budget**: 1% × $50,000 = $500 maximum loss on this trade.
2. **Per-share risk**: $100 entry − $92 stop = $8 per share.
3. **Position size**: $500 / $8 = 62 shares (round down to stay within budget).
4. **Notional exposure**: 62 × $100 = $6,200, or 12.4% of the account.

The key insight is that the *stop distance*, not a fixed notional, determines the position. A tighter $97 stop ($3 risk) would allow 166 shares; a wider $85 stop ($15 risk) only 33 shares. Risk-based sizing automatically shrinks positions when the required stop is far away — exactly when the trade is most dangerous.

Now stack the portfolio view. If this trader already holds four other tech-sector longs each sized to 1% individual risk, the *correlated* worst case is not 1% but closer to 5%, because in a sector-wide selloff all five stops trigger together. The portfolio-level rule (cap total simultaneous risk at, say, 5-6% across correlated names) is what prevents five "safe" 1% trades from becoming one 5% bet. See [[correlation]] and the [[#Portfolio-Level Risk|portfolio-level section]] above.

## Pre-Trade Risk Checklist

Before committing capital, a disciplined trader confirms each item. Skipping any one is the recurring source of avoidable losses:

- [ ] **Defined invalidation**: Where exactly is the thesis wrong? That price is the stop, not an arbitrary percentage.
- [ ] **Dollar risk computed**: The exact dollar loss if the stop is hit is known *before* entry.
- [ ] **Size derived from risk, not conviction**: Position size = risk budget / stop distance — not "how much I feel like."
- [ ] **Reward/risk ≥ target**: Realistic target divided by stop distance meets the minimum ratio (commonly ≥ 2:1).
- [ ] **Correlation check**: Does this trade duplicate existing exposure (same sector, same factor, same vol bet)?
- [ ] **Liquidity check**: Can the full position be exited in one day without moving the price? (see [[liquidity-risk]])
- [ ] **Gap/event check**: Is earnings, FOMC, or a known catalyst inside the holding window? Size for gap risk if so.
- [ ] **Portfolio limit check**: Does adding this push total open risk, [[value-at-risk|VaR]], or sector exposure past the budget?
- [ ] **Pre-mortem**: "If this loses, what is the most likely reason?" If the answer is uncomfortable, resize or skip.

## The Risk Management Lifecycle

Risk management is a continuous loop, not a one-time gate at entry:

1. **Identify** — enumerate the risks a strategy or position carries (use the [[#Risk Type Summary|risk type table]]).
2. **Measure** — quantify with [[value-at-risk|VaR]], [[expected-shortfall|CVaR]], [[maximum-drawdown]], and [[stress-test|stress scenarios]].
3. **Budget** — assign each position/strategy a risk allocation (see [[#Risk Budgeting|risk budgeting]] and [[vega-budgeting]]).
4. **Mitigate** — apply stops, [[hedging|hedges]], [[diversification]], and sizing rules.
5. **Monitor** — track live exposure daily; net Greeks and correlations drift even when nothing is traded.
6. **Respond** — execute pre-committed [[derisking]] actions when thresholds breach; never improvise during stress.
7. **Review** — after each drawdown or material event, conduct a post-mortem and update the rules.

The discipline is in steps 5-7: most blowups come not from missing a risk at entry but from failing to monitor and respond as exposure evolves.

## Failure Modes

The predictable ways risk management breaks down, and why:

| Failure mode | Mechanism | Defence |
|--------------|-----------|---------|
| Over-betting | Position too large relative to edge; one bad streak ruins the account | [[fixed-fractional-position-sizing]], fractional [[kelly-criterion\|Kelly]] |
| Moving the stop | Stop widened or cancelled to avoid taking the loss | Hard stops; pre-commitment; alerts not discretion |
| Correlation blindness | "Diversified" book is one concentrated bet | [[correlation]] matrix review; factor exposure check |
| Ignoring the tail | Sized for the 95th percentile, ruined by the 99.9th | [[stress-test]], [[tail-risk]] hedges, [[expected-shortfall]] |
| Leverage creep | [[leverage]] added gradually until a normal move is fatal | Hard leverage cap; gross-exposure limit |
| Adding to losers | Averaging down turns a small loss into a large one | Rule: drawdowns shrink the book, never grow it |
| Survivorship in backtest | Strategy looks safe because the blowup sample was excluded | Include crisis periods; [[deflated-sharpe-ratio]] |
| Risk theatre | Metrics computed and reported but never acted on | Tie every limit to a specific pre-committed action |

See [[failure-modes]] for the strategy-development treatment of these patterns.

## Quick Reference Rules

- Never risk more than 1-2% of account equity on a single trade
- Minimum recommended risk/reward ratio is 1:2
- Position size = (Account Equity x Risk %) / (Entry - Stop Loss)
- Correlated positions compound risk -- assess total portfolio exposure
- [[leverage]] amplifies losses as much as gains
- A 50% drawdown requires a 100% gain to recover
- Total simultaneous open risk across correlated names should be capped, not just per-trade risk
- Every risk limit must map to a specific pre-committed action, or it is decoration

## Sub-Pages

This section contains detailed pages on specific risk management topics:

- [[risk-management-overview]] -- Comprehensive guide to risk management
- [[position-sizing]] -- Methods for determining trade size
- [[options-position-sizing]] -- Position sizing specific to options strategies
- [[stop-loss]] -- Stop loss types and strategies
- [[value-at-risk]] -- VaR methodology and applications
- [[maximum-drawdown]] -- Understanding and managing drawdowns
- [[drawdown-management]] -- Recovery strategies after drawdowns
- [[kelly-criterion]] -- Optimal bet sizing theory
- [[leverage]] -- Understanding and managing leverage
- [[hedging]] -- Hedging techniques and strategies
- [[derisking]] -- When and how to reduce portfolio risk
- [[counterparty-risk]] -- Managing counterparty exposure
- [[liquidity-risk]] -- Liquidity risk assessment
- [[model-risk]] -- Model and strategy risk
- [[tail-risk]] -- Extreme event risk management
- [[risk-of-ruin]] -- Calculating the probability of account blowup
- [[sortino-ratio]] -- Downside risk-adjusted performance
- [[expected-shortfall]] -- Conditional Value at Risk

## Related

- [[risk-management-overview]] -- The full guide to risk management
- [[sharpe-ratio]] -- Risk-adjusted return measurement
- [[correlation]] -- How asset co-movement affects portfolio risk
- [[diversification]] -- Reducing risk through uncorrelated positions
- [[volatility]] -- The magnitude of price fluctuations
- [[black-swan]] -- Extreme, unpredictable events

## Sources

- See [[risk-management-overview]] for detailed source citations
