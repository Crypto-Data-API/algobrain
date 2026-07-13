---
title: "Splunk"
type: entity
created: 2026-04-13
updated: 2026-06-20
status: excellent
tags: [company, stocks, technology, machine-learning]
aliases: ["Splunk", "SPLK", "Splunk Inc"]
entity_type: company
founded: 2003
headquarters: "San Francisco, California, USA"
website: "https://www.splunk.com"
ticker: "SPLK (delisted Mar 2024)"
exchange: "NASDAQ (former)"
sector: "Technology"
industry: "Data analytics / observability / SIEM"
related: ["[[cisco]]", "[[merger-arbitrage]]", "[[options]]", "[[lululemon]]"]
---

# Splunk

> **Completed-acquisition case study.** Splunk no longer trades as an independent company. NASDAQ: SPLK was delisted in March 2024 after [[cisco|Cisco Systems]] closed its all-cash acquisition. This page is written in past tense and retained as a historical case study in large-cap software M&A and [[merger-arbitrage]]. Nothing here implies the stock still trades.

**Splunk Inc** (formerly NASDAQ: SPLK) was a data analytics and observability platform company specializing in machine data analysis, security information and event management (SIEM), and IT operations intelligence. Splunk was acquired by **Cisco Systems** in March 2024 for approximately $28 billion ($157 per share), making it one of the largest tech acquisitions of the decade.

## Key Facts

| Metric | Detail |
|--------|--------|
| **Ticker** | SPLK (NASDAQ) — delisted March 2024 post-acquisition |
| **Acquirer** | Cisco Systems (CSCO) |
| **Acquisition price** | $157/share ($28B) |
| **Acquisition closed** | March 18, 2024 |
| **Founded** | 2003, San Francisco |
| **Founder** | Michael Baum, Rob Das, Erik Swan |
| **Product** | Data platform for search, monitoring, and analysis of machine-generated big data |

## What the Business Was

Splunk's core product indexed and searched machine-generated data — server logs, application traces, network traffic, security events — making it the standard platform for IT operations and cybersecurity teams. The company pioneered the concept of "data-to-everything" and was a key player in the shift from traditional log analysis to real-time observability. Its commercial model evolved from perpetual on-prem licenses to a usage- and subscription-based model spanning Splunk Cloud (its hosted SaaS offering) and Splunk Enterprise, a transition that pressured reported revenue during the shift but built a durable, high-margin recurring base that ultimately made it attractive to a strategic acquirer.

Splunk operated in two adjacent but converging markets: **security** (where it competed in the SIEM category) and **observability** (where it competed in monitoring, logging, and APM). It was widely regarded as the incumbent leader in machine-data search and the dominant SIEM platform, with a large installed base in large enterprises and government.

### Business segments / product lines

| Product line | What it did | Competitive context |
|--------------|-------------|---------------------|
| **Splunk Enterprise / Cloud** | Core data platform — index, search, dashboard machine data | Faced [[elastic|Elastic]] (open-source Elasticsearch/ELK) on cost; [[datadog|Datadog]] on cloud-native observability |
| **Splunk Enterprise Security (SIEM)** | Security analytics, threat detection, correlation | Competed with Microsoft Sentinel, IBM QRadar, [[crowdstrike|CrowdStrike]] / [[palo-alto-networks|Palo Alto]] platforms |
| **Splunk SOAR** | Security orchestration and automated response | Acquired (Phantom); category increasingly bundled into broader security platforms |
| **Splunk Observability** | APM and infrastructure monitoring (built on the SignalFx acquisition) | Directly versus [[datadog|Datadog]], New Relic, Dynatrace |
| **Splunk ITSI** | IT service intelligence — service-level monitoring | Niche enterprise IT operations |

## Competitive Positioning at the Time

At acquisition, Splunk was the incumbent in log analytics and SIEM but had spent years on the defensive against two structural threats: cheaper open-source ingestion ([[elastic|Elastic]]) and faster-growing, cloud-native observability ([[datadog|Datadog]]). Its data-volume-based pricing was a frequent customer complaint and the primary wedge competitors used against it. The company's response — the cloud transition, consumption-based pricing, and the SignalFx-built observability suite — stabilized the franchise but did not reverse the perception that growth leadership had migrated to younger, pure-SaaS peers.

| Peer | Relative strength vs. Splunk | Relative weakness vs. Splunk |
|------|------------------------------|------------------------------|
| [[datadog]] (DDOG) | Cloud-native, faster growth, unified observability platform, modern UX | Smaller in security/SIEM; less entrenched in legacy on-prem enterprise |
| [[elastic]] (ESTC) | Open-source distribution, far cheaper ingest, large developer adoption | Weaker enterprise security packaging and managed-service depth |
| [[crowdstrike]] / [[palo-alto-networks]] | Endpoint and platform security momentum, security-native | Not log-analytics-first; less general-purpose machine-data search |
| Microsoft Sentinel | Bundled into Azure/M365, cloud-economics pricing | Less depth as a standalone, vendor-neutral data platform |

The strategic logic for an acquirer was precisely this competitive squeeze: Splunk owned a large, sticky enterprise security/observability footprint and a recurring revenue base, but lacked a hyperscale distribution channel to defend it. [[cisco|Cisco]] supplied that channel.

## Trading Relevance

- **ITPM case study**: Splunk was the second trade initiated by "Dieter" during his ITPM mentoring program with [[anton-kreil]], alongside [[lululemon]], as part of a [[long-short-equity]] [[options]] portfolio (Source: [[itpm-meet-dieter-the-doubler]])
- **M&A trade**: the Cisco acquisition at $157/share represented a ~31% premium over the pre-announcement price. M&A arbitrage traders who held through closing collected the spread. See [[merger-arbitrage]]
- **Now part of Cisco**: as of March 2024, SPLK shares no longer trade. Splunk's products are integrated into Cisco's security and observability portfolio

## The Deal: Cisco Acquisition

Cisco announced the acquisition on September 21, 2023, and closed it on March 18, 2024. The deal was:
- **All-cash** at $157 per share (approximately $28 billion enterprise value)
- **Strategic rationale**: Cisco sought to combine its networking hardware with Splunk's data analytics to build an end-to-end security and observability platform, deepen its recurring-software mix, and use its enterprise sales channel to defend and cross-sell Splunk's installed base against [[datadog]] and Microsoft
- **Regulatory path**: received clearance from US, EU, and Australian regulators with minimal conditions — a key reason the deal traded as a relatively "clean" arb (see below)
- **Consideration type**: all-cash deals carry no exchange-ratio risk for the target holder, only timing and break risk; this kept the spread tight relative to stock-for-stock mergers

## Merger-Arb / Trading Postmortem

The Cisco acquisition is a textbook clean, all-cash [[merger-arbitrage]] case:

- **The premium and the spread.** The $157/share cash price was a ~31% premium over the pre-announcement price. On the day after announcement (Sept 22, 2023), SPLK gapped up toward but stayed below $157 — that residual gap to the deal price *was* the arb spread, compensating holders for the time-to-close and the small probability the deal broke.
- **How the spread decayed.** With clean regulatory expectations and a cooperative target board, the deal closed roughly six months after announcement (Sep 2023 → Mar 2024). Arb desks earned the annualized spread by buying SPLK post-announcement and holding to the March 2024 cash settlement. Because consideration was cash, there was no need to short an acquirer's stock to hedge (contrast the stock-for-stock cases of [[exscientia]]→[[recursion-pharmaceuticals]]).
- **Risk that did NOT materialize.** The main tail risk was antitrust/regulatory delay or block; in practice US, EU, and Australian clearances came with minimal conditions, so the spread tightened steadily into close rather than blowing out.
- **Options angle.** Pre-deal SPLK was a popular [[options]] underlying; post-announcement, implied volatility collapsed (vol crush) because a fixed cash price caps the distribution of outcomes. Selling premium on a near-certain cash deal is a common but capacity-limited arb overlay — assignment around the cash close requires care.
- **ITPM connection.** Splunk was earlier used as a discretionary [[long-short-equity]] [[options]] position in [[anton-kreil]]'s ITPM mentoring program (Source: [[itpm-meet-dieter-the-doubler]]) — a separate, pre-deal trade rationale unrelated to the eventual M&A.

## Lessons / What Defined the Outcome

- **Incumbency without growth leadership invites takeover.** Splunk owned a sticky, high-margin franchise but had ceded the growth narrative to cloud-native peers; a strategic acquirer (not the public market) ultimately re-rated it.
- **Clean cash deals are the "boring good" of merger arb.** No exchange-ratio risk, benign regulatory read, cooperative board → tight spread, low variance, modest annualized return. The opposite end of the spectrum from the collapse cases in this sector ([[nikola]], [[lilium]], [[view-inc]]).
- **Platform consolidation thesis.** Security + observability are consolidating into a few platform vendors; Splunk's absorption into Cisco was a data point in that secular trend, alongside the rise of [[crowdstrike]] and [[palo-alto-networks]] as platform aggregators.

## Risks That Materialized (for an independent Splunk thesis)

- **Pricing-model backlash and competitive erosion** from [[elastic]] (cost) and [[datadog]] (cloud-native UX) capped standalone multiple expansion.
- **Loss of independence:** holders of an independent-Splunk thesis no longer have a vehicle — exposure exists only inside [[cisco]]'s consolidated security/observability portfolio, where it is not separately disclosed.

## Sources

- [[itpm-meet-dieter-the-doubler]] — second trade in Dieter's ITPM mentoring portfolio

## Related

- [[cisco]] — acquirer; absorbed Splunk's security and observability portfolio
- [[datadog]] — cloud-native observability peer
- [[elastic]] — open-source log-analytics peer
- [[crowdstrike]] — security-platform peer/consolidator
- [[palo-alto-networks]] — security-platform peer/consolidator
- [[lululemon]] — paired as the other ITPM case study trade
- [[options]] — instrument used for the ITPM trade
- [[merger-arbitrage]] — the Cisco acquisition as an arb opportunity
