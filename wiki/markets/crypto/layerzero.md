---
title: "LayerZero"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["ZRO", "LayerZero Labs"]
entity_type: protocol
founded: 2021
headquarters: "Vancouver, Canada (LayerZero Labs)"
website: "https://layerzero.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stargate-finance]]", "[[wormhole]]", "[[hyperliquid]]", "[[base]]", "[[arbitrum]]"]
---

# LayerZero

**LayerZero** (ticker **ZRO**) is the dominant [[cross-chain]] messaging ("omnichain [[interoperability]]") protocol — often described as a **"Layer 0"** — letting smart contracts on one blockchain send verified messages and tokens to another without trusting a single bridge. Founded by Bryan Pellegrino and Ryan Zarick (LayerZero Labs, 2021) and backed by a16z, Sequoia, Multicoin, Circle Ventures and OKX Ventures, it operates across **150+ chains** including [[ethereum]], [[base]], [[arbitrum]], [[solana]], BNB Chain and Polygon, and reported roughly **$133 billion in bridged/messaged volume in 2025**. For traders, ZRO is the purest liquid bet on the [[interoperability]]/bridging infrastructure narrative — and since 2025 it has a direct fee-to-token link via revenue-funded buybacks.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ZRO |
| **Market Cap Rank** | #158 |
| **Market Cap** | $228.91M |
| **Current Price** | $0.906938 |
| **24h Change** | -8.09% |
| **7d Change** | -4.42% |
| **24h Volume** | $26.06M |
| **All-Time High** | $7.47 (2024-12-06) |
| **All-Time Low** | $0.7997 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. ZRO trades roughly 13% above its all-time low (~$0.80) and about 88% below its December-2024 all-time high of $7.47 — having broken decisively below the ~$2 level it held through much of 2025. The -8.1% single-day move is one of the weaker prints in this peer group, consistent with high-beta infra tokens leading the broad sell-off.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZRO |
| **Sector** | [[interoperability]] / [[cross-chain]] messaging (Layer 0) |
| **Token launch (TGE)** | June 2024 |
| **Supply mechanics** | 1.00B max supply; only ~25% circulating (MC/FDV ≈ 0.25) — significant unlock overhang |
| **Value accrual** | Monthly ZRO buybacks funded by Stargate protocol revenue (since late 2025) |
| **Key backers** | Sequoia, a16z, Multicoin, Circle Ventures, OKX Ventures |
| **Website** | [https://layerzero.network/](https://layerzero.network/) |

---

## Technology & Protocol

LayerZero is **not a blockchain** — it is an omnichain messaging protocol that sits alongside existing [[layer-1]] and [[layer-2]] chains and moves arbitrary data between them. Its core design separates message *transport* from message *verification*:

- **Endpoints.** An immutable on-chain smart contract deployed on every connected chain; applications send and receive messages through it.
- **DVNs (Decentralized Verifier Networks).** In LayerZero V2, applications configure a *set* of independent verifiers (e.g. Google Cloud, Polyhedra, plus the protocol's own) that must attest a message is valid. This replaces V1's single oracle+relayer model and lets each app tune its own security/cost trade-off.
- **Executors.** Off-chain agents that deliver the verified message and pay destination gas, abstracting cross-chain gas from the user.
- **OFT / ONFT standards.** The Omnichain Fungible Token (OFT) and NFT standards let a token exist natively at the *same address* across many chains, burning on the source and minting on the destination rather than wrapping — the model used by [[stargate-finance|Stargate]] and ZRO itself.

This "configurable trust" architecture is the protocol's main differentiator versus a monolithic bridge: there is no single shared validator set whose compromise drains every connected app, in contrast to the bridge-hack pattern that defined 2021-22.

---

## Major News & Events

- **Aug 24, 2025 — Stargate acquisition.** The Stargate DAO voted (~88.6% approval, highest turnout in its history) to accept the LayerZero Foundation's **$110M acquisition** of [[stargate-finance|Stargate]], dissolving the DAO and swapping all STG for ZRO at a fixed ratio of **1 STG = 0.08634 ZRO**. LayerZero won despite [[wormhole|Wormhole]] bidding $120M in USDC — the DAO preferred strategic alignment over the higher cash offer. (Sources: DL News, The Defiant, Unchained)
- **Late 2025 — ZRO buyback program.** Stargate revenue now funds **monthly open-market ZRO buybacks**. Sep–Nov 2025: $2.4M revenue generated, $1.2M used to buy ZRO. After the six-month revenue-share window closed in **February 2026**, 100% of Stargate protocol revenue flows to ZRO buybacks. (Source: LayerZero blog)
- **2025 — V2 scale.** Protocol reported operating across 150+ chains with ~$133B in 2025 volume.
- **Price history:** ATH $7.47 (Dec 2024). ZRO spent most of 2025 in a downtrend, holding ~$2 before breaking lower into the 2026 bear market; as of 2026-06-21 it trades ~$0.91, near its all-time low of ~$0.80.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~252.33M ZRO |
| **Total / Max Supply** | 1.00B ZRO |
| **Fully Diluted Valuation (FDV)** | ~$906.9M |
| **Market Cap / FDV Ratio** | ~0.25 |

With only ~25% of max supply circulating, **MC/FDV ≈ 0.25** flags a heavy dilution overhang: roughly three-quarters of the 1.00B supply (team, investors, ecosystem, community allocations) is still vesting and will reach the market over the coming years. Value accrual runs the other direction via **monthly open-market ZRO buybacks** funded by [[stargate-finance|Stargate]] protocol revenue — after the six-month revenue-share window closed in February 2026, 100% of Stargate fees flow to buybacks. The net token-supply trajectory therefore depends on whether buyback demand can offset unlock-driven emission; in a bear tape, unlock supply tends to dominate. ZRO is also the protocol governance token.

---

## Market Structure & Derivatives

- **Spot venues:** Binance, [[kraken|Kraken]], Upbit, Bitget, KuCoin, Crypto.com; Uniswap V3 on [[ethereum|Ethereum]] (and OFT deployments across chains).
- **Derivatives:** **[[hyperliquid|Hyperliquid]] ZRO-PERP**, plus perps on major centralized derivatives venues. At a ~$229M cap with ~$26M daily volume, ZRO is the most liquid name in this peer set — but funding and open interest still swing sharply around unlock dates and buyback announcements; verify live before sizing leverage.
- **Flow signals:** monthly buyback announcements now act as a recurring on-chain demand signal; the unlock calendar acts as the recurring supply signal. Watching the two against each other is the core ZRO trade.

---

## Narrative & Category

ZRO is the bellwether of the **[[interoperability]] / [[cross-chain]] infrastructure** basket, trading alongside [[wormhole]] (W), Axelar, Chainlink CCIP, and (more loosely) the omnichain-L1 names [[zetachain]] and Hyperlane. It rotates with the broader [[l1-l2-rotation]] infra trade and tends to lead both up and down as a high-beta proxy for "is multichain activity expanding?". Categories: Interoperability, Cross-chain Communication, Layer 0, plus VC-portfolio tags (a16z, Sequoia, Multicoin, OKX Ventures).

---

## Valuation Framing (qualitative)

LayerZero is unusual among small/mid-caps in having an explicit fee-to-token link: Stargate revenue → ZRO buybacks. That gives it a (thin) cash-flow anchor most interoperability tokens lack, and a ~$229M cap on a protocol that routed ~$133B in 2025 volume looks low on a price-to-volume basis. The offsetting bear case is structural: **MC/FDV ≈ 0.25** means today's price is set against only a quarter of eventual supply, so even modest unlock-era selling can overwhelm buyback demand. Bridging is also winner-take-most — dominance is the bull thesis, but it concentrates exploit tail risk. Net: a usage/flow story gated by a multi-year dilution schedule and the macro [[market-regime]]. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | Native chain |
|---|---|---|---|---|---|---|
| **LayerZero** | ZRO | Omnichain messaging (L0) | #158 | $228.91M | ~0.25 | None (cross-chain) |
| [[wormhole]] | W | Cross-chain messaging | — | — | — | None (cross-chain) |
| [[zetachain]] | ZETA | Omnichain [[layer-1]] | #426 | $54.23M | ~0.70 | Own L1 (Cosmos) |
| [[monad]] | MON | Parallel-EVM L1 | #147 | $243.00M | ~0.12 | Own L1 |

*ZRO is the most liquid interoperability token here; ZetaChain is a competing omnichain design built as its own settlement L1 rather than a messaging overlay.*

---

## Risks

- **Dilution overhang.** MC/FDV ≈ 0.25 — ~75% of supply still vesting; unlock-driven selling can dominate fundamentals and outpace buyback demand in a weak tape.
- **Bridge / interoperability tail risk.** Cross-chain infrastructure is the highest-value exploit target in crypto (cf. the [[wormhole|Wormhole]] $325M hack, 2022). LayerZero's configurable-DVN model spreads this risk but does not eliminate it; a misconfigured or compromised verifier set on a major app is an ever-present tail.
- **Winner-take-most competition.** Interoperability is a concentrated market; loss of dominance to Wormhole, CCIP, or a native chain-abstraction approach would undercut the volume base that funds buybacks.
- **Buyback dependence.** The token's value-accrual story rests on Stargate revenue scaling with usage — an unproven flywheel if cross-chain volume contracts.
- **Liquidity / volatility.** High-beta infra token; the -8.1% daily move underscores drawdown risk in an extreme-fear regime.

---

## Platform & Chain Information

**Native Chain:** Ethereum (OFT deployed at the same address across chains)

| Chain | Address |
|---|---|
| Ethereum / Base / Polygon / BSC / Arbitrum / Optimism / Avalanche | `0x6985884c4392d348587b19cb9eaaf157f13271cd` |

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://layerzero.network/](https://layerzero.network/) |
| **Twitter** | [@LayerZero_Core](https://twitter.com/LayerZero_Core) |
| **Whitepaper** | [LayerZero V2 Whitepaper](https://layerzero.network/publications/LayerZero_Whitepaper_V2.1.1.pdf) |

---

## Related

- [[crypto-markets]]
- [[stargate-finance]] — acquired by LayerZero, STG→ZRO swap
- [[wormhole]] — main interoperability competitor (lost the Stargate bid)
- [[zetachain]] — competing omnichain L1
- [[interoperability]], [[cross-chain]]
- [[ethereum]], [[base]], [[arbitrum]], [[solana]]
- [[hyperliquid]] — ZRO-PERP venue
- [[l1-l2-rotation]]

---

## Sources

- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json` (market data block above)
- CoinGecko top-1000 snapshot, 2026-04-09 (historical context)
- [Unchained — LayerZero Foundation proposes $110M Stargate acquisition](https://unchainedcrypto.com/layerzero-foundation-proposes-110-million-stargate-acquisition-retiring-stg-for-zro-tokens/)
- [The Defiant — Stargate approves $110M takeover by LayerZero](https://thedefiant.io/news/defi/stargate-approves-usd110-million-takeover-by-layerzero)
- [DL News — LayerZero pips rivals to $110M Stargate acquisition](https://www.dlnews.com/articles/defi/layerzero-pips-rivals-110m-stargate-deal-dao-dissolves/)
- [LayerZero blog — Understanding ZRO buybacks](https://layerzero.network/blog/understanding-zro-buybacks)
- Perplexity sonar verification, 2026-06-10
