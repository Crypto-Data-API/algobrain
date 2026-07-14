---
title: "Long-Dated Options"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, derivatives, crypto, leaps, long-dated, vega, rho]
markets: [crypto, options]
aliases: ["LEAPS", "Long-Dated Options", "Long-Term Options", "Long-Dated Crypto Options"]
related: ["[[deribit]]", "[[dvol]]", "[[funding-rate]]", "[[crypto-options-volatility-selling]]", "[[long-call]]", "[[long-put]]", "[[options-greeks]]", "[[vega]]", "[[theta]]", "[[gamma]]", "[[rho]]", "[[implied-volatility]]", "[[options-risk-budgeting]]", "[[volatility-skew]]", "[[long-vol-vs-short-vol]]", "[[long-volatility-strategies]]", "[[stock-replacement]]", "[[poor-mans-covered-call]]", "[[interest-rate-options]]"]
domain: [options, portfolio-theory, risk-management]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]", "[[long-call]]", "[[long-put]]"]
difficulty: intermediate
---

**Long-dated options** are options whose expiration is many months to a few years out — far enough that their Greeks behave differently from short-dated contracts (high [[vega]], low [[gamma]], low [[theta]], meaningful rate/carry sensitivity), making them a distinct portfolio-construction tool rather than just "regular options with more time." The equity instance is **LEAPS** (Long-term Equity AnticiPation Securities) — listed equity options with 9-36-month tenors, introduced by the [[cboe|CBOE]] in 1990. **Crypto has no LEAPS**: on [[deribit|Deribit]], the deep long end of the BTC/ETH curve tops out near ~12 months (quarterly/annual expiries), it is European-style and cash-settled to a Deribit index, and its "rho" is really sensitivity to the [[perpetual-futures|perp]]/[[funding-rate|funding]]-and-basis forward rather than a risk-free discount rate. This page covers the long-dated-options concept in general and flags where the crypto version diverges from the equity LEAPS framing it was first written for (collected in **Crypto specifics**).

## Overview

The defining trade-offs of long-dated options vs. short-dated options:

| Greek | Short-dated (30 DTE) | Long-dated (~365 DTE / ~1yr — crypto's practical max) |
|---|---|---|
| Delta range | Sensitive: 0.05 to 0.95 across small price moves | Compressed: ~0.30 to ~0.85 even for far-OTM/ITM strikes |
| Gamma | High, especially near ATM in last weeks | Low; nearly constant across strikes |
| Vega | Modest | High; the dominant Greek |
| Theta | High in absolute terms; accelerates near expiry | Low in absolute terms; nearly linear |
| Rho | Negligible | Material; sensitive to forward rates |
| IV impact on price | Modest | Large |

This profile makes long-dated options structurally different instruments. A short-dated ATM call is a high-gamma, high-theta directional bet. A long-dated ATM call is a long-vega, high-carry, slowly-decaying coin proxy with embedded leverage. The same insight is sometimes phrased as: short-dated options are bets on *price path*, while long-dated options are bets on *price level plus volatility regime plus carry/[[funding-rate|funding]] regime* (the crypto stand-in for the equity trader's interest-rate regime). See [[options-greeks]] for the full Greek framework and [[theta]] / [[vega]] / [[gamma]] / [[rho]] for the individual sensitivities.

### When to reach for LEAPS vs short-dated options

| Situation | Prefer LEAPS | Prefer short-dated |
|---|---|---|
| Thesis horizon | 6-36 months | days to weeks |
| Primary exposure wanted | direction + IV regime | direction / gamma scalp |
| Capital efficiency vs stock | high (stock replacement) | not the use case |
| Vol view | long-term IV is cheap | near-term IV mispriced |
| Tolerance for theta bleed | low (small per day) | high (paid for gamma) |
| Rate view matters | yes (rho material) | no (rho ~0) |
| Liquidity needs | can accept wide spreads | needs tight spreads |

See [[stock-replacement]], [[poor-mans-covered-call]], and [[long-volatility-strategies]] for the canonical LEAPS use cases and [[zero-dte-options]] for the opposite end of the tenor spectrum.

## Contract Specifications

Long-dated options share the same framework as standard options; the specs differ sharply between the equity LEAPS instance and the crypto (Deribit) instance:

| Spec | Equity LEAPS | Crypto long-dated (Deribit BTC/ETH) |
|---|---|---|
| **Max tenor** | 9-36 months (CBOE lists January expiries 2-3 years out) | ~12 months — quarterly and annual (last-Friday) expiries; no multi-year contracts |
| **Style** | American on single stocks; European on cash indices (SPX, NDX) | European-style only (no early exercise) |
| **Settlement** | Physical delivery on stock LEAPS; cash on index LEAPS | Cash-settled to a Deribit BTC/ETH index — no delivery, minimal pin risk |
| **Venues** | CBOE, NYSE Arca, NASDAQ PHLX (shared liquidity) | Effectively one venue (Deribit); OKX/Binance far thinner at the long end |
| **Strike spacing** | Wider than near-month ($5-$10 increments) | Coarser at the long end; far fewer listed strikes than the front months |
| **Reclassification** | A LEAPS becomes a "standard option" under 9 months (same symbol) | No LEAPS category exists — a contract is just longer-dated |

The practical consequence: there is **no 2-3 year crypto option**. The longest liquid crypto tenor (~1 year, and realistically the 3-6 month part of the curve for anything but headline BTC/ETH strikes) is shorter than the equity trader's LEAPS toolkit, so multi-year theses cannot be expressed in a single crypto contract — they must be rolled.

(Source: [[deribit]] contract specs; [[cboe-leaps-product-specs]] for the equity contrast)

## Pricing & Greeks

The Black-Scholes pricing identity for LEAPS is the same as for short-dated options:

```
Call = S × e^(-qT) × N(d1) - K × e^(-rT) × N(d2)
```

But each input now contributes very differently because T is large (1-3 years):

### Vega is the dominant Greek

Vega scales roughly with √T. A 2-year ATM call has roughly 2-3x the vega of a 30-day ATM call at the same moneyness. This means:
- A 1-vol-point IV change moves a $10 short-dated call by ~$0.20 but moves a $30 LEAPS call by ~$1.50.
- LEAPS positions are *materially exposed to long-term IV regime*, not near-term IV.
- LEAPS are typically priced using a longer-dated portion of the [[volatility-surface]] which is less liquid, less observable, and more model-dependent than the front of the curve.

### Gamma is low and nearly flat

Gamma scales roughly with 1/√T. A 2-year ATM call has roughly 1/3 the gamma of a 30-day ATM call. As a result:
- Delta-hedging a LEAPS position is much less expensive (rebalances less frequently).
- The convexity benefit of being long gamma is muted; LEAPS calls behave more like delta-only instruments.

### Theta is small in absolute terms but compounds

Theta on a 30-day ATM call might be -$0.10/day. On a 2-year ATM call it might be -$0.02/day -- much smaller per day, but accumulating over a longer hold. Total theta cost over two years can still equal 50-80% of the option's premium if held to expiration without an offsetting move.

### Rho is meaningful

This is the most-overlooked feature of LEAPS:
- For a 30-day ATM call, rho is typically a few cents per 100bp -- ignorable.
- For a 2-year ATM call, rho can be 5-12% of the premium per 100bp move in rates.
- In the 2022-2024 rate-hike cycle, this materially affected LEAPS pricing -- ITM call premiums rose with rates (cheaper to delay payment for the strike), while LEAPS puts richened (better to receive cash sooner if rates are high).

Long-dated books on a [[options-risk-budgeting]] dashboard *must* show net rho explicitly; short-dated books typically ignore rho but cannot ignore it once long tenors are in the mix. See also [[interest-rate-options]] for the full rate-sensitivity dimension.

**Crypto's rho is carry, not rates.** A Deribit option prices off the *forward*, which for BTC/ETH embeds the [[perpetual-futures|perp]]/futures **basis and [[funding-rate|funding]]**, not just a USD risk-free rate. So the long-dated crypto analog of rho is sensitivity to that carry — and crypto carry is far more volatile than the Fed funds path: futures basis and funding swing from deeply positive in leveraged bull runs (a long-dated call's forward is pushed up) to negative after a crash. A 6-12 month BTC call therefore carries a meaningful, *time-varying* carry sensitivity that a US-rates rho intuition understates. USDC-margined (linear) contracts also carry ordinary USD-rate rho on top; inverse (coin-margined) contracts fold the carry into the collateral leg. Track net carry sensitivity the way an equity LEAPS book tracks rho.

### Skew & term structure

The long-dated end of the [[volatility-surface]] has a flatter skew than the short-dated end (left-tail risk averages out over longer horizons), and term structure usually slopes upward (longer expirations have higher IV). LEAPS pricing is therefore typically *richer in vega-per-dollar* than short-dated options at the same moneyness, even though the IV level itself is higher. See [[volatility-skew]] and [[implied-volatility]] for the surface dynamics that drive this.

### How the Greeks scale with tenor (rules of thumb)

These approximations follow from the Black-Scholes closed forms and are the practical mental model for re-pricing a LEAPS as conditions change:

| Greek | Scaling vs √T | Practical consequence |
|---|---|---|
| Vega | ∝ √T | doubling tenor multiplies vega by ~1.4x; LEAPS vega dominates the book |
| Gamma | ∝ 1/√T | longer tenor flattens gamma; cheap to delta-hedge, little convexity |
| Theta | ∝ 1/√T (per day) | small daily bleed, but accumulates over the long hold |
| Rho | ∝ T (roughly) | rho grows ~linearly with tenor; the overlooked LEAPS risk |
| Delta | compresses toward 0.5 | far-OTM/ITM strikes have less extreme delta than at short tenor |

The √T relationships mean a LEAPS is best understood as a *vega-and-rho instrument with a delta attached*, not a delta instrument with minor Greeks. Contrast the short-dated profile in [[gamma]] and [[zero-dte-options]], where gamma and theta dominate.

## Use Cases

### 1. Coin replacement / leverage

The dominant retail use — the crypto analog of stock replacement. Buy a deep-ITM long-dated call (delta 0.80-0.90) instead of holding spot:
- Capital outlay: a ~1-year $40,000-strike BTC call with BTC at $60,000 might cost ~$24,000; holding 1 BTC of spot costs $60,000. The call gives similar directional exposure for a fraction of the capital, with downside capped at the premium.
- Effective leverage: roughly 2-3x, without the liquidation risk of a [[perpetual-futures|perp]] — the option cannot be margin-called out at a bad tick the way a leveraged perp can.
- Trade-off: you pay theta (small but real), forgo any staking yield (for ETH), and accept a hard ~1-year expiration/roll. See [[stock-replacement]].

### 2. Multi-quarter directional bets

For a thesis that plays out over 6-12 months (e.g. a halving-cycle move, ETF-driven adoption, a major protocol upgrade, or a multi-quarter narrative), long-dated calls deliver directional exposure with enough runway that timing isn't the dominant P&L driver. A 1-week call on the same thesis would expire long before it plays out and bleed to theta even if directionally correct. Crypto's ~12-month tenor cap means genuinely multi-year theses must be *rolled* rather than held in one contract.

### 3. Vol-of-vol / term-structure trades

Long-dated crypto options are the long leg in [[term-structure]] vol trades:
- Long a 6-12 month option, short a 1-week or 1-month of the same strike: profits if long-end [[dvol|DVOL]]/IV rises relative to the front (term-structure steepening), or if realised vol over the next month is low.
- This is a [[long-volatility-strategies|long-vol]] trade in the term-structure dimension — readily expressed on Deribit's BTC/ETH surface.

### 4. Poor man's covered call

Buy a deep-ITM 6-12 month call as a coin substitute, then sell short-dated OTM calls against it for income. This [[poor-mans-covered-call]] structure mimics a [[covered-calls|covered call]] on spot BTC/ETH with a fraction of the capital outlay (and is what several on-chain covered-call vaults automate).

### 5. Long-dated puts as portfolio hedge

A long-dated OTM BTC put rolled periodically is a relatively cheap form of [[tail-risk-hedging]] for a crypto book — the per-day theta cost is lower than continuously rolling short-dated puts, though the convexity is also lower and the ~12-month tenor limit means more frequent rolls than an equity SPX-put program.

### 6. Tax considerations

There is **no [[section-1256-contracts|§1256]] treatment** for crypto options — the US 60/40 blended rate and mark-to-market that apply to broad-based index options (and the long-term-cap-gains benefit of a >12-month equity LEAPS hold) do **not** carry over to offshore Deribit contracts. Treatment is jurisdiction-specific: in the US, crypto-option gains are ordinary capital gains (short-term at full marginal rates unless a holding-period rule applies); in Australia, an *investor* holding >12 months may access the 50% CGT discount, but anyone with *trader* status is taxed on ordinary/trading-income account regardless of tenor. Record-keeping across coin-margined P&L is onerous. Tax law changes — consult a professional. (Source: [[section-1256-contracts]]; [[irs-publication-550]] for the US-equity contrast)

## Risks

- **Liquidity is materially worse than near-month options** -- and worse in crypto than in equities. The long end of even the Deribit BTC/ETH curve carries wide vol-point spreads and thin OI; anything past ~6 months is sparse, and long-dated alt options effectively don't trade. Budget a large round-trip cost and use RFQ (Paradigm) for size.
- **Vega risk dominates** -- a long-dated call held through a [[dvol|DVOL]]/vol-regime decline can lose money even with the underlying flat or up. Crypto vol regimes shift faster and further than equity ones.
- **Carry (crypto "rho") risk** -- the forward embeds [[funding-rate|funding]] and futures basis, which swing widely; a long-dated call bought when carry is richly positive re-prices lower if funding collapses post-crash. USDC contracts add ordinary USD-rate rho on top.
- **Forgone yield** -- long-dated ETH calls do not receive staking yield, and the forward already prices the carry; there are no equity-style cash dividends, but the yield/carry drag over ~1 year is real. Check the forward (basis) before pricing the trade.
- **Corporate-action analogs** -- hard forks, token migrations, and large airdrops over a long tenor can trigger Deribit contract adjustments that change the economic exposure (the crypto counterpart of splits/special dividends; see [[options-corporate-action-adjustments]]).
- **No early-exercise risk** -- Deribit options are European-style and cash-settled, so the American-style early-assignment risk that dogs equity LEAPS calls simply does not exist. A genuine advantage.
- **Pin risk at expiration** is generally low (low gamma) and further muted by cash settlement to the Deribit index, but a near-ATM long-dated contract still faces a binary settlement print.
- **Model risk** -- the long end of the crypto IV surface is even less observable than equities': DVOL is a 30-day index, so long-dated IV is extrapolated, and the sparse long-end strike grid makes the surface more model-dependent.
- **Single-venue and collateral risk** -- Deribit *is* the long-dated crypto options market (no deep fallback), and inverse (coin-margined) contracts move the collateral with spot; use USDC-margined (linear) for clean USD exposure.
- **Time concentration** -- a book of long-dated options all on the same quarterly/annual expiry is a single point of expiration risk; ladder across Deribit's quarterly cycles.

## Strike & Tenor Selection

LEAPS construction is dominated by two choices: how deep ITM to go, and how far out to date.

| Goal | Strike choice | Delta | Rationale |
|---|---|---|---|
| Tightest coin proxy | deep ITM | 0.80-0.90 | minimal extrinsic, behaves like spot, low theta drag |
| Maximum leverage | ATM / slightly OTM | 0.45-0.55 | most embedded leverage, most theta + vega risk |
| Long-vol expression | ATM | ~0.50 | maximises vega-per-dollar; bet is on the [[dvol\|DVOL]] regime |
| PMCC base ([[poor-mans-covered-call]]) | deep ITM | 0.80+ | low extrinsic so short calls can be sold profitably |
| Tail hedge ([[tail-risk-hedging]]) | OTM put | 0.10-0.25 | cheap convexity, rolled periodically |

Tenor: the practitioner default is the longest *liquid* expiration — in crypto that means the deep 3-6 month part of the Deribit curve, with ~12 months the outer bound rather than the 2-3 years an equity LEAPS trader can reach. Roll before the contract drifts into the thin, high-decay final weeks — stay in the slow-decay zone and never let a long-dated position become a short-dated one by accident. Ladder across Deribit's quarterly cycles to diffuse the single-point expiration risk noted under Risks.

## Worked Example

**Setup**: 2026-07-14. Trader is bullish BTC on a ~1-year thesis: halving-cycle continuation plus ETF-driven adoption. BTC at $60,000. The trader considers two paths (USDC-margined, 1 BTC per contract):

1. Buy 1 BTC spot: $60,000 outlay; full upside; full downside; no yield.
2. Buy 1x Deribit ~1-year (Jun 2027) $45,000-strike BTC call (deep ITM, ~0.80 delta) at ~$21,000: $21,000 outlay; ~0.80 delta = ~0.8 BTC of effective exposure; downside capped at the premium.

**Greeks comparison** (per contract, 1 BTC):

| Greek | Value |
|---|---|
| Delta | +0.80 |
| Gamma | +low (near-flat at this tenor) |
| Vega | +$180 per DVOL/IV point (vs. ~$40 on a 30-DTE call) |
| Theta | small per day (accumulates over the ~1-year hold) |
| Carry (rho analog) | sensitive to [[funding-rate\|funding]]/basis — rich positive funding lifts the call's forward |

**Scenarios at expiration (Jun 2027)**:
- BTC at $90,000: spot = +$30,000 (+50% on capital). Call = max(90k−45k, 0) − 21k = +$24,000 (+114% on capital). Call wins on % return; spot wins on absolute dollars.
- BTC at $60,000 (flat): spot = 0%. Call = max(60k−45k, 0) − 21k = −$6,000 (−29%). Spot wins decisively in flat scenarios (theta + vega bleed).
- BTC at $45,000: spot = −$15,000 (−25%). Call = −$21,000 (−100%). Both lose; here the strike floor means the deep-ITM call has actually lost more.
- BTC at $30,000: spot = −$30,000 (−50%). Call = −$21,000 (bounded). Below ~$39,000 the call's capped loss beats holding spot — the bearish-tail protection.

**Vega scenario**: BTC flat at $60,000 but DVOL drops 10 points (a large but routine crypto vol-regime change). The call takes ~−$1,800 in vega P&L on top of theta — a notable hidden loss the spot holder doesn't experience, and larger in crypto than in equities because DVOL swings are wider.

The long-dated call is asymmetric: better in the bullish tail and the bearish tail (bounded loss below ~$39k), worse in the middle (theta + vega bleed if flat). It's a leveraged bet on movement with capped downside — and, unlike a [[perpetual-futures|perp]], it cannot be liquidated at a bad tick — not a spot substitute in the strict sense.

## Crypto Specifics

The Greek scaling (vega ∝ √T, gamma ∝ 1/√T, theta small-but-cumulative) is model-driven and identical for crypto. What changes going from equity LEAPS to long-dated crypto options:

- **No LEAPS, and a ~12-month ceiling.** [[deribit|Deribit]] lists BTC/ETH options out to roughly a year (quarterly/annual expiries); there is no 2-3 year contract. Multi-year theses must be rolled, so "buy and forget" stock-replacement over 24 months has no crypto equivalent.
- **"Rho" is carry, not rates.** Crypto options price off the perp/futures forward, which embeds [[funding-rate|funding]] and basis. That carry is far more volatile than a central-bank rate path and can flip sign around a crash — the dominant rate-like sensitivity of a long-dated crypto position. USDC (linear) contracts add ordinary USD rho on top.
- **No dividends; forgone staking yield instead.** BTC pays nothing; ETH's staking yield is a soft carry the option holder forgoes, already reflected in the forward. There is no dividend-driven early-assignment problem because Deribit options are **European-style and cash-settled** — removing a whole class of equity-LEAPS risk.
- **Thinner long end.** Liquidity past ~6 months is sparse even on BTC/ETH and non-existent on alts; expect wide vol-point spreads and use RFQ for size. The long-dated crypto surface is more model-dependent than equities' because [[dvol|DVOL]] is only a 30-day index and the long end is extrapolated.
- **Fatter vol swings.** DVOL can move far more than VIX, so the vega that dominates a long-dated position is a larger, faster-moving risk than an equity LEAPS holder faces.

## Getting the Data (CryptoDataAPI)

The long-dated IV surface and DVOL term structure come from [[deribit|Deribit]] / [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] supplies the carry (funding/basis), vol-regime, and options-positioning context that price the "rho" and vega of a long-dated book.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the crypto carry / "rho" driver
- `GET /api/v1/derivatives/open-interest?coin=BTC` — futures/perp OI feeding the basis
- `GET /api/v1/volatility/regime` — per-asset vol regime (the vega risk that dominates long tenors)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike

**Historical data:**
- `GET /api/v1/backtesting/funding` — historical funding for modeling carry over a long hold
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; funding/derivatives detail on [[cryptodataapi]].

## Related

- [[deribit]] — the venue and contract specs for long-dated crypto options
- [[dvol]] — the crypto vol index; its 30-day tenor is why the long end is extrapolated
- [[funding-rate]] — the carry that stands in for equity LEAPS rho
- [[crypto-options-volatility-selling]] — the short-vol counterpart on the same surface
- [[long-call]] / [[long-put]] -- long-dated options are these structures with longer tenor
- [[options-greeks]] -- the Greek framework with LEAPS-specific behaviour
- [[vega]] -- the dominant Greek for LEAPS
- [[rho]] -- usually ignored; mandatory to track for LEAPS
- [[volatility-surface]] -- long-end of the surface for LEAPS pricing
- [[volatility-skew]] -- flatter at long tenors
- [[stock-replacement]] -- the canonical retail use of LEAPS
- [[poor-mans-covered-call]] -- LEAPS-based covered-call substitute
- [[options-risk-budgeting]] -- LEAPS contributions to portfolio Greeks
- [[long-volatility-strategies]] -- LEAPS as the long-vol leg
- [[tail-risk-hedging]] -- LEAPS puts for low-cost hedging
- [[interest-rate-options]] -- the rho dimension generalised
- [[options-corporate-action-adjustments]] -- multi-year tenor risks

## Sources

- [[cboe-leaps-product-specs]] -- LEAPS product specification.
- [[book-options-as-a-strategic-investment]] (McMillan) -- LEAPS strategy chapter.
- [[book-option-volatility-and-pricing]] (Natenberg) -- term structure of vega/theta.
- [[irs-publication-550]] -- US tax treatment of options gains by holding period.
- [[occ]] -- Options Clearing Corporation contract specifications and adjustments memorandum.
