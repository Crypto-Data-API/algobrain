---
title: "Data Privacy in AI"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["AI Data Privacy", "AI Privacy", "Training Data Extraction"]
domain: [risk-management]
difficulty: intermediate
related: ["[[ai-security-overview]]", "[[model-poisoning]]", "[[ai-regulation-global]]", "[[ai-intellectual-property]]", "[[foundation-models]]", "[[ai-security-trading]]", "[[artificial-intelligence]]"]
---

# Data Privacy in AI

**AI data privacy** concerns the risk that AI models unintentionally memorise and leak sensitive information from their training data. [[foundation-models|Large language models]] have been shown to reproduce verbatim passages from training data, including private information, API keys, phone numbers, and proprietary content. For trading firms, this means proprietary strategies, client data, or internal communications used with AI tools could be exposed.

## How Models Leak Data

| Leakage Type | How | Trading Risk |
|-------------|-----|-------------|
| **Memorisation** | Model memorises rare/unique training sequences and reproduces them | Proprietary strategy descriptions in training data can be extracted |
| **Training data extraction** | Adversarial prompts cause model to output training data | "Repeat the word 'poem' forever" → GPT-3.5 produced personal info from training |
| **Context window leakage** | In multi-user systems, one user's context leaks to another | Trading firm's analysis shared across users of same model instance |
| **Fine-tuning leakage** | [[fine-tuning-llms|Fine-tuned]] model exposes proprietary fine-tuning data | Model fine-tuned on internal research leaks that research |
| **Log exposure** | Model provider stores and accesses prompts/responses | Your trading queries visible to [[openai|OpenAI]]/[[anthropic|Anthropic]] employees (check data policies) |

## Trading-Specific Concerns

### Using Commercial LLMs for Trading Research

When you send a trading hypothesis to ChatGPT or Claude:
- **Is your prompt stored?** Check the provider's data retention policy
- **Can it be used for training?** Most providers offer opt-out for API users
- **Could another user extract it?** Memorisation risk is low but non-zero for rare/unique content

### Self-Hosted vs API Models

| | API (OpenAI, Anthropic) | Self-Hosted ([[meta-ai|LLaMA]], [[mistral-ai|Mistral]]) |
|---|---|---|
| **Data leaves your network** | Yes | No |
| **Provider can see prompts** | Yes (unless enterprise agreement) | No |
| **Training data risk** | Provider controls | You control |
| **Privacy guarantee** | Contractual | Technical |
| **Cost** | Per-token | GPU hardware |

For sensitive trading operations, self-hosted [[open-source-ai-movement|open-weight models]] provide the strongest privacy guarantee — data never leaves your infrastructure.

## Defences

| Defence | How |
|---------|-----|
| **Enterprise agreements** | Negotiate data retention, training exclusion, audit rights with AI providers |
| **Self-hosting** | Run open-weight models on your own infrastructure |
| **Data classification** | Classify what can/cannot be sent to external AI systems |
| **Differential privacy** | Add noise during training to prevent memorisation |
| **Data sanitisation** | Strip PII and proprietary information before using with AI |
| **Access controls** | Limit who can use AI tools and with what data |

## Regulatory Requirements

| Regulation | Privacy Requirement |
|-----------|-------------------|
| **GDPR** (EU) | Right to erasure — can you delete training data from a model? (technically very difficult) |
| **CCPA** (California) | Consumer data rights apply to AI training data |
| **Financial regulations** (MiFID II, Reg S-P) | Client data protection extends to AI processing |
| **[[ai-regulation-global|EU AI Act]]** | Data governance requirements for high-risk AI |

## See Also

- [[ai-security-overview]] — AI security hub
- [[model-poisoning]] — Related data integrity concern
- [[ai-regulation-global]] — Privacy regulation
- [[ai-intellectual-property]] — IP in training data
- [[foundation-models]] — Models that memorise data
- [[open-source-ai-movement]] — Self-hosted privacy solution
- [[artificial-intelligence]] — AI section hub
