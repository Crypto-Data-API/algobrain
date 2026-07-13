---
title: "Macro Trend Regime"
type: concept
created: 2026-06-03
updated: 2026-06-11
status: good
tags: [crypto, market-regime, trend-following, market-microstructure, quantitative]
aliases: ["Macro Trend", "Crypto Macro Regime", "Bull/Bear Regime"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[bitcoin-cycle-regime]]", "[[derivatives-native-regime]]", "[[volatility-regime-classification]]", "[[bull-vs-bear-market]]", "[[regime-matrix]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid]]"]
---

The **Macro Trend regime** is the broadest and longest-duration regime in the [[crypto-market-regime-taxonomy]] — a structural backdrop that typically persists 1–6 months and sets the directional bias every faster regime trades inside. It is read from three structural inputs: market structure (higher-highs/higher-lows vs lower-highs/lower-lows), aggregate [[funding-rate|funding]] sign and level, and the trend in BTC dominance (BTC.D) flow. In effect it generalises the classic [[bull-vs-bear-market]] distinction into a crypto-native, funding-aware, perps-traded context — anchored on [[hyperliquid]] perpetuals where funding and [[open-interest|OI]] are transparent and continuously readable (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).

Macro Trend is basket #1 of fourteen. It is deliberately slow: it does not tell you when to enter on a 4-hour chart, it tells you which side the wind is at your back. Overlay regimes (volatility, technical signal quality) and fragility detectors (derivatives stress, on-chain flow) all operate *within* whichever macro state is active.

## Sub-Regimes

The framework decomposes the macro backdrop into six structural states. Each carries a directional bias and a distinct posture for coin selection, leverage, holding duration, and how much funding cost you can tolerate (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).

### Full Bull Run (Long)
- **Signal:** Clean HH/HL structure across BTC and majors; aggregate funding positive and rising; BTC dominance drifting *down* as risk appetite broadens.
- **Directional bias:** Long.
- **What to trade:** Long majors and high-quality alts. Leverage can be moderate (longs are paying funding, but trend pays more); hold for weeks, trail stops behind structure rather than taking quick profits. Tolerate elevated positive funding as the cost of staying in the trend. Scale out into euphoric blow-off extensions rather than guessing the top.

### Altcoin Season (Long alts)
- **Signal:** BTC.D breaking down below the ~55–60% zone the framework flags as a rotation threshold, with capital visibly leaving BTC into ETH/SOL and the long tail.
- **Directional bias:** Long alts, flat-to-underweight BTC.
- **What to trade:** Concentrate in ETH/SOL and rotating alt leaders; keep BTC exposure light. Holding periods shorten versus a Full Bull Run because alt moves are faster and reverse harder — size for higher volatility and accept higher funding cost on the hottest alt perps. See [[bitcoin-cycle-regime]] for where in the broader cycle alt-season tends to land.

### Full Bear Market (Short)
- **Signal:** LH/LL structure; aggregate funding negative or flipping negative; BTC.D *rising* as capital flees alts into BTC and stables.
- **Directional bias:** Short.
- **What to trade:** Short alts preferentially (they bleed fastest and basis is more punishing for longs); fade dead-cat bounces into prior support-turned-resistance. Run smaller size than in a bull trend — bear rallies are violent — and shorter holds. When funding is deeply negative, shorts pay to hold, so favour quick covers over riding the full leg.

### Accumulation / Range (Neutral)
- **Signal:** Compressed realised volatility, flat/low-trend [[open-interest|OI]], stable funding hovering near neutral, price carving a horizontal base.
- **Directional bias:** Neutral / two-sided.
- **What to trade:** Mean reversion and range fades — sell the range top, buy the range bottom, with tight TP/SL. Minimal leverage; funding cost is low so carry is cheap, but there is no trend to pay you, so keep holds short and book profits at the opposite band.

### Sideways / Chop (Both)
- **Signal:** Low ATR, mixed/whipsawing funding, no coherent structural bias — neither HH/HL nor LH/LL holds for long.
- **Directional bias:** Both / none.
- **What to trade:** This is a *reduce-size* regime. Trade a tighter range than in clean Accumulation, and explicitly **avoid breakout plays** — most "breakouts" in chop are liquidity sweeps that revert. Prefer fast scalps over positional trades; the edge is patience, not conviction.

### Distribution Phase (Short setup)
- **Signal:** OI rising while price stalls or makes lower highs; funding bleeding persistently positive (crowd still long into a stalling tape) — classic late-cycle topping behaviour.
- **Directional bias:** Short setup forming (not yet confirmed short).
- **What to trade:** Prepare shorts but wait for structure to crack; meanwhile trail any remaining longs aggressively and harvest into strength. Positive funding into a flat price is the tell that longs are overcrowded and paying to stay wrong — a precursor the framework treats as a handoff toward Full Bear.

## Detection Signals

Read these together; no single one is decisive (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]):

- **Market structure** — sequence of HH/HL (bullish), LH/LL (bearish), or neither (range/chop) on the macro timeframe.
- **Aggregate funding** — sign and magnitude across major perps: positive/rising confirms long crowding and bull conviction; negative confirms bearish positioning; near-zero/whipsaw confirms indecision.
- **BTC dominance trend** — falling BTC.D supports alt risk-on; rising BTC.D supports flight-to-BTC / bear or early-cycle phases.
- **ATR / volatility** — compression flags Accumulation or Chop; expansion accompanies trending Bull/Bear legs.
- **OI trend** — rising OI with price trend confirms participation; rising OI with stalling price flags Distribution.

[[hyperliquid|Hyperliquid]]'s on-chain transparency makes the funding and OI reads unusually clean — perp funding and aggregate OI are observable directly rather than inferred from opaque exchange feeds, which sharpens the structural read this regime depends on.

## Relationship to Other Regimes

Macro Trend is the **backdrop**, not a trade signal. Everything else in the taxonomy is conditioned on which macro state is live:

- **Overlay regimes** — [[volatility-regime-classification]] and technical-signal regimes tune *how* you express the macro bias (size, stop width, entry style) but do not override it.
- **Fragility detectors** — the [[derivatives-native-regime]] (funding extremes, OI unwinds, liquidation cascades) and on-chain flow regimes detect stress *inside* a macro state and often **lead** macro transitions: a derivatives-native blow-up or an on-chain distribution lead frequently flags the Bull→Distribution→Bear handoff before price structure confirms it.
- See the [[regime-matrix]] for how macro bias composes with the faster regimes into a single posture.

## Pitfalls

- **Mistaking chop for trend** — forcing trend trades in a Sideways/Chop regime; the breakouts are fake and the whipsaw funding is the warning you ignored.
- **Ignoring funding/OI confirmation** — calling a bull or bear from price alone. Price can trend while funding/OI quietly diverge (Distribution); the structural read needs all three legs.
- **Calling alt-season too early** — going heavy alts before BTC.D actually breaks down. Premature alt rotation in a still-BTC-dominated tape bleeds funding and underperforms simple BTC longs.
- **Over-sizing in Distribution** — treating a stalling top as a continuation and adding leverage while OI/funding scream crowding. This is where leveraged longs get liquidated into the first real leg down.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket regime framework defining the Macro Trend states, signals, and biases.
- [[bull-vs-bear-market]] — the classical trend-direction distinction this regime generalises to a funding-aware, perps context.

## Related

- [[crypto-market-regime-taxonomy]]
- [[bitcoin-cycle-regime]]
- [[derivatives-native-regime]]
- [[volatility-regime-classification]]
- [[bull-vs-bear-market]]
- [[regime-matrix]]
- [[funding-rate]]
- [[open-interest]]
- [[hyperliquid]]
