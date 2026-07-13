---
title: "Ackman's Pandemic CDS Trade (Feb-Mar 2020)"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [news, stocks, derivatives, options, risk-management, behavioral-finance]
aliases: ["Ackman COVID Hedge", "Pershing Square Pandemic Trade", "$27M to $2.6B CDS Trade", "100x Hedge"]
event_date: 2020-03-23
markets_affected: [stocks, bonds]
impact: high
verified: true
sources_count: 4
related: ["[[bill-ackman]]", "[[convex-tail-hedge-arbitrage]]", "[[fastest-profitable-trades]]", "[[credit-default-swaps]]", "[[credit-default-swap-index-arbitrage]]", "[[2020-03-12-black-thursday-crypto]]", "[[tail-risk-hedging]]", "[[crisis-alpha]]", "[[convexity]]", "[[options]]", "[[risk-management]]", "[[2008-global-financial-crisis]]"]
---

In late February and early March 2020, [[bill-ackman|Bill Ackman]]'s Pershing Square Capital Management spent approximately **$27 million** purchasing credit-default-swap protection on the CDX IG (investment-grade) and CDX HY (high-yield) corporate-bond indices. Three to four weeks later, as COVID-19 lockdowns spread and credit spreads exploded wider, Ackman closed the position for approximately **$2.6 billion** — a roughly **100× return on premium in ~30 days**, almost certainly the largest realized profit-on-premium of any single hedge in modern markets. The trade is the canonical 21st-century example of the "buy convex tail hedges when implied volatility is cheap relative to tail probability" framework — see [[convex-tail-hedge-arbitrage]] for the repeatable strategy generalization and [[fastest-profitable-trades]] for the broader pattern.

## Headline facts

| Field | Detail |
|-------|--------|
| **Date entered** | Late February 2020 (positions accumulated over ~2 weeks) |
| **Date exited** | March 12-23, 2020 (closed in tranches as spreads peaked) |
| **Premium paid** | ~$27 million |
| **Realized P&L** | ~$2.6 billion |
| **Multiple** | ~100× on premium; ~25-26× on realized return |
| **Holding period** | ~30 days |
| **Instruments** | CDX IG and CDX HY index credit-default swaps |
| **Counterparties** | Major investment-bank credit derivatives desks |
| **Reinvestment** | Proceeds redeployed into discounted equities (Hilton, Lowe's, Starbucks, Berkshire Hathaway) at March 2020 lows |

## Why this trade was possible

### Pre-pandemic credit-spread environment

In January and February 2020, the credit-derivatives market was pricing extreme complacency:

- **CDX IG (investment-grade index)**: spreads near 50bp, the tightest level since before the [[2008-global-financial-crisis]].
- **CDX HY (high-yield index)**: spreads near 280bp, also near multi-year tights.
- **Implied default probability** baked into these spreads was ~1-2% over a 5-year horizon — pricing-in essentially no recession risk.
- **VIX**: trading 12-15, near multi-year lows.

Credit-spread protection was, in Ackman's words later, "the lowest implied insurance cost in the history of credit derivatives." The premium-to-notional ratio was so low that even a modest widening of spreads would produce double-digit multiples on premium.

### The asymmetry recognition

Ackman's recognition was not a virology call or a recession forecast — it was a **convexity recognition**. He noticed:

1. Spreads were priced for benign continuation of late-cycle expansion.
2. Whatever shock arrived (he was watching COVID-19's progression in Wuhan), spreads had massive room to widen.
3. The cost to be wrong was bounded at the premium paid (~$27M).
4. The payoff if right was uncapped — at minimum, spreads would re-rate to 2008-comparable levels (CDX IG to 250bp+, CDX HY to 1500bp+), implying 30-100× returns on premium.

This is a textbook **positive-asymmetry tail-hedge** structure: bounded downside, unbounded upside, with the trade "free-rolling" because the premium cost was small relative to portfolio NAV (Pershing Square was ~$8B AUM at the time, so $27M was ~0.34% of NAV).

### The COVID catalyst

By late February:
- Wuhan lockdowns extended to other Chinese cities.
- Italy reported its first community transmission cluster (Feb 21).
- Markets initially shrugged; S&P 500 hit an all-time high on Feb 19.
- Ackman accumulated CDX IG and CDX HY protection over the following days as the situation in Italy escalated.

The first CDX move came in late February. By March 9 (the "Black Monday" oil shock following Saudi-Russia price war + accelerating pandemic news), CDX HY had blown out from 280bp to 600bp+. By March 23, CDX IG hit 150bp and CDX HY hit 870bp.

Ackman closed the position in tranches as spreads peaked. The realized P&L was approximately **$2.6 billion**.

## The mechanics: CDX index protection

### What CDX is

CDX is a basket of 100-125 individual corporate credit-default swaps, traded as a single index. Buying CDX protection means buying credit-default swaps on the index — paying a fixed quarterly premium (the spread, e.g., 50bp annualized) in exchange for receiving the loss notional if the basket members default.

Two main CDX series:

- **CDX IG (Investment Grade)**: 125 investment-grade reference entities (large US corporates).
- **CDX HY (High Yield)**: 100 high-yield reference entities (junk-rated corporates).

When credit spreads widen, the mark-to-market value of CDX protection *increases* — you've bought insurance whose price has gone up. Conversely, when spreads tighten, your protection bleeds value.

### Why CDX vs single-name CDS

Ackman bought CDX index protection rather than single-name CDS for three reasons:

1. **Liquidity**: CDX index trades in size measured in tens of billions of notional per day; single-name CDS markets are far thinner.
2. **Diversification of credit risk**: 100-125 names diversifies idiosyncratic credit risk, leaving pure macro spread risk.
3. **Lower premium per unit of notional protection**: CDX index spreads are typically tighter than the average single-name spread because of diversification.

### Position size estimate

Public reporting after the trade indicates Pershing Square bought protection on approximately **$71 billion in notional**:

- The entire $27M premium was the cost of carrying that protection at then-current spreads.
- A 50bp annualized premium on $71B notional is $355M/year. To pay only $27M, the position was either held for a partial year (held about 4-6 weeks before unwind) or structured at slightly lower-cost tenors.
- A move from 50bp to 150bp on $71B IG notional, plus a comparable spread move on the HY portion, generates billions in mark-to-market profit. The $2.6B realized number is consistent with this magnitude.

## Timeline

| Date | Event |
|------|-------|
| 2020-01-23 | Wuhan lockdown begins; markets initially unmoved. CDX IG ~50bp |
| 2020-02-19 | S&P 500 closes at all-time high. Ackman beginning to accumulate CDX protection |
| 2020-02-21 | Italy reports first community-transmission cluster |
| 2020-02-24 | S&P 500 -3.4%. Ackman continues accumulating |
| 2020-02-27 | S&P 500 -4.4%; CDX IG ~75bp, CDX HY ~400bp |
| 2020-03-09 | "Black Monday" — Saudi-Russia oil price war; S&P -7.6% (circuit breaker). CDX HY ~600bp |
| 2020-03-12 | "Black Thursday" — S&P -9.5%, oil -25%. CDX IG ~150bp, CDX HY ~750bp. Ackman begins unwinding |
| 2020-03-16 | S&P -12% (largest single-day drop since 1987). CDX HY ~870bp peak |
| 2020-03-18 | Ackman appears on CNBC: "Hell is coming." Tearful interview; meanwhile his hedge is paying off massively |
| 2020-03-23 | S&P bottoms at 2,237. Ackman has substantially closed the CDX positions for ~$2.6B realized |
| 2020-03-24+ | Ackman redeploys proceeds into discounted equities at the bottom |
| 2020-12-31 | S&P closes at 3,756 (+68% from Mar 23 low); Ackman's redeployed equity positions compound the gains |

## Why the trade is repeatable (and how)

The Ackman 2020 trade is widely cited but harder than it looks to repeat. The replicable framework — see [[convex-tail-hedge-arbitrage]] for the strategy page — has four components:

### 1. Identify periods of cheap convexity

The setup is not "predict the next pandemic." It's "identify periods where the implied cost of tail protection is low relative to a reasonable tail probability." Indicators:

- **CDX IG and HY at multi-year tights** (sub-100bp IG, sub-350bp HY).
- **VIX at multi-year lows** (sub-15).
- **MOVE index** (Treasury volatility) at multi-year lows.
- **Credit spreads disconnected from leading indicators** (yield curve inversion, ISM weakness, rising delinquencies).
- **Late-cycle behavior**: maximum complacency, narrow spread between corporate and sovereign yields.

When all of these align, convex tail protection is structurally cheap. The best entries in modern history: 2006-07 (pre-GFC), late 2019-early 2020 (pre-COVID), late 2021 (pre-2022 rate cycle).

### 2. Use CDX, not equity puts

CDX index protection has structural advantages over equity puts for the same convex-tail thesis:

- **Persistence**: CDS doesn't decay with theta the way OTM puts do. You pay periodic premium but the protection rolls forward.
- **Direct credit exposure**: Pandemic / recession risk is fundamentally a credit risk; CDS captures it directly.
- **Notional capacity**: CDX markets trade tens of billions per day; equity puts at large size have wider bid-ask.
- **No dividend / earnings risk**: equity puts get whipsawed by dividends and earnings; CDX doesn't.

For most non-institutional traders, equity index puts (SPY, QQQ deep-OTM puts) are the accessible analog. The principle is the same; the instrument is more expensive per unit of convexity.

### 3. Size for the bounded downside, not the unbounded upside

Ackman sized the trade at ~0.34% of fund NAV. This is critical: the trade can sit "underwater" for years (paying premium with no payoff) before the catalyst arrives. Sizing must be small enough that the carry cost doesn't force unwinding before the catalyst — but large enough that a payoff is meaningful.

Rule of thumb (per [[convex-tail-hedge-arbitrage]]): 25-100bp of NAV per quarter, rolled. Total cost-of-carry over a 5-year period: 5-20% of NAV. Average payoff in a tail year: 50-200% of NAV. Long-run expected return: positive, but with multi-year drawdown periods.

### 4. Have a redeployment plan for the proceeds

Ackman's full P&L was not just the $2.6B realized on the hedge — it was the $2.6B redeployed into discounted equities at the March 2020 bottom, which compounded dramatically over 2020-2021.

The hedge alone generates outsized returns. The hedge plus a pre-planned "buy panic with the proceeds" leg is the full Ackman playbook. This requires:

- Pre-identified high-quality businesses you would want to buy at deep discounts.
- Watchlist of price levels at which you would deploy.
- Capital structure that allows immediate redeployment (no LP redemption pressure during the panic).

This is the [[crisis-alpha]] component: the hedge is the entry ticket, but the real return comes from being a buyer when others are forced sellers.

## Why this trade is sometimes misunderstood

Some commentators framed Ackman's CNBC "Hell is coming" interview as front-running his own equity longs by talking the market down — a serious accusation that has been alleged but not proven. The reality:

- By the time Ackman appeared on CNBC (March 18), he had already substantially closed the CDX hedge.
- He had already begun redeploying into discounted equities.
- His statements on CNBC (advocating for shutdown, expressing alarm) were consistent with his prior actions — he didn't talk the market down to *enter* a short, he talked through it while deploying long capital at the bottom.

Whether his public commentary was strategically timed or genuinely alarmed is unknowable. The trade itself was constructed before his commentary and would have generated the same P&L without it.

## Lessons for repeatability

1. **Convex tail hedges are an asset class, not a one-time trade.** [[convex-tail-hedge-arbitrage]] generalizes the framework: scan for periods of cheap implied volatility / spreads, size for the carry cost over multi-year periods, treat the hedge as a permanent allocation rather than a tactical bet.
2. **The trade is found in instrument selection, not crystal-ball forecasting.** Ackman didn't predict COVID with any specificity; he priced the asymmetry between current spread levels and a reasonable distribution of recession-shock outcomes. CDX gave him 100× upside for 1× downside; that ratio was the trade.
3. **Pre-positioning matters more than reaction speed.** By the time the headlines broke, the trade was already on. Trying to enter once the panic begins captures fractional returns at much higher cost — 5-10× rather than 100×.
4. **Bounded downside + unbounded upside + large notional capacity + cheap entry = the four-corner trade.** When all four align, the trade size should be max-credible.
5. **Have a redeployment plan.** The full Ackman trade is the hedge + the post-crash equity buy. Without the redeployment leg, you have a great hedge return but you miss the compounding.
6. **Prepare for the "underwater" period.** The Ackman position would have looked "wrong" if COVID hadn't materialized — Pershing Square would have paid $27M (~0.34% of NAV) and walked away. Many tail hedges look "wrong" 80-90% of the time. The structural edge is in showing up consistently for the 10-20% of years when the payoff lands.

## Modern analogs and ongoing opportunities

Per [[2026-exploit-target-watchlist]] and [[ai-amplified-exploit-arbitrage]], the cheap-convexity setup recurs:

- **Crypto**: BTC and ETH put options at periods of compressed implied volatility (DVOL < 50, BVIV < 40). Cheap entry, large potential payoff in liquidation cascades or exploit-driven crashes. See [[liquidation-cascade-arbitrage]].
- **DeFi sympathy depegs**: synthetic stablecoin depeg basket per [[2026-04-kelp-stable-sympathy-depeg]].
- **Bridge config exploits**: per [[multi-dvn-bridge-config-arbitrage]].
- **VIX futures and options** during periods of generational vol-suppression (VIX < 12 for sustained period).
- **Sovereign CDS** on emerging markets where 5-year CDS is pricing benign continuation despite political stress.

The Ackman 2020 trade is the most-cited modern example. The framework is older — see [[fastest-profitable-trades]] for the historical precedents (Soros 1992, Druckenmiller, Krieger 1987, etc.).

## Related

- [[bill-ackman]] — trader entity page
- [[convex-tail-hedge-arbitrage]] — repeatable strategy generalization
- [[fastest-profitable-trades]] — pattern-extraction across history
- [[credit-default-swaps]] — instrument
- [[tail-risk-hedging]] — broader concept
- [[crisis-alpha]] — adjacent strategy
- [[convexity]] — pricing concept
- [[2008-global-financial-crisis]] — prior comparable spread-widening event
- [[2020-03-12-black-thursday-crypto]] — companion crypto-side event
- [[risk-management]] — sizing framework

## Sources

- Pershing Square Capital Management public letters and investor communications (2020-2021)
- [[bill-ackman]] entity page in this wiki
- Public reporting on the trade: Bloomberg, FT, WSJ post-crisis coverage
- CDX index data (March 2020 spread series)
- Pershing Square Holdings annual report (2020)
