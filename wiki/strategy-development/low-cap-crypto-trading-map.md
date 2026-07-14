---
title: "Low-Cap Crypto Trading Map"
type: concept
created: 2026-05-04
updated: 2026-07-13
status: excellent
tags: [strategy-development, crypto, solana, memecoin, sniping, pump-fun, bonding-curve, mev, microcap, low-cap, research]
aliases: ["Low-Cap Trading Map", "Memecoin Trading Map", "Solana Microcap Map", "Pump.fun Strategy Map"]
domain: [crypto, sniping, memecoin]
difficulty: advanced
related: ["[[asterdex-perp-trading-map]]", "[[hyperliquid-perp-trading-map]]", "[[arbitrage-opportunity-map]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[failure-modes]]", "[[strategy-correlation-matrix]]", "[[pump-fun]]", "[[raydium]]", "[[pumpswap]]", "[[memecoin-sniping]]", "[[pump-fun-bonding-curve-sniping]]", "[[token-migration-sniping]]", "[[jito-bundle-sniping]]", "[[jito-solana-mev-arbitrage]]", "[[axiom-pro]]", "[[bonkbot]]", "[[trojan-bot]]", "[[bitquery]]", "[[telegram-bot-trading]]", "[[cryptodataapi]]"]
---

# Low-Cap Crypto Trading Map

A comprehensive strategy map for trading the **Solana low-cap / memecoin meta** — the ecosystem of token launchpads, AMMs, sniping bots, and microcap discovery flow that emerged around [[pump-fun|Pump.fun]] in 2024 and matured through 2025-26. This is the companion to [[asterdex-perp-trading-map]] and [[hyperliquid-perp-trading-map]]: where those maps cover *perpetual futures on transparent and private order books*, this map covers *spot launches, bonding curves, and graduation flow on Solana AMMs*.

The asterdex map's organizing question is "given a venue's microstructure, which alphas does it enable?" The same question applies here, but the venue is not a single exchange. It is a **stack**: a launchpad ([[pump-fun]]), a bonding-curve mechanism, a graduation event, an AMM ([[raydium]] or [[pumpswap]]), an aggregator ([[jupiter-exchange-solana|Jupiter]]), an MEV layer ([[jito-solana-mev-arbitrage|Jito]]), and a layer of front-end bots ([[axiom-pro|Axiom Pro]], [[bonkbot|BonkBot]], [[trojan-bot|Trojan]], Maestro, Photon, GMGN, BullX) that abstract execution for retail and pro traders.

This page does not invent strategies. It synthesizes the strategies that already have wiki pages, organizes them by entry mechanism and edge type, and tells the truth about how each one decays.

---

## Platform Profile: What Makes the Solana Low-Cap Stack Different

### Key Stack Components

| Layer | Component | Role |
|---|---|---|
| Launchpad | [[pump-fun]] | Permissionless token launch on a deterministic bonding curve; token graduates to AMM at ~$69k cumulative buys. |
| Bonding curve | Pump.fun internal | Deterministic price-impact curve; early buyers always lower cost basis. |
| Graduation venue | [[raydium]] (historically), [[pumpswap]] (newer default) | Where graduated tokens become AMM-tradeable. |
| Aggregator | [[jupiter-exchange-solana|Jupiter]] | Routes swaps across Raydium, PumpSwap, and other Solana AMMs. |
| MEV layer | [[jito-solana-mev-arbitrage|Jito]] | Bundle auction and Block Engine; the execution path for serious snipers. |
| Front-end bots | [[axiom-pro|Axiom Pro]], [[bonkbot|BonkBot]], [[trojan-bot|Trojan]], Maestro, Photon, GMGN, BullX, XXYY | Abstract sniping/copy/limit orders for non-developers. |
| Analytics | [[bitquery|Bitquery]], [[dexscreener-com|Dexscreener]], [[birdeye-so|Birdeye]], SolanaFM, [[dune-analytics|Dune]] | Real-time data feeds, holder dashboards, leaderboards. |

### The Five Structural Realities of the Low-Cap Meta

**1. Launches are programmable, not curated.**

Anyone can launch a token on Pump.fun for ~$2 in fees. The vast majority are noise. The ones that matter for trading are detected by *programmable filters* (dev wallet history, holder distribution, social-signal velocity), not by human curation.

**Strategic implication:** Edge lives in the filter pipeline, not in the trade itself. The best sniper is the one whose pre-trade screen is most accurate at distinguishing organic launches from rugs and bundles.

**2. The bonding curve is a deterministic ramp, then a discrete cliff.**

For the first $69k of cumulative buys, price evolves on a deterministic curve. At graduation, the price-discovery regime *changes discretely* to AMM dynamics. Two distinct alphas live on either side of this boundary: [[pump-fun-bonding-curve-sniping|bonding-curve sniping]] (pre-graduation) and [[token-migration-sniping|migration sniping]] (graduation moment).

**Strategic implication:** A serious operator runs both, with the same watchlist feeding both entry types.

**3. Solana mempool dynamics enable MEV — and require defense.**

Without protection, sniper buys leak to sandwich bots that frontrun and backrun the trade. [[jito-bundle-sniping|Jito bundles]] are the structural defense. Operating without bundles on contested launches is a transfer to MEV bots.

**Strategic implication:** Bundle execution is not optional infrastructure for serious snipers — it is the floor.

**4. The bot stack abstracts but does not eliminate the underlying mechanics.**

[[axiom-pro|Axiom Pro]], [[bonkbot|BonkBot]], [[trojan-bot|Trojan]], Maestro, Photon, GMGN, BullX, XXYY all wrap the same primitives (Pump.fun launch detection, bonding-curve interaction, Raydium/PumpSwap routing, Jito bundle submission). Choosing a bot is choosing a UX and a fee structure. The *mechanics being executed* are the same across vendors.

**Strategic implication:** Bot vendor choice matters for fees, latency, and feature set, but the underlying strategies are identical. Don't confuse "I use Axiom" with "I have an edge."

**5. Edge decay is the dominant fact.**

2024 was the year of obvious edges: any decent rug filter + early-launch entry was profitable. 2025 narrowed the edges as bot competition intensified. By 2026 the meta requires niche specialization (specific dev-wallet-cluster tracking, social-signal arbitrage, regime detection) plus robust execution infra to remain net-positive. A strategy that worked in early 2024 likely does not work today without significant adaptation.

**Strategic implication:** Treat edge as perishable. Re-validate monthly. Be honest about whether you are extracting alpha or paying tuition to MEV bots.

---

## Strategy Index (At a Glance)

Every strategy on this page, the stack phase it acts in, its [[edge-taxonomy|edge source]], and its honest 2026 edge. The "screen/overlay" rows are universal multipliers, not standalone trades.

| # | Strategy | Stack phase | Underlying page | Edge source | 2026 edge |
|---|---|---|---|---|---|
| 1 | Bonding-curve sniping | Pre-graduation | [[pump-fun-bonding-curve-sniping]] | Latency + structural + informational | Thin |
| 2 | Curve-inflection entry | Pre-graduation | [[pump-fun-bonding-curve-sniping]] | Structural + informational | Moderate |
| 3 | Pre-graduation exit discipline | Pre-graduation | [[pump-fun-bonding-curve-sniping]] | Behavioral (overlay) | Critical |
| 4 | Token migration sniping | Graduation | [[token-migration-sniping]] | Latency + structural | Thin |
| 5 | Post-graduation reversal | Graduation | [[memecoin-sniping]] | Behavioral + informational | Moderate |
| 6 | Market-cap levels trading | AMM phase | [[memecoin-sniping]] | Behavioral | Thin |
| 7 | Holder filtering (screen) | All phases | [[memecoin-sniping]] | Structural (overlay) | Critical |
| 8 | Rug detection (screen) | All phases | [[memecoin-sniping]] | Structural (overlay) | Critical |
| 9 | Bot-stack copy trading | AMM phase | [[telegram-bot-trading]] | Borrowed | Variable |
| 10 | Jito bundle sniping (execution) | All buy-side | [[jito-bundle-sniping]] | Latency + structural (overlay) | Critical |

Read the table top-to-bottom as the token's lifecycle: launch → bonding curve → graduation → AMM. The screens (7, 8) and the execution overlay (10) apply at every stage and are *not optional* — Part 6 shows that operating without them makes every other row net-negative.

---

## Part 1: Bonding-Curve Phase Strategies

These strategies act *before* graduation, on the deterministic Pump.fun bonding curve.

### Strategy 1: Bonding-Curve Sniping (Launch Entry)

See [[pump-fun-bonding-curve-sniping]] for the full page.

**Mechanism:** Detect new token launches via on-chain monitoring. Enter within the first 1-30 seconds. Filter aggressively for dev wallet reputation, social signal, and holder distribution. Exit on a take-profit ladder or pre-graduation.

**Edge type:** Latency + structural + informational.

**Counterparty:** Latency-disadvantaged retail buyers, FOMO chasers buying further along the curve.

**Capacity:** Capped per-token at curve depth; strategy-level ~$10-50M for top operators per the existing wiki page.

**When it works:** Always-on opportunity, but particularly profitable during high launchpad activity (bull markets, viral memecoin cycles).

**When it doesn't:** Bot saturation in 2024-26 has compressed the first-second edge; non-bundle execution gets sandwiched; bad filter pipelines produce 99%+ loss rates.

---

### Strategy 2: Curve-Inflection Entry

A variant of bonding-curve sniping focused on *mid-curve inflection points* rather than launch-instant entry.

**Mechanism:** The bonding curve is non-linear; price impact accelerates as cumulative buys grow. Identify the inflection where curve velocity exceeds a threshold (organic momentum signal) and enter then, not at launch.

**Edge type:** Structural (the curve's mathematical shape) + informational (curve velocity is a momentum proxy not visible on standard charts).

**Trade-off vs. launch entry:** Lower per-trade win rate on the right tail (you're not catching the largest runs from the bottom), but higher win rate on the *that-this-token-graduates* prediction (you're entering only when momentum is real). Better median trade, worse mean trade.

**Suitable for:** Operators who want lower variance than pure launch sniping.

---

### Strategy 3: Pre-Graduation Exit Discipline

Strictly speaking not a separate strategy but a discipline overlay on the above two. The graduation event seeds a fresh AMM pool; depending on the seed mechanics, this can dilute pre-graduation holders. Many bonding-curve snipers exit 70-90% of position at ~$50k cumulative buys (well before the $69k threshold) to capture the curve top without graduation-event slippage.

**Edge type:** Behavioral discipline. The mistake snipers make is "holding for graduation" hoping the post-graduation pump pays them more than the pre-graduation top. Empirically this is a losing trade in expectation across the curve-snipe sample.

**Per [[pump-fun-bonding-curve-sniping]]'s rules:** "Pre-graduation: exit ~80% of position at $50k cumulative buys (before LP seed)."

---

## Part 2: Graduation Event Strategies

These strategies act *at* the graduation moment — the discrete liquidity transition from bonding curve to AMM.

### Strategy 4: Token Migration Sniping

See [[token-migration-sniping]] for the full page.

**Mechanism:** Detect the migration tx (bond completion + AMM pool seeding) via Bitquery / RPC subscription. Submit a Jito-bundled buy in the same slot or next slot. Capture the listing-block volatility before discovery-lagged retail arrives.

**Edge type:** Latency + structural.

**Capacity:** Per-trade ceiling ~1-2 SOL on freshly-seeded pools; strategy-level ~$1-2M.

**When it works:** Hot graduation regimes with high follow-through volume; works well in tandem with bonding-curve sniping (same watchlist, same filter pipeline).

**When it doesn't:** PumpSwap-native migrations route around Raydium/Jupiter and reduce the discovery-lag window; saturated slots push tip cost above captured edge.

---

### Strategy 5: Post-Graduation Reversal

A counter-trend variant: many tokens dump immediately after graduation as bonding-curve snipers exit. A subset of those tokens recover within minutes-hours as fresh AMM-side buyers arrive (often driven by Dexscreener / Birdeye discovery lag).

**Mechanism:** Wait 5-30 minutes after graduation. Identify graduations that:

- Did not immediately rug (LP intact, dev not dumping).
- Show fresh wallet inflows on the AMM side (not just curve-snipers exiting).
- Maintain social-signal velocity (Telegram / X mention rate not collapsing).

Enter on the AMM at the post-snipe-dump local low.

**Edge type:** Behavioral (sniper exits create a structural local low) + informational (cross-referencing AMM-side inflow vs. curve-side exits).

**Trade-off:** Lower win rate than migration sniping, but each winner runs farther because you're not exiting at the listing-block top.

---

## Part 3: AMM-Phase Strategies (Post-Graduation Microcap Trading)

These strategies act on tokens *after* graduation, on the AMM venue, before they become "midcap" and qualify for normal technical analysis.

### Strategy 6: Market-Cap Levels Trading

Per the [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi|April 2026 gap-finder source]] (citing the trader Sajad), only two indicators are needed for low-cap trading: **market cap psychological levels** ($100k, $500k, $1M, $5M, $10M) and **support/resistance**. These thresholds act as both:

- **Resistance** — sellers cluster at round-number MC because retail screens use them as targets and bots use them as sell triggers.
- **Support** — buyers cluster on the way down at the same levels.

**Mechanism:**

- Identify tokens approaching a major MC level from below.
- Enter on a confirmed S/R structure at the prior level.
- Take profits at the next level.
- Exit if the level fails decisively.

**Edge type:** Behavioral. The MC level is psychological, not fundamental. The edge exists because enough retail uses MC as a reference frame to make the levels self-fulfilling.

**Suitable for:** Discretionary or semi-automated traders without sniping infrastructure. This is the cheapest entry into the low-cap meta.

**Decay note:** As more bots target the same MC levels, breakouts become noisier and stop-outs more common. The edge is real but thin and has been compressing.

---

### Strategy 7: Holder Filtering as Continuous Screen

Not a trade by itself, but a *continuous filter* applied across all the above strategies. Per the gap-finder source [4]: bots like XXYY raised win rates from ~1% to ~20%+ by filtering out bundled launches (top holders concentrated in a few wallets, often signaling coordinated dump risk).

**Mechanism:**

- Top-10 holder concentration < 30-40%.
- Dev wallet < 5% of supply (or locked / burned).
- LP locked / burned (verifiable on-chain).
- No hidden mint authority.
- Buy/sell pattern looks organic (many small wallets, not a handful of large ones).

This pipeline is the difference between a profitable sniping book and a tuition-paying one. It is the single highest-leverage piece of infrastructure in the entire low-cap meta.

---

### Strategy 8: Rug Detection as Continuous Screen

Per gap-finder sources [1] and [3]: pre-trade rug checks are non-negotiable. No indicator strategy works in the presence of a rug — the asset goes to zero regardless of chart structure.

**Mechanism:**

- LP lock / burn verification.
- Dev wallet historical activity (has this dev rugged before?).
- Mint authority status (renounced or active?).
- Honeypot tester (can the contract actually sell?).
- Bundled-holder pattern detection (per Strategy 7).

Tools like RugCheck, [[birdeye-so|Birdeye]]'s safety scans, and the screens built into [[axiom-pro|Axiom Pro]] / Maestro / GMGN automate most of this. A trader without these screens is gambling, not trading.

---

### Strategy 9: Bot-Stack Copy Trading

The bot stack ([[axiom-pro|Axiom]], [[bonkbot|BonkBot]], [[trojan-bot|Trojan]], Maestro, Photon, GMGN, BullX) provides copy-trade features for tracked top wallets. The mechanism is straightforward: identify a wallet that has demonstrated repeatable alpha on Pump.fun, then mirror its trades.

**Per [[asterdex-perp-trading-map#Strategy 10 EchoSync Copy Trading as Passive Alpha|the asterdex map's analysis of copy trading]]:** copy trading is "renting someone else's edge." It works only if (a) the target trader's edge is real and not lucky-streak survivorship, (b) the copying delay is small enough that the signal hasn't decayed, and (c) the copier's market impact doesn't degrade the source's alpha.

**On Solana low-cap:**

- Copy delay is dominated by RPC latency + bot-vendor latency, typically 100-500ms.
- The source trader's edge may be specific to their dev-wallet-cluster knowledge, which doesn't transfer.
- Capacity is brutal: if 1,000 wallets copy the same trader on a $20k-MC token, the collective buying impact destroys the trade for everyone including the source.

**Best use case:** Diversified copy across 5-10 tracked wallets, allocated as a satellite (5-15%) of the low-cap book, never as core strategy.

---

## Part 4: Execution Layer Strategy

### Strategy 10: Jito Bundle Sniping (Execution Wrapper)

See [[jito-bundle-sniping]] for the full page.

**Mechanism:** Wrap any of the above buy-side strategies in a [[jito-solana-mev-arbitrage|Jito]] bundle to defend against sandwich attacks and gain leader-targeted execution priority.

**Edge type:** Latency + structural (MEV defense).

**Per-trade contribution:** +30 to +120 bps versus naive RPC on contested fills, -30 to -80 bps on uncontested fills.

**This is not a directional strategy.** It is an execution overlay. Every serious operator in the meta uses bundles for contested flow.

---

## Part 5: Hidden Edges in the Low-Cap Meta

These are not standalone strategies but *information asymmetries* that compound the above strategies for operators who pay attention.

### Hidden Edge 1: Dev Wallet Cluster Tracking

A small set of dev wallets is responsible for a disproportionate share of successful Pump.fun launches. Other clusters are responsible for a disproportionate share of rugs. Maintaining a personal database of dev-wallet behavior — beyond the public rug DBs — is a durable informational edge.

**Implementation:** Tag every snipe with the dev wallet. Track outcomes. Build a personal scoring model that weights wallets by historical win rate, average return per launch, and rug rate. Bias size and entry aggression toward high-scoring wallets.

**Why it persists:** Dev wallets are pseudonymous but on-chain and persistent. Public databases capture the obvious cases but miss the long tail.

---

### Hidden Edge 2: Migration-Venue Routing Asymmetry

Per the gap-finder source: "PumpSwap launches Pump.fun's native DEX for graduates" (Dec 2025), and Bitquery integration enables faster migrations. There is now a real arb between Raydium-graduated and PumpSwap-graduated tokens during the window where one venue's pool is liquid and the other isn't yet (or where Jupiter has indexed one but not the other).

**Implementation:** Detect migration venue. If PumpSwap-only, the discovery-lag window vs. Raydium-routed users is longer (Jupiter-using retail can't easily route until indexed). This *extends* the migration-sniping edge for operators who watch the right pool.

---

### Hidden Edge 3: Social-Signal Velocity vs. Price Velocity

A token whose social-signal velocity (Telegram member growth rate, X mentions per minute) is rising faster than its price velocity has under-priced momentum. The reverse — price racing ahead of social signal — is over-priced.

**Implementation:** Maintain a real-time stream of social metrics per token in the watchlist. Compute a Z-score of (social velocity / price velocity) and overlay on entry decisions. This is informational edge — it requires a data pipeline, not just a chart.

**Caveat:** Social signal can be manufactured (paid promotion, bot armies). Filter for organic patterns vs. coordinated artificial inflation.

---

### Hidden Edge 4: Bonding-Curve Velocity as Graduation Predictor

Per the gap-finder source [5]: "sustainable curves predict bonds vs. rugs." A bonding curve moving smoothly with diverse buyers is far more likely to graduate than one with a few large buys followed by silence. The velocity profile (buys per minute, distinct wallets per buy) is a leading indicator for graduation probability.

**Implementation:** Score each in-progress bond by curve smoothness and buyer diversity. Bias capital toward the top quartile. Skip launches with suspicious velocity patterns even if they pass static filters.

---

### Hidden Edge 5: Bot-Vendor Latency Differential

Different front-end bots have different latencies to launches and migrations. [[axiom-pro|Axiom Pro]] is broadly considered top-tier for memecoin sniping per the gap-finder source [6]; [[bonkbot|BonkBot]] and [[trojan-bot|Trojan]] are mobile-first; Maestro emphasizes notifications; Photon and GMGN/BullX have their own niches. There is real, measurable latency dispersion across these vendors on the same launch.

**Implementation:** Run two or three bots in parallel on the same watchlist for a calibration period. Measure per-launch latency. Allocate the highest-priority entries to the lowest-latency vendor.

**Decay note:** Bot-vendor latency rankings shift as vendors upgrade infrastructure. Re-calibrate quarterly.

---

## Part 6: Strategy Decay and Kill Criteria

The dominant fact about the low-cap meta is that *every strategy decays*, often within months. This section is the truth-telling layer.

### Per-Strategy Decay Profiles (Honest Assessment)

| Strategy | 2024 Edge | 2025 Edge | 2026 Edge | Decay Driver |
|---|---|---|---|---|
| Bonding-curve sniping (launch entry) | Large | Moderate | Thin | Bot saturation of first-second window |
| Curve-inflection entry | Moderate | Moderate | Moderate | Less crowded; still works for patient operators |
| Migration sniping | Large | Moderate | Thin | Slot-level competition + Jito tip floor escalation |
| Post-graduation reversal | Moderate | Moderate | Moderate | Less automated; discretionary edge persists |
| MC-levels trading | Moderate | Thin | Thin | Self-fulfilling bots crowd the same levels |
| Holder filtering | Critical (universal multiplier) | Critical | Critical | Bundlers evolve; filters must follow |
| Rug detection | Critical (universal multiplier) | Critical | Critical | New rug patterns appear; tooling must update |
| Copy trading | Variable | Variable | Variable | Capacity-constrained; depends entirely on source |
| Jito bundle execution | Critical (universal multiplier) | Critical | Critical | Tip floor erodes margin but bundles remain mandatory |
| Dev-wallet-cluster tracking | Moderate | Moderate | Moderate | Persistent edge for operators who maintain own DB |
| Social-velocity overlay | Moderate | Moderate | Moderate | Persistent if data pipeline maintained |

### Universal Kill Criteria for the Low-Cap Book

Retire or reduce the entire low-cap allocation if any of the following trigger:

| Signal | Action |
|---|---|
| Rolling 60-day net PnL < 0 across all sub-strategies combined | Halt new entries; review filter pipeline before re-enabling |
| Pump.fun daily new-launch count drops > 75% from trailing 90-day average | Reduce exposure proportionally; the meta is dying or migrating |
| PumpSwap migration share > 95% AND PumpSwap-specific edge unworkable | Migration sniping retired; reassess other strategies |
| Jito bundle land rate < 30% sustained 14 days after tip recalibration | Investigate competitor displacement; consider non-bundle paths for lower-value flow |
| Pump.fun protocol shutdown, regulatory action, or major mechanic change | Immediate halt; reassess the entire stack |
| Solana network instability > 4 hours total in 7 days | Reduce position sizes; prioritize liquid exits |
| Dev-wallet-cluster DB win rate drops below 5% for 30 days | Filter pipeline is stale; rebuild before further deployment |
| Average MEV-tax-avoided per bundle drops below tip cost for 30 days | Bundle premium no longer earning its keep on at least some flow |

### Per [[failure-modes]]: The Four Killers in This Meta

1. **Leverage.** The low-cap meta is spot-only. There is no leverage primitive built in. The few attempts to add perp markets on memecoins (via [[hyperliquid-perp-trading-map|Hyperliquid]] or other venues) inherit all the cascade risk of those venues plus the underlying volatility of the memecoin. Avoid leveraged exposure in this meta entirely.

2. **Position concentration.** A 10% allocation to a single Pump.fun launch is not aggressive — it is suicidal. The base rate of total loss per launch is too high. Even high-conviction snipes should be 0.5-2% of the dedicated low-cap book.

3. **Holding past the take-profit ladder.** The single most expensive mistake in this meta is watching a 5x become a 10x become a 0. Discipline on the ladder is the difference between a profitable book and a story about the trade you "should have sold."

4. **Operating without rug filters or bundle execution.** Either of these alone is enough to make a strategy net-negative regardless of how good the entry signal is.

---

## Part 7: Capital Sizing and Portfolio Construction

### Sizing Within the Low-Cap Book

The low-cap meta is inherently a *portfolio of lottery tickets*, not a single concentrated bet. Sizing principles:

| Sub-strategy | Allocation of low-cap book | Per-trade size cap | Rationale |
|---|---|---|---|
| Bonding-curve sniping | 25-40% | 0.5-2 SOL | High volume, lottery shape, needs many shots |
| Migration sniping | 15-25% | 0.5-2 SOL | Slot-constrained per-trade ceiling |
| Post-graduation reversal | 10-20% | 1-5% of low-cap book | Lower frequency, higher per-trade conviction |
| MC-levels trading | 10-20% | 1-3% of low-cap book | Discretionary, slower pace |
| Copy trading (satellite) | 5-15% | Per copied trade size | Diversified across 5-10 source wallets |
| Reserve (idle SOL) | 10-20% | n/a | For opportunistic entries, network fees, gas during congestion |

### Sizing the Low-Cap Book Within a Total Portfolio

The low-cap meta has the highest variance and highest decay risk of any strategy class in this wiki. A reasonable upper bound: **5-15% of total trading capital** for an operator with strong infrastructure and demonstrated edge; **0-3%** for an operator without bundle execution, holder filters, and bot infrastructure.

Per the [[strategy-correlation-matrix]] philosophy: low-cap PnL is *uncorrelated to broad crypto beta in normal regimes* but *highly correlated to broad crypto beta in stress regimes* (a market-wide risk-off kills launchpad activity along with everything else). Treat low-cap allocation as risk-on satellite, not as diversifier.

### Decision Framework — Should You Trade the Low-Cap Meta at All?

Before any strategy selection, this gate decides whether you belong in this meta:

```
Gate 1 — Infrastructure floor (non-negotiable)
  Have rug filter + holder filter (Strategies 7, 8)?   NO → do not trade; you will pay tuition
  Have Jito bundle execution (Strategy 10)?            NO → cap allocation at 0-3%; uncontested flow only
  Have launch-detection data pipeline (Bitquery/RPC)?  NO → discretionary MC-levels (Strategy 6) only

Gate 2 — Edge selection (pick by your real advantage)
  Lowest latency on the watchlist        → sniping (1, 4)
  Patience + momentum read               → curve-inflection (2), post-grad reversal (5)
  No infra, discretionary chart reader   → MC-levels trading (6)
  Own dev-wallet database                → bias all entries by Hidden Edge 1

Gate 3 — Sizing (see Part 7)
  Per-trade ≤ 0.5-2% of low-cap book (lottery shape)
  Low-cap book ≤ 5-15% of total capital (≤ 0-3% without infra)

Gate 4 — Re-validation (the perishability check)
  Rolling 60-day net PnL < 0?            → halt, rebuild filter pipeline
  Edge unchanged from last month?        → re-measure; decay is the default
```

This framework encodes the page's central thesis: in the low-cap meta the *screens and execution overlay are the edge*, and the directional strategies only monetize that edge. An operator who passes Gate 1 has a chance; one who fails it is, per Part 9, simply transferring capital to MEV bots and bundlers. Contrast with the perp venues in [[asterdex-perp-trading-map]] and [[hyperliquid-perp-trading-map]], where the infrastructure floor is a wallet and a UI — the low-cap meta's infrastructure burden is its defining structural feature.

---

## Part 8: Comparative Map — Low-Cap Stack vs. Perp Venues

Where the [[asterdex-perp-trading-map|asterdex map]] organized strategies around a single venue's microstructure, and the [[hyperliquid-perp-trading-map|hyperliquid map]] did the same for a transparent order book, this map organizes strategies around a *stack of protocols*. Some structural contrasts:

| Dimension | Low-Cap Stack | AsterDEX | Hyperliquid |
|---|---|---|---|
| Venue type | Stack: launchpad + AMM + aggregator + MEV layer | Single perp DEX with hidden orders | Single perp DEX with transparent book |
| Asset universe | Spot tokens, primarily memecoins | 358 perp pairs (crypto + stocks) | 229 perp pairs |
| Leverage available | None (spot only) | Up to 1001x | Up to 50x |
| Edge type dominance | Latency + structural + informational | Structural (hidden orders) + capital efficiency | Informational (transparent flow) + liquidity |
| Per-trade size | $50-500 typical, $5k ceiling | $1k-$1M+ | $1k-$1M+ |
| Trade frequency | High (many lottery tickets) | Variable | Variable |
| Decay speed | Fast (months) | Slower (quarters) | Slower (quarters) |
| Infrastructure burden | Heavy (bots, filters, bundles, RPC) | Light (wallet + UI) | Light (wallet + UI) |
| MEV exposure | High without defense | Low (hidden orders) | Moderate (transparent but on a single chain) |
| Win rate per trade | 5-25% | 40-60% (depends on strategy) | 40-60% (depends on strategy) |
| Reliance on right-tail | Extreme | Moderate | Moderate |

**The high-level read:** the low-cap stack is the most *infrastructurally demanding* and *fastest-decaying* meta covered in this wiki, but offers the highest per-trade upside in absolute terms. It is the closest thing in crypto trading to *option-buying with negative time value* — most of your trades expire worthless, a few pay 100x+, and the entire game is played in the right-tail of the return distribution.

---

## Part 9: What This Wiki Says Will Kill You in the Low-Cap Meta

The five fatal patterns from [[arbitrage-opportunity-map]] / [[failure-modes]], with low-cap-specific manifestations:

1. **Operating without holder/rug filters.** No indicator strategy survives a rug. Per gap-finder sources [1] and [3], filter pipeline quality determines survival, full stop. This is the *single most important fact* in the entire meta.

2. **Operating without Jito bundle execution on contested flow.** Naive RPC submission on hot launches is a transfer to MEV bots. Over hundreds of trades this compounds into the difference between profitable and unprofitable.

3. **Holding past the take-profit ladder.** The right-tail of the return distribution is real, but it is rare. Watching a 5x become a 0 because you were waiting for 100x is the #1 way profitable snipers go broke.

4. **Treating one bot vendor as a strategy.** Using [[axiom-pro|Axiom]] does not give you alpha; it gives you a UI and a fee structure for executing primitives that everyone else is also executing. Vendor choice matters; vendor choice is not strategy.

5. **Failing to re-validate edge.** The 2024 edge is not the 2025 edge is not the 2026 edge. Operators who deploy a static playbook and don't measure decay end up bleeding to bots that have evolved past their filter pipeline. Monthly re-validation is the floor.

---

## Methodology

This map synthesizes:

- The [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi|April 2026 Perplexity gap-finder source]] on the low-cap / Pump.fun ecosystem.
- The existing strategy pages: [[memecoin-sniping]], [[pump-fun-bonding-curve-sniping]], [[token-migration-sniping]], [[jito-bundle-sniping]], [[jito-solana-mev-arbitrage]], [[telegram-bot-trading]].
- The existing entity pages: [[pump-fun]], [[raydium]], [[pumpswap]], [[jupiter-exchange-solana]], [[axiom-pro]], [[bonkbot|Bonk]], [[photon-sol|Photon]], [[trojan-bot|Trojan]].
- The structural framing of [[asterdex-perp-trading-map]] and [[hyperliquid-perp-trading-map]].
- The [[edge-taxonomy]], [[regime-matrix]], [[strategy-correlation-matrix]], and [[failure-modes]] frameworks.

The goal is not to invent strategies. It is to organize the existing wiki's coverage of the low-cap meta into a single navigable map, with honest decay assessment.

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]] — primary source for the bot-stack catalog, holder/rug filter framing, MC-levels trading, and PumpSwap migration.
- [[pump-fun-bonding-curve-sniping]] — bonding-curve phase strategy detail.
- [[token-migration-sniping]] — graduation-event strategy detail.
- [[jito-bundle-sniping]] — execution-layer strategy detail.
- [[jito-solana-mev-arbitrage]] — full Jito infrastructure context.
- [[memecoin-sniping]] — broader memecoin strategy context.
- [[telegram-bot-trading]] — bot stack context.
- [[asterdex-perp-trading-map]] — sibling map (perp venue side).
- [[hyperliquid-perp-trading-map]] — sibling map (transparent perp side).
- [[arbitrage-opportunity-map]] — wiki-wide arbitrage synthesis.
- [[edge-taxonomy]] — six sources of trading edge.
- [[failure-modes]] — how strategies die.
- [[strategy-correlation-matrix]] — crisis correlation analysis.
- Pump.fun protocol documentation (program ID `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`).
- Bitquery Pump.fun API docs.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].

## Related

[[asterdex-perp-trading-map]] · [[hyperliquid-perp-trading-map]] · [[arbitrage-opportunity-map]] · [[exchange-api-reference]] · [[defi-contract-registry]] · [[edge-taxonomy]] · [[regime-matrix]] · [[failure-modes]] · [[strategy-correlation-matrix]] · [[pump-fun]] · [[raydium]] · [[pumpswap]] · [[jupiter-exchange-solana]] · [[memecoin-sniping]] · [[pump-fun-bonding-curve-sniping]] · [[token-migration-sniping]] · [[jito-bundle-sniping]] · [[jito-solana-mev-arbitrage]] · [[axiom-pro]] · [[bonkbot]] · [[trojan-bot]] · [[bitquery]] · [[telegram-bot-trading]]
