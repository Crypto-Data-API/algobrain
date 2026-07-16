---
title: "Toncoin (Gram)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["GRAM", "Gram", "TON", "The Open Network", "Toncoin"]
entity_type: protocol
founded: 2018
headquarters: "TON Foundation (Telegram-aligned); Zug, Switzerland"
website: "https://ton.org/"
related: ["[[bitcoin]]", "[[blum]]", "[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[layer-1]]", "[[narrative-trading]]", "[[solana]]"]
---

# Toncoin (Gram)

**Toncoin** (TON) — being renamed **Gram (GRAM)** effective **15 June 2026** — is the native asset of The Open Network, the Layer 1 blockchain originally designed by Telegram in 2018 and revived by the open-source community after Telegram's 2020 SEC settlement. Its trading thesis is unique among [[layer-1|L1s]]: it is the only chain natively distributed through **Telegram's ~900M monthly active users**, making it the benchmark "social/payments distribution" asset.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

The GRAM rename (effective 15 June 2026) is now live — CoinGecko lists the asset as **"Gram (prev. Toncoin)"**, ticker **GRAM**. Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in an **established bear market**. After the buy-rumor/sell-news rebrand sequence, GRAM has rolled over (down on both 24h and 7d) and trades at $1.60.

| Metric | Value |
|---|---|
| **Price** | $1.60 |
| **Market Cap** | $4,290,795,812 |
| **Market Cap Rank** | #24 |
| **24h Volume** | $52,577,893 |
| **24h Change** | -2.06% |
| **7d Change** | -5.18% |
| **24h Range** | $1.56 – $1.63 |
| **Circulating Supply** | 2,691,571,265 GRAM |
| **Total Supply** | 5,200,347,094 GRAM |
| **Max Supply** | None (uncapped — inflationary PoS) |
| **Fully Diluted Valuation** | $8,290,186,413 |
| **Market Cap / FDV** | ~0.52 |
| **All-Time High** | $8.25 (2024-06-15) — **-80.69%** from ATH |
| **All-Time Low** | $0.519364 (2021-09-21) — **+206.81%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | **GRAM** (renamed from TON, effective 15 June 2026 — rename only, no token swap or migration) |
| **Market Cap Rank** | #24 (2026-06-20) |
| **Market Cap** | $4.29B (2026-06-20); price $1.60 |
| **Chain / Sector** | Own [[layer-1\|L1]] (sharded, PoS, sub-second finality); sectors: payments, Telegram mini-apps, consumer crypto |
| **Categories** | Smart Contract Platform, BNB Chain Ecosystem, Layer 1 (L1), Ethereum Ecosystem, Animoca Brands Portfolio, Alleged SEC Securities, DWF Labs Portfolio, TON Ecosystem, Proof of Stake (PoS), Pantera Capital Portfolio, GMCI Layer 1 Index, GMCI 30 Index, GMCI Index |
| **Website** | [https://ton.org/](https://ton.org/) |

---

## Overview

TON (The Open Network) is a general-purpose blockchain that allows developers to build decentralized apps and tokens. It descends from Telegram's original Telegram Open Network, whose "Gram" token sale raised $1.7B before a landmark SEC enforcement action forced Telegram to return **$1.2B to investors in 2020** and abandon the project. The community-run TON Foundation revived the chain; Telegram has since re-embraced it as the exclusive blockchain for Telegram Mini Apps, wallet integration and ads payments, with founder Pavel Durov publicly championing the ecosystem.

---

## 2025–2026 Developments

- **GRAM rebrand (June 2026)** — the TON Foundation announced on **2 June 2026** that Toncoin would be renamed **Gram**, reviving the original 2018 token name. A governance vote concluding **8 June 2026** passed with **81.22%** of participating voting power. Effective **12:00 UTC, 15 June 2026**, with a phased exchange/wallet/ticker rollout 9-22 June. The change is cosmetic — no token swap, no migration, no new issuance. TON jumped ~15% when the plan was floated (2 June) but sold off as the vote cleared, a classic buy-rumor/sell-news sequence.
- **"Make TON Great Again" roadmap** — Durov frames the rename as **step 4 of 7** in a publicly stated roadmap; steps 5-7 are undisclosed (a standing speculation catalyst). Reclaiming the Gram name is a calculated bet that the ecosystem has enough legal distance from the 2020 SEC episode.
- **Institutional staking** — a Nasdaq-listed firm reported a **3.3M TON staking position** with **$5.6M in May 2026 rewards**, read as evidence of institutional yield demand; TON Foundation has also pushed institutional stablecoin rails, and there is a market expectation that Telegram itself will become a major validator.
- **Market recovery, then rollover** — TON ran from ~$1.23 (April 2026 snapshot) to ~$1.70-1.79 in early June 2026 on the GRAM news cycle, then faded as the rebrand vote cleared. **As GRAM on 2026-06-20 it trades $1.60, market cap $4.29B (#24)** — the post-event sell-off plus an extreme-fear market.

---

## Protocol & Technology

TON (The Open Network) is a sharded, [[proof-of-stake]] [[layer-1|Layer 1]] designed for mass-consumer throughput, descended from Telegram's original 2018 design and revived by the open-source community.

### Architecture
- **Infinite sharding ("dynamic sharding")** — TON's signature design. The chain can split into shardchains on demand and merge them when load falls, theoretically scaling to very high throughput rather than running every transaction through one global chain. A **masterchain** coordinates ~workchains, each of which can spawn shardchains.
- **Sub-second finality / high TPS** — targets fast, cheap transactions suited to payments and consumer mini-apps rather than complex DeFi composability.
- **Asynchronous smart contracts** — TON uses an actor-model, message-passing execution (contracts communicate asynchronously across shards). This is powerful for scale but a different, less composable programming model than the EVM, which has slowed DeFi growth relative to [[ethereum]] and [[solana]].
- **TON Virtual Machine (TVM) & FunC/Tact** — contracts are written in TON-specific languages (FunC, the higher-level Tact), not Solidity — a developer-onboarding hurdle.

### The Telegram distribution moat
TON's defining advantage is not its VM but its **distribution**: it is the exclusive blockchain integrated into Telegram (~900M MAU). This manifests as:
- **TON Wallet inside Telegram** — a self-custody/custodial wallet reachable by hundreds of millions without leaving the app.
- **Telegram Mini Apps** — in-app dApps (games, trading bots, tap-to-earn) that drove the 2024 Notcoin/Hamster Kombat boom and apps like [[blum|Blum]]; GRAM is the gas/settlement asset for this economy.
- **Telegram Ads & payments** — Telegram routes parts of its ad and payments economy through TON, and Pavel Durov has championed the ecosystem.
- **Validator expectation** — there is a standing market expectation that Telegram itself will run major validators, deepening the alignment.

### Consensus & staking
TON uses a **delegated/nominated Proof-of-Stake** model: validators stake TON/GRAM to produce blocks and earn rewards + fees; nominators delegate to validators for yield. Staking yields have attracted institutional participation (e.g. a Nasdaq-listed firm's 3.3M-token staking position reporting $5.6M May 2026 rewards). Because supply is **uncapped**, staking rewards are funded partly by ongoing inflation — a structural dilution feature, not a bug.

### The GRAM rename
The June 2026 TON→GRAM rebrand is **cosmetic** — no token swap, no migration, no new issuance. It revives the original 2018 "Gram" name, betting the ecosystem has enough legal distance from Telegram's 2020 SEC settlement (which forced the return of $1.2B and barred the original Gram). Operationally it is a ticker/branding migration across exchanges and wallets (phased 9–22 June 2026).

---

## Tokenomics & Supply

> *Authoritative figures are in the [[the-open-network#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 2,691,571,265 GRAM |
| **Total Supply** | 5,200,347,094 GRAM |
| **Max Supply** | None (uncapped) |
| **Fully Diluted Valuation** | $8,290,186,413 |
| **Market Cap / FDV Ratio** | ~0.52 |

**Emissions & dilution.** GRAM has **no maximum supply** — it is an inflationary PoS asset where new tokens are minted to pay validators/nominators. Circulating (~2.69B) is ~52% of total supply (~5.2B), and total supply itself grows with inflation, so FDV ($8.29B) materially exceeds market cap ($4.29B). The ~2.5B gap between circulating and total is a standing overhang from the original distribution (early miners, foundation, ecosystem allocations) plus ongoing staking emissions. For traders this means GRAM faces **two dilution vectors**: scheduled unlocks of the non-circulating ~48% and perpetual PoS inflation. The GRAM rename added zero new issuance.

---

## Price History

> *Authoritative current figures are in the [[the-open-network#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $8.25 (2024-06-15) — -80.69% |
| **All-Time Low** | $0.519364 (2021-09-21) — +206.81% |
| **24h Change (2026-06-20)** | -2.06% |
| **7d Change (2026-06-20)** | -5.18% |

---

## Platform & Chain Information

**Native Chain:** The Open Network

### Contract Addresses

| Chain | Address |
|---|---|
| The Open Network | `EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c` |
| Ethereum | `0x582d872a1b094fc48f5de31d3b73f2d9be47def1` |
| Binance Smart Chain | `0x76a797a59ba2c17726896976b7b3747bfd1d220f` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TON/USDT | N/A |
| Kraken | TON/USD | N/A |
| Bitget | TON/USDT | N/A |
| KuCoin | TON/USDT | N/A |
| Crypto.com Exchange | TON/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | TON-PERP | Perpetual |
| Uniswap V3 (Ethereum) | 0X582D872A1B094FC48F5DE31D3B73F2D9BE47DEF1/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ton.org/](https://ton.org/) |
| **Twitter** | [@ton_blockchain](https://twitter.com/ton_blockchain) |
| **Telegram** | [toncoin](https://t.me/toncoin) (8.48M members) |
| **GitHub** | [https://github.com/ton-blockchain/ton](https://github.com/ton-blockchain/ton) |
| **Whitepaper** | [https://ton.org/whitepaper.pdf](https://ton.org/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,937 |
| **GitHub Forks** | 1,498 |
| **Commits (4 weeks)** | 159 |
| **Pull Requests Merged** | 927 |
| **Contributors** | 62 |

---

## Trading Characteristics

> *Current figures: see [[the-open-network#Market Data\|Market Data]] (2026-06-20).*

| Characteristic | Detail (2026-06-20) |
|---|---|
| **24h Volume** | $52.58M (cooled from the GRAM-news peak of ~$207M on 2026-05-04) |
| **Market Cap Rank** | #24 |
| **24h Range** | $1.56 – $1.63 |
| **Volume / MCAP turnover** | ~1.2% |
| **Last Updated** | 2026-06-20 |

---

## Trading Relevance

- **Where it trades**: spot on [[binance|Binance]], [[kraken|Kraken]], Bitget, KuCoin, Crypto.com, [[okx|OKX]] (note: never listed on Coinbase as of early 2026); perps on [[hyperliquid|Hyperliquid]] (TON-PERP) and major venues; also the gas/settlement asset for the entire Telegram mini-app economy (e.g. [[blum]], Notcoin, Hamster Kombat era apps).
- **Ticker-migration trade (live now)**: exchanges roll TON→GRAM tickers between 9-22 June 2026. Historical ticker changes (e.g. MATIC→POL) produced temporary liquidity fragmentation, index-tracking lags and retail confusion — exploitable for arb and a known operational risk for bots/strategies keyed to the TON symbol. Update data pipelines before 15 June 2026.
- **Narrative basket**: consumer/social-distribution basket; payments; "Durov roadmap" event trades (steps 5-7 undisclosed). Telegram-regulatory headlines (e.g. anything touching Durov legally) hit TON directly — it is effectively a liquid proxy for Telegram platform risk.
- **Catalysts**: GRAM rollout completion (22 June 2026), undisclosed roadmap steps 5-7, Telegram validator participation, institutional staking growth, mini-app activity cycles.
- **Risk profile**: ~81% below its June 2024 ATH ($8.25) as of 2026-06-20; uncapped supply with ~0.52 MC/FDV — meaningful future dilution; concentration risk in a single distribution channel (Telegram).

---

## Ecosystem & Use Cases

- **Telegram Mini Apps** — the killer use case: in-app games and tools (Notcoin, Hamster Kombat era; ongoing apps like [[blum|Blum]]) reachable inside Telegram, with GRAM as gas/settlement.
- **Payments** — Telegram in-app payments, tips, ads payouts and the TON Wallet for ~900M MAU; the "social-payments distribution" thesis.
- **Stablecoins** — USDT on TON drove much of 2024–2025 on-chain volume; TON Foundation has pushed institutional stablecoin rails.
- **Staking / validators** — nominated PoS staking for yield; institutional staking demand emerging.
- **DeFi (nascent)** — DEXes (STON.fi, DeDust) and lending exist but are smaller than EVM/Solana DeFi due to the non-EVM, async programming model.
- **NFTs & usernames** — Telegram username/anonymous-number auctions and Telegram Gifts settle on TON.

---

## Market Structure & Derivatives

- **Spot venues**: [[binance|Binance]] (price leader), [[kraken|Kraken]], Bitget, KuCoin, Crypto.com, [[okx|OKX]]. **Never listed on Coinbase** as of early 2026 — a notable distribution gap vs US retail. Korean (Upbit/Bithumb) flow matters for momentum.
- **Perps & funding**: GRAM/TON-PERP on [[hyperliquid|Hyperliquid]] and major CEX perp desks; with price rolling over post-rebrand, funding has likely turned neutral-to-negative as longs unwind the event trade.
- **Ticker-migration microstructure (live)**: the TON→GRAM symbol change (phased 9–22 June 2026) fragments liquidity across exchanges still on the old ticker, lags index trackers, and confuses retail — the MATIC→POL precedent showed this creates short-lived arb and operational risk for symbol-keyed bots. Pipelines must map TON→GRAM.
- **Liquidity**: ~$52.6M 24h volume on a ~$4.3B cap (~1.2% turnover) — cooled sharply from the ~$207M GRAM-news peak; thinner liquidity now means sharper moves on headlines.

---

## Valuation Framework

GRAM is best valued as a **consumer-distribution / payments L1**, not a DeFi-fee chain:

- **Active users & mini-app activity** — the core driver; on-chain active addresses, mini-app DAU, and Telegram-integration depth proxy demand. GRAM re-rates on user-growth cycles, not TVL.
- **Stablecoin volume / payments throughput** — USDT-on-TON volume and Telegram payments flow gauge real settlement use.
- **Staking ratio** — share of supply staked tightens float and signals validator/institutional commitment.
- **Inflation drag** — uncapped supply means new issuance must be netted against demand; model net flow, not gross demand.
- **MC/FDV ~0.52** — discount for ~48% non-circulating supply plus perpetual inflation.
- **Optionality** — Durov roadmap steps 5–7 (undisclosed) and a potential Telegram validator role are unpriced call options that the market periodically bids up.

There is no clean cash-flow multiple; GRAM trades on the **Telegram distribution narrative** and event catalysts.

---

## Trading Playbook

- **Distribution / consumer-crypto basket** — GRAM is the benchmark "social-distribution" L1; trade it on Telegram-ecosystem cycles (mini-app booms) and as a liquid proxy for Telegram platform sentiment.
- **Event trades** — Durov roadmap reveals (steps 5–7), Telegram validator news, institutional-staking headlines. These are reflexive: the GRAM rename itself was a textbook **buy-the-rumor/sell-the-news** (spiked 2 June on the floated plan, sold off through the vote and into 2026-06-20).
- **Ticker-migration arb (live)** — exploit symbol fragmentation and index-tracking lag during the 9–22 June TON→GRAM rollout.
- **Telegram tail risk** — any legal headline touching Pavel Durov hits GRAM directly; it is a one-channel bet. Hedge or size for binary platform risk.
- **Dilution-aware** — uncapped inflation + ~48% locked supply argue against long-term passive holding without conviction in user growth outrunning issuance.
- **Risk in extreme fear** — Fear & Greed = 22, GRAM down on the week post-event; favor patience over chasing, and respect thin post-peak liquidity.

---

## History

| Date | Event |
|---|---|
| 2018 | Telegram designs Telegram Open Network (TON); $1.7B Gram presale (a16z, Sequoia, Benchmark, Kleiner Perkins among buyers) |
| 2020 | SEC enforcement forces Telegram to return $1.2B and abandon Gram; community forks the open-source code as The Open Network |
| 2021 | Community-run TON Foundation revives the chain; ATL $0.519 |
| 2023–2024 | Telegram re-embraces TON as exclusive Mini-App / wallet / ads chain; Notcoin & Hamster Kombat mini-app boom |
| 2024-06 | TON all-time high $8.25 |
| 2025–2026 | USDT-on-TON growth; institutional staking; stablecoin rails |
| 2026-06-02 | Telegram floats "Gram" rebrand; TON +15% |
| 2026-06-08/09 | Governance vote passes 81.22% |
| 2026-06-15 | TON officially renamed **GRAM** (cosmetic; no swap) |
| 2026-06-20 | GRAM $1.60, #24, down post-event in an extreme-fear market |

---

## Competitive Positioning

| L1 | Positioning | Edge vs GRAM | GRAM's Edge |
|---|---|---|---|
| [[ethereum\|Ethereum]] | DeFi/settlement leader | EVM composability, deepest DeFi/TVL, institutional rails | Native Telegram distribution; far better consumer UX/onboarding |
| [[solana\|Solana]] | High-throughput consumer L1 | EVM-adjacent tooling momentum, huge DeFi/memecoin/DePIN ecosystem, Coinbase-listed | Telegram's ~900M-MAU distribution; mini-app native |
| BNB Chain | CEX-distributed L1 | Binance distribution + deep DeFi | Telegram > exchange app for organic reach |
| Tron | Stablecoin/payments rail | Dominant USDT settlement share | Consumer mini-app layer + social graph |
| Base ([[base]]) | Coinbase consumer L2 | Coinbase US retail distribution, EVM | Telegram global reach; not US-gated |

GRAM's moat is **distribution, not technology**: the only chain natively inside Telegram. Its weaknesses are the **non-EVM async programming model** (thinner DeFi), **uncapped inflation**, **single-channel dependence on Telegram**, and **no Coinbase listing** limiting US retail access. The bull case is that consumer distribution ultimately beats developer composability for mass adoption.

---

## Risks

- **Single-channel dependence** — GRAM is effectively a leveraged bet on Telegram. Any regulatory/legal action against Telegram or Durov is direct, binary downside.
- **Uncapped inflation** — perpetual PoS issuance dilutes holders; demand must continually outpace supply.
- **Supply overhang** — ~48% of supply non-circulating; scheduled unlocks add to inflation pressure.
- **SEC / securities history** — the asset carries the legacy of the 2020 Gram enforcement; the GRAM rename reopens that question ("Alleged SEC Securities" is a listed category). US listing/access remains constrained (no Coinbase).
- **Thin DeFi / composability** — the non-EVM model limits the DeFi flywheel that drives value on Ethereum/Solana.
- **Event/narrative dependence** — price is driven by Durov-roadmap and rebrand catalysts; the buy-rumor/sell-news pattern (June 2026 GRAM rename) is a recurring trap.
- **Post-peak liquidity** — volume has cooled ~75% from its May peak; sharper moves on lighter books.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[blum]] — Telegram-ecosystem trading app
- [[bitcoin]], [[ethereum]], [[solana]] — L1 context
- [[layer-1]] — sector
- [[proof-of-stake]] — consensus model
- [[hyperliquid]] — TON/GRAM-PERP venue
- [[narrative-trading]] — consumer-distribution / event baskets

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- CoinGecko top-1000 snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- [AMBCrypto — TON officially rebrands Toncoin to Gram as Telegram deepens role in network (June 2026)](https://ambcrypto.com/ton-officially-rebrands-toncoin-to-gram-as-telegram-deepens-role-in-network/)
- [The Crypto Times — Gram Is Back: TON Community Approves Rebrand With 81% Support (9 June 2026)](https://www.cryptotimes.io/2026/06/09/gram-is-back-ton-community-approves-rebrand-with-81-support/)
- [The Crypto Times — Toncoin Jumps 15% as Telegram Floats "Gram" Rebrand Plan (2 June 2026)](https://www.cryptotimes.io/2026/06/02/toncoin-jumps-15-as-telegram-floats-gram-rebrand-plan-for-ton/)
- [BanklessTimes — Toncoin Crashes as GRAM Rebrand Vote Clears Governance (5 June 2026)](https://www.banklesstimes.com/articles/2026/06/05/toncoin-ton-crashes-as-gram-rebrand-vote-clears-governance/)
- [Cryptonews — TON Revives 'Gram' Token Name in Bid to Own Telegram's 900M Users](https://cryptonews.com/news/ton-revives-gram-token-name-telegram-users/)
- [CoinGecko — Toncoin](https://www.coingecko.com/en/coins/toncoin) (market cap ~$4.46B, June 2026)
- Verified via Perplexity (sonar, 2026-06-10) and web search, 2026-06-10.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 268.12M TON |
| **Total Supply** | 400.00M TON |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $2.93M |
| **Market Cap / FDV Ratio** | 0.67 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
