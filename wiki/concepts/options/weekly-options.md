---
title: "Weekly Options"
type: concept
created: 2026-05-06
updated: 2026-07-14
status: good
tags: [options, derivatives, weekly, crypto]
aliases: ["Weeklys", "Weeklies", "SPXW", "Weekly Options", "Deribit Weeklies"]
domain: [derivatives, options]
prerequisites: ["[[options]]", "[[greeks]]", "[[theta]]", "[[gamma]]"]
difficulty: intermediate
markets: [crypto, options]
related: ["[[0dte-trading]]", "[[gamma-scalping]]", "[[deribit]]", "[[dvol]]", "[[max-pain]]", "[[funding-rate]]", "[[implied-volatility]]", "[[iv-crush]]", "[[options-portfolio-construction]]"]
---

**Weekly options** ("Weeklys") are option contracts that expire within a week of listing rather than following the traditional monthly cycle. Cboe introduced them for equities/indices in 2005; today they dominate index volume. In crypto they are the everyday tool: [[deribit|Deribit]] lists **daily, weekly (Friday), monthly, and quarterly** BTC/ETH options, all cash-settled to the Deribit index at **08:00 UTC**. Weeklies have a fundamentally different Greeks profile from monthlies — **faster [[theta]] decay, sharper [[gamma]] near expiry, and lower [[vega]]** — which makes them powerful for event-driven trading and dangerous for un-managed short positions. In crypto's high-[[realized-volatility|realized-vol]] tape, short weekly gamma is among the fastest ways to lose money.

## Overview

Weeklies were an additive innovation over the monthly third-Friday cycle: rather than wait for the next monthly, traders target almost any specific day for entry and exit. Origin and expansion in traditional markets:

- **2005** — first Cboe "Weeklys" on a small set of products.
- **2010s** — broad expansion to hundreds of equity, ETF, and index underliers.
- **Nov 2022** — Cboe completes daily SPX expirations (adding Tuesday/Thursday SPXW), turning SPX into a continuous-expiration market.
- **2023+** — weekly and daily options exceed monthly volume on the index complex; [[0dte-trading|0DTE]] becomes a major share of activity.

Crypto followed the same arc: Deribit's short-dated and daily BTC/ETH options now carry a large share of volume, and 0DTE-style crypto trading has grown around daily expiries.

## Weekly vs monthly: the Greeks (asset-agnostic core)

The differences in Greeks structure change strategy design, in crypto and TradFi alike.

**Theta (time decay):**

- Theta is non-linear and accelerates into expiration. A weekly spends its whole life inside that acceleration zone, so a same-strike weekly loses time value much faster per day than a monthly at the same delta.
- For premium sellers, weeklies offer higher daily theta yield per unit of premium — but the position must be actively managed because everything else accelerates too.

**Gamma:**

- Gamma rises sharply in the final days; a weekly's late-life gamma can be 5–10× the same-delta 30-day option.
- Sharp gamma means small underlying moves create outsized P&L swings both ways. **Short gamma in the last day or two of a weekly can suffer catastrophic losses on a single move** — acute in crypto, where a 5–10% intraday move is routine.

**Vega:**

- Vega declines toward expiration; weeklies have low vega, so [[implied-volatility|IV]]/[[dvol|DVOL]] changes contribute less to their P&L. They are a closer-to-pure bet on realized price movement and time.

**Practical implication:** weeklies trade *time and price*; monthlies trade *time, price, and vol*. Choose the tenor whose exposure you actually want.

## Crypto specifics (Deribit)

### Cycle and settlement — no AM/PM distinction

- **Expiries** on Deribit: **daily**, **weekly (Fridays)**, **monthly**, and **quarterly (last Friday of Mar/Jun/Sep/Dec)** — all at **08:00 UTC**.
- **Settlement**: every Deribit option, weekly or quarterly, is **cash-settled to the Deribit index** (a composite of major spot venues) at 08:00 UTC. Unlike SPX's split between AM-settled monthlies (SOQ) and PM-settled SPXW weeklies, crypto has **no AM/PM settlement mismatch** — so a Deribit calendar spread does not carry the overnight settlement-basis risk that an SPX/SPXW calendar does. This is a genuine simplification for crypto calendar and diagonal structures.
- **Inverse (coin-margined)**: settlement value is paid/received in the coin; read short-weekly risk in cash terms (see [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]]).
- **European, cash-settled**: no physical assignment/pin-risk in the equity sense — the option settles to the index number, avoiding the "will I be assigned?" ambiguity of physically-settled weeklies.

### 24/7, weekend expiries, and funding

- Crypto weeklies live **through weekends**, and the Friday 08:00 UTC expiry means a weekly's most dangerous final hours can coincide with thin overnight/weekend liquidity — amplifying the short-gamma risk above.
- Rolling weekly hedges in [[perpetual-futures|perps]] pay/receive [[funding-rate|funding]] continuously; weekly and monthly Deribit expiries interact with **[[max-pain|max-pain]] gravitation** and dealer [[gamma-exposure|gamma]] hedging around 08:00 UTC, and with perp funding resets across venues (see [[deribit]]).

### Tax note

The US **[[section-1256-contracts|Section 1256]] / 60-40** treatment that makes SPXW attractive for TradFi traders is an equity-index feature and **does not apply to crypto options** — crypto options are taxed under local rules (e.g., AU trader tax; see the wiki's tax section). Do not import the SPX tax rationale into a crypto weekly-options plan.

## Portfolio use cases (crypto)

- **Precise event timing** — sell a weekly straddle into a known catalyst (FOMC, CPI, an ETF ruling) to capture [[iv-crush]] or the realized move with no exposure beyond the event window.
- **Tactical [[gamma-scalping|gamma scalping]]** — long-gamma weekly positions in a known catalyst window, actively delta-hedged on Deribit + perps, harvesting realized vol > implied.
- **Faster premium decay** — diagonal/calendar overlays that sell short-dated Deribit weekly premium against longer-dated positions extract theta faster on the short leg.
- **Defined-risk event bets** — a weekly butterfly or iron condor for a known event: fixed cost, cash-settled, no assignment risk.
- **Rolling tail hedges** — buy weekly OTM puts as cheap, short-duration protection that rolls each week, sizing hedge cost to the current [[dvol|DVOL]] regime.

## Risks

- **Gamma blowups** — short weekly positions can lose multiples of premium collected on a single sharp move; worst-case single-day losses in options trading come from short gamma in the last 1–2 days of a weekly. Crypto's move sizes make this worse than equities.
- **Liquidity at non-standard strikes** — strikes outside the heavily-traded range can have very wide spreads in the final hours, especially over weekends.
- **Front-of-curve vol crowding** — daily/weekly premium selling has become a consensus trade in both TradFi and crypto, which can erode the [[variance-risk-premium|volatility risk premium]] at the very front of the term structure.
- **Funding through the roll** — weekly perp hedges accrue funding that must be netted against the theta harvested.

## Getting the Data (CryptoDataAPI)

Weekly-options positioning is read through options OI/max-pain, the catalyst calendar, and funding; the IV surface and DVOL come from Deribit / Greeks.live:

- **Options OI / max pain — expiry positioning** — `GET /api/v1/market-intelligence/options` (BTC options OI, volume, max pain). See [[cryptodataapi-market-intelligence]].
- **Event calendar — time weeklies to catalysts** — `GET /api/v1/event/calendar`. See [[cryptodataapi-regimes]].
- **Funding — the roll carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC`. See [[cryptodataapi-derivatives]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
```

## Related

- [[0dte-trading]] — the same-day weekly extreme
- [[gamma-scalping]] — long-gamma weekly positions harvested via delta hedging
- [[deribit]] — the crypto venue; daily/weekly/monthly/quarterly expiries at 08:00 UTC
- [[dvol|DVOL]] — the vol benchmark for weekly IV (Deribit/Greeks.live)
- [[max-pain]] — expiry gravitation around Deribit weeklies/monthlies
- [[iv-crush]] — what a weekly straddle sold into an event harvests
- [[funding-rate]] — the carry on rolling weekly perp hedges
- [[implied-volatility]] — the vol input weeklies carry little of
- [[options-portfolio-construction]] — fitting weeklies into a book

## Sources

- Cboe Weeklys product history and SPXW specifications (Tuesday/Thursday additions, Nov 2022)
- Deribit public documentation — expiry schedule, index cash settlement, and inverse contract specs
- [[book-option-volatility-and-pricing]] — Natenberg on the theta/gamma acceleration of short-dated options
- OCC settlement and exercise rules (traditional-market context)
