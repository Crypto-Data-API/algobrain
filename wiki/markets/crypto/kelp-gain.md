---
title: "Kelp Gain"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["AGETH", "Kelp Gain", "agETH", "KelpDAO Gain"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://kelpdao.xyz/gain/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[liquid-restaking]]", "[[liquid-staking]]", "[[rseth]]", "[[eigenlayer]]", "[[restaking]]", "[[slashing]]", "[[lido]]", "[[uniswap]]", "[[2026-04-18-kelp-layerzero-exploit]]", "[[2026-04-kelp-stable-sympathy-depeg]]", "[[rpc-poisoning]]", "[[dvn-compromise-patterns]]", "[[2026-exploit-target-watchlist]]"]
---

# Kelp Gain

**Kelp Gain** (agETH) is an **auto-compounding [[liquid-restaking|liquid-restaking]] "gain" token** from **KelpDAO**, built on top of Kelp's [[rseth|rsETH]] [[liquid-restaking|liquid-restaking token (LRT)]] on [[ethereum|Ethereum]]. Users deposit ETH or its variants (rsETH, ETHx, stETH) and receive **agETH**, a single token that automatically routes the underlying restaked ETH across multiple Layer 2 networks and DeFi protocols to capture rewards, airdrops, and yield — with the gains accruing into the token's value rather than being paid out separately.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, agETH traded at **$3,239.91**, ranked **#616** by market capitalization with a market cap of **$32,258,310**. Its 7-day change was **0.00%** (24h change not available in this snapshot). The high per-token unit price (~$3,239.91) is not a typo or a speculative premium — it reflects **accumulated ETH value**: agETH is a value-accrual (auto-compounding) token whose redemption value rises as restaking and DeFi rewards compound into it, so one agETH is worth roughly the value of more than one ETH-equivalent of underlying restaked assets.

> **April 2026 incident:** KelpDAO's `rsETH` LayerZero OFT bridge was exploited on April 18, 2026 for ~$290M direct loss; ~$15B TVL drain across DeFi within 48h. Mechanism: 1-of-1 [[dvn-compromise-patterns|DVN compromise]] via [[rpc-poisoning|RPC poisoning + DDoS]]. Full post-mortem: [[2026-04-18-kelp-layerzero-exploit]]. Sympathy-depeg trade: [[2026-04-kelp-stable-sympathy-depeg]].

---

## What agETH Is

agETH is KelpDAO's automated **yield-aggregation layer for restaked ETH**. The mechanism stacks three layers of yield:

1. **Ethereum staking** — the base ETH earns consensus-layer staking rewards.
2. **Restaking** ([[eigenlayer|EigenLayer]] via [[rseth|rsETH]]) — the staked ETH is re-pledged to secure additional services (Actively Validated Services), earning restaking rewards on top. See [[liquid-restaking]] and [[restaking]].
3. **DeFi / L2 reward strategies** — agETH deploys the restaked position across Layer 2s and DeFi protocols for additional rewards and airdrop farming.

Because agETH **auto-compounds** these rewards back into the token (value-accrual model), holders do not receive a stream of new tokens or rebasing balances; instead each agETH steadily grows in underlying ETH value. This is why the unit price sits well above 1 ETH-equivalent in dollar terms.

### Yield accrual and withdrawals

- **Yield model:** value-accrual / auto-compounding — agETH appreciates against ETH as layered rewards compound in.
- **Redemption:** unwinding agETH back to ETH passes through the restaking and Ethereum staking **withdrawal/exit queues** (EigenLayer escrow plus the Ethereum validator exit queue), so native redemption is not instant. For immediate liquidity, holders swap agETH on secondary markets (e.g., [[uniswap|Uniswap V3]]), where it can trade at a premium or discount to its NAV.

### Architecture deep-dive: the yield-aggregation wrapper

agETH is best understood as a **wrapper-of-a-wrapper**: it sits one layer above [[rseth|rsETH]] (Kelp's base LRT), which itself sits above [[eigenlayer|EigenLayer]] restaking, which sits above Ethereum staking. Each layer adds yield and risk:

- **Base layer — ETH staking.** Consensus-layer issuance + priority fees/MEV (~3-4% historically).
- **Restaking layer — rsETH / EigenLayer.** The same ETH is re-pledged to secure Actively Validated Services (AVSs), earning additional AVS rewards and points. This is the [[restaking|restaking]] thesis and the source of the *added* slashing surface.
- **Aggregation layer — agETH.** Kelp's "gain" strategy actively routes the restaked position across Layer-2s and DeFi protocols to harvest incentives, airdrops, and yield, then **auto-compounds** the proceeds back into NAV. The token balance stays fixed; the agETH→ETH redemption rate rises.

Because agETH is a NAV-accruing (non-rebasing) token, its **dollar unit price (~$3,240) is mechanically high** — it represents more than one ETH-equivalent of underlying value, not a speculative premium. This is the same accounting as wstETH or [[rseth|rsETH]] in its wrapped form. The composability cost is that agETH inherits the **full stacked attack surface** of every protocol it touches — a point the April 2026 LayerZero/DVN exploit made concrete.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | agETH |
| **Protocol type** | Auto-compounding [[liquid-restaking|liquid-restaking]] gain token (KelpDAO) |
| **Built on** | [[rseth|rsETH]] LRT / [[eigenlayer|EigenLayer]] restaking on [[ethereum|Ethereum]] |
| **Accepted deposits** | ETH, rsETH, ETHx, stETH |
| **Market Cap Rank** | #616 |
| **Market Cap** | $32,258,310 |
| **Current Price** | $3,239.91 (reflects accumulated ETH value) |
| **24h Change** | n/a (not in snapshot) |
| **7d Change** | 0.00% |
| **Native Chain** | [[ethereum|Ethereum]] |
| **Categories** | DeFi, Ethereum Ecosystem, Restaking |
| **Website** | [https://kelpdao.xyz/gain/](https://kelpdao.xyz/gain/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 12,873 AGETH |
| **Total Supply** | 12,873 AGETH |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

agETH is **not a fixed-supply speculative token**: supply expands and contracts with deposits and redemptions (mint on deposit, burn on withdrawal), so "circulating = total" and **MC/FDV = 1.00** by construction. There is no emission schedule or unlock overhang — the supply simply mirrors how much ETH is wrapped into the strategy. Market cap therefore tracks **TVL**, not a token-valuation narrative. The relevant "tokenomics" are the underlying yield, the safety of the strategy, and how tightly secondary-market price tracks NAV.

### Value Accrual & Governance

Value accrues to agETH holders purely through **NAV appreciation** — there is no fee token to capture, no governance vote attached to agETH itself, and no inflation. KelpDAO governance (and any fee take-rate on the gain strategy) sits with the broader Kelp protocol and its governance token (KEP/Kelp ecosystem), not with agETH. Holders are simply long a managed, auto-compounding restaked-ETH position; their "return" is the realized layered yield minus protocol fees and minus any losses from the stacked risks below.

---

## Comparison vs Liquid-Restaking / Yield-ETH Peers

| Token | Issuer | Type | Yield stack | Notes |
|---|---|---|---|---|
| **agETH (Kelp GAIN)** | KelpDAO | Auto-compounding LRT "gain" vault | Staking + restaking + DeFi/L2 incentives | NAV-accruing wrapper on rsETH; April 2026 bridge exploit |
| **[[rseth\|rsETH]]** | KelpDAO | Base liquid-restaking token | Staking + EigenLayer restaking | Kelp's core LRT (agETH's substrate) |
| **[[eigenlayer\|eETH / weETH (ether.fi)]]** | ether.fi | Liquid-restaking token | Staking + restaking + points | Largest LRT by TVL historically |
| **[[lido\|wstETH (Lido)]]** | Lido | Liquid-staking token | Staking only | Deepest liquidity; **no restaking layer** (lower risk, lower yield) |

The trade-off across this ladder is monotonic: **more layers = more yield + more risk**. wstETH is the conservative benchmark (pure staking, deepest liquidity). rsETH adds restaking risk. **agETH adds a further DeFi/L2/airdrop-strategy layer on top of rsETH**, so it sits at the highest-yield, highest-risk end of the spectrum — which is exactly why the April 2026 bridge exploit propagated through it.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe1b4d34e8754600962cd944b535180bd758e6c2e` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XE1B4D34E8754600962CD944B535180BD758E6C2E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## How & Where It Trades

- **Primary liquidity is on-chain DEXs**, chiefly [[uniswap|Uniswap V3]] on Ethereum (agETH/WETH), since agETH is a DeFi position rather than a CEX-listed speculative token. There is no meaningful centralized-exchange or perp market — this is a hold-and-redeem instrument, not a trading vehicle.
- **Two ways out:** (1) **native redemption** to ETH via the EigenLayer escrow + Ethereum validator exit queue (slow, but recovers full NAV); or (2) **secondary swap** on Uniswap (instant, but exposed to the pool's NAV premium/discount and slippage). In stress, these diverge sharply — the redemption path holds par while the secondary price can gap down.
- **Liquidity is thin** (low 24h volume), so the secondary market is the binding constraint in a panic: a rush of holders preferring the instant exit over the slow queue is exactly what produces a depeg, as the related rsETH episode showed.
- **Premium/discount to NAV** is the number to watch, not the dollar price: agETH trading *below* NAV can be an entry for a holder who can tolerate the redemption queue (buy below par, redeem at par), while a persistent discount signals stress or distrust in the strategy.

## Narrative, Category & Catalysts

agETH sits in the **liquid restaking (LRT) / [[eigenlayer|EigenLayer]] yield** narrative — a 2024-2025 mega-theme that drove tens of billions of restaked-ETH TVL. **Catalysts:** rising restaking/AVS rewards, new airdrop campaigns the gain strategy can farm, ETH price appreciation (TVL and yield scale with it), and renewed confidence after the April 2026 incident. **Headwinds (dominant in 2026):** the April 2026 KelpDAO/LayerZero bridge exploit and broader scrutiny of LRT/bridge risk, restaking-yield compression as AVS incentives normalize, and the Extreme-Fear macro regime that suppresses appetite for leveraged-yield ETH wrappers.

---

## Risks and Considerations

agETH stacks staking, restaking, and DeFi yield — which means it stacks the corresponding risks:

- **Layered restaking risk:** [[restaking|Restaking]] re-pledges the same ETH to secure additional services, so failures or [[slashing|slashing]] in any AVS can cascade back to the restaked principal. This is the core added risk versus plain staking.
- **Smart-contract risk:** agETH depends on KelpDAO contracts, [[rseth|rsETH]], [[eigenlayer|EigenLayer]], and every L2/DeFi protocol it routes into — a large, compounded attack surface.
- **Bridge / cross-chain risk (demonstrated):** On 2026-04-18 KelpDAO's rsETH LayerZero OFT bridge was exploited for ~$290M via a 1-of-1 [[dvn-compromise-patterns|DVN compromise]] ([[rpc-poisoning|RPC poisoning + DDoS]]), triggering ~$15B of TVL drain across DeFi within 48h. See [[2026-04-18-kelp-layerzero-exploit]] and the sympathy-depeg case study [[2026-04-kelp-stable-sympathy-depeg]]. This is a concrete, realized example of LRT bridge risk.
- **Depeg / NAV risk:** agETH's secondary-market price can detach from its underlying NAV during stress or thin liquidity (24h volume is very low), as the related rsETH depeg episode illustrated.
- **Withdrawal-queue / liquidity risk:** native redemption runs through EigenLayer escrow and the Ethereum validator exit queue, so exits are slow; in a rush, secondary-market agETH can sell at a discount.
- **Airdrop-farming dependence:** part of the value proposition relies on airdrop/reward strategies that are not guaranteed and can dry up.

> *On-chain holder distribution data requires blockchain analytics integration and is not yet ingested.*

---

## History / Timeline

- **2026-04-09** — agETH appears in the CoinGecko top-1000 snapshot used to seed this page (KelpDAO auto-compounding LRT gain token on [[ethereum|Ethereum]]).
- **2026-04-18** — [[2026-04-18-kelp-layerzero-exploit|KelpDAO / LayerZero Exploit]]: 116,500 rsETH (~$290M) released via a 1-of-1 [[dvn-compromise-patterns|DVN compromise]] ([[rpc-poisoning|RPC poisoning + DDoS]]); ~$15B TVL drain across DeFi within 48h. The realized example of stacked LRT/bridge risk. Companion sympathy-depeg case study: [[2026-04-kelp-stable-sympathy-depeg]].
- **2026-06-21** — Market snapshot: ~$32.26M cap (≈ TVL), price $3,239.91 (NAV-reflecting), 7-day change 0.00%.
- **2026-06-23** — Macro regime read: Extreme Fear (F&G 21), long-horizon Bottoming/Accumulation.

> Only dated events confirmed in ingested sources/snapshots are listed (see the linked exploit post-mortem for the full April 2026 chronology).

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: 2026-06-23 — **Extreme Fear** (F&G 21), long-horizon **Bottoming / Accumulation**; [[ethereum|ETH]] ~$1,737.

- **This is a carry trade, not a directional bet.** agETH is long ETH *plus* layered yield. Your P&L = ETH move + accrued yield − stacked risks. In a bottoming regime, accumulators who want ETH exposure with extra carry may prefer it to spot ETH — but only if they accept the added restaking/DeFi/bridge risk that the April exploit made concrete.
- **NAV discount = the signal.** Watch agETH's secondary price vs. redemption NAV, not the dollar figure. A discount in thin/stressed conditions can be a redemption-arbitrage entry (buy under par, redeem at par over the queue) for patient capital; a persistent discount is a red flag about strategy trust or liquidity.
- **Liquidity & exit planning.** Native redemption is slow (EigenLayer escrow + validator exit queue); the instant Uniswap exit is thin. Plan the exit *before* entering — in a panic you may face the same depeg dynamics that hit rsETH.
- **Risk-stacking discipline.** If you only want ETH staking yield, the lower-risk rung is [[lido|wstETH]] (no restaking). Choose agETH only when the *incremental* yield justifies the *incremental* restaking + bridge + DeFi attack surface — post-exploit, demand a wider margin.
- **Invalidation:** further bridge/contract incidents, restaking-yield compression toward plain-staking levels (removing the reason to take extra risk), or a widening, sticky NAV discount.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kelpdao.xyz/gain/](https://kelpdao.xyz/gain/) |
| **Twitter** | [@KelpDAO](https://twitter.com/KelpDAO) |
| **Telegram** | [KelpDAOxyz](https://t.me/KelpDAOxyz) |

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[liquid-restaking]]
- [[rseth]]
- [[eigenlayer]]
- [[restaking]]
- [[slashing]]
- [[lido]]
- [[uniswap]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- (Source: [[2026-04-18-kelp-layerzero-exploit]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge of KelpDAO's liquid-restaking gain model; see linked incident post-mortems for the April 2026 exploit.
