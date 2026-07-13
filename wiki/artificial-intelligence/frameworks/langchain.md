---
title: "LangChain & LangGraph"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, agents, machine-learning]
aliases: ["LangChain", "LangGraph"]
domain: [ai-trading]
difficulty: advanced
related: ["[[ai-trading-agents]]", "[[eliza-framework]]", "[[crewai]]", "[[anthropic]]", "[[openai]]", "[[artificial-intelligence]]"]
---

# LangChain & LangGraph

**LangChain** is the most widely used open-source framework for building applications powered by large language models. **LangGraph**, built on top of LangChain, adds stateful graph-based agent orchestration. Together they form the standard toolkit for building [[ai-trading-agents|AI trading agents]] that need to chain together multiple LLM calls, tool uses, and decision points.

## LangChain

LangChain provides modular components for LLM applications:

- **Models**: Unified interface to [[anthropic|Claude]] (via `langchain-anthropic`), [[openai|GPT-4o]] (via `langchain-openai`), Gemini, and other LLMs — swap providers by changing one line
- **Prompts**: Template management and few-shot example injection
- **Chains**: Sequential pipelines that pass output from one step to the next
- **Tools**: Functions that LLMs can call (API queries, calculations, database lookups)
- **Memory**: Conversation and context persistence between calls
- **Retrieval**: RAG (Retrieval Augmented Generation) for querying document stores

### Trading Example

A typical LangChain trading pipeline:

1. **Retrieve** relevant market news from a vector database
2. **Analyze** sentiment using Claude or GPT-4o
3. **Generate** a trading signal based on the analysis
4. **Validate** against risk management rules (tool call)
5. **Execute** via exchange API (tool call)

```python
# Minimal LangGraph trading-research agent (illustrative)
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

llm = ChatAnthropic(model="claude-sonnet-4-6")        # provider-agnostic swap point
tools = [get_price, get_news, run_indicator, check_risk]  # @tool-decorated functions
agent = create_react_agent(llm, tools)                # ReAct loop: reason -> call tool -> observe

result = agent.invoke({"messages": [("user",
    "Is NVDA showing a momentum breakout? Check price, RSI, and news, "
    "then size a position under the 2% risk rule.")]})
```

## LangGraph

LangGraph extends LangChain with **stateful, cyclical agent graphs** — enabling agents that:

- Loop through observe-think-act cycles
- Branch based on conditions (different agents for different market regimes)
- Maintain persistent state across interactions
- Handle interruptions and human-in-the-loop checkpoints

This makes LangGraph particularly suited for trading agents that need to continuously monitor markets, adapt to changing conditions, and maintain state across trading sessions.

## Ecosystem

| Component | Purpose | Trading Use |
|-----------|---------|-------------|
| **LangSmith** | Observability and debugging | Trace agent decisions, debug failed trades |
| **LangServe** | Deploy as API | Serve trading agents as microservices |
| **LangChain Hub** | Prompt sharing | Community trading prompts and chains |

## Maturity and Trade-offs

LangChain is the most adopted LLM-application framework by GitHub stars and downloads, with LangGraph now the recommended path for stateful/agentic workloads and LangSmith offered as a paid observability layer. Caveats worth knowing for production trading systems:

- **Abstraction churn** — the framework has restructured its APIs and package layout multiple times (split into `langchain-core`, provider packages, and `langgraph`); pin versions and budget for migration.
- **Heavy abstractions** — for simple single-call pipelines, raw provider SDKs (the [[anthropic]] or [[openai]] SDK) are leaner; LangChain pays off when you need orchestration, retrieval, and multi-step state.
- **Alternatives** — direct SDKs with the [[model-context-protocol|Model Context Protocol]] for tools, or lighter agent frameworks, are increasingly used where teams want fewer dependencies.

## See Also

- [[ai-trading-agents]] — Multi-agent trading systems
- [[crewai]] — Higher-level multi-agent framework built on LangChain
- [[eliza-framework]] — Crypto-native alternative
- [[agentic-ai]] — The agent patterns LangGraph implements
- [[anthropic]] — Claude models accessible through LangChain
- [[openai]] — GPT-4o models accessible through LangChain
- [[artificial-intelligence]] — AI section hub

## Sources

- LangChain / LangGraph official documentation and package ecosystem (langchain-core, langgraph, langsmith), reviewed June 2026
- Anthropic and OpenAI provider integration packages for LangChain
