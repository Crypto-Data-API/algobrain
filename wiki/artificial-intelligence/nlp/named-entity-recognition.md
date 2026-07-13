---
title: "Named Entity Recognition (NER)"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["NER", "Named Entity Recognition", "Entity Extraction"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[nlp-overview]]", "[[text-preprocessing-finance]]", "[[nlp-sentiment-analysis]]", "[[natural-language-processing]]", "[[foundation-models]]", "[[artificial-intelligence]]"]
---

# Named Entity Recognition (NER)

**Named Entity Recognition** (NER) identifies and classifies named entities in text — companies, people, monetary amounts, dates, locations, and financial instruments. It is the key technique for extracting structured data from unstructured financial text, enabling automated processing of news, filings, and research.

## Financial Entity Types

| Entity Type | Examples | Trading Value |
|-------------|---------|--------------|
| **Company** | "Apple Inc.", "AAPL", "the Cupertino giant" | Map mentions to tradable tickers |
| **Person** | "Jerome Powell", "Warren Buffett" | Track influential actors |
| **Money** | "$94.8 billion", "€2.3M" | Extract financial figures |
| **Date** | "Q3 2025", "next Thursday", "March 15" | Temporal context for events |
| **Percentage** | "raised 25 basis points", "up 3.2%" | Quantify changes |
| **Product** | "iPhone 17", "Model Y" | Product-level analysis |
| **Financial Instrument** | "10-year Treasury", "BTC-PERP" | Identify assets discussed |
| **Regulatory Body** | "SEC", "CFTC", "FCA" | Regulatory risk detection |

## Tools & Approaches

| Tool | Type | Strengths |
|------|------|-----------|
| **spaCy** | Rule + ML hybrid | Fast, production-ready, custom financial models available |
| **Flair** | Neural sequence labeling | High accuracy, contextual embeddings |
| **[[foundation-models|LLMs]]** (Claude, GPT-4) | [[zero-shot-few-shot-learning|Zero-shot]] extraction | No training needed, handles novel entities, understands context |
| **Stanza** (Stanford NLP) | Neural pipeline | Academic quality, multi-language |
| **Custom BERT-NER** | Fine-tuned [[finbert|BERT]] | Highest accuracy for specific financial entity types |

## Trading Applications

### Event Extraction Pipeline
```
News article → NER extracts [Company: Apple] [Amount: $94.8B] [Event: beat estimates]
→ Structured event: {ticker: AAPL, metric: revenue, actual: 94.8B, event: earnings_beat}
→ Trading signal
```

### Automated Filing Analysis
NER on SEC 8-K filings extracts:
- Board member changes (person entities)
- Material financial events (money entities)
- Regulatory actions (organization entities)
- Contract values (money + company entities)

### News Deduplication
Same event reported by 50 outlets. NER extracts the core entities → deduplicate by matching entity sets → count as one event instead of 50 (prevents double-counting in [[nlp-sentiment-analysis|sentiment models]]).

## Challenges in Financial NER

| Challenge | Example |
|-----------|---------|
| **Ambiguity** | "Apple" — company or fruit? "Amazon" — company or river? |
| **Ticker conflicts** | "$A" — Agilent stock or just the letter A? |
| **Abbreviations** | "JPM" = JPMorgan, "GS" = Goldman Sachs |
| **Nested entities** | "CEO of Goldman Sachs Group Inc." contains person role + company |
| **Cross-reference** | "The Cupertino company" = Apple (requires coreference resolution) |

## See Also

- [[nlp-overview]] — NLP pipeline hub
- [[text-preprocessing-finance]] — Preparing text for NER
- [[nlp-sentiment-analysis]] — Often paired with NER
- [[foundation-models]] — Zero-shot NER with LLMs
- [[natural-language-processing]] — NLP fundamentals
- [[artificial-intelligence]] — AI section hub

## Sources

- spaCy documentation — production NER pipelines and custom entity models.
- Akbik et al., "Contextual String Embeddings for Sequence Labeling" (Flair), 2018.
- Qi et al., "Stanza: A Python NLP Toolkit for Many Human Languages" (Stanford), 2020.
- D. Jurafsky & J. H. Martin, *Speech and Language Processing*, 3rd ed. — NER and coreference resolution.
