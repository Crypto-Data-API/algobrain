---
title: "Explainability & Interpretability"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["Explainability", "Interpretability", "XAI", "Explainable AI"]
domain: [risk-management]
difficulty: intermediate
related: ["[[ethics-safety-overview]]", "[[algorithmic-bias]]", "[[ai-governance-frameworks]]", "[[neuro-symbolic-ai]]", "[[expert-systems]]", "[[ai-regulation-trading]]", "[[xgboost-trading]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# Explainability & Interpretability

**Explainability** is the ability to understand *why* an AI system made a specific decision. **Interpretability** is the degree to which a human can understand the model's internal logic. For trading, explainability is both a regulatory requirement (financial regulators demand auditable decisions) and a practical necessity (you need to understand why your model is taking a position before risking capital).

## Interpretable vs Explainable

| | Interpretable | Explainable |
|---|-------------|-------------|
| **Definition** | Model is inherently understandable | Post-hoc explanations of a black-box model |
| **Example** | Linear regression, decision tree, [[expert-systems|rule-based system]] | SHAP values on [[xgboost-trading|XGBoost]], attention maps on transformers |
| **Trust level** | High — you see the logic directly | Medium — explanation approximates the true reasoning |
| **Complexity** | Limited (simple models only) | Works on any model |

## The Interpretability Spectrum

```
Most Interpretable ←──────────────────────────────→ Least Interpretable

Linear    Decision   [[expert-systems|Rule    [[random-forest-trading|Random   [[xgboost-trading|XGBoost]]   [[lstm-trading|LSTM]]   [[foundation-models|LLM]]
Regression  Tree     System]]  Forest]]                           (GPT-4)
```

## Explainability Techniques

### Model-Agnostic Methods

| Method | How | Output | Best For |
|--------|-----|--------|---------|
| **SHAP** (SHapley Additive exPlanations) | Game-theoretic feature attribution | Per-feature contribution to each prediction | Any model — gold standard for trading |
| **LIME** (Local Interpretable Model-agnostic Explanations) | Fit simple model locally around a prediction | Approximate explanation for one decision | Quick local explanations |
| **Permutation importance** | Shuffle each feature, measure accuracy drop | Global feature ranking | Feature selection, model auditing |
| **Partial dependence plots** | Show how one feature affects predictions on average | Feature-response curves | Understanding feature relationships |

### Model-Specific Methods

| Method | Model | Output |
|--------|-------|--------|
| **Feature importance** | [[xgboost-trading|XGBoost]], [[random-forest-trading|Random Forest]] | Which features the model uses most |
| **Attention weights** | [[transformer-architecture|Transformers]], [[attention-mechanism|attention]] models | Which input tokens the model focuses on |
| **Gate activations** | [[recurrent-neural-networks|LSTM]] | Which timesteps the model remembers/forgets |
| **Saliency maps** | [[convolutional-neural-networks|CNNs]] | Which image regions drive the prediction |

## Trading Applications

### Why Your Model Bought

```
SHAP explanation for BUY signal on AAPL:
  RSI(14) = 28        → +0.32 (oversold, bullish)
  Volume surge = 2.1x → +0.21 (accumulation signal)
  Sector momentum     → +0.15 (tech rotating in)
  VIX = 28            → -0.12 (high vol, bearish)
  ────────────────────
  Net signal: +0.56 (BUY, above 0.3 threshold)
```

This is actionable: you can see *why* the model is bullish and decide whether you agree with its reasoning.

### Regulatory Requirements

| Regulation | Explainability Requirement |
|-----------|--------------------------|
| **EU AI Act** | High-risk AI systems must provide "meaningful explanations" |
| **ECOA / Fair Lending** (US) | Credit decisions must state specific reasons for denial |
| **MiFID II** (EU) | Algorithmic trading systems require documentation and auditability |
| **OCC SR 11-7** (US) | Model risk management requires model understanding |
| **GDPR Art. 22** (EU) | Right to explanation for automated decisions |

### The [[neuro-symbolic-ai|Neuro-Symbolic]] Solution

Combine interpretable rules with powerful black-box models:
- **Black-box model** generates signal (powerful but unexplainable)
- **Symbolic layer** provides rule-based explanation (auditable)
- **SHAP/LIME** verifies that the explanation matches the model's actual reasoning

## See Also

- [[ethics-safety-overview]] — Ethics hub
- [[algorithmic-bias]] — Explanations reveal bias
- [[neuro-symbolic-ai]] — Combining interpretable and powerful models
- [[expert-systems]] — Inherently interpretable
- [[xgboost-trading]] — SHAP works excellently with tree models
- [[ai-regulation-trading]] — Trading-specific regulations
- [[ai-governance-frameworks]] — Corporate governance of AI
- [[artificial-intelligence]] — AI section hub

## Sources

- Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions" (2017) — SHAP
- Ribeiro et al., "Why Should I Trust You?" (2016) — LIME
- Regulatory texts: EU AI Act, GDPR Art. 22, US ECOA, MiFID II, OCC SR 11-7
- Anthropic and other labs' mechanistic-interpretability research on transformer internals
