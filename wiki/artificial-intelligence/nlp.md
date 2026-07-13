---
title: "Natural Language Processing (NLP)"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, nlp]
aliases: ["Nlp", "NLP", "Natural Language Processing", "natural-language-processing"]
related: ["[[nlp-overview]]", "[[natural-language-processing-finance]]", "[[nlp-sentiment-analysis]]", "[[finbert]]", "[[bert]]", "[[gpt-4]]", "[[word-embeddings]]", "[[tokenization-nlp]]", "[[named-entity-recognition]]", "[[foundation-models]]"]
difficulty: beginner
domain: [machine-learning]
---

**Natural Language Processing (NLP)** is the branch of [[artificial-intelligence]] concerned with letting computers read, interpret, and generate human language. It spans tasks from classifying the sentiment of a sentence to extracting entities, answering questions, summarizing documents, and generating fluent text. Modern NLP is dominated by [[transformer-trading|transformer]] neural networks and [[foundation-models|large language models]]. In trading, NLP is the bridge from the vast amount of *unstructured text* (news, filings, transcripts, social media) to *structured, tradable signals*.

## Core tasks

| Task | What it does | Finance example |
|------|-------------|-----------------|
| **Tokenization** | Split text into model-readable units | See [[tokenization-nlp]] |
| **Sentiment / text classification** | Label text by category or tone | Bullish/bearish headline tagging |
| **Named entity recognition (NER)** | Extract people, companies, amounts, dates | Pull `$AAPL`, "$1.2B", "Q3" from a filing — see [[named-entity-recognition]] |
| **Summarization** | Condense long text | One-paragraph earnings-call digest |
| **Question answering / RAG** | Answer from a document corpus | "What did the CFO say about margins?" via [[retrieval-augmented-generation|RAG]] |
| **Generation** | Produce fluent text | Draft a research note |
| **Embeddings** | Map text to vectors for similarity | Cluster similar news; see [[word-embeddings]] |

## How modern NLP works

The dominant pipeline is: text → [[tokenization-nlp|tokenization]] → [[word-embeddings|embeddings]] → transformer model → output. Two model families matter most:

- **Encoder models** (e.g. [[bert|BERT]], [[finbert|FinBERT]]) — strong for classification and extraction; cheap and fast.
- **Decoder / generative models** (e.g. [[gpt-4|GPT-4]], Claude) — strong for summarization, reasoning, and open-ended generation.

Pretraining on huge corpora followed by fine-tuning (or prompting) on the target task is the standard recipe.

## Trading and finance relevance

NLP is the engine behind text-driven alpha and research automation:

- **Sentiment signals** — text-derived sentiment has documented short-horizon predictive power, especially around earnings and breaking news; see [[nlp-sentiment-analysis]] and [[social-sentiment-analysis]].
- **Fundamental/document automation** — parsing 10-Ks, transcripts, and analyst reports at scale; see earnings-call-analysis and [[llm-market-analysis]].
- **Event detection** — flagging market-moving events from news faster than humans.
- **Alternative data** — turning Reddit/X chatter, Glassdoor reviews, and consumer text into datasets.

For the finance-specific deep dive see [[natural-language-processing-finance]] and the section overview [[nlp-overview]]. Pitfalls — overfitting to noisy text, latency/cost of large models, and look-ahead from using post-event corpora — are real; see [[ai-trading-risks]].

## Related

- [[nlp-overview]] — the trading-focused NLP section hub
- [[natural-language-processing-finance]] — finance-specific NLP
- [[finbert]] — finance-tuned sentiment model
- [[gpt-4]], [[bert]] — model families
- [[foundation-models]] — large pretrained models

## Sources

- D. Jurafsky & J. H. Martin, *Speech and Language Processing*, 3rd ed. (standard NLP text).
- [[book-hands-on-ml-algorithmic-trading]] — applied NLP for trading.
- [[book-the-book-of-alternative-data]] — text as alternative data.
