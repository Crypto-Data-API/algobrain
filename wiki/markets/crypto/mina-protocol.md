---
title: "Mina Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["MINA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://minaprotocol.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[zero-knowledge-proofs]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Mina Protocol

**Mina Protocol** (ticker **MINA**) is a [[proof-of-stake]] [[layer-1]] that bills itself as "the world's lightest blockchain": instead of growing without bound, the entire chain is compressed to a constant-size **succinct [[zero-knowledge-proofs|zk-SNARK]] proof of roughly 22 KB**. This lets any participant — even on a phone — verify the full chain state without downloading its history, enabling a highly decentralized and verifiable network. Mina also exposes its zk machinery to developers through **zkApps** (zero-knowledge smart contracts written in TypeScript via the o1js library), positioning it as privacy- and verifiability-focused infrastructure.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MINA |
| **Market Cap Rank** | #427 |
| **Market Cap** | $54.22M |
| **Current Price** | $0.04203 |
| **24h Change** | -0.67% |
| **7d Change** | -2.85% |
| **24h Volume** | $3.52M |
| **All-Time High** | $9.09 (June 2021) |
| **All-Time Low** | $0.03990 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. MINA trades roughly 5% above its all-time low (~$0.0399) and about 99.5% below its June-2021 all-time high of $9.09 — one of the deeper peak-to-trough declines among surviving [[layer-1|L1s]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.29B MINA |
| **Total Supply** | ~1.29B MINA |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation (FDV)** | ~$54.22M |
| **Market Cap / FDV** | ~1.00 |

MINA has **no fixed max supply**; new tokens are issued continuously as block rewards to fund [[proof-of-stake]] staking. Because circulating supply effectively equals total supply (MC/FDV ≈ 1.00), there is no large locked overhang from team/investor cliffs — but the trade-off is **persistent token inflation** that dilutes holders unless they stake. Mina uses **Ouroboros Samasika**, a succinct-blockchain-adapted variant of Cardano-style Ouroboros [[proof-of-stake]]; any holder can stake (or delegate to a block producer) to earn rewards and help secure the chain.

---

## How & Where It Trades

**Spot venues.** MINA is listed on [[binance]] (MINA/USDT), [[kraken]] (MINA/USD), Upbit (MINA/KRW), Bitget, KuCoin, and Crypto.com.

**Derivatives.** A MINA perpetual trades on [[hyperliquid]] (MINA-PERP), plus perp markets on major centralized derivatives venues. At a ~$54M market cap with ~$3.7M daily volume, derivatives depth is thin and funding/OI are volatile — confirm live before sizing leverage. Spot liquidity is concentrated in USDT pairs.

---

## Technology & Consensus

Mina's core innovation is **recursive zk-SNARKs**: each new block carries a proof that recursively attests to the validity of all prior blocks, so the proof of the entire chain stays a constant ~22 KB regardless of how long the chain runs. Consequences:

- **Succinct verification.** Light clients verify the whole chain by checking one small proof — no multi-hundred-gigabyte node sync, sharply lowering the hardware barrier to running a verifying node.
- **Ouroboros Samasika consensus.** A provably secure [[proof-of-stake]] protocol adapted to the succinct-blockchain setting, allowing nodes to bootstrap from genesis using only the SNARK.
- **zkApps.** Off-chain execution with on-chain proof verification, written in TypeScript (o1js), enabling private inputs and verifiable computation — a natural fit for identity, compliance, and oracle use cases.

---

## Use Case, Narrative & Category

Mina sits in the **zero-knowledge / privacy / succinct-blockchain L1** category, overlapping conceptually with [[zero-knowledge-proofs|ZK]] scaling projects but distinct in that the *base layer itself* is the SNARK, not a rollup atop [[ethereum]]. Its narrative centers on decentralization (a phone can verify the chain), privacy-preserving applications, and a "verifiable internet" / proof-of-everything thesis. Tagged categories include Smart Contract Platform, Layer 1 (L1), Zero Knowledge (ZK), Privacy Blockchain, Proof of Stake (PoS), Coinbase 50 Index, plus numerous VC-portfolio tags (Paradigm, Coinbase Ventures, Multicoin, Pantera, Polychain).

---

## Valuation Framing (qualitative)

At a ~$54M market cap, MINA is a deep small-cap whose price is ~99.5% below its 2021 peak. With MC/FDV ≈ 1.00 there is no locked-supply cliff, so the dilution risk is *flow* (continuous PoS emissions) rather than a discrete unlock event — holders must stake to avoid being inflated away. The bull case is technological optionality: a constant-size, phone-verifiable [[zero-knowledge-proofs|zk]] base layer is a genuinely differentiated design, and ZK/privacy is a recurring narrative. The bear case is the gap between that thesis and realized usage — zkApp adoption has lagged, and a token can stay "interesting tech, no flow" indefinitely. In an extreme-fear regime, thin liquidity (~$3.5M/day) amplifies both directions. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | ZK role |
|---|---|---|---|---|---|---|
| **Mina** | MINA | Succinct zk [[layer-1]] | #427 | $54.22M | ~1.00 | Base layer *is* the SNARK |
| [[linea]] | LINEA | zkEVM [[layer-2]] | #391 | $61.63M | ~0.34 | zk-rollup atop [[ethereum]] |
| [[zetachain]] | ZETA | Omnichain L1 | #426 | $54.23M | ~0.70 | TSS / cross-chain, not zk |
| [[astar]] | ASTR | Multi-chain L1/L2 | #475 | $47.34M | ~0.87 | zkEVM L2 (Polygon CDK) |

*Mina is the only project here where the entire base chain is compressed to a recursive SNARK; the others use zk as a scaling rollup or use non-zk cross-chain security.*

---

## Notable History

- Mina launched its mainnet in 2021 after a high-profile CoinList sale; MINA printed its all-time high of **$9.09 in June 2021**.
- The token has since declined ~99.5%, reaching an all-time low near $0.0399 around March 2026.
- It carries **FTX Holdings** and **Alameda/various-VC portfolio** tags, a legacy association from the 2021–22 cycle that surfaced overhang concerns during the FTX collapse.
- As of 2026-06-21 it trades at ~$0.042, about 5% off its low.

---

## Risks

- **Perpetual inflation.** Uncapped supply means non-stakers are continuously diluted; demand must keep pace with emissions to hold price.
- **zkApp adoption lag.** The succinct-chain thesis is technically elegant but on-chain application traction and developer adoption have been limited; the value case depends on usage that has not yet materialized at scale.
- **Prover performance / centralization.** Generating recursive SNARKs is computationally heavy, which can concentrate block production among well-resourced operators.
- **Legacy distribution overhang.** FTX/Alameda-era holdings and VC allocations add historical supply-disposition risk.
- **Severe drawdown / liquidity.** Down ~99.5% from ATH, ~$3.7M daily volume, and an extreme-fear macro regime amplify volatility and slippage.

---

## Trading Profile

**Venues & liquidity.** MINA is a genuine two-venue market: it trades on [[binance]] (spot MINA/USDT plus a USD-margined MINA perpetual) and on [[hyperliquid]] (MINA-PERP, up to ~40-50x). Having both a deep CEX order book and an on-chain perp means a trader can quote, hedge, and roll positions across venues, and the two funding curves and mark prices can diverge enough to matter for carry and arbitrage. That said, MINA is a deep small-cap (rank ~393, thin daily volume): book depth is modest, so large clips move price and slippage grows fast beyond small size. Availability across two venues improves execution optionality (route to whichever side is deeper, split fills), but it does not remove the underlying thinness — size conservatively, ladder entries/exits, and confirm live depth and funding before leveraging.

**Applicable strategies.**
- [[funding-rate-harvest]] — a two-venue small-cap perp whose funding on Binance and Hyperliquid can run persistently rich or negative; harvest the carry delta-neutral against spot.
- [[hl-vs-cex-funding-divergence]] — with the same asset perped on both Hyperliquid and Binance, the two funding rates frequently dislocate on a thin book, a clean cross-venue funding trade.
- [[cash-and-carry]] — hold Binance spot MINA against a short perp to capture positive funding/basis while staying market-neutral on a low-notional name.
- [[liquidation-cascade-fade]] — thin depth means leverage flushes overshoot violently; fade the wick after a cascade once open interest resets.
- [[range-mean-reversion]] — MINA spends long stretches pinned near its all-time-low zone in tight ranges, favoring mean-reversion between support and resistance bands.
- [[oi-price-exhaustion]] — on a low-float perp, rising open interest into a stalling price flags crowded positioning ripe for a reversal.

**Volatility & regime character.** MINA is a low-cap, high-beta infrastructure/privacy [[layer-1]] token (succinct zk-SNARK base layer, ZK/privacy narrative). It behaves as a high-beta alt: it amplifies BTC/ETH directional moves on the way up and down, with sharp idiosyncratic spikes tied to ZK-narrative rotations and its heavy multi-year drawdown. Correlation to BTC/ETH is meaningful in risk-on/risk-off swings, but on a thin book single-venue flow and narrative shifts can decouple it intraday. Emissions-driven inflation adds a persistent structural drag distinct from beta.

**Risk flags.**
- **Liquidity / venue concentration** — thin daily volume and modest book depth; execution and funding are sensitive to flow on either venue, and slippage is material beyond small size.
- **Perpetual inflation / emissions** — uncapped supply with continuous PoS block rewards is a persistent dilution flow (rather than a discrete unlock cliff) that weighs on price.
- **Narrative dependence** — the ZK/privacy/succinct-chain thesis drives sentiment; if zkApp adoption keeps lagging, the token can drift on "interesting tech, no flow."
- **Perp funding dislocations** — low float plus two perp venues make funding and basis swing quickly; a crowded side can force violent funding resets and liquidation cascades.
- **Legacy overhang** — FTX/Alameda-era holdings and VC allocations carry historical supply-disposition risk.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MINA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MINA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MINA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MINA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MINA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[zero-knowledge-proofs]]
- [[proof-of-stake]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MINA |
| **Market Cap Rank** | #388 |
| **Market Cap** | $58.44M |
| **Current Price** | $0.0452 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Zero Knowledge (ZK), FTX Holdings, Proof of Stake (PoS), Privacy Blockchain, Made in USA, CoinList Launchpad |
| **Website** | [https://minaprotocol.com/](https://minaprotocol.com/) |

---

## Overview

The world's lightest blockchain, powered by participants. Mina is building a privacy-preserving gateway between the real world and crypto — and the infrastructure for the secure, democratic future we all deserve.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.29B MINA |
| **Total Supply** | 1.29B MINA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $58.44M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $9.09 (2021-06-01) |
| **Current vs ATH** | -99.50% |
| **All-Time Low** | $0.0367 (2026-06-30) |
| **Current vs ATL** | +22.96% |
| **24h Change** | +1.35% |
| **7d Change** | -0.64% |
| **30d Change** | +3.22% |
| **1y Change** | -78.19% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MINA/USDT | N/A |
| Kraken | MINA/USD | N/A |
| Upbit | MINA/KRW | N/A |
| Bitget | MINA/USDT | N/A |
| KuCoin | MINA/USDT | N/A |
| Crypto.com Exchange | MINA/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://minaprotocol.com/](https://minaprotocol.com/) |
| **Twitter** | [@minaprotocol](https://twitter.com/minaprotocol) |
| **Reddit** | [https://www.reddit.com/r/MinaProtocol/](https://www.reddit.com/r/MinaProtocol/) |
| **Telegram** | [minaprotocol](https://t.me/minaprotocol) (16,301 members) |
| **Discord** | [https://discord.com/invite/Vexf4ED](https://discord.com/invite/Vexf4ED) |
| **GitHub** | [https://github.com/MinaProtocol/mina](https://github.com/MinaProtocol/mina) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,883 |
| **GitHub Forks** | 525 |
| **Commits (4 weeks)** | 92 |
| **Pull Requests Merged** | 6,822 |
| **Contributors** | 87 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.76M |
| **Market Cap Rank** | #388 |
| **24h Range** | $0.0438 — $0.0454 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
