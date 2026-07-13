---
title: "RLHF & Constitutional AI"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["RLHF", "Constitutional AI", "Reinforcement Learning from Human Feedback"]
domain: [ai-trading]
difficulty: advanced
related: ["[[foundation-models]]", "[[anthropic]]", "[[openai]]", "[[ai-safety-alignment]]", "[[hallucinations-ai]]", "[[artificial-intelligence]]"]
---

# RLHF & Constitutional AI

**RLHF** (Reinforcement Learning from Human Feedback) and **Constitutional AI** are the alignment techniques that make [[foundation-models|foundation models]] useful and safe. They're the reason Claude and GPT-4 give helpful, structured financial analysis instead of incoherent text — and understanding their limitations explains why LLMs sometimes fail at financial tasks.

## RLHF (OpenAI's Approach)

1. **Pre-train** a language model on internet text
2. **Collect human preferences**: Show humans two model outputs, ask which is better
3. **Train a reward model** on those preferences
4. **Fine-tune the LLM** using reinforcement learning to maximize the reward model's score

RLHF is used by [[openai|OpenAI]] (GPT-4), [[google-deepmind|Google]] (Gemini), and others. It aligns models to human preferences but can create biases — models may be overly cautious about financial advice or hedge their outputs with excessive caveats.

## Constitutional AI (Anthropic's Approach)

[[anthropic|Anthropic's]] approach uses a set of written principles (a "constitution") to guide model behavior:

1. Model generates responses
2. Model critiques its own responses against the constitution
3. Model revises based on self-critique
4. Process is repeated to create training data for alignment

This creates models that are more transparent about their reasoning and limitations — useful for financial applications where you need to understand why a model reached a conclusion.

## Trading Implications

- **Safety guardrails** can block legitimate financial analysis (model refuses to discuss specific trades)
- **Hedging language** ("This is not financial advice") dilutes actionable output — prompt engineering can mitigate this
- Models aligned via RLHF may have **sycophancy bias** — telling you what you want to hear rather than challenging your thesis
- Understanding alignment helps explain why models sometimes refuse to engage with [[risk-management|risk scenarios]] or bearish analyses

## See Also

- [[foundation-models]] — The models being aligned
- [[anthropic]] — Creator of Constitutional AI
- [[openai]] — Pioneer of RLHF
- [[ai-safety-alignment]] — Broader safety landscape
- [[hallucinations-ai]] — A problem alignment tries to reduce
- [[prompt-engineering-trading]] — Mitigating sycophancy and over-hedging through prompting
- [[artificial-intelligence]] — AI section hub

## Sources

- Christiano et al., "Deep Reinforcement Learning from Human Preferences" and OpenAI InstructGPT papers (RLHF)
- Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (Anthropic)
- Anthropic published material on Constitutional AI and Claude alignment methodology
