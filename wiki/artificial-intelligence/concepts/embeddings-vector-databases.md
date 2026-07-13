---
title: "Embeddings & Vector Databases"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, indicators]
aliases: ["Embeddings", "Vector Database", "Semantic Search"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[retrieval-augmented-generation]]", "[[langchain]]", "[[hugging-face]]", "[[foundation-models]]", "[[feature-engineering-finance]]", "[[artificial-intelligence]]"]
---

# Embeddings & Vector Databases

**Embeddings** are numerical vector representations of text (or images, audio) that capture semantic meaning. **Vector databases** store and efficiently search these embeddings. Together, they power [[retrieval-augmented-generation|RAG]] systems, semantic search, and similarity-based analysis in trading applications.

## How Embeddings Work

An embedding model converts text into a high-dimensional vector (typically 384-3072 dimensions) where semantically similar texts are close together:

- "Federal Reserve raises interest rates" → `[0.23, -0.81, 0.45, ...]`
- "Fed hikes rates by 25 basis points" → `[0.25, -0.79, 0.43, ...]` (very similar vector)
- "Apple launches new iPhone" → `[0.67, 0.12, -0.33, ...]` (very different vector)

Similarity between two vectors is measured by **cosine similarity** (the cosine of the angle between them, the most common choice for text), dot product, or Euclidean distance. "Close together" means a high cosine similarity / small distance. A vector database indexes millions of such vectors so that the nearest neighbours to a query vector can be found in milliseconds, typically via **approximate nearest neighbour (ANN)** algorithms such as HNSW or IVF, which trade a small amount of recall for large speed gains.

## Common Embedding Models

| Model | Provider | Dimensions | Notes |
|-------|----------|-----------|-------|
| **text-embedding-3-large / -small** | [[openai]] | up to 3072 | Strong general-purpose, adjustable dimensions |
| **Voyage / voyage-finance-2** | Voyage AI | 1024+ | Domain-tuned variants for finance |
| **all-MiniLM-L6-v2** | sentence-transformers ([[hugging-face]]) | 384 | Tiny, fast, runs locally — good for prototyping |
| **[[finbert\|FinBERT]]-based encoders** | open-source | 768 | Finance-domain language understanding |

Domain choice matters: a finance-tuned embedding model places "duration risk" and "interest-rate sensitivity" closer together than a generic model would, improving retrieval quality on financial corpora.

## Trading Applications

| Application | How It Works |
|-------------|-------------|
| **Semantic search** | Find all earnings calls discussing "margin compression" regardless of exact wording |
| **Document clustering** | Group SEC filings by topic automatically |
| **Similarity detection** | Find historical periods with similar market commentary |
| **[[retrieval-augmented-generation|RAG]]** | Ground LLM answers in relevant financial documents |
| **Anomaly detection** | Flag press releases whose language diverges from historical patterns |

## Vector Database Options

| Database | Type | Trading Use Case |
|----------|------|-----------------|
| **Pinecone** | Managed cloud | Production RAG pipelines |
| **Chroma** | Local/embedded | Prototype and personal research |
| **Weaviate** | Open-source | Self-hosted financial search |
| **FAISS** | Library (Meta) | High-performance local search |
| **pgvector** | PostgreSQL extension | Integrated with existing data infrastructure |
| **Qdrant** | Open-source / managed | Rust-based, filtered search on metadata |
| **Milvus** | Open-source | Large-scale, billion-vector deployments |

For most personal trading-research stacks, **Chroma** or **pgvector** are sufficient — there is no need for a managed service until corpus size or query volume becomes large.

## A Concrete Caveat for Traders

Semantic similarity is not the same as *signal*. Two earnings calls that embed close together are linguistically similar, which is useful for retrieval and clustering — but it does not imply their stocks will behave similarly. Embeddings are a search and organisation tool, not a predictive feature on their own. Used naively as model inputs they can leak look-ahead bias (embedding models are trained on data that may post-date the period being studied) and overfit to vocabulary fashions. Treat them as a way to *find* relevant documents fast, then apply judgement.

## See Also

- [[retrieval-augmented-generation]] — Primary use case for vector databases
- [[langchain]] — Framework for building embedding pipelines
- [[hugging-face]] — Source of embedding models
- [[feature-engineering-finance]] — Related concept in ML trading
- [[artificial-intelligence]] — AI section hub

## Sources

- OpenAI embeddings documentation (text-embedding-3 family)
- sentence-transformers / Hugging Face model cards (all-MiniLM, etc.)
- Pinecone, Chroma, Weaviate, Qdrant, pgvector official documentation
- Malkov & Yashunin, "Efficient and robust approximate nearest neighbor search using HNSW graphs" (2018)
