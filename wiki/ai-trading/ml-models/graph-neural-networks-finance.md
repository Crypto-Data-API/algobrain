---
title: "Graph Neural Networks in Finance"
type: concept
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, deep-learning]
domain: [machine-learning, ai-trading]
difficulty: advanced
related:
  - "[[deep-learning]]"
  - "[[lstm-trading]]"
  - "[[transformer-trading]]"
  - "[[xlstm-ts]]"
  - "[[correlation]]"
  - "[[pairs-trading]]"
  - "[[stock-prediction]]"
---

Graph Neural Networks (GNNs) are deep-learning architectures that operate directly on graph-structured data, making them a natural fit for financial markets where stocks, entities, and counterparties are connected by sector, supply-chain, ownership, and price-correlation relationships. In finance they have been applied to long-horizon [[stock-prediction|stock prediction]], fraud detection, anti-money laundering, and counterparty risk modelling (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Overview

GNNs model financial systems as graphs. **Nodes** typically represent stocks or other entities (companies, exchanges, counterparties, accounts). **Edges** encode relationships such as sector similarity, rolling price [[correlation]], and supply-chain dependencies. By passing information along the edges of the graph, a GNN can learn representations of each node that take its neighbourhood into account — capturing cross-asset structure that univariate models miss.

This contrasts with traditional sequence models like [[lstm-trading|LSTMs]] or [[transformer-trading|transformers]] that treat each instrument's time series in isolation (or stack them as parallel channels) without explicitly modelling the relational structure between them.

## How it works

In a financial GNN, the graph construction is itself a modelling choice. Typical edges include:

- **Sector similarity** — connecting companies that share an industry classification
- **Rolling price correlation** — edges weighted by recent return co-movement
- **Supply-chain dependencies** — directed edges from suppliers to customers
- **Ownership / corporate relationships** — parent-subsidiary, joint-venture, board interlock

Once the graph is built, message-passing layers propagate information from each node to its neighbours, building up representations that can be used for prediction, classification, or anomaly detection.

A particularly effective variant for financial relationship graphs is the **Node-level Graph Attention Network (NGAT)**, which uses attention to learn which neighbour relationships matter most for each prediction (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Performance / Results

**Long-horizon stock prediction:**

- NGAT models tailored for corporate relationship graphs achieved **over 70% accuracy on long-term (multi-year) stock prediction**
- This substantially outperforms traditional next-day prediction benchmarks, which typically sit in the **50-60%** range
- The implication is that relational structure carries strong signal at longer horizons even when it adds little at the daily scale (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]])

**Knowledge graph applications:**

- **Fraud detection** — knowledge graphs identify suspicious patterns such as circular transactions and unusual connections between accounts, phone numbers, addresses, and devices
- **Anti-money laundering** — tracking fund flows across borders, linking shell companies to ultimate beneficiaries
- **Risk management** — modelling dependencies between financial instruments and counterparties to surface concentrated or correlated exposures (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]])

## Trading Applications

- **Long-horizon equity selection** — NGAT-style models for multi-year stock prediction in portfolio construction
- **Sector rotation** — leveraging learned sector and supply-chain edges to anticipate cross-sector flows
- **[[pairs-trading|Pairs trading]] and statistical arbitrage** — using correlation-graph embeddings to identify candidate pairs and time entries
- **Cross-asset signal generation** — capturing relationships that univariate time-series models such as [[lstm-trading]], [[xlstm-ts]], and [[transformer-trading]] miss
- **Counterparty and concentration risk** — graph-based exposure mapping for trading-book risk management
- **Surveillance and compliance** — fraud, AML, and market-abuse detection as adjacent applications

## Limitations

- **Graph construction is a modelling choice** — different edge definitions (correlation window, sector taxonomy, supply-chain source) produce different graphs and different predictions
- **Stationarity** — corporate relationships and correlations drift; static graphs decay, dynamic graphs add complexity
- **Data requirements** — building rich corporate-relationship graphs requires high-quality reference data
- **Interpretability** — attention weights help but full causal attribution remains difficult
- **Reported accuracy figures (>70% multi-year)** come from specific datasets and require independent replication before being treated as a generalisable benchmark

## Related

- [[deep-learning]] — broader context for GNN architectures
- [[lstm-trading]] — sequence-based alternative that does not model relational structure
- [[transformer-trading]] — attention-based architecture; transformers and GNNs share conceptual roots
- [[xlstm-ts]] — recent state-of-the-art short-horizon forecaster, complementary to GNNs at longer horizons
- [[correlation]] — correlation edges are a common GNN input
- [[pairs-trading]] — natural application area
- [[stock-prediction]] — primary application
- [[anti-money-laundering]] — adjacent use case
- [[risk-management]] — counterparty graph applications

## Sources

- [[2026-04-22-gap-finder-ai-2026-major-news-stories]] — documents GNN applications in finance, NGAT performance on long-term stock prediction (>70% accuracy vs 50-60% next-day baselines), and knowledge-graph use cases for fraud detection, AML, and risk management
