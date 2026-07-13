---
title: "Alpaca"
type: entity
created: 2026-04-15
updated: 2026-04-19
status: good
tags: [company, broker, api-trading, algorithmic, stocks, options, crypto]
entity_type: company
founded: 2015
headquarters: "San Mateo, California, USA"
website: "https://alpaca.markets"
aliases: ["Alpaca Markets", "Alpaca Securities", "Alpaca Crypto"]
related: ["[[interactive-brokers]]", "[[robinhood]]", "[[tastytrade]]", "[[oanda]]", "[[tiger-brokers]]", "[[hyperliquid]]", "[[alpaca-vs-options-brokers]]", "[[alpaca-vs-hyperliquid]]", "[[api-trading]]", "[[paper-trading]]", "[[algorithmic-trading-overview]]"]
---

# Alpaca

Alpaca is a US broker-dealer and brokerage-infrastructure company headquartered in San Mateo, California, built around an API-first trading and embedded-finance product. Founded in 2015, it is best known among retail algorithmic traders for its commission-free US equities API, free paper-trading environment, and Python-first developer experience, and among fintechs for its white-label "Broker API" that powers over 9 million brokerage accounts across 40+ countries. In January 2026 Alpaca closed a $150M Series D led by Drive Capital at a $1.15B valuation, with participation from Citadel Securities, Kraken, and BNP Paribas among others.

## Company and Regulation

- **Founded**: 2015
- **Headquarters**: San Mateo, California, USA
- **Regulatory entities**:
  - **Alpaca Securities LLC** -- FINRA-registered broker-dealer (CRD #288202), SIPC member
  - **Alpaca Crypto LLC** -- separate crypto entity
  - **Self-clearing** as of 2025, with OCC (options), FICC (fixed income), and Nasdaq Exchange memberships achieved in 2025
- **Funding**: $320M+ total; Series D of $150M (January 2026) at $1.15B valuation; $40M line of credit secured alongside
- **Revenue**: $100M+ ARR as of early 2026
- **Scale**: powers 9M+ brokerage accounts across 300+ partner organizations in 40+ countries
- **Investors**: Drive Capital (lead Series D), Citadel Securities, Kraken, BNP Paribas venture arm, Portage, Horizons Ventures, Social Leverage, Unbound, Diagram, Derayah Financial

The dual B2B / B2C structure is important: Alpaca operates both a **direct retail brokerage** (open an account at alpaca.markets, trade via their API or third-party tools) and a **Broker API** product (fintechs embed Alpaca's brokerage rails into their own apps). The retail-facing product is a commodity; the B2B product is the strategic business.

## Products and Markets

### US Equities and ETFs

- **$0 commission** on US stocks and ETFs
- **Fractional shares** supported on the majority of the universe
- **Extended-hours trading** (pre-market, after-hours, and 24/5 overnight trading introduced 2025)
- **No FX or international listings directly** -- US-listed securities only (international exposure comes via US-listed ADRs and ETFs)

### Options (Equity and ETF)

- **Launched**: 2023 for single-leg; **multi-leg options launched 2025**
- **Commissions**: $0 per contract, no exchange fees passed through on standard retail flow (fee pass-through may apply for high-volume accounts)
- **Approval levels**: 1-4 standard retail levels (long calls/puts → covered → spreads → naked)
- **Multi-leg**: spreads, straddles, strangles, condors, butterflies supported as of the 2025 release
- **Greeks, implied volatility, and risk analytics**: available via API; **no native options-chain UI or risk visualizer** comparable to tastytrade or IBKR TWS -- users bring their own frontend or use third-party tools
- **OCC direct clearing** as of 2025 (previously cleared via a correspondent)

### Crypto (Spot Only)

- **Entity**: Alpaca Crypto LLC
- **Coverage**: BTC, ETH, SOL, LTC, AVAX, DOGE, BCH, LINK, UNI, YFI, AAVE, SHIB, and other majors (coverage shifts with regulatory posture)
- **24/7** trading
- **Fees**: maker/taker tiered, historically in the 0.15%/0.25% range (verify at Alpaca's current schedule)
- **Stablecoin rails**: USDC supported as a funding currency for crypto accounts
- **No crypto perpetual futures, no crypto options, no leverage on crypto** -- spot only. This is the single biggest product gap relative to crypto-native venues; see [[alpaca-vs-hyperliquid]].

### What Alpaca does NOT offer

- **No crypto perpetual futures** or any crypto derivatives
- **No futures** (CME, etc.)
- **No FX** (spot or margin)
- **No bonds** directly to retail as of April 2026 (fixed-income is a 2025-2026 buildout via the FICC membership, initially for institutional/Broker-API partners)
- **No international equities** as a direct retail product

## API and Developer Experience

The developer experience is Alpaca's central product differentiator:

| Surface | Detail |
|---|---|
| **Trading API** | REST v2 and WebSocket streaming for orders, positions, account, quotes, trades |
| **Market Data API** | Separate endpoint; free tier is IEX-only, paid tier ("Algo Trader Plus", historically ~$99/mo) unlocks full SIP consolidated tape and historical bars |
| **Broker API** | B2B white-label product: create accounts, fund, trade, produce statements and tax docs under a partner's brand |
| **SDKs** | Official: `alpaca-py` (Python), `alpaca-ts` (TypeScript), Go, C#. Community SDKs for R, Rust, others |
| **Paper trading** | **Free** sandboxed environment with identical API surface -- the standout retail-friendly feature |
| **Order types** | Market, limit, stop, stop-limit, bracket, OCO, trailing stop |
| **Rate limits** | Standard plan: 200 requests/minute; Broker API and Algo Trader Plus have higher limits |
| **Webhooks / streaming** | WebSocket streams for order updates, quotes, trades, bars |
| **Ecosystem** | First-class integrations with [[quantconnect]], [[backtrader]], `vectorbt`, `lumibot`, `freqtrade` (equities module), Composer, MetaTrader bridges |

The Python SDK and paper trading together make Alpaca the default "getting started" broker for retail algo developers. There is no native GUI trading platform -- users either trade via the API, via third-party frontends (TradingView connections, Composer), or via Alpaca's minimal web dashboard.

## Fees Summary

| Product | Fee |
|---|---|
| US equities / ETFs | $0 commission |
| Options | $0 per contract |
| Crypto spot | ~0.15% maker / ~0.25% taker (tiered; verify current schedule) |
| Market data (free tier) | $0 -- IEX-only |
| Market data (paid, "Algo Trader Plus") | ~$99/month historical -- full SIP + unlimited historical |
| Margin rate | Base rate + tiered spread; historically lower than Robinhood, higher than IBKR Pro |
| Wire / ACH | Free ACH; wires carry standard fees |

## Jurisdictional Availability

- **Direct retail US brokerage** is the core product for US-resident clients
- **Non-US retail** is primarily routed through Broker API partner fintechs in their own jurisdictions (a partner in the UAE or Thailand embeds Alpaca; end users see the partner brand)
- Crypto availability is US-first with limited state-by-state coverage; some states remain restricted

## Regulatory and Operational

- **FINRA BrokerCheck**: Alpaca Securities LLC, CRD #288202
- **SIPC**: member (equities coverage up to standard SIPC limits)
- **OCC**: direct member as of 2025 (options clearing)
- **FICC**: direct member as of 2025 (fixed income clearing)
- **Nasdaq Exchange Member** as of 2025
- **Notable outages and incidents**: no large public enforcement actions as of April 2026; occasional API outages and data-feed disruptions are documented on their public status page but nothing approaching the scale of the March 2020 or GameStop-era incidents at other brokers

## Strengths

1. **Best-in-class developer experience** for US equity algo trading. The combination of free paper trading, a clean REST/WebSocket API, and a mature Python SDK is uniquely friendly to retail quant developers.
2. **Commission-free options with multi-leg support** as of 2025 -- $0 per contract undercuts IBKR ($0.65) and tastytrade ($1 open / $0 close).
3. **24/5 overnight equities trading** for US retail -- useful for algo strategies reacting to Asian/European news.
4. **Broker API ecosystem** -- if you are building a fintech, Alpaca is the closest thing to Stripe-for-brokerage.
5. **Low friction signup and funding** -- fast account opening, ACH funding, no account minimum for cash accounts.

## Weaknesses

1. **No crypto perpetual futures** -- disqualifying for crypto derivatives traders. See [[alpaca-vs-hyperliquid]].
2. **No futures, no FX, no international equities** -- single-market scope relative to [[interactive-brokers|IBKR]].
3. **No native options analytics UI** -- no risk graphs, no P&L curves, no options-chain visualizer. Users must build or source their own. [[tastytrade]] and IBKR TWS are dramatically ahead here.
4. **Options product is relatively new (2023/2025)** and the ecosystem around it (educational content, third-party options analytics, institutional volume data) is less developed than at tastytrade or IBKR.
5. **Execution quality** has been adequate but not a differentiator. Alpaca routes primarily via wholesale market makers; direct-market-access options comparable to IBKR Pro are not available.
6. **Data tier is bifurcated** -- the free IEX-only feed is insufficient for most serious work. Full-market data requires the paid subscription, which is cheap but is an additional step relative to IBKR's bundled market data.
7. **PDT rule applies** (standard FINRA rule for margin accounts < $25K) -- not unique to Alpaca but worth flagging for algo developers with small accounts.

## Who Should Use Alpaca

- **Retail algo developers on US equities** -- almost certainly yes. The paper-trading loop and SDK quality are hard to beat.
- **Retail options traders** -- only for specific workflows. If you want API-first options and are willing to build your own analytics, yes. If you want a polished options UI with streaming Greeks, no -- use [[tastytrade]] or IBKR TWS.
- **Crypto spot traders** -- acceptable for stock/crypto dollar-cost-averaging and simple algos. Fees are higher than crypto-native venues; no perps.
- **Crypto perp traders** -- no, period. Use [[hyperliquid]], [[dydx]], or [[binance|Binance Futures]]; see [[alpaca-vs-hyperliquid]].
- **Fintechs building embedded brokerage** -- likely yes; the Broker API is the primary product.

## Comparisons in this Wiki

- [[alpaca-vs-options-brokers]] -- Alpaca vs [[interactive-brokers]], [[tastytrade]], [[robinhood]] for options
- [[alpaca-vs-hyperliquid]] -- Alpaca vs [[hyperliquid]] for crypto perpetual futures

## Sources

- Alpaca corporate site -- https://alpaca.markets
- Alpaca developer docs -- https://docs.alpaca.markets
- Alpaca blog: "Alpaca Raises $150 Million at a $1.15B Valuation to Build the Global Standard for Brokerage Infrastructure" (2026-01-14)
- BusinessWire press release -- 2026-01-14
- Fortune -- "Alpaca fundraise Series D brokerage infrastructure" -- 2026-01-14
- FINRA BrokerCheck -- firm/summary/288202

## Related

- [[interactive-brokers]] -- the benchmark for professional API brokerage
- [[robinhood]] -- the retail zero-commission comparison point
- [[tastytrade]] -- the options-specialist comparison point
- [[oanda]] -- the forex/CFD API broker analogue
- [[tiger-brokers]] -- the regulated multi-asset broker analogue
- [[hyperliquid]] -- the crypto-native alternative for anything leveraged
- [[api-trading]], [[paper-trading]], [[algorithmic-trading-overview]] -- workflow concepts
