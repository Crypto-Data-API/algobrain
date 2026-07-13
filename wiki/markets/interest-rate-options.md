---
title: "Interest Rate Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, futures, interest-rates, sofr, treasuries, eurodollar, macro, derivatives]
aliases: ["Interest Rate Options", "Rate Options", "SOFR Options", "Treasury Options", "Eurodollar Options"]
related: ["[[options-greeks]]", "[[rho]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[options-risk-budgeting]]", "[[long-dated-options]]", "[[move-index]]", "[[sofr]]", "[[treasury-futures]]", "[[eurodollar]]", "[[fed-funds-futures]]", "[[yield-curve]]", "[[duration]]", "[[convexity]]", "[[macro-trading]]", "[[long-volatility-strategies]]"]
---

Interest rate options are listed and OTC options whose payoff is a function of an interest rate, a rate-linked future, or a bond price. They are the dominant tool for institutional rate hedging, yield-curve speculation, and volatility harvesting on the rates complex. Distinct from equity options, the underlying is a futures contract or a forward rate (not a tradeable spot), payoff is denominated in basis points × tick value, and the [[volatility-surface]] is dominated by skew toward higher rates. The single largest listed rate-options product by ADV is now [[sofr|SOFR]] options after the [[eurodollar]] product was retired in 2023.

## Market Overview

The listed rate-options ecosystem (in order of ADV as of 2025):

| Product | Exchange | Underlying | Tick value | ADV (2025) |
|---|---|---|---|---|
| SOFR options | CME | SOFR futures (3M and 1M) | $25 / 0.005 | ~3M contracts/day |
| 10Y Treasury options | CME | 10-year T-Note futures (TY) | $15.625 / 1/64 of 1% | ~700k |
| 5Y Treasury options | CME | 5-year T-Note futures (FV) | $7.8125 / 1/64 of 1% | ~250k |
| 30Y Treasury options | CME | 30Y T-Bond futures (US) | $15.625 / 1/64 of 1% | ~120k |
| 2Y Treasury options | CME | 2Y T-Note futures (TU) | $7.8125 / 1/128 of 1% | ~80k |
| Fed Funds options | CME | Fed Funds futures (ZQ) | $20.835 / 0.005 | ~30k |

OTC rate options (interbank, traded via [[isda]] documentation):
- **Caps & floors** on SOFR (post-LIBOR transition) -- portfolio-level protection against rate spikes/drops.
- **Swaptions** -- options to enter an interest rate swap; the dominant institutional rate-vol product. Payer/receiver swaptions on USD swap curves are the macro-hedge instrument of choice for pension funds and insurance balance sheets.
- **Bermudan callables** embedded in callable bonds and structured notes.

Daily notional in the OTC swaption market alone exceeds $200 billion. Total rate-options market notional is the largest of any options complex globally, dwarfing the equity options market by an order of magnitude.

## Contract Specifications (Listed)

### SOFR Options (CME)
- **Underlying**: 3-Month SOFR futures (front and back of curve listed).
- **Style**: American-style on quarterly options; weekly options also listed.
- **Settlement**: Physical delivery into SOFR futures position on exercise.
- **Strike intervals**: 6.25 basis points for nearby; 12.5 bps for further.
- **Tick size**: 0.0025 (= $6.25 per contract); minimum block trade thresholds apply.
- **Expirations**: Quarterly (March, June, September, December) and serial (monthly) plus weekly.
- **Last trading day**: For quarterly: last business day of the contract month.

(Source: [[cme-sofr-options-specs]])

### Treasury Options (CME)
- **Underlying**: Treasury futures contracts (TU, FV, TY, US, UB).
- **Style**: American-style.
- **Settlement**: Physical delivery into the underlying futures position.
- **Strike intervals**: Half-point increments below 110 strike, 1-point above (varies by maturity).
- **Quote convention**: in 64ths of a point of par.
- **Expirations**: Quarterly plus serial monthlies and weeklies.

(Source: [[cme-treasury-options-specs]])

### Fed Funds Options (CME)
- **Underlying**: 30-Day Fed Funds futures (ZQ).
- **Use case**: pricing the path of the Federal Funds target rate over the next 1-12 months. Highly liquid around FOMC meeting dates; thin between.

## OTC Rate Options in Detail

The OTC market dwarfs the listed market by notional. Three product families dominate:

### Caps and Floors

A **cap** is a strip of individual call options (called **caplets**) on a floating reference rate (post-LIBOR, almost always [[sofr|SOFR]] compounded over each period). Each caplet pays off if the floating rate fixes above the **cap strike** on its reset date; the payoff is `notional × max(rate − strike, 0) × day-count`. A floating-rate borrower buys a cap to bound their maximum funding cost — the cap acts as rate insurance, and the premium is the cost of that insurance.

A **floor** is the symmetric instrument: a strip of put options (**floorlets**) that pay when the rate fixes *below* the floor strike. Lenders and floating-rate investors buy floors to protect minimum income.

A **collar** combines a bought cap and a sold floor (or vice versa), financing the protection by giving up the upside beyond the floor strike — a zero-cost or low-cost structure widely used in corporate liability management.

Key mechanics:

| Feature | Cap / Floor detail |
|---|---|
| Underlying | A *strip* of optionlets, one per reset period over the cap tenor |
| Reference rate | SOFR (compounded in arrears) post-LIBOR transition; legacy LIBOR caps still running off |
| Strike | A single rate level applied to every caplet (or a stepped schedule) |
| Settlement | Cash, per period, on each reset date — not a single terminal payoff |
| Vol convention | Quoted in **flat vol** (one vol for the whole cap) or stripped to **forward-forward caplet vols** |
| Typical user | Corporate borrowers, project-finance/real-estate debt, CLO/loan structures |

### Swaptions

A **swaption** is an option to enter an [[interest-rate-swap|interest rate swap]] at a pre-agreed fixed rate (the swaption strike) on a future date. They are the **dominant institutional rate-vol product** and the single largest source of rate-vega in the financial system.

- **Payer swaption** — the right to *pay fixed / receive floating* (profits if rates rise above the strike). Economically a call on rates.
- **Receiver swaption** — the right to *receive fixed / pay floating* (profits if rates fall below the strike). Economically a put on rates.

Swaptions are described by two tenors: the **option expiry × the underlying swap tenor**, written e.g. "**1y10y**" (one-year option into a ten-year swap). The grid of all expiry × tenor combinations is the **swaption volatility cube** (expiry, tenor, strike) — the rates-market analog of the equity [[volatility-surface]], and the central object rate-vol desks risk-manage.

| Feature | Swaption detail |
|---|---|
| Underlying | A forward-starting interest-rate swap |
| Settlement | **Physical** (enter the actual swap) or **cash** (settle to a swap-value mark) |
| Style | Mostly European; **Bermudan** swaptions allow exercise on multiple dates and are embedded in callable bonds |
| Vol convention | **Normal (basis-point) vol** is the post-2016 market standard; lognormal vol still quoted for some legacy books |
| Typical user | Pension funds, insurers (liability hedging), bank ALM, mortgage hedgers, macro funds |

The **mortgage-convexity hedging** flow is a structurally important driver: holders of mortgage-backed securities are implicitly short prepayment options, and they hedge the resulting negative [[convexity]] by buying receiver swaptions — a flow that can sharply bid rate vol during rapid rate moves (the "convexity vortex").

### Bermudan Callables and Structured Notes

Callable bonds embed a **Bermudan swaption** sold by the investor to the issuer (the issuer's right to call). Structured notes (range accruals, snowballs, callable steepeners) embed exotic rate options. Dealer desks that issue these products absorb large amounts of rate vega and recycle it into the listed and vanilla-swaption markets — the rates analog of the equity structured-product → [[variance-swaps|variance-swap]] vega-recycling pipeline.

## Pricing & Greeks

Rate options have a different mathematical structure than equity options:

### Underlying is a futures, not spot

Rate options are universally on a futures contract, never directly on the spot rate. SOFR options are on SOFR futures; Treasury options are on Treasury futures. The futures price already embeds the forward rate expectation, so the option is a Black-76-style instrument:

```
Call = e^(-rT) × [F × N(d1) - K × N(d2)]
```

where F is the futures price (or 100 - rate, in the case of rate futures).

### Quote convention is unusual

For rate futures (SOFR, Eurodollar, Fed Funds), price is quoted as `100 - rate`. So a SOFR future at 96.50 implies a 3.50% rate. Options on these futures use the price quote convention -- a "97 call" pays off if the futures rises above 97 (= rates fall below 3.00%). This sign-flip is the most common source of confusion for traders coming from equities.

### Tick value × basis points

A 1bp move in the underlying rate produces a fixed dollar change per contract:
- 3M SOFR option: 1bp = $25.
- 10Y Treasury option: 1bp ≈ $80 (varies with [[duration]] of the cheapest-to-deliver).
- 30Y Treasury option: 1bp ≈ $200.

This means rate-option Greeks are typically expressed in **basis points** rather than dollars; a position with delta = 0.40 gains $25 × 0.40 = $10 per 1bp move per SOFR option contract, or $80 × 0.40 = $32 per 1bp on a 10Y Treasury option.

### Vol surface dominated by skew toward higher rates

Unlike equity options where the put side is steeper (crash skew), rate-option vol surfaces typically show:
- **Upside-rate skew** -- options that pay if rates spike are richer than equidistant options that pay if rates fall. The economic mechanism: rate spikes are correlated with credit-event regimes that demand rate-cap hedging from corporate borrowers.
- **Smile near ATM** -- both wings are richer than ATM, giving a smile rather than the equity-typical smirk.
- **Term-structure of vol**: front-end vol (1-3M expirations) tends to be higher than back-end (1-2Y) when the Fed is in an active cycle; flatter when the Fed is on hold.

The [[move-index|MOVE Index]] -- the rate-options analogue of the [[vix|VIX]] -- is the standard benchmark for rate-vol regime and is computed from a basket of 1-month Treasury options.

### Greeks behaviour

- **Delta**: against the futures price. For SOFR futures (where price = 100 - rate), a long call has positive delta in *price*, which is *negative delta in rate*. Some platforms display "rate delta" instead.
- **Gamma**: high for at-the-money options near a Fed meeting; convexity matters for rate hedgers.
- **Vega**: typically expressed per vol-point of normal/lognormal vol; dominant Greek for swaptions especially.
- **Theta**: small near-the-money for long-dated swaptions but accelerates for short-dated options into Fed meetings.
- **Cross-Greeks**: rate options have meaningful **vanna** (delta sensitivity to vol) and **DV01-of-vega** (vega sensitivity to rates). These are routinely tracked on institutional rate desks and ignored on equity desks.

## Normal vs Lognormal Vol — A Rates-Specific Convention

One of the deepest mechanical differences from equity options is the **vol quoting convention**. Equity vol is universally lognormal (Black-Scholes) — vol scaled to the *percentage* move of the underlying. Rate vol can be quoted two ways:

- **Lognormal (Black-76) vol** — vol as a percentage of the rate level. Breaks down near zero rates (a 0.10% rate cannot have a meaningful percentage vol) and went briefly nonsensical during the **negative-rate era** in EUR and JPY, when lognormal vol is undefined for rates below zero.
- **Normal (basis-point, "bp vol") vol** — vol expressed as the absolute basis-point standard deviation of the rate. Well-defined at and below zero, and now the **market standard for swaptions** and most rate-vol quoting. A "70 bp-vol" 1y10y swaption means the 10y swap rate is expected to move with a ~70bp annualized standard deviation.

The conversion is roughly `normal vol ≈ lognormal vol × rate level`. Confusing the two — or applying an equity-style lognormal model to a near-zero rate — is a classic and expensive rate-options error. The market's migration to normal vol after the 2014-2021 low/negative-rate period is now near-universal for OTC rates. Pricing models in the space (SABR, Hull-White, Bachelier/normal-Black) must be specified together with the vol convention to be meaningful.

## The MOVE Index — the "VIX of Rates"

The **[[move-index|MOVE Index]]** (Merrill Lynch Option Volatility Estimate, now maintained by ICE) is the rate market's benchmark fear gauge — the direct analog of the equity [[vix|VIX]]. Key differences from VIX:

| Dimension | MOVE | [[vix|VIX]] |
|---|---|---|
| Underlying | 1-month options on Treasury futures across the curve (2y, 5y, 10y, 30y) | 30-day SPX options strip |
| Vol type | **Yield (basis-point) vol** — annualized bp move expected in Treasury yields | Price (lognormal) vol |
| Weighting | Yield-curve-weighted blend across maturities | Single-index strike strip |
| Typical range | ~50-90 in calm regimes; 130+ in stress | ~12-20 calm; 30+ in stress |

The MOVE is used to gauge the **rate-vol regime**, to time long/short rate-vol positioning, and as a cross-asset signal — a rising MOVE alongside a stable VIX often flags rates-led, rather than equity-led, stress (e.g. the 2022-2023 banking and rate-hike period saw MOVE elevated for an extended stretch). Relative-value desks trade the **MOVE/VIX ratio** as a cross-asset vol spread. See [[move-index]] for the methodology.

## Use Cases

### 1. Rate hedging (corporate borrowers)

A floating-rate borrower (e.g. a corporate with $500M of SOFR-linked debt) can buy an interest rate **cap** (effectively a strip of SOFR call options) to protect against rate spikes above a chosen strike. The premium paid is the cost of insurance against borrowing-cost surges. This is the largest single use case for rate options by notional.

### 2. Macro speculation

Hedge funds and macro PMs use rate options to express directional views on Fed policy or curve shape:
- Buying a SOFR put expiring after the next FOMC = bet that rates rise (futures fall) more than priced in.
- Buying a 10Y Treasury call = bet on a flight-to-quality rally.
- Calendar spreads on Fed Funds options around FOMC meetings = bet on the meeting's reaction function.

### 3. Volatility harvesting

Selling premium on rate options is a major income strategy for [[macro-funds|macro funds]] and pension overlays. The structural [[volatility-risk-premium]] in rate options is similar in magnitude to equity options (3-5 vol points of normal vol), and it operates relatively independently from equity vol regimes -- providing diversification.

### 4. Curve trading

Options on different points of the yield curve let traders express **curve-shape** views:
- Long-vol position on the 2Y vs short-vol on the 10Y = bet that front-end curve is more volatile than the back-end (typical near Fed inflections).
- Steepener via put on 30Y / call on 2Y = bet on the curve steepening, with bounded downside.

### 5. Swaption-based balance-sheet hedging

Pension funds, insurance companies, and bank ALM desks use long-dated swaptions to hedge convexity in their liabilities. The swaption market is the *real* large rate-options market by notional; listed options are a small share.

### 6. Volatility surface arbitrage

Relative-value funds trade the slope of the [[move-index|MOVE]]-implied vol curve, the term structure of swaption vol, and the cross-asset vol spread between rates and equities. This is the rate-vol cousin of dispersion-trading in equity vol.

## Product Comparison

| Product | Venue | Underlying | Settlement | Vol convention | Primary user |
|---|---|---|---|---|---|
| [[sofr|SOFR]] options | CME (listed) | SOFR futures | Physical into future | Price (Black-76) | Short-rate hedgers, macro |
| Treasury options | CME (listed) | Treasury futures (TU/FV/TY/US) | Physical into future | Price (Black-76) | Duration hedgers, macro |
| Fed Funds options | CME (listed) | 30-day Fed Funds future (ZQ) | Physical into future | Price | Fed-path speculators |
| **Caps / floors** | OTC ([[isda]]) | Strip of SOFR forward rates | Cash, per reset period | Flat / caplet vol | Corporate borrowers |
| **Swaptions** | OTC ([[isda]]) | Forward interest-rate swap | Physical or cash | **Normal (bp) vol** | Pensions, insurers, ALM, macro |
| **Bermudan callables** | Embedded in bonds/notes | Underlying swap, multi-exercise | Bond call | Normal vol | Issuers / note buyers |
| [[move-index|MOVE]]-linked RV | Cross-product | Treasury option vol surface | N/A (index) | Yield (bp) vol | Rate-vol RV desks |

The **listed products are exchange-cleared, transparent, and physically settle into a futures position**; the **OTC products are bilateral, ISDA-documented, and carry counterparty risk** but offer the bespoke maturities and curve exposures (swaptions, caps) that institutional liability hedging requires. Most listed flow is short-dated and tactical; most rate vega by notional lives in the long-dated OTC swaption book.

## Risks

- **Underlying is a futures, with its own basis risk**. Treasury options are on Treasury futures, which themselves have basis risk to the cheapest-to-deliver bond. A "10Y rate" move in the cash market doesn't translate 1:1 to a move in TY futures.
- **Convexity asymmetry** -- long-dated swaption books carry significant [[convexity]] risk that is non-linear in rate moves; standard linear DV01 hedges are inadequate in big rate moves.
- **Skew risk** -- rate-option upside skew can compress fast in calm regimes, leaving holders of caps long rich vol that decays. Conversely, skew can spike during stress, making hedges expensive when needed.
- **Liquidity asymmetry** -- around FOMC meetings, options on near-meeting expirations get extremely active; between meetings, even nominally liquid strikes can have wide markets.
- **Quote-convention errors** -- the `100 - rate` futures convention causes real and frequent operational errors. Risk systems must explicitly model the sign relationship.
- **Settlement to futures vs. cash** -- on exercise, you get a futures position, not cash. Exercise into an unhedged futures position can produce overnight gap risk.
- **OTC counterparty risk** -- swaptions and OTC caps/floors carry [[counterparty-risk]] that listed options do not. Post-2008, [[isda-cmta|ISDA CSA]] collateralisation standardised but did not eliminate this.
- **Model risk on swaption pricing** -- normal vs. lognormal vol conventions; SABR vs. local vol vs. Hull-White models all give different prices for OTM swaptions. Mismatched models between counterparties can produce material valuation differences.
- **Rho is the trade, not a side risk** -- unlike equity options where rho is ignorable, rate options *are* a rho trade. Stating exposure as "delta" or "vega" without rho is meaningless.

## Notable Examples

- **2022-2023 rate-hike cycle**: SOFR options activity exploded as corporates rushed to cap floating-rate exposure ahead of and during the most aggressive Fed hike cycle since 1981. SOFR options ADV roughly tripled from 2021 to 2023.
- **2013 "taper tantrum"**: 10Y Treasury futures vol spiked from ~5% to ~10% normal-vol in a few weeks; long-vega swaption holders profited substantially.
- **March 2020 COVID liquidity crisis**: Treasury option markets briefly froze, with bid-ask spreads widening 5-10x normal. The Fed's intervention into Treasury markets restored liquidity within weeks but exposed the fragility of the Treasury basis.
- **August 2024 yen carry unwind**: a coordinated rates-FX-equity stress event spiked the [[move-index|MOVE]] from 90 to 120 in a single week, vindicating long-vol rate hedges.

## Related

- [[options-greeks]] -- with rate-specific behaviour notes
- [[rho]] -- the dominant cross-Greek for rate options
- [[interest-rate-swap]] -- the underlying of a swaption
- [[volatility-surface]] -- the swaption vol cube is the rates analog
- [[variance-swaps]] -- equity-vol cousin; same structured-product vega-recycling dynamic
- [[move-index]] -- the rate-vol benchmark
- [[sofr]] -- the dominant rate underlying post-LIBOR
- [[treasury-futures]] -- the underlying for cash Treasury options
- [[eurodollar]] -- the legacy rate-options market (retired 2023)
- [[fed-funds-futures]] -- short-end Fed-policy options
- [[yield-curve]] -- the macro context for curve-shape trades
- [[duration]] / [[convexity]] -- the bond-math primitives
- [[implied-volatility]] -- general framework
- [[volatility-skew]] -- with rate-specific upside-rate skew
- [[options-risk-budgeting]] -- portfolio-level integration
- [[long-dated-options]] -- LEAPS analogues exist on rate products
- [[macro-trading]] -- the dominant client of rate-vol products
- [[long-volatility-strategies]] -- rate vol as a diversifying long-vol sleeve

## Sources

- [[cme-sofr-options-specs]] -- SOFR options product specification.
- [[cme-treasury-options-specs]] -- Treasury options product specification.
- [[cme-fed-funds-options-specs]] -- Fed Funds options specification.
- [[book-options-futures-and-other-derivatives]] (Hull) -- canonical text covering Black-76 and the rate-options framework.
- [[book-fixed-income-securities]] (Tuckman & Serrat) -- rate-vol modelling and swaptions.
- [[isda]] -- standardised documentation for OTC rate options.
- [[move-index-methodology]] -- ICE methodology for the rate-vol benchmark.
