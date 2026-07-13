---
title: "Algorithmic Bias"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["Algorithmic Bias", "AI Bias", "AI Fairness"]
domain: [risk-management]
difficulty: intermediate
related: ["[[ethics-safety-overview]]", "[[explainability-interpretability]]", "[[ai-regulation-global]]", "[[supervised-learning]]", "[[ai-healthcare]]", "[[ai-finance]]", "[[artificial-intelligence]]"]
---

# Algorithmic Bias

**Algorithmic bias** occurs when an AI system produces systematically unfair outcomes — discriminating against protected groups based on race, gender, age, or other characteristics. Bias enters through training data, feature selection, objective function design, or feedback loops. For traders, algorithmic bias is both a **portfolio risk factor** (companies face lawsuits and fines) and a **model risk** (biased trading models produce skewed signals).

## How Bias Enters AI Systems

| Source | How | Trading Example |
|--------|-----|----------------|
| **Training data** | Historical data reflects past discrimination | Credit model trained on data where minorities were historically denied → perpetuates denial |
| **Label bias** | Human labellers inject their biases | Sentiment labels reflect labeller's cultural perspective, not universal truth |
| **Selection bias** | Non-representative data sample | Model trained only on US market data fails on international markets |
| **Feature proxy** | Neutral features correlate with protected attributes | Zip code in a lending model proxies for race |
| **Feedback loops** | Model decisions influence future training data | If model under-recommends a stock, less data generated → reinforces under-representation |
| **Objective function** | Optimising for the wrong metric | Maximising trade count (not quality) biases toward liquid large-caps |

## High-Profile Bias Incidents

| Incident | Impact | Trading Relevance |
|----------|--------|-------------------|
| **Apple Card** (2019) | Goldman Sachs credit limits allegedly biased by gender | Regulatory investigation, reputational damage to GS and AAPL |
| **Amazon hiring** (2018) | AI recruiting tool penalised resumes mentioning "women's" | Programme scrapped, reputational cost |
| **COMPAS recidivism** | Criminal sentencing AI biased against Black defendants | Set precedent for AI accountability |
| **Healthcare algorithm** (2019) | Optum algorithm used cost (not health need) → systematically underserved Black patients | $100M+ remediation |

Each incident caused measurable stock impact and regulatory scrutiny for the companies involved.

## Bias in Trading Models

| Bias Type | How It Manifests | Consequence |
|-----------|-----------------|-------------|
| **Survivorship bias** | Model trained only on stocks that still exist | Overestimates returns, underestimates risk |
| **Look-ahead bias** | Future information leaks into training | Backtest looks amazing, live performance fails |
| **Recency bias** | Model overweights recent market regime | Fails when regime changes |
| **Sector bias** | Unbalanced training across sectors | Signals concentrated in familiar sectors |
| **Liquidity bias** | Model works on liquid assets, fails on illiquid | Strategy capacity limited |

## Mitigation Strategies

| Strategy | How | When |
|----------|-----|------|
| **Bias auditing** | Test model outputs across demographic/market segments | Before deployment and periodically |
| **Fairness constraints** | Add equality constraints to the [[constraint-optimisation|optimisation]] | During model training |
| **Diverse training data** | Ensure data represents all relevant groups/conditions | Data collection phase |
| **Disparate impact testing** | Measure whether outcomes differ across groups | Validation phase |
| **Human-in-the-loop** | Human reviews flagged decisions | Deployment |
| **Model cards** | Document model capabilities, limitations, and fairness metrics | Documentation |

## See Also

- [[ethics-safety-overview]] — Ethics hub
- [[explainability-interpretability]] — Related: can you explain biased decisions?
- [[ai-regulation-global]] — Regulations mandating bias testing
- [[ai-finance]] — Bias in financial AI specifically
- [[supervised-learning]] — Where most bias enters
- [[artificial-intelligence]] — AI section hub

## Sources

- ProPublica, "Machine Bias" (2016) — COMPAS recidivism analysis
- Obermeyer et al., Science (2019) — racial bias in a healthcare risk algorithm (Optum)
- Public reporting on the Apple Card / Goldman Sachs gender-bias investigation (2019) and Amazon's scrapped AI recruiting tool (2018)
- EU AI Act and US fair-lending law (ECOA) bias-testing requirements
