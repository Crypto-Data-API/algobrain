---
title: "Tax-Loss Harvesting (Australia)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [australia, tax, strategy, portfolio-theory]
aliases: ["Australian Tax Loss Harvesting", "EOFY Selling"]
related: ["[[tax-loss-harvesting]]", "[[wash-sale]]", "[[australian-investor-tax]]", "[[capital-gains-tax-discount]]", "[[calendar-effects]]", "[[portfolio-rebalancing]]", "[[franking-credits]]", "[[superannuation]]", "[[smsf]]", "[[cryptocurrency-tax-australia]]", "[[tax-efficient-investing]]", "[[risk-management]]"]
domain: [portfolio-theory, risk-management]
difficulty: intermediate
prerequisites: ["[[australian-investor-tax]]", "[[capital-gains-tax-discount]]"]
---

Australian tax-loss harvesting is the practice of selling investments at a loss before 30 June (the end of the Australian financial year) to crystallise capital losses that offset capital gains, thereby reducing your tax bill. While the core concept is the same as [[tax-loss-harvesting|general tax-loss harvesting]], Australia's rules differ in one widely-cited way: **there is no US-style statutory 30-day wash sale rule**. However — and this is the critical 2026 nuance — the ATO has repeatedly signalled that artificial sell-and-rebuy "wash sales" can still be attacked under the general anti-avoidance provision (Part IVA). The "no wash sale rule" claim is true only in the narrow statutory sense; in substance the ATO does have a wash-sale stance (see [[wash-sale]] and the section below).

> **Not financial or tax advice.** This page is general educational information about Australian tax concepts, not personal advice. Tax rates, thresholds, CGT discount mechanics, and ATO positions change between financial years and depend on your individual circumstances. **All figures below are indicative only** and may be out of date. Confirm current rules at [ato.gov.au](https://www.ato.gov.au) and consult a registered tax agent or financial adviser before acting.

## Overview

The Australian tax-loss harvesting strategy revolves around the 30 June financial year end. Investors review their portfolios in May and June each year, identify positions with unrealised losses, and sell those positions to "crystallise" the loss for tax purposes. These realised losses offset any realised gains in the same financial year, directly reducing the tax owed.

The strategy is particularly powerful in Australia because:

1. **No statutory wash sale rule**: Australia has no US-style 30-day wash sale *statute*. Mechanically you can sell and rebuy the same stock within days — but the ATO's anti-avoidance stance constrains doing this purely for tax (see [[wash-sale]] and the dedicated section below)
2. **Capital losses carry forward indefinitely**: If you have no gains to offset this year, the losses roll forward to future years
3. **The [[capital-gains-tax-discount]] amplifies the benefit**: At the top marginal bracket, a harvested loss saves roughly *(indicative)* ~23.5% of the loss amount against discounted long-term gains, or up to the full top marginal rate (~47% incl. Medicare levy, indicative) against undiscounted short-term gains. **These percentages are illustrative and depend on the current rate schedule** — verify against ATO rates for the relevant year
4. **EOFY seasonality creates additional opportunities**: Widespread tax selling in May-June can depress prices, creating buying opportunities (see [[calendar-effects]])

## How It Works

### Step-by-Step

1. **Review your portfolio in May** — identify all positions with unrealised losses
2. **Prioritise which losses to harvest**:
   - Losses that offset **short-term gains** (taxed at full marginal rate) are more valuable than losses offsetting **long-term gains** (where only 50% of the gain is assessable)
   - Larger losses provide proportionally larger tax savings
   - Consider whether you still want to own the asset long-term
3. **Sell the losing position before 30 June** — the loss is "crystallised" and becomes a realised capital loss
4. **The loss offsets gains** — subtract from any realised capital gains in the current financial year
5. **Repurchase the asset (if desired)** — since there is no wash sale rule, you can buy back the same asset within days. The new purchase creates a new parcel with a new cost base and acquisition date
6. **Carry forward excess losses** — if losses exceed gains, the excess carries forward indefinitely

### Worked Example

*(Illustrative only — the 37% rate and CGT-discount mechanics are indicative and may not match the current year's schedule. Figures are for concept demonstration, not a tax calculation.)*

**Scenario**: An investor in the (indicative) 37% bracket has the following in the current financial year:
- Sold BHP shares for a $20,000 gain (held >12 months — qualifies for [[capital-gains-tax-discount|50% CGT discount]])
- Holds Woodside Energy shares with a $15,000 unrealised loss
- Holds ANZ shares with a $5,000 unrealised loss

**Without tax-loss harvesting:**
- $20,000 gain, discounted to $10,000, taxed at 37% = **$3,700 tax**

**With tax-loss harvesting (sell Woodside and ANZ before 30 June):**
- $20,000 gain - $15,000 loss - $5,000 loss = $0 net capital gain
- **$0 tax** — saving $3,700

The investor can then repurchase Woodside and ANZ in early July (or even late June) if they still believe in the long-term thesis.

## The No Wash Sale Rule Advantage

This is Australia's most significant tax-loss harvesting advantage over the US and many other jurisdictions.

### US Wash Sale Rule (for comparison)

In the United States, the IRS wash sale rule prohibits claiming a loss if you purchase a "substantially identical" security within 30 days before or after the sale. This creates a 61-day window during which you cannot hold the same position — exposing you to market risk if the stock rebounds.

### Australia's Position

Australia has **no statutory wash sale rule** equivalent to the US 30-day test for shares or cryptocurrency. But "no statute" is not "no rule" — the ATO's actual stance is more restrictive than the popular framing suggests:

- Selling at a loss and repurchasing the same shares is **not automatically** an avoidance scheme
- The ATO's general anti-avoidance provision (**Part IVA of the Income Tax Assessment Act 1936**) **can** apply if the **sole or dominant purpose** of the arrangement is to obtain a tax benefit
- The ATO has explicitly described "**wash sales**" as a target. It has published guidance (including a Taxpayer Alert in the **TA 2008/7** lineage on wash-sale arrangements) treating disposals where the taxpayer retains effective economic exposure to the same asset as potentially caught by Part IVA. The ATO's modern messaging — including data-matching campaigns and EOFY warnings — explicitly cautions against artificial wash sales
- The substance test is what matters: if you genuinely intended to exit and the repurchase has an independent commercial rationale, ordinary harvesting is generally accepted. If the sale and rebuy are economically a round-trip whose only point is the loss, the deduction is at risk
- In practice, straightforward harvesting where there is a real change (different asset, real time gap, genuine reassessment) has not been the ATO's enforcement focus; systematic, large, same-day round-trips are

#### Statutory wash sale vs ATO anti-avoidance — the distinction that matters

| Feature | US wash sale rule | Australia |
|---|---|---|
| Mechanism | Hard statutory 30-day rule (IRC §1091) | No statute; **Part IVA** general anti-avoidance + ATO wash-sale guidance |
| Trigger | Buy "substantially identical" security ±30 days | "Sole or dominant purpose" of obtaining a tax benefit |
| Effect if caught | Loss deferred (added to new cost base) | Tax benefit can be **cancelled** by the Commissioner |
| Certainty | Bright-line, mechanical | Judgement-based, fact-dependent |
| Practical takeaway | Wait 31 days or use a non-identical proxy | Have a genuine reason; avoid pure round-trips; document substance |

The upshot: Australia is *more flexible* (no automatic 30-day lockout) but *less certain* (a purpose test you must satisfy). See [[wash-sale]] for the US mechanics in detail.

### Practical Approaches

| Approach | What you do | ATO challenge risk | Market-risk exposure |
|---|---|---|---|
| Proxy swap | Sell loser, buy a *similar but different* ETF, swap back after 30+ days | Lowest | Low (stay invested in the sector) |
| EOFY gap | Sell late June, rebuy early July | Low-moderate | Brief out-of-market gap |
| Same-day round-trip | Sell and rebuy same/next day | **Highest** (looks like a wash sale under Part IVA) | Minimal |

The proxy-swap route is the cleanest because it changes the asset *and* keeps you invested, sidestepping both the Part IVA purpose test and the [[wash-sale]]-style "same economic exposure" concern. The detailed tiers:

**Most conservative (lowest risk of ATO challenge):**
- Sell the losing stock, buy a similar but different ETF to maintain market exposure, then swap back after 30+ days
- Example: Sell losing CBA shares, buy VAS (Vanguard Australian Shares ETF) to maintain bank exposure, swap back later

**Common practice (generally accepted):**
- Sell the losing stock on the last trading day of June, repurchase in early July
- The short gap and new financial year provide a reasonable separation

**Most aggressive (higher audit risk):**
- Sell and repurchase on the same day or next day
- Technically not prohibited, but may attract ATO scrutiny if done repeatedly and systematically with large amounts

### What to Avoid

- **Do not** pre-arrange the sale and repurchase as a single transaction (e.g., don't tell your broker "sell and rebuy same day")
- **Do not** harvest losses on assets you would have sold anyway — the loss must be a genuine capital loss, not a manufactured one
- **Do not** harvest losses between related parties (e.g., selling to your SMSF or a family trust you control) — the ATO will disallow this
- **Do not** ignore the substance of the transaction — if there is no genuine commercial purpose beyond the tax benefit, Part IVA may apply

## EOFY Seasonality and Calendar Effects

Widespread tax-loss harvesting creates observable patterns in the Australian market that connect to [[calendar-effects]]:

### The May-June Selling Effect

- Institutional and retail investors sell losing positions in May and June
- This creates increased selling pressure on underperforming stocks
- Stocks that have fallen 20-50% during the year often see additional declines in May-June as investors harvest losses
- The increased selling can create temporary dislocations from fair value

### The July Rebound

- After 1 July, investors repurchase assets they sold for tax purposes
- Buying pressure on previously depressed stocks can create a "July bounce"
- This effect is well-documented in academic research on the ASX
- Smart investors can front-run this by buying in late June (harvesting their own losses elsewhere while purchasing other people's tax-loss sales)

### Contrarian Opportunity

- Stocks with large year-to-date losses approaching 30 June may be temporarily oversold due to tax selling
- If the fundamental thesis is intact, buying these stocks in late June can capture the July rebound
- This is the mirror image of the [[calendar-effects|January Effect]] observed in US markets (where tax selling occurs in December)

## Tax-Loss Harvesting in Super

The strategy works inside [[superannuation]] and [[smsf|SMSFs]], but with differences:

- **Accumulation phase**: Super funds pay (indicative) ~15% on gains, ~10% effective with the [[capital-gains-tax-discount|CGT discount]] on assets held >12 months. Losses in super are still valuable — each dollar of loss saves ~10-15 cents in tax *(indicative rates — confirm current super tax settings)*
- **Pension phase**: Gains are tax-free, so tax-loss harvesting has **no value** — there is no tax to reduce
- **Super vs personal**: If you hold the same stock personally and in your SMSF, you can harvest the loss in whichever entity provides the greater tax benefit (usually personal, where marginal rates are higher)

## Combining with Other Strategies

### Portfolio Rebalancing + Tax-Loss Harvesting

Use the EOFY tax-loss harvest as an opportunity to [[portfolio-rebalancing|rebalance your portfolio]]:

- Sell overweight positions that are also at a loss — simultaneously harvesting the loss and correcting the allocation
- Use proceeds to increase underweight positions
- This is the most tax-efficient time to rebalance because you are being "paid" (via tax savings) to make changes you would make anyway

### Franking Credit Offset

If you receive significant [[franking-credits|franking credit]] income from fully franked dividends, the grossed-up dividend amount increases your assessable income. Harvesting capital losses can offset capital gains that would otherwise push you into a higher bracket, indirectly protecting the value of your franking credits.

### Crypto Tax-Loss Harvesting

[[cryptocurrency-tax-australia|Cryptocurrency]] is particularly suited to tax-loss harvesting in Australia because:

- No wash sale rule applies to crypto (same as shares)
- Crypto markets are more volatile — larger unrealised losses are common
- Crypto-to-crypto swaps are CGT events, creating more opportunities to crystallise losses
- The ATO has not specifically targeted crypto tax-loss harvesting as an avoidance concern
- You can sell BTC at a loss, immediately rebuy, and claim the loss — legally and without controversy

## Record Keeping

The ATO requires detailed records for tax-loss harvesting:

- Date and price of original purchase (creating the cost base)
- Date and price of loss-making sale (crystallising the loss)
- Date and price of repurchase (new cost base)
- Evidence that each transaction was executed independently (not a pre-arranged scheme)
- Keep records for at least 5 years after the loss is applied against gains

## Common Mistakes

1. **Selling a position at a loss that has been held >12 months, then rebuying and selling the new parcel at a gain within 12 months** — the original loss offsets the new gain at the full rate (no discount), which is tax-efficient. But if you sell the new parcel after 12 months, the discount applies to the gain, while the loss was applied at the full rate — still beneficial, just less so
2. **Forgetting to apply losses in the correct order** — losses reduce the net gain before the [[capital-gains-tax-discount|CGT discount]] is applied, not after
3. **Harvesting losses in [[smsf]] pension phase** — pointless, as gains are already tax-free
4. **Not carrying forward losses** — if you have losses and no gains this year, ensure your tax agent carries the losses forward on your return
5. **Ignoring brokerage costs** — selling and rebuying incurs brokerage twice, which may exceed the tax benefit on small positions

## Related

- [[tax-loss-harvesting]]
- [[wash-sale]] — the US statutory rule Australia lacks (but partly replicates via Part IVA)
- [[australian-investor-tax]]
- [[capital-gains-tax-discount]]
- [[calendar-effects]]
- [[portfolio-rebalancing]]
- [[franking-credits]]
- [[superannuation]]
- [[smsf]]
- [[cryptocurrency-tax-australia]]
- [[tax-efficient-investing]]
- [[risk-management]]

## Sources

- ATO — Capital losses guide ([ato.gov.au](https://www.ato.gov.au))
- ATO — Part IVA general anti-avoidance provisions (Income Tax Assessment Act 1936)
- ATO — guidance and Taxpayer Alert material on "wash sale" arrangements (TA 2008/7 lineage)
- ATO — Record keeping for capital gains
- ATO — Capital gains tax discount (CGT discount) guidance

*Note: all rates, thresholds, and ATO positions cited are indicative and subject to change between financial years — verify against current ATO publications. This is general information, not advice.*

General market knowledge; no specific wiki source ingested yet.
