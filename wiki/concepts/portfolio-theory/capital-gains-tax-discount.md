---
title: "Capital Gains Tax Discount (Australia)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [australia, tax, portfolio-theory, strategy]
aliases: ["CGT Discount", "50% CGT Discount", "12 Month CGT Discount"]
related: ["[[australian-investor-tax]]", "[[tax-loss-harvesting-australia]]", "[[superannuation]]", "[[smsf]]", "[[position-trading-overview]]", "[[swing-trading-overview]]", "[[covered-call]]", "[[tax-efficient-investing]]", "[[stage-3-tax-cuts]]", "[[portfolio-construction]]", "[[cryptocurrency-tax-australia]]"]
domain: [portfolio-theory, risk-management]
difficulty: beginner
prerequisites: ["[[australian-investor-tax]]"]
---

> **Not tax or financial advice.** This page explains the discount in general terms. All rates, brackets, thresholds and dollar figures below are **indicative** and change with legislation — confirm current numbers and your eligibility with the ATO or a registered tax agent before acting.

The 50% CGT discount is the single most valuable tax provision available to Australian investors. If you hold a CGT asset (shares, ETFs, cryptocurrency, property, managed fund units) for more than 12 months before selling, you only include **half** of the net capital gain in your assessable income. For an investor in the top tax bracket, this roughly halves the effective tax rate on long-term gains — a saving that dwarfs almost any other legal tax optimisation strategy. Crucially, the discount is only available on **capital account**: a [[trader-vs-investor-classification-au|share trader carrying on a business]] holds shares as trading stock and gets no discount at all (see [[tr-97-11-carrying-on-a-business]]).

## Overview

Introduced in 1999 (replacing the previous inflation-indexation method), the CGT discount applies automatically when an individual or trust disposes of a CGT asset that has been held for at least 12 months and one day. [[superannuation]] funds receive a reduced discount of 33.33% (paying tax on two-thirds of the gain). Companies receive no discount at all.

The discount fundamentally shapes rational investment behaviour in Australia:

- It creates a strong tax incentive to hold investments for at least 12 months
- It makes [[position-trading-overview|position trading]] and buy-and-hold dramatically more tax-efficient than day trading or [[scalping]]
- It means the timing of sales around the 12-month mark can have a material impact on after-tax returns
- Combined with [[superannuation]] tax rates, it creates effective CGT rates as low as 0% (SMSF pension phase)

## How It Works

1. **Buy a CGT asset** (e.g., 1,000 shares of CBA at $100 each = $100,000 cost base)
2. **Hold for more than 12 months** (e.g., buy 1 January 2025, sell 2 January 2026 or later)
3. **Sell at a gain** (e.g., sell at $130 each = $130,000 proceeds, $30,000 gross capital gain)
4. **Apply any capital losses** (e.g., $5,000 in harvested losses = $25,000 net capital gain)
5. **Apply 50% discount** (e.g., $25,000 x 50% = $12,500 assessable capital gain)
6. **Pay tax at marginal rate** (e.g., at 37% bracket = $4,625 tax on a $30,000 gross gain)

Without the discount (if sold before 12 months): $25,000 net gain taxed at 37% = $9,250 tax. The discount saved $4,625 — simply by waiting.

## Effective Tax Rate Tables

### Short-Term vs Long-Term Capital Gains (Individuals)

| Marginal Tax Bracket | Short-Term CGT Rate (held <12 months) | Long-Term CGT Rate (held >12 months, 50% discount) | Tax Saved per $10,000 Gain |
|----------------------|---------------------------------------|-----------------------------------------------------|---------------------------|
| 0% ($0-$18,200) | 0% | 0% | $0 |
| 19% ($18,201-$45,000) | 19% | 9.5% | $950 |
| 30% ($45,001-$135,000)* | 30% | 15% | $1,500 |
| 37% ($135,001-$190,000)* | 37% | 18.5% | $1,850 |
| 45% ($190,001+)* | 45% | 22.5% | $2,250 |
| 45% + 2% Medicare | 47% | 23.5% | $2,350 |

*Post [[stage-3-tax-cuts]] brackets (from 1 July 2024)

### Super Fund Capital Gains

| Super Fund Phase | Short-Term CGT Rate | Long-Term CGT Rate (33.33% discount) | Notes |
|------------------|---------------------|---------------------------------------|-------|
| Accumulation | 15% | 10% | 33.33% discount (not 50%) |
| Pension phase | 0% | 0% | No tax regardless of holding period |

### Worked Example: The 12-Month Cliff

Consider an investor in the 37% bracket who bought $50,000 of shares now worth $80,000 (a $30,000 gain):

**Selling at 11 months (no discount):**
- $30,000 gain taxed at 37% = **$11,100 tax**
- After-tax gain: $18,900
- After-tax return: 37.8%

**Selling at 13 months (50% discount):**
- $30,000 gain, discounted to $15,000, taxed at 37% = **$5,550 tax**
- After-tax gain: $24,450
- After-tax return: 48.9%

**Difference: $5,550 saved** by waiting 2 months. This "cliff" effect means investors should almost always delay selling a profitable position if they are close to the 12-month mark — even if they believe the asset will decline slightly in the interim, the tax saving may outweigh the expected capital loss.

## Comparison to US Capital Gains Tax

| Feature | Australia | United States |
|---------|-----------|---------------|
| **Method** | Discount method (50% of gain excluded) | Separate preferential rate |
| **Short-term rate** | Marginal income tax rate (up to 47%) | Ordinary income tax rate (up to 37%) |
| **Long-term rate** | Effective 0-23.5% (half of marginal rate) | 0%, 15%, or 20% (depending on income) |
| **Holding period** | >12 months | >12 months |
| **Entity types** | Individuals and trusts only (not companies) | Individuals (companies taxed at flat 21%) |
| **Super/retirement** | 33.33% discount in super, 0% in pension | 0% in Roth IRA (on withdrawal) |
| **Wash sale rule** | No general wash sale rule | 30-day wash sale rule (stocks and crypto from 2026) |
| **Net Investment Income Tax** | No equivalent | 3.8% NIIT for high earners |

The Australian system is particularly advantageous for investors in the lower-middle brackets. An Australian investor at the 30% bracket pays an effective 15% on long-term gains — the same as a US investor earning $44,626-$492,300 pays on long-term gains — but the Australian can also access franking-credits on dividends and the no-wash-sale advantage for [[tax-loss-harvesting-australia|tax-loss harvesting]].

## Strategy Implications

### Holding Period Management

- **Before selling a profitable position, always check the acquisition date** — if you are within weeks of the 12-month mark, the tax saving from waiting almost certainly exceeds any expected decline
- **Set calendar reminders** for the 12-month anniversary of significant purchases
- **For [[portfolio-rebalancing]]**: time rebalancing sales to occur after the 12-month mark for positions with gains

### Impact on Trading Strategy Selection

The CGT discount creates a structural tax penalty for short-term trading in Australia:

| Strategy | Typical Holding Period | CGT Discount? | Tax Efficiency |
|----------|----------------------|---------------|----------------|
| [[scalping]] | Minutes to hours | No | Very poor — full marginal rate on every gain |
| Day trading | Hours to one day | No | Very poor |
| [[swing-trading-overview|Swing trading]] (short) | Days to weeks | No | Poor |
| [[swing-trading-overview|Swing trading]] (long) | Weeks to months | Sometimes | Variable |
| [[position-trading-overview|Position trading]] | Months to years | Usually yes | Good |
| Buy and hold | Years to decades | Yes | Excellent |
| [[passive-investing]] / DCA | Decades | Yes | Excellent |

For an active trader in the 45% bracket, every dollar of short-term gain is taxed at 47% (with Medicare). The same gain held 12 months is taxed at 23.5%. A trader generating $100,000 in gains per year would pay $47,000 in tax on short-term trades vs $23,500 on long-term — a $23,500 annual difference. Over 20 years compounded, this tax drag is devastating.

### Covered Call Interaction

Writing [[covered-call|covered calls]] against long-held share positions does NOT trigger a CGT event on the underlying shares. This means:

- You can hold shares for >12 months (qualifying for CGT discount)
- Simultaneously sell call options to generate income
- The option premium is a separate CGT event (with its own holding period)
- If shares are called away (assigned), the share disposal qualifies for the CGT discount if held >12 months
- This makes covered calls a tax-efficient income strategy for long-term holders

### Tax-Loss Harvesting Interaction

When using [[tax-loss-harvesting-australia|tax-loss harvesting]], capital losses are applied **before** the CGT discount:

- **Correct order**: Gross gain - Losses = Net gain, then apply 50% discount
- **Example**: $20,000 gross gain - $5,000 loss = $15,000 net gain x 50% = $7,500 assessable
- This means each dollar of loss effectively shelters only 50 cents of assessable income on discounted gains
- Losses are still valuable — but they are worth more when offsetting short-term (non-discounted) gains
- **Strategy**: Offset short-term gains first (where the full gain is assessable), then long-term gains

### Timing Around End of Financial Year

- If you have both gains and losses to realise, consider crystallising **losses before 30 June** and **deferring gains to after 1 July** — this shifts the gain into the next financial year while capturing the loss in the current year
- Be aware of the 12-month mark: a share bought on 1 July 2024 qualifies for the discount if sold on or after 2 July 2025

## What Does NOT Qualify for the Discount

- **Companies**: No CGT discount for corporate entities — gains taxed at flat 30% (or 25% for small companies)
- **Non-residents**: Post-8 May 2012, non-residents cannot claim the CGT discount on assets that are not "taxable Australian property" (TAP). TAP includes direct real property interests and indirect interests in entities with >50% Australian real property
- **Trading stock**: If you are classified as a share trader (see [[australian-investor-tax#Trader vs Investor Distinction]]), your shares are "trading stock" and no CGT discount applies
- **Assets held <12 months**: The discount is all-or-nothing. Held 364 days = no discount. Held 366 days = full 50% discount
- **Collectable assets acquired for <$500**: Exempt from CGT entirely (but no loss can be claimed either)

## Eligibility at a Glance

| Holder / asset | Discount available? | Effective treatment |
|---|---|---|
| Individual, asset held >12 months, capital account | Yes — 50% | Half the gain assessable at marginal rate |
| Individual, asset held <12 months | No | Full gain assessable |
| Trust (flowing to individual beneficiary) | Yes — 50% flows through | Discount preserved in the beneficiary's hands |
| [[superannuation\|Super fund]] (accumulation) | Yes — 33.33% | Two-thirds of gain taxed at 15% |
| [[smsf\|SMSF]] (pension phase) | N/A — 0% tax | No CGT regardless of holding period |
| [[company\|Company]] | No | Full gain at the company rate |
| [[trader-vs-investor-classification-au\|Share trader]] (revenue account) | No | Gain is ordinary income; shares are trading stock |
| Non-resident (non-TAP asset, post-8 May 2012) | No | Discount denied |

The single biggest lever most investors control is the **>12-month holding rule** combined with **capital-account status** — both are required, and a share trader forfeits the discount even on positions held for years.

## Common Pitfalls

- **Selling one day too early.** The discount is all-or-nothing at the 12-month-and-one-day mark; check the acquisition date before realising a gain (see [the 12-month cliff](#worked-example-the-12-month-cliff)).
- **Assuming companies get the discount.** They do not — a common trap when investors incorporate to "save tax" without modelling the lost discount and double-tax on distributions.
- **Forgetting trader status removes it.** If your activity is a business under [[tr-97-11-carrying-on-a-business|TR 97/11]], the discount is gone — model after-tax outcomes both ways before scaling up trading.
- **Mis-ordering losses and the discount.** Capital losses apply *before* the 50% discount, so a dollar of loss only shelters 50 cents of a discounted gain — apply losses to non-discounted (short-term) gains first. See [[tax-loss-harvesting-australia]].
- **Using the contract date wrong.** For CGT timing, the relevant date is generally the contract date, not settlement — this can shift which financial year (and whether the 12-month test) applies.
- **Ignoring non-resident rules.** Becoming a non-resident can deny the discount on non-TAP assets accrued after 8 May 2012.

## Recent Changes

The [[stage-3-tax-cuts]] (effective 1 July 2024) altered the income tax brackets, which affects the effective CGT rates:

- The 32.5% bracket was replaced with a 30% bracket (up to $135,000)
- This slightly reduced effective long-term CGT for middle-income earners (from 16.25% to 15%)
- The top bracket threshold moved from $180,001 to $190,001, providing a small benefit for earners in that range
- The 50% discount itself was NOT changed — it remains one of the most politically durable tax provisions

## Related

- [[australian-investor-tax]]
- [[tax-loss-harvesting-australia]]
- [[superannuation]]
- [[smsf]]
- [[position-trading-overview]]
- [[swing-trading-overview]]
- [[covered-call]]
- [[tax-efficient-investing]]
- [[stage-3-tax-cuts]]
- [[portfolio-construction]]
- [[cryptocurrency-tax-australia]]
- [[passive-investing]]
- [[scalping]]
- [[trader-vs-investor-classification-au]]
- [[tr-97-11-carrying-on-a-business]]
- [[company]]
- [[negative-gearing]]

## Sources

- ATO — CGT discount for individuals
- ATO — Working out your capital gain
- Australian Government Treasury — Capital gains tax policy
- *Income Tax Assessment Act 1997* (Cth) Div 100–115 — CGT regime and the discount (Div 115)
