---
title: "BTC Dominance"
type: concept
created: 2026-06-03
updated: 2026-06-21
status: excellent
tags: [crypto, bitcoin, altcoins, market-regime, market-microstructure]
aliases: ["BTC.D", "Bitcoin Dominance", "BTC Dominance Index"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[bitcoin-cycle-regime]]", "[[macro-trend-regime]]", "[[crypto-market-regime-taxonomy]]", "[[institutional-flow-regime]]", "[[bull-vs-bear-market]]", "[[bitcoin]]", "[[altcoins]]"]
---

# BTC Dominance

**BTC dominance** (ticker **BTC.D**) is [[bitcoin|Bitcoin's]] share of the total crypto market capitalisation — Bitcoin market cap divided by the aggregate market cap of all cryptocurrencies, expressed as a percentage. It is the single most-watched **capital-rotation gauge** in crypto: where dominance is heading tells you whether money is concentrating into Bitcoin or fanning out into [[altcoins]], independent of whether the absolute market is up or down. As of the 2026-06-03 snapshot used by the [[crypto-market-regime-taxonomy|regime taxonomy]], BTC.D was ~59.3%.

## How It Is Computed

```
BTC.D = (BTC price × BTC circulating supply) / (total crypto market cap) × 100%
```

The denominator is the sum of *every* tracked coin's market cap (price × circulating supply), so the figure depends entirely on which assets the data provider includes and whether [[stablecoins]] are counted. Because Bitcoin's supply is essentially fixed and known (~19.9M of a 21M cap as of 2026), short-term moves in BTC.D are driven almost entirely by *relative price* between BTC and everything else, not by supply changes.

Historically BTC.D peaked near **~95%+ in 2017** before the first major altcoin/ICO wave, bottomed around **~36-40% in early 2018** at the height of altcoin mania, and has since oscillated broadly in the **~40-70%** band as cycles rotate between BTC-led and alt-led phases.

### Worked example (qualitative)

Suppose the total crypto market is worth $2T and Bitcoin's market cap is $1.18T. Then BTC.D = 1.18 / 2.0 = **59%** — close to the current snapshot reading. Now consider two different ways the market could move:

- **Alts rally 20%, BTC flat.** Altcoin caps rise from $820B to ~$984B; total cap rises to ~$2.16T; BTC.D *falls* to ~54.6% even though Bitcoin's price did not move. Capital rotated into alts — bullish for [[altcoins]].
- **Risk-off: alts drop 30%, BTC drops 10%.** Total cap falls to ~$1.63T, BTC cap to $1.06T; BTC.D *rises* to ~65% — but the whole market is down. Dominance rose only because alts bled faster than BTC, not because anyone rotated in.

The lesson the example encodes: **BTC.D is a ratio, so it can move with neither asset doing what the number naively implies.** Always read it alongside absolute price.

## Why It Matters

Dominance is a **relative** measure, so it decouples rotation from direction:

- **Rising BTC.D** — capital is concentrating in Bitcoin. This happens both in BTC-led bull runs (BTC leading price discovery while alts lag — see [[bitcoin-cycle-regime|BTC Solo Bull Run]]) *and* in risk-off bleeds (traders rotating out of higher-beta alts into BTC as the relative safe haven). Direction must be read alongside absolute price.
- **Falling BTC.D** — capital is rotating *out* of Bitcoin into alts. When dominance falls through the ~55–60% zone with the broad market rising, it is the classic [[macro-trend-regime|Altcoin Season]] trigger: long ETH/SOL/alts, flat or underweight BTC.
- **Flat BTC.D** — no clear rotation; the trade is in absolute price, not in the BTC-vs-alts pair.

## As a Regime Signal

Dominance is a recurring **detection input** across the regime taxonomy:

- [[macro-trend-regime|Macro Trend]] — falling BTC.D below ~55–60% flags Altcoin Season; rising BTC.D in a downtrend confirms a [[bull-vs-bear-market|bear]] rotation.
- [[bitcoin-cycle-regime|BTC Cycle]] — rising BTC.D while alts stall marks a BTC-solo leg that historically precedes alt rotation by 1–2 weeks.
- [[institutional-flow-regime|Institutional Flow]] — spot-ETF flows are BTC- and ETH-concentrated, structurally supporting dominance and altering the classic alt-rotation pattern.

## The Altseason Pattern

The textbook bull-cycle rotation runs in four legs, and dominance traces each one:

1. **BTC leads** — fresh capital enters via Bitcoin (and, since 2024, spot ETFs). BTC.D rises while alts stagnate.
2. **ETH catches up** — profits rotate into Ethereum; ETH/BTC rises and BTC.D begins to roll over.
3. **Large-cap alts** — SOL, large L1s/L2s outperform; BTC.D falls through the ~55-60% zone.
4. **Altseason proper** — speculation reaches small-caps and memecoins; BTC.D drops fastest. This phase has historically marked late-cycle euphoria and preceded major tops.

This is why a *falling BTC.D in a rising market* is read bullishly for [[altcoins]], while a *falling BTC.D in a falling market* usually just means alts are bleeding faster than BTC — direction matters.

## The Four-Quadrant Read

Because dominance is a ratio, the only correct interpretation pairs **BTC.D direction** with **total market-cap direction**:

| | Total cap rising | Total cap falling |
|---|---|---|
| **BTC.D rising** | BTC-led bull (alts lag); rotation into BTC | Risk-off; alts bleeding faster than BTC ("flight to BTC") |
| **BTC.D falling** | Classic **altseason**; rotate into alts | Late-stage capitulation; alts collapsing, sometimes a stablecoin flight |

The top-left and bottom-right are the actionable extremes: top-left favors alt longs, bottom-right favors cash/stablecoins or BTC over alts.

## How Traders Watch It

- **Threshold breaks.** Many traders treat the ~55–60% zone as a swing line: a sustained break *below* it in a rising market is the canonical [[macro-trend-regime|Altcoin Season]] cue; a reclaim *above* it signals capital retreating to [[bitcoin|BTC]].
- **Pair with ETH/BTC and OTHERS.D.** ETH/BTC is the leading-edge rotation gauge (alts usually follow ETH); the OTHERS.D index (total cap excluding the top 10) isolates small-cap speculation, which leads only in late-cycle euphoria.
- **Confirm, don't predict.** Dominance is a *confirmation* tool. Traders combine it with absolute trend structure, funding rates, and on-chain flows before sizing an alt-rotation trade.
- **Current snapshot context.** At ~59% (qualitatively, an Established Bear Market backdrop with crypto Fear & Greed near 23), dominance is *elevated* — capital is concentrated defensively in BTC, the opposite of an altseason setup.

## Caveats

- **Stablecoins distort it.** Most dominance charts include [[stablecoins]] (USDT, USDC) in the total cap denominator, so a flight to stablecoins mechanically *lowers* BTC.D even when nothing rotated into alts. With stablecoins now a large slice of total cap, this distortion is material — some traders prefer a stablecoin-excluded dominance (sometimes charted as "BTC.D excluding stables") or watch the ETH/BTC and OTHERS.D (total-cap-excluding-top-10) indices directly.
- **New-supply dilution.** Large new token launches and unlocks inflate total cap, nudging dominance down without genuine rotation.
- **Provider dependence.** Different aggregators track different coin universes, so BTC.D differs slightly across CoinMarketCap, CoinGecko, and TradingView.
- **Not a price forecast.** Dominance tells you *where* capital is rotating, not whether the market is going up or down — it must be paired with absolute price structure and [[macro-trend-regime|trend regime]].

## Related

- [[bitcoin-cycle-regime]] — dominance rotation as a BTC-cycle state
- [[macro-trend-regime]] — Altcoin Season trigger
- [[crypto-market-regime-taxonomy]] — the 14-basket regime hub
- [[institutional-flow-regime]] — how ETF flows reshape dominance
- [[bull-vs-bear-market]] — dominance behaviour across the cycle

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — uses BTC dominance (59.3% at snapshot) as a core regime input
