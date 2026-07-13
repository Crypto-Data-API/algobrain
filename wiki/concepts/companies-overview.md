---
title: "Companies Overview"
type: overview
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [company, fundamental-analysis, valuation]
aliases: ["Companies Overview", "Companies"]
related: ["[[entities-overview]]", "[[fundamental-analysis]]", "[[peer-comparison]]", "[[valuation]]", "[[financial-statement-analysis]]"]
domain: [fundamental-analysis]
difficulty: beginner
---

This page is the directory and methodology hub for **company** pages in the wiki — public companies analysed for investment, plus the financial-services firms, [[exchanges-overview|exchanges]], and technology companies relevant to trading. Company pages live primarily under `wiki/entities/companies/` and cover business model, competitive positioning, fundamentals, and the investment thesis. For the broader directory of people, exchanges, regulators, and protocols, see [[entities-overview]].

## How Companies Are Analysed Here

Company pages are built on a consistent [[fundamental-analysis|fundamental-analysis]] frame so they can be compared like-for-like:

- **Business model and moat** — how the company makes money and what protects those profits (network effects, switching costs, scale, brand).
- **[[financial-statement-analysis|Financial statements]]** — revenue growth, margins ([[gross-margin]], operating margin), [[return-on-equity|ROE]]/[[return-on-invested-capital|ROIC]], debt, and free cash flow.
- **[[valuation|Valuation]]** — absolute methods ([[dcf-analysis|DCF]]) and relative multiples via [[peer-comparison]]: [[price-to-earnings-ratio|P/E]], [[forward-pe|forward P/E]], [[ev-ebitda|EV/EBITDA]], and price-to-sales.
- **Sector context** — companies are benchmarked against [[gics-classification|GICS sector]] peers, since a multiple is only meaningful relative to its industry. Sector-specific metrics apply where relevant (e.g., [[retail-metrics]] for consumer businesses, net interest margin for banks).
- **Risks and catalysts** — what could break the thesis and what could re-rate the stock.

## Reading a Company Page

Each company page aims to answer three questions a trader or investor actually cares about: *What does it do and how durable is that? What are the numbers saying? Is it cheap or expensive relative to its growth and its peers?* Pages are kept current with the company's reporting cycle where they support live analysis (these feed the investor dashboard's stock view via the fundamentals node).

## All Company Pages

```dataview
TABLE status, updated, tags
FROM "wiki/entities/companies"
WHERE type = "entity"
SORT updated DESC
```

## Related

- [[entities-overview]] — the full entity directory (people, exchanges, regulators, protocols)
- [[fundamental-analysis]] — the analytical framework applied to every company
- [[peer-comparison]] — benchmarking a company against its sector
- [[valuation]] — methods for estimating intrinsic value
- [[financial-statement-analysis]] — reading the financials behind the thesis
