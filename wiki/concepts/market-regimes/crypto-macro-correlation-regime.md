---
title: "Crypto Macro Correlation Regime"
type: concept
created: 2026-06-03
updated: 2026-06-11
status: good
tags: [crypto, market-regime, correlation, market-microstructure, sp500, nasdaq]
aliases: ["Macro Correlation Regime", "Crypto-Equities Correlation", "Risk-On Risk-Off Crypto", "BTC-Nasdaq Beta"]
domain: [market-microstructure, portfolio-theory]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[correlation-regime]]", "[[dxy]]", "[[policy-shock-regime]]", "[[bitcoin-cycle-regime]]", "[[institutional-flow-regime]]", "[[hyperliquid]]"]
---

# Crypto Macro Correlation Regime

**Basket #6** of the [[crypto-market-regime-taxonomy|14-basket crypto regime taxonomy]]. This is the regime in which crypto stops trading on its own internal dynamics and instead **follows external forces** — equity indices (Nasdaq, S&P 500), [[dxy|dollar strength]], gold, and treasury yields — increasingly behaving as a **high-beta tech asset** rather than an uncorrelated alternative. The timescale is **days to weeks**: macro correlation windows open around prints and policy events and close again when crypto-native catalysts reassert. The tradeable consequence is that during this regime your edge is *macro*, not crypto — funding fades, on-chain flows, and dominance rotation all get overridden by the risk-on/risk-off tape, so positioning, leverage, and coin selection follow equities and the dollar instead.

This page is the **crypto-specific, cross-asset** version of the broader correlation concept. For the *general mechanism* — why correlations spike toward 1 in stress, how diversification evaporates exactly when it is needed, and the dispersion/correlation-trading toolkit — see [[correlation-regime]]. This page does **not** repeat that mechanism; it focuses on how crypto specifically couples to and decouples from the macro complex, and how to trade the perps book around it on a venue like [[hyperliquid|Hyperliquid]].

## Sub-Regimes

Each sub-state carries its own signal, directional bias, and an explicit *what-to-trade* line (coins / leverage / duration).

### Risk-Off (Equities Sell) — *bias: Short crypto*
- **Signal:** Nasdaq/S&P dropping, [[dxy|DXY]] rising, gold bid as a haven, treasury yields and VIX spiking — the classic risk-off cross-asset signature. When BTC's rolling correlation to equities is high, BTC *follows the selling* rather than offering shelter (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).
- **What to trade:** Reduce or short majors (`BTC-PERP`, `ETH-PERP`); cut alt beta hardest of all since alts fall faster than BTC in risk-off. **Lower leverage**, shorter duration, tighter stops. Do not deploy crypto-native long signals into a macro sell — they will be run over by the equity tape.

### Risk-On (Equities Rally) — *bias: Long crypto*
- **Signal:** Tech stocks ripping, [[dxy|DXY]] falling, realized and implied vol compressed, yields easing — broad appetite for duration and risk. In this state BTC tends to **lead** and alts follow with a lag (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).
- **What to trade:** Long majors first (`BTC-PERP`/`ETH-PERP`), then rotate into alts as the move broadens. Moderate-to-higher leverage acceptable while vol is low, days-to-weeks duration. The hand-off into the alt leg often overlaps with falling [[bitcoin-cycle-regime|BTC dominance]] (Basket #2).

### Dollar Strength (DXY Spike) — *bias: Short alts*
- **Signal:** A sustained [[dxy|DXY]] uptrend, with the framework flagging **DXY above ~105** as a level where dollar strength suppresses *all* risk assets — crypto included (heuristic, not a hard line) (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). A rising dollar tightens global liquidity and drains the marginal bid from the longest-duration, highest-beta assets, which is exactly what alts are.
- **What to trade:** Underweight or short alts; keep any longs concentrated in BTC (relative safety within crypto). Treat a DXY breakout as a *risk-asset suppressor* overlay on every other regime — see [[dxy|DXY]] for the dollar's role as the global liquidity gauge.

### Gold / Copper-Gold Ratio Shift — *bias: Risk sentiment gauge*
- **Signal:** The **copper/gold ratio rising = global risk-on** (industrial demand bid relative to the safe-haven metal); the ratio **falling = macro fear** (capital fleeing to gold). Gold rising *alone* alongside a falling copper/gold ratio confirms a defensive macro posture (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).
- **What to trade:** This sub-state is primarily a **confirming sentiment gauge**, not a standalone entry — use it to corroborate the Risk-On vs Risk-Off read before sizing the crypto book. A copper/gold roll-over alongside a DXY spike is a strong de-risk tell.

## BTC-Nasdaq Beta

Crypto's beta to tech equities is **itself regime-dependent** — it is not a fixed number. The beta runs **high during macro-driven windows** (Fed decisions, [[cpi|CPI]] prints, NFP, major rate-path repricings), when BTC and ETH effectively trade as a *leveraged Nasdaq* — same direction, amplified magnitude. It runs **low, or even decouples to near-zero**, during crypto-native phases when the dominant driver is internal: a [[bitcoin-cycle-regime|halving]] supply shock, an on-chain accumulation trend, an exchange exploit, or a listing/unlock event. The practical rule: ask *what is driving the tape right now?* During [[event-catalyst-regime|macro prints]] the correlation is the trade; during supply- or on-chain-driven phases the correlation is noise and crypto-native edges reassert. Trading a constant beta assumption — long crypto for "diversification" into an FOMC, or fading equities expecting crypto to decouple during a macro panic — is the central error this regime exists to prevent.

## Detection Signals

- **Rolling BTC–Nasdaq / BTC–S&P correlation** — the primary gate. A correlation spike means this regime is active and crypto-native signals should be down-weighted; a collapse toward zero means crypto has decoupled and Baskets #2/#7/#8 reassert.
- **[[dxy|DXY]] level and trend** — direction and the ~105 suppressor heuristic; a rising dollar is a headwind for the entire risk complex.
- **Gold price and copper/gold ratio** — the macro risk-on/risk-off sentiment gauge described above.
- **VIX** — equity-vol fear; spikes coincide with correlation-to-1 and de-risking.
- **Treasury yields / rate-path repricing** — the macro driver behind most high-beta windows.

Crucially, **this regime is defined by override**: when these macro signals dominate, crypto-native edges — [[funding-rate|funding]], [[open-interest|OI]], on-chain flows, dominance rotation — get suppressed. Detecting the macro regime is therefore as much about knowing *when to switch your crypto-native models off* as about taking a directional macro view.

## Relationship to Other Regimes

- **Overrides the crypto-native baskets** during macro windows. When BTC–Nasdaq correlation is high, the equity tape — not the [[bitcoin-cycle-regime|halving clock]], not funding, not on-chain flow — sets direction. This is the Risk-Off cross-over noted in [[bitcoin-cycle-regime|BTC Cycle]] (Basket #2).
- **Pairs with [[policy-shock-regime|Policy Shock]]** (Basket #12) — rate decisions, tariffs, and rate-path signals are the *discrete events* that ignite a macro-correlation window; this regime is the *persistent state* those shocks push the market into.
- **Pairs with [[institutional-flow-regime|Institutional Flow]]** (Basket #10) — TradFi capital (ETF allocators, 401(k) flows) is the **channel through which the equity beta is transmitted**: the more crypto is held by macro-allocating institutions, the tighter the equity coupling.
- **Decouples during [[bitcoin-cycle-regime|BTC Cycle]] supply-driven phases** — halving and on-chain accumulation phases are exactly when the correlation collapses and crypto trades on its own clock.

## Pitfalls

- **Assuming the BTC-equities correlation is constant.** It is regime-dependent (see BTC-Nasdaq Beta above). Diversification claims built on a low historical correlation evaporate precisely in the macro windows where the correlation spikes to 1 — the general failure mode documented in [[correlation-regime]].
- **Trading a crypto-native signal blind during a macro print.** Firing a funding-fade or a range-breakout into an FOMC or CPI window ignores that the dominant driver has switched to macro; the print, not the order book, moves the tape.
- **Ignoring [[dxy|DXY]] as a risk-asset suppressor.** A grinding dollar uptrend can bleed alts lower even when crypto-internal signals look constructive. Always read the dollar trend over the crypto book.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Crypto Data API 14-basket regime framework (VENTURE AI LABS); source for the Macro Correlation sub-states, the DXY ~105 suppressor heuristic, copper/gold sentiment gauge, and BTC-Nasdaq beta regime-dependence.

## Related

- [[crypto-market-regime-taxonomy]] — hub page for all 14 baskets
- [[correlation-regime]] — the general cross-asset correlation mechanism (equities-framed); this page is the crypto-specific version
- [[dxy]] — the dollar index as global liquidity / risk-suppressor gauge
- [[policy-shock-regime]] — Basket #12, the discrete shocks that ignite macro windows
- [[institutional-flow-regime]] — Basket #10, the channel transmitting equity beta
- [[bitcoin-cycle-regime]] — Basket #2, which this regime overrides in risk-off and decouples from in supply-driven phases
- [[hyperliquid]] — the perps venue the framework targets
