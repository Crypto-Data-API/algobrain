---
title: "DeGate"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["DG", "DeGate DEX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://degate.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-exchange]]", "[[zk-rollup]]", "[[defi]]"]
---

# DeGate

**DeGate** (token **DG**) is a decentralized **order-book** [[decentralized-exchange|exchange]] built as a [[zk-rollup|ZK-rollup]] on [[ethereum|Ethereum]]. It aims to deliver a centralized-exchange-like trading experience — limit orders, grid trading, and an order book — with the self-custody and Ethereum-level security of a [[defi|DeFi]] protocol, while using zero-knowledge proofs to keep fees and latency low. DG trades at **$0.04225352**, ranking **#913** by market capitalization (~**$16.36M** market cap), flat over 24h (**0.00%**) and essentially flat over 7 days (**-0.12%**).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Most large decentralized exchanges (e.g., [[uniswap|Uniswap]]) use the [[automated-market-maker|automated-market-maker (AMM)]] model, which is simple but suffers from [[slippage]] and gives traders no real limit-order control. DeGate takes the opposite approach: it runs a **non-custodial order-book DEX** where users place limit and grid orders just as they would on a centralized exchange ([[cex|CEX]]), but funds remain in the user's control and settlement is enforced on Ethereum.

DeGate is structured as a community-owned **DAO**, with the protocol marketed under the tagline of a "self-custodial trading platform" offering a familiar limit-order experience without surrendering keys.

---

## Architecture — How DeGate Works

DeGate is a **ZK-rollup order-book DEX**. The design separates *where orders are matched* (off-chain, by a sequencer/operator) from *where settlement is proven* (on-chain, on Ethereum L1). The three pillars:

**1. ZK-rollup execution layer.** Orders, trades, deposits, and withdrawals are batched and executed off-chain. The operator then generates a **zero-knowledge validity proof** ([[zk-snark|zk-SNARK]]) attesting that the entire batch of state transitions was computed correctly, and posts that proof plus a state commitment to an on-chain rollup contract. Because Ethereum verifies the proof rather than re-executing every trade, DeGate inherits L1 security (the chain cannot accept an invalid state) while keeping per-trade cost and latency far below trading directly on L1. This is **validity-proof** security, distinct from the fraud-proof / challenge-period model used by [[optimistic-rollup|optimistic rollups]] — withdrawals do not require a 7-day dispute window.

**2. Account-based, non-custodial design.** Users deposit assets into the rollup, where balances are tracked in a Merkle-tree state. Trading happens against this off-chain state, but the *only* way assets leave is via a proven withdrawal — the operator can never move user funds to itself. DeGate's lineage traces to **Loopring**'s zkRollup order-book technology; both share the model of an order book settled by validity proofs.

**3. Censorship resistance and the escape hatch.** Because rollups rely on an operator to order and prove transactions, the critical question is *what happens if the operator goes rogue or offline*. DeGate implements a **force-withdrawal / escape-hatch** mechanism: if the operator stops processing, users can submit an on-chain request and, after a timeout, directly withdraw their funds from the rollup contract using a Merkle proof of their balance — bypassing the operator entirely. The protocol also emphasizes that core security contracts are designed to be **non-upgradable** so that no admin key can alter rules out from under users.

### Trading features (CEX-like)

- **Limit orders** — true price-time limit orders, not just AMM swaps.
- **Grid trading** — automated grid bots that place a ladder of buy/sell orders across a range, a popular range-bound strategy (see [[grid-trading]]).
- **Order-book UI** — depth charts and an order book aimed at active traders who find [[automated-market-maker|AMMs]] limiting.
- **Gas abstraction** — fees can be paid in the traded token rather than requiring separate ETH for gas.

---

## Token Role: DG

- **Governance** — DG is the governance token of the DeGate DAO; holders vote on protocol parameters, treasury allocation, and roadmap.
- **Incentives** — DG is used to incentivize trading activity and bootstrap liquidity on the exchange.
- **Value alignment** — as an exchange token, DG's fundamental backing is the **fee throughput** of the DeGate order book; sustained volume is what gives the token underlying support. Unlike a base-layer gas token, DG does not secure the rollup itself (proof verification and Ethereum L1 do that), so its accrual is governance- and incentive-driven rather than security-driven.

The supply structure is a structural headwind: circulating supply (~387M) sits well below the 1B max, giving a market-cap / FDV ratio of ~0.39 — meaning roughly 60% of fully diluted value is not yet circulating and future unlocks dilute holders.

---

## Comparison vs Competitors

DeGate sits at the intersection of two competitive fields: ZK-rollup infrastructure and decentralized exchanges. It competes most directly with other order-book / self-custody DEX designs.

| Protocol | Model | Settlement / chain | Order type | Differentiator |
|---|---|---|---|---|
| **DeGate** (DG) | ZK-rollup order book | Validity proofs to Ethereum L1 | Limit, grid, order book | CEX-style limit orders + escape-hatch self-custody |
| **[[loopring]]** (LRC) | ZK-rollup order book / AMM | Validity proofs to Ethereum L1 | Order book + AMM pools | Closest architectural cousin; earlier mover |
| **[[dydx]]** (DYDX) | App-chain order book | Cosmos app-chain (v4) | Perps order book | Off-chain matching, perps focus, own chain |
| **[[uniswap]]** (UNI) | AMM | Ethereum L1 + L2s | Swap (no limit book) | Deepest liquidity, but slippage and no native limit orders |

DeGate's differentiator is the combination of a **true CEX-style order book with ZK-rollup self-custody and a force-withdrawal guarantee**. Its constraint is liquidity: order-book venues need deep two-sided liquidity to be useful, and bootstrapping that on an L2 against incumbent AMMs and CEXs is hard — reflected in DeGate's very thin trading volume (~$36k/24h at the snapshot).

---

## How & Where It Trades

DG is an Ethereum ERC-20 (contract `0x53c8...dede`). Per the CoinGecko snapshot it trades almost entirely **on-chain via Uniswap V2** (DG/USDC) with negligible centralized-exchange depth. Practical implications:

- **Liquidity is extremely thin** — ~$36k of 24h volume against a ~$16M cap means even modest orders move price; expect wide effective spreads and high [[slippage]].
- **No deep derivatives market** — there is no meaningful perp/futures venue for DG; exposure is spot-only.
- **Execution** — buying requires an Ethereum wallet and tolerance for L1 gas plus DEX [[slippage]]; size into limit-style fills rather than market orders.

---

## Narrative, Category & Catalysts

DG belongs to the **ZK-rollup / order-book DEX** narrative — a niche that gets attention in "real DeFi vs CEX" cycles when self-custody concerns spike (e.g., after centralized-venue failures). Potential catalysts: meaningful growth in DeGate order-book volume, new chain or asset listings, DAO incentive programs, and any broad rotation back into ZK / Ethereum-L2 themes. In the current **Established Bear Market** (Fear & Greed 21, Extreme Fear; ETH ~26% below its 200-day MA as of 2026-06-22), appetite for low-liquidity infrastructure microcaps is depressed.

---

## History / Timeline

- **All-time high $0.6019** recorded **2021-03-20** (per CoinGecko price history) during the prior cycle.
- **All-time low $0.0130** on **2023-09-13**.
- DG now sits ~93% below its 2021 ATH.

> *Other protocol-milestone dates are not independently verified in an ingested source and are intentionally omitted rather than invented.*

---

## Risks

- **Liquidity risk** — order-book DEXs are only as good as their depth; ~$36k daily volume means wide spreads, high [[slippage]], and difficulty exiting size.
- **ZK-rollup / smart-contract risk** — the proving system, rollup contracts, and bridge are complex; a bug in the prover or settlement contract could threaten funds despite escape-hatch design.
- **Operator/sequencer dependence** — like most rollups, DeGate relies on an operator for ordering; censorship resistance ultimately depends on the force-withdrawal mechanism working as intended in a live failure.
- **Token/dilution risk** — circulating supply (~387M) is well below max supply (1B), MC/FDV ~0.39; future unlocks are a structural headwind.
- **Market backdrop** — the 2026-06-22 environment is risk-off ([[bitcoin|BTC]] ~$64,160, ~16% below its 200-day MA; Fear & Greed 21, "Extreme Fear"), which compresses liquidity and demand for infrastructure microcaps.

> *Informational only, not investment advice. Crypto assets are highly volatile.*

---

## Trading Playbook (bear / Extreme-Fear regime)

- **Regime:** Established Bear Market, Extreme Fear (F&G 21). Low-liquidity infra microcaps like DG carry amplified downside and gap risk; this is a capital-preservation regime.
- **If trading at all:** size tiny, use limit orders into the order book (never market orders) to control [[slippage]], and pre-define an invalidation level given how fast thin tokens reprice.
- **Bull-case trigger:** treat sustained growth in *actual order-book volume/TVL* — not price alone — as the fundamental signal; a token whose only backing is fee throughput needs the fees to materialise.
- **Watch:** broad ZK/L2 narrative rotation and any return of risk appetite (F&G out of Extreme Fear) before assuming durable strength.

> *Not investment advice.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DG |
| **Market Cap Rank** | #913 |
| **Market Cap** | $16,361,251 |
| **Current Price** | $0.04225352 |
| **24h Change** | 0.00% |
| **7d Change** | -0.12% |
| **Categories** | Decentralized Exchange (DEX), Decentralized Finance (DeFi), Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK) |
| **Website** | [https://degate.com/](https://degate.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 387.22M DG |
| **Total Supply** | 1.00B DG |
| **Max Supply** | 1.00B DG |
| **Fully Diluted Valuation** | $43.97M |
| **Market Cap / FDV Ratio** | 0.39 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.6019 (2021-03-20) |
| **Current vs ATH** | -92.70% |
| **All-Time Low** | $0.0130 (2023-09-13) |
| **Current vs ATL** | +238.92% |
| **24h Change** | -1.04% |
| **7d Change** | -0.53% |
| **30d Change** | -4.65% |
| **1y Change** | -35.32% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x53c8395465a84955c95159814461466053dedede` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X53C8395465A84955C95159814461466053DEDEDE/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://degate.com/](https://degate.com/) |
| **Discord** | [https://discord.gg/degate](https://discord.gg/degate) |
| **GitHub** | [https://github.com/degatedev](https://github.com/degatedev) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $36,195.00 |
| **Market Cap Rank** | #917 |
| **24h Range** | $0.0438 — $0.0447 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-exchange]]
- [[zk-rollup]]
- [[automated-market-maker]]
- [[loopring]]
- [[dydx]]
- [[grid-trading]]
- [[slippage]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; ZK-rollup order-book architecture from public DeGate documentation. No additional specific wiki source ingested yet.
