---
title: "Gas"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["GAS", "NEO GAS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://neo.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[neo]]", "[[perpetual-futures]]", "[[proof-of-stake]]", "[[funding-rate]]", "[[open-interest]]", "[[cash-and-carry]]", "[[pairs-trading]]"]
---

# Gas

**Gas** (ticker **GAS**) is the utility/fee token of the **NEO** blockchain. NEO uses a **dual-token model**: [[neo|NEO]] is the governance asset (one indivisible unit per vote, staked to participate in consensus and earn rewards), while **GAS** is the fuel that pays for transactions, smart-contract deployment, and on-chain operations. Holding (and staking) NEO continuously generates GAS, so the two tokens are economically inseparable companions — much as ether is the gas of [[ethereum|Ethereum]], GAS is the gas of NEO.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | GAS |
| **Current Price** | $1.10 |
| **Market Cap** | $71.78M |
| **Market Cap Rank** | #348 |
| **24h Volume** | $2.27M |
| **24h Change** | +2.02% |
| **7d Change** | -1.52% |
| **All-Time High** | $91.94 (2018-01-15) — now ~-98.8% |
| **All-Time Low** | $0.6213 (2020-03-13) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

The snapshot falls in a risk-off market: the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (Extreme Fear)** and the backdrop is an **established bear market**. GAS is modestly higher on the day (+2.02%) and roughly flat-to-down on the week (-1.52%) — relatively resilient versus the rest of this cohort. Turnover (~$2.3M against a ~$71.8M cap, ~3.2% of cap) is reasonable for a legacy mid-cap.

---

## Tokenomics & Supply — the NEO/GAS Dual-Token Model

NEO deliberately separates **governance** from **utility** across two tokens:

- **NEO** — the governance token. It is indivisible (you cannot hold fractions of a NEO), and holding/staking NEO is what *generates* GAS. NEO holders vote for consensus nodes (under NEO's delegated BFT consensus, a Proof-of-Stake-style mechanism where influence scales with NEO held rather than mining power).
- **GAS** — the utility/fee token. It is divisible and is consumed to pay network transaction and smart-contract fees. GAS is distributed to NEO holders (and stakers / voters) as an ongoing reward, on a schedule designed to decay gradually over time.

This separation means a network user can transact (spending GAS) without diluting governance, and a long-term holder can accrue GAS yield simply by holding NEO — analogous to earning "interest" from PoS participation.

| Metric | Value |
|---|---|
| **Circulating Supply** | 65.09M GAS |
| **Total Supply** | 65.09M GAS |
| **Max Supply** | No fixed max (emitted continuously to NEO holders) |
| **Fully Diluted Valuation** | ~$71.6M |
| **Market Cap / FDV** | ~1.00 |

> **Dilution flag:** because circulating ≈ total supply (MC/FDV ~1.00), there is **no large locked-token overhang** — a structural positive versus most tokens in this cohort. However, GAS has **no fixed max supply**: new GAS is emitted indefinitely to NEO holders on a gradually-decaying schedule, so the float grows over time as a perpetual, low-grade inflation rather than as cliff unlocks.

---

## How & Where It Trades

**Spot — centralized:**
- Binance (GAS/USDT), Upbit (GAS/KRW), Bitget (GAS/USDT), KuCoin (GAS/USDT), Crypto.com Exchange (GAS/USD)

**Derivatives:**
- [[hyperliquid|Hyperliquid]] lists a **GAS-PERP** perpetual, providing leveraged exposure with associated [[funding-rate|funding]] and [[open-interest|open-interest]] dynamics.

Liquidity is anchored on major CEXs (notably Binance and the Korean Upbit market) plus the Hyperliquid perp, giving GAS reasonable depth for its size.

---

## Use Case, Narrative & Category

GAS sits in the **infrastructure / smart-contract-platform** category within the **NEO ecosystem**. Its functions:

- **Transaction fees** — every NEO-chain transaction consumes GAS
- **Smart-contract operations** — deploying and invoking contracts is paid in GAS
- **Staking yield** — GAS is the reward NEO holders earn for holding/staking and voting

The narrative is fundamentally a bet on NEO-chain usage: GAS demand rises with on-chain activity and developer adoption, and GAS supply is tied to NEO holdings. GAS is therefore a derivative play on [[neo|NEO]]'s ecosystem health.

---

## Peer Comparison

GAS is best understood against other native fee/gas tokens of smart-contract L1s. The relevant axis is not "another DEX token" but "the fuel of its chain."

| Token | Chain | Role | Supply model | Note |
|---|---|---|---|---|
| **GAS** | NEO | Fee token (dual-token) | Uncapped, emitted to NEO holders | Decoupled governance ([[neo\|NEO]]) vs utility (GAS) |
| ETH | [[ethereum\|Ethereum]] | Fee + staking asset | Net-deflationary post-EIP-1559/Merge | Single token does gas + governance |
| BNB | BNB Chain | Fee + utility | Burn-to-deflation | Single token; periodic burns |
| MATIC/POL | Polygon | Fee + staking | Capped/migrating | Single token |

NEO's two-token split is the distinctive design: a user can transact (spend GAS) without diluting governance, and a long-term holder can accrue GAS yield by holding NEO — analogous to a [[proof-of-stake|proof-of-stake]] reward. The trade-off is that GAS has no governance premium and is pure utility demand.

---

## Valuation Framing (Qualitative)

- **MC/FDV ~1.00** — no unlock overhang, unusual and favourable for this cohort; dilution is the slow emission stream, not cliffs.
- **Demand is downstream of NEO activity** — GAS has no independent demand driver; its bull case is entirely a revival of NEO-chain usage and developer mind-share, which has structurally declined since 2018.
- **~-98.8% from ATH** — GAS reflects the multi-year erosion of the "Chinese Ethereum" narrative; it is a legacy-L1 utility token, not a growth story.
- **Relative resilience** — within this run's cohort, GAS shows the cleanest supply structure and steadier price action, but lacks a catalyst.

This is framing, not a price target; the wiki holds no fair-value model for GAS.

---

## Notable History

- **2018-01-15** — All-time high of **$91.94**, set at the peak of the 2017–18 bull market when NEO ("the Chinese Ethereum") was a top-tier platform narrative.
- **2020-03-13** — All-time low of **$0.6213** during the COVID liquidity crash.
- **2018–2026** — Long structural decline (~-98.8% from ATH) as NEO lost smart-contract mind-share to newer L1s.
- **2026-06-20** — Trading near $1.10, up ~2% on the day and down ~1.5% on the week amid extreme-fear conditions.

---

## Risks

- **Ecosystem dependency** — GAS demand is entirely downstream of NEO-chain usage; if NEO activity stagnates, GAS utility demand stagnates with it.
- **Continuous emission** — GAS is emitted indefinitely to NEO holders, creating persistent sell pressure absent matching utility demand.
- **Competitive risk** — NEO competes with far larger L1s; loss of developer mind-share weighs on both tokens.
- **Liquidity risk** — ~$2M daily volume is modest; large orders can move price.
- **Macro / regime risk** — with Fear & Greed at 23 in an established bear market, legacy-L1 utility tokens are exposed to broad drawdowns.

---

## Platform & Chain Information

**Native Chain:** NEO

### Contract Addresses

| Chain | Address |
|---|---|
| NEO | `602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://neo.org/](https://neo.org/) |
| **Twitter** | [@neo_blockchain](https://twitter.com/neo_blockchain) |
| **Reddit** | [https://www.reddit.com/r/NEO](https://www.reddit.com/r/NEO) |
| **GitHub** | [https://github.com/neo-project/neo](https://github.com/neo-project/neo) |

---

## Trading Profile

**Venues & liquidity.** GAS trades on **both** major venues: Binance (GAS/USDT spot plus a USD-margined GAS perpetual) and [[hyperliquid|Hyperliquid]] (GAS-PERP, up to ~40–50x leverage). This is a **deep, liquid two-venue market** for a ~#347-ranked asset — the dual-venue setup means a genuine cross-venue price/funding signal exists rather than a single thin book. Practically, execution can be split between the Binance CEX order book and the Hyperliquid on-chain perp, and the presence of a spot leg on Binance plus perps on both venues enables carry/basis structures. Still, GAS is a legacy mid-cap with modest turnover, so size positions to book depth rather than headline leverage: high available leverage is a risk multiplier, not a sign of depth, and large market orders on either venue will move price.

**Applicable strategies.**
- [[cash-and-carry]] — Binance spot (GAS/USDT) versus a GAS perp lets you lock the spot-perp basis; NEO/GAS's uncapped emission and NEO-holder distribution can produce persistent funding regimes worth harvesting.
- [[funding-rate-harvest]] — with perps on both Binance and Hyperliquid, a delta-neutral spot-long / perp-short GAS position can collect funding when the perp trades at a premium.
- [[hl-vs-cex-funding-divergence]] — GAS funding can diverge between the Hyperliquid GAS-PERP and the Binance USD-margined perp; the two-venue market makes that spread directly tradable.
- [[pairs-trading]] — GAS is economically inseparable from [[neo|NEO]] (holding NEO mints GAS), so a GAS/NEO pair trade expresses dislocations in that structural link.
- [[range-mean-reversion]] — absent a catalyst, GAS has spent long stretches ranging; mean-reversion around established bands fits its low-momentum, resilient-but-flat character.
- [[liquidation-cascade-fade]] — thin legacy-alt books make GAS prone to sharp leverage-driven flushes on the perps; fading over-extended liquidation moves can capture the rebound.

**Volatility & regime character.** GAS is a **legacy infrastructure / smart-contract-platform (L1 fee) token** — high-beta relative to BTC/ETH in risk-off phases but with a demand driver entirely downstream of NEO-chain activity, which has structurally declined since 2018. It carries no memecoin reflexivity and no governance premium; it behaves as a low-momentum alt that tends to follow broad market beta while lacking an independent catalyst. Correlation to BTC/ETH beta is high on the downside (broad drawdowns hit legacy-L1 utility tokens hard) and muted on the upside without a NEO-ecosystem narrative to lift it.

**Risk flags.**
- **Ecosystem / narrative dependence** — GAS demand is 100% downstream of NEO-chain usage; a stagnant NEO ecosystem caps any fundamental bid.
- **Perpetual emission** — GAS has no max supply and is emitted continuously to NEO holders, creating persistent structural sell pressure (a slow inflation drag rather than cliff unlocks).
- **Liquidity / venue concentration** — modest daily turnover for the size; despite two venues, depth is thin enough that large orders move price and stops can slip.
- **Perp funding dislocations** — leveraged GAS-PERP positioning on both venues can drive funding to extremes and trigger liquidation cascades in a thin book.
- **Macro / regime risk** — in extreme-fear / bear regimes, catalyst-less legacy-L1 tokens are exposed to correlated drawdowns.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=GAS` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=GAS` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=GAS&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=GAS&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=GAS"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[neo]]
- [[hyperliquid]]
- [[ethereum]]
- [[perpetual-futures]]
- [[proof-of-stake]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko top-1000 markets snapshot).

