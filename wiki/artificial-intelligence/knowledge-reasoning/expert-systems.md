---
title: "Expert Systems"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education, history]
aliases: ["Expert System", "Rule Engine", "Production System"]
domain: [ai-trading]
difficulty: beginner
related: ["[[knowledge-reasoning-overview]]", "[[logic-based-ai]]", "[[ai-winters]]", "[[history-of-ai]]", "[[neuro-symbolic-ai]]", "[[artificial-intelligence]]"]
---

# Expert Systems

An **expert system** is an AI program that encodes the decision-making knowledge of a human expert as a set of if-then rules. They were the dominant AI paradigm of the 1980s, drove the second [[ai-winters|AI winter]] when they failed to scale, and persist today in trading as legacy risk management, compliance, and trade validation systems.

## Architecture

```
┌──────────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Knowledge Base  │ ──→ │ Inference Engine │ ──→ │  Conclusion  │
│  (IF-THEN rules) │     │ (forward/backward│     │  + Explanation│
│                  │     │  chaining)       │     │              │
└──────────────────┘     └─────────────────┘     └──────────────┘
         ↑                        ↑
    Domain Expert            User Input
    (encodes rules)         (provides facts)
```

| Component | Role | Trading Example |
|-----------|------|----------------|
| **Knowledge base** | Repository of rules | "IF trade_value > $10M AND market = after_hours THEN require_senior_approval" |
| **Inference engine** | Applies rules to derive conclusions | Forward chaining: apply all matching rules. Backward chaining: start from goal, find supporting rules |
| **Explanation facility** | Traces the reasoning chain | "Trade rejected because: Rule 47 (position limit) → Rule 12 (sector concentration) → BLOCKED" |
| **User interface** | Accepts input, presents conclusions | Risk dashboard, trade blotter alerts |

## Trading Applications (Still in Use)

| System | Domain | How It Works |
|--------|--------|-------------|
| **Pre-trade risk checks** | Risk management | Rules block trades violating limits before execution |
| **Credit scoring** | Lending/counterparty | Rules evaluate counterparty creditworthiness |
| **AML/KYC screening** | Compliance | Rules flag suspicious transactions for review |
| **Trade surveillance** | Market abuse detection | Rules detect wash trading, spoofing, layering patterns |
| **Margin calculation** | Clearing | Rules compute initial/variation margin per exchange specs |
| **Portfolio compliance** | Fund management | Rules verify portfolio stays within mandate (sector limits, concentration, ESG) |

## Why Expert Systems Failed (and Survived)

### Why They Failed (1980s)
- **Knowledge bottleneck**: Extracting rules from experts is slow and expensive
- **Brittleness**: Rules couldn't handle situations they weren't written for
- **Maintenance nightmare**: Thousands of rules with complex interactions, no learning
- **Overpromise**: Marketed as "AI that replaces experts" — couldn't deliver

This failure triggered the second [[ai-winters|AI winter]] (1987-1993).

### Why They Survived in Trading
- **Regulatory requirement**: Rules-based systems are **auditable and explainable** — regulators can examine every decision
- **Hard constraints**: Position limits, margin requirements, and compliance rules are inherently rule-based — they don't need to "learn"
- **Mission-critical**: A risk system that hallucinates is worse than one that's conservative
- **Low latency**: Rule evaluation is microseconds; ML inference is milliseconds-seconds

## Expert Systems vs Modern AI

| Dimension | Expert Systems | [[foundation-models|LLMs]] | Best Approach |
|-----------|---------------|------|---------------|
| **Novel situations** | Fail silently | Handle gracefully | LLM |
| **Hard constraints** | Enforce perfectly | May violate | Expert system |
| **Explainability** | Complete audit trail | "The model said so" | Expert system |
| **Maintenance** | Manual rule updates | Retrain on data | LLM |
| **Pattern discovery** | None | Excellent | LLM |
| **Regulatory acceptance** | Gold standard | Emerging | Expert system |

The modern answer: use both. See [[neuro-symbolic-ai]].

## See Also

- [[knowledge-reasoning-overview]] — KR&R hub
- [[logic-based-ai]] — The logic underlying expert systems
- [[ai-winters]] — Expert system failures triggered the second AI winter
- [[history-of-ai]] — Expert systems in historical context
- [[neuro-symbolic-ai]] — Modern hybrid combining rules + neural networks
- [[ai-regulation-trading]] — Why rule-based systems remain required
- [[artificial-intelligence]] — AI section hub

## Sources

- Russell & Norvig, "Artificial Intelligence: A Modern Approach" — historical treatment of expert systems, the knowledge-acquisition bottleneck, and the second AI winter (c. 1987-1993).
- Feigenbaum et al. — foundational expert-systems work (MYCIN, DENDRAL) that defined the rule-base / inference-engine architecture.
- Industry practice on rules-based pre-trade risk, surveillance, and compliance engines (e.g. position-limit checks, AML/KYC screening) that remain standard in trading infrastructure for auditability and low latency.
