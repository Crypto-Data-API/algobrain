---
title: "Ethereum Classic"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, history]
aliases: ["ETC"]
entity_type: protocol
founded: 2015
headquarters: "Decentralized"
website: "https://ethereumclassic.org"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[proof-of-work]]", "[[the-dao-hack]]"]
---

# Ethereum Classic

**Ethereum Classic** (ETC) is the original Ethereum chain that refused to reverse [[the-dao-hack|the 2016 DAO hack]], continuing as a proof-of-work smart-contract platform with a fixed supply cap (~210.7M ETC) after [[ethereum|Ethereum]] itself moved to proof-of-stake. For traders, ETC is a liquid, perpetually-listed legacy L1 known for violent narrative-driven squeezes (it absorbed most of Ethereum's displaced PoW hashrate after the 2022 Merge) and now has two dated 2026 catalysts: the **"fifthening" block-reward cut (Aug–Oct 2026)** and the **Olympia treasury upgrade targeting mainnet by end-2026**.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ETC |
| **Market Cap Rank** | #63 (2026-06-20) |
| **Market Cap** | ~$1.17B (2026-06-20) |
| **Genesis Date** | 2015-07-30 (Ethereum genesis; ETC split at block 1,920,000 in July 2016) |
| **Consensus** | [[proof-of-work\|Proof of Work]] (Etchash) |
| **Hashrate** | broke above 300 TH/s in 2025 and held into 2026; ~90–95% of all Ethash/Etchash-family hashpower |
| **Supply mechanics** | Hard cap 210.7M ETC; ~156.6M circulating; block reward declines 20% every 5M blocks ("fifthening") |
| **Website** | [https://ethereumclassic.org](https://ethereumclassic.org) |

---

## Market Data

| Metric | Value |
|---|---|
| **Current Price** | $7.50 |
| **Market Cap** | $1,174,442,387 (~$1.17B) |
| **Market Cap Rank** | #63 |
| **Fully Diluted Valuation** | $1,174,442,387 (~$1.17B) |
| **Market Cap / FDV** | 1.00 (no unlock overhang) |
| **24h Volume** | $78,393,730 (~$78.4M) — Vol/MC 6.67% |
| **24h Change** | +5.34% |
| **7d Change** | +4.91% |
| **Circulating Supply** | 156,559,601 ETC |
| **Total Supply** | 156,559,601 ETC |
| **Max Supply** | 210,700,000 ETC (74.3% mined) |
| **All-Time High** | $167.09 (2021-05-06) — −95.51% |
| **All-Time Low** | $0.6150 (2016-07-25) — +1,119.22% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Backdrop (2026-06-20):** the [[crypto-markets|crypto market]] sits in **extreme fear** (Fear & Greed Index = 23) inside an **Established Bear Market** regime. Against that fearful tape, ETC printed **+5.34% on the day** and **+4.91% on the week** — notable *relative strength*, consistent with its long-standing character as a catalyst-reactive squeeze vehicle (see [[#Trading Playbook]]). Spot turnover of ~$78M (Vol/MC ≈ 6.7%) is healthy for a legacy L1, keeping ETC genuinely liquid even in a risk-off market.

> *April 2026 reference: a CoinGecko snapshot on 2026-04-09 showed ~$8.39 / ~$1.31B MC; figures above supersede it.*

---

## Overview

Ethereum Classic emerged from the July 2016 chain split after the DAO hack: the majority forked to reverse the theft (today's Ethereum), while ETC preserved the original "code is law" ledger. It remains a Layer 1 smart-contract platform secured by proof of work, with a Bitcoin-style monetary policy: a fixed maximum supply of 210.7M ETC and a 20% emission reduction ("fifthening") every 5 million blocks.

After Ethereum's September 2022 Merge, ETC became the dominant destination for displaced Ethash GPU/ASIC hashpower, making it the most-secured PoW smart-contract chain by a wide margin.

---

## Protocol / Technology

**Origin — the original Ethereum chain.** ETC is not a clone or fork-of-convenience; it is the *continuation of the original Ethereum ledger*. Both chains share the same genesis block (2015-07-30) and identical history up to block **1,920,000** in July 2016. At that block, the community split over how to handle [[the-dao-hack|the DAO hack]] — an exploit that drained ~3.6M ETH from The DAO smart contract.

**"Code is law."** The majority (today's [[ethereum|Ethereum]]) executed a controversial hard fork to *reverse* the theft and refund DAO investors. A minority rejected protocol-level intervention on the grounds that an immutable ledger must honour the outcomes of deployed code — **"code is law"** — and continued the unaltered chain as **Ethereum Classic**. This philosophical stance (immutability over interventionism) remains ETC's defining identity and underpins its "ungovernable, credibly-neutral smart-contract chain" positioning.

**Consensus — [[proof-of-work]] (Etchash).** ETC is secured by Etchash, a tweaked Ethash variant (DAG size adjusted to limit ASIC monopolisation), mined by GPUs and Ethash ASICs. This is the sharpest technical divergence from [[ethereum]]: when Ethereum completed **The Merge** (September 2022) and switched to [[proof-of-stake]], the entire Ethash mining industry was orphaned overnight. A large share of that displaced hashpower migrated to ETC, the largest remaining Ethash-family chain. Etchash hashrate **broke above 300 TH/s in 2025 and held into 2026**, with ETC commanding ~90–95% of all Ethash/Etchash-family hashpower — making it the most-secured PoW smart-contract chain by a wide margin.

**51%-attack history and defenses.** Before the Merge, ETC's modest hashrate made it economically attackable. It suffered **three 51% / chain-reorganization attacks in August 2020**. In response the community deployed **MESS (Modified Exponential Subjective Scoring)**, a defensive finality-confidence mechanism that penalizes deep reorgs, and the post-Merge hashrate influx since 2022 has structurally raised the cost of any future attack by orders of magnitude. The attack history nonetheless remains a permanent risk marker for traders (see [[#Risks]]).

**EVM compatibility.** ETC runs the Ethereum Virtual Machine and broadly tracks Ethereum's protocol upgrades through its own ECIP (Ethereum Classic Improvement Proposal) process, so Solidity contracts and EVM tooling port across — though the on-chain application ecosystem is far thinner than Ethereum's.

**Olympia upgrade (the funding/treasury redesign).** The **Olympia Upgrade (ECIPs 1111–1114)**, proposed mid-2025, is the most significant protocol change since the fork. It activates **EIP-1559 base-fee burning** and redirects **80% of the burned base fee into an on-chain treasury contract**, governed by a native DAO where ETC holders vote on Ethereum Classic Funding Proposals (ECFPs). This is designed to fix ETC's chronic development-funding problem (it has long lacked a foundation endowment or block-reward dev tax). The governance layer is live on testnet as of spring 2026, with **mainnet activation targeted for end of 2026** — a rare, dated protocol catalyst.

---

## Tokenomics & Supply

ETC runs a **Bitcoin-style disinflationary monetary policy** — a deliberate contrast to [[ethereum]]'s uncapped (and post-Merge, fee-burn-variable) issuance, and a core pillar of its store-of-value pitch:

- **Hard cap: 210.7M ETC** — a fixed maximum supply (deliberately echoing [[bitcoin]]'s capped scarcity, scaled up ~10×).
- **"Fifthening": −20% emission every 5M blocks.** The block reward steps down by one-fifth every 5,000,000 blocks (≈ every ~2.5 years). The **next fifthening falls in August–October 2026**, cutting the block reward from **2.048 → 1.6384 ETC** — a dated, supply-side catalyst.
- **Circulating ≈ total (156.6M), MC/FDV = 1.00.** There is **no token-unlock overhang, no team/VC vesting cliff, no foundation treasury dumping** — the only ongoing sell pressure is organic **miner sell pressure** (miners liquidating coinbase rewards to cover electricity/hardware). At ~74.3% of max supply mined, remaining issuance is the slow, predictable PoW emission curve.
- **Post-Olympia:** EIP-1559 base-fee burning will, for the first time, introduce a *deflationary* offset proportional to network usage — though with ETC's thin on-chain activity, burn volumes will be modest near-term.

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Circulating Supply** | 156,559,601 ETC |
| **Total Supply** | 156,559,601 ETC |
| **Max Supply** | 210,700,000 ETC |
| **% of max mined** | ~74.3% |
| **Fully Diluted Valuation** | $1.17B |
| **Market Cap / FDV Ratio** | 1.00 |
| **Next fifthening** | Aug–Oct 2026 (2.048 → 1.6384 ETC, −20%) |

---

## Ecosystem & Use Cases

ETC is best understood not as a vibrant application platform but as an **"ungovernable PoW smart-contract chain" and PoW store-of-value**:

- **Thin DeFi/app ecosystem.** Despite EVM compatibility, ETC hosts minimal DeFi TVL and few flagship dApps relative to [[ethereum]]. The immutability ethos that defines it also deters the rapid, intervention-friendly development culture that grew Ethereum's ecosystem.
- **Mining economy.** ETC's largest real economic activity is mining itself — it is the principal home for stranded/legacy Ethash GPU and ASIC capacity post-Merge. Hashrate, difficulty, and miner profitability are first-order on-chain fundamentals.
- **Store-of-value / credibly-neutral settlement.** The fixed 210.7M cap, "code is law" immutability, and dominant PoW security combine into a niche narrative: a smart-contract chain that *cannot* be socially re-organized — appealing to maximalists who view Ethereum's fork as the original sin.
- **Olympia → on-chain funding.** Once live, the treasury DAO could seed an ecosystem-development flywheel, the single biggest swing factor for ETC's long-run utility.

## 2025–2026 Developments

- **Olympia Upgrade (ECIPs 1111–1114)** — proposed mid-2025, the most significant protocol change since the fork: activates **EIP-1559** fee burning and redirects **80% of the burned base fee into an on-chain treasury contract**, governed by a native DAO where ETC holders vote on funding proposals (ECFPs). The governance layer is live on testnet as of spring 2026, with **mainnet activation targeted for end of 2026**. This addresses ETC's chronic development-funding problem.
- **Hashrate strength**: Etchash hashrate broke 300 TH/s in 2025 and held steady through 2026.
- **Next fifthening: August–October 2026** — block reward drops from 2.048 to 1.6384 ETC (-20% new supply), a dated supply-side catalyst.
- Price remained deeply depressed: **-95.51% from the May 2021 ATH ($167.09)** — at **$7.50 on 2026-06-20** — though ETC outperformed the fearful tape with a +5.34% session and +4.91% week.

## Market Structure & Derivatives

- **Spot venues**: top-tier liquidity everywhere — Binance (ETC/USDT), Kraken (ETC/USD), Upbit (ETC/KRW), Coinbase (a Coinbase 50 Index constituent), Bitget, KuCoin, Crypto.com. ~**$78.4M daily spot/total volume (2026-06-20)**, Vol/MC ≈ 6.7% — genuinely liquid for a legacy L1 even in a risk-off market.
- **Derivatives**: ETC-PERP perps on [[hyperliquid|Hyperliquid]] and all major CEX perp venues (Binance, Bybit, OKX). As a high-short-interest, catalyst-reactive name, ETC's [[perpetual-futures|perpetual futures]] funding tends to oscillate sharply — it can flip deeply negative as shorts crowd in during quiet drift, which is precisely the fuel for the short-squeeze pops ETC is famous for. Watch funding + open interest extremes around the dated 2026 catalysts.
- **Trading character**: **low-beta drift punctuated by violent squeezes** — historically a favorite squeeze/rotation vehicle (the 2021 retail mania to $167, Merge-era PoW-narrative pops). High short interest plus thin conviction ownership make it reactive to catalyst headlines; in the absence of catalysts it tends to bleed against [[bitcoin]] and [[ethereum]].

---

## Valuation Framework

ETC has **no cash flows, no protocol fee accrual to holders (pre-Olympia), and a near-zero DeFi economy** — there is nothing to discount. It is valued instead on a stack of qualitative anchors:

- **Security/scarcity narrative** — dominant PoW hashrate (~300 TH/s, ~90–95% of Ethash family) plus a hard 210.7M cap support a "credibly-neutral, immutable, Bitcoin-style smart-contract chain" thesis.
- **Beta to majors** — ETC is a high-beta proxy for [[ethereum]] and [[bitcoin]]; absent idiosyncratic news it largely follows the majors, amplified on the way up and down.
- **Catalyst optionality** — the **fifthening (Aug–Oct 2026)** supply cut and **Olympia mainnet (target end-2026)** funding upgrade are rare *dated* events that can re-rate the asset independent of the broad tape.
- **Drawdown context** — at $7.50 it sits **−95.51% from its $167.09 ATH**; deep-value mean-reversion bulls weigh this against the structural reality of a thin ecosystem.

---

## Trading Playbook

- **Event-driven pre-positioning** ([[event-driven]]): accumulate ahead of the **fifthening** and **Olympia mainnet**, then **fade the sell-the-news** — ETC's dated catalysts historically run up into the event and reverse after.
- **Squeeze plays**: monitor [[perpetual-futures|perp]] funding and open-interest extremes; deeply negative funding + rising OI flags crowded shorts that catalyst headlines can violently squeeze.
- **ETH/ETC ratio pair trade**: ETC's identity is defined *relative* to [[ethereum]]; the ETH/ETC ratio is a cleaner expression of the PoW-vs-PoS and immutability narratives than an outright ETC long, and strips out broad market beta.
- **Beta sizing**: in extreme-fear regimes (like 2026-06-20), ETC's relative-strength days can mark short-covering rather than trend — size as a tactical/speculative beta bet, not a core hold.

---

## History

| Date | Event |
|---|---|
| 2015-07-30 | Ethereum genesis (shared origin of ETH and ETC) |
| 2016-07 | [[the-dao-hack\|DAO hack]] reversal hard fork; chain splits at block 1,920,000 — ETC continues the unaltered "code is law" ledger |
| 2016-07-25 | All-time low $0.6150 |
| 2020-08 | Three 51% / reorg attacks within the month; MESS defense subsequently deployed |
| 2021-05-06 | All-time high $167.09 amid retail mania |
| 2022-09 | [[ethereum\|Ethereum]] Merge to [[proof-of-stake]]; displaced Ethash hashpower migrates to ETC |
| 2025 | Etchash hashrate breaks 300 TH/s; Olympia upgrade (ECIPs 1111–1114) proposed |
| 2026 (spring) | Olympia governance live on testnet; mainnet targeted end-2026 |
| 2026-08→10 | Next fifthening: block reward 2.048 → 1.6384 ETC |
| 2026-06-20 | $7.50, MC ~$1.17B (#63); +5.34% on the day vs an extreme-fear tape |

---

## Competitive Positioning

ETC's peer set is best framed as **(a) its sibling [[ethereum]]** and **(b) the PoW store-of-value reference, [[bitcoin]]**:

| Dimension | **ETC (Ethereum Classic)** | [[ethereum\|ETH (Ethereum)]] | [[bitcoin\|BTC (Bitcoin)]] |
|---|---|---|---|
| **Consensus** | [[proof-of-work\|PoW]] (Etchash) | [[proof-of-stake\|PoS]] (post-Merge) | [[proof-of-work\|PoW]] (SHA-256) |
| **Supply policy** | Hard cap 210.7M, fifthening −20%/5M blocks | Uncapped; net issuance varies with EIP-1559 burn | Hard cap 21M, halving −50%/210k blocks |
| **Smart contracts** | EVM (thin ecosystem) | EVM (largest ecosystem) | Limited scripting (no general EVM) |
| **Core ethos** | Immutability — "code is law" | Pragmatic, upgrade-driven | Sound money / immutability |
| **Market cap (2026-06-20)** | ~$1.17B (#63) | Mega-cap (top 2) | Mega-cap (#1) |
| **Trader role** | High-beta squeeze/catalyst proxy | Blue-chip L1 | Macro reserve / beta anchor |

The takeaway: ETC offers Ethereum-like *technology lineage* with Bitcoin-like *monetary scarcity and PoW security*, but with a fraction of either's liquidity, ecosystem, or mind-share — its edge is narrative/catalyst optionality, not fundamentals.

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | ETC/USDT |
| Kraken | ETC/USD |
| Upbit | ETC/KRW |
| Bitget | ETC/USDT |
| KuCoin | ETC/USDT |
| Crypto.com Exchange | ETC/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ETC-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ethereumclassic.org](https://ethereumclassic.org) |
| **Twitter** | [@ETC_Network](https://twitter.com/ETC_Network) |
| **Reddit** | [https://www.reddit.com/r/EthereumClassic](https://www.reddit.com/r/EthereumClassic) |
| **Discord** | [https://ethereumclassic.org/discord](https://ethereumclassic.org/discord) |
| **GitHub** | [https://github.com/ethereumclassic](https://github.com/ethereumclassic) |

## Developer Activity

| Metric | Value (April 2026) |
|---|---|
| **GitHub Stars** | 193 |
| **GitHub Forks** | 244 |
| **Commits (4 weeks)** | 17 |
| **Contributors** | 17 |

---

## Risks

- **51%-attack history** — ETC was 51%-attacked three times in August 2020. Post-Merge hashrate (~300 TH/s) and MESS defenses have raised the attack cost by orders of magnitude, but the precedent is a permanent risk marker, and any sustained hashrate decline would reopen the vulnerability.
- **Thin ecosystem** — minimal DeFi/app activity and developer mindshare; the "code is law" immutability ethos that defines ETC also throttles ecosystem growth. Utility upside hinges largely on the unproven Olympia funding DAO.
- **Miner sell pressure** — the only structural sell flow is miners liquidating coinbase rewards; falling price compresses miner margins and can force capitulation selling, a reflexive downside loop.
- **Deep drawdown / narrative dependence** — −95.51% from ATH and largely "newsless" between catalysts; price is driven by [[bitcoin]]/[[ethereum]] beta and episodic squeeze/narrative flows rather than fundamentals.
- **Extreme-fear backdrop** — as of 2026-06-20 the market is in an Established Bear Market with Fear & Greed = 23; high-beta legacy alts like ETC are vulnerable to risk-off liquidation, and the day's relative strength may reflect short-covering rather than durable demand.
- **Catalyst sell-the-news risk** — the fifthening and Olympia mainnet are well-telegraphed; run-ups can fully price the event and reverse on activation.

---

## Related

- [[ethereum]]
- [[the-dao-hack]]
- [[crypto-markets]]
- [[hyperliquid]]
- [[proof-of-work]]
- [[proof-of-stake]]
- [[bitcoin]]
- [[perpetual-futures]]
- [[event-driven]]

---

## Sources

- Ethereum Classic — Olympia Upgrade, ECIPs 1111–1114 community review: https://ethereumclassic.org/blog/2025-07-04-olympia-upgrade-draft-review/
- Ethereum Classic DAO — "Olympia Upgrade: Unlocking On-Chain Funding" (May 2025): https://medium.com/@ethereum-classic/ethereum-classics-olympia-upgrade-unlocking-on-chain-funding-and-future-sustainability-08ad0287224a
- KuCoin — Ethereum vs Ethereum Classic 2026 guide (fixed supply model): https://www.kucoin.com/blog/ethereum-vs-ethereum-classic-2026-guide
- CoinMarketCap AI — ETC latest updates (hashrate >300 TH/s; fifthening Aug–Oct 2026, 2.048 → 1.6384 ETC): https://coinmarketcap.com/cmc-ai/ethereum-classic/latest-updates/
- Web verification, 2026-06-10: Olympia testnet status (mainnet target end-2026), hashrate, fifthening window confirmed.
- (Source: [[coingecko-top-1000-2026-04-09]])

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 157.52M ETC |
| **Total Supply** | 157.52M ETC |
| **Max Supply** | 210.70M ETC |
| **Fully Diluted Valuation** | $1.10B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $167.09 (2021-05-06) |
| **Current vs ATH** | -95.82% |
| **All-Time Low** | $0.6150 (2016-07-25) |
| **Current vs ATL** | +1034.59% |
| **24h Change** | -1.08% |
| **7d Change** | -0.25% |
| **30d Change** | -5.84% |
| **1y Change** | -64.35% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $27.87M |
| **Market Cap Rank** | #63 |
| **24h Range** | $6.96 — $7.18 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
