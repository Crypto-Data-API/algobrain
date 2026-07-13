---
title: "Defining Intelligence"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Defining Intelligence", "What Is Intelligence"]
domain: [ai-trading]
difficulty: beginner
related: ["[[philosophy-overview]]", "[[artificial-general-intelligence]]", "[[turing-test]]", "[[types-of-ai]]", "[[history-of-ai]]", "[[artificial-intelligence]]"]
---

# Defining Intelligence

There is no consensus definition of intelligence — in humans or machines. This matters for trading because AI companies' valuations are implicitly tied to claims about their systems' "intelligence," and these claims are built on definitions that are contested, shifting, and often strategically chosen.

## Competing Definitions

| Definition | Source | Implication for AI |
|-----------|--------|-------------------|
| **"The ability to achieve goals in a wide range of environments"** | Legg & Hutter (2007) | Favours general-purpose AI (GPT-4, Claude) |
| **"The ability to learn from experience"** | [[supervised-learning|Machine learning]] community | Current ML systems qualify |
| **"The ability to reason, plan, and solve novel problems"** | Classical AI | Current LLMs are mixed — good at reasoning, weak at true novelty |
| **"The ability to understand"** | Philosophy of mind | Controversial — see [[chinese-room-argument]] |
| **"Whatever humans do that computers can't"** | Common intuition | A moving goalpost — as AI does more, the definition shifts |

## The Moving Goalpost Problem

Every time AI masters a task previously considered "intelligent," the definition shifts:

| Year | Task | Pre-AI: "This requires intelligence" | Post-AI: "This is just computation" |
|------|------|--------------------------------------|-------------------------------------|
| 1997 | Chess | "If a machine beats Kasparov, it's intelligent" | "Chess is just search, not real intelligence" |
| 2011 | Jeopardy! | "Understanding language is the hallmark of intelligence" | "Watson just pattern-matches, not real understanding" |
| 2016 | Go | "Go requires intuition that computers can't replicate" | "AlphaGo uses brute force with neural nets" |
| 2023 | Conversation | "Holding a natural conversation requires understanding" | "LLMs are just [[chinese-room-argument|stochastic parrots]]" |
| 2024 | Coding | "Writing novel code requires creative intelligence" | "Code generation is just sophisticated autocomplete" |

This pattern reveals a bias: we retroactively redefine intelligence to exclude whatever AI can do, preserving human uniqueness. For traders, this means **capability demonstrations are more important than philosophical classification** — what can the AI actually do, regardless of whether we call it "intelligent"?

## Types of Intelligence Relevant to Trading

| Type | Human Level | Current AI Level | Trading Relevance |
|------|------------|-----------------|-------------------|
| **Analytical** | High | High (and scaling) | Market analysis, data processing |
| **Pattern recognition** | High | Superhuman in narrow domains | [[cnn-chart-recognition|Chart patterns]], [[nlp-sentiment-analysis|sentiment]] |
| **Strategic** | High | Superhuman in games ([[reinforcement-learning|RL]]) | Game theory, but markets are harder than Go |
| **Social/emotional** | High | Low (can simulate but doesn't feel) | Understanding market psychology |
| **Creative** | High | Surprisingly good (but derivative) | Strategy ideation, novel combinations |
| **Common sense** | High | Weak (improving rapidly) | Context that prevents foolish AI decisions |

## See Also

- [[philosophy-overview]] — Philosophy hub
- [[artificial-general-intelligence]] — When AI achieves "general" intelligence
- [[turing-test]] — Testing for intelligence
- [[chinese-room-argument]] — Understanding vs simulation
- [[types-of-ai]] — Narrow, general, superintelligence classification
- [[artificial-intelligence]] — AI section hub

## Sources

- Legg & Hutter, "Universal Intelligence: A Definition of Machine Intelligence" (2007) — the "achieve goals across environments" definition
- Chollet, "On the Measure of Intelligence" (2019) — skill-acquisition efficiency and the ARC benchmark, a direct attack on the moving-goalpost problem
- "Stochastic parrots" framing — Bender, Gebru et al., FAccT (2021)
- Historical milestones — Deep Blue v. Kasparov (1997), IBM Watson on Jeopardy! (2011), AlphaGo v. Lee Sedol (2016), LLM coding/conversation capability (2023-2024)
