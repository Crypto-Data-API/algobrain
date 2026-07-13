---
title: "Hyperliquid Oracle Mechanics"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [crypto, defi, derivatives, market-microstructure, liquidity]
aliases: ["HL Oracle", "Hyperliquid Price Feed", "HL Oracle Pricing"]
related: ["[[hyperliquid]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-vault-architecture]]", "[[oracle-risk]]", "[[mark-price]]", "[[chainlink]]", "[[pyth]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[hyperliquid-funding-rate-microstructure]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[perpetual-futures]]", "[[oracle-risk]]"]
difficulty: advanced
---

# Hyperliquid Oracle Mechanics

The **oracle** on [[hyperliquid|Hyperliquid]] is the mechanism that ties an on-chain perpetual contract to an external "fair value." It is the single most consequential piece of infrastructure on the platform: it determines when [[liquidation|liquidations]] fire, what direction and magnitude [[funding-rate|funding payments]] flow, and which market participants get force-closed during stress. Every BTC, ETH, SOL, and `xyz:`-prefixed traditional-asset perp on Hyperliquid is anchored to a **validator-aggregated oracle price** that is updated roughly every three seconds and combined with the on-chain [[order-book]] mid to produce a final [[mark-price]].

Understanding the oracle is not optional for serious Hyperliquid traders. The [[2025-03-jellyjelly-hlp-attack|JELLYJELLY incident of March 2025]] demonstrated that a thin spot-market oracle can be manipulated end-to-end — coordinated traders can move the underlying inputs the validators read, force a price into the oracle median, and weaponize the [[hyperliquid-vault-architecture|HLP vault]] into absorbing the other side at distressed levels. This page walks through how the oracle is constructed, where it is vulnerable, and what the implications are for liquidity providers, arbitrageurs, and cascade traders.

---

## 1. What the Oracle Does

The oracle is *not* the price you trade against. It is the **anchor** the protocol uses to keep an on-chain perpetual tethered to off-chain reality. Specifically, it drives:

| Function | How the oracle is used |
|---|---|
| **[[liquidation|Liquidation]] price** | Maintenance-margin checks compare equity to a [[mark-price]] derived from the oracle median |
| **[[funding-rate|Funding rate]]** | Funding is computed each block as a function of `(mark - oracle)` |
| **[[hyperliquid-vault-architecture|HLP]] backstop pricing** | When the [[liquidation-engine]] cannot close on-book, HLP absorbs at oracle-anchored prices |
| **[[auto-deleveraging|ADL]] selection** | Profit-and-loss for ADL tie-breaks is measured against the oracle |
| **[[mark-price]] display in UI** | The "Mark" price in the HL frontend is derived from the oracle plus on-book mid |
| **[[risk-engine|Risk engine]] caps** | Position-size tiers and leverage caps reference oracle notional |

The CLOB still discovers the *trade* price — what fills cross at — but the oracle is the price the protocol uses to decide who is solvent and who has to pay. That distinction is the heart of [[oracle-risk]].

---

## 2. Oracle Architecture

Hyperliquid does not use [[chainlink|Chainlink]], [[pyth|Pyth]], or any external oracle network. Instead, every Hyperliquid validator independently runs a **price oracle process** that reads from a curated set of external venues, computes a local price, and submits it as part of consensus. The on-chain oracle is the **median across all validators' submitted prices**, weighted by stake.

This design is similar in spirit to [[dydx|dYdX v4]]'s validator-side price oracle, but uses Hyperliquid's own validator set and a custom set of source feeds per market.

### 2.1 Crypto Pairs (BTC, ETH, SOL, HYPE, etc.)

For native crypto perpetuals, each validator computes a local price as a **median of mid-prices** drawn from major centralized exchanges. Public Hyperliquid documentation lists the source set for top pairs as roughly:

- [[binance|Binance]] mid
- [[okx|OKX]] mid
- [[bybit|Bybit]] mid
- [[coinbase|Coinbase]] mid (where applicable)
- [[kraken|Kraken]] mid (where applicable)

Per validator: `local_price = median(CEX1_mid, CEX2_mid, CEX3_mid, ...)`.

Then the on-chain oracle is `oracle_price = stake_weighted_median(validator_local_prices)`.

The **double median** (within validator, then across validators) is intentional: a single rogue exchange feed cannot move the per-validator price above the median of its peers, and a single rogue validator cannot move the on-chain oracle.

### 2.2 Long-Tail Crypto (Memecoins, New Listings)

For thinner crypto pairs — newly listed memecoins, [[hip-3|HIP-3]] permissionless markets, low-cap altcoins — the **set of source venues shrinks**, often dramatically. A token may only trade on two or three centralized venues, or in some cases only on decentralized AMMs. In those cases:

- The per-validator median is taken over a *much smaller* set of feeds
- Some feeds may be DEX TWAP rather than CEX mid
- The cost of coordinating manipulation across the oracle's source set drops sharply

This is the **manipulation surface that the JELLYJELLY attack exploited**. See section 7.

### 2.3 Traditional Asset Perps (`xyz:` Prefix)

Hyperliquid lists perps on traditional assets under the `xyz:` prefix: `xyz:SP500`, `xyz:GOLD`, `xyz:SILVER`, `xyz:CL` (crude oil), `xyz:NG` (natural gas), `xyz:TSLA`, `xyz:NVDA`, `xyz:HOOD`, `xyz:COIN`, etc. These markets cannot read prices from CEX crypto venues — there is no Binance feed for crude oil. Validators source these from:

- **Equities and indices**: [[cme|CME]] or other regulated futures-exchange feeds (e.g. ES futures for SP500, GC for gold)
- **Energy**: NYMEX/ICE futures feeds for crude (CL) and Brent (BZ); Henry Hub for natural gas
- **Metals**: COMEX gold/silver/platinum
- **Single-name equities**: Last-trade or NBBO from US equities feed providers, with market hours handling

For traditional assets, the oracle has a **session problem**: the underlying TradFi market is open ~6.5h/day for equities, with overnight gaps and weekend closures, but the Hyperliquid perp trades 24/7. During off-hours, validators effectively freeze the oracle on the last-known TradFi print and rely on the on-book mid for any further price discovery, with the protocol applying tighter funding bands to discourage unhinged drift. This creates a tradeable [[hyperliquid-tradfi-perp-weekend-basis|weekend basis]] (mentioned as a hidden edge in the [[hyperliquid-perp-trading-map]]).

---

## 3. Oracle Update Frequency

Hyperliquid's documentation states the oracle is updated **approximately every three seconds**, which corresponds to the chain's block cadence. In practice:

| Step | Frequency |
|---|---|
| Validator polls external feeds | Sub-second (validator-implementation-dependent) |
| Validator submits price as part of consensus | Every block (~1-2 seconds) |
| On-chain stake-weighted median computed | Every block |
| Mark price recomputed | Every block |
| Funding accrues | Continuous, settled hourly |

So the oracle and the [[mark-price]] both update **every block**, not every few minutes. This is meaningfully faster than [[gmx|GMX]]'s keeper-based [[chainlink|Chainlink]] updates and on par with [[dydx|dYdX v4]]'s validator oracle. Faster updates reduce the window during which on-book prices can deviate from external fair value before the protocol notices.

The flip side: a faster oracle means **the manipulation window is also shorter**, which is why thin-pair attacks tend to be brief and violent rather than slow grinds.

---

## 4. Mark Price vs Oracle Price vs Index Price

These three terms are often conflated. On Hyperliquid they are distinct, and each drives different parts of the protocol.

### 4.1 Index Price

The "index" is the **raw external reference** — the stake-weighted median of validator-submitted prices, derived from off-chain feeds. This is what most documentation calls the **oracle price** and what this page treats as synonymous with it. The index has no input from the on-book Hyperliquid order book; it is purely external.

### 4.2 Mark Price

The **mark price** is what the protocol actually uses for liquidations and PnL marking. On Hyperliquid, mark is constructed each block as a function of:

```
mark = clamp(
    oracle_price + ema(book_mid - oracle_price, half_life),
    oracle_price * (1 - max_deviation),
    oracle_price * (1 + max_deviation)
)
```

That is: mark is anchored to the oracle but allowed to drift toward the smoothed deviation between order-book mid and oracle, with a hard band so book manipulation alone cannot push the mark too far from external fair value. The exact constants are documented in Hyperliquid's protocol spec; the structure matches the family of [[mark-price|mark price]] designs used by [[binance]] and [[bybit]].

**This is the key invariant**: a malicious actor cannot trigger liquidations purely by ramping the on-book price, because the band keeps mark close to oracle. To move the mark, you must move the **oracle** — which means moving the source feeds.

### 4.3 Oracle Price (Index)

Already described in section 2. This is the `xyz:` or CEX-median anchor.

### 4.4 Trade Price

The price at which fills actually cross on the [[order-book]]. The trade price is what arbitrageurs see in the tape and what generates realized PnL on entry/exit. It is **not** what marks your unrealized PnL or triggers liquidation.

### 4.5 Which Price Drives What

| Concept | Driven by |
|---|---|
| **Liquidation trigger** | mark price (oracle-anchored) |
| **Unrealized PnL** | mark price |
| **Realized PnL** | trade price |
| **[[funding-rate]] direction & magnitude** | `mark - oracle` (premium index) |
| **UI "Mark" display** | mark price |
| **UI "Index" or "Oracle" display** | oracle (index) price |
| **Last trade ticker** | trade price |
| **HLP backstop fills** | oracle-anchored, with spread |

The protocol-critical price is the **oracle**. Mark is a smoother around it; trade price is just whatever happens to cross.

---

## 5. Funding Rate Derivation

Funding on perpetuals exists to keep the perp price tethered to spot. Hyperliquid uses the **premium index method** familiar from [[binance]] and [[bybit]]:

```
premium_index = (mark - oracle) / oracle
funding_rate = clamp(
    premium_index * funding_coefficient + interest_rate_diff,
    -funding_cap,
    +funding_cap
)
```

Two Hyperliquid-specific facts matter:

### 5.1 Hourly Settlement (Not 8-Hour)

Hyperliquid settles funding **every hour**, not every 8 hours like the major CEXs. Funding accrues continuously block-by-block, and is exchanged between longs and shorts on the hourly boundary. Consequences:

- 24 settlement points per day vs 3 on Binance
- Each individual payment is roughly 1/8th the size of a CEX payment
- The mean-reversion of the perp-spot premium is **8x faster** in settlement-time terms
- Cross-venue [[funding-rate-arbitrage]] requires careful normalization: `hl_annualized = hl_hourly × 24 × 365`, vs `binance_annualized = binance_8h × 3 × 365`

This is well-documented in the [[hyperliquid-perp-trading-map]] and is the main feature exploited by [[hyperliquid-hlp-basis-arbitrage|HLP basis arbitrage]].

### 5.2 Funding Is a Function of Mark vs Oracle, Not Mark Alone

Because funding is `(mark - oracle) × constant`, **a manipulated oracle directly poisons funding**. If an attacker pushes the oracle below where the perp is fairly priced, the premium index turns positive (mark sits above the depressed oracle), and longs start paying shorts — even though "true" fair value is unchanged. This is one of the second-order damage vectors in oracle-manipulation attacks.

It also means that traders monitoring [[funding-rate]] as a sentiment signal need to be aware of oracle integrity. A funding spike caused by oracle drift is **not** the same signal as a funding spike caused by genuine retail leverage demand, even though they look identical in a Coinglass dashboard.

---

## 6. Manipulation Surface

The oracle is not a single point of failure — it is the *thinnest layer* of the system, and the layer where attacks have actually succeeded. The threat model:

### 6.1 What a Manipulator Has to Do

To weaponize the oracle, an attacker must move the **stake-weighted validator median**. Concretely:

1. Move the per-validator median, which means moving the median of the source-feed mids.
2. To move the median of N feeds, the attacker must move at least `floor(N/2) + 1` of them.
3. Each feed is a public exchange — Binance, OKX, Bybit, Coinbase, Kraken, CME, etc.

For BTC, this is essentially impossible. Coordinated manipulation across Binance + OKX + Bybit + Coinbase BTC books would require tens of millions of dollars of capital deployed simultaneously and would be visible on every market data feed in the world.

For an obscure memecoin trading on three minor exchanges with $5M of total spot daily volume, **moving the median costs perhaps a few hundred thousand dollars**.

### 6.2 The Asymmetry

The cost of moving the oracle scales roughly with the **liquidity of the median source venue**, not with the size of the position the attacker can take on Hyperliquid. So if a memecoin has:

- $5M/day spot volume across the oracle source set
- $100M+ open interest on Hyperliquid

…then a few hundred thousand dollars of spot-side manipulation can move tens of millions of dollars of HL positions. **This is the JELLYJELLY pattern.**

The manipulation cost scales with the *liquidity of the median source venue*, and the payoff scales with HL [[open-interest]]. The ratio of the two is the danger metric. The table makes the asymmetry concrete across pair tiers:

| Pair tier | Oracle source set | Spot vol (oracle sources) | Approx cost to move median | HL OI | Realistically attackable? |
|-----------|-------------------|---------------------------|----------------------------|-------|---------------------------|
| **Majors** (BTC, ETH) | 4-5 deep CEXs | $10B+/day | tens of $M, globally visible | very large | No — effectively impossible |
| **Large alts** (SOL, HYPE) | 3-5 CEXs | $1B+/day | low-to-mid 8 figures | large | No — uneconomic vs payoff |
| **Mid alts** | 2-4 venues | $50-500M/day | 7 figures | moderate | Marginal — depends on OI/vol ratio |
| **Long-tail / memecoin** | 2-3 thin venues (some DEX TWAP) | $1-10M/day | low 6-7 figures | can exceed spot vol many-fold | **Yes — the [[2025-03-jellyjelly-hlp-attack|JELLYJELLY]] zone** |
| **HIP-3 permissionless** | listing-dependent, often thin | varies, often low | varies, can be low | new, untuned caps | **Yes — inherits the long-tail risk** |

The operational read for any HL participant: the danger flag is **HL OI > ~5× the daily oracle-source spot volume** combined with **fewer than 4 source venues**. That single condition predicts JELLYJELLY-class fragility better than any absolute size number.

### 6.3 Mitigations Hyperliquid Has Layered In

Post-incidents, Hyperliquid has implemented a stack of defenses:

- **Listing criteria** for new perps: minimum spot venues, minimum spot liquidity, age requirements
- **Per-asset position size caps** that scale with oracle source liquidity
- **Mark-price deviation bands** that cap how far mark can drift from oracle (preventing pure book attacks but not oracle attacks)
- **HLP risk limits per market** to bound vault exposure to any one thin pair
- **[[hyperliquid-circuit-breakers|Circuit breakers]]** that pause trading when oracle deviation from on-book mid exceeds thresholds
- **Validator quorum interventions** for extreme cases (the JELLYJELLY response involved manual quorum action)

These help but do not eliminate the structural vulnerability: any new long-tail listing inherits some version of this risk.

---

## 7. The JELLYJELLY Case Study (March 2025)

The JELLYJELLY incident is the canonical example of HL oracle exploitation. Documented in detail at [[2025-03-jellyjelly-hlp-attack]]; the short version:

### 7.1 Setup

- **JELLYJELLY** (a [[solana]]-based memecoin) was listed on Hyperliquid as a perpetual.
- Oracle source feeds for JELLY were **a small number of CEX/DEX venues** with thin spot liquidity — total daily spot volume on the order of low single-digit millions.
- HLP was the default backstop counterparty; default position-size caps were in place but generous.

### 7.2 The Attack Sequence

1. The attacker opened a **large long position** on JELLY perp on Hyperliquid using high leverage. Reports indicate the position was sized in the multi-million-dollar notional range.
2. The attacker simultaneously **dumped JELLY on the spot venues** that fed the oracle, using inventory accumulated in advance.
3. The oracle median **dropped sharply** as more than half of its source feeds reflected the dumped spot price.
4. The drop in the oracle pushed the attacker's HL long position toward [[liquidation]], and because the on-book HL price had not moved as fast (HL CLOB liquidity was thinner than the dump capacity), the [[liquidation-engine]] could not close the position cleanly on book.
5. **HLP absorbed the position at the oracle-anchored backstop price** — which was now far below where the position had been opened.
6. The attacker had effectively transferred a large paper loss to HLP, while their own short-side spot positioning recovered them most of the perp loss.

Reported HLP paper drawdown on the position: **approximately $13M** before mitigations were applied.

### 7.3 The Resolution

Hyperliquid's validator set used quorum action to **intervene manually** — settling the JELLY market at a corrected price and restoring HLP. This was effective but controversial: it demonstrated that the protocol is willing to override the "code is law" outcome under sufficient stress, which is itself an important risk to model when sizing into HL.

### 7.4 Why It Worked

- The **oracle source set was thin**: dumping low-millions of spot moved the median.
- HLP **had no per-asset cap small enough** to limit absorption to a tolerable size.
- The **on-chain CLOB lacked the depth** to absorb the liquidation organically.
- Existing [[hyperliquid-circuit-breakers|circuit breakers]] were not sized for the speed of the move.

### 7.5 What Was Tightened

Post-incident, Hyperliquid:

- Tightened **listing criteria** for new perps (minimum spot venues, minimum liquidity)
- Added **per-asset HLP exposure caps**
- Lowered **default leverage** for new listings
- Added clearer **circuit-breaker thresholds**

But none of these fixes change the fundamental dynamic: **as long as a perp trades with an oracle drawn from thinner sources than its HL open interest, a JELLYJELLY-style attack is theoretically possible.**

---

## 8. Oracle Risk vs Mark Price Risk

Two distinct concepts, often conflated:

### 8.1 Oracle Risk

The risk that the **inputs are wrong** — the external feeds the validators read are incorrect, manipulated, or stale.

- Source: external venues, real-world data
- Mitigation: more diverse, more liquid source feeds; faster polling; sanity-check filters
- Example: JELLYJELLY (manipulated spot)
- Example: a CEX outage producing stale prices that get pulled into the median

### 8.2 Mark Price Risk

The risk that **HL's smoothing/aggregation logic itself misbehaves** — the formula combining oracle and book produces a number that doesn't represent fair value.

- Source: protocol code, parameter choices (band widths, EMA half-lives)
- Mitigation: parameter audits, on-chain monitoring, simulation
- Example: a thin-book asset where on-book mid is meaningless and the EMA term injects noise
- Example: parameter drift after a HIP-3 listing where defaults aren't tuned for the market

These risks **stack**. A bad oracle inside a sound mark-price formula still produces bad marks. A clean oracle inside a poorly tuned formula can also produce bad marks. Risk-aware [[hyperliquid-hlp-basis-arbitrage|HLP depositors]] need to monitor both layers.

---

## 9. Comparison to Other DEX Oracles

| Platform | Oracle source | Update model | Failure mode |
|---|---|---|---|
| **Hyperliquid** | Validator-aggregated medians of CEX/CME feeds | ~3s, every block | Thin-pair source manipulation (JELLYJELLY) |
| **[[gmx|GMX]]** | [[chainlink|Chainlink]] price feeds + low-latency keepers | Keeper-driven (sub-second on majors) | Off-chain price manipulation, keeper outages |
| **[[dydx|dYdX v4]]** | Validator-aggregated, similar to HL | Per-block | Similar surface to HL; smaller validator set |
| **[[drift-protocol|Drift]]** | [[pyth|Pyth]] pull oracle | On-demand | Pyth aggregator failure |
| **[[synthetix|Synthetix Perps V2]]** | [[chainlink|Chainlink]] + Pyth + offchain price feed | Keeper + offchain | Atomic-swap manipulation pre-2023 |
| **[[uniswap|Uniswap]] (used as oracle)** | TWAP of pool price | Block-by-block | Sandwich and TWAP manipulation |

Hyperliquid's design is closest to dYdX v4, both being validator-aggregated. Compared to [[gmx]] / [[chainlink]], HL is faster but uses fewer external sources per asset; compared to [[pyth]], HL is more centralized in validator set but does not require pull transactions.

The key takeaway: **no DEX oracle is invulnerable**. They each have a different failure profile. Hyperliquid's profile is "thin pairs are dangerous; majors are very robust."

---

## 10. What This Means for HLP Depositors

For depositors in the [[hyperliquid-vault-architecture|HLP vault]], oracle risk is **the** dominant tail risk. Recommendations:

### 10.1 Monitor Listed Asset Profile

The risk of HLP is roughly proportional to the **fraction of HLP exposure in pairs with thin oracle source sets**. If HLP is 95% BTC/ETH/SOL/HYPE and 5% memecoins, oracle tail risk is very low. If a flood of new HIP-3 listings tilts the mix toward thin pairs, tail risk rises.

### 10.2 Watch for Listings With Extreme Asymmetry

Any new listing where:

- HL open interest > 5x the daily oracle-source spot volume
- Oracle source set has fewer than 4 venues
- Spot venues themselves have low orderbook depth

…is a JELLYJELLY waiting to happen. HLP's per-asset caps reduce but do not eliminate the exposure.

### 10.3 Treat Hyperliquid's Circuit-Breaker Policy as Part of the Yield

Post-JELLYJELLY, the validators have shown they will intervene manually in extreme cases. This is **good** for HLP depositors (it bounded the loss) but **bad** for the platform's neutrality story. Depositors should price both effects.

### 10.4 Cross-Reference With [[hyperliquid-hlp-basis-arbitrage]]

The risk-bearing component of HLP yield is exactly the compensation for accepting these tail risks. Don't double-count: HLP's 25-60% APR includes payment for taking JELLYJELLY-style exposure. If your model assumes that exposure away, you're overestimating the Sharpe.

---

## 11. What This Means for Cascade Traders

For traders running [[liquidation-cascade-arbitrage]] or [[stop-hunting-and-liquidity-sweeps]] strategies, **oracle deviation is one of the cleanest cascade-imminent signals available on any venue**, because Hyperliquid's oracle is fully observable on-chain.

### 11.1 The Signal

Define `deviation = (book_mid - oracle) / oracle`. Monitor it per-asset on a 1-second cadence. When deviation exceeds historical norms (say, |deviation| > 3 standard deviations on a 24h rolling basis), one of two things is happening:

- **CLOB-leading move**: The on-book price is moving ahead of the oracle (CEX feeds will catch up). This often precedes a forced funding adjustment as the mark catches up.
- **Oracle-leading move**: The oracle is moving ahead of the book. This often precedes a **liquidation cascade** as positions marked at the new oracle become underwater faster than the book reflects.

### 11.2 Why This Is Cleaner Than Coinglass Heatmaps

[[liquidation-heatmap|Liquidation heatmaps]] tell you *where* liquidations cluster geographically (by price). Oracle deviation tells you *when* a cascade is mechanically imminent — the protocol's internal solvency check is about to flag positions, and the [[liquidation-engine]] is about to start hitting bids.

A cascade trader who watches both axes — heatmap-clustering plus oracle deviation — has a much sharper trigger than one who watches only price.

### 11.3 Risk

The same logic works in reverse: if the deviation is driven by **oracle manipulation** rather than genuine fair-value movement, the cascade you're trading may reverse violently when the manipulation unwinds. Don't blindly trade deviation — cross-check against multiple external feeds yourself.

---

## 12. Practical Implications Summary

| Audience | Implication |
|---|---|
| **HLP depositors** | Tail risk is dominated by thin-pair listings; track listing pace and asset mix |
| **Funding-rate arbs** | A manipulated oracle poisons funding; cross-check with CEX premium index |
| **Cascade traders** | Oracle deviation is a fast, high-signal cascade trigger |
| **Liquidity providers / market makers** | Mark-price band tells you the maximum unrealized P&L excursion before forced unwind |
| **Directional traders** | Liquidation prices reference the oracle, not the book — a wick on HL alone won't liquidate you, but a CEX wick that propagates into the median will |
| **Protocol risk teams** | Oracle source diversity, not absolute number of sources, is the right metric to monitor |

---

## 13. Oracle-Aware Strategy Map

The oracle is not just a risk to manage — it is an input that several strategies in the [[trading-strategy-baskets|strategy basket]] consume directly. Because HL's oracle and [[mark-price]] are fully observable on-chain (every block), the `(book_mid − oracle)` and `(mark − oracle)` deviations are tradeable signals available on no CEX. This table maps each oracle property to the strategies that depend on it.

| Oracle property | Signal it produces | Strategies that consume it |
|-----------------|--------------------|----------------------------|
| `(mark − oracle)` drives [[funding-rate]] | Funding = premium index × constant | [[hyperliquid-hlp-basis-arbitrage]], [[funding-rate-arbitrage]], [[hl-vs-cex-funding-divergence]] |
| Oracle update lags fastest CEX prints ~200-500 ms | Mark-oracle deviation spikes pre-cascade | [[cascade-detection-signals]], [[liquidation-cascade-arbitrage]], [[liquidation-cascade-fade]] |
| Thin-pair source set is manipulable | HLP absorbs at distressed oracle-anchored price | [[hlp-cascade-alongside-playbook]], HLP risk-bearing yield (see section 10) |
| `xyz:` perps freeze oracle off-session | Weekend / off-hours basis vs TradFi fair value | [[hyperliquid-tradfi-perp-weekend-basis]], [[hyperliquid-perp-trading-map]] (Hidden Edge #3) |
| Manipulated oracle poisons funding | Funding spike that is *not* genuine leverage demand | [[funding-rate]] sentiment readers; cross-check vs CEX premium index |
| Mark-price band caps book-only attacks | Max unrealized excursion before forced unwind | market makers / [[liquidity]] providers sizing margin |

The unifying point: on HL, **oracle deviation is the single richest microstructure signal**, because the protocol's own solvency check is observable. A cascade trader who watches `(mark − oracle)` alongside a [[liquidation-heatmap]] has a sharper, earlier trigger than one watching price alone (section 11).

---

## Related

- [[hyperliquid]] — platform overview, market data, architecture
- [[hyperliquid-vault-architecture]] — HLP vault structure (the oracle's main customer for backstop fills)
- [[hyperliquid-liquidation-engine]] — how mark-price triggers liquidations on HL
- [[hyperliquid-funding-rate-microstructure]] — how `(mark - oracle)` is converted into funding payments
- [[hyperliquid-hlp-basis-arbitrage]] — strategy depending on funding/oracle relationships
- [[hyperliquid-perp-trading-map]] — strategy map noting oracle risk
- [[2025-03-jellyjelly-hlp-attack]] — detailed incident write-up
- [[oracle-risk]] — generic concept page
- [[mark-price]] — generic concept page
- [[chainlink]] — comparison oracle network
- [[pyth]] — comparison oracle network
- [[funding-rate]] — funding rate mechanics
- [[funding-rate-arbitrage]] — strategies built on funding
- [[liquidation]] — liquidation mechanics
- [[liquidation-cascade-arbitrage]] — strategies built on cascades
- [[liquidation-cascade-fade]] — contrarian cascade-exhaustion trade
- [[cascade-detection-signals]] — mark-oracle deviation as a cascade trigger
- [[hl-vs-cex-funding-divergence]] — cross-venue funding arb that consumes the oracle-driven funding
- [[hlp-cascade-alongside-playbook]] — HLP-hedge during oracle-driven absorption events
- [[hyperliquid-tradfi-perp-weekend-basis]] — off-session oracle-freeze basis trade
- [[liquidation-heatmap]] — spatial liquidation clustering, paired with oracle deviation
- [[trading-strategy-baskets]] — portfolio context for the oracle-aware strategies
- [[open-interest]] — flow metric in the manipulation-asymmetry calculus
- [[perpetual-futures]] — base concept
- [[stop-hunting-and-liquidity-sweeps]] — related cascade-trading strategy

## Sources

1. **Hyperliquid Documentation** — [https://hyperliquid.gitbook.io/](https://hyperliquid.gitbook.io/) — Protocol spec covering oracle aggregation, mark price formula, funding rate calculation, and listing policy.
2. **Hyperliquid GitHub / spec repos** — Validator oracle implementation references; price-source configuration per market.
3. **JELLYJELLY incident analysis** — Multiple post-mortems published March 2025 by [[hyperliquid|Hyperliquid]] team and independent analysts; see [[2025-03-jellyjelly-hlp-attack]] for detailed timeline.
4. **dYdX v4 docs** — Comparison oracle architecture (validator-aggregated, similar design).
5. **Chainlink and Pyth documentation** — Comparison oracle networks used by [[gmx]], [[drift-protocol|Drift]], [[synthetix]].
6. **[[hyperliquid-perp-trading-map]]** — Internal synthesis of HL strategies and risks, including oracle risk for TradFi perps.
7. **[[hyperliquid-hlp-basis-arbitrage]]** — Strategy page noting HLP's exposure to oracle-driven absorption events.
