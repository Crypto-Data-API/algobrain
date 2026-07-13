---
title: "OPRA (Options Price Reporting Authority)"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, stocks, regulation]
entity_type: company
founded: 1976
website: https://www.opraplan.com
aliases: ["OPRA", "Options Price Reporting Authority", "OPRA LLC"]
related:
  - "[[polygon-io]]"
  - "[[databento]]"
  - "[[optionmetrics]]"
  - "[[orats]]"
  - "[[unusual-whales]]"
---

# OPRA (Options Price Reporting Authority)

OPRA is the consolidated tape for every US-listed equity and index option — the single canonical source from which virtually all options market data downstream is derived. For traders, OPRA matters because the quality, latency, and cost of every options data product they touch (broker quotes, flow scanners, historical archives) is determined by how that vendor consumes and processes this feed.

## Overview

OPRA is the official consolidated real-time data feed for ALL US-listed equity and index options. Formed in 1976, it is a national market system plan operated as the Securities Information Processor (SIP) for the 18 US options exchanges (as of 2025: the four Cboe exchanges, six Nasdaq exchanges including ISE and PHLX, NYSE Arca and NYSE American, the four MIAX exchanges including MIAX Sapphire which launched August 2024, BOX, and MEMX), mandated under SEC Regulation NMS to provide a single canonical tape of options market activity. The Securities Industry Automation Corporation (SIAC), a wholly-owned NYSE subsidiary, administers the SIP infrastructure, which runs on NYSE's Pillar platform. Every options quote, trade, and NBBO calculation across the US options market originates from OPRA — virtually all third-party options data vendors (including [[polygon-io]], [[databento]], and [[optionmetrics]]) are downstream consumers of this feed.

## 2024–2026: The 96-Line Era

- **5 February 2024**: OPRA completed its long-planned migration from a 48-line to a 96-line multicast network, roughly doubling distribution capacity to approximately 1 trillion messages per day. The expansion forced every direct subscriber to upgrade network infrastructure (40 Gbps+ provisioning is now typical for the full feed).
- **Latency improvements**: since the Pillar/96-line upgrade, median SIP latency is roughly 20 microseconds, with 99th-percentile latency reduced to ~57.5 microseconds — a ~75% reduction in latency outliers versus the prior architecture.
- **April 2025 selloff**: during the tariff-driven volatility spike, peak 1-millisecond bursts on OPRA exceeded 23.7 million packets per second — over 187 million messages per second at burst rate. Vendors now advise feed handlers be engineered for microburst rates on the order of 75 million messages per second to avoid processing latency.
- These message rates keep raising the infrastructure bar for direct consumption, widening the moat of specialist redistributors like [[databento]] and [[polygon-io]].

## Pricing

- **Professional Subscriber**: ~$30+/mo per device direct fees plus vendor markup (varies by entitlement: top-of-book vs full-depth, real-time vs delayed)
- **Non-Professional Subscriber**: ~$1.50–2.00/mo per user with retail-broker entitlements; many brokers absorb this cost
- **Vendor / Redistributor**: tiered fees based on number of internal/external users and message rates; full enterprise OPRA redistribution typically runs $10K–$100K+/mo depending on use case
- **Direct feed access**: requires high-bandwidth connectivity (40 Gbps+ since the February 2024 96-line expansion) and specialized hardware to handle peak message rates; effectively co-location only
- Delayed (15-minute) options data is generally available without OPRA fees through retail platforms

## What You Get

- **Last sale data**: every options trade across all 18 US options exchanges with price, size, exchange, and trade condition codes
- **NBBO (National Best Bid and Offer)**: continuously calculated best bid/ask across all venues
- **Local exchange quotes**: each exchange's individual best bid/offer (BBO)
- **Trade condition codes**: indicators for complex orders, late trades, intermarket sweeps, and other regulatory flags
- **Open interest data**: end-of-day OI by contract from OCC (the Options Clearing Corporation), often distributed alongside OPRA
- **Underlying coverage**: every listed US equity option, ETF option, and index option (SPX, NDX, RUT, VIX, etc.)

## Use Cases / Who Uses It

- **Data vendors**: [[polygon-io]], [[databento]], [[algoseek]], [[orats]], [[optionmetrics]], [[unusual-whales]] all source raw OPRA and resell processed/normalized versions
- **Brokerages**: [[interactive-brokers]], [[charles-schwab]], [[robinhood]], and others consume OPRA to display real-time quotes and route orders
- **Market makers and HFT firms**: direct OPRA feed consumers for sub-millisecond quoting and hedging
- **Hedge funds and prop desks**: subscribe via vendors or direct for real-time options analytics
- **Academic researchers**: access historical OPRA data through [[optionmetrics]] (IvyDB) or vendor archives
- **Compliance and surveillance**: consolidated tape is the regulatory reference for best execution analysis

## Strengths and Limitations

**Strengths:**
- **Canonical source of truth**: every other US options data product is derived from OPRA — there is no alternative national consolidated tape
- **Regulatory mandate**: complete coverage of every listed contract on every exchange, no gaps
- **Trade condition transparency**: full set of regulatory flags enables sophisticated microstructure analysis
- **NBBO calculation**: removes the need to merge per-exchange feeds yourself

**Limitations:**
- **Bandwidth and message volume**: microburst message rates now reach tens of millions of messages/second (187M+ msgs/sec at 1-ms burst scale in April 2025); the full 96-line feed requires 40 Gbps+ connectivity and institutional infrastructure
- **Cost barrier for direct access**: only large vendors and trading firms can justify direct connectivity; everyone else pays a vendor
- **No depth-of-book**: OPRA is top-of-book only — for full order book depth, you need exchange-specific feeds (e.g., CBOE PITCH, ISE Depth)
- **No analytics**: raw quotes and trades only; Greeks, IV, and analytics must be calculated downstream
- **Few internet redistributors**: most retail platforms cannot stream true real-time OPRA due to bandwidth — what they show is often heavily filtered or delayed

## Related

- [[polygon-io]] — major OPRA redistributor with REST and WebSocket APIs
- [[databento]] — institutional OPRA data with historical archive
- [[optionmetrics]] — historical OPRA-derived database (IvyDB) for research
- [[orats]] — OPRA-fed analytics and scanners
- [[unusual-whales]] — retail-facing options flow built on OPRA
- [[options-greeks]] — calculated downstream from OPRA quotes
- [[implied-volatility]] — derived from OPRA option prices
- [[volatility-surface]] — built from full OPRA chain snapshots
- [[interactive-brokers]] — broker that surfaces OPRA quotes

## Sources

- OPRA plan official site and fee schedules: https://www.opraplan.com
- OPRA SIP Operating Metrics, February 2025: https://cdn.opraplan.com/documents/OPRA_SIP_Metrics_February_2025.pdf (latency and capacity statistics)
- Databento Microstructure Guide, "What is the Options Price Reporting Authority (OPRA)?": https://databento.com/microstructure/opra (SIAC as SIP administrator, 18 participant exchanges, 96-line migration 5 Feb 2024, latency figures)
- Databento blog, "Beyond 40 Gbps: Processing OPRA in real-time": https://databento.com/blog/beyond-40-gbps-processing-opra-in-real-time (April 2025 peak burst rates)
- Pico, "OPRA 96-line Expansion: The Big Boost in Latency and Infrastructure Requirements": https://www.pico.net/blog/opra-96-line-expansion-the-big-boost-in-latency-and-infrastructure-requirements/
- Verified via Perplexity and web search, 2026-06-10
