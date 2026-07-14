---
title: "Dealer Gamma Hedging"
type: concept
created: 2026-05-05
updated: 2026-07-13
status: good
tags: [options, market-microstructure, market-makers, gamma, indicators]
aliases: ["Dealer Hedging", "Market Maker Gamma Hedging", "Gamma Hedging Flows", "GEX"]
related: ["[[gamma-exposure-trading]]", "[[gamma-scalping]]", "[[options-greeks]]", "[[volatility-regime-classification]]", "[[options-stress-testing]]", "[[max-pain]]", "[[vix-august-2024-spike]]", "[[cryptodataapi]]"]
domain: [market-microstructure, options]
prerequisites: ["[[options-greeks]]", "[[gamma]]"]
difficulty: advanced
---

Dealer gamma hedging is the mechanical, non-discretionary process by which options [[market-makers|market makers]] buy and sell the underlying asset to keep their inventory [[delta]]-neutral as spot moves. Because dealers are the residual counterparty to most options trades and because their hedging is rule-based rather than view-driven, their flows are often the second-order mover of intraday equity prices -- frequently more important than fundamentals, news, or [[technical-analysis]] for explaining why SPX grinds sideways one day and trends violently the next. Understanding which side of [[gamma]] dealers are on is one of the few structural edges still available to discretionary traders, and it is foundational to professional discretionary trade construction.

## Overview

Options dealers do not take directional bets. They quote two-sided markets, capture the [[bid-ask-spread]], and immediately neutralize the risk of every position they accumulate. The first-order risk is [[delta]] -- the change in option value per dollar move in the underlying. Dealers hedge delta by trading the underlying (or a correlated futures contract). The second-order risk is [[gamma]] -- the change in delta per dollar move. Gamma is the reason dealers cannot hedge once and walk away: as spot moves, delta drifts, and dealers must continuously re-hedge.

The direction of that re-hedging depends on the *sign* of the dealer's net gamma:

- **Long gamma (dealers stabilize):** dealers sell into rallies and buy into dips -- a [[mean-reversion|mean-reverting]], vol-suppressing flow
- **Short gamma (dealers amplify):** dealers buy into rallies and sell into dips -- a trend-amplifying, vol-expanding flow

The aggregate sign of dealer gamma is published daily by analytics shops including spotgamma, [[tier1alpha]], and [[menthorq]]. The price at which it flips sign -- the **gamma flip level** -- is one of the most important intraday levels in the index complex.

## The Mechanics

Consider the simplest possible flow: a retail trader buys an SPX put.

1. **Trade prints.** Retail is long the put. The dealer is short the put
2. **Dealer's delta exposure.** A short put has *positive* delta (if SPX rises, a short put gains value). To remain delta-neutral, the dealer is implicitly short SPX -- so they must **buy SPX futures** to neutralize
3. **Spot moves up.** As SPX rises, the put moves further [[out-of-the-money]]. Its delta moves toward zero. The short-put delta the dealer is hedging shrinks
4. **Dealer re-hedges.** The dealer no longer needs the full SPX hedge -- they **sell some SPX** back
5. **Spot moves down.** Put goes [[in-the-money]]. Short-put delta grows (more positive). Dealer must **buy more SPX**

Notice the pattern: when dealers are short puts (long gamma from the put side), they sell into rallies and buy into dips. The hedging flow is mean-reverting.

The opposite holds for short calls: dealers who sold calls are short gamma from the call side, and as spot rises through the strike they must keep buying SPX to chase the growing positive delta they need to offload. That flow amplifies the move.

The aggregate book contains thousands of strikes across SPX, [[etf-options|SPY]], XSP, and now massive [[zero-dte|0DTE]] flow. Whether dealers are net long or net short gamma depends on the *strike distribution* of all open interest, weighted by gamma per contract and current spot proximity. The number is recomputed continuously as spot moves and as new trades print.

> **Convention:** Most public GEX models assume dealers are *short calls* and *long puts* -- i.e., the natural counterparty to a customer base that buys puts for protection and sells calls for yield ([[covered-call|covered calls]], [[buy-write|buy-writes]]). This assumption is reasonable in normal regimes but breaks down in stress (when retail panic-buys calls) and in single names (where flow can run either direction).

## Long-Gamma Dealer Regime

When net dealer gamma is positive ("long gamma"), dealers are mechanically forced to fade every move:

- **Spot rallies** -> dealer's hedge book becomes too long -> dealer **sells** into the rally
- **Spot dips** -> hedge book becomes too short -> dealer **buys** the dip

The market behaves like it is being held in place by a giant rubber band. Realized [[volatility]] compresses. Intraday ranges narrow. [[breakout-trading|Breakouts]] fail. The [[vix]] grinds lower regardless of headlines. These are the "boring grind" days that frustrate momentum traders and reward [[options-premium-selling|premium sellers]].

Conditions that typically produce a long-gamma regime (rules of thumb -- specific GEX thresholds vary by model and market):

- SPX has rallied through a large [[call-wall|call wall]] (the strike with the largest call OI) -- dealers who sold those calls now need to keep selling stock as gamma builds
- Retail and overwriters have sold large quantities of upside calls (yield-enhancement [[etfs]] like JEPI, QYLD, XYLD have grown enormously since 2020)
- After a sustained rally with low realized vol, dealers' net call gamma exceeds put gamma in absolute terms
- Post-FOMC, post-CPI, or post-OPEX rallies that "release the [[vol-crush|vol crush]]" and leave the book deeply long gamma

Discretionary desks use this regime to size *up* short premium ([[iron-condor|iron condors]], [[strangle|short strangles]]) and to fade intraday extremes with tight stops. The key insight: in a long-gamma regime, the path of least resistance is *back to the middle*, not in the direction of the latest move.

## Short-Gamma Dealer Regime

When net dealer gamma flips negative ("short gamma"), the hedging flow inverts:

- **Spot rallies** -> dealer's hedge book becomes too short -> dealer **buys** into the rally
- **Spot dips** -> hedge book becomes too long -> dealer **sells** into the dip

Dealers become forced trend-followers. Realized vol expands. Intraday ranges widen. [[breakout-trading|Breakouts]] follow through. The [[vix]] spikes faster than the actual fundamental news warrants. These are the "vol expansion" days that reward [[trend-following]] and crush short premium.

Conditions that typically produce a short-gamma regime:

- Spot has fallen below a large [[put-wall|put wall]] -- dealers who sold those puts are now short delta and must keep selling on every bounce
- A fast move down has pushed spot through the gamma flip level (no rally needed -- gravity does the work)
- Retail surge in put-buying for protection (peri-FOMC, geopolitical shocks) increases dealer short-put inventory
- [[volmageddon|Volmageddon]]-style structured product unwinds (Feb 2018) -- short-vol products forced dealers into massive short-gamma exposure
- [[meme-stocks|Meme stocks]] / single-name [[gamma-squeeze|gamma squeezes]] (GME 2021, NVDA 2024) where call-buying rather than put-buying dominates

The key insight: in a short-gamma regime, fading moves is mathematically fighting the market's largest forced buyer/seller. Dips get bought by retail and sold by dealers; the dealer side is bigger.

## The Gamma Flip Level

The **gamma flip** (sometimes called the "volatility trigger" -- spotgamma's term) is the spot price at which aggregate dealer gamma changes sign from positive to negative. It is computed daily by aggregating gamma exposure across the entire options chain at a hypothetical spot price and finding where the sum crosses zero.

Practical use:

- **Spot above the flip:** market is in long-gamma mode. Trade [[mean-reversion]]. Sell premium. Fade extremes
- **Spot below the flip:** market is in short-gamma mode. Trade [[momentum]]. Buy options. Avoid fading
- **Spot oscillating around the flip:** transitional regime -- often the highest-vol environment as small moves can trigger large hedging swings

The flip level acts like a *behavioral* support/resistance:

- When approached from above, dealers' long-gamma buying tends to defend it (acts like support)
- When breached to the downside, dealers' new short-gamma selling tends to reinforce the breakdown (acts like resistance on bounces)

This is one of the most-watched levels by discretionary desks. Many traders mark the flip level on their charts each morning and use it for sizing decisions, [[stop-loss|stop placement]], and [[target-setting|targets]].

> **Caveat:** The exact flip level varies between providers because each models the dealer book differently. Differences of 1-2% across spotgamma, [[tier1alpha]], and [[menthorq]] are common. Use the level as a *zone*, not a single price.

## GEX (Gamma Exposure)

**Gamma Exposure (GEX)** is the dollar measure of how much underlying dealers must trade per 1% move in spot. The standard formula:

```
GEX_strike = gamma * open_interest * contract_multiplier * spot^2 / 100

Aggregate GEX = sum across all strikes of:
  +GEX_strike for calls (assuming dealers are short calls)
  -GEX_strike for puts (assuming dealers are long puts)
```

Some models use the inverse sign convention -- always check the provider's definition before trading on the number.

Interpretation (rules of thumb -- thresholds are model-specific):

| GEX level (SPX) | Regime | Behavior |
|---|---|---|
| Above ~$5B positive | Deeply long gamma | Pinned, very low realized vol, narrow ranges |
| ~$0 to $5B positive | Mildly long gamma | Mean-reverting bias, but can break with news |
| Around zero | Flip zone | Highest sensitivity -- small moves trigger large hedging |
| Negative | Short gamma | Trending, vol-expansive, [[breakout-trading|breakouts]] follow through |
| Below ~-$2B | Deeply short gamma | Crash/melt-up risk; daily ranges 2-3x normal |

These thresholds are nominal -- they have drifted with the explosion of [[zero-dte|0DTE]] volume and overall options market growth. Always reference the provider's *historical distribution* of GEX rather than a fixed number.

Aggregate GEX is published daily by spotgamma, [[squeezemetrics]], [[tier1alpha]], [[menthorq]], and Unusual Whales (via GammaLab). Per-strike GEX is what matters for identifying [[call-wall|call walls]], [[put-wall|put walls]], and the gamma flip itself.

## Vanna and Charm Flows

Beyond gamma, two other [[options-greeks|Greeks]] drive predictable hedging flows:

### Vanna (dDelta / dVol)

[[vanna|Vanna]] measures how delta changes with [[implied-volatility]]. When IV moves, dealers must re-hedge even if spot does not move.

- **Falling IV** (vol crush after a catalyst, FOMC dove pivot, calm post-OPEX week): puts dealers are long become less negative-delta -> dealers' hedge becomes too long -> they **sell** stock to re-hedge. But for dealers who are short calls, falling IV makes those calls less positive-delta -> dealers' hedge becomes too short -> they **buy** stock. The net flow is regime-dependent
- **Rising IV** (panic, surprise headline): the inverse

In typical post-event vol-crush conditions, **vanna flows are systematically supportive** -- a major reason markets often grind higher in the days after FOMC even when the news was neutral. This is the "vanna tailwind" effect.

### Charm (dDelta / dTime)

[[charm|Charm]] measures how delta decays as time passes. Out-of-the-money options bleed delta toward zero as expiry approaches; in-the-money options' delta drifts toward 1.0 (or -1.0).

Charm is most powerful in the **last 1-2 hours of trading on OPEX days** and in the final week before [[opex|monthly OPEX]]. Dealers re-hedge as charm accrues:

- A short OTM put dealer is long delta from that position (gamma-neutral but charm-accruing); as time passes the position becomes less long-delta -> dealer **sells** stock
- A short OTM call dealer is short delta; as charm decays the position becomes less short-delta -> dealer **buys** stock

In aggregate, charm flows on OPEX week tend to produce a slow-drift bias toward the highest-OI strike (the [[max-pain|max pain]] level) and a characteristic "afternoon drift" that experienced traders learn to recognize.

## OPEX Cycles

Monthly options expiration ("OPEX") is the third Friday of each month. Quarterly OPEX (third Friday of Mar/Jun/Sep/Dec) is "[[quad-witching|quad witching]]" -- simultaneous expiry of stock options, index options, index futures, and stock futures. Quarterly OPEX produces the largest gamma roll-off of the year.

The pattern that drives OPEX-aware entries:

1. **OPEX week (Mon-Thu):** gamma is concentrated -- pinning is strong, ranges compress, the market feels "stuck"
2. **OPEX Friday morning:** charm and gamma flows intensify; a few key strikes act as magnets
3. **OPEX Friday afternoon (post-close for monthly settlement):** roughly 30-50% of [[open-interest]] expires and rolls off the dealer book
4. **Following Monday/Tuesday:** the long-gamma "shock absorber" is gone or much smaller; small flows can move price meaningfully -> **vol expansion**

Empirical studies (cited by spotgamma and others) show post-OPEX Mondays have historically averaged ~1.5-2x the realized vol of OPEX-week Mondays, though this is a tendency, not a guarantee. The release is most pronounced when:

- OPEX week saw heavy pinning to a specific strike
- The pre-OPEX gamma flip level was tightly clustered around spot
- Post-OPEX positioning leaves dealers near or below the new flip level
- A macro catalyst (FOMC, [[non-farm-payrolls|NFP]], CPI) lands the week after OPEX

Experienced discretionary traders use post-OPEX windows for *initiating* directional swings and for *de-grossing* short premium. The pre-OPEX week is for harvesting theta inside the pinning range.

## How Retail Gets It Wrong

Most retail traders do not know dealer gamma exists, much less which side of it they are on. The predictable failure modes:

1. **Chasing breakouts on long-gamma days.** Spot pushes to the call wall, retail sees a "breakout," buys, and gets faded by dealer selling. The breakout has no follow-through because the dealer flow is mechanically opposite
2. **Fading panic dips on short-gamma days.** Spot crashes through the put wall; retail sees an "oversold bounce setup" and buys, only to watch dealers sell into every rally. The pain compounds because the regime requires *not* fading
3. **Selling vol at exactly the wrong time.** Selling [[short-strangle|short strangles]] when GEX is deeply negative is mathematically fighting the largest forced buyer/seller in the market. Most retail blow-ups in 2018, March 2020, and August 2024 (see [[vix-august-2024-spike]]) trace to short-vol positions held into a short-gamma regime
4. **Confusing dealer flows for fundamental signal.** A 50bp grind higher on a dovish-leaning [[fomc]] day looks like "the market loved the news" -- it is often just vanna and gamma unwind. Trading the *next* day on the assumption that fundamentals were the driver leads to overstaying
5. **Ignoring single-name gamma squeezes.** Retail piles into call buying, dealers chase, retail then assumes the move is "fundamental conviction" and holds through the squeeze unwind. See GME (Jan 2021), AMC (May 2021), NVDA (mid-2024) for repeated examples of [[gamma-squeeze|gamma squeezes]] and their reflexive collapses

The error pattern is consistent: retail interprets dealer-driven price action through a fundamentals/technicals lens, missing the structural cause.

## Trade Integration

A disciplined trade construction process integrates dealer gamma in three concrete ways:

### Sizing decisions

- **Net dealer gamma is large positive (rules of thumb: GEX > $4B in SPX):** size up [[options-premium-selling|short premium]] -- iron condors, short strangles, [[short-strangle|short strangles]] selling 1-sigma wings. The vol-suppressing dealer flow is doing the work for you
- **Net dealer gamma is mildly positive:** standard sizing on premium-selling; standard sizing on directional swings
- **Net dealer gamma is mildly negative:** cut short premium, prefer [[debit-spreads|debit spreads]] over [[credit-spreads]], size *down* on directional trades to allow for wider stops
- **Net dealer gamma is deeply negative:** no naked premium selling; only defined-risk long-vol structures (long [[straddle|straddles]], long [[gamma-scalping|gamma]]); size directional exposure to half-normal at most

### Entry timing

- Use the gamma flip level as intraday support (when above) and resistance (when below)
- Use [[call-wall|call walls]] as profit targets / take-profit zones for long deltas
- Use [[put-wall|put walls]] as cover zones for short deltas
- Use post-OPEX Monday/Tuesday for *initiating* swing trades (vol expansion makes follow-through more likely)
- Use OPEX week for *harvesting theta* (pinning makes mean-reversion more reliable)

### Hedging

- When you are long delta in a deeply short-gamma regime, your *implicit* position is much riskier than the headline delta number suggests -- realized vol on adverse days is 2-3x normal. Hedge with long puts or [[vix-futures|VIX futures]] aggressively
- Long-gamma regimes give you cheap hedging windows -- IV is suppressed, options are relatively cheap. Buy protection when GEX is highest, not after the regime breaks

The discipline: **let dealer gamma sign the trade idea, then use technicals/fundamentals to fine-tune entry**. Never invert the order.

## Limitations

Dealer gamma analytics are powerful but imperfect. Known limitations:

- **Estimated, not observed.** Public GEX numbers are estimates derived from listed [[open-interest|open interest]]. Dealers also run large OTC, FLEX, and structured-product books that are not visible. The true sign of dealer gamma can differ from the published sign at any moment
- **Assumes full hedging.** Models assume dealers fully hedge to delta-neutral. In practice dealers run residual exposure -- sometimes intentionally (proprietary views), sometimes because hedging would itself move the market. Dispersion desks at [[citadel]], susquehanna, and [[wolverine]] all run non-zero books
- **Customer flow assumption.** Most models assume "customers buy puts, sell calls" -- a reasonable normal-state assumption that breaks during call-buying frenzies (meme stocks, AI rallies) and put-buying panics
- **Large institutional flows can overwhelm dealer hedging.** [[volatility-control-funds|Vol-control fund]] de-leveraging, [[risk-parity]] re-balancing, [[cta]] trend-flow, and corporate buyback grids can dominate intraday tape regardless of dealer gamma. GEX is a *baseline*; large exogenous flows override it
- **0DTE distortion.** The explosion of 0DTE volume since 2022 has fundamentally altered gamma dynamics. Daily expiration means the gamma profile resets every day rather than monthly. Some traders argue this has *reduced* the predictive power of monthly OPEX patterns (see [[zero-dte-options|0DTE options]] and [[zero-dte-impact-on-vix|0DTE impact on VIX]])
- **Single-name vs. index.** Index GEX (SPX, QQQ) is reasonably well-modeled because option flow is concentrated. Single-name GEX is much noisier because flows are episodic and dealer assumptions are weaker
- **Backtest difficulty.** Historical GEX data is hard to obtain and providers' methodologies have changed over time. Naive [[backtesting|backtests]] of GEX-based strategies are unreliable
- **Reflexivity.** Once GEX-based trading became widespread post-2020, some of the cleanest patterns degraded. The pin-and-release effect is still visible but less reliable than 2018-2020

The bottom line: GEX is a *probabilistic regime classifier*, not a deterministic signal. Use it to bias sizing and structure, not as a stand-alone entry trigger.

## Tools

| Tool | Coverage | Strength | Notes |
|---|---|---|---|
| spotgamma | SPX, QQQ, single names | Industry standard for retail discretionary | ~$200/mo Alpha, ~$500/mo Pro; HIRO real-time hedging oscillator |
| [[tier1alpha]] | SPX, sectors, single names | Institutional-grade modeling, vol-control flow estimates | Premium pricing; used by hedge funds |
| [[menthorq]] | SPX, ES, single names | TradingView integration, real-time | Mid-tier pricing |
| [[squeezemetrics]] | SPX | Free GEX and DIX (dark pool indicator) | Limited but useful baseline |
| unusual-whales | SPX + heavy single-name | GammaLab visualization, options flow | Combines flow with positioning |
| [[cboe-skew]] | SPX | Implied tail-risk measure | Free; correlates with put-skew gamma exposure |
| Custom build | Anything | Full control | Requires [[opra-feed|OPRA feed]] + [[open-interest]] data + Black-Scholes greeks engine |

A custom GEX calculator is feasible for a quantitatively-inclined trader: pull daily open interest by strike from CBOE / OPRA, compute per-contract gamma using the [[black-scholes|Black-Scholes]] greeks formula at current spot and IV, sum across the chain with appropriate sign assumptions. The methodology is described in [[squeezemetrics]]'s public white paper.

For most discretionary traders, paying for spotgamma or [[tier1alpha]] is a better use of time than building custom GEX -- the analytics are sophisticated and the morning notes provide context (key levels, regime calls, OPEX setups) that a raw GEX number alone does not.

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

- [[gamma-exposure-trading]] -- the trading strategy built on top of GEX regime identification
- [[gamma-scalping]] -- the dealer's own technique applied at retail scale
- [[gamma]] -- the underlying [[options-greeks|Greek]]
- [[delta]] -- the first-order risk being hedged
- [[vanna]] -- the IV-driven hedging flow
- [[charm]] -- the time-driven hedging flow
- [[max-pain]] -- the magnetic strike behavior on OPEX
- [[opex|OPEX cycles]] -- the calendar driver of gamma roll-off
- [[zero-dte-options|0DTE options]] -- the structural change since 2022
- [[volatility-regime-classification]] -- broader framework that includes GEX as one input
- [[options-stress-testing]] -- using gamma scenarios for portfolio risk
- [[tier1alpha]] -- institutional alternative
- [[menthorq]] -- TradingView-native alternative
- [[squeezemetrics]] -- free baseline data
- [[market-makers]] -- the dealers doing the hedging
- [[vix-august-2024-spike]] -- a textbook short-gamma blow-up
- [[volmageddon]] -- the canonical historical short-gamma cascade
- [[gamma-squeeze]] -- single-name short-call-gamma feedback loop

## Sources

- General market-microstructure knowledge -- dealer hedging mechanics, options Greeks
- [[squeezemetrics]] white paper on aggregate GEX calculation methodology
- Cboe research notes on 0DTE impact on dealer gamma profile
- Public discussion of post-OPEX vol expansion (Goldman Sachs derivatives strategy notes, Nomura's QIS team commentary -- referenced in spotgamma and [[tier1alpha]] daily reports)
