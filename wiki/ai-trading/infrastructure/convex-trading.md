---
title: "Convex Trading"
type: source
created: 2026-05-07
updated: 2026-06-20
status: good
tags: [data-provider, options, derivatives, technology, risk-management]
aliases: ["Convex Trading", "Convex"]
source_type: data
source_url: "https://convextrading.com"
confidence: low
related:
  - "[[options-concentration-risk]]"
  - "[[options-portfolio-construction]]"
  - "[[options-greeks]]"
  - "[[risk-management]]"
  - "[[orats]]"
  - "[[trade-machine]]"
---

Convex Trading is a third-party options analytics and portfolio-management platform aimed at active retail and semi-professional options traders. It positions itself as a more sophisticated alternative to broker-supplied tools, offering aggregated Greeks across positions, scenario analysis, and trade-construction tools. Coverage of Convex Trading in independent reviews and academic literature is limited; this page documents what is known with the explicit caveat that the product is niche and the available public information is thin.

> **Note**: Convex Trading is a niche product. The information below reflects what is publicly available as of the page's creation date; specific feature claims, pricing, and capability details should be verified directly with the vendor before relying on them.

## What It Aims to Provide

Based on publicly available product descriptions, Convex Trading offers some combination of:

- **Multi-position Greeks aggregation**: roll up delta, gamma, vega, theta across an options book
- **P&L scenario analysis**: payoff diagrams and forward P&L under price / vol / time shocks
- **Trade construction**: build multi-leg structures and visualize their payoff
- **Position tracking**: import positions from a broker (typically via manual entry or CSV)
- **Volatility analytics**: IV surface views and historical volatility comparisons

The product is positioned for serious retail / semi-pro options traders who have outgrown broker-supplied tools (Thinkorswim Analyze tab, IBKR Risk Navigator, tastytrade) but cannot or will not pay institutional pricing for [[bloomberg-terminal|Bloomberg]] or [[orats]] enterprise.

## Pricing Tier

Convex Trading's public pricing has historically been in the prosumer band — typically tens to low hundreds of dollars per month — placing it between free broker tools and institutional platforms. Specific tiers and feature gating change over time and should be verified at the vendor site.

## Relationship to Options Concentration Risk

For [[options-concentration-risk]], a tool like Convex Trading sits in the third-party-analytics layer alongside [[trade-machine]] and [[pivolio]]. Its value proposition is filling the gap between:

- **Broker tools** (Risk Navigator, Thinkorswim Analyze) — adequate but limited to one broker's positions
- **Institutional platforms** (Bloomberg, Barra, in-house Python) — vastly more powerful but expensive or build-intensive

A trader running an options book across multiple brokers, or one who wants concentration views (sector, factor, vol-regime) that broker tools don't provide natively, would consider a third-party tool of this kind. The specific concentration-management features Convex Trading offers should be evaluated case-by-case against the dimensions enumerated in [[options-concentration-risk]] (single-name, sector, factor, beta, vol regime, tenor).

## Use by automated and AI-assisted systems

As an analytics-and-visualization layer rather than an execution engine, Convex Trading is used by automated workflows in a supporting role rather than as a trading bot:

- **Risk read-out, not order routing** — a trader running a semi-automated options book can use the platform's aggregated [[options-greeks|Greeks]] and scenario views as a human-in-the-loop sanity check before an automated or rules-based strategy submits orders elsewhere.
- **Scenario inputs for sizing logic** — payoff and stress outputs (P&L under price / vol / time shocks) can inform position-sizing rules even if the sizing itself is computed in a separate script.
- **No documented public API** — available descriptions do not confirm a programmatic API, so any integration into an AI/automated pipeline is likely manual (CSV / screen review) rather than fully machine-driven. Verify directly with the vendor before assuming programmatic access. This is the main constraint on using it inside a fully automated stack, where API-first tools like [[orats]] or a custom build are usually preferred.

For traders building genuinely automated options systems, the realistic pattern is to use a tool like this for oversight and ad-hoc analysis while sourcing machine-readable data and execution from API-first providers.

## Strengths (general for this product category)

- **Multi-broker aggregation** (if supported): can combine positions across brokers in one view
- **Cheaper than institutional**: meaningful step up from broker tools without institutional pricing
- **Active-trader workflows**: typically built with options-specific use cases in mind, not general-purpose portfolio software

## Limitations (general for this product category)

- **Limited public information**: independent reviews of Convex Trading specifically are thin; capability claims should be verified
- **Smaller vendor risk**: niche options-analytics tools come and go; vendor longevity is a real consideration
- **No institutional-grade factor models**: third-party prosumer tools generally do not offer Barra/Axioma-style factor decomposition
- **Data dependency**: quality of stress / scenario analysis depends on the underlying market data feed; ensure the tool sources reliable IV and price data
- **Manual position entry**: many third-party tools rely on manual entry or CSV upload for positions, which introduces errors and friction

## Compared to Alternatives

For an active options trader looking at third-party analytics:

| Tool | Position |
|------|----------|
| [[ibkr-risk-navigator|IBKR Risk Navigator]] | Free, IBKR-only, broad capability |
| [[thinkorswim]] Analyze | Free, TD/Schwab-only |
| [[tastytrade]] | Free, tasty-style book focus |
| **Convex Trading** | Third-party, multi-broker (claimed), prosumer pricing |
| [[trade-machine]] (CML) | Backtester-focused, prosumer pricing |
| [[pivolio]] | Niche options portfolio tool, prosumer pricing |
| [[orats]] | More established options data + analytics |
| [[bloomberg-terminal]] | Institutional, comprehensive |

The choice among prosumer tools comes down to specific feature fit, broker integration, and personal workflow preference.

## Related

- [[options-concentration-risk]] — listed alongside [[pivolio]] and [[trade-machine]] as third-party concentration tools
- [[options-portfolio-construction]] — the broader workflow these tools support
- [[options-greeks]] — what these tools aggregate
- [[trade-machine]] — comparable third-party tool, backtester-focused
- [[pivolio]] — comparable third-party options portfolio tool
- [[orats]] — more established options data + analytics platform
- [[ibkr-risk-navigator]] — free broker alternative
- [[risk-management]] — broader risk-management context

## Sources

- Convex Trading public website and product descriptions
- Referenced in [[options-concentration-risk]] as a third-party options analytics tool
- Note: independent third-party reviews are limited; this page documents the product category position rather than detailed feature claims
