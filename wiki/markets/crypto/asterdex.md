---
title: "AsterDEX"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, dex, derivatives, perpetuals, algorithmic, api-trading]
aliases: ["ASTER", "Aster DEX", "AsterDEX", "Aster"]
entity_type: exchange
headquarters: "Decentralized"
website: "https://www.asterdex.com/en"
related: ["[[crypto-markets]]", "[[bnb]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[decentralized-exchanges]]", "[[decentralized-exchange]]", "[[dex]]", "[[defi]]", "[[funding-rate]]", "[[hyperliquid-vs-asterdex-vs-tiger-brokers]]"]
---

# AsterDEX

**AsterDEX** (ASTER) is a decentralized perpetual futures exchange formed from the merger of **APX Finance** and **Astherus** in March 2025, backed by YZi Labs (formerly Binance Labs) with public support from Binance founder Changpeng Zhao. It is the **second-largest perpetual DEX by volume** as of Q1 2026, with monthly trading volume of $77.77 billion (vs [[hyperliquid|Hyperliquid's]] $178.23B). AsterDEX grew explosively in Q4 2025, recording $259 billion in monthly volume for both October and November 2025, reshaping the sector from single-platform dominance to a multi-venue ecosystem.

AsterDEX distinguishes itself from Hyperliquid through **multi-chain deployment** (BNB Chain, Ethereum, Solana, Arbitrum), **hidden orders** for MEV protection, **up to 1001x leverage** in Simple Mode, and **24/7 US stock perpetuals** — settling on-chain in crypto without traditional financial infrastructure.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | ASTER |
| **Market Cap Rank** | #48 |
| **Market Cap** | ~$1.74B |
| **Current Price** | ~$0.6478 |
| **24h Volume** | ~$102.38M |
| **24h Change** | +4.59% |
| **7d Change** | +1.55% |
| **All-Time High** | $2.41 (2025-09-24) — current ~-73% |
| **All-Time Low** | $0.099713 (2025-09-17) — current ~+550% |
| **Circulating Supply** | 2.68B ASTER |
| **Total Supply** | 7.82B ASTER |
| **Max Supply** | 8.00B ASTER |
| **Categories** | Decentralized Exchange (DEX), Derivatives, Perpetuals, BNB Chain Ecosystem |
| **Website** | [asterdex.com](https://www.asterdex.com/en) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

ASTER outperformed the tape over the week to 2026-06-20 (+4.59% 24h, +1.55% 7d) even as the broad market sat in **extreme fear** (crypto [[fear-and-greed-index|Fear & Greed Index]] = **23**) within an **Established Bear Market**. Uniquely among the DEX tokens in this cluster, ASTER is a **top-50** asset by market cap (~$1.74B) — orders of magnitude larger than peers like [[sushi|SUSHI]] or [[mango-markets|MNGO]] — reflecting the explosive 2025 launch and CZ-adjacent backing. At ~$0.65 it trades ~73% below its September 2025 ATH ($2.41) but is up roughly 5.5x from its launch-week ATL ($0.0997).

---

## Key Facts

| Field | Detail |
|---|---|
| **Type** | Decentralized Perpetual Futures Exchange |
| **Chains** | BNB Chain, Ethereum, Solana, Arbitrum |
| **Founded** | March 2025 (merger of APX Finance + Astherus) |
| **Backing** | YZi Labs (formerly Binance Labs), CZ advisory |
| **Native Token** | ASTER |
| **Markets** | 100+ trading pairs (crypto perps, spot, US stock perps) |
| **KYC Required** | No |
| **Max Leverage** | 1001x (Simple Mode), standard (Pro Mode) |
| **Monthly Volume** | $77.77B (Q1 2026) |
| **Audits** | Halborn, PeckShield, Salus |
| **Website** | [asterdex.com](https://www.asterdex.com/en) |

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.68B ASTER (~33% of max) |
| **Total Supply** | 7.82B ASTER |
| **Max Supply** | 8.00B ASTER |
| **Fully Diluted Valuation** | ~$5.18B (price × max supply) |
| **Market Cap / FDV Ratio** | ~0.34 |

The ASTER token serves multiple functions: governance, staking rewards through liquidity provision, and earning incentives via the platform's points program. 53.5% of supply is reserved for airdrops/community with ongoing vesting. CZ personally invested over $2.5M in ASTER tokens.

**Dilution flag:** only ~33% of the 8.0B max supply circulates, so the market cap (~$1.74B) is roughly one-third of fully diluted value (~$5.18B). The remaining ~5.3B tokens — heavily weighted toward the airdrop/community and team/investor allocations — represent a material unlock overhang that can pressure price as vesting proceeds, even if trading volume stays strong. This wide MC/FDV gap is the single most important tokenomics consideration for ASTER versus the near-fully-circulating peers in its cluster.

*(Source: [[coingecko-top-1000-2026-04-09]]; figures refreshed to the 2026-06-20 snapshot.)*

---

## Architecture

AsterDEX operates as a **hybrid AMM-CEX model** across four blockchains:

- **AMM layer** for liquidity efficiency — aggregates liquidity across networks, reducing slippage by up to 40% for retail traders
- **CEX-style order book (Pro Mode)** for professional traders — sub-100ms matching latency via its native execution engine
- **Multi-chain deployment** — unlike [[hyperliquid|Hyperliquid's]] single-chain design, AsterDEX's multi-chain approach aggregates liquidity but introduces bridge/router risk across chains

Aster has plans to launch its **own Layer-1 blockchain**, though this is not yet live as of Q1 2026.

---

## Trading Modes

| Mode | Description | Max Leverage |
|------|-------------|-------------|
| **Pro Mode** | Full order book with hidden orders, TP/SL, advanced risk controls, automated grid trading | Standard caps |
| **Simple Mode** | One-click high-leverage trading, MEV-resistant execution | Up to 1001x |

### Hidden Orders

The **Hidden Orders** feature in Pro Mode is a standout — limit orders remain fully invisible in the public order book until executed, protecting large positions from MEV bots and front-running. This makes AsterDEX particularly attractive for whales and institutional-sized positions, in direct contrast to [[hyperliquid|Hyperliquid's]] fully transparent order book.

### Yield-Bearing Collateral

AsterDEX allows users to deposit yield-generating assets (asBNB, USDF) as collateral via its **Trade & Earn** program — margin earns yield while simultaneously backing trades, maximizing capital efficiency compared to platforms where collateral sits idle.

---

## Markets & Leverage

- **100+ trading pairs** including crypto perpetuals, spot, and **US stock perpetuals** (24/7, settled in crypto, up to 100x leverage)
- Leverage up to **1001x** in Simple Mode on BTC and ETH — at this leverage, a 0.1-0.2% adverse move triggers [[liquidation]], making it suited only for extremely short-term speculation
- Supports **isolated and cross-margin** modes
- Supports **4 blockchains**: Arbitrum, Ethereum, BNB Chain, Solana — no bridging required

---

## Fee Structure

| Market | Mode | Maker | Taker |
|--------|------|-------|-------|
| **Spot** | Standard | 0.04% | 0.10% |
| **Perps** | Pro | 0.005% | 0.040% |
| **Perps** | Simple (≤500x) | 0.08% open/close | 0.08% open/close |
| **Perps** | Simple (500x+) | No open fee | Dynamic (min 0.03%) |

Pro Mode perp maker fees (0.005%) are among the **lowest in the space** — significantly below [[hyperliquid|Hyperliquid's]] ~0.015%. A 5% discount applies when paying fees with ASTER. VIP volume tiers offer up to 50% discounts for high-frequency traders.

---

## Automation & API

AsterDEX has a growing automation ecosystem with both native and third-party tooling:

### Native API

- **Public API** with documented endpoints and rate limits
- **Python SDK** with full step-by-step tutorial on GitHub covering: authentication, balance checks, leverage/margin settings, market orders with TP/SL, trailing stop losses, batch orders, limit order management, and OHLCV data fetching
- **Liquidation data API** — real-time liquidation event feeds for building liquidation-aware bots
- **Bitquery GraphQL** developer API for perpetual futures data (liquidations, order lifecycle, [[funding-rate|funding rates]], margin data)

### Native Bots & Tools

- **Grid Trading Bots** — built directly into the platform UI, no external tool needed
- **EchoSync Copy Trading** — launched December 2025 integration enabling one-click mirroring of top traders or AI models
- **Human vs AI trading competition** — AsterDEX hosted a competition with AI models (Claude Sonnet, DeepSeek) competing, demonstrating the platform's engagement with algorithmic trading

### Developer Access

A full **API tutorial with Python code** is publicly available on GitHub, lowering the barrier for custom bot development.

---

## Security & Transparency

- Audited by **Halborn, PeckShield, and Salus**
- Live **Immunefi bug bounty** program
- Insurance fund backstop for [[liquidation]] events — users were compensated after an XPL index misconfiguration incident
- **Privacy-first**: Hidden orders and MEV protection designed for large-volume traders
- Governance through ASTER token; team retains ability to adjust trading parameters (leverage, funding, margin rates) in real-time

---

## Risks

- **Bridge/router risk**: Multi-chain architecture introduces additional attack surfaces across four chains
- **1001x leverage risk**: Extreme leverage in Simple Mode can result in [[liquidation]] from a 0.1-0.2% adverse price move
- **Centralized risk parameters**: Team can adjust leverage, funding, and margin rates in real-time — governance is not fully decentralized
- **Token dilution**: 53.5% of ASTER supply reserved for airdrops/community with ongoing vesting
- **Shorter track record**: Launched March 2025; less battle-tested than [[hyperliquid|Hyperliquid]]
- **Terms-based geo-restrictions**: Compliance enforcement is weaker than interface-level blocks
- **Token dilution / unlock overhang**: ~67% of max supply not yet circulating (MC/FDV ~0.34)
- **Macro / regime risk**: Even as a top-50 token, ASTER is a high-beta perp-DEX play exposed to the Established Bear Market (Fear & Greed 23 as of 2026-06-20)

---

## Market Structure & Derivatives

AsterDEX is itself a **derivatives venue** — the ASTER token is the equity-like claim on a perpetual-futures exchange, so token value tracks platform volume, fee capture, and market share rather than a productive cash flow.

- **Volume / market share:** Second-largest perpetual DEX by volume (~$77.77B monthly in Q1 2026) behind [[hyperliquid|Hyperliquid]] (~$178.23B), after recording ~$259B in both October and November 2025. The perp-DEX category has shifted from single-platform dominance to a genuine multi-venue duopoly.
- **Liquidity model:** Hybrid AMM + CEX-style order book, with hidden orders for MEV protection and yield-bearing collateral (asBNB, USDF) — see Architecture and Trading Modes above.
- **Token-level liquidity:** ASTER spot trades ~$102M/24h against a ~$1.74B cap (volume/cap ~0.06), healthy depth for a top-50 name; an ASTER-PERP market also trades on [[hyperliquid|Hyperliquid]], so watch [[funding-rate|funding]] and open interest for crowded positioning.

## Peer Comparison (perp DEXs & DEX tokens)

| Token / Venue | Rank | Market Cap | Category | Note |
|---|---|---|---|---|
| **Aster (ASTER)** | #48 | ~$1.74B | Perp DEX (multi-chain) | #2 perp DEX by volume; CZ-adjacent |
| [[hyperliquid\|Hyperliquid (HYPE)]] | top-tier | multi-$B | Perp DEX (own L1) | Category leader by volume |
| [[sushi\|Sushi (SUSHI)]] | #471 | ~$48.09M | Spot DEX / AMM | DeFi-1.0 blue chip |
| [[mango-markets\|Mango (MNGO)]] | #601 | ~$33.23M | Solana margin/perp DEX | Far smaller, illiquid |
| [[sun-token\|Sun (SUN)]] | #133 | ~$328.94M | TRON DEX/launchpad | Buyback-and-burn |

*Caps reflect the 2026-06-20 snapshot where available; HYPE shown qualitatively.*

## Valuation Framing (qualitative)

ASTER is best framed as a **revenue-share / market-share play on the perp-DEX category**. Bull case: the sector keeps taking share from CEXs, AsterDEX defends its #2 position (and its multi-chain + US-stock-perp + hidden-order differentiation), and fee capture plus token buy-pressure compound — justifying a premium top-50 valuation. Bear case: the ~$5.18B FDV implies large future dilution, Hyperliquid extends its lead, leverage-driven volume proves cyclical, and centralized risk-parameter control or a CZ/Binance-association headline re-rates the token lower. As a high-beta derivatives token in an Established Bear Market, drawdowns can be severe. *This is framing, not a price target or recommendation.*

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | ASTER/USDT |
| Kraken | ASTER/USD |
| Bitget | ASTER/USDT |
| KuCoin | ASTER/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ASTER-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Twitter** | [@Aster_DEX](https://twitter.com/Aster_DEX) |
| **Telegram** | [AsterDEX](https://t.me/AsterDEX) (35,952 members) |
| **GitHub** | [github.com/asterdex/api-docs](https://github.com/asterdex/api-docs) |
| **Whitepaper** | [docs.asterdex.com](https://docs.asterdex.com/usdaster) |

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- AsterDEX documentation and API docs
- DeFiLlama / DeFi Perp DEX volume rankings

---

## See Also

- [[hyperliquid]] — Largest perp DEX by volume; primary competitor
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] — Platform comparison
- [[perpetual-futures]] — How perpetual contracts work
- [[decentralized-exchanges]] — DEX architectures
- [[funding-rate]] — Funding rate mechanics
- [[bnb]] — BNB Chain ecosystem
- [[crypto-markets]]
