---
title: "ITAA 1997 Overview (Trading-Relevant Provisions)"
type: overview
created: 2026-05-30
updated: 2026-06-11
status: good
tags: [australia, tax, regulation, education]
aliases: ["Income Tax Assessment Act 1997", "ITAA 1997", "Income Tax Assessment Act"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: intermediate
related:
  - "[[australian-investor-tax]]"
  - "[[non-commercial-losses-div-35]]"
  - "[[tr-97-11-carrying-on-a-business]]"
  - "[[trader-vs-investor-classification-au]]"
  - "[[commissioners-discretion-s-35-55]]"
  - "[[pcg-2021-2-div-35-discretion]]"
  - "[[smsf-trading-tax-treatment]]"
  - "[[capital-gains-tax-discount]]"
  - "[[smsf]]"
---

> **Not tax advice.** This page is a trader-facing reference to Australian tax provisions. Always verify positions against current legislation and confirm with a registered tax agent or specialist tax lawyer before relying on any treatment.

The Income Tax Assessment Act 1997 (ITAA 1997) is the principal Commonwealth statute governing Australian income tax. For traders, a small number of provisions in Divisions 6, 8, 35, 70, 102, 104, 110, and 152 carry almost the entire load of determining whether trading gains are taxed as ordinary income or capital gains, whether losses are immediately deductible, and whether structures like an [[smsf]] alter the treatment. This page indexes those provisions and points to the dedicated wiki pages that develop each.

## Why traders care about specific ITAA sections

The Act is unusual in that the **same trading activity can be taxed under three completely different regimes** depending on classification:

1. **Business income / loss** (Division 6, Division 8) — gross trading receipts assessable; trading losses immediately deductible against other income, **subject to the Division 35 non-commercial loss rules**
2. **Capital gains / losses** (Parts 3-1, 3-3, Divisions 100–152) — net gains taxable, with the [[capital-gains-tax-discount|50% CGT discount]] for individuals on assets held > 12 months; capital losses only offset capital gains
3. **Trading stock** (Division 70) — applies if shares/securities are held as trading stock of a share-trading business; mark-to-market style treatment, no CGT

The threshold question — which regime applies — is answered by the **carrying on a business** test in [[tr-97-11-carrying-on-a-business|TR 97/11]] and the case law it draws from (e.g., *Ferguson v FC of T*, *FC of T v Radnor Pty Ltd*).

## Key sections at a glance

| Section / Division | Subject | Trader relevance | Wiki page |
|---|---|---|---|
| **s 6-5** | Ordinary income (assessable) | Trading-business receipts go here | — |
| **s 8-1** | General deduction rule | Trading-business losses claimable here, subject to Div 35 | — |
| **Div 35** | Non-commercial losses | Defers business losses unless one of four tests met | [[non-commercial-losses-div-35]] |
| **s 35-10** | Loss deferral rule + exceptions | The operative rule | [[non-commercial-losses-div-35]] |
| **s 35-10(2E)** | $250k adjusted taxable income gate | Above this, no exception tests available | [[non-commercial-losses-div-35]] |
| **s 35-30** | Assessable income test ($20k) | Easiest exception for active traders | [[non-commercial-losses-div-35]] |
| **s 35-35** | Profits test (4 of past 5 years) | For consistently profitable smaller activities | [[non-commercial-losses-div-35]] |
| **s 35-40** | Real property test ($500k) | Rarely relevant to traders | [[non-commercial-losses-div-35]] |
| **s 35-45** | Other assets test ($100k) | Plant & equipment, IP, motor vehicles — narrow for pure traders | [[non-commercial-losses-div-35]] |
| **s 35-55** | Commissioner's discretion | "Special circumstances" or "lead time" escape | [[commissioners-discretion-s-35-55]] |
| **Div 70** | Trading stock | If shares treated as trading stock | — |
| **s 102-5** | Net capital gain inclusion | CGT regime entry point | [[australian-investor-tax]] |
| **s 104 series** | CGT events (A1, C2, etc.) | What constitutes a "disposal" | — |
| **s 110-25** | Cost base elements | Brokerage, incidental costs | [[australian-investor-tax]] |
| **Div 115** | 50% CGT discount | The critical 12-month rule | [[capital-gains-tax-discount]] |
| **Div 152** | Small business CGT concessions | Rarely applicable to pure trading | — |

## The classification cascade

A practical decision tree:

```
1. Are the shares/derivatives held as part of a "business" per TR 97/11?
   ├── YES → Business income regime
   │         ├── Profits taxed under s 6-5
   │         ├── Losses deductible under s 8-1 SUBJECT TO Div 35
   │         └── If Div 35 exceptions fail → loss deferred indefinitely
   │
   └── NO → Investment regime (capital account)
             ├── Gains taxed under CGT (Div 100+)
             ├── 50% CGT discount if held > 12 months (Div 115)
             └── Capital losses ONLY offset capital gains, carried forward
```

The Commissioner's view on which side of this line a trader sits is **highly fact-specific**. The eight indicators in [[tr-97-11-carrying-on-a-business|TR 97/11]] are not a checklist — they are weighed in the round. See [[trader-vs-investor-classification-au]] for the practical guide.

## Entity-specific overlays

The same ITAA provisions apply differently depending on the entity holding the position:

| Entity | Rate / regime | Special features |
|---|---|---|
| **Individual** | Marginal rates (up to 47% incl. Medicare) | 50% CGT discount; Div 35 fully applies |
| **Company** | 25% (base rate entity) or 30% | No CGT discount; Div 35 does **not apply** (s 35-5(2)) |
| **Trust** | Beneficiary's marginal rate (or trustee assessment) | 50% CGT discount flows through; Div 35 attributable share basis |
| **Partnership** | Partner's marginal rate | Div 35 applies per partner's share |
| **[[smsf|SMSF]]** | 15% accumulation / 0% pension | 33.33% CGT discount; Div 35 does **not** apply (super fund rules) |

The [[smsf-trading-tax-treatment]] page develops the SMSF-specific treatment in detail.

## ATO administrative materials

These are not legislation but are highly persuasive in practice:

| Reference | Subject | Wiki page |
|---|---|---|
| **TR 97/11** | Indicators of "carrying on a business" | [[tr-97-11-carrying-on-a-business]] |
| **TR 2005/15** | Tax consequences of financial contracts for differences | — |
| **TD 2011/21** | When are gains from share trading ordinary income vs capital | — |
| **PCG 2021/2** | Commissioner's approach to s 35-55 discretion | [[pcg-2021-2-div-35-discretion]] |
| **PS LA 2008/3** | Provision of advice on Commissioner's discretion | — |
| **Numerous private rulings** | Fact-specific applications | — (search ATO Legal Database) |

## Common trader mistakes

- **Assuming all trading is on capital account by default.** If your activity has the volume, system, profit-seeking purpose, and business-like organisation of TR 97/11 it is a business — and the ATO can reclassify retrospectively.
- **Assuming all trading is business income.** The opposite mistake — claiming losses under s 8-1 without satisfying TR 97/11 — invites an audit. The "I'm a trader" self-label is not enough.
- **Ignoring Division 35** once a business is established. Losses do not flow through automatically; one of the four tests in s 35-10 must be satisfied (or the discretion granted).
- **Mixing CGT and trading-stock treatment** in the same financial year. Once an election is made or implicit treatment adopted, consistency matters.
- **Forgetting the $250,000 income gate** in s 35-10(2E). For high-income earners, none of the four exception tests are available — the only path to immediate loss deduction is the Commissioner's discretion under [[commissioners-discretion-s-35-55|s 35-55]].

## Source notes

This page is written from the public text of the ITAA 1997, ATO public rulings (TR 97/11, PCG 2021/2), and standard tax-practice references. Section numbers and thresholds are accurate as at FY 2024–25 / 2025–26. **Confirm current figures and any amendments before relying on this.**

## Related

- [[non-commercial-losses-div-35]] — Division 35 detail
- [[tr-97-11-carrying-on-a-business]] — the threshold business test
- [[trader-vs-investor-classification-au]] — practical guide
- [[commissioners-discretion-s-35-55]] — s 35-55 escape hatch
- [[pcg-2021-2-div-35-discretion]] — Commissioner's practical approach
- [[smsf-trading-tax-treatment]] — SMSF-specific treatment
- [[australian-investor-tax]] — broader investor tax overview
- [[capital-gains-tax-discount]] — 50% CGT discount
- [[smsf]] — Self-Managed Super Fund structure
