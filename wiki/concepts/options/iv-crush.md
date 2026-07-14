---
title: "IV Crush"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, volatility, derivatives, event-driven, risk-management, crypto]
aliases: ["IV Crush", "Implied Volatility Crush", "Vol Crush", "Volatility Crush"]
domain: [derivatives, options]
prerequisites: ["[[implied-volatility]]", "[[vega]]", "[[greeks]]"]
difficulty: intermediate
markets: [crypto, options]
related: ["[[long-straddle]]", "[[short-volatility-strategies]]", "[[volatility-term-structure]]", "[[volatility-skew]]", "[[variance-risk-premium]]", "[[vega]]", "[[dvol]]", "[[deribit]]", "[[funding-rate]]", "[[straddle]]", "[[bitcoin-halving]]"]
---

**IV crush** is the abrupt collapse of [[implied-volatility|implied volatility]] in the seconds-to-hours after a known information event resolves. Pre-event, options pricing inflates [[vega]] to reflect uncertainty about a binary outcome. The instant the outcome is known — an earnings print, an FDA vote, an M&A approval, an FOMC statement, a spot-ETF ruling, or a network upgrade — the uncertainty disappears, vega collapses, and every option spanning the event loses extrinsic value **regardless of which way the underlying moved**. IV crush is the canonical reason traders are *directionally correct and still lose money*. In crypto it is measured on [[deribit|Deribit]] and tracked through the [[dvol|DVOL]] index.

## Definition

IV crush is the *negative* leg of the implied-vol cycle around scheduled events. The cycle has two halves:

1. **Pre-event IV ramp** — IV rises in the days/hours before a known event as the market prices event uncertainty. The contract *spanning* the event rises far faster than back-dated contracts, producing an inverted [[volatility-term-structure|term structure]].
2. **Post-event IV crush** — the moment the event resolves, front-cycle IV collapses, typically 30–50% of its pre-event level in absolute vol points (more on extreme names/events).

The crush is *separate from* the underlying's directional move. A coin can rise 8% on a catalyst while the ATM straddle still loses over half its value because the IV component dominates the intrinsic gain.

## Mechanism

### Why IV inflates pre-event

A scheduled event is a planned discontinuity in price discovery. Two flows push IV up:

- **Hedging demand** — holders buy puts (and calls) to hedge the gap; dealers absorb the supply and re-mark IV upward.
- **Speculative demand** — discretionary and retail traders buy short-dated options as binary-event lottery tickets, anchoring on prior outsized moves.

The ramp concentrates in the front cycle that *contains* the event; back-dated IV barely moves, producing a steeply inverted term structure. An inversion of >10 vol points is itself a detection signal for an upcoming catalyst.

### Why IV collapses post-event

Once the event resolves, front-cycle vega no longer prices future uncertainty — only the residual realized-vol uncertainty over the contract's remaining life, which is dramatically lower. The biggest known catalyst in the option's lifespan has occurred, remaining time is short, and dealers who absorbed pre-event vega mark down their offers. The bulk of the crush lands in the first minutes after the headline.

## Common venues (traditional and crypto)

| Event | Typical pre-event IV | Typical post-event IV | Crush |
|-------|---------------------|----------------------|-------|
| Single-stock earnings (mega-cap) | 60–90% | 30–40% | 30–50 vol pts |
| Small-cap biotech FDA vote | 150–300% | 60–100% | 100–200 vol pts |
| FOMC (front SPX/SPY weekly) | +5–10 IV pts | back to baseline | 5–10 vol pts |
| **BTC spot-ETF ruling (Deribit BTC)** | DVOL ramp | "sell-the-news" crush | 15–40 vol pts |
| **Ethereum network upgrade (ETH)** | large ETH IV ramp | sharp crush | 30–60 vol pts |
| **Macro (CPI/FOMC) on BTC/ETH** | DVOL +5–15 pts | back to baseline | 5–15 vol pts |

The classic equity illustration remains instructive: **NFLX Q3 2018** rose ~8% on earnings yet the pre-print ATM straddle lost ~40% because IV crushed from ~95% to ~38% — the textbook "directional win, IV-crush loss." Crypto's equivalents are documented below.

## Impact on strategies

| Strategy | Vega exposure | IV crush impact |
|----------|--------------|-----------------|
| [[long-straddle]] / strangle through event | long vega | Severely negative — the canonical losing trade |
| Long single call/put through event | long vega | Negative — even directionally-correct trades often lose |
| [[short-volatility-strategies\|Short straddle]] / strangle | short vega | Positive — harvests the crush directly |
| [[iron-condor]] (defined-risk short premium) | short vega | Positive — collects crush within wing range |
| Calendar (long back, short front) | net short front vega | Profit if underlying pins between strikes |
| Directional vertical spread | ~vega-neutral | Largely insulated — directional P&L dominates |

The structural lesson: **if you have no view on volatility, do not be net long vega across a known event.** Express directional views through *vega-balanced* spreads, not single options.

## Measuring expected move from IV

The market's pre-event implied move is encoded in the front-cycle ATM straddle:

```
expected_move ≈ front_atm_straddle_price / spot
expected_move ≈ atm_iv × sqrt(days_to_expiration / 365)
```

The straddle-price form is preferred because it captures skew. If BTC is at $60,000 and the day-of-event ATM straddle is $4,200, the market prices a ~7% move — the straddle only "breaks even" if BTC moves more than ~7% either way. Backtest: compare *implied* vs *realized* move across a name's past events; if realized is systematically smaller, short premium into that event has positive expectancy (the [[variance-risk-premium]] at work).

## Crypto specifics

### Crypto catalysts that ramp then crush DVOL on Deribit

Crypto has its own calendar of scheduled binaries that produce the ramp-and-crush cycle on Deribit:

- **Spot-ETF rulings** — the **US BTC spot-ETF approval (Jan 2024)** is the canonical crypto case: DVOL and front-cycle IV ran up into the decision, then crushed on the "sell-the-news" resolution even as the event itself was bullish.
- **Network upgrades** — the **Ethereum Merge (15 Sep 2022)** ran ETH front-month IV to extreme levels for weeks, then crushed hard once the upgrade completed without incident.
- **Macro prints** — **FOMC and CPI** move BTC/ETH materially; DVOL and front-weekly IV ramp into the release and normalize after, a smaller crush analogous to SPX FOMC weeklies.
- **[[bitcoin-halving|Halvings]], major legal rulings (e.g., SEC cases), and large token unlocks** — each a dated catalyst around which front-cycle IV inflates and then decays.

### 24/7 resolution — the crush happens live, not over a gap

The key structural difference from equities: crypto trades **24/7**, so events resolve *while the market is fully open*. There is no post-market print and overnight gap — the crush unfolds continuously and can be watched (and traded) in real time on DVOL and the term structure. This means the crush is often faster and cleaner, and there is no "assignment / gap-open" step; a premium seller can buy back into the crush immediately rather than waiting for the next session. It also means the pre-event inverted term structure is a live, observable detection signal on Deribit.

### Inverse settlement and funding

Deribit options are **inverse** (coin-margined), so IV-crush P&L accrues in the coin and must be read in cash terms (see [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]]). Around big catalysts, perpetual [[funding-rate|funding]] often spikes with positioning, so an event trade that hedges delta with perps carries an extra funding line through the event window.

### Weekend and unscheduled events

Not every crypto vol event is a scheduled crush. Some of the largest DVOL moves have come from **unscheduled weekend shocks** (exchange failures, depegs, cascade liquidations) — these are vol *spikes*, the opposite of a crush, and they punish short-vega books that sold "cheap" post-crush premium. The lesson: the harvest trade (selling pre-event vega) is distinct from carrying naked short vega through crypto's tail-heavy, always-open tape.

## How to trade it

### Selling premium pre-event (the harvest trade)

Sell vega-rich front-cycle premium 1–3 days before the event, buying it back post-crush. Structures: short ATM straddle (pure vega, undefined risk), short strangle (lower vega per margin), [[iron-condor]] (defined risk), or a calendar (long back / short front). Risk: a "tail print" outside the wings loses — size to the historical largest move on that asset (which for BTC/ETH can be large).

### Fading the crush (rare long-vol entry)

After the crush, post-event IV sometimes *undershoots* the realistic future-vol baseline; long-vega positions established in the hour after can profit if DVOL normalizes upward. Less reliable than the harvest trade; mostly a pro vol-book play.

### What not to do

Buying long premium *into* a known event without an explicit vol view is, on average, a losing trade — the [[variance-risk-premium]] is positive precisely because IV crush systematically over-rewards short premium.

## Getting the Data (CryptoDataAPI)

IV crush is timed by the catalyst calendar and confirmed by the vol regime; the IV surface and DVOL themselves come from Deribit / Greeks.live:

- **Event / catalyst calendar** — `GET /api/v1/event/calendar` (filterable events up to 30d out) and `GET /api/v1/event/regime` (forward catalyst bias). See [[cryptodataapi-regimes]].
- **Volatility regime** — `GET /api/v1/volatility/regime` and `GET /api/v1/volatility/regime/score` to confirm compression/expansion around the event. See [[cryptodataapi-regimes]].
- **Options positioning** — `GET /api/v1/market-intelligence/options` (BTC options OI, volume, max pain). See [[cryptodataapi-market-intelligence]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

## Related

- [[long-straddle]] — the strategy most damaged by IV crush
- [[short-volatility-strategies]] — strategies that harvest the crush
- [[volatility-term-structure]] — how the inversion signals an upcoming event
- [[volatility-skew]] — the strike dimension of the surface
- [[variance-risk-premium]] — why short premium into events pays on average
- [[vega]] — the exposure IV crush acts on
- [[dvol|DVOL]] — the crypto IV index where the crush is measured (Deribit/Greeks.live)
- [[deribit]] — the venue; inverse contracts and event dynamics
- [[bitcoin-halving]] — a scheduled crypto catalyst
- [[funding-rate]] — the correlated carry line through event windows

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on the term structure of IV and event-driven vol
- Sinclair, E. (2013), *Volatility Trading* — variance risk premium and event-vol harvesting
- Deribit public documentation — DVOL methodology; BTC spot-ETF and Ethereum Merge IV history
- CBOE Options Institute — educational materials on event-implied volatility and expected move
