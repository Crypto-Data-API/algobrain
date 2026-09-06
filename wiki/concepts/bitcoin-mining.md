---
title: "Bitcoin Mining"
type: concept
created: 2026-07-19
updated: 2026-09-06
status: good
tags: [crypto, bitcoin, on-chain, energy]
aliases: ["Bitcoin Miners", "BTC Mining", "Hashrate", "Hash Price", "Hashprice"]
domain: [market-microstructure]
prerequisites: ["[[proof-of-work]]", "[[bitcoin]]"]
difficulty: intermediate
related: ["[[proof-of-work]]", "[[bitcoin-halving]]", "[[miner-capitulation-bottom]]", "[[on-chain-analysis]]", "[[consensus-mechanism]]", "[[mara]]", "[[hut-8]]", "[[core-scientific]]", "[[bitdeer-technologies]]", "[[cryptodataapi-on-chain]]"]
---

# Bitcoin Mining

**Bitcoin mining** is the process by which specialized computers compete to solve [[proof-of-work|Proof-of-Work]] puzzles, securing the [[bitcoin|Bitcoin]] network and earning newly issued BTC plus transaction fees in return. Miners are Bitcoin's decentralized security budget: the aggregate computing power they point at the network (**hashrate**) is what makes rewriting Bitcoin's transaction history economically infeasible. Because miner revenue is BTC-denominated while their costs (hardware, electricity, hosting) are fiat-denominated, mining economics create a legible, trackable cost structure that shows up on-chain as hashrate, difficulty, and reserve-balance signals — most notably in the miner-capitulation dynamics this page covers.

## How Mining Secures the Network

Bitcoin's [[proof-of-work|Proof-of-Work]] consensus asks miners to repeatedly hash a candidate block's header, searching for a value below a network-set target — a computationally expensive search with no shortcut except raw hashing throughput. The first miner to find a valid hash broadcasts the block; every other node can verify the solution almost instantly. Because finding a valid block is hard but checking one is easy, the network converges on a single canonical chain without needing to trust any individual participant. Attacking the chain — rewriting confirmed history — would require out-hashing the rest of the honest network combined (the "51% attack" threshold), which at Bitcoin's current scale would cost far more in hardware and electricity than any plausible payoff. See [[proof-of-work]] for the general mechanism and [[consensus-mechanism]] for how it compares to other designs.

## Hashrate and the Difficulty Adjustment

**Hashrate** is the aggregate computing power (measured in hashes per second, at Bitcoin's scale now exahashes/second, EH/s) that miners collectively point at the network. It rises as miners add or upgrade equipment and falls as they power down unprofitable rigs — making it a real-time proxy for miner participation and, by extension, miner economic health.

Bitcoin's protocol targets a **10-minute average block time** regardless of how much hashrate is competing, by adjusting a **difficulty** parameter every **2,016 blocks** (roughly two weeks at the target block time). If blocks were found faster than 10 minutes on average over that window (hashrate rose), difficulty increases for the next period; if blocks were found slower (hashrate fell), difficulty decreases. This retarget is mechanical and lagged — it reacts to the *prior* two weeks of hashrate, not the current instant — which is precisely why a hashrate shock (miners rapidly capitulating or a regional ban forcing mass shutdowns) shows up first as slower block production and only later as a difficulty correction. That lag is the structural basis of the Hash Ribbons indicator described below.

## Miner Revenue: Block Reward Plus Fees

A miner's revenue per block has two components:

1. **Block subsidy** — newly minted BTC paid to the miner who finds a valid block, currently 3.125 BTC after the 2024 event and halving on a fixed schedule roughly every four years. See [[bitcoin-halving]] for the full schedule, supply-shock thesis, and the ETF-era debate over whether the halving still moves price the way it did pre-2024.
2. **Transaction fees** — fees paid by users to have their transactions included, which the miner also collects. Fees are a small share of total miner revenue in most periods but spike during periods of high on-chain demand (congestion, ordinals/inscriptions activity, or exchange-driven settlement waves).

Because the subsidy is fixed by protocol and halves on a known schedule while fees float with demand, miner revenue is only partially within miners' control — a structural fact that drives the mining-economics discussion below and, over the long run, means transaction fees must eventually replace the subsidy as the dominant component of network security spending as issuance approaches zero.

## Mining Economics: ASICs, Energy, and Hash Price

Bitcoin mining today is dominated by **ASICs** (Application-Specific Integrated Circuits) — chips designed to do nothing but compute Bitcoin's SHA-256 hash function as fast and efficiently as possible; general-purpose GPUs stopped being competitive years ago. A miner's all-in cost per BTC mined is driven by three inputs:

- **Hardware cost and efficiency** — the purchase price of ASIC rigs and their efficiency, measured in joules per terahash (J/TH); newer-generation machines produce more hashrate per watt, which is why older fleets become unprofitable first as the network's average efficiency improves.
- **Energy cost** — the price paid per kilowatt-hour, which varies enormously by region and contract type (fixed industrial rate, curtailable/demand-response deals, stranded or flared-gas power). Energy is typically the largest recurring operating cost for an industrial miner.
- **Hosting, debt service, and overhead** — data-center hosting fees, financing costs on rig purchases, and general operating overhead layer on top of energy.

The standard industry metric that ties all of this together is **hash price** (sometimes "hashprice"): the USD revenue a miner earns per unit of hashrate per day (commonly quoted per petahash/second, $/PH/s/day), computed from the current block reward plus average fees, the BTC/USD price, and total network difficulty/hashrate. Hash price is the cleanest single number for miner profitability because it normalizes for network-wide competition — as more hashrate joins the network, the same fixed daily BTC issuance is split more ways, mechanically pushing hash price down even if BTC's dollar price is unchanged. A miner's **breakeven hash price** is the level at which their all-in costs (energy + overhead, amortizing hardware) exactly equal their revenue; miners with efficient, cheap-power operations have a lower breakeven than older or high-cost-power operations, which is the entire basis of the capitulation dynamic below.

## Miner Capitulation Dynamics

When hash price falls below a miner's breakeven — because BTC's price drops, network hashrate/difficulty rises, or the miner's own energy costs increase — that miner is losing money on every block it mines. The response happens in stages:

1. **Forced reserve selling.** A stressed miner first sells accumulated BTC reserves to cover fiat-denominated bills (electricity, hosting, debt service), which shows up on-chain as declining miner wallet balances.
2. **Shutdown.** If losses persist and reserves run out, the miner powers off some or all of its rigs rather than mine at a loss. This is **miner capitulation** proper — the highest-cost, least efficient operators exit first.
3. **Hashrate decline, then a lagged difficulty drop.** As enough miners shut down, network hashrate falls. Because difficulty only retargets every 2,016 blocks, there is a lag during which the survivors mine faster relative to the (still-too-high) difficulty, improving their own economics even before the official adjustment — and once the retarget does land, breakeven hash price for the survivors falls further.
4. **Exhaustion and stabilization.** Once the highest-cost miners have capitulated and difficulty has adjusted down, the remaining miners face an easier cost curve. Historically, hashrate stabilizing and then recovering after a capitulation episode has coincided with the tail end of deep bear markets — the underlying thesis behind the **[[miner-capitulation-bottom]]** strategy page, which builds a full trading signal (Hash Ribbons, the Puell Multiple, and miner-reserve stabilization) around exactly this mechanism. Read that page for the honest small-sample caveats: it explicitly does *not* treat capitulation as a precise bottom-caller, and flags that spot-ETF demand and better-capitalized public miners since 2024 may be dampening the classic forced-selling dynamic.

The standard on-chain tool for tracking this cycle is the **Hash Ribbon** — a moving-average crossover of network hashrate (commonly the 30-day vs. 60-day average). A cross of the short average below the long average flags capitulation (hashrate rolling over); a cross back above flags recovery. See [[on-chain-analysis#Miner Metrics]] for the mechanics of the Hash Ribbon, miner reserves, and the Puell Multiple as a family of related miner-stress indicators.

Not every hashrate decline reflects economic capitulation — regional mining bans, weather, and power-grid curtailment events can knock hashrate down for reasons unrelated to price (the 2021 China mining ban is the canonical example, cutting global hashrate by roughly half with no corresponding price bottom). This is exactly why [[miner-capitulation-bottom]] treats Hash Ribbon recovery as one confluence input rather than a standalone signal.

## Public and Industrial Miners

Since Bitcoin's early years, mining has consolidated from individual hobbyists into large industrial operations and, increasingly, publicly listed companies with balance-sheet access to capital markets — [[mara|MARA Holdings]], [[core-scientific|Core Scientific]], [[hut-8|Hut 8]], [[bitdeer-technologies|Bitdeer]], and other listed miners the wiki covers under `wiki/entities/companies/`. A notable structural shift since roughly 2024-2025 is that several of these operators have begun converting mining infrastructure (power contracts, data-center sites) toward AI/HPC hosting and GPU colocation, on the thesis that contracted, dollar-denominated AI compute revenue is more stable than BTC-priced, difficulty-eroded mining revenue — see [[bitdeer-technologies]] for a concrete example. This diversification, alongside larger balance-sheet buffers and hedging capability at public miners, is part of why [[miner-capitulation-bottom]] flags the classic forced-capitulation mechanism as potentially weaker in the current era than it was in earlier cycles.

## Trading Relevance

- **Hashrate and difficulty trends** are a real-time, public proxy for aggregate miner health and confidence — a rolling hashrate decline is an early signal worth cross-checking against price action, not a standalone trade trigger.
- **Hash price** is the cleanest single miner-profitability number; tracking it against known ASIC-fleet efficiency and regional energy costs gives a rough read on how much of the miner population is underwater at a given BTC price.
- **Miner reserves and Hash Ribbon state** feed directly into the [[miner-capitulation-bottom]] accumulation signal, and into the broader on-chain regime framework in [[on-chain-analysis]].
- **The halving is a scheduled miner-revenue shock**, instantly halving block-subsidy income and tightening the cost squeeze on high-cost operators without any price move — see [[bitcoin-halving]] for the schedule and historical aftermath.
- **Public miners are an equity proxy** for mining-sector stress or the AI/HPC pivot, distinct from (but correlated with) direct on-chain miner metrics.

## Getting the Data (CryptoDataAPI)

[[cryptodataapi|CryptoDataAPI]]'s On-Chain Intelligence category carries verified miner-specific endpoints (see [[cryptodataapi-on-chain]] for the full category).

**Live data:**
- `GET /api/v1/on-chain/miners/reserves` — BTC miner pool reserves and flows (Foundry, AntPool, F2Pool, ViaBTC, Binance Pool)
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (30-day vs. 60-day hashrate moving average): capitulation / recovery / normal
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV and supply-shock zone classification, useful confluence context alongside miner stress
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/miners/hash-ribbon"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]]. For the complete confluence signal built on these endpoints (including a backtesting-archive route and regime gate), see the [[miner-capitulation-bottom|AI agent workflow]] on the miner-capitulation strategy page.

## Related

- [[proof-of-work]] — the consensus mechanism mining performs
- [[bitcoin-halving]] — the scheduled block-subsidy reduction that halves miner revenue roughly every four years
- [[miner-capitulation-bottom]] — the full trading signal built on Hash Ribbons, the Puell Multiple, and miner-reserve stabilization
- [[on-chain-analysis]] — mechanics of the Hash Ribbon, Puell Multiple, and other miner metrics
- [[consensus-mechanism]] — how Proof-of-Work compares to Proof-of-Stake and other designs
- [[mara]], [[hut-8]], [[core-scientific]], [[bitdeer-technologies]] — publicly listed industrial miners
- [[cryptodataapi-on-chain]] — the verified data category behind the endpoints above

## Sources

- [[proof-of-work]], [[on-chain-analysis]], [[bitcoin-halving]] — wiki concept pages cross-checked for consistency (block-time target, difficulty-adjustment cadence, halving schedule, Hash Ribbon/Puell Multiple definitions)
- [[miner-capitulation-bottom]] — wiki strategy page cross-checked to avoid contradicting its edge framing, null-hypothesis caveats, and ETF-era dampening thesis
- [[cryptodataapi-on-chain]] — wiki source page verifying the `/on-chain/miners/reserves` and `/on-chain/miners/hash-ribbon` endpoints against https://cryptodataapi.com/api/docs
- [[bitdeer-technologies]] — wiki entity page for the AI/HPC pivot example among public miners
- General knowledge of Bitcoin mining mechanics (ASIC economics, hash price as an industry-standard profitability metric, the 2021 China mining ban) cross-checked against the cited wiki pages; no specific external source document has been ingested for this page
