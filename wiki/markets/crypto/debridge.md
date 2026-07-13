---
title: "deBridge"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["DBR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://debridge.com"
related: ["[[crypto-markets]]", "[[solana]]", "[[ethereum]]", "[[cross-chain]]", "[[bridge]]", "[[cross-chain-bridge]]", "[[decentralized-exchange]]"]
---

# deBridge

**deBridge** (DBR) is a cross-chain interoperability and liquidity-transfer protocol that moves value and data between blockchains without locked liquidity or wrapped-asset pools. Instead of a traditional lock-and-mint bridge, deBridge uses an **intent-based** model in which solvers/market-makers fill cross-chain orders at guaranteed rates, settling near-instantly. DBR is the protocol's governance token; its native chain is [[solana|Solana]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | DBR |
| **Chain** | [[solana\|Solana]] (native); also [[ethereum\|Ethereum]] and other EVM chains |
| **Current Price** | $0.0143356 |
| **Market Cap** | $76.34M |
| **Market Cap Rank** | #327 |
| **24h Volume** | $1.28M |
| **24h Change** | +3.42% |
| **7d Change** | -7.73% |
| **Fully Diluted Valuation** | $143.35M |
| **Market Cap / FDV** | ~0.53 |
| **All-Time High** | $0.05521 (2024-12-22) |
| **All-Time Low** | $0.012388 (2026-04-19) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Trading context: the market is in **extreme fear** ([[crypto-fear-and-greed-index|Fear & Greed]] = 23) within an **established bear market** as of 2026-06-21. DBR trades near its all-time low set in April 2026 (~$0.0124), with the -7.7% weekly move underlining bridge/infrastructure-token weakness in this regime. Daily volume of ~$1.28M against a $76.34M cap is thin (~1.7% velocity) — the lowest turnover ratio in this cohort — so exit liquidity is poor for size and the token is the **best-ranked** of the six by market cap (#327) yet among the least actively traded.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~5.33B DBR |
| **Total Supply** | 10.00B DBR |
| **Max Supply** | 10.00B DBR |
| **Market Cap / FDV** | ~0.53 |

About half of max supply is circulating, so meaningful unlock-driven dilution remains. DBR is a **bridge governance token**, used to steer protocol parameters and fee policy. Because deBridge holds **zero locked TVL** (no pooled liquidity sitting in the protocol), its token does not derive value from staked collateral the way lock-and-mint bridges do; value accrual is tied to protocol fee capture and governance over the routing/solver network.

---

## Technology — intent-based cross-chain settlement

deBridge is **messaging-and-settlement infrastructure** rather than a pooled [[bridge]]. Its design deliberately avoids the lock-and-mint architecture responsible for most of crypto's largest [[cross-chain-bridge|bridge]] hacks:

- **deBridge Liquidity Network (DLN)** — an intent-based [[cross-chain]] order system. A user posts an order ("send X on chain A, receive Y on chain B at this rate"); independent **solvers/market-makers** compete to fill it, fronting their own liquidity. There is **no shared liquidity pool to drain**, which structurally reduces the classic bridge-hack attack surface — there is no honeypot of pooled TVL.
- **Guaranteed rates / no slippage from pools** — because solvers quote a fixed fill, users get a guaranteed receive amount rather than AMM slippage. Orders that no solver fills simply expire and the user is made whole.
- **Generic message passing (deBridge Messaging)** — beyond value transfer, deBridge can relay arbitrary cross-chain messages/data, enabling cross-chain dApps, governance, and composable workflows.
- **Solver economics** — solvers earn the spread/fee for providing instant liquidity and bear the inventory and finality risk of bridging, similar to fast-bridge "filler" models. The protocol's validators/oracles attest to source-chain events so solvers can be reimbursed on settlement.

Because deBridge holds **zero locked TVL**, the systemic risk migrates from "pool exploit" to **messaging-layer correctness and solver/finality assumptions** — a different, arguably smaller, attack surface than pooled bridges.

---

## Market Structure & Derivatives

### Spot venues for the DBR token
- **Centralized:** Kraken (DBR/EUR), Bitget (DBR/USDT), KuCoin (DBR/USDT), Crypto.com (DBR/USD).
- **Decentralized:** Orca on [[solana|Solana]] (DBR/SOL spot).

DBR is a mid-small-cap infra token; deep derivatives markets (perp OI, funding) are **not** a material data point at this snapshot — there is no flagship DBR perp with persistent liquidity. The economically meaningful activity is cross-chain transfer **volume routed through DLN**, not DBR-token derivatives. With ~$1.28M daily spot volume, exit liquidity is thin and slippage can be material for size.

### Contract address
| Chain | Address |
|---|---|
| [[solana\|Solana]] | `DBRiDgJAMsM95moTzJs7M9LnkGErpbv9v6CUR1DXnUu5` |

---

## Use Case / Narrative / Category

deBridge sits in the **interoperability / [[cross-chain]] liquidity** category — a space defined by the tension between user demand for seamless multi-chain movement and the catastrophic hack history of pooled bridges. Its narrative is "bridging without bridge risk": by removing locked liquidity and using solver-fronted intents, it aims to be the routing layer for cross-chain swaps, intents, and messaging across [[solana|Solana]] and EVM ecosystems. It competes in the broader intent/solver-network thesis alongside other cross-chain messaging and fast-bridge protocols.

### Peer comparison — cross-chain / interoperability

| Protocol | Token | Model | Locked TVL | Native chain |
|---|---|---|---|---|
| **deBridge** | **DBR** | **Intent-based, solver-fronted (DLN)** | **None** | **[[solana\|Solana]]** |
| LayerZero | ZRO | Omnichain messaging (DVNs) | None (messaging) | Multi-chain |
| Wormhole | W | Guardian-attested messaging + bridges | Wrapped-asset exposure | Multi-chain |
| Across | ACX | Intent-based fast bridge (relayers) | Hub-pool liquidity | [[ethereum\|Ethereum]] |
| Axelar | AXL | Validator-set general message passing | Gateway contracts | Cosmos |

deBridge's differentiator within this set is the **pool-free, intent-and-solver** model with native Solana roots and generic message passing, positioning it closest to LayerZero (messaging) and Across (intent bridging) while structurally avoiding the wrapped-asset/pool exposure of Wormhole-style designs.

### Valuation framing (qualitative)

DBR has the **best market-cap rank in this cohort (#327)** at ~$76M, but a ~$143M FDV (MC/FDV ~0.53) means roughly half of max supply is still to unlock — a meaningful dilution overhang. Because the protocol holds zero locked collateral, token value accrues purely through **fee capture on routed volume and governance**, not staked TVL; the bull case is that DBR becomes the default cross-chain routing layer for the Solana↔EVM corridor as multi-chain activity recovers. The bear case is intense competition (LayerZero, Wormhole, Across, Axelar), fee compression among solvers, and trading near ATL with thin volume in a risk-off regime where cross-chain volume itself contracts.

---

## Notable History

- DBR's all-time high of **$0.0552** came on 2024-12-22, around its token launch/listing wave.
- The all-time low of **$0.0124** was set on 2026-04-19, during the broad market downturn.
- As of 2026-06-21 DBR trades ~74% below ATH and only marginally above its ATL, reflecting sustained pressure on bridge/infra tokens through the bear market.

---

## Risks

- **Cross-chain / solver risk** — while there is no shared liquidity pool to exploit, the protocol still relies on solver honesty, correct finality assumptions, and secure message verification; a flaw in the messaging layer is the key systemic risk.
- **Liquidity risk** — ~$1.8M/24h spot volume is modest; slippage and exit liquidity can be poor for size.
- **Competition** — interoperability is crowded; fee compression and solver competition can erode protocol economics.
- **Token dilution** — roughly half of max supply still to unlock.
- **Smart-contract risk** — bridge/messaging contracts remain high-value targets industry-wide.
- **Regime risk** — cross-chain volume and infra valuations tend to fall in risk-off markets like the current one ([[crypto-fear-and-greed-index|Fear & Greed]] 23).

---

## Related

- [[crypto-markets]]
- [[solana]]
- [[ethereum]]
- [[cross-chain]]
- [[bridge]]
- [[cross-chain-bridge]]
- [[decentralized-exchange]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000).
- General market knowledge; no specific wiki source ingested yet.
