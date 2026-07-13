---
title: "Risk Management"
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
confidence: medium
tags: [risk-management, concepts]
aliases: ["Risk Mgmt", "Money Management"]
domain: [risk-management]
prerequisites: []
difficulty: beginner
related: ["[[position-sizing]]", "[[stop-loss]]", "[[liquidation]]", "[[leverage]]", "[[portfolio-theory]]", "[[book-market-wizards]]", "[[book-the-black-swan]]", "[[book-when-genius-failed]]"]
---

# Risk Management

**Risk management** is the practice of identifying, assessing, and controlling the potential for financial loss in trading. It is widely regarded as the single most important skill a trader can develop -- more important than entry timing, [[technical-analysis-overview|technical analysis]], or any specific strategy.

This page is the **hub** for the risk-management section of the wiki. The body below covers the universal principles (the mathematics of loss, position sizing, stops, correlation, ruin); the tables in the next section route you to every dedicated sub-page, organized by category.

## The Risk Taxonomy

Before the sub-page map, it helps to name the major *types* of risk a trader manages. These are not mutually exclusive -- a single bad day can hit several at once.

| Risk Type | One-line definition | Primary defense |
|-----------|---------------------|-----------------|
| Market risk | Adverse price moves in held positions | [[position-sizing]], [[stop-loss]], [[hedging]] |
| Liquidity risk | Cannot exit at fair value | Size to liquidity; avoid the long tail ([[liquidity-risk]]) |
| Leverage / liquidation risk | Amplified loss and forced closure | Conservative [[leverage]]; isolated margin ([[liquidation-risk]]) |
| Correlation risk | "Diversified" positions move together | Assess *total* portfolio exposure ([[correlation]]) |
| Tail / black-swan risk | Rare, extreme, model-breaking losses | Convex hedges, robust sizing ([[tail-risk]], [[black-swan]]) |
| Counterparty / settlement risk | The other side fails to deliver | Vet venues; diversify custody ([[counterparty-risk]]) |
| Model risk | The model is wrong about reality | Stress beyond the model ([[model-risk]], [[value-at-risk]]) |
| Behavioral risk | The trader sabotages the plan | Predefined rules, journaling ([[trading-journal]]) |
| Systemic risk | System-wide contagion | Crisis hedges, reduced gross ([[systemic-risk]]) |

## Risk-Management Hub — Sub-Page Map

Use these tables to navigate the full risk-management section. Each row links a sub-page and states what it covers.

### Position Sizing & Capital Allocation

| Page | Covers |
|------|--------|
| [[position-sizing]] | Calculating trade size from risk budget |
| [[options-position-sizing]] | Sizing options by max-loss and Greeks, not premium |
| [[risk-of-ruin]] | Probability of catastrophic account loss |
| [[capital-preservation]] | Survival-first philosophy |
| [[kelly-criterion\|Kelly criterion]] | Growth-optimal bet sizing and fractional Kelly |
| [[leverage]] | Amplified exposure and its dangers |
| [[margin]] / [[portfolio-margin]] | Margin mechanics and cross-margining |

### Loss Control & Exits

| Page | Covers |
|------|--------|
| [[stop-loss]] | Hard, trailing, time, and volatility stops |
| [[take-profit]] | Profit-taking placement |
| [[drawdown]] / [[maximum-drawdown]] | Peak-to-trough loss measurement |
| [[drawdown-management]] | De-risking rules as drawdown deepens |
| [[derisking]] / [[deleveraging]] | Cutting exposure under stress |
| [[trade-repair-and-rolling]] | Restructuring losing options positions |

### Risk Measurement & Metrics

| Page | Covers |
|------|--------|
| [[value-at-risk]] | VaR methodology, limits, the Taleb critique |
| [[expected-shortfall]] | Tail-loss beyond VaR (CVaR) |
| [[sortino-ratio]] | Downside-deviation-adjusted return |
| [[mean-variance-optimization]] | Markowitz allocation framework |
| [[portfolio-greeks-aggregation]] | Book-level options Greeks |
| [[scenario-analysis]] / [[stress-test]] | What-if and shock testing |
| [[historical-stress-test]] / [[options-stress-testing]] | Replaying past crises against the book |

### Market & Structural Risks

| Page | Covers |
|------|--------|
| [[liquidity-risk]] | Inability to exit at fair price |
| [[liquidation-risk]] | Forced closure in leveraged accounts |
| [[interest-rate-risk]] | Duration and rate sensitivity |
| [[basis-risk]] | Hedge-vs-exposure mismatch |
| [[counterparty-risk]] | Default of the other side |
| [[settlement-risk]] | Failure between trade and settlement |
| [[crowding-risk]] | Many traders in the same position |
| [[pain-trade]] | The move that hurts the most participants |

### Tail, Systemic & Crisis Risk

| Page | Covers |
|------|--------|
| [[tail-risk]] | Fat-tailed extreme losses |
| [[black-swan]] | Unforeseeable high-impact events |
| [[systemic-risk]] | System-wide contagion |
| [[crisis-alpha]] | Strategies that profit in crises |
| [[hedging]] | Offsetting unwanted exposure |
| [[geopolitical-risk-premium]] | War/sanctions/political shock pricing |
| [[sovereign-risk]] / [[solvency]] | Government default and firm insolvency |

### Options-Specific Risk

| Page | Covers |
|------|--------|
| [[options-trading-pitfalls]] | The recurring options account-killers |
| [[pin-risk]] | Expiration-day exercise uncertainty |
| [[vega-budgeting]] / [[theta-targeting]] | Allocating vol and decay exposure |
| [[gamma-to-theta-ratio]] / [[theta-realisation-ratio]] | Greek-efficiency metrics |
| [[options-concentration-risk]] | Over-exposure to one name/expiry |
| [[options-risk-budgeting]] / [[options-portfolio-construction]] | Whole-book options framework |
| [[diversification-in-options]] / [[expiration-laddering]] | Spreading expiry and underlying risk |

### Model, Regulatory & Tax Risk

| Page | Covers |
|------|--------|
| [[model-risk]] | When pricing/risk models diverge from reality |
| [[regulatory-risk-map]] | Which strategies face which jurisdictional limits |
| [[pattern-day-trader-rule]] | US PDT account constraint |
| [[tax-implications-trading]] | Tax profiles, Section 1256, wash sales |
| [[wash-sale-rules-options]] | Wash-sale mechanics for options |

### Crypto / DeFi Risk

| Page | Covers |
|------|--------|
| [[smart-contract-risk]] | Code-level exploit exposure |
| [[oracle-manipulation]] / [[flash-loan-attacks]] | DeFi attack vectors |
| [[rug-pulls]] / [[rug-detection-checklist]] | Exit-scam identification |
| [[depeg-risk]] | Stablecoin/peg failure |
| [[cross-chain-bridge-risk]] | Bridge exploit exposure |
| [[insurance-fund]] / [[auto-deleveraging]] | Exchange backstop mechanics |

## The Mathematics of Loss

The relationship between losses and recovery gains is nonlinear and punishing:

| Drawdown | Gain Needed to Recover |
|----------|----------------------|
| 10% | 11.1% |
| 20% | 25.0% |
| 50% | 100.0% |
| 75% | 300.0% |
| 90% | 900.0% |

A 50% loss requires a 100% gain just to break even. This asymmetry is the fundamental reason protecting capital takes priority over growing it. The primary goal is **survival** -- remaining in the game long enough for your edge to manifest across many trades. As [[nassim-taleb]] argues, risk models that rely on normal distributions systematically underestimate the probability of extreme losses, making robust risk management even more critical than conventional models suggest (Source: [[book-the-black-swan]]).

## Core Principles

### 1. Risk Per Trade

**Never risk more than a small percentage of total capital on a single trade.**

- **The 1% Rule**: Max loss per trade = 1% of account equity. On $100,000, that is $1,000.
- **The 2% Rule**: Slightly more aggressive, common among swing traders.
- **Conservative (0.5%)**: For larger accounts or uncertain conditions.

### 2. Risk/Reward Ratio

| R:R Ratio | Meaning | Win Rate to Break Even |
|-----------|---------|----------------------|
| 1:1 | Equal risk and reward | 50% |
| 1:2 | Risking $1 to make $2 | 33.3% |
| 1:3 | Risking $1 to make $3 | 25% |

**Minimum recommended R:R is 1:2.** A trader only needs to win 33.3% of the time to break even. Example: BTC long at $70,000, [[stop-loss]] at $69,000 ($1,000 risk), target $72,000 ($2,000 reward). Even a 40% win rate is profitable over time.

### 3. Maximum Drawdown Tolerance

Define limits in advance: 10-15% drawdown = reduce sizes by half; 20% = stop trading and review; 25%+ = serious strategy overhaul.

## Position Sizing Methods

### Fixed Fractional (Most Common)

```
Position Size = (Account Equity x Risk %) / (Entry - Stop Loss)
```

Example: $50,000 account, 1% risk ($500), buying ETH at $2,000 with stop at $1,950 ($50 risk/unit): Position = $500 / $50 = **10 ETH**. Sizes scale automatically with account growth.

### Kelly Criterion

```
Kelly % = W - (1 - W) / R    (W = win rate, R = avg win / avg loss)
```

With 55% win rate and 2:1 payoff: Kelly = 0.55 - 0.45/2 = 32.5%. In practice, traders use **fractional Kelly** (1/4 to 1/2) since full Kelly assumes perfect probability knowledge. See [[portfolio-theory]].

### Fixed Dollar

Risk a flat dollar amount per trade. Simpler but does not scale with account equity.

## Stop Loss Types

- **Hard stop**: Fixed price level decided before entry. Clear and unemotional.
- **Trailing stop**: Moves with price (e.g., always 3% below highest reached, or based on [[average-true-range|ATR]] multiples). Captures more upside in trends.
- **Time-based stop**: Exit if the target is not hit within a timeframe. Addresses opportunity cost.
- **Volatility-based stop**: Width adapts to asset [[volatility]] using [[average-true-range|ATR]] multiples (e.g., 2x ATR below entry).

## Correlation Risk

Even with the 1% rule per trade, correlated positions compound risk. Long BTC + long ETH + long SOL is effectively one leveraged crypto bet. During stress events, [[correlation|correlations]] spike to 1.0 -- precisely when [[diversification]] is needed most but fails most (Source: [[book-when-genius-failed]]). The [[ltcm]] collapse of 1998 is the definitive case study: positions modeled as uncorrelated all moved against the fund simultaneously during the Russian debt crisis. Always assess **total portfolio risk**, not just individual trade risk.

## Risk of Ruin

| Risk Per Trade | Ruin Probability (50% WR, 1:1) | Ruin Probability (50% WR, 1:2) |
|---------------|-------------------------------|-------------------------------|
| 1% | ~0% | ~0% |
| 5% | ~13% | ~2% |
| 10% | ~38% | ~12% |
| 25% | ~78% | ~50% |

Small risk per trade dramatically reduces ruin probability, even with a modest edge.

## Risk in Leveraged Markets

When trading [[perpetual-futures]], risk management is even more critical: [[leverage]] amplifies losses, [[liquidation]] can result in total margin loss, and [[funding-rate]] costs erode positions over time. Use [[position-sizing]] based on the *leveraged* position size, not just margin posted. Prefer isolated margin to cap per-position loss. See [[liquidation]].

## Common Misconceptions

1. **"Risk management limits profits"** -- It limits individual trade profits but maximizes *lifetime* profits by preventing account destruction.
2. **"I don't need stops in spot"** -- Holding a -80% spot position ties up capital. Opportunity cost matters.
3. **"Pros use high leverage"** -- Most professional traders use conservative sizing. They survive by not blowing up.
4. **"I'll manage risk after I'm profitable"** -- Risk management is what *makes* profitability possible. Every trader interviewed in *Market Wizards* emphasized that risk control is the foundation of longevity (Source: [[book-market-wizards]]).
5. **"A stop loss means I'll always lose that amount"** -- Stops prevent *larger* losses. Not every stop gets hit.

## The ITPM Approach to Risk Management

The [[itpm|Institute of Trading and Portfolio Management]] adds a portfolio-level dimension to risk management that goes beyond individual trade risk:

- **[[long-short-equity|Long/short portfolios]]** inherently manage market risk by holding both long and short positions, reducing net exposure
- **[[trade-repair-and-rolling|Trade repair and rolling]]** — Instead of simply cutting losing options positions, professionals restructure them through rolling strikes/expirations or converting to spreads
- **Half-size entries** — [[edward-shek]] advocates starting positions at half-size and scaling up on confirmation, rather than going full-size immediately
- **Portfolio hedging** — Adding hedge positions (e.g., TLT calls to hedge a net-short equity book) to protect overall P&L rather than managing each trade in isolation
- **The [[eighty-twenty-analysis|80/20 volatility rule]]** — Only ~20% of the time offers enough volatility for active trading; the other 80% should focus on managing existing positions

(Source: [[itpm-god-like-trader-status]])

## Further Reading

- [[position-sizing]] -- Detailed methods for calculating trade sizes
- [[stop-loss]] -- Types and placement strategies
- [[liquidation]] -- Forced closure in leveraged markets
- [[leverage]] -- Understanding amplified exposure
- [[portfolio-theory]] -- Academic frameworks for optimal allocation
- [[trading-journal]] -- Recording and reviewing trades for improvement
- [[trade-repair-and-rolling]] -- Restructuring losing options positions
- [[long-short-equity]] -- Portfolio-level risk through long/short construction
- [[stock-repair]] -- using options to reduce cost basis and repair losing stock positions
- [[value-at-risk]] -- VaR methodology, limits, and the Taleb critique
- [[model-risk]] -- When pricing and risk models diverge from reality, and how to defend against it
- [[regulatory-risk-map]] -- Which strategies face regulatory constraints in which jurisdictions
- [[tax-implications-trading]] -- Tax profiles by strategy type, wash sales, Section 1256, DeFi taxable events

## Sources

- [[book-market-wizards]] -- Schwager's interviews reveal risk management as the universal trait among top traders
- [[book-the-black-swan]] -- Taleb's critique of normal distribution assumptions and the case for robust risk frameworks
- [[book-when-genius-failed]] -- Lowenstein's account of LTCM demonstrates how correlation risk and leverage destroyed a fund staffed by Nobel laureates
