---
title: "Uniswap"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["UNI", "Uniswap Protocol", "UNIfication"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized protocol; Uniswap Labs: New York, USA"
website: "https://uniswap.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-exchange]]", "[[decentralized-exchanges]]", "[[automated-market-maker]]", "[[aave]]", "[[hyperliquid]]", "[[sky]]", "[[narrative-trading]]"]
---

# Uniswap

**Uniswap** (UNI) is the largest decentralized exchange protocol — the AMM that defined DeFi, with **~$4 trillion cumulative volume across 43 chains** as of 2026. UNI is its governance token, transformed in late 2025 by the **"UNIfication" proposal**: governance voted (99.9% in favor, concluded 2025-12-25) to finally **activate the protocol fee switch and route fees to UNI burns**, plus an immediate **100M UNI burn (~$600M)** — converting UNI from a pure governance token into a cash-flow-linked, deflationary asset. Market cap **$1.87B, rank #45 (2026-06-20)**.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in an **established bear market**. Against that tape UNI is a notable outperformer — **+19.53% over 7 days** — as the post-UNIfication burn mechanic and fee-switch yield narrative draw flows even while the broad market bleeds.

| Metric | Value |
|---|---|
| **Price** | $2.99 |
| **Market Cap** | $1,865,846,458 |
| **Market Cap Rank** | #45 |
| **24h Volume** | $199,162,550 |
| **24h Change** | -1.79% |
| **7d Change** | +19.53% |
| **24h Range** | $3.00 – $3.12 |
| **Circulating Supply** | 621,671,562 UNI |
| **Total Supply** | 893,806,420 UNI |
| **Max Supply** | 1,000,000,000 UNI (net of burns) |
| **Fully Diluted Valuation** | $2,682,615,140 |
| **Market Cap / FDV** | ~0.70 |
| **All-Time High** | $44.92 (2021-05-03) — **-93.31%** from ATH |
| **All-Time Low** | $1.03 (2020-09-17) — **+191.51%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | UNI |
| **Type** | [[decentralized-exchange\|DEX]] governance/value-accrual token (AMM protocol fees → burns post-UNIfication) |
| **Market Cap** | $1.87B, rank #45 (2026-06-20); price $2.99 |
| **Protocol scale** | ~$4T cumulative volume, 43 chains; consistently #1 DEX by volume on Ethereum mainnet |
| **Versions** | v2 (2020), v3 concentrated liquidity (2021), **v4 hooks (Jan 2025)**, **Unichain L2 (Feb 2025)** |
| **Fee switch** | UNIfication passed Dec 2025: protocol fees on v2/v3 pools (≈95% of mainnet LP fees in scope) diverted to UNI burns; Labs front-end fees switched off |
| **Burn** | 100M UNI (~10% of max supply, ~$600M) burned at activation |
| **Categories** | [[decentralized-exchange\|DEX]], DeFi, [[automated-market-maker\|AMM]], Governance |
| **Website** | [https://uniswap.org/](https://uniswap.org/) |

---

## Overview

UNI is the governance token for Uniswap, the automated market maker (AMM) DEX deployed on Ethereum and 40+ other chains. Token holders govern the protocol: treasury usage, upgrades, and — decisively in 2025 — fee policy.

### 2025–2026 developments

- **2025-01** — **Uniswap v4** launched: singleton architecture + "hooks" (custom pool logic), cutting gas and enabling bespoke AMM designs.
- **2025-02** — **Unichain**, Uniswap Labs' OP-stack L2, went live mainnet; UNI has a native representation there; aimed at consolidating DEX flow and MEV capture in-house.
- **2025-11-10** — Uniswap Labs + Foundation jointly proposed **UNIfication**: activate the long-dormant fee switch, redirect a share of LP trading fees to **burning UNI**, burn 100M treasury UNI upfront, retire Labs' front-end/interface fees, and refocus Labs on protocol development. UNI spiked ~40–60% on the announcement.
- **2025-12-25** — On-chain vote concluded: **passed with 99.9% support** (~125M UNI for vs 742 against). After timelock: 100M UNI burned, fee switches flipped on v2/v3 mainnet pools (~95% of LP fees collected on mainnet now subject to the protocol-fee split).
- **2026** — UNI now has a "real yield"-style burn linked to DEX volumes. The token spent Q2 2026 around $2.5–3 amid the broader alt bear (UNI **$2.99 on 2026-06-20, -93.3% from its $44.92 ATH**), but staged a **+19.5% 7-day move into 2026-06-20** as fee-burn flows attracted buyers despite an extreme-fear market.

---

## Protocol & Technology

Uniswap is the canonical [[automated-market-maker|AMM]] [[decentralized-exchange|DEX]]: instead of an order book, liquidity providers (LPs) deposit pairs of tokens into pools and traders swap against the pool, with prices set by a deterministic curve. Each version refined the design.

### v2 (2020) — constant-product AMM
The `x * y = k` constant-product formula. LPs deposit a 50/50 pair; price is the ratio of reserves; a 0.30% fee accrues to LPs pro-rata. Simple, robust, composable — v2 pools (UNI/WETH etc.) remain reference liquidity. Weakness: capital spread across the entire 0→∞ price range, so most of it is idle.

### v3 (2021) — concentrated liquidity
LPs choose a **price range** to provide liquidity in, concentrating capital where trading happens. This delivered orders-of-magnitude better capital efficiency and tighter spreads, but turned LPing into an active, [[impermanent-loss]]-sensitive position (positions go one-sided and stop earning when price exits the range). Multiple fee tiers (0.01% / 0.05% / 0.30% / 1.00%) let pools match volatility.

### v4 (Jan 2025) — singleton + hooks
- **Singleton architecture**: all pools live in one contract, slashing the gas cost of pool creation and multi-hop swaps.
- **Hooks**: pools can attach custom logic at lifecycle points (before/after swap, before/after LP add/remove). This enables on-chain limit orders, dynamic fees, TWAMM, custom oracles (including [[chainlink|Chainlink]] feeds), MEV-internalization and KYC'd pools — turning Uniswap into a programmable AMM platform rather than a fixed product.
- **Flash accounting & native ETH**: net balance settlement reduces token-transfer overhead; native ETH pools remove WETH wrapping costs.

### Unichain (Feb 2025) — Uniswap's own L2
An OP-stack [[layer-2|L2]] in the Optimism Superchain built to consolidate Uniswap flow, capture MEV in-house, and offer fast/cheap swaps. UNI has a native representation there; routing Uniswap volume to Unichain is a strategic lever for value capture.

### The fee switch (UNIfication, Dec 2025)
For years UNI accrued **no protocol revenue** — the "fee switch" that would divert a slice of the LP fee to the protocol was dormant. **UNIfication** (passed 99.9%, Dec 2025) finally activated it on v2/v3 mainnet pools (~95% of mainnet LP fees in scope) and routes the protocol share to **burning UNI**, plus a one-time 100M UNI (~$600M) burn. The mechanism: trading volume × in-scope fee × protocol split → UNI bought and burned. This is the structural change that makes UNI a cash-flow-linked, deflationary asset rather than a pure governance token. The trade-off: the protocol share comes out of the LP take, a potential push factor for LPs toward rival venues.

---

## Trading Relevance

- **Where it trades**: deep spot on Binance, Coinbase, Kraken, Upbit, Bitget, KuCoin; perps on [[hyperliquid|Hyperliquid]] (UNI-PERP), Binance, Bybit, OKX. ~$150M+ daily spot volume. Self-referentially, UNI/WETH and UNI/WBTC pools on Uniswap itself.
- **Narrative basket**: anchor of the **"DeFi fee-switch / real-yield" basket** with AAVE, [[sky|SKY]] (buybacks), LDO — the late-2025 trade was long tokens converting fees into buybacks/burns. UNIfication was the basket's marquee event.
- **Valuation handle**: post-UNIfication, UNI can be modeled on burn yield = f(DEX volume × fee share). Track Uniswap volumes (mainnet + Unichain) as the fundamental driver; volume downturns now hit the token mechanically, not just narratively.
- **Catalysts**: burn-rate reports, v4 hook adoption, Unichain volume migration, expansion of fee switch to more pools/chains, regulatory clarity for DEX front-ends (the SEC dropped its Uniswap Labs probe in early 2025).
- **Risks**: LP exodus if protocol fees push LPs to rival venues (fee split comes out of LP take), aggregator/intent-flow disintermediation, competition from Hyperliquid-style appchains and Solana DEXes.

---

## Tokenomics & Supply

> *Authoritative figures are in the [[uniswap#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 621,671,562 UNI |
| **Total Supply** | 893,806,420 UNI |
| **Max Supply** | 1,000,000,000 UNI (net of burns) |
| **Fully Diluted Valuation** | $2,682,615,140 |
| **Market Cap / FDV Ratio** | ~0.70 |

**Emissions, unlocks & burns.** UNI launched in Sept 2020 with a 1B 4-year distribution (60% community, 21.5% team, 17.8% investors, 0.7% advisors) and a perpetual 2%/yr inflation that begins after the initial schedule — a long-dated dilution vector. Counteracting it: the **100M UNI (~$600M) UNIfication burn (Dec 2025)** plus **ongoing fee-switch burns** linked to DEX volume, which have pushed total supply below the original schedule (893.8M total vs 1B max). Net issuance is now a tug-of-war between the 2% tail inflation and volume-driven burns — in active markets the burn can dominate, making UNI net-deflationary; in low-volume bear tapes burns shrink. MC/FDV ~0.70 reflects modest remaining non-circulating supply.

---

## Price History

> *Authoritative current figures are in the [[uniswap#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $44.92 (2021-05-03) — -93.31% |
| **All-Time Low** | $1.03 (2020-09-17) — +191.51% |
| **24h Change (2026-06-20)** | -1.79% |
| **7d Change (2026-06-20)** | +19.53% |

---

## Ecosystem & Use Cases

- **Reference DEX & price discovery** — Uniswap pools are the on-chain price reference for thousands of ERC-20s; many oracles and aggregators read from them.
- **Aggregator & intent flow** — 1inch, CowSwap, 0x and wallet routers route huge volume through Uniswap pools; Uniswap's own UniswapX is an intent/RFQ layer competing for that flow.
- **LP yield** — concentrated-liquidity LPing (v3/v4) is a core DeFi yield activity, now augmented by hook-based strategies and active-LP vaults (e.g. Arrakis, Gamma).
- **Composability** — v4 hooks let other protocols embed bespoke AMM logic (limit orders, dynamic fees, custom oracles), making Uniswap a base layer others build on.
- **Governance** — UNI holders govern the treasury, fee policy (UNIfication), grants, and Unichain strategy.
- **Multichain footprint** — deployed on Ethereum, Unichain, Arbitrum, Optimism, Polygon, BSC, Base, Avalanche and more (43 chains cumulatively).

---

## Market Structure & Derivatives

- **Spot venues**: deep books on Binance, Coinbase, Kraken, Upbit (KRW), Bitget, KuCoin; UNI/WETH and UNI/WBTC self-referential pools on Uniswap. ~$199M 24h volume (2026-06-20), high for a ~$1.9B-cap token — turnover ~10.7%, indicating active two-way flow during the 7-day rally.
- **Perpetuals & funding**: UNI-PERP on [[hyperliquid|Hyperliquid]], Binance, Bybit, OKX. With a sharp 7-day rally into an extreme-fear market, funding likely turned positive (longs paying) — watch for crowded-long squeeze risk if the move stalls.
- **OI & basis**: rising OI alongside the rally is the bullish confirmation; OI rising on declining price would flag a short build. Cash-and-carry desks fade extreme funding.
- **Self-listing dynamic**: Uniswap is both a traded asset and the venue — DEX volume on Uniswap directly drives the burn that re-rates UNI, a reflexive feedback loop unique among major tokens.

---

## Valuation Framework

Post-UNIfication, UNI is one of the few large tokens with a clean cash-flow handle:

- **Burn yield = f(DEX volume × in-scope fee × protocol split)** — annualized UNI burned ÷ market cap gives a "buyback yield." This is the headline fundamental; it scales mechanically with Uniswap volume (mainnet + Unichain).
- **Protocol revenue / fees** — track total LP fees and the protocol share on Token Terminal / Dune; compare fee capture to market cap (a P/F multiple).
- **TVL & volume share** — Uniswap's DEX market share vs rivals; declining TVL/volume directly shrinks burns.
- **Net supply change** — burns minus the 2% tail inflation; net-deflationary in active markets is the bull case.
- **MC/FDV ~0.70** — limited remaining dilution beyond tail inflation.

The key shift: volume downturns now hit the token **mechanically** (fewer burns), not just narratively. Model UNI off forward Uniswap volume assumptions, haircut for LP attrition risk from the fee split.

---

## Trading Playbook

- **Real-yield / fee-switch basket** — UNI is the anchor of the "DeFi fee-switch / buyback" basket with [[aave|AAVE]], [[sky|SKY]] and LDO; rotate the basket on fee-switch/burn catalysts. See [[narrative-trading]].
- **Burn-rate momentum** — long when Uniswap volume (and thus burn rate) is inflecting up; the 2026-06-20 +19.5% week is an example of burn-narrative flows decoupling UNI from a bleeding market.
- **Volume-decay short** — conversely, fade UNI into volume droughts: burns shrink and the deflation thesis weakens.
- **Catalyst calendar** — burn-rate reports, v4 hook adoption metrics, Unichain volume migration, fee-switch expansion to more pools/chains, regulatory clarity for DEX front-ends.
- **Pairs** — UNI vs AAVE (both fee-switch tokens) to isolate DEX-vs-lending; UNI vs a Solana-DEX token to trade chain-share rotation.
- **Risk in extreme fear** — a +19.5% week into a Fear & Greed of 22 is fragile; size for mean-reversion and watch perp funding for crowded longs.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x1f9840a85d5af5bf1d1762f925bdaddc4201f984` |
| Unichain | `0x8f187aa05619a017077f5308904739877ce9ea21` |
| Polygon PoS | `0xb33eaad8d922b1083446dc23f610c2567fb5180f` |
| Binance Smart Chain | `0xbf5140a22578168fd562dccf235e5d43a02ce9b1` |
| Arbitrum One | `0xfa7f8980b0f1e64a2062791cc3b0871572f1f7f0` |
| Optimistic Ethereum | `0x6fd9d7ad17242c41f7131d257212c54a0e816691` |
| Avalanche | `0x8ebaf22b6f053dffeaf46f4dd9efa95d89ba8580` |
| Xdai | `0x4537e328bf7e4efa29d05caea260d7fe26af9d74` |
| Near Protocol | `1f9840a85d5af5bf1d1762f925bdaddc4201f984.factory.bridge.near` |
| Harmony Shard 0 | `0x90d81749da8867962c760414c1c25ec926e889b6` |
| Huobi Token | `0x22c54ce8321a4015740ee1109d9cbc25815c46e6` |
| Energi | `0x665b3a802979ec24e076c80025bff33c18eb6007` |
| Sora | `0x009be848df92a400da2f217256c88d1a9b1a0304f9b3e90991a67418e1d3b08c` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | UNI/USDT |
| Kraken | UNI/USD |
| Upbit | UNI/KRW |
| Bitget | UNI/USDT |
| KuCoin | UNI/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | UNI-PERP | Perpetual |
| Uniswap V3 (Ethereum) | UNI/WBTC | Spot |
| Uniswap V2 (Ethereum) | UNI/WETH | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://uniswap.org/](https://uniswap.org/) |
| **Twitter** | [@Uniswap](https://twitter.com/Uniswap) |
| **Reddit** | [r/Uniswap](https://www.reddit.com/r/Uniswap) |
| **Discord** | [https://discord.gg/FCfyBSbCU5](https://discord.gg/FCfyBSbCU5) |
| **GitHub** | [Uniswap/uniswap-v3-core](https://github.com/Uniswap/uniswap-v3-core) |
| **Governance** | [vote.uniswapfoundation.org — UNIfication proposal #93](https://vote.uniswapfoundation.org/proposals/93) |

---

## Developer Activity

*(snapshot 2026-04-09)*

| Metric | Value |
|---|---|
| **GitHub Stars** | 4,976 |
| **GitHub Forks** | 3,015 |
| **Pull Requests Merged** | 214 |
| **Contributors** | 11 |

---

## History

| Date | Event |
|---|---|
| 2018-11 | Uniswap v1 launches (Hayden Adams), ETH↔ERC-20 AMM |
| 2020-05 | v2 launches (any ERC-20 pair, price oracles, flash swaps) |
| 2020-09 | UNI token + retroactive airdrop (400 UNI to past users); ATL $1.03 |
| 2021-05 | v3 concentrated liquidity; UNI all-time high $44.92 |
| 2023–2024 | Multichain expansion; SEC Wells notice to Uniswap Labs (later dropped) |
| 2025-01 | **v4** (singleton + hooks) goes live |
| 2025-02 | **Unichain** L2 mainnet |
| 2025-11-10 | **UNIfication** proposed (fee switch + 100M burn) |
| 2025-12-25 | UNIfication passes 99.9%; fee switch activated, 100M UNI burned |
| 2026-06-20 | UNI $2.99, #45; +19.5% on the week vs an extreme-fear market |

---

## Competitive Positioning

| Venue | Model | Edge vs Uniswap | Uniswap's Edge |
|---|---|---|---|
| [[hyperliquid\|Hyperliquid]] | On-chain perp DEX (order book) | Dominant in perps; in-house chain captures all flow | Spot/AMM dominance; deepest long-tail liquidity; v4 hooks |
| Curve ([[curve-finance]]) | Stableswap AMM | Best stablecoin/pegged-asset swaps; veCRV emissions | General-purpose; far broader asset coverage; fee burn |
| PancakeSwap | BSC-first AMM | Cheap fees, large BSC retail base | Ethereum/L2 blue-chip status; institutional trust; v4 tech |
| Aerodrome | Base-native AMM (ve(3,3)) | Dominant on Base; emissions flywheel | Cross-chain reach; brand; cumulative $4T volume |
| Solana DEXes (Raydium, Orca, Jupiter) | Solana AMMs/aggregator | Speed, low fees, memecoin flow | Ethereum-ecosystem depth; fee-switch value accrual |
| 1inch / CowSwap (aggregators) | Route across DEXes | Best execution by sourcing many pools | Uniswap is usually their largest liquidity source; UniswapX competes back |

Uniswap's moat: **brand, liquidity depth, and developer mindshare**, now reinforced by the fee-switch value-accrual loop and v4's hook ecosystem. The chief threats are perp-DEX disintermediation ([[hyperliquid]]), chain-share loss to Solana, and LP attrition if the protocol fee split pushes LPs to zero-protocol-fee rivals.

---

## Risks

- **LP exodus** — the protocol fee comes out of the LP take; if LPs migrate to rival venues with no protocol fee, liquidity (and thus volume and burns) could erode — a reflexive downside loop.
- **Volume dependence** — UNI's value now scales with DEX volume; a prolonged low-volume bear shrinks burns and the deflation thesis (acute risk in the current Fear & Greed = 22 tape).
- **Competition** — perp DEXes ([[hyperliquid]]), Solana DEXes, and Base-native AMMs compete for the same flow; aggregators/intent systems can disintermediate the front-end.
- **Regulatory** — DEX front-ends and the fee switch invite securities/MTL scrutiny; the SEC dropped its Uniswap Labs probe in early 2025 but the regulatory perimeter for DeFi remains unsettled.
- **Smart-contract / hook risk** — v4 hooks are powerful but expand the attack surface; malicious or buggy hooks could harm specific pools (Uniswap mitigates with hook permissions, but composability cuts both ways).
- **Tail inflation** — the 2%/yr UNI emission resumes long-term; in low-burn regimes net supply rises.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-exchange]] / [[decentralized-exchanges]] / [[automated-market-maker]]
- [[hyperliquid]] — perp competitor and UNI perp venue
- [[curve-finance]] — fellow AMM (stableswap niche)
- [[sky]], [[aave]] — fellow fee-switch / buyback DeFi basket
- [[chainlink]] — oracle integrable via v4 hooks
- [[impermanent-loss]] — core LP risk in concentrated liquidity
- [[layer-2]] — Unichain context
- [[narrative-trading]] — real-yield basket

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- The Block, "Uniswap governance passes major 'UNIfication' proposal; 100 million token burn imminent" (Dec 2025) — https://www.theblock.co/post/383742/uniswap-passes-unification-proposal
- CoinDesk, "Uniswap proposes sweeping 'UNIfication' with UNI burn and protocol fee overhaul" (2025-11-10) — https://www.coindesk.com/tech/2025/11/10/uniswap-proposes-sweeping-unification-with-uni-burn-and-protocol-fee-overhaul
- CoinDesk, "Uniswap's token burn, protocol fee proposal backed overwhelmingly by voters" (2025-12-26) — https://www.coindesk.com/business/2025/12/26/uniswap-s-token-burn-protocol-fee-proposal-backed-overwhelmingly-by-voters
- DLNews, "Uniswap DAO to activate fee switch, burn almost $600m UNI" — https://www.dlnews.com/articles/defi/uniswap-dao-to-activate-fee-switch-and-burn-100m-uni-tokens/
- Uniswap Agora governance, UNIfication proposal — https://vote.uniswapfoundation.org/proposals/93
- CoinGecko top-1000 snapshot (2026-04-09), original auto-generated data
- Verified via Perplexity sonar + web search, 2026-06-10
