---
title: "Level 4 Order Book Data (Hyperliquid)"
type: source
created: 2026-06-20
updated: 2026-06-20
status: draft
tags: [data-provider, crypto, hyperliquid, market-microstructure, backtesting, on-chain]
aliases: ["Level 4 Order Book Data", "L4 Order Book Data", "L4 data", "Hyperliquid Level 4 dataset"]
source_type: data
source_url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6465720"
source_author: "SSRN working paper (authors per the SSRN listing) + research summary"
source_date: 2026-04-22
source_file: "raw/articles/2026-04-22-gap-finder-hyperliquid-order-books.md"
confidence: medium
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hyperliquid-order-book-microstructure]]", "[[hyperliquid-api-and-sdk]]", "[[market-microstructure]]", "[[clob]]", "[[hypurrscan]]", "[[exchange-api-reference]]"]
---

**Level 4 (L4) order book data** is the most granular tier of order book data: a complete, message-by-message record of every order **addition, execution, cancellation, and update**, sufficient to reconstruct the entire state of the book over time. The grounding research highlights a research-grade L4 dataset for [[hyperliquid|Hyperliquid]] described in an SSRN working paper, **"Level 4 Order Book Data from the Hyperliquid Exchange,"** captured by running a **non-validating node** on Hyperliquid to record these extremely granular order-book events (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]; SSRN). Because Hyperliquid runs a fully on-chain [[clob|CLOB]] in [[hypercore|HyperCore]], the venue is unusually well suited to producing this kind of complete, auditable event stream.

> This page summarizes only what the grounding research states about the dataset. It does not reproduce specific figures, sample sizes, or empirical results that are not in the research — see the SSRN paper itself for those.

## Data levels: L1 → L2 → L3 → L4

Order book data is conventionally described in levels of increasing granularity. The grounding research distinguishes top-of-book quotes (L1), aggregated depth (L2), individual orders (L3), and the cancellation/update-inclusive view (L4) (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

| Level | What it contains | What you can do with it | What it omits |
|---|---|---|---|
| **L1** | Best bid / best ask (top of book) + last trade | Spread, mid, simple signals | All depth beyond BBO |
| **L2** | Aggregated size at each price level | Depth profile, slippage estimates, impact-price calc | Which orders make up a level; cancels |
| **L3** | Individual resting orders (not just aggregated levels) | Per-order queue position, order-size distribution | Full lifecycle of cancels/amendments over time |
| **L4** | Full event stream: additions, executions, **cancellations**, updates | Reconstruct the entire book state at any instant; study order lifecycles | (Nothing material for book reconstruction) |

The jump that matters for microstructure research is from L2/L3 to **L4**: only when you have cancellations and updates can you replay the book exactly and study *order flow* rather than just *snapshots* of resting liquidity.

## Why L4 — the microstructure questions it answers

The grounding research notes that an L4 dataset is invaluable for market-microstructure research because it enables studies that aggregated data cannot support (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]):

| Question | Why L4 is required |
|---|---|
| **Price impact** | Need the full sequence of additions/executions to measure how consuming the book moves price, and how it refills |
| **Order-flow toxicity** | Requires identifying which flow is informed vs. uninformed — only visible with per-event detail |
| **Market resiliency** | How fast depth refills after a sweep is a function of cancel/add dynamics, not snapshots |
| **Market-maker behavior** | Quoting, cancelling, and inventory management are lifecycle behaviors captured only at L4 |

These map directly onto the open questions on [[hyperliquid-order-book-microstructure]] — typical depth, spread dynamics, resting time of limit orders, partial vs. full matching — which L4 data is precisely the instrument for answering empirically.

## How it is captured: non-validating node

The dataset described in the SSRN paper was built by **operating a non-validating node** on Hyperliquid to capture order-book events (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]; SSRN). A non-validating node observes and records chain state and the event stream without participating in consensus, which makes it a clean capture path for a fully on-chain CLOB: the node sees the same order/cancel/execute messages that HyperBFT processes, and records them at full fidelity.

## On-chain reconstruction vs off-chain capture

The grounding research explicitly raises the trade-off between **reconstructing the book directly from on-chain data** versus using an **off-chain data-capture setup** (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). The two paths differ in fidelity, completeness, and operational cost:

| Dimension | On-chain reconstruction (e.g., non-validating node) | Off-chain capture (e.g., WebSocket logging) |
|---|---|---|
| **Completeness** | Full event stream as committed to chain — additions, executions, cancels, updates | Limited to what the public feed exposes; aggregated/diff feeds may not be true L4 |
| **Auditability** | High — events are the on-chain ground truth | Depends on the feed; capture gaps possible on disconnect |
| **Operational cost** | Higher — run and maintain a node | Lower — subscribe via the [[hyperliquid-api-and-sdk|native API/SDK]] |
| **Gap risk** | Low if the node stays synced | Sequence gaps if a diff is missed (see [[exchange-api-reference#data-quality-caveats|caveats]]) |
| **Latency for live use** | Node-bound | Lower for live signals, but not L4-complete |

For *live* trading, the [[hyperliquid-api-and-sdk|public WebSocket/REST feeds]] (snapshot + diffs) are the practical path. For *research* requiring exact book reconstruction and order-lifecycle analysis, the on-chain non-validating-node capture behind the L4 dataset is the higher-fidelity route. This mirrors the broader point on [[exchange-api-reference]] that reference feeds tell you what data is *available*, not whether your reconstructed book is *correct* at the instant you act.

## How this fits the wiki's Hyperliquid tooling

| Tool / dataset | Granularity | Primary use |
|---|---|---|
| [[hyperliquid-api-and-sdk]] | L1/L2 (snapshot + diffs), trades | Live trading, real-time book maintenance |
| [[hypurrscan]] | Curated dashboards over indexed chain state | Monitoring, vault/liquidation analytics |
| **Level 4 dataset (this page)** | Full L4 event stream | Microstructure research, backtesting, MM-behavior studies |

L4 data signals that Hyperliquid is not only a trading venue but also a fertile ground for cutting-edge microstructure research — a bridge between trading practice and academic insight.

## Related

- [[hyperliquid]] — the venue the dataset captures
- [[hypercore]] — the on-chain engine producing the event stream
- [[hyperliquid-order-book-microstructure]] — the questions L4 answers
- [[hyperliquid-api-and-sdk]] — the lower-fidelity live-data path
- [[market-microstructure]] · [[clob]] — conceptual grounding
- [[hypurrscan]] — curated on-chain analytics alternative
- [[exchange-api-reference]] — cross-venue data caveats

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])
- SSRN — "Level 4 Order Book Data from the Hyperliquid Exchange": https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6465720
- Hyperliquid Docs — Order Book: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/order-book
