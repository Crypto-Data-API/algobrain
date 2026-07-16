---
title: "Cetus Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, liquidity, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["CETUS", "Cetus CLMM", "Cetus DEX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.cetus.zone/"
related: ["[[2026-exploit-target-watchlist]]", "[[ai-amplified-exploit-arbitrage]]", "[[binance]]", "[[crypto-markets]]", "[[funding-rate]]", "[[governance-restitution-arbitrage]]", "[[liquidation-cascade-fade]]", "[[move-clmm-vulnerability-class]]", "[[orca]]", "[[perpetual-futures]]", "[[raydium]]", "[[uniswap]]"]
---

# Cetus Protocol

**Cetus Protocol** (ticker **CETUS**) is the pioneer [[dex|DEX]] and concentrated-liquidity protocol built on the [[sui|Sui]] blockchain (with a deployment on Aptos), the two leading Move-language L1s. Its mission is to build a flexible underlying liquidity network that makes trading easier for any user and asset; it is to Sui roughly what [[raydium]] and [[orca]] are to [[solana|Solana]]. Cetus is best known both as Sui's primary liquidity venue and as the subject of one of 2025's largest DeFi exploits (~$223M, May 2025), from which it fully relaunched.

> **Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).**
>
> | Metric | Value |
> |---|---|
> | **Price** | $0.0181 |
> | **Market cap** | $17.11M (rank **#891**) |
> | **24h volume** | $1.61M |
> | **24h change** | +0.37% |
> | **7d change** | -0.58% |
> | **Circulating supply** | 947.83M CETUS (94.8% of max) |
> | **Total / max supply** | 1.00B CETUS |
> | **Fully diluted valuation** | $18.05M |
> | **All-time high** | $0.4877 (2024-11-10) — now **-96.3%** |
> | **All-time low** | $0.0143 (2026-02-06) — now **+26.3%** |
>
> *Macro backdrop: Crypto Fear & Greed Index 23 ("Established Bear Market"). CETUS is a thin micro-cap ($17M cap, $1.6M daily volume — ~9% turnover) and a high-beta derivative of [[sui|SUI]]; in a bear regime it carries amplified downside and real liquidity risk on size. Near-full circulation (~94.8%) limits dilution overhang. Figures are point-in-time and will drift.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CETUS |
| **Market Cap Rank** | #891 |
| **Market Cap** | $17.11M |
| **Current Price** | $0.0181 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Sui Ecosystem, Animoca Brands Portfolio, OKX Ventures Portfolio, Dex Aggregator |
| **Website** | [https://www.cetus.zone/](https://www.cetus.zone/) |

---

## Overview

Cetus is a pioneer DEX and concentrated liquidity protocol built on the Sui and Aptos blockchain. The mission of Cetus is building a powerful and flexible underlying liquidity network to make trading easier for any users and assets. It focuses on delivering the best trading experience and superior liquidity efficiency to DeFi users through the process of building its concentrated liquidity protocol and a series of affiliate interoperable functional modules.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 947.83M CETUS |
| **Total Supply** | 1.00B CETUS |
| **Max Supply** | 1.00B CETUS |
| **Fully Diluted Valuation** | $18.05M |
| **Market Cap / FDV Ratio** | 0.95 |

> **Dilution note:** ~94.8% of the 1B max supply is circulating (MC/FDV ~0.95), so dilution overhang is small — a genuine positive. The main caveat is the post-exploit restitution: shortfalls are being repaid to affected LPs in CETUS over a 12-month linear unlock, a modest source of incremental sell pressure layered on top of normal emissions.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4877 (2024-11-10) |
| **Current vs ATH** | -96.30% |
| **All-Time Low** | $0.0143 (2026-02-06) |
| **Current vs ATL** | +26.27% |
| **24h Change** | +0.37% |
| **7d Change** | -0.58% |

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0x06864a6f921804860930db6ddbe2e16acdf8504495ea7481637a1c8b9a8fe54b::cetus::CETUS` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CETUS/USDT | N/A |
| Bitget | CETUS/USDT | N/A |
| KuCoin | CETUS/USDT | N/A |
| Crypto.com Exchange | CETUS/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.cetus.zone/](https://www.cetus.zone/) |
| **Twitter** | [@cetusprotocol](https://twitter.com/cetusprotocol) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.61M |
| **Market Cap Rank** | #891 |
| **Volume / Market Cap** | ~9.4% daily turnover (thin) |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-06-20 |

---

## Concentrated Liquidity Market Maker (CLMM)

Cetus's core product is its **CLMM** -- Concentrated Liquidity Market Maker -- which is the Sui/Aptos equivalent of [[uniswap|Uniswap V3's]] concentrated liquidity model. This is the same design pattern implemented by [[raydium]] and [[orca]] on [[solana]].

### How Cetus CLMM Works

| Concept | Detail |
|---|---|
| **Price ranges** | LPs select a min and max price for their position, concentrating capital where it earns fees |
| **Tick spacing** | Cetus divides price space into discrete ticks; LPs choose a range of ticks |
| **Capital efficiency** | A narrow range provides 10-100x more capital efficiency than a full-range AMM |
| **Fee tiers** | Multiple fee tiers per pair (e.g., 0.01%, 0.05%, 0.25%, 1%) for different volatility profiles |
| **Position NFTs** | Each LP position is represented as an NFT, enabling composability and secondary markets |

### Comparison to Uniswap V3

| Feature | [[uniswap|Uniswap V3]] (Ethereum) | Cetus (Sui/Aptos) |
|---|---|---|
| **Chain** | Ethereum, L2s | Sui, Aptos (Move-based chains) |
| **Gas costs** | $2-20+ per transaction | Sub-cent on Sui |
| **Finality** | ~12 seconds (Ethereum) | Sub-second on Sui |
| **Liquidity depth** | Very deep (largest DeFi protocol) | Growing but much thinner |
| **Token pairs** | Thousands | Hundreds |
| **Smart contract language** | Solidity (EVM) | Move |

Cetus's advantage is operating on Sui's high-throughput, low-fee environment, which makes frequent LP rebalancing and small-size swaps economically viable in ways they are not on Ethereum mainnet.

---

## Sui Blockchain Ecosystem Position

Cetus is the **primary DEX and liquidity protocol on Sui**, analogous to the role [[raydium]] and [[orca]] play on [[solana]]. As the Sui ecosystem grows, Cetus captures a proportional share of all trading volume.

### Sui vs Other L1 Ecosystems

- **Sui** uses the Move programming language and an object-centric data model, enabling parallel transaction execution
- **DeFi on Sui** is earlier-stage than Solana or Ethereum, meaning Cetus has less competition but also less total volume
- Cetus also deployed on **Aptos** (another Move-based chain), giving it a multi-chain presence within the Move ecosystem

---

## LP Strategies on Cetus

### Stable Pair LP

Provide concentrated liquidity for correlated pairs (e.g., USDC/USDT on Sui). Minimal [[impermanent-loss]], consistent fee income. The 0.01% fee tier is appropriate for stables.

### Blue-Chip LP

Provide liquidity for SUI/USDC or other major pairs. Use a medium-width range (e.g., +/-20% from current price) to capture fees while managing IL. The 0.25% fee tier balances volume and fee income.

### New Token Launch LP

Sui ecosystem token launches often create initial liquidity on Cetus. Early LP positions can earn very high fees from initial trading frenzy, but the asset may dump 90%+, causing catastrophic IL. Only suitable for very small allocations.

---

## CETUS Token Trading Analysis

### What Drives CETUS Price

1. **Sui ecosystem growth** -- CETUS is the primary beneficiary of increasing DeFi activity on Sui
2. **TVL growth** -- more liquidity on Cetus = more fee revenue = more protocol value
3. **SUI token price** -- CETUS is a high-beta derivative of SUI's performance; when SUI pumps, Sui DeFi tokens follow
4. **Cross-chain expansion** -- Aptos deployment provides additional growth vector
5. **Near full circulation** -- 922.46M of 1B supply circulating (92.2%), meaning low dilution risk

### Trading Characteristics (Extended)

- **Micro-cap:** $17.18M market cap makes CETUS highly volatile and susceptible to large % moves on small capital
- **Sui beta:** CETUS amplifies SUI price movements, often 2-3x
- **Volume:** $2.77M daily -- thin liquidity; large orders will move price significantly
- **Drawdown:** -96.19% from ATH; high-risk, high-reward profile
- **Near full supply:** 92.2% circulating is an advantage -- minimal sell pressure from token unlocks

### Risk Factors

- **Sui ecosystem risk:** If Sui fails to attract developers and users, Cetus has no alternative ecosystem
- **Small TVL:** Lower TVL means less fee revenue and greater vulnerability to liquidity migration
- **Competition on Sui:** Turbos Finance and other Sui DEXes compete for market share
- **Smart contract risk:** Move is a newer language with less battle-tested tooling than Solidity — Cetus's own ~$223M exploit (May 2025) is the canonical case study for the [[move-clmm-vulnerability-class|Move CLMM vulnerability class]]
- **Low liquidity:** The token itself trades thinly, making entries and exits challenging at size

---

## Market Structure & Derivatives

- **CEX spot:** Listed on Binance, Bitget, KuCoin and Crypto.com, mostly CETUS/USDT — a respectable CEX footprint for a sub-$20M token, reflecting Cetus's status as Sui's flagship DEX and its Animoca/OKX Ventures backing.
- **DEX spot:** Native liquidity is on Sui (and Aptos) within Cetus's own CLMM pools; SUI/CETUS and SUI/USDC are the reference pairs. As the primary venue on Sui, Cetus is also a DEX aggregator, routing across Sui liquidity.
- **24h volume:** ~$1.61M against a ~$17M cap — thin. Order books and pools are shallow; large orders cause material slippage on both CEX and DEX.
- **Derivatives:** No significant CETUS perp/futures market in the snapshot venues. CETUS exposure is essentially spot-only, so there is limited ability to hedge or express short views with leverage — a liquidity/risk consideration for any position.
- **Post-exploit liquidity:** Following the May 2025 hack and June 2025 relaunch, restored pools sit at 85-99% of pre-hack depth; liquidity has largely recovered but the episode left a lasting risk premium on the token.

## Valuation Framing (Qualitative)

CETUS is a **Sui-DEX-fee token** and should be framed against protocol economics, discounted heavily for security and ecosystem risk:

1. **Sui ecosystem TVL & volume** — CETUS is a levered claim on total Sui on-chain trading. The numerator of the thesis is Sui DeFi adoption; if Sui's TVL and DEX volume grow, Cetus captures a proportional share of fees.
2. **Fee revenue vs cap** — at ~$17M cap, the question is whether Cetus's fee run-rate justifies the valuation relative to peers like [[raydium]]/[[orca]] on a fees-to-market-cap basis (Sui is much earlier-stage, so absolute fees are far smaller).
3. **Security discount** — the ~$223M exploit means CETUS should trade at a persistent risk discount versus an un-hacked peer; the bull case requires the market to re-rate Cetus's post-relaunch hardening as credible.
4. **SUI beta** — CETUS amplifies [[sui|SUI]] moves (often 2-3x); much of its price action is simply leveraged SUI exposure rather than idiosyncratic value.

Net: a high-risk, high-beta bet on the Sui DeFi ecosystem with an embedded security-event discount; size as a speculative micro-cap, not a core holding.

## CETUS vs CLMM-DEX Peers

| DEX | Token | Chain(s) | Snapshot cap | Notes |
|---|---|---|---|---|
| **Cetus** | CETUS | [[sui\|Sui]], Aptos | ~$17M | Primary Sui DEX; ~$223M exploit (2025), relaunched |
| [[raydium]] | RAY | [[solana\|Solana]] | ~$167M | 50%+ Solana DEX volume; CLMM + launchpad |
| [[orca]] | ORCA | [[solana\|Solana]] | (smaller) | Solana CLMM (Whirlpools) |
| [[uniswap]] | UNI | [[ethereum\|Ethereum]] + L2s | (much larger) | Original CLMM (V3); deepest liquidity |

Cetus occupies the same *structural niche* as Raydium/Orca but on a smaller, earlier ecosystem — more upside if Sui DeFi scales, but far thinner liquidity and an additional, demonstrated smart-contract risk.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **2025-05-22:** Cetus exploit (~$223M) — a flawed `checked_shlw` overflow guard in the protocol's `u256` math library allowed an attacker to open near-zero-cost CLMM positions and drain liquidity pools. Roughly $60-62M was bridged to Ethereum (via Wormhole) before it could be stopped; the remaining ~$162M sat on Sui and was **frozen by coordinated Sui validator action** — a controversial intervention that critics argued undermined Sui's decentralization claims. This is the canonical case study for the [[move-clmm-vulnerability-class|Move-language CLMM vulnerability class]]. (Verified via WebSearch, 2026-06-11)
- **2025-05-28:** A community governance vote (and the Sui Foundation) committed to **fully compensating affected users**. The Sui Foundation extended a **~$30M loan** to Cetus to bridge the gap between recovered funds and total losses. (Verified via WebSearch, 2026-06-11)
- **2025-06-08:** **Cetus relaunched** its protocol just ~17 days after the exploit, restoring affected liquidity pools to between **85% and 99%** of their pre-hack value. Remaining shortfalls are being repaid to LPs in **CETUS tokens over a 12-month linear unlock**, contingent on any further recoveries from the attacker. The CETUS token had fallen ~44% from its pre-attack price by early June 2025. (Verified via WebSearch, 2026-06-11)
- **As of June 2026:** Cetus is **operating normally** and remains the primary DEX/liquidity protocol on Sui. The exploit, frozen-funds intervention, and full restitution remain a defining episode in DeFi security and chain-governance debates. See [[governance-restitution-arbitrage]] and [[ai-amplified-exploit-arbitrage]] for the strategy angle.

---

## Trading Profile

### Venues & liquidity

CETUS is tradable on [[binance]] — both spot (CETUS/USDT) and a USD-margined [[perpetual-futures|perpetual]], which brings [[funding-rate|funding]], [[open-interest|open interest]] and [[liquidations|liquidation]] data to what the rest of this page describes as an otherwise spot-dominated token. CETUS is **NOT** on [[hyperliquid]]; Binance is effectively the sole primary leveraged venue. That concentration matters: with a thin ~$17M cap and shallow spot depth, the Binance perp is where most price discovery and leveraged flow occur, and there is no deep secondary perp venue to arbitrage against or to absorb liquidations. Practically, execution and sizing should assume shallow order books, wider effective spreads on size, and outsized slippage/liquidation risk — keep clip sizes small, use limit/passive execution, and treat leverage conservatively because a single venue's funding and liquidation dynamics dominate.

### Applicable strategies

- [[funding-rate-harvest]] — the Binance USD-M perp is the only funding-bearing venue for CETUS, so harvesting persistent funding (delta-hedged spot vs perp) is the cleanest carry expression on this thin micro-cap.
- [[crowded-long-funding-fade]] — CETUS is a high-beta SUI derivative prone to reflexive rallies; when perp funding spikes richly positive on a chase, fading crowded longs into elevated funding is a defined edge.
- [[liquidation-cascade-fade]] — shallow single-venue liquidity means Binance liquidation cascades overshoot violently; fading the flush after forced selling exhausts can capture sharp mean-reversion bounces.
- [[oi-confirmed-trend]] — because Binance is the sole OI source, rising open interest alongside price is a relatively clean confirmation signal for trend continuation vs a hollow, liquidation-driven move.
- [[cash-and-carry]] — with spot on Binance and a co-located USD-M perp, positive-basis windows on this exploit-discounted token can be locked as a market-neutral carry trade.
- [[breakout-and-retest]] — as a levered claim on SUI DeFi with a deep ATH drawdown, CETUS trends impulsively; breakout-and-retest structures respect the thin liquidity by demanding confirmation before sizing.

### Volatility & regime character

CETUS is a thin **micro-cap DeFi/infrastructure token** (Sui's flagship CLMM DEX) and a **high-beta derivative of [[sui|SUI]]**, historically amplifying SUI moves ~2-3x. It is not a memecoin but shares memecoin-like reflexivity through low float liquidity and ~9% daily turnover: small capital produces large percentage swings in both directions. Correlation to BTC/ETH is real but secondary — CETUS tracks SUI and the broader Sui-DeFi narrative first, then the majors. In risk-off/bear regimes it carries amplified downside and genuine liquidity risk on size; in risk-on it can decouple upward violently on Sui-ecosystem momentum.

### Risk flags

- **Liquidity & venue concentration:** shallow spot books and a single primary leveraged venue (Binance) mean thin depth, high slippage on size, and no cross-venue perp to hedge or arbitrage — liquidation and funding dynamics are dominated by one exchange.
- **Emissions / restitution overhang:** post-exploit shortfalls are repaid to LPs in CETUS over a 12-month linear unlock, a modest but persistent incremental sell-pressure layer on top of normal emissions (float is already ~94.8%, limiting broader dilution).
- **Narrative dependence:** the token is a levered bet on Sui-DeFi adoption and SUI price; idiosyncratic value is limited, so it lives and dies by ecosystem sentiment and the residual security-event discount from the ~$223M 2025 exploit.
- **Security / event risk:** the demonstrated Move-CLMM exploit leaves a lasting risk premium; renewed security or chain-governance headlines can trigger fast, gap-like repricing that thin liquidity cannot absorb smoothly.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CETUSUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CETUSUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=CETUS` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=CETUS` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CETUSUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CETUSUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=CETUS"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[sui]] -- Cetus's home L1 (Move-based)
- [[dex]] -- decentralized exchange concept
- [[uniswap]] -- concentrated liquidity pioneer
- [[raydium]] -- Solana CLMM for comparison
- [[orca]] -- Solana concentrated liquidity DEX
- [[move-clmm-vulnerability-class]] -- the exploit's vulnerability class

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market-data snapshot, refreshed 2026-06-20
- [CoinDesk: Sui's Cetus DEX is back online after $223M exploit](https://www.coindesk.com/business/2025/06/09/sui-s-cetus-dex-is-back-online-after-usd223m-exploit)
- [CoinDesk: Sui Network steps in to compensate Cetus losses in full](https://www.coindesk.com/markets/2025/05/28/sui-network-steps-in-to-compensate-cetus-losses-in-full-after-223m-exploit)
- [The Block: Cetus restarts platform after recovering from $223M exploit](https://www.theblock.co/post/357386/sui-dex-cetus-protocol-restarts-platform-after-recovering-from-223-million-exploit)
- [Cyfrin: Inside the $223M Cetus exploit — root cause analysis](https://www.cyfrin.io/blog/inside-the-223m-cetus-exploit-root-cause-and-impact-analysis)
- Verified via WebSearch, 2026-06-11
