---
title: "bZx Flash Loan Attacks (2020)"
type: news
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [news, crypto, defi, hacks, exploits, security, flash-loans, history]
event_date: 2020-02-15
markets_affected: [crypto]
impact: high
verified: true
sources_count: 0
related: ["[[flash-loan-attacks]]", "[[oracle-manipulation]]", "[[smart-contract-risk]]", "[[defi]]", "[[flash-loan-arbitrage]]", "[[defi-hacks-and-exploits]]"]
---

The bZx flash loan attacks of February 2020 were the first high-profile exploits to weaponize [[flash-loan-attacks|flash loans]] — uncollateralized loans that must be borrowed and repaid within a single transaction. Two attacks on February 15 and 18 drained ~$1M from bZx (a decentralized margin trading protocol), but their real significance was conceptual: they proved that anyone could temporarily command millions in capital to manipulate DeFi protocols, without risking any of their own money. The bZx attacks launched flash loan exploits as a permanent category of DeFi risk.

## Attack 1: February 15, 2020 (~$350K profit)

The attacker executed a complex multi-protocol arbitrage within a single transaction:

1. **Flash-borrowed** 10,000 ETH from [[dydx]]
2. **Deposited** 5,500 ETH into [[compound]] as collateral, borrowing 112 WBTC
3. **Opened a 5x leveraged short** on ETH/BTC on bZx with the remaining 4,500 ETH — this caused bZx to sell a large amount of ETH for WBTC on [[uniswap]], crashing the ETH/BTC price on that venue
4. **Sold** the 112 WBTC on Uniswap at the now-inflated WBTC price (since bZx's trade had moved the market)
5. **Repaid** the 10,000 ETH flash loan
6. **Net profit**: ~$350K in a single transaction

The key insight: the attacker used bZx's own leveraged trade to move the price on Uniswap, then traded against that price movement on a different protocol. bZx was left holding an underwater margin position.

## Attack 2: February 18, 2020 (~$600K profit)

Three days later, a similar (possibly the same) attacker used an [[oracle-manipulation]] variant:

1. **Flash-borrowed** 7,500 ETH
2. **Manipulated** the sUSD price on Kyber Network by purchasing sUSD with a portion of the ETH
3. **Deposited** the pumped sUSD as collateral on bZx, which valued it at the manipulated price
4. **Borrowed** ETH against the inflated sUSD collateral
5. **Repaid** the flash loan, keeping the excess ETH
6. **Net profit**: ~$600K

This attack exploited bZx's reliance on a single DEX (Kyber) for price discovery — a thin oracle that could be moved with relatively small capital.

## Why These Attacks Mattered

### Flash Loans Democratized Exploits

Before flash loans, exploiting DeFi protocols required significant capital. The bZx attacks showed that *anyone* could borrow unlimited capital for the duration of one transaction, execute a complex exploit, and walk away with profit — all with zero upfront capital and zero liquidation risk. The attacker's only cost was gas fees.

### Oracle Design Was Exposed

Both attacks relied on protocols trusting spot prices from low-liquidity DEXs. bZx used Kyber's spot price as its oracle — a price that could be moved with a few million dollars of capital. This directly inspired the shift toward:

- **Time-weighted average prices (TWAPs)** — harder to manipulate within a single block
- **[[chainlink]]** and other decentralized oracle networks — aggregating prices across multiple sources
- **Multi-block oracle designs** — requiring manipulation to persist across multiple blocks

### The "DeFi Composability Risk" Concept

The attacks exploited the interaction between multiple protocols (dYdX, Compound, bZx, Uniswap, Kyber). Each protocol was individually secure, but their *composability* — the ability to chain them together in a single transaction — created emergent attack vectors that no single audit could catch.

## Aftermath

- bZx paused trading and eventually reimbursed affected users
- bZx was attacked again in November 2021 for $55M (private key compromise) and eventually wound down
- Flash loan attack tooling became standardized — Aave and dYdX flash loans became the default "capital source" for subsequent exploits
- The term "flash loan attack" entered the mainstream DeFi vocabulary

## Related

- [[flash-loan-attacks]] — the attack category pioneered by bZx
- [[oracle-manipulation]] — both attacks exploited weak oracle design
- [[flash-loan-arbitrage]] — the legitimate use of the same mechanism
- [[smart-contract-risk]] — composability risk as a subcategory
- [[defi-hacks-and-exploits]] — master timeline of DeFi exploits
- [[uniswap]] — used as the trading venue in attack 1
- [[compound]] — used as the lending venue in attack 1

## Sources

_Content based on public transaction analysis, bZx post-mortems, and PeckShield's real-time reporting. No raw sources ingested._
