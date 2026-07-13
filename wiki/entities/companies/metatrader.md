---
title: "MetaTrader"
type: entity
created: 2026-06-13
updated: 2026-06-17
status: good
tags: [forex, data-provider, algorithmic]
entity_type: company
founded: 2000
headquarters: "Limassol, Cyprus (MetaQuotes)"
website: "https://www.metatrader5.com"
aliases: ["MetaTrader", "MT4", "MT5", "MetaTrader 4", "MetaTrader 5", "MetaQuotes"]
related: ["[[forex]]", "[[ctrader]]", "[[tradingview-platform]]", "[[algorithmic-trading]]", "[[liquidity-provider]]"]
---

MetaTrader is the dominant retail [[forex]] and CFD trading platform, developed by **MetaQuotes Software**. Its two principal versions — **MetaTrader 4 (MT4)**, released in 2005, and **MetaTrader 5 (MT5)**, released in 2010 — are distributed to traders by hundreds of brokers worldwide and have been the default front-end of retail FX for two decades. Industry estimates routinely put MetaTrader's combined share of the retail FX platform market well above **half**, making it the de-facto standard a new retail trader encounters first.

## Overview

MetaQuotes, founded in 2000 and headquartered in Limassol, Cyprus, licenses MetaTrader to brokers rather than operating a venue itself. Each broker brands and feeds its own instance, which is why the same platform sits in front of very different liquidity and execution arrangements. The platform spans desktop (Windows), web, and mobile (iOS/Android).

## MT4 vs MT5

- **MT4** — built for FX margin trading; lighter, hedging-friendly position model, and an enormous installed base and community. Despite MetaQuotes pushing the market toward MT5, MT4 remains heavily used.
- **MT5** — multi-asset (FX, stocks, futures), netting *and* hedging account modes, more timeframes, an economic calendar, depth-of-market, and a faster strategy tester. Adoption grew substantially as MetaQuotes restricted new MT4 licences.

## Algorithmic Trading

MetaTrader's automation is built on the **MQL** language — **MQL4** for MT4 and **MQL5** for MT5 (a C++-like language). Automated strategies are packaged as **Expert Advisors (EAs)**; custom indicators and scripts are also supported. A built-in **Strategy Tester** provides backtesting and optimization, and the MQL5 marketplace distributes third-party EAs, indicators, and data. This contrasts with [[ctrader]], whose automation (**cAlgo / cBots**) is written in C# on .NET.

MetaTrader's grip on retail [[algorithmic-trading]] is a network effect: because nearly every retail broker offers it, an enormous library of EAs, indicators, and tutorials targets MQL, which in turn pulls more brokers and developers onto the platform. For most retail algos, "writing a trading bot" effectively means writing an MQL Expert Advisor.

## Broker Bridges and Liquidity

A broker does not run MetaTrader in isolation — it sits behind a **server** that MetaQuotes licenses, and the broker decides what happens to client orders:

- **Dealing-desk / B-book** — the broker is the counterparty, internalizing orders and warehousing the risk (it profits when clients lose). No external [[liquidity-provider]] is touched.
- **A-book / STP** — orders are routed to external liquidity via a **bridge** (third-party software such as oneZero, PrimeXM, or Integral) that connects the MT4/MT5 server to a pool of bank and non-bank [[liquidity-provider|liquidity providers]].
- **Hybrid** — most large brokers B-book small/losing flow and A-book the rest.

The bridge is the critical, invisible layer that determines whether a MetaTrader fill reflects real market liquidity or a synthetic dealer quote.

## Market Structure and Criticism

Because MetaTrader is broker-distributed, execution quality depends entirely on the broker's model — many retail MT4/MT5 brokers run a dealing-desk / market-maker book rather than passing orders to an [[liquidity-provider|external liquidity provider]]. The platform has also drawn scrutiny over requotes, slippage, and the prevalence of low-quality marketed EAs (including "set-and-forget" grid/martingale bots that blow up accounts). Regulators have also acted against MetaTrader's reach: in 2022 **Apple and Google removed the MT4/MT5 apps** from their US stores amid concerns over fraudulent brokers, before they were later reinstated. Traders seeking transparent ECN/STP execution and depth-of-market often prefer [[ctrader]] or exchange-style venues such as [[lmax-exchange]].

## Relevance to Traders

MetaTrader is the baseline a forex trader will almost certainly encounter first: it sets expectations for charting, order types, and EA-based automation. Understanding its broker-distributed model — and its limits — is essential for evaluating execution quality and choosing where to actually trade.

## Related

- [[ctrader]] — the main ECN/algo-oriented alternative (C# vs MQL)
- [[forex]] — the market MetaTrader was built for
- [[algorithmic-trading]] — EAs and the MQL ecosystem
- [[tradingview-platform]] — increasingly used for charting alongside MetaTrader execution
- [[liquidity-provider]] — what sits (or doesn't) behind a MetaTrader broker

## Sources

_Compiled from MetaQuotes public documentation and FX platform comparisons (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md)._
