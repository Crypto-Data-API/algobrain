---
title: "Nikkei 225 Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, stocks, japan, asia]
aliases: ["Nikkei Options", "Nikkei 225 Options", "OSE Nikkei Options", "SGX Nikkei Options"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
related: ["[[index-options]]", "[[spx-options]]", "[[dax-options]]", "[[ftse-100-options]]", "[[osaka-exchange]]", "[[jpx]]", "[[sgx]]", "[[nikkei-225]]", "[[topix-options]]", "[[vnky]]", "[[american-vs-european-options]]", "[[cash-vs-physical-settlement]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[options-greeks]]", "[[short-strangle]]", "[[iron-condor]]", "[[currency-hedging]]", "[[carry-trade]]", "[[xiv-blowup-feb-2018]]", "[[yen-carry-unwind-aug-2024]]", "[[dispersion-trading]]"]
---

Nikkei 225 options are listed at two principal venues: the **Osaka Exchange (OSE)**, part of Japan Exchange Group (JPX), in **JPY-denominated** form, and at the **Singapore Exchange (SGX)** in both **JPY-denominated** and **USD-denominated** forms. The OSE contract — the home market — is European-style, cash-settled, with a **¥1,000 per index point** multiplier, and settles to the **Special Quotation (SQ)** of the Nikkei 225 calculated from morning-session opening prices. SGX's Nikkei 225 options provide international-hours coverage and a USD-denominated wrapper that simplifies access for non-Japanese institutional accounts.

## Overview

The Nikkei 225 is a price-weighted (not market-cap weighted) index of 225 large Japanese companies, calculated since 1949 by Nikkei Inc. As a price-weighted index it is sensitive to the highest-priced individual stocks (e.g., Fast Retailing, Tokyo Electron, SoftBank Group historically) — a structural quirk that affects single-name dispersion against the index and is operationally distinct from cap-weighted indices like SPX or DAX.

Nikkei 225 options are the dominant Japanese equity-index volatility product, used for:

- **JPY-denominated portfolio hedging** by Japanese pension funds (GPIF and corporate pensions), trust banks, and insurers.
- **Yen-equity-vol expression** in global macro books, particularly during yen-carry regime shifts.
- **Asia-overnight risk hedging** by Western institutional desks via SGX during US/European trading hours.

## Venue Comparison

| Dimension | **OSE Nikkei 225** | **SGX Nikkei 225 (JPY)** | **SGX Nikkei 225 (USD)** |
|---|---|---|---|
| Exchange | Osaka Exchange (JPX) | Singapore Exchange | Singapore Exchange |
| Currency | JPY | JPY | USD |
| Multiplier | **¥1,000 per index point** | ¥500 per index point | $5 per index point |
| Exercise | European | European | European |
| Settlement | Cash | Cash | Cash |
| Settlement basis | Nikkei 225 SQ (Special Quotation) | Nikkei 225 SQ | Nikkei 225 SQ |
| Trading hours | Tokyo session 08:45–15:45 JST + night session to 06:00 JST next day | SGX session — broader Asia-overnight coverage including European morning | SGX session |
| Primary users | Japanese institutional, retail | International institutional Asian-hours trading | Non-JPY institutional accounts |

The OSE contract is the **deeper, home-market product**; SGX exists for international-hours access and currency convenience.

## Contract Mechanics — OSE Nikkei 225 Options

| Spec | Value |
|---|---|
| Underlying | Nikkei 225 Stock Average |
| Multiplier | **¥1,000 per index point** |
| Exercise style | European |
| Settlement | Cash, in JPY |
| Strike intervals | 250 index points (standard); 125 near-the-money for weeklies |
| Tick size | Variable: 1 yen for premium <100, 5 yen for 100-1000, 10 yen for >1000 |
| Trading hours | Day session 08:45–15:45 JST; Night session 16:30–06:00 JST next day |
| Settlement | Special Quotation (SQ) calculated on second Friday of expiration month |
| Tax treatment | Jurisdiction-specific |
| Listed | Osaka Exchange (JPX) |

At a Nikkei 225 level of 38,000, a single OSE contract represents **¥38 million of notional** (38,000 × ¥1,000) — at typical USD/JPY rates around 150, that is approximately **$250,000 USD-equivalent**, similar in size to a [[rut-options|RUT]] contract.

OSE also lists **mini Nikkei 225 options and futures** at smaller multipliers for retail and smaller institutional accounts; verify current Mini-Nikkei spec sheets for exact sizing.

## Settlement — the SQ

OSE Nikkei 225 options settle to the **Special Quotation (SQ)** — the Japanese-market analog of the US SOQ:

- **Expiration day**: the **second Friday** of the expiration month (note: NOT the third Friday like US options). Specifically, the contract's last trading day is the business day before the second Friday, and SQ calculation occurs on the second Friday morning.
- **SQ calculation**: the SQ is computed from the **opening prices of all 225 component stocks** on the second-Friday morning session at the Tokyo Stock Exchange. Components open at staggered times during the morning auction; the SQ is published once all 225 opening prints are determined.
- **Trading**: option trading on the expiring contract ceases at the close of the prior day's session.

The SQ methodology is structurally similar to US AM-settlement: it concentrates settlement-driven flows into Tokyo's morning open and creates **Thursday-night-to-Friday-morning gap risk**. Several historical Nikkei SQ events have produced material gaps between Thursday close and SQ — notably in March 2011 (Tōhoku earthquake aftermath) and during the **August 2024 yen-carry unwind**, when the Monday-after-SQ session saw dramatic moves on top of an already-elevated SQ print.

The **second-Friday-not-third-Friday** convention is the single most important operational distinction for traders cross-trading Nikkei vs US index options: monthly expiration cycles do not align, and any cross-asset spread structure must account for the date offset.

## Liquidity & Spreads

OSE Nikkei 225 options are the deepest Asian equity-index options market:

- **OSE volume** — typically **40,000-100,000 contracts/day** across all expirations, peaking around monthly SQ.
- **SGX volume** — typically **10,000-30,000 contracts/day**, with concentration in front-month expirations.
- **Bid/ask** — OSE near-the-money strikes typically 5-20 yen wide on premium (¥5,000-¥20,000 per contract); wider on far-OTM and back-month.
- **Strike density** — 250-point standard intervals; 125-point near-the-money on weeklies.
- **Quote sizes** — 10-50 contracts at the inside on OSE during Tokyo session; thinner on night session and on SGX.
- **Liquidity windows** — peak during Tokyo morning session (09:00-11:30 JST) and afternoon session (12:30-15:00 JST). SGX provides Asian-overnight and European-morning coverage.

## Greeks & Volatility-Surface Behaviour

Nikkei 225 options price under standard Black-Scholes/European mechanics (cash-settled, no early exercise), but the surface has Japan-specific features:

- **Downside skew** — like most equity indices, Nikkei carries a negative [[volatility-skew|skew]] (OTM puts richer than OTM calls), reflecting hedging demand from Japanese pensions and insurers. The skew steepens sharply in yen-strengthening (risk-off) regimes.
- **Yen-correlation overlay** — because Nikkei is tightly coupled to USD/JPY through the [[carry-trade|yen-carry]] channel, the vol surface co-moves with FX vol. A spike in USD/JPY realized vol typically drags Nikkei index vol with it — a cross-asset linkage SPX does not have.
- **Price-weighted dispersion** — the index being price-weighted (not cap-weighted) means a handful of high-priced names (Fast Retailing, Tokyo Electron) dominate index vol; single-name shocks in those names feed into index vol more than cap-weighted intuition suggests. This shapes [[dispersion-trading|dispersion]] economics against the index.
- **VNKY** — the [[vnky|Nikkei Volatility Index]] is the Nikkei analog of the [[vix|VIX]] and the standard read on Nikkei implied-vol regime.
- **Greeks display quirk** — non-JPY desks must track an FX overlay: a JPY-denominated option's delta and vega translate into base-currency P&L that moves with USD/JPY, so the *effective* Greeks for a USD book embed a currency leg unless hedged.

### Term Structure

Nikkei vol term structure behaves like other major indices — **contango in calm regimes** (longer-dated implied above short-dated, reflecting the [[variance-risk-premium]]) and **backwardation in stress** (front-end spikes above the back). Two Japan-specific wrinkles:

- **SQ clustering** — because monthly SQ falls on the **second Friday**, the term structure's monthly "steps" are offset from US/European third-Friday cycles; calendar spreads against SPX must align the date mismatch.
- **Event humps** — BoJ meeting dates and major US macro events create localized humps in the Nikkei term structure, often larger relative to baseline than equivalent SPX humps given Japan's policy-shift sensitivity.

## Common Spread Structures

| Structure | Construction | Typical Nikkei use |
|---|---|---|
| **Put spread** | Long higher-strike put, short lower-strike put | Cheapened downside hedge for JPY pension books |
| **[[short-strangle|Short strangle]]** | Sell OTM put + OTM call | Harvest Japanese [[variance-risk-premium]] in range-bound regimes |
| **[[iron-condor|Iron condor]]** | Short strangle + protective wings | Defined-risk premium selling around the SQ cycle |
| **Risk reversal** | Long call, short put (or reverse) | Express yen-carry directional view with skew positioning |
| **Calendar spread** | Long back-month, short front-month same strike | Trade SQ-cycle term-structure offset vs US |
| **Collar** | Long put, short call vs long Nikkei | Pension liability-matching downside protection at low net cost |
| **Cross-region pair** | Nikkei vol vs SPX/DAX/SX5E vol | Regional-divergence / yen-carry dispersion expression |

## Use Cases

### Japanese-portfolio hedging

The primary domestic use case. Japanese pensions (GPIF and corporate), insurers, and trust banks hold long Nikkei 225 put open interest as portfolio hedges. Long-dated put structures are particularly common in pension liability-matching contexts.

### Yen-equity-vol expression in global macro

Nikkei 225 options are a core macro instrument for expressing views on Japanese equity volatility, which has its own regime distinct from US and European vol:

- **Yen-carry regime shifts** — Nikkei vol spikes are tightly linked to yen strengthening episodes (yen-carry unwinds), creating a vol-correlation structure that differs from SPX.
- **BoJ policy shifts** — Nikkei vol responds sharply to BoJ rate / yield-curve-control / ETF-purchase policy changes.
- **August 2024 yen-carry unwind** — a canonical recent case: the BoJ rate move + USD/JPY drop generated a Nikkei SQ-week move that included a single-day -12% Nikkei session (the largest since 1987), with vol spikes in Nikkei options exceeding equivalent SPX vol moves. See [[yen-carry-unwind-aug-2024]].

### Asia-overnight hedging

Western institutional desks use **SGX Nikkei 225 options** during US/European hours when OSE is closed, hedging or expressing views on Asia-overnight exposure. The SGX USD-denominated wrapper is particularly useful for US institutions that want to avoid JPY translation in their P&L.

### Cross-region pair trades

Nikkei-vs-SPX, Nikkei-vs-DAX, or Nikkei-vs-EURO-STOXX-50 dispersion expresses regional divergence views. Japan's distinct macro regime (negative or near-zero policy rates for decades, structural deflation history, demographic decline) makes Nikkei a useful regional-divergence leg.

### Premium-selling on Japanese vol

Nikkei [[short-strangle|strangles]] and [[iron-condor|iron condors]] capture the Japanese [[variance-risk-premium]]. Empirically the Japanese VRP has been comparable to US/European VRP in long-window terms, with periodic regime spikes during yen-carry episodes that can be larger in Nikkei vol than in SPX vol.

### Carry-and-hedge structures

Long Nikkei + long Nikkei put structures, sometimes paired with short [[carry-trade|yen-carry trade]] currency hedges, are a recurring institutional template for capturing Japanese equity-risk premium while limiting tail risk.

## Risks / Quirks

- **Second-Friday SQ, not third-Friday** — operationally distinct from US/European monthly expirations; cross-asset structures must align dates carefully.
- **Price-weighted index** — high-priced stocks (Fast Retailing, Tokyo Electron) carry disproportionate index weight; single-name shocks in those names move the index more than market-cap intuition would suggest.
- **SQ overnight gap risk** — Thursday-night-to-Friday-morning gap risk on monthly SQ is real and has historically produced material settlement surprises.
- **Yen-carry exposure** — Nikkei is highly correlated with USD/JPY in many regimes; non-JPY investors are essentially taking a joint Nikkei-and-yen bet unless explicitly currency-hedged.
- **August 2024 case** — the yen-carry-unwind episode produced a Nikkei single-day move (-12.4% on Aug 5, 2024) larger than any single-day SPX move in modern history except for COVID-era March 2020. Nikkei tail-risk pricing has structurally adjusted post-event.
- **Currency risk for non-JPY accounts** — JPY-denominated P&L can swing materially against a non-JPY base currency; SGX USD wrapper reduces but does not eliminate this (the underlying Nikkei still moves with yen via the yen-carry channel).
- **Trading-hours fragmentation** — OSE day session, OSE night session, and SGX session collectively cover most of a 24-hour cycle, but with material differences in liquidity across windows. Stop-loss execution across session boundaries can be expensive.
- **Tax treatment is non-Section-1256 for US holders** — meaningful after-tax disadvantage vs SPX for short-term-heavy strategies.
- **Mini-Nikkei sizing variants** — multiple sizes exist; verify the exact contract specification and multiplier before sizing.

## Tax Treatment

Nikkei 225 options have **no analog to US Section 1256 treatment**. Tax treatment depends on holder jurisdiction:

- **Japan** — tax treatment varies by holder type (retail, corporate, institutional pension); consult local tax counsel for specifics.
- **US holders** — typically taxed as ordinary capital gains/losses on a section-1234-style basis; foreign-listed index options generally do not qualify for §1256 treatment. Some commodity-pool-related structures and ETF-wrapped exposures may have different tax characterization.
- **Singapore (for SGX-traded contracts)** — Singapore has favorable capital-gains tax treatment for many investor types; SGX-listed Nikkei contracts can have specific tax efficiencies for Singapore-resident accounts.
- **Other jurisdictions** — varied; consult local tax counsel.

The absence of Section-1256-style treatment for US-resident Nikkei traders is a meaningful structural disadvantage vs SPX that some accounts try to mitigate by trading **Nikkei-225-themed ETF options** (e.g., on EWJ or DXJ) where US-listed wrapper rules apply, accepting the basis difference and additional fund-management costs.

## Comparison to Other Major Index Options

| Feature | **Nikkei 225 (OSE)** | [[spx-options\|SPX]] | [[dax-options\|DAX (ODAX)]] | [[ftse-100-options\|FTSE 100]] |
|---|---|---|---|---|
| Index weighting | **Price-weighted** | Cap-weighted | Cap-weighted (total-return) | Cap-weighted (price-return) |
| Currency | JPY (also SGX USD) | USD | EUR | GBP |
| Multiplier | ¥1,000 / pt | $100 / pt | €5 / pt | £10 / pt |
| Exercise | European | European | European | European |
| Settlement | Cash, SQ | Cash, AM/PM SOQ | Cash, midday auction | Cash, opening-auction EDSP |
| Expiry day | **2nd Friday** | 3rd Friday (+ weeklies) | 3rd Friday | 3rd Friday |
| US §1256 60/40 | **No** | **Yes** | No | No |
| Vol index | [[vnky\|VNKY]] | [[vix\|VIX]] | [[vdax-new\|VDAX-NEW]] | [[vftse\|VFTSE]] |
| Distinctive driver | Yen-carry / BoJ | Global benchmark | Autos/industrials, total-return | Resources/financials, intl revenue |

The two operational quirks that most distinguish Nikkei from the Western indices are the **price-weighting** (vs cap-weighting everywhere else) and the **second-Friday SQ** (vs third-Friday everywhere else). Both demand explicit handling in any cross-region structure.

## Related

- [[index-options]] — overview of the franchise
- [[spx-options]] — US large-cap analog
- [[dax-options]] — German large-cap analog
- [[ftse-100-options]] — UK large-cap analog
- [[osaka-exchange]], [[jpx]] — primary listing venue
- [[sgx]] — Singapore listing venue
- [[nikkei-225]] — the underlying index
- [[topix-options]] — alternative Japanese-equity index option (cap-weighted, distinct profile)
- [[vnky]] — Nikkei VIX-equivalent
- [[carry-trade]], [[yen-carry-unwind-aug-2024]] — yen-carry regime context
- [[american-vs-european-options]]
- [[cash-vs-physical-settlement]]
- [[implied-volatility]], [[volatility-skew]], [[options-greeks]]
- [[short-strangle]], [[iron-condor]]
- [[currency-hedging]] — essential for non-JPY investors
- [[dispersion-trading]] — Nikkei-vs-component dispersion is a meaningful Japanese franchise

## Sources

- Osaka Exchange (JPX) — Nikkei 225 Options product specifications (jpx.co.jp — Nikkei 225 options contract spec) — multiplier, settlement, expirations.
- Osaka Exchange — Special Quotation (SQ) calculation methodology.
- Nikkei Inc. — Nikkei 225 Stock Average index methodology.
- Singapore Exchange (SGX) — Nikkei 225 options product specifications (sgx.com — JPY and USD variants).
- JPX historical SQ data — gap-risk case studies.
- [[yen-carry-unwind-aug-2024]] — empirical reference for recent Nikkei vol regime shift.
