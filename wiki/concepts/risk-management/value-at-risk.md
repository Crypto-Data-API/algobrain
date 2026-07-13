---
title: "Value at Risk (VaR)"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [risk-management, quantitative, volatility]
aliases: ["VaR", "Value-at-Risk"]
domain: [risk-management]
difficulty: intermediate
related: ["[[risk-management]]", "[[model-risk]]", "[[tail-risk]]", "[[black-swan]]", "[[expected-shortfall]]", "[[ltcm]]", "[[book-the-black-swan]]", "[[book-when-genius-failed]]"]
---

Value at Risk (VaR) is the most widely used summary statistic for downside market risk. It states the **maximum loss expected over a given time horizon, at a given confidence level, under normal market conditions**. For example, "the 1-day 99% VaR of this portfolio is $10M" means there is a 1% probability of losing more than $10M in one day, assuming the model's distributional assumptions hold. VaR is the standard regulatory and internal risk metric across most banks, hedge funds, and trading desks — and also one of the most criticized.

## Definition

Formally, for a portfolio with daily P&L random variable $L$ (loss), the **VaR at confidence level $\alpha$** over horizon $h$ is the smallest value $v$ such that:

$$P(L > v) \leq 1 - \alpha$$

So 99% VaR is the 99th percentile of the loss distribution. By construction, VaR says nothing about how bad losses get *beyond* that percentile — that's where its most serious criticism lives.

## How VaR Is Computed

There are three main methodologies in practice:

### 1. Parametric (Variance-Covariance)

Assume returns follow a multivariate normal distribution. Compute portfolio variance from positions and the covariance matrix of risk factors. Read off VaR from a normal quantile (1.65σ for 95%, 2.33σ for 99%). Fast and analytic, but only valid if returns are actually close to normal — which they aren't, especially in the tails.

### 2. Historical Simulation

Apply current portfolio weights to historical returns over a window (typically 250–500 days) and read off the appropriate percentile of the resulting empirical loss distribution. Captures fat tails *if* the historical window contains stress events. Fails if the window is too short or omits crisis periods.

### 3. Monte Carlo

Simulate many synthetic return scenarios from a chosen statistical model (potentially with fat tails, stochastic volatility, jumps), revalue the portfolio under each scenario, and take the percentile. Most flexible, most computationally expensive, and most sensitive to model assumptions.

## Why VaR Became Standard

VaR was developed at JPMorgan in the early 1990s and disseminated through the **RiskMetrics** publication (1994). It spread rapidly because:

- It produces a **single number** that senior management and regulators can compare across desks, products, and firms
- It is **comparable** in a way that more granular risk reports are not
- The **Basel II framework** (and successors) made VaR the basis for regulatory market-risk capital

## The Critique (Taleb and Others)

[[nassim-taleb]]'s *The Black Swan* contains the most influential critique of VaR (Source: [[book-the-black-swan]]). The arguments:

1. **VaR ignores the tail**. By construction, it tells you nothing about what happens beyond the confidence level — and the losses beyond the confidence level are exactly the ones that destroy firms.
2. **Gaussian assumptions underestimate fat tails**. Parametric VaR built on normality treats 5+ sigma events as essentially impossible; in real markets they happen on a timescale of years.
3. **VaR creates false confidence**. A precise number invites the illusion of control. Risk managers, traders, and senior management treat the VaR number as a hard ceiling and size positions against it.
4. **VaR is procyclical**. Historical-simulation VaR uses a recent window, so during quiet periods VaR is low and capital constraints are loose, encouraging more risk-taking; during crisis it spikes and forces deleveraging at the worst moment.
5. **VaR is non-subadditive** in some methodologies — the VaR of a combined portfolio can exceed the sum of the VaRs of its parts, violating the basic intuition that diversification reduces risk.

The [[ltcm|LTCM]] collapse is widely cited as a case study in VaR's limitations: their models said August 1998 was effectively impossible, then it happened, and the firm lost $4.6 billion (Source: [[book-when-genius-failed]]).

## Successors and Complements

### Expected Shortfall (CVaR)

**Expected Shortfall** (also called Conditional VaR or CVaR) is the average loss *given that* loss exceeds VaR. Formally:

$$ES_\alpha = E[L \mid L > VaR_\alpha]$$

ES addresses VaR's biggest flaw — it cares about how bad the tail gets, not just whether you're in the tail. It is also subadditive (always rewards diversification). Basel III moved the regulatory standard from VaR to ES.

### Stress Testing and Scenario Analysis

Run the portfolio through specific historical (1987, 1998, 2008, March 2020) or hypothetical scenarios and report the loss directly. Avoids percentile-based abstraction.

### Drawdown-Based Limits

Set hard rules on maximum drawdown rather than statistical VaR. More directly aligned with the actual constraint (the firm running out of capital) and harder to game with model assumptions.

## Practical Use

VaR is still useful as one input among several. Sensible practice:

- Use VaR as a **rough comparison metric**, not as a binding constraint
- Always look at **expected shortfall** alongside VaR
- Always run **stress tests** independent of VaR
- Treat any single risk number with appropriate skepticism — risk is multidimensional

## Related

- [[risk-management]]
- [[model-risk]]
- [[tail-risk]]
- [[expected-shortfall]]
- [[ltcm]]
- [[black-swan]]

## Sources

- (Source: [[book-the-black-swan]]) — Taleb's critique of VaR and Gaussian risk models
- (Source: [[book-when-genius-failed]]) — Lowenstein's account of how VaR-style risk modeling failed at LTCM
