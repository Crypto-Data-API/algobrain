---
title: "Aave"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins, ethereum, stablecoins]
aliases: ["AAVE", "Aave Protocol", "ETHLend"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized (Aave Labs: London, UK)"
website: "https://aave.com/"
related: ["[[ai-finance]]", "[[arbitrum]]", "[[artificial-intelligence]]", "[[compound-governance-token]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[defai]]", "[[defi]]", "[[ethena]]", "[[ethereum]]", "[[funding-rate]]", "[[gho]]", "[[hyperliquid]]", "[[layer-2]]", "[[ml-defi-risk-models]]", "[[morpho]]", "[[perpetual-futures]]", "[[cross-sectional-relative-value]]", "[[funding-rate-harvest]]", "[[sky]]", "[[stablecoins]]"]
---

# Aave

**Aave** (AAVE) is the largest decentralized lending protocol in [[defi|DeFi]], letting users lend and borrow crypto assets against overcollateralized positions across [[ethereum|Ethereum]] and 10+ other chains. For traders it matters three ways: AAVE is the benchmark "DeFi blue chip" governance token (with a permanent protocol-revenue buyback creating a structural bid), the protocol's ~$12B+ TVL and borrow rates are a key gauge of on-chain leverage and risk appetite, and its [[gho|GHO]] stablecoin and Horizon RWA market anchor the institutional-DeFi narrative. Founded by Stani Kulechov in 2017 as ETHLend, rebranded to Aave in 2018, with the LEND-to-AAVE token migration in October 2020.

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $74.15 |
| **Market Cap** | $1.126B |
| **Market Cap Rank** | #64 |
| **24h Volume** | $107.17M |
| **24h Change** | +2.20% |
| **7d Change** | +11.86% |
| **Circulating Supply** | 15.18M AAVE |
| **Total / Max Supply** | 16.00M / 16.00M AAVE |
| **Fully Diluted Valuation** | $1.187B |
| **MC / FDV** | 0.95 |
| **All-Time High** | $661.69 (2021-05-18) — now ~-88.8% |
| **All-Time Low** | $26.02 (2020-11-05) — now ~+185% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

AAVE is showing relative strength versus the broad tape: the +11.9% week stands out against a market in **extreme fear** (crypto Fear & Greed Index = 23) and a long-horizon "Established Bear Market" regime. The near-1.0 MC/FDV ratio means there is essentially no hidden dilution overhang — almost all supply is liquid and circulating, a rare property among large-cap tokens (contrast [[arbitrum|ARB]] at 0.64 or [[ethena|ENA]] at 0.62).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AAVE |
| **Market Cap** | $1.126B, rank #64 (2026-06-20) |
| **Protocol TVL** | ~$12.4B — as of June 2026 (approximate) |
| **Sector** | DeFi lending/borrowing (category leader by TVL) |
| **Supply mechanics** | 15.18M circulating / 16M max; supply shrinking via DAO buybacks |
| **Native chain** | [[ethereum|Ethereum]], deployed on 10+ chains ([[arbitrum|Arbitrum]], Base, Optimism, [[polygon|Polygon]], Avalanche, BNB Chain, etc.) |
| **Stablecoin** | [[gho|GHO]] — native overcollateralized stablecoin, ~$500M supply (end-2025) |
| **Website** | [https://aave.com/](https://aave.com/) |

---

## Overview

Aave is a decentralized money market protocol where users can lend and borrow cryptocurrency across dozens of assets used as collateral. Lenders earn interest by providing liquidity to the market, while borrowers collateralize cryptoassets to take out loans from the liquidity pools. The AAVE token governs the protocol through the Aave DAO and acts as a backstop via the Safety Module.

Aave pioneered flash loans (uncollateralized loans repaid within one transaction) and has been the reference implementation for DeFi lending since v2 (2020). Aave v3 (2022) added cross-chain "Portals", isolation mode, and high-efficiency eMode. **Aave v4 launched on mainnet on 30 March 2026**, replacing per-chain monolithic pools with a modular hub-and-spoke system: a central liquidity hub per network with specialized "spoke" markets that borrow from it, improving capital efficiency and risk isolation.

---

## Protocol & Technology

Aave is an *overcollateralized* money market: every borrow must be backed by collateral worth more than the loan. Interest rates are algorithmic, set by per-asset utilization curves (the higher the share of a pool that is borrowed, the higher the rate, with a "kink" past which rates spike to defend liquidity).

### Core mechanics

| Mechanism | What it does | Trading relevance |
|---|---|---|
| **aTokens** | Interest-bearing receipt tokens (e.g., aUSDC) minted 1:1 on deposit; rebase up as interest accrues | Composable yield primitive used across [[defi|DeFi]] |
| **Health Factor (HF)** | Ratio of (collateral × liquidation threshold) to debt; HF < 1 triggers liquidation | Aggregate HF distribution is a leverage/liquidation-cascade gauge ([[ml-defi-risk-models]]) |
| **Liquidations** | Bots repay unhealthy debt for a liquidation bonus (5–15%) | A core on-chain MEV and deleveraging mechanism |
| **Flash loans** | Uncollateralized loans repaid within one transaction | Enables arbitrage, collateral swaps, self-liquidation; a building block for [[decentralized-exchange|DEX]] arb |
| **Isolation mode** | New/risky collateral can only back stablecoin borrows up to a debt ceiling | Limits contagion from long-tail asset listings |
| **eMode (high-efficiency)** | Correlated assets (e.g., ETH/stETH, USD stables) get up to ~93% LTV | Powers leveraged staking / [[restaking]] loops |

### Version roadmap

- **v2 (2020)** — reference implementation; introduced flash loans, rate switching, and the Safety Module.
- **v3 (2022)** — cross-chain *Portals*, isolation mode, eMode, supply/borrow caps, and gas optimization; multi-chain deployment to 10+ networks.
- **v4 (mainnet 30 March 2026)** — *hub-and-spoke* architecture. Each network has a central **Liquidity Hub** that aggregates supply, with specialized **spoke** markets (RWA, isolated risk, premium) borrowing from it. Goals: unified liquidity, finer risk isolation, and a "Unified Liquidity Layer" for cross-spoke capital efficiency.

### GHO and Safety Module

[[gho|GHO]] is Aave's native, overcollateralized, DAO-governed stablecoin: borrowers mint GHO against Aave collateral and pay a stability fee that flows directly to the DAO treasury (100% protocol-captured, unlike pooled lending spreads). Savings GHO (sGHO, July 2025) pays native yield from protocol revenue with no lockup. The **Safety Module** (staked AAVE / stkGHO / GHO-stkBPT) is the protocol's backstop of last resort — stakers earn rewards but can be slashed up to ~30% to cover shortfall events, aligning the AAVE token with protocol solvency.

---

## 2025–2026 Developments

- **Aavenomics buybacks (2025)** — The DAO approved a buyback program in 2025; the pilot retired more than 94,000 AAVE, and governance subsequently locked in a **permanent $50M/year buyback budget** funded from protocol revenues, with weekly purchases of ~$250K–$1.75M. This is a structural, price-insensitive bid on the token.
- **GHO breakout (2025)** — GHO supply grew to ~$500M, generating $14M+ annualized DAO revenue. Savings GHO (sGHO) launched July 2025, paying native yield from protocol revenue with no lockups.
- **Aave Horizon (August 2025)** — institutional RWA lending market launched with VanEck, Circle, Securitize, [[xrp|Ripple]], WisdomTree, Superstate, Centrifuge, Hamilton Lane, [[ethena|Ethena]] and others; became the largest RWA-backed lending market in DeFi, ending 2025 with **$570M+ deposits**.
- **Aave v4 mainnet (30 March 2026)** — hub-and-spoke architecture live.
- **UK FCA approval (2026)** — Aave Labs subsidiaries (Push Labs Limited, Push Virtual Assets Limited) registered as cryptoasset exchange providers in the UK.
- AAVE is also held in the [[world-liberty-financial|World Liberty Financial]] portfolio, which has periodically driven headline flow.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 15.18M AAVE |
| **Total Supply** | 16.00M AAVE |
| **Max Supply** | 16.00M AAVE (hard cap) |
| **Fully Diluted Valuation** | $1.187B |
| **Market Cap / FDV Ratio** | 0.95 |

AAVE has a **fixed 16M hard cap** — no inflation schedule. The only structural supply changes are (1) the small remaining gap between circulating and total supply (ecosystem reserve / Safety Module incentives), and (2) the DAO buyback program, which *retires* tokens. This makes AAVE one of the few large-cap tokens with **net-deflationary float dynamics funded by real fee revenue**.

- **Aavenomics buybacks** — a permanent **$50M/year buyback budget** funded from protocol revenue, with weekly purchases of ~$250K–$1.75M. The 2025 pilot retired 94,000+ AAVE. This is a structural, price-insensitive bid.
- **No unlock cliffs** — unlike [[arbitrum|ARB]], [[ethena|ENA]] or other recent-vintage tokens, AAVE carries no large team/investor unlock overhang (token has been fully distributed since the 2020 LEND migration). The ~0.95 MC/FDV reflects this.
- **Dilution flag**: minimal. The buyback turns positive net protocol revenue into supply reduction; the main risk to the deflation thesis is a fee/revenue downturn (e.g., a sharp DeFi TVL contraction) that forces the DAO to pause buybacks.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $74.15 |
| **All-Time High** | $661.69 (2021-05-18) — now ~-88.8% |
| **All-Time Low** | $26.02 (2020-11-05) — now ~+185% |
| **7d Change** | +11.86% (outperforming a Fear & Greed = 23 tape) |

---

## Trading Relevance

- **Where it trades**: deep spot liquidity on [[binance|Binance]] (AAVE/USDT), [[kraken|Kraken]], Coinbase, Upbit, Bitget, KuCoin; perps on [[hyperliquid|Hyperliquid]] (AAVE-PERP), Binance Futures and most major perp venues. DEX liquidity on Uniswap v3 and Balancer.
- **Narrative basket**: the core "DeFi blue chip" / "DeFi fundamentals" basket alongside [[sky|Sky/Maker]], Uniswap, Lido — the basket that benefits when rotation favors revenue-generating protocols over memecoins.
- **Catalysts to watch**: weekly buyback flow, GHO/sGHO supply growth, Horizon RWA deposits, v4 spoke launches, any fee-switch expansion, US/UK regulatory milestones.
- **As a market signal**: Aave borrow rates and utilization are a real-time read on on-chain leverage; spiking stablecoin borrow APYs historically precede deleveraging cascades and liquidation runs (relevant to [[ml-defi-risk-models]]).

### Platform & Chain Information (April 2026 snapshot)

**Native Chain:** Ethereum (`0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9`), with bridged deployments on Base, [[polygon|Polygon PoS]], BNB Chain, [[arbitrum|Arbitrum One]], Optimism, Avalanche, Fantom, Harmony, NEAR, Energi, Sora and Hydration.

---

## Ecosystem & Use Cases

- **Money market / leverage** — the dominant use: deposit collateral, borrow stablecoins or volatile assets. Power users build leverage loops (deposit ETH → borrow stable → buy ETH → re-deposit) and basis/carry trades.
- **GHO ecosystem** — minting/borrowing GHO, sGHO savings, and GHO liquidity across [[decentralized-exchange|DEXs]]; GHO is increasingly used as collateral elsewhere in DeFi.
- **Aave Horizon (RWA)** — institutional tokenized-asset lending market (launched Aug 2025) with VanEck, Circle, Securitize, [[xrp|Ripple]], WisdomTree, Superstate, Centrifuge, Hamilton Lane and [[ethena|Ethena]]; ended 2025 with $570M+ deposits, the largest RWA-backed lending market in DeFi.
- **Flash-loan infrastructure** — collateral swaps, debt refinancing, self-liquidation, and [[decentralized-exchange|DEX]] arbitrage rely on Aave flash loans.
- **Composability** — aTokens and GHO are reused as collateral and yield primitives across the [[defi|DeFi]] stack, including [[restaking]] and looping strategies.

---

## Market Structure & Derivatives

- **Spot venues** — deep liquidity on [[binance|Binance]] (AAVE/USDT), [[kraken|Kraken]], Coinbase, Upbit, Bitget, KuCoin; on-chain on Uniswap v3 and Balancer. 24h spot volume ~$107M (2026-06-20).
- **Perpetuals** — AAVE-PERP on [[hyperliquid|Hyperliquid]], Binance Futures, Bybit, OKX and most major perp venues; AAVE is a liquid mid-cap perp with two-sided depth.
- **Funding / OI** — AAVE perp funding tends to flip positive (longs pay) during DeFi-narrative rallies like the current +11.9% week; persistently rich funding plus a flat spot price is a classic over-crowded-long warning. Open interest concentration on a single venue is a squeeze risk in both directions.
- **Borrow-rate signal** — independent of the token, Aave's own *stablecoin borrow APYs and utilization* are a real-time read on on-chain leverage; spiking borrow rates historically precede deleveraging/liquidation cascades (see [[ml-defi-risk-models]]).

---

## Valuation Framework

Because AAVE captures real revenue and burns supply, it is one of the few crypto tokens amenable to cash-flow-style analysis. Metrics to track (describe, do not invent point values):

- **Protocol revenue** — net interest spread (borrow minus supply rates) plus GHO stability fees plus liquidation income. A portion is routed to buybacks.
- **TVL** — total value supplied/borrowed; the denominator for fee generation. Track via DefiLlama. AAVE's TVL leadership (~$12B+) is the core fundamental.
- **P/F and P/S** — price-to-fees and price-to-sales versus peers ([[compound-governance-token|Compound]], [[morpho|Morpho]], [[sky|Sky]]). AAVE typically trades at a premium for liquidity, brand, and the buyback.
- **Buyback yield** — annual buyback budget ($50M) divided by market cap; an effective "shareholder yield" floor on the token.
- **GHO supply growth** — incremental, 100%-captured revenue; a high-margin growth lever distinct from pooled lending.

---

## Trading Playbook

- **Fundamentals dashboard** — track Aave TVL, GHO/sGHO supply, utilization/borrow rates, weekly buyback execution, and Horizon RWA deposits. These are the high-frequency signals that lead the token.
- **Macro context** — in the current **extreme-fear / Established Bear Market** regime (F&G = 23), DeFi blue chips with real cash flows tend to be relative-strength leaders on bounces — AAVE's +11.9% week fits that pattern. But beta is still high: a broad risk-off leg drags AAVE with it.
- **Relative-value** — AAVE/ETH and AAVE vs the DeFi basket ([[sky|SKY]], [[uniswap|UNI]], [[ethena|ENA]]) are standard rotation pairs; AAVE vs [[compound-governance-token|COMP]]/[[morpho|MORPHO]] is the intra-lending pair trade.
- **Catalysts** — weekly buyback flow, GHO/sGHO growth, Horizon deposits, v4 spoke launches, fee-switch expansion, and US/UK regulatory milestones.
- **Risk discipline** — size for high volatility; AAVE drops with the lending-market deleveraging it helps measure. Watch its own borrow rates as an early-warning indicator.

---

## History

- **2017** — launched as **ETHLend** (LEND token) by Stani Kulechov: a peer-to-peer lending marketplace.
- **2018** — rebranded to **Aave** ("ghost" in Finnish), pivoting to pooled liquidity money markets.
- **Jan 2020** — Aave v1 mainnet; introduces aTokens and flash loans.
- **Oct 2020** — LEND→AAVE migration (100 LEND : 1 AAVE) and the Safety Module launch.
- **Dec 2020** — Aave v2.
- **2022** — Aave v3 (cross-chain, isolation mode, eMode); multi-chain expansion.
- **2023** — GHO stablecoin launch.
- **2025** — Aavenomics buybacks, sGHO, and Aave Horizon (RWA); GHO supply ~$500M.
- **30 March 2026** — Aave v4 mainnet (hub-and-spoke).
- **2026** — UK FCA registration of Aave Labs subsidiaries; permanent $50M/yr buyback in force.

---

## Competitive Positioning

| Protocol | Token | Niche | Differentiator vs Aave |
|---|---|---|---|
| **Aave** | AAVE | DeFi lending leader by TVL (~$12B+) | Liquidity, brand, GHO, buyback, hard-capped supply |
| [[compound-governance-token\|Compound]] | COMP | The original pooled lending protocol | Smaller TVL; simpler/older design; less multi-chain reach |
| [[morpho\|Morpho]] | MORPHO | Modular/peer-matched lending + isolated vaults | More capital-efficient matching; curator-driven risk; newer |
| [[sky\|Sky]] (ex-Maker) | SKY | Stablecoin issuer (USDS) + buyback | Issuer model vs money market; overlaps via GHO competition |
| [[ethena\|Ethena]] | ENA | Synthetic-dollar (USDe) yield via basis trade | Funding-rate yield vs lending spread; partners on Horizon |

Aave's moat is liquidity depth and the network effect of being the default DeFi money market; the live competitive frontier is **Morpho's** more efficient isolated-vault model and **Sky's** rival stablecoin (USDS vs GHO).

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://aave.com/](https://aave.com/) |
| **Twitter** | [@aave](https://twitter.com/aave) |
| **Reddit** | [https://www.reddit.com/r/Aave_Official](https://www.reddit.com/r/Aave_Official) |
| **Discord** | [https://aave.com/discord](https://aave.com/discord) |
| **GitHub** | [https://github.com/aave/aave-protocol](https://github.com/aave/aave-protocol) |
| **Whitepaper** | [Aave Protocol Whitepaper v1.0](https://github.com/aave/aave-protocol/blob/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf) |

---

## Risks

- **Smart-contract / oracle risk** — a money market holding ~$12B is a prime exploit target; a faulty price oracle can cause bad-debt or wrongful liquidations.
- **Bad debt / Safety Module slashing** — extreme volatility or illiquid collateral can leave under-collateralized positions; the Safety Module (staked AAVE) is slashable to cover shortfalls, directly impairing the token.
- **GHO depeg** — as an overcollateralized stablecoin, GHO can trade off-peg under stress, denting protocol revenue and confidence.
- **Liquidation cascades** — sharp drawdowns trigger forced liquidations on Aave itself, amplifying market moves and dragging the token (the same dynamic AAVE's borrow rates *measure*).
- **Revenue cyclicality** — fees scale with DeFi activity; a deep bear market (the current **Established Bear Market** regime) compresses spreads and could force the DAO to slow buybacks, weakening the deflation thesis.
- **Competition** — [[morpho|Morpho]]'s efficiency and [[sky|Sky]]'s/[[ethena|Ethena]]'s stablecoins erode share.
- **Regulatory** — yield-bearing DeFi products and stablecoins (GHO) face evolving US/EU/UK regimes; the UK FCA registration is a positive but the landscape remains uncertain.

---

## Related

- [[defi]]
- [[gho]]
- [[ethereum]]
- [[crypto-markets]]
- [[stablecoins]]
- [[stablecoin-yields]]
- [[decentralized-exchange]]
- [[layer-2]]
- [[restaking]]
- [[compound-governance-token]] — peer lending protocol
- [[morpho]] — peer lending protocol
- [[ethena]]
- [[sky]]
- [[arbitrum]]
- [[hyperliquid]]
- [[world-liberty-financial]]
- [[ml-defi-risk-models]]

---

## Sources

- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko): price $74.15, mcap $1.126B, rank #64, vol $107.17M, 24h +2.20%, 7d +11.86%, MC/FDV 0.95.
- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- [Aave 2025 Year in Review — aave.com](https://aave.com/blog/aave-2025-recap)
- [Aave Horizon Launches — aave.com](https://aave.com/blog/horizon-launch)
- [CoinGecko — Aave](https://www.coingecko.com/en/coins/aave)
- [CoinMarketCap — Aave](https://coinmarketcap.com/currencies/aave/)
- Perplexity sonar verification, 2026-06-10 (market cap ~$938–960M, TVL ~$12.43B, UK FCA approval)

## Trading Profile

### Venues & liquidity

AAVE trades on **both** [[binance|Binance]] (deep AAVE/USDT spot plus a USD-margined AAVE perpetual) and [[hyperliquid|Hyperliquid]] (AAVE-PERP, up to ~40–50x leverage). This is a genuine two-venue, two-sided market: a top-tier CEX order book for spot/hedging and an on-chain perp with transparent funding and OI. Depth is solid for a mid-cap DeFi blue chip — the ~$100–200M daily volume supports mid-size positions with modest slippage, though it is thinner than BTC/ETH, so large clips should be worked (limit/VWAP) rather than swept. The dual-venue structure enables clean CEX-vs-DEX execution: hedge or leg into positions on Binance while capturing Hyperliquid funding, and it makes spot-vs-perp and cross-venue basis structures practical. Size to the *shallower* book (usually Hyperliquid), and watch single-venue OI concentration, which can amplify squeezes in either direction.

### Applicable strategies

- [[funding-rate-harvest]] — AAVE perp funding flips positive on DeFi-narrative rallies; harvest the carry by holding spot and shorting the richly-funded perp.
- [[hl-vs-cex-funding-divergence]] — funding on Hyperliquid AAVE-PERP and Binance's USD-margined perp can diverge; trade the spread between the two venues.
- [[cash-and-carry]] — AAVE's deep spot on Binance plus a liquid perp makes a clean long-spot / short-perp carry when basis is positive.
- [[crowded-long-funding-fade]] — persistently rich funding with a flat AAVE spot price is the classic over-crowded-long tell to fade.
- [[oi-confirmed-trend]] — AAVE trends (buyback-driven bids, DeFi rotations) are more reliable when rising open interest confirms the move.
- [[cross-sectional-relative-value]] — trade AAVE against the DeFi-lending basket ([[compound-governance-token|COMP]], [[morpho|MORPHO]], [[sky|SKY]]) to isolate relative strength.

### Volatility & regime character

AAVE is a **high-beta DeFi infrastructure / lending token**, not a memecoin — it moves with the DeFi-fundamentals basket and carries strong beta to [[ethereum|ETH]] (and BTC risk-on/off). It tends to lead on relief bounces (real cash flows, buyback bid) but still gets dragged in broad risk-off legs. Its own borrow rates and utilization are a live gauge of on-chain leverage, so AAVE volatility often coincides with system-wide DeFi deleveraging. Expect elevated realized vol versus large caps and regime-dependent correlation that tightens toward ETH in stress.

### Risk flags

- **Venue/OI concentration** — a liquid but mid-cap perp; single-venue open-interest build-ups can drive squeezes and funding dislocations in both directions.
- **Narrative dependence** — price is tied to the DeFi-fundamentals rotation; when flow favors memecoins or majors, AAVE can lag despite strong fundamentals.
- **Perp funding dislocations** — funding can turn sharply rich (or negative) around narrative swings, punishing late crowded positioning.
- **Fundamental / protocol tail risk** — smart-contract, oracle, bad-debt/Safety-Module slashing and [[gho|GHO]] depeg events can gap the token independent of the broad tape.
- **Revenue cyclicality** — a deep DeFi downturn compresses fees and can force the DAO to slow the structural buyback bid.
- **Regulatory** — evolving US/EU/UK rules on yield-bearing DeFi and stablecoins remain a headline-driven overhang.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=AAVE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=AAVE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=AAVE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=AAVE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=AAVE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
