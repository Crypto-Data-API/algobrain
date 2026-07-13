---
title: "Market Risk"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [risk-management, volatility, portfolio-theory, correlation, derivatives]
aliases: ["Market Risk", "market-risk", "Systematic Risk", "Price Risk"]
related: ["[[credit-risk]]", "[[beta]]", "[[value-at-risk]]", "[[expected-shortfall]]", "[[interest-rate-risk]]", "[[diversification]]", "[[volatility]]", "[[standard-deviation]]", "[[correlation]]", "[[capital-asset-pricing-model]]", "[[hedging]]", "[[derivatives]]", "[[futures]]", "[[options]]", "[[stop-loss]]", "[[stress-test]]", "[[tail-risk]]", "[[liquidity-risk]]", "[[basel-iii]]"]
domain: [risk-management]
prerequisites: ["[[volatility]]", "[[beta]]"]
difficulty: intermediate
---

**Market risk** (also *systematic risk* or *price risk*) is the risk of loss arising from adverse movements in market prices — equity prices, interest rates, exchange rates, and commodity prices. It is the risk you bear simply for holding a position exposed to the market, as distinct from [[credit-risk]] (the risk a counterparty defaults) and [[liquidity-risk]] (the risk you cannot trade at a fair price). Crucially, market risk contains a *systematic*, market-wide component that cannot be diversified away and is therefore the risk the market pays you to bear (see [[capital-asset-pricing-model|CAPM]] and [[beta]]).

## Overview

Any position marked to market — a stock, a bond, a currency pair, a commodity future, a derivative — changes value as its underlying price moves. Market risk is the formal name for the possibility that those moves go against you. It is the most visible risk in trading because it shows up continuously in the daily profit-and-loss, unlike credit or operational losses, which arrive in lumps.

The defining feature of market risk is that a large part of it is *common* to many assets at once. When equity markets fall, most stocks fall together; when the yield curve shifts, most bonds re-price together. This shared, undiversifiable core is the **systematic** component — the piece that portfolio construction cannot eliminate and that, under [[capital-asset-pricing-model|CAPM]], is compensated with a risk premium. The remainder — the part of an individual asset's price movement unique to that asset — is **idiosyncratic** and can be diversified away.

## The four classic sub-types

Regulatory and practitioner convention breaks market risk into four price factors, often called the four "risk classes":

- **Equity risk** — exposure to changes in stock prices and equity-index levels (and to equity volatility for options positions). A long equity book loses when the broad market or the specific sector sells off.
- **Interest-rate risk** — exposure to shifts in the level, slope, and curvature of the yield curve. This is the dominant market risk of fixed-income portfolios, measured with duration and convexity; it exists even for default-free government bonds. See [[interest-rate-risk]].
- **Currency (FX) risk** — exposure to moves in exchange rates. It affects anyone holding assets, liabilities, or cash flows denominated in a foreign currency, and it can dominate the return of an unhedged cross-border investment even when the underlying asset barely moves in local-currency terms.
- **Commodity price risk** — exposure to changes in the prices of physical commodities (oil, gas, metals, agriculturals) and their futures curves. It affects producers, consumers, and speculators, and carries its own structure through storage costs, seasonality, and the shape of the forward curve (contango/backwardation).

A fifth factor, **volatility risk** (exposure to changes in implied volatility itself), is often treated separately because options and other convex instruments profit or lose from moves in volatility even when the underlying price is unchanged.

## Systematic vs. idiosyncratic risk

The single most important idea in market risk is the split between the two:

- **Systematic (market) risk** is the portion of an asset's return variability driven by market-wide factors — the whole equity market, the level of rates, broad risk appetite. Because it hits everything at once, it cannot be diversified away. An asset's exposure to it is summarised by its [[beta]]: a beta of 1 moves one-for-one with the market, a beta above 1 amplifies it, below 1 dampens it.
- **Idiosyncratic (specific / unsystematic) risk** is the portion unique to a single name — a company's earnings miss, a management scandal, a plant fire. Because these shocks are largely uncorrelated across unrelated assets, they wash out in a well-spread portfolio.

Under [[capital-asset-pricing-model|CAPM]], only systematic risk is *compensated*: the expected return on an asset rises with its beta, not with its total volatility. Idiosyncratic risk earns no premium precisely because a diversified investor can shed it for free (see [[diversification]]). This is why "market risk" and "systematic risk" are used almost interchangeably — the compensated core of market risk *is* the systematic component. The practical implication is stark: you are paid for taking market risk, but you are *not* paid for taking avoidable, name-specific risk, so leaving idiosyncratic risk in a portfolio is uncompensated exposure.

## Measurement

Market risk is unusually measurable because prices are observable in real time. The common tools, roughly in order of sophistication:

- **[[volatility]] / [[standard-deviation]]** — the foundational measure of dispersion. The standard deviation of returns quantifies how widely an asset or portfolio swings; it is the raw material for most other risk metrics and for [[beta]] estimation.
- **[[beta]] and factor exposures** — instead of one blob of volatility, decompose risk into exposures to named factors (the market, rates, credit spreads, style factors such as value or momentum — see [[factor-investing]]). Factor models tell you *what* is driving the risk, not just how large it is, and enable targeted hedging.
- **[[value-at-risk|Value-at-Risk (VaR)]]** — a single number answering "what loss will not be exceeded, over a set horizon, with a set confidence?" (e.g. a 1-day 99% VaR). VaR became the industry-standard summary of market risk. Its well-known **limitations**: it says nothing about the *size* of losses in the tail beyond the cutoff, it is not "sub-additive" in general (so it can wrongly suggest diversification increases risk), and it depends heavily on the estimation window and distributional assumptions — historically it lulled institutions into underestimating [[tail-risk]] before crises.
- **[[expected-shortfall|Expected Shortfall (ES) / Conditional VaR (CVaR)]]** — the average loss *given* that the VaR threshold is breached. Because it looks *into* the tail rather than *at* its edge, ES is coherent (sub-additive) and captures the severity of extreme losses that VaR ignores. This is why the Basel framework shifted its market-risk capital measure from VaR toward Expected Shortfall.
- **[[stress-test|Stress testing]] and scenario analysis** — instead of relying on a statistical distribution estimated from calm periods, revalue the portfolio under specific severe scenarios (a repeat of 2008, a rate shock, an FX devaluation) to expose vulnerabilities that VaR and ES miss, especially [[black-swan|tail events]] and non-linear payoffs.
- **Regulatory capital** — banks must hold capital against market risk. The framework is codified in the Basel accords (see [[basel-iii]]); its modernised market-risk rules are the **Fundamental Review of the Trading Book ([[frtb|FRTB]])**, which replaced VaR with a stressed Expected Shortfall measure, tightened the boundary between the trading and banking books, and revised the standardised approach.

## Management

You can *reduce* and *reshape* market risk, but you cannot eliminate its systematic core — that is the whole point of it being undiversifiable. The main levers:

- **[[diversification]]** — spreading capital across imperfectly correlated assets removes idiosyncratic risk and lowers total portfolio volatility. It cannot remove systematic risk: a fully diversified equity portfolio still carries the market's beta.
- **[[hedging]] with [[derivatives]]** — offsetting an exposure with an instrument that moves the opposite way. Index [[futures]] hedge broad equity or rate exposure; [[options]] provide asymmetric protection (a put caps downside while preserving upside); currency forwards hedge FX risk; commodity futures hedge input-price risk. Hedging transfers market risk to a willing counterparty rather than destroying it.
- **Position limits and risk budgeting** — hard caps on exposure per desk, factor, or asset class, and allocation of a fixed "risk budget" (often expressed in VaR or volatility terms) across strategies.
- **[[stop-loss]] orders** — pre-committed exit levels that bound the loss on a single position, imposing discipline and truncating the left tail (at the cost of being whipsawed by noise).
- **Dynamic hedging** — continuously adjusting a hedge as market conditions change, most notably *delta hedging* an options book so that small underlying moves are neutralised; the hedge ratio is re-balanced as prices, volatility, and time change.
- **Reducing gross exposure / raising cash** — the bluntest tool: simply holding less risky assets lowers market risk directly, at the cost of forgoing the risk premium.

The residual after all of these is the systematic exposure the portfolio *chooses* to keep — its deliberate bet on being paid for bearing market risk.

## Relationship to other risks

Market risk is one of several distinct risk categories that interact, especially under stress:

- **vs. [[credit-risk]]** — credit risk is the risk of *default* by a borrower or counterparty; market risk is the risk of *price moves* in instruments you hold. The two blur at the edges: the widening of *credit spreads* on traded bonds is often handled as a market-risk factor, but the *jump-to-default* loss when an issuer actually fails is a fat-tailed credit exposure that ordinary volatility-based market-risk measures understate.
- **vs. [[liquidity-risk]]** — liquidity risk is the risk of not being able to trade out of a position at a fair price (or at all). It amplifies market risk: a position that looks modestly risky in normal conditions can be impossible to exit without a large price concession in a stressed market, turning a paper loss into a realised one.
- **vs. operational risk** — [[operational-risk|operational risk]] (failures of people, systems, and processes — a rogue trade, a settlement error, a cyber breach) is unrelated to price direction and is managed with controls rather than hedges, but a control failure can leave an unintended market exposure open.

The critical crisis dynamic is that these risks are **not independent**. In a severe sell-off, **correlations converge toward 1** (see [[correlation]]): assets that were diversifying in calm markets fall together, so [[diversification]] delivers least benefit exactly when it is needed most. Simultaneously, liquidity evaporates (widening bid-ask spreads and market impact), forced deleveraging feeds further selling, and credit and market losses reinforce one another. This clustering of tail events across normally-distinct risk types is why [[stress-test|stress testing]] and [[tail-risk]] analysis exist alongside statistical measures like [[value-at-risk|VaR]] that assume more stable relationships.

## Example (qualitative)

Consider a diversified equity portfolio of many stocks across sectors. Careful diversification has removed almost all *idiosyncratic* risk — a single company's bad earnings barely dents the whole book. What remains is the portfolio's *systematic* exposure, summarised by its [[beta]] to the market.

Now a broad market shock hits — say a sharp rise in interest rates or a global risk-off event. Because the portfolio still carries market beta, it falls with the market; diversification offers no shelter from this systematic move. A risk manager who had measured only average-condition [[volatility]] or a calm-period [[value-at-risk|VaR]] would have understated the drawdown, because in the sell-off cross-asset [[correlation|correlations rose toward 1]] and even the "diversifying" holdings dropped together. A manager who had instead **bought index put [[options]]** or **shorted index [[futures]]** would have offset much of the loss — having paid the option premium or borne the futures basis as the ongoing price of hedging systematic market risk. The idiosyncratic risk was diversified away for free; the systematic risk had to be either accepted (and paid for via the risk premium) or explicitly hedged. (Illustrative only — no specific figures implied.)

## Related

- [[credit-risk]] — default risk, the other dominant risk in fixed income; contrast with price risk
- [[liquidity-risk]] — the risk of not trading at a fair price; amplifies market risk in crises
- [[beta]], [[capital-asset-pricing-model]] — how systematic (compensated) market risk is measured and priced
- [[systematic-risk]] — the undiversifiable core of market risk (forward link)
- [[diversification]] — removes idiosyncratic risk but not systematic risk
- [[volatility]], [[standard-deviation]], [[correlation]] — the statistical building blocks of market-risk measurement
- [[value-at-risk]], [[expected-shortfall]], [[stress-test]], [[tail-risk]] — the measurement toolkit and its limits
- [[interest-rate-risk]] — the interest-rate sub-type in detail
- [[hedging]], [[derivatives]], [[futures]], [[options]], [[stop-loss]] — the management toolkit
- [[factor-investing]] — decomposing market risk into named factor exposures
- [[basel-iii]], [[frtb]] — bank regulatory capital for market risk

## Sources

- General, widely-taught risk-management and portfolio-theory knowledge (e.g. Hull, *Risk Management and Financial Institutions* and *Options, Futures, and Other Derivatives*; Bodie, Kane & Marcus, *Investments*). The systematic/idiosyncratic decomposition and the pricing of systematic risk follow the Capital Asset Pricing Model.
- The four market-risk classes, the VaR-to-Expected-Shortfall shift, and the trading-book capital treatment follow the Basel Committee on Banking Supervision's market-risk framework, including the Fundamental Review of the Trading Book (BIS/Basel documents). No specific figures are asserted here beyond these general, publicly-documented conventions.
