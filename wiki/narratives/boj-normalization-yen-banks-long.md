---
title: "BOJ Normalization → Yen-Carry Unwind Hedge & JP Banks Long"
type: narrative
created: 2026-05-10
updated: 2026-05-10
status: proposed
side: long
tickers_primary: [FXY, MUFG, SMFG]
tickers_secondary: [MFG]
tickers_hedge: [QQQ, SPY]
time_horizon_days: 120
catalysts:
  - "BOJ policy meetings (8/year — next ~mid-June 2026, then end-July 2026)"
  - "FOMC decisions — narrowing US-Japan rate differential is the highest-information unwind trigger"
  - "Japan Ministry of Finance verbal/physical FX intervention if USDJPY pushes past 155 on the way down"
  - "Quarterly BOJ Outlook Report"
  - "Japanese megabank earnings (Q1 fiscal 2026 — early August; Q2 — early November)"
sources:
  - "[[bank-of-japan]]"
  - "[[2024-08-yen-carry-unwind]]"
  - "[[usdjpy]]"
  - "[[carry-trade]]"
  - "[[vix-august-2024-spike]]"
  - "[[yen-carry-triangular-arbitrage]]"
invalidation:
  - "BOJ explicitly walks back further normalization (Uchida-style 2024-08-07 reversal) and signals no hikes for 12 months"
  - "USDJPY ranges below 140 for 30+ sessions before entry — unwind already priced in"
  - "Fed restarts hiking cycle — US-Japan rate differential widens, carry trade re-establishes"
  - "Japanese megabanks rally >25% in 30 days before entry — chasing a crowded run"
  - "Japanese banking-system stress (regional bank failure / unrealized JGB losses crystallize) breaks the long-bank leg"
risk_reward_target: "3:1"
summary: "Japan's central bank is finally raising rates after 25 years near zero. That makes the yen stronger and forces global investors to unwind trillions of yen-funded bets in US tech, Mexican bonds, and crypto — exactly what crashed markets in August 2024. We're long the yen (FXY) and Japanese banks (MUFG, SMFG) which earn more as rates rise, with QQQ puts as a kicker if the unwind cascades."
created_by: "slash-command"
---

# BOJ Normalization → Yen-Carry Unwind Hedge & JP Banks Long

## Headline

Per [[bank-of-japan]], the BOJ ended NIRP and YCC in March 2024 and is now in
its first meaningful tightening cycle in a generation. Per
[[2024-08-yen-carry-unwind]], a single 25 bp BOJ hike on July 31, 2024 —
paired with a dovish Fed pivot the same day — unwound an estimated **$1-3
trillion** in yen-funded carry positioning, drove the **Nikkei -12.4% in one
session** (worst since 1987), and spiked **VIX from 16 to 65 in 48 hours**.
The carry trade has structurally rebuilt at smaller scale since, but BOJ
normalization continues. **Own the assets that benefit from BOJ tightening
(long yen, long JP megabank NIM expansion) and add a low-cost QQQ put
kicker that cashes in if the next unwind cascades like August 2024.**

This is the basket's missing **global macro hedge**. Every other active
narrative is risk-on or sector-specific. None pays off cleanly when
JPY-funded leverage gets force-liquidated through global risk assets.

## Thesis

Three structural inputs make this trade work over the 120-day window:

1. **BOJ is mid-cycle.** The policy rate is at 0.5% versus a ~1.0% terminal
   estimate, and each subsequent hike narrows the US-Japan rate differential
   — the single highest-information variable for USDJPY per [[usdjpy]]. The
   10Y UST-JGB spread blew to ~400 bp at peak in 2024; every basis point of
   compression pulls USDJPY toward 140 and adds force to the carry-unwind
   feedback loop.
2. **JP banks are direct beneficiaries.** Japanese megabanks have been
   suffocated for three decades by zero rates compressing net interest
   margins. As JGB yields rise, NIM expands mechanically — and MUFG, SMFG,
   MFG hold massive JGB books that re-rate to higher coupon as the curve
   normalizes. This is the cleanest "long BOJ tightening" trade in equity
   form. The ADRs trade in NY hours and are options-eligible.
3. **The carry trade is structurally crash-prone.** Per [[carry-trade]] and
   [[2024-08-yen-carry-unwind]], 25 years of BOJ ZIRP/NIRP made JPY *the*
   funding currency for global leverage. Position concentration + reflexive
   forced-unwind dynamics + vol-targeting accelerants = a payoff structure
   where the third moment is systematically negative. The QQQ put hedge is
   cheap because most of the time it expires worthless; it pays
   catastrophically when carry positioning unwinds through US tech (the
   largest non-Japan home for JPY-funded leverage).

The basket is **internally consistent**: if BOJ stays dovish and the yen
weakens, the QQQ puts decay but JP bank longs should still grind higher on
slow normalization; if BOJ surprises hawkish or US data forces
rate-differential compression, the yen + JP banks + QQQ puts all fire
together.

## Why now

- **120-day window covers two BOJ meetings** (mid-June 2026, end-July 2026)
  plus one quarterly Outlook Report. Discrete, dated catalysts.
- **August 2026 is the one-year anniversary** of the 2024-08-05 unwind.
  Per [[usdjpy]], the Sunday-Monday session boundary is when carry unwinds
  tend to ignite — late-summer Tokyo holiday liquidity is thinnest exactly
  when positioning awareness peaks.
- **USDJPY skew is structurally cheap.** Per [[usdjpy]], 1M risk reversals
  run -0.5 to -1.5 vol points (yen-call premium) in calm regimes — meaning
  yen-call protection is comparatively under-priced versus the realized
  tail. The same logic applies to FXY upside calls.
- **JP bank ADR implied vol has compressed** as the cycle has normalized.
  Entry vol is favorable for long calls 90-180 DTE.
- **No active narrative covers this leg.**
  [[stagflation-tail-hedge-long-vol-overlay]] is a generic SPY put / VIX
  call program; it does not capture the specific JPY transmission channel.

## Expression

- **Primary** (~70% of strategy capital):
  - **FXY** (Invesco CurrencyShares Japanese Yen Trust) — long calls
    60-120 DTE, OR long FXY shares with covered-call collar. Per
    [[usdjpy]], this is the equity-options-friendly yen vehicle. Cleanest
    pure-play on yen strength.
  - **MUFG** (Mitsubishi UFJ) — long calls or call verticals 90-180 DTE.
    Largest Japanese bank by assets; deepest options liquidity of the
    megabank ADRs.
  - **SMFG** (Sumitomo Mitsui) — long calls or call verticals 90-180 DTE.
    Diversifies single-name MUFG concentration; near-identical driver.
- **Secondary** (~10% of strategy capital):
  - **MFG** (Mizuho) — smaller third leg of the megabank basket; lower
    options liquidity, sized accordingly.
- **Hedge / asymmetric kicker** (~20% of strategy capital):
  - **QQQ puts** — 60-90 DTE, 5-10% OTM. Per [[2024-08-yen-carry-unwind]],
    the cleanest transmission of JPY carry unwind into US markets is via
    long-duration tech (NVDA / AMZN / MSFT were sold to raise JPY in
    August 2024). QQQ is the most efficient single-instrument expression
    of that exposure.
  - **SPY puts** as alternative if QQQ vol is rich.

The bot's Stage 5 (structure) and Stage 6 (sizing) will confirm specific
strikes against R:R ≥ 3:1. Note the FXY leg may not pass a strict 3:1
directional R:R cleanly because FX moves are smaller in % terms than
equities — the bot may auto-prefer call verticals or smaller naked-call
positions on FXY to compensate.

## Risks

- **Dovish BOJ reversal.** The August 7, 2024 Uchida walk-back is the
  canonical pattern: BOJ explicitly says "no hikes while markets unstable,"
  yen weakens immediately, JP bank rally stalls. Watch BOJ communication
  after any USDJPY move >2%.
- **Fed re-tightens.** A surprise hawkish Fed (US inflation re-acceleration,
  tariff pass-through) widens the rate differential, re-establishes carry,
  and hurts the entire basket. This is in tension with
  [[tariff-persistence-domestic-manufacturers-long]] — a sticky-inflation
  regime would be bullish that narrative and bearish this one.
- **Japan banking-system stress.** JP banks hold massive JGB inventories. A
  *too-fast* yield rise crystallizes unrealized losses (SVB-style).
  MUFG/SMFG/MFG all have manageable HTM marks but a sharp curve steepening
  could pressure the long bank thesis even as the long yen leg pays. Watch
  JGB 30Y yield specifically.
- **Already crowded yen long.** Specs were heavily long yen by April 2026.
  Carry unwinds work best from positioning extremes, not into them.
  IV-rank check before sizing; if FXY 30-day IV is in the top quartile,
  defer entry.
- **Time decay on QQQ puts.** The hedge bleeds in a calm regime; size
  accordingly. The narrative explicitly accepts this as the cost of
  carrying the kicker.
- **Liquidity gap on the unwind itself.** Per [[usdjpy]], FX markets gap on
  the Sunday-Monday boundary in stress. The QQQ put leg should be sized
  assuming you cannot rebalance during the 12 hours when an unwind
  ignites — which is exactly when the hedge is most valuable.
- **MoF intervention.** Japan's Ministry of Finance has historically
  intervened to *weaken* a too-strong yen (rare, but possible). Material
  risk only if USDJPY breaks below 130.

## Signals generated

[Auto-populated by the bot. Append-only.]

## See also

- [[bank-of-japan]] — primary regulator entity (good status)
- [[2024-08-yen-carry-unwind]] — the canonical recent precedent
- [[usdjpy]] — the primary FX transmission channel
- [[carry-trade]] — strategy framework
- [[yen-carry-triangular-arbitrage]] — sibling arbitrage expression
- [[vix-august-2024-spike]] — equity-vol companion event
- [[stagflation-tail-hedge-long-vol-overlay]] — sibling generic-tail-hedge narrative; this narrative is the JPY-specific complement
- [[long-call-vertical]] — primary expression structure
- [[fxy-etf]] — retail-equity yen vehicle
