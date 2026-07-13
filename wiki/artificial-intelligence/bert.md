---
title: "BERT"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, indicators]
aliases: ["BERT", "Bidirectional Encoder Representations from Transformers", "bert"]
domain: [ai-trading]
difficulty: intermediate
prerequisites: ["[[transformer-architecture]]", "[[word-embeddings]]"]
related: ["[[transformer-architecture]]", "[[finbert]]", "[[word-embeddings]]", "[[nlp-overview]]", "[[nlp-sentiment-analysis]]", "[[named-entity-recognition]]", "[[text-classification-finance]]", "[[fine-tuning-llms]]", "[[earnings-call-analysis]]"]
---

BERT (Bidirectional Encoder Representations from Transformers) is a language model introduced by Google in 2018 that learns deep, context-aware representations of text by reading a sentence in both directions at once. It was a watershed in [[nlp-overview|NLP]]: instead of training a bespoke model per task, you pre-train BERT once on a huge unlabeled corpus, then **fine-tune** it on a small labeled dataset for a specific task -- sentiment, classification, entity extraction. In finance this made high-quality text models accessible to teams without massive labeled datasets, and its domain-adapted descendant [[finbert|FinBERT]] became a standard tool for sentiment scoring.

## How It Works

BERT is the **encoder** half of the [[transformer-architecture|transformer]]. Its two key ideas:

- **Bidirectional context** -- earlier models (and GPT-style decoders) read left-to-right. BERT attends to the entire sentence simultaneously, so the representation of a word depends on words both before and after it. This matters in finance, where "the company beat estimates but lowered guidance" inverts meaning depending on the full sentence.
- **Pre-training objectives** -- BERT is pre-trained with **masked language modelling** (predict randomly hidden words) and (originally) next-sentence prediction, learning general language structure from raw text with no labels.

After pre-training, you add a small task head and **fine-tune** on labeled examples. Because the heavy lifting happened in pre-training, fine-tuning needs far less data -- often a few thousand labeled headlines or filings.

## BERT vs GPT-style LLMs

BERT is an **encoder** (it produces representations; great for *understanding/classification* tasks) while GPT-style models are **decoders** (they generate text). For a fixed task like "score this headline -1/0/+1" or "extract the tickers," a fine-tuned BERT/FinBERT is often cheaper, faster, more deterministic, and more accurate than prompting a large generative LLM -- and it runs locally without per-token API costs. For open-ended reasoning and generation, the generative LLMs win. Many trading NLP pipelines use both: a small encoder for high-volume classification, a large LLM for synthesis.

## Trading and Finance Relevance

- **[[nlp-sentiment-analysis|Sentiment]]** -- [[finbert|FinBERT]] (BERT fine-tuned on financial text) classifies news, headlines, and social posts as positive/negative/neutral; the resulting sentiment series feeds news-driven and event-driven signals.
- **[[earnings-call-analysis|Earnings-call analysis]]** -- classifying management tone (hawkish/dovish, confident/hedging) and detecting guidance changes in transcripts.
- **[[text-classification-finance|Event and document classification]]** -- routing filings, tagging news by event type (M&A, downgrade, litigation), and triaging urgency.
- **[[named-entity-recognition|Entity extraction]]** -- pulling companies, tickers, people, and amounts out of unstructured filings and news.
- **Embeddings** -- BERT sentence embeddings power semantic search and clustering over filings, research notes, and a wiki like this one.

The practical advantages for trading desks are latency and cost: a fine-tuned encoder can score thousands of headlines per second on modest hardware, which matters for news-reaction strategies where the edge decays in seconds.

## Limitations

- **Short context window** -- vanilla BERT caps at 512 tokens, awkward for long filings (mitigated by chunking or long-context variants like Longformer/BigBird).
- **Needs fine-tuning** -- out of the box it does not "know" finance; domain adaptation ([[finbert|FinBERT]]) is what makes it useful, and the labeled data for fine-tuning must be clean.
- **No generation/reasoning** -- it classifies and represents; it cannot summarise or answer open questions.

## Related

- [[transformer-architecture]] -- the architecture BERT is the encoder of
- [[finbert]] -- the finance-domain fine-tune used in trading sentiment pipelines
- [[word-embeddings]] -- BERT produces contextual embeddings
- [[nlp-overview]] · [[nlp-sentiment-analysis]] · [[text-classification-finance]] · [[named-entity-recognition]]
- [[fine-tuning-llms]] -- how BERT is adapted to financial tasks
- [[earnings-call-analysis]] -- a key application

## Sources

- Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (2018) -- the original paper
- Araci, "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models" (2019) -- the finance domain adaptation
- Vaswani et al., "Attention Is All You Need" (2017) -- the transformer architecture BERT builds on
