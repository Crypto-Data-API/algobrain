---
title: "FXall"
type: entity
created: 2026-06-13
updated: 2026-06-13
status: good
tags: [forex, market-microstructure, data-provider]
entity_type: company
founded: 2001
headquarters: "Operated by LSEG (Refinitiv), global"
website: "https://www.lseg.com/en/fx/venues/fxall-electronic-trading-platform"
aliases: ["FXall", "Refinitiv FXall", "LSEG FXall"]
related: ["[[forex]]", "[[bank-for-international-settlements]]", "[[liquidity-provider]]", "[[market-microstructure]]", "[[cls-group]]"]
---

FXall is an institutional electronic [[forex|FX]] trading platform operated by [[lseg|LSEG]] (London Stock Exchange Group, via its Refinitiv business). It is primarily a multi-dealer request-for-quote (RFQ) and workflow platform covering spot, forwards, swaps, [[ndf|NDFs]], and [[options]], serving the disclosed, relationship-based segment of the [[forex|FX]] market.

## Overview

FXall is owned and operated by [[lseg|LSEG]], having passed through successive corporate owners — originally an independent venue, then part of Thomson Reuters, then Refinitiv, and now consolidated under LSEG following its acquisition of Refinitiv. It is one of the largest institutional [[forex|FX]] venues, with a client base spanning corporates, asset managers, hedge funds, and banks. Its core proposition is bringing buy-side firms and corporate treasuries together with a panel of [[liquidity-provider|liquidity providers]] in a disclosed, name-given environment, paired with an end-to-end trade workflow.

## Execution and Workflow

FXall's primary execution model is **multi-dealer RFQ (request-for-quote)** with **disclosed liquidity**: a client requests prices from a chosen panel of dealers, each dealer sees who is asking, and the client selects the best response. This contrasts with an anonymous central limit order book ([[clob|CLOB]]), where participants trade against a shared, name-blind order book. RFQ favours relationship pricing, larger or less-standardised tickets, and instruments where a streaming book is thin; CLOB favours anonymity, tight standardised spot pricing, and high-frequency interaction. (See [[rfq-vs-clob]].)

Beyond RFQ, FXall also supports **streaming** prices and **order-based execution**, alongside strong **pre-trade analytics** and a **post-trade STP (straight-through processing) and reporting** workflow. It provides netting and settlement integration — including links into [[cls-group|CLS]] for settlement-risk reduction — so that flow can move from execution through confirmation, allocation, and settlement within a single operational chain. Instrument coverage spans **spot, forwards, swaps, [[ndf|NDFs]], and [[options]]**, supporting multi-currency, multi-product institutional [[forex|FX]] workflows.

## Position in the Market

FXall sits within [[lseg|LSEG]]'s broader [[forex|FX]] suite. It complements the **Matching** [[clob|CLOB]] venue — the anonymous, order-book-driven interbank platform — by covering the disclosed RFQ and workflow side of the market. Together they let LSEG offer both major execution paradigms across the same client and data footprint. FXall also integrates with the wider LSEG/Refinitiv data ecosystem, connecting execution to reference data, analytics, and post-trade tooling within the same provider environment.

## Relevance to Traders

For institutional participants, FXall is a reference point in **venue selection**: choosing it implies a preference for disclosed, relationship-based RFQ execution over anonymous [[clob|CLOB]] trading. Understanding **RFQ vs CLOB execution models** is central to [[market-microstructure|microstructure]] analysis of [[forex|FX]] — the two paths carry different information leakage, pricing, and counterparty dynamics. FXall's **multi-currency workflow** and integrated [[straight-through-processing|STP]]/settlement chain explain why much corporate-treasury and buy-side flow concentrates on platforms like it: these participants value workflow, confirmation, and settlement integration as much as raw spread, and prefer disclosed pricing where a known dealer relationship and credit line matter more than anonymity.

## Related

- [[forex]]
- [[liquidity-provider]]
- [[market-microstructure]]
- [[cls-group]]
- [[bank-for-international-settlements]]
- [[clob]]
- [[rfq-vs-clob]]
- [[ndf]]
- [[lseg]]

## Sources

Compiled from LSEG/Refinitiv public documentation (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md). https://www.lseg.com/en/fx/venues/fxall-electronic-trading-platform
