---
title: "Long-Dated Options (LEAPS)"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, leaps, long-dated, vega, rho]
aliases: ["LEAPS", "Long-Dated Options", "Long-Term Options"]
related: ["[[long-call]]", "[[long-put]]", "[[options-greeks]]", "[[vega]]", "[[theta]]", "[[gamma]]", "[[rho]]", "[[implied-volatility]]", "[[options-risk-budgeting]]", "[[volatility-skew]]", "[[long-vol-vs-short-vol]]", "[[long-volatility-strategies]]", "[[stock-replacement]]", "[[poor-mans-covered-call]]", "[[interest-rate-options]]"]
domain: [options, portfolio-theory, risk-management]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]", "[[long-call]]", "[[long-put]]"]
difficulty: intermediate
---

**LEAPS** -- Long-term Equity AnticiPation Securities -- are listed equity options with expirations 9 to 36 months out, distinguished from standard listed options (which typically expire within 12 months) only by their longer tenor. Originally introduced by the [[cboe|CBOE]] in 1990, LEAPS now exist on most large-cap US equities, the major US equity indices (SPX, NDX, RUT, DJX), and many ETFs. Their Greeks behave materially differently from short-dated options -- high [[vega]], low [[gamma]], low [[theta]], meaningful [[rho]] -- which makes them a distinct portfolio-construction tool rather than just "regular options with more time."

## Overview

The defining trade-offs of long-dated options vs. short-dated options:

| Greek | Short-dated (30 DTE) | LEAPS (730 DTE / 2yr) |
|---|---|---|
| Delta range | Sensitive: 0.05 to 0.95 across small price moves | Compressed: ~0.30 to ~0.85 even for far-OTM/ITM strikes |
| Gamma | High, especially near ATM in last weeks | Low; nearly constant across strikes |
| Vega | Modest | High; the dominant Greek |
| Theta | High in absolute terms; accelerates near expiry | Low in absolute terms; nearly linear |
| Rho | Negligible | Material; sensitive to forward rates |
| IV impact on price | Modest | Large |

This profile makes LEAPS structurally different instruments. A short-dated ATM call is a high-gamma, high-theta directional bet. A LEAPS ATM call is a long-vega, long-rho, slowly-decaying stock proxy with embedded leverage. The same insight is sometimes phrased as: short-dated options are bets on *price path*, while [[long-dated-options]] are bets on *price level plus volatility regime plus interest-rate regime*. See [[options-greeks]] for the full Greek framework and [[theta]] / [[vega]] / [[gamma]] / [[rho]] for the individual sensitivities.

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

LEAPS share the same listed-options framework as standard options, with these differences:

- **Tenor**: 9-36 months at issuance. The CBOE typically lists January expirations 2 and sometimes 3 years out; some indices have additional June and December LEAPS expirations.
- **Strike spacing**: Wider than near-month options for the same underlying (typically $5 increments on stocks above $50, $10 on stocks above $200).
- **Conversion to standard option**: When a LEAPS contract reaches less than 9 months to expiration, it is reclassified as a standard option (no contract change; the symbol remains the same).
- **Style**: American-style for individual stocks; European-style for cash-settled indices (SPX, NDX, RUT).
- **Settlement**: Physical delivery for stock LEAPS; cash for index LEAPS.
- **Listed venues**: [[cboe|Cboe]], NYSE Arca Options, NASDAQ PHLX -- LEAPS on major underlyings trade on multiple exchanges with shared liquidity.

(Source: [[cboe-leaps-product-specs]])

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

LEAPS books on a [[options-risk-budgeting]] dashboard *must* show net rho explicitly; equity-options books typically ignore rho but cannot ignore it once LEAPS are in the mix. See also [[interest-rate-options]] for the full rate-sensitivity dimension.

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

### 1. Stock replacement / leverage

The dominant retail use. Buy a deep-ITM LEAPS call (delta 0.80-0.90) instead of buying 100 shares:
- Capital outlay: a 24-month $150-strike call on a $200 stock might cost $60. Buying 100 shares costs $20,000; the call costs $6,000 for similar directional exposure.
- Effective leverage: roughly 3-4x (you control $20,000 of stock for $6,000 of capital).
- Trade-off: you pay theta (small but real) and lose any dividends. You also have a hard expiration -- a 24-month timeout that long-stock holders don't face. See [[stock-replacement]].

### 2. Multi-month directional bets

For a thesis that plays out over 6-18 months (e.g. a corporate restructuring, a multi-quarter cyclical recovery, a product cycle), LEAPS deliver the directional exposure with a long enough runway to avoid timing being a P&L driver. A 30-day call on the same thesis would expire before the thesis can play out and lose to theta even if directionally correct.

### 3. Vol-of-vol arbitrage

LEAPS are the long leg in [[term-structure]] vol trades:
- Long 24-month LEAPS, short 1-month options of the same strike: profits if long-end IV rises relative to short-end (term-structure steepening), or if realised vol over the next month is low.
- This is a [[long-volatility-strategies|long-vol]] trade in the term-structure dimension.

### 4. Poor man's covered call

Buy a deep-ITM 12-18 month LEAPS call as a stock substitute, then sell short-dated OTM calls against it for income. This [[poor-mans-covered-call]] structure mimics a [[covered-calls|covered call]] with a fraction of the capital outlay.

### 5. LEAPS puts as long-dated portfolio hedge

A long-dated OTM SPX put rolled annually is the cheapest form of [[tail-risk-hedging]] in many cycles -- the per-day theta cost is much lower than continuously rolling 60-day puts, though the convexity is also lower.

### 6. Tax considerations

Holding a LEAPS contract for more than 12 months can qualify gains for long-term capital gains treatment in many jurisdictions (notably the US), unlike short-dated options whose gains are typically short-term. This effective ~15-20% tax saving on the gain can be material for retail investors. Tax law is jurisdiction-specific and changes -- consult a tax professional. (Source: [[irs-publication-550]])

## Risks

- **Liquidity is materially worse than near-month options**. Bid-ask spreads on stock LEAPS can be 5-15% of mid; spreads on index LEAPS (SPX, NDX) are tighter (1-3%) but still wider than near-month. A round-trip cost of 4-8% is common.
- **Vega risk dominates** -- a long LEAPS call held through a vol-regime decline can lose money even with the underlying flat or up.
- **Rho risk** -- a hike cycle damages LEAPS puts and helps LEAPS ITM calls; a cut cycle does the opposite. Easy to overlook.
- **Dividend risk** -- LEAPS calls do not receive dividends; on high-yielding stocks, the implicit dividend cost over 2 years is substantial. Check the forward dividend stream before pricing the trade.
- **Corporate actions** -- mergers, special dividends, and splits over multi-year tenors can trigger contract adjustments that change the economic exposure (see [[options-corporate-action-adjustments]]).
- **Early exercise risk on American-style LEAPS calls** when a large dividend is imminent (rare but real).
- **Pin risk at expiration** is generally low (low gamma), but a LEAPS contract that is near-ATM at expiration still faces a binary settlement.
- **Model risk** -- the long-end of the IV surface is less observable and more model-dependent. Different brokers may price the same LEAPS materially differently.
- **Time concentration** -- a portfolio of LEAPS expiring in the same January creates a single point of expiration risk; consider laddering.

## Strike & Tenor Selection

LEAPS construction is dominated by two choices: how deep ITM to go, and how far out to date.

| Goal | Strike choice | Delta | Rationale |
|---|---|---|---|
| Tightest stock proxy | deep ITM | 0.80-0.90 | minimal extrinsic, behaves like shares, low theta drag |
| Maximum leverage | ATM / slightly OTM | 0.45-0.55 | most embedded leverage, most theta + vega risk |
| Long-vol expression | ATM | ~0.50 | maximises vega-per-dollar; bet is on IV regime |
| PMCC base ([[poor-mans-covered-call]]) | deep ITM | 0.80+ | low extrinsic so short calls can be sold profitably |
| Tail hedge ([[tail-risk-hedging]]) | OTM put | 0.10-0.25 | cheap convexity, rolled annually |

Tenor: the practitioner default is the longest *liquid* expiration, then roll roughly 9-12 months before expiry to avoid the gamma/theta acceleration of the final months — i.e. stay in the slow-decay zone and never let a LEAPS become a short-dated option by accident. Laddering expirations across two or three January cycles diffuses the single-point expiration risk noted under Risks.

## Worked Example

**Setup**: 2026-05-07. Trader is bullish AAPL on a 24-month thesis: services-led margin expansion. AAPL at $192. The trader considers two paths:

1. Buy 100 shares: $19,200 outlay; full upside; full downside; receives $96/year in dividends.
2. Buy 1x AAPL Jan 2028 $170 LEAPS call (~620 days out) at $42 per contract: $4,200 outlay; long 0.78 delta = ~78 shares of effective exposure; no dividend.

**Greeks comparison** (per LEAPS contract):

| Greek | Value |
|---|---|
| Delta | +0.78 |
| Gamma | +0.005 (very low) |
| Vega | +$0.45 per IV point (vs. ~$0.10 on a 30-DTE call) |
| Theta | -$0.04/day |
| Rho | +$0.32 per 100bp |

**Scenarios at expiration (Jan 2028)**:
- AAPL at $250: stock = +$5,800 + $192 dividends = +$5,992 (+31% on capital). LEAPS = max(250-170, 0) - 42 = $38 = +$3,800 per contract (+90% on capital). LEAPS wins on % return; stock wins on absolute dollars.
- AAPL at $192 (flat): stock = +$192 dividends = +1%. LEAPS = max(192-170, 0) - 42 = -$20 = -$2,000 (-48%). Stock wins decisively in flat scenarios.
- AAPL at $150: stock = -$4,200 + $192 = -$4,008 (-21%). LEAPS = -$4,200 (-100%). Both lose; LEAPS loss is bounded.
- AAPL at $100: stock = -$9,200 + $192 = -$9,008 (-47%). LEAPS = -$4,200 (-100%). LEAPS loss is bounded; bigger drawdown protection.

**Vega scenario**: AAPL flat at $192 but IV drops 5 points (large vol regime change). LEAPS = -$2.25 in vega P&L on top of theta -- a notable hidden loss the stock holder doesn't experience.

The LEAPS structure is asymmetric: better in the bullish tail and the bearish tail (bounded loss), worse in the middle (theta + vega bleed if flat). It's a leveraged bet on movement, not a stock substitute in the strict sense.

## Related

- [[long-call]] / [[long-put]] -- LEAPS are these structures with longer tenor
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
