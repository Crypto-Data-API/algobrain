---
title: "Arbitrum"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["ARB", "Arbitrum One", "Offchain Labs"]
entity_type: protocol
founded: 2021
headquarters: "Decentralized (developer: Offchain Labs, New York)"
website: "https://arbitrum.io/"
related: ["[[aave]]", "[[arbitrum]]", "[[base]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[gmx]]", "[[hyperliquid]]", "[[l1-l2-rotation]]", "[[layer-2]]", "[[mantle]]", "[[optimism]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[pairs-trading]]", "[[polygon]]", "[[real-world-assets]]", "[[robinhood]]", "[[token-unlocks]]", "[[uniswap]]"]
---

# Arbitrum

**Arbitrum** (ARB) is the leading [[ethereum|Ethereum]] [[layer-2|Layer 2]]: an optimistic rollup developed by Offchain Labs that holds the largest TVL/TVS of any general-purpose Ethereum L2 (~$16.6B TVS, March 2026). The ARB token governs the Arbitrum DAO and its multi-billion-dollar treasury. The defining ARB trade tension: best-in-class network adoption (Robinhood Chain, tokenized equities, $10B+ stablecoin supply) against weak token value capture and persistent unlock supply — ARB has fallen ~96% from its 2024 high.

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.084409 |
| **Market Cap** | $536.92M |
| **Market Cap Rank** | #97 |
| **24h Volume** | $29.55M |
| **24h Change** | +1.20% |
| **7d Change** | -0.63% |
| **Circulating Supply** | 6.36B ARB (~64% of max) |
| **Total / Max Supply** | 10.00B / 10.00B ARB |
| **Fully Diluted Valuation** | $843.84M |
| **MC / FDV** | 0.64 |
| **All-Time High** | $2.39 (2024-01-12) — now ~-96.5% |
| **All-Time Low** | $0.074613 — now ~+13% above ATL |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

ARB sits just above its all-time low and has slipped out of the top-90 (rank #97), a stark divergence from its network leadership — the live embodiment of the "great network, weak token value capture" thesis. The 0.64 MC/FDV means ~36% of supply is still locked, so calendar unlocks remain a structural headwind. Context: the broad tape is in **extreme fear** (Fear & Greed = 23) in an "Established Bear Market" regime, and ARB's flat week (-0.63%) lagged DeFi blue chips like [[aave|AAVE]] (+11.9%).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ARB |
| **Market Cap Rank** | #97 (2026-06-20) |
| **Market Cap** | $536.92M at $0.084409 (2026-06-20) |
| **Sector** | [[layer-2|Layer 2]] (optimistic rollup), Ethereum Ecosystem, Governance |
| **Network scale** | ~$16.64B Total Value Secured (2026-03-16) — #1 general-purpose Ethereum L2; >$10B stablecoin supply (2025) |
| **Supply mechanics** | 10B max; ~64% circulating (2026-06-20); team/investor unlocks continue |
| **Token role** | Governance over Arbitrum DAO treasury; does not capture sequencer fees directly |
| **Website** | [https://arbitrum.io/](https://arbitrum.io/) |

> Earlier snapshot (2026-04-09, CoinGecko): rank #87, market cap $617.72M, price $0.1022.

---

## Overview

Arbitrum is one of the leading Ethereum scaling solutions, bringing cheap transactions to a large user base in an environment closely compatible with Ethereum. It is an optimistic rollup and the leading L2 by TVL. Mainnet launched August 2021; the ARB token was airdropped March 2023. It is fully EVM-compatible (Ethereum dApps deploy with minimal changes) and runs transactions ~10-50x cheaper than Ethereum mainnet. Major dApps live on Arbitrum include [[gmx|GMX]], [[aave|Aave]], [[uniswap|Uniswap V3]], Camelot (Arbitrum-native DEX), Pendle (yield trading), [[asterdex]], and Gains Network; [[hyperliquid]] also originated as an Arbitrum-bridged ecosystem (USDC deposits route via Arbitrum). The **Orbit** framework lets projects launch custom L2/L3 chains on the Arbitrum stack (used by Robinhood Chain).

### How optimistic rollups work

Arbitrum batches thousands of transactions off-chain and posts compressed transaction data to Ethereum. The "optimistic" model assumes transactions are valid by default, with a **challenge period (~7 days)** during which fraud proofs can be submitted. This provides strong security with significantly lower cost than executing on Ethereum directly. Settlement is on Ethereum mainnet; the ARB token is a pure governance token over the Arbitrum DAO (sequencer revenue accrues to the DAO, not automatically to holders).

---

## Protocol & Technology

| Component | What it is | Why it matters |
|---|---|---|
| **Nitro** | The core stack: WASM-based fraud-proof engine running a Geth fork; compresses calldata and posts to Ethereum | The performance/cost backbone; enabled 10–50x cheaper txs than mainnet |
| **Stylus** | A second VM (alongside EVM) letting devs write contracts in Rust, C, C++ (WASM), with ~10x+ cheaper compute for some workloads | Expands the developer pool beyond Solidity; differentiates vs EVM-only L2s |
| **BoLD** | Permissionless, bonded fraud-proof dispute protocol | Removes the trusted-validator whitelist — a key decentralization milestone for the optimistic security model |
| **Orbit** | Framework to launch custom L2/L3 chains settling to Arbitrum (e.g., **Robinhood Chain**) | The "appchain"/rollup-as-a-service business; the [[robinhood\|Robinhood]] win runs here |
| **Timeboost** | Express-lane transaction-ordering auction (live Apr 2025) | Converts MEV into DAO revenue (>$6M cumulative in its first year) |
| **Arbitrum Nova** | AnyTrust sidechain (data-availability committee) for ultra-cheap social/gaming txs | A separate, cheaper-but-less-decentralized chain alongside Arbitrum One |

### Governance and the DAO

ARB is a **pure governance token**. Sequencer fees, Timeboost auction proceeds, and Arbitrum Expansion Program income accrue to the **Arbitrum DAO treasury**, not automatically to ARB holders — the crux of the value-capture debate. The DAO (with the Arbitrum Foundation and the Security Council) controls a multi-billion-dollar treasury, protocol upgrades, and ecosystem grants. 2025–26 **buyback initiatives** (~92.65M ARB moved to treasury) are the first mechanisms linking network revenue to token demand, but DAO revenue still trails ecosystem spending — prompting the FY2027 budget debate.

### Settlement and security

Arbitrum One inherits Ethereum's security via on-chain data posting and the BoLD dispute game; the ~7-day challenge window is the canonical L2 withdrawal-finality tradeoff. The chain is fully **EVM-equivalent**, so [[ethereum|Ethereum]] dApps deploy with minimal changes.

### Major developments 2025-2026

- **Timeboost (Apr 2025)** — Arbitrum's express-lane transaction-ordering auction went live, converting MEV into DAO revenue: **>$6M cumulative fees in its first year**. Total 2025 DAO gross revenue ≈ **$23.5M** (transaction fees + Timeboost + Arbitrum Expansion Program).
- **Robinhood (mid-2025 onward)** — [[robinhood|Robinhood]] launched tokenized US stocks/ETFs for EU customers **on Arbitrum One** (~2,000 tokenized assets within six months) and is building its own **Robinhood Chain** on Arbitrum's Orbit stack — the highest-profile TradFi endorsement of any L2.
- **DAO treasury & buybacks (2025-26)** — buyback initiatives moved ~92.65M ARB (~$30-47M) to the treasury; the Foundation diversified to >$150M in non-ARB assets by end-2025. DAO revenue still trails ecosystem spending, prompting fresh funding proposals in 2026.
- **Scale (2025)** — Arbitrum touted ~$20B TVS and $10B+ stablecoin supply in its 2025 growth review; $16.64B TVS as of 2026-03-16 kept it the largest general-purpose Ethereum L2. Over **2.1 billion transactions** processed in 2025 across **1,000+ projects**, with **$800M+ in tokenized real-world assets** on-chain by end-2025. DAO revenue comes from transaction fees, Timeboost auctions, treasury management, and the Arbitrum Expansion Program at 90%+ gross margins.
- **Token unlocks** — ongoing monthly cliff unlocks (e.g., **92.65M ARB, ~$7.6M, on 2026-06-16**) keep persistent supply pressure on ARB — calendar-known events relevant to [[token-unlocks]] strategies.
- **June 2026** — the Arbitrum Foundation proposed its fiscal-year 2027 budget to the DAO.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 6.36B ARB (~64% of max) |
| **Total Supply** | 10.00B ARB |
| **Max Supply** | 10.00B ARB |
| **Fully Diluted Valuation** | $843.84M |
| **Market Cap / FDV Ratio** | 0.64 |

ARB is a **pure governance token**: sequencer revenue accrues to the DAO, not automatically to holders — the crux of the value-capture debate. Buyback programs (2025-26) are the first mechanisms linking network revenue to token demand.

**Dilution flag (HIGH).** With MC/FDV at 0.64, ~36% (~3.64B ARB) is still locked — the largest dilution overhang of the six tokens here. Distribution: ~44% DAO treasury, ~27% team/advisors, ~17% investors, plus airdrop/ecosystem allocations, vesting on monthly cliffs. **Ongoing monthly cliff unlocks** (e.g., ~92.65M ARB, ~$7.6M, on 2026-06-16) impose persistent supply pressure — calendar-known events tradable via [[token-unlocks]] strategies. Buybacks partially offset this but have not yet outpaced emissions.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.084409 |
| **All-Time High** | $2.39 (2024-01-12) — now ~-96.5% |
| **All-Time Low** | $0.074613 — price sits ~+13% above ATL |
| **7d Change** | -0.63% (lagging the DeFi bounce) |

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

| Chain | Address |
|---|---|
| Arbitrum One | `0x912ce59144191c1204e64559fe8253a0e49e6548` |
| Arbitrum Nova | `0xf823c3cd3cebe0a1fa952ba88dc9eef8e0bf46ad` |
| Ethereum | `0xb50721bcf8d664c30412cfbc6cf7a15145234ad1` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | ARB/USDT |
| Kraken | ARB/USD |
| Upbit | ARB/KRW |
| Bitget | ARB/USDT |
| KuCoin | ARB/USDT |
| Crypto.com Exchange | ARB/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ARB-PERP | Perpetual |
| Uniswap V3 (Ethereum) | ARB/WETH | Spot |

---

## Trading Relevance

- **Narrative basket**: Ethereum L2s (vs OP, ZK, STRK, BASE-adjacent plays) and "tokenized equities / TradFi-on-chain" via the Robinhood relationship. ARB is the liquid proxy for the L2 sector and for Robinhood Chain headlines.
- **Value-capture catalysts**: Timeboost revenue growth, DAO buyback expansion, and any fee-switch-style proposal are the levers that could re-rate ARB; treasury-vs-spending governance fights are the bear catalysts.
- **Supply**: ~40% of max supply still non-circulating in April 2026; unlock dates remain tradable events. MC/FDV 0.60.
- **Liquidity**: excellent — ~$108M daily spot volume (April snapshot), deep perps on Binance/Bybit/[[hyperliquid]]; suitable for both directions at size.
- **Relative-value**: ARB/OP and ARB/ETH ratios are standard L2 pair trades; ARB's TVS leadership vs its sub-$1B FDV (June 2026) is the value argument, weak direct value capture the counter.

---

## Ecosystem & Use Cases

- **DeFi** — [[gmx|GMX]] (perps, Arbitrum-native), [[aave|Aave]], [[uniswap|Uniswap V3]], Camelot (native DEX), Pendle (yield), [[asterdex]], Gains Network; [[hyperliquid|Hyperliquid]] originated as an Arbitrum-bridged ecosystem (USDC deposits route via Arbitrum).
- **Tokenized equities / RWA** — [[robinhood|Robinhood]] runs ~2,000 tokenized US stocks/ETFs for EU users on Arbitrum One; $800M+ in tokenized [[real-world-assets|RWAs]] on-chain by end-2025.
- **Appchains (Orbit)** — Robinhood Chain and other L2/L3s settle to Arbitrum, making it a rollup hub, not just a single chain.
- **Stablecoins / payments** — $10B+ stablecoin supply (2025) underpins on-chain settlement and DeFi collateral.
- **Scale** — 2.1B+ transactions in 2025 across 1,000+ projects at 90%+ gross margins on DAO revenue lines.

---

## Market Structure & Derivatives

- **Spot venues** — [[binance|Binance]] (ARB/USDT), [[kraken|Kraken]], Upbit (KRW), Bitget, KuCoin, Crypto.com; on-chain on Uniswap V3 (ARB/WETH). 24h spot volume ~$29.55M (2026-06-20) — thinner than the April snapshot, reflecting the risk-off tape.
- **Perpetuals** — ARB-PERP on [[hyperliquid|Hyperliquid]], Binance Futures, Bybit, OKX; ARB is one of the more liquid L2 perps and a common short-side expression of the "L2 token value-capture" bear thesis.
- **Funding / OI** — ARB perp funding has skewed neutral-to-negative through the bear; persistent negative funding (shorts pay) signals a crowded short and squeeze potential into positive catalysts (buyback/Robinhood headlines).
- **Pair trades** — ARB/OP ([[optimism|Optimism]]) and ARB/ETH are the canonical L2 relative-value expressions; ARB vs newer L2s like [[mantle|Mantle]] captures incumbent-vs-challenger rotation.

---

## Valuation Framework

ARB is hard to value on cash flows because the token does not directly capture fees. Useful lenses (describe, do not invent values):

- **TVS / TVL** — Total Value Secured (~$16.6B) is the dominance metric; track via L2BEAT and DefiLlama. ARB's share of total L2 TVS is the network-leadership argument.
- **DAO revenue** — sequencer fees + Timeboost + Expansion Program (~$23.5M gross in 2025). Because this accrues to the *DAO*, not holders, the relevant question is whether buybacks/fee-switch proposals convert it to token demand.
- **FDV vs treasury** — ARB's FDV ($844M) vs the DAO's multi-billion treasury (including >$150M diversified non-ARB assets) frames a "trading below treasury-backed value" deep-value case — heavily caveated by governance control of that treasury.
- **MC/FDV (0.64)** — the dilution adjustment that any valuation must apply.

---

## Trading Playbook

- **The core tension** — best-in-class adoption (Robinhood, $16.6B TVS) vs weak value capture and dilution. The token re-rates only if value capture improves (buyback expansion, fee-switch) or a major catalyst (Robinhood Chain mainnet) lands.
- **Macro context** — in the **extreme-fear / Established Bear Market** regime (F&G = 23), pure-governance L2 tokens with dilution are among the weakest beta; ARB lagged the DeFi bounce (-0.63% week). Bounces favor cash-flow tokens ([[aave|AAVE]]) over governance-only ones.
- **Catalysts (bull)** — Timeboost revenue growth, buyback expansion, any fee-switch proposal, Robinhood Chain milestones, Stylus adoption.
- **Catalysts (bear)** — monthly unlock cliffs, DAO treasury-vs-spending fights, the FY2027 budget outcome, L2 fee compression.
- **Risk discipline** — size around unlock dates ([[token-unlocks]]); ARB near ATL can grind lower on supply alone even with strong network metrics.

---

## History

- **2018** — Offchain Labs (Ed Felten, Steven Goldfeder, Harry Kalodner) founded.
- **Aug 2021** — Arbitrum One mainnet.
- **2022** — Nitro upgrade (WASM fraud proofs, calldata compression).
- **Mar 2023** — ARB token airdrop and Arbitrum DAO launch.
- **2023** — Stylus testnet (multi-VM, Rust/C/C++); Arbitrum Nova.
- **2024** — ATH $2.39 (Jan); subsequent ~96% drawdown.
- **2025** — BoLD permissionless proofs; Timeboost live (Apr); [[robinhood|Robinhood]] tokenized equities + Robinhood Chain on Orbit; 2.1B+ txs; buyback initiatives.
- **2026** — $16.64B TVS (#1 general-purpose L2); 2026-06-16 unlock of 92.65M ARB; Foundation proposes FY2027 budget.

---

## Competitive Positioning

| L2 | Token | Stack | Differentiator vs Arbitrum |
|---|---|---|---|
| **Arbitrum** | ARB | Optimistic rollup (Nitro/Stylus/Orbit) | #1 general-purpose TVS; Robinhood; multi-VM (Stylus); large DAO treasury |
| [[optimism\|Optimism]] | OP | Optimistic rollup (OP Stack / Superchain) | Superchain shared-sequencer vision; Base built on OP Stack; smaller standalone TVS |
| [[base\|Base]] | (no token) | OP Stack rollup by Coinbase | Coinbase distribution + fiat on-ramp; no token (no governance trade) |
| [[mantle\|Mantle]] | MNT | Modular L2 (EigenDA-style DA) | Large treasury; modular DA; smaller ecosystem |
| [[polygon\|Polygon]] | POL | PoS chain + AggLayer | Payments/RWA focus; not a pure rollup; AggLayer interop play |

ARB's edge is incumbency: the deepest general-purpose L2 ecosystem and the marquee Robinhood relationship. The shared weakness across optimistic-rollup tokens (ARB, OP) is fee value-capture; **Base** sidesteps the debate by having no token at all, which is itself a competitive pressure on ARB's narrative.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://arbitrum.io/](https://arbitrum.io/) |
| **Twitter** | [@arbitrum](https://twitter.com/arbitrum) |
| **Telegram** | [arbitrum](https://t.me/arbitrum) (10,172 members, Apr 2026) |
| **Discord** | [https://discord.com/invite/Arbitrum](https://discord.com/invite/Arbitrum) |
| **GitHub** | [https://github.com/ArbitrumFoundation/docs](https://github.com/ArbitrumFoundation/docs) |

---

## Developer Activity (snapshot 2026-04-09)

| Metric | Value |
|---|---|
| **GitHub Stars** | 96 |
| **GitHub Forks** | 122 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 245 |
| **Contributors** | 21 |

---

## Risks

- **Value capture (HIGH)** — sequencer/Timeboost revenue goes to the DAO, not holders; without a fee-switch or sustained buybacks, the token may permanently lag the network.
- **Dilution (HIGH)** — ~36% of supply still locked; monthly unlock cliffs impose calendar-known sell pressure ([[token-unlocks]]).
- **Governance / treasury risk** — DAO spending outpaces revenue; budget fights (FY2027) and treasury mismanagement are recurring bear catalysts.
- **L2 competition & fee compression** — [[base|Base]] (no token), [[optimism|Optimism]]'s Superchain, ZK rollups, and post-blob Ethereum upgrades compress L2 economics.
- **Centralization/security** — sequencer centralization and the ~7-day optimistic challenge window remain structural tradeoffs (BoLD mitigates the validator-set side).
- **Macro beta** — in the current **Established Bear Market** / extreme-fear regime, governance-only L2 tokens are high-beta to risk-off.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[hyperliquid]]
- [[robinhood]]
- [[gmx]]
- [[layer-2]]
- [[narrative-trading]]
- [[real-world-assets]]
- [[decentralized-exchange]]
- [[aave]] — major dApp on Arbitrum
- [[base]] — competing L2 (Coinbase)
- [[optimism]] — competing optimistic rollup
- [[mantle]] — competing modular L2
- [[polygon]] — another Ethereum scaling solution
- [[token-unlocks]] — ARB unlock schedule trading
- [[l1-l2-rotation]] — rotation dynamics between L1s and L2s

---

## Sources

- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko): price $0.084409, mcap $536.92M, rank #97, vol $29.55M, 24h +1.20%, 7d -0.63%, FDV $843.84M, MC/FDV 0.64.
- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Blockworks — Arbitrum Timeboost goes live: https://blockworks.co/news/arbitrum-timeboost-live-dao-revenue
- CoinLaw — Arbitrum statistics 2026 (TVS, revenue, Robinhood): https://coinlaw.io/arbitrum-statistics/
- CryptoRank — Arbitrum 2025 growth story ($20B TVS, $10B stablecoins): https://cryptorank.io/news/feed/9f492-arbitrum-2025-growth-story
- AMBCrypto — Arbitrum DAO funding/revenue gap: https://ambcrypto.com/arbitrum-seeks-fresh-funding-as-dao-revenue-still-trails-ecosystem-spending/
- CoinLore — ARB price/rank (June 2026): https://www.coinlore.com/coin/arbitrum
- Arbitrum Foundation, "2025 Transparency Report: The Year of Institutional Adoption" — https://blog.arbitrum.foundation/the-arbitrum-foundation-2025-transparency-report-the-year-of-institutional-adoption/
- Arbitrum Foundation, "Arbitrum in 2025: The Year of Everywhere" — https://blog.arbitrum.foundation/arbitrum-in-2025-the-year-of-everywhere/
- crypto.news, "Arbitrum ecosystem enters institutional phase as transactions top 2.1B and TVL hits $20B" — https://crypto.news/arbitrum-ecosystem-enters-institutional-phase-as-transactions-top-2-1b-and-tvl-hits-20b/
- Web verification, 2026-06-10 (2026-06-16 unlock of 92.65M ARB; FY2027 budget proposal).

## Trading Profile

### Venues & liquidity

ARB is a deep, liquid two-venue derivatives market. It trades on **both [[binance|Binance]]** (ARB/USDT spot plus a USD-margined perpetual) and **[[hyperliquid|Hyperliquid]]** (ARB-PERP, up to ~40-50x leverage). This dual-venue availability means execution can be split across a large centralized book (Binance) and the on-chain HL book, tightening effective spreads and letting size scale into the market without single-venue slippage. Order-book depth is solid for a rank-~96 alt — thinner than the majors, so tactical sizing and limit-based entries beat aggressive market orders in the risk-off tape. The presence of the same asset on a CEX perp and an on-chain perp opens venue-relative funding and basis expressions (see below); it also makes the L2-sector short thesis easy to express with leverage on either venue.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — ARB perps live on both Binance and Hyperliquid, so funding-rate gaps between the CEX and HL books are directly harvestable.
- [[funding-rate-harvest]] — ARB perp funding has skewed neutral-to-negative through the bear; systematically collecting funding on the paid side is a repeatable carry on a liquid alt perp.
- [[crowded-short-funding-fade]] — persistent negative funding (shorts pay) on ARB flags crowded shorts, setting up squeeze fades into buyback/Robinhood catalysts.
- [[token-unlock-supply-event]] — ARB's calendar-known monthly cliff unlocks (~92.65M ARB) are tradable, pre-scheduled supply events tailor-made for unlock positioning.
- [[cash-and-carry]] — with liquid ARB spot (Binance/Uniswap) and USD-margined perps, long-spot / short-perp carry captures basis when funding runs positive.
- [[pairs-trading]] — ARB/OP and ARB/ETH are the canonical L2 relative-value pairs; ARB's TVS leadership vs weak value capture drives the spread.

### Volatility & regime character

ARB is a **high-beta Ethereum L2 / DeFi-infrastructure governance token**. It trades as the liquid proxy for the L2 sector and moves with ETH and broad alt risk sentiment, amplified to the downside because it is a pure-governance token with a heavy dilution overhang. Correlation to [[ethereum|ETH]] is high (it is an Ethereum-ecosystem asset), and it is a high-beta expression of BTC/ETH direction: it lags on bounces (governance-only tokens underperform cash-flow tokens like [[aave|AAVE]]) and leads on drawdowns. In the current Established Bear Market / extreme-fear regime, ARB's beta to risk-off is elevated, and it can grind lower on supply pressure even when network metrics are strong.

### Risk flags

- **Dilution / token unlocks** — MC/FDV ~0.64 means ~36% of supply is still locked; monthly cliff unlocks impose calendar-known sell pressure ([[token-unlocks]]).
- **Weak value capture** — sequencer/Timeboost revenue accrues to the DAO, not holders, so the token can persistently lag the network; narrative-dependent re-rating (buyback/fee-switch/Robinhood Chain).
- **Narrative dependence** — price hinges on L2-sector sentiment and Robinhood/tokenized-equities headlines rather than fundamentals.
- **Perp funding dislocations** — persistent negative funding can flip violently into positive catalysts, causing squeezes; leveraged shorts are exposed on either venue.
- **Liquidity / venue concentration** — deep but not major-tier; spot volume thins in risk-off tape, so slippage rises for aggressive sizing despite the two-venue book.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=ARB` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=ARB` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=ARB&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=ARB&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=ARB"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[arbitrum]]

---
