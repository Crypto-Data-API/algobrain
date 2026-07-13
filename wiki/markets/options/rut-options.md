---
title: "RUT Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, stocks, indicators]
aliases: ["RUT Options", "Russell 2000 Options"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[ndx-options]]", "[[vix]]", "[[vix-options]]", "[[iwm-options]]", "[[russell-2000]]", "[[section-1256-contracts]]", "[[am-vs-pm-settlement]]", "[[soq-settlement]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[options-greeks]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[dispersion-trading]]", "[[short-strangle]]", "[[iron-condor]]", "[[size-factor]]", "[[small-cap-premium]]"]
---

RUT options are Cboe-listed, cash-settled, European-style index options on the [[russell-2000|Russell 2000 Index]] — the 2000 smallest US-listed companies by market capitalization, the canonical small-cap benchmark. They carry a $100 contract multiplier, qualify as [[section-1256-contracts|Section 1256 contracts]] under US tax law, and are the standard vehicle for expressing small-cap-specific volatility, factor exposure, and dispersion against [[spx-options|SPX]] or [[ndx-options|NDX]].

## Overview

The Russell 2000 has structurally different return and volatility characteristics from large-cap indices: higher realized volatility, deeper drawdowns in risk-off episodes, sharper rebounds in risk-on rallies, and a meaningfully different sector composition (heavier in regional banks, biotech, and small industrials; lighter in mega-cap tech). RUT implied vol is typically **3-6 vol points above SPX** and skew is steeper on the put side, reflecting the genuinely larger tail risk of small-cap names with weaker balance sheets and lower liquidity buffers.

RUT options exist alongside [[iwm-options|IWM options]] (on the iShares Russell 2000 ETF), with the same institutional/retail split that distinguishes [[spx-options|SPX]] from [[spy-options|SPY]] and [[ndx-options|NDX]] from [[qqq-options|QQQ]]:

- **RUT**: index, cash-settled, European-style, Section 1256 — the institutional product.
- **IWM**: ETF, physical-settled, American-style, standard equity tax — the retail-friendly product with penny ticks and ~1/10 the notional.

## Contract Mechanics

| Spec | Value |
|---|---|
| Underlying | Russell 2000 Index (RUT) |
| Multiplier | $100 |
| Exercise style | European |
| Settlement | Cash |
| Strike intervals | $5 standard; $1 near-the-money on some weeklies |
| Tick size | $0.05 below $3.00 premium; $0.10 above |
| Trading hours | 9:30 am – 4:15 pm ET regular session; some Cboe extended-hours trading |
| Symbols | RUT (AM-settled monthlies), RUTW (PM-settled weeklies and dailies) |
| Tax treatment | [[section-1256-contracts|Section 1256]] (60/40) |
| Listed | Cboe Options Exchange |

At a Russell 2000 index level near 2,000, a single RUT contract represents approximately **$200,000 of notional** — about 4x an IWM contract and 0.4x an SPX contract, sitting between the two in size.

## RUT vs Sibling Index Options

RUT sits within the cash-settled US index-options franchise. Against its siblings, RUT is the small-cap, higher-vol, lower-liquidity member:

| Dimension | RUT | [[spx-options\|SPX]] | [[ndx-options\|NDX]] | [[xsp-options\|XSP]] | IWM (ETF) |
|---|---|---|---|---|---|
| Underlying | Russell 2000 | S&P 500 | Nasdaq-100 | 1/10 S&P 500 | Russell 2000 ETF |
| Components | 2000 small-caps | 500 large-caps | 100 large-cap tech | 500 large-caps | 2000 small-caps |
| Notional / contract | ~$200K | ~$500K | ~$500K+ | ~$50K | ~$50K |
| Exercise | European | European | European | European | American |
| Settlement | Cash | Cash | Cash | Cash | Physical |
| Tax | [[section-1256-contracts\|§1256]] 60/40 | §1256 60/40 | §1256 60/40 | §1256 60/40 | Standard equity |
| Early assignment | None | None | None | None | Yes |
| Typical IV vs SPX | +3-6 vol pts | baseline | usually higher | = SPX | tracks RUT |
| Put skew | Steepest of the four | Steep | Steep | = SPX | tracks RUT |
| Liquidity | Lowest of index four | Highest | Deep | Growing | Penny-quoted, deep |
| Vol index | RVX | [[vix\|VIX]] | VXN | VIX | RVX |

The core selection logic: trade **RUT** when you want clean small-cap exposure with Section 1256 tax and no early-assignment risk and can tolerate wide spreads; trade **IWM** when you want penny pricing and smaller notional and don't mind standard equity tax and American-style assignment.

## Settlement

The familiar AM/PM split applies:

- **AM settlement (RUT monthlies)** — settles to the **Special Opening Quotation (SOQ)** of the Russell 2000 on the third Friday, calculated from opening prints of all 2000 component stocks. Final trading is the prior afternoon. The SOQ on a 2000-stock basket can drift materially from Thursday's close because many small-caps open with delays or open auctions, and the index reconstitution effect can amplify SOQ idiosyncrasies.
- **PM settlement (RUTW)** — settles to the official 4:00 pm ET closing print of the index. Trading continues until 4:00 pm on expiration day.

See [[am-vs-pm-settlement]] and [[soq-settlement]]. The Russell 2000 SOQ is among the most idiosyncratic of the major US indices because of the sheer number of components and the high incidence of opening delays in the smallest names.

## Liquidity & Spreads

RUT is the **least liquid of the four major US index options** (SPX, NDX, RUT, XSP), and the gap to SPX is roughly two orders of magnitude:

- **Volume** — typically **20,000-40,000 contracts/day**, vs SPX's 2-4 million. RUTW dailies have grown the franchise since 2024 but the base remains modest.
- **Bid/ask** — **$0.10-$0.50** at near-the-money strikes; **$1-$3+ wide** on far-OTM wings. Penny-equivalent quoting is rare even on the front month.
- **Strike density** — $5 standard intervals; weeklies offer some $1 increments near-the-money but coverage is patchy.
- **Quote sizes** — usually 5-30 contracts at the inside; meaningful size has to be worked into the market.
- **Far-OTM tails** — thin, with infrequent quote refreshes during stress. RUT crash puts can trade $5+ wide in vol spikes.

The practical implication: RUT execution discipline matters. Limit orders, patience, and sometimes splitting a position across multiple expirations or moneyness levels are required to fill at edge. Market orders on RUT — especially on wings — are routinely punished.

## Greeks Behavior

RUT's [[options-greeks|Greeks]] behave like SPX's qualitatively, but the higher-vol, steeper-skew small-cap regime shifts the magnitudes:

- **[[delta]]** — standard index delta; one full-delta RUT contract carries ~$200K of directional notional, so position-level delta dollars accumulate quickly. Beta-weighting RUT delta back to SPX overstates risk if you forget RUT's ~1.2-1.4x beta to the broad market.
- **[[gamma]]** — meaningful, and *more punishing than SPX* on a like-for-like basis because realized moves are larger. Short-gamma RUT positions (condors, strangles) require wider stops and more frequent adjustment than the SPX analog; the small-cap index can gap on a banking or biotech headline.
- **[[theta]]** — the premium-seller's engine. RUT's higher IV means richer absolute premium per unit of notional, so theta-per-dollar-at-risk is attractive — but it is compensation for the fatter realized-vol tail, not free.
- **[[vega]]** — RUT vega is "expensive" in the sense that RUT IV is both higher and more volatile than SPX IV (the RVX index is more jumpy than VIX). Long-vega RUT positions can pay off violently in credit-stress episodes; short-vega positions carry correspondingly larger vol-spike risk.
- **Skew dynamics** — the steeper put skew (see [[volatility-skew]]) means downside puts are richer relative to upside calls than on SPX, which shapes the economics of put spreads, risk reversals, and any skew-sensitive structure.

## Common Spread Structures

Because RUT shares SPX's European/cash mechanics, the same defined-risk structures apply — but RUT's wider spreads favor *fewer legs* and disciplined limit execution:

- **[[iron-condor|Iron condors]]** — sell an OTM put spread and an OTM call spread to harvest the small-cap [[variance-risk-premium]] within a range. RUT condors collect more premium than SPX condors but face fatter tails; wing width and management discipline matter more.
- **[[short-strangle|Short strangles]]** — sell an OTM put and OTM call (undefined risk). The richest theta-per-margin on RUT, but the most exposed to a small-cap gap; typically run smaller than the SPX equivalent.
- **[[bull-put-spread|Put credit spreads]]** — sell a higher put, buy a lower put; a directional/neutral premium structure that caps the tail, well-suited to RUT's steep put skew (you sell the rich downside).
- **[[risk-reversal|Risk reversals]]** — sell a put, buy a call (or vice versa) to express directional views while monetizing skew; the steep RUT skew makes the financing leg cheaper for bullish risk reversals.
- **Calendar / diagonal spreads** ([[calendar-spread]], [[diagonal-spread]]) — term-structure trades; viable on RUT but constrained by patchier far-month strike density and wider quotes.
- **Vertical spreads** ([[vertical-spread]]) — preferred over naked legs whenever possible because the defined risk caps the cost of RUT's fat-tail events.

Two-legged and four-legged defined-risk structures dominate practical RUT trading; the wider quoted markets make complex many-legged structures expensive to enter and exit.

## Typical Strategies / Use Cases

### Small-cap-specific volatility expression

RUT is the cleanest single-instrument vehicle for expressing a view on small-cap volatility, small-cap drawdown risk, or small-cap rebound. The realized-vol differential vs SPX (typically 3-6 vol points) reflects the genuinely different risk character of small-caps and their sensitivity to credit conditions, regional banking, and economic-cycle inflection.

### Factor / size-premium hedging

For factor portfolios with explicit size-premium exposure (long small-caps, short large-caps, or long-only smid-cap books), RUT puts hedge the small-cap leg directly. The Section 1256 tax treatment improves hedge cost vs equivalent IWM hedges.

### Large-vs-small dispersion

The **SPX-vs-RUT** (or **NDX-vs-RUT**) dispersion trade expresses a view on whether large-caps or small-caps will dominate the volatility regime. In credit-sensitive risk-off episodes, RUT vol explodes faster than SPX vol; in tech-led broad-market rallies, RUT can lag and RUT vol compress while SPX vol stays flat. The implied-correlation gap between large-cap and small-cap baskets is a long-running source of dispersion edge. See [[dispersion-trading]].

### Premium selling on small-cap vol

RUT [[short-strangle|strangles]] and [[iron-condor|iron condors]] capture the small-cap [[variance-risk-premium]], which empirically runs larger than SPX's in vol points but with proportionally larger drawdowns. The trade-off vs SPX: lower liquidity, wider spreads, fatter realized-vol tails — meaning the per-trade edge is bigger but the volatility of P&L is also bigger.

### Macro regime-shift expression

Russell 2000 is highly sensitive to small-bank credit conditions, the regional-banking cycle, and the broader economic cycle. Long RUT puts are a recurring tail-hedge in macro books that anticipate credit stress (a strategy that paid in March 2020, March 2023 SVB, and other regional-bank episodes).

## Risks / Quirks

- **Lower liquidity than SPX or NDX** — wider spreads and thinner quote sizes mean operational slippage is structurally higher. Hedge unwinds on stress days can be expensive.
- **AM-settle gap on monthlies** — the 2000-component SOQ is more SOQ-idiosyncratic than SPX's 500-component or NDX's 100-component SOQ, with greater Thursday-night-to-Friday-morning gap risk.
- **Russell index reconstitution** — the annual June reconstitution rebalances the entire Russell 2000 index, generating index-fund flows that can move RUT in non-fundamental ways. Options pricing around June reconstitution carries a regime-specific risk.
- **Higher vol regime** — a "normal" RUT environment has higher realized vol than a "normal" SPX environment; strategy P&L and drawdown profiles do not transfer directly from SPX backtests.
- **Steeper put skew** — protective puts on RUT cost more in vol points than on SPX even before notional adjustment.
- **Sector concentration in regional banks and biotech** — these sub-sectors can drive RUT independently of broad-market direction; an SVB-style banking shock or a major biotech FDA event can move RUT 1-2% on a session SPX barely noticed.
- **Capacity constraints** — the lower volume means very large positions face real liquidity constraints; institutional RUT books frequently use smaller sizes than they would in SPX.

## Tax Treatment

RUT options are **broad-based stock index options** under IRC §1256, qualifying for [[section-1256-contracts|Section 1256]] treatment:

- **60/40 blended** — every realized gain or loss is split 60% long-term / 40% short-term regardless of holding period.
- **Mark-to-market on December 31** — open positions are deemed-closed at year-end FMV, with results reported on Form 6781.
- **3-year loss carryback** against prior Section 1256 gains.
- **No standard §1091 wash-sale concerns** in the equity sense.

The 60/40 blended rate (~26.8% federal vs ~37% short-term) creates the same structural after-tax edge over IWM that SPX has over SPY. For active premium-sellers on small-caps, this can be the single most important reason to absorb RUT's wider quoted spreads rather than trade IWM.

See [[section-1256-contracts]] for full mechanics.

## Related

- [[index-options]] — overview of the index-options franchise
- [[options]] — options fundamentals
- [[spx-options]] — large-cap broad-market sibling
- [[ndx-options]] — large-cap tech-concentrated sibling
- [[xsp-options]] — mini-SPX, same Section 1256 treatment
- [[iwm-options]] — physically-settled ETF cousin
- [[vix]] — the S&P 500 volatility index (RUT's analog is RVX)
- [[russell-2000]] — the underlying index
- [[size-factor]], [[small-cap-premium]] — factor context
- [[section-1256-contracts]] — tax framework
- [[am-vs-pm-settlement]] — settlement regime split
- [[soq-settlement]] — SOQ calculation methodology
- [[cash-vs-physical-settlement]]
- [[american-vs-european-options]]
- [[volatility-skew]] — RUT skew is among the steepest of US index options
- [[dispersion-trading]] — SPX-vs-RUT and NDX-vs-RUT pairs
- [[options-greeks]], [[implied-volatility]]
- [[short-strangle]], [[iron-condor]], [[bull-put-spread]], [[vertical-spread]], [[risk-reversal]], [[calendar-spread]], [[diagonal-spread]]
- [[variance-risk-premium]] — the premium small-cap sellers harvest
- [[delta]], [[gamma]], [[theta]], [[vega]] — Greeks behavior on RUT

## Sources

- Cboe RUT product specifications (cboe.com/tradable_products/sp_500/rut_options) — multiplier, settlement, expirations.
- Cboe Special Opening Quotation methodology documentation.
- FTSE Russell — Russell 2000 Index methodology and reconstitution rules.
- IRC Section 1256 — broad-based index option qualification.
- IRS Publication 550 — Section 1256 mechanics.
