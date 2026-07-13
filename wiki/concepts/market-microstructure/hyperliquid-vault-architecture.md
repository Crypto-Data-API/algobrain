---
title: "Hyperliquid Vault Architecture"
type: concept
created: 2026-05-05
updated: 2026-06-11
status: good
tags: [crypto, defi, derivatives, market-microstructure, liquidity]
aliases: ["HLP Internals", "Hyperliquid HLP Architecture", "HLP Sub-Vaults"]
related: ["[[hyperliquid]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-oracle-mechanics]]", "[[hlp-withdrawal-mechanics]]", "[[hlp-cascade-alongside-playbook]]", "[[lp-vault-comparison]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[perpetual-futures]]", "[[market-making]]"]
difficulty: advanced
---

# Hyperliquid Vault Architecture

The **Hyperliquidity Provider** ([[hyperliquid-hlp-basis-arbitrage|HLP]]) is not a single trading strategy — it is **three structurally distinct strategies sharing one balance sheet**: a **liquidator vault**, a **market-maker vault**, and a **funding harvester**. From a depositor's perspective HLP looks like a yield product (deposit USDC, earn 25-60% APR), but from a microstructure standpoint it is the protocol's risk-warehousing layer for [[hyperliquid|Hyperliquid]] — simultaneously absorbing liquidations, quoting both sides of all 229 perps, and holding whatever residual delta the first two activities leave behind. This page decomposes HLP's internals, situates it inside Hyperliquid's broader user-vault ecosystem, and contrasts the architecture with [[gmx|GMX]]'s GLP, [[jupiter|Jupiter]]'s JLP, and [[dydx|dYdX]]'s insurance fund.

Understanding the three-strategy decomposition matters because each component has a different P&L distribution, a different failure mode, and a different relationship with the rest of the order book. A trader who treats HLP as a black-box yield instrument is leaving information on the table; a trader who reads HLP's exposure correctly can front-run [[liquidation-cascade-arbitrage|liquidation cascades]], fade adverse-selection-driven inventory, or step aside before a [[hyperliquid-oracle-mechanics|thin-pair oracle attack]] hits the vault.

---

## The Three Sub-Strategies Inside HLP

HLP is best modeled as three logically separate trading desks whose books are netted into a single pro-rata vault token.

### Sub-Strategy 1: The Liquidator Vault

**Mechanism.** When a leveraged position on Hyperliquid breaches its [[maintenance-margin]] threshold, the [[hyperliquid-liquidation-engine|HL liquidation engine]] forcibly closes the position. HLP is the standing counterparty of last resort: it takes the position over from the trader at the liquidation price and unwinds it on the [[order-book]]. In exchange, HLP captures the **liquidation bonus** — approximately **1% of the liquidated collateral** per event — plus any favorable price differential between the takeover price and the eventual unwind price.

**Why it is a profit center.** [[liquidation|Liquidations]] cluster near round-number stop levels and after sharp moves. The liquidator's edge is structural: it is paid a guaranteed bonus to be the buyer of last resort *and* it gets first-look execution against a forced seller (or first-look at filling a short into a forced buyer). On April 2, 2026 Hyperliquid processed **32,964 liquidations** in a single day; on a typical day it processes ~10,000. Even at a small bonus per event, this compounds.

**P&L profile.** Convex-positive in volatility. HLP's liquidator desk earns more when the market is dislocating and liquidating retail, and it earns nothing in a flat tape. This makes the liquidator leg a **long-volatility** posture, partially offsetting losses elsewhere in HLP during cascades.

**Failure mode.** When a liquidation gap exceeds the liquidated collateral — i.e. the position is unwound at a price worse than the maintenance margin can cover — HLP eats the deficit. This is the [[insurance-fund]] role bolted onto the liquidator. JELLYJELLY in March 2025 was an extreme version: the unwind price was so bad that HLP's "liquidator" leg lost ~$13M on a single position before [[auto-deleveraging|ADL]] / governance intervened.

### Sub-Strategy 2: The Market-Maker Vault

**Mechanism.** HLP runs an automated quoter that posts **two-sided liquidity on all 229 perpetual markets** — including the long tail where no human market maker would bother. The MM model is conventional: quote a bid below mid and an ask above mid, earn the spread on round-trips, collect the **maker rebate** (~0.015% on Hyperliquid) on every fill, and rebalance toward zero inventory.

**Why it is a profit center.** Hyperliquid's [[market-microstructure|microstructure]] gives HLP three structural maker advantages:

1. **Zero gas** — quote churn is free, so HLP can quote tightly and update aggressively.
2. **On-chain CLOB priority** — HLP's quotes settle in the same block they're posted; no cross-venue latency arbitrage against it.
3. **Long-tail breadth** — on [[bitcoin|BTC]]/[[ethereum|ETH]] HLP competes with sophisticated external [[market-making|market makers]], but on micro-cap perps HLP is often the only resting liquidity, capturing wider spreads.

**P&L profile.** Mean-reverting positive carry. The MM leg grinds out small profits per trade across thousands of fills per day; in calm regimes this is the dominant contributor. However, it has a **negatively skewed tail**: when a one-way order flow hits (e.g. a memecoin pump where everyone wants to long), the MM is forced to keep selling, accumulates an ever-larger short, and can be run over.

**Failure mode.** [[adverse-selection|Adverse selection]]. The MM cannot distinguish informed flow (which wins against it) from uninformed flow (which loses to it); it just quotes. Sophisticated taker flow systematically picks off the MM's quotes, leaving HLP holding losing inventory. This is a structural cost, not a bug — it's why HLP needs to be paid via fee rebates and spread.

### Sub-Strategy 3: The Funding Harvester

**Mechanism.** After the MM and liquidator desks do their work, HLP is left holding a **residual book delta** — typically net long or net short across the 229 markets, summed up. Rather than aggressively flatten this residual (which would cost spread to do), HLP holds it and harvests the [[funding-rate]].

When the residual is **net short and funding is positive** (perps trading above spot, longs paying shorts), HLP gets paid hourly for staying short. When the residual is **net long and funding is negative**, HLP gets paid hourly for staying long. The harvester is essentially a [[funding-rate-arbitrage|funding-rate arbitrage]] desk that uses MM/liquidator inventory as its leg-in mechanism — it never has to pay spread to enter, because the inventory arrives "for free" from the other two desks.

**Why it is a profit center.** Funding flow on Hyperliquid is **persistent and directional** during trends. In a crypto bull market most majors carry positive funding; HLP's residual is structurally short MM-side (because retail keeps lifting offers), so the harvester gets paid. The hourly funding cadence (vs Binance's 8h) means 24 collection points per day, smoothing the income.

**P&L profile.** Trend-correlated. The harvester makes the most when the market is one-directional and funding is rich; it makes least or loses when funding is mean-reverting and noisy.

**Failure mode.** Holding the wrong side of a directional move. If HLP is structurally short into a 30% rally, the harvester's positive funding income is dwarfed by mark-to-market loss on the position. This is the single largest source of HLP drawdowns historically.

---

## P&L Attribution

Approximate decomposition of HLP's net APR, based on observable on-chain data and community analyses (HypurrScan, ASXN, etc.):

| Component | Contribution to gross | Sign | Notes |
|---|---|---|---|
| **Market-making** (spread + maker rebates) | **30-40%** | + | Highest-volume contributor; mean-reverting positive |
| **Liquidations** (bonus + favorable unwinds) | **20-30%** | + | Convex; spikes during volatility |
| **Funding harvester** (residual carry) | **20-40%** | + | Trend-dependent; rich in bull markets |
| **Adverse selection** (MM losing to informed flow) | **-10% to -30%** | – | Ongoing tax; widens during sharp moves |
| **Tail events** (JELLYJELLY-class incidents) | episodic | – | Multi-percent drawdowns when they occur |

**Read this as ranges, not point estimates.** The decomposition is not officially published by the Hyperliquid team; the numbers reflect on-chain reconstruction by independent analysts and shift quarter-to-quarter. The relevant insight is that **no single leg dominates**: even in a quarter where the MM leg is barely positive, liquidations and funding can carry the vault.

For depositors this means HLP's APR is **regime-rotating**, not regime-dependent. In quiet markets the MM leg pays. In cascades the liquidator leg pays. In trending markets the harvester pays. The diversification across the three legs is structural, not allocated — they emerge from the same balance sheet.

See [[hyperliquid-hlp-basis-arbitrage]] for the trader's side of this equation.

---

## Vault Accounting

HLP uses a **pro-rata vault-token** model — the same accounting primitive as a [[yearn-vault|Yearn]] vault or [[curve-finance|Curve]] LP, adapted for an active trading book.

**Deposit flow.**
1. User deposits USDC into the HLP contract.
2. Contract mints HLP-vault-token shares at the current NAV (Net Asset Value).
3. Shares represent a fixed claim on the vault's mark-to-market value — not on a specific position.

**NAV calculation.** Hyperliquid recomputes the vault NAV using mark prices for every open position plus cash. This is updated in real time on-chain; depositors can verify NAV any moment. The "performance fee" is implicit — HLP's APR is whatever the vault books, net of trading costs the strategies themselves incur (fees rebate to the vault since HLP is a maker, but takes when forced to unwind do cost spread).

**Lock-up.** Deposits are subject to a **4-day lock** before withdrawal is permitted. This protects the vault from depositor flash-runs during a drawdown — without the lock, a depositor seeing HLP take a paper loss could pull capital faster than the vault could unwind, forcing distressed liquidation of remaining positions onto the remaining depositors.

See [[hlp-withdrawal-mechanics]] for the full timing/withdrawal queue model.

**No tokenized share trading.** Unlike [[gmx|GLP]] or [[jupiter|JLP]], the HLP share is not freely tradable on a secondary market. You can only get in via primary deposit and out via the lock-up withdrawal. This means there is no [[stablecoin-depeg|share-token depeg]] risk — but it also means depositors cannot exit faster than the lock.

---

## The Broader Hyperliquid Vault Ecosystem

HLP is **the protocol's vault**, but Hyperliquid's vault primitive is general — any user can spin up their own vault, deposit capital as a "leader," and accept other depositors. The ecosystem now includes hundreds of user-deployed vaults running every imaginable strategy.

| Vault Class | Operator | Strategy | Notes |
|---|---|---|---|
| **HLP** | Protocol-native | MM + liquidator + funding harvester | The flagship; ~$300M-$1B TVL |
| **HFP** (Hyper Funding Pool) | Community / various | Pure funding-rate carry | Smaller, more focused than HLP |
| **Leader vaults** | Individual traders | Discretionary / systematic directional | "Copy-trading" wrapper — depositors back a known operator |
| **Theta vaults** | Community / various | [[options-overlay|Options-style overlays]] (selling vol on perps) | Earlier-stage; analogous to [[ribbon-finance|Ribbon]] theta vaults |
| **HyperVaults / HyperPS** | Builders | Strategy-specific (basis trades, grids, mean-reversion) | Permissionless deployment |

**Why this matters.** A vault on Hyperliquid is essentially a sub-account whose shares are tokenized and tradable. Anyone can build one. The result is that the HLP architecture — three strategies sharing one balance sheet — is being replicated, decomposed, and recombined across the ecosystem. There are now **specialized "pure-play" vaults** for each of HLP's three sub-strategies:

- A pure liquidator vault concentrates on liquidation arb, accepting tail risk for higher liquidation-bonus capture.
- A pure MM vault runs only on tight-spread majors, avoiding the long-tail adverse-selection drag.
- A pure funding harvester vault runs delta-hedged carry only.

This decomposition gives sophisticated depositors more control over their factor exposure than HLP's bundled package. It also creates a ranking/discovery problem — see [[lp-vault-comparison]] for the comparative framework.

---

## Capacity Limits

HLP's published target band was **$300M-$1B TVL**. This is the range in which the vault's three strategies can deploy capital without market impact dominating returns.

**Why TVL caps APR.** Each of HLP's three legs has a capacity ceiling:

- **MM leg** is capped by order book depth. Quoting larger means standing in front of more flow but also accepting larger inventory swings. Beyond ~$500M the MM leg starts cannibalizing its own quotes (its quotes become *the* book on long-tail perps).
- **Liquidator leg** is capped by total liquidation volume. There are only so many forced-liquidation dollars per day; doubling HLP's size doesn't double liquidation income, it just dilutes per-share bonus capture.
- **Funding harvester** is capped by [[open-interest|OI]] you can hold without moving the funding rate against yourself.

**Empirical compression.** APR has compressed roughly **100%+ → 25-50%** as TVL went from ~$20M (early 2024) to $300M+ (Q1 2025). This is consistent with the capacity model: each leg saturates separately, so doubling TVL roughly halves per-share return until volume catches up.

**Current saturation level.** As of Q1-Q2 2026, HLP runs in the **$300M-$700M** band depending on flow. The vault is plausibly near or at the lower end of capacity-saturated for the MM leg, but the liquidator and harvester legs still scale with platform volume — so as Hyperliquid grows from $2.95T (2025) to higher cumulative volume, HLP's effective capacity grows with it.

**Implication for [[hyperliquid-hlp-basis-arbitrage|HLP basis arb]].** Don't expect 60% APR to hold as TVL drifts up; do expect the floor to track Hyperliquid's growth in volume and liquidations rather than to collapse to zero.

---

## How HLP Differs From GLP and JLP

HLP, [[gmx|GMX]]'s GLP, and [[jupiter|Jupiter]]'s JLP are often grouped as "DEX LP vaults," but they are **architecturally distinct categories**.

| Dimension | **HLP** (Hyperliquid) | **GLP** (GMX) | **JLP** (Jupiter) |
|---|---|---|---|
| Trading model | Order-book MM + liquidator | AMM-style oracle-priced counterparty | AMM-style oracle-priced counterparty |
| Counterparty mechanism | Active two-sided quoting | Passive — takes the other side at oracle price | Passive — takes the other side at oracle price |
| What the vault holds | USDC + active perp inventory | Basket of crypto assets (BTC, ETH, stables) | Basket of crypto assets (SOL, BTC, ETH, stables) |
| Asset exposure | Roughly delta-neutral (net of harvester) | **Long beta basket** by construction | **Long beta basket** by construction |
| Adverse selection | Bounded by MM's ability to skew quotes | Unbounded — must take any trade at oracle price | Unbounded — must take any trade at oracle price |
| Liquidation handling | **Vault is the liquidator** | Vault pays liquidation losses to traders | Vault pays liquidation losses to traders |
| Yield source | Spread + rebate + liquidation bonus + funding | Trader losses + swap fees + borrow fees | Trader losses + swap fees + borrow fees |
| Tail risk | Oracle attack on thin pair (JELLYJELLY) | "Whale wins" — single trader takes the basket | "Whale wins" — single trader takes the basket |

**The key distinction.** GLP/JLP **are passive baskets that take the other side of any trade at oracle price**. They don't quote — they're *forced* to be the counterparty regardless of whether they want the trade. Their only protections are skew-based borrow fees and oracle accuracy.

HLP, by contrast, **actively quotes** — it can widen spreads or pull quotes when it doesn't want flow. It can also choose how aggressively to skew its book when inventory builds up. This is closer to a CEX's market-making setup than to an AMM.

**Consequence for depositors.** GLP/JLP returns are dominated by trader P&L (specifically: trader losses, since the counterparty wins what traders lose). HLP returns are dominated by spread, rebate, and liquidation income — not directly by aggregate trader P&L. A bull market is good for GLP (basket appreciates) and good-but-different for HLP (more volume, more liquidations, more funding to harvest). A whale that runs the table is much worse for GLP than for HLP, because GLP must keep taking the trade at oracle price while HLP can stop quoting.

See [[lp-vault-comparison]] for the full side-by-side.

---

## The On-Chain Transparency Edge

Every HLP position, every fill, every liquidation, and every NAV update is **public and queryable in real time** via [[hyperliquid|HyperliquidScan]], [[hypurrscan|HypurrScan]], and the native API. This is not a marketing claim — it is a structural feature of the [[hyperliquid|HyperBVM]] CLOB.

**What this enables for depositors.**
- Verify NAV independently before depositing.
- Compute the vault's current delta, gamma, and per-pair exposure.
- Spot inventory build-ups that signal impending drawdowns.
- Audit the lock-up withdrawal queue.

**What this enables for outsiders (traders).**
- See exactly what HLP is long or short.
- Front-run HLP's known liquidation thresholds (its mechanical behavior is observable).
- Coordinate or fade HLP's inventory: if HLP is heavily short a memecoin, that's information about the order book imbalance.
- Monitor the [[insurance-fund]] balance to assess whether [[auto-deleveraging|ADL]] risk is rising.

**What this enables for Hyperliquid the protocol.**
- No "hidden losses" — a JELLYJELLY-style hit is visible to depositors within minutes, which preserves trust even when the vault drawdowns.
- Permissionless replication — competitors building "HLP-clone" vaults can do so transparently.

**The trade-off** is that HLP's positions are **public to attackers as well as defenders**. A coordinated whale group can see exactly where HLP is over-exposed and structure trades to maximize HLP's loss. This is the architecture of the JELLYJELLY incident: the attackers knew what HLP would be forced to absorb, and sized accordingly.

---

## JELLYJELLY-Class Vulnerability

HLP's architecture **defends well against some attacks and poorly against others**. Understanding the boundary is essential for assessing tail risk.

### What HLP's Architecture Defends Against

- **Collusion between MM and counterparty.** HLP is the MM and the protocol's vault — there is no separate maker that could collude with takers against depositors. The MM behavior is mechanical and on-chain.
- **Flash loan attacks on AMM curves.** Unlike [[gmx|GLP]] or [[jupiter|JLP]], HLP does not price on a curve that can be moved by a large trade. Prices come from the order book + oracle median; flash loans cannot single-block the mark.
- **Withdrawal runs.** The 4-day lock-up prevents a panic-induced withdrawal cascade from forcing distressed unwinds.
- **Oracle manipulation in deep pairs.** [[bitcoin|BTC]] and [[ethereum|ETH]] use a **median of three sources** (Hyperliquid mid, Binance mid, OKX mid). Manipulating two of three exchanges simultaneously is expensive and visible.

### What HLP's Architecture Does NOT Defend Against

- **Oracle manipulation in thin pairs.** On a low-liquidity perp where the oracle's reference markets are themselves thin, a coordinated push on the reference exchange spills into the Hyperliquid mark. HLP is then forced to liquidate or take counterparty positions at the manipulated price.
- **Coordinated whale sizing.** A group can open a position large enough that, when liquidated, it overwhelms HLP's ability to unwind cleanly. The position is taken over at the maintenance-margin price; the unwind happens against thin order books; HLP eats the gap. This was the **JELLYJELLY** mechanism in March 2025.
- **Long-tail listing risk.** Every new perp listed expands HLP's MM duty without obviously expanding its risk budget. Each new pair is a potential JELLYJELLY waiting to happen.
- **Cross-pair correlated stress.** A 2020-COVID-style event where every perp moves the same direction at the same time stresses the harvester leg in a way the MM and liquidator legs cannot offset.

### Mitigations Hyperliquid Has Deployed

- **Oracle median (3-source).** Limits single-exchange manipulation.
- **Tiered maintenance margin.** Larger positions face higher margin, capping per-trader concentration.
- **Position limits.** Soft caps via tier escalation; effectively limit single-position size.
- **HIP-3 listing process.** Permissionless markets are gated by [[hype|HYPE]] staking requirements that internalize some listing risk.
- **Assistance fund.** A separate governance-controlled fund backstops HLP in extreme events. This is the layer that absorbed the JELLYJELLY paper loss (~$13M).

The pattern: HLP's architecture **does well against low-information attacks** (flash loans, panics) and **less well against high-information coordinated attacks** that exploit thin pairs and HLP's mandatory-counterparty role on liquidations.

See [[hlp-cascade-alongside-playbook]] for trader strategies during such events.

---

## Comparable Architectures

A taxonomy of LP/insurance vaults across major derivatives venues:

| Venue | Vault | Architecture | Yield Source | Tail Risk |
|---|---|---|---|---|
| **Hyperliquid** | HLP | Active CLOB MM + liquidator + harvester | Spread + rebates + liq bonus + funding | Thin-pair oracle attack |
| **[[gmx|GMX]] v1/v2** | GLP / GM pools | Passive oracle-priced AMM-style basket | Trader losses + fees + borrow | "Whale wins" + oracle manipulation |
| **[[jupiter|Jupiter]]** | JLP | Passive oracle-priced basket (SOL-heavy) | Trader losses + swap fees + borrow | Same as GLP + Solana-chain risk |
| **[[dydx|dYdX]] v4** | Insurance fund | Reserve only — no MM duty | Liquidation overflow | Insurance fund depletion |
| **[[drift-protocol|Drift]]** | Insurance fund + vAMM backstops | Reserve + auction-priced backstop | Liquidations + swap fees | Backstop auction failure |
| **Aevo / Lyra** | MMV (market-making vaults) | Active options MM | Options spread + theta | Vol-spike adverse selection |
| **Ribbon (theta vaults)** | DOVs | Sell weekly options against deposits | Option premium | Sharp move past strike |

**HLP's place in this spectrum.** It is the **most active** of the major vaults — closer to a CEX market-making book than to a passive AMM basket. The dYdX insurance fund sits at the opposite extreme: a pure reserve, no MM duty, no quoting. GLP and JLP sit in the middle: passive but obligated to take counterparty positions.

The trade-off across the spectrum is **complexity vs predictability**. HLP can in theory earn more (multiple revenue streams) but has more failure modes. The dYdX fund does one thing (backstop liquidations) and fails in only one way (gets depleted). Depositors choosing among these are implicitly choosing how much operational complexity they want to be exposed to.

---

## What This Means for Traders

Trading **around** HLP requires understanding which leg is currently dominating its risk:

- **In quiet markets** the MM leg dominates. HLP's quotes are tight and aggressive; trying to fade them is unprofitable.
- **During liquidation cascades** the liquidator leg dominates; HLP is forced into directional inventory. This is the [[hlp-cascade-alongside-playbook|cascade-alongside playbook]] window — trade *with* HLP's known liquidation behavior, not against it.
- **In trending markets** the harvester leg dominates. HLP's net position is informative: heavy net-short = retail is heavily long = potential reversal setup.
- **Around new listings** HLP's MM leg is most vulnerable. Adverse-selection cost on a freshly listed pair is highest in the first 24-72 hours; the MM widens but cannot fully protect itself. Informed flow can pick off the early quotes.

Depositing **into** HLP is a different question — it requires assessing whether the vault's blended yield (currently 25-50% APR) compensates for the tail-risk profile (multi-percent drawdowns during incidents like JELLYJELLY, plus the 4-day lock-up). For most allocators it does; for tail-risk-averse depositors a pure-play sub-vault (HFP, theta vault, etc.) may be preferable.

See [[hyperliquid-hlp-basis-arbitrage]] for the full strategy stack and [[hyperliquid-perp-trading-map]] for HLP's place in the broader Hyperliquid opportunity set.

---

## Related

[[hyperliquid]] · [[hyperliquid-hlp-basis-arbitrage]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-oracle-mechanics]] · [[hlp-withdrawal-mechanics]] · [[hlp-cascade-alongside-playbook]] · [[lp-vault-comparison]] · [[hyperliquid-perp-trading-map]] · [[funding-rate-arbitrage]] · [[market-making]] · [[liquidation-cascade-arbitrage]] · [[insurance-fund]] · [[gmx]] · [[jupiter]] · [[dydx]] · [[adverse-selection]]

## Sources

- [[hyperliquid]] — protocol overview, liquidation engine, HLP reference data.
- [[hyperliquid-hlp-basis-arbitrage]] — strategy-side detail on trading around HLP.
- [[hyperliquid-perp-trading-map]] — HLP's role in the broader strategy opportunity set on Hyperliquid.
- [[2026-04-06-hyperliquid-volume-surge]] — recent volume / liquidation context.
- HypurrScan, ASXN, and other on-chain Hyperliquid analytics dashboards (independent reconstruction of HLP P&L attribution).
- Hyperliquid documentation: HLP vault mechanics, lock-up, NAV updates.
- JELLYJELLY incident post-mortems (community analyses, March 2025) — primary source for thin-pair-attack mechanics.
- GMX, Jupiter, and dYdX official documentation for comparative architecture.
