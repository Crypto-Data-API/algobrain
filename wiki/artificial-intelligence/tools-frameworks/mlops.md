---
title: "MLOps"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["MLOps", "ML Operations", "Machine Learning Operations"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tools-frameworks-overview]]", "[[experiment-tracking]]", "[[model-deployment]]", "[[ml-trading-pipeline]]", "[[cross-validation-trading]]", "[[overfitting-in-trading]]", "[[artificial-intelligence]]"]
---

# MLOps

**MLOps** (Machine Learning Operations) is the discipline of deploying, monitoring, and maintaining ML models in production. It bridges the gap between "model works in a Jupyter notebook" and "model runs reliably in live trading." Most ML trading projects fail not because the model is bad, but because the operational infrastructure is missing.

## The MLOps Lifecycle

```
Data → Feature Engineering → Training → Validation → Deployment → Monitoring → Retraining
  ↑                                                                              |
  └──────────────────────────── Feedback Loop ────────────────────────────────────┘
```

| Stage | What Happens | Tools |
|-------|-------------|-------|
| **Data management** | Versioned datasets, feature stores, data quality checks | DVC, Feast, Great Expectations |
| **Feature engineering** | Transform raw data to model inputs | [[scikit-learn|sklearn]], pandas, [[feature-engineering-finance|custom code]] |
| **Training** | Train model on versioned data with tracked hyperparameters | [[pytorch|PyTorch]], XGBoost, [[experiment-tracking|MLflow]] |
| **Validation** | [[cross-validation-trading|Walk-forward CV]], [[overfitting-in-trading|overfit detection]], A/B testing | sklearn, custom validation |
| **[[model-deployment|Deployment]]** | Package model, serve predictions via API or batch job | Docker, FastAPI, SageMaker, Seldon |
| **Monitoring** | Track prediction drift, data drift, performance degradation | Evidently AI, WhyLabs, custom dashboards |
| **Retraining** | Automatically retrain when performance degrades | Airflow, Prefect, scheduled pipelines |

## Why MLOps Matters for Trading

| Without MLOps | With MLOps |
|-------------|-----------|
| "Which model version is running?" | Tagged, versioned models with audit trail |
| "The model stopped working but nobody noticed" | Alerts on performance drift within hours |
| "I can't reproduce last month's results" | Every run tracked with data version, code version, hyperparameters |
| "The data format changed and everything broke" | Data validation catches schema changes before training |
| "We retrained on bad data" | Data quality gates prevent corrupted data from entering pipeline |
| "Deploying a new model takes 3 days" | One-click deployment with rollback |

## MLOps Tools Landscape

### Open-Source

| Tool | Function | Trading Use |
|------|---------|-------------|
| **[[experiment-tracking|MLflow]]** | Experiment tracking, model registry, deployment | Standard for tracking trading model experiments |
| **DVC** (Data Version Control) | Dataset versioning (git for data) | Version market data snapshots used for training |
| **Airflow / Prefect** | Workflow orchestration | Schedule daily retraining, data pipelines |
| **Docker** | Containerisation | Package model + dependencies for deployment |
| **Feast** | Feature store | Serve pre-computed features for online inference |
| **Great Expectations** | Data validation | Verify data quality before training |
| **Evidently AI** | Model monitoring | Detect prediction and data drift |

### Cloud Platforms

| Platform | Provider | Strength |
|----------|---------|---------|
| **SageMaker** | AWS | End-to-end ML platform, most widely used |
| **Vertex AI** | Google Cloud | Integrated with TensorFlow/JAX, AutoML |
| **Azure ML** | Microsoft | Enterprise integration, MLflow-compatible |

### Commercial

| Tool | Function |
|------|---------|
| **[[experiment-tracking|Weights & Biases]]** | Experiment tracking (best UX) |
| **Neptune** | Experiment tracking |
| **Databricks** | Unified data + ML platform (MLflow creators) |
| **Tecton** | Feature platform |

## Why Trading MLOps Differs From Generic MLOps

Standard MLOps monitors prediction quality; trading MLOps must monitor **profitability under non-stationarity**. Three differences matter:

1. **The ground truth arrives late and is noisy.** A classifier's label is known immediately; a trade's true quality is only revealed after the position closes, and even then a single outcome is a draw from a distribution. Drift detection must work on *distributional* signals (feature drift, regime change) rather than waiting for realised P&L.
2. **The environment is adversarial and reflexive.** Once an edge is deployed at size it can decay because others find it or because your own flow moves the market. Monitoring must watch for **alpha decay** (rolling out-of-sample Sharpe trending toward zero), not just data-pipeline health.
3. **Retraining can be the failure mode.** Naive auto-retraining on recent data overfits to the latest regime and can chase noise. Trading retraining pipelines need walk-forward validation gates and a champion/challenger promotion step ([[overfitting-in-trading]]) before a new model touches live capital.

## MLOps for Solo Traders vs Institutions

| | Solo Trader | Institution |
|---|------------|------------|
| **Minimum viable MLOps** | MLflow for tracking, DVC for data, cron for retraining | Full platform (SageMaker/Vertex), feature store, monitoring |
| **Deployment** | Python script on VPS / cloud function | Containerised microservices, auto-scaling |
| **Monitoring** | Manual daily check | Automated alerts, dashboards, SLAs |
| **Retraining** | Weekly manual retrain | Automated pipeline triggered by drift detection |
| **Cost** | ~$0-50/month | $10K-100K+/month |

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[experiment-tracking]] — Logging and comparing runs
- [[model-deployment]] — Serving models in production
- [[ml-trading-pipeline]] — The pipeline MLOps manages
- [[cross-validation-trading]] — Validation within the pipeline
- [[overfitting-in-trading]] — What monitoring catches
- [[ml-development-environments]] — Where models are first built
- [[artificial-intelligence]] — AI section hub

## Sources

- MLflow, DVC, Feast, Evidently AI, Great Expectations, Apache Airflow, Prefect — official project documentation.
- AWS SageMaker, Google Vertex AI, Azure ML — cloud provider MLOps documentation.
- Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (Google, NeurIPS 2015) — the foundational case for MLOps discipline.
- Lopez de Prado, *Advances in Financial Machine Learning* (2018) — walk-forward validation and the dangers of naive retraining in finance.
