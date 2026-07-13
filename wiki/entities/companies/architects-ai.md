---
title: "Architects AI (ARC-AI)"
type: entity
created: 2026-06-19
updated: 2026-06-19
status: draft
tags: [trading-tools, algorithmic, backtesting, company]
entity_type: company
website: "https://architectsai.com"
aliases: ["Architects AI", "ARC-AI", "ARC A.I.", "Architects A.I."]
related: ["[[arc-strategy]]", "[[ninjatrader]]", "[[backtesting]]", "[[average-candle-range]]", "[[box-and-swing-structure]]"]
---

# Architects AI (ARC-AI)

**Architects AI**, branded around its **ARC-AI** product line, is a trading-technology vendor that develops and sells packaged automated trading strategies, distinguished by a proprietary backtesting and optimization engine built inside [[ninjatrader|NinjaTrader]]. It represents the commercialization of level-and-candle, ARC-style trading: where the [[arc-strategy|ARC (Area-Range-Candle)]] method is a discretionary YouTube framework, ARC-AI is an attempt to encode and industrialize similar logic into a turnkey product.

> **Disambiguation:** "ARC" in *ARC-AI* / Architects AI is the vendor's product branding. It is conceptually adjacent to but not the same thing as the discretionary [[arc-strategy|Area-Range-Candle]] retail method, and is entirely unrelated to the [[arc-usdt|ARC/USDT crypto token]]. The shared three letters are a frequent source of confusion.

## Overview

Architects AI describes itself as a trading-technology and software-development firm and emphasizes collaboration with established trading platforms (Source: gap-finder Perplexity research 2026-06-19). Its core offering is a suite of "ARC-AI" strategy packages, each powered by a proprietary core engine that runs inside [[ninjatrader|NinjaTrader]] and provides a professional-grade [[backtesting]] and optimization framework.

According to the vendor's own materials, that framework is designed to:

- search over **parameter spaces** for strategy settings,
- perform **walk-forward testing**, and
- evaluate **robustness** of a strategy across differing market conditions

(Source: gap-finder Perplexity research 2026-06-19).

> The descriptions above are drawn from the vendor's marketing materials as relayed in the gap-finder research, not from independent due diligence. Vendor-reported capabilities and performance should be independently verified before any capital is committed.

## Why It Matters for the Wiki

The wiki already documents general-purpose backtesting engines such as [[backtesting|backtesting frameworks]] and hyperparameter optimizers. Architects AI is the *commercial-product* analogue: it shows how a vendor wraps the same backtesting-and-optimization concepts into a packaged tool aimed at discretionary retail traders, and it provides a concrete bridge between the conceptual [[arc-strategy|ARC method]] and an actual execution/automation environment ([[ninjatrader]]).

It is also a useful case study in translating a loosely defined YouTube strategy — "draw a box, wait for 20% of the [[average-candle-range|range]], then trade a [[john-wick-candle|John Wick]] candle at a level" — into parameterized, optimizable rules in NinjaScript.

## Risks and Cautions

Commercial strategy bundles built on aggressive parameter optimization carry well-known hazards that the wiki's methodology pages emphasize:

- **Overfitting risk** in black-box optimizers — a strategy optimized over a parameter grid can look excellent in-sample and fail live. See [[backtesting]] and walk-forward / deflated-Sharpe considerations.
- **Vendor-claim verification** — marketed performance is rarely net of realistic costs, slippage, and capacity constraints.
- **Black-box opacity** — if the trader cannot inspect the rules, kill criteria and failure-mode analysis are harder to apply.

These cautions apply to any prepackaged commercial strategy, ARC-AI included; the wiki documents the entity descriptively, not as an endorsement.

## Related

- [[arc-strategy]] — the discretionary method ARC-AI commercializes
- [[ninjatrader]] — host platform for the ARC-AI engine
- [[backtesting]]
- [[average-candle-range]]
- [[box-and-swing-structure]]
- [[arc-usdt]] — unrelated crypto token (disambiguation)

## Sources

- gap-finder Perplexity deep research (2026-06-19) — summarizing vendor materials (architectsai.com and a partner listing); vendor claims not independently verified
- Source video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge
