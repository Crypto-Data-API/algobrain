---
title: "ML Development Environments"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Jupyter", "ML IDE", "Development Environment", "Notebooks"]
domain: [ai-trading]
difficulty: beginner
related: ["[[tools-frameworks-overview]]", "[[scikit-learn]]", "[[pytorch]]", "[[text-code-generation]]", "[[anthropic]]", "[[artificial-intelligence]]"]
---

# ML Development Environments

The tools where traders and quants build, test, and iterate on AI models — from Jupyter notebooks for exploration to full IDEs for production code.

## Environment Comparison

| Environment | Type | Best For | Trading Use |
|-------------|------|---------|-------------|
| **Jupyter Notebook** | Interactive notebook | Exploratory analysis, visualisation, prototyping | Data exploration, feature investigation, quick model tests |
| **JupyterLab** | Multi-tab notebook IDE | Longer analysis sessions, multiple files | Research workflows with data + code + charts |
| **VS Code + Jupyter** | Full IDE with notebook support | Production code + notebooks in one tool | Transitioning from prototype to production |
| **Google Colab** | Cloud notebook (free GPU) | Prototyping with GPU access | Test [[pytorch|PyTorch]]/[[tensorflow|TF]] models without local GPU |
| **Kaggle Notebooks** | Cloud notebook | Learning, competitions | Study financial ML Kaggle competitions |
| **Cursor / Claude Code** | AI-native IDE | [[text-code-generation|AI-assisted coding]] | Fastest way to build trading infrastructure with AI |
| **Databricks** | Cloud data + ML platform | Team collaboration, large datasets | Institutional quant research |
| **Amazon SageMaker Studio** | Cloud ML IDE | Full [[mlops|MLOps]] workflow | Enterprise ML deployment |

## The Trading Research Workflow

```
1. Jupyter Notebook — explore data, test hypotheses, visualise
     ↓ (promising idea found)
2. VS Code / Cursor — refactor notebook code into modules
     ↓ (code structured and tested)
3. Production deployment — Docker + FastAPI + monitoring
```

Most trading ML work stays in phase 1-2. Production deployment (phase 3) is where [[mlops]] enters.

### A trading-specific warning about notebooks

Notebooks make it dangerously easy to introduce **lookahead bias** and **survivorship bias** without noticing: out-of-order cell execution can leak future data into a feature, and re-running a cell after editing it silently mutates state. For research that will inform real capital, the discipline is to (a) restart-and-run-all before trusting any backtest result, (b) move validated logic out of the notebook into version-controlled modules, and (c) compute features with strict point-in-time data. Treat notebook output as a hypothesis generator, not as evidence — see [[backtesting-pitfalls]].

## Cloud GPU Options

| Provider | GPU | Cost (approx) | Best For |
|----------|-----|------|---------|
| **Google Colab** | T4 / A100 | Free / $10-50/month | Prototyping, learning |
| **Lambda Labs** | A100 / H100 | $1-3/hour | Serious training |
| **RunPod** | Various NVIDIA | $0.50-3/hour | Flexible, community GPUs |
| **AWS SageMaker** | Various | $1-30/hour | Enterprise, integrated ML |
| **Vast.ai** | Community GPUs | $0.20-1/hour | Cheapest option |
| **Local** | RTX 4090 | ~$1,500 one-time | Privacy, no ongoing cost |

## Related

- [[tools-frameworks-overview]] — Tools hub
- [[scikit-learn]] — Library used in notebooks
- [[pytorch]] — Deep learning in notebooks
- [[mlops]] — Where research code becomes production
- [[backtesting-pitfalls]] — Notebook hazards (lookahead bias)
- [[anthropic]] — Claude Code for trading development
- [[artificial-intelligence]] — AI section hub

## Sources

- Project Jupyter documentation (jupyter.org).
- Google Colaboratory FAQ and pricing (research.google.com/colaboratory).
- Cloud GPU pricing pages: Lambda Labs, RunPod, Vast.ai (approximate ranges current to 2026; rental prices drift — verify before committing).
