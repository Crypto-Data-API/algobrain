---
title: "Confluent, Inc."
type: entity
created: 2026-04-13
updated: 2026-06-19
status: excellent
tags: [company, stocks, ai-trading, machine-learning, technology]
entity_type: company
founded: 2014
headquarters: "Mountain View, California, USA"
website: "https://www.confluent.io"
aliases: ["CFLT", "Confluent, Inc."]
ticker: "CFLT (delisted 2026-03-17)"
exchange: "NASDAQ (former)"
sector: "AI Data Streaming"
industry: "AI Data Streaming"
sp500: false
ai_category: "AI Data Streaming"
market_cap_tier: "Mid Cap"
related: ["[[ibm]]", "[[ai-trading-overview]]", "[[artificial-intelligence]]", "[[atlassian]]", "[[data-sources-overview]]", "[[oracle]]", "[[salesforce]]", "[[snowflake]]", "[[trade-desk-(the)]]"]
---

Confluent, Inc. (formerly NASDAQ: CFLT) is the data-streaming platform company built around Apache Kafka, founded in 2014 by Kafka's creators (Jay Kreps, Neha Narkhede, Jun Rao) out of LinkedIn. **As of June 2026 it is no longer an independently traded stock: [[ibm|IBM]] agreed on 7 December 2025 to acquire Confluent for $31.00 per share in cash, and CFLT was delisted from NASDAQ on 17 March 2026.** For traders the name now matters as a completed-arb case study and as part of IBM's AI/data stack.

> **M&A case study, not a live ticker.** Everything below describes a company that ceased to trade on 17 March 2026. The trading sections are written in the past tense around the closed [[ibm|IBM]] acquisition; CFLT cannot be bought or sold. Exposure to the data-streaming theme now runs through the acquirer and listed adjacencies.

## Business Overview

Confluent commercialises real-time "data in motion": **Confluent Platform** (self-managed Kafka for enterprises) and **Confluent Cloud** (fully managed, consumption-priced streaming), plus Apache Flink-based stream processing and Tableflow for feeding streaming data into analytics/AI systems. The thematic bull case was that AI agents and real-time applications require event streaming as foundational infrastructure. Competition came from hyperscaler-managed Kafka (AWS MSK, Azure Event Hubs), open-source self-hosting, and newer engines such as Redpanda.

### Business Segments / Products (historical)

| Product | What it was | Monetization | Notes |
|---|---|---|---|
| **Confluent Platform** | Self-managed, enterprise Kafka distribution | Term license / subscription | The original on-prem franchise; sticky but slower-growing |
| **Confluent Cloud** | Fully managed, multi-cloud Kafka | Consumption (usage) pricing | The growth engine; consumption model = high upside but volatile |
| **Stream processing (Apache Flink)** | Managed real-time processing on top of streams | Usage | Moves Confluent up-stack from transport to compute |
| **Tableflow / connectors** | Turns streams into analytics/AI-ready tables; ecosystem connectors | Usage / subscription | The "data-streaming → analytics/AI" bridge |
| **Stream Governance** | Schema registry, lineage, security | Subscription add-on | Enterprise-grade governance moat |

The strategic arc: from "the company behind open-source Kafka" toward a complete, governed, real-time data platform spanning transport, processing, and activation — the layer that AI/real-time apps were argued to depend on.

## Financial Profile (final years as a public company)

- **FY2025:** subscription revenue $1,120M, up 21% YoY; Confluent Cloud revenue $624M, up 27% YoY. Quarterly subscription revenue ramped from $261M (Q1, +26%) to $302M (Q4, +20%).
- GAAP-unprofitable throughout its public life (heavy stock-based compensation), with improving non-GAAP operating margins.
- IPO'd June 2021 at $36; peaked above $90 in 2021; spent 2024–2025 mostly in the $18–35 range as cloud consumption growth decelerated.

## Competitive Positioning / Peers (historical)

Confluent sat in the modern data-infrastructure stack — overlapping with cloud data warehouses/lakehouses on the analytics side and with hyperscaler-native streaming on the transport side. The competitive axis was **best-of-breed multi-cloud streaming versus "good-enough" bundled cloud-native services**.

| Company | Ticker | Overlap with Confluent | Relative position |
|---|---|---|---|
| **Confluent** | CFLT (delisted) | — | Category creator for managed Kafka / data-in-motion |
| [[mongodb]] | MDB | Modern data infrastructure; developer-first; consumption + subscription | Adjacent (operational database vs streaming); shared consumption-model dynamics |
| [[snowflake]] | SNOW | Data platform; consumption pricing; feeds analytics/AI | Downstream complement and competitor as both expand scope |
| [[databricks]] | (private) | Lakehouse + streaming + AI | Major adjacent platform; private, so no direct stock read |
| **Redpanda** | (private) | Kafka-compatible streaming engine | Newer, performance-positioned challenger to core Kafka |
| **AWS MSK / Azure Event Hubs** | (cloud) | Hyperscaler-managed Kafka/streaming | Bundling threat — the central margin/competition risk |

The persistent bear point was that hyperscalers could commoditize managed streaming inside a broader cloud bill; the bull point was that governed, multi-cloud, best-of-breed streaming with Flink and governance justified a standalone platform.

## The IBM Acquisition — M&A Case Study

### Timeline

- **2025:** growth moderated to ~20% as enterprises optimised cloud spend; the stock sold off sharply mid-2025 on weak consumption guidance, which positioned it as a strategic-acquisition candidate and fed takeover speculation.
- **7 December 2025:** definitive merger agreement with [[ibm|IBM]] at **$31.00/share cash** — IBM's play to add real-time data infrastructure to its watsonx/AI stack.
- **17 March 2026:** acquisition closed; CFLT delisted from NASDAQ.

### Deal structure and strategic fit

- **All-cash, $31.00/share.** A clean, single-price cash deal — no stock component, so the merger-arb spread did not depend on an acquirer's share price (contrast with the [[cyberark-software|CyberArk]]/[[palo-alto-networks|Palo Alto]] cash-and-stock structure).
- **Strategic rationale:** [[ibm|IBM]] bought real-time data infrastructure to feed its **watsonx** AI platform and broader hybrid-cloud data stack — owning the "data in motion" layer beneath enterprise AI workloads.
- **Acquirer fit:** Confluent's enterprise/regulated customer base and governance tooling align with IBM's enterprise channel and Red Hat/OpenShift hybrid-cloud footprint.

### Merger-arbitrage view (past tense)

Because the deal was **all-cash at a fixed $31.00**, the arb was a textbook low-drama completion: the spread between the post-announcement price and $31.00 captured (a) deal-break/antitrust risk and (b) the time value to the March 2026 close. With a strategic (non-vertical-monopoly) acquirer, antitrust risk was modest, so the spread was thin and the position resolved cleanly at close. See [[merger-arbitrage]] for the general framework.

### Lesson for the playbook

Beaten-down infrastructure-software names with strategic open-source franchises became 2025–2026 takeover targets. The pattern: a category-defining platform de-rates on consumption-growth deceleration, then a strategic buyer pays a control premium for the franchise and its enterprise base. CFLT's spread (announcement to March 2026 close) was a clean, low-drama deal completion.

## Trading Relevance (historical / routing)

- **No longer tradable** — exposure to the data-streaming theme now routes through [[ibm]] (acquirer), or adjacent listed infrastructure names ([[snowflake]], [[mongodb]], [[datadog]]).
- **Index / ETF note:** when listed, CFLT appeared in software/cloud and growth baskets (e.g. IGV, WCLD); those holdings were removed on the March 2026 delisting.
- **Lesson for the playbook:** beaten-down infrastructure-software names with strategic open-source franchises became 2025–2026 takeover targets; CFLT's merger-arb spread (announcement to March 2026 close) was a clean, low-drama deal completion.

## Bull vs Bear Case (as it stood pre-deal)

**Bull case (pre-deal)**
- Category creator for managed Kafka; "data in motion" framed as mandatory plumbing for real-time AI.
- Confluent Cloud growing faster than the overall mix; Flink + governance moving up-stack into higher-value compute.
- Strong enterprise/regulated customer base with governance differentiation — ultimately the qualities that made it an attractive acquisition.

**Bear case (pre-deal)**
- Consumption-growth deceleration as enterprises optimized cloud spend.
- Hyperscaler-bundled Kafka (AWS MSK, Azure Event Hubs) and open-source self-hosting as commoditization threats.
- Persistent GAAP losses and heavy stock-based compensation dilution.

## Capital Return / Dilution (historical)

Confluent paid no dividend and ran no meaningful buyback as a public company; it was a growth-stage name funding expansion and absorbing **heavy stock-based compensation**, which diluted shareholders throughout its public life. The all-cash IBM acquisition crystallized value at $31.00/share and ended the public-company dilution question.

## Risks (now resolved by the close)

The principal pre-deal risks — consumption-growth deceleration, hyperscaler competition, GAAP losses, and SBC dilution — were the very factors that de-rated the stock into takeover range. The only post-announcement risk was deal completion (antitrust / shareholder vote / financing), which resolved cleanly at the 17 March 2026 close.

## Related

- [[ibm]]
- [[artificial-intelligence]]
- [[ai-trading-overview]]
- [[atlassian]]
- [[data-sources-overview]]
- [[oracle]]
- [[salesforce]]
- [[snowflake]]
- [[trade-desk-(the)]]
- [[sap]]
- [[twilio]]
- [[mongodb]]
- [[databricks]]
- [[datadog]]
- [[merger-arbitrage]]
- [[technology]]
- [[nasdaq]]

## Sources

- (Source: [[stockmarketapi-ai-stocks-2026-04-13]])
- [Confluent Q4/FY2025 results 8-K exhibit (SEC)](https://www.sec.gov/Archives/edgar/data/0001699838/000169983826000004/cflt-20251231xexx991.htm)
- [Confluent DEFA14A re IBM merger (SEC, Dec 2025)](https://www.sec.gov/Archives/edgar/data/0001699838/000110465925119435/tm2532777d5_defa14a.htm)
- [TS2 — Confluent stock surges on takeover rumors](https://ts2.tech/en/confluent-cflt-stock-surges-on-takeover-rumors-whats-next-for-the-data-streaming-pioneer/)
- Verified via Perplexity (sonar) and web search, 2026-06-10
