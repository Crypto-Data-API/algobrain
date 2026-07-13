---
title: "Cumulative Volume Delta (CVD)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [market-microstructure, order-types, indicators, volume, futures, crypto]
aliases: ["CVD", "Cumulative Volume Delta", "Cumulative Delta", "Volume Delta", "Delta"]
related: ["[[order-flow]]", "[[footprint-chart]]", "[[absorption]]", "[[volume]]", "[[volume-profile]]", "[[point-of-control]]", "[[volume-profile-trading-strategy]]", "[[volume-imbalance]]"]
domain: [market-microstructure]
prerequisites: ["[[order-flow]]", "[[volume]]"]
difficulty: intermediate
---

**Cumulative Volume Delta (CVD)** is a running total of net aggressive buying versus aggressive selling. For each trade, **delta** = (volume executed by buyers lifting the offer) − (volume executed by sellers hitting the bid); CVD is the cumulative sum of that delta over time. Where [[volume-profile]] shows *where* volume traded, CVD shows *who was more aggressive* — distinguishing high volume caused by initiative (one side leaning in) from high volume caused by [[absorption]] (one side soaking up the other with resting limit orders).

## Overview

Raw [[volume]] is directionless: a bar showing 10,000 contracts traded doesn't say whether buyers or sellers were the aggressors. [[order-flow]] tools fix this by classifying each trade by **aggressor side** — typically using the trade's execution against the order book: a trade at the ask is buyer-initiated (+delta), a trade at the bid is seller-initiated (−delta). Summing those signed volumes within a bar gives **bar delta**; carrying the sum forward across bars gives **cumulative volume delta**.

CVD is plotted as its own line or sub-chart and read *against price*. The key information is rarely the absolute level — it is the **relationship between price and CVD**: are they confirming each other, or diverging?

## How it is computed

1. For every trade, determine the aggressor side (lift-the-offer = buy; hit-the-bid = sell). This is exact on tick/level-1 data; on coarse data it is estimated (e.g. uptick/downtick or [[bid-ask-spread|bid-ask]] rules).
2. Signed volume: +size for buys, −size for sells.
3. **Delta** = sum of signed volume in the period.
4. **CVD** = cumulative running sum of delta.

Because step 1 depends on accurate aggressor classification, CVD quality depends on data quality. Tick-accurate feeds on [[sierra-chart]], [[ninjatrader]], quantower, bookmap and crypto perpetual exchanges give clean CVD; reconstructed delta from low-resolution data is approximate.

## Absorption vs initiative

CVD's central use is separating two reasons price might *not* move despite heavy volume:

- **Initiative** — one side is the aggressor and price follows. Rising CVD with rising price = buyers in control, move is "real." This confirms trend.
- **Absorption** — aggressive volume pours in but price stalls because the other side absorbs it with passive limit orders. CVD rises sharply while price refuses to advance → buyers are being absorbed by a resting seller. This is an exhaustion/reversal tell. (See [[absorption]].)

This is exactly the distinction [[volume-profile]] alone cannot make: a thick [[volume-nodes|high-volume node]] could be acceptance (balanced two-sided trade) or absorption (one side defending). CVD plus the [[footprint-chart]] resolves it.

## Price / CVD divergence

The most-watched signal:

| Price | CVD | Read |
|-------|-----|------|
| New high | CVD lower high (flattening/falling) | Bullish exhaustion — buying aggression waning under the rally; reversal risk |
| New low | CVD higher low (flattening/rising) | Bearish exhaustion — selling aggression waning; reversal risk |
| Rising | Rising in step | Healthy uptrend, initiative confirmed |
| Falling | Falling in step | Healthy downtrend, initiative confirmed |

A divergence does not time a reversal by itself; it flags that the move's fuel (aggressive flow) is fading, and is acted on in confluence with a level — a [[value-area-high-and-low|value edge]], a [[point-of-control]], or an [[volume-nodes|HVN]].

## How traders use CVD

- **Confirmation for [[volume-profile-trading-strategy|profile setups]]** — fade an [[volume-nodes|HVN]] only when CVD shows absorption/divergence into it; take a breakout through a [[volume-nodes|LVN]] only when CVD expands with price.
- **Spotting trapped aggressors** — a sharp CVD push that price doesn't reward means aggressive traders are offside and may have to cover, fuelling a reversal.
- **Trend health** — CVD trending with price keeps you in; CVD stalling warns of a turn.
- **Cross-venue / spot-vs-perp** — in crypto, comparing CVD across spot and perpetual venues, or against funding, surfaces who is actually pushing price.

## Worked Example

The following is a qualitative, hypothetical illustration — no real prices are implied.

A market grinds up into a prior session [[point-of-control|POC]] or [[volume-nodes|high-volume node]] that the trader expects to act as resistance. Two scenarios play out:

1. **Absorption / divergence (fade signal).** Price ticks to a marginal **new high**, but the CVD line makes a **lower high** — aggressive buyers are still lifting the offer, yet each push buys less and less upside. Read together with the [[footprint-chart]], the trader sees heavy buy volume printing at the ask while price refuses to extend: a resting seller is *absorbing* the initiative. This is the classic [[absorption]] tell. The trader fades the level (short), placing a stop just beyond the high and targeting the [[value-area-high-and-low|value-area edge]] or POC below, on the thesis that trapped buyers will have to cover.

2. **Initiative confirmed (continuation signal).** Instead, price breaks the high and CVD makes a **higher high in step** — buying aggression is expanding, not fading. No absorption is visible. The trader does *not* fade; the breakout has genuine initiative behind it and is more likely to continue. A short here would be fighting confirmed flow.

The level is identical in both cases; CVD is what tells the trader whether the order flow into it is exhausting or accelerating. Crucially, the divergence in scenario 1 is only acted on **at a level** — CVD divergence in open space is ignored, because it can persist indefinitely.

## Limitations and risks

- **Aggressor classification error** — on poor data the buy/sell split is estimated and CVD can be misleading; quality depends on tick accuracy.
- **Not synchronised across venues** — CVD is per-feed; fragmented liquidity (especially crypto) means one venue's CVD may not represent the whole market.
- **Resets and reference frame** — CVD is a cumulative sum, so the chosen reset point (session, custom) changes its absolute level; only the *shape vs price* is robust.
- **No level, no trade** — CVD is a confirmation tool, not a standalone entry; divergence can persist for a long time before (or without) a reversal.
- **Spoofing / wash distortion** — manipulative flow ([[wash-trading]], [[spoofing]]) can pollute delta, especially on thin instruments.

## Related

- [[order-flow]] — the parent discipline; CVD is its summary directional metric
- [[footprint-chart]] — shows per-price bid/ask volume that CVD aggregates
- [[absorption]] — the passive-side behaviour CVD helps detect
- [[volume]] / [[volume-imbalance]] — raw and signed volume context
- [[volume-profile]] / [[point-of-control]] — *where* volume traded, complemented by CVD's *who*
- [[volume-profile-trading-strategy]] — uses CVD to confirm entries at profile levels

## Sources

- Gap-finder Perplexity deep research, "Volume profile indicator as a trading strategy" (2026-06-19).
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge.
