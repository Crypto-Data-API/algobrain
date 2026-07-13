---
title: "XSP Options (Mini-SPX)"
type: market
created: 2026-05-06
updated: 2026-06-19
status: excellent
tags: [options, derivatives, sp500, stocks]
aliases: ["XSP", "Mini-SPX Index Options", "Mini-SPX"]
domain: [derivatives, options]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[spy-options]]", "[[ndx-options]]", "[[rut-options]]", "[[section-1256-contracts]]", "[[am-vs-pm-settlement]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[weekly-options]]", "[[vix]]", "[[options-portfolio-construction]]"]
---

XSP options are **Mini-SPX Index Options** — Cboe-listed, cash-settled, European-style [[index-options]] whose underlying is **1/10 the value of the S&P 500 Index**. They share the institutional structure of [[spx-options|SPX]] (cash settlement, no early assignment, [[section-1256-contracts|Section 1256]] 60/40 tax treatment) but at roughly the same notional size as a [[spy-options|SPY]] option contract. XSP exists specifically to bridge the gap: traders who want SPX's tax and settlement advantages but cannot or do not want to size up to full SPX-level notional now have a single-product solution.

## Overview

When SPX trades at 5000, XSP references a value of 500. With a $100 multiplier, one XSP contract therefore represents about $50,000 of S&P 500 exposure — essentially identical to one [[spy-options|SPY]] contract at the same time, and one-tenth of one [[spx-options|SPX]] contract.

The product was relaunched in 2020 by Cboe with full European-style, cash-settled mechanics and Section 1256 tax treatment, deliberately positioned as an institutional-quality alternative for traders who had previously been forced to use SPY for size reasons but were paying the tax penalty.

## Specifications

| Spec | Value |
|---|---|
| Underlying | Mini-SPX Index (1/10 of SPX) |
| Multiplier | $100 |
| Exercise style | European |
| Settlement | Cash |
| Settlement timing | PM-settled (uses 4:00pm ET closing index value) |
| Strike intervals | $1 increments common; $0.50 near-the-money on some weeklies |
| Tick size | $0.05 below $3.00 premium; $0.10 above |
| Trading hours | Regular session 9:30am–4:15pm ET; some extended-hours trading |
| Symbol | XSP |
| Tax treatment | [[section-1256-contracts|Section 1256]] (60/40) |

## Settlement & Exercise Mechanics

XSP inherits SPX's institutional mechanics, which are the entire reason to use it over [[spy-options|SPY]]:

- **European exercise** — XSP can be exercised *only* at expiration, never before. This eliminates the [[assignment-and-exercise|early-assignment risk]] that plagues short American options: no surprise assignment on a short call before an ex-dividend date, no deep-ITM short put getting exercised against you mid-trade. For multi-leg sellers this removes a whole category of operational risk.
- **Cash settlement** — at expiration, in-the-money XSP options settle to a *cash* difference (intrinsic value × $100 multiplier) rather than delivering shares. There is no underlying ETF position to manage, no shares to buy or sell, and no overnight gap risk from holding stock post-assignment.
- **PM settlement** — unlike SPX monthlies (which settle AM to the [[soq-settlement|SOQ]]), XSP settles to the official **4:00pm ET closing value** of the S&P 500 (the Mini-SPX index is simply 1/10 of that). Trading continues until the close on expiration day. This sidesteps the AM "settlement gap" risk where the [[am-vs-pm-settlement|opening-print SOQ]] can differ materially from the prior close. See [[am-vs-pm-settlement]] and [[cash-vs-physical-settlement]].
- **No dividend / pin risk** — because there is no deliverable ETF, there is no dividend-capture assignment risk and no [[assignment-and-exercise|pin risk]] from shares changing hands near the strike at expiry.

The combined effect — European + cash + PM — makes XSP "set-and-forget" relative to SPY: positions resolve cleanly into cash at the close with no assignment surprises.

## Tax Treatment (Section 1256)

The IRS treats XSP as a "broad-based stock index option" — same status as SPX, NDX, RUT, and VIX options:

- **60/40 blended rate** — every realized gain or loss is split 60% long-term and 40% short-term regardless of holding period.
- **Mark-to-market on Dec 31** — open positions are deemed-closed at year-end FMV.
- **3-year loss carryback** — XSP losses on Form 6781 can offset prior Section 1256 gains.
- **No traditional wash-sale concerns under §1091** in the same way as equities.

This is the entire point of using XSP over SPY for active traders: the underlying exposure is essentially identical, but the after-tax return can be several percentage points higher per year for short-term-heavy strategies. See [[section-1256-contracts]].

## Why XSP Exists (the gap it fills)

Before XSP's 2020 relaunch, traders had a forced trade-off:

- **Use SPY** — get 1/10 size, penny pricing, and broad listing, but pay standard equity tax and accept American-style early-assignment risk.
- **Use SPX** — get European exercise, cash settlement, and Section 1256 tax, but accept ~$500,000 notional per contract.

This was a real problem for, e.g., a $100K account running a delta-neutral premium-selling strategy: a single SPX contract was too much risk per unit, but trading SPY meant giving up a ~10-percentage-point tax advantage to active short-term traders. XSP closes the gap by combining SPX-style mechanics with SPY-style sizing.

## XSP vs SPY (tax and structure)

| Dimension | XSP | [[spy-options|SPY]] |
|---|---|---|
| Underlying | 1/10 SPX index value | SPDR S&P 500 ETF |
| Notional/contract | ~$50,000 (XSP 500) | ~$50,000 (SPY 500) |
| Exercise | European | American |
| Settlement | Cash | Physical (100 shares) |
| Tax | Section 1256 (60/40) | Standard equity |
| Early assignment | None | Yes |
| Dividend risk | None (no underlying ETF) | Yes (quarterly) |
| Tick size | $0.05 / $0.10 | $0.01 (penny pilot) |
| Strike granularity | $1 (mostly), $0.50 some | $1 broadly, $0.50 some |
| Liquidity | Lower (growing) | Highest in US options |

**Tax advantage example.** Trader with $50K of net XSP gains, top federal bracket:

- **SPY (standard equity, all short-term):** ~37% × $50K = ~$18,500.
- **XSP (Section 1256 60/40):** 60% × ~20% + 40% × ~37% = blended ~26.8% × $50K = ~$13,400.
- **After-tax saving: ~$5,100 (about 10% of gross P&L).**

For a frequent-trading premium-seller, this differential compounds significantly across years.

## XSP vs SPX (size)

| Dimension | XSP | [[spx-options|SPX]] |
|---|---|---|
| Notional/contract | ~$50,000 | ~$500,000 |
| Use case | $25K–$500K accounts | $500K+ accounts, institutions |
| Liquidity | Tens of thousands of contracts/day | Millions/day |
| Strike density | High at front month | Highest of any index option |
| Settlement | PM | AM (monthlies), PM (SPXW weeklies) |

XSP is essentially "SPX for retail size" — same tax, same exercise, same settlement type, just 1/10 of the notional and (currently) lower liquidity.

## ITPM Use Cases

[[itpm|ITPM]]-style portfolios use XSP in specific contexts:

- **Mid-size accounts** — books between roughly $50K and $500K where SPX would over-concentrate and SPY would tax-drag.
- **Tactical adjustments** — fine-tuning index exposure in 1/10 SPX increments without leaving Section 1256.
- **Tax-loss harvesting partner to SPY** — closing a SPY losing position and immediately opening XSP can preserve market exposure while crystallizing the loss; whether this is "substantially identical" for [[wash-sale-rules-options]] purposes is a tax-advisor question, but the practitioner reading is that the products are not equivalent for §1091.
- **Diagonals and calendars** — building multi-leg structures at retail size while retaining the European-exercise benefit of no early assignment.

## Typical Strategies

Because XSP shares SPX's mechanics, the same structures apply at 1/10 the notional:

- **Defined-risk premium selling** — [[iron-condor|iron condors]] and [[short-strangle|strangles]] sized for $25K–$500K accounts that capture the [[volatility-risk-premium]] without early-assignment risk.
- **Granular hedging** — long puts or [[put-spread|put spreads]] in 1/10-SPX increments, letting a mid-size book fine-tune index hedge size where one full [[spx-options|SPX]] contract would over-cover.
- **Calendars and diagonals** — multi-leg term-structure trades at retail size with European exercise.
- **Tax-aware substitution** — running an SPY-equivalent strategy in XSP to keep [[section-1256-contracts|Section 1256]] treatment (the core reason the product exists).

## Greeks Behavior

XSP's [[options-greeks|Greeks]] are *identical in character* to SPX's because the underlying is literally the same index scaled by 1/10 — only the dollar magnitudes shrink by ten:

- **[[delta]]** — one full-delta XSP contract carries ~$50K of directional notional (vs ~$500K for [[spx-options|SPX]]), so a mid-size book can fine-tune index delta in $50K increments rather than being forced into $500K jumps. This granularity is one of XSP's underrated practical advantages.
- **[[gamma]]** — same shape as SPX gamma at 1/10 the dollar scale; short-gamma XSP positions decay and adjust just like the SPX analog but with proportionally smaller P&L swings, which suits smaller accounts that need tighter risk control.
- **[[theta]]** — same volatility-risk-premium harvest as SPX per unit of notional; the European/cash mechanics mean theta accrues cleanly to expiration with no early-assignment interruption.
- **[[vega]]** — XSP vega tracks SPX/[[vix|VIX]]-implied volatility one-for-one (scaled). There is no separate XSP vol regime to learn — it *is* the S&P 500 vol surface at 1/10 size.
- **Skew** — XSP's [[volatility-surface|surface]] mirrors SPX's well-documented steep equity-index put skew; the same skew-aware structuring that applies to SPX applies here.

Because the Greeks are SPX's at 1/10 scale, every SPX risk model, sizing rule, and surface intuition transfers directly — XSP requires no new mental model, only a notional rescale.

## Common Spread Structures

XSP supports the full SPX structure set at retail size, with the European/cash mechanics removing assignment complexity:

- **[[iron-condor|Iron condors]]** — sell an OTM put spread and an OTM call spread to harvest the [[volatility-risk-premium]] within a range; the headline retail premium-selling structure on XSP, sized for $25K-$500K accounts.
- **[[short-strangle|Short strangles]]** — sell an OTM put and OTM call (undefined risk) for maximum theta; viable on XSP but typically run smaller given account size.
- **[[bull-put-spread|Put credit spreads]]** / **[[bear-call-spread|call credit spreads]]** — single defined-risk verticals to express directional-plus-premium views, monetizing the put skew.
- **[[calendar-spread|Calendars]] and [[diagonal-spread|diagonals]]** — term-structure trades at retail size; the European exercise is a genuine edge here because there is no risk of the short leg being assigned before the long leg matures.
- **[[butterfly-spread|Butterflies]] / [[broken-wing-butterfly|broken-wing butterflies]]** — pin-the-range structures that benefit from clean cash settlement to the close.
- **[[put-spread|Put-spread]] hedges** — granular index protection in 1/10-SPX increments for a mid-size book where one full SPX put would over-hedge.

The recurring theme: XSP lets a smaller account run the *same* defined-risk and term-structure playbook an institution runs in SPX, with no early-assignment risk and at one-tenth the notional.

## Risks

- **Liquidity is the main weakness** — wider spreads and thinner open interest than SPX or SPY mean operational slippage is structurally higher (detailed below).
- **No penny pricing** — XSP's $0.05/$0.10 tick is coarser than SPY's penny ticks; on a single short-dated round trip the tick cost can outweigh the tax advantage (the tax edge dominates only on an annualized, multi-trip basis).
- **Settlement-print risk** — although PM settlement avoids the AM [[soq-settlement|SOQ]] gap, expiration still resolves to a single 4:00pm closing index print; a sharp close-of-day move can settle a position differently from where it traded at 3:55pm.
- **Capacity ceiling for large books** — very large positions may exhaust XSP depth and are better executed in SPX; XSP is sized for retail and lower-mid-tier institutional use.
- **Lower strike granularity at far months** — strike density thins beyond the front expirations, constraining fine-tuned structures in longer-dated trades.
- **Tax law is not advice** — Section 1256 treatment depends on continued "broad-based index option" qualification and the trader's circumstances; the substantially-identical question vs SPY for [[wash-sale-rules-options|wash-sale]] purposes is a tax-advisor matter.

## Liquidity Caveats

XSP's main weakness is liquidity relative to SPX or SPY:

- **Bid/ask spreads** are wider than SPX or SPY at equivalent moneyness, particularly on far-month or far-OTM contracts.
- **Open interest** is lower; less depth at any given strike.
- **Market-maker presence** is solid but thinner than the deepest US options — expect to work limit orders, not market orders.
- **Trend** — volume has been growing year-over-year since 2020, particularly as retail traders become aware of the tax advantage. The product is not as deep as SPX or SPY but is liquid enough for typical retail and lower-mid-tier institutional sizes.

For very large positions, traders may still prefer to "trade up" to SPX. For small tactical positions, SPY's penny pricing can sometimes outweigh XSP's tax advantage on a single round trip — but rarely on an annualized basis.

## Related

- [[index-options]] — overview of the index-options franchise
- [[options]] — options fundamentals
- [[spx-options]] — full-size sibling
- [[spy-options]] — physically-settled retail alternative
- [[ndx-options]] — Nasdaq-100 index-options sibling
- [[rut-options]] — Russell 2000 index-options sibling
- [[vix]] — implied volatility on the S&P 500
- [[section-1256-contracts]] — tax framework
- [[am-vs-pm-settlement]]
- [[soq-settlement]] — the AM print XSP avoids
- [[cash-vs-physical-settlement]]
- [[assignment-and-exercise]] — early-assignment risk XSP eliminates
- [[american-vs-european-options]]
- [[weekly-options]]
- [[options-portfolio-construction]]
- [[options-position-sizing]]
- [[options-greeks]], [[delta]], [[gamma]], [[theta]], [[vega]] — Greeks behavior (SPX at 1/10 scale)
- [[volatility-surface]], [[volatility-risk-premium]] — vol context
- [[iron-condor]], [[short-strangle]], [[bull-put-spread]], [[bear-call-spread]], [[calendar-spread]], [[diagonal-spread]], [[butterfly-spread]], [[put-spread]] — common structures

## Sources

- Cboe XSP product specifications (cboe.com/tradable_products/sp_500/mini_spx_options)
- IRC Section 1256 — Internal Revenue Code
- Cboe XSP relaunch documentation (2020)
