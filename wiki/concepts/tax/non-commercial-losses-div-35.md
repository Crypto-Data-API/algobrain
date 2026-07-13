---
title: "Non-Commercial Losses (ITAA 1997 Division 35)"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [australia, tax, regulation, risk-management]
aliases: ["Division 35", "Div 35", "Non-Commercial Loss Rules", "NCL Rules", "Section 35-10"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: advanced
prerequisites: ["[[tr-97-11-carrying-on-a-business]]", "[[australian-investor-tax]]"]
related:
  - "[[tr-97-11-carrying-on-a-business]]"
  - "[[trader-vs-investor-classification-au]]"
  - "[[commissioners-discretion-s-35-55]]"
  - "[[pcg-2021-2-div-35-discretion]]"
  - "[[itaa-1997-overview]]"
  - "[[smsf-trading-tax-treatment]]"
  - "[[australian-investor-tax]]"
---

> **Not tax advice.** Division 35 is fact-sensitive and the dollar thresholds, income gate, and exception tests have been amended several times. **All dollar figures below ($250,000 / $20,000 / $500,000 / $100,000) are stated as indicative of the regime as commonly published and must be confirmed against the current Act.** Verify current law and confirm with a registered tax agent before relying on anything here.

## At a Glance

| Question | Short answer (indicative — verify) |
|----------|-----------------------------------|
| **What is Div 35?** | The non-commercial loss regime: it can *defer* a business loss so it cannot offset other income this year |
| **Who does it apply to?** | Individuals and partnerships that include an individual carrying on a business activity |
| **Who is exempt?** | Companies, trusts (own capacity), [[smsf\|SMSFs]], and pure capital-account investors |
| **First question** | Is the activity a *business*? (see [[tr-97-11-carrying-on-a-business\|TR 97/11]]) — if not, Div 35 is irrelevant |
| **Income gate** | Adjusted taxable income must be **< ~$250,000** before any of the four tests can apply (s 35-10(2E)) |
| **The four tests** | s 35-30 (~$20k assessable income) · s 35-35 (profits 3 of 5 yrs) · s 35-40 (~$500k real property) · s 35-45 (~$100k other assets) |
| **If a test passes** | Loss is deductible this year against *any* income |
| **If no test passes** | Loss is **deferred** (not lost) to a future year of the same/similar activity |
| **Final escape hatch** | Commissioner's discretion under [[commissioners-discretion-s-35-55\|s 35-55]] (narrow grounds) |
| **Most-used test for traders** | s 35-30 — any real trading book generates ~$20k+ assessable income |

Division 35 of the ITAA 1997 is the **non-commercial loss** regime. It applies when an individual (or partnership including an individual) carries on a business activity that produces a loss for the year. By default, the loss is **deferred** to a later year in which the same activity produces income or a gain — meaning it cannot offset salary, dividends, capital gains, or other income. Four objective tests in s 35-10 provide exceptions; the Commissioner's discretion in [[commissioners-discretion-s-35-55|s 35-55]] is the final escape hatch. For traders classified as carrying on a business (per [[tr-97-11-carrying-on-a-business|TR 97/11]]), Division 35 is the single most important provision determining whether a losing year actually reduces this year's tax bill.

## Who Division 35 applies to

Division 35 applies to **individuals** and **partnerships that include at least one individual** who carry on a business activity (s 35-5). It does **not** apply to:

- Companies (s 35-5(2)) — they have their own loss-carry-forward rules under Div 36
- Trusts (in their own capacity) — losses are trapped at trust level under Div 165 / s 102UC
- [[smsf|SMSFs]] and other super funds — covered by the super-fund-specific loss rules (see [[smsf-trading-tax-treatment]])
- Investments held on capital account — no "business" means Div 35 is irrelevant; CGT regime applies instead

The first question to answer is therefore always: **is this a business?** See [[tr-97-11-carrying-on-a-business]] and [[trader-vs-investor-classification-au]].

## The default rule — s 35-10

If you carry on a business activity and it produces a loss for the income year, **the loss is quarantined** unless one of the four exception tests in s 35-30, 35-35, 35-40 or 35-45 is met *and* the $250,000 income gate in s 35-10(2E) is satisfied.

A deferred loss is not "lost" — it is carried forward and applied against assessable income from the same or similar business activity in a later year. But it cannot offset other income (salary, investment income, capital gains) in the year it arose.

> Operative text in plain English: *Losses from a non-commercial business activity are deferred until the activity becomes profitable or you meet one of the exception tests in a future year.*

## The $250,000 adjusted taxable income gate — s 35-10(2E)

Before any of the four exception tests can apply, the taxpayer's **adjusted taxable income** for the year must be **less than $250,000**. "Adjusted taxable income" is broader than taxable income — it adds back:

- Reportable fringe benefits
- Reportable superannuation contributions (concessional contributions above the SG)
- Total net investment losses (including negatively geared property and shares)

**If you earn more than $250,000 adjusted, the four tests in 35-30 to 35-45 are simply not available.** Your only path to claiming the loss in-year is the Commissioner's discretion under [[commissioners-discretion-s-35-55|s 35-55]] — and the discretion is granted on much narrower grounds than the objective tests.

This is the single most important provision for high-income earners running a side trading activity: **the test is failed by default at $250k+, regardless of how genuine the trading business is**.

## The four exception tests

If the $250k gate is passed, the taxpayer needs to satisfy any **one** of the following tests to claim the loss in the same year:

| Test | Section | Threshold (indicative) | What it measures | Relevance to traders |
|------|---------|-----------------------|------------------|----------------------|
| **Assessable income** | s 35-30 | ~$20,000 | Assessable income *from the activity* (gross, not profit) | **High** — the workhorse test; any real trading book clears it |
| **Profits (3 of 5 yrs)** | s 35-35 | profit > $0 in 3 of 5 yrs | Pattern of taxable profit | **Medium** — useful for consistently-profitable books with one bad year |
| **Real property** | s 35-40 | ~$500,000 | Real property used exclusively in the activity | **Low** — rare for traders (would need owned commercial premises) |
| **Other assets** | s 35-45 | ~$100,000 | Plant, equipment, IP, software used in the activity | **Low** — possible for HFT/colocated hardware or valued trading software |


### s 35-30 — Assessable income test ($20,000)

The business activity must produce **at least $20,000 of assessable income** in the income year.

For traders, "assessable income from the activity" typically means:

- Gross trading receipts (proceeds from share/derivative disposals) where the trading is on revenue account
- Dividends received on shares held as trading stock
- Interest on cash held for trading
- Premiums received on options written as part of the business

Importantly, the $20,000 is **assessable income**, not profit or net trading gain. A trader with $500,000 of gross trading proceeds and a $50,000 net loss still satisfies s 35-30 because the assessable income comfortably exceeds $20,000.

**This is the most commonly used exception for active traders.** Any meaningful trading book will generate $20k+ of assessable income each year.

### s 35-35 — Profits test (4 of past 5 years)

The business activity must have produced a **taxable profit in at least three of the past five income years (including the current year — so effectively three of the preceding four)**. The profit threshold is just "more than zero" — there is no minimum profit dollar requirement.

This test rewards consistently profitable smaller activities. A trader who books small profits most years but has one bad year can still claim the loss provided the rolling profit pattern is intact.

### s 35-40 — Real property test ($500,000)

The taxpayer must use real property worth **at least $500,000** in carrying on the business activity, where the property is exclusively used for the activity. The threshold is measured by market value or reduced cost base.

Rarely relevant to traders. Could apply if a trading business operates from owned commercial premises worth $500k+ — but this would be unusual.

### s 35-45 — Other assets test ($100,000)

The taxpayer must use other assets (plant and equipment, motor vehicles, IP, trademarks) worth **at least $100,000** in the business activity.

Narrow for pure financial traders — most trading is conducted from a personal laptop with negligible plant. Could be relevant if the business uses expensive proprietary hardware (e.g., a colocated HFT setup) or has built substantial trading software valued as intangible assets.

## What happens if no test is met

The loss is **deferred**, not extinguished. It carries forward indefinitely and is applied against assessable income from the same business activity (or a "similar" activity) in a future year. Practical mechanics:

1. The loss is recorded on the tax return as a deferred non-commercial loss
2. In a future year when the activity has assessable income, the deferred loss is applied against that income first
3. Any unused deferred loss continues to carry forward
4. The loss cannot offset other income (salary, investment income, capital gains) in any year

For a trader who fails Div 35 in a losing year, the practical result is that **a $50k trading loss provides no cash-tax relief that year**. The loss only becomes useful when the trading activity itself returns to profit.

## Interaction with the CGT regime

Division 35 only applies to losses **on revenue account** from a business activity. If the trading activity is on **capital account** (i.e., the trader is held to be an investor under TR 97/11), Division 35 is irrelevant — but the trader also cannot claim the loss against ordinary income. Instead:

- Capital losses are quarantined under s 102-10
- They offset capital gains in the same year first
- Unused capital losses carry forward indefinitely against future capital gains
- They never offset salary, dividends, or interest

This produces the slightly counter-intuitive result that the "better" classification depends on the rest of the taxpayer's situation:

- **Trader who consistently loses money on trading but earns large capital gains elsewhere**: capital treatment is fine — losses absorb the gains
- **Trader who has occasional bad years but otherwise high other income**: business treatment with Div 35 exceptions met (e.g., the $20k assessable income test) is better — losses offset salary
- **Trader with $250k+ income and big trading losses**: neither is great. Capital → loss quarantined to future gains. Business → loss deferred unless Commissioner grants discretion. The trader's structure may need rethinking (see [[smsf-trading-tax-treatment]]).

## Worked examples

### Example 1 — Active trader, $80k salary, $30k trading loss
- Adjusted taxable income: well under $250k → gate passed
- Trading activity assessable income (gross proceeds + dividends): $850,000 → far exceeds $20k → **s 35-30 test met**
- Loss of $30k is deductible against the $80k salary in the year incurred
- Net taxable income: $50k

### Example 2 — High earner, $300k salary, $40k trading loss
- Adjusted taxable income: $300k+ → **gate FAILED**
- No exception test is available regardless of trading volume
- The $40k loss is deferred under s 35-10
- Only path forward: apply for Commissioner's discretion under [[commissioners-discretion-s-35-55|s 35-55]] on "special circumstances" or "lead time" grounds — but neither typically applies to ordinary market-driven losses

### Example 3 — Established trader, occasional bad year
- Adjusted taxable income: under $250k → gate passed
- Trading profits in 3 of last 5 years → **s 35-35 profits test met**
- Even if current-year assessable income falls below $20k, the loss is deductible

### Example 4 — Investor, not a trader
- The activity is on capital account, not a business
- Division 35 does not apply
- Capital losses quarantined to future capital gains under s 102-10
- No deduction against salary in any year

## Decision flowchart

```
Is the activity carried on as a business (TR 97/11)?
├── NO → Capital account; Div 35 irrelevant
│         Losses quarantined to capital gains only
│
└── YES → Did you produce a loss this year?
          ├── NO → No issue
          │
          └── YES → Is your adjusted taxable income < $250k?
                    ├── NO → Loss DEFERRED unless s 35-55 discretion granted
                    │
                    └── YES → Did any of these tests pass?
                              s 35-30: $20k assessable income from activity? OR
                              s 35-35: profits in 3 of last 5 years? OR
                              s 35-40: $500k real property used in activity? OR
                              s 35-45: $100k other assets used in activity?
                              ├── YES → Loss DEDUCTIBLE this year against any income
                              └── NO → Loss DEFERRED unless s 35-55 discretion granted
```

## Risk-management implications for traders

Division 35 is itself a risk-management problem:

1. **Plan loss recognition around the $250k gate.** A trader oscillating around the threshold should consider timing of bonus income, super contributions, and investment loss realisation in years they expect trading losses.
2. **Document the assessable income carefully.** The s 35-30 test relies on assessable income from the activity. Keep clean records of gross trading proceeds, dividends, and other receipts.
3. **Consider entity choice.** Companies and SMSFs are not subject to Div 35. A trader with consistent losses in early years may prefer a corporate or [[smsf|SMSF]] structure to avoid the deferral — but each has its own tradeoffs (no CGT discount in companies; preservation in super). See [[smsf-trading-tax-treatment]].
4. **The discretion is not a backstop.** [[commissioners-discretion-s-35-55|s 35-55]] is granted on narrow grounds. A bad trading year from ordinary market movement is unlikely to qualify.

## Common pitfalls

| Pitfall | Why it bites |
|---------|-------------|
| **Assuming a loss always offsets salary** | Div 35 can *defer* it; for high earners the $250k gate blocks the four tests entirely |
| **Confusing assessable income with profit (s 35-30)** | The ~$20k test is on *gross assessable income from the activity*, not net trading gain — easy to under-count |
| **Forgetting the income gate is "adjusted"** | Reportable super, FBT, and net investment losses are *added back*, pushing borderline earners over ~$250k |
| **Treating capital-account losses as Div 35** | If you are an *investor* not a trader (TR 97/11), Div 35 is irrelevant — losses are quarantined to capital gains (s 102-10) |
| **Banking on Commissioner's discretion** | s 35-55 is narrow; ordinary market losses rarely qualify on "special circumstances" or "lead time" grounds |
| **Poor records** | The s 35-30 test depends on documented gross proceeds, dividends, and other receipts from the activity |
| **Picking an entity for tax alone** | Companies/SMSFs sidestep Div 35 but lose the [[capital-gains-tax-discount|CGT discount]] / face preservation rules — see [[smsf-trading-tax-treatment]] |

## Source notes

Written from the public text of ITAA 1997 Division 35, ATO public guidance materials, and standard Australian tax-practice references. Section numbers and the $250,000 / $20,000 / $500,000 / $100,000 thresholds are stated as in the current Act. **Confirm current law and dollar thresholds via the Commonwealth Federal Register of Legislation or a registered tax agent before relying on this.**

## Related

- [[tr-97-11-carrying-on-a-business]] — the threshold "business" test
- [[trader-vs-investor-classification-au]] — practical classification guide
- [[commissioners-discretion-s-35-55]] — the escape hatch
- [[pcg-2021-2-div-35-discretion]] — how the Commissioner actually grants discretion
- [[itaa-1997-overview]] — broader ITAA index
- [[smsf-trading-tax-treatment]] — SMSF alternative
- [[australian-investor-tax]] — broader tax context
- [[capital-gains-tax-discount]] — the alternative regime
