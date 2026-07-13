---
title: "Tokenization (NLP)"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Tokenization", "BPE", "WordPiece", "SentencePiece", "Token"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[nlp-overview]]", "[[foundation-models]]", "[[word-embeddings]]", "[[transformer-architecture]]", "[[model-inference-vs-training]]", "[[artificial-intelligence]]"]
---

# Tokenization (NLP)

**Tokenization** is the process of splitting text into discrete units (tokens) that a [[foundation-models|language model]] can process. It is the first step in how LLMs "read" — every prompt you send to [[anthropic|Claude]] or [[openai|GPT-4]] is tokenized before the model sees it. Understanding tokenization explains context window limits, API pricing, and why some financial text costs more to process than others.

## How Tokenization Works

Raw text is not fed directly to models. Instead:

```
"AAPL beat Q3 earnings by $0.15" 
→ ["AA", "PL", " beat", " Q", "3", " earnings", " by", " $", "0", ".", "15"]
→ [3280, 6489, 8653, 1195, 18, 24608, 555, 400, 15, 13, 868]
```

Each token maps to an integer ID in the model's vocabulary. The model processes these integer sequences, not raw text.

## Tokenization Algorithms

| Algorithm | Used By | How It Works |
|-----------|---------|-------------|
| **BPE** (Byte-Pair Encoding) | GPT-4, [[anthropic|Claude]], LLaMA | Iteratively merges the most frequent character pairs into tokens |
| **WordPiece** | BERT, [[finbert|FinBERT]] | Similar to BPE but uses likelihood-based merging |
| **SentencePiece** | T5, [[mistral-ai|Mistral]] | Language-agnostic, works directly on raw text (no pre-tokenization) |
| **Tiktoken** | [[openai|OpenAI]] models | OpenAI's fast BPE implementation |

## Why Traders Should Care

### Context Window = Token Limit

When a model has a "200K context window," it means 200,000 tokens — not characters or words.

| Text Type | Approx. Tokens/Word | 200K Token Limit = |
|-----------|--------------------|--------------------|
| English prose | ~1.3 tokens/word | ~150,000 words (~300 pages) |
| Financial text (numbers, tickers) | ~1.8 tokens/word | ~110,000 words |
| Code | ~2.5 tokens/character sequence | Varies widely |

Financial text is token-expensive because numbers, tickers ($AAPL), and currency symbols ($94.8B) each break into multiple tokens.

### API Pricing = Token Count

[[model-inference-vs-training|API costs]] are priced per million tokens. A 50-page 10-K filing might be 80,000 tokens — costing $0.20-$1.20 depending on the model. Processing 500 filings per quarter costs $100-600 in API fees.

### Token Budget Strategy

When analyzing long documents with limited context:
1. **Chunk** the document into sections
2. **Summarize** each chunk individually
3. **Synthesize** summaries into a final analysis
4. Or use [[retrieval-augmented-generation|RAG]] to retrieve only the relevant chunks

## Financial Tokenization Quirks

| Issue | Example | Impact |
|-------|---------|--------|
| **Tickers split** | "$AAPL" → ["$", "AA", "PL"] (3 tokens) | Wastes tokens, model may not recognize ticker |
| **Numbers split** | "$94,832,000" → 5+ tokens | Financial figures are expensive to process |
| **Abbreviations** | "EPS" might be 1 or 2 tokens depending on model | Inconsistent representation |
| **Tables** | Markdown tables tokenize inefficiently | Structure gets flattened |

## See Also

- [[foundation-models]] — The models that use tokenization
- [[word-embeddings]] — What happens after tokenization
- [[nlp-overview]] — NLP pipeline hub
- [[model-inference-vs-training]] — Token-based pricing
- [[transformer-architecture]] — Processes token sequences
- [[artificial-intelligence]] — AI section hub

## Sources

- Sennrich et al., "Neural Machine Translation of Rare Words with Subword Units," 2016 — introduced BPE for NLP.
- Kudo & Richardson, "SentencePiece," 2018 — language-agnostic subword tokenization.
- OpenAI, tiktoken library documentation — BPE tokenizer and per-model token counting.
- D. Jurafsky & J. H. Martin, *Speech and Language Processing*, 3rd ed. — tokenization fundamentals.
