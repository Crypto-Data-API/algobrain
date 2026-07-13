---
title: "Gamma Exposure (GEX)"
type: concept
created: 2026-06-27
updated: 2026-07-13
status: good
tags: [options, derivatives, volatility, market-microstructure, indicators]
aliases: ["GEX", "Gamma Exposure", "Dealer Gamma Exposure", "Net Dealer Gamma", "Gamma Flip", "Volatility Trigger"]
related: ["[[dealer-gamma-hedging]]", "[[options-pinning]]", "[[gamma-squeeze]]", "[[max-pain]]", "[[delta]]", "[[gamma]]", "[[vanna]]", "[[charm]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility]]", "[[options-greeks]]", "[[0dte-impact-on-spx]]", "[[vix]]", "[[short-squeeze]]", "[[cryptodataapi]]"]
domain: [market-microstructure, derivatives]
prerequisites: ["[[delta]]", "[[gamma]]", "[[dealer-gamma-hedging]]"]
difficulty: intermediate
---

**Gamma exposure (GEX)** is a single market-wide number that estimates *how much of the underlying options dealers must trade to stay hedged per unit move in price* — and, critically, in which direction. It answers one question about the index or a single stock: are options market-makers, in aggregate, positioned to **dampen** moves (a calm, mean-reverting tape) or to **amplify** them (a trending, jumpy tape)? GEX is the aggregate reading; the per-trade hedging machinery that produces it is covered in depth on **[[dealer-gamma-hedging]]**, and this page focuses on the *metric itself* — its formula, the two regimes, the gamma-flip line, and how equity traders read it.

## Building Blocks — Delta and Gamma

- **[[delta]]** is an option's *speed*: how much its value changes per $1 move in the underlying.
- **[[gamma]]** is its *acceleration*: how fast that delta itself changes as the underlying moves — the convexity term.
- **Long gamma** = you *own* options; **short gamma** = you *sold* options. Long/short here denotes the side of the trade, not a directional bet: gamma affects up-moves and down-moves symmetrically.

To stay directionally neutral a dealer **[[delta-hedging|delta-hedges]]** by trading the underlying, and must **re-hedge continuously** because gamma makes delta drift as price moves. The *sign* of the dealer's net gamma decides whether that forced re-hedging fights the move or feeds it.

## The Two Regimes

| Dealer's net position | They hedge by trading the underlying… | Effect on price | Realized-vol effect |
|---|---|---|---|
| **Long gamma** (net bought options) | *against* the move — sell rallies, buy dips | **dampens / pins** (stabilizing) | compresses |
| **Short gamma** (net sold options) | *with* the move — buy rallies, sell dips | **amplifies** (squeeze / crash) | expands |

Two points traders routinely get wrong:

1. **Dealers do not choose their gamma sign — customer order flow imposes it.** The dealer is the residual counterparty. If the public net *buys* options, dealers end up short gamma; if the public net *sells* options (covered calls, put-writing), dealers end up long gamma.
2. **Whether a dealer holds or is short the stock does not decide calm-vs-wild — only the gamma sign does.** A dealer who *sold a call* holds stock as a hedge yet is short gamma (amplifying). The stock-hedge direction only reflects call-vs-put, not the vol regime.

## The GEX Number

GEX sums each strike's gamma across the whole options chain, weighted by open interest, into one dollar figure. A common per-strike formulation:

```
GEX_strike = gamma × open_interest × contract_multiplier (100) × spot² × 0.01

Aggregate GEX = Σ over strikes:
  + GEX_strike for calls      (standard assumption: dealers are long calls)
  − GEX_strike for puts       (standard assumption: dealers are short puts)
```

- **Positive GEX** (dealers net long gamma) → vol-suppressing, mean-reverting — "shock absorbers ON."
- **Negative GEX** (dealers net short gamma) → vol-expanding, trend-amplifying — "absorbers OFF, accelerator ON."

GEX says nothing about *direction* (up vs down) — only about *how bumpy the ride will be*. The dramatic "small spark → outsized sell-off" sessions are almost always negative-GEX days.

> **Convention matters.** The sign of each leg depends on an assumption about which side dealers are on. The dominant retail convention (SqueezeMetrics/SpotGamma) assumes dealers are **long calls, short puts** — the natural counterparty to a customer base that buys downside puts for protection and overwrites calls for yield. This is reasonable in normal regimes but *inverts* in stress (retail panic-buying calls or puts) and is unreliable for single names. Always check a provider's stated convention before trading its number.

## The Gamma Flip Line

The **gamma flip** — SpotGamma's "**volatility trigger**" — is the spot price at which aggregate dealer gamma crosses from positive to negative. It is computed by recalculating aggregate GEX at a range of *hypothetical* spot prices and finding where the sum crosses **zero**. It is published daily by analytics shops (SpotGamma, Tier1Alpha, MenthorQ, SqueezeMetrics).

| Spot vs flip | Regime | How to trade it |
|---|---|---|
| **Above** the flip | long gamma | calm, mean-reverting → fade extremes, sell premium |
| **Below** the flip | short gamma | wild, trending → moves follow through, buy vol / avoid fading |
| **On** the line | transitional | jumpiest — small moves trigger large hedging swings |

The flip acts as a *behavioral* support/resistance: defended from above by dealer long-gamma buying, and reinforced on the way down by new short-gamma selling. **Caveats:** it is an *estimate* built on a positioning *assumption*; providers compute it differently (differences of 1–2% are common, so treat it as a zone); and the surge of **[[0dte-impact-on-spx|0DTE]]** flow since 2022 has smeared gamma across the strike grid, weakening the once-clean single line.

## Call Walls, Put Walls, and Pinning

Per-strike GEX is what makes the aggregate actionable:

- **Call wall** — the strike with the largest positive gamma (biggest call OI). In a positive-GEX regime it acts as a **magnet and ceiling**: dealer selling into rallies caps advances there.
- **Put wall** — the strike with the largest negative gamma below spot; often a support shelf, but if breached it *flips* the regime toward negative GEX and accelerates the decline.
- **Pinning** — in a deeply positive-GEX, high-OI environment (classically monthly **OPEX** weeks), dealer hedging drags spot toward the highest-open-interest strike and holds it there, the effect described on **[[options-pinning]]** and proxied by **[[max-pain]]**.

## Historical Episodes

- **Volmageddon (Feb 5, 2018).** The collapse of short-volatility products (XIV) forced dealers deeply short gamma; the negative-GEX feedback loop turned a moderate decline into a ~4% single-day S&P drop and a VIX spike from ~17 to ~37.
- **GameStop gamma squeeze (Jan 2021).** Retail call-buying flipped dealers short gamma in a single name; forced dealer buying to hedge the rising calls compounded the **[[short-squeeze]]**, a textbook **[[gamma-squeeze]]**.
- **August 5, 2024 VIX spike.** A negative-GEX, thin-liquidity morning saw the VIX briefly print above 60 as short-gamma and short-vol positioning unwound — the same amplifier mechanism.

## Vanna and Charm (Secondary Flows)

Beyond gamma, two other Greeks drive predictable dealer re-hedging:

- **[[vanna]]** (delta's sensitivity to implied vol) — as **[[implied-volatility]]** falls after a catalyst (the "vol crush"), vanna flows are often systematically *supportive*, a reason indices drift higher in the days after FOMC even on neutral news.
- **[[charm]]** (delta's decay with time) — strongest in the final hours of OPEX Fridays and the last week before monthly expiration, biasing spot toward high-OI strikes.

Both are detailed on **[[dealer-gamma-hedging]]**.

## How to Read GEX Sensibly

1. Mark the **gamma flip** each morning; it sets the day's regime bias (fade vs follow).
2. Note the nearest **call wall / put wall** as candidate resistance/support and pin targets.
3. In **positive GEX**, favor mean-reversion and premium-selling; in **negative GEX**, favor momentum, defined-risk long-vol, and *smaller* size (realized vol runs 2–3× normal on bad days).
4. Treat GEX as a **probabilistic regime classifier**, never a stand-alone entry trigger.

## Limitations

- **Estimated, not observed.** Public GEX is inferred from *listed* open interest; large OTC, FLEX, and structured-product books are invisible, so the true dealer sign can differ from the published one.
- **Positioning assumption.** The "long calls / short puts" convention breaks in call-buying frenzies and put panics, and is far weaker for single names than for indices.
- **Exogenous flows override it.** Vol-control funds, risk-parity rebalancing, CTA trend flow, and corporate buybacks can dominate the tape regardless of GEX.
- **0DTE distortion.** Daily expirations reset the gamma profile each session and have degraded the clean monthly-OPEX patterns since 2022.
- **Reflexivity.** As GEX-based trading went mainstream post-2020, the cleanest pin-and-release patterns weakened.

## Data Providers

SpotGamma (retail standard; HIRO real-time hedging oscillator), Tier1Alpha (institutional-grade modeling), MenthorQ (TradingView-native), SqueezeMetrics (free GEX and the DIX dark-pool indicator), and Unusual Whales (GammaLab). A custom calculator is feasible from an OPRA/CBOE open-interest feed plus a Black-Scholes greeks engine — see the methodology on **[[dealer-gamma-hedging]]**.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/quant/gex` — gamma exposure: MM inventory + liquidation profile (per-coin optional)
- `GET /api/v1/quant/positioning` — trader-type split (market maker / whale / other)

**Historical data:**
- `GET /api/v1/quant/history` — point-in-time quant records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[dealer-gamma-hedging]] — the per-trade hedging mechanism GEX aggregates (deep dive: regimes, walls, vanna/charm, OPEX, tools)
- [[options-pinning]] — the long-gamma pinning effect; [[max-pain]] — the popular pin-target proxy
- [[gamma-squeeze]] — the single-name short-call-gamma feedback loop
- [[0dte-impact-on-spx]] — how daily expirations reshaped the gamma profile
- [[delta]], [[gamma]], [[vanna]], [[charm]], [[options-greeks]] — the Greeks underneath
- [[implied-volatility]], [[realized-volatility]], [[volatility]], [[vix]] — what GEX regimes translate into
- [[short-squeeze]] — the price-action GEX can amplify on the upside

## Sources

- Synthesized from the wiki's options-microstructure cluster: [[dealer-gamma-hedging]], [[options-pinning]], [[max-pain]], [[gamma-squeeze]].
- Public GEX methodology from SqueezeMetrics (aggregate GEX white paper) and SpotGamma educational materials (gamma flip / "volatility trigger", call/put walls).
- Underlying literature (via those pages): Natenberg, *Option Volatility and Pricing*; Harris, *Trading and Exchanges*; Cboe research on 0DTE impact on dealer gamma.
