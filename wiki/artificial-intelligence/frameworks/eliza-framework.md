---
title: "Eliza Framework"
type: concept
created: 2026-04-09
updated: 2026-04-22
status: good
tags: [ai-trading, agents, machine-learning]
aliases: ["Eliza", "elizaOS"]
domain: [ai-trading]
difficulty: advanced
related: ["[[ai-trading-agents]]", "[[crewai]]", "[[langchain]]", "[[virtuals-protocol]]", "[[ai-agent-tokens]]", "[[defai]]", "[[artificial-intelligence]]", "[[ai16z-dao]]", "[[truth-terminal-goat]]", "[[solana]]"]
---

# Eliza Framework

**Eliza** (also known as elizaOS) is an open-source framework for building autonomous AI agents, originally designed for crypto-native applications. It became the dominant framework for building on-chain AI agents during the 2025 [[ai-narrative-arc|AI agent boom]], powering trading bots, social media agents, and DeFi automation tools. Eliza's modular architecture allows agents to interact with blockchains, exchanges, and social platforms through a plugin system.

## Architecture

Eliza agents are composed of:

- **Character files**: Define the agent's personality, knowledge base, and behavioral constraints
- **Plugins**: Modular connectors for external services (exchanges, blockchains, Twitter, Discord, Telegram)
- **Memory**: Persistent storage for conversation history and learned patterns
- **Actions**: Defined behaviors the agent can take (execute trade, post tweet, analyze data)
- **Evaluators**: Decision logic that determines when to take actions based on context

## Why Eliza Dominated Crypto AI

Several factors made Eliza the go-to framework for crypto agents:

1. **Crypto-native**: Built-in plugins for EVM chains, Solana, and DEX interactions
2. **Social integration**: Native Twitter, Discord, and Telegram support for social trading bots
3. **Open-source**: MIT license, active community development
4. **Low barrier**: Character-file-based configuration meant non-developers could create agents
5. **Token ecosystem**: [[virtuals-protocol|Virtuals Protocol]] and other launchpads used Eliza to deploy tokenized agents

## Connection to Virtuals Protocol

[[virtuals-protocol|Virtuals Protocol]] (VIRTUAL) used Eliza as the foundation for its agent launchpad, where users could create, tokenize, and trade AI agents. This created a direct link between the Eliza framework and the speculative AI token market — agents built on Eliza got their own tokens, driving both adoption and hype.

## How Eliza Became the Standard for Crypto AI Agents

Eliza's rise to dominance was not purely technical — it was a convergence of timing, narrative, and ecosystem effects:

### Timeline

| Date | Event |
|---|---|
| **Mid-2024** | Shaw (pseudonymous developer) begins building Eliza as an open-source agent framework |
| **Oct 2024** | [[truth-terminal-goat|Truth Terminal/GOAT]] memecoin mania creates massive demand for AI agent infrastructure |
| **Nov-Dec 2024** | [[ai16z-dao|ai16z DAO]] launches using Eliza; Shaw's dual role as framework creator and ai16z contributor creates flywheel |
| **Dec 2024** | [[virtuals-protocol|Virtuals Protocol]] adopts Eliza for its agent launchpad; hundreds of Eliza-based agents get tokenized |
| **Jan 2025** | Eliza GitHub repo surpasses **10,000+ stars**; becomes one of the fastest-growing open-source projects in crypto |
| **Q1 2025** | Estimated **thousands of agents** deployed using Eliza across Solana, Base, and EVM chains |
| **Q2 2025** | Framework matures; rebranding toward "elizaOS"; focus shifts from hype to infrastructure |

### What Made Eliza Win

1. **First mover in the narrative window**: When the AI agent narrative peaked, Eliza was the only production-ready, crypto-native agent framework available
2. **ai16z as proof of concept**: [[ai16z-dao|ai16z's]] $2B market cap run validated Eliza in the market's eyes
3. **Virtuals Protocol integration**: Virtuals used Eliza as the default framework for its agent launchpad, meaning every new Virtuals agent was an Eliza agent by default — this created massive distribution
4. **Network effects**: As more developers built Eliza plugins, the framework became more useful, attracting more developers (classic open-source flywheel)
5. **Low barrier to entry**: Character files (JSON configs defining agent personality and behavior) meant that non-developers could create agents, dramatically widening the user base

### Adoption Metrics

| Metric | Peak (Q1 2025) | Notes |
|---|---|---|
| **GitHub Stars** | 10,000+ | One of the top-starred crypto repos of 2025 |
| **Active Forks** | 3,000+ | Indicates active development across many teams |
| **Plugins Available** | 50+ | Covering DEXs, social media, analytics, bridges |
| **Agents Deployed** | Thousands (estimated) | Hard to count precisely; many ephemeral |
| **Supported Chains** | Ethereum, Solana, Base, Arbitrum, Polygon, others | Multi-chain from launch |

### Virtuals Protocol Integration

[[virtuals-protocol|Virtuals Protocol]] (VIRTUAL token) was Eliza's most important distribution channel. The integration worked as follows:

1. Users create an agent using Eliza's character file system
2. The agent is deployed on Virtuals' launchpad with its own token
3. The agent token can be traded on Virtuals' bonding curve
4. Revenue from the agent's activities (trading, content creation, services) flows to token holders

This created a speculative layer on top of Eliza — every Eliza agent became a tradeable asset. At peak mania (January 2025), new Eliza-based agent tokens were launching daily, with some reaching $10M+ market caps within hours.

### ai16z DAO Usage

[[ai16z-dao|ai16z]] was the most prominent single deployment of Eliza, using the framework to power:
- Market analysis agents that scanned social sentiment and on-chain data
- Trade recommendation agents operating through the ai16z trust marketplace
- Social media agents that posted analysis and engaged with the community
- The "virtual Marc Andreessen" persona agent

Shaw's role as both Eliza's creator and ai16z's lead developer created a unique dynamic where the framework and its flagship project were deeply intertwined — beneficial for adoption but problematic for claims of decentralization.

---

## Eliza-Based Agents Trading on DEXs

A significant subset of Eliza agents are configured to execute trades autonomously on decentralized exchanges:

### How It Works
1. Agent analyzes inputs (price data, social sentiment, on-chain metrics, other agents' signals)
2. Agent's evaluator logic determines trade signals
3. Agent executes swaps via DEX plugins ([[uniswap|Uniswap]], [[jupiter|Jupiter]], [[raydium|Raydium]], etc.)
4. Agent manages positions (stop losses, take profits, rebalancing)

### Where Eliza Agents Trade

| DEX / Platform | Chain | Agent Activity |
|---|---|---|
| [[jupiter|Jupiter]] | Solana | Highest volume of Eliza agent trades |
| [[raydium|Raydium]] | Solana | Popular for new token sniping |
| [[uniswap|Uniswap]] | Ethereum / L2s | EVM-based agent trades |
| [[hyperliquid|Hyperliquid]] | Hyperliquid L1 | Perp trading by Eliza agents |
| Orca | Solana | Concentrated liquidity strategies |

### Performance Reality

The honest assessment of Eliza agent trading performance:

- **No verified outperformance**: As of 2026, no Eliza-based trading agent has publicly demonstrated sustained alpha generation with audited results
- **Most agents lose money**: The majority of autonomous trading agents, Eliza-based or otherwise, underperform buy-and-hold benchmarks after accounting for gas costs and slippage
- **Social trading agents perform better as marketing than alpha generators**: Agents that post trade ideas on Twitter generate attention (and token demand) regardless of trade quality
- **MEV and sniping agents**: The most profitable Eliza agent use cases are MEV extraction and new token sniping — activities that extract value from other traders rather than generating genuine alpha

---

## Limitations

As documented in the [[ai-narrative-arc|2025 agent narrative]], Eliza-based agents faced the same challenges as all AI trading agents:

- Compounding errors in multi-step reasoning
- Hallucinated actions (believing trades executed when they didn't)
- High API costs for continuous operation
- Overfitting to social media narratives rather than genuine market signals
- Security risks when agents had on-chain execution capability
- **Wallet security**: Agents with private key access are attack vectors; multiple Eliza agent wallets were drained in 2025 through social engineering and plugin vulnerabilities
- **LLM dependency**: Eliza agents inherit the limitations of their underlying LLM (typically GPT-4 or Claude) — including context window limits, inconsistent reasoning, and inability to truly "learn" from trading experience

---

## Trading Relevance

- Eliza is the framework behind many crypto AI agents that trade on [[hyperliquid|Hyperliquid]], [[uniswap|Uniswap]], and other DEXes
- Understanding Eliza helps evaluate [[ai-agent-tokens|AI agent tokens]] — many are simply Eliza agents with a token attached
- The framework's adoption metrics (GitHub stars, active forks) serve as a proxy for AI agent ecosystem health
- **Eliza GitHub activity as signal**: Rising commit frequency, new plugin releases, and contributor growth can signal renewed interest in the AI agent narrative before token prices react
- **"Built on Eliza" as due diligence**: When evaluating an AI agent token, checking whether it actually uses Eliza (vs. just claiming to) is a basic filter — inspect the GitHub repo, not the marketing page
- **Framework risk**: If Eliza development stalls or a superior framework emerges, the entire ecosystem of Eliza-based agent tokens could lose their narrative support

## See Also

- [[ai16z-dao]] — Flagship project built on Eliza (same creator)
- [[ai-trading-agents]] — Broader concept of AI trading agents
- [[crewai]] — Alternative multi-agent framework
- [[langchain]] — LLM orchestration framework
- [[virtuals-protocol]] — Tokenized agent launchpad built on Eliza
- [[ai-agent-tokens]] — Overview of AI agent tokens
- [[ai-narrative-arc]] — The 2024-2026 AI hype cycle
- [[truth-terminal-goat]] — The event that created demand for AI agent infrastructure
- [[defai]] — DeFi + AI convergence category
- [[artificial-intelligence]] — AI section hub
