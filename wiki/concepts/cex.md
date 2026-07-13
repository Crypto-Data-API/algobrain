---
title: "Centralized Exchange (CEX)"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [crypto, exchange, market-microstructure, liquidity, regulation]
aliases: ["Cex", "CEX", "Centralized Exchange", "Centralised Exchange"]
domain: [market-microstructure]
prerequisites: ["[[order-books]]", "[[liquidity]]"]
difficulty: beginner
related: ["[[binance]]", "[[coinbase]]", "[[cex-vs-dex]]", "[[decentralized-exchanges]]", "[[order-books]]", "[[liquidity]]", "[[kyc]]", "[[self-custody]]", "[[market-microstructure]]", "[[perpetual-futures]]", "[[ftx]]"]
---

A **centralized exchange (CEX)** is a [[crypto-markets|cryptocurrency]] trading venue operated by a single company that custodies user funds, matches orders through an internal engine, and acts as the trusted intermediary between buyers and sellers. CEXs — [[binance]], [[coinbase]], OKX, Bybit, Kraken — dominate crypto trading volume and function much like traditional stock brokers combined with an exchange: they hold your assets, run [[kyc]], and operate a centralized [[order-books|order book]] matching engine.

## How a CEX works

1. **Deposit and custody.** Users send fiat or crypto to addresses controlled by the exchange. The exchange holds the private keys — "not your keys, not your coins." Balances are tracked in the exchange's internal ledger, not on-chain.
2. **Order matching.** A central limit order book (CLOB) matches bids and asks in a millisecond-latency matching engine, off-chain. Most trades are internal ledger updates, not blockchain transactions.
3. **Settlement.** Trades settle instantly within the exchange ledger; on-chain movement happens only on deposit/withdrawal.
4. **Market making and liquidity.** Professional market makers quote tight spreads on major pairs; the exchange may run incentive (maker-rebate) programs to deepen [[liquidity]].

## Why CEXs dominate

- **Liquidity and depth.** [[binance]]'s BTC/USDT book is among the deepest in the world; tight spreads and low [[slippage]] for large size.
- **Speed and UX.** Matching engines run in microseconds; polished apps, customer support, password recovery, and fiat on/off ramps lower the barrier for retail.
- **Product breadth.** Spot, margin, [[perpetual-futures]], options, staking, and lending under one login with advanced [[order-types]] and [[leverage]].
- **Price discovery.** Because most volume is centralized, CEX prints are the reference price most of the market quotes against (indices, oracles, and even many DEX oracles pull CEX data).

## Trading relevance

- **Counterparty risk is the defining hazard.** Because the exchange custodies funds, its failure is your loss. [[ftx|FTX]] (2022), Mt. Gox (2014), and Celsius all wiped out depositors. Sophisticated traders keep only active trading capital on a CEX and move long-term holdings to [[self-custody]].
- **Proof of reserves** became standard post-FTX, but a reserves snapshot does not prove the absence of undisclosed liabilities.
- **Listings move markets.** A CEX listing (especially Binance/Coinbase) is a documented short-term catalyst — the "Coinbase effect" — driving spikes in price and volume; delistings do the reverse.
- **Funding and basis.** CEX [[perpetual-futures]] [[funding-rate|funding rates]] are a real-time sentiment gauge and the leg in cross-venue [[arbitrage]] (e.g., CEX-vs-DEX funding divergence, CEX-vs-CME basis).
- **Regulatory and freeze risk.** A CEX can freeze accounts, block withdrawals, geofence jurisdictions, or be ordered to seize assets — a structural risk DEXs do not share.

## CEX vs DEX

The core tradeoff is **custody and trust model**: a CEX gives you depth, speed, support, and fiat rails in exchange for custodial and counterparty risk; a [[decentralized-exchanges|DEX]] gives you [[self-custody]], permissionless access, and on-chain transparency in exchange for [[smart-contracts]] risk and (often) thinner liquidity. See the full breakdown in [[cex-vs-dex]].

## Related

- [[binance]]
- [[coinbase]]
- [[cex-vs-dex]]
- [[decentralized-exchanges]]
- [[order-books]]
- [[liquidity]]
- [[kyc]]
- [[self-custody]]
- [[ftx]]
- [[perpetual-futures]]

## Sources

- [[cex-vs-dex]] — internal comparison of centralized vs decentralized venues.
- Binance / Coinbase exchange documentation — matching, custody, and listing processes.
- Financial Crisis-style post-mortems on FTX (CFTC/SEC complaints, 2022) — counterparty-risk case study.
