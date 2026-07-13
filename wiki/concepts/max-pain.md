---
title: "Max Pain"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, market-microstructure, behavioral-finance]
aliases: ["Max Pain", "Maximum Pain Theory", "Max Pain Strike"]
related: ["[[options-pinning]]", "[[pin-risk]]", "[[gamma-exposure]]", "[[dealer-hedging]]", "[[zero-dte-options]]", "[[volatility-skew]]", "[[options-open-interest]]", "[[opex]]", "[[gamma-flip]]", "[[implied-volatility]]"]
domain: [market-microstructure, options, behavioral-finance]
difficulty: intermediate
---

**Max pain** is the strike price at which the *largest aggregate dollar value* of outstanding options expires worthless — i.e., the strike that maximises the combined out-of-the-money-ness of all open puts and calls weighted by their open interest. The eponymous "Max Pain Theory" claims that, on or near monthly expiration, the underlying tends to gravitate toward this strike because of dealer [[dealer-hedging|hedging]] flows. The empirical literature finds a real but modest pinning effect on individual stocks, no strong effect on broad indices, and a phenomenon that has weakened materially since the 2022 explosion in [[zero-dte-options|0DTE]] expirations changed the open-interest term structure.

## Overview

Max pain has been a staple of retail options folklore since at least the early 2000s, when several options-data vendors began publishing daily "max pain strikes" for the most active single names alongside their open-interest charts. The intuition is appealing and easy to communicate: option *writers* (typically market makers and dealer desks) are net short premium and would prefer all open contracts to expire worthless; the level at which their aggregate payout is minimised — equivalently the level at which the *holders'* aggregate payout is minimised, hence "maximum pain" for the holders — becomes a magnet on expiration day.

The mechanism behind the theory is that dealers, who are the structural counterparty to retail and institutional option flow, hedge their net short-gamma exposure by trading the underlying. When spot drifts away from heavy open-interest strikes, hedge flows push it back; the "stable" point is the strike that minimises the dealer's aggregate hedging cost. In its strong form, the theory predicts that closing prices on monthly OPEX Friday will systematically cluster at the max-pain strike. In its weaker form, it predicts a measurable bias of expiry prices toward strikes with heavy open interest — without claiming determinism.

The strong form does not survive contact with data. The weak form does, on individual stocks, with effect sizes that are small relative to typical daily volatility. On broad indices (SPX, NDX) the effect is weaker still, partly because index OI is spread across more strikes and partly because index dealers run more sophisticated hedging strategies that do not concentrate at a single magnet point.

### Strong form vs weak form at a glance

| Claim | Form | Survives the data? |
|---|---|---|
| The close *always* lands on max pain at monthly OPEX | strong | No — rejected; close prices scatter |
| Expiry prices are *biased* toward heavy-OI strikes in active single names | weak | Yes — small, statistically significant ([[options-pinning]]) |
| The bias is *manipulation* by writers | strong | No — tested and rejected (Ni-Pearson-Poteshman) |
| The bias is *mechanical dealer hedging* | weak | Yes — the accepted mechanism ([[dealer-hedging]]) |
| Max pain works as well on indices as on single names | strong | No — indices much weaker, worse post-2022 |
| The magnet is the *max-pain* strike specifically | strong | No — it is the *heaviest-OI / gamma-weighted* strike ([[gamma-exposure]]) |

## Definition / Computation

For a given expiration, max pain is computed as follows.

Let `K_1, K_2, ..., K_n` be the listed strikes for the expiration. Let `OI_call(K_i)` and `OI_put(K_i)` be the open interest of calls and puts at each strike. For a hypothetical settlement price `S` on expiration day, the aggregate dollar value of options that expire **in the money** (the holders' payout, or equivalently the writers' loss) is:

```
TotalPayout(S) = sum_i [ max(S - K_i, 0) * OI_call(K_i) ]
              + sum_i [ max(K_i - S, 0) * OI_put(K_i) ]
```

multiplied by the contract multiplier (100 in US listed options). The **max pain strike** is the value of `S` (typically restricted to the listed strike grid) that *minimises* `TotalPayout(S)`:

```
K_max_pain = argmin_S TotalPayout(S)
```

In words: search across candidate settlement prices, compute total dollar payout at each, take the price that produces the smallest total. That price is the level at which writers pay out the least and holders receive the least — the "maximum pain" point for option buyers.

A simple worked example. Suppose at one expiration AAPL has the following open interest:

| Strike | Calls OI | Puts OI |
|--------|----------|---------|
| 170    | 5,000    | 30,000  |
| 175    | 12,000   | 18,000  |
| 180    | 25,000   | 8,000   |
| 185    | 22,000   | 4,000   |
| 190    | 14,000   | 2,000   |

Computing `TotalPayout(S)` at each strike:

| S   | Calls ITM | Puts ITM | Total ($/share) |
|-----|-----------|----------|-----------------|
| 170 | 0         | 0        | 0 + (5*18,000 + 10*8,000 + 15*4,000 + 20*2,000) = 270,000 |
| 175 | (5)*5,000 = 25,000 | 0 + (5*30,000) = 150,000 | 175,000 + 150,000 + ... |
| 180 | 5*5,000 + 0   | 10*30,000 + 5*18,000 | (computed in full) |
| 185 | 10*5,000 + 5*12,000 | 15*30,000 + 10*18,000 + 5*8,000 | ... |

The strike that minimises the full sum is the max-pain level. In practice, third-party vendors ([Maximum-Pain.com](https://www.maximum-pain.com/), [optionstrat](https://optionstrat.com/), [SpotGamma](https://spotgamma.com/) and others) compute and publish this number daily across thousands of underlyings.

Two computational subtleties matter:

1. **Open interest snapshot lag.** Public OI data is typically settled and reported by the OCC overnight. A max-pain strike computed from morning data is one session stale.
2. **Multiple OI clusters.** The minimisation can be near-flat across several adjacent strikes when OI is bimodal (heavy puts below spot and heavy calls above). In such cases the "max pain strike" is reported as a single number but represents an arbitrary tiebreaker.

## Mechanism (Why Strikes Matter)

The economic story behind the alleged effect is real, even if the simplified retail telling is too strong.

Dealers and market makers — the natural counterparty to public options flow — accumulate inventory by writing options that retail and institutions buy, and hedging the net Greek exposure in the underlying. The dominant hedging instrument is the underlying itself, traded delta-for-delta as positions move.

Near a strike with very heavy open interest, two effects emerge:

1. **Gamma cliff.** A short-gamma dealer's delta changes rapidly through the strike on expiration day. As spot crosses the strike, the dealer must buy or sell large quantities of the underlying. Symmetrically, a long-gamma dealer must sell into rallies and buy into dips, which mechanically *suppresses* moves through the strike.

2. **Mean-reverting rebalancing.** When spot drifts away from a heavy-OI strike late on expiration day, dealers running approximately delta-neutral books rebalance back toward neutral. If a dealer is long calls and short shares, a rally requires selling more shares, dampening the rally; a sell-off requires buying back shares, dampening the dip. The aggregate effect is *pinning* — sticky behaviour around strikes with heavy long-gamma dealer inventory.

The link to max pain in particular comes from the empirical regularity that dealer inventory tends to be *long gamma* near the strikes with heavy OI on monthly OPEX Fridays — because retail and institutional flow into expiring contracts has been net option-buying in the run-up to expiry. A long-gamma dealer hedging a net long position has the suppressing influence above. The strike with the heaviest OI is the natural attractor.

But — and this is where the retail folklore breaks down — the max-pain calculation itself is dollar-weighted across *all* strikes, not gamma-weighted. The strike that minimises holders' total payout is not necessarily the strike with the heaviest dealer long gamma. The two coincide *only* when OI happens to be roughly symmetric in calls and puts around a single peak. When OI is asymmetric (heavy puts below spot, light calls above), the max-pain strike can be a different number from the actual gamma-weighted attractor strike.

This is why empirical tests of "does the underlying close at the max-pain strike?" are systematically weaker than tests of "does the underlying pin to the heaviest-OI strike?" — the first is the wrong target.

See [[gamma-exposure|GEX]] and [[dealer-hedging]] for the more rigorous gamma-weighted version of the same intuition.

## Empirical Evidence

The serious academic literature on options pinning provides the empirical baseline.

**Ni, Pearson, and Poteshman (2005)**, *Stock Price Clustering on Option Expiration Dates*, *Journal of Financial Economics* 78(1): 49-87 — the canonical reference. The authors examine US single-stock options from 1996-2002 and find:

- Optionable stocks are statistically significantly more likely to close near a strike on expiration Friday than on a non-expiration Friday.
- The effect is concentrated in stocks with **active options trading** and is much weaker for thinly traded underlyings.
- The estimated magnitude is on the order of **a few tens of basis points** of additional density around strikes — real but small.
- The effect is **largely attributable to hedge rebalancing by option market makers**, not to deliberate manipulation by writers (the authors test and reject the manipulation hypothesis).
- The magnet strike is the **heaviest-OI strike**, not specifically the max-pain strike (though the two often coincide).

**Golez and Jackwerth (2012)** extend the analysis to S&P 500 futures options and find a similar but smaller pinning effect on the index. The effect on broad indices is meaningfully weaker than on single stocks, consistent with the dispersion of OI across more strikes and the more diversified dealer hedging book.

**Augustin, Brenner, and Subrahmanyam (2019)** revisit the analysis for the post-2010 period and find pinning effects roughly comparable to Ni-Pearson-Poteshman in single names, with the caveat that the rise of weekly options has spread OI across more expirations and slightly diluted the monthly-OPEX magnet effect.

The consensus across this literature: **pinning is real, dealer-hedging-driven, modest in magnitude, stronger in single names than indices, and cleanly identified by heavy OI rather than by the max-pain calculation specifically.** The popular max-pain narrative captures a real phenomenon but uses the wrong number to track it.

What pinning is *not*: it is not a 1-2% effect on close prices, it is not a deterministic gravity well, and it is not large relative to typical intraday volatility. A stock with a max-pain strike at $100 and a closing price at $99.85 is not evidence for the theory; that's noise. The Ni-Pearson-Poteshman effect manifests as a small bump in the *probability density* of expiration prices around heavy strikes, not as a guarantee that any particular session will close on a strike.

## Why It Has Weakened

Several structural changes since 2022 have eroded the max-pain effect on US indices and ETFs in particular.

**1. 0DTE diffusion.** Beginning with SPX daily expirations in May 2022 (followed by QQQ, IWM, and others), an enormous share of options volume has migrated to same-day-expiry contracts. By 2024-2025, [[zero-dte-options|0DTE]] options account for roughly 40-50% of total SPX options volume. These contracts open with zero open interest and accumulate OI through a single session before expiring. The traditional max-pain calculation — built on monthly OPEX OI accumulated over weeks — applies to a shrinking fraction of total options activity.

**2. OI fragmentation across daily expirations.** With expirations Monday through Friday, OI no longer concentrates at the third-Friday monthly. Instead, it spreads across five expirations per week. The "magnet effect" of any single expiration's max-pain strike is mechanically diluted because each expiration carries a smaller share of total open interest.

**3. Dealer book composition has shifted.** The growth of [[short-strangle|systematic premium-selling]] strategies, structured products (autocallables, principal-protected notes), and [[options-overlay|options overlay]] funds has changed which side of the book dealers run. Net short-gamma vs net long-gamma positioning is more dynamic and regime-dependent than the simple "dealers are long-gamma at heavy strikes" intuition.

**4. Algorithmic counterflow.** A generation of quantitative strategies explicitly trade *against* anticipated pinning — selling premium at heavy strikes, buying deep OTM into the close — which absorbs and damps the original effect. As soon as a market regularity becomes well-known, traders front-run it, and the regularity weakens. This is the standard arbitrage-decay mechanism.

**5. Index dealer hedging is more diffuse.** Modern index-options market-makers hedge across the entire greek surface (delta, gamma, vanna, charm, vega) rather than at the strike-by-strike level. The aggregate hedge is more often expressed in [[vix-futures]] or SPY than in raw index futures, further dispersing the strike-specific effect.

The net result: max pain as a tradeable signal has roughly the same status as classical [[technical-analysis|technical analysis]] — it captures a real if modest market regularity, has been heavily front-run by sophisticated participants, and now exists mostly as a retail folk belief whose practical edge has compressed toward zero on the most liquid US underlyings.

It remains marginally relevant on:

- Less heavily-arbitraged single stocks with chunky monthly OI.
- International indices where 0DTE has not yet diffused.
- Stocks around earnings expirations where OI accumulates in a particular pattern.

### Where the signal still has (some) life

| Underlying class | Pinning strength | Practical use of max pain |
|---|---|---|
| Liquid US single names, monthly OPEX | modest, real | weak edge; use [[gamma-exposure|GEX]] instead |
| Liquid US indices (SPX/NDX), monthly | weak, diluted | negligible; dominated by [[zero-dte-options|0DTE]] flow |
| Thinly-arbitraged single names, chunky OI | strongest residual | the one place a heuristic glance still pays |
| US indices, daily/0DTE expirations | effectively none | OI starts at zero each session; max pain undefined |
| International indices (pre-0DTE) | moderate | folk signal still partly intact |
| Crypto ([[deribit-options|Deribit]]) monthly | some around big expiries | different dealer mix; 0DTE now diluting it too |

The honest summary: never *trade* max pain as a standalone signal on liquid US underlyings; at most use it as a context flag and cross-check against the gamma-weighted picture in [[gamma-exposure]] and [[gamma-flip]].

## Distinction from Pinning and Pin Risk

Three related concepts get conflated and should be kept distinct.

**[[options-pinning|Pinning]]** is the empirical phenomenon: the tendency of underlying prices to cluster near strikes on expiration day, driven by dealer delta-hedging of net long-gamma positions. Pinning is the *result*; max-pain theory is one (somewhat flawed) attempt to predict *which* strike the price will pin at. Pinning is a well-documented market microstructure effect; max pain is a folk model of pinning.

**[[pin-risk|Pin risk]]** is a position-level concept describing the risk faced by a holder of a short option position when the underlying closes very close to the strike at expiration. The holder does not know with certainty whether the option will be exercised — and may be assigned post-close (e.g., on Saturday morning under historical OCC procedures, or now electronically through Sunday) on a deep stock position they did not anticipate. Pin risk is a real per-trade hazard; max pain is an aggregate market-level prediction. They are unrelated except by overlapping vocabulary.

**Max pain (this page)** is a specific summary statistic of the open-interest distribution — the strike that minimises aggregate option-holder payout. It is one possible target for the pinning effect, but a less accurate one than gamma-weighted summaries. As a tradeable signal it is weak; as a folk concept it is widely cited.

## Common Misconceptions

1. **"The market always closes at max pain on OPEX."** No. The Ni-Pearson-Poteshman effect is statistical, small, and operates on probability density rather than determinism. Close prices land near the max-pain strike more often than chance, but typically by a few tens of basis points of additional density.

2. **"Market makers manipulate price to max pain."** Manipulation has been tested and rejected in the academic literature. The effect is driven by the *mechanical hedging* of dealers running short-gamma positions, not by deliberate price control. Dealers are individually profit-maximising and would gladly let the price drift if their hedges did not require the trades.

3. **"Max pain works equally well on indices and single names."** It does not. Single names show stronger pinning; broad indices show weaker pinning, and the effect on indices has weakened further since 2022 with [[zero-dte-options|0DTE]] fragmenting OI.

4. **"Max pain is the same as gamma exposure."** It is not. Max pain weights OI by dollar-payout; [[gamma-exposure|GEX]] weights OI by gamma sensitivity. The two often agree but not always; GEX is the more rigorous predictor of dealer hedging pressure.

5. **"Max pain is predictive 1-2 weeks before expiration."** No. The pinning effect manifests in the final session or two of the contract life. OI weeks ahead of expiry is dominated by hedging and overlay flows that have nothing to do with where the underlying will settle.

6. **"Max pain works on crypto / FX / commodities."** Largely no — most of the literature is on US single-stock and index options. Crypto options ([[deribit-options|Deribit]] BTC options) show some pinning behaviour around big monthly expiries, but the dealer composition is different and the 0DTE dilution is now acute on Deribit too.

## Related

- [[options-pinning]] — the broader phenomenon of strike-clustering at expiry
- [[pin-risk]] — the position-level risk of being close to a strike at settlement
- [[gamma-exposure]] — the gamma-weighted (and more rigorous) cousin of max pain
- [[dealer-hedging]] — the underlying mechanism
- [[zero-dte-options]] — the structural change that has weakened max pain since 2022
- [[opex]] — monthly options expiration, the traditional setting for max pain
- [[options-open-interest]] — the input to the calculation
- [[gamma-flip]] — the level at which dealer gamma sign changes
- [[volatility-skew]] — affects the OI distribution and thus the max-pain strike

## Sources

- Ni, S. X., Pearson, N. D., and Poteshman, A. M. (2005). *Stock Price Clustering on Option Expiration Dates*. *Journal of Financial Economics*, 78(1): 49-87. The canonical empirical study; documents a small but statistically significant pinning effect driven by dealer hedging, not manipulation.
- Golez, B., and Jackwerth, J. C. (2012). *Pinning in the S&P 500 Futures*. *Journal of Financial Economics*, 106(3): 566-585. Extends the analysis to the index complex with similar but smaller effect sizes.
- Augustin, P., Brenner, M., and Subrahmanyam, M. G. (2019). *Informed Options Trading Prior to Takeover Announcements: Insider Trading?*. *Management Science*, 65(12): 5697-5720. Cited here for the post-2010 update on pinning persistence; the headline paper is on insider trading, but the methodology section discusses pinning baseline.
- OCC (Options Clearing Corporation) — daily open-interest data used to compute max-pain strikes.
- Cboe — historical reference on 0DTE expansion (May 2022 SPX daily expirations) and the resulting OI fragmentation.
- [[book-option-volatility-and-pricing]] — Natenberg covers pinning and the dealer-hedging mechanism in standard treatment.
