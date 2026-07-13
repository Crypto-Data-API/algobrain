---
title: "Northfield Information Services"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [data-provider, risk-management, portfolio-theory, quantitative]
aliases: ["Northfield", "Northfield Risk Models", "Northfield Information Services"]
source_type: data
source_url: "https://www.northinfo.com"
confidence: medium
related:
  - "[[barra]]"
  - "[[axioma]]"
  - "[[options-concentration-risk]]"
  - "[[factor-investing]]"
  - "[[risk-management]]"
---

Northfield Information Services is a Boston-based provider of equity factor risk models and portfolio optimization software, positioned as the smaller and more affordable institutional alternative to [[barra|MSCI Barra]] and [[axioma|Axioma]]. Founded in 1986 by Dan diBartolomeo, Northfield offers a family of multi-factor risk models — Fundamental Factor Model, Macro Factor Model, Statistical Factor Model — alongside the Optimizer-J portfolio construction engine. Northfield is particularly popular with mid-sized US asset managers, family offices, and academic quants who want institutional-grade risk infrastructure without the Barra/Axioma price tag.

## What Northfield Produces

- **US Fundamental Factor Model**: style + industry decomposition for US equities, similar in spirit to Barra USE5
- **Global Equity Risk Model**: multi-region, multi-country factor model
- **Short-Term Model**: higher-frequency variant for active rebalancing
- **Macroeconomic Factor Model**: maps equity returns onto macro factors (interest rates, inflation, growth, dollar) — a different lens than fundamental style factors
- **Statistical Factor Model**: PCA-based pure-statistical alternative
- **Fixed-income models**: corporate bond, sovereign, and credit risk models
- **Optimizer-J**: portfolio construction engine compatible with all Northfield risk models

## Pricing Tier

Northfield publishes no formal price list, but anecdotal industry pricing suggests Northfield typically runs at a meaningful discount to Barra/Axioma:

- **US-only model license**: roughly $30K-$80K/year for smaller firms (single-digit-billion AUM)
- **Global model + optimizer**: low-to-mid six figures
- **Academic licenses**: significantly discounted; some universities license historical Northfield factor data
- **Family office tier**: scaled-down packages for sub-$1B portfolios

This positioning — institutional-grade methodology at a substantially lower price — is Northfield's primary go-to-market.

## How It's Used in Practice

Northfield is typically deployed by firms that need real factor risk decomposition but cannot justify Barra/Axioma cost:

- Mid-sized active equity managers ($500M-$10B AUM) doing factor-aware long-only or 130/30 strategies
- Family offices managing concentrated equity positions who want to understand factor risk in single-name exposures
- Academic institutions running quantitative finance research
- Wealth advisors with custom indexing / direct indexing programs
- Long-only mutual funds with factor tilt mandates

The output looks similar to Barra/Axioma reports — predicted volatility, factor contributions, MCTR, stress scenarios — produced through Northfield's reporting interface or via API into the firm's analytics stack.

## Relationship to Options Concentration Risk

For a discretionary or semi-systematic options trader running a meaningful book ($1M-$50M of options exposure), Northfield is the most realistic institutional-grade option for [[options-concentration-risk]] decomposition. The lower price point makes it accessible to single-trader prop shops and family offices that cannot justify Barra/Axioma.

Like the larger competitors, Northfield's factor models work on the equity-side — converting options to delta-equivalent equity exposure and decomposing those exposures into factors. Vol-side concentration (net vega exposure, skew concentration) needs separate handling.

## Strengths

- **Pricing**: meaningfully cheaper than Barra/Axioma; accessible to smaller firms
- **Methodology depth**: dan diBartolomeo and the Northfield research team have published extensively; the methodology is academically grounded
- **Macro factor model**: the macro-economic-factor model is a useful complement to standard style-factor decomposition
- **Customer support**: smaller firm with direct PM-to-vendor relationships; quants can talk to model designers
- **Long history**: 40 years of factor data; deep US history
- **Statistical model**: PCA-based alternative for users who distrust fundamental factor specification

## Limitations

- **Smaller install base**: Northfield reports do not have the consultant-facing comparability of Barra; pension consultants will sometimes ask for Barra-equivalent reporting
- **Regional / global coverage**: weaker than Barra and Axioma on emerging markets and smaller markets
- **Optimizer ecosystem**: Optimizer-J is solid but has a smaller third-party tooling ecosystem than Axioma Portfolio Optimizer
- **Marketing/visibility**: Northfield is well-known among quants but invisible to retail / semi-pro options traders
- **Documentation**: methodology papers are excellent but less voluminous than Barra's
- **No native options**: same equity-centric limitation as competitors

## Northfield vs Barra vs Axioma

| Dimension | Northfield | [[barra]] (MSCI) | [[axioma]] (Qontigo) |
|-----------|-----------|------------------|----------------------|
| **Default for** | Mid-sized active mgrs, family offices | Pensions, large asset mgrs | Quant shops, 130/30 funds |
| **Price** | $30K-low six fig | Low-to-mid six fig | Mid-six fig |
| **Methodology lens** | Fundamental + Macro + Statistical | Fundamental | Fundamental + Statistical |
| **US coverage depth** | Strong | Strongest | Strong |
| **Global coverage** | Adequate | Strongest | Strong |
| **Optimizer** | Optimizer-J | BarraOne | Axioma Optimizer |

For options-book concentration analysis specifically, all three vendors produce equivalent outputs at the equity-exposure level. Northfield's price point makes it the realistic choice for smaller shops.

## Related

- [[barra]] — the larger competitor / industry standard
- [[axioma]] — the other large competitor, popular in quant shops
- [[factor-investing]] — the conceptual framework
- [[options-concentration-risk]] — Northfield is the affordable factor-decomposition option for smaller books
- [[risk-management]] — broader risk context
- [[portfolio-theory]] — multi-factor models extend Markowitz / CAPM
- [[correlation]] — factor models as alternatives to raw covariance estimation

## Sources

- Northfield Information Services product documentation (northinfo.com)
- Industry RFP responses; Northfield methodology papers
- Referenced in [[options-concentration-risk]] as a Barra-style factor decomposition vendor
