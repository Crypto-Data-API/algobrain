---
title: "Hyperliquid Liquidation Engine"
type: concept
created: 2026-05-05
updated: 2026-06-11
status: good
tags: [crypto, defi, derivatives, market-microstructure, leverage]
aliases: ["HL Liquidation Engine", "Hyperliquid Forced Liquidation", "HL Liq Mechanics"]
related: ["[[hyperliquid]]", "[[hyperliquid-vault-architecture]]", "[[hyperliquid-oracle-mechanics]]", "[[liquidation]]", "[[liquidation-cascade-fade]]", "[[liquidation-cascade-arbitrage]]", "[[insurance-fund]]", "[[mark-price]]", "[[auto-deleveraging]]", "[[2024-03-hyperliquid-cascade]]", "[[2025-03-jellyjelly-hlp-attack]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[perpetual-futures]]", "[[liquidation]]"]
difficulty: advanced
---

# Hyperliquid Liquidation Engine

The **Hyperliquid liquidation engine** is the protocol-native risk-management system that monitors, triggers, and unwinds undercollateralized [[perpetual-futures]] positions on the Hyperliquid L1. Three design choices distinguish it from every centralized-exchange liquidation engine and from older DEX designs: (1) it runs on a sub-second-block on-chain Central Limit Order Book ([[order-book|CLOB]]) where every liquidation order is publicly visible in the mempool and on-chain, (2) it uses the [[hyperliquid-vault-architecture|HLP vault]] as a depositor-capitalized backstop that absorbs flow when the public book cannot, and (3) it falls back to [[auto-deleveraging|ADL]] only when both the public book and HLP refuse to clear — but unlike CEX ADL, the entire chain of decisions is recorded on-chain and can be audited after the fact. Together these choices change the **shape** of liquidation cascades on Hyperliquid relative to Binance, Bybit, [[gmx|GMX V2]], and [[dydx|dYdX v4]]: faster compression of the cascade window, smaller per-event overshoot, but a structurally larger tail-risk concentration in HLP itself.

> **Where this page sits.** This page is the microstructure deep-dive. For the contrarian directional fade strategy that *exploits* engine overshoot, see [[liquidation-cascade-fade]]. For the keeper-side trade that *triggers* liquidations and collects bonuses on lending protocols, see [[liquidation-cascade-arbitrage]]. For the depositor-side passive yield play, see [[hyperliquid-hlp-basis-arbitrage]]. The engine described here is the substrate all three strategies trade around.

## Liquidation Triggers

A Hyperliquid position is liquidated when its **margin ratio** — equity divided by maintenance margin requirement — falls below 1.0. The trigger price is computed from the **mark price**, not the last-traded price, and the maintenance margin requirement is **tiered by notional** and varies sharply by pair.

### Mark Price vs Oracle Price

Hyperliquid distinguishes two related but separate prices:

| Price | Sources | Used For |
|---|---|---|
| **Mark price** | Median of three sources: (1) Hyperliquid mid-price, (2) Binance mid-price, (3) OKX mid-price | Liquidation triggers, unrealized P&L, [[funding-rate]] computation |
| **Oracle price** | External price feeds (per pair, see [[hyperliquid-oracle-mechanics]]) | HIP-3 traditional-asset settlement, certain spot-perp basis checks |

The **three-source median** is the critical detail: a single venue cannot push Hyperliquid's mark by more than ~50bp without one of the other two confirming, because the median ignores the outlier. This was a deliberate post-mortem upgrade after early DEX exchanges (notably [[gmx|GMX V1]]) suffered single-oracle manipulation losses. It also means that during major [[flash-crashes]], Hyperliquid's mark sometimes lags spot venues by 100-300ms — the median needs the second venue to print before it can move — which has both protective and exploitative implications discussed below.

For tradfi assets listed via [[hyperliquid|HIP-3]] (commodities, equities, indices), the mark instead derives from a builder-configured oracle feed; this introduces additional [[oracle-disputes|oracle risk]] not present on the crypto pairs.

### Maintenance Margin Tiers

Maintenance margin scales **stepwise** with position notional, not continuously. Larger positions are forced to hold proportionally more equity:

**BTC perp tiers (April 2026):**

| Position Notional (USD) | Maintenance Margin | Max Initial Leverage |
|---|---|---|
| 0 – 1,000,000 | 2.5% | 40x |
| 1,000,000 – 5,000,000 | 5.0% | 20x |
| 5,000,000 – 10,000,000 | 10.0% | 10x |
| > 10,000,000 | 20.0% | 5x |

ETH and HYPE follow similar curves with slightly tighter tiers. **Long-tail altcoins** (the 200+ HIP-3 markets) have dramatically higher maintenance margins — often 10-25% even at small notionals — and lower max leverage (3-10x). This is the engine's first defense against thin-liquidity exploits like the [[2025-03-jellyjelly-hlp-attack|JELLYJELLY incident]]: tight tiers force the trader to keep skin in the game even on a small position, and the protocol can reject leverage that would be unsupportable in stress.

### The Health Factor

Operationally the engine tracks a single number per position: the health factor

```
health = equity / (position_notional * maintenance_margin_pct)
```

When `health` crosses 1.0 the position is flagged for liquidation on the next block. Hyperliquid's sub-second blocks (~200ms target) mean this transition is much faster than CEX liquidation queues (which often run at 1-second polling intervals) — a position can go from healthy to liquidating to closed inside a single human reaction time.

## Liquidation Execution Flow

The execution path is a tiered cascade — each tier only fires if the previous one fails to clear the position cleanly:

### Tier 1: Public Book Liquidation

When health crosses 1.0, the engine **takes over** the position and submits market orders into the on-chain CLOB. For a long liquidation, this is a market sell of the position size; for a short, a market buy. Critical mechanics:

- **Partial liquidation first.** The engine attempts to liquidate **only the portion needed** to restore the position's health to ~1.5 (a configurable buffer above the maintenance threshold), not the entire position. This is a major departure from older "full-position-at-bankruptcy" designs (e.g. pre-2020 BitMEX) and reduces cascade severity by capping the supply burst.
- **Mempool visibility.** Because Hyperliquid is on-chain, every liquidation order is broadcast and visible to validators and observers. There is a brief window (sub-100ms in practice, longer during congestion) during which sophisticated counterparties — keepers, MEV bots, [[hyperliquid-hlp-basis-arbitrage|HLP-aware traders]] — can pre-position bids to absorb the flow. This dynamic is closer to MEV behavior on Ethereum than to the closed liquidation queues of CEXs.
- **Best-available execution.** The engine sweeps the book at whatever price the resting bids offer, with no minimum-price floor. If the book is healthy, slippage is small (10-30bp). If the book is thin, slippage can be 100-500bp, at which point Tier 2 takes over.

### Tier 2: HLP Backstop Absorption

When the public book cannot fill the liquidation at acceptable slippage — operationally defined as the engine receiving fills at a price worse than a configured threshold relative to mark — the **HLP vault** absorbs the residual at the **liquidation price** (the price at which the position becomes bankrupt, equity = 0). HLP is in effect a **buyer of last resort within the protocol** that does not require external solvency.

This is the structural feature that distinguishes Hyperliquid from every CEX: instead of a static insurance fund denominated in the exchange's own balance sheet, HLP is a depositor-capitalized vault whose participants accept liquidation flow risk in exchange for liquidation profits. When liquidations are profitable in aggregate (which they are, in steady state, because the engine seizes positions before they go bankrupt and pockets the difference between mark and the closeout fill), depositors earn the spread; when a single cascade overwhelms the vault, depositors absorb the loss.

The HLP-absorbs-at-liquidation-price mechanic is also the source of the **HLP yield**: every time HLP buys a liquidated long below mark or sells a liquidated short above mark, that delta is the depositor's earnings. See [[hyperliquid-hlp-basis-arbitrage]] for the strategy ecosystem built around this mechanic.

### Tier 3: Auto-Deleveraging (ADL)

If even HLP cannot absorb — for example, because the cascade has already drawn HLP into a heavily one-sided position and a further leg in the same direction would risk insolvency for the vault itself — the engine falls back to [[auto-deleveraging|ADL]]. ADL force-closes the **most profitable counterparties** (longs in a crash, shorts in a squeeze, ranked by unrealized profit and leverage) at the **bankruptcy price** of the failing position.

Hyperliquid's ADL is a last resort and is rare in practice — far rarer than on Bybit (which ADL'd publicly during 2020-03-12) — because HLP has historically been deep enough to clear all but the most extreme events. But it remains the final line of defense; without it, a sufficiently large bankrupt position would create protocol-level bad debt.

The transparency point matters: every Hyperliquid ADL event is recorded on-chain with the affected positions, the bankruptcy price, and the depth of HLP at the moment of fallback. CEX ADL events are reported only as aggregate counts (or not at all). This auditability is one of the few unambiguous wins of on-chain microstructure for sophisticated traders, who can compute their ADL exposure ex ante by monitoring HLP's positioning.

## The HLP Backstop Role

[[hyperliquid-vault-architecture|HLP]] is structurally three things at once, and trading around the engine requires keeping all three in mind:

1. **A market maker.** HLP runs automated quoting on every Hyperliquid pair, providing baseline liquidity in normal regimes. Its quote width and depth are observable on-chain.
2. **A liquidator.** HLP receives a share of the liquidation premium when it absorbs a position at the liquidation price. This is mechanically similar to the [[liquidation-cascade-arbitrage|keeper bonus]] on Aave or Compound, except the bonus accrues to a depositor pool rather than to an individual keeper.
3. **An insurance fund.** When the public book and HLP's own market-making inventory cannot absorb a liquidation, the rest of the HLP capital pool is the next line. This is the role that creates the tail risk: a single sufficiently large adverse event can draw HLP into a deep paper loss.

The interaction matters during cascades. In Tier 1 of a small liquidation, HLP's market-making bid is *one of* the resting bids the engine sweeps — HLP earns spread, depositors earn yield. In Tier 2 of a larger liquidation, HLP's *vault capital* is committed beyond what its market-making book had originally quoted, accepting larger inventory than a normal market-maker would tolerate. In a [[2025-03-jellyjelly-hlp-attack|JELLYJELLY-style coordinated attack]], an adversary deliberately drives flow into HLP precisely *because* the vault must absorb at the liquidation price, even when that price is wildly off-market.

The asymmetry: HLP earns small, frequent spreads in calm regimes; HLP loses large, rare amounts in tail regimes. Depositor yield is therefore an option premium, not an arbitrage. See [[hyperliquid-hlp-basis-arbitrage]] for the depositor-side framing and [[insurance-fund]] for general background.

## Auto-Deleveraging (ADL) — Last Resort

ADL is the engine's nuclear option. When invoked:

1. The engine identifies all open positions on the **opposite side** of the bankrupt position (longs on the same instrument if the bankrupt position was short, or vice versa).
2. Positions are ranked by a combination of **unrealized profit** and **effective leverage** — the most profitable, highest-leveraged counterparties go first.
3. Selected positions are force-closed at the **bankruptcy price** of the failing position. The counterparty receives the bankrupt price, not the fair market price; the difference between bankrupt price and mark is the loss they absorb on behalf of the protocol.
4. The closure is irrevocable and bypasses normal order matching.

For the [[liquidation-cascade-fade]] trader this is the worst possible outcome: a perfectly-timed counter-trend long, executed during the cascade trough, gets ADL'd at exactly the cascade bottom and captures none of the snapback. ADL is the single largest reason cascade-fade strategies on perpetual venues underperform their backtest assumptions.

For the HLP depositor, ADL is the mechanism that *protects* HLP from going bankrupt — the vault would be the last counterparty wiped out, not the first. So depositor risk is bounded above by HLP's capital, not by the protocol's full open interest.

For the protocol, ADL is the alternative to socialized losses (the older OKEx model where all profitable traders share losses pro-rata). Hyperliquid's targeted ADL is harsher per-trader but preserves the property that traders who weren't on the winning side of the bad position are unaffected.

## Partial Liquidations

Older liquidation engines closed the **entire** position at the moment health crossed 1.0. This was simple but catastrophic — a single 5x-leveraged long that crossed maintenance would dump 5x its equity in notional into the book in a single step. Modern engines, Hyperliquid included, **liquidate only the portion needed** to restore health.

The math: if a position has maintenance margin requirement *M* and unrealized loss *L* such that equity / (notional × *M*) = 1.0, partial liquidation closes a fraction *f* of the position such that the new equity-to-notional ratio is *M* × 1.5 (or whatever buffer is configured). This typically means closing 20-40% of the position rather than 100%.

Effects on cascade dynamics:

- **Smaller per-step supply.** Each cascade leg dumps less notional, reducing the price impact per liquidation.
- **More liquidations per event.** Because each liquidation only restores part of the buffer, the same position may be partially liquidated multiple times during a sustained move. The April 6, 2026 event showing 17,214 liquidations in a single day (more on this below) is partly an artifact of partial-liquidation accounting — many of those events are repeat partials on the same position.
- **More time for the bid to refill.** Between partial liquidations the book has milliseconds-to-seconds to reform, attracting [[liquidation-cascade-fade|fade traders]] and HLP market-making bids back into the book.
- **Smaller overshoot, smaller fade premium.** The cascade-fade strategy on Hyperliquid catches smaller mean-reversion moves than the same strategy on a 2020-vintage CEX precisely because the engine doesn't dump the whole position at once.

## Comparison Table — HL vs Major Perp Venues

| Feature | Hyperliquid | Binance | Bybit | GMX V2 | dYdX v4 |
|---|---|---|---|---|---|
| **Trigger price** | Mark = median(HL mid, Binance mid, OKX mid) | Mark = index from multiple spot venues | Mark = index from multiple spot venues | Chainlink oracle | Mark = exchange mid |
| **Partial liquidation** | Yes (default) | Yes | Yes | Effectively no — closes full position | Yes |
| **ADL** | Yes, on-chain auditable | Yes, opaque to user | Yes, ADL ranking visible to user | No traditional ADL — uses GLP/GM pool absorption | Yes |
| **Insurance fund** | HLP vault (depositor-capitalized) | $1B+ exchange-balance-sheet fund | ~$300M exchange-balance-sheet fund | GLP/GM pool absorbs all losses | Insurance fund, smaller |
| **Liquidation order visibility** | On-chain, mempool-visible | Internal queue, opaque | Internal queue, opaque | On-chain transactions | On-chain (Cosmos appchain) |
| **Block time / cycle** | ~200ms blocks | Continuous (microsecond engine) | Continuous (microsecond engine) | Per-block (Arbitrum, ~250ms) | ~1s blocks |
| **Backstop liquidity model** | HLP vault buys at liquidation price | Insurance fund pays for shortfall | Insurance fund + ADL | LP pool *is* the counterparty | Insurance fund |
| **MEV exposure** | High — public mempool | None (centralized) | None (centralized) | Moderate (Arbitrum sequencer) | Low (off-chain order book) |

The headline contrasts:

- **Binance/Bybit** have the deepest insurance funds and the smoothest engine micro-behavior, but the entire system is opaque — you cannot verify ex post whether ADL was invoked correctly, whether the insurance fund actually absorbed what it claimed, or whether the engine's execution was honest. Counterparty risk is **corporate**.
- **GMX V2** has no engine in the traditional sense — the LP pool *is* the perpetual counterparty, so liquidations are implicit (the trader's loss directly pays the LPs). This works in calm regimes and has crippling failure modes in directional markets (LPs lose if pool is short during a rally).
- **dYdX v4** is closest architecturally to Hyperliquid (on-chain CLOB, ~1s blocks, transparent insurance fund), but its block time is 5x slower and its insurance fund is smaller and not depositor-staked — so MEV exposure is lower but tail-risk capacity is also lower.
- **Hyperliquid** sits in the middle: faster than dYdX, more transparent than CEXs, with a backstop that is structurally larger (depositor capital can scale) but structurally riskier (a single tail event can wipe depositors). The right way to think about it: Hyperliquid trades CEX corporate-balance-sheet risk for DeFi smart-contract-and-vault-depositor risk.

## Cascade Dynamics on Hyperliquid

The engine's design choices produce a recognizably different cascade shape than on a CEX:

**Compressed timeline.** A CEX cascade typically unfolds over minutes — a Binance flash crash takes 60-120 seconds for the engine to chew through the leveraged-long book. Hyperliquid's sub-second blocks mean an entire cascade can fire in **seconds**: each block processes a tranche of liquidations, the next block sees the new mark, triggers the next tranche, and so on. The 2026-04-06 event (17,214 liquidations in one day, much of it concentrated in a few minutes during a BTC drop) was effectively impossible to react to discretionarily — an entire cascade-fade entry-and-exit window can complete inside what feels like a single price-feed update on a CEX UI.

**Mempool-visible flow.** Every liquidation order is observable before it executes. Sophisticated traders running a node, watching the mempool, can in principle pre-position bids one block ahead of the engine's market-sells. This compresses the overshoot — the bid stack reforms while the cascade is still printing — but it also tilts the playing field toward operators with co-located infrastructure, very much in the way CEX HFT does on traditional venues. See [[hyperliquid|Hyperliquid's automation ecosystem]] for the bot landscape.

**HLP as cascade dampener.** When the public book thins, HLP's market-making layer is the next line. Because HLP's quotes are not driven by short-term VaR (the vault has a long horizon and depositor-pooled capital), HLP often *adds* depth precisely when human market makers are pulling. This makes Hyperliquid cascades shallower than they would be without HLP — but it also concentrates the eventual loss into HLP itself when the cascade is too large for the vault to absorb at fair price.

**On-chain post-mortem.** Every cascade is permanently auditable: the exact sequence of liquidations, the prices, the HLP positions before and after, the ADL events if any, are all queryable. This is where research like the [[2024-03-hyperliquid-cascade]] analysis becomes possible — the inputs are all public.

## The 17,214-Liquidations-Day Pattern

Looking at a high-liquidation-count day on Hyperliquid is instructive for understanding what an event "looks like" in operational terms. The April 6, 2026 daily snapshot recorded approximately **17,214 liquidations** across all pairs (32,964 was the peak day on April 2) — well above the ~10,000 baseline. Decomposing what such a day actually contains:

- **Most liquidations are partial.** Of the 17,000+ events, an estimated 60-75% are partial liquidations on the same set of underlying positions — the engine repeatedly clipping the same overleveraged long as price ratchets down. The number of *distinct positions* affected is roughly 4,000-6,000.
- **Concentration in a few minutes.** A typical high-count day has a ~5-15 minute window in which 30-50% of the day's liquidations occur. Outside that window, baseline liquidation rate continues at maybe 50-100 per hour.
- **Pair distribution is heavy-tailed.** BTC-PERP and ETH-PERP account for the most *notional* but not the most *count*; long-tail altcoin perps with high maintenance margin frequently produce many small-dollar liquidations during cross-asset crashes.
- **HLP P&L is the diagnostic.** Whether the day was *profitable* for HLP depositors — meaning the vault captured the liquidation premium and ended the day net positive — or *adverse* (HLP took inventory and bled mark-to-market) is the single most important question. On 2026-04-06 HLP closed the day positive by all public metrics, indicating the cascade was a clean bid-fill scenario rather than an HLP-trapping event.

A high-liquidation day is not in itself bearish for HLP; the dangerous days are the ones where the engine is forced into HLP at unfavorable prices and HLP's quote-driven hedge cannot offload before mark moves further. See [[2025-03-jellyjelly-hlp-attack]] for the canonical example of a *bad* high-liquidation day.

## The JELLYJELLY Exploit Illustrated

In March 2025, an adversarial trader (or coordinated group) used the **JELLYJELLY** perp — a thin-liquidity HIP-3 listing — to inflict a paper loss on HLP. The attack vector exploited the interaction of three engine features:

1. **Long-tail listing means low public-book depth.** JELLYJELLY's public CLOB had minimal resting liquidity; HLP was effectively the dominant counterparty.
2. **The mark was on-chain and movable.** The three-source-median protection only applies to assets with cross-venue mid-price feeds; HIP-3 listings rely on builder-configured oracles with weaker manipulation-resistance.
3. **HLP must absorb at the liquidation price.** When the attacker pushed mark to a level that triggered their own (deliberately leveraged) opposite-side position, the engine's Tier 2 fallback to HLP forced the vault into a large inventory at a price that the attacker had constructed.

The reported HLP paper loss was ~**$13M**, ultimately mitigated by community/governance intervention that delisted or constrained the market mid-incident. The post-mortem identified several engine improvements:

- Tighter maintenance margins and lower max leverage on long-tail HIP-3 listings.
- Caps on HLP's inventory exposure per pair, regardless of liquidation flow.
- Manual delist capability for markets where mark integrity has been compromised.

The structural lesson, which applies generally and not only to Hyperliquid, is that **liquidation engines that route to a backstop at the liquidation price are exploitable when the attacker controls both the trigger (mark) and the captive counterparty (a thin-book pair)**. This is a flaw shared in spirit with [[gmx|GMX V1]]'s 2022 AVAX-perp exploit, where a single trader manipulated the AVAX oracle to extract from the GLP pool. The mechanics differ; the attack pattern is the same.

For HLP depositors, JELLYJELLY revealed that pair-level exposure caps are essential, and that the protocol's willingness to intervene mid-attack is an under-appreciated form of soft-governance insurance. For traders, it is a reminder that *the cleanest cascades to fade are on liquid majors* — long-tail perps may have larger overshoots but also larger black-swan risk on the mark itself.

## Trader Implications

### For the Hyperliquid Trader (avoiding liquidation)

- **Use isolated margin.** Cross-margin cascades a single bad position into all your other positions; isolated margin localizes the failure. The engine will still partial-liquidate isolated positions but won't pull from your other equity.
- **Stay well below the maintenance buffer.** A position at 2× the maintenance margin requirement has roughly 50% more drawdown headroom than one at 1× before triggering. Given the engine's mark-price latency (the three-source median's 100-300ms lag), a position at exactly the trigger will often be liquidated even on a brief mark move that reverses immediately.
- **Avoid long-tail HIP-3 markets at high leverage.** The maintenance-margin tiers are wider precisely because the mark is more manipulable; the engine has less protective headroom.
- **Watch for funding-rate spikes.** High positive funding ([[funding-rate]]) means the leveraged-long book is heavy and a cascade is more likely; a position at modest leverage in such an environment is at higher *conditional* risk than the headline leverage suggests. See [[funding-rate-arbitrage]].
- **Sub-account isolation.** Use separate sub-accounts for unrelated strategies. A liquidation in one sub-account does not propagate.

### For the HLP Depositor (which liquidations grow vs shrink the vault)

- **Many small liquidations on liquid pairs grow HLP.** When BTC, ETH, or SOL print a flush and the public book absorbs most of the flow, HLP earns spread on its market-making layer and the small fraction routed to Tier 2 is a clean buy-low / sell-high P&L event.
- **Single large liquidations on thin pairs shrink HLP.** When a long-tail HIP-3 perp produces a single forced liquidation that exhausts the public book, HLP absorbs the residual at the liquidation price and is trapped in inventory until either (a) mark recovers or (b) HLP can offload over time. JELLYJELLY-style attacks are the worst form.
- **Sustained one-sided liquidation flow shrinks HLP.** A multi-hour cascade where 95% of liquidations are long-side leaves HLP heavily long the asset at a falling mark. Even on liquid pairs, this is the most damaging regime — HLP's hedging capacity is finite and slow.
- **Monitor HLP positioning, not just APR.** APR is the trailing return; HLP's *current inventory* is the leading indicator. A large net-long HLP position during a falling mark is a leading risk signal that depositors should pay attention to.

### For the Cascade Trader (precise signals to act on)

- **Liquidation feed is on-chain, real-time.** Hyperliquid's `liquidation` events are queryable directly from the L1 with no aggregator latency. This is the cleanest input available for any [[liquidation-cascade-fade]] implementation in crypto.
- **Mempool watching is a decisive edge.** Because liquidation orders appear in mempool before execution, an operator running a node can in principle pre-position bids at the price the engine is about to sweep through. This is closer to MEV than to discretionary trading.
- **Three-source-median lag is exploitable.** When all three of (HL mid, Binance mid, OKX mid) move together, mark moves immediately. When only one or two move, mark lags. A trader watching cross-venue spot can predict mark trajectory ahead of the engine — useful for entry timing.
- **HLP positioning is your fade ally.** When HLP is heavily long after a cascade leg, HLP itself is *also* a trapped long, and HLP's eventual offloading provides a soft ceiling on the snapback. This is information no CEX cascade trader has.
- **Beware ADL.** A perfectly-timed cascade fade on Hyperliquid is more vulnerable to ADL than the same trade on Binance, because HLP's failure-state directly triggers ADL on profitable counterparties. The fade trader's risk is asymmetric — they cannot win as much as the unconstrained trade implies because their *winning* trades are precisely the ones most likely to be ADL'd.

## Related

- [[hyperliquid]] — the venue itself, market list, trading features
- [[hyperliquid-vault-architecture]] — HLP vault internals, deposit/withdraw mechanics, governance
- [[hyperliquid-oracle-mechanics]] — three-source median construction, HIP-3 oracle feeds
- [[hyperliquid-hlp-basis-arbitrage]] — depositor-side strategy + active HLP-aware trading
- [[liquidation]] — general background on perpetual liquidations
- [[liquidation-cascade-fade]] — contrarian directional fade strategy
- [[liquidation-cascade-arbitrage]] — keeper-side liquidation as a yield strategy (lending protocols)
- [[insurance-fund]] — generic insurance-fund mechanism across exchanges
- [[mark-price]] — mark vs last vs index price construction
- [[auto-deleveraging]] — ADL mechanic in detail
- [[perpetual-futures]] — the underlying instrument
- [[order-book]] — CLOB microstructure
- [[funding-rate]], [[funding-rate-arbitrage]] — leveraged-book tells before cascades
- [[order-flow]], [[order-flow-analysis]] — CVD-based exhaustion signals
- [[flash-crashes]] — the regime cascade-fade strategies target
- [[2024-03-hyperliquid-cascade]] — early Hyperliquid cascade event analysis
- [[2025-03-jellyjelly-hlp-attack]] — coordinated attack on HLP via thin-pair manipulation
- [[2020-03-12-black-thursday-crypto]] — pre-modern engine cascade for comparison
- [[gmx]], [[dydx]] — comparable DEX engines
- [[market-microstructure]] — domain parent
- [[edge-taxonomy]] — for framing why cascade trading is structurally edged

## Sources

- **Hyperliquid Documentation.** [https://hyperliquid.gitbook.io/](https://hyperliquid.gitbook.io/) — Official docs covering margin tiers, mark-price construction, HLP vault mechanics, ADL behavior, and HIP-3 listing rules.
- **Hyperliquid on-chain data via QuickNode SQL Explorer (2026-04-06).** Daily liquidation counts, HLP vault TVL, position distributions; the source of the 17,214 / 32,964 / 10,406 daily-liquidation figures referenced above.
- **HypurrScan and similar Hyperliquid analytics dashboards.** HLP positioning, vault P&L, top-position tracking. See [[hyperliquid-hlp-basis-arbitrage]] sources.
- **JELLYJELLY incident post-mortems (March 2025).** Multiple community analyses (Hyperliquid forums, Twitter/X threads from active HLP depositors and Hyperliquid validators); see [[2025-03-jellyjelly-hlp-attack]] for the dedicated event page.
- **2024-03 Hyperliquid memecoin cascade.** ~5% HLP drawdown over 48h followed by full recovery; documented in [[2024-03-hyperliquid-cascade]] and [[hyperliquid-hlp-basis-arbitrage]].
- **Comparative engine documentation.** Binance Futures Risk Management (insurance-fund disclosures), Bybit Insurance Pool (semi-annual), GMX V2 docs (GLP/GM absorption mechanics), dYdX v4 protocol docs (insurance fund + ADL).
- **Cascade microstructure literature.** Ali, Z. *"Anatomy of the Oct 10–11, 2025 Crypto Liquidation Cascade,"* SSRN 5611392 (2025) — on cross-exchange cascade contagion, applicable directly to Hyperliquid given its mark depends on Binance/OKX feeds. Amberdata *"How $3.21B Vanished in 60 Seconds"* — partial-liquidation timing analysis.
- **Hyperliquid entity page** ([[hyperliquid]]) — the parent reference with platform statistics, fee structure, and competitive landscape.
