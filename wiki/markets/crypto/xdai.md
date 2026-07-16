---
title: "XDAI"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["XDAI", "xDai"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.gnosischain.com"
related: ["[[crypto-markets]]", "[[dai]]", "[[gnosis]]", "[[stablecoins]]"]
---

# XDAI

**xDai (XDAI)** is the native gas and payments token of [[gnosis|Gnosis Chain]] (formerly the xDai Chain), an [[ethereum|Ethereum]] sidechain. It is a USD-pegged [[stablecoins|stablecoin]] that doubles as the chain's gas currency: every transaction on Gnosis Chain is paid in xDai, and the value targets ~$1.00 per token. As of the latest snapshot it ranks **#337** by market capitalization. xDai is unusual among stablecoins in that it is a **native chain coin** (like ETH on Ethereum), not an ERC-20 — its dollar peg comes from a 1:1 bridge against an underlying Ethereum-side stablecoin rather than from its own reserve.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | XDAI |
| **Peg target** | US Dollar (~$1.00) |
| **Issuer / chain** | Gnosis Chain (native gas token) |
| **Current price** | $0.999815 |
| **Market cap** | $74.76M |
| **Market cap rank** | #337 |
| **24h volume** | $170,423 |
| **Circulating supply** | 74.78M XDAI |
| **Total supply** | 74.78M XDAI |
| **24h change** | +0.02% |
| **7d change** | +0.01% |
| **All-time high** | $9.92 (2023-01-29) |
| **All-time low** | $0.17845 (2022-09-09) |

The token is holding its peg almost perfectly ($0.9998), consistent with a healthy 1:1 bridge. The $9.92 ATH is a historical data artifact from a thin early market rather than a genuine valuation, and the price has been essentially flat at $1 for an extended period.

---

## Architecture — peg & backing mechanism

xDai is created when value is bridged from [[ethereum|Ethereum]] to [[gnosis|Gnosis Chain]] via the chain's stablecoin bridge. Each xDai on Gnosis Chain is meant to be backed 1:1 by the underlying collateral locked in the bridge contract on Ethereum (historically [[dai|Dai (DAI)]], MakerDAO's overcollateralized crypto-backed stablecoin). Because xDai is the chain's native coin (not an ERC-20 deployed *on* Gnosis Chain), it is used directly to pay gas, similar to how ETH is used on Ethereum.

- **Collateral / reserve model**: xDai holds **no reserve of its own**. Its dollar value is fully *derivative* — it is a **bridge-wrapped representation** of an Ethereum-side stablecoin locked in the bridge contract. The reserve is the locked DAI (and, in practice, other bridged dollars routed through the chain's stablecoin infrastructure). The peg therefore inherits the design and risk of whatever stablecoin backs the bridge.
- **Mint / burn (peg) mechanism**: lock the underlying stablecoin in the Ethereum-side bridge → an equal amount of xDai is **minted** on Gnosis Chain. Bridge back → xDai is **burned** and the underlying is released on Ethereum. This 1:1 mint/burn bridge **is** the peg mechanism — there is no central redeemer setting price, and no over-collateralization buffer at the xDai layer itself.
- **Redemption / gating**: redemption is permissionless via the bridge (subject to bridge availability and fees); the peg is enforced by **bridge arbitrage** — if xDai trades below $1 on a venue, arbitrageurs buy it and bridge out for $1 of the underlying, and vice versa.
- **Yield**: xDai itself is a non-yielding gas coin. (Gnosis separately offers staking and the GNO ecosystem; xDai's role is settlement/gas, not yield.)
- **Stability**: as a soft-pegged, bridge-backed dollar, xDai's peg ultimately depends on (1) the **solvency/peg of the bridged collateral**, (2) the **integrity of the bridge validators/contract**, and (3) the bridge remaining open. A failure of any of the three — not a reserve shortfall at xDai — is what would break the peg.

### Comparison vs peer dollars / bridged dollars

| Token | Type | Backing | Peg risk vs xDai |
|---|---|---|---|
| **xDai** | Bridge-wrapped native gas coin | Ethereum-side locked stablecoin (DAI) | **Bridge** is the single point of failure; inherits backing's peg |
| **[[dai]]** | Crypto-collateralised CDP | Over-collateralised crypto + RWA | The asset xDai wraps; xDai adds bridge risk on top |
| **Bridged [[usdc]] (USDC.e)** | Bridge-wrapped fiat dollar | Locked native USDC | Same bridge-dependency pattern, different underlying |
| **[[usdt]] / [[usdc]] (native)** | Off-chain fiat + T-bills | Issuer reserves | No bridge layer; centralised custody instead |

The key conceptual point: xDai is **"DAI plus bridge risk."** It is only as safe as the weaker of {its underlying stablecoin's peg, the Gnosis bridge}.

---

## How / where it trades

Most xDai is not traded on centralized exchanges — it lives on [[gnosis|Gnosis Chain]] where it functions as gas and as the base currency for the chain's DeFi ecosystem (Honeyswap, Curve on Gnosis, Balancer/Aura on Gnosis, etc.). On-chain liquidity is the primary venue; centralized-exchange listings are minimal.

- **DeFi composability**: as the chain's native unit, xDai is the **base settlement and gas asset** for essentially all Gnosis-Chain DeFi — it is paired across the chain's DEX pools and used as collateral/quote in lending and stableswap venues. Its utility is *internal* to the Gnosis ecosystem rather than cross-chain.
- **Reported 24h volume is thin (~$170K)**, consistent with a coin whose main use is on-chain settlement rather than speculative trading. Treat off-chain order books as low-liquidity.
- Acquired primarily by **bridging into Gnosis Chain** (locking DAI/stablecoin on Ethereum) rather than buying on an exchange.

---

## Narrative / category & catalysts

xDai's "narrative" is **infrastructure, not speculation** — it is the plumbing of a payments-and-DAO-oriented sidechain, not a momentum altcoin. Gnosis Chain's positioning (cheap, fast, stable-denominated gas) made it a hub for **DAOs, prediction-market and payments use cases** (e.g. Gnosis Pay, the self-custodial Visa card settling on Gnosis Chain).

- **Catalysts (relevant ones):** growth of Gnosis-Chain activity and Gnosis Pay adoption (more real-world settlement → more xDai in circulation); health of the underlying bridged stablecoin; bridge security upgrades.
- **What it is *not*:** there is no token-unlock, no FDV-overhang trade, and no expectation of price appreciation — by design xDai should stay at $1. The only "price" events that matter are **de-peg events** (bridge or collateral failure).

---

## History / Timeline

| Date | Event |
|---|---|
| **2018–2020** | xDai Chain launches as an Ethereum stablecoin sidechain using a DAI-backed bridge; xDai becomes its native gas coin. |
| **2021** | Project rebrands/merges into the **[[gnosis|Gnosis]]** ecosystem; the chain becomes **Gnosis Chain**, xDai remains the native gas coin. |
| **2022-09-09** | Recorded all-time **low ~$0.17845** — a thin-market data artifact rather than a genuine collapse of the bridge peg. |
| **2023-01-29** | Recorded all-time **high ~$9.92** — likewise an early/thin-market data artifact, **not** a real $9.92 valuation of a $1-pegged coin. |
| **2026-06-21** | Holds peg almost perfectly at **~$0.9998** on thin ~$170K volume — normal behaviour for a settlement coin. |

> **Data-artifact flag:** the $9.92 ATH and $0.178 ATL are **historical data noise** from a thin early market and ticker artifacts, not real peg breaks. xDai has otherwise traded as a tight ~$1 asset; treat those extremes as non-economic.

---

## Trading playbook

- **Hold as gas/settlement, not as a trade.** xDai is acquired by bridging and used to pay Gnosis-Chain fees or to transact in Gnosis DeFi; there is no appreciation thesis and minimal CEX liquidity. It is closest in spirit to "ETH for paying gas," but dollar-denominated.
- **The only real risk to price is a de-peg.** Because xDai is bridge-wrapped DAI, the trade/risk that matters is **bridge or collateral failure** (see Risks). Monitor the Gnosis bridge's security posture and the underlying stablecoin's peg, not price momentum.
- **Macro framing (2026-06-23).** Broad crypto is in **Extreme Fear** (Fear & Greed 21; market-health 29/100, bearish). xDai itself is holding peg, but bear-market stress raises the general risk that cross-chain bridges are probed/exploited and that DeFi collateral is strained — the relevant tail risk for any bridge-backed dollar.

---

## Risks

- **De-peg risk**: a failure or exploit of the Gnosis Chain bridge, or insolvency of the underlying collateral, could break the 1:1 backing and send xDai below $1.
- **Collateral risk**: peg quality depends on the underlying bridged stablecoin (e.g. DAI/USDC) maintaining its own peg; a de-peg there propagates to xDai.
- **Bridge / smart-contract risk**: bridge validators and contracts are a single point of failure; cross-chain bridges have historically been a major target for exploits.
- **Liquidity risk**: very thin external trading volume means large redemptions or exits must go through the bridge or shallow on-chain pools, risking slippage.
- **Regulatory risk**: USD-pegged stablecoins face evolving global regulation that could affect issuance, bridging, or redemption.
- **Macro backdrop**: the broader market sits in an "Established Bear Market" (Fear & Greed Index 23), which raises stress on DeFi collateral and bridge usage generally, even though xDai itself is holding peg.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 74.78M XDAI |
| **Total Supply** | 74.78M XDAI |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Platform & Chain Information

**Native Chain:** Gnosis Chain (xDai)

### Contract Addresses

| Chain | Address |
|---|---|
| Gnosis Chain | `0xe91d153e0b41518a2ce8dd3d7944fa863463a97d` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.gnosischain.com](https://www.gnosischain.com) |
| **Twitter** | [@gnosischain](https://twitter.com/gnosischain) |
| **Telegram** | [gnosischain](https://t.me/gnosischain) |
| **Discord** | [https://discord.gg/VQb3WzsywU](https://discord.gg/VQb3WzsywU) |
| **GitHub** | [https://github.com/xdaichain](https://github.com/xdaichain) |

---

## Related

- [[stablecoins]]
- [[dai]] — the underlying stablecoin xDai wraps via the bridge
- [[gnosis]] — host chain and ecosystem
- [[ethereum]] — Ethereum-side bridge collateral lives here
- [[usdc]], [[usdt]] — peer fiat dollars
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]

---
