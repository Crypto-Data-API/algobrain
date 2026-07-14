---
title: "Straddle"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, straddle]
aliases: ["Straddle", "Crypto Straddle"]
related: ["[[straddle-strangle]]", "[[strangle]]", "[[short-straddle]]", "[[iron-butterfly]]", "[[volatility-trading]]", "[[long-volatility-strategies]]", "[[short-volatility-strategies]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[delta]]", "[[vega]]", "[[theta]]"]
domain: [options]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
markets: [crypto, options]
---

# Straddle

A **straddle** is a two-legged option structure consisting of a call and a put on the same underlying, at the **same strike price** and the **same expiration**. It is a pure expression of a view on volatility relative to what the market has priced in: the **long** straddle profits if realized volatility exceeds the implied volatility paid; the **short** straddle profits if realized volatility comes in below the implied volatility received. In crypto this is traded on [[deribit]] BTC/ETH, where the premium is benchmarked against the [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] index.

This page is the conceptual umbrella covering **both directions** of the structure. For the tradeable long-vol playbook see [[straddle-strangle]]; for the systematic short-vol book see [[crypto-options-volatility-selling]] and [[short-straddle]]. For the split-strike cousin see [[strangle]]; for the risk-defined version see [[iron-butterfly]].

## Overview

A straddle is the simplest "pure vol" structure: because the two legs share a strike, the position has (approximately) zero directional exposure at inception and its P&L is driven almost entirely by how far the underlying travels and by what happens to implied vol. The **long** straddle is defined-risk / undefined-reward (you can only lose the debit, but gains are unbounded); the **short** straddle is the mirror — defined-reward / undefined-risk — and in crypto is almost always run risk-defined (as an [[iron-butterfly]]) or tightly delta-hedged because the tail is genuinely fat.

## Construction

Two simultaneous legs on the same underlying, same strike `K`, same expiry `T`:

- **One call** at strike `K` expiring at `T`
- **One put** at strike `K` expiring at `T`

The strike is chosen **at-the-money** (`K ≈ S`, the current spot), making the structure roughly delta-neutral: the ATM call's +0.5 delta offsets the ATM put's −0.5. The total premium = call premium + put premium. Because both legs are ATM, that premium is approximately the market's **expected absolute move** over the period (the Black-Scholes ATM-straddle result) — which in crypto is large, since BTC 30-day DVOL routinely sits at 40–60%.

| | Long straddle | Short straddle |
|---|---|---|
| Position | Buy call + buy put | Sell call + sell put |
| Volatility view | Long vol (realized > implied) | Short vol (realized < implied) |
| Max loss | Premium paid | Undefined (capped by margin in practice) |
| Max gain | Undefined | Premium received |
| Margin | Low (debit upfront) | High (undefined risk) |

## Payoff & breakevens

At expiry, both variants share the same breakevens, `K ± total premium`:

- **Long straddle** — profit outside the breakevens (a widening "V"); max loss = premium, at `S_T = K`.
  - Upper BE = `K + premium`; lower BE = `K − premium`.
- **Short straddle** — profit inside the breakevens (an inverted "V", capped at the credit); loss grows without bound outside them.

In crypto the breakevens are wide in percentage terms because ATM IV is high: a 30-day BTC straddle can imply a ~10–13% move to break even. The long side is betting the realized move clears that; the short side is betting it does not.

## Greeks profile

The Greeks stack from the two legs and flip cleanly between variants:

| Greek | Long straddle | Short straddle | Comment |
|---|---|---|---|
| [[delta]] | ≈ 0 at inception | ≈ 0 at inception | ATM call +0.5 cancels ATM put −0.5 |
| Gamma | Positive | Negative | Largest ATM; concentrates into expiry |
| [[vega]] | Positive | Negative | Both legs gain on IV rises (long) / lose (short) |
| [[theta]] | Negative | Positive | Both legs decay; long pays, short collects |
| Rho | Small | Small | Minor in crypto tenors |

A long straddle is "paying theta to be long gamma and long vega"; a short straddle is the inverse — "collecting theta for short gamma and short vega." The [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] index is the direct read on the vega leg.

## Market view / when to use

**Long straddle** — when [[implied-volatility]]/DVOL is *cheap* and there is reason to expect a vol expansion: a discrete crypto catalyst (protocol upgrade, ETF decision, token unlock, FOMC/CPI) with uncertain direction, or a coiled "compressed" [[volatility-regime|vol regime]] likely to break violently. The structural problem is timing — theta accelerates into expiry and DVOL often crushes after the event.

**Short straddle** — when DVOL is *elevated* (often post-event) and likely to revert toward realized vol, with the underlying expected to stay range-bound. It is the backbone of systematic premium-selling ([[crypto-options-volatility-selling]]) but is catastrophically exposed to crypto's gap moves; it is run delta-hedged or as an [[iron-butterfly]].

## Adjustments & management

- **Long**: take profit at 50–100% on the winning leg; leg out after a decisive move; convert to a [[gamma-scalping|gamma scalp]] by delta-hedging on the Deribit perp; roll up/out before the theta-heavy final weeks; cut on [[iv-crush]].
- **Short**: delta-hedge continuously (crypto gap risk), define the tail by buying wings (→ [[iron-butterfly]]), take profit at ~50% of credit, and honour a hard DVOL-spike kill switch — see [[crypto-options-volatility-selling]] for the full risk framework.

## Differences vs strangle and iron butterfly

- **[[strangle]]** — same vol view, **different strikes** (OTM call + OTM put). Cheaper, wider breakevens, gamma spread across two strikes rather than concentrated at `K`. Practitioners pick the straddle for maximum gamma at a known catalyst price, the strangle for cheaper exposure demanding a bigger move.
- **[[iron-butterfly]]** — the **risk-defined** version of the short straddle: short ATM call + short ATM put **plus** long OTM wings. Caps both the reward (net credit) and the loss (wing width − credit), collapsing margin. In crypto the iron butterfly is the practical way to express the "short straddle" view because naked, undefined-risk short vol is rarely acceptable given the tail.

## Crypto specifics

- **Venue**: [[deribit]] BTC/ETH dominate listed-option OI; [[greeks-live]] is the analytics workbench.
- **Inverse vs linear settlement**: classic Deribit options are **inverse (coin-margined)** — premium and P&L in the coin, so collateral moves with spot; **USDC-margined (linear)** options give clean USD P&L. Choose linear for a pure vol view.
- **DVOL**: the [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] index (Deribit's 30-day IV, the "crypto VIX") is the direct gauge of whether the straddle is cheap (buy) or rich (sell). **DVOL and the IV surface come from Deribit / [[greeks-live]], not CryptoDataAPI.**
- **24/7 & weekend gaps**: no market close means gamma works continuously; thin weekend liquidity produces air-pockets that help the long straddle and punish the short one.
- **No §1256**: offshore Deribit contracts get no [[section-1256-contracts|§1256]] 60/40 treatment (ordinary CGT/income; US short-term rates).
- **Perp-funding interaction**: [[funding-rate|funding]] shapes skew and prices the delta-hedge leg on the perp.
- **Alt-option liquidity**: usable straddles are effectively a BTC/ETH-only structure; alt option chains are too thin.

## Risks

- **Long**: [[iv-crush|DVOL crush]] after the catalyst, theta bleed in quiet tape, wide Deribit bid-ask, and a low per-trade hit rate (most events resolve smaller than implied).
- **Short**: unbounded gap risk (2020-03-12, LUNA, FTX, 2025-10-10), margin-spiral / auto-liquidation on a DVOL spike, and coin-margin wrong-way risk on inverse contracts.

## Worked crypto example

**BTC spot $60,000, 30 DTE, ATM 60,000 strike, each leg ≈ $3,450 → straddle premium ≈ $6,900** (≈ 11.5% of spot); breakevens **$53,100 / $66,900**.

- **Long straddle**: profits if BTC finishes below $53,100 or above $66,900 (or if DVOL spikes while held). Max loss $6,900 if it pins $60,000. Best paired with a compressed-DVOL entry ahead of a catalyst.
- **Short straddle**: collects the $6,900 credit, profits if BTC stays between the breakevens and DVOL reverts, but faces unbounded loss on a gap — which is why in practice it is capped into an [[iron-butterfly]] (buy 54,000 put + 66,000 call wings) and delta-hedged on the perp.

## Getting the Data (CryptoDataAPI)

The straddle's core input — implied vol / **DVOL** — is a **Deribit / [[greeks-live]]** product and is *not* served by CryptoDataAPI. [[cryptodataapi]] provides the surrounding context for deciding whether to be long or short the structure: the vol *regime*, options OI / max pain, dealer gamma, and funding.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed = cheap vol / buy; vol_shock = rich / sell)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory / cascade risk)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (RV vs DVOL = cheap/rich judgment)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/BTC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[straddle-strangle]] — the tradeable long-vol strategy page
- [[strangle]] — same vol view, different strikes
- [[short-straddle]], [[crypto-options-volatility-selling]] — the short-vol expressions
- [[iron-butterfly]] — risk-defined version of the short straddle
- [[volatility-trading]], [[long-volatility-strategies]], [[short-volatility-strategies]] — the parent disciplines
- [[deribit]], [[greeks-live]] — venue and DVOL/surface source
- [[delta]], [[vega]], [[theta]] — the dominant Greeks
- [[implied-volatility]], [[variance-risk-premium]] — what the straddle premium prices, and why short straddles carry an edge in calm regimes

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — straddles, strangles, butterfly spreads.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — Greek profile and volatility-based usage.
- [[deribit]] / [[greeks-live]] — DVOL construction, IV surface, cash settlement, inverse vs USDC-margined contracts.
