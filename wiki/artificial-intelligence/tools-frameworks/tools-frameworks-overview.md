---
title: "AI Tools & Frameworks"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["AI Tools", "ML Frameworks", "AI Engineering"]
related: ["[[pytorch]]", "[[tensorflow]]", "[[scikit-learn]]", "[[mlops]]", "[[experiment-tracking]]", "[[model-deployment]]", "[[ml-development-environments]]", "[[langchain]]", "[[hugging-face]]", "[[artificial-intelligence]]"]
---

# AI Tools & Frameworks

The practical engineering stack for building AI trading systems — from ML frameworks for model development, through experiment tracking and versioning, to production deployment and monitoring. This section covers the tools you actually install and use, complementing the theoretical concepts elsewhere in the AI section.

For agent-specific frameworks ([[langchain]], [[crewai]], [[eliza-framework]]), see the Frameworks subsection.

## The AI Engineering Stack

```
Development
  ├── [[pytorch]] / [[tensorflow]] — model building and training
  ├── [[scikit-learn]] — traditional ML (XGBoost, Random Forest)
  ├── [[ml-development-environments]] — Jupyter, VS Code, cloud notebooks
  └── [[hugging-face]] — pre-trained models, datasets, Transformers library

Experiment Management
  └── [[experiment-tracking]] — MLflow, Weights & Biases, experiment logging

Production
  ├── [[model-deployment]] — serving models for inference (APIs, edge, batch)
  └── [[mlops]] — the full lifecycle: version, test, deploy, monitor, retrain
```

## Choosing the Right Tool

| Task | Best Tool | Why |
|------|----------|-----|
| **Train a deep learning model** | [[pytorch]] | Dominant for research and production; best debugging |
| **Quick ML prototype** | [[scikit-learn]] | Simplest API; 5 lines from data to model |
| **Use a pre-trained LLM** | [[hugging-face|Hugging Face Transformers]] | Largest model hub, standard API |
| **Build [[xgboost-trading|XGBoost]] pipeline** | [[scikit-learn]] + XGBoost library | Scikit-learn API compatibility |
| **Track experiments** | [[experiment-tracking|MLflow / W&B]] | Compare runs, log hyperparameters, reproduce results |
| **Deploy model as API** | [[model-deployment|FastAPI + Docker / SageMaker]] | Production inference serving |
| **Full ML pipeline** | [[mlops|MLOps platform]] | End-to-end: data → train → deploy → monitor → retrain |
| **Build an LLM agent** | [[langchain]] / [[crewai]] | Agent orchestration, tool use, memory |
| **Fine-tune an LLM** | [[hugging-face|HF Transformers + PEFT]] | LoRA, QLoRA, parameter-efficient [[fine-tuning-llms|fine-tuning]] |
| **Interactive analysis** | [[ml-development-environments|Jupyter]] | Explore data, visualise, iterate |

## A pragmatic starter stack for a systematic trader

For a solo or small-team quant building real strategies (not large-scale research), the lowest-friction stack as of 2026 is:

- **Models:** [[scikit-learn]] + XGBoost/LightGBM for tabular signals; [[pytorch]] only if you genuinely need sequence/deep models.
- **Environment:** [[ml-development-environments|Jupyter / VS Code]] for research, then move validated logic into version-controlled modules.
- **Tracking:** [[experiment-tracking|MLflow self-hosted or W&B free tier]] — non-negotiable for [[overfitting-in-trading|avoiding overfit flukes]].
- **Deployment:** [[model-deployment|FastAPI + Docker]] on a VPS; NVIDIA Triton only if GPU multi-model serving is needed.
- **Ops:** [[mlops|MLflow registry + a cron/Airflow retraining gate]] with walk-forward validation before any model touches live capital.

The expensive enterprise platforms (SageMaker, Vertex, Databricks) earn their keep at institutional scale; they are usually overkill — and a cost trap — for individual traders.

## See Also

- [[pytorch]] — Deep learning framework
- [[tensorflow]] — Alternative deep learning framework
- [[scikit-learn]] — Traditional ML toolkit
- [[mlops]] — ML operations lifecycle
- [[experiment-tracking]] — Logging and comparing runs
- [[model-deployment]] — Serving models in production
- [[ml-development-environments]] — Development environments
- [[langchain]], [[crewai]], [[eliza-framework]] — Agent frameworks
- [[hugging-face]] — Model hub and libraries
- [[artificial-intelligence]] — AI section hub
