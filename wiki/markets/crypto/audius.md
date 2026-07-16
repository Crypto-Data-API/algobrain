---
title: "Audius"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, nft, defi]
aliases: ["AUDIO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://audius.co/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[governance-token]]", "[[solana]]", "[[binance]]", "[[dca-strategy]]", "[[rsi-mean-reversion]]"]
---

# Audius

**Audius** (AUDIO) is a decentralized music-streaming protocol that lets artists publish and monetize music directly to listeners without traditional label or platform intermediaries. Content is hosted by a network of node operators, and the **AUDIO** token is used for [[staking]] (network security), [[governance-token|governance]], and unlocking features. Audius is often described as a Web3 alternative to SoundCloud/Spotify.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* In a broad crypto bear regime (BTC ~$64,390; Fear & Greed Index 21 — "Extreme Fear"), AUDIO traded around **$0.0147121**, ranked **#801** by market cap (~**$21,052,409**), down **-2.17%** on the day and **down -4.48%** over 7 days.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AUDIO |
| **Market Cap Rank** | #801 |
| **Market Cap** | $21,052,409 |
| **Current Price** | $0.0147121 |
| **24h Change** | -2.17% |
| **7d Change** | -4.48% |
| **Categories** | Music, NFT, Solana Ecosystem, Ethereum Ecosystem, Coinbase Ventures Portfolio, Multicoin Capital Portfolio, Pantera Capital Portfolio, Energi Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio, Governance |
| **Website** | [https://audius.co/](https://audius.co/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Audius is a decentralized streaming platform that aims to give artists a more direct relationship with listeners and a larger share of value than traditional streaming services. The protocol coordinates a network of **content nodes** (which store and serve audio) and **discovery nodes** (which index metadata and serve search/feeds). Operators run these nodes and [[staking|stake]] AUDIO to participate, earning rewards for providing infrastructure. Listeners stream for free, while certain premium features and artist tooling are gated by tokens.

Audius runs across multiple chains: the AUDIO token and [[governance-token|governance]] live on [[ethereum|Ethereum]], while much of the high-throughput content/transaction layer has used [[solana|Solana]] for performance and low fees. The project gained mainstream attention through artist partnerships and a 2022 integration that let users share Audius tracks directly into TikTok.

### Token role

The **AUDIO** token has three core functions:

- **Staking / security** — node operators stake AUDIO to run content and discovery nodes; staking aligns operators with network health and earns rewards.
- **Governance** — AUDIO holders vote on protocol proposals through on-chain [[governance-token|governance]].
- **Access / rewards** — AUDIO unlocks features and is distributed as rewards to artists, fans, and operators who contribute to the network.

---

## Architecture Deep Dive

Audius is a multi-layer decentralized streaming stack that separates *who stores the audio* from *who indexes the metadata* from *where value settles*:

- **Content nodes (Creator nodes).** Store and serve the actual audio files and artist content. Operators [[staking|stake]] AUDIO to run them; the network replicates content across nodes for availability and censorship-resistance. This is the storage/CDN layer.
- **Discovery nodes.** Index on-chain and off-chain metadata (tracks, playlists, social graph, play counts) and serve the search, feeds, and APIs that the apps query. They are the read layer that makes the catalog usable.
- **Governance / token layer on [[ethereum]].** The AUDIO token, staking, and on-chain [[governance-token|governance]] live on Ethereum. This is also where the July 2022 exploit occurred — in the governance contracts, not the media layer.
- **High-throughput ledger on [[solana]].** Much of the high-frequency activity (track listens, social actions, tipping) has been recorded on Solana for low fees and high throughput, since putting every play on Ethereum L1 would be prohibitively expensive. This **two-chain split** (settlement/governance on Ethereum, throughput on Solana) is a defining architectural choice and a recurring source of integration complexity.
- **Free-to-stream, token-gated extras.** Listeners stream without holding AUDIO; the token gates premium artist tooling, badges, and certain features, and is distributed as rewards. This is the root of the **token-utility decoupling** risk noted below — usage growth does not mechanically pull AUDIO demand.

The deliberate separation of storage (content nodes) from indexing (discovery nodes) means no single operator controls the catalog, and the protocol can keep serving music even if individual nodes go offline — the decentralization value proposition versus a centralized service whose servers are a single point of control.

---

## Comparison vs Music-Streaming Peers

| Dimension | **Audius** | Spotify | SoundCloud | Apple Music | Other Web3 music (e.g. Sound.xyz) |
|---|---|---|---|---|---|
| Model | **Decentralized protocol** | Centralized | Centralized | Centralized | Decentralized / [[nft\|NFT]]-music |
| Infrastructure | Node operators ([[staking\|staked]]) | Company servers | Company servers | Company servers | Varies |
| Artist payout path | More direct, token rewards | Label/distributor intermediated | Direct-ish, ad/sub revenue | Label intermediated | NFT primary + royalties |
| Catalog scale | Small (independent-artist focused) | **Massive (licensed majors)** | Large | **Massive (licensed majors)** | Small / niche |
| Licensing | Limited major-label deals | Full major-label licensing | Partial | Full major-label licensing | Primary-sale focused |
| Token | AUDIO (stake/govern/access) | None | None | None | Project-specific |
| Censorship-resistance | **High** | Low | Low | Low | High |
| Core weakness | Catalog/network effects; token decoupling | Centralization; low artist pay | Monetization | Centralization | Tiny audience |

Audius' structural disadvantage is the same one that defeats most Web3 media: incumbents own the **licensed major-label catalog** and the **network effects of hundreds of millions of users**. Audius competes on artist economics, censorship-resistance, and an independent-artist niche rather than head-to-head catalog breadth.

---

## Notable History: the July 2022 governance exploit (handled honestly)

In **July 2022**, Audius suffered a serious smart-contract exploit. An attacker exploited a vulnerability in the protocol's **governance contracts** — specifically a flaw related to contract initialization/storage that allowed a malicious governance proposal to be passed and executed. The attacker used this to transfer roughly **18.5 million AUDIO** (worth on the order of ~$1 million at the time, with a larger nominal face value) out of the community treasury, then sold the tokens.

This is an important, honestly-noted risk event for the project:

- It was a **governance/smart-contract** failure, not a failure of the streaming product itself.
- The Audius team paused affected contracts, patched the vulnerability, and put forward remediation; the incident nonetheless dented confidence and highlighted the risks of on-chain treasury governance.
- It exemplifies a recurring DeFi/DAO risk: governance contracts that control a treasury are a high-value attack surface, and initialization or proposal-validation bugs can let an attacker seize funds through ostensibly "legitimate" governance.

See [[governance-token]] and [[dao|DAO]] for the broader pattern of governance-attack risk.

---

## Governance & Value Accrual

- **On-chain governance.** AUDIO holders (and stakers/delegators) vote on protocol proposals — node economics, rewards, and protocol upgrades — through an on-chain [[governance-token|governance]] system on [[ethereum]]. The July 2022 incident was a direct failure of this governance layer, after which contracts were patched and proposal/initialization validation hardened.
- **Value-accrual tension.** AUDIO's hardest problem is **token-utility decoupling**: because listening is free and most users never touch the token, growth in streams does not mechanically translate into AUDIO demand. Value accrues mainly through staking (security/rewards) and governance, not a usage fee that every listener pays — a structurally weaker accrual model than fee-capturing protocols.
- **Emissions.** AUDIO has used ongoing staking and reward emissions that add to circulating supply over time, a persistent dilution factor for holders. Circulating supply is now essentially equal to total supply (MC/FDV ≈ 1.00), so near-term unlock overhang is low, but reward emissions continue.

---

## Competitive Position & Risks

Audius is among the better-known Web3 music projects and has real product usage, but it operates against entrenched incumbents (Spotify, Apple Music, SoundCloud) with vastly larger catalogs, licensing deals, and budgets. Decentralized streaming must overcome music-licensing complexity and the network effects of established platforms.

Key risks:

- **Adoption / network-effect risk** — competing with incumbents on catalog, discovery, and royalty infrastructure is extremely hard.
- **Token-utility decoupling** — listeners can use the app without ever touching AUDIO, so product growth does not automatically accrue to token value.
- **Smart-contract / governance risk** — demonstrated by the July 2022 exploit above.
- **Emissions / inflation** — AUDIO has used ongoing staking and reward emissions, adding supply over time.
- **Low liquidity** — at a ~$21.5M market cap, AUDIO is a small-cap token prone to sharp volatility on thin volume in the current bear regime; it trades roughly 99% below its 2021 all-time high.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.41B AUDIO |
| **Total Supply** | 1.41B AUDIO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $23.93M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.95 (2021-03-27) |
| **Current vs ATH** | -99.66% |
| **All-Time Low** | $0.0163 (2026-04-03) |
| **Current vs ATL** | +3.80% |
| **24h Change** | +0.64% |
| **7d Change** | -1.69% |
| **30d Change** | -17.11% |
| **1y Change** | -70.53% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x18aaa7115705e8be94bffebde57af9bfc265b998` |
| Solana | `9LzCMqDgTKYz9Drzqnpgee3SGa89up3a247ypMj2xrqM` |
| Energi | `0x2c25972d4adb478773be354a09e4596f29e31fb3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AUDIO/USDT | N/A |
| Kraken | AUDIO/USD | N/A |
| Upbit | AUDIO/BTC | N/A |
| Bitget | AUDIO/USDT | N/A |
| KuCoin | AUDIO/USDT | N/A |
| Crypto.com Exchange | AUDIO/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X18AAA7115705E8BE94BFFEBDE57AF9BFC265B998/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Orca | 9LZCMQDGTKYZ9DRZQNPGEE3SGA89UP3A247YPMJ2XRQM/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://audius.co/](https://audius.co/) |
| **Twitter** | [@audius](https://twitter.com/audius) |
| **Reddit** | [https://www.reddit.com/r/audius/](https://www.reddit.com/r/audius/) |
| **Discord** | [http://discord.gg/audius](http://discord.gg/audius) |
| **GitHub** | [https://github.com/AudiusProject](https://github.com/AudiusProject) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.97M |
| **Market Cap Rank** | #778 |
| **24h Range** | $0.0168 — $0.0176 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

AUDIO is **tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply.** With no deep perp market, positions must be built and sized in spot inventory: shorting requires borrow (thin and expensive at this cap) or is effectively unavailable, so the tradable edge is long-only or flat. At a small-cap footprint on thin volume, the single-venue concentration means the Binance AUDIOUSDT order book *is* the liquidity — execution should favor limit orders, patient scaling, and modest clip sizes to avoid slippage, and stop placement must account for wick risk in a thin book. Venue concentration also implies delisting/listing headline sensitivity (see Risk flags).

### Applicable strategies

- [[dca-strategy]] — spot-primary, long-only asset ~99% below its ATH; accumulating in fixed increments smooths entry without needing leverage or short access.
- [[rsi-mean-reversion]] — thin small-cap book produces sharp oversold/overbought wicks on the daily/4h that snap back, favoring fade-the-extreme entries.
- [[bollinger-band-reversion]] — low-liquidity spikes routinely pierce band extremes and revert, a clean spot fade setup with no perp dependency.
- [[range-trading]] — outside narrative catalysts AUDIO chops in bounded ranges at micro-cap prices, letting range boundaries define spot entries/exits.
- [[breakout-and-retest]] — narrative or listing-driven expansions off a long base can be entered on the retest, reducing false-breakout risk in a whippy book.
- [[buy-and-hold]] — for conviction on the decentralized-streaming thesis, a spot hold sidesteps the absent leverage/funding mechanics entirely.

### Volatility & regime character

Small-cap altcoin (rank ~837, ~$21M cap) with high beta to BTC/ETH risk-on/risk-off and amplified downside in bear regimes on thin volume. As an infra/DeFi-adjacent music-streaming and [[governance-token|governance]] token, it carries **narrative reflexivity** — moves are catalyst- and sentiment-driven (Web3-music, DePIN/streaming narratives) rather than fundamentally anchored, given token-utility decoupling. Expect wide intraday ranges relative to large caps, low autocorrelation outside trends, and correlation that spikes toward 1.0 in broad crypto drawdowns.

### Risk flags

- **Liquidity / venue concentration** — spot-only, single primary venue (Binance); no liquid perp, so no hedge/short venue and heightened slippage and delisting-headline risk.
- **Emissions** — ongoing staking/reward emissions add supply over time (dilution), though MC/FDV ≈ 1.00 limits near-term unlock overhang.
- **Narrative dependence** — value accrual is weak (token-utility decoupling); price leans on Web3-music/DePIN narrative flow and sentiment.
- **Smart-contract / governance risk** — history of a governance-contract exploit (July 2022); treasury-governance surface remains a tail risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=AUDIOUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=AUDIOUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=AUDIOUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=AUDIOUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[solana]]
- [[governance-token]]
- [[dao]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
