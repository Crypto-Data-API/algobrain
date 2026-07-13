---
title: "Volatility Smile"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [options, derivatives, volatility, indicators]
aliases: ["Volatility Smile", "Vol Smile", "Implied Volatility Smile"]
related: ["[[implied-volatility]]", "[[options-pricing]]", "[[black-scholes]]", "[[volatility-skew]]", "[[options]]", "[[volatility-surface]]", "[[tail-risk]]", "[[stochastic-volatility]]", "[[the-greeks]]", "[[put-call-parity]]"]
domain: [indicators, derivatives]
prerequisites: ["[[implied-volatility]]", "[[black-scholes]]"]
difficulty: advanced
---

The volatility smile is a pattern observed when plotting [[implied-volatility]] (IV) against strike price for [[options]] of the same expiration: out-of-the-money (OTM) puts and OTM calls both exhibit higher implied volatility than at-the-money (ATM) options, creating a U-shaped or "smile" curve. This pattern directly contradicts the [[black-scholes]] model, which assumes constant volatility across all strikes and would predict a flat line. The smile reveals that the market prices in a higher probability of extreme moves (fat tails) than a log-normal distribution assumes.

## Why It Violates Flat-Vol Black-Scholes

[[black-scholes|Black-Scholes]] assumes the underlying follows geometric Brownian motion with a **single, constant volatility σ** — so every option on the same underlying and expiry should imply the *same* σ regardless of strike, producing a flat line. In reality, when you invert market prices to back out [[implied-volatility|IV]] strike-by-strike (the only Black-Scholes input not directly observable), the recovered σ is *not* constant — it bends upward at the wings. The smile is therefore best understood as **the market's correction to a wrong model assumption**: rather than re-deriving a new pricing model on the fly, traders keep Black-Scholes as a quoting convention and bend σ across strikes to make the formula reproduce observed prices. The shape of that bend encodes the market's true (non-log-normal, fat-tailed, skewed) belief about the return distribution.

### Worked Example — Reading a Smile/Skew

A single-expiry IV curve for an equity index (illustrative numbers) might look like:

| Strike (% of spot) | Moneyness | Implied volatility |
|---|---|---|
| 85% | deep OTM put | 30% |
| 90% | OTM put | 25% |
| 95% | near-money put | 21% |
| 100% | ATM | 18% |
| 105% | OTM call | 17% |
| 110% | deep OTM call | 18% |

Here the left wing (downside puts) is much higher than the right wing (upside calls): 30% vs 18%. That asymmetry is the **equity skew** ("smirk") — the curve is not a symmetric smile but a downward-sloping line that turns up only slightly on the call side. The market is charging a large premium for downside crash protection and relatively little for upside, exactly the opposite of what flat-vol Black-Scholes assumes. (Illustrative numbers only.)

## Historical Context

Before the 1987 stock market crash ("Black Monday"), equity option implied volatilities were relatively flat across strikes, broadly consistent with Black-Scholes assumptions. After October 19, 1987 -- when the S&P 500 fell 20.5% in a single day -- the smile (and more specifically, the [[volatility-skew|skew]]) appeared and has persisted ever since. Traders and market makers permanently adjusted their pricing to reflect the reality that catastrophic downside moves occur far more frequently than Gaussian models predict. The 1987 crash was an event that a log-normal model would assign a probability of roughly 10^(-160) -- essentially impossible -- yet it happened.

## Smile vs. Skew (by Asset Class)

The terminology can be confusing because the shape of the IV curve varies by asset class:

| Asset class | Typical shape | Why |
|---|---|---|
| Equity index (S&P 500) | Downward [[volatility-skew\|skew / smirk]] — OTM puts ≫ ATM ≫ OTM calls | Crash risk is one-directional (down); persistent demand for put protection, supply of covered calls |
| Individual stocks | Skew, but flatter; can flip to call-skew on takeover/squeeze names | Idiosyncratic upside (M&A, short squeezes) can lift call IV |
| FX | More symmetric smile | Currencies can gap large in either direction (devaluation, intervention) |
| Commodities | Often reverse skew — OTM calls ≫ OTM puts | Supply shocks spike prices *up* (oil, grains, natural gas) |
| Crypto | Variable; frequently call-skewed in bull phases | Demand for upside leverage in euphoric regimes |

- **Equity index options** typically show a [[volatility-skew|skew]] rather than a symmetric smile: OTM puts have much higher IV than ATM options, while OTM calls have slightly lower or similar IV. This reflects demand for downside protection and the asymmetric nature of equity crashes (markets crash down, not up).
- **FX options** tend to show a more symmetric smile, since currencies can make large moves in either direction.
- **Commodity options** often show a reverse skew (OTM calls have higher IV than OTM puts) for commodities prone to supply-driven spikes.
- **Individual stock options** can show either pattern depending on the name and market conditions.

## What the Smile Tells Us

### Fat Tails and Tail Risk

The smile reflects the market's empirical observation that financial returns have fatter tails than a normal distribution predicts. The excess IV at extreme strikes represents a premium for [[tail-risk|tail risk]] -- the risk of rare but severe price moves. A 25-delta put on the S&P 500 might carry 25% implied volatility while the ATM option shows 18%, indicating the market prices a meaningfully higher probability of a large down move than Black-Scholes would imply.

### Supply and Demand

The smile is partly driven by supply and demand dynamics in the options market. Institutional investors are natural buyers of OTM puts (for portfolio protection), while structured product issuers are natural sellers of OTM calls (through covered call overwriting). This persistent order flow imbalance inflates put IV and can suppress call IV, contributing to the skewed shape.

### Stochastic Volatility and Jumps

The smile can be explained theoretically by relaxing Black-Scholes assumptions. Models that incorporate stochastic volatility (e.g., the Heston model, where volatility itself is random) or jump-diffusion processes (e.g., the Merton jump-diffusion model, where prices can gap discontinuously) produce option prices consistent with the observed smile. These models have additional parameters calibrated to fit the market's smile surface.

## Term Structure and the Volatility Surface

A single smile is only one **slice** — it fixes the expiration and varies the strike. Two extensions complete the picture:

- **Term structure of volatility** holds *moneyness* roughly fixed (e.g. ATM) and varies *expiration*. In calm markets it usually slopes upward (longer-dated options carry higher IV, mean-reverting toward a long-run average — *contango*); in stress it inverts, with near-dated IV spiking above long-dated (*backwardation*) as the market prices an imminent shock.
- **The [[volatility-surface|volatility surface]]** is the full 3-D object: implied volatility as a function of *both* strike (or moneyness/delta) *and* time to expiration. Each constant-expiry cut is a smile/skew; each constant-strike cut is a term-structure curve.

| Axis | Holds fixed | Varies | Captures |
|---|---|---|---|
| Smile / skew | Expiration | Strike (moneyness) | Strike-dependent IV; fat tails, crash skew |
| Term structure | Strike / moneyness | Expiration | Time-dependent IV; calm vs. stress regimes |
| Vol surface | nothing | Strike *and* expiration | The complete IV(strike, T) map desks calibrate to |

Market-making desks calibrate their models (local-vol, [[stochastic-volatility|stochastic-vol]], SABR) to the *entire* surface so that every quoted option is consistent — both across strikes (no [[put-call-parity|parity]] violations or static-arbitrage along a smile) and across expirations (no calendar arbitrage). The surface, not any single number, is the trading desk's true model of volatility.

## Trading the Smile

- **Risk reversals**: Selling an OTM put and buying an OTM call (or vice versa) is a direct bet on the shape of the smile. If a trader believes put skew is excessive, selling the high-IV put and buying the lower-IV call captures the difference if the skew flattens.
- **Butterfly spreads**: A butterfly spread constructed across strikes profits from the curvature of the smile. If the smile is steeper than the trader expects realised volatility to justify, selling the wings (OTM puts and calls) via butterflies can be profitable.
- **Volatility surface arbitrage**: Sophisticated desks trade mispricings across the entire [[volatility-surface|volatility surface]] (strikes and expirations), using models calibrated to the current smile to identify options that are relatively cheap or expensive.

## Common Pitfalls

- **Treating high-wing IV as "overpriced."** A steep skew is not free money — it reflects genuine [[tail-risk|tail risk]]. Selling the high-IV put wing repeatedly earns a premium most of the time and then suffers a large loss in the crash it was insuring against (the classic short-vol blow-up).
- **Ignoring [[the-greeks|vega]] and skew exposure.** A position can be vega-neutral overall yet heavily exposed to a *change in the shape* of the smile (skew/convexity); risk-reversal and butterfly P&L is dominated by these higher-order vol Greeks (vanna, volga).
- **Confusing the IV number with a forecast.** IV from the smile is a *risk-neutral, supply/demand-laden* quantity, not a pure probability forecast; the gap between it and realized vol is the [[volatility-risk-premium|volatility risk premium]], not a free signal.
- **Static-arbitrage violations from sloppy interpolation.** Fitting a smile naively (e.g. cubic splines) can produce strikes that imply negative probability density or [[put-call-parity|parity]] breaks; practitioners use arbitrage-free parameterizations (SVI, SABR).

## Related

- [[implied-volatility]] -- the y-axis of the smile plot
- [[options-pricing]] -- the broader framework within which the smile exists
- [[black-scholes]] -- the model whose assumptions the smile violates
- [[volatility-skew]] -- the asymmetric version of the smile, dominant in equity markets
- [[the-greeks]] -- vega and skew Greeks govern smile-trading P&L
- [[put-call-parity]] -- ties same-strike call/put IV together; constrains the smile
- [[tail-risk]] -- the economic phenomenon the smile reflects
- [[volatility-surface]] -- the full strike-and-expiration object the smile is a single-expiration slice of
- [[stochastic-volatility]] -- the model family (Heston, SABR) that reproduces the smile

## Sources

- Hull, J. (2017). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. Standard textbook treatment of the volatility smile, smile vs skew by asset class, and the stochastic-volatility/jump explanations.
- Derman, E. and Kani, I. (1994). *Riding on a Smile*. RISK 7(2). Local-volatility model fitting the observed smile.
- Heston, S. (1993). *A Closed-Form Solution for Options with Stochastic Volatility*. Review of Financial Studies 6(2). The stochastic-volatility model that reproduces smile curvature.
- Merton, R. (1976). *Option Pricing When Underlying Stock Returns Are Discontinuous*. Journal of Financial Economics 3(1-2). Jump-diffusion model explaining fat tails and smile.
- Natenberg, S. (1994). *Option Volatility and Pricing*. McGraw-Hill. Practitioner treatment of the smile and trading it via risk reversals and butterflies.
