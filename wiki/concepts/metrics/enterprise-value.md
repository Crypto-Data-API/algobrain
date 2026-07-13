---
title: "Enterprise Value"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, indicators, valuation]
domain: [fundamental-analysis]
prerequisites: ["[[financial-statement-analysis]]"]
difficulty: intermediate
aliases: ["EV", "Enterprise Value", "enterprise value"]
related: ["[[ebitda]]", "[[ev-ebitda]]", "[[price-to-earnings-ratio]]", "[[debt-to-equity]]", "[[free-cash-flow]]", "[[dcf-analysis]]", "[[market-capitalization]]", "[[valuation]]", "[[discounted-cash-flow]]"]
---

Enterprise Value (EV) represents the total value of a business — what it would cost to acquire the entire company, including both equity and debt, minus available cash. It is a more complete measure of company value than market capitalisation alone because it accounts for the capital structure.

## Formula

```
EV = Market Capitalisation + Total Debt + Preferred Equity + Minority Interest − Cash & Equivalents
```

A simpler shorthand most analysts use day to day:

```
EV = Market Cap + Net Debt        (where Net Debt = Total Debt − Cash & Equivalents)
```

The intuition: when you buy a company, you pay equity holders ([[market-capitalization|market cap]]), you assume responsibility for its debt and other senior claims (preferred equity, minority interest), but you also take ownership of its cash, which you can use to pay down some of that debt. Net of cash, EV is the true "all-in" takeout price.

### The build-up, line by line

| Component | Sign | Why |
|---|---|---|
| Market capitalisation | + | What you pay common equity holders (price × shares) |
| Total debt (short + long term) | + | You assume the obligation to repay lenders |
| Preferred equity | + | A senior claim ahead of common equity |
| Minority (non-controlling) interest | + | The slice of consolidated subsidiaries you don't own |
| Cash & cash equivalents | − | You inherit the cash and can use it to retire debt |

### Worked example

Suppose two companies each generate the same $240M of [[ebitda|EBITDA]] but carry very different balance sheets:

| | Company A (debt-free) | Company B (leveraged) |
|---|---|---|
| Market cap | $2,160M | $1,680M |
| Total debt | $0 | $560M |
| Cash | $0 | $80M |
| Net debt | $0 | $480M |
| **Enterprise value** | **$2,160M** | **$2,160M** |
| Market cap / EBITDA | 9.0x | 7.0x |
| **EV / EBITDA** | **9.0x** | **9.0x** |

A naive equity-only multiple makes Company B look "cheaper" (7.0x vs 9.0x), but that discount is entirely an artefact of its leverage. EV/EBITDA correctly shows the two businesses are valued identically at **9.0x** — which is exactly why [[ev-ebitda|EV/EBITDA]] is the preferred cross-company multiple.

## Why EV Matters

Market cap only reflects what equity holders own. EV reflects what an acquirer would actually pay — they inherit the debt but also get the cash on hand. This makes EV-based ratios (like [[ev-ebitda|EV/EBITDA]]) more useful for comparing companies with different capital structures than PE ratio alone. A debt-free company and an identical leveraged company can have very different market caps but nearly the same EV; EV-based multiples correctly treat them as similarly valued businesses.

## Common EV-Based Ratios

| Ratio | Formula | Use |
|-------|---------|-----|
| [[ev-ebitda|EV/EBITDA]] | EV / EBITDA | Capital-structure-neutral valuation comparison; the workhorse multiple |
| EV/Sales (EV/Revenue) | EV / Revenue | Useful for unprofitable or early-stage companies with no earnings |
| EV/EBIT | EV / EBIT | Like EV/EBITDA but penalises capex-heavy firms via depreciation |
| EV/FCF | EV / [[free-cash-flow]] | Cash-based valuation; hardest to game |

The denominators all sit *above* interest on the income statement, so they are paired with EV (a whole-firm numerator) rather than with [[market-capitalization|market cap]] (an equity-only numerator). The matching rule is the key discipline: **equity-only numerator → equity-only denominator** (e.g. [[price-to-earnings-ratio|P/E]], price/[[book-value]]); **whole-firm numerator (EV) → pre-interest denominator** (EBITDA, EBIT, sales). Mixing them — e.g. EV/net-income — is a classic modelling error.

## Common Pitfalls

- **Stale debt and cash.** Market cap is real-time, but debt and cash come from the last quarterly balance sheet. In fast-moving situations (raises, buybacks, big capex) the two are out of sync.
- **What counts as "debt"?** Operating leases (post-IFRS 16/ASC 842), underfunded pensions, convertible notes, and contingent earn-outs are frequent disputes. Two analysts can compute materially different EVs for the same firm.
- **Restricted vs. operating cash.** Cash trapped overseas, pledged as collateral, or needed for working capital should not be netted at full value.
- **Negative net debt.** A cash-rich company (cash > debt) has EV *below* its market cap. If cash exceeds market cap, EV goes negative — usually a sign the market doubts the cash or fears it will be burned.
- **Minority interest and associates.** Consolidated revenue/EBITDA includes 100% of partly-owned subs, so minority interest must be added to EV to keep numerator and denominator consistent.

## Trading Relevance

EV is the price tag in every M&A and [[buyouts|leveraged buyout]] model — deal values are quoted on an EV basis, and merger-arbitrage and event-driven traders work in EV terms because they must account for the target's debt they will assume. EV-based multiples ([[ev-ebitda|EV/EBITDA]], EV/EBIT, EV/Revenue, EV/FCF) are the standard cross-sectional valuation screens in quantitative value strategies, preferred over [[price-to-earnings-ratio|P/E]] precisely because they are capital-structure-neutral and harder to game with buybacks. In a [[dcf-analysis|DCF]] (or [[discounted-cash-flow]]), discounting unlevered free cash flow at the WACC yields EV directly; subtracting net debt then recovers equity value. A practical trap: EV is sensitive to how "debt" and "cash" are defined — operating leases, underfunded pensions, and restricted cash are frequent points of dispute in deal valuation.

### The EV ↔ equity-value bridge

The most-used identity in deal and DCF work runs in both directions:

```
Equity Value (market cap) = Enterprise Value − Net Debt − Preferred − Minority Interest
Enterprise Value          = Equity Value      + Net Debt + Preferred + Minority Interest
```

A [[discounted-cash-flow]] produces EV first (it discounts cash flows available to *all* capital providers). You then walk *down* the bridge — subtract net debt and other senior claims — to reach the equity value, and divide by shares to get a per-share fair value. Merger-arb traders run the same bridge in reverse: an announced equity offer price is grossed up by assumed debt to find the EV the acquirer is really paying.

## Fred's Context

[[fred-mcnaught|Fred]] primarily uses [[price-to-earnings-ratio|PE ratio]] and [[return-on-equity|ROE]] for valuation, but EV-based metrics are important when evaluating [[buyouts|buyout]] scenarios and comparing companies with different debt levels — situations Fred discusses in several sessions (e.g., [[fred-sam-session-2024-04-11]] on buyout tactics, [[fred-sam-session-2024-04-26]] on [[debt-to-equity|D/E]] relationship with ROE).

## Related

- [[ebitda]] — Most common EV denominator
- [[ev-ebitda]] — The primary multiple built on EV
- [[market-capitalization]] — Equity-only value; EV's starting point
- [[free-cash-flow]] — Unlevered FCF discounts to EV directly
- [[dcf-analysis]], [[discounted-cash-flow]] — DCF of unlevered FCF yields EV directly
- [[price-to-earnings-ratio]] — Equity-only valuation metric (matching-rule contrast)
- [[debt-to-equity]] — Capital structure that EV neutralises
- [[valuation]] — Broader valuation framework
- [[buyouts]] — EV is the acquisition price framework

## Sources

- Damodaran, A., *Investment Valuation* — enterprise value definition, EV multiples, and net-debt adjustments
- CFA Institute curriculum, *Equity Investments* — enterprise value and EV-based multiples
- Rosenbaum, J. & Pearl, J., *Investment Banking: Valuation, LBOs, and Mergers & Acquisitions* — EV in deal and LBO modelling
