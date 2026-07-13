---
title: "Federated Learning for Anti-Money Laundering"
type: concept
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, risk-management, regulation]
domain: [machine-learning, ai-trading]
difficulty: advanced
related:
  - "[[graph-neural-networks-finance]]"
  - "[[deep-learning]]"
  - "[[risk-management]]"
  - "[[regulation]]"
  - "[[anti-money-laundering]]"
---

Federated learning is a machine-learning paradigm in which multiple financial institutions collaboratively train a shared model without ever exchanging their underlying private data. Applied to anti-money laundering (AML), it allows banks and payment networks to pool detective power across institutional boundaries while preserving customer privacy and competitive secrecy (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## Overview

Traditional AML and fraud-detection models suffer from a fundamental data-access problem: money laundering and fraud rings span many institutions, but each bank only sees its own slice of the activity. Sharing raw customer or transaction data across institutions is restricted by privacy law, contractual obligations, and competitive concerns.

**Federated learning** sidesteps this by training models in a distributed fashion. Each institution trains locally on its own data; only model updates (not raw data) are exchanged and aggregated into a shared model. This enables collaboration without data leakage.

A concrete instance documented in recent research is **Private Vertical FL for Anti-Money Laundering (PV4AML)**, which combines federated learning with cryptographic techniques so that banks and payment networks can build ensemble fraud-detection models without exposing the individual institution data on which those models are trained (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]]).

## How it works

At a high level, federated learning for AML works like this:

1. A shared model architecture is agreed upon by participating institutions
2. Each institution trains the model locally on its own labelled data (e.g. known fraud and AML cases)
3. Only model updates — typically gradients or parameter deltas — are transmitted, never raw records
4. A coordinator aggregates the updates into an improved global model
5. The improved model is redistributed and the cycle repeats

**Vertical federated learning** (the V in PV4AML) is the variant suited to AML: different institutions hold *different features* about overlapping entities (e.g. one bank holds account history, a payment network holds transaction graph data). The "private" in PV4AML refers to the cryptographic techniques layered on top to ensure individual institution data is never exposed during the training or inference process.

## Performance / Results

The source material documents PV4AML at the architectural and capability level rather than via specific accuracy numbers:

- PV4AML **combines cryptographic techniques** with federated learning to enable banks and payment networks to build **ensemble fraud detection models**
- Privacy-preserving by construction: **individual institution data is never exposed**
- Enables collaborative training of fraud and AML models across institutions that could not otherwise share data (Source: [[2026-04-22-gap-finder-ai-2026-major-news-stories]])

Concrete benchmarks for fraud detection lift, false-positive rates, and detection latency are not provided in the source.

## Trading Applications

While federated learning for AML is not itself a trading strategy, it has meaningful second-order effects relevant to traders and risk managers:

- **Counterparty risk pricing** — better cross-institution fraud and AML detection improves the assessment of counterparty integrity, feeding into pricing and limits
- **Market integrity** — stronger detection of market abuse, money laundering, and fraud reduces hidden tail risks that can erupt as enforcement actions or de-listings
- **Regulatory tailwinds** — privacy-preserving collaborative compliance is increasingly favoured by regulators, see [[regulation]]; firms that lead here may face lower compliance costs
- **Downstream signals for [[risk-management|risk management]]** — federated AML models can flag networks and counterparties that warrant additional scrutiny in trading and prime-brokerage relationships
- **Adjacent to [[graph-neural-networks-finance|graph neural networks]]** — many AML use cases combine GNNs (to model the transaction graph) with federated learning (to train across institutions)

## Limitations

- **Coordination is hard** — federated learning requires institutions to agree on model architectures, update protocols, and governance
- **Cryptographic overhead** — privacy-preserving techniques add computational cost and latency relative to centralised training
- **Label scarcity persists** — federated training improves data access but does not solve the underlying scarcity of confirmed-fraud labels
- **Adversarial risk** — malicious participants can in principle poison the global model via crafted updates; mitigations exist but add complexity
- **Regulatory clarity** — privacy-preserving collaboration sits in evolving regulatory territory and may face jurisdictional friction

## Related

- [[graph-neural-networks-finance]] — frequently combined with federated learning for transaction-graph AML
- [[deep-learning]] — underlying model family
- [[risk-management]] — counterparty and operational risk applications
- [[regulation]] — privacy and AML regulatory context
- [[anti-money-laundering]] — primary application domain

## Sources

- [[2026-04-22-gap-finder-ai-2026-major-news-stories]] — documents federated learning for fraud detection and AML, including the PV4AML (Private Vertical FL for Anti-Money Laundering) framework combining cryptographic techniques with federated training across banks and payment networks
