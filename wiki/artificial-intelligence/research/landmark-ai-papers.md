---
title: "Landmark AI Papers"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Key AI Papers", "Landmark Papers"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[ai-research-overview]]", "[[transformer-architecture]]", "[[attention-mechanism]]", "[[foundation-models]]", "[[generative-adversarial-networks]]", "[[diffusion-models]]", "[[reinforcement-learning]]", "[[history-of-ai]]", "[[artificial-intelligence]]"]
---

# Landmark AI Papers

These papers define the trajectory of modern AI. Each introduced a concept or architecture that created or destroyed billions in market value. Understanding them provides context for evaluating new research claims and anticipating the next capability jump.

## The Essential Papers

### Architecture Breakthroughs

| Year | Paper | Key Contribution | Impact |
|------|-------|-----------------|--------|
| **2012** | *ImageNet Classification with Deep Convolutional Neural Networks* (Krizhevsky et al.) | **AlexNet** — deep [[convolutional-neural-networks|CNNs]] beat traditional CV | Launched the deep learning era; NVIDIA GPU demand began |
| **2014** | *Generative Adversarial Networks* (Goodfellow et al.) | **[[generative-adversarial-networks|GANs]]** — two networks competing to generate realistic data | Foundation for all generative image AI |
| **2015** | *Deep Residual Learning for Image Recognition* (He et al.) | **ResNet** — skip connections enable 100+ layer networks | Standard backbone for all vision AI |
| **2017** | *Attention Is All You Need* (Vaswani et al.) | **[[transformer-architecture|Transformer]]** architecture, [[attention-mechanism|self-attention]] | **The most consequential AI paper ever.** Powers GPT, Claude, Gemini, BERT, and all modern AI |
| **2018** | *BERT: Pre-training of Deep Bidirectional Transformers* (Devlin et al.) | **BERT** — bidirectional pre-training, fine-tuning paradigm | Enabled [[finbert|FinBERT]] and all downstream NLP |
| **2020** | *Language Models are Few-Shot Learners* (Brown et al.) | **GPT-3** — scaling + [[zero-shot-few-shot-learning|in-context learning]] emerge | Proved scaling works; launched the LLM era |
| **2020** | *Denoising Diffusion Probabilistic Models* (Ho et al.) | **[[diffusion-models|DDPM]]** — diffusion beats GANs for generation | Foundation for Stable Diffusion, DALL-E |
| **2021** | *LoRA: Low-Rank Adaptation of Large Language Models* (Hu et al.) | **LoRA** — efficient [[fine-tuning-llms|fine-tuning]] with minimal parameters | Democratised model customisation |

### Scaling & Reasoning

| Year | Paper | Key Contribution | Impact |
|------|-------|-----------------|--------|
| **2020** | *Scaling Laws for Neural Language Models* (Kaplan et al.) | **Scaling laws** — predictable relationship between compute, data, params, and performance | Justified billions in GPU investment; foundation of [[nvidia-ai|NVIDIA]] thesis |
| **2022** | *Chain-of-Thought Prompting* (Wei et al.) | **CoT** — step-by-step reasoning dramatically improves LLM performance | Changed how everyone uses LLMs; key [[prompt-engineering-trading|prompting technique]] |
| **2022** | *Training language models to follow instructions with human feedback* (Ouyang et al.) | **InstructGPT / [[rlhf-constitutional-ai|RLHF]]** — aligning models to human preferences | Made ChatGPT possible; core safety technique |
| **2023** | *Constitutional AI: Harmlessness from AI Feedback* (Bai et al.) | **[[rlhf-constitutional-ai|Constitutional AI]]** — self-critique from principles | [[anthropic|Anthropic's]] alignment approach; powers Claude |
| **2025** | *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL* (DeepSeek) | Open RL-trained reasoning model rivalling closed frontier models at far lower training cost | Triggered the Jan 2025 ~$600B one-day [[nvidia-ai|NVIDIA]] selloff — markets repriced the AI compute thesis |

### Scientific Breakthroughs

| Year | Paper | Key Contribution | Impact |
|------|-------|-----------------|--------|
| **2016** | *Mastering the game of Go with deep neural networks and tree search* (Silver et al.) | **AlphaGo** — [[reinforcement-learning|RL]] + search beats human Go champion | Proved AI can master complex strategy; DeepMind's defining moment |
| **2021** | *Highly accurate protein structure prediction with AlphaFold* (Jumper et al.) | **[[ai-science|AlphaFold]]** — solved 50-year protein folding problem | 2024 Nobel Prize; transformed drug discovery |
| **2024** | *AlphaProof and AlphaGeometry* (DeepMind) | Mathematical reasoning at competition level | Expanding AI capability beyond language/vision |

### Agent & Tool Use

| Year | Paper | Key Contribution | Impact |
|------|-------|-----------------|--------|
| **2022** | *ReAct: Synergizing Reasoning and Acting* (Yao et al.) | **ReAct** — LLMs alternate reasoning and tool use | Foundation of [[agentic-ai|agentic AI]] patterns |
| **2023** | *Toolformer* (Schick et al.) | Models learn to use tools (APIs, calculators) autonomously | Enabled function calling in GPT-4, Claude |
| **2024** | *Reflexion* (Shinn et al.) | Agents learn from their own mistakes through self-reflection | Self-improving agent pattern |

## How to Read AI Papers (for Traders)

You don't need to understand the math. Focus on:
1. **Abstract**: What problem does it solve? What's the result?
2. **Results table**: How much better than previous best? (marginal improvement vs step change)
3. **Limitations section**: What *doesn't* work? (often more honest than the rest)
4. **Compute cost**: How much did it cost to train? (signals who can replicate)
5. **Open-source?**: Will the model/code be released? (competitive dynamics)

## See Also

- [[ai-research-overview]] — Research hub
- [[ai-benchmarks]] — How these papers' models are evaluated
- [[transformer-architecture]] — "Attention Is All You Need" deep dive
- [[foundation-models]] — The models these papers created
- [[history-of-ai]] — Historical context
- [[financial-ml-papers]] — The finance-specific research canon
- [[artificial-intelligence]] — AI section hub

## Sources

- Original papers as cited inline (arXiv / conference proceedings): Vaswani et al. 2017 (Transformer), Devlin et al. 2018 (BERT), Brown et al. 2020 (GPT-3), Kaplan et al. 2020 (Scaling Laws), Wei et al. 2022 (Chain-of-Thought), Ouyang et al. 2022 (InstructGPT/RLHF), Bai et al. 2022 (Constitutional AI), Silver et al. 2016 (AlphaGo), Jumper et al. 2021 (AlphaFold)
- DeepSeek (2025) — DeepSeek-R1 technical report; market reaction widely reported (NVIDIA single-day market-cap loss, Jan 27 2025)
