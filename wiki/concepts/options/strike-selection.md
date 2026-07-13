---
title: "Strike Selection"
type: concept
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, indicators, methodology]
aliases: ["Picking Strikes", "Delta-Based Strike Selection", "Probability-Based Strike Selection", "Strike Picking"]
domain: [options, technical-analysis]
prerequisites: ["[[options]]", "[[delta]]", "[[implied-volatility]]", "[[options-selection-framework]]"]
difficulty: intermediate
related:
  - "[[delta]]"
  - "[[gamma]]"
  - "[[theta]]"
  - "[[vega]]"
  - "[[iv-rank-and-iv-percentile]]"
  - "[[options-selection-framework]]"
  - "[[options-liquidity-screening]]"
  - "[[expiration-selection]]"
  - "[[moneyness-selection]]"
  - "[[spread-width-selection]]"
  - "[[probability-of-profit]]"
  - "[[cash-secured-puts]]"
  - "[[covered-calls]]"
  - "[[iron-condors]]"
  - "[[credit-spread]]"
  - "[[moneyness-selection]]"
  - "[[iv-crush]]"
  - "[[volatility-risk-premium]]"
---

**Strike selection** is the act of picking the specific exercise prices for the options legs in a structure. After [[options-liquidity-screening|liquidity screening]] and [[expiration-selection|DTE choice]], strike picking is where most traders' edge is created or destroyed. The dominant industry convention is **delta-based selection** — using an option's delta as a proxy for the probability that strike finishes in-the-money — rather than chart-based or "feels right" selection.

## Delta as Approximate Probability of Expiring ITM

Under Black-Scholes assumptions, the absolute value of an option's delta approximates the risk-neutral probability the option finishes in-the-money at expiration. This is not exactly true (delta and probability of ITM diverge slightly because of skew, drift, and the difference between risk-neutral and physical measures), but the approximation is close enough that practitioners use it directly.

| |Delta| (call or |put|) | Approx P(ITM at expiry) | Approx P(OTM at expiry) |
|---|---|---|
| 0.10 | ~10% | ~90% |
| 0.16 | ~16% | ~84% |
| 0.20 | ~20% | ~80% |
| 0.30 | ~30% | ~70% |
| 0.40 | ~40% | ~60% |
| 0.50 | ~50% | ~50% (ATM) |
| 0.70 | ~70% | ~30% |
| 0.84 | ~84% | ~16% |

This is the foundation of the delta convention: a "16-delta short put" has roughly an 84% chance of finishing OTM, which is the sense in which premium sellers describe it as "high probability."

## Common Strike Conventions

Specific delta values have become industry shorthand because they correspond to recognizable statistical anchors.

### 16 Delta — One Standard Deviation

A 16-delta strike is approximately one standard deviation OTM. From the Black-Scholes lognormal distribution, the 1-sigma move at expiration corresponds to a probability of ~16% in either tail (a normal distribution has ~15.87% beyond 1σ; lognormal is similar at typical equity vols).

- ~84% probability of expiring OTM (single leg)
- ~68% probability of profit on a credit spread once the credit cushion is added
- The "tastytrade default" for short premium

### 30 Delta — Tighter Premium Sale

A 30-delta strike is closer to ATM, ~0.5-0.7 standard deviations OTM.

- ~70% probability of expiring OTM
- ~60-65% PoP on a credit spread (depends on width)
- Larger credit collected, larger gamma exposure
- Used when [[iv-rank-and-iv-percentile|IVR]] is moderate and the trader wants meaningful credit per trade

### 50 Delta — At The Money

A 50-delta call (or 50-delta put) is at-the-money — the strike equal to spot.

- Maximum gamma and vega
- ~50% probability of expiring ITM on each side
- The benchmark for ATM straddles, ATM debit spreads, and gamma-scalping setups

### 70 Delta — Deep ITM, Synthetic Stock

A 70-delta call has ~0.70 of the underlying's directional exposure. At 80-delta and above, the call behaves nearly identically to the underlying for moderate moves.

- Used as the long leg in deep-ITM debit call spreads
- Used for stock replacement with [[long-dated-options|LEAPS]] (see [[leaps]])
- Captures dividend exposure differently than stock — see dividend-adjustments
- Lower vega than ATM, lower gamma — the position behaves more like delta-1 stock

## Probability of Profit (PoP) Calculation

[[probability-of-profit|PoP]] is the broker-quoted probability that a position closes at or above breakeven at expiration. For a single short option, PoP ≈ probability OTM ≈ |1 − delta|. For a credit spread, the breakeven is shifted by the credit received.

**Formula** (short put credit spread):

```
breakeven price = short strike − credit received
PoP ≈ 1 − P(underlying < breakeven at expiry)
```

**Worked example** — short 16-delta SPY put at 490 with $1.45 credit, on a 45 DTE expiration:

- Breakeven: $490 − $1.45 = $488.55
- The 488.55 strike has approximately a 14-delta in absolute value
- PoP ≈ 1 − 0.14 = **86%** (roughly)

Most broker platforms (TOS, tastytrade, IBKR) compute and display PoP directly using their own model — the numbers vary by 1-3% depending on whether they use Black-Scholes, binomial, or empirical bootstrap distributions.

## Probability of Touch

For OTM strikes, **probability of touch** (the chance the underlying touches the strike at *any* time before expiration) is approximately *2× probability of finishing ITM*.

- 16-delta strike: ~16% P(ITM at expiry), ~32% P(touch) before expiry
- 30-delta strike: ~30% P(ITM), ~60% P(touch)

This is the "rule of two" derived from reflection-principle properties of Brownian motion. It matters because traders who manage positions at the touch of a strike (rather than waiting for expiry) experience adversity at roughly twice the rate suggested by P(ITM). A 16-delta short put feels "84% safe" by P(ITM) but is touched by spot ~32% of the time before expiry — meaning the trader will face mark-to-market adversity on roughly one in three trades, even if most of those eventually recover and expire OTM.

## Picking Strikes by IV Rank Context

Strike selection should respond to [[iv-rank-and-iv-percentile|IVR]]:

| IVR | Short premium strikes | Long premium strikes |
|---|---|---|
| 0-20 | Skip — credit too small | Buy ATM (50d), credit cheap |
| 20-50 | 30-delta (tighter, larger credit) | ATM (50d) for balanced trades |
| 50-80 | 16-delta (standard) | Skip — vega too expensive |
| 80-100 | 10-delta (wider; collect fat credit at low gamma) | Skip — IV crush risk extreme |

The intuition: when IV is high, options are expensive — sell them, but go further OTM because the credit is fat enough to make wider strikes worth it. When IV is low, options are cheap — buy them, but stay near ATM because cheap OTM premium is a low-probability lottery ticket and you don't want to pay for vega that won't expand.

## Strike Selection by Strategy

Each major strategy has a canonical delta target.

### Cash-Secured Puts ([[cash-secured-puts]])

Sell a put at a strike where you'd be happy to be assigned the underlying.

- 30-delta — aggressive yield, ~30% chance of assignment
- 20-delta — balanced, ~20% chance of assignment
- 10-delta — conservative, mostly yield with tail-event assignment

Strike picked at a *price* the trader actually wants to own the stock at, not just at a delta target — this is the only major short-premium strategy where price-anchoring matters.

### Covered Calls ([[covered-calls]])

Sell a call at a strike where you're willing to part with the stock.

- 30-delta — aggressive yield, ~30% chance of being called
- 20-delta — balanced
- 10-delta — pure yield, rarely called

Strike often picked just above resistance levels (chart-based) blended with delta target, since the upside cap is real — being called at a strike is a real opportunity-cost decision.

### Iron Condors ([[iron-condors]])

Two credit spreads, one each side. Symmetric structure.

- Both shorts at 16-delta (standard) — ~64-70% PoP, balanced across IV regimes
- Both shorts at 20-delta — slightly tighter, larger credit
- Asymmetric (e.g., 16d call / 20d put) — used when the trader has a directional lean

### Debit Spreads (Bull Call / Bear Put)

Buy ATM, sell OTM. Net debit.

- Long leg at 50-delta (ATM)
- Short leg at 25-30-delta — captures meaningful credit to offset debit while keeping max-profit-to-debit ratio attractive
- For higher-conviction directional trades: long leg at 60-70 delta, short leg at 30-40 delta

### Strangles ([[short-strangle]])

Sell a put and a call simultaneously, both OTM.

- 16-delta both sides — standard
- 10-delta both sides — wide, for high-IVR environments

### Delta-target cheat sheet

A single table collapsing the canonical delta targets above. This expresses, in [[delta]] terms, the same choice that [[moneyness-selection]] frames in ITM/ATM/OTM terms.

| Strategy | Short-leg delta | Long-leg / protective delta | Anchor |
|---|---|---|---|
| Cash-secured put ([[cash-secured-puts]]) | 10-30d | n/a | Price you'd own the stock at |
| Covered call ([[covered-calls]]) | 10-30d | underlying stock | Price you'd sell the stock at |
| Iron condor ([[iron-condors]]) | 16d both sides | 5-10d wings | Symmetric P(OTM) |
| Bull/bear credit spread ([[credit-spread]]) | 16-30d | 5-10d | IVR-dependent |
| Debit spread (bull call / bear put) | 25-40d | 50-70d long | Conviction-dependent |
| Short strangle ([[short-strangle]]) | 10-16d both | n/a | IVR-dependent width |
| Stock replacement ([[leaps]]) | n/a | 70-90d long | Delta-1 behaviour |
| Tail hedge / portfolio insurance | n/a | 5-16d long put | Cheap convexity |

## Standard Deviation Move from IV

A practical strike-selection check: convert IV directly into expected move and verify the chosen strike is consistent.

**Formula** (simplified, lognormal):

```
1-sigma move = spot × IV × sqrt(DTE / 365)
```

**Example**: SPY at $510, IV (ATM, 45 DTE) = 16%.

- 1-sigma move = 510 × 0.16 × sqrt(45/365) = 510 × 0.16 × 0.351 = **$28.65**
- 1-sigma down = 510 − 28.65 = $481.35
- 1-sigma up = 510 + 28.65 = $538.65

The 16-delta short put on this expiration should be near $481 — which it is (the 480 strike will be ~17 delta, the 485 ~14 delta).

This sanity-check catches mispriced chains, skew anomalies, or input errors. If the 16-delta strike is much closer to spot than the 1-sigma calculation, the put-side IV is elevated (skew is steep) — signaling fear, and possibly a better selling opportunity than the IVR alone suggests.

## Skew and Strike Selection

Equity options exhibit a persistent **volatility skew**: OTM puts trade at higher IV than OTM calls of equivalent moneyness. A 16-delta SPY put will have a higher implied vol than a 16-delta SPY call — sometimes 5-10 vol points higher. Implications:

- 16-delta short puts pay disproportionately well versus 16-delta short calls (this is the equity-index "skew premium")
- The PoP on the put-side credit spread is *understated* by the model if it doesn't account for skew (puts have more downside drift implied)
- A symmetric strangle (16d call / 16d put) collects asymmetric credit, with the put paying more

Traders selling premium on indices systematically benefit from put-side skew — this is one of the structural reasons short-put-overlay strategies have positive long-run expected value (see [[volatility-risk-premium]], [[5-percent-otm-put-overlay]]).

## Selecting Strikes Around Earnings

Around earnings, strike-selection logic shifts:

- **IV term structure inverts**: front-month IV spikes above back-month IV (kink at the earnings date)
- **Implied earnings move** (implied-earnings-move) gives the market-implied straddle move; strikes outside the implied move have markedly different P(ITM) than non-earnings periods
- **Standard delta convention overstates safety**: a 16-delta pre-earnings put has higher gamma exposure to a single binary event than its delta suggests
- **Practical rule**: for premium selling around earnings, use the implied move boundary as the short-strike floor (e.g., short put strike at least 1× implied move below spot)

See earnings-announcement and [[iv-crush]] for the full event-volatility context.

## Worked Example — Selecting Strikes for a Put Credit Spread

A trader wants to sell premium on a neutral-to-bullish $200 stock, 45 DTE, with ATM [[implied-volatility|IV]] of 30% and [[iv-rank-and-iv-percentile|IVR]] of 65 (elevated — favourable for selling).

1. **Sanity-check the 1σ move.** `1σ = 200 × 0.30 × sqrt(45/365) = 200 × 0.30 × 0.351 ≈ $21`. The 1σ-down level is ~$179, which is where the ~16-delta put should sit.
2. **Pick the short strike by delta + IVR.** IVR 65 is in the 50-80 band, so the cheat-sheet default is a **16-delta short put** (~84% P(OTM)). The 180 strike lines up with the 1σ check — pick the **180 put**, collecting, say, $3.10.
3. **Pick the long strike (the wing).** A 5-wide spread → buy the **175 put** (~10-12 delta) for ~$2.10. Net credit ≈ **$1.00**; max loss ≈ $5.00 − $1.00 = $4.00.
4. **Compute breakeven and PoP.** Breakeven = 180 − 1.00 = **$179.00**. That breakeven strike is ~14-delta, so [[probability-of-profit|PoP]] ≈ 1 − 0.14 ≈ **86%**.
5. **Apply probability-of-touch.** The 180 short has ~32% P(touch), so the trader should expect mark-to-market adversity on roughly one trade in three — and pre-decide a management point (e.g., close at 50% max profit or roll at 2× credit tested).
6. **Check skew.** Equity put-side skew means the 180 put's IV exceeds the symmetric 220 call's IV by several vol points, so the put credit spread collects extra skew premium — a structural tailwind ([[volatility-risk-premium]]).
7. **Check for events.** Confirm there is no earnings-announcement inside the 45-DTE window. If there were, the trader would move the short strike at least 1× the implied-earnings-move below spot, or skip the trade.

The full loop: 1σ sanity-check → delta target by IVR → wing for defined risk → breakeven/PoP → touch-based management plan → skew/event overlay.

## Common Pitfalls

1. **Treating delta as exact probability.** |Delta| ≈ risk-neutral P(ITM), but skew, drift, and the risk-neutral-vs-physical gap make it an approximation — not a guarantee.
2. **Ignoring probability of touch.** A "16-delta, 84%-safe" short is touched ~32% of the time; traders who manage at the touch face adversity at double the P(ITM) rate.
3. **Using the same delta target across IV regimes.** In low IVR, go nearer ATM for long premium; in high IVR, go further OTM for short premium. A fixed 16-delta rule misprices both extremes.
4. **Selling fixed deltas through earnings.** A 16-delta pre-earnings put carries far more single-event gamma than its delta implies; use the implied-earnings-move boundary instead (see [[iv-crush]]).
5. **Symmetric strangles on skewed underlyings.** A 16d/16d strangle collects asymmetric credit — the put pays more because of [[volatility-risk-premium|skew]]; treat the two sides as different bets.
6. **Picking strikes with no liquidity.** Delta math is irrelevant if the strike can't be exited cleanly; pair strike picks with [[options-liquidity-screening]].

## Related

- [[delta]] — the dominant strike-selection metric
- [[gamma]] — peaks at ATM; informs how strikes behave under spot moves
- [[theta]] — decay rate, peaks at ATM in absolute dollars
- [[vega]] — IV sensitivity by strike
- [[iv-rank-and-iv-percentile]] — context that shifts the optimal delta target
- [[options-selection-framework]] — strike selection is filter 5 in the framework
- [[spread-width-selection]] — pairs with strike picks for credit spreads
- [[probability-of-profit]] — the broker-quoted version of the strike-by-delta math
- [[cash-secured-puts]], [[covered-calls]], [[iron-condors]], [[credit-spread]] — strategies with canonical delta targets
- [[volatility-risk-premium]] — structural reason the put-side strike collects skew premium
- [[moneyness-selection]] — the ITM/ATM/OTM framing of the same strike choice
- [[iv-crush]] — the post-event collapse that punishes event-spanning strikes

## Sources

- (Source: [[2026-04-22-gap-finder-stock-options-trading-pitfalls-tradesta]])
- Sheldon Natenberg, *Option Volatility and Pricing* — delta-as-probability, skew, and strike behaviour
- John C. Hull, *Options, Futures, and Other Derivatives* — Black-Scholes delta and probability of ITM
- tastytrade research — empirical basis for the 16-delta short-premium convention
