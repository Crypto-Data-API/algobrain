---
title: "Black-Scholes Model (Crypto Options)"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, derivatives, quantitative, volatility, crypto]
aliases: ["Black-Scholes Model", "Black-Scholes-Merton", "BSM", "BSM Model", "Black-Scholes-Merton 1973", "Black-Scholes Equation", "Black-Scholes Formula", "Black-76"]
domain: [derivatives, options, quantitative]
prerequisites: ["[[black-scholes]]", "[[implied-volatility]]", "[[greeks]]", "[[options]]"]
difficulty: advanced
markets: [crypto, options]
related: ["[[black-scholes]]", "[[implied-volatility]]", "[[greeks]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[deribit]]", "[[dvol]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[volatility-skew]]", "[[options]]"]
---

The **Black-Scholes model** (Black-Scholes-Merton, 1973) is the closed-form framework for pricing European options, and it is the pricing engine underneath every crypto options venue — above all [[deribit|Deribit]], which clears roughly 85-90% of global crypto options volume. This page covers the model as it is *actually applied to crypto*: what changes when the option is European, cash-settled, and **inverse** (coin-denominated), when the "risk-free rate" is really a [[funding-rate|funding]]- and basis-implied forward, when the market trades 24/7, and when [[implied-volatility|implied vol]] is benchmarked by [[dvol|DVOL]] rather than the VIX. For the general derivation, history (Fischer Black, Myron Scholes, Robert Merton, and [[ed-thorp|Ed Thorp]]'s independent discovery), and the full list of theoretical limitations, see the canonical [[black-scholes]] page.

## The model in one paragraph

Black-Scholes assumes the underlying follows geometric Brownian motion with constant volatility, and that an option can be perfectly replicated by a continuously rebalanced portfolio of the underlying and a risk-free bond. No-arbitrage then forces the option price to equal the cost of that replicating portfolio, yielding a closed-form value. Every one of the [[greeks]] — [[delta]], [[gamma]], [[theta]], [[vega]], rho — is a partial derivative of that pricing function, which is why the model doubles as the risk-management language of options desks. The replication argument is also the theoretical justification for [[delta-hedging]] and [[gamma-scalping]].

## Inputs

Black-Scholes prices a European option from five inputs. The crypto reading of each differs from the equity textbook:

| Input | Symbol | Equity meaning | Crypto meaning |
|-------|--------|----------------|----------------|
| Spot | S | Stock price | BTC/ETH index price (Deribit uses its own composite index) |
| Strike | K | Strike | Strike, quoted in USD on Deribit |
| Time | T | Year fraction, often trading-day | **Calendar-time** year fraction — the market never closes |
| Rate | r | T-bill rate | **Cost of carry** implied by the futures/forward, driven by [[funding-rate|funding]] and basis, not a government rate |
| Volatility | σ | Annualized vol | Annualized vol; the market benchmark is [[dvol|DVOL]] |

The single most important crypto distinction is `r`. In equities the risk-free rate is a real, observable T-bill yield. In crypto there is no clean risk-free rate, so desks price off the **forward** implied by the term futures curve and the perpetual [[funding-rate]]. Practically this means crypto desks use the forward-based **Black-76** variant of the model: replace `S` with the forward `F = S·e^{rT}` and price off `F` directly. Deribit itself marks options against the forward derived from its own futures, so the "rate" you back out of crypto option prices is a market-clearing carry number, not a macro rate — and it moves with funding.

## The formula

For a European call (spot form):

> C = S·N(d1) − K·e^(−rT)·N(d2)

For a European put:

> P = K·e^(−rT)·N(−d2) − S·N(−d1)

with

> d1 = [ln(S/K) + (r + σ²/2)·T] / (σ·√T)
> d2 = d1 − σ·√T

and N(·) the cumulative standard normal. N(d2) is the risk-neutral probability the call finishes in the money; N(d1) is the option's [[delta]]. In the forward (Black-76) form used on crypto desks, substitute the forward `F` and discount the whole payoff: `C = e^(−rT)·[F·N(d1) − K·N(d2)]` with `d1 = [ln(F/K) + (σ²/2)T]/(σ√T)`.

### ATM approximations (useful on Deribit)

For a near-ATM option with small `rT`, the practitioner shortcuts are exact enough for sizing:

> ATM call ≈ 0.4 · S · σ · √T
> ATM straddle ≈ 0.8 · S · σ · √T ≈ the market-implied expected move

These are the fastest way to sanity-check a Deribit quote or to translate [[dvol|DVOL]] into an expected BTC move (see worked example below).

## The Greeks and their behaviour

The Greeks are the derivatives of the BSM price and govern how a crypto option position must be hedged:

| Greek | Definition | Behaviour |
|-------|-----------|-----------|
| [[delta]] (Δ) | ∂C/∂S = N(d1) for a call | 0→1 for calls, 0→−1 for puts; ≈0.5 ATM. The share/coin quantity to hedge |
| [[gamma]] (Γ) | ∂²C/∂S² | Peaks ATM, explodes near expiry; the convexity [[gamma-scalping|gamma scalpers]] monetise |
| [[theta]] (Θ) | −∂C/∂T | Time-decay; accelerates near expiry; the rent short-vol collects |
| [[vega]] (ν) | ∂C/∂σ | Largest for longer-dated ATM options; the [[dvol|DVOL]] sensitivity |
| rho (ρ) | ∂C/∂r | Sensitivity to carry — in crypto, sensitivity to funding/basis, larger than most assume |

Because BSM gives all Greeks in closed form, a desk can compute a live risk book from the surface in real time. Two second-order Greeks — **vanna** (∂Δ/∂σ) and **volga** (∂ν/∂σ) — matter more in crypto than equities because the crypto vol surface moves violently and the skew flips sign around large moves.

## Implied volatility, DVOL and the surface

The model takes σ as an input, but traders run it backwards: given a market option price, solve for the σ that reproduces it. That number is [[implied-volatility]], and it is the real output of Black-Scholes in practice. Plotting BSM-implied vol across strikes and expiries builds the **[[volatility-surface|vol surface]]**, whose two features — the [[volatility-skew|skew]] across strikes and the term structure across expiries — encode the market's fear and expectations.

The crypto benchmark distilled from that surface is **[[dvol|DVOL]]**, Deribit's 30-day forward implied-vol index for BTC and ETH — the "VIX of crypto." DVOL is computed from Deribit's BSM-implied vols and is the number crypto vol traders quote. Note that DVOL and the full IV surface are **not** available through CryptoDataAPI — they come from Deribit directly (and aggregators such as Greeks.live / Amberdata).

## Assumptions — and why they break harder in crypto

Every BSM assumption is violated in real markets, but crypto violates them *more*:

- **Constant volatility** — crypto vol is wildly stochastic; DVOL routinely swings 40→100%+ around events (COVID March 2020, LUNA, FTX). Stochastic-vol models (Heston, SABR) fit the crypto surface better than flat BSM.
- **Log-normal, continuous paths** — crypto has fatter tails and more frequent gaps than equities, and it gaps *on weekends* while TradFi is closed. Jump-diffusion adjustments are more necessary.
- **No skew** — flat BSM predicts one vol for all strikes; the crypto surface shows a pronounced skew that historically favours OTM *calls* in bull phases (the opposite of the persistent equity put skew) and flips to put skew in stress. See [[volatility-skew]].
- **Frictionless continuous hedging** — hedging a crypto option means trading spot or [[perpetual-futures|perps]], paying funding and wider spreads, so real prices carry a hedging-cost premium over theoretical value (see [[delta-hedging]]).
- **Clean risk-free rate** — as noted, there isn't one; the carry input is funding/basis-driven and itself volatile.

Despite this, BSM remains the universal starting point: it is "wrong but useful," the shared coordinate system in which every crypto desk quotes vol and computes Greeks.

## Worked example (BTC)

BTC index at **$60,000**, a **30-day** ATM call, DVOL (≈ our σ) at **55%**, carry ≈ 0. Using the ATM approximation:

- Call ≈ 0.4 · 60,000 · 0.55 · √(30/365) = 0.4 · 60,000 · 0.55 · 0.2866 ≈ **$3,783** (≈ 0.063 BTC).
- Straddle ≈ 0.8 · 60,000 · 0.55 · 0.2866 ≈ **$7,566**, i.e. the market is pricing a ±~12.6% move over 30 days.

Now the crypto twist: on Deribit this call is **inverse** — quoted and settled in BTC (~0.063 BTC). If BTC rallies to $66,000, the option gains value *and* the 0.063 BTC premium is itself worth more in USD. That coupling — the payoff currency moving with the underlying — is the inverse-contract adjustment that flat USD BSM does not capture on its own (next section). If instead this were priced with DVOL at 90% (a stress regime), the same 30-day straddle would imply a ±~20.6% move, showing how directly the vol input drives crypto option cost.

## Crypto specifics

### Deribit conventions

- **European, cash-settled** options on BTC and ETH — no early exercise, so plain BSM (not a binomial/American model) is the correct pricer. Settlement is to Deribit's index at expiry.
- **Expiries** at **08:00 UTC**: daily, weekly (Fridays), monthly, and quarterly (last Friday of Mar/Jun/Sep/Dec). See [[weekly-options]].
- **Quoting**: premium is shown in the base coin (BTC/ETH) as well as USD; margin, collateral and P&L are coin-denominated on inverse contracts.
- Deribit publishes its own mark IV per instrument and the DVOL index; these are the de facto crypto vol benchmarks.

### Inverse vs linear settlement — the effect on price and Greeks

This is the crypto-specific heart of the matter. A **linear** (USD-margined) option pays off in USD, exactly like the equity textbook, and BSM applies directly. An **inverse** (coin-margined) option — the Deribit standard — pays off in the *coin*, so the payoff currency is itself the risky asset. Consequences:

- The USD value of an inverse call has extra convexity: as spot rises, the option's coin value and the coin's USD value both rise, so the **effective USD delta of an inverse call is higher** than the naive BSM delta, and an inverse put's is lower in magnitude. This is a quanto-like adjustment; desks convert Deribit's coin-Greeks to "cash Greeks" before hedging in USD terms.
- Collateral is self-reinforcing on the downside: a falling coin simultaneously shrinks your margin *and* worsens short-put positions, amplifying [[liquidation]] cascades (see the [[deribit]] page). Position sizing must model collateral value and directional exposure jointly.
- Practical rule: never hedge an inverse option using the raw BSM delta Deribit displays in coin terms without first translating to USD/cash delta, or the hedge will be systematically mis-sized.

### Perpetual-funding and basis as the "rate"

Because the carry input `r` is set by the futures/[[funding-rate|funding]] market, changes in perpetual funding and term basis move option prices through rho and shift the forward the whole surface is struck against. When funding is deeply positive (crowded longs), forwards trade rich, lifting call values and steepening call skew; when funding flips negative in a sell-off, the forward and skew swing the other way. A crypto BSM user therefore watches funding and basis as *pricing inputs*, not just as a separate carry trade (see [[cash-and-carry]]).

### 24/7, calendar time, and weekend gaps

- Crypto never closes, so `T` is **calendar-time** year fraction and [[theta]] accrues continuously — including weekends, unlike equity conventions that sometimes discount non-trading days.
- Because the market trades through catalysts (FOMC, CPI, ETF decisions, [[bitcoin-halving|halving]]), there is no overnight "gap" the way equities gap over a closed session — vol resolves live. But weekend liquidity is thin, so realized moves can be jumpy exactly when hedging is hardest, stressing the continuous-hedging assumption.
- Deribit's 08:00 UTC expiry and the concentration of open interest on a single venue mean BSM-implied [[max-pain|max-pain]] and dealer [[gamma-exposure|gamma]] effects are amplified around expiry relative to fragmented equity markets.

## Getting the Data (CryptoDataAPI)

Black-Scholes needs a volatility input and a carry input. CryptoDataAPI supplies proxies and positioning context, though the **IV surface and DVOL itself come from Deribit / Greeks.live, not CryptoDataAPI**:

- **Volatility regime** (RV/IV context for σ) — `GET /api/v1/volatility/regime` and market-wide `GET /api/v1/volatility/regime/score`. See [[cryptodataapi-regimes]].
- **Options positioning / max pain** — `GET /api/v1/market-intelligence/options` (BTC options OI, volume, max pain). See [[cryptodataapi-market-intelligence]].
- **Carry input (funding/basis for `r`)** — `GET /api/v1/derivatives/funding-rates?coin=BTC` and `GET /api/v1/derivatives/open-interest`. See [[cryptodataapi-derivatives]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

## Related

- [[black-scholes]] — canonical general model, derivation, history, and limitations
- [[implied-volatility]] — the model's real output; solved for from market prices
- [[dvol|DVOL]] — Deribit's 30-day IV index, the crypto vol benchmark (Deribit/Greeks.live)
- [[greeks]] — the partial derivatives BSM provides in closed form
- [[delta]], [[gamma]], [[theta]], [[vega]] — the individual Greeks
- [[delta-hedging]] — the replication argument put into practice
- [[gamma-scalping]] — monetising BSM gamma when realized vol beats implied
- [[volatility-skew]], [[volatility-surface]] — where flat BSM fails and the market speaks
- [[deribit]] — the venue where crypto BSM is priced; inverse contracts and DVOL
- [[perpetual-futures]], [[funding-rate]] — the source of the crypto carry input
- [[max-pain]], [[gamma-exposure]] — expiry effects amplified on Deribit

## Sources

- Black, F. & Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy*
- Black, F. (1976), "The Pricing of Commodity Contracts" — the forward-based variant crypto desks use
- [[book-option-volatility-and-pricing]] — Natenberg's practical treatment of BSM as a trading tool
- Deribit public documentation — inverse contract specs, mark IV, and DVOL methodology
- [[deribit]] — wiki entity page synthesizing crypto options conventions
