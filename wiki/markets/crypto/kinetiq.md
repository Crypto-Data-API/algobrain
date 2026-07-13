---
title: "Kinetiq"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, defi]
aliases: ["KNTQ", "Kinetiq", "kHYPE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://kinetiq.xyz/"
related: ["[[crypto-markets]]", "[[liquid-staking]]", "[[hyperliquid]]", "[[hype]]", "[[hyperevm]]", "[[slashing]]"]
---

# Kinetiq

**Kinetiq** (KNTQ) is a [[liquid-staking|liquid-staking]] protocol built natively on [[hyperliquid|Hyperliquid]]. Users stake the native [[hype|HYPE]] token and receive **Kinetiq Staked HYPE (kHYPE)**, a receipt token that earns Hyperliquid staking rewards while remaining liquid and usable across [[hyperevm|HyperEVM]] DeFi. **KNTQ is the protocol's governance/utility token** (CoinGecko classifies it under "Liquid Staking Governance Tokens"); **kHYPE is the separate liquid-staking receipt token** that represents staked HYPE plus accrued rewards.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, KNTQ traded at **$0.192736**, ranked **#424** by market capitalization with a market cap of **$54,048,309**. It was **-0.55% over 24 hours** and **-7.95% over 7 days** — note that this price refers to the **KNTQ governance token**, not the kHYPE receipt token (whose value tracks staked HYPE).

---

## What Kinetiq Is

Kinetiq solves the classic staking trade-off on Hyperliquid: native staking locks up HYPE and forfeits its use elsewhere, while Kinetiq lets users keep liquidity. Two distinct tokens are involved:

- **kHYPE** — the **liquid-staking receipt token**. When a user deposits HYPE, the protocol mints kHYPE representing their stake. kHYPE accrues staking rewards (value-accrual model: the redemption value of kHYPE in HYPE rises over time as rewards compound, rather than the holder receiving new tokens via rebase). kHYPE can be held, traded, or used as DeFi collateral while continuing to earn.
- **KNTQ** — the **protocol governance/utility token**. It is the asset priced and ranked in the market-data snapshot above. It is used for protocol governance and ecosystem incentives and is economically distinct from the staked-HYPE position represented by kHYPE.

### Staking mechanism and validator selection

Behind the scenes, all staked HYPE is delegated to top-performing Hyperliquid validators selected by **StakeHub**, Kinetiq's autonomous validator scoring and delegation system. StakeHub aims to optimize for validator performance and uptime and to diversify delegation, reducing concentration on any single validator. Staking rewards flow back to the pool and accrue to kHYPE holders.

### Yield accrual and withdrawals

- **Yield model:** value-accrual (kHYPE appreciates against HYPE) rather than balance rebasing.
- **Unstaking:** redeeming kHYPE for the underlying HYPE is subject to Hyperliquid's native staking **unbonding/withdrawal queue**, so exits are not instant. Holders who need immediate liquidity instead swap kHYPE on the secondary market, where price can sit at a small premium or discount to its underlying redemption value.

### Architecture deep-dive

Kinetiq is the [[lido|Lido]]-style liquid-staking layer for the [[hyperliquid|Hyperliquid]] ecosystem. Its stack has three moving parts:

1. **Deposit/mint contracts (on [[hyperevm|HyperEVM]])** — accept HYPE, mint kHYPE at the current exchange rate (kHYPE→HYPE rate ≥ 1, rising over time), and manage the withdrawal queue for redemptions.
2. **StakeHub — autonomous validator scoring & delegation.** This is Kinetiq's principal differentiator. Rather than statically delegating to a fixed validator set, StakeHub continuously scores Hyperliquid validators on performance, uptime, commission, and reliability, then routes and rebalances delegation toward the best performers while spreading stake to limit single-validator concentration. The aim is to maximize net staking yield and minimize downtime/[[slashing|slashing]] exposure without manual intervention.
3. **DeFi integration layer** — kHYPE is designed to be composable across HyperEVM DeFi (lending markets, DEX liquidity, collateral), so holders can earn staking yield *and* deploy the same capital — the core liquid-staking value proposition.

Economically, kHYPE follows a **value-accrual (non-rebasing) model** identical in spirit to [[lido|Lido]]'s wstETH or [[rocket-pool]]'s rETH: the token balance is fixed, and accrued staking rewards push up the kHYPE→HYPE redemption rate. This makes kHYPE clean to integrate as DeFi collateral (no surprise balance changes) but means the "yield" is realized through price appreciation against HYPE, not visible token drips.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KNTQ (governance token) |
| **Receipt token** | kHYPE (staked HYPE) |
| **Protocol type** | [[liquid-staking|Liquid staking]] on [[hyperliquid|Hyperliquid]] |
| **Market Cap Rank** | #424 |
| **Market Cap** | $54,048,309 |
| **Current Price (KNTQ)** | $0.192736 |
| **24h Change** | -0.55% |
| **7d Change** | -7.95% |
| **Native Chain** | [[hyperevm|HyperEVM]] |
| **Categories** | DeFi, Liquid Staking Governance Tokens, Liquid Staking, HyperEVM Ecosystem |
| **Website** | [https://kinetiq.xyz/](https://kinetiq.xyz/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics (KNTQ)

| Metric | Value |
|---|---|
| **Circulating Supply** | 270.00M KNTQ |
| **Total Supply** | 1.00B KNTQ |
| **Max Supply** | 1.00B KNTQ |

With ~270M of 1.00B circulating (**MC/FDV ≈ 0.27**), roughly **73% of KNTQ supply is uncirculated** — a meaningful future-unlock overhang typical of a recently launched governance token (team, investor, ecosystem, and incentive allocations vesting over time). This is a structural headwind for the KNTQ token's price independent of how well the kHYPE staking product performs. Always separate the two: kHYPE value tracks staked HYPE + rewards; KNTQ value depends on governance demand, fee capture, and the unlock schedule.

---

## Value Accrual & Governance

KNTQ is the protocol's governance and incentive token. Across liquid-staking protocols, the governance token's value case rests on (1) **governance rights** over protocol parameters (validator-selection policy, fees, treasury), (2) **fee capture** — liquid-staking protocols typically take a commission (a percentage of staking rewards), and a portion of that revenue can accrue to stakers/holders of the governance token, and (3) **incentive/ecosystem alignment** — directing emissions to bootstrap kHYPE liquidity and DeFi integrations. The strength of KNTQ's value accrual depends on the size of Kinetiq's staking TVL and the fee take-rate; a large kHYPE float earning a steady commission is what ultimately backstops the governance token. Verify the live fee switch and revenue-share mechanics against current docs before assuming direct cash-flow accrual.

---

## Comparison vs Liquid-Staking Peers

| Protocol | Chain / asset staked | LST | Governance token | Differentiator |
|---|---|---|---|---|
| **Kinetiq** | [[hyperliquid\|Hyperliquid]] / [[hype\|HYPE]] | kHYPE | KNTQ | StakeHub autonomous validator scoring; native HYPE LST leader |
| **[[lido\|Lido]]** | [[ethereum\|Ethereum]] / ETH | stETH/wstETH | LDO | Largest LST by TVL; curated node-operator set |
| **[[rocket-pool\|Rocket Pool]]** | Ethereum / ETH | rETH | RPL | Permissionless node operators; RPL collateral bonding |
| **[[jito\|Jito]]** | [[solana\|Solana]] / SOL | JitoSOL | JTO | MEV-boosted staking yield on Solana |

Kinetiq's strategic bet is that **Hyperliquid becomes a major venue** and that its HYPE token therefore needs a deep, trusted liquid-staking layer — the role Lido plays for ETH and Jito for SOL. Being the leading/native LST on a fast-growing chain is the classic moat for this category (liquidity begets DeFi integrations, which beget more staking). The risk mirror-images that thesis: HYPE/Hyperliquid stagnation caps Kinetiq's addressable market.

---

## How & Where It Trades

- **Two distinct assets:** kHYPE (the LST) trades mainly via **HyperEVM DeFi** — DEX pools and as collateral — where its price tracks NAV (staked HYPE + rewards) with small premium/discount. KNTQ (the governance token) is the asset priced in the market-data block above, ranked **#424** with a ~$54M cap.
- **Liquidity:** KNTQ is a small-cap governance token; secondary liquidity is modest and concentrated in the young HyperEVM/Hyperliquid ecosystem. Treat exit liquidity as thin.
- **Low float / unlock:** ~73% of KNTQ uncirculated means **scheduled unlocks are a recurring overhang** — check the vesting calendar before sizing; unlock cliffs are a common catalyst for governance-token drawdowns.
- **Perps:** no major perpetual market is evident in this snapshot; primarily spot for KNTQ.

---

## Narrative, Category & Catalysts

Kinetiq rides two intertwined narratives: the **Hyperliquid ecosystem** (HYPE is the leading on-chain perp venue as of mid-2026) and **liquid staking / LST DeFi**. Catalysts: growth in HYPE staking TVL, new DeFi integrations that use kHYPE as collateral, a KNTQ fee-switch activation, and broad rotation into Hyperliquid-ecosystem tokens. Headwinds: KNTQ unlock schedule, dependence on Hyperliquid's continued momentum, and competition if rival HYPE LSTs emerge.

---

## Platform & Chain Information

**Native Chain:** HyperEVM

### Contract Addresses

| Chain | Address |
|---|---|
| HyperEVM | `0x000000000000780555bd0bca3791f89f9542c2d6` |

---

## Risks and Considerations

- **Validator / slashing risk:** Staked HYPE is delegated to Hyperliquid validators. Validator downtime or misbehavior can lead to reduced rewards or [[slashing|slashing]] penalties, which would reduce the HYPE backing kHYPE.
- **Smart-contract risk:** The Kinetiq contracts, StakeHub delegation logic, and any DeFi integrations are attack surface; a contract exploit could impair the staked pool.
- **Depeg / NAV risk:** kHYPE's secondary-market price can trade below its underlying redemption value (a depeg from NAV), especially during market stress or thin liquidity, even though it is redeemable 1:1-plus-rewards over time via the withdrawal queue.
- **Withdrawal-queue / liquidity risk:** Native unstaking is not instant; in a rush for exits, secondary-market kHYPE could trade at a meaningful discount.
- **Governance-token vs receipt-token distinction:** KNTQ (the priced token here) and kHYPE behave very differently. KNTQ is a speculative governance asset with its own volatility (e.g., -7.95% over the 7-day window), while kHYPE tracks staked HYPE. Do not conflate the two.
- **Concentration / nascent ecosystem:** Hyperliquid staking and HyperEVM DeFi are young; protocol maturity and liquidity depth are still developing.
- **KNTQ unlock overhang:** ~73% of governance-token supply is uncirculated; vesting unlocks add structural sell pressure independent of product performance.
- **Single-ecosystem dependence:** Kinetiq's addressable market is bounded by Hyperliquid/HYPE adoption; a slowdown in that ecosystem directly caps both kHYPE TVL and KNTQ demand.

> *On-chain holder distribution data requires blockchain analytics integration and is not yet ingested.*

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: 2026-06-23 — **Extreme Fear** (Fear & Greed = 21), long-horizon **Bottoming / Accumulation** read; Hyperliquid is the leading on-chain perp venue.

- **Pick your exposure deliberately.** kHYPE and KNTQ are different trades. kHYPE is a *yield-on-HYPE* position (you are long HYPE plus staking carry, with NAV/depeg and queue risk). KNTQ is a *leveraged bet on Hyperliquid ecosystem growth* with an unlock overhang — far higher beta and idiosyncratic risk.
- **Depeg watch on kHYPE:** in Extreme-Fear/illiquid conditions, LSTs can trade at a discount to NAV as holders rush the secondary market rather than the slow native queue. For accumulators, a kHYPE discount to redemption value can be an entry (buy below NAV, redeem at par over the queue) — but only if you can tolerate the unbonding period and trust the redemption path.
- **KNTQ — respect the unlock calendar.** In a bottoming regime, governance tokens with >70% uncirculated supply are vulnerable to unlock-driven drawdowns; avoid sizing into a known cliff. Any allocation is a bet that Hyperliquid keeps gaining share through the bear.
- **No leverage on either** given thin HyperEVM liquidity.
- **Invalidation:** stalling HYPE staking TVL or shrinking DeFi kHYPE integrations undermine the core thesis regardless of token price.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kinetiq.xyz/](https://kinetiq.xyz/) |
| **Twitter** | [@kinetiq_xyz](https://twitter.com/kinetiq_xyz) |
| **Telegram** | [kinetiq_announcements](https://t.me/kinetiq_announcements) |
| **GitHub** | [https://github.com/kinetiq-research](https://github.com/kinetiq-research) |
| **Docs** | [https://kinetiq.xyz/docs](https://kinetiq.xyz/docs) |

---

## See Also

- [[crypto-markets]]
- [[liquid-staking]]
- [[hyperliquid]]
- [[hype]]
- [[hyperevm]]
- [[slashing]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge of Kinetiq's liquid-staking model; no dedicated wiki source ingested yet.
