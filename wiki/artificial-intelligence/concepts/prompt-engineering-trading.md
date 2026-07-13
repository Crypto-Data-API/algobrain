---
title: "Prompt Engineering for Trading"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning]
aliases: ["Prompt Engineering", "Trading Prompts"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[foundation-models]]", "[[llm-market-analysis]]", "[[zero-shot-few-shot-learning]]", "[[ai-trading-agents]]", "[[anthropic]]", "[[openai]]", "[[artificial-intelligence]]"]
---

# Prompt Engineering for Trading

**Prompt engineering** is the practice of crafting instructions that elicit optimal outputs from [[foundation-models|large language models]]. For trading applications, effective prompts are the difference between vague market commentary and actionable, structured analysis. It is the primary skill for traders using AI tools.

## Key Techniques

### Zero-Shot Prompting
Direct instruction with no examples. Works for straightforward tasks:
> "Classify the following headline as bullish, bearish, or neutral for AAPL stock: 'Apple beats revenue expectations by 3%'"

### Few-Shot Prompting
Provide examples of desired input/output format. Improves consistency for [[nlp-sentiment-analysis|sentiment classification]]:
> "Here are examples of how to classify earnings sentiment: ..."

### Chain-of-Thought (CoT)
Ask the model to reason step-by-step. Critical for complex analysis:
> "Analyze this earnings report step by step: First identify the revenue trend, then compare to guidance, then assess margin implications, then conclude with a trading view."

### Structured Output
Request specific formats (JSON, tables) for programmatic processing:
> "Return your analysis as JSON with fields: ticker, direction, confidence (0-1), timeframe, key_drivers"

See [[zero-shot-few-shot-learning]] for the theory behind these techniques.

## Trading-Specific Prompt Patterns

| Pattern | Use Case |
|---------|----------|
| **Analyst role-play** | "You are a senior equity analyst specializing in semiconductors..." |
| **Contrarian challenge** | "Given the bull case above, construct the strongest bear case" |
| **Multi-source synthesis** | "Given these 5 data points [data], what's the unified signal?" |
| **Risk assessment** | "What are the top 3 risks to this trade thesis?" |
| **Historical parallel** | "Has this pattern occurred before? What happened next?" |

## Common Mistakes

1. **Vague prompts** → vague outputs. "What do you think about TSLA?" produces generic commentary
2. **No structure** → unactionable output. Always specify the output format you need
3. **Trusting numbers** → [[hallucinations-ai|hallucinated figures]]. LLMs generate plausible-sounding but incorrect financial data. Always verify specific numbers
4. **Single-prompt reliance** → missed nuance. Use multi-step prompting for complex analysis

## See Also

- [[foundation-models]] — The models being prompted
- [[zero-shot-few-shot-learning]] — The learning paradigms behind prompting
- [[llm-market-analysis]] — Applied financial analysis with LLMs
- [[hallucinations-ai]] — Risks of trusting LLM outputs
- [[ai-trading-agents]] — Agents use prompts as system instructions
- [[retrieval-augmented-generation]] — Grounds prompts in real documents to reduce hallucinated figures
- [[artificial-intelligence]] — AI section hub

## Sources

- Anthropic and OpenAI prompt-engineering guidance (chain-of-thought, structured output, role prompting)
- General practitioner literature on few-shot prompting and structured extraction for financial NLP
