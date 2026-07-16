---
title: "Linea"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, defi, altcoins, ethereum]
aliases: ["LINEA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://linea.build/association"
related: ["[[consensys]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[zero-knowledge-proofs]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]"]
---

# Linea

**Linea** (ticker **LINEA**) is a [[layer-2]] [[zero-knowledge-proofs|zk]]-rollup for [[ethereum]], built by [[consensys]] (the company behind MetaMask and Infura). It is a Type-2 zkEVM — fully Ethereum-equivalent at the bytecode level — that batches transactions off-chain and posts validity proofs to Ethereum [[mainnet]]. Its design is explicitly aligned with Ethereum: LINEA tokenomics route protocol revenue into burning both ETH and LINEA, positioning the chain as an ETH-aligned execution layer rather than a competing [[layer-1]]. Governance sits with the Linea Association, a non-profit consortium of Ethereum-native builders.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | LINEA |
| **Market Cap Rank** | #391 |
| **Market Cap** | $61.63M |
| **Current Price** | $0.00254735 |
| **24h Change** | +3.75% |
| **7d Change** | -2.34% |
| **24h Volume** | $9.94M |
| **All-Time High** | $0.04667 (September 2025) |
| **All-Time Low** | $0.00226 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The broader tape is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] sits at **23 (extreme fear)** and the long-horizon regime reads as an **Established Bear Market** as of 2026-06-21. LINEA is one of the firmer names in this peer group on the day (+3.75%) but still trades roughly 13% above its all-time low (~$0.00226) and about 95% below its September-2025 all-time high (~$0.0467) — a typical post-airdrop drawdown profile for a recently launched [[layer-2]] token.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~24.17B LINEA |
| **Total Supply** | ~71.59B LINEA |
| **Max Supply** | ~72.01B LINEA |
| **Fully Diluted Valuation (FDV)** | ~$183.43M |
| **Market Cap / FDV** | ~0.34 |

With circulating supply only ~34% of fully diluted supply, a large share of tokens remains locked in ecosystem and contributor allocations, implying meaningful future emission and dilution pressure. Notably, LINEA is **not** the gas token of the network — transactions on Linea are paid in [[ethereum|ETH]]. The token's value accrual is driven by a dual-burn mechanism: a portion of net protocol fees (in ETH) is used to burn ETH, and the remainder buys back and burns LINEA, tying token scarcity to network usage rather than to staking inflation. There is no native LINEA staking-for-security model in the conventional [[proof-of-stake]] sense, since the chain's security inherits from Ethereum via validity proofs.

---

## How & Where It Trades

**Spot venues.** LINEA is listed on major centralized exchanges including [[binance]] (LINEA/USDT), [[kraken]] (LINEA/USD), Upbit (LINEA/KRW), Bitget, KuCoin, and Crypto.com. On-chain, it trades on Uniswap V3 (Ethereum) and DEXs within the Linea ecosystem.

**Derivatives.** A LINEA perpetual is listed on [[hyperliquid]] (LINEA-PERP), alongside perp markets on the major centralized derivatives venues. As a small-cap (~$59M) token, open interest and funding are thin and prone to sharp swings; funding/OI should be checked live before sizing any leveraged position. Liquidity is concentrated in USDT pairs, and 24h volume (~$9.7M) is modest relative to market cap, so slippage on larger orders is a real concern.

---

## Technology & Consensus

Linea is a **Type-2 zkEVM** — bytecode-equivalent to Ethereum, meaning existing Solidity contracts and developer tooling work unchanged. The architecture follows the standard zk-rollup pattern:

- A **sequencer** orders and executes transactions off-chain.
- A **prover** generates succinct [[zero-knowledge-proofs|zero-knowledge validity proofs]] (using a lattice-based proof system) attesting that the state transition is correct.
- Proofs and compressed transaction data are posted to [[ethereum|Ethereum L1]], which acts as the settlement and data-availability layer.

Because correctness is enforced cryptographically by validity proofs (not by an optimistic challenge window), withdrawals do not require the multi-day fraud-proof delay associated with optimistic rollups like [[arbitrum]] and [[optimism]]. Security ultimately inherits from Ethereum.

---

## Use Case, Narrative & Category

Linea sits in the **Ethereum-scaling / zkEVM L2** category alongside [[zksync]], [[starknet]], Polygon zkEVM, and [[scroll]]. Its differentiated narrative is "ETH alignment": the chain is marketed as the place where ETH capital is most productive (native yield on bridged ETH, ETH burn, deep DeFi integration), leaning on Consensys's distribution through MetaMask and Infura. Categories tagged on the asset include Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Linea Ecosystem, and Consensys Portfolio.

---

## Valuation Framing (qualitative)

Linea is a ~$62M-cap zkEVM L2 token with a distinctive value-accrual design: it is **not** the gas token (gas is paid in [[ethereum|ETH]]), and instead accrues value through a dual-burn of ETH and LINEA funded by protocol fees. That makes the bull case explicitly a *usage-and-burn* flywheel — if Linea captures meaningful L2 activity, the burn tightens supply — backed by [[consensys]]'s MetaMask/Infura distribution. The bear case is twofold: MC/FDV ≈ 0.34 means ~66% of supply is still locked and emitting, a structural overhang; and post-EIP-4844 blob pricing has compressed L2 fees across the board, shrinking the revenue that powers the burn just as zkEVM competition (zkSync, Starknet, Scroll, Polygon zkEVM) intensifies. A young, unproven flywheel against a deep dilution schedule. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | Gas token |
|---|---|---|---|---|---|---|
| **Linea** | LINEA | zkEVM [[layer-2]] | #391 | $61.63M | ~0.34 | [[ethereum\|ETH]] (not LINEA) |
| [[zksync]] | ZK | zkEVM L2 | — | — | — | ETH |
| [[starknet]] | STRK | zk-rollup L2 | — | — | — | STRK / ETH |
| [[mina-protocol]] | MINA | Succinct zk [[layer-1]] | #427 | $54.22M | ~1.00 | MINA |
| [[astar]] | ASTR | Multi-chain L1/L2 (zkEVM) | #475 | $47.34M | ~0.87 | ASTR |

*Among ZK peers, Linea is unusual in not using its own token for gas — value accrual rests entirely on the ETH/LINEA dual-burn rather than on gas demand or staking inflation.*

---

## Notable History

- Linea launched its mainnet (alpha) in mid-2023, incubated by [[consensys]].
- The **LINEA token generation event** occurred in September 2025; the token printed its all-time high (~$0.0467) shortly after launch before entering a prolonged decline.
- As of 2026-06-21 the token trades near its all-time low (~$0.00226), down ~95% from ATH — consistent with broad post-airdrop unwinding and the prevailing bear-market regime, though it posted a modest daily bounce against the peer set.

---

## Risks

- **Dilution.** Circulating supply is only ~34% of total; ongoing unlocks of ecosystem and contributor allocations are a structural overhang.
- **Centralization (current).** Like most rollups, Linea's sequencer and prover are not yet fully decentralized, creating censorship and liveness risk and a trusted operator dependency.
- **Intense L2 competition.** zkEVM is a crowded field; fee compression (post-EIP-4844 blob pricing) squeezes the revenue that funds the burn mechanism.
- **Value-accrual uncertainty.** Since gas is paid in ETH, LINEA's value depends entirely on the burn/buyback mechanism scaling with usage — an unproven flywheel for a young chain.
- **Liquidity / volatility.** Small-cap microstructure: thin order books, ~$9.7M daily volume, and an extreme-fear macro backdrop amplify drawdowns.

---

## Trading Profile

**Venues & liquidity.** LINEA trades on **both** [[binance]] (LINEA/USDT spot plus a USD-margined perpetual) and [[hyperliquid]] (LINEA-PERP, leverage up to ~40-50x). This dual-venue footprint makes it a deeper, more liquid two-venue market than most sub-$100M-cap alts, but it remains a small-cap name — order books thin out quickly beyond modest clip sizes and 24h volume is modest relative to a low-priced, high-supply token. The presence of a centralized (Binance) and a decentralized-perp (Hyperliquid) venue side by side enables cross-venue execution: you can leg spot on Binance against a Hyperliquid perp, but sizing must respect the thinner of the two books at any moment. Because the token is very low-priced (sub-cent) with a huge circulating count, quote-precision and minimum tick effects matter for scalping and grid work. Check live funding, OI, and L2 depth before sizing any leveraged position.

**Applicable strategies.**
- [[funding-rate-arbitrage]] — a Binance USD-margined perp and a Hyperliquid LINEA-PERP quoting the same underlying let you capture funding differentials between the two venues.
- [[hl-vs-cex-funding-divergence]] — thin small-cap perps like LINEA frequently see Hyperliquid and Binance funding diverge, a directly tradable dislocation across the two available venues.
- [[cash-and-carry]] — Binance spot LINEA hedged against a short perp harvests basis/funding carry while staying delta-neutral on a volatile post-airdrop token.
- [[liquidation-cascade-fade]] — low float and leverage up to ~50x make LINEA prone to stop-run cascades that overshoot, offering mean-reversion entries once the flush exhausts.
- [[breakout-and-retest]] — narrative- and unlock-driven moves in a low-cap L2 token produce clean range breaks; trading the retest filters false breakouts in a thin book.
- [[oi-price-exhaustion]] — with live Hyperliquid OI available, rising open interest into a stalling price flags crowded positioning ripe for a reversal in this reflexive small-cap.

**Volatility & regime character.** LINEA is a **high-beta, small-cap infrastructure/DeFi (zkEVM L2) altcoin** with a pronounced post-airdrop drawdown profile — down ~95% from its September-2025 ATH and trading near all-time lows. It carries strong **ETH beta** (it is an Ethereum-scaling L2 with explicit ETH alignment) layered on top of broad BTC-driven risk-on/risk-off cycles, so it tends to amplify moves in ETH and the wider alt complex. Expect high realized volatility, sharp reflexive swings on thin liquidity, and regime sensitivity to L2-narrative flows and Ethereum sentiment.

**Risk flags.**
- **Liquidity / venue concentration.** Small-cap microstructure means thin books; despite two venues, depth is limited and larger orders slip. Perp OI and funding can swing sharply.
- **Token unlocks / emissions.** Circulating supply is only ~34% of total; ongoing ecosystem and contributor unlocks are a structural supply overhang that can drive sustained selling and gap risk.
- **Narrative dependence.** Value accrual rests on an unproven ETH/LINEA dual-burn flywheel and zkEVM narrative; fee compression and L2 competition can drain the story quickly.
- **Perp funding dislocations.** Thin two-venue perp market is prone to funding spikes and cross-venue divergences — a source of edge but also of squeeze risk for leveraged positions.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=LINEA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=LINEA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=LINEA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=LINEA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=LINEA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[zero-knowledge-proofs]]
- [[consensys]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.

