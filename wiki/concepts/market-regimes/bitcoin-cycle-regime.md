---
title: "BTC Cycle Regime"
type: concept
created: 2026-06-03
updated: 2026-07-13
status: good
tags: [crypto, bitcoin, market-regime, market-microstructure, quantitative]
aliases: ["BTC Cycle", "Bitcoin Cycle Regime", "Halving Cycle Regime", "BTC Dominance Regime"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[macro-trend-regime]]", "[[on-chain-regime]]", "[[institutional-flow-regime]]", "[[bitcoin-halving]]", "[[btc-dominance]]", "[[bull-vs-bear-market]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
---

# BTC Cycle Regime

**Basket #2** of the [[crypto-market-regime-taxonomy|14-basket crypto regime taxonomy]]. Bitcoin runs its own **weeks-to-months cycle** that does not always track the broad crypto tape — driven by [[bitcoin-halving|halving]] supply shocks, miner sell-flows, and capital rotation measured by [[btc-dominance|BTC dominance]]. The point of treating it as a separate regime is that BTC can lead price discovery while alts stall, or sell off on a macro shock while the rest of the market is still bid — so the **tradeable expression is in BTC itself**, often as a relative-value posture (long BTC / underweight alts) rather than a broad-market call. On a venue like [[hyperliquid|Hyperliquid]] this is expressed as a directional perps position in `BTC-PERP` plus a deliberate weighting choice against the alt book, sized to the cycle's holding duration rather than to intraday noise.

This basket sits **alongside the [[macro-trend-regime|Macro Trend]] backdrop** (Basket #1): Macro Trend sets the broad bull/bear bias everything trades inside, while BTC Cycle captures the partly-independent rhythm of Bitcoin's supply and rotation dynamics. Forward-links: [[bitcoin-halving]] and [[btc-dominance]] (may be stubs — linking is intentional to flag the gap).

## Sub-Regimes

Each sub-state carries its own signal, directional bias, and an explicit *what-to-trade* line (coins / leverage / duration / funding tolerance).

### BTC Solo Bull Run — *bias: Long BTC*
- **Signal:** [[btc-dominance|BTC.D]] rising while alts are flat or bleeding; BTC making higher highs and leading price discovery with majors lagging. The framework notes that **1–2 week persistent BTC-led runs historically precede an alt rotation** (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]).
- **What to trade:** Long `BTC-PERP`; flat or underweight alts (do not chase laggards into a dominance uptrend). Moderate leverage (~2–3x), duration days-to-weeks, **tolerate mildly positive funding** since the trend pays for the carry — but treat funding spiking to extremes as a hand-off to [[derivatives-native-regime|derivatives-native]] fragility.

### Pre-Halving Ramp — *bias: Long BTC*
- **Signal:** Halving calendar proximity inside the historical **~60–90 day pre-halving accumulation window**, with dominance firm and on-chain accumulation building (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). See [[bitcoin-halving]] for the supply-issuance mechanics.
- **What to trade:** Accumulate `BTC-PERP` (or spot) with **moderate leverage**; longer duration (weeks). Funding tolerance moderate — the position is a slow accumulation, not a momentum chase, so avoid paying rich funding for early entry.

### Post-Halving Lag — *bias: Neutral → Long*
- **Signal:** Halving has passed; miner sell-pressure subsides and the **supply shock builds slowly over the following ~6–12 months** rather than firing on the halving date itself (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). Hash-ribbon recovery and falling exchange inflows ([[on-chain-regime]]) confirm.
- **What to trade:** Patient long bias on `BTC-PERP`/spot; **low leverage**, long duration (months). Accept neutral chop early — the edge is positioning ahead of a delayed supply-demand imbalance, not catching an immediate move. Low funding tolerance; carry over months erodes a leveraged hold.

### BTC Risk-Off Sell — *bias: Short BTC*
- **Signal:** BTC correlating tightly with Nasdaq/equities **selling**, macro fear spikes (DXY up, VIX up), risk-off bid in bonds. This is the cross-over with [[crypto-macro-correlation-regime|Macro Correlation]] (Basket #6) — when correlation is high, the BTC cycle is overridden by the equity tape.
- **What to trade:** Reduce or short `BTC-PERP`; cut alt beta hard (alts fall faster than BTC in risk-off). Shorter duration, tighter stops; **negative funding can be a tell** of crowded shorts and reversal risk, so size for squeezes.

## Detection Signals

- **[[btc-dominance|BTC dominance]] trend** — the primary rotation gauge: rising/high = capital hiding in BTC; falling = rotation into alts.
- **[[bitcoin-halving|Halving calendar]] proximity** — distance to/from the last halving selects between Pre-Halving Ramp and Post-Halving Lag.
- **Miner flows / hash ribbon** — miner sell-pressure and hash-rate recovery, read via [[on-chain-regime|on-chain intelligence]] (Basket #7), which leads price.
- **BTC–Nasdaq correlation** — rolling correlation to equities; a spike flips the regime toward [[crypto-macro-correlation-regime|Macro Correlation]] and the Risk-Off sub-state.

## Dominance Rotation

[[btc-dominance|BTC.D]] — Bitcoin's share of total crypto market cap — is the **rotation gauge** that ties the sub-regimes together. **High or rising BTC.D** means capital is concentrating in (or hiding in) Bitcoin; in those windows alts tend to bleed against BTC even when total market cap is flat, which is why the Solo Bull Run sub-state pairs *long BTC* with *underweight alts*. **Falling BTC.D**, particularly a break **below the ~55–60% zone**, is the classic **alt-season trigger** — capital rotating down the risk curve into majors-alts then lowcaps (link [[macro-trend-regime|Altcoin Season]]). The threshold is a framework heuristic, not a hard line (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]); the *direction and persistence* of the dominance trend matter more than the exact level.

## Relationship to Other Regimes

- **Feeds the [[macro-trend-regime|Macro Trend]] backdrop** — a strong BTC cycle is usually what *initiates* a macro bull leg; the broad regime then carries it.
- **[[institutional-flow-regime|ETF / institutional flows]]** increasingly drive the BTC cycle — sustained ETF inflows set multi-month structural floors and have blunted the sharpness of the old halving-timed tops/bottoms.
- **[[on-chain-regime|On-chain]] miner signals lead it** — hash ribbons, miner reserve drawdowns, and exchange inflows turn before price does, making Basket #7 the early-warning layer for this one.
- **[[crypto-macro-correlation-regime|Macro Correlation]]** can temporarily *override* the cycle — when BTC trades as high-beta tech, the equity tape, not the halving clock, sets direction.

## Pitfalls

- **Treating halving dates as mechanical price triggers.** The supply shock is gradual (Post-Halving Lag) — price does not jump on the date. Positioning *for the date* is a classic over-fit.
- **Ignoring that [[institutional-flow-regime|ETF flows]] have altered the classic 4-year cycle.** Post-spot-ETF, demand-side flows can dominate the supply-side halving narrative; the old cycle template is a prior, not a law.
- **Conflating BTC.D moves with absolute price direction.** Dominance can rise while BTC falls (alts falling faster) or fall while BTC rises (alts ripping harder). BTC.D is a *relative* gauge — always read it next to absolute price and total market cap.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Crypto Data API 14-basket regime framework (VENTURE AI LABS); source for the BTC Cycle sub-states, pre/post-halving windows, and dominance thresholds.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (top coins)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain
- `GET /api/v1/market-intelligence/etf/btc/aum` — BTC ETF total AUM
- `GET /api/v1/market-intelligence/exchange-balance` — exchange BTC balance + flow
- `GET /api/v1/market-intelligence/taker-buy-sell` — taker buy/sell ratio by exchange (4h window)

**Historical data:**
- `GET /api/v1/market-intelligence/etf/{asset}/flows` — BTC/ETH/SOL/XRP ETF flow history
- `GET /api/v1/market-intelligence/coinbase-premium` — Coinbase premium index history
- `GET /api/v1/market-intelligence/btc/cycle-indicators` — all 8 BTC cycle indicators, historical
- `GET /api/v1/backtesting/liquidations` — liquidation records archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]]. Also see [[cryptodataapi-regimes]].

## Related

- [[crypto-market-regime-taxonomy]] — hub page for all 14 baskets
- [[macro-trend-regime]] — Basket #1, the backdrop this cycle initiates
- [[crypto-macro-correlation-regime]] — Basket #6, overrides the cycle in risk-off
- [[on-chain-regime]] — Basket #7, leading miner/flow signals
- [[institutional-flow-regime]] — Basket #10, ETF flows reshaping the cycle
- [[bitcoin-halving]] · [[btc-dominance]] · [[bull-vs-bear-market]] · [[hyperliquid]]
