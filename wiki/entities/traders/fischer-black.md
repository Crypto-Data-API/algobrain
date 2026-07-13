---
title: "Fischer Black"
type: entity
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [person, options, derivatives, history]
aliases: ["Fischer Sheffey Black"]
entity_type: person
founded: 1938
headquarters: "Cambridge, Massachusetts, USA"
related: ["[[myron-scholes]]", "[[robert-merton]]", "[[black-scholes]]", "[[options-greeks]]", "[[book-my-life-as-a-quant]]"]
---

Fischer Black (January 11, 1938 – August 30, 1995) was an American economist and derivatives pioneer who, with [[myron-scholes]], derived the **[[black-scholes|Black-Scholes options pricing formula]]** in 1973. Black died of throat cancer in August 1995, two years before the Nobel committee awarded the prize for the work — Nobels are not awarded posthumously, so only Scholes and [[robert-merton]] received it, though the citation explicitly named Black. He is considered one of the most original financial thinkers of the 20th century and one of the few academics whose work transformed both finance theory and Wall Street practice.

## Key Facts

| Field | Detail |
|-------|--------|
| Lived | January 11, 1938 – August 30, 1995 (Washington, D.C. — died of throat cancer) |
| Education | A.B. physics, Harvard (1959); Ph.D. applied mathematics, Harvard (1964, on artificial intelligence) |
| Known for | Co-creator of the [[black-scholes\|Black-Scholes(-Merton)]] option-pricing model (1973); [[black-litterman\|Black-Litterman]] (1991); Black-Derman-Toy (1990); "Noise" (1986) |
| Collaborators | [[myron-scholes]], [[robert-merton]], [[jack-treynor]], [[emanuel-derman]], Bill Toy, Robert Litterman |
| Academic posts | University of Chicago (1971–75); MIT Sloan (1975–84) |
| Wall Street | Partner, goldman-sachs (1984–95), quantitative strategies group |
| Nobel | Ineligible (died 1995; prize awarded 1997) — Nobels are not posthumous; citation named him |
| Honors | AFA President (1985); biennial Fischer Black Prize (est. 2002); MIT Fischer Black Professorship |

## Early Career

Black trained in physics and mathematics at Harvard (AB 1959), then earned a Harvard PhD in applied mathematics (1964) with a dissertation on artificial intelligence. He worked at Arthur D. Little as a consultant, where he met [[jack-treynor]], who introduced him to capital asset pricing theory. Before joining Goldman he held professorships at the University of Chicago (1971–1975) and MIT Sloan (1975–1984). Black moved into finance from a non-economics background — a fact reflected in his unusual style: he prized clarity, distrusted complicated models, and often took contrarian positions on consensus theories.

## Black-Scholes (1973)

In the late 1960s and early 1970s, Black collaborated with [[myron-scholes]] (then at MIT Sloan) on the problem of pricing stock options. They derived a closed-form solution under the assumptions of log-normal stock returns, constant [[volatility]], and no arbitrage. Their paper, *"The Pricing of Options and Corporate Liabilities"*, was rejected by several journals before being published in the *Journal of Political Economy* in 1973 — the same year the [[cboe|Chicago Board Options Exchange]] opened and made the formula immediately operational. Within years, traders on the floor were using Black-Scholes-derived sheets to quote prices.

Robert Merton's parallel work the same year extended the result; the trio's frameworks together became the foundation of the modern derivatives industry.

### Why the model worked — the mechanics

The conceptual breakthrough was the **replicating portfolio** (dynamic delta-hedging argument). Black and Scholes showed that an option's payoff can be exactly reproduced by continuously holding a position in the underlying stock plus borrowing/lending at the risk-free rate, with the stock weight equal to the option's **delta**. If a portfolio that perfectly replicates the option exists, then by no-arbitrage the option must cost exactly what that portfolio costs — and crucially the stock's *expected return drops out* of the pricing equation, leaving the price a function only of the spot, strike, time, risk-free rate, and [[volatility]]. This reduces option valuation to estimating a single unobservable input, volatility, which is why option markets are quoted and traded in **[[implied-volatility|implied-vol]]** terms to this day. The hedge sensitivities of the formula — the [[options-greeks|"Greeks"]] (delta, gamma, theta, vega, rho) — became the standard risk language of every derivatives desk. The model's known failure (it assumes constant volatility, but markets price tail risk more richly for deep out-of-the-money options) shows up as the [[volatility-smile|volatility smile/skew]], the most studied departure from Black-Scholes and a primary source of [[model-risk]].

## Goldman Sachs (1984–1995)

In 1984, Black left academia (then a faculty member at MIT Sloan) to join Goldman Sachs as a partner in its quantitative strategies group. This was unusual for a senior academic at the time, and his move helped legitimize the academic-to-Wall-Street pipeline. At Goldman he worked on:

- **Quantitative trading and risk management** systems
- **Black-Derman-Toy** (1990, with [[emanuel-derman|Emanuel Derman]] and Bill Toy) — a one-factor short-rate model that calibrates to the observed yield curve and volatility term structure, widely used by fixed-income desks to price interest-rate options and callable bonds
- **[[black-litterman|Black-Litterman]]** (1991, with Robert Litterman) — a portfolio optimization framework that blends equilibrium returns with investor views
- Practical trading applications of theoretical models

### Black-Litterman: fixing mean-variance optimization

Naive [[modern-portfolio-theory|Markowitz mean-variance optimization]] is notoriously unusable in practice: it is hypersensitive to the expected-return inputs, so tiny changes in forecasts produce wildly different, extreme, and frequently unintuitive (large long/short) allocations. Black and Litterman's fix was to **start from a neutral anchor and tilt**. Rather than asking the investor to supply expected returns directly, the model reverse-engineers the "[[capm|equilibrium]]" expected returns *implied* by the market-cap weights (the returns that would make the market portfolio optimal), treats those as a Bayesian **prior**, and then lets the investor overlay only the specific **views** they actually hold (absolute or relative, e.g. "asset A beats asset B by 2%"), each weighted by a stated confidence. The output is a posterior set of expected returns that departs from the market portfolio *only in the directions the investor expressed a view*, and only as far as their confidence warrants. The result is stable, diversified, intuitive weights — which is why Black-Litterman remains a standard tool in institutional asset allocation and a recurring building block in systematic [[macro-trading|macro]] and multi-asset books.

[[emanuel-derman|Emanuel Derman]]'s memoir *My Life as a Quant* (Source: [[book-my-life-as-a-quant]]) describes Black at Goldman as a singular intellect — quiet, precise, often skeptical of his colleagues' models, and unusually willing to abandon his own work when better arguments came along.

## Style and Beliefs

Black was famous for his contrarian instincts and minimalist style. He published a 1986 paper titled simply *"Noise"* (his AFA presidential address) arguing that **noise traders** — participants who trade on noise as if it were information — are what make markets liquid and tradable, since informed traders need an uninformed counterparty to trade against. But the same noise also pushes prices away from fundamental value; Black memorably guessed that price might wander within a factor of two of value (i.e. half to twice "true" value) most of the time, an unusually candid admission from a co-author of an efficient-pricing model that markets are only roughly, not exactly, efficient. The framing prefigured the [[behavioral-finance]] and [[market-microstructure]] literatures and is a foundational reference for [[mean-reversion]] and value-versus-noise debates around the [[efficient-market-hypothesis]]. He was equally famous for his views on **business cycles** (which he attributed to errors in production planning rather than monetary shocks) and on the **equity premium** (which he found puzzling and probably much smaller than measured).

## Legacy

The Black-Scholes formula is the most famous equation in finance, but Black's broader influence is even larger. His insistence that financial models should be simple, falsifiable, and useful to traders shaped a generation of practitioners. The Black-Litterman model remains a standard tool in institutional asset allocation; Black-Derman-Toy is taught in every fixed-income course. Most importantly, Black demonstrated by example that the boundary between academic finance and trading practice could be productive in both directions.

Posthumous recognition: the American Finance Association (of which Black was president in 1985) established the biennial **Fischer Black Prize** in 2002, awarded to a leading finance scholar under 40; MIT Sloan endowed a Fischer Black Professorship. His "Noise" address and the Black-Litterman framework remain actively cited in 2020s quant research and asset-allocation practice.

## Related

- [[myron-scholes]]
- [[robert-merton]]
- [[black-scholes]]
- [[black-litterman]]
- [[options-greeks]]
- [[implied-volatility]]
- [[volatility-smile]]
- [[jack-treynor]]
- [[emanuel-derman]]
- [[model-risk]]
- [[behavioral-finance]]
- [[efficient-market-hypothesis]]
- [[long-term-capital-management]]

## Sources

- (Source: [[book-my-life-as-a-quant]]) — Emanuel Derman's first-hand account of working alongside Black at Goldman Sachs
- Black, F. & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy*, 81(3), 637–654.
- Black, F. (1986). "Noise." *Journal of Finance*, 41(3), 529–543 (AFA presidential address).
- Mehrling, P. (2005). *Fischer Black and the Revolutionary Idea of Finance*. Wiley.
- MacTutor biography: https://mathshistory.st-andrews.ac.uk/Biographies/Black_Fischer/
- AFA Fischer Black Prize: https://afajof.org/fischer-black-prize/
- Verified via Perplexity (sonar), 2026-06-10.
