---
title: "Capital Gains"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [risk-management, portfolio-theory, valuation]
aliases: ["Capital Gains", "Capital Gain", "Capital Gains Tax", "CGT", "Realized Gains"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[tax-efficient-investing]]"]
difficulty: beginner
related: ["[[capital-gains-tax-discount]]", "[[tax-efficient-investing]]", "[[tax-loss-harvesting]]", "[[australian-investor-tax]]", "[[dividend]]", "[[rebalancing]]", "[[holding-period]]", "[[wash-sale-rule]]", "[[cryptocurrency-tax-australia]]"]
---

A **capital gain** is the profit realised when a capital asset (shares, ETFs, property, cryptocurrency, collectibles) is sold for more than its **cost base** (purchase price plus allowable acquisition costs). The gain is "unrealised" while the position is held and becomes a taxable event only on disposal in most jurisdictions. Because tax codes treat capital gains differently from ordinary income — usually favouring long holding periods — capital-gains treatment is a first-order input into after-tax strategy design.

## Mechanics

```
Capital gain = Sale proceeds − Cost base
Cost base    = Purchase price + brokerage + other acquisition/improvement costs
Net gain     = Total gains − Total capital losses (current year + carried forward)
Tax payable  = f(net gain, holding period, entity type, jurisdiction)
```

Capital **losses** can typically offset capital gains (and sometimes a limited amount of ordinary income); unused losses carry forward. The interaction of gains, losses, and holding period is what makes [[tax-loss-harvesting]] and disposal timing material to net returns.

### Realized vs unrealized gains

A gain is **unrealized** (a "paper gain") while the asset is still held, and **realized** only when it is disposed of. This distinction is the single most important lever in after-tax investing:

| | Unrealized gain | Realized gain |
|---|---|---|
| Taxable now? | No (in most jurisdictions) | Yes — disposal is the taxable event |
| Compounds tax-free? | Yes — the full pre-tax balance keeps working | No — tax leaks out at each realization |
| Investor control | High — you choose when to crystallize | Triggered by your sell decision |
| Risk | Position remains exposed to the market | Locked in; capital is freed |

Because unrealized gains compound on the *full* pre-tax balance, deferral is a form of an interest-free loan from the tax authority. This is the mathematical engine behind buy-and-hold tax efficiency (see [[tax-efficient-investing]]) and a core argument for low [[portfolio-turnover|turnover]].

### Worked example (illustrative, US-style figures)

> Illustrative only — uses round numbers, not current statutory rates.

Buy 1,000 shares at $50 (cost base $50,000 incl. brokerage). Sell at $80.

```
Proceeds      = 1,000 × $80 = $80,000
Cost base     = $50,000
Capital gain  = $30,000

Scenario A — held 11 months (short-term, taxed as ordinary income @ ~32%):
  Tax = $30,000 × 0.32 = $9,600   →  after-tax gain $20,400

Scenario B — held 13 months (long-term, preferential @ 15%):
  Tax = $30,000 × 0.15 = $4,500   →  after-tax gain $25,500

Waiting ~2 extra months saved $5,100 — a 17% lift on the after-tax outcome.
```

The same trade, same price, different *after-tax* result purely from holding period. This is the "12-month cliff" quantified.

## Short-term vs long-term: the holding-period incentive

Nearly every developed tax system rewards longer [[holding-period|holding periods]], creating a structural tax penalty for high-turnover trading.

| Jurisdiction | Short-term treatment | Long-term treatment | Threshold |
|---|---|---|---|
| **United States** | Taxed as ordinary income (up to 37% + 3.8% NIIT) | Preferential 0% / 15% / 20% | >12 months |
| **Australia** | Full marginal rate (up to 47%) | 50% of the gain excluded → effective half-rate; see [[capital-gains-tax-discount]] | >12 months |
| **United Kingdom** | CGT rates with annual exempt amount | Same rate, no long-term discount | n/a (no holding distinction) |
| **Germany** | Flat ~26.375% (Abgeltungsteuer) on securities | Same flat rate | n/a |

The US uses **preferential rate brackets**; Australia uses a **discount method** (50% of the gain is excluded for individuals/trusts held >12 months, 33.33% in superannuation). Companies generally receive no discount. See [[capital-gains-tax-discount]] for the detailed Australian treatment and worked examples.

### The US rate structure (qualitative)

> US brackets are indexed annually and change with legislation — the figures below describe the *structure*, not current-year thresholds. Verify exact numbers against the IRS for any real filing.

- **Short-term capital gains** (assets held ≤12 months) are taxed at the same graduated rates as **ordinary income** — the top federal marginal rate has historically been ~37%.
- **Long-term capital gains** (held >12 months) fall into preferential brackets — historically **0% / 15% / 20%**, with the rate stepping up as taxable income rises. Most middle-income investors land in the 15% bracket; only the highest incomes reach 20%.
- A **Net Investment Income Tax (NIIT)** of 3.8% applies on top of the above for high earners, so the effective top long-term rate has been ~23.8% and the effective top short-term rate ~40.8%.
- **State taxes** stack on top — some states (California, New York) tax capital gains as ordinary income with no preferential rate, while others (Texas, Florida) levy no state income tax at all.

The practical takeaway: the *spread* between short- and long-term treatment can exceed 20 percentage points, which is why the holding-period decision is one of the largest controllable levers on after-tax return for a US trader.

## Trading relevance

- **Strategy selection.** [[scalping|Scalping]] and day trading generate short-term gains taxed at the highest rates; [[position-trading-overview|position trading]] and buy-and-hold capture preferential long-term treatment. After-tax, a lower-pretax-return long-term strategy can beat a higher-pretax-return churn strategy.
- **The 12-month cliff.** In the US and Australia, crossing the 12-month mark discretely changes the tax rate. When a profitable position is close to the anniversary, the tax saving from waiting often exceeds the expected price drift — a concrete timing rule, not a vibe.
- **Tax-loss harvesting.** Realising losses to offset gains lowers the tax bill; the [[wash-sale-rule]] (US 30-day rule; no general AU equivalent) governs how aggressively this can be done.
- **Deferral as compounding.** Unrealised gains compound tax-free; every realisation event "leaks" capital to tax. This is why low-turnover and tax-deferred wrappers (super, IRA/401(k), ISA) materially raise long-run compounding.
- **Rebalancing tension.** [[rebalancing|Rebalancing]] forces realisations; timing rebalances after the long-term threshold, or using new contributions/dividends to rebalance, reduces the tax drag.
- **Crypto.** Most jurisdictions treat crypto disposals (including crypto-to-crypto swaps and spending) as CGT events — a frequent surprise for active on-chain traders. See [[cryptocurrency-tax-australia]].

## Tax-loss harvesting and the wash sale

[[tax-loss-harvesting]] is the deliberate realization of losing positions to bank capital losses that offset realized gains (and, in the US, up to $3,000 of ordinary income per year, with the remainder carried forward). It converts a paper loss into a usable tax asset without necessarily abandoning the market exposure — the trader typically rotates into a *similar but not identical* security.

The constraint is the **[[wash-sale-rule|wash-sale rule]]**:

| | United States | Australia |
|---|---|---|
| Rule | Loss disallowed if a "substantially identical" security is bought within **30 days before or after** the sale | No bright-line wash-sale rule; ATO can apply the general **anti-avoidance** provisions (Part IVA) where the dominant purpose is a tax benefit |
| Workaround | Switch to a *not* substantially identical proxy (e.g. a different issuer's S&P 500 ETF), or wait out the 61-day window | Allow a genuine change in economic position; avoid same-day buy-back schemes |
| Effect of a violation | Disallowed loss is added to the cost base of the replacement shares (deferred, not lost) | Loss may be denied outright if Part IVA is invoked |

The wash-sale window is **61 calendar days** in the US (30 before + sale day + 30 after) and applies across accounts — including a spouse's account and IRAs, a common trap.

## Pitfalls and risks

- **The phantom gain on funds.** Mutual funds distribute realized capital gains to holders annually; you can owe tax on a gain you never personally captured (and even in a year the fund's price fell). ETFs are more tax-efficient via in-kind redemption.
- **Forgetting the cost-base adjustments.** Reinvested dividends, return-of-capital distributions, stock splits, and corporate actions all change the cost base. Omitting them inflates the reported gain and overpays tax.
- **The wash-sale trap across accounts.** Buying the same security in a retirement account within the window permanently disallows the loss in the taxable account (US) — it is not merely deferred.
- **Letting the tax tail wag the dog.** Holding a deteriorating position purely to reach the 12-month mark, or to defer a gain, can cost more in market risk than it saves in tax. Tax efficiency is a *secondary* objective behind the investment thesis itself.
- **Bracket creep on a single large sale.** A big realized gain can push income into a higher long-term bracket or trigger the NIIT — spreading disposals across tax years can keep the rate down.

## Related

- [[capital-gains-tax]] — the tax instrument applied to realized gains
- [[capital-gains-tax-discount]] — Australian 50% discount in detail
- [[tax-efficient-investing]]
- [[tax-loss-harvesting]] — banking losses to offset gains
- [[wash-sale]] · [[wash-sale-rule]] — the constraint on harvesting
- [[australian-investor-tax]]
- [[cryptocurrency-tax-australia]] — crypto as a CGT asset
- [[holding-period]] — the short-vs-long-term hinge
- [[portfolio-turnover]] — turnover as the driver of realized-gain tax drag
- [[dividend]] — the other taxable return stream
- [[rebalancing]] — the recurring realization trigger

## Sources

- IRS — Topic No. 409 Capital Gains and Losses (US short-term vs long-term rates); Publication 550 (wash sales).
- ATO — Capital gains tax / CGT discount (Australia); guidance on Part IVA anti-avoidance.
- HMRC — Capital Gains Tax overview (UK).
- General market knowledge for illustrative worked examples (rates are illustrative, not current statutory figures).
