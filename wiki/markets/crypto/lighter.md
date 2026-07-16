---
title: "Lighter"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, altcoins]
aliases: ["LIT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lighter.xyz/"
related: ["[[crypto-markets]]", "[[decentralized-exchange]]", "[[dydx-chain]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[perp-dex-aggregation]]", "[[perpetual-futures]]", "[[zk-rollup]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Lighter

**Lighter** (LIT) is a high-performance [[decentralized-exchange|DEX]] for [[perpetual-futures|perpetual futures]], built as a [[zk-rollup|zk-rollup]] with verifiable order matching and liquidations. It markets itself as the first exchange to offer *provable* (cryptographically verifiable) order matching and liquidation while delivering CEX-grade latency, settling on [[ethereum|Ethereum]]. The LIT token is the protocol's governance and incentive asset; Lighter is one of the new wave of perp DEXs competing directly with [[hyperliquid|Hyperliquid]] and [[dydx-chain|dYdX]].

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | LIT |
| **Market Cap Rank** | #120 |
| **Market Cap** | $381.64M |
| **Current Price** | $1.53 |
| **24h Change** | -2.51% |
| **7d Change** | -6.11% |
| **24h Volume** | $24.24M |
| **Circulating Supply** | 250.00M LIT |
| **Total / Max Supply** | 1.00B LIT |
| **Fully Diluted Valuation** | ~$1.53B |
| **All-Time High** | $7.86 — now ~-80.5% |
| **All-Time Low** | $0.780945 — now ~+96% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: despite the broad market sitting in **extreme fear** (Fear & Greed = 23) and an **Established Bear Market** regime as of 2026-06-21, LIT holds a relatively high rank (#120) and strong daily turnover (~$24M, ~6% of market cap), reflecting active speculative interest in the perp-DEX narrative. The token is down ~6% on the week but still trades nearly 2x its all-time low.

---

## Technology & Protocol

Lighter's differentiator is **verifiable execution via a ZK architecture**:

- **Provable matching & liquidations** — order matching, cancellation sequencing, and liquidations are executed in a way that can be cryptographically proven on [[ethereum|Ethereum]] via [[zk-rollup|zero-knowledge]] proofs. This addresses the trust gap where users must otherwise rely on an operator's good faith for fair sequencing and liquidation — a recurring concern with off-chain "trusted sequencer" perp venues.
- **CEX-grade latency** — the rollup design targets the speed sophisticated traders expect, while inheriting Ethereum settlement security.
- **MEV resistance** — provable, deterministic sequencing limits the operator's ability to reorder or front-run flow, appealing to market makers and high-frequency participants.
- **Order-book model** — Lighter runs a transparent CLOB rather than an AMM, positioning it alongside [[dydx-chain|dYdX]] and [[hyperliquid|Hyperliquid]] rather than pool-based perp DEXs.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 250.00M LIT |
| **Total Supply** | 1.00B LIT |
| **Max Supply** | 1.00B LIT |
| **Market Cap / FDV** | ~0.25 |

Only **~25% of max supply circulates**, so LIT carries **substantial future dilution / unlock overhang** — its fully-diluted valuation is roughly 4x its current market cap (**~$1.53B FDV vs ~$382M cap**). This **low float / high FDV** structure is a key trading consideration: token unlocks and emissions can pressure price even if protocol fundamentals improve. It contrasts sharply with incumbents like dYdX (~84% float), making LIT far more exposed to vesting cliffs.

---

## Market Structure & Derivatives

**Spot venues (CEX):** LIT trades on Bitget, KuCoin, Crypto.com Exchange, and other centralized exchanges, mostly against USDT/USD.

**On-chain spot:** Available on Uniswap V3 (Ethereum) against WETH.

**The protocol's own venue:** Lighter is itself a perp DEX. Its differentiator is **verifiable matching** — order matching and liquidations are executed in a way that can be cryptographically proven (ZK), addressing the trust gap where users must otherwise rely on an operator's good faith for sequencing and liquidation fairness. This targets sophisticated traders who care about MEV resistance and provable fair execution, similar in spirit to a transparent CLOB.

**Derivatives on LIT itself:** LIT is listed as a perpetual on [[hyperliquid|Hyperliquid]] (LIT-PERP). Given the low circulating float and high FDV, the LIT perp can see pronounced [[funding-rate|funding-rate]] swings and open-interest spikes — speculative longs/shorts around unlock events and listing momentum make funding a useful sentiment signal. Thin float means the perp is sensitive to liquidation cascades on sharp moves.

---

## Use Case / Narrative / Category

Lighter is part of the **next-generation perp-DEX** cohort betting that decentralized derivatives volume keeps migrating on-chain. Its narrative leans on **technical credibility** — verifiable matching/liquidations and CEX-level performance — to differentiate from AMM-based and operator-trusted competitors. The bull case is capturing perp volume from CEXs and incumbents; the token thesis depends on fee capture and incentive design accruing value to LIT holders. It is a frequently-cited name in [[perp-dex-aggregation|perp-DEX]] discussions alongside Hyperliquid and dYdX.

---

## Valuation Framing (qualitative)

LIT's ~$382M market cap masks a **~$1.53B fully-diluted valuation** — the single most important number for the token. At ~25% float, the market is effectively pricing four future LIT for every one circulating, so even strong protocol growth can be offset by unlock-driven supply. On a relative basis LIT is *richer* than dYdX (which has a real USDC fee link and much higher float at a smaller cap), so a buyer is paying up for the ZK-verifiable-execution narrative and momentum. The valuation case rests on Lighter winning durable perp volume and translating fees into token value before vesting dilutes holders.

---

## Peer Comparison

| Token | Architecture | MC Rank | Market Cap | MC/FDV | Edge / Risk |
|---|---|---|---|---|---|
| **Lighter (LIT)** | ZK-rollup, verifiable matching | #120 | ~$382M | **~0.25** | Provable execution; heavy unlock overhang |
| [[hyperliquid\|Hyperliquid (HYPE)]] | Own L1 order book | top-tier | multi-$B | high | Volume leader; deep liquidity |
| [[dydx-chain\|dYdX (DYDX)]] | Cosmos appchain CLOB | #268 | ~$101M | ~0.84 | USDC fee link; high float |
| GMX | Oracle/AMM perps | mid-cap | $100Ms | high | Pool-backed, no order book |

---

## Notable History

- A relatively new entrant; the LIT token reached an all-time high around **$7.86** before retracing ~80% through the 2026 bear market.
- Positioned alongside Hyperliquid and dYdX in the competitive perp-DEX landscape, emphasizing ZK-verifiable execution.
- Currently trades ~96% above its all-time low (~$0.78), having found a floor in the recent drawdown.

---

## Risks

- **Dilution overhang:** With only ~25% of supply circulating, scheduled unlocks/emissions are a persistent downside risk; FDV is ~4x market cap.
- **Intense competition:** The perp-DEX space is crowded (Hyperliquid, dYdX, GMX, others); winning durable volume share is uncertain.
- **Bear-market beta:** As a higher-volatility DeFi token, LIT is highly exposed to the current extreme-fear / Established Bear Market backdrop.
- **Unproven longevity:** As a newer protocol, it lacks the multi-cycle track record of older DeFi names; smart-contract and operational risks are elevated.
- **Token value capture:** Like many DEX governance tokens, value accrual to LIT holders is not guaranteed even if the protocol succeeds.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[hyperliquid]]
- [[dydx-chain]]
- [[perpetual-futures]]
- [[perp-dex-aggregation]]
- [[funding-rate]]
- [[decentralized-exchange]]
- [[zk-rollup]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Trading Profile

**Venues & liquidity** — LIT is tradable as a perpetual on [[hyperliquid|Hyperliquid]] (LIT-PERP, leverage up to ~40-50x) but is **not listed on Binance**; spot access is limited to smaller/offshore CEXs and on-chain DEXs. This makes LIT a **PERP-FIRST asset**: directional and speculative flow concentrates on the HL perp, so that book is the reference venue for price discovery. Depth is thinner than for Binance-listed majors, so large orders move the mark and should be worked in slices rather than taken at market. The absence of a deep, Binance-anchored spot book means there is no easy CEX hedge leg — cash-and-carry/basis structures must be built against on-chain or offshore spot, and position sizing should assume slippage and gap risk are higher than for large caps.

**Applicable strategies**
- [[funding-rate-harvest]] — low-float, high-FDV LIT perp can run persistently skewed funding around unlock/listing hype; harvesting the crowded side collects carry.
- [[crowded-long-funding-fade]] — momentum longs into perp-DEX narrative pumps push funding richly positive; fading the crowd captures the mean-reversion when hype cools.
- [[hl-vs-cex-funding-divergence]] — because HL is the dominant perp venue and offshore CEX listings are thin, funding can diverge sharply across books, creating a relative-value edge.
- [[liquidation-cascade-fade]] — thin circulating float makes the HL perp prone to liquidation cascades on sharp moves; fading capitulation wicks targets the overshoot.
- [[oi-price-exhaustion]] — open-interest spikes around unlock events and listing momentum flag late, crowded positioning that often precedes exhaustion reversals.
- [[token-unlock-supply-event]] — only ~25% of max supply circulates, so scheduled vesting cliffs are a recurring, tradable supply-side catalyst for LIT.

**Volatility & regime character** — LIT is a **high-beta DeFi / perp-DEX infrastructure token** with elevated realized volatility driven by low float, high FDV, and narrative sensitivity. It behaves as a risk-on altcoin: it amplifies BTC/ETH beta in both directions, tending to underperform in risk-off/bear regimes (as in the current extreme-fear backdrop) and to overshoot on the upside when perp-DEX narrative flows return. Correlation to majors is high in stress but decouples on idiosyncratic catalysts (protocol news, unlocks, listing momentum).

**Risk flags**
- **Venue concentration** — no Binance listing; perp flow concentrated on Hyperliquid, so an HL outage, parameter change, or liquidity shift disproportionately affects execution.
- **Unlock / emission overhang** — ~25% float with FDV ~4x market cap; vesting cliffs and emissions can pressure price regardless of protocol traction.
- **Narrative dependence** — value thesis rests on the perp-DEX story and fee capture; sentiment shifts (competition from Hyperliquid, dYdX, GMX) can compress the multiple quickly.
- **Perp funding dislocations** — thin float and speculative positioning produce pronounced funding swings and cascade risk; crowded funding can flip violently around catalysts.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=LIT` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=LIT` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=LIT&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=LIT&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=LIT"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
