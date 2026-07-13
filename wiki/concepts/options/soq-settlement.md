---
title: "SOQ Settlement (Special Opening Quotation)"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, market-microstructure, indicators]
aliases: ["SOQ", "Special Opening Quotation", "SOQ Settlement"]
related: ["[[index-options]]", "[[spx-options]]", "[[ndx-options]]", "[[rut-options]]", "[[vix-options]]", "[[xsp-options]]", "[[am-vs-pm-settlement]]", "[[cash-vs-physical-settlement]]", "[[pin-risk]]", "[[gap-risk]]", "[[max-pain]]", "[[options-pinning]]", "[[liquidity-evaporation]]", "[[occ]]", "[[cboe]]", "[[american-vs-european-options]]", "[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[circuit-breakers]]"]
domain: [derivatives, options, market-microstructure]
prerequisites: ["[[index-options]]", "[[am-vs-pm-settlement]]"]
difficulty: intermediate
---

The **Special Opening Quotation (SOQ)** is the settlement value used for AM-settled cash-index options — most importantly traditional monthly [[spx-options|SPX]], [[ndx-options|NDX]], [[rut-options|RUT]], and the cash-settled [[vix-options|VIX]] options. Unlike the regular index level (which is computed from real-time component prices), the SOQ is a one-time number derived from the **opening prints** of every index component on expiration morning, published by Cboe under ticker symbols such as **SET** (SPX), **NDS** (NDX), **RLS** (RUT), and **VRO** (VIX). When index components open in an orderly, staggered way the SOQ closely tracks the prior close; when components open with gaps, halts, or LULD bands the SOQ can print percent-points away from where the index marked Thursday afternoon — generating settlement losses on AM-settled positions that no intraday-vol model would have flagged.

## Overview

Cash-settled index options need a single, unambiguous reference value at expiration. Two methods are used in US markets — see [[am-vs-pm-settlement]] for the full split:

| Settlement style | Reference value | Products |
|---|---|---|
| **AM (SOQ)** | Special Opening Quotation, Friday morning | SPX (3rd-Friday monthly), NDX, RUT, VIX |
| **PM (close)** | 4:00 pm ET official close of index | SPXW (weeklies, 0DTE), XSP, NDXP, RUTW |

The SOQ exists because AM-settled contracts stop trading at the **prior afternoon's close** (Thursday, for a Friday-expiring SPX monthly). The contract is dormant overnight, then settles to a value computed once Friday's component opens are in. The published symbol per index:

| Index | SOQ ticker | Underlying components used |
|---|---|---|
| [[spx-options\|SPX]] | **SET** | 500 S&P 500 stocks at NYSE/Nasdaq opens |
| [[ndx-options\|NDX]] | **NDS** | 100 Nasdaq-100 stocks at Nasdaq open |
| [[rut-options\|RUT]] | **RLS** | ~2,000 Russell 2000 stocks at NYSE/Nasdaq opens |
| [[vix-options\|VIX]] | **VRO** | SPX option prices at the open (not S&P 500 stocks directly) |

The SOQ is a real, published number — but it is a *derived* number from a one-time auction process, not a tradeable market print. That detail is the source of every interesting risk story attached to SOQ settlement.

## Mechanism / How It Works

### Standard equity-index SOQ (SET, NDS, RLS)

For SPX (and analogously for NDX and RUT) the SOQ is calculated from the **first regular-session trade** of each component on its primary listing exchange, weighted by the index's standard methodology:

1. **Final trading session** — the AM-settled contract closes Thursday at 4:00 pm ET. After Thursday's close it cannot be traded; positions are locked overnight.
2. **Friday open** — at 9:30 am ET the underlying primary exchanges (mostly NYSE and Nasdaq) begin their opening auctions for index components.
3. **Component opening prints** — each component prints its first regular-way trade, typically within a few seconds of 9:30 for the largest names but with a long tail for smaller, less-liquid components. Some components are subject to **LULD price-band openings** or **regulatory halts**, which delay their first print by minutes to hours.
4. **SOQ computation** — once every component has an opening print (or a fallback value if a component fails to open), the index methodology is applied to those opening prices and a single SOQ value is published. Cboe disseminates SET (the SPX SOQ) typically by 11:00 am-12:00 pm ET on calm days, later on stressed days.
5. **Cash settlement** — every AM-settled contract is then settled to the SOQ value. Long ITM options receive `(SOQ − strike) × 100` for calls or `(strike − SOQ) × 100` for puts; short positions are debited the same amount.

The methodology is documented in Cboe's *Special Opening Quotation* product specifications and the index providers' (S&P, Nasdaq, FTSE Russell) calculation manuals.

### VIX SOQ (VRO) — a different mechanism

The VIX SOQ is **not** computed from a basket of stocks. The VIX index itself is a calculation derived from SPX option prices, so its settlement value must reference SPX *option* prices — specifically those struck around the VIX expiration date (30 days forward). Mechanics:

1. **VIX options expire on Wednesday morning.** They cease trading Tuesday afternoon at 4:00 pm ET.
2. **Wednesday open** — Cboe runs a special opening auction in the relevant SPX options series (the strip of SPX options used in the VIX formula, with ~30 days to their own expiration).
3. **VRO calculation** — the VIX formula is applied to the opening prices/midpoints of the SPX options in the strip, producing a single VIX settlement value (VRO).
4. **Cash settlement** — VIX option payoffs are then computed against VRO.

Because VRO depends on **SPX option opening prices** rather than on the VIX index itself, three quirks emerge:

- **VRO can differ materially from spot VIX** at the open, even when SPX itself has barely moved, because thin SPX-option opening auctions can produce idiosyncratic mids.
- **Far-OTM SPX strikes** participate in the VIX formula. Opening auctions in those wings are less liquid than near-the-money strikes, so a small number of trades can swing VRO.
- **Strategic flow** can target the auction. The Griffin & Shams (2017) paper *Manipulation in the VIX?* documented unusual SPX-option volume on VIX-settlement mornings consistent with attempts to influence VRO. Whether this reflects manipulation, hedging, or both remains contested, but the structural vulnerability is real and well-documented.

[[xsp-options|XSP]] (mini-SPX) and the newer NDXP, RUTW, etc. are PM-settled and avoid the SOQ machinery entirely.

### Why SOQ ≠ Thursday's close

The settlement value is anchored to component opens, not to the index level at the prior close. Three structural sources of divergence:

1. **Overnight news.** Anything that moves equity futures between 4:00 pm Thursday and 9:30 am Friday — Asian/European session reactions, earnings pre-announcements, geopolitical news, leaked Fed minutes — is reflected in component opens.
2. **Staggered openings.** The S&P 500 does not open as a single basket. Mega-caps print within seconds; smaller-cap components can take 5-30 minutes, occasionally hours under LULD. The SOQ blends opens that occur over a window, not a snapshot.
3. **Auction microstructure.** Opening auctions print at the level that maximizes matched volume, not at the prior close. On stress mornings, indicative prices in the auction widen sharply and final auction prints can land far from any continuous-trading reference.

The position-level consequence: an AM-settled option that looked safe at Thursday's close can settle deep in the money to a SOQ that prints 2-5% (or more) away from the Thursday mark. This is overnight [[gap-risk|gap risk]] expressed through the SOQ mechanism.

### Settlement-value cheat sheet

The single most useful operational table — which value settles which contract, and when the exposure window closes:

| Product | Settlement style | Settles to | Last trade | Exposure window |
|---|---|---|---|---|
| SPX (3rd-Fri monthly) | AM (SOQ) | **SET** | Thu 4:00 pm ET | Thu close → Fri ~10 am SOQ print |
| SPXW (weekly / 0DTE) | PM (close) | Fri 4:00 pm index close | Fri 4:00 pm ET | continuous to close |
| NDX (monthly) | AM (SOQ) | **NDS** | Thu 4:00 pm ET | overnight gap |
| RUT (monthly) | AM (SOQ) | **RLS** | Thu 4:00 pm ET | overnight gap (heaviest tail — ~2,000 names) |
| [[vix-options\|VIX]] | AM (SOQ) | **VRO** | Tue 4:00 pm ET | overnight + thin SPX-option auction |
| [[xsp-options\|XSP]], NDXP, RUTW | PM (close) | Fri 4:00 pm close | Fri 4:00 pm ET | none overnight |

The interpretive rule: any row whose "settles to" column is a ticker (SET/NDS/RLS/VRO) rather than the 4:00 pm close carries SOQ gap risk and should be flat by the prior afternoon's bell if the residual extrinsic is small.

### Worked example — held SPX put through the SOQ window (illustrative)

> *Numbers below are illustrative, not market data.* A trader is short one SPX 5000-strike AM-settled monthly put. Thursday close: SPX at 5120, so the put is 120 points OTM and marked near $0.40 of residual extrinsic — "basically expiring worthless." The trader leaves it on to "harvest the last few dollars."
>
> Overnight, an offshore session sells off and US futures gap down ~3%. Friday's component opens stagger in; the **SET** prints at 4965. The put is now 35 points ITM and settles to `(5000 − 4965) × 100 = $3,500` debit per contract — versus the ~$40 of credit the trader hoped to keep. There was no continuous-trading opportunity to react: the position was locked at Thursday's close and settled to a number that did not exist until ~10 am Friday.
>
> The lesson is structural, not directional: the loss came not from being wrong about direction but from holding a closed-position overnight gap that the SOQ converts into a settlement event. Closing the put Thursday for ~$0.40 would have capped the outcome.

## Empirical Evidence / Examples

### August 24, 2015 — China devaluation flash-crash open

The canonical SOQ-stress event. After the PBOC's surprise weekend yuan devaluation, US futures dropped overnight; on Monday August 24 the cash-equity open was chaotic. Hundreds of S&P 500 components and ETFs were halted under LULD bands at the open, and over 1,200 trading halts occurred in the first hour of trading. SPX futures fell ~5%, but the cash SPX printed an open print near 1893 — about 5% below Friday's close — and the SOQ for any AM-settled August expirations (and for any expiration whose SOQ window overlapped the dislocation) reflected those staggered, halted opens. Many AM-settled put positions that had been comfortably out-of-the-money on Friday's close settled deep ITM. The episode prompted SEC review of LULD rules and is referenced in essentially every modern Cboe and S&P discussion of opening-auction microstructure.

### Brexit referendum — June 24, 2016

UK leave vote announced Thursday night UK time. US futures dropped 5%+ overnight. SPX cash opened down ~2.5% on Friday June 24, with the SOQ for that morning's AM-settled options reflecting the gap. Traders carrying AM-settled SPX Friday positions through Thursday's close were settled to a SOQ they had no opportunity to react to.

### August 5, 2024 — yen-carry unwind

The largest single-day VIX spike in history (see [[vix-august-2024-spike]]). The Monday open saw VIX gap from a Friday close near 23 to over 50 within the first 30 minutes. While most index-options expirations that week were PM-settled SPXW, the broader lesson — that gap-and-go opens can produce settlement values multiple standard deviations from the prior mark — applies directly to the SOQ mechanism on monthly OPEX Fridays.

### VIX SOQ volume anomalies (2017 onward)

Griffin & Shams (2017, *Review of Financial Studies*) documented systematic spikes in SPX option volume at the open on VIX expiration mornings, concentrated in the far-OTM strikes that have outsized influence on the VIX formula. Subsequent academic and SEC scrutiny has not produced enforcement actions, but the empirical pattern has persisted in subsequent samples. The structural takeaway: **a derived settlement value computed from a thin auction is vulnerable to flow concentrated in that auction**, regardless of intent.

### Routine "small" SOQ deviations

Even on uneventful weeks, the SET (SPX SOQ) typically prints a few index points away from the Thursday close. Cboe data shows the median absolute deviation between Thursday close and Friday SET is roughly 0.2-0.4% — small in normal weeks, but compounded across years of monthly expirations the cumulative drag (or boost) on AM-settled positions is non-trivial. Empirical practitioner studies (Tastytrade, OptionMetrics) find that AM-settled monthly SPX options have systematically wider realized terminal P&L distributions than PM-settled SPXW weeklies, consistent with the SOQ adding a small-but-real overnight gap component.

## Implications for Risk

### SOQ-deviation regimes and the position response

| Regime | Typical SET-vs-Thu-close gap | Driver | Position response |
|---|---|---|---|
| Calm OPEX week | ~0.2–0.4% | staggered orderly opens | residual extrinsic usually safe; still close large short tails |
| Catalyst overnight (Fed, CPI, earnings cluster) | 0.5–2% | repricing in component opens | close all material AM shorts Thursday |
| Macro gap (Brexit-type) | 2–5% | overnight regime shock | never carry AM shorts into known catalysts |
| Halt-cascade open (Aug 2015-type) | 5%+, non-equilibrium | LULD / [[circuit-breakers]] | SOQ may differ from any tradeable print; tail bet, not VaR |

The table is the operational heart of the page: the further right the regime, the more the SOQ behaves like a discrete jump rather than a Gaussian sample, and the less any intraday hedge or VaR scenario protects the held position.

### Mitigation playbook

| Mitigation | What it removes | Cost |
|---|---|---|
| Close AM shorts by Thursday bell | the entire overnight SOQ window | forgo last few dollars of extrinsic |
| Trade PM-settled cousins ([[xsp-options\|XSP]], SPXW) instead | SOQ machinery entirely | slightly different sizing / tax |
| Convert AM monthly to a defined-risk spread | unbounded SOQ tail on the short leg | pay for the long wing |
| Model VIX P&L vs a VRO distribution | false precision of "VRO = spot VIX" | analytical effort |
| Flag any AM/PM cross as its own risk line | hidden uncovered gap exposure | bookkeeping discipline |

### Risk of SOQ vs continuous-trading risk

The SOQ converts a final 17.5-hour window (Thursday 4:00 pm to Friday ~10:00 am) into a discrete settlement event. For a short option carried into Thursday's close, that window is a closed-position gap with no hedging available — exactly the structure that makes [[gap-risk|gap risk]] systematic. The position-level rule is simple: **any AM-settled short position with material risk should be closed by Thursday's bell**, not held into expiration. The few cents of remaining extrinsic value are not worth the SOQ-distribution exposure.

### Calendar / diagonal mismatch

A spread that pairs an AM-settled monthly with a PM-settled weekly is **structurally mismatched**. The AM leg is settled to Friday's SOQ at ~10 am; the PM leg is settled to Friday's 4:00 pm close. In between, the position has uncovered residual delta and gamma that the spread's design assumed away. Risk-budgeted books (see [[options-risk-budgeting]]) should flag any AM/PM cross as a separate line item, not as a covered spread.

### VIX-options specific risk

VIX option positions face the **VRO basis risk**: VRO can differ from spot VIX at the open by several VIX points, even when SPX has barely moved, because the SPX-option strip used in the calculation reflects illiquid opening auctions. Long VIX call positions sized to "VIX hits 25" can settle at VRO 22 or VRO 28 depending on auction microstructure on settlement morning. Practitioner rule: model VIX-options P&L against a distribution of VRO values, not against the assumption that VRO = spot VIX at the open.

### Halt-cascade interaction

When LULD halts, regulatory halts, or [[circuit-breakers|market-wide circuit breakers]] occur during the SOQ window, the SOQ calculation stretches: components that fail to open under their first LULD band may not print until 10:00 am or later. The published SOQ in such cases blends "early" component opens (immediately reflecting the news) with "late" component opens (printing into a partially-recovered tape). The result is a SOQ that may differ from any continuously-tradeable SPX print. This is a cousin of [[liquidity-evaporation]] — the settlement value reflects a market that effectively wasn't trading.

### Pinning and SOQ

[[options-pinning|Strike pinning]] dynamics work differently for AM vs PM settlement. PM-settled options are pinned by intraday dealer hedging through Friday afternoon; AM-settled options' settlement is fixed by Thursday's close and the Friday open auctions, so dealer hedging Friday afternoon does not affect their settlement. As a result, AM-settled monthly OPEX positions have a different terminal-distribution shape than PM-settled weekly positions on the same underlying — relevant for any [[options-portfolio-construction|portfolio]] mixing the two.

## Common Mistakes / Pitfalls

1. **Treating Thursday's close as the settlement value.** AM-settled contracts settle to the SOQ, not to Thursday's close. The exposure window extends through Friday's component opens. Closing AM positions Thursday afternoon is the canonical mitigation.
2. **Mixing AM and PM legs in a single spread.** Calendars and diagonals that pair monthly AM with weekly PM legs are *not* covered spreads at expiration — they have uncovered exposure during the 6.5-hour gap between SOQ print and 4:00 pm close.
3. **Assuming VRO ≈ spot VIX.** The VIX SOQ is a separate calculation from a separate auction. Hedges sized to the live VIX index can settle several VIX points away.
4. **Ignoring SOQ on stress days.** When a Sunday-night gap appears in the futures, the Friday-morning SOQ on a held AM position can print further from the prior mark than any intraday VaR scenario considered.
5. **Trusting the SOQ as a tradeable price.** The SOQ is a published settlement value, not a market quote. There is no opportunity to "trade against" the SOQ — by the time it prints, AM-settled positions are already settled.
6. **Forgetting the LULD-halt interaction.** A SOQ computed during a halt-cascade morning (August 24, 2015 being the canonical case) reflects opening auctions that themselves print at non-equilibrium prices. Modeling SOQ as a Brownian-motion sample is wrong for those days.
7. **Underpricing SOQ tail risk.** Cboe stress disclosures and historical SET-vs-Thursday-close distributions both show tails far heavier than Gaussian. Any short premium book carrying AM-settled positions over weekends with known catalysts (Fed, earnings season, geopolitics) is taking a tail bet on the SOQ distribution.

## Related

- [[index-options]] — the parent product class
- [[spx-options]], [[ndx-options]], [[rut-options]] — AM-settled monthlies use SOQ
- [[vix-options]] — SOQ via VRO (computed from SPX options, not stocks)
- [[xsp-options]] — PM-settled cousin, no SOQ exposure
- [[am-vs-pm-settlement]] — the broader split this fits inside
- [[cash-vs-physical-settlement]] — settlement-type contrast
- [[american-vs-european-options]] — exercise-style distinction
- [[pin-risk]] — position-level uncertainty at expiration
- [[options-pinning]] — the empirical price-clustering phenomenon
- [[gap-risk]] — overnight-gap mechanism that produces SOQ deviations
- [[max-pain]] — open-interest-weighted strike concept
- [[liquidity-evaporation]] — auction-thinness mechanism that compounds SOQ stress
- [[circuit-breakers]] — halt mechanism interacting with SOQ
- [[options-portfolio-construction]] — portfolio-level handling of AM/PM mix
- [[options-risk-budgeting]] — flagging AM/PM mismatch as separate risk

## Sources

- Cboe Global Markets — *Special Opening Quotation* product specifications and methodology documentation (cboe.com).
- Cboe Global Markets — *VIX Index Settlement Calculation* white paper, including the SPX-option strip used to compute VRO.
- Griffin, J. and Shams, A. (2017). "Manipulation in the VIX?" *Review of Financial Studies*. Empirical study of unusual SPX-option volume on VIX expiration mornings.
- SEC and Cboe joint statements on the August 24, 2015 trading-halt cascade and its interaction with index-option settlement.
- S&P Dow Jones Indices — *S&P 500 Index Methodology*, on the calculation procedure inherited by the SOQ.
- OCC settlement and exercise rules for cash-settled index options.
- [[itpm-options-portfolio-management]] — institutional treatment of AM/PM settlement choice.
- [[tastytrade-spx-research]] — empirical comparisons of AM-settled vs PM-settled SPX terminal distributions.
