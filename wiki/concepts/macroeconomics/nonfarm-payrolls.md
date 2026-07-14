---
title: "Nonfarm Payrolls"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [macro, volatility, options, calendar-effects, bonds]
aliases: ["NFP", "Non-Farm Payrolls", "Non Farm Payrolls", "Nonfarm Payrolls Release", "Jobs Report", "Employment Situation Report", "Payrolls"]
domain: [macroeconomics, market-microstructure]
prerequisites: ["[[unemployment-rate]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[fomc-meetings]]", "[[cpi-release]]", "[[implied-volatility]]", "[[volatility-term-structure]]", "[[us-treasury-bonds]]", "[[interest-rate-risk]]", "[[options-concentration-risk]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[expiration-laddering]]", "[[macro-events]]", "[[options-portfolio-construction]]", "[[fed-funds-futures]]", "[[vix-august-2024-spike]]"]
---

The **Employment Situation Report** — colloquially **Nonfarm Payrolls (NFP)** — is the US Bureau of Labor Statistics' monthly labor-market release, published at **8:30 AM Eastern on the first Friday of each month** for the prior month's data. Alongside [[cpi-release|CPI]] and [[fomc-meetings|FOMC]], it is one of the three largest scheduled-vol events on the US calendar. For an options book, NFP is a **once-a-month vol cliff** — front-end [[implied-volatility|IV]] ramps into the Friday print, the surface inverts at the front, and IV crushes within seconds of 8:30. Concentration of multiple positions in the expiry covering NFP is one of the most common stacked-event exposures in options books and a recurring cause of [[options-concentration-risk|correlated event blow-ups]] when the print delivers a tail outcome — most recently the **August 2, 2024 NFP miss** that detonated the [[vix-august-2024-spike|August 5 vol spike]].

## Overview

The Employment Situation Report contains two surveys conducted in parallel:

- **Establishment (payroll) survey** — the headline NFP number (jobs added/lost), average hourly earnings (AHE), and average weekly hours
- **Household survey** — the unemployment rate, labor-force participation, and demographic breakdowns

Markets focus on:

- **Headline NFP** vs consensus (jobs change in thousands)
- **Two-month revisions** (often as large as the headline figure itself, frequently changing the trajectory implied by the new print)
- **Unemployment rate** (the trigger for the [[sahm-rule|Sahm Rule]] recession indicator at 0.5% off the trough)
- **Average hourly earnings YoY** (the wage-inflation proxy the [[federal-reserve|Fed]] watches)
- **Labor-force participation rate**

The report is a **rates event** that propagates to FX and equity vol surfaces in the first minute of trading. NFP is structurally noisier than [[cpi-release|CPI]] (typical absolute miss vs consensus is 60–80k jobs against a ~150k baseline), which makes the IV ramp and post-print crush both larger in magnitude than the typical CPI cycle.

### Release at a glance

| Attribute | Detail |
|---|---|
| Publisher | US Bureau of Labor Statistics (BLS) |
| Release time | 8:30 AM Eastern |
| Cadence | First Friday of each month (12/year), for prior-month data |
| Headline figure | Net change in nonfarm payroll employment (thousands), establishment survey |
| Key sub-components | Unemployment rate, average hourly earnings (AHE) YoY, participation, two-month revisions |
| Primary market | US front-end rates (2-year UST); propagates to FX, equities, gold |
| Lead-in indicators | ADP (Wed), JOLTS (lagged), initial jobless claims (Thu) |
| Options signature | Front-week IV ramp into the print, term-structure inversion, IV crush within seconds of 8:30 |

The four numbers traders parse on the print, roughly in order of market sensitivity: **(1)** unemployment rate when near a regime threshold (e.g. the [[sahm-rule|Sahm Rule]]), **(2)** headline NFP vs consensus, **(3)** two-month revisions (often as large as the headline), **(4)** average hourly earnings as the wage-inflation read.

## How It Works

### Schedule and cadence

- **Frequency**: monthly, 12 prints per year
- **Time**: 8:30 AM Eastern
- **Day**: first Friday of the month, with rare exceptions when the first Friday falls on a holiday
- **Reference period**: data for the *prior* calendar month
- **Pre-release indicators**: ADP National Employment Report (Wednesday before, smaller market reaction), JOLTS (a month lag, released earlier in the cycle), weekly initial jobless claims (Thursday before each NFP, can move markets if a sharp deviation)

The first-Friday cadence creates a strict scheduling property for options expiries: the **monthly SPX expiry (3rd Friday)** is roughly two weeks after NFP, and weekly Friday expiries can fall *on* NFP day. This makes the weekly Friday cycle covering NFP a high-IV expiry every month — a structurally identifiable concentration target.

### Effect on the vol surface

The IV signature is a sharper, larger-magnitude version of the [[cpi-release|CPI surface signature]]:

- **Pre-print ramp**: front-week SPX IV typically rises +1 to +3 absolute vol points in the 3 trading days before NFP, larger than the CPI ramp because of the higher absolute miss volatility
- **Term-structure inversion**: the Friday-expiry cycle covering NFP often trades 2–4 vol points above the next weekly expiry on the Thursday close
- **Post-print crush**: 1–4 vol points come out of front-week IV within 5–15 minutes of 8:30, with *most of the move in the first 30 seconds*
- **0DTE NFP-Friday options**: weekly options expiring on NFP Friday have shown some of the highest implied-move-to-realized-move ratios in the SPX 0DTE complex
- **No-crush outcomes**: when NFP misses by >100k or revisions sharply revise the trajectory, IV does *not* crush — it can re-ramp as the print re-prices the expected [[fed-funds-futures|Fed path]]

### Effect on rates, FX, and equities

NFP is most directly a **front-end rates event**:

- **2-year UST yields**: 8–25 bp moves in the first 30 minutes on surprise prints; the most NFP-sensitive Treasury point
- **10-year UST yields**: smaller move, longer half-life
- **USD**: hot NFP → dollar stronger; soft NFP → dollar weaker; DXY moves 0.5–1.5% in the first hour are typical on surprise prints
- **Gold**: hot NFP (real rates up) → gold lower; soft NFP → gold higher
- **SPX**: directional reaction depends on the regime. In *late-cycle* regimes (when the market is worried about an imminent slowdown), a *miss* is bad for stocks (recession fear) and a *beat* is also bad for stocks (no Fed cuts). In *expansion* regimes, a beat is good for stocks. The asymmetry is the single hardest part of trading NFP directionally
- **Small caps**: [[iwm|IWM]] often shows the largest beta-amplified reactions to NFP because small-caps are more sensitive to the rate path

#### Cross-asset reaction matrix

Typical first-hour direction on a **hot** (above-consensus) print, and the mirror for a **soft** print. Magnitudes are *indicative* and regime-dependent — the equity sign in particular flips by regime (see the note below).

| Asset | Hot NFP (beat) | Soft NFP (miss) | Notes |
|---|---|---|---|
| 2-year UST yield | Up (most sensitive point) | Down sharply | 8–25 bp first-30-min moves on surprises |
| 10-year UST yield | Up, smaller | Down, smaller | Longer half-life |
| USD / DXY | Stronger | Weaker | 0.5–1.5% first-hour on surprises |
| Gold | Lower (real rates up) | Higher | Inverse to real yields |
| SPX / NDX | **Regime-dependent** | **Regime-dependent** | Expansion: beat good; late-cycle: beat *and* miss can be bad |
| Small caps ([[iwm\|IWM]]) | Beta-amplified version of SPX | Beta-amplified | Most rate-path-sensitive |
| Front-week equity IV | Crushes (in-line) or re-ramps (tail) | Crushes or re-ramps | See [Effect on the vol surface](#effect-on-the-vol-surface) |
| [[move-index\|MOVE]] (rates vol) | Up on surprise | Up on surprise | Surprise in either direction lifts rates vol |

**The equity asymmetry** is the hardest part of trading NFP directionally: in *expansion* regimes a beat is bullish for stocks; in *late-cycle* regimes a beat is bearish (no Fed cuts) and a miss is also bearish (recession fear). Know which regime you are in before taking a directional view — and price the [[fed-funds-futures|Fed path]] reaction, not just the headline.

### The 8:30 mechanic and the first 60 seconds

The first 30 seconds after 8:30 produces 60–80% of the eventual hour-one move on surprise prints. By 8:31, front-week SPX IV is at or near its post-print equilibrium. Cash equities open at 9:30 against the new futures level, often with overshoot in NFP-sensitive names (banks, homebuilders, retailers) and sometimes a fade as the morning progresses.

A common practitioner observation: NFP morning sets the entire day's tape direction roughly 70% of the time when the print is a >50k surprise, because dealer hedging flows in the SPX vol surface persist into the cash session.

## Examples / Empirical Evidence

### 2024-08-02 NFP miss → 2024-08-05 vol spike

July 2024 NFP printed **+114k vs +175k consensus**, with the unemployment rate rising to 4.3% (triggering the [[sahm-rule|Sahm Rule]] recession indicator). The reaction:

- 2-year UST yields -27 bp on the day, the largest single-day move since the SVB events
- SPX -1.84% on Friday, NDX -2.5%
- Over the weekend, the [[bank-of-japan|BOJ]] yen-carry unwind compounded the move
- **Monday 2024-08-05**: SPX -3.0%, VIX cash spiked to **65.73** intraday (highest print since March 2020), Nikkei -12.4%
- Front-week SPX IV that had crushed on the Friday close re-ramped to >50 by Monday open
- See [[vix-august-2024-spike]] for the full event chronology

This is the canonical recent example of an NFP print that did *not* crush IV but instead detonated a multi-day vol regime change. Short-premium books with positions expiring the week of August 5 took catastrophic losses; the magnitude of the dislocation was amplified by the cross-asset feedback (yen carry, single-name equities, [[implied-correlation|implied correlation cascade]]).

### 2023-02-03 hot print

January 2023 NFP printed **+517k vs +185k consensus**, the largest upside surprise of the cycle. SPX -1.04% on the day, 2-year UST yields +18 bp, killed the "Fed pivot" rally that had driven January equities. Front-week IV crushed initially on the lack of a recession signal, then re-ramped as the rate-path implication settled in.

### 2024-09-06 cool print, in-regime reaction

August 2024 NFP printed +142k vs +160k consensus with revisions revising the prior two months down. SPX -1.7%; the *miss* was bad for equities because it confirmed the slowdown narrative. Front-week IV crushed only modestly because the surface was already pricing recession risk after the August 5 event.

### 2025-08-01 NFP miss + revisions

July 2025 NFP printed below consensus with substantial downward revisions to May and June (combined -258k revisions). SPX -1.6% on the day, VIX +18%; bonds rallied sharply. The print compounded with broader macro positioning to produce a multi-day vol expansion through early August 2025.

### 2017-2019 calm-regime in-line crushes

The 2017–2019 cycle saw multiple NFP prints land within ±25k of consensus. In those instances, front-week SPX IV crushed cleanly within minutes of 8:30, SPX moved <0.3%, and short-premium books harvested clean post-event theta. **This is the textbook NFP outcome that practitioners are sized for** — but the tail outcomes (like 2024-08-02) are what define the risk profile.

## Implications for Options Traders

### NFP as an event-cluster concentration risk

The connection to [[options-concentration-risk]] is structural and recurring:

- **NFP-Friday weekly expiries** concentrate vol exposure to a single 8:30 print across many options books simultaneously. When the print is a tail outcome, the *positioning* itself amplifies the move
- **Many single names share the NFP exposure** via [[implied-correlation]] — a book of short strangles on six index-component mega-caps with NFP-Friday expiries has six positions but one NFP bet
- **NFP and FOMC cluster within the same options-cycle window**. NFP typically lands the Friday before or after an [[fomc-meetings|FOMC]] meeting in any given cycle. A monthly expiry covering both is an *option on the path* — a particularly high-magnitude event-cluster exposure
- **Same-direction-trade crowding**. The short-premium cohort tends to lean into the IV ramp on the Thursday before NFP at similar strikes, creating dealer positioning that amplifies the no-crush outcome when it arrives
- **Cross-asset spillover**. A surprise NFP that detonates rates vol ([[move-index|MOVE]] up sharply) drags equity vol with it; books that were "diversified" between SPX and TLT short premium can find both legs losing simultaneously

### DTE laddering around NFP

- A 0DTE iron condor on NFP Friday is a *pure NFP bet*; size it as such in the [[expiration-laddering|ladder]]
- 7 DTE positions opened on the prior Friday and held through NFP carry both the gamma and the vega exposure to the print
- 30+ DTE positions cross the print but with materially less surface distortion at the position level
- Practitioner rule: aggregate vega in any single NFP-Friday expiry should not exceed 20–25% of the book's vega budget; if it does, the book *is* an NFP trade

### Theta cliff vs IV crush — the NFP version

NFP exhibits the same theta-vs-vega-realisation tension as [[cpi-release|CPI]], but more pronounced:

- The IV ramp Wednesday-Thursday absorbs accumulating theta — short-premium positions look profitable on paper but the unrealised vega P&L is offsetting
- The realised P&L only arrives in the 8:30:01–8:30:30 AM window
- A position closed Thursday afternoon at the elevated IV has paid for vol that has not yet decayed — it has effectively traded out at fair value rather than collecting the event premium
- The optimal short-premium NFP cycle is typically: *enter Wednesday or Thursday at the IV ramp peak, hold through the 8:30 print, close into the 8:31–9:00 crushed-IV window* on confirmed in-line outcomes, *or* take the loss quickly on a >50k surprise

### How professional desks position around NFP

- **Calendar spreads**: short the NFP-week front cycle, long the next monthly cycle, harvesting the term-structure inversion as it normalises post-print
- **Beta-weighted delta to zero into the print** unless there's an explicit directional view
- **Hard vega cap by NFP date** — explicit limit (e.g. max 20% of book vega in expiries within 5 days of NFP)
- **No naked short single-name puts on rate-sensitive sectors over NFP** — homebuilders, regional banks, small-cap industrials all amplify the move
- **Tail hedges**: small allocation to long [[vix-call-spreads]] or long out-of-the-money spx-puts specifically for the no-crush tail outcome (the August-2024 scenario)
- **Gamma-flat overnight**: many short-premium desks reduce gamma exposure to roughly zero on the Thursday close before NFP, accepting the loss of theta in exchange for limited overnight gap exposure
- **Watch ADP, JOLTS, claims**: pre-NFP indicators inform the *sign* of the expected surprise; desks adjust expressed vega accordingly, though correlation between ADP and NFP is famously low

### Common mistakes

- **Treating every NFP as the textbook crush**. The 2024-08-02 print is a recent reminder that surprise NFP outcomes do not crush IV — they detonate it
- **Stacking earnings and NFP in the same weekly expiry**. A name reporting earnings the same week as NFP has two event-vol crushes priced into one IV; the position has to be sized for both
- **Confusing the headline with the unemployment rate**. The market often reacts more to the household-survey unemployment rate (and especially the [[sahm-rule|Sahm Rule]] threshold) than to the headline NFP number when the rate is at a regime-relevant level
- **Ignoring the two-month revisions**. A +200k headline with -150k of combined prior-month revisions is *net flat* and the market prices it that way — the headline alone is misleading
- **Sizing by max-loss without [[implied-correlation|correlation cascade]] adjustment**. The book-level stress on a surprise NFP is not the sum of per-position max losses
- **Holding short-vol single-name books through NFP without an index-vol overlay**. The August 2024 sequence showed how single-name vol spikes via index correlation when the macro print delivers a tail outcome

## Related

- [[fomc-meetings]] — the policy event NFP feeds directly into
- [[cpi-release]] — the other major monthly macro vol event
- [[macro-events]] — broader taxonomy of scheduled-vol events
- [[implied-volatility]] — what the print reshapes
- [[volatility-term-structure]] — pre- and post-print term-structure inversion
- [[options-concentration-risk]] — event-cluster exposure across an options book
- [[theta-targeting]] — why NFP distorts the realisation of theta income
- [[vega-budgeting]] — NFP stress scenarios in the budget
- [[expiration-laddering]] — laddering DTE around NFP prints
- [[options-portfolio-construction]] — where macro-event sizing fits in the broader book
- [[interest-rate-risk]] — duration exposure across the book
- [[us-treasury-bonds]] — the asset most directly priced off the print
- [[fed-funds-futures]] — the path the print re-prices
- [[move-index]] — rates-vol index that spikes on surprise prints
- [[vix-august-2024-spike]] — the canonical recent NFP-detonation event
- [[sahm-rule]] — recession indicator triggered by the unemployment-rate component
- [[unemployment-rate]] — the household-survey component
- [[options-stress-testing]] — formal NFP scenarios in book-level stress

## Sources

- US Bureau of Labor Statistics — *Employment Situation Report (release calendar and data)*. https://www.bls.gov/ces/
- Federal Reserve Economic Data (FRED) — *NFP and unemployment-rate historical series*.
- CME Group — *Fed Funds futures and post-NFP repricing flows*.
- [[vix-august-2024-spike]] — case study of an NFP-detonated vol spike
