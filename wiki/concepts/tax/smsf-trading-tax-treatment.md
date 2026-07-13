---
title: "SMSF Trading Tax Treatment"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [australia, tax, smsf, retirement, regulation]
aliases: ["SMSF Tax Treatment of Trading", "Self-Managed Super Fund Trading Tax", "SMSF Trading Income Tax"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: advanced
prerequisites: ["[[smsf]]", "[[non-commercial-losses-div-35]]", "[[australian-investor-tax]]"]
related:
  - "[[smsf]]"
  - "[[non-commercial-losses-div-35]]"
  - "[[tr-97-11-carrying-on-a-business]]"
  - "[[trader-vs-investor-classification-au]]"
  - "[[itaa-1997-overview]]"
  - "[[australian-investor-tax]]"
  - "[[capital-gains-tax-discount]]"
---

> **Not tax or financial advice.** SMSF tax treatment intersects superannuation law (the SIS Act), the ITAA, and ATO administrative practice. Every rate, cap, and threshold below is **indicative** and indexed/amended frequently. SMSF compliance is closely monitored by the ATO (the regulator of SMSFs — see [[australian-regulatory-framework]]). Confirm any structural decision with a registered tax agent and an approved SMSF auditor, and check current figures at ato.gov.au before relying on them.

A Self-Managed Super Fund ([[smsf|SMSF]]) is taxed under a substantially different regime from individuals trading on their own account. The Superannuation Industry (Supervision) Act 1993 (SIS Act) governs the fund's compliance status; the ITAA 1936/1997 governs taxation. The two combine to produce a regime that is dramatically more tax-efficient than individual trading in accumulation phase, even more so in pension phase, but that imposes structural constraints (preservation, sole purpose test, in-house asset limit) that don't exist outside super. Critically for traders: **[[non-commercial-losses-div-35|Division 35]] does not apply to SMSFs**, but the sole-purpose test and the prohibition on "running a business inside super" introduce a different set of issues.

## Headline rates

| Phase | Tax on ordinary income | Tax on net capital gains (>12 months) | Tax on franked dividends |
|---|---|---|---|
| **Accumulation** | 15% | 10% (after 33.33% CGT discount) | Effectively 0% (franking credits offset 15%) |
| **Pension (account-based)** | 0% | 0% | Full franking credit refund |

Compare to an individual at the top marginal rate (47% incl. Medicare):

- A fully franked dividend at top marginal individual: ~24.5% effective
- Same dividend in SMSF accumulation: ~0% effective (or modest refund)
- Same dividend in SMSF pension: cash refund of franking credit

This is why so much SMSF allocation goes to high-yielding, fully franked Australian shares (franking-credits).

## Trading vs investing — the SMSF-specific question

The threshold question for individuals — am I trading or investing? ([[trader-vs-investor-classification-au]]) — has a different answer in the SMSF context because of the **sole purpose test** and the ATO's settled position on SMSFs running businesses.

### Sole purpose test (SIS Act s 62)

An SMSF must be maintained **solely** for providing retirement benefits to members (or death benefits to dependants). Activities that are not consistent with the sole purpose test breach SIS s 62 and can render the fund non-complying — which triggers a 45% tax rate on the entire taxable income of the fund. Catastrophic.

The ATO's position is that an SMSF **can hold investments** (including actively managed portfolios) without breaching s 62, but **cannot operate a business** where the business activity is the dominant purpose. The line is fact-sensitive.

### When trading inside an SMSF becomes "carrying on a business"

The same TR 97/11 indicators apply — but the consequences are different and the regulatory overlay is harder. Indicators of business trading in an SMSF context:

- Very high frequency (day trading, scalping)
- Trading is the predominant activity of the fund
- Use of margin, derivatives, short-selling at scale
- Trading objectives that are not consistent with the long-term retirement-benefit purpose

The ATO's practical view: **SMSFs can be active investors but should not operate as trading businesses.** SMSFs found to be running a trading business may face:

- Sole purpose test concerns
- Non-arm's-length income (NALI) issues if any related-party dealing exists
- GST registration requirements above the trading turnover threshold ($75k)
- ATO compliance audit

For most SMSF members, the correct approach is to be an **active investor** — make trading decisions, rebalance, use options for income — without crossing into "business" territory.

### Revenue account vs capital account inside the fund

Independent of the sole-purpose question, the ATO still characterises each gain as either *revenue* (ordinary income, no CGT discount) or *capital* (eligible for the 33.33% SMSF discount on assets held ≥12 months). The same [[tr-97-11-carrying-on-a-business|TR 97/11]] business indicators and the s 6-5 / s 102-5 distinction apply. The stakes are different from an individual because the *rate* is lower, but the discount still matters:

| Characterisation | Treatment in accumulation SMSF | Effective rate (LTCG) |
|---|---|---|
| **Capital account, held ≥12 months** | 33.33% discount applies | ~10% |
| **Capital account, held <12 months** | No discount | 15% |
| **Revenue account (trading stock / business)** | Ordinary income, no discount; assets are trading stock valued at year-end | 15% |

In pension phase the rate is 0% either way, so the revenue/capital question is largely moot there — another reason high-turnover activity, if any, is least costly when run on the pension-phase side of a fund (subject always to the sole-purpose test).

## Division 35 does not apply to SMSFs

Section 35-5 of the ITAA 1997 limits Division 35 to "individuals" (and partnerships including individuals). SMSFs are taxed as separate taxable entities (s 295-5) and are not "individuals." Consequently:

- The $250,000 income gate is **irrelevant** in an SMSF
- The four exception tests are **irrelevant**
- Trading losses inside an SMSF are dealt with under the **super-fund-specific loss rules**, not Division 35

This is one of the most underappreciated reasons traders use SMSFs: **the Division 35 deferral problem disappears**.

## SMSF loss treatment

Trading losses inside an SMSF are treated as follows:

| Loss type | Treatment |
|---|---|
| **Revenue losses** (if trading on revenue account) | Offset against assessable income of the fund; excess carried forward indefinitely under Div 36 |
| **Capital losses** | Offset against capital gains of the fund; excess carried forward indefinitely against future capital gains |
| **Loss conversion** | An SMSF in accumulation has 15% rate, so loss tax-shield is 15c per dollar — far less than the 47c shield available to an individual at top marginal |

The trade-off: SMSF loss recognition is automatic (no Div 35 deferral), but the **loss shield value is lower** (15% rate vs up to 47% individual rate). For consistently profitable traders this is irrelevant; for traders with frequent losses against a high-income individual return, individual treatment can extract more tax value per loss dollar — if Div 35 is satisfied.

## CGT discount inside SMSFs

The SMSF CGT discount is **33.33%** (one-third) rather than 50% for individuals.

| Holding period | Individual taxable gain | SMSF taxable gain |
|---|---|---|
| < 12 months | 100% (full marginal rate) | 100% (15% / 0%) |
| ≥ 12 months | 50% (full marginal rate) | 66.67% (15% / 0%) |

Practical impact: a fully discounted long-term capital gain in an SMSF in **accumulation phase** is taxed at 15% × 66.67% = **10% effective rate**. In **pension phase**: 0%.

For a marginal-rate-47% individual, the same long-term gain is taxed at 47% × 50% = **23.5% effective rate**.

An SMSF in accumulation pays less than half the CGT rate of a top-bracket individual, and an SMSF in pension pays nothing.

## Franking credits — the killer feature

SMSFs are major beneficiaries of Australia's full-refund franking credit regime.

### Accumulation phase
Fully franked dividend → fund receives the cash dividend + franking credit attached. The franking credit (corporate tax already paid at 30%) offsets the SMSF's 15% tax liability. The result is typically a **net refund** to the fund. Example:

- $100 fully franked dividend
- Attached franking credit: $42.86 (gross-up to $142.86 grossed-up income)
- Fund tax at 15% on $142.86 = $21.43
- Less franking credit of $42.86 = **refund of $21.43**

### Pension phase
Same dividend + franking credit. Fund tax rate is 0%. **Full $42.86 franking credit refunded in cash**. Net cash to fund: $142.86 on a $100 dividend.

This is the foundation of the "high-yield fully franked Australian shares" portfolio that dominates SMSF allocation patterns. See franking-credits and the [[smsf]] page.

## Transfer balance cap and contributions

The amount that can sit in pension phase is capped — currently around **$1.9 million per person** (the "transfer balance cap"; indexed). Amounts above the cap stay in accumulation phase and continue to be taxed at 15%. For wealthy SMSFs the cap is the binding constraint on how much income can be tax-free.

Contribution caps (separate issue) limit how much new money can be put in:

- **Concessional contributions** (deductible employer / personal): $30,000/yr (2024–25)
- **Non-concessional contributions** (after-tax): $120,000/yr, with bring-forward to $360,000 over 3 years
- **Total Super Balance** cap at $1.9m disables non-concessional contributions

## Practical structuring for traders

### When SMSF trading makes sense

- The trader has substantial existing super balance ($300k+) to make the structure cost-effective
- The trading strategy is suitable for retirement-purpose investing (medium-to-long horizon, risk-controlled)
- The trader can accept preservation (no access until preservation age, normally 60)
- The activity will not run afoul of the sole purpose test (i.e., active investor, not trading business)
- Tax savings on gains exceed the structural costs

### When SMSF trading does not make sense

- Active day-trading or high-frequency strategies (sole purpose risk; ATO scrutiny)
- Trader needs current-year loss relief against high salary (Div 35 wouldn't apply but losses are wasted at SMSF's lower rate)
- Balance too small to support structural costs ($2.5–5k/yr)
- Trader needs liquidity before preservation age

### Hybrid structures

Some traders run two layers:

- **Individual account**: active trading, derivatives, leverage — accept the [[non-commercial-losses-div-35|Div 35]] complications, target capital-account treatment with [[capital-gains-tax-discount|50% CGT discount]] on long holds
- **SMSF**: passive ETF + dividend portfolio + occasional rebalancing — capture franking credit refunds, 0% pension-phase rate

This separates the high-tax-shield need (individual) from the long-term compounding need (SMSF).

## Compliance traps to avoid

| Trap | Consequence |
|---|---|
| **Sole purpose test breach** | Non-complying fund → 45% tax on entire balance |
| **Non-arm's-length income (NALI)** | Income taxed at 45% inside the fund |
| **In-house asset limit (5%)** | Excess assets must be disposed of |
| **Lending to members** | Prohibited; severe penalties |
| **Personal use of fund assets** | Sole purpose breach |
| **Inadequate investment strategy documentation** | Trustee penalties |
| **Margin loans without LRBA structure** | SIS Act borrowing rules breached |

The high effective penalty regime is why SMSFs require professional administration and annual audit.

### Non-arm's-length income (NALI) — the trader's hidden landmine

NALI is the single most relevant penalty regime for an active SMSF trader, because it can be triggered without any deliberate wrongdoing. Income is NALI (taxed at the top rate, ~45%, inside the fund) where the fund earns more than it would have on arm's-length terms, or incurs *less* expense than arm's-length. For a trading SMSF the common triggers are:

| NALI trigger | How it arises for a trader | Mitigation |
|---|---|---|
| **Below-market services** | A member who is a professional trader manages the fund's portfolio for free using their employer's tools/research | Charge an arm's-length fee, or use only general (non-employment) skills |
| **Related-party transactions** | Buying assets from, or selling to, a related entity off-market | Transact only on-market at market prices |
| **Non-commercial financing** | An LRBA (limited recourse borrowing) on better-than-commercial terms | Use a commercial-rate, properly documented LRBA |
| **General-expense shortfall** | The fund pays nothing for services that would normally cost money | Pay arm's-length expenses or rely on the *general nature* exemptions where available |

The consequence is severe and disproportionate: a small non-arm's-length input can taint a large stream of income at 45%. This is why active members are usually advised to keep their personal trading edge in their *individual* account and run the SMSF on plain-vanilla, on-market, arm's-length terms.

## Structural-cost and suitability decision aid

A rough decision aid (not advice). The SMSF tax advantages only pay off above a balance where fixed annual costs (setup, audit, administration, actuarial certificate in some cases) are a small fraction of returns.

| Factor | Points toward SMSF | Points away from SMSF |
|---|---|---|
| Existing super balance | Larger (so fixed costs are a small % drag) | Small (fixed costs dominate) |
| Trading frequency | Low-to-moderate (active investor) | Very high (sole-purpose / NALI / business risk) |
| Need for current-year loss relief vs salary | None (profitable) | High (losses worth more at individual ~47% shield) |
| Time horizon | Long (retirement) | Short (need liquidity before preservation age) |
| Income type | High franked-dividend yield (franking refund) | Mostly capital gains realised short-term |
| Willingness to run admin + annual audit | High | Low |

## Comparison summary

| Feature | Individual (revenue) | Individual (capital) | SMSF (accumulation) | SMSF (pension) |
|---|---|---|---|---|
| Gain tax rate | Up to 47% | Up to 47% × 50% = 23.5% | 15% (10% on LTCG) | 0% |
| Loss treatment | Div 35 applies | Quarantined to capital gains | Carried forward at 15% shield | Carried forward |
| Franking credits | Offset tax; refund if surplus | Same | Offset + refund | Full cash refund |
| Liquidity / access | Immediate | Immediate | Preserved | Preserved (but pension drawn) |
| Compliance burden | Tax return | Tax return | Audit + SAR | Audit + SAR + pension reporting |
| Suitable for active trading | Yes | Partial | Risky (sole purpose) | Risky (sole purpose) |
| Suitable for buy-and-hold | OK | Best | Best | Best |

## Source notes

Written from the public text of the ITAA 1997, ITAA 1936, SIS Act 1993, ATO public guidance on SMSFs, and standard Australian super-fund taxation references. Rates, caps, and thresholds are stated as at FY 2024–25 / 2025–26. **Confirm current law and indexation before relying on any threshold.**

## Related

- [[smsf]] — the SMSF structure overview
- [[non-commercial-losses-div-35]] — Division 35 (does NOT apply in SMSF)
- [[tr-97-11-carrying-on-a-business]] — the carrying-on-a-business test
- [[trader-vs-investor-classification-au]] — individual classification analysis
- [[itaa-1997-overview]] — broader index
- [[australian-investor-tax]] — broader tax framework
- [[capital-gains-tax-discount]] — CGT discount mechanics
- [[australian-regulatory-framework]] — where the ATO sits as SMSF regulator
- [[asic]] — conduct regulator (relevant if the SMSF holds AFSL-regulated products)
- [[risk-management]] — sizing and preservation constraints inside super
