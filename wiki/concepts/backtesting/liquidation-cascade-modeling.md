---
title: "Liquidation Cascade Modeling"
type: concept
created: 2026-05-05
updated: 2026-07-13
status: excellent
tags: [backtesting, risk-management, crypto, derivatives, leverage, liquidity]
aliases: ["Cascade Modeling", "Liquidation Cascade Backtest", "Cascade Stress Test"]
related: ["[[auto-deleveraging]]", "[[liquidation-cascade-arbitrage]]", "[[liquidation-risk]]", "[[funding-rate]]", "[[slippage-modeling]]", "[[market-impact-models]]", "[[monte-carlo-permutation-test]]", "[[2025-10-crypto-liquidation-cascade]]", "[[coinglass]]", "[[kaiko]]", "[[crypto-perp-backtesting-pitfalls]]", "[[backtesting-pitfalls]]", "[[intrabar-fill-modeling]]", "[[backtesting]]", "[[cryptodataapi]]"]
domain: [backtesting, risk-management, market-microstructure]
prerequisites: ["[[liquidation-risk]]", "[[auto-deleveraging]]", "[[slippage-modeling]]"]
difficulty: advanced
---

Liquidation cascade modeling is the practice of representing forced-liquidation events as **systemic, self-reinforcing processes** in a backtest, rather than as independent margin calls. Cascades accelerate price moves far beyond the trigger that started them: a -3% drop can mechanically compound into a -15% rout as each liquidated position dumps inventory into thinning liquidity, triggering the next tier of stops. This is the *modeling* page — the trading strategy that *exploits* cascades is documented at [[liquidation-cascade-arbitrage]]; the broader pitfall context is at [[crypto-perp-backtesting-pitfalls]].

## What Cascades Look Like in Data

Empirically, a true cascade has a recognizable signature:

- **Non-linear price acceleration.** A 5-minute candle that prints -8% on 5x average volume, followed by a second candle with similar magnitude, with no discrete news catalyst.
- **Clustered liquidation prints.** Per-second liquidation totals jump 10–100× baseline. CoinGlass and exchange feeds typically show $50M+ liquidations per minute sustained over 15–60 minutes.
- **Cross-venue synchronization.** Cascades on [[binance]], [[bybit]], [[hyperliquid]], OKX fire within seconds of each other because mark prices reference a common index.
- **Funding-rate inversion.** Funding spikes from baseline (say +0.01% per 8h) to extreme prints (±0.5% to ±2% per 8h) reflecting the post-cascade OI imbalance.
- **Order-book hollowing.** Top-10-level depth on the dominant venue drops 50–90% in the 30 seconds before the worst prints.
- **[[auto-deleveraging|ADL]] activation** on at least one major venue, indicated by insurance-fund drawdown or published ADL events.

Reference events that produced clean signatures:

| Event | Approx. liquidations | Defining feature | Why it matters for modeling |
|---|---|---|---|
| [[2025-10-crypto-liquidation-cascade\|October 10–11, 2025]] | ~$20B | Widespread [[auto-deleveraging\|ADL]] across CEXs | Broke nominally delta-neutral basis/funding-arb trades |
| May 19, 2021 | ~$8.6B | BTC −30% intraday | Killed naive funding-arb; classic over-leverage flush |
| May 7–12, 2022 (LUNA/UST) | ~$10B+ | Multi-day cross-protocol + stablecoin depeg | Collateral assumed-at-par failure |
| December 4, 2021 | ~$2.5B | Pre-dawn BTC flash crash, ~30 min | Thin-liquidity hours; depth-hollowing in minutes |

Cascade magnitudes are widely cited from aggregators such as [[coinglass]]; treat them as approximate and revised-after-the-fact (see *Using post-event revised data* below).

## Why Simple Monte Carlo Misses Cascades

Standard backtest stress tests run one of two flawed simulations:

1. **Independent shock sampling.** Draw price changes from a fitted distribution (Gaussian, Student-t, GARCH residuals). Cascades violate independence by construction — liquidations *cause* the next liquidations. Resampling preserves marginal moments but destroys the conditional dependence that *is* the tail event.
2. **Constant-slippage assumption.** Cost models that apply a fixed bps haircut per fill ignore the order-book hollowing that defines a cascade. Real fills during October 2025 saw 2–10% effective slippage on $1M+ market orders versus a backtest assumption of 5–20 bps.

A cascade has three properties Monte Carlo without explicit cascade structure cannot reproduce:

- **Self-excitation** (Hawkes-process-like clustering of liquidation arrivals)
- **Liquidity feedback** (depth shrinks as prints get larger)
- **Cross-venue contagion** (correlated mark-price moves trigger liquidations elsewhere)

Tail risk is therefore systematically understated. Strategies that look "robust" in a 10,000-run Monte Carlo can blow up on a single live cascade because the simulator never produced one.

## Cascade Triggers

The most productive triggers to model explicitly:

- **Funding-rate spikes.** Funding > 99th-percentile (long-side or short-side) means OI is heavily skewed; a price move against the crowded side cascades.
- **Oracle deviations and stale marks.** Mark-price formulas using TWAP can lag spot during fast moves, force-liquidating positions at prints that no longer reflect reality. Several Hyperliquid and dYdX events traced to this.
- **[[auto-deleveraging|ADL]] feedback loops.** Once insurance funds deplete, ADL force-closes profitable opposing positions, removing the liquidity that would otherwise have cushioned the cascade. This is reflexive — ADL itself accelerates the move that triggered ADL.
- **Concentrated whale positions.** A single account with $500M+ notional at a known liquidation price is a deterministic cascade trigger when price approaches.
- **Cross-collateral chains.** A drop in BTC liquidates ETH/SOL positions collateralized in BTC, which dumps spot, which triggers more BTC liquidations.
- **Stablecoin depegs.** If margin collateral (USDT/USDC/DAI) trades below $1, every leveraged position becomes simultaneously undercollateralized.

## Modeling Approaches

There is no single best method; the right choice depends on the strategy being tested.

### 1. Agent-Based Models

Simulate a population of leveraged accounts with distributed entry prices and leverages, plus a market-maker stack with finite depth. Each step:

- Update mark price by exogenous drift + endogenous market-impact from forced flow.
- Identify accounts whose health factor < 1; queue them for liquidation.
- Liquidator orders walk the book; depth is reduced by filled volume.
- Surviving market makers replenish on a delay and at wider quotes.
- Repeat until equilibrium or full collapse.

Strengths: realistic feedback, captures non-linearity. Costs: calibration-heavy; sensitive to assumed leverage distribution.

### 2. Copula-Based Models

Fit a copula (typically t-copula or vine copula) to the joint distribution of (price return, liquidation volume, funding-rate change, depth shrinkage). Sample from the copula to produce dependent shocks. This preserves the tail dependence that Gaussian models destroy.

Strengths: tractable; better than independent sampling. Costs: still does not reproduce time-clustering — sampled events are i.i.d. across time even if cross-sectionally dependent.

### 3. Historical-Event Replay (Recommended Baseline)

Take real cascade events tick-by-tick (October 2025, May 2021, May 2022, December 2021) and replay them as deterministic stress overlays on top of the strategy. The strategy is exposed to the actual order book, actual liquidation flow, and actual ADL activity that occurred.

Strengths: no calibration; uses ground truth. Costs: limited sample size; assumes future cascades resemble past ones (they often do — the mechanic is structural, not statistical).

### 4. Hawkes / Self-Exciting Point Processes

Model liquidation arrivals as a Hawkes process where each event raises the intensity of the next. Calibrate decay and excitation parameters from CoinGlass historical data. Combine with a market-impact model to translate arrivals into price moves.

Strengths: directly captures clustering. Costs: more sophisticated; estimation requires care.

In practice, a defensible perp backtest layers all three: copula for routine tail draws, historical replay for known cascade days, and a Hawkes overlay for synthetic stress. See also [[monte-carlo-permutation-test]] for orthogonal robustness checks.

### Approach comparison

| Approach | Captures self-excitation? | Captures liquidity feedback? | Captures cross-venue contagion? | Calibration burden | Best role |
|---|---|---|---|---|---|
| Agent-based | Yes (emergent) | Yes | If multi-venue agents modelled | High | Mechanism research, scenario generation |
| Copula | No (i.i.d. across time) | Partial (via depth variable) | Yes (cross-sectional) | Medium | Routine tail draws |
| Historical replay | Yes (ground truth) | Yes (actual book) | Yes (actual flow) | None (uses real data) | **Recommended baseline** / acceptance test |
| Hawkes point process | Yes (by construction) | Only with impact overlay | Only if multivariate | Medium–high | Synthetic non-historical stress |

The reason no single method suffices: each reproduces a *subset* of the three properties that make a cascade non-Gaussian (self-excitation, liquidity feedback, cross-venue contagion). Layering them is how you cover all three without over-trusting any one calibration.

## Worked Example: Why a Hedged Trade Still Blows Up

> Illustrative scenario; the numbers are chosen to show the mechanism, not measured from a specific fund.

Consider a "delta-neutral" basis trade: long spot BTC, short the perpetual, harvesting positive funding. On paper it has near-zero directional exposure and a tiny modelled max drawdown.

- **Naive Monte Carlo (independent Gaussian/Student-t shocks):** the two legs offset, funding accrues steadily, simulated worst-case drawdown ≈ 2–3%. The strategy looks "robust" across 10,000 runs.
- **What a cascade does instead:** a −12% wick triggers mass liquidations. The exchange's insurance fund depletes and [[auto-deleveraging\|ADL]] force-closes the *profitable short leg* — precisely the hedge. The position is now unhedged and long into a falling market. Simultaneously, depth on the dominant venue has hollowed 50–90%, so the attempt to re-hedge fills 2–10% through the book instead of the modelled 5–20 bps. Funding inverts violently against the surviving leg.
- **Result:** the "2–3% max drawdown" strategy realises a double-digit loss in minutes — not because the model was unlucky, but because the simulator *could never produce a cascade*. The tail it was stress-tested against did not contain the tail that kills it.

This is the central lesson: tail risk for leveraged perp strategies is *structural and conditional*, not a fat marginal. A backtest that resamples marginal moments ([[backtesting-pitfalls|a classic pitfall]]) is blind to it. The fix is to expose the strategy to dependence-aware overlays and, above all, to **historical replay of the events listed above**.

## Required Data

| Data | Source | Use |
|------|--------|-----|
| Per-venue liquidation history (timestamp, side, size) | [[coinglass]] | Calibrate trigger probabilities and clustering parameters |
| Tick-level order book depth | [[kaiko]] (institutional), Tardis (crypto-native) | Depth-shrinkage curves; market-impact estimation |
| Funding rate term structure | Exchange APIs, Coinglass | Stress signal; cascade trigger leading indicator |
| Insurance-fund balances | Exchange disclosures (Binance, Bybit, OKX) | ADL trigger probability |
| Mark-price vs. index-price spreads | Exchange APIs | Oracle-deviation cascade triggers |
| Open-interest concentration | CoinGlass, Laevitas | Crowding signal |
| Spot-perp basis | Multi-venue feeds | Cross-instrument contagion paths |

Glassnode point-in-time on-chain metrics also help for reconstructing pre-cascade exchange flows without lookahead bias.

## Stress-Testing Checklist for Backtests

Before declaring a perp strategy production-ready, replay it against (at minimum):

- [ ] **October 10–11, 2025** — $20B cascade with widespread [[auto-deleveraging|ADL]] activation across CEXs.
- [ ] **May 19, 2021** — BTC -30% intraday, ~$8.6B liquidations; broke many naive funding-arb strategies.
- [ ] **May 7–12, 2022 (LUNA/UST)** — Multi-day cross-protocol cascade; ~$10B+ DeFi + CEX liquidations; stablecoin depeg.
- [ ] **December 4, 2021** — Pre-dawn BTC flash crash, ~$2.5B liquidations in 30 minutes.
- [ ] **March 12, 2020 (Black Thursday)** — DeFi-specific; tested oracle and gas-price assumptions, see [[liquidation-cascade-arbitrage]].
- [ ] **November 2022 (FTX collapse)** — Counterparty risk + sustained liquidation flow; tests venue diversification.
- [ ] **At least one synthetic Hawkes-driven cascade** scaled to 1.5× the worst historical print, to probe non-historical tail.

If the strategy survives all of these with bounded drawdown and intact hedge structure, the backtest has cleared the cascade bar. If any single event produces ruin, the live deployment will eventually too.

## Common Modeling Errors

- **Constant slippage in cost model.** Fixed bps haircuts ignore depth collapse. Use a depth-walking [[slippage-modeling|slippage model]] or [[market-impact-models|impact model]] that scales with realized stress.
- **Ignoring [[auto-deleveraging|ADL]].** Backtests that only liquidate losers systematically overstate hedged-strategy Sharpe. Inject ADL probability proportional to PnL%-leverage rank.
- **Single-venue liquidity assumption.** Treating one exchange's book as the global book misses cross-venue contagion and the actual depth available to a multi-venue executor.
- **Independent liquidation sampling.** Drawing liquidation events from a Poisson process without self-excitation underprices clustering risk.
- **Static funding-rate assumption.** Funding term structure shifts violently in cascades; carry trades that look profitable on average funding lose multiples in stress.
- **No oracle/mark-price model.** Strategies trading near liquidation lines need explicit modeling of mark-vs-index lag, especially on [[hyperliquid]] and dYdX.
- **Survivorship bias in venue selection.** Backtesting only on currently-live venues drops FTX, BitMEX-dominant eras, etc. — periods that contain the most informative cascade structure.
- **Using post-event revised data.** Liquidation totals get re-stated days after; backtests should use the print available at the time, not the corrected number.

## Sources

- October 2025 liquidation cascade analysis: https://cryptoslate.com/bitcoin-sees-another-flash-crash-leading-to-1-52-billion-cascade-in-crypto-liquidations/
- LuxAlgo on slippage and liquidity backtesting limits: https://www.luxalgo.com/blog/backtesting-limitations-slippage-and-liquidity-explained/
- Glassnode on point-in-time data and lookahead-bias prevention: https://insights.glassnode.com/why-use-point-in-time-data/

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

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]].

## Related

- [[auto-deleveraging]] — the venue mechanic that turns cascades into hedge-killers
- [[liquidation-cascade-arbitrage]] — strategy page that *trades* cascades; this page handles the *modeling*
- [[liquidation-risk]] — base concept
- [[funding-rate]] — leading indicator and mechanical trigger
- [[slippage-modeling]] — required cost-model component for cascade backtests
- [[market-impact-models]] — depth-walking and impact functions
- [[intrabar-fill-modeling]] — sub-bar fill realism; cascades make intrabar ordering decisive
- [[monte-carlo-permutation-test]] — orthogonal robustness check
- [[backtesting-pitfalls]] — the general catalogue of backtest failure modes
- [[backtesting]] — base concept
- [[2025-10-crypto-liquidation-cascade]] — primary case study
- [[coinglass]], [[kaiko]] — required data sources
- [[crypto-perp-backtesting-pitfalls]] — parent overview
