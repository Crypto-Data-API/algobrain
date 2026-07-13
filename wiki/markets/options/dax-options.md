---
title: "DAX Options (ODAX)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, stocks, europe]
aliases: ["DAX Options", "ODAX", "Eurex DAX Options"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[ftse-100-options]]", "[[nikkei-options]]", "[[eurex]]", "[[dax]]", "[[vdax-new]]", "[[stoxx-50-options]]", "[[american-vs-european-options]]", "[[cash-vs-physical-settlement]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[options-greeks]]", "[[short-strangle]]", "[[iron-condor]]", "[[dispersion-trading]]", "[[currency-hedging]]", "[[index-reconstitution]]"]
---

DAX options are Eurex-listed, cash-settled, European-style [[index-options]] on the **DAX 40 Index** — the German blue-chip index, expanded from 30 to 40 constituents in **September 2021**. The standard contract (symbol **ODAX**) carries a **€5 per index point** multiplier. DAX options are denominated in EUR, settle to a special intraday-auction value, and are the most liquid equity-index options product in continental Europe alongside Eurex's [[stoxx-50-options|EURO STOXX 50 options]]. Smaller Mini-DAX and Micro-DAX derivative products exist for retail-scale sizing — see the contract-mechanics section — but ODAX is the institutional benchmark.

## Overview

The DAX 40 represents the 40 largest German listed companies by free-float market cap, replacing the historical DAX 30 in September 2021 to broaden sector representation and align with international large-cap conventions. DAX options on Eurex (ticker **ODAX**) are the dominant German equity-index volatility product, used for portfolio hedging by European pension funds and insurers, dispersion trading vs single-name DAX components, and EUR-denominated [[variance-risk-premium]] harvesting.

A particular feature of the DAX index that traders coming from US indices should know: **the DAX is a total-return (performance) index**, meaning it includes dividend reinvestment. This is in contrast to SPX (price-return) and most other major US indices. The performance-index construction means that DAX option pricing does **not** require the dividend-yield correction term that SPX options pricing does — dividends are already inside the index level — though variations such as the DAX Price Index (Kursindex) exist for specific use cases.

## Contract Mechanics

| Spec | Value |
|---|---|
| Underlying | DAX 40 Performance Index |
| Multiplier | **€5 per index point** (ODAX standard contract) |
| Exercise style | European |
| Settlement | Cash, in EUR |
| Strike intervals | 50 index points standard; 25 points near-the-money; some 10-point strikes on weeklies |
| Tick size | 0.1 index point (= €0.50) |
| Trading hours | Eurex pre-trading 07:30 CET; main trading 09:00–17:30 CET; post-trading until 20:30 CET (varies by product) |
| Symbol | ODAX (standard); MDAX-related symbols for micro variants |
| Tax treatment | Jurisdiction-specific (no US Section 1256 analog) |
| Listed | Eurex (Deutsche Börse derivatives exchange) |

At a DAX level of 18,000, a single ODAX contract represents **€90,000 of notional** (18,000 × €5) — substantially smaller than an SPX contract (~€460,000 equivalent at SPX 5000) and closer to a [[xsp-options|XSP]] contract in size. This per-contract notional is a key reason DAX options are used by mid-sized European institutional accounts directly without needing a "mini" version.

Eurex also lists smaller-sized DAX-derivative products (Mini-DAX futures, Micro-DAX futures, and contract variations) that target retail and smaller institutional sizes. Specific multipliers vary by product — verify on the current Eurex contract spec sheet before sizing.

## Settlement

DAX option settlement is **cash, in EUR**, based on a **DAX intraday-auction settlement value** computed by the Frankfurt Stock Exchange on expiration day:

- **Expiration day**: third Friday of the expiration month (monthly contracts); weekly expirations available on Fridays for selected weeks.
- **Settlement value**: the **DAX intraday auction price** computed at **13:00 CET** (the Frankfurt midday auction) on expiration day. This is functionally equivalent to a "midday SOQ" — calculated from a single-price auction in DAX 40 components rather than from staggered opening prints.
- **Trading**: option trading on the expiring contract typically halts shortly before the 13:00 CET auction.

The **midday-auction settlement** is structurally distinct from US AM-settlement (open auction) and PM-settlement (close): it concentrates settlement-driven flows into a narrow Frankfurt-midday window, with the actual SOQ-equivalent value published shortly after. This affects pinning dynamics and the risk profile of expiry-day positioning relative to US-style expirations.

There is **no AM/PM regime split** on DAX options as there is on SPX — all monthlies and weeklies use the same intraday-auction methodology, simplifying multi-leg structures across expirations.

## Liquidity & Spreads

DAX options are the most liquid equity-index options product traded outside the US (vying with EURO STOXX 50 options for the title of most-liquid European product):

- **Volume** — typically **80,000-150,000 ODAX contracts/day**; activity heavily concentrated in front-month and second-month expirations.
- **Open interest** — concentrated around round-number strikes and key technical levels in DAX cash terms (e.g., 16,000 / 18,000 / 20,000 multiples).
- **Bid/ask** — typically **0.2-0.5 index points wide** at near-the-money strikes (€1-€2.50 per contract); widening to 1+ index points on far-OTM wings.
- **Strike density** — 50-point intervals broadly; 25-point near-the-money; some 10-point strikes near current spot on weeklies.
- **Quote sizes** — 10-50 contracts at the inside in normal markets; market-maker depth strong but thinner than US SPX.
- **Globex parallel** — Eurex has its own electronic trading platform with deep market-maker presence; off-hours and US-overlap-hours trading is supported but liquidity peaks in European session.

## Greeks & Volatility-Surface Behaviour

ODAX options price under standard European Black-Scholes mechanics (cash-settled, no early exercise), but the **total-return index construction** is the critical pricing wrinkle:

- **No dividend-yield term** — because the DAX is a performance (total-return) index, reinvested dividends are already inside the index level. A pricing model that subtracts a separate dividend yield (correct for the price-return [[spx-options|SPX]]) will **misprice ODAX** unless the dividend term is set to zero. This is the single most common modelling error for traders importing US options intuition. The forward of a total-return index grows at the full risk-free rate with no dividend drag.
- **Downside skew** — negative [[volatility-skew|skew]] (OTM puts richer than calls) from European pension/insurer hedging demand, steepening in risk-off regimes; broadly similar shape to SPX but with episodic European-crisis fat tails.
- **Sector-driven surface** — heavy weights in **autos** (Volkswagen, BMW, Mercedes, Porsche), industrials, and financials mean the surface reacts to auto/trade and Eurozone-banking shocks more than a diversified index; single-sector events can steepen DAX skew independently of broader European vol.
- **[[vdax-new|VDAX-NEW]]** — the DAX volatility index, the German analog of the [[vix|VIX]], is the standard read on ODAX implied-vol regime.
- **Strong market-maker depth** — Eurex's electronic franchise gives tight ATM books, so DAX surfaces are among the most reliably quoted outside the US.

### Term Structure

ODAX vol term structure is in **contango in calm regimes** and inverts to **backwardation in stress**, reflecting the European [[variance-risk-premium]]. ECB meeting dates, German Ifo / manufacturing data, and Eurozone political/fiscal events create localized term-structure humps; the 2010-2012 sovereign-debt era and the 2022 energy shock produced unusually elevated and persistent backwardation. Because **all ODAX expirations share the single 13:00 CET midday-auction settlement** (no AM/PM split), calendar and diagonal structures roll cleanly across expirations without a settlement-regime mismatch.

## Common Spread Structures

| Structure | Construction | Typical ODAX use |
|---|---|---|
| **Put spread** | Long higher-strike put, short lower-strike put | Cost-reduced downside hedge for EUR institutional books |
| **[[short-strangle|Short strangle]]** | Sell OTM put + OTM call | Harvest European [[variance-risk-premium]] in range-bound markets |
| **[[iron-condor|Iron condor]]** | Short strangle + protective wings | Defined-risk premium selling around the midday-auction expiry |
| **Risk reversal** | Long call, short put (or reverse) | Express directional + skew view on German large-caps |
| **Calendar spread** | Long back-month, short front-month same strike | Trade term structure around ECB / data events (clean, single-settlement) |
| **Dispersion** | Short ODAX vol, long single-name DAX-component vol | Short implied correlation via Eurex's deep single-name franchise |
| **Cross-region pair** | DAX vol vs SPX / SX5E / FTSE vol | ECB-vs-Fed divergence; German-exporter / auto-cycle expression |

## Typical Strategies / Use Cases

### European-portfolio hedging

DAX options are the primary portfolio hedge for German and broader European equity portfolios that have heavy DAX exposure (German pensions, insurance company general accounts, family offices). Long ODAX puts pay out in EUR, avoiding the FX mismatch that would arise from hedging a EUR portfolio with USD-denominated [[spx-options|SPX]] puts.

### EUR-denominated vol expression

Long or short volatility views on European large-caps are most cleanly expressed via DAX options or [[stoxx-50-options|EURO STOXX 50 options]]. The vol regimes are correlated with US large-caps but have meaningful regional independence — European political risk, ECB policy shifts, and German manufacturing/auto cycle effects can move DAX vol independently of SPX vol.

### Dispersion vs single-name DAX components

Selling ODAX vol against buying single-name vol on the underlying DAX components captures the European dispersion premium, the same structural trade as SPX-vs-S&P-500-components dispersion in the US. Eurex's deep single-name options franchise (especially in autos, financials, and industrials) makes the dispersion legs operationally feasible at institutional size.

### Cross-region pair trades

DAX-vs-SPX or DAX-vs-EURO-STOXX-50 dispersion expresses views on regional economic divergence: "European autos at risk", "German exporters caught in trade dispute", "ECB diverging from Fed". The pair trade requires careful currency and notional matching but provides the cleanest regional-divergence vol expression.

### Premium-selling strategies

ODAX [[short-strangle|strangles]] and [[iron-condor|iron condors]] capture the European [[variance-risk-premium]]. Empirically the European VRP has been comparable to the US VRP in magnitude over long windows, with some periods (notably 2010-2012 sovereign-debt era) showing structurally larger VRP due to elevated tail-risk pricing.

## Risks / Quirks

- **Performance-index construction** — DAX is total-return; pricing models that include a separate dividend-yield term (designed for SPX-style price indices) may misprice DAX options unless adjusted. Most standard pricing libraries handle this correctly when given the right index type, but it is a real source of error in homemade models.
- **Index-composition change in Sep 2021** — the DAX 30 → DAX 40 transition expanded the index, changed sector weights, and altered the implied-volatility regime. Historical DAX vol data pre-2021 reflects a different index; backtests should account for the structural break.
- **Concentrated sector exposure** — DAX is heavily exposed to **autos** (Volkswagen, BMW, Mercedes, Porsche), **industrials**, and **financials**. A single sector shock (auto-emissions scandal, banking stress) can move DAX in ways the broader European market does not see.
- **Currency** — for non-EUR investors, DAX option P&L is denominated in EUR; FX moves can offset or amplify P&L. See [[currency-hedging]].
- **Midday-auction settlement** — a 13:00 CET single-auction settlement creates concentrated flow at expiration; pinning and slippage dynamics differ from US AM/PM-settled products.
- **Eurex hours vs US hours** — DAX options are most liquid 09:00-17:30 CET; US-overlap hours have thinner books, and cross-Atlantic hedging requires care for execution timing.
- **Tax treatment is jurisdiction-specific** — German, US, UK, and other tax regimes treat DAX options differently. There is no Section-1256-style 60/40 blend; consult local tax advice.
- **Lower vol than SPX historically** — but with episodic spikes during Eurozone crises (2010-2012, 2022 energy shock) that exceeded equivalent SPX moves.

## Tax Treatment

DAX options have **no analog to US Section 1256 treatment**. Tax treatment depends on the holder's jurisdiction:

- **Germany** — gains taxed under Abgeltungsteuer (flat 25% capital gains tax + solidarity surcharge + church tax where applicable) for retail; institutional treatment varies. Loss-offset rules and limits apply.
- **US holders** — typically taxed as ordinary capital gains/losses on a section-1234-style basis; foreign-listed index options generally do **not** qualify for §1256 treatment unless specifically designated, and most non-US index options do not qualify. CFTC and IRS guidance evolves; consult professional advice.
- **UK holders** — capital gains tax with annual exemption; spread-betting wrappers (where available) can change the treatment.
- **Other jurisdictions** — varied; consult local tax counsel.

The absence of US Section 1256 treatment for DAX options is a meaningful disadvantage for US-resident traders comparing DAX options vs SPX options for European-equity exposure. US investors who want EUR-denominated equity-index exposure and US tax efficiency often have to choose between DAX (tax-disadvantaged) and SPX (currency-disadvantaged) — a real trade-off with no clean solution.

## Comparison to Other Major Index Options

| Feature | **DAX (ODAX, Eurex)** | [[spx-options\|SPX]] | [[ftse-100-options\|FTSE 100]] | [[nikkei-options\|Nikkei 225]] |
|---|---|---|---|---|
| Index type | Cap-weighted, **total-return** | Cap-weighted, price-return | Cap-weighted, price-return | **Price-weighted**, price-return |
| Currency | EUR | USD | GBP | JPY |
| Multiplier | €5 / pt | $100 / pt | £10 / pt | ¥1,000 / pt |
| Exercise | European | European | European | European |
| Settlement | Cash, **13:00 CET midday auction** | Cash, AM/PM SOQ | Cash, opening-auction EDSP | Cash, SQ |
| Expiry day | 3rd Friday | 3rd Friday (+ weeklies) | 3rd Friday | **2nd Friday** |
| AM/PM split | **No** (single methodology) | **Yes** | No | No |
| Dividend term in pricing | **None** (total-return) | Subtract div yield | Subtract div yield | Subtract div yield |
| US §1256 60/40 | **No** | **Yes** | No | No |
| Vol index | [[vdax-new\|VDAX-NEW]] | [[vix\|VIX]] | [[vftse\|VFTSE]] | [[vnky\|VNKY]] |
| Distinctive driver | Autos/industrials, total-return, ECB | Global benchmark | Resources/financials, intl revenue | Yen-carry / BoJ |

The two features that most distinguish ODAX from the rest are the **total-return index construction** (no dividend term in pricing — unique among these four) and the **single midday-auction settlement** with no AM/PM split, which simplifies multi-expiry structures relative to SPX. Alongside [[stoxx-50-options|EURO STOXX 50 options]], ODAX is the most liquid equity-index options product in continental Europe.

## Related

- [[index-options]] — overview of the franchise
- [[options]] — options fundamentals
- [[spx-options]] — US large-cap analog
- [[ftse-100-options]] — UK large-cap analog
- [[nikkei-options]] — Japanese large-cap analog
- [[stoxx-50-options]] — pan-European large-cap (Eurex sibling)
- [[eurex]] — the listing exchange
- [[dax]] — the underlying index
- [[vdax-new]] — German VIX-equivalent
- [[american-vs-european-options]]
- [[cash-vs-physical-settlement]]
- [[implied-volatility]], [[volatility-skew]], [[options-greeks]]
- [[short-strangle]], [[iron-condor]]
- [[dispersion-trading]] — DAX dispersion is a deep European franchise
- [[currency-hedging]] — relevant for non-EUR investors
- [[index-reconstitution]] — DAX 30 → DAX 40 regime change

## Sources

- Eurex DAX options product specifications (eurex.com — DAX options contract spec) — multiplier, settlement, expirations.
- Deutsche Börse — DAX 40 Index methodology and component weights.
- Deutsche Börse September 2021 announcement — DAX 30 to DAX 40 expansion details.
- Eurex Frankfurt — intraday auction settlement methodology.
- Eurex Mini-DAX and Micro-DAX product specifications for sizing variants.
