---
title: "Ontologies & Taxonomies in Finance"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Ontology", "Taxonomy", "Financial Ontology", "FIBO"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[knowledge-reasoning-overview]]", "[[knowledge-graphs-finance]]", "[[expert-systems]]", "[[artificial-intelligence]]"]
---

# Ontologies & Taxonomies in Finance

An **ontology** is a formal description of a domain's concepts, properties, and relationships. A **taxonomy** is a hierarchical classification system. In finance, these structures define what a "bond" is, how "equity derivatives" relate to "options," and how regulatory categories map to instrument types. They provide the schema for [[knowledge-graphs-finance|knowledge graphs]] and the foundation for structured financial data.

## Taxonomy vs Ontology

| | Taxonomy | Ontology |
|---|---------|---------|
| **Structure** | Hierarchical tree (parent-child) | Network of relationships (graph) |
| **Example** | "Equity > Common Stock > Preferred Stock" | "Common Stock *is issued by* Corporation, *trades on* Exchange, *pays* Dividend" |
| **Expressiveness** | Classification only | Classification + relationships + rules + constraints |
| **Use** | Categorize instruments | Reason about instrument properties |

## Key Financial Ontologies

| Ontology | Publisher | Covers | Trading Use |
|----------|----------|--------|-------------|
| **FIBO** (Financial Industry Business Ontology) | EDM Council / OMG | Full financial domain — instruments, entities, processes | Industry standard for financial data interoperability |
| **FIX Protocol Ontology** | FIX Trading Community | Trading messages, order types | Standard trade communication |
| **ISDA CDM** | ISDA | Derivatives contracts | Derivatives processing, smart contracts |
| **GLEIF** | Global LEI Foundation | Legal entity identifiers | Entity identification across systems |
| **XBRL Taxonomies** | XBRL International | Financial reporting | SEC filing data extraction |

## Trading Applications

### Instrument Classification
Consistent classification across systems:
```
Instrument: "AAPL 150C 2025-06-20"
Taxonomy: Derivative > Option > Equity Option > Call > American Style
Properties: underlying=AAPL, strike=150, expiry=2025-06-20
```

### Regulatory Mapping
Different regulators classify the same instrument differently:
- SEC: "Security"
- CFTC: May be a "Swap" depending on structure
- MiFID II: "Transferable Security" with specific reporting requirements

An ontology maps between these classifications automatically.

### Data Integration
Trading firms pull data from dozens of sources (Bloomberg, Refinitiv, exchanges, internal). Ontologies provide a common schema:
- Bloomberg's "GOVT" = Refinitiv's "Government Bond" = internal "Sovereign Debt"
- Without ontology: manual mapping per source pair (N² problem)
- With ontology: each source maps to the ontology once (N problem)

### Smart Contract Templates
ISDA's Common Domain Model (CDM) encodes derivatives contracts as formal ontological structures — enabling automated contract creation, lifecycle management, and settlement. This directly connects to [[defi]] where smart contracts implement financial logic.

## See Also

- [[knowledge-reasoning-overview]] — KR&R hub
- [[knowledge-graphs-finance]] — Graphs structured by ontologies
- [[expert-systems]] — Rules operating on ontological categories
- [[artificial-intelligence]] — AI section hub
