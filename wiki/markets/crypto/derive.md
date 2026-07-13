---
title: "Derive"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, options, derivatives]
aliases: ["DRV", "Lyra"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://derive.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-exchange]]", "[[options]]", "[[perpetual-futures]]"]
---

# Derive

**Derive** (DRV, base chain **Derive Chain**) is a decentralized protocol for programmable onchain [[options]], [[perpetual-futures|perpetuals]], and structured products. Formerly known as **Lyra**, the protocol rebranded to Derive and migrated from being an Optimism-based options AMM to operating its own **Derive Chain** — an [[ethereum|Ethereum]] [[layer-2|L2]] rollup built with the OP Stack. DRV is the protocol's governance and fee-accrual token, making it one of the few liquid tokens that is a direct claim on **onchain options-and-perps** flow.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | DRV |
| **Base chain** | Derive Chain (OP Stack L2); token also on [[ethereum|Ethereum]], [[base|Base]], Arbitrum, Optimism |
| **Current Price** | $0.096316 |
| **Market Cap** | $96,289,150 |
| **Market Cap Rank** | #276 |
| **Fully Diluted Valuation** | $144,468,850 |
| **24h Volume** | $126,398 |
| **24h Change** | +2.52% |
| **7d Change** | -6.00% |
| **All-Time High** | $0.228265 (2025-01-15) |
| **vs ATH** | -57.80% |
| **All-Time Low** | $0.012437 (2025-04-07) |
| **vs ATL** | +674% |

Trading context: the broader market sits in **extreme fear** ([[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] ~23) within an **established bear market** as of 2026-06-21. DRV's extremely thin 24h volume (~$126K) against a ~$96M market cap reflects very low *DRV-token* spot liquidity in this regime — a notable entry/exit risk. Note this is the liquidity of the **governance token**, not of the protocol's own ETH/BTC options and perps markets, which are the economically meaningful venue (see below).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~999.76M DRV |
| **Total Supply** | 1.50B DRV |
| **Max Supply** | 1.50B DRV |
| **Market Cap / FDV** | ~0.67 |

With ~67% of max supply already circulating, remaining emissions/unlock dilution is more limited than for newer DeFi tokens. The Derive DAO collects trading fees from the Derive Protocol and sequencer/gas fees from Derive Chain, both governed by DRV holders. A portion of trading fees accrues to a protocol **insurance fund** that backstops the rollup and the options/perps markets.

---

## How & Where It Trades

### Protocol mechanics (the venue itself)
Derive is itself a trading venue, not just a token:

- **Options AMM / order book** — Derive runs onchain options markets on assets such as [[ethereum|ETH]] and [[bitcoin|BTC]]. Pricing uses a Black-Scholes-style model with a vol surface; liquidity is provided through market-maker vaults and an AMM that quotes both sides. Inherited from the Lyra design, the AMM hedges its delta exposure to remain roughly market-neutral.
- **Perpetual futures** — Derive offers onchain [[perpetual-futures|perps]] with funding-rate mechanics, giving traders leveraged directional exposure alongside the options book.
- **Structured products / vaults** — automated strategies (e.g. covered calls, cash-secured puts) packaged as deposit vaults, letting passive LPs earn options premium.
- **Portfolio margin** — cross-margining across options and perps positions, a feature aimed at professional/quant traders.
- **Derive Pro (AI agent)** — an AI-powered trading app (built with Messari) that translates a market view into prepared transactions, using smart-contract wallets for one-click, gasless, "chainless" execution across spot/perps/options and external spot AMMs on Optimism, Arbitrum, and Base.

### Spot venues for the DRV token
- **Centralized:** Kraken (DRV/USD).
- **Onchain:** DRV is bridgeable across Ethereum, Base, Arbitrum, and Optimism via the listed contract addresses.

DRV is a small-cap governance token, so it is not (as of this snapshot) a deeply liquid name on major derivatives venues; OI and funding for a DRV perp are not material data points here. The protocol's *own* derivatives volumes (on ETH/BTC options and perps) are the economically meaningful activity rather than DRV-token derivatives.

### Contract addresses
| Chain | Address |
|---|---|
| Ethereum | `0xb1d1eae60eea9525032a6dcb4c1ce336a1de71be` |
| Base | `0x9d0e8f5b25384c7310cb8c6ae32c8fbeb645d083` |
| Arbitrum One | `0x77b7787a09818502305c95d68a2571f090abb135` |
| Optimism | `0x33800de7e817a70a694f31476313a7c572bba100` |

---

## Use Case / Narrative / Category

Derive sits in the **onchain derivatives** category — one of [[defi|DeFi]]'s most technically demanding verticals. Its thesis: bring CEX-grade [[options]] and [[perpetual-futures|perps]] onchain with self-custody, transparent margining, and composability. As the leading onchain *options* [[decentralized-exchange|DEX]] (via its Lyra heritage), it competes for the slice of DeFi flow that wants non-linear payoffs (volatility, hedging, premium harvesting) rather than just spot swaps or perps. The "DeFAI" angle (Derive Pro) positions it at the intersection of AI agents and onchain trading.

---

## Valuation Framing (qualitative)

DRV is one of the few tokens in this loop with a **genuine fee-accrual mechanism**: the Derive DAO collects trading fees from the options/perps protocol plus sequencer/gas fees from Derive Chain, with a portion routed to an insurance fund. That makes a fee-multiple framing more meaningful than for pure-governance peers — though the actual fee-to-token pass-through is governance-controlled and modest at current volumes.

- **Protocol revenue, not token volume, is the signal.** With DRV-token spot volume at only ~$126K/24h, the token tape is uninformative; the real gauge is options/perps notional traded on Derive itself and the resulting fee run-rate.
- **vs ATH:** -57.8% is a *shallower* drawdown than most names in this basket (many are -95%+), reflecting that DRV held value better through the cycle, partly on the strength of a working product.
- **FDV overhang:** MC/FDV ~0.67 — ~33% of supply still to enter circulation is the main dilution flag.

## Peer Comparison

| Protocol | Token | Niche | Mkt Cap Rank | Mkt Cap | vs ATH |
|---|---|---|---|---|---|
| **Derive (ex-Lyra)** | DRV | Onchain options + perps DEX (own L2) | #276 | ~$96M | -57.8% |
| [[hyperliquid\|Hyperliquid]] | HYPE | Onchain perps DEX (own L1) | top-tier | — | — |
| dYdX | DYDX | Onchain perps DEX | — | — | deep drawdown |
| GMX | GMX | Onchain perps (pool-based) | — | — | deep drawdown |
| Aevo | AEVO | Onchain options + perps | — | — | deep drawdown |

> Derive is the most **options-centric** of these; the others are perps-first. Peers without ranks/caps are not in this snapshot's relevant rows and are shown for context only.

---

## Notable History

- **Lyra Finance** launched as an Optimism-based options AMM, becoming one of the better-known onchain options protocols.
- Rebranded to **Derive** and migrated to its own OP Stack rollup (**Derive Chain**), expanding from pure options into perps and structured products and converting LYRA → DRV.
- DRV's all-time high of **$0.228** came on 2025-01-15; the all-time low of **$0.0124** on 2025-04-07. As of 2026-06-21 it trades ~58% below ATH (but ~674% above its ATL) amid the broad bear market.

---

## Risks

- **Liquidity / market-impact risk** — extremely thin DRV-token spot volume (~$126K/24h) means large orders can move price sharply; exit liquidity is a real concern.
- **Smart-contract & oracle risk** — options pricing depends on accurate vol and price oracles; a faulty oracle or contract bug could mis-price or drain the AMM. The insurance fund mitigates but does not eliminate this.
- **AMM / market-maker solvency** — onchain options AMMs bear short-gamma risk; sharp vol spikes can cause LP losses, as the broader onchain-options sector has seen historically.
- **Sequencer / rollup risk** — running its own L2 concentrates liveness and upgrade risk in Derive Chain's sequencer and bridge.
- **Token dilution** — ~33% of max supply still to enter circulation.
- **Regime risk** — derivatives volumes tend to contract in bear markets, pressuring the fee base that backs DRV's value accrual.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-exchange]]
- [[options]]
- [[perpetual-futures]]
- [[layer-2]]
- [[defi]]
- [[base]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000).
