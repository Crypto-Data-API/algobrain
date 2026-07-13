---
title: "Alpaca vs Hyperliquid for Crypto Perpetuals"
type: comparison
created: 2026-04-19
updated: 2026-04-19
status: good
tags: [comparisons, brokers, crypto, perps, derivatives, api-trading]
subjects: ["[[alpaca]]", "[[hyperliquid]]"]
comparison_dimensions: [product, custody, jurisdiction, leverage, fees, api, liquidity]
related: ["[[crypto-perpetual-futures]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[alpaca-vs-options-brokers]]", "[[hyperliquid-vs-dydx-vs-gmx]]", "[[dydx]]", "[[binance]]"]
---

# Alpaca vs Hyperliquid for Crypto Perpetuals

This is a deliberately asymmetric comparison. **[[alpaca]] does not offer crypto perpetual futures.** Its only crypto product is spot trading in a curated list of majors via Alpaca Crypto LLC, with no leverage and no derivatives. [[hyperliquid]] is a purpose-built L1 perpetuals DEX processing $400B+ in quarterly volume with up to 40-50x leverage on 229+ perp markets. The two platforms are not substitutes; they serve different users and different products. This page exists to make that clear and to document the tradeoffs for anyone who might confuse one for the other because both have "good APIs."

## The Core Mismatch

| Question | [[alpaca]] | [[hyperliquid]] |
|---|---|---|
| Does it offer crypto perpetual futures? | **No** | **Yes** -- the product IS perps |
| Does it offer any crypto leverage? | No | Yes, up to 40-50x |
| Does it offer crypto options? | No | No (but Deribit does) |
| Can you short crypto? | No -- spot only | Yes (and is the primary use case) |

If the question is "should I use Alpaca or Hyperliquid for crypto perps", the answer is Hyperliquid by default -- not because Hyperliquid is better, but because Alpaca is not a participant in the perps market. The relevant comparison for crypto perps is Hyperliquid vs [[dydx]] vs [[gmx]] (decentralized) or Hyperliquid vs [[binance|Binance Futures]] vs [[bybit]] (centralized). See [[hyperliquid-vs-dydx-vs-gmx]].

## What Alpaca Actually Offers in Crypto

- **Spot trading** in BTC, ETH, SOL, LTC, AVAX, DOGE, BCH, LINK, UNI, YFI, AAVE, SHIB, and other majors (coverage shifts with regulatory posture)
- **24/7 access** via the same REST/WebSocket API used for equities
- **Maker/taker fees** historically in the 0.15%/0.25% range -- higher than crypto-native venues, comparable to Coinbase retail
- **USDC funding** supported
- **Custody**: Alpaca-custodial, under Alpaca Crypto LLC
- **No leverage, no margin, no shorts, no perps, no futures, no options**

That is the full picture. For an algo developer who wants to DCA into BTC alongside an equities portfolio using the same API, Alpaca is fine. For anyone needing leverage, shorts, funding-rate exposure, or perp-basis trades, Alpaca is not a participant.

## What Hyperliquid Offers

- **Perpetual futures** on 229+ markets -- crypto majors, altcoins, and tradfi assets via HIP-3 permissionless markets
- **Leverage** up to 40-50x (tiered down at size)
- **Maker/taker fees** approximately 0.015% / 0.045% -- roughly 10x lower than Alpaca's spot crypto fees despite Hyperliquid being a leveraged derivative venue
- **Self-custody** -- users retain control of funds; Hyperliquid is non-custodial
- **No KYC** at the protocol level; US and Ontario are blocked at the interface level
- **On-chain CLOB** on a purpose-built L1, sub-200ms latency, 200,000 orders/sec
- **Mature API** with REST, WebSocket, Python SDK, hierarchical API keys, sub-accounts
- **Rich third-party bot ecosystem**: 3Commas, WunderTrading, Gunbot, Katoshi AI, etc.

See [[hyperliquid]] for full details.

## Jurisdictional Reality

This is the most important practical constraint:

- **US residents** cannot directly trade on Hyperliquid (the interface geo-blocks US IPs; VPN bypasses violate Hyperliquid's terms and likely US law). They *can* trade Alpaca crypto spot.
- **Non-US residents** can trade on Hyperliquid. Alpaca is technically available in 40+ countries via Broker API partners, but direct retail access from most non-US jurisdictions is less seamless.

For a US-based trader who wants crypto perps, the realistic options are:
1. Move offshore (legally complex)
2. Use CME crypto futures via a futures broker ([[interactive-brokers]], tastytrade, etc.) -- similar economic exposure but different market structure and higher minimums
3. Use equity ETF / ETN proxies ([[ibit]], [[bito]], etc.) -- no leverage, different risk profile
4. Accept the spot-only constraint and trade Alpaca, Coinbase, Kraken

None of these is a direct Hyperliquid substitute. The jurisdictional gate is real.

## API Comparison (If You're Choosing Between Them Anyway)

Even on pure developer experience, the products differ:

| Dimension | [[alpaca]] | [[hyperliquid]] |
|---|---|---|
| REST API | Yes, mature, HTTP/JSON | Yes, mature, HTTP/JSON |
| WebSocket streaming | Yes | Yes, lower latency |
| Python SDK | `alpaca-py` -- official, broad | `hyperliquid-python-sdk` -- official, thinner |
| Paper trading | **Yes** -- first-class free sandbox | Testnet available but less polished |
| Rate limits | 200 req/min free, higher on paid | Higher; gas-free order placement |
| Authentication | API key + secret | API key hierarchy with delegated signing |
| Order book depth | Limited (IEX free tier) | Full order book via WebSocket |
| Historical data | Paid (~$99/mo for full SIP) | Free on-chain historical data |
| Account model | Traditional brokerage account | Non-custodial wallet + sub-accounts |
| Tax reporting | Standard 1099s | None native -- user responsibility (complex) |

For a retail developer in a US jurisdiction, Alpaca's paper-trading loop and tax simplicity are genuine wins. For a non-US developer building a perps bot, Hyperliquid's free historical data and absence of data-subscription fees are wins.

## When Each Makes Sense

**Use [[alpaca]] when:**
- You are US-based and want crypto spot exposure inside an equities algo workflow
- You want tax-reported custodial crypto with standard 1099s
- You are dollar-cost-averaging into majors via API
- You are building a US-regulated fintech that needs embedded crypto spot

**Use [[hyperliquid]] when:**
- You want to trade perpetual futures
- You need leverage, shorts, funding-rate exposure, or basis trades
- You can legally access the platform (non-US / non-Ontario)
- You want the lowest-fee, highest-liquidity decentralized perps venue
- You are running systematic bots on funding-rate arbitrage, liquidation cascades, or market-making

## What About CME Crypto Futures via Alpaca?

Alpaca does not currently offer CME futures of any kind as of April 2026. The company's 2025 FICC membership is oriented toward fixed income, not futures. So even the "regulated US alternative to perps" path (CME micro BTC / ETH futures) is not available at Alpaca -- that requires [[interactive-brokers]] or a dedicated futures broker.

## Verdict

For crypto perpetual futures, Alpaca is not a candidate. Hyperliquid is a reasonable default for non-US traders; Binance Futures or Bybit for centralized alternatives; dYdX or GMX for different decentralized tradeoffs (see [[hyperliquid-vs-dydx-vs-gmx]]). Alpaca's crypto product is spot-only and should be evaluated against Coinbase Advanced, Kraken, and Gemini -- not against derivatives venues.

The single-sentence summary: **use Alpaca for equities and spot crypto; use Hyperliquid for perps. They are not competitors.**

## Related

- [[alpaca]], [[hyperliquid]] -- entity pages
- [[hyperliquid-vs-dydx-vs-gmx]] -- the relevant competitive comparison for perps
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] -- broader platform comparison
- [[crypto-perpetual-futures]], [[perpetual-futures]], [[funding-rate]] -- concept pages
- [[alpaca-vs-options-brokers]] -- where Alpaca actually competes
- [[dydx]], [[gmx]], [[binance]], [[bybit]] -- other perp venues
- [[interactive-brokers]] -- the fallback for US traders who want regulated crypto derivatives (via CME)
