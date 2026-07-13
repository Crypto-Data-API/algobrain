---
title: "Risk-Free Rate"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [portfolio-theory, valuation, risk-management, bonds, treasuries]
aliases: ["Risk Free Rate", "Risk-Free Rate of Return", "Rf", "riskless rate"]
related: ["[[capital-asset-pricing-model]]", "[[sharpe-ratio]]", "[[treynor-ratio]]", "[[information-ratio]]", "[[us-treasury-bonds]]", "[[fed-funds-rate]]", "[[inflation]]", "[[opportunity-cost]]", "[[beta]]"]
domain: [portfolio-theory, valuation, risk-management]
prerequisites: ["[[us-treasury-bonds]]"]
difficulty: beginner
---

The **risk-free rate** is the theoretical rate of return an investor can earn on an investment that carries (essentially) zero risk of default — the baseline reward for simply parking capital with no credit risk. In practice it is proxied by the yield on short-term government debt of a stable issuer, most commonly the **U.S. Treasury bill** for USD-denominated analysis. It is the single most reused input in finance: nearly every valuation model, performance ratio, and asset-pricing framework starts from it.

## Overview

There is no truly risk-free asset — even a government can default, and an investor still bears inflation and reinvestment risk — so "risk-free" is an idealisation. The market convention is to use the most creditworthy, most liquid government security available in the relevant currency and to match its maturity to the horizon of the problem:

- **Short horizon / cash benchmark** → 3-month U.S. Treasury bill (T-bill) yield.
- **Equity valuation / DCF** → 10-year Treasury note yield, because equities are long-duration assets.
- **Long-dated liabilities (pensions, insurers)** → 20- or 30-year Treasury bond yield.

The rate quoted on these securities is a **nominal** rate: it includes expected [[inflation]]. Subtracting expected inflation gives the **real risk-free rate** (see [[nominal-vs-real-return]]). The risk-free rate is closely tethered to monetary policy — short-term yields track the central bank's policy rate (in the U.S., the [[fed-funds-rate]]).

## Why It Matters

The risk-free rate is the anchor against which every other return is measured:

1. **It is the floor on required return.** Any risky asset must be expected to return *more* than the risk-free rate, or a rational investor would simply hold the riskless asset. The extra return demanded is the **risk premium**.
2. **It sets the discount rate.** In DCF valuation and the weighted average cost of capital, the risk-free rate is the base to which equity and credit premiums are added. A higher risk-free rate mechanically lowers the present value of future cash flows — which is why rising Treasury yields tend to pressure long-duration growth-stock valuations.
3. **It defines excess return.** Performance ratios measure return *above* the risk-free rate. The [[sharpe-ratio]] uses (portfolio return − risk-free rate) ÷ volatility; the [[treynor-ratio]] and [[information-ratio]] are built on the same excess-return idea.
4. **It is a pillar of asset pricing.** In the [[capital-asset-pricing-model|CAPM]], expected return = risk-free rate + [[beta]] × (market return − risk-free rate). The risk-free rate appears twice and is the line's intercept.
5. **It frames [[opportunity-cost]].** When T-bills yield 5%, the hurdle for taking on any risk rises; when they yield near 0%, investors are pushed out the risk curve ("reach for yield").

## How It Is Used

- **CAPM / cost of equity:** plug the current 10-year Treasury yield in as Rf, then add beta-scaled equity risk premium.
- **Sharpe ratio:** subtract the T-bill yield from the strategy's return before dividing by volatility, so that a strategy is only credited for return *earned by taking risk*.
- **DCF discounting:** Rf is the foundation of the discount rate; analysts add an equity risk premium and company-specific premiums on top.
- **Cash drag and benchmarking:** the T-bill yield is the natural benchmark for a cash allocation and the "do nothing" alternative for any active bet.

A practical caution: the chosen proxy should match the currency and horizon of the cash flows being analysed. Using a 3-month T-bill rate to discount a 20-year cash-flow stream introduces a duration mismatch; using a U.S. rate to value euro-denominated cash flows introduces a currency mismatch.

## Choosing the proxy in practice

- **Currency dictates the benchmark.** USD analysis uses U.S. Treasuries; euro analysis conventionally uses German Bunds (the euro area's most creditworthy issuer); GBP uses UK Gilts; JPY uses JGBs. The point is to pick the *most default-remote, most liquid* sovereign in the relevant currency.
- **Overnight index rates for short-horizon and derivatives work.** In money markets and derivatives pricing, the reference "riskless" rate is increasingly an overnight-indexed benchmark such as **SOFR** (the Secured Overnight Financing Rate that replaced USD LIBOR) or the OIS curve, because it strips out the bank-credit and term premia embedded in older interbank rates. For equity valuation, however, the Treasury curve remains the standard.
- **The negative-rate problem.** Between roughly 2014 and 2022, several sovereigns (Germany, Japan, Switzerland) had *negative* short-term yields, which made a literal risk-free rate awkward in CAPM and Sharpe calculations. Practitioners variously floored Rf at zero, used a longer-maturity positive yield, or added a "normalized" risk-free rate — a reminder that Rf is a modelling convention, not a physical constant.
- **T-bills are the cleanest proxy for the pure riskless rate** because they carry negligible default risk and negligible duration risk; longer Treasuries add [[interest-rate-risk]] (price sensitivity to yield changes), which is why the maturity is matched to the horizon rather than always using the shortest bill.

## Hypothetical Example

Suppose 3-month Treasury bills yield **5.0%** and an investor is weighing a diversified equity portfolio expected to return **9.0%** with annual volatility of **16%**.

- The **excess return** over the risk-free rate is 9.0% − 5.0% = **4.0%** — this is the reward for bearing equity risk.
- The portfolio's **Sharpe ratio** is 4.0% ÷ 16% = **0.25** — modest, because much of the 9% is simply the risk-free rate the investor could have earned with no risk.

Now imagine the central bank cuts rates and T-bills fall to **1.0%**, while the equity expectation is unchanged at 9.0%. The excess return jumps to 8.0% and the Sharpe ratio to 0.50 — the *same* equity portfolio looks far more attractive purely because the riskless alternative pays less. This illustrates why falling risk-free rates tend to lift risk-asset valuations and why rising rates compress them. (Illustrative figures only — not a forecast.)

## Related

- [[capital-asset-pricing-model]] — risk-free rate is the CAPM intercept
- [[sharpe-ratio]], [[treynor-ratio]], [[information-ratio]] — all measure return above Rf
- [[us-treasury-bonds]] — the real-world proxy for the riskless asset
- [[fed-funds-rate]] — policy rate that drives short-term Rf
- [[inflation]], [[nominal-vs-real-return]] — real vs nominal risk-free rate
- [[opportunity-cost]] — Rf is the baseline alternative to any risky bet
- [[beta]] — scales the risk premium added to Rf in CAPM
- [[sofr]] — the overnight benchmark used as the riskless rate in derivatives pricing
- [[interest-rate-risk]] — why longer Treasuries are not a pure riskless proxy

## Sources

- Standard corporate-finance and investment texts (e.g., Bodie, Kane & Marcus, *Investments*; Damodaran, *Investment Valuation*) treat the risk-free rate as the base input to CAPM, DCF, and the Sharpe ratio. The proxy-selection and horizon-matching conventions described here are general, widely-taught market knowledge.
