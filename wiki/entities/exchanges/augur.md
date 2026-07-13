---
title: "Augur"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [crypto, defi, ethereum, event-driven]
aliases: ["Augur", "REP", "Augur Protocol"]
entity_type: protocol
founded: 2018
website: "https://www.augur.net"
related: ["[[polymarket]]", "[[prediction-markets]]", "[[ethereum]]", "[[gnosis]]", "[[uma]]"]
---

Augur is a decentralized [[prediction-markets|prediction market]] protocol built on [[ethereum|Ethereum]], launched in July 2018 by the Forecast Foundation. It pioneered the trustless, permissionless prediction-market design that [[polymarket|Polymarket]] and others later refined, using the REP (Reputation) token as the backbone of its staking-based oracle. Once the flagship of on-chain forecasting, Augur went dormant after 2021, eclipsed by Polygon-based and CLOB-style competitors — but a revival effort began in 2025, and in April 2026 the protocol's famous fork backstop was triggered for the first time in production.

## Overview / How It Works

Augur lets any user create a market on any future event — elections, sports, asset prices, arbitrary "yes/no" or scalar outcomes — without permission or a centralized matching engine. Markets trade as ERC-20 outcome shares (one per possible result) that pay 1 unit of collateral if their outcome resolves true, zero otherwise. A complete set of shares always sums to 1 unit of collateral, which makes pricing and arbitrage straightforward.

Resolution is handled off-chain by REP holders acting as decentralized oracles. After an event ends, a designated reporter posts an initial outcome; if disputed, REP holders stake tokens on competing outcomes through escalating dispute rounds. Mis-reporters lose their stake; honest reporters earn fees. In an irreconcilable dispute, the protocol forks: REP splits into outcome-specific universes, and holders must migrate to the universe they believe represents truth. The forking mechanic is the ultimate backstop and the source of REP's claim to oracle security.

## Key Milestones

| Date | Event |
|------|-------|
| 2014 | Augur whitepaper published by Jack Peterson and Joey Krug |
| 2015 | Token sale; ~$5.3M raised in REP |
| 2018-07 | V1 launched on Ethereum mainnet |
| 2018-2019 | Active election and sports markets; UX widely criticized for gas costs and slow resolution |
| 2020-07 | V2 launched: DAI as collateral (replacing ETH), invalid-outcome handling, 0x-based order book |
| 2020-11 | Volume peaks around the US presidential election |
| 2021+ | Sharp decline in active markets as [[polymarket|Polymarket]] (Polygon L2) captures retail flow |
| 2025 | Revival effort begins; new team resumes development around the dormant protocol |
| 2026-04 | The Augur fork is triggered — REP holders enter an 8-week escalation game / migration window (timeline posted 2026-04-09) |

## REP Token

REP (Reputation) is the work token used to secure Augur's oracle. Holders are not passive — REP only earns fees if actively staked on dispute outcomes during the reporting window. Key mechanics:

- **Initial reporting** — designated reporter posts the initial outcome and stakes REP as a bond.
- **Disputes** — any holder can dispute by staking REP on an alternative outcome. Each round doubles the required stake.
- **Forking** — if a dispute exceeds the dispute threshold, the universe forks into one child universe per possible outcome. REP holders must migrate; non-migrating REP becomes worthless in the parent.
- **Fees** — settled markets pay reporting fees pro-rata to correctly-staked REP.
- **REPv2** — the V2 migration introduced a new REP contract; legacy REP holders had to migrate. A non-trivial fraction of REP was never migrated, effectively shrinking active supply.

## Comparison to Polymarket

| Dimension | Augur | [[polymarket\|Polymarket]] |
|-----------|-------|----------------------------|
| Chain | Ethereum L1 | Polygon (L2) |
| Collateral | DAI (V2) | USDC |
| Oracle | REP staking + fork | [[uma\|UMA]] optimistic oracle |
| Order matching | On-chain 0x order book | Off-chain CLOB, on-chain settlement |
| Market creation | Permissionless, any user | Curated by Polymarket team |
| Typical fees | Gas-dominated, often >$10/trade in 2020 | Sub-cent on Polygon |
| Resolution speed | Days to weeks | Hours |
| Peak volume | ~$8M monthly (Nov 2020) | $1B+ monthly (2024 US election) |

The takeaway: permissionless market creation and a fork-based oracle are theoretically elegant but operationally painful. Polymarket's curated, L2, optimistic-oracle design dominated retail by sacrificing some decentralization for radically better UX.

## Decline / Current Status

Augur's volume collapsed after the 2020 election cycle. Causes:

- **Gas costs** — placing or settling a trade on Ethereum L1 routinely exceeded the EV of small bets.
- **Slow resolution** — designated-reporter windows plus dispute periods meant cash was locked up for days after an event ended.
- **UX friction** — wallet setup, DAI acquisition, and complex outcome-share mechanics gated mass adoption.
- **Competitor design** — [[polymarket|Polymarket]] on Polygon, then [[kalshi|Kalshi]] as a CFTC-regulated centralized venue, captured the audience.
- **Team departure** — co-founder Joey Krug joined [[pantera-capital|Pantera Capital]] as co-CIO; Forecast Foundation development slowed.

By 2024 the front-end was largely abandoned, market creation had dried up, and REP traded on thin liquidity primarily as a legacy asset.

## 2025-2026 Reboot and Fork

Twelve months into a revival effort that began in 2025, Augur is live again in a limited but consequential way. As of June 2026, `augur.net` describes the protocol as being "in week 5 of an 8-week Escalation Game — a profit-driven dispute mechanism where REP holders stake against an attacker until one side runs out of capital or the fork backstop activates." The fork has been formally triggered, and REP holders (both REPv1 and REPv2 still trade on Kraken, Uniswap, and other venues) were given a migration window — the timeline was posted on 2026-04-09, with roughly two months to migrate after the fork resolves.

This is historically significant: the fork backstop was the centerpiece of Augur's oracle-security argument since the 2014 whitepaper but had never been exercised in production. Whether the escalation game resolves cleanly will be the first real-world test of fork-based oracle security. Economically the protocol remains tiny — REP traded around $0.83-0.97 with ~11M circulating supply in mid-2026 (CoinMarketCap) — so this is a design experiment, not a liquid market.

## Trading Relevance

Augur matters today for three reasons:

1. **Historical lessons** — Augur is the canonical case study in why decentralization without UX kills retail adoption. Any analysis of [[prediction-markets|prediction-market]] design choices, oracle trade-offs, or DeFi product-market fit references Augur.
2. **Cross-venue arbitrage history** — during 2020, the same election markets traded simultaneously on Augur, [[polymarket|Polymarket]], FTX, and PredictIt at meaningfully different prices. Spreads of 3-8 percentage points were common, but Augur's gas costs often ate the edge for retail-sized trades. This is the original template for the [[prediction-market-strategies|prediction-market arbitrage]] playbook now applied across [[polymarket|Polymarket]] / [[kalshi|Kalshi]].
3. **Oracle-design reference** — Augur's fork mechanic remains the most security-maximalist oracle design shipped to mainnet, and is a comparison point for [[uma|UMA]]'s optimistic oracle and other dispute-game systems.

REP itself is not a useful trading vehicle in 2026 — too thin, no protocol revenue — though the live 2026 fork/escalation game is a binary event some speculators are watching (a clean fork resolution would validate the oracle design; a messy one would likely finish the token).

## Related

- [[polymarket]]
- [[kalshi]]
- [[prediction-markets]]
- [[prediction-market-strategies]]
- [[polymarket-vs-kalshi]]
- [[ethereum]]
- [[gnosis]] — competing prediction-market protocol (conditional tokens framework)
- [[uma]] — optimistic oracle used by Polymarket

## Sources

- Augur whitepaper (Jack Peterson & Joey Krug, 2014) — https://arxiv.org/abs/1501.01042
- Augur official site (reboot, fork, and migration status) — https://www.augur.net (accessed 2026-06-10)
- CoinMarketCap — REP price and supply data — https://coinmarketcap.com/currencies/augur/
- Kraken Learn, "What is Augur (REP)?" — https://www.kraken.com/learn/what-is-augur-rep
- Verified via Perplexity (sonar) and direct fetch of augur.net, 2026-06-10
