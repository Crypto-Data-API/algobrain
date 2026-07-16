---
title: "Hive"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["HIVE", "Hive blockchain"]
entity_type: protocol
headquarters: "Decentralized (community-run)"
website: "https://hive.io/"
related: ["[[crypto-markets]]", "[[delegated-proof-of-stake]]", "[[justin-sun]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[steem]]", "[[tron]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[range-mean-reversion]]"]
---

# Hive

**Hive** (HIVE) is a social/content-focused **[[layer-1|layer-1 blockchain]]** running a **[[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]]** consensus, on which decentralized social, blogging, and gaming applications (notably *Splinterlands* and the front-end *PeakD*/Hive.blog) are built. Hive is best known for its origin: it was created as a **community hard fork of the [[steem]] blockchain on 20 March 2020**, after [[justin-sun]] and [[tron]] acquired Steemit Inc. and the community feared the new owner would use its stake to control governance. It ranks **#687** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* HIVE trades at **$0.04945073**, with a market cap of **$27,245,428** (rank **#687**), up **+0.47%** over 24h and down **-2.13%** over the past 7 days. The market backdrop is risk-off (Fear & Greed 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HIVE |
| **Market Cap Rank** | #687 |
| **Market Cap** | $27,245,428 |
| **Current Price** | $0.04945073 |
| **24h Change** | +0.47% |
| **7d Change** | -2.13% |
| **Consensus** | [[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]] |
| **Categories** | SocialFi, [[layer-1|Layer 1 (L1)]], [[smart-contracts|Smart Contract Platform]], Gaming Blockchains |
| **Website** | [https://hive.io/](https://hive.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Hive runs a **[[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]]** consensus (see [[delegated-proof-of-stake]]) in which token holders vote for a set of "witnesses" (block producers) who secure the chain. Transactions are **feeless** for users, paid for instead by allocating bandwidth via staked tokens. This design is optimized for high-frequency, low-value actions like posting, voting, and in-game transactions rather than high-value DeFi settlement.

The token system has three primary assets:

- **HIVE** — the liquid, transferable base token.
- **Hive Power (HP)** — HIVE that is "powered up" (staked) and provides governance weight, content-curation influence, and resource credits; powering down is gradual.
- **Hive Backed Dollars (HBD)** — an algorithmic stable-value token pegged loosely to USD.

Hive's flagship applications include the blockchain trading-card game **Splinterlands**, the content front-ends **PeakD** and **Hive.blog**, and a range of "second-layer" community apps. Because content and reputation live on-chain, applications share a common social graph.

### Consensus and block production in detail

Hive's DPoS model elects **20 "elected" witnesses plus one rotating "backup" witness** per round (a 21-witness schedule), so the practical validator set is small and stake-weighted. Token holders cast witness votes weighted by their **Hive Power**, and the same staked weight also drives content-reward curation. Blocks are produced on a roughly **3-second cadence**, giving fast, predictable confirmation that suits social and gaming workloads. Because there is no [[proof-of-work|proof-of-work]] mining, energy cost is negligible relative to a UTXO chain like Bitcoin.

The feeless model is enforced via **Resource Credits (RCs)** — a regenerating, non-transferable allowance proportional to a user's staked Hive Power. RCs are consumed by on-chain actions (posting, voting, transferring) and regenerate over time, rate-limiting spam without charging an explicit per-transaction fee. This is the same bandwidth-rationing principle [[steem]] pioneered and that Hive inherited at the fork.

### Smart contracts and second layers

The Hive base layer is **not** a general-purpose [[smart-contracts|smart-contract]] virtual machine in the [[ethereum|Ethereum]] sense; application logic largely runs in **second-layer** sidechains and off-chain processors that read and write Hive's custom JSON operations. The most prominent is **Hive Engine**, a community sidechain that supports tokens, an NFT/marketplace layer, and DeFi-style features, plus **VSC (Virtual Smart Chain)** efforts to bring EVM-compatible contracts that settle to Hive. This architecture keeps the base chain lean while pushing programmability to layers that can be upgraded independently.

### Value accrual and tokenomics design

HIVE's economic flywheel is engagement-driven rather than fee-driven. New issuance funds a **reward pool** split between content authors, curators, and witnesses, while a large share of issuance is directed to **Hive Power** stakers and the **HBD** stabilization mechanism. Powering up (staking) locks supply and increases governance and curation influence, creating a soft sink; powering down releases HIVE over a **13-week** vesting schedule, dampening sell pressure. There is no hard cap, so the long-run value question is whether application demand (Splinterlands gameplay, posting, RC demand) absorbs ongoing issuance.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 536.37M HIVE |
| **Total Supply** | N/A HIVE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | N/A |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.41 (2021-11-26) |
| **Current vs ATH** | -98.28% |
| **All-Time Low** | $0.0554 (2026-03-31) |
| **Current vs ATL** | +5.89% |
| **24h Change** | +1.83% |
| **7d Change** | -0.45% |
| **1y Change** | -69.43% |

HIVE trades roughly **-98%** below its November 2021 all-time high of ~$3.41, reflecting the post-bull-market drawdown common to social/content tokens.

---

## History — The Steem Hard Fork (March 2020)

Hive's defining event is its split from [[steem]]:

- In **February 2020**, [[justin-sun]]'s [[tron]] Foundation acquired **Steemit Inc.**, the company that ran the dominant Steemit front-end and held a large pre-mined stake of STEEM (the "ninja-mined" stake).
- The Steem community had long treated that stake as off-limits for governance. Fearing Sun would use it to seize control of the chain's witnesses, witnesses enacted a soft fork to freeze the stake.
- In response, Sun — reportedly with cooperation from major exchanges including Binance, Huobi, and Poloniex — used **exchange customers' staked STEEM to vote in a new set of witnesses**, effectively taking control of the chain. This use of customer funds for governance was widely criticized.
- The community responded on **20 March 2020** by **hard-forking the chain into Hive**, copying the existing account balances and content to a new ledger **but excluding the disputed Steemit/ninja-mined stake**. Existing STEEM holders (other than the contested stake) received an equivalent HIVE airdrop.

Hive is therefore best understood as the **community-governance continuation** of the original Steem social blockchain, while [[steem]] continued under Tron-aligned governance. The two chains are mirror images of the same dispute and should be read together.

The fork is frequently cited as one of the clearest real-world demonstrations of a **community exercising "exit"** against a hostile capital takeover: rather than fight for control of the original ledger, the community copied the social graph, balances, and code to a chain whose genesis explicitly diluted the contested stake. It is a recurring case study in [[delegated-proof-of-stake|DPoS]] governance-attack analysis alongside the broader exchange-custody-voting controversy.

---

## Governance

- **Witness governance:** Stake-weighted (Hive Power) votes elect the 20+1 witness schedule. Witnesses signal support for protocol changes; a hard fork ships when a supermajority of top witnesses upgrade their nodes.
- **Decentralized Hive Fund (DHF / "the DAO"):** A treasury funded by a slice of issuance and HBD inflows. Stakeholders create funding **proposals**; HP-weighted votes route DHF money to development, marketing, and infrastructure work. This gives Hive an on-chain mechanism to fund public goods without a foundation controlling the purse.
- **No founder/premine overhang:** Because the fork excluded the disputed Steemit/ninja-mined stake, Hive launched without a dominant founder treasury — a deliberate contrast to [[steem]]'s pre-2020 stake concentration.

---

## Hive vs. Peer Social / DPoS Chains

| Dimension | Hive (HIVE) | [[steem]] (STEEM) | [[tron]] (TRX) | Generic [[layer-1]] L1 |
|---|---|---|---|---|
| **Primary use** | SocialFi, blogging, gaming | SocialFi, blogging | DeFi/stablecoins, content | General smart contracts |
| **Consensus** | [[delegated-proof-of-stake|DPoS]] (21 witnesses) | [[delegated-proof-of-stake|DPoS]] (21 witnesses) | DPoS (27 SRs) | Varies (PoS/PoW) |
| **User fees** | Feeless (Resource Credits) | Feeless (bandwidth) | Low gas (energy/bandwidth) | Per-tx gas |
| **Stable token** | HBD (algorithmic) | SBD (algorithmic) | USDD / USDT issuance | Varies |
| **Governance** | HP-weighted witnesses + DHF DAO | SP-weighted witnesses | Sun/Tron-aligned SRs | Varies |
| **Origin** | 2020 community fork of Steem | 2016 original chain | 2017 ICO | Varies |
| **Founder overhang** | None (excluded at fork) | Historical ninja-mine stake | Centralized influence | Varies |

The key takeaway: Hive and Steem are technically near-identical forks, but they diverge sharply on **governance legitimacy** — Hive's pitch is credibly community-owned issuance and a treasury DAO, whereas Steem's post-2020 governance is associated with [[justin-sun]]/[[tron]] alignment.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HIVE/USDT | N/A |
| Upbit | HIVE/KRW | N/A |
| Bitget | HIVE/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hive.io/](https://hive.io/) |
| **Twitter** | [@hiveblocks](https://twitter.com/hiveblocks) |
| **Reddit** | [https://www.reddit.com/r/hivenetwork/](https://www.reddit.com/r/hivenetwork/) |
| **Telegram** | [hiveblockchain](https://t.me/hiveblockchain) (4,144 members) |
| **Discord** | [https://myhive.li/discord](https://myhive.li/discord) |
| **GitHub** | [https://github.com/openhive-network/hive](https://github.com/openhive-network/hive) |
| **Whitepaper** | [https://hive.io/whitepaper.pdf](https://hive.io/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 321 |
| **GitHub Forks** | 102 |
| **Pull Requests Merged** | 8 |
| **Contributors** | 2 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.04945073 |
| **Market Cap (2026-06-22)** | $27,245,428 |
| **Market Cap Rank** | #687 |
| **24h Change** | +0.47% |
| **7d Change** | -2.13% |
| **Last Updated** | 2026-06-22 |

---

## Risks

- **Niche / engagement-dependent:** Hive's value is tied to active social and gaming usage; if app activity (e.g., Splinterlands) declines, the demand for resource credits and HP weakens.
- **DPoS governance concentration:** A small set of witnesses produces blocks; large stakeholders can heavily influence both governance and content rewards.
- **Inflationary supply:** HIVE has no hard cap; ongoing issuance funds rewards and can dilute holders if demand does not keep pace.
- **HBD peg risk:** Algorithmic stable-value tokens can de-peg under stress; HBD is not a fully collateralized stablecoin. A debt-style mechanism mints HIVE to defend the peg, which can dilute holders during de-peg events.
- **Second-layer fragmentation:** Programmability lives in sidechains (Hive Engine, VSC) rather than the base layer; security and continuity of those layers are not guaranteed by base-chain consensus.
- **Liquidity / small-cap risk:** ~$27M market cap and thin order books mean prices move sharply on small flows.
- **Cycle risk:** Down ~98% from ATH in an Extreme Fear market (Fear & Greed 21 on 2026-06-22); small-caps are vulnerable in risk-off regimes.

> Not investment advice. Figures are point-in-time; verify on-chain and project claims independently.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

HIVE is tradable on **Binance** — both **spot** (HIVE/USDT) and a **USD-margined perpetual** future, which exposes **funding**, **open interest**, and **liquidation** data for the token. It is **NOT** listed on Hyperliquid, so **Binance is the primary leveraged venue** and the effective price-discovery hub for derivatives. Because leveraged flow is concentrated on a single exchange, perp funding and OI on Binance dominate the derivatives picture, and there is no on-chain perp DEX to cross-check or arbitrage against. With a sub-$30M market cap and thin spot books (also on Upbit and Bitget), leveraged positions can move price disproportionately: traders should size conservatively, favor limit/maker execution to avoid slippage, and treat available perp depth — not headline market cap — as the true liquidity constraint. Venue concentration also means funding spikes and liquidation cascades tend to originate and resolve on Binance, so execution and sizing should be calibrated to Binance order-book depth and funding cadence.

### Applicable strategies

- [[funding-rate-harvest]] — a low-cap, single-venue perp like HIVE frequently sustains skewed Binance funding; harvesting it against a spot hedge can capture carry when directional conviction is low.
- [[crowded-long-funding-fade]] — sentiment-driven pumps on a thin SocialFi token often over-crowd the long side; fading persistently positive funding targets the mean-reversion after leverage builds up.
- [[liquidation-cascade-fade]] — concentrated leverage on one venue makes HIVE prone to sharp forced-liquidation flushes; fading over-extended cascades on Binance can capture the snap-back.
- [[range-mean-reversion]] — outside of narrative bursts HIVE spends long stretches ranging in a deep drawdown, making band/range reversion viable on the thin spot pair.
- [[oi-confirmed-trend]] — using Binance open-interest changes to confirm that a HIVE move is backed by real positioning (not spoofed spot) filters false breakouts on an illiquid book.
- [[breakout-and-retest]] — narrative or Splinterlands-driven catalysts can trigger clean breakouts; waiting for a retest reduces the whipsaw risk inherent to a low-liquidity small-cap.

### Volatility & regime character

HIVE is a **small-cap** SocialFi / gaming [[layer-1]] token (rank ~#682, sub-$30M cap) with **high beta** to broad crypto risk sentiment and strong directional correlation to **BTC/ETH** during risk-on/risk-off swings. Its price is **narrative- and engagement-reflexive**: activity in flagship apps (Splinterlands, PeakD) and periodic SocialFi/gaming rotations can drive sharp, low-liquidity moves that decouple briefly from majors before mean-reverting. In quiet regimes it trends sideways in a deep post-2021 drawdown with low realized volatility; in active regimes thin books amplify moves in both directions. Treat it as a reflexive small-cap altcoin rather than a stable infra/DeFi holding.

### Risk flags

- **Liquidity / venue concentration:** leveraged trading is concentrated on Binance with no Hyperliquid or perp-DEX alternative; thin spot books make slippage and gap risk significant.
- **Inflationary supply / no hard cap:** ongoing HIVE issuance funds rewards and can dilute holders if app demand lags; powering-down (13-week vesting) shapes sell-pressure timing.
- **Narrative dependence:** value is tied to SocialFi/gaming engagement (Splinterlands, PeakD); fading activity or rotation out of the narrative removes demand support.
- **Governance & peg risk:** DPoS witness concentration and the algorithmic HBD peg introduce protocol-level tail risks that can hit HIVE during stress and trigger cascade liquidations on the single leveraged venue.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HIVEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HIVEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HIVE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HIVE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HIVEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HIVEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HIVE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[steem]] — the chain Hive forked from
- [[justin-sun]]
- [[tron]]
- [[delegated-proof-of-stake]]
- [[layer-1]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific dedicated Hive source has been ingested into the wiki yet.
