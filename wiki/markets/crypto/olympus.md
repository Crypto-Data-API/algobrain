---
title: "Olympus"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["OHM", "OlympusDAO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://olympusdao.finance/"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[liquidity-pool]]", "[[uniswap]]", "[[yield-farming]]"]
---

# Olympus

**Olympus** (ticker **OHM**) is a decentralized finance ([[defi|DeFi]]) protocol on [[ethereum|Ethereum]] building "programmable monetary infrastructure." Its core asset, **OHM**, is a **treasury-backed token** managed on-chain. Olympus pioneered the **Protocol-Owned Liquidity (POL)** and "bonding" model — the original "(3,3)" DeFi 2.0 design — and now operates a suite of on-chain monetary tools aimed at solvency and self-sustaining liquidity.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | OHM |
| **Native Chain** | [[ethereum|Ethereum]] (multi-chain: Arbitrum, Optimism, Base, Berachain, Solana) |
| **Market Cap Rank** | #149 |
| **Market Cap** | $238.02M |
| **Current Price** | $15.91 |
| **24h Volume** | $94,809 |
| **24h Change** | -0.16% |
| **7d Change** | -3.35% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market is in an **Established Bear Market** with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** as of 2026-06-21. OHM is roughly flat on the day and down ~3% on the week. Notably, **24h volume is only ~$95K against a ~$238M market cap** (turnover ~0.04%) — extraordinarily low, characteristic of a token where most supply is locked in protocol-owned liquidity and long-term staked holders rather than actively traded.

---

## Technology & Protocol

Olympus reframes a DeFi token as **on-chain monetary infrastructure** — effectively a decentralized, treasury-backed reserve currency with programmable policy. Core mechanisms:

- **Protocol-Owned Liquidity (POL)** — instead of *renting* liquidity with farm emissions (the mercenary-LP problem), Olympus's **treasury owns the LP positions** themselves, so the protocol earns its own [[liquidity-pool|pool]] trading fees and cannot have liquidity withdrawn by yield-chasers. POL was Olympus's signature innovation and was widely forked across DeFi.
- **Bonding** — users sell assets (or LP tokens) to the treasury for discounted OHM vesting over days; this is how the treasury historically *acquired* its POL and reserves.
- **Backing / RFV** — each OHM is nominally backed by treasury reserves (the "risk-free value" / backing-per-OHM concept), establishing a notional price floor.
- **Range Bound Stability (RBS)** — a now-legacy automated market-operations system that bought/sold OHM at defined bands around its moving average to dampen volatility.
- **Cooler Loans** — borrow stablecoins against gOHM at fixed, no-liquidation terms, turning treasury backing into usable credit.
- **Convertible Deposits (CDs)** and the **Yield Repurchase Facility (YRF)** — newer tools that deploy treasury yield to buy back OHM and manage supply, repositioning OHM as **backed money** rather than a high-yield farm.

Together these constitute a "programmable central bank" running entirely on-chain.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 14.96M OHM |
| **Total Supply** | 19.84M OHM |
| **Max Supply** | Uncapped (elastic) |
| **Circulating / Total** | ~75.4% |
| **All-Time High** | $1,415.26 (2021-04-25) |
| **All-Time Low** | $7.54 (2022-11-26) |

OHM has **no fixed max supply** — historically it was a **rebase token** whose supply expanded via staking rewards, with each OHM nominally backed by treasury reserves (the "risk-free value" / backing-per-OHM concept). The protocol's later reforms (post-RBS era) sharply reduced inflationary rebasing and pivoted toward treasury-backed value, buybacks (YRF), and credit (Cooler Loans). With ~75% of total supply circulating and the rest in treasury/locked positions, the relevant valuation anchor is **treasury backing per OHM**, not a fixed cap. The extremely low trading volume reflects deep Protocol-Owned Liquidity and staked supply rather than illiquidity from a thin float.

---

## Market Structure & Derivatives

**Centralized venues:** OHM has limited CEX presence; trading is **predominantly on-chain**, which is by design — Olympus owns most of its own liquidity rather than relying on third-party market makers.

**On-chain / protocol mechanics:** OHM trades via **[[uniswap]] V3/V2**, **Sushiswap**, and **Balancer V2** (OHM/DAI, OHM/WETH, OHM/gOHM) on [[ethereum]]. The defining mechanic is **Protocol-Owned Liquidity (POL)**: instead of renting liquidity with farm emissions, Olympus's treasury *owns* the [[liquidity-pool]] LP positions, so it earns its own trading fees and cannot have liquidity "rugged" by mercenary LPs. Additional tools include **Cooler Loans** (borrow against gOHM at fixed terms), **Convertible Deposits**, the **Yield Repurchase Facility (YRF)**, and historically **Range Bound Stability (RBS)** — together a "programmable central bank."

**Derivatives:** OHM is not a meaningful perpetuals listing; with ~$107K daily volume, price discovery is entirely on-chain spot. Funding/OI are not relevant signals here.

---

## Narrative & Category

Olympus is the canonical **"DeFi 2.0" / Protocol-Owned Liquidity** narrative. Its original "(3,3)" game-theory framing (stake/bond cooperation) drove a 2021 mania; today the protocol positions OHM as **decentralized treasury-backed money** with on-chain monetary policy. Categories include Crypto-Backed Tokens, DeFi, [[yield-farming]], Rebase Tokens, Lending/Borrowing, and Governance. Its POL innovation was widely forked across DeFi (Wonderland/TIME, KlimaDAO, and dozens of "(3,3)" clones).

---

## Valuation Framing

Olympus is unusual because it has an explicit **balance-sheet anchor**: the treasury holds reserves backing OHM, so the key qualitative question is the **market-cap-to-backing premium** (the modern descendant of the old "premium over RFV"). When OHM trades far above backing, the implied bet is on future treasury growth and policy credibility; when it trades near backing, downside is theoretically cushioned by the floor (modulo treasury-asset risk). At ~$238M market cap the token is valued for its credible-money repositioning and Cooler Loans / buyback machinery rather than the discredited high-APY farm of 2021. The near-zero trading volume means the on-screen price is a weak signal — backing-per-OHM and treasury composition are the better gauges.

---

## Peer Comparison

| Protocol | Token | Model | MC Rank | Market Cap | Notes |
|---|---|---|---|---|---|
| **Olympus** | OHM | Treasury-backed / POL | #149 | ~$238M | Original DeFi-2.0; backing floor; buybacks |
| Frax / FXS | FXS | Algorithmic + collateral | mid-cap | — | Fractional-reserve stable + governance |
| KlimaDAO | KLIMA | Carbon-backed (OHM fork) | micro-cap | — | Forked POL/(3,3) onto carbon credits |
| [[reserve-rights-token\|Reserve]] | RSR | Overcollateralized RTokens | #306 | ~$81M | Different model: staked first-loss capital |

*Figures for non-Olympus peers are illustrative category placement, not snapshot data.*

---

## Notable History

- **2021 mania:** OHM rocketed to an ATH of **$1,415.26** (April 2021) on the "(3,3)" staking-yield meme, with quadruple-digit APYs.
- **2022 collapse:** as the market turned, the reflexive high-APY model unwound violently; OHM fell to an ATL of **$7.54** (Nov 2022) — a cautionary tale of unsustainable emissions ("Ponzinomics" critiques).
- **Reform era:** OlympusDAO pivoted away from hyper-inflationary rebasing toward treasury-backed value, RBS, Cooler Loans, and the YRF, repositioning OHM as backed money rather than a high-yield farm. It now trades in the mid-teens (~$16), ~99% below ATH but well above its 2022 low.

---

## Risks

- **Reflexivity / model risk** — the original (3,3) design proved fragile under selling pressure; any return to inflationary mechanics carries blow-up risk.
- **Liquidity / exit risk** — extremely low daily volume (~$107K) means real sell pressure could move price sharply; thin two-way market.
- **Treasury/backing risk** — OHM's value rests on treasury composition and on-chain backing assumptions; treasury drawdowns directly impair the floor.
- **Smart-contract complexity** — POL, Cooler Loans, CDs, YRF and RBS are an intricate, evolving attack surface.
- **Bear-market beta & reputation** — carries DeFi-2.0 stigma from the 2022 collapse; high-beta into extreme-fear conditions (F&G 23).

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[defi]]
- [[liquidity-pool]]
- [[uniswap]]
- [[yield-farming]]
- [[reserve-rights-token]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 from CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | OHM |
| **Market Cap Rank** | #137 |
| **Market Cap** | $272.32M |
| **Current Price** | $18.23 |
| **Categories** | Crypto-Backed Tokens, Decentralized Finance (DeFi), Lending/Borrowing Protocols, Cross-chain Communication, Governance |
| **Website** | [https://olympusdao.finance/](https://olympusdao.finance/) |

---

## Overview

Olympus is a decentralized financial (DeFi) protocol building programmable monetary infrastructure. At its core is OHM, a treasury-backed token held and managed on-chain.

The protocol is built for solvency, self-sustaining liquidity, and policy-driven equilibrium. This guides how value, liquidity, and credit are managed, through on-chain mechanisms including Protocol Owned Liquidity (POL), Cooler Loans, Convertible Deposits (CDs), the Yield Repurchase Facility (YRF), and Range Bound Stability (RBS).

Together, these components form a programmable central bank, without human bias.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 14.94M OHM |
| **Total Supply** | 19.83M OHM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $361.52M |
| **Market Cap / FDV Ratio** | 0.75 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1,415.26 (2021-04-25) |
| **Current vs ATH** | -98.71% |
| **All-Time Low** | $7.54 (2022-11-26) |
| **Current vs ATL** | +141.68% |
| **24h Change** | +0.92% |
| **7d Change** | +6.50% |
| **30d Change** | +13.36% |
| **1y Change** | -14.21% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` |
| Berachain | `0x18878df23e2a36f81e820e4b47b4a40576d3159c` |
| Optimistic Ethereum | `0x060cb087a9730e13aa191f31a6d86bff8dfcdcc0` |
| Solana | `2Xva1NeLRuBFdK41gEuXqgeWtnKKDve9PKeCnMEpNG6K` |
| Base | `0x060cb087a9730e13aa191f31a6d86bff8dfcdcc0` |
| Arbitrum One | `0xf0cb2dc0db5e6c66b9a70ac27b06b878da017028` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X64AA3364F17A4D01C6F1751FD97C2BD3D7E7F1D5/0XA3931D71877C0E7A3148CB7EB4463524FEC27FBD | Spot |
| Uniswap V2 (Ethereum) | 0X64AA3364F17A4D01C6F1751FD97C2BD3D7E7F1D5/0X857FFC55B1AA61A7FF847C82072790CAE73CD883 | Spot |
| Sushiswap | 0X64AA3364F17A4D01C6F1751FD97C2BD3D7E7F1D5/0X6B175474E89094C44DA98B954EEDEAC495271D0F | Spot |
| Balancer V2 | 0X64AA3364F17A4D01C6F1751FD97C2BD3D7E7F1D5/0X7F39C581F595B53C5CB19BD0B3F8DA6C935E2CA0 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://olympusdao.finance/](https://olympusdao.finance/) |
| **Twitter** | [@OlympusDAO](https://twitter.com/OlympusDAO) |
| **Reddit** | [https://www.reddit.com/r/olympusdao/](https://www.reddit.com/r/olympusdao/) |
| **Telegram** | [OlympusTG](https://t.me/OlympusTG) (3,131 members) |
| **Discord** | [https://discord.gg/olympusdao](https://discord.gg/olympusdao) |
| **GitHub** | [https://github.com/OlympusDAO](https://github.com/OlympusDAO) |
| **Whitepaper** | [https://docs.olympusdao.finance/](https://docs.olympusdao.finance/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6,721.54 |
| **Market Cap Rank** | #137 |
| **24h Range** | $17.84 — $18.56 |
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
- [[ethereum]]

---
