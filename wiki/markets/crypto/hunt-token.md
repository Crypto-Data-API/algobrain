---
title: "Hunt"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi, nft]
aliases: ["HUNT", "Hunt Token", "Mint Club"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://hunt.town"
related: ["[[base]]", "[[bonding-curve]]", "[[crypto-markets]]", "[[ethereum]]", "[[nft]]"]
---

# Hunt

**Hunt** (HUNT) is the native token of the **Hunt.town** ecosystem, which is best known for **Mint Club** — a no-code platform that lets anyone create tokens and [[nft|NFTs]] backed by an automated [[bonding-curve|bonding curve]]. On Mint Club, every created asset is priced and instantly liquid via a deterministic bonding-curve formula, with HUNT (or another reserve token) acting as the backing/reserve asset. HUNT originated in 2020 as the token of *Steemhunt* (a product-discovery community) and later migrated to the Ethereum/Base-based Hunt.town and Mint Club ecosystem, where it now serves governance and reserve functions.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* HUNT trades at **$0.07949**, ranked **#932** by market cap (~**$15.83M**), down **0.30%** over 24h and down **3.29%** over 7 days, amid broad Extreme Fear (Fear & Greed 21; BTC ~$64,508).

---

## What Hunt / Mint Club does

**Mint Club** is the flagship product of the Hunt.town ecosystem. It is a permissionless launchpad where users mint fungible tokens or NFTs whose price is governed by a [[bonding-curve|bonding curve]] rather than by listing on an external exchange or seeding a liquidity pool. Key properties:

- **Instant liquidity** — buying mints new supply along the curve and selling burns it, so an asset is always tradeable against its reserve without needing an order book or AMM pool.
- **No-code creation** — creators configure the curve (reserve token, slope, supply cap) without writing smart-contract code.
- **Reserve-backed value** — each minted asset is collateralized by deposited reserve tokens, giving it a programmatic, math-defined floor logic.

This makes Mint Club a tooling/infrastructure play in the broader "tokenize anything" and creator-economy space, adjacent to [[defi|DeFi]] primitives and on-chain [[nft|NFT]] issuance. It operates across [[ethereum|Ethereum]] and [[base|Base]].

### How the bonding curve works

A [[bonding-curve|bonding curve]] is a smart contract that defines a deterministic relationship between a token's **supply** and its **price**: as more of the asset is minted, the price moves along the curve (typically upward); as it is burned (sold back), the price moves down. Crucially, the contract itself is the counterparty — there is no order book and no need to bootstrap an AMM liquidity pool. On Mint Club:

1. A creator deploys an asset by choosing a **reserve token** (HUNT or another approved token), a **curve shape/slope**, and a supply cap.
2. **Buying** deposits reserve tokens into the contract, mints new supply, and pushes the price up the curve.
3. **Selling** burns supply and returns reserve tokens from the contract, pushing the price down.
4. Because every asset is fully **reserve-backed**, it always has a programmatic, math-defined exit value — liquidity is guaranteed *by construction*, not by external market makers.

This is the same primitive that later powered memecoin launchpads like Pump.fun; Mint Club's distinction is generalizing it to **both fungible tokens and NFTs**, across multiple reserve assets, with a no-code interface — and using **HUNT as a canonical reserve asset**, which is the core source of structural demand for the token.

### Hunt.town and the broader ecosystem

Beyond Mint Club, the **Hunt.town** community layer hosts products and incentive flows (e.g., community "buildings"/Guild-style mechanics and a daily-mining/burn dynamic in various iterations) that route activity and, in some designs, **burn** HUNT — reinforcing the fixed-supply, deflationary-leaning thesis. The token's utility is therefore tied directly to *how much creation and trading happens on Mint Club*, making HUNT a fairly pure bet on launchpad/creator-economy throughput.

---

## Token role

HUNT serves several functions in the ecosystem:

- **Reserve asset** — HUNT is one of the canonical backing/reserve tokens used to collateralize bonding-curve assets created on Mint Club.
- **Governance** — holders participate in ecosystem governance (the Hunt token is categorized as a governance token).
- **Community / utility** — used within Hunt.town community products and incentive flows.

Supply is fixed (no inflation): circulating supply equals total and max supply (~198.9M HUNT), and market cap effectively equals FDV (MC/FDV ≈ 1.00), so there is no overhang of future unlocks diluting holders — a notable structural positive relative to many small-caps.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HUNT |
| **Market Cap Rank** | #932 |
| **Market Cap** | $15,829,679 |
| **Current Price** | $0.07949 |
| **24h Change** | -0.30% |
| **7d Change** | -3.29% |
| **Categories** | NFT, Ethereum Ecosystem, Base Ecosystem, Governance, Base Native, Bonding Curve |
| **Website** | [https://hunt.town](https://hunt.town) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Tokenomics/price-history figures below carry an earlier 2026-04-09 CoinGecko snapshot and are retained for historical context. Note: some aggregators tag HUNT as "GameFi" from its Steemhunt origins; its current core product is the Mint Club bonding-curve platform.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 198.91M HUNT |
| **Total Supply** | 198.91M HUNT |
| **Max Supply** | 198.91M HUNT |
| **Fully Diluted Valuation** | $19.82M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.46 (2021-11-28) |
| **Current vs ATH** | -93.18% |
| **All-Time Low** | $0.00039817 (2020-04-25) |
| **Current vs ATL** | +24938.10% |
| **24h Change** | -0.27% |
| **7d Change** | +2.78% |
| **30d Change** | +3.72% |
| **1y Change** | -55.91% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x9aab071b4129b083b01cb5a0cb513ce7eca26fa5` |
| Base | `0x37f0c2915cecc7e977183b8543fc0864d03e064c` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | HUNT/KRW | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X9AAB071B4129B083B01CB5A0CB513CE7ECA26FA5/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hunt.town](https://hunt.town) |
| **Twitter** | [@steemhunt](https://twitter.com/steemhunt) |
| **Reddit** | [https://www.reddit.com/r/steemhunt](https://www.reddit.com/r/steemhunt) |
| **Discord** | [https://discord.gg/ZFnssyzvde](https://discord.gg/ZFnssyzvde) |
| **GitHub** | [https://github.com/Steemhunt](https://github.com/Steemhunt) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $354,592.00 |
| **Market Cap Rank** | #926 |
| **24h Range** | $0.0980 — $0.1036 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Competitive Position

Mint Club competes in the no-code token/NFT-launch and [[bonding-curve|bonding-curve]] tooling space alongside platforms such as friend.tech-style social-token launchers, Pump.fun (Solana memecoin bonding-curve launchpad), and various NFT mint platforms. Its differentiation is a generalized, reserve-backed bonding-curve primitive that works for both fungible tokens and NFTs across [[ethereum|Ethereum]] and [[base|Base]], with instant liquidity by construction. As a ~$16M-cap project it is small, and its fortunes are tied to creator/launchpad activity, which is highly cyclical with overall crypto risk appetite.

### Comparison vs Bonding-Curve / Launchpad Peers

| Platform | Token | Chain(s) | What it launches | Contrast with Mint Club / HUNT |
|---|---|---|---|---|
| **Mint Club (Hunt.town)** | HUNT | Ethereum + Base | Fungible tokens **and** NFTs, any reserve asset, no-code | Generalized reserve-backed curve; HUNT as reserve token |
| **Pump.fun** | PUMP | Solana | Memecoins via bonding curve, then graduate to AMM | Far larger volume; memecoin-only, SOL-reserve, "graduation" model |
| **friend.tech** | — | Base | Social "keys" priced on a bonding curve | Social-token specific; activity collapsed post-hype |
| **Zora** | ZORA | Base / Ethereum | NFT/creator mints | Creator-NFT focus, not generalized fungible-token curves |
| **Virtuals Protocol** | VIRTUAL | Base | AI-agent tokens via bonding curve | Same Base bonding-curve mechanic, AI-agent vertical |

Takeaway: the bonding-curve launchpad mechanic Mint Club helped popularize became a dominant 2024–2025 pattern, but the *volume* gravitated to Solana (Pump.fun) and to vertical-specific Base launchpads (Virtuals). HUNT's edge is generality and a fixed-supply reserve role; its challenge is that mindshare and flow rotate quickly between chains and verticals.

---

## How & Where HUNT Trades

- **Limited CEX, DEX-led.** The main centralized listing is **Upbit (HUNT/KRW)** — which gives HUNT notable **Korean-retail sensitivity** — while the deepest on-chain liquidity is **Uniswap V3 on [[ethereum]]** (plus liquidity on [[base|Base]]). It is not a broad Tier-1 listing.
- **Multichain.** Native on **Ethereum** and **Base**; on-chain liquidity is split across the two, with the Korean-won pair on Upbit driving much of the idiosyncratic flow.
- **No meaningful derivatives.** There is no significant perp/futures market, so risk is managed by size rather than hedging, and there is no funding-rate signal.
- **Trading implications** — A thin micro-cap (~$16M) whose Upbit KRW listing can produce sharp, market-independent moves on Korean retail flow. Spreads widen and slippage rises quickly on size; use limit orders.

---

## Narrative, Category & Catalysts

- **Category** — **Bonding-curve launchpad / creator-economy infrastructure**, tagged NFT, Governance, and Base-native. A "tokenize anything" tooling play.
- **Structural positive — fixed supply.** Unlike most small-caps, HUNT has **no inflation** (MC/FDV ≈ 1.00), so there is no unlock overhang; demand from Mint Club reserve usage and burns is the swing factor rather than dilution.
- **Catalysts** — A pickup in launchpad/creator activity (more assets minted with HUNT as reserve), new Mint Club / Hunt.town product launches, a broader return of memecoin/launchpad risk appetite, and any additional exchange listings that deepen liquidity.
- **Headwind — reflexivity & regime.** Bonding-curve activity is highly procyclical: in an Established Bear with Fear & Greed at **21**, new-token creation and speculation dry up, directly reducing demand for the reserve token. HUNT trades ~93% below its 2021 ATH.

---

## History & Timeline

Only dated, verifiable milestones are listed.

| Date | Event |
|---|---|
| 2020-04-25 | HUNT all-time low of **$0.00039817** (early Steemhunt era) |
| 2020 | HUNT originates as the token of **Steemhunt**, a product-discovery community |
| 2021-11-28 | HUNT all-time high of **$1.46** during the 2021 bull-market top |
| (later) | HUNT migrates to the Ethereum/Base-based **Hunt.town / Mint Club** ecosystem, taking on reserve + governance roles |
| 2026-06-22 | Trades ~$0.0795, ~93% below ATH, mildly lower in Extreme Fear (BTC ~$64,508; F&G 21) |

---

## Risks

- **Narrative / activity dependence** — HUNT's value is tied to launchpad and creator-economy activity. In Extreme Fear regimes (F&G 21), new-token creation and speculation dry up, pressuring demand for the reserve token.
- **Low liquidity** — modest 24h volume and a small cap mean wide spreads and meaningful slippage on size.
- **Bonding-curve reflexivity** — assets minted on the platform are only as liquid as their reserves; a rush of selling unwinds the curve and can cascade, an inherent property of [[bonding-curve|bonding-curve]] systems.
- **Competitive pressure** — no-code launch tooling is a crowded, fast-moving niche; mindshare can shift quickly to whichever chain/platform is in vogue.
- **Legacy-brand drift** — HUNT carries Steemhunt-era branding and aggregator tags (e.g., GameFi) that no longer reflect the product, which can create confusion about what the token actually backs.

> Small-cap utility/governance tokens are speculative. Nothing here is investment advice.

---

## Trading Playbook (Bear / Extreme-Fear Regime)

> Educational framing only — not investment advice. HUNT is a thin, procyclical launchpad micro-cap.

- **Regime first.** Bonding-curve/launchpad demand is intensely procyclical. In an Established Bear with Fear & Greed at 21, creation and speculation dry up, sapping the reserve-token demand that underpins HUNT — the base case is low activity and drift.
- **Fixed supply is the one structural tailwind.** With MC/FDV ≈ 1.00 there is no unlock overhang, so HUNT avoids the dilution trap that drags many peers. That makes it cleaner to hold *if* launchpad activity recovers — but it does not protect against a demand-side bear.
- **Trade the Korean bid.** The Upbit KRW listing means Korean retail can spike HUNT independently of the broader market; treat sudden Upbit volume as a mean-reversion signal more often than a trend start.
- **Liquidity discipline.** Thin DEX (Uniswap ETH / Base) plus one major CEX rail means wide spreads on size; use limit orders, size small, and pre-check pool depth.
- **Invalidation / risk control.** No derivatives to hedge — manage by size. The realistic long thesis is a launchpad/creator-economy risk-on rotation (the kind that drove Pump.fun/Virtuals volume) lifting Mint Club throughput; absent that, rallies into the bear are fades.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[base]]
- [[bonding-curve]]
- [[nft]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — earlier tokenomics/price-history snapshot
- Current market data (price, rank, market cap, 24h/7d) as of 2026-06-22 via cryptodataapi.com / CoinGecko.
- General market knowledge of the Hunt.town / Mint Club ecosystem, bonding-curve mechanics, and the Steemhunt origin; no specific in-depth wiki source on HUNT ingested yet.
