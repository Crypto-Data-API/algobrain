---
title: "HYPE (Hyperliquid Token)"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, exchange, leverage, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, altcoins]
entity_type: protocol
aliases: ["HYPE", "HYPE-token", "hype-token"]
website: "https://hyperliquid.xyz"
related: ["[[crypto-markets]]", "[[decentralized-exchanges]]", "[[hip-3-builder-deployed-perps]]", "[[hlp]]", "[[hyperbft]]", "[[hypercore]]", "[[hyperliquid-fee-tiers-and-maker-rebates]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
headquarters: "Decentralized"
---

# HYPE (Hyperliquid Token)

**HYPE** is the native token of [[hyperliquid|Hyperliquid]] (ticker **HYPE**, native [[hypercore|HyperCore]] / [[hyperevm|HyperEVM]] chain), the leading decentralized [[perpetual-futures|perpetual futures]] exchange by volume. HYPE serves as the gas, staking and governance token for the Hyperliquid L1, securing the [[hyperbft|HyperBFT]] consensus and aligning incentives between validators, traders, and the protocol. Its defining feature is a **fee-revenue → buyback** flywheel: the [[assistance-fund|Assistance Fund]] uses the bulk of protocol fees to buy HYPE on the open market, making the token a direct claim on exchange cash flows rather than a pure governance asset.

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | HYPE |
| **Market Cap Rank** | #10 |
| **Price** | $70.43 |
| **Market Cap** | $15.67B |
| **24h Volume** | $788.1M |
| **24h Change** | +4.45% |
| **7d Change** | +19.88% |
| **Circulating Supply** | 222.45M HYPE |
| **Total Supply** | 955.31M HYPE |
| **Max Supply** | 1.00B HYPE |
| **Fully Diluted Valuation (FDV)** | ~$70.4B (on max supply) |
| **Market Cap / FDV** | ~0.22 |
| **All-Time High** | $76.70 |
| **All-Time Low** | $3.81 (2024-11-29) |

At **$70.43** HYPE ranks **#10** by market cap (~$15.67B), having rallied **+19.9% on the week** to trade just below its $76.70 all-time high — a notable show of relative strength against a risk-off backdrop where the crypto [[fear-and-greed-index|Fear & Greed Index]] read **23 (extreme fear)** in an **"Established Bear Market"** regime. The token is up roughly **18x** from its $3.81 airdrop-era low. The bullish divergence from broad market sentiment reflects HYPE's structural buyback bid (see below) and continued Hyperliquid volume dominance.

---

## Key Features

| Feature | Detail |
|---|---|
| **Network** | Hyperliquid L1 (custom consensus) |
| **Functions** | Staking, governance, gas fees on HyperEVM |
| **Launch** | Airdrop in late 2024 to early platform users |
| **Notable** | One of the largest token airdrops in crypto history by value |
| **Staking** | Delegated staking to Hyperliquid validators |

---

## Token Economics: Fee Revenue → Buyback Flywheel

HYPE's economics are the core of the bull case and distinguish it from most governance tokens:

- **Fee → buyback engine.** Hyperliquid directs **over 90% of protocol trading fees** to the [[assistance-fund|Assistance Fund]], which uses them to buy HYPE on the open market. This converts exchange revenue into persistent, mechanical buy-side demand — Hyperliquid has reportedly accounted for a large share of all crypto buyback activity in 2026. Holders effectively own a claim on exchange cash flows, valued more like an equity than a utility token.
- **Staking & security.** HYPE is staked to validators to secure the [[hyperbft|HyperBFT]] consensus that orders trades on [[hypercore|HyperCore]]; stakers earn rewards and reduce effective float. Higher staking rates lower circulating sell pressure.
- **Gas & collateral.** HYPE is the gas asset on [[hyperevm|HyperEVM]] and is increasingly used as collateral and the unit of account across the ecosystem; demand scales with on-chain activity and with [[hip-3-builder-deployed-perps|HIP-3 builder-deployed perps]] that let third parties launch markets.
- **HLP linkage.** The [[hlp|Hyperliquid Provider (HLP) vault]] is the protocol's community market-making/liquidation backstop. HLP performance, the Assistance Fund, and HYPE buybacks together form the value-accrual and risk-absorption layer of the ecosystem (see the JELLY incident below for the tail-risk side of this design).
- **Airdrop origin.** HYPE was distributed primarily through a late-2024 community airdrop to early traders and liquidity providers — one of the largest by value in crypto history — which seeded a wide, engaged holder base.

### Tokenomics (refreshed 2026-06-20)

| Metric | Value |
|---|---|
| **Circulating Supply** | 222.45M HYPE |
| **Total Supply** | 955.31M HYPE |
| **Max Supply** | 1.00B HYPE |
| **Fully Diluted Valuation** | ~$70.4B |
| **Market Cap / FDV Ratio** | ~0.22 |

**Dilution flag:** only ~22% of max supply circulates. Future emissions to team, investors and ecosystem reserves are a recurring overhang — a scheduled **~$700M monthly unlock on 6 June 2026** added sell pressure and contributed to the pullback from the June ATH. The buyback flywheel must outpace unlock-driven supply for price to compound.

---

## Trading Relevance

- HYPE is the primary proxy trade for growth of the Hyperliquid exchange and the broader decentralized perps sector
- Hyperliquid's trading volume and [[open-interest]] growth directly drive the fee-revenue buyback bid, and thus HYPE's fundamental valuation
- HYPE staking dynamics affect circulating supply -- higher staking rates reduce sell pressure
- As Hyperliquid's [[hyperevm|HyperEVM]] ecosystem expands (DeFi protocols deploying on the chain) and [[hip-3-builder-deployed-perps|HIP-3]] markets multiply, demand for HYPE as gas and collateral grows
- HYPE competes with DYDX ([[dydx]]), GMX and Vertex as the leading decentralized derivatives exchange tokens, and screens against [[exchange-tokens|CEX tokens]] like [[binance-coin|BNB]], OKB and [[whitebit|WBT]] as a "claim on an exchange" trade

---

## Market Structure & Derivatives

- **HYPE spot:** trades on Kraken (HYPE/USD), Bitget, KuCoin and other tier-1 CEXs, plus on Hyperliquid's own spot order book. With **$788M 24h volume** (2026-06-20) HYPE is among the more liquid altcoins, an order of magnitude deeper than the small-cap exchange tokens it is sometimes grouped with.
- **HYPE perps:** Hyperliquid itself runs a deep HYPE-PERP order book with on-chain [[funding-rate|funding]] and [[open-interest|open interest]]; HYPE perps are also listed across major CEX derivatives venues. Watch funding/OI for crowding around unlock dates and ETF flows.
- **Regulated wrappers:** US spot HYPE ETFs went live in May 2026 (21Shares 13 May; Bitwise's **BHYP** on NYSE 15 May, with built-in staking), opening institutional access (see news section).
- **Fee tiers:** trading economics for active users are set by [[hyperliquid-fee-tiers-and-maker-rebates|Hyperliquid's fee tiers and maker rebates]], which feed the fee-revenue base that backs the buyback.

---

## Narrative & Category

HYPE sits at the intersection of three of the strongest 2025–2026 crypto narratives: **decentralized perps / on-chain derivatives** (the category Hyperliquid leads by volume), **"real-yield" / revenue-backed tokens** (the buyback flywheel makes HYPE a cash-flow asset), and **high-performance L1s** (HyperCore + HyperEVM). This positioning is why HYPE has held up far better than most altcoins in the current bear regime — it offers a fundamentals story (exchange revenue, buybacks, ETF access) that pure-beta tokens lack.

## Valuation Framing

HYPE is best framed as **equity in a fast-growing exchange** rather than a utility token. The key qualitative anchors:

- **Buyback yield vs dilution.** Net value accrual depends on whether fee-funded buybacks exceed unlock-driven supply growth. With ~78% of max supply still locked, unlock cadence is the dominant near-term swing factor.
- **Revenue multiple.** At a ~$15.7B cap (FDV ~$70B), the market prices Hyperliquid as one of crypto's most valuable protocols; the implied multiple on annualized fee revenue is the central debate. Bulls cite buyback intensity and ETF demand; bears cite the FDV overhang and competition.
- **MC/FDV ~0.22** signals significant locked supply — the headline market cap understates the eventual fully diluted claim.

## Peer Comparison

| Token | Ticker | Type | Rank | Price | Market Cap | MC/FDV |
|---|---|---|---|---|---|---|
| **Hyperliquid** | HYPE | Perp DEX / L1 | #10 | $70.43 | $15.67B | ~0.22 |
| [[dydx]] | DYDX | Perp DEX | — | — | — | — |
| [[whitebit\|WhiteBIT Coin]] | WBT | CEX token | #17 | $52.35 | $6.19B | ~0.30 |
| [[binance-coin\|BNB]] | BNB | CEX token / L1 | — | — | — | — |
| [[mx-token\|MX]] | MX | CEX token | #196 | $1.75 | $0.16B | ~0.22 |

*HYPE is the only decentralized-exchange token in this peer set with both top-10 liquidity and a mechanical fee→buyback bid; CEX peers rely on discretionary burn/buyback programs.*

---

## Trading Profile

**Venues & liquidity.** HYPE is a deep, liquid two-venue market: it trades on **Binance** (spot plus a USD-margined perpetual) and on **Hyperliquid** itself (**HYPE-PERP**, up to ~40-50x leverage), alongside other tier-1 CEXs and Hyperliquid's own spot book. The presence of a top-tier CEX perp *and* the native on-chain perp means order-book depth is split across a centralized venue and the protocol's own HyperCore book, so large size can be worked across both without exhausting a single book. This dual availability tightens spreads and reduces slippage for size, but it also opens a structural CEX-vs-Hyperliquid basis and funding channel that traders can arbitrage. Practical implication: size and route execution with an eye to which venue holds depth at a given moment, and use the on-chain book's transparent [[funding-rate|funding]] and [[open-interest|OI]] as a real-time read on positioning.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — HYPE prints deep perps on *both* Binance and its native Hyperliquid book, so funding can dislocate meaningfully between the two venues, a clean divergence trade.
- [[cash-and-carry]] — with liquid spot (Binance/CEX) and a USD-margined perp, long spot / short perp captures HYPE's often-positive funding as carry.
- [[funding-rate-harvest]] — persistent positive funding around bullish HYPE narratives (buybacks, ETF flows) lets a delta-hedged book harvest the funding stream.
- [[token-unlock-supply-event]] — HYPE's ~$700M monthly cliff unlocks with only ~22% of max supply circulating make scheduled unlock dates tradable supply events.
- [[oi-confirmed-trend]] — Hyperliquid's transparent HYPE-PERP open interest lets traders confirm whether trend legs are backed by fresh positioning or short-covering.
- [[liquidation-cascade-fade]] — leverage up to ~40-50x plus crowded positioning around unlocks makes HYPE prone to sharp liquidation flushes that mean-revert, offering fade setups.

**Volatility & regime character.** HYPE is a **high-beta large-cap alt** and an **infra / DeFi exchange token** — effectively equity-like exposure to a fast-growing perp DEX rather than pure memecoin reflexivity. It carries elevated realized volatility but has shown *relative* strength versus the broad alt complex thanks to its mechanical fee→buyback bid, so it can decouple from BTC/ETH beta during buyback-driven or narrative-driven moves while still selling off with the market in broad risk-off regimes. Treat it as high-beta to BTC/ETH with an idiosyncratic buyback/unlock overlay that can dominate short-term direction.

**Risk flags.**
- **Venue & governance concentration** — Hyperliquid's small, team-influenced validator set (see the JELLY incident) means the native venue carries counterparty/governance risk atypical of a CEX perp; force-settlement precedent is a tail risk for on-chain positions.
- **Token unlocks / emissions** — only ~22% of max supply circulates; recurring large monthly unlocks are a persistent supply overhang that must be traded around.
- **Narrative dependence** — much of HYPE's premium rests on the buyback flywheel and ETF-access story; if fee revenue or buyback intensity fades, the fundamental bid weakens.
- **Perp funding dislocations** — the two-venue structure can produce sharp funding gaps and basis moves, especially into unlock dates and ETF-flow events, that can whipsaw leveraged carry books.
- **Regulatory** — as a KYC-light leveraged perp venue, Hyperliquid faces jurisdictional regulatory risk that could affect access and liquidity.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=HYPE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=HYPE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=HYPE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=HYPE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=HYPE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## See Also

- [[hyperliquid]] -- The exchange and L1 chain HYPE powers
- [[hypercore]] -- The on-chain central limit order book / matching engine
- [[hyperbft]] -- The consensus HYPE stakers secure
- [[hlp]] -- The community market-making / liquidation vault
- [[hip-3-builder-deployed-perps]] -- Permissionless market creation that drives HYPE demand
- [[hyperliquid-fee-tiers-and-maker-rebates]] -- Fee economics feeding the buyback
- [[decentralized-exchanges]] -- The DEX landscape HYPE operates within
- [[perpetual-futures]] -- The primary instruments traded on Hyperliquid
- [[crypto-markets]] -- Broader market context

## Overview

Hyperliquid is a layer one (L1) blockchain best known for perpetual futures and spot trading. Beyond its flagship DEX trading platform, the ecosystem supports borrowing, lending, real world assets (RWAs), and a full-fledged Ethereum Virtual Machine ([[hyperevm|HyperEVM]]), making it a leading force in decentralized finance (defi).

Just as electronic trading dramatically improved markets in the 2000s, Hyperliquid offers an opportunity for a massive technical upgrade of the existing financial system through a transparent, efficient, and resilient blockchain. HYPE is the native token of the Hyperliquid blockchain, with a maximum supply of 1 billion. (See the authoritative market-data block at the top of this page for current figures; the all-time high stands at **$76.70** with the all-time low at **$3.81**, 2024-11-29.)

---

## Platform & Chain Information

**Native Chain:** Hyperliquid

### Contract Addresses

| Chain | Address |
|---|---|
| Hyperliquid | `0x0d01dc56dcaaca66ad901c959b4011ec` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | HYPE/USD | N/A |
| Bitget | HYPE/USDT | N/A |
| KuCoin | HYPE/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | HYPE-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.hyperliquid.xyz/trade](https://app.hyperliquid.xyz/trade) |
| **Twitter** | [@HyperliquidX](https://twitter.com/HyperliquidX) |
| **Telegram** | [hyperliquid_announcements](https://t.me/hyperliquid_announcements) (43,124 members) |
| **Whitepaper** | [https://hyperliquid.gitbook.io/hyperliquid-docs](https://hyperliquid.gitbook.io/hyperliquid-docs) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

### The JELLY Exploit (March 2025)

In March 2025, Hyperliquid faced its most serious crisis when a trader manipulated the JELLY (Jelly-my-Jelly memecoin) perpetual futures market. The attacker opened a large short position, then used a separate account to pump JELLY's spot price, forcing the Hyperliquid Vault (HLP) — the protocol's market-making pool — to absorb the short at a massive loss as the position was liquidated.

Key details:
- The HLP vault lost an estimated $10-12M in the incident
- Hyperliquid's response was controversial: the validators voted to delist the JELLY market and force-settle all positions at a price that minimized vault losses — effectively socializing losses and overriding the market
- Critics compared this to centralized exchange behavior (similar to how [[ftx-collapse|FTX]] and other CeFi platforms have unilaterally intervened in markets)
- The incident raised fundamental questions about whether Hyperliquid's validator set is genuinely decentralized or effectively controlled by the team

### Validator Centralization Concerns

As of early 2026, Hyperliquid's validator set remains small and concentrated. Critics argue that:
- The team runs or controls a majority of validator stake
- The JELLY delisting demonstrated that validators can coordinate to override market outcomes
- This creates counterparty risk more similar to a centralized exchange than a truly permissionless protocol

Supporters counter that Hyperliquid's performance (sub-second finality, deep liquidity) requires a smaller validator set, and that the JELLY intervention protected users from market manipulation.

### USDH Native Stablecoin (September 2025)

In September 2025, Hyperliquid validators approved **Native Markets** to launch **USDH**, a fully-backed stablecoin tied to US Treasuries with reserve yield flowing back to the protocol (estimated ~$110M/year that previously accrued to Circle/USDC). USDH, however, split platform liquidity between two stablecoins. By 2026 the program was being wound down: **Coinbase acquired the USDH brand assets**, and USDH is being phased out, with users able to redeem USDH for USDC (zero fee) or fiat during the transition (Source: external; Verified via web search, 2026-06-11).

### Spot HYPE ETFs Launch (May 2026)

US spot HYPE ETFs went live in **May 2026**:
- **21Shares** launched the first US spot HYPE ETF on **13 May 2026** (fee ~0.30%).
- **Bitwise** debuted **BHYP** on the NYSE on **15 May 2026** (fee ~0.34%), featuring built-in staking and 100% HYPE exposure.

The ETFs mark HYPE's entry into regulated US wrappers and a meaningful expansion of institutional access. Coinbase has also acted as a treasury deployer for ETF-related flows (Source: external; Verified via web search, 2026-06-11).

### 2025-2026 Update (as of June 2026)

- **Price/market cap:** After hitting a record **~$75.51 on 1-2 June 2026** and a brief ~20% pullback around the early-June unlock, HYPE had recovered to **$70.43** by 2026-06-20 (+19.9% on the week), market cap **~$15.67B**, rank **#10** — just below its $76.70 all-time high (Source: external; CoinGecko snapshot 2026-06-20).
- **Buybacks:** Hyperliquid continues to direct **over 90% of protocol fees to HYPE buybacks** via the [[assistance-fund|Assistance Fund]], reportedly accounting for a large share of all crypto buyback activity in 2026 — a key structural demand driver distinct from most governance tokens.
- **Token unlocks:** A scheduled **~$700M monthly unlock on 6 June 2026** added sell pressure. Unlock cadence remains a recurring overhang against the buyback bid.

## Risk Factors

- **Validator centralization**: small validator set with team-controlled majority creates single-point-of-failure risk
- **Regulatory**: as a perp DEX facilitating leveraged trading without KYC, Hyperliquid faces regulatory risk in multiple jurisdictions
- **Token unlock**: only ~24% of total supply is circulating — future unlocks (team, ecosystem) could create significant sell pressure
- **Competition**: [[dydx]], GMX, Vertex, and new perp DEXs compete for the same market. Hyperliquid's lead is based on execution speed and liquidity, both of which can be replicated
- **Smart contract risk**: as an L1 running a novel consensus mechanism, undiscovered bugs could lead to loss of funds
- **FDV vs. market cap**: with a market cap / FDV ratio of ~0.25, the implied fully diluted valuation (~$37B) prices Hyperliquid as one of the most valuable protocols in crypto. This valuation assumes significant future growth

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- [CoinGecko — Hyperliquid](https://www.coingecko.com/en/coins/hyperliquid)
- [Bitwise — Bitwise Launches Spot Hyperliquid ETF (BHYP)](https://bitwiseinvestments.com/newsroom/bitwise-launches-spot-hyperliquid-etf-bhyp)
- [AMBCrypto — Bitwise joins 21Shares in race for Spot HYPE ETF](https://ambcrypto.com/hyperliquid-bitwise-joins-21shares-in-race-for-spot-hype-etf-dominance/)
- [crypto.news — The real Hyperliquid story isn't the ETF (USDH/buybacks)](https://crypto.news/the-real-hyperliquid-story-isnt-the-etf/)
- Verified via web search, 2026-06-11

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HYPE |
| **Market Cap Rank** | #10 |
| **Market Cap** | $14.62B |
| **Current Price** | $65.74 |
| **Categories** | Decentralized Exchange (DEX), Smart Contract Platform, Exchange-based Tokens, Decentralized Finance (DeFi), Derivatives, Perpetuals, Layer 1 (L1), Proof of Stake (PoS) (+1 more) |
| **Website** | [https://app.hyperliquid.xyz/trade](https://app.hyperliquid.xyz/trade) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 222.45M HYPE |
| **Total Supply** | 955.31M HYPE |
| **Max Supply** | 1.00B HYPE |
| **Fully Diluted Valuation** | $62.81B |
| **Market Cap / FDV Ratio** | 0.23 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $76.70 (2026-06-16) |
| **Current vs ATH** | -14.29% |
| **All-Time Low** | $3.81 (2024-11-29) |
| **Current vs ATL** | +1626.13% |
| **24h Change** | -3.17% |
| **7d Change** | -3.30% |
| **30d Change** | -10.34% |
| **1y Change** | +36.66% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $431.36M |
| **Market Cap Rank** | #10 |
| **24h Range** | $65.66 — $68.82 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-07-16 |

---
