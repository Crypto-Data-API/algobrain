---
title: "Deferred Revenue"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, education, stocks]
domain: [fundamental-analysis, valuation]
difficulty: beginner
aliases: ["Deferred Revenue", "Unearned Revenue", "Deferred Income", "Contract Liability", "Unearned Income"]
prerequisites: ["[[accrual-accounting]]", "[[balance-sheet]]"]
related: ["[[balance-sheet]]", "[[income-statement]]", "[[cash-flow-statement]]", "[[revenue]]", "[[accrual-accounting]]", "[[revenue-growth]]", "[[working-capital]]", "[[financial-statement-analysis]]", "[[free-cash-flow]]"]
---

**Deferred revenue** (also called *unearned revenue* or a *contract liability*) is money a company has **collected from customers but has not yet earned**. It sits on the [[balance-sheet]] as a **liability** — not as [[revenue]] — because the company still owes the customer a product or service. It is the accounting expression of "paid now, delivered later," and it is central to understanding subscription, software (SaaS), insurance, and prepaid-service businesses.

## Why it is a liability, not revenue

Under [[accrual-accounting]], revenue is recognised when it is **earned** (the obligation to the customer is satisfied), not when cash arrives. So when a customer pays upfront:

1. **Cash** increases (an asset).
2. **Deferred revenue** increases by the same amount (a liability) — the company's promise to deliver.
3. Nothing yet hits the [[income-statement]].

As the company delivers over time, it **recognises** the earned portion: deferred revenue (liability) goes down and [[revenue]] on the income statement goes up. The liability is essentially a "revenue backlog" waiting to be earned.

```
Day 0  — Customer prepays $1,200 for a 12-month subscription
         Cash +$1,200 (asset)   Deferred revenue +$1,200 (liability)
         Revenue recognised: $0

Each month — deliver one month of service
         Deferred revenue −$100   Revenue +$100  (income statement)

Month 12 — Deferred revenue balance = $0, full $1,200 recognised
```

## Where it appears on the statements

| Statement | How deferred revenue appears |
|-----------|------------------------------|
| [[balance-sheet]] | A liability — usually **current** (to be earned within 12 months), with any longer-dated portion shown as **non-current** |
| [[income-statement]] | Nothing directly; revenue is recognised only as the obligation is satisfied |
| [[cash-flow-statement]] | An **increase** in deferred revenue is a positive adjustment in operating cash flow ([[working-capital]]) — cash was collected ahead of the revenue |

This makes deferred revenue a rare liability that investors often view *positively*: it represents cash already in hand and demand already committed.

## How it is used in analysis

- **Forward-revenue visibility.** A growing deferred-revenue balance signals strong future [[revenue-growth]] — customers have already paid for services the company will recognise in coming quarters. For subscription businesses, it is a leading indicator that the income statement lags.
- **Negative working capital advantage.** Because customers fund the business in advance, prepaid-model companies can operate with **negative [[working-capital]]** and strong [[free-cash-flow]] — cash collected upfront finances operations before costs are incurred.
- **Bookings vs. billings vs. revenue.** Analysts of SaaS firms distinguish *bookings* (contracts signed), *billings* (revenue + change in deferred revenue, a proxy for cash demand), and recognised *revenue*. **Remaining performance obligations (RPO)** — disclosed under modern revenue standards — extends this view to contracted-but-unrecognised revenue beyond the deferred-revenue balance.
- **Quality check.** Rising deferred revenue alongside rising recognised revenue is a healthy growth signal; recognised revenue rising while deferred revenue *shrinks* can indicate the company is burning through backlog faster than it is replenishing it.

## Limitations

- **Not guaranteed profit.** Deferred revenue is cash received, but delivering the service still costs money; it is not free margin.
- **Refund/cancellation risk.** If contracts can be cancelled, some of the liability may be returned rather than earned.
- **Recognition judgement.** How and when an obligation is deemed "satisfied" involves estimates; aggressive timing can pull revenue forward — a [[financial-statement-analysis]] red flag.
- **Lumpy billings.** Annual or multi-year prepay cycles make the balance swing between quarters; trend it year over year, not quarter to quarter.

## Worked example (hypothetical)

**Acme Cloud** (a hypothetical SaaS company) sells annual subscriptions. On 1 January it signs 100 customers who each prepay **$1,200** for the year — **$120,000** total cash collected upfront.

- **1 January:** Cash rises $120,000; deferred revenue (liability) rises $120,000. Recognised [[revenue]] so far: **$0**.
- **End of Q1 (3 months delivered):** Acme has earned 3/12 of each contract = **$30,000** recognised as revenue. Deferred revenue falls to **$90,000**.
- **Cash flow effect:** the $120,000 collected upfront, less the $30,000 now recognised, leaves a $90,000 deferred-revenue balance that boosted Q1 operating cash flow ahead of the income statement.

By year-end the full $120,000 is recognised and the deferred-revenue liability returns to zero — unless new subscriptions have refilled it, which for a growing business they will.

## Related

- [[balance-sheet]] — where deferred revenue is carried as a liability
- [[income-statement]] — where the balance is released into recognised revenue over time
- [[cash-flow-statement]] — where an increase boosts operating cash flow
- [[revenue]] · [[revenue-growth]] — the earned figure deferred revenue feeds
- [[accrual-accounting]] — the recognition basis that creates the liability
- [[working-capital]] — deferred revenue can drive a negative-working-capital model
- [[free-cash-flow]] — upfront cash collection strengthens it

## Sources

- IFRS 15, *Revenue from Contracts with Customers* (introduces the "contract liability" term)
- US GAAP ASC 606, *Revenue from Contracts with Customers*
- Stephen Penman, *Financial Statement Analysis and Security Valuation*
