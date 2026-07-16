---
title: "StorX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["SRX", "StorX Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://storx.tech/"
related: ["[[crypto-markets]]", "[[decentralized-storage]]", "[[depin]]", "[[filecoin]]", "[[xdc-network]]"]
---

# StorX

**StorX Network** (SRX) is a decentralized cloud-storage [[depin|DePIN]] that encrypts, fragments, and distributes files across a worldwide network of independent hosting nodes. It offers a [[decentralized-storage|decentralized-storage]] marketplace as an alternative to centralized cloud providers, letting users retain control of (and grant access to) their own data without a central intermediary. StorX is built on the **XDC Network**, and the native token **SRX** is used to pay for storage and to reward node operators.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 SRX trades at **$0.052735**, ranked **#620** by market capitalization (~**$32.03M**), down **-0.67%** on the day and **-2.58%** over the trailing week — modest consolidation in a risk-off market (BTC ~$64,180; Fear & Greed 22 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SRX |
| **Market Cap Rank** | #620 |
| **Market Cap** | $32,031,121 |
| **Current Price** | $0.052735 |
| **24h / 7d Change** | -0.67% / -2.58% |
| **Categories** | Storage, XDC Ecosystem, DePIN |
| **Website** | [https://storx.tech/](https://storx.tech/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Earlier top-1000 snapshot fields below are retained for history.*

---

## Overview

StorX helps users securely encrypt, fragment, and distribute important data across multiple hosting nodes spread worldwide. It provides a marketplace for hosting data, replacing centralized intermediaries with a decentralized network so users retain complete control over (and grant access to) their data sets without a central intermediary. StorX is part of the broader [[depin|Decentralized Physical Infrastructure Networks (DePIN)]] thesis: coordinating real-world infrastructure (here, unused disk capacity) through token incentives.

## Architecture & Mechanism

StorX follows the canonical decentralized-storage pattern:

- **Client-side encryption** — files are encrypted on the user's device before upload, so node operators never see plaintext.
- **Sharding / erasure coding** — each file is split into many fragments distributed across independent nodes; the file can be reconstructed from a subset of shards, providing redundancy against node failure or churn.
- **Distributed hosting nodes** — independent operators ("Reservoirs") supply storage capacity and are paid in SRX for hosting and serving data.
- **XDC Network settlement** — StorX is built on the [[xdc-network|XDC Network]] (XinFin), an enterprise-focused chain; SRX exists as an XRC-20 token, and payments/rewards settle there.

This architecture places StorX in direct conceptual competition with established [[decentralized-storage|decentralized-storage]] networks such as [[filecoin|Filecoin]], Arweave, Sia, and Storj, all of which monetize spare storage capacity through token incentives.

### Why the design matters

The combination of **client-side encryption + erasure-coded sharding** is what makes a decentralized storage network usable without trusting any individual node: no operator ever holds a complete, readable copy of a file, and the file survives the loss of a subset of nodes. The economic question every such network must answer is whether the **token-incentivized supply** of spare disk actually attracts **paying demand** for storage — the perennial weakness of storage [[depin|DePIN]], where node capacity is easy to bootstrap but verifiable, paid utilization is hard to prove externally. StorX's enterprise/data-sovereignty framing and its [[xdc-network|XDC]] base are its attempt to differentiate on the demand side (regulated/enterprise data) rather than competing purely on raw capacity price.

## Token Role (SRX)

- **Payment** — users pay for storage capacity in SRX.
- **Node rewards** — operators earn SRX for providing reliable, available storage.
- **Network incentive** — SRX aligns supply (node operators) and demand (storage users), the core flywheel of any [[depin|DePIN]].

### Value accrual & governance

SRX's value accrues through being the **required payment-and-reward unit** of the network — demand for paid storage drives buy-side pressure, while node rewards are the sell-side. Crucially, circulating supply (606.5M) sits **well below the 1.5B max supply**, so although MC/FDV against *total* supply is ~1.0, the larger max cap implies **future emissions remain possible** as more node-reward tokens are minted. This is the key tokenomics watch-item: if reward emissions outrun genuine paid-storage demand, the incentive token faces structural sell pressure — the classic DePIN supply/demand imbalance. Governance is exercised through the StorX project rather than a fully decentralized token-holder DAO.

## Competitive Position

StorX's differentiation is its XDC Network base and an enterprise/data-sovereignty framing, but it is a small player against far larger decentralized-storage networks with deeper developer ecosystems and storage deals. Its success depends on actual paid storage demand rather than token speculation — the central challenge for every DePIN storage project, where on-chain "utilization" is notoriously hard to verify externally.

| Project | Focus | Chain / Tech | Token | Contrast vs StorX |
|---|---|---|---|---|
| **StorX (SRX)** | Encrypted, sharded cloud-storage marketplace | [[xdc-network\|XDC Network]] (XRC-20) | SRX | Enterprise/data-sovereignty framing on XDC; small footprint |
| **[[filecoin\|Filecoin]] (FIL)** | Largest decentralized-storage network; verifiable storage proofs | Own L1 (IPFS-based) | FIL | Vastly larger capacity, developer ecosystem, and storage deals |
| **Arweave (AR)** | Permanent, pay-once "permaweb" storage | Own L1 (blockweave) | AR | Permanence model — pay once, store forever; different economics |
| **Storj (STORJ)** | S3-compatible decentralized object storage | Ethereum ERC-20 | STORJ | Strong S3 compatibility & enterprise SDKs; deeper integrations |
| **Sia (SC)** | Decentralized cloud storage via Renterd/hostd | Own L1 | SC | Long-running, contract-based storage marketplace |

The competitive reality is **scale and mindshare favor the incumbents**: Filecoin, Arweave, and Storj command the developer ecosystems, integrations, and storage deals, leaving StorX to compete on its XDC base and enterprise/sovereignty niche rather than on raw scale.

## Risks

- **Adoption / real utilization** — value ultimately requires paying storage customers; demand metrics for niche storage DePINs are hard to verify and often thin.
- **Narrative dependence** — trades with the DePIN/storage narrative cycle; underperforms in risk-off tape.
- **Competition** — entrenched, better-funded rivals (Filecoin, Arweave, Storj) dominate mindshare and capacity.
- **Ecosystem concentration** — reliance on the XDC Network ties StorX's fortunes to that chain's adoption and liquidity.
- **Low liquidity** — ~$32M market cap with modest daily volume; thin order books amplify volatility and slippage.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 606.50M SRX |
| **Total Supply** | 606.50M SRX |
| **Max Supply** | 1.50B SRX |
| **Fully Diluted Valuation** | $33.88M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.69 (2021-09-19) |
| **Current vs ATH** | -98.81% |
| **All-Time Low** | $0.00852373 (2023-01-31) |
| **Current vs ATL** | +555.45% |
| **24h Change** | +0.85% |
| **7d Change** | +1.58% |
| **30d Change** | -10.11% |
| **1y Change** | -5.77% |

---

## Platform & Chain Information

**Native Chain:** Xdc Network

### Contract Addresses

| Chain | Address |
|---|---|
| Xdc Network | `xdc5d5f074837f5d4618b3916ba74de1bf9662a3fed` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

### How & where it trades

| Venue type | Detail |
|---|---|
| **On-chain** | Native **XRC-20** token on the [[xdc-network\|XDC Network]]; on-chain liquidity lives within the XDC ecosystem rather than mainstream Ethereum DEXs |
| **CEX** | No major centralized listings surfaced in the snapshot; liquidity is concentrated in XDC-ecosystem and smaller venues |
| **Derivatives** | No meaningful liquid perp/futures market — SRX is effectively spot-only |
| **Liquidity profile** | Snapshot 24h volume ~$1.74M against a ~$32M cap is comparatively healthy for the size — but it is **chain-concentrated** on XDC, so it depends on XDC-ecosystem venue health |

The defining trading feature of SRX is **ecosystem concentration**: because it is an XRC-20 asset, its liquidity and accessibility are tied to the [[xdc-network|XDC Network]]'s exchange support and bridges rather than the deep Ethereum/Solana DEX liquidity that comparable tokens enjoy. This both isolates it from broad crypto flow and ties its fortunes to XDC adoption (see [[liquidity]], [[slippage]]).

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://storx.tech/](https://storx.tech/) |
| **Twitter** | [@StorXNetwork](https://twitter.com/StorXNetwork) |
| **Telegram** | [StorXNetwork](https://t.me/StorXNetwork) (1,388 members) |
| **Discord** | [https://discord.gg/ha4Jufj2Nm](https://discord.gg/ha4Jufj2Nm) |
| **GitHub** | [https://github.com/StorXNetwork](https://github.com/StorXNetwork) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.74M |
| **Market Cap Rank** | #599 |
| **24h Range** | $0.0554 — $0.0560 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Narrative, Category & Catalysts

SRX sits in the **decentralized-storage** and **[[depin|DePIN]]** narratives, with an **[[xdc-network|XDC ecosystem]]** tag that ties it to enterprise-chain adoption. Its categories are Storage, XDC Ecosystem, and DePIN.

Catalysts and counter-catalysts:

- **Real paid-storage demand.** The only durable catalyst is verifiable, paying storage utilization — the metric that separates a real storage network from an emissions-subsidized one. It is also the hardest to verify externally.
- **DePIN / decentralized-storage narrative cycles.** SRX is high-beta to the DePIN theme; it rallies when storage/DePIN is in favor and bleeds in risk-off tape.
- **XDC Network adoption.** Because SRX lives on XDC, growth in XDC enterprise adoption, trade-finance use cases, and ecosystem liquidity directly affects SRX accessibility and demand.
- **Data-sovereignty / privacy demand.** Tightening data-residency and sovereignty requirements could favor encrypted, distributed-storage alternatives to centralized cloud.

The structural counter-narrative is **incumbent dominance plus emission risk**: Filecoin/Arweave/Storj own the mindshare and integrations, while SRX's circulating supply still has headroom to the 1.5B max, leaving potential reward-emission sell pressure if demand lags.

---

## History & Timeline

Only well-established, dated milestones are listed.

| Date | Event |
|---|---|
| **2021-09-19** | SRX all-time high of **$4.69** during the 2021 bull market |
| **2023-01-31** | SRX all-time low (~$0.00852373) during the deep bear market |
| **2026-06-21** | Trades ~$0.0527 (rank #620, ~$32.0M cap), ~99% below ATH, amid an Extreme-Fear macro regime |

(ATH/ATL dates from the CoinGecko snapshot; no unverified product-launch dates asserted.)

---

## Trading Playbook (context: Extreme-Fear bear regime, 2026-06-22)

> *Not investment advice. SRX is an XDC-ecosystem small-cap with chain-concentrated liquidity.*

- **Regime read.** Established bear market (Fear & Greed 21, BTC ~16% under its 200-day MA). Storage/DePIN small-caps are high-beta and narrative-driven; they typically underperform in risk-off tape absent a project-specific catalyst.
- **Liquidity & venue.** SRX trades primarily within the [[xdc-network|XDC]] ecosystem; accessibility depends on XDC venue support and bridges, isolating it from mainstream crypto flow. Verify route/depth before sizing and assume [[slippage]] on larger orders.
- **Watch utilization & emissions.** The asymmetric long case requires verifiable paid-storage demand outpacing reward emissions toward the 1.5B max supply. Monitor utilization signals over chart patterns.
- **No hedge.** No liquid derivatives market — exposure is unhedged spot; size for the high volatility implied by the ~99% drawdown from ATH.
- **Risk controls.** Define invalidation on the demand thesis (no verifiable paid utilization) and on XDC-ecosystem risk; cap size accordingly. In Extreme Fear, prefer regime confirmation over bottom-fishing (see [[risk-management]]).

---

## See Also

- [[crypto-markets]]
- [[depin]]
- [[decentralized-storage]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- Project documentation and architecture descriptions: general market knowledge; no additional specific wiki source ingested yet.
