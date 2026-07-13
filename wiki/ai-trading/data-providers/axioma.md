---
title: "Axioma (Qontigo)"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [data-provider, risk-management, portfolio-theory, quantitative, institutional]
aliases: ["Axioma", "Qontigo Axioma", "Axioma Portfolio"]
source_type: data
source_url: "https://qontigo.com/products/axioma-risk/"
confidence: high
related:
  - "[[barra]]"
  - "[[northfield]]"
  - "[[options-concentration-risk]]"
  - "[[factor-investing]]"
  - "[[risk-management]]"
---

Axioma is the principal institutional competitor to [[barra|MSCI Barra]] in the multi-factor equity risk model space. Now part of Qontigo (a Deutsche Börse-owned analytics group formed by the merger of Axioma, STOXX, and DAX), Axioma offers global, regional, and country-specific factor risk models alongside a portfolio optimization engine that hedge funds, asset managers, and pension funds use to construct factor-aware portfolios. Axioma's models are particularly valued for their flexibility around custom factor specification, faster update cadence on factor returns, and a portfolio optimization layer that integrates risk-model output directly into mean-variance and tracking-error-targeted portfolio construction.

## What Axioma Produces

- **Axioma Worldwide Equity Risk Model (AXWW)**: global multi-factor model covering 60+ markets with consistent factor methodology
- **Regional models**: AXUS (US), AXEU (Europe), AXAP (Asia-Pacific), AXEM (Emerging Markets), plus country-specific models
- **Multiple model variants**: short-horizon (daily) and medium-horizon (monthly) variants for different rebalancing frequencies
- **Style factors**: market sensitivity, volatility, momentum, value, growth, size, leverage, liquidity, exchange-rate sensitivity (regional models)
- **Industry classifications**: GICS-based industry factors with regional adjustments
- **Statistical factors (option)**: an alternative pure-statistical PCA-based factor model that does not impose a priori factor labels
- **Axioma Portfolio Optimizer**: an LP/QP optimization engine that ingests the risk model and constructs portfolios subject to risk, factor, and trading constraints

## Pricing Tier

Institutional, similar to [[barra|Barra]]. No public price list. Practical ranges:

- **Risk model data feed**: low-to-mid six figures per year for a single firm
- **Axioma Risk + Optimizer license**: mid-six figures, scales with seats and asset coverage
- **Quantitative research subscription** (limited model access for academic / smaller firms): ~$30K-$80K/year
- **Bloomberg integration**: Axioma data is available through Bloomberg for joint subscribers
- **No retail tier**

## How It's Used in Practice

Axioma is most often deployed in two modes:

1. **Risk reporting and limits enforcement**. The risk team runs the firm's portfolios through Axioma daily, produces factor exposure reports, MCTR (marginal contribution to total risk) tables, and stress scenarios. PMs see the same exposures and adjust trades when they exceed limits.

2. **Portfolio construction**. Quant teams use the Axioma Optimizer in production to size positions subject to:
   - Tracking error vs benchmark (typical: 2-4% TE for active equity)
   - Factor neutrality constraints (e.g., "neutral to momentum, neutral to size")
   - Sector / industry caps
   - Position-size limits, turnover budgets, transaction-cost models

The optimizer's tight integration with the risk model is Axioma's key selling point vs Barra-as-data-feed-only deployments.

## Relationship to Options Concentration Risk

For [[options-concentration-risk]], Axioma serves the same function as [[barra|Barra]] — decomposing the underlying delta exposure of an options book into systematic factors and idiosyncratic residual. The flexibility of Axioma's framework lets quants build custom factor models that include, for example:

- A vol-regime factor proxying changes in [[vix]]
- A skew factor capturing skew steepening/flattening
- A dispersion factor capturing index-vs-component vol divergence

These extensions make Axioma a more popular choice at quant shops running options-heavy books, where the standard equity factors don't fully capture vol-related concentration.

Like Barra, native Axioma models treat options as delta-equivalents on the underlying. Full options-aware decomposition still requires a separate Greeks-aware system on top.

## Strengths

- **Flexibility**: custom factor specification is more straightforward than in Barra
- **Statistical models**: optional pure-PCA alternative to fundamental factor models
- **Optimizer integration**: tight risk-model-to-optimizer pipeline is a competitive advantage
- **Faster updates**: short-horizon models update factor returns at higher frequency than Barra's standard models
- **Bench-side adoption**: Axioma is particularly popular among systematic active equity managers and 130/30 funds
- **Coverage**: 60+ country models with consistent methodology across regions

## Limitations

- **Cost**: institutional-only, comparable to Barra
- **Smaller install base**: Barra is the older incumbent; many consultants and pensions still default to Barra reports for comparability
- **Equity-centric**: like Barra, native coverage is equities; fixed income and derivatives need extensions
- **Documentation**: Axioma methodology papers are public but less voluminous than Barra's published research base
- **Vendor consolidation risk**: Qontigo is a Deutsche Börse subsidiary; further M&A could change pricing or product roadmap

## Axioma vs Barra

| Dimension | Axioma (Qontigo) | [[barra]] (MSCI) |
|-----------|------------------|------------------|
| **History** | Strong from 2000s | Deep history back to 1980s |
| **Default standard** | Quant shops, 130/30 | Pensions, traditional asset mgrs |
| **Custom factors** | Easier | Possible but less native |
| **Optimizer** | Integrated | BarraOne includes optimization |
| **Pricing** | Comparable institutional | Comparable institutional |
| **Statistical model option** | Yes (PCA variant) | More fundamental-factor-centric |

In practice, larger firms often run both — Barra for the consultant-facing reports, Axioma for production optimization.

## Related

- [[barra]] — primary competitor; the older incumbent
- [[northfield]] — cheaper US-focused alternative
- [[factor-investing]] — the conceptual framework
- [[options-concentration-risk]] — factor decomposition exposes hidden options-book concentration
- [[risk-management]] — broader risk context
- [[portfolio-theory]] — Axioma Optimizer extends Markowitz with factor and trading constraints
- [[correlation]] — factor models replace raw covariance estimation

## Sources

- Qontigo product documentation (qontigo.com)
- Axioma risk-model methodology papers (publicly available)
- Referenced in [[options-concentration-risk]] as a Barra-equivalent factor decomposition vendor
