---
title: "Model Risk"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [risk-management, quantitative, derivatives]
aliases: ["model risk", "model-risk"]
domain: [risk-management, quantitative]
prerequisites: ["[[value-at-risk]]", "[[black-scholes]]"]
difficulty: intermediate
related: ["[[risk-management]]", "[[value-at-risk]]", "[[ltcm]]", "[[black-scholes]]", "[[volatility-smile]]", "[[book-when-genius-failed]]", "[[book-my-life-as-a-quant]]"]
---

Model risk is the risk that a quantitative model used to price, hedge, or measure risk gives results that diverge dangerously from reality. It is one of the central concerns of modern quantitative finance because the use of models is so pervasive — virtually every derivative price, every risk number, and every algorithmic execution depends on assumptions that can fail. The term gained currency after high-profile model-driven blowups, most famously [[ltcm|Long-Term Capital Management]] in 1998 (Source: [[book-when-genius-failed]]).

## Sources of Model Risk

### 1. Wrong Model Specification

The chosen model omits a feature of reality that turns out to matter. Examples:

- Black-Scholes assumes **constant volatility**; real markets exhibit a [[volatility-smile]] and stochastic volatility
- VaR models assume **multivariate normality**; real return distributions have fat tails and asymmetric correlations
- Interest rate models assume specific dynamics (mean-reverting, single-factor) that fail during regime changes

[[emanuel-derman|Emanuel Derman]] and [[fischer-black]] confronted this directly when developing the BDT and local-volatility models at Goldman Sachs (Source: [[book-my-life-as-a-quant]]). Derman's central message: every model is a simplification, and the simplifications themselves are sources of risk.

### 2. Wrong Parameter Estimates

Even a correctly specified model produces wrong outputs if calibrated on bad data. Common failures:

- **Short calibration windows** that exclude crisis periods
- **Survivor-biased data** ([[survivorship-bias]])
- **Stale correlations** that look stable until they don't

LTCM's risk models, calibrated on 1990s data, treated August 1998 as a roughly 14-sigma event — meaning effectively impossible. The actual frequency of such events in long financial history is measured in years, not eternities.

### 3. Implementation Bugs

The mathematical model is correct, but the code is wrong. Discount factors applied twice, day-count conventions confused, off-by-one errors in volatility surfaces. These are common, hard to detect, and can cause silent mispricing of large positions for years.

### 4. Wrong Use of a Right Model

A model is correct for its intended purpose but applied to a problem it was not designed for. A risk model intended to size positions in normal markets used to size them in crisis markets. A pricing model for European options used to price exotic structures with discontinuous payoffs. The model itself is fine; the application is the failure.

### 5. Feedback Effects

When enough market participants use the same model, the model itself becomes part of the market dynamics. Portfolio insurance in [[1987-crash|1987]] is the canonical example: the model assumed it could trade against the market, but everyone trying to trade against the market simultaneously *was* the market. Similar effects appeared in 2007–2008 with structured credit models and gaussian copulas.

## Why Model Risk Is Hard to Manage

Model risk is harder than market risk for several reasons:

1. **It is unobservable until it materializes** — backtests by definition fit the past
2. **Sophisticated users overweight model outputs** — Nobel laureates at LTCM trusted their models far more than less-credentialed traders trusted theirs
3. **Models create false precision** — VaR of $42.7M sounds authoritative; "we're not sure" sounds amateur
4. **Reputational pressure** rewards confident model-based answers, not honest uncertainty

## Defenses

### Stress Testing and Scenario Analysis

Run the book against historical crises (1987, 1998, 2008, March 2020) and against hypothetical extreme scenarios. Compare to model VaR. If model VaR is much smaller than stress losses, you have a model risk problem.

### Multiple Models

Price the same instrument with two different models. If they disagree by an amount larger than your trading edge, model risk dominates the trade.

### Model Reserves

Hold capital against the difference between best-estimate and conservative model outputs. This is now a regulatory requirement under Basel III for material trading-book models.

### Model Validation Function

Independent model risk teams (separate from front office) should validate models before deployment and re-validate periodically. SR 11-7 (US Federal Reserve guidance) is the standard reference.

### Skin in the Game and Honest Limits

If the model says a position is safe but a senior trader's gut says it isn't, the gut should win at least some of the time. Hard position limits and concentration limits constrain the damage when models are wrong.

### Avoid Leverage Where Models Can't Be Trusted

The deepest defense is the [[nassim-taleb|Taleb]] / Lowenstein lesson from LTCM: when you cannot trust your model in the tails, do not apply leverage that requires the model to be right in the tails.

## Related

- [[risk-management]]
- [[value-at-risk]]
- [[ltcm]]
- [[volatility-smile]]
- [[black-scholes]]
- [[1987-crash]]
- [[2008-global-financial-crisis]]

## Sources

- (Source: [[book-when-genius-failed]]) — Lowenstein's dissection of LTCM as the canonical model-risk failure
- (Source: [[book-my-life-as-a-quant]]) — Derman's first-person view of building, debugging, and questioning quant models at Goldman Sachs
