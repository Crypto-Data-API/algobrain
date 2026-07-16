---
title: "Prom"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, cross-chain, crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["PROM", "Prom", "Prometeus"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://prom.io/"
related: ["[[cross-chain-bridge]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Prom

**Prom** (PROM) — formerly known as **Prometeus** — is a modular **[[layer-2]]** built around a zkEVM that aims to provide interoperability across many chains, including both EVM and non-EVM networks. The project (this page covers the **Prom zkEVM / gaming-and-data Layer 2**, which rebranded from Prometeus, not a separate "Prometeus data-monetization network") submits its transaction proofs to additional chains on top of a chosen settlement chain, positioning itself as a bridge between ecosystems. It ranks **#799** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot, PROM traded at **$1.16** with a market cap of **$21,090,019** (rank **#799**), down **2.51%** over 24 hours but up **8.60%** over 7 days — a relative outperformer on the week despite a risk-off backdrop (Bitcoin near $64,508, Fear & Greed 21 / "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PROM |
| **Market Cap Rank** | #799 |
| **Market Cap** | $21,090,019 |
| **Current Price** | $1.16 |
| **24h Change** | -2.51% |
| **7d Change** | +8.60% |
| **Categories** | Smart Contract Platform, Layer 2 (L2), BNB Chain Ecosystem, Ethereum Ecosystem |
| **Website** | [https://prom.io/](https://prom.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Architecture — How It Works

Prom is a **modular zkEVM [[layer-2]]**. Three properties define it.

**zkEVM execution.** As a zkEVM, Prom is EVM-equivalent — developers can redeploy standard [[ethereum|Ethereum]] smart contracts unchanged. Transactions are executed off-chain, batched, and compressed; a **zero-knowledge validity proof** attests that the batch was executed correctly. Posting that succinct proof to a settlement layer is what gives an [[zero-knowledge-rollup|zk-rollup]] its security: anyone can verify the proof without re-executing the work, so users get cheaper, faster execution than Ethereum L1 while inheriting settlement-layer security. This is the stronger security model versus [[optimistic-rollup|optimistic rollups]] (Arbitrum, Optimism, Base), which rely on a multi-day fraud-proof challenge window instead of cryptographic finality.

**Modular settlement.** "Modular" means the execution, settlement, and data-availability layers are decoupled. Rather than being permanently bolted to one settlement chain, Prom can submit its validity proofs to multiple settlement targets — the basis of its interoperability pitch.

**Interoperability.** The distinctive design goal is to act as connective tissue: Prom submits proofs of its transactions to additional chains on top of the chosen settlement chain, building a [[cross-chain-bridge|bridge]] between ecosystems and aiming to connect both EVM and non-EVM networks. Following its rebrand from Prometeus, the go-to-market has leaned toward **on-chain gaming and data** verticals, where low fees and high throughput matter most and where a captive token economy can drive usage.

> **Disambiguation:** this page covers the **Prom zkEVM / gaming-and-data Layer 2** (rebranded from Prometeus), *not* a separate "Prometeus data-monetization network." The PROM ticker is one of the longer-lived in this cohort and has carried several product identities.

## Token role

**PROM** is the network's native token. In an L2 context, a native token typically serves some combination of:

- **Gas / fees** — paying for execution on the rollup.
- **Staking / sequencing / proving incentives** — backing the actors who order transactions and generate validity proofs.
- **Governance** — directing protocol parameters and treasury.

A notable structural feature is PROM's **near-fully-circulating, scarce supply**: circulating supply (~18.25M) is close to the ~19.25M max supply (Mkt Cap / FDV ≈ 0.95), so there is minimal dilution overhang — unusual for an active L2 and a point often cited by holders. PROM is also one of the longer-lived tickers in this cohort (its ATH dates to the 2021 cycle), having pivoted through multiple identities before the current zkEVM positioning.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.25M PROM |
| **Total Supply** | 19.25M PROM |
| **Max Supply** | 19.25M PROM |
| **Fully Diluted Valuation** | $19.42M |
| **Market Cap / FDV Ratio** | 0.95 |

### Value Accrual & Governance

PROM's standout feature is a **near-fully-circulating, scarce supply** (~18.25M of a ~19.25M cap, **MC/FDV ≈ 0.95**). For holders this is a meaningful structural positive: there is **almost no unlock or emissions overhang** to dilute the price, in sharp contrast to the heavily-locked supply profiles on [[stronghold-token|SHX]] (MC/FDV ≈ 0.18), [[audiera|BEAT]] (≈ 0.29), or [[chain-2|XCN]] (≈ 0.72). The low absolute supply also keeps the unit price in the ~$1 range rather than fractions of a cent.

Value accrues to PROM through the standard L2-token channels — **gas/fees** for execution on the rollup, **staking/sequencing/proving incentives** for the actors who order transactions and generate validity proofs, and **governance** over parameters and treasury. The open question, common to all L2 tokens, is how much real fee revenue and staking demand the chain actually captures: scarce supply only matters if there is offsetting demand from genuine usage.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $105.94 (2021-04-30) |
| **Current vs ATH** | -99.05% |
| **All-Time Low** | $0.0887 (2019-11-08) |
| **Current vs ATL** | +1037.18% |
| **24h Change** | -2.51% |
| **7d Change** | +8.60% |
| **1y Change** | -82.94% |

> *24h/7d figures are the 2026-06-22 snapshot; older deltas reflect the prior 2026-04-09 ingest.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xfc82bb4ba86045af6f327323a46e80412b91b27d` |
| Binance Smart Chain | `0xaf53d56ff99f1322515e54fdde93ff8b3b7dafd5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PROM/USDT | N/A |
| Upbit | PROM/BTC | N/A |
| Bitget | PROM/USDT | N/A |
| KuCoin | PROM/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XFC82BB4BA86045AF6F327323A46E80412B91B27D/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://prom.io/](https://prom.io/) |
| **Twitter** | [@prom_io](https://twitter.com/prom_io) |
| **Telegram** | [prom_io](https://t.me/prom_io) (34,553 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $946,827.00 |
| **Market Cap Rank** | #830 |
| **24h Range** | $1.01 — $1.05 |
| **Last Updated** | 2026-04-09 |

---

## How & Where It Trades

- **Spot (CEX):** PROM is listed on Binance (PROM/USDT), Upbit (PROM/BTC), Bitget, and KuCoin — broader tier-1 reach than most micro-caps in this set.
- **Spot (DEX):** A Uniswap V3 PROM/USDT pool on [[ethereum|Ethereum]] provides on-chain liquidity; the token also has a BNB Chain deployment.
- **Liquidity read:** ~$0.95M of 24h volume against a ~$21M cap (~4.5% turnover) is tradeable but thin. The **+8.60% 7d / -2.51% 24h** split shows how sharply a low-float, scarce-supply token can swing on modest flow. The scarce supply cuts both ways: no unlock overhang to absorb, but a thin float means low liquidity and exaggerated moves.
- **Derivatives:** No confirmed major perp surfaced in the snapshot; treat PROM as primarily spot-driven for hedging purposes.

## Competitive Position

Prom competes in the extremely crowded **zkEVM Layer-2** field. Differentiating on raw scaling is hard, so it leans on **interoperability** (multi-settlement proof submission, EVM + non-EVM reach) and a **gaming/data vertical** focus rather than competing head-on as a general-purpose L2.

| Project | Token | Type | Differentiator | Relative scale |
|---|---|---|---|---|
| **Prom** | PROM | zkEVM L2 (modular, multi-settlement) | Interoperability + gaming/data vertical; scarce ~19M supply | Micro-cap (~$21M), small TVL |
| Polygon zkEVM | POL | zkEVM L2 | Polygon ecosystem + AggLayer | Large ecosystem |
| zkSync Era | ZK | zkEVM L2 | Native AA, large airdrop base | Large |
| Scroll | SCR | zkEVM L2 | Bytecode-equivalent, Ethereum-aligned | Mid/large |
| Linea | — | zkEVM L2 | ConsenSys / MetaMask distribution | Large |
| Arbitrum / Base | ARB / — | Optimistic rollup | Dominant TVL & liquidity (fraud-proof model) | Largest |

Prom's scarce, near-fully-circulating token is a marketing positive, but it is a **small player by ecosystem size and TVL** relative to the L2 leaders, and its zk-validity-proof security model — while stronger than optimistic rollups in theory — does not by itself attract the developers and liquidity that the larger chains command.

## Narrative, Category & Catalysts

PROM's narrative blends **zkEVM scaling**, **cross-chain interoperability**, and an **on-chain gaming/data** vertical, with the scarce-supply story as a recurring holder talking point. As a long-lived ticker (ATH from the 2021 cycle) that has pivoted through several identities, it also carries a "survivor / old-coin rotation" angle. Catalysts would include real gaming/data deployments driving fee revenue, a settlement-target or major-chain integration that validates the interoperability thesis, a tier-1 derivatives listing, or a broad L2-sector rotation. The -82.94% 1-year change underlines that, so far, usage has not matched the narrative.

## Risks

**Technology & security**
- **Bridge / interoperability risk** — cross-chain proof submission and bridging introduce some of the most exploited attack surfaces in crypto ([[cross-chain-bridge|bridge]] hacks); multi-settlement design widens that surface.
- **Sequencer / proving centralisation** — like most L2s, early-stage rollups typically run a centralised sequencer and prover, a liveness and censorship risk until decentralised.

**Adoption & competition**
- **L2 commoditization** — many well-funded zkEVMs compete for the same developers and liquidity; carving durable share is difficult.
- **Ecosystem traction** — value accrues to L2 tokens via real usage and fees; without sustained dApp/gaming activity, token demand is thin and the scarce-supply story is hollow.

**Market & track record**
- **Rebrand / pivot history** — Prometeus to Prom and successive repositionings can dilute brand trust and signal product-market-fit struggles; the -82.94% 1y change reflects a long drawdown.
- **Microcap / thin-float volatility** — ~$21M cap with a tiny ~18M float; the +8.60% 7d / -2.51% 24h split shows how sharply it swings on low liquidity.

---

## History / Timeline

*Dated points below are from public market data; undated product milestones are omitted to avoid fabrication.*

- **2019-11-08** — Recorded all-time low of **$0.0887** (early Prometeus era).
- **2021-04-30** — All-time high of **$105.94**, near the top of the 2021 bull cycle.
- **Subsequent cycle** — project rebrands from Prometeus to **Prom** and repositions around a **zkEVM L2** with a gaming/data vertical and interoperability focus; the token retains its scarce, near-fully-circulating supply.
- **2026-06-22** — Trades at **$1.16** (~99% below ATH, +1,037% above ATL), rank ~#799, up 8.60% on the week despite an Extreme-Fear backdrop.

---

## Trading Playbook (bear / Extreme-Fear, bottoming regime)

*Context: 2026-06-23 macro is Extreme Fear (F&G 21), market-health 29/100 bearish, long-horizon regime "bottoming / accumulation."*

- **Stance: speculative, small only.** PROM's week-over-week outperformance (+8.60%) in a risk-off tape can mark either early accumulation interest or a thin-float squeeze — both reverse fast. Do not chase strength on a low-liquidity micro-cap.
- **The structural positive** is the clean MC/FDV ≈ 0.95 — no unlock cliff, so rallies are not capped by scheduled supply, unlike heavily-locked peers ([[stronghold-token|SHX]], [[audiera|BEAT]]). That makes PROM more of a pure demand-vs-sentiment play.
- **Catalyst triggers:** real gaming/data deployment metrics, a settlement-chain integration validating the interop thesis, a tier-1 perp listing, or a broad L2-sector rotation. Without usage data, the narrative alone is fragile.
- **Risk controls:** size for thin liquidity and wide swings; with no reliable perp, hedging is hard, so cap position size and use sentiment-based stops tied to the BTC bottoming range.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

PROM is tradable on **[[binance]]** — both **spot** (PROM/USDT) and a **USD-margined [[perpetual-futures|perpetual]]**, which carries the standard derivatives telemetry: [[funding-rate|funding]], **open interest**, and **liquidations**. It is **NOT listed on Hyperliquid**, so Binance is the **primary (effectively sole) leveraged venue**. This concentration matters for execution: leveraged flow, funding, and liquidation dynamics all route through one order book, so basis and funding signals are Binance-defined rather than blended across venues. Given the thin spot float (~$1M/day turnover against a ~$21M cap), perp liquidity and open interest are shallow — size positions small, expect wider slippage on market orders, and prefer limit/scaled entries. A single-venue perp also means venue outages or delisting risk is undiversified, and crowded positioning can trigger outsized liquidation cascades on modest moves.

### Applicable strategies

- [[funding-rate-harvest]] — a low-float, sentiment-driven micro-cap perp tends to swing between funding extremes; harvest the rate when it decouples from spot drift.
- [[crowded-long-funding-fade]] — Binance-concentrated leverage on a thin float makes over-extended long funding a reliable fade signal into pullbacks.
- [[liquidation-cascade-fade]] — with shallow perp depth and one venue, forced liquidations overshoot; fading the flush targets the mean-reversion snapback.
- [[oi-confirmed-trend]] — pair Binance open-interest changes with price to separate real trend from thin-float noise before committing directionally.
- [[breakout-and-retest]] — scarce-supply, low-float PROM can gap on catalysts (gaming/data deployments, L2 rotation); trade the confirmed breakout retest rather than chasing.
- [[volatility-targeting]] — exaggerated swings on low liquidity demand size scaling to realized volatility to keep risk constant.

### Volatility & regime character

PROM is a **micro-cap zkEVM/[[layer-2]] infra token** (~$21M cap, rank ~#735-830 band) with a **near-fully-circulating scarce supply** (MC/FDV ≈ 0.95). It behaves as a **high-beta altcoin**: broadly correlated to BTC/ETH risk appetite, but with thin-float reflexivity that amplifies both up and down moves on modest flow (see the +8.60% 7d / -2.51% 24h split). It is a **DeFi/infrastructure token rather than a memecoin**, so narrative catalysts (interoperability, gaming/data verticals, L2-sector rotation) drive it more than pure meme reflexivity — but low liquidity gives it memecoin-like tail volatility. In risk-off regimes it can either lead early accumulation or squeeze on thin liquidity, both of which reverse quickly.

### Risk flags

- **Venue concentration** — leveraged trading depends on Binance alone (no Hyperliquid); an outage, margin change, or delisting is undiversified single-point risk.
- **Liquidity / thin float** — ~$1M/day spot turnover and shallow perp depth mean wide slippage, gap risk, and exaggerated liquidation-driven moves.
- **Narrative dependence** — value accrual hinges on real gaming/data/L2 usage that has not yet matched the story (-82.94% 1y); without fee/traction data the thesis is fragile.
- **Rebrand / track-record risk** — successive pivots (Prometeus to Prom) can dilute brand trust and signal product-market-fit uncertainty.
- **Bridge / interoperability surface** — cross-chain proof submission and bridging are among crypto's most exploited attack surfaces, an event risk that can gap the token.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=PROMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=PROMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=PROM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=PROM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=PROMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=PROMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=PROM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[cross-chain-bridge]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Overview

Prom is a modular ZkEVM Layer 2 that enables interoperability across various chains, including both EVM and non-EVM compatible networks. Prom submits its proof of transaction to the additional chains on top of the chosen Settlement chain, building the bridge between ecosystems.

---
