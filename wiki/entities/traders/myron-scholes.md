---
title: "Myron Scholes"
type: entity
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [person, options, derivatives, risk-management, history]
aliases: ["Myron S. Scholes"]
entity_type: person
founded: 1941
headquarters: "Stanford, California, USA"
related: ["[[fischer-black]]", "[[robert-merton]]", "[[black-scholes]]", "[[ltcm]]", "[[john-meriwether]]", "[[options-greeks]]", "[[the-greeks]]", "[[options]]", "[[implied-volatility]]", "[[model-risk]]", "[[book-when-genius-failed]]", "[[book-my-life-as-a-quant]]"]
---

Myron Scholes is a Canadian-American financial economist who, with [[fischer-black]], derived the **Black-Scholes options pricing formula** in 1973. Scholes shared the 1997 Nobel Prize in Economic Sciences (with [[robert-merton]]) for the work; Black, who had died in 1995, would have been a co-recipient. Scholes is also notable as a founding partner of [[ltcm|Long-Term Capital Management]], which made him simultaneously one of the most celebrated and one of the most cautionary figures in modern finance.

## Key Facts

| Field | Detail |
|---|---|
| Full name | Myron Samuel Scholes |
| Born | 1 July 1941, Timmins, Ontario, Canada |
| Citizenship | Canadian-American |
| Education | BA economics (McMaster); MBA and PhD (University of Chicago, under Eugene Fama and Merton Miller) |
| Era | The quantitative-finance revolution, 1970s–present |
| Known for | Co-author of the [[black-scholes\|Black-Scholes]] option-pricing formula (1973) |
| Major honour | 1997 Nobel Memorial Prize in Economic Sciences (shared with [[robert-merton]]) |
| Notable affiliations | Co-founding partner of [[ltcm\|Long-Term Capital Management]]; co-founder of Platinum Grove Asset Management |
| Current role | Chief Investment Strategist, Janus Henderson; Frank E. Buck Professor of Finance, Emeritus, Stanford GSB |

## Academic Career

Scholes earned his PhD at the University of Chicago under Eugene Fama and Merton Miller, and held faculty positions at MIT Sloan, Chicago, and Stanford. With Fischer Black at MIT in the early 1970s, he developed the closed-form solution for the price of a European option that had eluded generations of mathematicians and economists. The **Black-Scholes equation** (Source: [[book-my-life-as-a-quant]]) became the foundation of the modern derivatives industry — by some accounts, the single most consequential equation in finance.

Beyond Black-Scholes, Scholes contributed to:

- The **dividend irrelevance** debate alongside Miller
- Empirical asset pricing tests of the [[capm|Capital Asset Pricing Model]]
- **Tax considerations** in capital structure and trading
- The economics of incentive compensation

## What the Black-Scholes Formula Actually Says

The breakthrough Scholes and [[fischer-black]] achieved (with [[robert-merton]] providing a parallel continuous-time derivation) was to price a [[options|European option]] **without forecasting the direction of the stock**. The argument: a continuously rebalanced portfolio of the underlying stock and a risk-free bond can exactly **replicate** the option's payoff; by no-arbitrage, the option must cost the same as that replicating portfolio. Because the hedge cancels out market direction, the stock's expected return drops out of the equation entirely — only five inputs remain:

1. **Underlying price** (S)
2. **Strike price** (K)
3. **Time to expiry** (T)
4. **Risk-free interest rate** (r)
5. **Volatility** (σ) — the only input not directly observable

Volatility is the crux: four inputs are known, so an option's market price effectively reveals the market's view of σ — the [[implied-volatility]] that traders watch and trade. The model's sensitivities to each input are [[the-greeks]] (delta, gamma, vega, theta, rho), the everyday language of every [[options-greeks|options desk]]. Black-Scholes turned options from an arcane, intuition-priced instrument into a quantitatively managed, hedgeable product, and is widely credited with enabling the explosive growth of the CBOE (which opened the same year, 1973) and the global derivatives industry.

### Known limitations

The model assumes constant volatility, log-normally distributed returns, no jumps, continuous frictionless hedging, and a single expiry. Real markets violate all of these, which is why traders quote a **[[volatility-skew]]** (out-of-the-money puts trade at higher implied vol than the model would imply) and adjust outputs across the [[implied-volatility]] surface. The formula is a coordinate system for thinking about options risk, not a literal description of price dynamics — a point Scholes himself stressed after LTCM.

## LTCM and Its Collapse

In 1994, Scholes joined [[john-meriwether]] as a founding partner of [[ltcm|Long-Term Capital Management]]. Alongside [[robert-merton]], he provided the academic credibility and modeling expertise that made LTCM both feared by competitors and trusted by lenders. The fund posted exceptional returns from 1994–1997 trading [[convergence-arbitrage]] strategies under heavy [[leverage]].

In **August–September 1998**, after Russia's default, LTCM's models — built largely on Gaussian assumptions and historical correlations — failed catastrophically. The fund lost $4.6 billion in weeks and required a Fed-orchestrated bailout (Source: [[book-when-genius-failed]]). The episode is widely cited as the canonical example of [[model-risk]]: brilliant theoretical models can underestimate the magnitude of crisis-driven moves and the disappearance of [[liquidity]].

## After LTCM

Scholes co-founded **Platinum Grove Asset Management** in 1999, which pursued similar fixed-income relative-value strategies. Platinum Grove suffered heavy losses during the 2008 financial crisis (its main fund fell ~29% in October 2008 and briefly suspended withdrawals) and was subsequently wound down.

**Current status (verified June 2026)**: Scholes, born July 1, 1941 in Timmins, Ontario, serves as **Chief Investment Strategist at Janus Henderson Investors**, where he leads asset-allocation product development and contributes macro insights and quantitative analysis on hedging, risk management, and portfolio construction as part of the firm's Solutions Group. He joined Janus Capital in 2014 (chief investment strategist following the 2017 Janus–Henderson merger) and remains the **Frank E. Buck Professor of Finance, Emeritus, at the Stanford Graduate School of Business**. He continues to lecture publicly on option-implied information, tail-risk management, and "compound return" investing.

## Legacy

The Black-Scholes formula remains the standard pricing benchmark for vanilla options worldwide, even though traders routinely adjust its outputs via [[implied-volatility]] surfaces and [[volatility-skew]] to compensate for its known limitations (constant volatility, log-normal returns, no jumps). Scholes himself has spent much of his post-LTCM career emphasizing the importance of liquidity premia and tail risks that the original model omits.

Scholes's career arc — Nobel-winning theorist, hedge-fund star, blow-up survivor, lecturer on risk — encapsulates the central tension of quantitative finance: theoretically elegant models are powerful but never complete, and leverage applied to incomplete models is dangerous.

## Related

- [[fischer-black]]
- [[robert-merton]]
- [[black-scholes]] · [[options]] · [[the-greeks]] · [[options-greeks]]
- [[implied-volatility]] · [[volatility-skew]]
- [[ltcm]] · [[when-genius-failed]]
- [[john-meriwether]]
- [[model-risk]] · [[leverage]] · [[liquidity]]
- [[convergence-arbitrage]]

## Sources

- (Source: [[book-when-genius-failed]]) — Lowenstein on Scholes's role at LTCM and the limits of academic modeling
- (Source: [[book-my-life-as-a-quant]]) — Emanuel Derman's first-hand recollections of Scholes, Black, and the academic-Wall Street pipeline
- Fischer Black & Myron Scholes, "The Pricing of Options and Corporate Liabilities," *Journal of Political Economy* 81(3), 1973 — the original Black-Scholes paper
- Nobel Prize 1997 (Merton & Scholes): https://www.nobelprize.org/prizes/economic-sciences/1997/scholes/facts/
- Janus Henderson bio (confirms current Chief Investment Strategist role and Stanford emeritus title): https://www.janushenderson.com/en-us/investor/bio/myron-scholes-phd/
- Verified via Perplexity (sonar) + web search, 2026-06-10
