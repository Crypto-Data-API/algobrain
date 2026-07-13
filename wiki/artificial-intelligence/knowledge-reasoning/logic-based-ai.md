---
title: "Logic-Based AI"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Formal Logic", "Logic-Based AI", "Symbolic Logic", "Fuzzy Logic"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[knowledge-reasoning-overview]]", "[[expert-systems]]", "[[neuro-symbolic-ai]]", "[[ai-planning]]", "[[history-of-ai]]", "[[artificial-intelligence]]"]
---

# Logic-Based AI

**Logic-based AI** uses formal logical systems to represent knowledge and derive new conclusions through inference. It is the oldest approach to AI and remains the foundation for systems where decisions must be **provably correct** — compliance checks, constraint validation, and rule-based trading systems.

## Types of Logic in Trading

### Propositional Logic
Simple true/false rules with AND, OR, NOT:

```
IF position_size > max_position AND asset_class = "crypto"
THEN reject_trade = TRUE
```

Used in: Trade validation, pre-trade risk checks, compliance screening.

### Predicate Logic (First-Order Logic)
Rules about objects and their relationships:

```
FOR ALL trades t:
  IF t.notional > 1,000,000 AND t.counterparty.credit_rating < "BBB"
  THEN require_collateral(t)
```

Used in: Counterparty risk, margin calculations, regulatory reporting.

### Fuzzy Logic
Degrees of truth (0 to 1) rather than binary true/false:

```
IF trend_strength IS "strong" (0.85) AND volume IS "high" (0.72)
THEN signal_confidence = 0.78
```

Used in: Technical indicator combination, risk scoring where sharp thresholds are artificial. Fuzzy logic acknowledges that "high volume" isn't a binary state — it's a continuum.

### Temporal Logic
Reasoning about time — what was true, what will be true, what must always be true:

```
ALWAYS: portfolio_leverage <= 3.0x
EVENTUALLY: all positions must be reconciled before market close
SINCE last_rebalance > 30 days: trigger rebalance alert
```

Used in: Monitoring rules, compliance temporal constraints, SLA enforcement.

## Trading Applications

| Application | Logic Type | Example |
|-------------|-----------|---------|
| **Pre-trade risk checks** | Propositional | Block trades exceeding position limits |
| **Compliance screening** | Predicate | Check sanctions lists, insider trading windows |
| **Margin calculation** | Predicate + arithmetic | SPAN margin, portfolio margin rules |
| **Alert rules** | Temporal | "If VIX > 30 for 3 consecutive days, reduce exposure" |
| **Signal combination** | Fuzzy | Combine RSI, MACD, volume into weighted confidence |
| **Portfolio constraints** | Propositional | Max 5% in any single name, min 20% in fixed income |

## Logic vs Machine Learning

| Dimension | Logic | [[supervised-learning|ML]] |
|-----------|-------|-----|
| **Input** | Human-written rules | Training data |
| **Explainability** | Complete — follows rule chain | Limited — black box |
| **Handles edge cases** | Only if rules cover them | Generalizes (sometimes wrongly) |
| **Adapts to new data** | No — must update rules manually | Yes — retrain on new data |
| **Regulatory acceptance** | High — auditable | Growing but questioned |
| **Scalability** | Poor — rules proliferate | Good — learns from data |

## The Legacy Problem

Many trading firms have thousands of hand-written rules accumulated over decades. These rule systems:
- Work reliably for known scenarios
- Fail silently on novel scenarios (no rule matches → no action)
- Are expensive to maintain (rules conflict, overlap, become outdated)
- Can't discover new patterns

This is why [[neuro-symbolic-ai]] — combining ML's pattern discovery with logic's rigor — is gaining traction.

## See Also

- [[knowledge-reasoning-overview]] — KR&R hub
- [[expert-systems]] — Logic rules packaged as decision engines
- [[neuro-symbolic-ai]] — Combining logic with neural networks
- [[ai-planning]] — Logic for multi-step decisions
- [[history-of-ai]] — Logic dominated early AI
- [[artificial-intelligence]] — AI section hub
