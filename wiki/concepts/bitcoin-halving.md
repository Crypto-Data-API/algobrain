---
title: "Bitcoin Halving"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [crypto, bitcoin, supply, cycles, market-microstructure]
aliases: ["Bitcoin Halving", "The Halving", "Halvening"]
related: ["[[bitcoin-cycle-regime]]", "[[btc-dominance]]", "[[crypto-market-regime-taxonomy]]", "[[institutional-flow-regime]]", "[[bitcoin]]"]
---

The **Bitcoin halving** (also "the halvening") is a hard-coded protocol event that cuts the [[bitcoin|BTC]] block subsidy in half every **210,000 blocks** — roughly every four years at Bitcoin's ~10-minute target block time. It is the mechanism that enforces Bitcoin's disinflationary issuance curve and its fixed terminal supply of 21 million BTC. For traders, the halving is the anchor of the classic four-year "Bitcoin cycle," though the arrival of US spot ETFs in 2024 has likely altered that pattern.

---

## What the Halving Is

New bitcoin enters circulation only as the **block subsidy** — the freshly minted BTC paid to the miner who appends a valid block. The protocol reduces this subsidy by 50% at every 210,000-block interval. Because issuance falls geometrically while the supply cap is fixed, total BTC supply asymptotically approaches 21 million; the final fraction of a coin is expected to be mined around the year **2140**, after which miners are compensated by transaction fees alone.

The halving is fully deterministic: the block height is known in advance, so the *event* is predictable even though the *date* drifts slightly with actual block times. This predictability is central to the "priced-in" debate (below).

---

## Halving Schedule

| Halving | Approx. date | Block height | New subsidy | Daily issuance (approx.) |
|---|---|---|---|---|
| Genesis | 2009-01 | 0 | 50 BTC | ~7,200 BTC |
| 1st | 2012-11 | 210,000 | 25 BTC | ~3,600 BTC |
| 2nd | 2016-07 | 420,000 | 12.5 BTC | ~1,800 BTC |
| 3rd | 2020-05 | 630,000 | 6.25 BTC | ~900 BTC |
| 4th | 2024-04 | 840,000 | 3.125 BTC | ~450 BTC |
| 5th (next) | ~2028 | 1,050,000 | 1.5625 BTC | ~225 BTC |

After the 2028 halving the subsidy continues to halve (~0.78 BTC ~2032, and so on) until issuance rounds to zero. By design, roughly 93–94% of all bitcoin that will ever exist had already been mined by the 2024 halving, so each successive halving shrinks an ever-smaller slice of remaining issuance.

---

## Supply-Shock Thesis

The dominant bull-case framework: each halving instantly cuts the *flow* of new BTC sellable by miners by ~50%. Miners are structurally forced sellers (they must cover fiat-denominated electricity and hardware costs), so they represent persistent supply pressure. Halving that pressure, while demand is constant or rising, implies upward price pressure — the "supply shock."

This logic underpins models like stock-to-flow (S2F), which frame each halving as roughly doubling Bitcoin's scarcity ratio. S2F was influential through the 2020–2021 cycle but **broke down badly afterward** and is not treated as reliable.

**The counter-argument** is market efficiency: the halving date and magnitude are known years in advance, so any predictable supply effect should already be discounted in the price. The "priced-in vs. supply-shock" tension remains one of the most actively debated questions in crypto, and there is no settled resolution.

---

## The Historical Four-Year Cycle (Pre-ETF)

Across the first three halvings, BTC exhibited a recognizable rhythm that traders codified into the [[bitcoin-cycle-regime]]:

| Halving | Halving price (approx.) | Subsequent cycle high | Time to peak |
|---|---|---|---|
| 2012-11 | ~$12 | ~$1,100 (2013-11) | ~12 months |
| 2016-07 | ~$650 | ~$19,800 (2017-12) | ~17 months |
| 2020-05 | ~$8,700 | ~$68,800 (2021-11) | ~18 months |
| 2024-04 | ~$64,000 | cycle in progress | — |

The stylized pattern: a **pre-halving accumulation/ramp**, a multi-month **lag** after the event (price often chops or grinds for ~3–6 months before the major leg up), a parabolic blow-off roughly **12–18 months post-halving**, then a deep bear market (drawdowns of 75–85%) into the next accumulation phase. This is the backbone of the four-phase model in [[bitcoin-cycle-regime]] and informs [[crypto-market-regime-taxonomy]].

**Critical caveats:**
- The sample size is **n = 3 completed cycles** — far too small to be statistically robust. Pattern-matching on four-year cycles is a narrative, not a tested edge.
- Each cycle's percentage gain has **diminished** as Bitcoin's market cap grew (diminishing-returns / "log-decay" observation).
- Confounding macro factors (2017 ICO mania, 2020–2021 COVID liquidity and zero rates) plausibly drove more of the price action than the halving itself.

---

## ETF Era: The Cycle May Be Broken

The launch of **US spot Bitcoin ETFs in January 2024** — months before the fourth halving — introduced a demand-side force with no precedent in prior cycles. This matters for the halving thesis in two ways:

1. **Scale of demand vs. supply.** Post-2024 miner issuance is only ~450 BTC/day. Spot-ETF net inflows on active days have repeatedly **dwarfed** new issuance, meaning the marginal price is now set far more by institutional flow than by the (already tiny) change in miner supply. The halving's supply delta is increasingly a rounding error against ETF and treasury-company demand.
2. **Timing distortion.** BTC made a new all-time high *before* the 2024 halving — behavior that never occurred in earlier cycles, where new highs came well after. This suggests ETF front-running and continuous institutional bid have **dampened and possibly desynchronized** the classic post-halving lag-then-parabola pattern.

The practical takeaway: treat the pre-2024 four-year cycle as a **historical regularity that may no longer hold**. The demand regime captured in [[institutional-flow-regime]] is now at least as important as the halving supply mechanic, and arguably more so. See [[bitcoin-cycle-regime]] for how this caveat is handled in regime classification.

---

## Miner Economics

The halving is, mechanically, a **revenue event for miners**: block-subsidy income halves overnight while electricity and hardware costs do not. Consequences:

- **Margin compression.** Higher-cost (older-rig, expensive-power) miners are pushed below breakeven and capitulate — powering down rigs.
- **Hashrate dip and difficulty adjustment.** As miners go offline, network hashrate falls; Bitcoin's difficulty adjustment (every 2,016 blocks) then lowers difficulty, restoring profitability for surviving miners. This shakeout typically resolves over weeks to a few months.
- **Hash Ribbons / capitulation signal.** The "Hash Ribbon" indicator (short vs. long moving averages of hashrate) flags miner capitulation; the *recovery* crossover after a halving-driven capitulation has historically marked attractive long entries — again, a small-sample heuristic, not a proven edge.
- **Forced selling reduction.** As weak miners exit and survivors run more efficiently, structural miner sell-pressure tends to fall — feeding back into the supply-shock narrative.

Over time, as the subsidy shrinks toward zero, **transaction fees** must replace it as miner revenue; the long-run security budget of the network depends on fee demand growing as subsidies decay.

---

## Trading Relevance

- **Pre-halving ramp:** markets tend to anticipate the event, with accumulation building in the 6–12 months prior. The halving itself is rarely a clean "buy the date" catalyst.
- **Post-halving lag:** historically a multi-month chop/consolidation followed the event before the major move — the event is not an immediate trigger.
- **Narrative and flows:** halvings draw heavy media attention and retail inflows; the story itself can be a self-fulfilling demand driver regardless of the underlying supply math.
- **Regime input, not a standalone signal:** the halving is best used as one input into a broader regime read (see [[bitcoin-cycle-regime]], [[crypto-market-regime-taxonomy]], [[btc-dominance]]) rather than a mechanical trade trigger. In the ETF era, cross-check the supply thesis against [[institutional-flow-regime]].
- **Beware overfitting:** with only three completed cycles, any "halving strategy" backtest is fitting to a handful of observations. Treat conclusions as low-confidence.

---

## Related

- [[bitcoin-cycle-regime]] — the four-phase cycle model that this event anchors
- [[institutional-flow-regime]] — ETF/treasury demand that has likely altered the classic cycle
- [[btc-dominance]] — BTC vs. altcoin capital rotation across cycle phases
- [[crypto-market-regime-taxonomy]] — where the halving cycle sits among crypto regimes
- [[bitcoin]] — the asset subject to halving events

---

## Sources

No external source documents have been ingested for this page yet; content reflects well-established, publicly documented protocol facts (halving schedule, subsidy amounts, block heights) and widely cited historical price/cycle observations. ETF-era impact reflects the 2024 spot-ETF launch and is noted as an evolving, contested interpretation. Future ingestions should add cited sources for the cycle and ETF-flow claims.
