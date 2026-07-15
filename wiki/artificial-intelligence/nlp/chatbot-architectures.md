---
title: "Chatbot & Conversational AI Architectures"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Chatbot", "Conversational AI", "Chat Architecture"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[foundation-models]]", "[[retrieval-augmented-generation]]", "[[langchain]]", "[[eliza-framework]]", "[[prompt-engineering-trading]]", "[[nlp-overview]]", "[[artificial-intelligence]]"]
---

# Chatbot & Conversational AI Architectures

**Conversational AI** systems enable natural language interaction with trading tools, data, and analysis. From simple rule-based bots to [[foundation-models|LLM]]-powered agents that can query live data, execute research, and maintain context across conversations.

## Architecture Evolution

| Generation | Architecture | Trading Example |
|-----------|-------------|----------------|
| **Rule-based** (1990s) | If-then rules, pattern matching | "What is the price of AAPL?" → lookup price API |
| **Intent-based** (2010s) | NLU classifies intent + extracts entities | Dialogflow/Alexa: "Buy 100 shares of AAPL" → parsed command |
| **Retrieval-based** (2018+) | Search knowledge base for best response | FAQ bots for broker customer service |
| **LLM-powered** (2023+) | [[foundation-models|Foundation model]] with tool access | Trading copilots: natural conversation with live data, wiki search, web research |

## Modern LLM Chatbot Architecture

```
User Message
    ↓
System Prompt (personality, rules, capabilities)
    ↓
LLM (Claude Opus / GPT-5-class) → decides what to do
    ↓
┌─────────────────────────────────────┐
│ Tool Calls (as needed):             │
│  • Wiki search (knowledge base)     │
│  • Price API (live market data)     │
│  • Web search (current events)      │
│  • Calculator (position sizing)     │
│  • Code execution (analysis)        │
└─────────────────────────────────────┘
    ↓
LLM synthesizes tool results into response
    ↓
User receives natural language answer with citations
```

## Key Components

| Component | Purpose | Implementation |
|-----------|---------|---------------|
| **System prompt** | Define personality, rules, capabilities | "You are a trading analyst. Cite sources. Never give financial advice." |
| **Conversation memory** | Maintain context across turns | Store message history, summarize when context window fills |
| **Tool integration** | Access external data and actions | Function calling / tool use via LLM API |
| **[[retrieval-augmented-generation|RAG]]** | Ground responses in real data | Vector search over documents before generating response |
| **Guardrails** | Prevent harmful outputs | Content filters, compliance checks, action limits |
| **Logging** | Record conversations for improvement | Store turns, tool usage, user feedback |

## Trading Chatbot Use Cases

| Use Case | Complexity | Example |
|----------|-----------|---------|
| **Market data query** | Low | "What's BTC trading at?" → price API call |
| **Portfolio Q&A** | Medium | "What's my exposure to tech stocks?" → portfolio API + analysis |
| **Research assistant** | Medium | "Summarize AAPL's latest earnings" → filing retrieval + LLM summary |
| **Strategy discussion** | High | "Should I hedge my ETH position?" → multi-step analysis with market context |
| **Trade execution** | Very high | "Buy 1 BTC at market" → authentication, confirmation, execution |

## Reference Architecture: A Trading Wiki Chatbot

A typical LLM trading assistant over a knowledge base like this one combines:
- [[anthropic|Claude]] (or another frontier LLM) for reasoning and conversation
- Wiki search via [[retrieval-augmented-generation|RAG]] for knowledge base access
- [[cryptodataapi|CryptoDataAPI]] for live and historical crypto market data
- A web-search tool (e.g. Tavily) for current events
- A deep-research tool (e.g. Perplexity) for long-form questions
- Text-to-speech (e.g. ElevenLabs) for a voice interface

## Sources

- Anthropic, "Tool use (function calling)" documentation — how modern LLM agents invoke tools.
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," 2020.
- J. Weizenbaum, "ELIZA — A Computer Program for the Study of Natural Language Communication," 1966 — the original chatbot.
- LangChain / LangGraph documentation — agent and conversational-pipeline frameworks.

## See Also

- [[foundation-models]] — The models powering modern chatbots
- [[retrieval-augmented-generation]] — Grounding chatbot responses in data
- [[langchain]] — Framework for building chatbot pipelines
- [[eliza-framework]] — Crypto-native agent framework (originally inspired by the 1966 ELIZA chatbot)
- [[prompt-engineering-trading]] — Crafting effective system prompts
- [[speech-and-audio-ai]] — Voice interface for chatbots
- [[nlp-overview]] — NLP pipeline hub
- [[artificial-intelligence]] — AI section hub
