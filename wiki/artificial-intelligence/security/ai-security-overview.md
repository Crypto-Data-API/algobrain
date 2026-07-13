---
title: "AI Security"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["AI Security", "Adversarial AI", "ML Security"]
related: ["[[adversarial-attacks]]", "[[model-poisoning]]", "[[prompt-injection]]", "[[model-theft-extraction]]", "[[data-privacy-ai]]", "[[ai-security-trading]]", "[[ai-safety-alignment]]", "[[ai-cybersecurity]]", "[[hallucinations-ai]]", "[[artificial-intelligence]]", "[[ai-governance-attacks]]", "[[proof-of-humanity]]", "[[llm-defi-interfaces]]"]
---

# AI Security

**AI security** addresses threats *to* AI systems themselves — attacks that manipulate, deceive, steal, or degrade machine learning models. This is distinct from [[ai-cybersecurity|AI *for* cybersecurity]] (using AI to defend networks). As trading firms deploy AI for signal generation, execution, and risk management, securing those AI systems against adversarial attack becomes a direct portfolio risk.

## The AI Threat Landscape

| Threat | What Happens | Trading Risk |
|--------|-------------|-------------|
| **[[adversarial-attacks]]** | Carefully crafted inputs fool a model at inference time | Manipulated chart images trick pattern recognition; adversarial order flow deceives signal models |
| **[[model-poisoning]]** | Corrupting training data to embed backdoors | Poisoned market data causes model to generate wrong signals on trigger conditions |
| **[[prompt-injection]]** | Hijacking LLM behaviour through crafted input | AI trading agent executes attacker's instructions instead of yours |
| **[[model-theft-extraction]]** | Stealing model weights or replicating via queries | Competitor extracts your proprietary trading model through API queries |
| **[[data-privacy-ai]]** | Extracting private training data from model outputs | LLM leaks proprietary strategy details or client information |
| **[[ai-security-trading]]** | All of the above applied to trading systems | Direct financial loss from compromised AI |

## Why AI Security Is Different from Traditional Security

| Traditional Software | AI Systems |
|---------------------|-----------|
| Bugs are deterministic — same input → same bug | Attacks exploit statistical behaviour — subtle perturbations cause failures |
| Code review can find vulnerabilities | Model internals are opaque (billions of parameters) |
| Patching fixes the issue | Retraining is expensive and may not fix the specific vulnerability |
| Attacks target infrastructure | Attacks target the model's *learned representations* |
| Testing proves absence of bugs | Testing can't prove absence of adversarial vulnerabilities |

## The Attack Surface of a Trading AI System

```
┌─────────────────────────────────────────────────────────────┐
│                    Trading AI System                         │
│                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │ Training  │   │  Model   │   │  Input   │   │  Output  │ │
│  │   Data    │   │ Weights  │   │ Pipeline │   │ Actions  │ │
│  │          │   │          │   │          │   │          │ │
│  │ Poisoning │   │  Theft/  │   │Adversarial│  │  Prompt  │ │
│  │ attacks  │   │Extraction│   │ examples │   │injection │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
│       ↑              ↑              ↑              ↑        │
│   [[model-poisoning]]  [[model-theft-extraction]]  [[adversarial-attacks]]  [[prompt-injection]]  │
└─────────────────────────────────────────────────────────────┘
```

## Defence Principles

1. **Assume adversarial environment**: Markets are inherently adversarial — other participants actively try to exploit your strategy
2. **Defence in depth**: No single defence is sufficient; layer multiple protections
3. **Monitor for drift**: Sudden model performance changes may indicate attack, not just market regime shift
4. **Limit attack surface**: Minimise exposed APIs, restrict query access, rate-limit model interactions
5. **Red team regularly**: Test your own systems with adversarial attacks before others do

## See Also

- [[adversarial-attacks]] — Crafted inputs that fool models
- [[model-poisoning]] — Corrupting training data
- [[prompt-injection]] — Hijacking LLM behaviour
- [[model-theft-extraction]] — Stealing model IP
- [[data-privacy-ai]] — Extracting private data from models
- [[ai-security-trading]] — Trading-specific security concerns
- [[ai-safety-alignment]] — Broader AI safety (complementary)
- [[ai-cybersecurity]] — Using AI *for* security (the flip side)
- [[artificial-intelligence]] — AI section hub
