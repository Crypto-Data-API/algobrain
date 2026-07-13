---
title: "AI Security for Trading Systems"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, risk-management]
aliases: ["AI Security Trading", "Trading AI Security"]
domain: [risk-management]
difficulty: advanced
related: ["[[ai-security-overview]]", "[[adversarial-attacks]]", "[[model-poisoning]]", "[[prompt-injection]]", "[[model-theft-extraction]]", "[[data-privacy-ai]]", "[[ai-trading-agents]]", "[[risk-management]]", "[[ai-trading-risks]]", "[[artificial-intelligence]]"]
---

# AI Security for Trading Systems

Trading AI systems face a unique security landscape: the environment is **inherently adversarial** (other market participants actively try to exploit your strategy), the consequences of compromise are **immediate financial loss**, and the attack surface spans data feeds, models, execution systems, and the LLM agents tying them together.

## Threat Model for a Trading AI System

| Component | Attack | Consequence | Likelihood |
|-----------|--------|-------------|-----------|
| **Market data feed** | [[model-poisoning|Data poisoning]] via manipulated prices | Model learns from false data → wrong signals | Medium |
| **News/sentiment feed** | [[adversarial-attacks|Adversarial text]] in planted articles | Sentiment model produces false signals | Medium |
| **Pre-trained model** | [[model-theft-extraction|Backdoored model]] from untrusted source | Model behaves correctly until trigger activates | Low |
| **LLM agent** | [[prompt-injection]] via processed documents | Agent ignores risk limits, executes unauthorised trades | Medium-High |
| **Strategy IP** | [[model-theft-extraction|Model extraction]] via API queries | Competitor replicates your edge | High |
| **Client data** | [[data-privacy-ai|Training data leakage]] | Proprietary information exposed | Medium |
| **Execution system** | Traditional cyber attack (not AI-specific) | Unauthorized trade execution | Low (existing controls) |

## Defence Architecture

```
┌──────────────────────────────────────────────────┐
│                  Defence Layers                    │
│                                                    │
│  Layer 1: Data Integrity                          │
│    • Validate data feeds against multiple sources  │
│    • Detect anomalous data patterns               │
│    • Track data provenance                        │
│                                                    │
│  Layer 2: Model Security                          │
│    • Only use models from trusted sources          │
│    • [[adversarial-attacks|Adversarial training]]  │
│    • Monitor for performance drift                │
│                                                    │
│  Layer 3: Agent Guardrails                        │
│    • [[expert-systems|Hard-coded risk limits]]     │
│    • Output validation before execution           │
│    • [[prompt-injection|Input sanitisation]]       │
│                                                    │
│  Layer 4: Execution Controls                      │
│    • Position limits enforced at exchange level    │
│    • Kill switch independent of AI system         │
│    • Human approval above thresholds              │
│                                                    │
│  Layer 5: Monitoring & Response                   │
│    • Real-time anomaly detection on model outputs  │
│    • Full audit trail of all AI decisions          │
│    • Incident response plan for AI compromise     │
└──────────────────────────────────────────────────┘
```

## The Most Important Rule

> **Never give an AI trading agent the ability to take actions that you couldn't reverse or afford to lose.**

Concretely:
- Position limits enforced by broker/exchange, not by the AI
- Maximum loss per day/week hard-coded outside the model
- Kill switch accessible to humans, not controllable by the AI
- Paper trade → small live → scale up (same as [[sim-to-real]])

## Security Checklist for Trading AI

| Category | Check |
|----------|-------|
| **Data** | ☐ Market data validated against multiple sources |
| **Data** | ☐ Alternative data sources vetted for manipulation risk |
| **Model** | ☐ Pre-trained models from trusted sources only |
| **Model** | ☐ Models tested against [[adversarial-attacks|adversarial examples]] |
| **Agent** | ☐ All external data sanitised before LLM processing |
| **Agent** | ☐ Risk limits enforced outside the LLM ([[neuro-symbolic-ai|symbolic layer]]) |
| **Agent** | ☐ Output validated before execution |
| **Execution** | ☐ Position and loss limits at broker/exchange level |
| **Execution** | ☐ Kill switch independent of AI system |
| **Monitoring** | ☐ Full audit trail of inputs, reasoning, actions |
| **Monitoring** | ☐ Anomaly detection on model performance |
| **Privacy** | ☐ Proprietary data never sent to external AI APIs (or enterprise agreement in place) |
| **IP** | ☐ Model API rate-limited and query patterns monitored |

## See Also

- [[ai-security-overview]] — AI security hub
- [[adversarial-attacks]] — Manipulating model inputs
- [[model-poisoning]] — Corrupting training data
- [[prompt-injection]] — Hijacking LLM agents
- [[model-theft-extraction]] — Protecting strategy IP
- [[data-privacy-ai]] — Preventing data leakage
- [[ai-trading-agents]] — The systems being secured
- [[risk-management]] — Broader trading risk framework
- [[neuro-symbolic-ai]] — Hard guardrails for soft models
- [[artificial-intelligence]] — AI section hub
