---
title: "Hyperliquid Trader — Stretch Revert Group dashboard (2026-07-20 snapshot)"
type: source
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [crypto, hyperliquid, mean-reversion, trading-bots, quantitative]
aliases: ["Stretch Revert dashboard snapshot", "Stretch Revert Group live figures"]
source_type: data
source_author: "Hyperliquid Trader (operator's own system)"
source_date: 2026-07-20
confidence: medium
claims_count: 9
related: ["[[stretch-revert]]", "[[live-journal]]", "[[frama]]", "[[vidya]]", "[[alma]]", "[[theil-sen-regression]]", "[[kama]]", "[[jurik-moving-average]]"]
---

# Hyperliquid Trader — Stretch Revert Group dashboard (2026-07-20 snapshot)

A point-in-time snapshot of the operator's own **Hyperliquid Trader** dashboard, "Stretch Revert Group" page, timestamped **2026-07-20 11:23:51 AEST**. It is the sole evidentiary basis for every live figure quoted on [[stretch-revert]] and in the [[live-journal]] entry of the same date.

> **This is a first-party operational dashboard, not a published or independently audited source.** It reports what the operator's own system recorded. Nothing here has been reconciled against exchange fill records, and no backtest, walk-forward, or cost-corrected study accompanies it.

## Provenance and confidence

| | |
|---|---|
| **Source type** | Live operational dashboard (screen content supplied to the wiki) |
| **Captured** | 2026-07-20 11:23:51 AEST |
| **Author** | The operator's own trading system |
| **Independence** | None — self-reported |
| **Reconciled against venue records?** | No |
| **Confidence** | **MEDIUM** — plausible and internally consistent, but self-reported, unaudited, and far too small a sample to support inference |

Confidence is capped at MEDIUM not because the numbers are doubted as a record of what the system did, but because the sample cannot support the conclusions a reader would naturally draw from them.

## Claims extracted

1. `[HIGH]` The Stretch Revert family comprises **14 members** in simulation; **10** run on the real-money prod bot. (Directly enumerated on the dashboard.)
2. `[HIGH]` Combined **53 fills** across simulation and production.
3. `[HIGH]` Combined realised P/L **+$50.08**.
4. `[HIGH]` Trade-weighted win rate **77%**. (Independently recomputed from the per-member rows: (28x0.79 + 7x0.71 + 10x0.80 + 8x0.75)/53 = 77.5%. Consistent.)
5. `[HIGH]` **Only 4 of 14 members have any fills** — `frama` (28, prod), `theilsen` (10, prod), `vidya` (8, sim), `alma` (7, prod). The other ten are at zero. Member counts sum to 53, matching the stated total.
6. `[HIGH]` `frama_stretch_revert`: 28 fills, 79% WR, **+$47.17** — i.e. **94% of the family's total P/L**.
7. `[HIGH]` `theilsen_stretch_revert`: 10 fills, **80% WR** but **−$3.00** net. High win rate with negative P/L.
8. `[MEDIUM]` `vidya_stretch_revert` (sim): profit factor 1.34 with Sharpe −0.06.
9. `[MEDIUM]` Execution parameters: most members ~3-5x leverage on 15m candles; `theilsen` runs 1x; `fast_kama` runs a 1-5m fast loop. (Stated on the dashboard; not independently verified.)

## What the snapshot does NOT establish

Recorded explicitly because the headline figures invite the opposite reading:

- **Not evidence of edge.** 53 fills is far below the sample needed to distinguish this from noise; the Sharpe confidence interval spans zero ([[crypto-short-history-statistical-power]]).
- **Not a 14-strategy track record.** It is a 4-strategy track record, effectively a 1-strategy record given `frama`'s 94% share.
- **Win rate is near-uninformative here.** Winning small and often then surrendering it in one unreverting move is the *expected* shape of a reversion payoff. `theilsen` demonstrates this directly: 80% wins, negative net.
- **Untested for multiple comparisons.** Fourteen variants were run; reading the best one as a result requires [[deflated-sharpe-ratio]] deflation first. For `jma_stretch_revert` this cannot be done correctly at all — [[jurik-moving-average|JMA]] is proprietary and the vendor's own search count is unknowable.
- **Says nothing about capacity or slippage.** Average trade P/L is ~$0.94; position sizes are too small to exercise book depth or reveal fill quality at size ([[execution-model-differences]]).
- **No deploy dates, capital allocation, or kill-criteria history** appear on the dashboard.

## Pages this source contributed to

- [[stretch-revert]] — created from this snapshot; supplies the live-status block and the Performance characteristics table
- [[live-journal]] — the 2026-07-20 backfill entry
- [[theil-sen-regression]], [[frama]], [[vidya]], [[alma]], [[kama]], [[jurik-moving-average]] — each references its own member's status

## Contradictions

None recorded. No competing source of live figures for this family exists in the vault.

## Follow-up needed

- Reconcile reported fills against Hyperliquid venue records
- Obtain deploy dates and sizing policy per member
- Re-capture once members beyond `frama` have accumulated fills — that is the observation that would actually test the family's defence-in-depth claim
- Supply the sibling group dashboards ([[bar-break-group]], [[ride-group]], [[clock-group]], [[burst-and-pulse-group]], [[whale-traders-lab]]), which have no documentation in this vault

## Related

[[stretch-revert]] · [[live-journal]] · [[mean-reversion]] · [[z-score]] · [[median-absolute-deviation]] · [[deflated-sharpe-ratio]] · [[probability-of-backtest-overfitting]] · [[crypto-short-history-statistical-power]] · [[execution-model-differences]] · [[hyperliquid]] · [[sources-overview]]
