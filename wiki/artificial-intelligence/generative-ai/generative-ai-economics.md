---
title: "Generative AI Economics"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["GenAI Economics", "AI Unit Economics", "Token Economics"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[generative-ai-overview]]", "[[generative-ai-landscape]]", "[[model-inference-vs-training]]", "[[foundation-models]]", "[[nvidia-ai]]", "[[open-source-ai-movement]]", "[[artificial-intelligence]]"]
---

# Generative AI Economics

Understanding the **unit economics** of generative AI — training costs, inference pricing, ROI for adopters, and the build-vs-buy decision — is essential for both using AI in trading and investing in AI companies. The economics determine which AI business models are sustainable and which are burning cash for market share.

## Training Costs

| Model | Estimated Training Cost | Compute Used |
|-------|------------------------|-------------|
| **GPT-4** (2023) | $50-100M+ | ~25,000 [[nvidia-ai|A100]] GPUs for months |
| **Frontier models** (GPT-4o, Claude Opus, Gemini class, 2024-25) | $100M-$1B+ (estimated) | Tens of thousands of [[nvidia-ai|H100/H200]] GPUs for months |
| **LLaMA 3 405B** | ~$10-30M | Meta's internal GPU cluster |
| **Mistral 7B** | ~$500K-1M | Efficient architecture, smaller scale |
| **[[finbert|FinBERT]]** | ~$10K | Single GPU, days |

Training is a **fixed cost** — once the model is trained, the cost is sunk. The economics depend on amortising this cost across enough inference revenue. Frontier-model training costs have climbed roughly an order of magnitude per generation, which is why only a handful of well-capitalised labs ([[openai|OpenAI]], [[anthropic|Anthropic]], Google, Meta, xAI) can compete at the frontier.

## Inference Pricing (What You Pay)

Published list prices as of June 2026 (USD per 1M tokens). Prices drift frequently; treat as indicative, not authoritative:

| Provider | Model | Input (per 1M tokens) | Output (per 1M tokens) | Monthly Cost (Heavy Use) |
|----------|-------|----------------------|----------------------|-------------------------|
| [[anthropic|Anthropic]] | Claude Opus 4.8 | $5.00 | $25.00 | $200-2,000 |
| [[anthropic|Anthropic]] | Claude Sonnet 4.6 | $3.00 | $15.00 | $100-1,000 |
| [[anthropic|Anthropic]] | Claude Haiku 4.5 | $1.00 | $5.00 | $20-200 |
| [[openai|OpenAI]] | GPT-4o | $5.00 | $15.00 | $100-1,000 |
| [[openai|OpenAI]] | GPT-4o mini | $0.15 | $0.60 | $10-100 |
| [[mistral-ai|Mistral]] | Mistral Large | $2.00 | $6.00 | $50-500 |
| Self-hosted | [[meta-ai|LLaMA 70B]] | ~$0.50 (GPU amortised) | ~$0.50 | $200-500 (GPU rental) |

Two structural cost-reducers materially change the math for trading workloads:
- **Prompt caching** — reusing a cached prefix (e.g. a long system prompt of trading rules, or the same filing across many queries) cuts input cost by up to ~90% on the cached portion across major providers.
- **Batch processing** — non-time-sensitive jobs (overnight earnings sweeps, historical sentiment backfills) run at roughly half price.

For a research pipeline that re-reads the same documents repeatedly, caching plus batching can drop the effective per-token cost well below the list prices above.

## ROI for Trading Applications

| Application | Monthly AI Cost | Time Saved | Value Created |
|-------------|----------------|-----------|---------------|
| **Research automation** (earnings analysis) | $200-500 | 20+ hours/month | Faster, broader coverage |
| **Code generation** (backtesting scripts) | $50-200 | 10+ hours/month | Strategies tested 10x faster |
| **Sentiment analysis at scale** | $100-300 | Impossible manually at this scale | Alpha from NLP signals |
| **Trading agent** (experimental) | $500-2,000 | Continuous operation | Unclear — most don't profit yet |

For solo traders, AI tools at $100-500/month provide research capability that previously required a team. The ROI is clearly positive for research and code generation; uncertain for autonomous trading.

## Build vs Buy

| | Build (Self-Hosted) | Buy (API) |
|---|---|---|
| **Upfront cost** | GPU hardware ($10-40K) or cloud ($1-5K/month) | None |
| **Marginal cost** | Low (electricity + maintenance) | Per-token |
| **Privacy** | Full — data never leaves your infrastructure | Data sent to provider (enterprise agreements available) |
| **Model quality** | [[open-source-ai-movement|Open models]] (LLaMA, Mistral) — good but not best | Frontier models (GPT-4, Claude Opus) — best available |
| **Maintenance** | You manage infrastructure, updates | Provider handles everything |
| **Best for** | High-volume production, sensitive data | Prototyping, moderate volume, best quality needed |

The trend: **start with APIs, move to self-hosted as volume grows and requirements crystallise.**

## The Profitability Question

Frontier foundation-model labs ran at large operating losses through the 2023-2025 build-out, with revenue scaling fast but capital expenditure on next-generation training and inference capacity scaling faster:
- [[openai|OpenAI]]: revenue grew from ~$3.7B (2024) into the tens of billions on an annualised run-rate by 2026, while continuing to spend heavily on training and data-centre commitments.
- [[anthropic|Anthropic]]: revenue scaled from roughly $1B (2024) to a multi-billion run-rate, funded by large investor rounds (notably from Amazon and Google).
- The bet: inference gross margins are positive per-token, so as usage compounds and training costs are amortised across a larger base, the business converges to profitability.

For investors, the core risk is **price compression**: as competition intensifies and [[open-source-ai-movement|open-source models]] close the quality gap, list prices fall (the table above shows several rounds of cuts since 2024). The durable winners are those with either a cost advantage (efficient training, owned compute) or a distribution/lock-in advantage, not those relying on a permanent quality moat. This is the central thesis underpinning the AI exposure in [[nvidia|NVIDIA]] and the hyperscalers (microsoft, Google, Amazon) versus pure-play model labs.

## See Also

- [[generative-ai-overview]] — GenAI hub
- [[generative-ai-landscape]] — Market map and competitive dynamics
- [[model-inference-vs-training]] — Compute cost breakdown
- [[foundation-models]] — The models being priced
- [[nvidia-ai]] — Infrastructure economics
- [[open-source-ai-movement]] — The cost-pressure dynamic
- [[artificial-intelligence]] — AI section hub

## Sources

- Anthropic — Claude API pricing (Opus 4.8, Sonnet 4.6, Haiku 4.5), retrieved June 2026
- OpenAI — API pricing (GPT-4o, GPT-4o mini), retrieved June 2026
- Third-party pricing trackers (aipricing.guru, cloudzero.com) corroborating provider list prices, June 2026
- Public reporting on OpenAI and Anthropic revenue run-rates and funding (2024-2026)
