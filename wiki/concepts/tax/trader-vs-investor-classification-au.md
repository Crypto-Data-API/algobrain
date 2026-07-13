---
title: "Trader vs Investor Classification (Australia)"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [regulation, risk-management, portfolio-theory]
aliases: ["Share Trader vs Share Investor", "Business vs Investment Classification", "Revenue vs Capital Account"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[tr-97-11-carrying-on-a-business]]", "[[australian-investor-tax]]"]
related:
  - "[[tr-97-11-carrying-on-a-business]]"
  - "[[non-commercial-losses-div-35]]"
  - "[[commissioners-discretion-s-35-55]]"
  - "[[itaa-1997-overview]]"
  - "[[smsf-trading-tax-treatment]]"
  - "[[australian-investor-tax]]"
  - "[[capital-gains-tax-discount]]"
---

> **Not tax or financial advice.** Classification is fact-sensitive, consequential, and turns on evolving case law and ATO practice. The tax rates, income gates and trade-count thresholds below are **indicative only** — the [[tr-97-11-carrying-on-a-business|TR 97/11]] indicators are weighed in the round, and current rates/thresholds must be checked against the ATO. Confirm with a registered tax agent or specialist tax lawyer (and consider a binding private ruling) before structuring around either treatment.

For Australian residents trading shares, options, or derivatives, the threshold tax question is whether the activity is a **business** (revenue account) or **investment** (capital account). The classification is determined by the indicators in [[tr-97-11-carrying-on-a-business|TR 97/11]] — not by self-label — and it cascades through every downstream tax treatment: how gains are taxed, how losses are deducted, what expenses qualify, whether [[non-commercial-losses-div-35|Division 35]] applies, and whether the [[capital-gains-tax-discount|50% CGT discount]] is available. This page is the practical bridge between the legal test and the real-world decision.

## The cascade

```
Carrying on a business per TR 97/11?
├── YES → REVENUE ACCOUNT (share trader)
│         ├── Gains: ordinary income (s 6-5), no CGT discount
│         ├── Losses: deductible (s 8-1), subject to Div 35
│         ├── Brokerage: immediately deductible
│         ├── Margin interest: deductible
│         ├── Data/software: deductible
│         └── Treated as trading stock (Div 70) OR ordinary income
│
└── NO  → CAPITAL ACCOUNT (share investor)
          ├── Gains: CGT regime, 50% discount if held >12 months
          ├── Losses: quarantined to capital gains, carried forward
          ├── Brokerage: added to cost base / reduces proceeds
          ├── Margin interest: deductible if income expectation
          ├── Data/software: generally not deductible
          └── No Div 35 issues — but no immediate loss relief either
```

## At-a-glance: which treatment helps when

| | Share trader (business / revenue) | Share investor (capital) |
|---|---|---|
| **Gains** | Ordinary income at marginal rate; no discount | [[capital-gains-tax-discount\|50% CGT discount]] if held >12 months |
| **Losses** | Deductible vs other income *if* [[non-commercial-losses-div-35\|Div 35]] satisfied | Quarantined to capital gains, carried forward |
| **Brokerage** | Immediately deductible | Added to cost base |
| **Margin interest** | Deductible | Deductible if income expectation |
| **Data / software / education** | Deductible | Generally not |
| **Best in a winning year** | ✗ (loses the discount) | ✓ |
| **Best in a losing year** | ✓ (if Div 35 gate passed) | ✗ |
| **Asset character** | Trading stock (Div 70) / revenue | CGT asset (Div 100–115) |

The catch: **you cannot choose year-by-year** — see [The asymmetry problem](#the-asymmetry-problem).

## Side-by-side: same trade, two regimes

> Dollar figures below are **illustrative** at assumed marginal rates; confirm current brackets, the Medicare levy, and any surcharge with the ATO.

Assume a trader buys 1,000 NVDA at A$400 (cost A$400,000) and sells 14 months later at A$600 (proceeds A$600,000). Marginal tax rate assumed at the top bracket plus Medicare.

| Item | Share trader (business) | Share investor (capital) |
|---|---|---|
| Holding period | 14 months | 14 months |
| Gross gain | $200,000 | $200,000 |
| Eligible for 50% CGT discount? | No | Yes |
| Taxable amount | $200,000 | $100,000 |
| Tax (47%) | $94,000 | $47,000 |
| **After-tax gain** | **$106,000** | **$153,000** |

In a **winning year**, the investor treatment is dramatically better because of the CGT discount.

Now flip it — a $200k loss instead of a gain, and assume the trader has $250k of salary income:

| Item | Share trader (business) | Share investor (capital) |
|---|---|---|
| Gross loss | $200,000 | $200,000 |
| Offset against salary? | Yes IF Div 35 test met | No |
| If $250k income gate failed | Loss DEFERRED | Quarantined to future capital gains |
| Best-case immediate tax saving | $94,000 (47% × $200k) | $0 |
| Worst-case immediate tax saving | $0 (loss deferred) | $0 |

In a **losing year**, business treatment can be much better — *if* you pass the Division 35 hurdles. Above the $250k income gate, neither classification provides immediate relief.

## The asymmetry problem

The asymmetry above is the core issue:

- **Winners**: investor classification is better (50% CGT discount)
- **Losers**: trader classification is better (immediate loss deduction)
- **Mixed years**: depends on netting

But the taxpayer **cannot pick year-by-year**. The classification follows the facts of the activity over time. Switching classification requires either:

- A genuine change in the way the activity is conducted (e.g., scaling up from occasional to systematic trading)
- A new activity with materially different facts (e.g., starting a separate derivatives business)
- Acceptance that prior years may be reclassified on audit

The ATO is alert to taxpayers attempting to **characterise losses as revenue and gains as capital** in the same activity. Consistency is enforced.

## How the ATO assesses in practice

The Commissioner's view is set out in TR 97/11 and a series of public rulings and ATO ID statements on share trading. Empirically, the weighting of the eight indicators in share trading cases tends to be:

1. **Volume and frequency of trades** — most decisive single factor
2. **Profit-seeking intent with rational basis** — close second
3. **Businesslike organisation** — records, processes, systems
4. **Manner of operation** — professional infrastructure
5. **Size and permanency** — capital + duration
6. **Repetition** — sustained, not flash-in-the-pan
7. **Commercial character** — supportable as a real enterprise
8. **Not a hobby** — negative test

A trader showing 500+ trades per year, with documented strategies, separate accounts, and material capital at risk, will typically be classified as carrying on a business. A buy-and-hold investor making 10–50 trades per year will typically be on capital account.

## Empirical thresholds (caution: not law)

Although there is no bright line, ATO private rulings and AAT decisions have clustered around the following observed patterns. **These are illustrative — not binding** — and the indicators are still weighed in the round:

| Factor | Typically investor | Borderline | Typically trader |
|---|---|---|---|
| Trades per year | < 50 | 50–200 | 200+ |
| Average holding period | > 6 months | 1–6 months | < 1 month |
| Capital at risk | < $50k | $50k–$200k | $200k+ |
| Hours per week | < 5 | 5–20 | 20+ |
| Written trading plan | No | Partial | Yes |
| Separate trading entity/account | No | Maybe | Yes |
| Use of leverage / derivatives | Rare | Some | Frequent |

A trader heavily skewed to the right column on most rows will satisfy TR 97/11. One heavily skewed to the left will not. The middle column is where most contested cases sit.

## Common scenarios

### Active stock picker, full-time, day-trading futures and options
**Almost certainly a business.** High volume, systematic, full-time, professional infrastructure. Revenue account.

### Software engineer with $250k salary, swing-trading 100 stocks/year on the side
**Grey.** Volume is moderate; profit motive is real; business-like records exist. **Practical issue:** the $250k income gate in [[non-commercial-losses-div-35|s 35-10(2E)]] means business classification provides no immediate loss relief in a losing year. Capital treatment with the 50% CGT discount may be more tax-efficient overall.

### Retiree managing $1M SMSF with monthly rebalancing
**Investment in SMSF.** The [[smsf|SMSF]] is not subject to Division 35 anyway (super funds have their own loss rules), and the asset is held to support retirement income. Capital account treatment. See [[smsf-trading-tax-treatment]].

### Options-premium seller writing covered calls monthly
**Often capital account if the underlying shares are held long-term and calls are written for incremental income.** The premium income is assessable under s 6-5 either way, but the question of whether the entire activity is a business is harder. Sustained, systematic writing across multiple instruments and significant time commitment moves toward business.

### Crypto trader, 24/7 active across multiple chains and protocols
**Same TR 97/11 test applies.** High frequency, systematic, profit-seeking → business. The CGT rules apply differently to crypto in some respects (e.g., personal-use asset exemption is narrow), but the trader/investor distinction operates the same way.

## Structural alternatives

If the natural classification is problematic for a given trader, structure can change the regime:

| Structure | Regime | Pros | Cons |
|---|---|---|---|
| **Individual on capital account** | CGT | 50% CGT discount; no Div 35 | Losses quarantined to gains |
| **Individual on revenue account** | Ordinary income | Losses offset salary (if Div 35 satisfied) | No CGT discount; $250k gate |
| **Company** | Company tax (25%/30%) | No Div 35; flat rate; corporate veil | No CGT discount; double tax on dividends; ATO PSI rules |
| **Discretionary trust** | Beneficiary's rate | Income splitting; CGT discount flows through | Complex; trust losses trapped; Div 35 by attribution |
| **[[smsf|SMSF]]** | Super fund (15% acc / 0% pension) | Massive long-term tax efficiency | Preservation; sole purpose test; no immediate access |

Each structure has its own version of the trader/investor question and its own loss-treatment rules. See [[smsf-trading-tax-treatment]] for the SMSF case.

## Practical advice for borderline traders

1. **Decide which regime you want, then build the facts.** If you want business treatment, document systematically from day one (plan, journal, records, time logs). If you want investment treatment, do not adopt business-like behaviour without reason.
2. **Mind the $250k income gate.** For high earners, business classification provides no immediate loss relief unless the Commissioner grants discretion under [[commissioners-discretion-s-35-55|s 35-55]]. The CGT regime may be better as a default.
3. **Consider an entity.** A company or SMSF eliminates Division 35. Each has tradeoffs.
4. **Get a private ruling for material classifications.** The ATO will provide a binding private ruling on your specific facts. Worth the cost for traders with significant capital.
5. **Be consistent.** Switching classification opportunistically invites audit and reclassification with penalties.

## Common pitfalls

- **Self-labelling.** Writing "share trader" on the return does not make you one — classification follows the [[tr-97-11-carrying-on-a-business|TR 97/11]] facts. The reverse trap is also real: years of business-like conduct cannot be re-cast as "capital" just because the year was a winner.
- **Forgetting the $250k income gate.** High earners on revenue account get *no* immediate loss relief unless the [[commissioners-discretion-s-35-55|Commissioner's discretion]] applies — so business treatment can be worse than capital even in a loss year. See [[non-commercial-losses-div-35]].
- **Assuming a company "fixes" tax.** A [[company|company]] removes Division 35 and offers a flat rate, but it *forfeits* the 50% CGT discount and can trigger double tax on distributed profits.
- **Mixing accounts.** Holding investment parcels and a trading business in one undifferentiated account makes it hard to defend a split treatment on audit — keep them genuinely separate if you intend to run both.
- **Crypto over-confidence.** The same TR 97/11 test applies to [[cryptocurrency-tax-australia|crypto]]; the personal-use-asset exemption is narrow and rarely saves an active trader.
- **No contemporaneous records.** Records built after an audit notice carry far less weight than a real-time plan, journal and reconciled P&L.

## Sources

Written from the public text of TR 97/11, ITAA 1997, ATO guidance materials, and Australian case law on share trading classification. Empirical threshold patterns are derived from publicly available AAT decisions and private rulings — **they are illustrative and not legally binding**. Confirm with a registered tax agent before structuring around any classification.

- ATO, *Taxation Ruling TR 97/11* — the indicators test underlying classification. https://www.ato.gov.au/law/view/document?docid=TXR/TR9711/NAT/ATO/00001
- ATO, *Shareholding as investor or share trading as business?* — the Commissioner's published distinction and worked factors. https://www.ato.gov.au/individuals-and-families/investments-and-assets/investing-in-shares
- *Income Tax Assessment Act 1997* (Cth) — s 6-5 (ordinary income), s 8-1 (general deductions), Div 35 (non-commercial losses, incl. the s 35-10(2E) $250k income gate), Div 70 (trading stock), Div 115 (50% CGT discount). https://www.legislation.gov.au/Details/C2023C00104
- ATO, *Non-commercial business losses* and the *s 35-55 Commissioner's discretion* guidance — relevant to revenue-side loss treatment.
- Administrative Appeals Tribunal / AAT share-trading decisions and ATO private rulings — basis for the illustrative threshold table (non-binding).

## Related

- [[tr-97-11-carrying-on-a-business]] — the indicators test
- [[non-commercial-losses-div-35]] — what applies in revenue regime
- [[commissioners-discretion-s-35-55]] — escape hatch for revenue-side losses
- [[itaa-1997-overview]] — broader index
- [[smsf-trading-tax-treatment]] — SMSF structure
- [[australian-investor-tax]] — broader tax framework
- [[capital-gains-tax-discount]] — the 50% discount on capital account
- [[cryptocurrency-tax-australia]] — same test applied to crypto
- [[smsf]] — fund structure outside Division 35
