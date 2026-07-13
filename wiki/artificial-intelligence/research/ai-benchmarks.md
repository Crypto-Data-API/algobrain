---
title: "AI Benchmarks"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["AI Benchmarks", "LLM Benchmarks", "MMLU", "HumanEval", "GPQA", "SWE-bench", "Humanity's Last Exam"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[ai-research-overview]]", "[[ai-evaluation-metrics]]", "[[foundation-models]]", "[[financial-ml-papers]]", "[[artificial-intelligence]]"]
---

# AI Benchmarks

**Benchmarks** are standardised tests used to compare AI model capabilities. When [[openai|OpenAI]] claims a model scores ~94% on GPQA Diamond or [[anthropic|Anthropic]] reports Claude's SWE-bench Verified score, these are benchmark results. Understanding benchmarks helps traders evaluate model comparisons, marketing claims, and capability trajectories.

> **June 2026 note:** The benchmark landscape has shifted decisively. The benchmarks that defined 2023-2024 (MMLU, HumanEval, HellaSwag, GSM8K) are now **saturated** — every frontier model scores 88%+ — and have been replaced as frontier discriminators by **GPQA Diamond** (expert science), **Humanity's Last Exam / HLE** (broad expert reasoning, the new "ceiling"), **SWE-bench Verified** (real agentic coding), **ARC-AGI-2** (novel reasoning), and **FrontierMath** (research-level math). When a lab markets a model in 2026, watch these, not MMLU.

## The Frontier Benchmarks (2026)

These are the benchmarks that actually separate frontier models in 2026 — the legacy tests below are saturated.

| Benchmark | What It Tests | Scale | Status (mid-2026) |
|-----------|--------------|-------|-------------------|
| **GPQA Diamond** | Graduate-level "Google-proof" science questions (physics, chem, bio) | 0-100% | Primary science discriminator; frontier models ~90-94% |
| **Humanity's Last Exam (HLE)** | ~2,500 expert-crafted questions across all fields, contamination-resistant | 0-100% | The new "ceiling" benchmark; frontier models still well short of saturation |
| **SWE-bench Verified** | Real GitHub issues → working pull requests (human-validated subset) | 0-100% | The standard agentic-coding test; best agents ~70-80% |
| **ARC-AGI-2** | Novel abstract-reasoning puzzles designed to resist memorisation | 0-100% | Headline "fluid reasoning" test; frontier systems making rapid gains |
| **FrontierMath** | Research-level mathematics (Tao/Terence-tier hard) | 0-100% | Very low scores even for best models; far from saturated |
| **AIME** | Competition math (American Invitational Mathematics Examination) | 0-100% | Top reasoning models now near-perfect on recent years |
| **LiveCodeBench** | Contamination-resistant competitive coding (rolling problem set) | 0-100% | Complements SWE-bench for raw coding |
| **GAIA / BFCL** | General assistant tasks / function-calling for agents | 0-100% | Tool-use and agentic capability |

## Legacy LLM Benchmarks (Mostly Saturated)

These defined 2022-2024 and still appear in marketing, but offer little frontier signal now — every top model clusters near the ceiling.

### General Knowledge & Reasoning

| Benchmark | What It Tests | Scale | Status |
|-----------|--------------|-------|--------|
| **MMLU** (Massive Multitask Language Understanding) | 57 subjects from STEM to humanities | 0-100% | **Saturated** — frontier models all 88%+ |
| **MMLU-Pro** | Harder MMLU with 10-choice questions | 0-100% | Near-saturated (~83-90% at the frontier) |
| **ARC-Challenge** | Grade-school science questions requiring reasoning | 0-100% | Saturated (~95%+) |
| **HellaSwag** | Common sense reasoning (sentence completion) | 0-100% | Solved (>95%) |
| **WinoGrande** | Pronoun resolution requiring common sense | 0-100% | Solved |
| **GSM8K** | Grade-school math word problems | 0-100% | Saturated (>95%) |
| **MATH** | Competition-level mathematics | 0-100% | Largely solved by reasoning models; superseded by AIME/FrontierMath |

### Coding

| Benchmark | What It Tests | Scale | Status |
|-----------|--------------|-------|--------|
| **HumanEval** | Python function generation from docstrings | 0-100% (pass@1) | **Saturated (~90%+)** — superseded by SWE-bench Verified |
| **HumanEval+** | Harder version with edge cases | 0-100% | Largely saturated |
| **MBPP** (Mostly Basic Python Problems) | Simple programming tasks | 0-100% | Saturated |
| **SWE-bench** (full) | Real GitHub issues → working pull requests | 0-100% | Superseded by the human-validated **SWE-bench Verified** subset |

### Long Context

| Benchmark | What It Tests | Scale |
|-----------|--------------|-------|
| **NIAH** (Needle in a Haystack) | Find a specific fact embedded in long context | Pass/fail at various context lengths |
| **RULER** | Multiple retrieval and reasoning tasks across long contexts | 0-100% |
| **InfiniteBench** | Tasks requiring 100K+ tokens of context | 0-100% |

## Financial-Specific Benchmarks

| Benchmark | What It Tests | Relevance |
|-----------|--------------|----------|
| **FinBen** (FinanceBench) | Financial QA from real filings | Can the model answer questions about 10-K filings accurately? |
| **FLUE** (Financial Language Understanding Evaluation) | Financial NLP tasks (sentiment, NER, classification) | How well does the model understand financial text? |
| **BizBench** | Business and financial reasoning | Multi-step financial calculations and logic |
| **CFLUE** (Chinese Financial Language Understanding) | Chinese financial NLP | Relevant for Chinese market analysis |

## How to Interpret Benchmark Results

### What Benchmarks Tell You
- **Relative ranking**: Which model is better at specific tasks
- **Capability trajectory**: Year-over-year improvement rates
- **Category strengths**: Model A better at reasoning, Model B better at code

### What Benchmarks DON'T Tell You
- **Real-world performance**: A model scoring 90% on MMLU may still [[hallucinations-ai|hallucinate]] financial figures
- **Domain expertise**: General benchmarks don't test financial knowledge specifically
- **Latency and cost**: A model might score highest but be too slow or expensive
- **Consistency**: Benchmarks test average performance, not worst-case
- **Contamination**: Models may have been trained on benchmark data (inflating scores)

### The Benchmark Saturation Problem

Benchmark saturation is now a defining feature of the field. As of mid-2026:
- MMLU, HumanEval, GSM8K, HellaSwag, WinoGrande are all effectively solved at the frontier
- The field churns through benchmarks roughly every 12-18 months: a new "hard" benchmark is released, models reach it within a year, and a harder one replaces it (MMLU → MMLU-Pro → GPQA → HLE)
- Contamination-resistant, rolling-problem-set designs (LiveCodeBench, FrontierMath, ARC-AGI-2, HLE) are now preferred precisely because they resist memorisation
- This is partly a positive signal — capabilities grow faster than tests — but it also makes cross-year, cross-model comparisons treacherous: a "state-of-the-art" claim is only meaningful against a current, uncontaminated benchmark

## Benchmark Watching for Trading

When a model provider announces new benchmark results:
1. **Compare to competitors**: Is this a meaningful gap or within noise?
2. **Check the benchmark**: Is it well-known and respected, or a cherry-picked obscure test?
3. **Financial benchmarks specifically**: Does it improve on financial tasks, or just general ones?
4. **Practical test**: Try the model on your actual trading tasks — benchmark scores don't guarantee domain performance

## See Also

- [[ai-research-overview]] — Research hub
- [[ai-evaluation-metrics]] — The mathematical metrics behind benchmark scores
- [[foundation-models]] — The models being benchmarked
- [[financial-ml-papers]] — Academic research on financial ML evaluation
- [[artificial-intelligence]] — AI section hub

## Sources

- MMLU: Hendrycks et al., "Measuring Massive Multitask Language Understanding" (2020), arXiv:2009.03300
- HumanEval: Chen et al., "Evaluating Large Language Models Trained on Code" (2021), arXiv:2107.03374
- GPQA: Rein et al., "GPQA: A Graduate-Level Google-Proof Q&A Benchmark" (2023), arXiv:2311.12022
- Humanity's Last Exam — Center for AI Safety & Scale AI, agi.safe.ai (2025)
- SWE-bench: Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (2023), arXiv:2310.06770; SWE-bench Verified subset (OpenAI, 2024)
- ARC-AGI / ARC-AGI-2 — François Chollet, Abstraction and Reasoning Corpus (arcprize.org)
- FrontierMath — Epoch AI (2024)
- Benchmark landscape and saturation status as of June 2026 — Perplexity sonar synthesis (kili-technology.com AI benchmarks guide 2026; demandsphere AI frontier model tracker; mysummit.school LLM benchmarks 2026), retrieved 2026-06-12
