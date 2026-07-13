---
title: "TR 97/11 — Indicators of Carrying On a Business"
type: concept
created: 2026-05-30
updated: 2026-06-21
status: excellent
tags: [regulation, risk-management, education]
aliases: ["TR 97/11", "Tax Ruling 97/11", "Carrying On a Business Test", "Eight Indicators Test"]
jurisdiction: AU
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[australian-investor-tax]]"]
related:
  - "[[non-commercial-losses-div-35]]"
  - "[[trader-vs-investor-classification-au]]"
  - "[[itaa-1997-overview]]"
  - "[[commissioners-discretion-s-35-55]]"
  - "[[australian-investor-tax]]"
---

> **Not tax or financial advice.** TR 97/11 is a public ATO ruling; how the indicators apply to any specific taxpayer is fact-specific, and the case law evolves. Nothing here is a substitute for advice on your own facts — confirm classification with the ATO (a binding private ruling is available) or a registered tax agent before relying on any treatment. Any rates, thresholds or trade-count figures below are **indicative** and weighed in the round, not bright-line tests.

Taxation Ruling **TR 97/11** is the ATO's canonical statement of the indicators that distinguish a "business" from a hobby or investment activity. Although TR 97/11 itself addresses the question in the context of primary production, the **eight indicators** it codifies have become the standard test applied across all activities — including share and derivative trading. For traders, TR 97/11 is the gateway question: if you are carrying on a business, your trading is on revenue account (assessable under s 6-5, deductible under s 8-1, subject to [[non-commercial-losses-div-35|Division 35]]); if you are not, you are an investor on capital account and the CGT regime applies. See [[trader-vs-investor-classification-au]] for the practical decision and [[australian-investor-tax]] for the broader framework.

## Where this question sits

TR 97/11 is the *first fork* in the Australian trading-tax decision tree. Everything downstream — the [[capital-gains-tax-discount|50% CGT discount]], loss treatment, deductibility of [[margin|margin]] interest and data feeds, whether [[non-commercial-losses-div-35|Division 35]] bites — hangs on which branch you take:

```
                    Your trading activity
                            │
            ┌───────────────┴───────────────┐
     TR 97/11 indicators              TR 97/11 indicators
     satisfied (in the round)         NOT satisfied
            │                               │
   "Carrying on a business"        "Mere realisation /
   = SHARE TRADER                   investment"
   = REVENUE ACCOUNT                = SHARE INVESTOR
            │                       = CAPITAL ACCOUNT
            │                               │
   s 6-5 income, s 8-1            CGT regime, Div 115
   deductions, Div 70            50% discount if >12mo
   trading stock, Div 35         held; losses quarantined
```

The test is **objective and fact-driven**: it looks at what you actually did, not what you call yourself (see [The "self-label" trap](#the-self-label-trap)). The same person can hold *some* parcels as an investor (capital account) and run a *separate* trading business (revenue account) if the two activities are genuinely distinct in conduct and record-keeping — but the ATO scrutinises this closely.

## Why TR 97/11 matters

The same trading activity produces wildly different tax outcomes depending on which side of the TR 97/11 line it falls:

| Aspect | Business (revenue account) | Investment (capital account) |
|---|---|---|
| **Gains** | Ordinary income at marginal rate | CGT regime with [[capital-gains-tax-discount|50% discount]] if held >12mo |
| **Losses** | Deductible against any income (subject to Div 35) | Quarantined to capital gains only |
| **Brokerage** | Immediately deductible | Added to cost base |
| **Interest on margin loans** | Deductible | Deductible only if expectation of dividends/income |
| **Software & data subscriptions** | Deductible | Generally not deductible |
| **Home office costs** | Deductible if used for the activity | Limited |
| **GST registration** | May be required | No |

The "right" classification depends on the trader's own facts and on what mix of gains/losses they expect — but the ATO will not be moved by a self-label. The classification follows the indicators, applied to the activity in the round.

## The eight indicators (TR 97/11 ¶ 13)

The ruling lists indicators drawn from case law (especially *Ferguson v FC of T* (1979) 79 ATC 4261, *Martin v FC of T* (1953) 90 CLR 470, and *FC of T v Radnor Pty Ltd* (1991) 91 ATC 4689). The indicators are **weighed in the round**, not used as a checklist — no single factor is decisive.

### 1. Whether the activity has a significant commercial purpose or character

The activity must have the **scale, nature and continuity** of a commercial undertaking. Casual or sporadic share trading typically fails; full-time, methodical trading with profit motivation typically passes.

**Trader-relevant tests:**
- Volume of capital at risk
- Time devoted to the activity
- Documentation of trading strategies, risk frameworks, and process
- Engagement with professional infrastructure (real-time data, trading platforms beyond a basic broker app)

### 2. Whether the taxpayer has more than just an intention to engage in business

Mere intent does not establish a business. There must be **activity** — actual trades executed, processes followed, decisions taken. Plans and study without operational activity fail.

**Trader-relevant tests:**
- Trade frequency
- Hours actively engaged
- Operational evidence (broker statements, trade journals, P&L tracking)

### 3. Whether the taxpayer has a purpose of profit as well as a prospect of profit

The trader must intend to make a profit **and** have a realistic prospect of doing so. Pure speculation with no rational basis fails on the second limb; intent alone fails on the first.

**Trader-relevant tests:**
- Documented strategy with positive expected value
- Risk management framework
- Backtesting or empirical basis for the approach
- Evidence the trader treats the activity as a profit-seeking enterprise, not entertainment

### 4. Whether there is repetition and regularity of the activity

This indicator carries significant weight in trading cases. **High-frequency, repeated trading** is a strong business indicator; occasional rebalancing or buy-and-hold is not.

**Trader-relevant tests:**
- Number of trades per month/year
- Average holding period
- Consistency of activity across the year (or seasonal but systematic)

The ATO has historically pointed to **hundreds of trades per year** as suggestive of business; occasional disposals (e.g., once per quarter) generally suggest investment. There is no bright-line number, but volume is one of the most cited factors in private rulings.

### 5. Whether the activity is of the same kind and carried on in a similar manner to that of ordinary trade in that line of business

The activity should be conducted in a manner **similar to how an established commercial trader operates**.

**Trader-relevant tests:**
- Use of professional broker accounts, prime brokerage, or institutional infrastructure
- Risk management aligned with market practice (position sizing, stop-losses, hedging)
- Treatment of trading as the primary or substantial activity, not casual
- Use of margin facilities, derivatives, short-selling — typical of professional trading

### 6. Whether the activity is planned, organised and carried on in a businesslike manner such that it is directed at making a profit

Distinguishes a structured operation from haphazard activity.

**Trader-relevant tests:**
- Documented trading plan with entry/exit rules
- Records and accounts (separate trading bank account, tracked P&L, journal)
- Systematic review processes
- Use of trading software, backtesting tools, or analytical frameworks
- Business structures (sole trader registration, ABN, possibly company)

### 7. The size, scale and permanency of the activity

Larger and more permanent activities are more readily characterised as business. Small, transient activities suggest hobby or investment.

**Trader-relevant tests:**
- Capital deployed
- Frequency over multiple years
- Continuity of approach (not a flash-in-the-pan year)
- Whether the activity could realistically support the trader financially

### 8. Whether the activity is better described as a hobby, a form of recreation or a sporting activity

The negative indicator. Activities pursued for personal enjoyment without rigour are excluded.

**Trader-relevant tests:**
- Whether the trader treats wins/losses as serious financial outcomes
- Whether the activity is conducted with discipline rather than for entertainment
- Whether there is real opportunity cost (e.g., the trader has reduced other paid work)

## How the indicators are weighed in trading cases

In practice, the strongest indicators for share trading specifically are:

1. **Volume and frequency** (#4, #7) — the single most-cited factor in tribunal decisions
2. **Profit purpose with rational basis** (#3) — documented strategy, not hope
3. **Businesslike organisation** (#6) — records, processes, systems
4. **Manner of operation** (#5) — professional infrastructure

A trader executing 500+ trades per year, with documented strategies, separate accounts, systematic risk management, and meaningful time commitment, will satisfy TR 97/11 in most cases. A trader executing 20 trades per year with a buy-and-hold-ish bias will not. (These trade counts are **indicative**, not statutory — the indicators are weighed in the round.)

## The case law behind the indicators

The eight indicators are not invented by the ATO; they are distilled from decades of Australian (and English) judicial reasoning on what makes an activity a "business." The leading authorities a tribunal returns to:

| Case | Citation | What it established | Relevance to traders |
|---|---|---|---|
| *Ferguson v FC of T* | (1979) 79 ATC 4261 | The leading modern statement of the indicators; a business can exist even when small or part-time, judged on commercial character and intention | A side-activity can still be a business if conducted commercially |
| *Martin v FC of T* | (1953) 90 CLR 470 | Businesslike conduct and genuine profit purpose are central; intention matters but must be backed by activity | Profit motive plus real operation, not aspiration |
| *FC of T v Radnor Pty Ltd* | (1991) 91 ATC 4689 | Repetition, regularity and scale weigh heavily; a single or isolated transaction is rarely a business | Volume and continuity are key for share trading |
| *Smith v Anderson* (UK) | (1880) 15 Ch D 247 | Classic dictum: "carrying on" implies a series of activities, not a one-off | Foundation for the repetition indicator |
| *FC of T v Myer Emporium* | (1987) 163 CLR 199 | Even an isolated transaction can be on revenue account if entered into with a profit-making intention as part of business operations | Why a "one big trade" can still be ordinary income |

The ATO's own published share-trading guidance and a long line of Administrative Appeals Tribunal (AAT) decisions apply these authorities specifically to share and derivative activity. Because each case turns on its own facts, no decision is a template — but the *direction* of the reasoning (volume, system, profit purpose, businesslike records) is consistent.

## Worked example (qualitative)

Two people each make 300 disposals in a financial year. The classification can still differ:

- **Person A** runs the activity full-time from a dedicated home office, keeps a written trading plan and a trade journal with rationale and position sizing for every entry, reconciles monthly P&L, uses a margin facility and a professional data feed, and has reduced other paid work to free up time. The activity has scale, system, repetition, and a documented profit purpose. On a TR 97/11 weighing, Person A is very likely **carrying on a business** (revenue account): brokerage and data feeds are deductible, losses can offset other income subject to [[non-commercial-losses-div-35|Division 35]], but gains attract no [[capital-gains-tax-discount|CGT discount]].
- **Person B** has a salaried day job, made most of those 300 disposals in a single volatile fortnight after reading a forum thread, keeps no plan or journal, and otherwise holds long-term. The activity lacks continuity, system, and businesslike organisation despite the headline trade count. On the same weighing, Person B is more likely a **share investor** (capital account): brokerage is added to the cost base, gains on parcels held >12 months get the 50% discount, but losses are quarantined to capital gains.

Same volume, opposite outcome — because the indicators are weighed in the round and **how** the activity is conducted matters as much as **how much**. See [[trader-vs-investor-classification-au]] for more borderline scenarios and the structural alternatives.

## Common pitfalls

- **Assuming a high trade count settles it.** Volume is the single most-cited factor but it is not decisive on its own (see Person B above). Conversely, a low trade count does not guarantee investor status if the activity is otherwise highly commercial.
- **Treating the self-label as binding.** Ticking "share trader" or "investor" does not change the legal character of the activity — see [The "self-label" trap](#the-self-label-trap).
- **Switching branches opportunistically.** Claiming business treatment in loss years and investor treatment in gain years invites reclassification and penalties; consistency across years is expected.
- **Ignoring Division 35 once in business.** Revenue-account losses are not automatically deductible against salary — the [[non-commercial-losses-div-35|non-commercial loss]] tests and the $250k income gate apply, with relief only via the [[commissioners-discretion-s-35-55|Commissioner's discretion]] in some cases.
- **No contemporaneous records.** Building the evidence *after* an audit notice is far weaker than a real-time trading plan, journal, and separate accounts.
- **Overlooking the GST and ABN consequences** of being in business, and the trading-stock rules in [[itaa-1997-overview|Division 70]].

## Edge cases and grey zones

| Profile | Likely classification | Notes |
|---|---|---|
| Day trader, full-time, 1,000+ trades/yr | **Business** | Clear |
| Active swing trader, 200 trades/yr, side activity to a day job | Likely business if documented strategy | Volume + system matter |
| Options writer collecting premium monthly on a portfolio | Grey — depends on volume, profit motive, and systematic approach | Often capital |
| Investor with 50 trades/yr, mostly buy-and-hold but some active rotation | Likely investment | Volume too low |
| Crypto trader with high frequency on DeFi | Likely business if frequent and systematic | Same test applies |
| HODLer of BTC across multiple years | **Investment** | No business activity |

## The "self-label" trap

The ATO has consistently rejected taxpayer self-labelling as determinative. Calling yourself a "trader" on the tax return without the underlying facts to support it will not change classification. Conversely, an investor who deliberately characterises gains as capital after years of business-like trading may face reclassification on audit, with penalties.

## Documentation that helps

If you intend to be classified as carrying on a trading business, build the evidence in real time:

- **Written trading plan** — strategies, risk rules, entry/exit criteria
- **Trade journal** — every position with rationale, sizing, outcome
- **P&L records** — monthly, quarterly, annual
- **Separate bank/broker accounts** for trading activity
- **Time logs** if possible — hours per week dedicated
- **Subscription records** — data feeds, trading platforms, education
- **Business registration** — ABN where appropriate; ASIC registration if a company

## Sources

Written from the public text of TR 97/11 and the broader Australian case law on "carrying on a business." **Confirm current ATO guidance and seek professional advice before relying on this classification.**

- ATO, *Taxation Ruling TR 97/11 — Income tax: am I carrying on a business of primary production?* — the canonical ruling codifying the eight indicators. https://www.ato.gov.au/law/view/document?docid=TXR/TR9711/NAT/ATO/00001
- ATO, *Carrying on a business of share trading* (web guidance and QC quick codes on the share trader vs share investor distinction). https://www.ato.gov.au/individuals-and-families/investments-and-assets/investing-in-shares
- *Ferguson v Federal Commissioner of Taxation* (1979) 79 ATC 4261 — leading authority on the indicators of carrying on a business.
- *Martin v Federal Commissioner of Taxation* (1953) 90 CLR 470 — businesslike conduct and profit purpose.
- *Federal Commissioner of Taxation v Radnor Pty Ltd* (1991) 91 ATC 4689 — repetition, regularity and scale.
- *Income Tax Assessment Act 1997* (Cth) ss 6-5, 8-1, Div 35, Div 70 — the operative provisions for revenue vs capital treatment. https://www.legislation.gov.au/Details/C2023C00104

## Related

- [[non-commercial-losses-div-35]] — what applies once you are in business
- [[trader-vs-investor-classification-au]] — practical guide using TR 97/11
- [[itaa-1997-overview]] — broader ITAA index (incl. Div 70 trading stock)
- [[commissioners-discretion-s-35-55]] — escape hatch when Div 35 tests fail
- [[australian-investor-tax]] — broader investor tax framework
- [[capital-gains-tax-discount]] — the 50% discount available only on capital account
- [[smsf]] — a structure with its own loss rules outside Division 35
- [[margin]] — margin interest deductibility differs by classification
