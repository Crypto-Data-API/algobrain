---
title: "Experiment Tracking"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Experiment Tracking", "MLflow", "Weights & Biases", "W&B"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tools-frameworks-overview]]", "[[mlops]]", "[[hyperparameter-tuning]]", "[[cross-validation-trading]]", "[[backtesting-pitfalls]]", "[[artificial-intelligence]]"]
---

# Experiment Tracking

**Experiment tracking** logs every ML training run — hyperparameters, metrics, data versions, code versions, and artifacts — so you can compare, reproduce, and audit your work. For trading, this is essential because the [[backtesting-pitfalls|difference between a real edge and an overfit fluke]] often comes down to tracking exactly what you tried and what worked.

## What to Track

| Category | Examples | Why |
|----------|---------|-----|
| **Hyperparameters** | learning_rate=0.01, max_depth=5, n_estimators=200 | Reproduce the exact model |
| **Metrics** | Sharpe=1.8, F1=0.72, max_drawdown=-8.2% | Compare across runs |
| **Data version** | Training data hash, date range, feature list | Know exactly what data the model saw |
| **Code version** | Git commit SHA | Reproduce the exact code |
| **Artifacts** | Trained model file, plots, confusion matrix | Deploy the exact winning model |
| **Environment** | Python version, library versions | Prevent "works on my machine" failures |
| **Notes** | "Tried adding volume features", "Market regime filter" | Remember why you tried each experiment |

## Key Tools

| Tool | Type | Strengths | Cost |
|------|------|-----------|------|
| **MLflow** | Open-source (LF AI & Data) | Full lifecycle (tracking + registry + deployment + GenAI eval), self-hosted, industry standard | Free; managed via Databricks |
| **Weights & Biases** (W&B) | SaaS | Best visualisation, team collaboration, hyperparameter sweeps, model registry | Free tier (personal), paid for teams |
| **Neptune** | SaaS | Clean UI, scales to very high run counts, foundation-model training | Free tier, paid for teams |
| **TensorBoard** | Open-source | Built into [[tensorflow|TensorFlow]]/[[pytorch|PyTorch]], real-time training visualisation | Free |
| **Comet** | SaaS | Good for comparing experiments, LLM tracing (Opik) | Free tier |
| **DVC** + **DVCLive** | Open-source | Git-native experiment tracking + data versioning | Free |

MLflow (latest 2.x as of 2026) is governed under the Linux Foundation's **LF AI & Data** umbrella rather than owned by a single vendor, though Databricks (its originator) offers a managed version. It is the de-facto open standard for self-hosted tracking. W&B is the most popular SaaS choice and has expanded into LLM evaluation/tracing (W&B Weave). For a solo trader the practical default is **MLflow self-hosted** (no recurring cost, full audit trail) or **W&B free tier** (better charts, zero ops).

## Trading-Specific Tracking Patterns

### Track the Strategy, Not Just the Model

Standard ML tracks model metrics (F1, accuracy). Trading experiments should additionally track:

```
Strategy Metrics:
  - Sharpe ratio (in-sample AND out-of-sample)
  - Number of trades
  - Win rate
  - Average win / average loss
  - Max drawdown
  - Transaction costs assumed
  - Data range (train and test periods)
  - Market regime during test period
```

### The Experiment Audit Trail

When you find a strategy that looks good:
1. Which of the 200 experiments led to this configuration?
2. How many configurations did you try before finding this one? ([[hyperparameter-tuning|Multiple testing correction]])
3. What was the out-of-sample performance vs in-sample?
4. Would you have selected this configuration if you'd only seen the out-of-sample results?

Experiment tracking makes these questions answerable. Without it, you're flying blind and probably [[overfitting-in-trading|overfitting]].

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[mlops]] — The broader operational context
- [[hyperparameter-tuning]] — What experiment tracking logs
- [[cross-validation-trading]] — Validation results to track
- [[backtesting-pitfalls]] — Why tracking prevents false discoveries
- [[overfitting-in-trading]] — The failure tracking helps detect
- [[artificial-intelligence]] — AI section hub

## Sources

- MLflow documentation and project page, LF AI & Data Foundation (mlflow.org).
- Weights & Biases documentation (docs.wandb.ai).
- Lopez de Prado, *Advances in Financial Machine Learning* (2018) — on multiple-testing correction and recording the full experiment count, the trading-specific rationale for tracking.
