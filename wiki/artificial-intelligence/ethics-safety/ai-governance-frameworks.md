---
title: "AI Governance Frameworks"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["AI Governance", "AI Risk Management Framework"]
domain: [risk-management]
difficulty: intermediate
related: ["[[ethics-safety-overview]]", "[[ai-regulation-global]]", "[[explainability-interpretability]]", "[[algorithmic-bias]]", "[[ai-regulation-trading]]", "[[artificial-intelligence]]"]
---

# AI Governance Frameworks

**AI governance** is how organisations manage the risks and responsibilities of deploying AI systems. It encompasses policies, processes, roles, and oversight mechanisms that ensure AI is used safely, ethically, and in compliance with regulations. For traders evaluating AI-heavy companies, strong governance = lower regulatory risk = more durable valuations.

## Key Governance Frameworks

| Framework | Publisher | Focus | Status |
|-----------|----------|-------|--------|
| **NIST AI RMF** (AI Risk Management Framework) | US NIST | Risk identification, assessment, management | Published Jan 2023, voluntary |
| **EU AI Act** | European Union | Risk-based classification and regulation | In force Aug 2024, obligations phased through 2025-2027 (see [[ai-regulation-global]]) |
| **ISO/IEC 42001** | ISO | AI management system standard | Published 2023, certification available |
| **OECD AI Principles** | OECD | International principles for trustworthy AI | Adopted 2019, updated 2024 |
| **Singapore FEAT** | MAS | Fairness, Ethics, Accountability, Transparency for finance | Published 2021, financial sector specific |

### NIST AI RMF (Most Relevant for US Trading Firms)

Four core functions:
1. **Govern**: Establish AI governance structure, roles, policies
2. **Map**: Identify AI systems, their contexts, and risks
3. **Measure**: Assess AI risks using metrics and testing
4. **Manage**: Mitigate identified risks, monitor, and improve

### EU AI Act Risk Tiers

| Tier | Risk Level | Examples | Requirements |
|------|-----------|---------|-------------|
| **Unacceptable** | Prohibited | Social scoring, real-time biometric surveillance | Banned |
| **High** | Stringent rules | Credit scoring, hiring, medical devices, **trading algorithms** | Conformity assessment, documentation, [[explainability-interpretability|explainability]], human oversight |
| **Limited** | Transparency | Chatbots, deepfakes | Must disclose AI use |
| **Minimal** | No requirements | Spam filters, AI in games | Self-regulate |

**Trading AI is classified as "high-risk"** under the EU AI Act — requiring documentation, human oversight, bias testing, and explainability.

## Corporate AI Governance Structure

```
Board of Directors
  └── AI Ethics Committee / Responsible AI Officer
        ├── Model Risk Management (existing in banks — OCC SR 11-7)
        ├── AI Fairness & Bias Review
        ├── Data Governance (privacy, consent, quality)
        ├── AI Security (adversarial attacks, model theft)
        └── Compliance & Regulatory Reporting
```

## Evaluating AI Governance (for Stock Analysis)

When analysing AI-heavy companies, assess:

| Signal | Positive | Negative |
|--------|---------|---------|
| **Governance structure** | Dedicated AI ethics team, published principles | No visible AI governance |
| **Model documentation** | Published model cards, transparency reports | Black-box claims, no disclosure |
| **Bias testing** | Regular bias audits, published results | No fairness testing mentioned |
| **Regulatory engagement** | Proactive regulatory relationships | Adversarial stance toward regulators |
| **Incident response** | Clear process for AI failures | Denial or cover-up of AI errors |

Companies with strong AI governance trade at lower regulatory risk premiums and are more resilient to the inevitable AI incident.

## See Also

- [[ethics-safety-overview]] — Ethics hub
- [[ai-regulation-global]] — Government regulation
- [[explainability-interpretability]] — What governance frameworks require
- [[algorithmic-bias]] — What governance frameworks test for
- [[ai-regulation-trading]] — Trading-specific regulation
- [[artificial-intelligence]] — AI section hub

## Sources

- NIST AI Risk Management Framework (AI RMF 1.0), January 2023
- ISO/IEC 42001:2023 — AI management system standard
- OECD AI Principles (2019, updated 2024)
- Monetary Authority of Singapore (MAS) FEAT Principles, 2018/2021
- US OCC Supervisory Guidance SR 11-7 on model risk management
- EU AI Act, Regulation (EU) 2024/1689
