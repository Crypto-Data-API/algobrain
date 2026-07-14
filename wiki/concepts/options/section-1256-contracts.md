---
title: "Section 1256 Contracts"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, derivatives, regulation, futures]
aliases: ["Section 1256", "1256 Contracts", "60/40 Tax Treatment"]
domain: [derivatives, options, taxation]
difficulty: intermediate
related: ["[[vix]]", "[[american-vs-european-options]]", "[[tax-implications-trading]]", "[[capital-gains]]", "[[options-portfolio-construction]]"]
---

**Section 1256 of the US Internal Revenue Code** governs the tax treatment of certain regulated derivatives — including broad-based stock index options, regulated futures contracts, and dealer equity options. Its defining feature is the **60/40 rule**: every realized gain or loss is automatically split 60% long-term capital gain/loss and 40% short-term, regardless of how long the position was held. For active traders of qualifying products like SPX, XSP, NDX, RUT, and [[vix|VIX]] options, Section 1256 is one of the largest structural tax advantages available in US markets.

## Overview

Section 1256 was enacted in 1981 to bring consistent treatment to certain exchange-traded derivatives that the IRS judged were marked-to-market for risk-management purposes anyway. The statute imposes three key rules:

1. **Mark-to-market at year-end** — open positions on Dec 31 are treated as if sold at fair market value on that date.
2. **60/40 character** — gains and losses (whether realized during the year or via mark-to-market) are split 60% long-term / 40% short-term regardless of holding period.
3. **Loss carryback** — losses in Section 1256 contracts can be carried back up to 3 years to offset prior Section 1256 gains (a feature unavailable to ordinary capital losses).

Reporting is on **IRS Form 6781** (Gains and Losses from Section 1256 Contracts and Straddles).

## What Qualifies

The IRS lists specific categories that qualify for Section 1256 treatment:

| Category | Examples |
|---|---|
| **Regulated futures contracts** | E-mini S&P 500, crude oil, gold, treasury futures, etc. |
| **Broad-based stock index options** | SPX, XSP, NDX (Nasdaq-100), RUT (Russell 2000), [[vix|VIX]] options |
| **Foreign currency contracts** | Specified forex contracts traded on a qualified board/exchange |
| **Dealer equity options** | Held by registered options dealers in their dealer capacity |
| **Dealer securities futures contracts** | Same dealer condition |

## What Does NOT Qualify

| Category | Reason |
|---|---|
| **SPY options** | SPY is a single-fund ETF, not a "broad-based stock index" |
| **QQQ / IWM options** | Same reason — ETF options, not index options |
| **Single-stock options** (AAPL, NVDA, etc.) | Equity options on individual stocks |
| **Narrow-based index options** | Indices with too few components per IRS definition |
| **Most crypto options** (Deribit, etc.) | Not regulated under §1256 — generally treated as property |

The single most-misunderstood point is that SPY options and SPX options are taxed completely differently despite tracking the same index. **Substance over form does not save SPY** — it's an option on an ETF, not an option on an index.

## Tax Math (worked example)

Consider an active trader making **$100,000 of net option-trading profit in a year**, all short-term holding periods, top federal bracket.

**Scenario A — All trades in SPY (standard equity):**

- Short-term gains taxed at top federal rate ~37% (plus 3.8% NIIT where applicable, plus state).
- Federal tax: $100,000 × 37% = **$37,000**.

**Scenario B — All trades in SPX (Section 1256):**

- 60% × $100,000 = $60,000 taxed long-term at top rate ~20%: $12,000.
- 40% × $100,000 = $40,000 taxed short-term at top rate ~37%: $14,800.
- Federal tax: **$26,800**.

**After-tax difference: $10,200 saved annually**, or about 10.2% of gross P&L. For a trader compounding over a decade, the cumulative impact is enormous.

This is the single biggest reason why professional options portfolios route nearly all S&P 500 exposure through SPX or XSP rather than SPY.

## Mark-to-Market Provision

Open Section 1256 positions on Dec 31 are deemed-closed at fair market value:

- The unrealized gain/loss is treated as realized for tax purposes.
- The position's tax basis is reset to the year-end FMV going into the next year.
- This eliminates ambiguity about long/short-term treatment and prevents indefinite deferral.

**Consequence:** even traders who never close a position can owe tax on gains. For multi-year long-dated SPX structures, this requires planning to ensure liquidity for the tax bill.

## Loss Carryback

Section 1256 losses are uniquely flexible:

- An election on Form 6781 allows losses to be **carried back 3 years**, but only against prior Section 1256 gains.
- Any unused loss carries forward indefinitely (as ordinary capital loss subject to standard rules).
- This is unavailable for losses in standard equity options.

Practically: a trader who has a strong year followed by a bad year can recover taxes already paid.

## Form 6781

The form has two main parts:

- **Part I** — gains and losses on Section 1256 contracts (combined into a single 60/40 split).
- **Part II** — losses from straddles, with specific anti-abuse rules to prevent matching of Section 1256 losses against non-1256 gains in offsetting positions.

Brokers issue 1099-Bs that already segregate Section 1256 contracts, simplifying preparation.

## Portfolio Implications

For actively traded options portfolios, Section 1256 awareness is foundational:

- **Default to SPX/XSP for index exposure**, not SPY, unless there is a specific reason (e.g., IRA, account size, penny-tick advantage that outweighs tax over a known short hold).
- **Account-size threshold for XSP vs SPX** — traders below ~$500K typically use XSP for granularity; above that, SPX dominates on commissions and operational simplicity.
- **Tax-aware Sharpe** — strategy ranking should be done on after-tax returns where possible. A SPY iron condor with a 0.8 gross Sharpe may underperform an identical SPX iron condor on after-tax basis.
- **Mark-to-market planning** — long-dated SPX hedges that span year-end create deemed-disposition events; cash flow planning matters.
- **Loss carryback** — a bad year following a good year can recover meaningful taxes paid.

## Limitations

- **Not unlimited** — straddle rules under §1092 can still defer losses; the anti-abuse provisions exist precisely to prevent gaming.
- **State tax treatment varies** — a few states do not honor the 60/40 split and tax all the gain at ordinary rates.
- **NIIT applies** — the 3.8% Net Investment Income Tax applies to Section 1256 gains for high-income filers, partially offsetting the federal advantage.
- **Dealer status matters** — dealer equity options must actually be held in dealer capacity; a non-dealer cannot self-elect into this category.
- **Wash sale interplay** — Section 1256 contracts are not subject to traditional §1091 wash sale rules in the same way, but coordinated positions across §1256 and non-§1256 products can trigger straddle and anti-abuse rules. See wash-sale-rules-options.

## Related

- [[vix]] — VIX options qualify
- [[american-vs-european-options]] — exercise style usually correlates with §1256 status
- [[tax-implications-trading]]
- [[capital-gains]]
- [[options-portfolio-construction]]

## Sources

- Internal Revenue Code §1256
- IRS Form 6781 instructions
- IRS Publication 550 (investment income and expenses)
- Treasury regulations §1.1256-1 et seq.
