---
title: "CPI Release"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [macro, inflation, volatility, options, calendar-effects, bonds]
aliases: ["CPI", "Consumer Price Index Release", "CPI Print", "CPI Day"]
domain: [macroeconomics, market-microstructure]
prerequisites: ["[[inflation]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[fomc-meetings]]", "[[nonfarm-payrolls]]", "[[implied-volatility]]", "[[volatility-term-structure]]", "[[us-treasury-bonds]]", "[[interest-rate-risk]]", "[[options-concentration-risk]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[expiration-laddering]]", "[[macro-events]]", "[[options-portfolio-construction]]", "[[fed-funds-futures]]"]
---

The **Consumer Price Index (CPI) release** is the Bureau of Labor Statistics' monthly inflation print, published at **8:30 AM Eastern** roughly mid-month for the prior calendar month's data. It is, alongside [[fomc-meetings|FOMC]] and [[nonfarm-payrolls|NFP]], one of the three highest-impact recurring US data events for the rates and equity complexes. For an options book, CPI is a **scheduled vol event** — front-end [[implied-volatility|IV]] ramps in the days before, the surface inverts at the front, and IV crushes within minutes of the 8:30 print. Multiple positions exposed to the *same* CPI date is one of the most common forms of [[options-concentration-risk|event-cluster concentration]] in retail and semi-pro options books.

## Overview

CPI is published by the [[bureau-of-labor-statistics|US Bureau of Labor Statistics (BLS)]] on a schedule released a year in advance. Each release contains:

- **Headline CPI** — total index, year-over-year and month-over-month
- **Core CPI** — excluding food and energy, the figure most relevant to monetary policy
- **Components** — shelter, food, energy, services ex-shelter, goods, used cars, medical care, transportation
- **Supercore** ("services ex-shelter ex-energy") — a measure the [[federal-reserve|Fed]] has emphasized in recent cycles for sticky-services inflation

The release is fed directly into the [[fed-funds-futures]] curve within seconds. A 0.1% surprise vs consensus on core CPI typically produces a 5–10 bp move in 2-year Treasuries and a 0.5–1.5% move in [[sp500|SPX]] within the first 30 minutes.

CPI releases are **frequently the single largest scheduled-data move** in months when an [[fomc-meetings|FOMC]] meeting does not occur. In FOMC months, the CPI print roughly two weeks before the meeting often sets the tone for the meeting itself — a hot CPI three weeks before an expected cut can re-price the path within hours.

## How It Works

### Schedule and cadence

- **Frequency**: monthly, 12 prints per year
- **Time**: 8:30 AM Eastern, before US cash equity open
- **Day**: typically the second or third Tuesday/Wednesday/Thursday of the month, varies; the BLS publishes the full annual calendar
- **Reference period**: data for the *prior* calendar month (e.g. January CPI is released in mid-February)

PPI (Producer Price Index) is released the day before or after CPI in most months and serves as a partial leading indicator, though the market reaction to PPI is materially smaller. PCE (Personal Consumption Expenditures), the Fed's *preferred* inflation gauge, is released roughly two weeks after CPI but produces a smaller market reaction because most of its components are already known from CPI and PPI.

### Release mechanics: how the number is made and disseminated

Understanding *why* CPI is a clean, instantaneous vol event requires understanding the production pipeline:

- **Collection**: BLS economic assistants collect ~80,000 prices each month across ~75 urban areas, plus housing-survey rents. The reference period is the full prior calendar month.
- **Embargo and lock-up**: Historically the BLS ran a press "lock-up" where credentialed media received the data early under embargo and released at exactly 8:30:00. The lock-up procedure has been tightened over the years to prevent leakage; the headline figures hit the wire services and the BLS website simultaneously at 8:30:00 ET.
- **No revisions to the headline**: Unlike [[nonfarm-payrolls|NFP]] (which is heavily revised), the CPI *index level* is not revised after release except for seasonal-adjustment factor updates published annually. This makes the print a one-shot, non-revised number — part of why the market re-prices it so violently in the first minute and then stops.
- **Algorithmic ingestion**: Trading systems parse the headline and core MoM/YoY directly from the machine-readable release. The bulk of the surface re-pricing on E-mini and Treasury futures happens in the first few hundred milliseconds — faster than any human can read the release.

This pipeline is what makes CPI behave like a scheduled single-name *earnings* event for the whole index complex: a known time, a non-revised binary surprise, and an instantaneous, algorithmic reaction.

### The surprise is what matters: actual vs. consensus

The market has already priced the *consensus* expectation (the median of economist forecasts, e.g. the Bloomberg or Reuters survey) into the curve before 8:30. The tradeable event is the **surprise** = actual − consensus, and specifically the surprise in **core MoM** (which strips the noisy food/energy components). A print that exactly matches consensus produces almost pure IV crush with little spot move; a surprise produces spot move *plus* a re-pricing of the [[fed-funds-futures|Fed path]], which can keep IV elevated. The "whisper number" (the buy-side's unofficial expectation, often differing from the published survey) can make an in-line headline still move markets if it misses the whisper.

### Effect on the vol surface

The IV signature of a CPI release closely mirrors a single-name earnings event but applied to the index complex:

- **Pre-print ramp**: front-week SPX IV typically rises +0.5 to +2.0 absolute vol points in the 3 trading days before the release
- **Term-structure inversion**: the expiry covering the print trades 1–3 vol points above the next cycle into the close before
- **Post-print crush**: 1–3 absolute vol points come out of front-week IV within 5–15 minutes of 8:30 AM, often half of that in the first 60 seconds
- **Magnitude scaling**: when the print is a known macro flashpoint (e.g., 2022 cycle prints), the ramp can reach +5 vol points and the crush is correspondingly larger

The IV reaction to the *surprise* — actual minus consensus — is the dominant component. An in-line print produces a clean crush; a surprise print produces a spot move plus a re-pricing of the expected path through the next 2–3 [[fomc-meetings|FOMC]] meetings, which can keep IV elevated for hours rather than crushing.

### Effect on rates, FX, and equities

CPI is fundamentally a **rates event** that propagates to other assets:

- **Treasuries**: 2-year yields are most sensitive (hot print → yields up sharply); 10-year yields move less but with longer half-life. [[move-index|MOVE]] often spikes on surprise prints
- **USD**: a hot CPI is dollar-positive (rate differentials widen vs G10); a soft print is dollar-negative. [[dxy|DXY]] moves of 0.5–1.5% in the first hour are common on surprise prints
- **Gold**: ambiguous on hot prints — real-rates higher (gold-negative) but inflation-protection demand (gold-positive). Recent regime: hot CPI tends to crush gold short-term
- **SPX**: hot CPI → equities lower (rate-path higher, valuation pressure on long-duration growth); soft CPI → equities higher. Magnitude depends on regime — in 2022 a 0.2% upside surprise on core could produce a -3% SPX day; in calm regimes a similar surprise produces -0.3%
- **Crypto**: increasingly correlated to risk-asset CPI reactions; [[bitcoin]] and [[ethereum]] often replicate the SPX direction with 1.5–3x amplification in the first 30 minutes

### Cross-asset reaction matrix

The canonical reflex map for a *core CPI surprise*, holding regime constant. Directions reverse for a soft (below-consensus) print; magnitudes scale with the size of the surprise and the prevailing regime (far larger in the 2022 hiking cycle than in calm years).

| Asset | Hot CPI (above consensus) | Soft CPI (below consensus) | Most sensitive tenor / proxy | Why |
|---|---|---|---|---|
| 2-year UST | Yield up sharply | Yield down sharply | 2y is the policy-path tenor | Re-prices near-term [[fed-funds-futures\|Fed path]] |
| 10-year UST | Yield up, smaller | Yield down, smaller | 10y / curve | Term premium + path; longer half-life |
| USD ([[dxy\|DXY]]) | Up | Down | DXY, USD/JPY | Rate-differential widening |
| [[sp500\|SPX]] | Down | Up | E-mini, [[nasdaq\|NDX]] (long-duration) | Discount-rate pressure on growth |
| Gold | Ambiguous, often down short-term | Often up | Real-rate-sensitive | Real rates up vs. inflation hedge — real rates usually win short-term |
| [[bitcoin\|BTC]] / [[ethereum\|ETH]] | Down, amplified 1.5–3× | Up, amplified | High-beta risk proxy | Trades as a leveraged risk asset |
| Front-week SPX IV | No-crush / re-ramp | Sharp crush | Expiry covering the print | Surprise re-prices path → vol stays bid |
| [[move-index\|MOVE]] | Spikes | Eases | Rates vol | Rates are the primary shock vector |

The single most important cell for an options book is the bottom-left: a *hot surprise* is the regime in which front-week IV **fails to crush** (or re-ramps), which is exactly when short-premium CPI-carry books take their worst losses (see 2022-09-13 below).

### The 8:30 AM mechanic

CPI prints at 8:30:00 AM Eastern. The *first* 60 seconds of trading on E-mini S&P futures and Treasury futures is where the bulk of the surface re-pricing happens. By 8:35, the IV of the front-week SPX cycle is typically already at its post-print equilibrium. The cash-open at 9:30 then re-prices single names against the new index level, often with overshoot in beta-heavy names ([[nvidia|NVDA]], [[tesla|TSLA]], small-cap names via [[iwm|IWM]]).

## Examples / Empirical Evidence

### 2022-09-13 hot print (-4.3% SPX day)

August 2022 core CPI printed +0.6% MoM vs +0.3% consensus. Within 90 minutes:

- 2-year UST yields +20 bp
- DXY +1.5%
- SPX cash open -2.8%, closed -4.3% — the largest single-day CPI reaction in the post-GFC era
- VIX +14% to ~27
- Front-week SPX IV had ramped from ~22 to ~26 going into the print, then *re-ramped* to ~30 instead of crushing — a "no-crush" outcome that punished short-vol books trying to harvest the post-print IV decay

The 2022-09-13 print is the canonical example of a CPI release where the *direction* of the IV move was opposite to the textbook crush, because the surprise re-priced the entire expected Fed path. Short-strangle books with positions expiring same-week took catastrophic losses.

### 2022-11-10 cool print (+5.5% SPX day)

October 2022 core CPI printed +0.3% MoM vs +0.5% consensus. Reverse mirror of September:

- 2-year UST yields -25 bp
- DXY -2.2%
- SPX +5.5% on the day, the largest single-day rally on a CPI print on record
- VIX -8% to ~24
- Front-week IV crushed sharply post-print as the "Fed pivot" narrative re-emerged

### 2024-01-11 in-line print

December 2023 core CPI printed +0.3% MoM, in line with consensus. Front-week SPX IV had ramped from 10.5 to 12.5 going in; it crushed back to 10.8 within 30 minutes of the print and SPX closed -0.07%. **The textbook short-premium outcome** — the IV ramp was the entire P&L.

### 2024-04-10 hot print

March 2024 core CPI printed +0.4% MoM vs +0.3% consensus, the third consecutive hot print. SPX -0.95%, 2-year yields +22 bp, killed the "three cuts in 2024" market narrative. Front-week IV resisted crushing for the rest of the day before normalising the next session.

### 2025-09-11 in-line print under the new regime

August 2025 core CPI printed in line at +0.3%; SPX closed +0.5% on the relief that the print was not hot, with front-week IV crushing roughly 1.5 vol points within an hour. A textbook "in-line crush" of the type that powers most short-premium CPI carry.

### CPI vs the other two macro vol events

| Event | Cadence | Time (ET) | Primary asset | Revised? | IV signature | Path impact |
|---|---|---|---|---|---|---|
| **CPI** | Monthly | 8:30 | Rates → equities | No (headline) | Sharp pre-ramp, fast crush; *re-ramp* on surprise | High — re-prices [[fed-funds-futures\|Fed path]] |
| **[[nonfarm-payrolls\|NFP]]** | Monthly | 8:30 | Rates, USD | Heavily | Similar ramp/crush; noisier due to revisions | Medium-high |
| **[[fomc-meetings\|FOMC]]** | 8×/year | 14:00 + 14:30 presser | All | N/A | Two-stage: statement then presser; crush after presser | Highest — the path *is* the news |

CPI and NFP both print at 8:30 and behave like index-level earnings events; FOMC is a two-stage afternoon event (statement at 14:00, then the [[powell|Chair's]] press conference at 14:30) where the second stage frequently dominates. The three interlock: CPI roughly two weeks before an FOMC sets the tone; NFP fills in the labour-side of the dual mandate. A book holding short premium across a CPI *and* the following FOMC is exposed to a stacked, correlated event (see event-cluster concentration below).

## Implications for Options Traders

### CPI as an event-cluster concentration risk

This is the angle most relevant to [[options-concentration-risk]]:

- **Many names share the same CPI exposure**. A book of short strangles on six index-component mega-caps has six positions but **one CPI bet**. A surprise print drags every name with it via [[implied-correlation]] cascade
- **CPI date often falls in the same expiry window as FOMC**. CPI is typically published 1–3 weeks before the next [[fomc-meetings|FOMC]] meeting. A book of short premium expiring the day after FOMC is *also* exposed to the CPI print preceding the meeting — a stacked event
- **The "hot CPI then hawkish FOMC" combo**. 2022 saw multiple instances where a hot CPI re-priced the path, then the subsequent FOMC confirmed the re-pricing — a one-two punch that the short-premium cohort experienced as a multi-day vol expansion rather than a single-event crush
- **Same-cycle, same-direction crowding**. In any given month, retail and semi-pro short-premium books tend to cluster on the same expiry covering the print. The *positioning* itself becomes a risk — a single surprise unwinds many books simultaneously, amplifying the correlated stress

### DTE laddering around CPI

- A 7 DTE [[iron-condor]] opened the Friday before a CPI Tuesday is a *direct CPI bet*; treat it as such in the [[expiration-laddering|DTE ladder]]
- 30 DTE positions that *cross* a CPI print absorb the surface distortion gradually and are less binary
- 0–1 DTE positions opened *after* the 8:30 print can harvest the residual crush with low gamma exposure to a follow-through move; this is a distinct strategy from holding through the print
- Practitioner rule: never let aggregate vega in any single CPI-day expiry exceed 25–30% of the book's vega budget

### Theta cliff vs IV crush

CPI illustrates the difference between **calendar theta** and **event vol crush**:

- The theta accumulating in the 3 days before a CPI print is largely *fictional* — it is offset by the vega expansion of the IV ramp
- The realised P&L on a short-premium position only arrives in the 5–15 minute window after 8:30 when IV crushes
- A position closed before the print at the elevated IV has not earned its theta — it has paid for vol that has not yet decayed

This is why a CPI-cycle short-premium strategy is often run as: *open the position at the IV ramp peak (T-1 close), hold through the 8:30 print, close into the post-crush window (typically by 9:30 cash open).* Anything else is either pre-event speculation (long-vol entry) or post-event drift trading.

### How professional desks position around CPI

- **Sell front-month vol against long back-month vol** — a [[calendar-spread]] structure that profits from the surface inversion crushing post-print
- **Beta-weighted delta to zero into the print** — directional exposure should be intentional, not residual; if you don't have a CPI directional view, hedge to flat
- **Vega cap by event** — explicit limit on aggregate vega exposed to any single 8:30 print (e.g., max 25% of book vega in expiries within 5 days of CPI)
- **No naked short single-name puts on tech mega-caps over CPI** — the index-level vol shock spreads with amplification via [[implied-correlation]]
- **Long [[vix-call-spreads]] as overlay** — small-cost tail hedge that pays on no-crush outcomes (2022-09-13 type events)
- **PPI tells / PCE follow-throughs** — desks watch PPI (day before or after) for component direction-of-error and re-base CPI expectations; PCE (two weeks later) is used to confirm or reject the CPI signal

### Common mistakes

- **Treating every CPI as the textbook crush**. The 2022 cycle showed that surprise prints do not crush — they re-ramp. A short-premium book sized for the average outcome will be stress-tested by the tail
- **Stacking earnings and CPI in the same expiry**. A name reporting earnings the same week as a CPI print has *two* event-vol crushes priced into one IV. The structure has to be sized for both possibilities
- **Ignoring the 8:31 AM IV print as the actionable level**. The crushed IV at 8:31 is the level at which post-event positions should be priced; anyone using the 8:29 IV is using a stale number
- **Confusing the headline with the core**. Markets price the *core* number more than headline; a hot headline driven by energy with cool core can produce the opposite of the naive reaction
- **Sizing by maximum-loss without accounting for [[implied-correlation|correlation cascade]]**. The book-level stress on a surprise CPI is not the sum of per-position max losses — it is the correlated sum, which is worse

## Related

- [[fomc-meetings]] — the policy event CPI feeds directly into
- [[nonfarm-payrolls]] — the other major monthly macro vol event
- [[macro-events]] — broader taxonomy of scheduled-vol events
- [[implied-volatility]] — what the print reshapes
- [[volatility-term-structure]] — pre- and post-print term-structure inversion
- [[options-concentration-risk]] — event-cluster exposure across an options book
- [[theta-targeting]] — why CPI distorts the realisation of theta income
- [[vega-budgeting]] — CPI stress scenarios in the budget
- [[expiration-laddering]] — laddering DTE around CPI prints
- [[options-portfolio-construction]] — where macro-event sizing fits in the broader book
- [[interest-rate-risk]] — duration exposure across the book
- [[us-treasury-bonds]] — the asset most directly priced off the print
- [[fed-funds-futures]] — market-implied path that re-prices on the print
- [[move-index]] — the rates-vol index that spikes on surprise prints
- [[inflation]] — the macro variable being measured
- [[options-stress-testing]] — formal CPI scenarios in book-level stress

## Sources

- US Bureau of Labor Statistics — *Consumer Price Index release calendar and data*. https://www.bls.gov/cpi/
- Federal Reserve Bank of Cleveland — *Inflation Nowcasting* (real-time CPI nowcasts).
- CME Group — *Fed Funds futures and post-CPI repricing flows*.
- [[itpm-trading-philosophy]] — practitioner framework for laddering DTE around macro events.
