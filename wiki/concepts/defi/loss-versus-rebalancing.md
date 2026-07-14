---
title: "Loss-Versus-Rebalancing (LVR)"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [defi, crypto, liquidity, amm, market-microstructure, adverse-selection, risk-management, volatility]
aliases: ["LVR", "Loss Versus Rebalancing", "Loss-vs-Rebalancing", "Rebalancing Loss"]
related: ["[[impermanent-loss]]", "[[automated-market-maker]]", "[[concentrated-liquidity]]", "[[uniswap]]", "[[adverse-selection]]", "[[delta-hedging]]", "[[jit-liquidity]]", "[[mev-strategies]]", "[[volatility]]", "[[market-making]]", "[[liquidity-provision]]", "[[cryptodataapi]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[automated-market-maker]]", "[[impermanent-loss]]"]
difficulty: advanced
---

# Loss-Versus-Rebalancing (LVR)

**Loss-versus-rebalancing (LVR, pronounced "lever")** is the cost an [[automated-market-maker|AMM]] liquidity provider pays to arbitrageurs who pick off the pool's stale quotes as the external market price moves. It is the difference between the P&L of an LP position and the P&L of a *rebalancing portfolio* that holds the identical asset weights but executes every rebalance at the true market price instead of at the pool's lagged price. Introduced by Jason Milionis, Ciamac Moallemi, Tim Roughgarden and Anthony Lee Zhang in 2022, LVR reframes liquidity provision as a continuous [[adverse-selection]] problem and has become the dominant modern lens on whether an AMM LP position is actually profitable — displacing [[impermanent-loss]] as the reference cost metric for serious LPs.

## The core idea: the LP versus the arbitrageur

An AMM quotes a price mechanically off its reserve ratio. When the real market (a deep CEX like [[binance|Binance]] order book, or an aggregate of them) moves, the pool's quote is momentarily *stale*. An arbitrageur trades against the pool to bring its price back in line and pockets the difference. Every one of those arbitrage trades is a small, guaranteed loss to the LP: the LP always sells the asset that is going up and buys the asset that is going down, one tick behind the market, forever.

LVR isolates exactly that loss. It answers a precise question:

> *How much worse off is the LP than a manager who held the same instantaneous portfolio (the same delta) but did all their buying and selling at the fair market price rather than at the pool's stale price?*

The answer is always non-negative, and it is the arbitrageur's profit. LVR is, definitionally, **the money that leaks from LPs to arbitrageurs because the AMM quote lags the market.** Fees are the only thing that offsets it.

## The rebalancing benchmark

The name comes from the benchmark. A constant-product AMM position has a delta (a directional exposure) that changes as price moves — it is short gamma, exactly like a short option. Milionis et al. construct a **rebalancing strategy** that replicates the AMM's delta at every instant by trading in the external market. Because the rebalancing strategy transacts at the true price and the AMM transacts at its own stale price, the two portfolios have identical exposure but different realized costs. The gap is LVR:

```
LVR(t)  =  V_rebalancing(t)  -  V_LP(t)   (before fees)
```

This decomposition is powerful because the rebalancing portfolio has **no market risk relative to the LP** — the two hold the same position at every moment. So LVR is a *pure*, predictable, monotonically increasing cost stream, not a random price outcome. That is what makes it hedgeable in the risk sense and analyzable in closed form.

## The formula

For a constant-product (Uniswap v2 style, 50/50) pool, the instantaneous LVR rate is a clean function of volatility only:

```
Instantaneous LVR rate  =  (σ² / 8) × (pool value)
```

where σ is the volatility of the pool pair. The units follow the units of σ:

- **Daily:** with ETH/USDC daily volatility σ = 5%, daily LVR ≈ σ²/8 = 0.05² / 8 = **3.125 basis points of pool value per day** (Source: Milionis, Moallemi, Roughgarden, Zhang 2022).
- **Annualized:** 3.125 bps/day compounds to roughly **11–12% of pool value per year** at that volatility. At crypto-typical realized vol (ETH often 60–90% annualized, i.e. ~3–5% daily), full-range v2 LVR runs on the order of **5–15% of pool value per year**.

The headline practitioner implication from the same paper: **a 30 bps-fee pool must turn over roughly 10% of its total value in volume every single day just for fees to cover LVR.** Below that turnover, the LP is bleeding to arbitrageurs faster than fees replace it — regardless of what the [[impermanent-loss]] number says.

LVR scales with **σ²**, so it is dominated by high-volatility periods: doubling volatility quadruples the LVR rate. This is why LVR spikes precisely during the events where LPs feel they "should" be earning the most fees — the fee income rises linearly with volume, but the LVR cost rises with the square of volatility.

## LVR vs impermanent loss

LVR and [[impermanent-loss|impermanent loss]] (IL) are often conflated. They measure different things, against different benchmarks, and IL systematically *understates* the true cost of LPing.

| | Impermanent Loss | Loss-Versus-Rebalancing |
|---|---|---|
| **Benchmark** | HODL (holding the initial tokens) | Rebalancing portfolio at market price |
| **What it captures** | Divergence between LP value and just holding | Adverse selection paid to arbitrageurs |
| **Path dependence** | Path-**independent** — depends only on start and end price | Path-**dependent** — accumulates with realized variance along the whole path |
| **Sign / behavior** | Can be zero if price round-trips back to entry | Strictly increasing; never given back, even on a round-trip |
| **Includes market risk?** | Yes — mixes directional P&L with the arbitrage cost | No — the pure, hedgeable cost after stripping directional exposure |
| **Hedgeable?** | The directional part is; the cost part is buried inside | Cleanly separable; the residual bleed after a perfect hedge |

The critical difference is **path dependence**. Suppose ETH goes from $3,000 to $4,000 and back to $3,000 over a week. IL at the end is **zero** — the price returned to entry, so LP value equals HODL value (before fees). But the pool was arbitraged the entire way up *and* the entire way down: arbitrageurs extracted value on every leg. LVR captured all of it and is decidedly **not** zero. IL saw a round-trip and reported "no harm done"; LVR correctly reports the cumulative bleed. LVR ≥ the arbitrage component of IL in expectation, and over volatile round-tripping markets LVR can be many times larger than the IL a naive LP would compute at withdrawal.

In short: **IL is what you notice at withdrawal; LVR is what you actually paid the whole time you were in the pool.**

## Markout: how LVR is measured empirically

You cannot observe the arbitrageur's counterfactual directly, but you can *measure* LVR from trade logs using **markout** — the same tool CEX market-making desks use to score their own fills.

Markout evaluates each fill by comparing its execution price to a reference (mid) price a fixed horizon later:

```
markout(Δ)  =  side × (P_reference(t + Δ)  -  P_fill(t)) × size
```

- A fill with **positive** average markout captured spread (the market did not move against it).
- A fill with **negative** average markout was **adversely selected** — the price moved against the position right after the trade.

For an AMM, every arbitrage fill has negative markout to the pool, because by construction the arb only trades when the pool is on the wrong side of the true price. Summed over all fills and taken to the continuous-time limit, the pool's negative markout **converges to LVR**. Markout at short horizons (one block, ~2–12 seconds on Ethereum; sub-second on an on-chain CLOB like [[hyperliquid]]) is the practical, data-driven estimator that DEX analytics dashboards now report alongside fee APR. Net LP edge is simply:

```
net LP edge  =  fee income  -  |LVR|  (≈ fee income + markout, since pool markout is negative)
```

## Why LVR is the dominant modern lens

LVR replaced IL as the serious LP's reference metric for four reasons:

1. **It is the *true* cost, not an artifact of the benchmark.** IL's HODL benchmark mixes a directional bet with the trading cost; LVR strips the direction out and leaves the pure, unavoidable bleed.
2. **It is predictable and closed-form.** σ²/8 lets an LP forecast the cost from a volatility estimate before deploying a dollar, and compare it directly against expected fee APR.
3. **It ties LP losses to a specific counterparty.** LVR *is* the arbitrageur's profit. That makes the AMM's economics legible as a two-sided game and points directly at the fix (capture the arb surplus for LPs — see mitigations below).
4. **It survives hedging.** This is the decisive property, and it is the crux of the hedging decision below.

## Implications for whether to hedge

The single most important consequence of the LVR framework: **delta-hedging an LP position removes impermanent loss's variance but does NOT remove LVR.**

Hedging the LP's delta (e.g. shorting a [[perpetual-futures|perp]] to offset the pool's long-ETH exposure) neutralizes the *directional* P&L — the part that makes IL look scary and random. What is left after a perfect hedge is a smooth, deterministic downward drift: the LVR. A perfectly delta-hedged LP still loses σ²/8 per unit time to arbitrageurs, because LVR is an adverse-selection cost, not a price-risk cost. Hedging cannot remove adverse selection; it can only remove the volatility of your equity curve.

So the hedging decision is *not* "should I eliminate my LP losses?" (you can't hedge away LVR) but "do I want my LP losses delivered as a bumpy IL number or as a steady LVR bleed?":

- **Hedge** if you are running LPing as a fee-harvesting business and want a low-variance, market-neutral return stream whose profitability is transparently `fee APR − LVR − hedging cost`. Hedging turns a short-gamma gamble into a clean carry trade — but only *makes money* if the fee APR exceeds LVR plus the hedge's own funding/slippage cost. See the LVR-aware delta-hedge overlay in [[concentrated-liquidity]].
- **Don't bother hedging** if the pool's fee APR comfortably exceeds LVR (deep, high-turnover majors, or correlated-asset pools like stETH/ETH and stablecoins where σ ≈ 0 makes LVR ≈ 0) and you are content to hold the directional exposure anyway.

The stablecoin/correlated-asset case is the clean tell: because LVR = σ²/8 and those pairs have near-zero relative volatility, they have near-zero LVR — which is *why* they are the only reliably profitable passive LP pools, and why [[curve|Curve]]-style pegged pools dominate low-risk LPing.

## Implications for concentrated-liquidity LPs

[[concentrated-liquidity|Concentrated liquidity]] (Uniswap v3/v4) does not reduce LVR — it **amplifies** it. Concentrating capital into a narrow range multiplies the effective ("virtual") liquidity `L` the arbitrageur trades against per unit of price move, so the LVR *density* while in range scales up by roughly the same concentration multiplier that scales up the fee income. A position squeezed into a ±10% band earning ~10× the fee APR of a full-range position is also paying ~10× the LVR rate while price sits in that band. Concentration is a leverage knob on the *entire* fee-vs-LVR trade, not a way to escape it.

Two structural wrinkles specific to v3:

- **Out of range, LVR is zero** — but so is fee income, and the position is now 100% the losing asset. You have simply exited the game holding the bag.
- **The break-even fee capture required per unit time rises with concentration.** Tighter ranges demand higher realized fee APR to clear the higher in-range LVR, which is why aggressive CL LPs must rebalance actively and increasingly hedge the residual LVR bleed rather than pretend concentration made the position safe.

## Mitigation: LVR-aware AMM designs

Because LVR is a design flaw of the continuous, stale-quote CFMM rather than a law of nature, a research and product effort has grown up to recapture the arbitrage surplus for LPs:

- **Batch-auction / function-maximizing AMMs (CoW AMM, FM-AMM).** Clear trades in discrete batches at a uniform price set by competition among solvers/arbitrageurs, so the arbitrage surplus flows to LPs instead of to a single fast arbitrageur — effectively eliminating LVR (and sandwich attacks) at the cost of synchronous on-chain composability.
- **Auction-managed AMMs (am-AMM).** Run a censorship-resistant on-chain auction for the right to be the pool's temporary "manager," who sets the swap fee and collects the surplus; the auction rent is returned to LPs, internalizing what would have been LVR.
- **Dynamic fees.** Raise the swap fee precisely when volatility (and thus LVR) is high, so the fee tracks the σ² cost curve. Uniswap v4 **hooks** make per-pool dynamic-fee and per-block-auction logic deployable, and stochastic-control work derives the optimal dynamic fee as a direct function of the LVR rate.
- **Oracle-based / protocol LVR protection (e.g. Diamond).** Use an external price reference to avoid quoting stale prices, or route the block-producer's LVR extraction back to LPs under competition.

For an individual LP today, the practical takeaways are: prefer high-turnover major pools or near-zero-σ correlated pairs; treat concentration as leverage on both fee APR and LVR; and if running size, hedge the delta and monitor whether `fee APR − LVR − hedge cost` is still positive.

## Getting the Data (CryptoDataAPI)

LVR is driven almost entirely by realized volatility (the σ in σ²/8) and by the pool/pair being LPed, so the relevant data is volatility regime plus the price series needed to estimate σ.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset volatility regime (compressed / expanding / vol_shock / mean_reverting / normal); the regime directly gates the LVR rate
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite 0–100
- `GET /api/v1/market-data/ticker/price?symbol=ETHUSDT` — current price for delta/mark computations
- `GET /api/v1/dex/trending?chain=ethereum` — trending DEX pools (identify which pairs/pools are being actively LPed)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000` — OHLCV to compute realized σ for the σ²/8 estimate
- `GET /api/v1/backtesting/klines` — deep archive for backtesting LVR vs fee APR across regimes
- `GET /api/v1/volatility/regime/{symbol}` — per-asset detail plus 60-day vol history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi]].

## Related

- [[impermanent-loss]] — the older, path-independent, HODL-benchmarked cost metric LVR supersedes
- [[concentrated-liquidity]] — Uniswap v3/v4 LPing, where concentration amplifies LVR (buildable strategy with an LVR-aware hedge overlay)
- [[jit-liquidity]] — single-block LP that sidesteps LVR by only being in the pool for one atomic swap
- [[automated-market-maker]] — the mechanism whose stale-quote design produces LVR
- [[adverse-selection]] — the microstructure concept LVR is the continuous-time AMM instance of
- [[delta-hedging]] — removes IL variance but not LVR; the tool for the hedged-LP business
- [[uniswap]] — the AMM where LVR was first quantified empirically
- [[market-making]] — CEX/CLOB analogue; markout is the shared measurement tool
- [[volatility]] — the σ that drives the σ²/8 LVR rate

## Sources

- Milionis, Moallemi, Roughgarden, Zhang, *Automated Market Making and Loss-Versus-Rebalancing* (2022), arXiv:2208.06046 — the paper that defines LVR, derives the σ²/8 constant-product rate, and gives the "10% daily turnover to cover 30 bps fees" result. https://arxiv.org/pdf/2208.06046
- Milionis, Moallemi, Roughgarden, *An Automated Market Maker Minimizing Loss-Versus-Rebalancing* (2022), arXiv:2210.10601 — oracle/redesign approaches to minimizing LVR.
- Adams, Moallemi, et al., *am-AMM: An Auction-Managed Automated Market Maker* (2024), arXiv:2403.03367 — auctioning the pool-manager role to internalize LVR.
- CoW Protocol / FM-AMM research — batch-auction AMM that eliminates arbitrage profit, LVR, and sandwich attacks (arXiv:2307.02074 on arbitrageurs' profits, LVR, and sandwich attacks).
- Atis Elsts, *Liquidity Provider Strategies for Uniswap v3: Loss Versus Rebalancing* (Medium) — practitioner walk-through of LVR for concentrated positions.
- *Measuring Arbitrage Losses and Profitability of AMM Liquidity* (2024), arXiv:2404.05803 — empirical markout-based LVR measurement across Uniswap pools.
- Fenbushi, *Ending LP's Losing Game: Exploring the LVR Problem and its Solutions* (2024) — survey of LVR mitigation designs.
