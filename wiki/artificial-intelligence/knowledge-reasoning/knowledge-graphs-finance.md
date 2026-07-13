---
title: "Knowledge Graphs in Finance"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Knowledge Graph", "Financial Knowledge Graph"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[knowledge-reasoning-overview]]", "[[ontologies-taxonomies]]", "[[named-entity-recognition]]", "[[retrieval-augmented-generation]]", "[[embeddings-vector-databases]]", "[[artificial-intelligence]]"]
---

# Knowledge Graphs in Finance

A **knowledge graph** is a structured network of entities and their relationships — companies connected to subsidiaries, executives, products, competitors, suppliers, and regulators. In trading, knowledge graphs power supply chain analysis, corporate ownership mapping, event propagation tracking, and regulatory compliance screening.

## Structure

```
[Apple Inc.] --CEO--> [Tim Cook]
[Apple Inc.] --SUPPLIER--> [TSMC]
[Apple Inc.] --COMPETITOR--> [Samsung]
[Apple Inc.] --LISTED_ON--> [NASDAQ]
[TSMC] --SUPPLIER--> [ASML]
[Tim Cook] --BOARD_MEMBER--> [Nike Inc.]
```

Entities are nodes, relationships are edges. Each can have properties (date ranges, confidence levels, source citations).

## Trading Applications

### Supply Chain Analysis
Map supplier/customer relationships to predict revenue contagion:
- TSMC fab disruption → impact on Apple, NVIDIA, AMD, Qualcomm
- Suez Canal blockage → trace affected supply chains to specific companies
- Commodity price spike → which companies have the most exposure?

### Corporate Ownership & Structure
Navigate complex corporate hierarchies:
- Who ultimately owns this entity? (Beneficial ownership)
- What subsidiaries does Berkshire Hathaway control?
- Which banks have exposure to this defaulting counterparty? (Contagion risk)

### Event Propagation
When news breaks, knowledge graphs predict secondary effects:
```
Event: "TSMC announces chip shortage"
→ Graph traversal: TSMC --SUPPLIES--> Apple, NVIDIA, AMD, Intel
→ Signal: Short downstream companies with highest TSMC dependency
```

### Sanctions & Compliance Screening
Check if counterparties connect to sanctioned entities through ownership chains:
```
Company X --SUBSIDIARY_OF--> Holding Y --CONTROLLED_BY--> Sanctioned Person Z
→ Flag: indirect sanctions exposure
```

### Alternative Data Integration
Knowledge graphs link entities across data sources:
- SEC filings mention "major customer" → knowledge graph resolves to specific company
- News mentions "tech giant" → disambiguate using graph context
- Patent filings reveal undisclosed partnerships

## Building Financial Knowledge Graphs

| Source | Entities Extracted | Relationships |
|--------|-------------------|---------------|
| **SEC filings** | Companies, executives, amounts | Ownership, board membership, material contracts |
| **News + [[named-entity-recognition|NER]]** | Companies, people, events | Acquisitions, partnerships, lawsuits |
| **Supply chain databases** | Companies, products | Supplier/customer relationships |
| **Patent databases** | Companies, technologies | Innovation links, licensing |
| **OpenCorporates / Wikidata** | Companies, jurisdictions | Corporate structure, registration |

Modern approaches use [[foundation-models|LLMs]] to extract relationships from unstructured text and populate knowledge graphs automatically — combining NLP and KR&R.

## Knowledge Graphs + LLMs

| Approach | How | Advantage |
|----------|-----|-----------|
| **Graph-enhanced [[retrieval-augmented-generation|RAG]]** | LLM queries the graph alongside vector search | Structured relationships + semantic understanding |
| **LLM-powered graph construction** | LLM extracts entities and relationships from text | Automated, scales to millions of documents |
| **Graph reasoning + LLM explanation** | Graph traversal finds paths; LLM explains in natural language | "Apple's revenue is at risk because of TSMC disruption via their A-series chip dependency" |

## Providers

| Provider | Focus | Users |
|----------|-------|-------|
| **Bloomberg** | Financial entity graph | Institutional traders |
| **Refinitiv/LSEG** | Corporate ownership, supply chain | Compliance, research |
| **FactSet** | Supply chain, ownership | Institutional research |
| **Diffbot** | Web-scraped knowledge graph | Alternative data |
| **Neo4j** | Graph database (build your own) | Custom implementations |

## See Also

- [[knowledge-reasoning-overview]] — KR&R hub
- [[ontologies-taxonomies]] — Formal structure for knowledge graph schemas
- [[named-entity-recognition]] — Extracting entities to populate graphs
- [[retrieval-augmented-generation]] — Combining graph search with LLMs
- [[embeddings-vector-databases]] — Alternative (vector) approach to knowledge retrieval
- [[artificial-intelligence]] — AI section hub

## Sources

- Vendor documentation for financial entity/relationship graphs: Bloomberg, Refinitiv/LSEG, FactSet, Diffbot, and Neo4j (graph-database platform).
- Open data sources for graph construction: OpenCorporates and Wikidata (corporate structure, jurisdictions).
- General literature on GraphRAG (graph-enhanced retrieval-augmented generation) and LLM-driven relationship extraction from filings and news (mid-2026).
