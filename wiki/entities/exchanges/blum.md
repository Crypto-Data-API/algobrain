---
title: "Blum"
type: entity
created: 2026-05-05
updated: 2026-06-10
status: good
tags: [crypto, exchange, derivatives, defi]
entity_type: exchange
founded: 2024
website: "https://blum.io"
aliases: ["Blum Exchange", "Blum Crypto", "BLUM"]
related: ["[[binance]]", "[[bybit]]", "[[hyperliquid]]", "[[okx]]", "[[crypto-perp-backtesting-pitfalls]]", "[[counterparty-risk]]", "[[perpetual-futures]]"]
---

Blum is a Telegram-native "hybrid exchange" — a mini-app that aggregates spot, memecoin, and derivatives trading across 30+ blockchains (TON, Solana, Ethereum, BNB Chain, and others) directly inside Telegram chats, with minimal friction and a gamified onboarding funnel. Aimed squarely at retail users and emerging-market traders who already live inside Telegram, it is part of the broader 2024-2026 wave of "messenger-native" finance products that changed the distribution of retail order flow. Its BLUM token launched via airdrop/TGE in June 2025, weeks after co-founder Vladimir Smerkis was arrested in Moscow on fraud charges unrelated to Blum itself.

## Founding and Product

Blum was founded in 2024 by former [[binance|Binance]] regional executives — CEO Gleb Kostarev (ex-Binance Asia head) and Vladimir Smerkis (ex-Binance CIS head, who departed in May 2025; see below) — as part of the Telegram TON / mini-app ecosystem boom. It onboarded users through a viral tap-to-earn "Drop Game" in the mold of Notcoin and Hamster Kombat, then layered trading on top. It is positioned alongside other Telegram-bot trading interfaces (Maestro, BananaGun, Unibot for spot DEX sniping) but differentiates with its "hybrid exchange" model: DEX-style multi-chain token access plus CEX-style order types and [[perpetual-futures|perpetual futures]] with leverage, plus a "memepad" for launching new tokens.

The product is consumed primarily through a Telegram bot / mini-app: a user opens a chat, taps a market, sets leverage, and submits an order without leaving the messenger. Funds are typically deposited via on-chain transfer to addresses managed through the app.

## Key Events 2025-2026

| Date | Event |
|---|---|
| 2025-05 (~17th) | Co-founder Vladimir Smerkis arrested in Moscow on "fraud on an especially large scale" charges (Art. 159 Russian Criminal Code, 2-12 years exposure). The case relates to his pre-Blum 2017 ventures The Token Fund and Tokenbox, where investor losses reportedly exceeded $15M. Blum stated he resigned as CMO and holds no co-founder role, and that the airdrop was unaffected. |
| 2025-06-25/28 | BLUM token TGE and airdrop after repeated delays: 30% of each user's allocation unlocked at TGE (2025-06-27), remaining 70% vesting linearly over six months. Initial trading on DEXes. |
| H1 2026 | BLUM listed on major centralized exchanges; phased token unlocks continue. |

User-count claims should be treated skeptically: Blum marketing cited tens of millions of registered tap-game users at peak, while a 2025 project statement referenced ~5.3 million users — registered-vs-active gaps of 10x+ are normal for Telegram mini-apps.

## Trading Mechanics

| Feature | Detail |
|---|---|
| **Product** | Perpetual futures (USDT-margined) |
| **Leverage** | Retail-tier (commonly up to 50-100x on majors, lower on small caps) |
| **Pairs** | BTC, ETH, SOL, and a long tail of altcoin perps |
| **Fees** | Retail-skewed taker fees; promotional rebates common |
| **Funding** | Standard 8-hour funding interval (per typical CEX-perp design) |
| **Custody** | Custodial — user funds held by Blum |
| **KYC** | Minimal or none on lower tiers; jurisdiction-dependent enforcement |

Specific fee schedules and leverage caps change frequently with promotional campaigns; check the official Blum docs for current numbers before sizing a strategy around them. (The table above reflects the typical Telegram-venue perp template; Blum's verified differentiators are the multi-chain hybrid spot/memepad layer and the BLUM token — see Key Events.)

## Telegram-Native UX

The strategic significance of Blum is not its matching engine — it is the distribution channel.

- Telegram has 900M+ monthly active users, heavily concentrated in CIS, MENA, and Southeast Asia
- Mini-apps inside Telegram bypass app-store review and let new users start trading in seconds
- Social virality (group chats, referral codes, copy-trading inside threads) compresses customer acquisition cost vs. traditional CEXes
- The same UX pattern previously turned Hamster Kombat and Notcoin into 100M+ user products inside Telegram

For traders studying retail flow, this matters: a meaningful and growing share of small-size perp orders now originate in Telegram chats rather than Binance / Bybit web apps, and that flow has different behavioral patterns.

## Liquidity and Order-Flow Profile

Blum's order flow skews:

- **Smaller per-trade size** than Binance / [[bybit|Bybit]] / OKX (retail-only book)
- **Higher leverage in proportion to size** — many users run 50-100x on small notional
- **More directional / less hedged** — retail users are predominantly long-biased on BTC/ETH and chase momentum on altcoins
- **Shallower book depth** than top-tier CEXes — large institutional orders cannot be filled here without significant slippage

Total-volume comparisons should be made cautiously: Blum and similar Telegram venues report aggressive marketing numbers, and reconciling them against on-chain deposit flow is non-trivial.

## Backtesting Implications

Blum (and Telegram-native venues generally) distort standard CEX backtest assumptions in three specific ways:

1. **Liquidity is shallower** — a backtest that assumes Binance-level depth will fill at prices that are not achievable on Blum. [[slippage-modeling|Slippage models]] calibrated to top-tier venues understate costs by 3-10x for the same notional.
2. **Retail-skewed flow distorts microstructure signals** — order-book imbalance, aggressor flow, and liquidation patterns differ from where institutional flow dominates. A signal trained on Binance order-flow features may not generalize.
3. **Liquidation cascades behave differently** — high leverage on shallow books means liquidations have outsized price impact per dollar of notional. The 2025 ADL crisis (see [[crypto-perp-backtesting-pitfalls]]) hit shallow-book venues disproportionately.

For research purposes Telegram-native venues are usually treated as either a separate bucket in cross-exchange studies or excluded from backtests targeting institutional-scale strategies.

## Risks

| Risk | Description |
|---|---|
| **Counterparty / custody** | Funds are custodial; Blum holds them. No proof-of-reserves equivalent to top-tier CEXes is widely audited. See [[counterparty-risk]]. |
| **Regulatory** | Telegram-distributed financial products face regulatory scrutiny in EU (MiCA), UK (FCA), US (CFTC/SEC). Geo-blocks are interface-level and easily bypassed, which compounds the risk. |
| **Operational** | Smaller venues have weaker incident-response and tooling than top-tier CEXes. Withdrawal halts during stress events are more likely. |
| **Liquidity** | Shallow book means large positions may be impossible to exit cleanly during volatility. |
| **Front-end risk** | Telegram-bot UX abstracts away order-detail confirmation that web/desktop UIs make explicit; misclicks at high leverage are easy. |
| **KYC inconsistency** | Lax KYC at sign-up may be retroactively tightened, freezing accounts of users who can't complete verification. |
| **Key-person / governance** | The May 2025 Moscow arrest of co-founder Smerkis (for pre-Blum ventures) shows how founder legal risk transmits to token price and airdrop confidence even when the project itself is not charged. |
| **Token-unlock overhang** | 70% of the June 2025 airdrop vested linearly over six months, and team/investor unlocks continue through 2026 — persistent sell-pressure schedule typical of mini-app tokens. |

## Comparison to Alternative Retail Perp Venues

| Venue | Distribution | Depth | KYC | Notes |
|---|---|---|---|---|
| **Blum** | Telegram bot | Shallow | Light | Retail-only flow; emerging markets focus |
| **[[binance|Binance]]** | Web / app | Deep | Full | Largest perp venue globally |
| **[[bybit|Bybit]]** | Web / app | Deep | Full | Strong derivatives focus |
| **[[okx|OKX]]** | Web / app | Deep | Full | Strong APAC presence |
| **[[hyperliquid|Hyperliquid]]** | Web + on-chain | Deep | None (wallet-based) | Decentralized; institutional-quality CLOB |
| **MetaMask Perps** | Wallet-native | Mid | None | Self-custodial; growing |
| **Phemex** | Web / app | Mid | Light tier available | Retail-focused CEX |

Blum's closest peer in distribution model is the broader Telegram-bot category (Maestro, BananaGun for spot DEXes); its closest peer in product type is a mid-tier retail-focused CEX without the brand recognition of the top five.

## Sources

1. Blum official site — https://blum.io
2. "Top 5 crypto platforms for perpetual futures" (Blum blog) — https://blum.io/post/top-5-crypto-platforms-for-perpetual-futures
3. Telegram TON ecosystem coverage and crypto-perp landscape research (2026-04-22 gap-finder source: `raw/articles/2026-04-22-gap-finder-backtesting-pitfalls-in-particular-with-.md`)
4. The Block, "Blum co-founder, ex-Binance exec Vladimir Smerkis arrested in Moscow on fraud charges" (2025-05) — https://www.theblock.co/post/354733/blum-co-founder-ex-binance-exec-vladimir-smerkis-arrested-in-moscow-on-fraud-charges
5. KuCoin Learn, "What Is Blum Crypto, a Trending Hybrid Exchange in Telegram?" — https://www.kucoin.com/learn/crypto/what-is-blum-hybrid-exchange-telegram-mini-app
6. Bitget Academy, "Blum Airdrop, TGE & Listing Day Set for June 27, 2025" — https://www.bitget.com/academy/blum-airdrop-tge-token-listing-details-june-27-2025
7. CoinMarketCap Academy, "Blum Airdrop Guide: How to Participate, Listing Date and TGE" — https://coinmarketcap.com/academy/article/blum-airdrop-guide-how-to-participate-listing-date-and-tge
8. Verified via Perplexity (sonar) and web search, 2026-06-10

## Related

- [[binance|Binance]] — Largest centralized perp venue; institutional benchmark
- [[bybit|Bybit]] — Major retail-friendly derivatives CEX
- [[hyperliquid|Hyperliquid]] — Decentralized perp venue with deep liquidity
- [[okx|OKX]] — Major derivatives CEX with strong APAC presence
- [[perpetual-futures]] — How perp contracts work
- [[crypto-perp-backtesting-pitfalls]] — Why retail-venue flow distorts standard assumptions
- [[counterparty-risk]] — Custody and venue solvency risk
- [[exchanges-overview]] — Catalog of crypto exchanges
