---
title: "Nym"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["NYM", "Nym Technologies"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nym.com"
related: ["[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[privacy-coins]]"]
---

# Nym

**Nym** (NYM) is a privacy-infrastructure project building a **mixnet** — a decentralized network that protects metadata at the network and application layers, hiding not just the contents of communications but who is talking to whom, when, and how often. Unlike [[privacy-coins|privacy coins]] that obscure on-chain transaction data, Nym targets network-level privacy (the kind a Tor/VPN replacement would provide), powering products such as the NymVPN. The native token **NYM** pays for bandwidth and incentivizes the node operators ("mix nodes" and gateways) that route and shuffle traffic.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 NYM trades at **$0.01791936**, ranked **#957** by market capitalization (~**$14.97M**), up **+0.98%** on the day and roughly flat at **-0.64%** over the trailing week — quiet trading in a risk-off market (BTC ~$64,180; Fear & Greed 22 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NYM |
| **Market Cap Rank** | #957 |
| **Market Cap** | $14,972,424 |
| **Current Price** | $0.01791936 |
| **24h / 7d Change** | +0.98% / -0.64% |
| **Categories** | Smart Contract Platform, Ethereum Ecosystem, DePIN, Osmosis Ecosystem, VPN, Andreessen Horowitz (a16z) Portfolio, YZi Labs (Prev. Binance Labs) Portfolio, Privacy Blockchain, Governance, CoinList Launchpad, Privacy Infrastructure, Privacy |
| **Website** | [https://nym.com](https://nym.com) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Earlier top-1000 snapshot fields below are retained for history.*

---

## Overview

Existing internet protocols leak sensitive data that can be used without users' knowledge — Nym is developing infrastructure to prevent this leakage by protecting every packet's metadata at the network and application layers. The central insight is that encryption hides message *content* but not metadata (who, when, how much, to whom), and metadata is often more revealing than content. Nym attacks this with a **mixnet**: a privacy-overlay network that is, in [[depin|DePIN]] terms, a decentralized physical-infrastructure network of independently operated routing nodes.

## Architecture & Mechanism

- **Mixnet** — traffic is routed through multiple layers of "mix nodes" that batch, reorder, and delay packets, and add cover (dummy) traffic. This breaks the timing and volume correlations an observer would use to link sender and receiver — a stronger guarantee than Tor's onion routing against a global passive adversary.
- **Sphinx packet format** — all packets are reformatted to a uniform size and structure so they are indistinguishable in transit.
- **Gateways and nodes** — entry/exit gateways and mix nodes are run by independent operators who stake and earn NYM for providing reliable, well-behaved bandwidth.
- **NymVPN** — a consumer product layering a conventional VPN mode and a stronger mixnet (anonymous) mode on top of the network, the primary route to real end-user demand.

Nym has been backed by prominent venture investors (its categories list Andreessen Horowitz / a16z and YZi Labs, formerly Binance Labs), reflecting institutional interest in network-level privacy.

### How the mixnet defeats metadata correlation

The threat model Nym targets is a **global passive adversary** — an observer that can watch every link of the network at once (e.g. a large ISP, a state-level surveillance program, or a backbone tap). Against such an adversary, ordinary encryption and even Tor are weak: encryption hides payloads but not the *pattern* of communication, and Tor's onion routing keeps packet timing and size intact, so an adversary that sees both ends can correlate them. Nym layers three defenses to break this:

1. **Mixing (batch-and-reorder).** Each mix node holds incoming packets briefly, then releases them in a reshuffled order. An observer watching a node's input and output streams cannot tell which outgoing packet corresponds to which incoming one — the per-packet timing link is destroyed.
2. **Uniform packets (Sphinx).** Every packet is padded to the same fixed size and reformatted with the layered Sphinx format, so packets are bit-for-bit indistinguishable in transit and an adversary cannot fingerprint flows by size.
3. **Cover (dummy) traffic.** Nodes and clients inject decoy packets so that "is anyone talking right now" is itself hidden — real messages hide in a constant background of noise.

Traffic traverses a layered topology (entry gateway → several mix layers → exit gateway), and the per-layer mixing compounds: the anonymity set grows with each hop. This is the same Stop-and-Go / continuous-time mix lineage as classic mixnet research, productized as a tokenized [[depin|DePIN]] network rather than a volunteer relay set.

## Token Role (NYM)

- **Payment for bandwidth** — users pay NYM (e.g. via NymVPN credentials) to use the mixnet.
- **[[staking]] & node incentives** — operators stake NYM and earn rewards for providing quality bandwidth; delegators can stake toward nodes, and misbehavior/poor quality is penalized. Rewards are tied to measured quality-of-service so that the incentive layer pushes the network toward reliable, well-behaved routing rather than mere uptime.
- **Governance** — NYM carries governance rights over network parameters.

Supply is largely circulating (~831M of a 1.00B max supply; MC/FDV ≈ 0.83), limiting (but not eliminating) future dilution — a notably *higher* float than the thin-float ZK-infra cohort it is often grouped with.

## Competitive Position

Nym competes with both centralized privacy tools (commercial VPNs) and decentralized alternatives. Its differentiation is the mixnet's stronger anonymity model versus VPNs and even Tor against a global passive adversary, paired with a token-incentivized [[depin|DePIN]] operator set.

| Project | Privacy model | Decentralization | Key trade-off |
|---|---|---|---|
| **Nym (NYM)** | Mixnet (mix + cover traffic + Sphinx) — defeats global passive adversary | Tokenized DePIN operator set | Highest latency; hardest to monetize |
| **Tor** | Onion routing (no mixing) | Volunteer relays, no token | Vulnerable to global timing correlation; free but unincentivized |
| **Orchid (OXT)** | Incentivized multi-hop VPN/onion bandwidth market | Tokenized bandwidth marketplace | VPN-grade, not mixnet-grade metadata privacy |
| **Commercial VPNs** | Single-hop encryption, trusted operator | Centralized | Fast, but the operator sees everything |

The core commercial test is converting a strong cryptographic story into paying users: mixing adds latency, and most users prioritize speed over metadata privacy.

## Narrative & Catalysts

Nym sits at the crossing of two narratives — **privacy** and **[[depin|DePIN]]** — both of which are sentiment-driven and tend to outperform in risk-on, "censorship-resistance" news cycles and underperform in risk-off tape. The principal value catalyst is **NymVPN adoption**: a consumer product that converts the mixnet's anonymity guarantee into recurring, paid bandwidth demand is the bridge from narrative to fundamentals. Secondary catalysts include integrations that route third-party app traffic through the mixnet and any regulatory developments that raise the salience of metadata privacy.

## History & Timeline

- **2022-04-15** — NYM reaches its all-time high of **$5.76** during the prior cycle's privacy/DePIN enthusiasm (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-02-05** — NYM prints its all-time low of **$0.0222** amid the broad bear market (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.0179, ~99% below ATH; market cap ~$15M, rank #957 (cryptodataapi.com / CoinGecko).

> Only real, dated price events from the ingested snapshot are listed here. Founding/TGE dates are not asserted because no specific dated source for them has been ingested.

## Risks

- **Adoption / demand** — value requires real paying bandwidth demand; privacy is a hard product to monetize at scale.
- **Latency vs. usability trade-off** — mixnet privacy is inherently slower, limiting mainstream appeal versus fast VPNs.
- **Regulatory pressure** — strong anonymity tooling attracts regulatory and law-enforcement scrutiny in some jurisdictions; potential delisting or geofencing risk.
- **Narrative dependence** — trades with the privacy/DePIN narrative cycle and underperforms in risk-off conditions like the current Extreme-Fear bear regime.
- **Low liquidity** — ~$15M market cap with thin daily volume (~$1M/24h); volatile on size, with material slippage on larger orders.

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** A ~$15M-cap privacy/DePIN microcap is a high-beta, narrative-driven asset; in a bear tape with BTC ~16% below its 200-day MA, the path of least resistance for such names is sideways-to-down with sharp, news-driven spikes.
- **Liquidity discipline.** Thin volume means market orders move price; size down and use limits. The ~99% drawdown from ATH is a sign of how far these names fall, not a floor.
- **Catalyst-driven only.** Without a NymVPN-adoption or privacy-news catalyst, there is little fundamental pull; treat any bounce as narrative-driven and manage risk tightly.
- **Asymmetry.** High float (MC/FDV ≈ 0.83) means *less* unlock overhang than thin-float peers — a relative positive if the privacy narrative re-rates.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 831.42M NYM |
| **Total Supply** | 1.00B NYM |
| **Max Supply** | 1.00B NYM |
| **Fully Diluted Valuation** | $35.10M |
| **Market Cap / FDV Ratio** | 0.83 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5.76 (2022-04-15) |
| **Current vs ATH** | -99.39% |
| **All-Time Low** | $0.0222 (2026-02-05) |
| **Current vs ATL** | +57.48% |
| **24h Change** | +0.59% |
| **7d Change** | +2.23% |
| **30d Change** | +53.64% |
| **1y Change** | -33.70% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x525a8f6f3ba4752868cde25164382bfbae3990e1` |
| Osmosis | `ibc/37CB3078432510EE57B9AFA8DBE028B33AE3280A144826FEAC5F2334CF2C5539` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | NYM/USD | N/A |
| Bitget | NYM/USDT | N/A |
| KuCoin | NYM/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X525A8F6F3BA4752868CDE25164382BFBAE3990E1/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://nym.com](https://nym.com) |
| **Twitter** | [@nym](https://twitter.com/nym) |
| **Reddit** | [https://www.reddit.com/r/nym](https://www.reddit.com/r/nym) |
| **Telegram** | [nymchan](https://t.me/nymchan) (34,690 members) |
| **Discord** | [https://discord.gg/nym](https://discord.gg/nym) |
| **GitHub** | [https://github.com/nymtech/nym/](https://github.com/nymtech/nym/) |
| **Whitepaper** | [https://nym.com/nym-whitepaper.pdf](https://nym.com/nym-whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,544 |
| **GitHub Forks** | 250 |
| **Commits (4 weeks)** | 74 |
| **Pull Requests Merged** | 1,866 |
| **Contributors** | 49 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.02M |
| **Market Cap Rank** | #952 |
| **24h Range** | $0.0346 — $0.0353 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[privacy-coins]]
- [[depin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- Project documentation and architecture descriptions: general market knowledge; no additional specific wiki source ingested yet.
