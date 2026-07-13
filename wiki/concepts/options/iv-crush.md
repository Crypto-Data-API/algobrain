---
title: "IV Crush"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, volatility, derivatives, earnings, risk-management]
aliases: ["IV Crush", "Implied Volatility Crush", "Vol Crush", "Volatility Crush"]
domain: [derivatives, options]
prerequisites: ["[[implied-volatility]]", "[[vega]]", "[[options-greeks]]"]
difficulty: intermediate
related: ["[[volatility-risk-premium-decay]]", "[[long-straddle]]", "[[short-volatility-strategies]]", "[[options-trading-pitfalls]]", "[[options-trader-psychology]]", "[[volatility-term-structure]]", "[[volatility-skew]]", "[[variance-risk-premium]]", "[[options-premium-selling]]", "[[fed-meeting]]", "[[fda-decision]]", "[[managing-winners]]"]
---

**IV crush** is the abrupt collapse of [[implied-volatility|implied volatility]] in the seconds-to-hours after a known information event resolves. Pre-event, options pricing inflates [[vega|vega]] to reflect uncertainty about a binary outcome. The instant the outcome is known — earnings prints, FDA panel votes, M&A approvals announce, the FOMC statement releases — the uncertainty disappears, vega collapses, and every option that spans the event loses extrinsic value regardless of which way the underlying moved. IV crush is the canonical reason traders are *directionally correct on earnings and still lose money*.

## Definition

IV crush is the *negative* leg of the implied-volatility cycle around scheduled events. The cycle has two halves:

1. **Pre-event IV ramp** — implied volatility rises in the days/hours before a known event as the market prices in event uncertainty. Front-cycle IV (the contract spanning the event) rises far faster than back-month IV, producing an inverted [[volatility-term-structure|term structure]].
2. **Post-event IV crush** — the moment the event resolves, the front-cycle IV collapses. The drop is typically 30-50% of the pre-event IV in absolute vol points, sometimes more on names with extreme pre-event ramps.

The crush is *separate from* the directional move of the underlying. A stock can rise 8% on earnings while the ATM straddle still loses 60% of its value because the IV component dominates the intrinsic gain.

## Mechanism

### Why IV inflates pre-event

A scheduled event is a planned discontinuity in price discovery. For the minutes spanning the announcement, the market does not know the outcome. Two flows push IV up:

- **Hedging demand** — long-stock holders buy puts (and sometimes calls) to hedge the gap. Dealers absorb that supply and re-mark IV upward to clear the imbalance.
- **Speculative demand** — discretionary and retail traders buy short-dated calls and puts as binary-event lottery tickets, anchoring on prior outsized prints (TSLA's old +20% earnings moves, NVDA's recent prints, etc.).

The ramp concentrates in the front weekly or monthly cycle that *contains* the event date. Back-month IV barely moves. This produces a steeply inverted term structure: front-week IV at 80%, next-month at 35%, three-months at 28%. An inverted term structure of >10 vol points is itself a detection signal for an upcoming event.

### Why IV collapses post-event

Once the event resolves, the front-cycle vega is no longer pricing future uncertainty — it is pricing only the residual realized-vol uncertainty over the remainder of the contract's life. That uncertainty is dramatically lower:

- The biggest known catalyst in the option's lifespan has now occurred.
- The remaining time to expiration may be days or hours, in which IV cannot reasonably justify its pre-event level.
- Dealers who absorbed pre-event vega supply now mark down their offers.

The collapse happens fast — typically the bulk of it in the first 1-5 minutes after the headline. By the next morning's open, post-event IV is back near the underlying's normal long-run level.

## Most Common Venues

| Event | Typical pre-event IV | Typical post-event IV | Crush magnitude |
|-------|---------------------|----------------------|-----------------|
| Single-stock earnings (mega-cap) | 60-90% | 30-40% | 30-50 vol points |
| Single-stock earnings (small-cap biotech) | 150-300% | 60-100% | 100-200 vol points |
| FDA PDUFA / panel vote | 100-250% | 40-80% | 60-170 vol points |
| M&A close vote / regulatory approval | 50-120% | 20-40% | 30-80 vol points |
| FOMC meeting (front SPX/SPY weekly) | +5-10 IV points | back to baseline | 5-10 vol points |
| Major economic data (CPI, NFP) | +3-5 IV points | back to baseline | 3-5 vol points |

The richest crushes are on small-cap biotechs around binary FDA decisions, where front-week IV can run 250%+ and crush to 60% intraday on the announcement. Single-stock earnings on liquid mega-caps (NVDA, NFLX, TSLA, META) run 60-90% pre-print and crush to 30-40%. Index events (FOMC, CPI) produce smaller crushes because the index implied vol baseline is much lower and the event uncertainty is a smaller fraction of total uncertainty.

## Magnitude: Empirical Reference Points

Documented historical magnitudes for IV crush:

- **NVDA earnings (2024-2025 cycle)**: front-week ATM IV consistently ramped from ~50% to ~110% in the week before, crushing to ~45-55% in the first hour after the print.
- **NFLX Q3 2018 earnings** (the canonical "directional win, IV-crush loss" case): stock rose ~8% on the print; the pre-print ATM straddle lost ~40% of its value because IV crushed from ~95% to ~38%.
- **Beyond Meat 2019 IPO post-lockup events**: front-week IV exceeded 200% in 2019; routine 100-150 vol-point crushes intraday.
- **FOMC days (2022-2023 hiking cycle)**: SPX 0DTE ATM IV typically ran 35-40% in the hour before the statement, crushing to 18-22% in the first 30 minutes after.

## Impact on Strategies

| Strategy | Vega exposure | IV crush impact |
|----------|--------------|-----------------|
| [[long-straddle]] / strangle through earnings | long vega | Severely negative — the canonical losing trade |
| Long single-leg call or put through earnings | long vega | Negative — even directionally-correct trades often lose |
| [[short-volatility-strategies\|Short straddle]] / strangle | short vega | Positive — harvests crush directly |
| [[iron-condors\|Iron condor]] (defined-risk short premium) | short vega | Positive — collects crush within wing range |
| Calendar spread (long back, short front) | net short vega front, long back | Profit *if* underlying pins between strikes |
| Directional vertical spread | vega-neutral or slightly biased | Largely insulated — directional P&L dominates |
| Diagonal spread | depends on construction | Mixed — front-leg crush helps short, hurts long |

The structural lesson: **if you have no view on volatility, do not be net long vega across a known event**. If you have a directional view, express it through *vega-balanced* spreads, not single options.

## Measuring Expected Move from IV

The market's pre-event implied move is encoded in the front-cycle ATM straddle:

```
expected_move ≈ front_atm_straddle_price / spot
expected_move ≈ atm_iv × sqrt(days_to_expiration / 365)
```

For practical use, the straddle-price approximation is preferred because it includes skew effects. If NVDA is at $500 and the day-of-earnings ATM straddle is bid $25.00, the market is pricing a ~5% move — meaning the straddle "breaks even" only if NVDA moves more than ~5% in either direction. See implied-earnings-move.

A common backtest: compare *implied* move to *realized* move across all earnings announcements for a given name. If realized move is systematically smaller than implied, short premium across earnings has positive expectancy on that name. If realized exceeds implied, long premium does. Most large-cap names show the former.

## How to Trade It

### Selling premium pre-event (the harvest trade)

Sell vega-rich front-cycle premium 1-3 days before the event, expecting to buy it back post-crush. Common structures:

- **Short ATM straddle** — pure vega harvest, undefined risk, requires conservative sizing
- **Short strangle** — slightly OTM on each side, lower vega per dollar of margin
- **[[iron-condors\|Iron condor]]** — defined-risk version, lower yield but bounded loss
- **Calendar spread** — long back-month / short front-month at the same strike, profits if underlying pins near strike and front-month vega crushes

Risk: the crush helps, but a directional move outside the wings (a "tail print") loses. Position sizing must account for the historical largest move on that name.

### Fading IV crush as a long-vol entry (the rare bullish-vol trade)

After the crush, IV is often *too* low — the post-event IV may temporarily undershoot the realistic future-vol baseline. Long-vega positions established in the hour after a print can profit if vol normalizes upward over the following days. Less reliable than the harvest trade; mostly used by professional vol books.

### What not to do

Buying long premium *into* a known event without an explicit vol view is, on average, a losing trade. The [[variance-risk-premium]] is positive precisely because IV crush systematically over-rewards short premium and under-rewards long. See [[volatility-risk-premium-decay]] and earnings-iv-crush.

## Related

- [[long-straddle]] — the strategy most damaged by IV crush
- [[short-volatility-strategies]] — strategies that benefit
- [[volatility-risk-premium-decay]] — the broader risk-premium framework
- [[options-trading-pitfalls]] — IV crush is pitfall #2 in the options pitfalls catalog
- [[volatility-term-structure]] — how the inversion signals an upcoming event

## Sources

- Sheldon Natenberg, *Option Volatility and Pricing* (2nd ed., McGraw-Hill) — term structure of IV and event-driven vol behaviour
- Euan Sinclair, *Volatility Trading* (Wiley) — variance risk premium and earnings-vol harvesting
- CBOE Options Institute — educational materials on event-implied volatility and expected move
- tastytrade research archive — empirical studies on IV crush and pre-earnings premium selling
