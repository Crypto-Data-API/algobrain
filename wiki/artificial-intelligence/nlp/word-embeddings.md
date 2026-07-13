---
title: "Word Embeddings"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Word Embedding", "Word2Vec", "GloVe", "Word Vectors"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[tokenization-nlp]]", "[[embeddings-vector-databases]]", "[[nlp-overview]]", "[[transformer-architecture]]", "[[finbert]]", "[[natural-language-processing]]", "[[artificial-intelligence]]"]
---

# Word Embeddings

**Word embeddings** are dense vector representations that capture the semantic meaning of words. They map words into a numerical space where similar words are close together — "bullish" is near "optimistic" and far from "recession." Embeddings are the bridge between [[tokenization-nlp|tokenized text]] and the mathematical operations neural networks perform.

## Evolution

| Generation | Method | Key Property | Trading Use |
|-----------|--------|-------------|-------------|
| **Bag of Words** (2000s) | Count word frequencies | No semantics, no order | Basic keyword matching |
| **TF-IDF** (2000s) | Weight words by importance | Finds distinctive words | Identify unusual language in filings |
| **Word2Vec** (2013) | Neural network on word co-occurrence | Words with similar contexts have similar vectors | Word analogies, basic semantic search |
| **GloVe** (2014) | Matrix factorization of co-occurrence | Global context captured | Similar to Word2Vec, slightly different training |
| **Contextual** (2018+) | [[transformer-architecture|Transformer]]-based (BERT, GPT) | Same word gets different vectors in different contexts | "Bank" near "river" vs "bank" near "finance" |
| **Sentence/Document** (2019+) | Sentence-BERT, Ada-002 | Embed entire passages | [[embeddings-vector-databases|Semantic search]], [[retrieval-augmented-generation|RAG]] |

## Why Context Matters for Finance

Static embeddings (Word2Vec) give "bank" one vector. But in finance:
- "The **bank** raised interest rates" → central bank (macro signal)
- "The river **bank** flooded" → irrelevant
- "Goldman Sachs, the investment **bank**" → specific company

Contextual embeddings from [[finbert|FinBERT]] or [[foundation-models|LLMs]] resolve this ambiguity — critical for accurate [[nlp-sentiment-analysis|financial sentiment analysis]].

## Trading Applications

| Application | Embedding Type | How |
|-------------|---------------|-----|
| **Semantic search over filings** | Sentence embeddings | [[embeddings-vector-databases|Vector DB]] search: "Find all paragraphs about margin compression" |
| **Document similarity** | Document embeddings | Cluster earnings calls by theme, detect outliers |
| **Sentiment features** | Contextual word embeddings | Feed FinBERT embeddings to [[xgboost-trading|XGBoost]] as features |
| **Analogy detection** | Word2Vec-style | "recession is to bear market as expansion is to ?" |
| **Cross-lingual analysis** | Multilingual embeddings | Analyze Japanese/Chinese financial news in English models |

## Financial Word Embedding Models

| Model | Source | Best For |
|-------|--------|---------|
| **FinBERT embeddings** | [[hugging-face]] | Financial text representation |
| **Ada-002 / text-embedding-3** | [[openai]] | General-purpose, high quality |
| **Voyage Finance** | Voyage AI | Finance-tuned embeddings |
| **Sentence-BERT** | [[hugging-face]] | Open-source sentence similarity |

## See Also

- [[embeddings-vector-databases]] — Storage and search for embeddings
- [[tokenization-nlp]] — The step before embedding
- [[retrieval-augmented-generation]] — Primary consumer of embeddings
- [[finbert]] — Financial-domain contextual embeddings
- [[nlp-overview]] — NLP pipeline hub
- [[transformer-architecture]] — Powers contextual embeddings
- [[artificial-intelligence]] — AI section hub

## Sources

- Mikolov et al., "Efficient Estimation of Word Representations in Vector Space" (Word2Vec), 2013.
- Pennington et al., "GloVe: Global Vectors for Word Representation," 2014.
- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers," 2018 — contextual embeddings.
- Reimers & Gurevych, "Sentence-BERT," 2019 — sentence-level embeddings for semantic search.
