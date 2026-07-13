---
title: "Types of Artificial Intelligence"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Types of AI", "AI Types", "ANI", "AGI", "ASI"]
domain: [ai-trading]
difficulty: beginner
related: ["[[history-of-ai]]", "[[foundation-models]]", "[[neural-networks]]", "[[machine-learning-vs-deep-learning]]", "[[artificial-intelligence]]"]
---

# Types of Artificial Intelligence

AI is classified along two dimensions: **capability level** (how general is the intelligence?) and **learning approach** (how does it learn?). Understanding these distinctions helps traders evaluate AI tools realistically — most trading applications use narrow AI, and claims of "general intelligence" in marketing should be treated skeptically.

## By Capability Level

### Narrow AI (ANI) — What We Have

**Artificial Narrow Intelligence** excels at specific tasks but cannot generalize beyond its training domain.

| Example | Capability | Limitation |
|---------|-----------|-----------|
| [[finbert|FinBERT]] | Classifies financial sentiment | Cannot trade, write code, or reason about macro |
| AlphaGo | Plays Go at superhuman level | Cannot play chess or analyze stocks |
| GPT-4 / Claude | Broad language tasks | No real-world agency, can [[hallucinations-ai|hallucinate]] |

All current AI — including [[foundation-models|GPT-4 and Claude]] — is narrow AI. Foundation models are "narrow" in a broader sense: they're excellent at language tasks but don't truly understand markets, physics, or causation.

### General AI (AGI) — What's Projected

**Artificial General Intelligence** would match human-level intelligence across all cognitive domains — reasoning, planning, learning, creativity, and common sense.

- **Status**: Does not exist (as of mid-2026). Frontier models display broad capability and can chain tools, but lack robust real-world agency, reliable long-horizon planning, and grounded causal understanding
- **Timeline estimates**: Vary wildly — [[openai|OpenAI]] suggests "within years," skeptics say decades or never
- **Trading relevance**: AGI would render most trading strategies obsolete (it could outthink all human and narrow-AI competitors simultaneously). For now, this is speculative — not actionable for trading

### Superintelligence (ASI) — Theoretical

**Artificial Superintelligence** would surpass human intelligence across every dimension. Purely theoretical. The subject of [[ai-safety-alignment|AI safety]] research and existential risk debates, not practical trading.

## By Learning Approach

| Approach | How It Learns | Trading Application |
|----------|--------------|-------------------|
| **Supervised learning** | Labeled examples (input → correct output) | Sentiment classification, price prediction |
| **Unsupervised learning** | Finds patterns in unlabeled data | Market regime detection, anomaly detection |
| **[[reinforcement-learning-trading|Reinforcement learning]]** | Trial and error with rewards | [[ai-market-making|Market making]], [[ai-agent-strategies|agent strategies]], execution optimization |
| **Self-supervised learning** | Predicts parts of input from other parts | How [[foundation-models]] (GPT, Claude, LLaMA) are pre-trained |
| **Transfer learning / [[fine-tuning-llms|Fine-tuning]]** | Adapts pre-trained model to new domain | Financial domain adaptation ([[finbert]]) |

## By Architecture

| Architecture | Era | Trading Use |
|-------------|-----|-------------|
| Rule-based / Expert systems | 1980s | Legacy risk systems, compliance rules |
| [[neural-networks|Neural networks]] | 1990s-2010s | Price prediction, pattern recognition |
| [[transformer-architecture|Transformers]] | 2017-present | All modern LLM applications |
| Diffusion models | 2020s-present | Synthetic data generation ([[gan-synthetic-data]]) |

## The Practical Taxonomy for Traders

For trading purposes, the most useful classification is:

1. **Predictive AI**: Models that forecast (price, sentiment, regime) — [[xgboost-trading]], [[lstm-trading]], [[random-forest-trading]]
2. **Generative AI**: Models that produce text, code, analysis — [[foundation-models|Claude, GPT-4]]
3. **Autonomous AI**: Agents that act independently — [[ai-trading-agents]], [[eliza-framework]]
4. **Infrastructure AI**: Compute and data layer — [[nvidia-ai]], [[bittensor-subnets]], [[akash-network]]

## See Also

- [[history-of-ai]] — How we got here
- [[neural-networks]] — The fundamental building block
- [[machine-learning-vs-deep-learning]] — The hierarchy of approaches
- [[foundation-models]] — The current state of the art
- [[ai-safety-alignment]] — Why capability level matters for safety
- [[artificial-intelligence]] — AI section hub

## Sources

- Russell & Norvig, "Artificial Intelligence: A Modern Approach" (4th ed., 2020) — standard taxonomy of AI approaches
- Searle, "Minds, Brains, and Programs" (1980) — the narrow-vs-general / understanding distinction
- Bostrom, "Superintelligence" (2014) — ANI/AGI/ASI framing
- Public statements from [[openai|OpenAI]] and [[anthropic|Anthropic]] leadership on AGI timelines (2023-2026)
