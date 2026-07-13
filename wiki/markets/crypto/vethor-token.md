---
title: "VeThor"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["VTHO", "VeThor Token"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.vechain.org/"
related: ["[[crypto-markets]]", "[[vechain]]", "[[ethereum]]"]
---

# VeThor

**VeThor** (ticker **VTHO**) is the **gas token** of the [[vechain]] blockchain. VeChain uses a **dual-token model**: **VET** (VeChain Token) is the value-transfer/staking asset, and **VTHO** (VeThor) is the energy/gas token consumed to pay for transactions and smart-contract execution. Crucially, holding VET *generates* VTHO continuously, so network usage costs are decoupled from the price of the primary asset — a design VeChain markets as better suited to enterprises than single-token chains like [[ethereum]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | VTHO |
| **Native chain** | VeChainThor (native gas asset) |
| **Price** | $0.00039276 |
| **Market Cap** | $39,554,667 |
| **Market Cap Rank** | #531 |
| **24h Volume** | $715,195 |
| **24h Change** | +1.35% |
| **7d Change** | -2.07% |
| **Circulating Supply** | 100.89B VTHO |
| **Total Supply** | 100.90B VTHO |
| **Max Supply** | Uncapped (inflationary; minted by [[vechain|VET]] holdings) |
| **Fully Diluted Valuation** | ~$39.56M |
| **Market Cap / FDV** | ~1.00 |
| **All-Time High** | $0.04671227 (2018-08-29) — now ~-99.2% |
| **All-Time Low** | $0.00015238 (2020-03-16) — now ~+157.7% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: VTHO is up ~1.3% on the day but down ~2% on the week, ~99% below its 2018 peak, against a market backdrop of **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = **23**) and an "Established Bear Market."

---

## Tokenomics & Supply — the VET/VTHO Dual-Token Gas Model

VeChain deliberately separates **store of value** from **cost of use**:

- **VET** is the base asset (staking/value transfer). Simply *holding* VET in a wallet or node continuously **generates VTHO** at a base rate (historically ~0.000432 VTHO per VET per day), similar to the NEO/GAS relationship.
- **VTHO** is the **gas**: every transaction and contract call on VeChain is paid in VTHO, which is then **partially burned** (a portion of VTHO used as gas is destroyed). This creates a generation-vs-burn dynamic.
- **Implication:** if network activity (burn) outpaces VTHO generation, VTHO becomes deflationary; if generation outpaces usage (the common case in low-activity periods), VTHO is **inflationary**, which structurally caps its price and explains the very large supply (~100.88B) and tiny unit price. There is **no fixed max supply** — VTHO is minted perpetually by VET holdings.
- **MC/FDV ≈ 1.00:** total equals circulating, so there is no investor/team unlock cliff; the relevant "dilution" is the ongoing emission driven by VET holders, not a vesting schedule.
- **Enterprise rationale:** because dApp operating costs are paid in VTHO (cheap, separately supplied) rather than in the appreciating base asset, businesses get predictable transaction costs even if VET rises — VeChain's core pitch for enterprise adoption.

---

## How & Where It Trades

- **Spot (CEX):** Binance (VTHO/USDT), Kraken (VTHO/USD), Upbit (VTHO/KRW), Bitget (VTHO/USDT), KuCoin (VTHO/USDT), and Crypto.com Exchange (VTHO/USD).
- **Native chain:** VeChainThor; VTHO is the native gas asset and is not primarily a DEX/AMM asset.
- **Derivatives / Hyperliquid:** VTHO is far less commonly offered as a perpetual than VET; no perp/funding/open-interest data is recorded for VTHO in this snapshot, and traders seeking VeChain-ecosystem derivatives typically use **VET** perps instead. **No VTHO perp recorded.**
- **Liquidity profile:** ~$0.72M of 24h volume on a ~$39.6M cap (turnover <2%) — the thinnest book in this batch, so VTHO is best treated as a utility/gas asset rather than a liquid trading vehicle.

---

## Peer Comparison — Dual-Token Gas Models

| Pair | Value asset | Gas asset | Mechanism | Note |
|---|---|---|---|---|
| **[[vechain|VeChain]]** | VET | **VTHO** | Holding VET mints VTHO; VTHO partly burned as gas | Enterprise/supply-chain L1 |
| NEO | NEO | GAS | Holding NEO mints GAS for fees | The original model VeChain echoes |
| Ontology | ONT | ONG | Holding ONT mints ONG | NEO-derived dual-token design |
| (contrast) [[ethereum]] | ETH | ETH | Single token pays gas (burned via EIP-1559) | Costs rise with ETH price |

The dual-token design's selling point is **predictable enterprise transaction costs**: a business pays fees in cheap, separately-supplied VTHO rather than in the appreciating base asset (VET), unlike single-token chains where gas cost tracks the L1 token price.

---

## Valuation Framing (qualitative)

VTHO is **not engineered to appreciate** — it is a deliberately abundant, perpetually-minted gas unit whose price is structurally capped by inflation. Its ~$40M cap is therefore better understood as a function of (1) the size of the VTHO float (~100.9B, continuously growing as [[vechain|VET]] holders generate it) and (2) the burn rate from on-chain activity. When VeChain network usage is low, generation outpaces burn and VTHO drifts down; only sustained, high-throughput enterprise adoption would tip the generation/burn balance toward deflation and support price. Investors seeking value accrual from the VeChain ecosystem typically hold **VET** (which captures the staking/value-transfer role) rather than VTHO. Treat VTHO as an infrastructure/utility holding, not a growth bet. Qualitative framing only — not a price target.

---

## Use Case, Narrative & Category

VTHO's narrative is inseparable from [[vechain]]'s **enterprise blockchain / supply-chain** positioning. VeChain has historically promoted partnerships across automotive and logistics (e.g., BMW, Groupe Renault, DNV GL) and a focus on real-world traceability and sustainability use cases; VTHO is the fuel that powers those on-chain operations. Aggregator categories: Layer 1 (L1), VeChain Ecosystem. As a gas token, VTHO is more of an infrastructure/utility holding than a standalone narrative play.

---

## Notable History

- **2018-08-29:** all-time high of $0.04671227, set during VeChain's mainnet-launch era and the token swap from its earlier ERC-20 form on [[ethereum]] to the native VeChainThor chain.
- **2020-03-16:** all-time low of $0.00015238 during the COVID crash.
- **2026-06-21:** trading at $0.00039276 (#531) — ~-99% from ATH but still ~+158% above ATL, reflecting its role as a perpetually-emitted gas asset whose price is structurally suppressed by inflation.

---

## Risks

- **Structural inflation:** VTHO is continuously minted by VET holders; unless on-chain activity (and burn) is high, generation outpaces usage and keeps downward pressure on price.
- **Utility, not appreciation:** by design VTHO is meant to be a cheap, abundant gas unit — it is not engineered as a value-accrual asset, limiting upside versus VET.
- **Dependence on VeChain adoption:** demand for VTHO is a derivative of [[vechain]] network usage; enterprise adoption has been slower and more uneven than early partnerships implied.
- **Liquidity:** the lowest turnover in this group raises execution/slippage risk.
- **Macro/beta:** high sensitivity to a bear market currently at extreme fear ([[crypto-fear-and-greed-index|Fear & Greed]] = 23).

---

## See Also

- [[crypto-markets]]
- [[vechain]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-markets dataset).
