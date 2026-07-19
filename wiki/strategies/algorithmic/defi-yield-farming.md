---
title: "DeFi Yield Farming"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [crypto, defi, yield-farming, liquidity-mining, staking, impermanent-loss, curve, aave, quantitative]
aliases: ["Yield Farming", "Liquidity Mining", "DeFi Yield Strategies", "LP Farming"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, risk-bearing, behavioral]
edge_mechanism: "Protocols pay LPs a blend of real trading fees (structural — LPs are the counterparty to every swapper) plus token emissions and bribes (behavioral — protocols overpay to bootstrap TVL); the farmer is compensated for bearing impermanent-loss/LVR, smart-contract, and reward-token-depreciation risks that passive holders refuse to bear."

# Data and infrastructure requirements
data_required: [pool-apr, tvl, pool-reserves, emissions-schedule, reward-token-price, funding-rates, gas-prices]
min_capital_usd: 5000        # on L2; on Ethereum L1 gas makes <~$25k positions uneconomic to compound
capacity_usd: 10000000       # deep stable pools absorb tens of millions, but APR compresses with size
crowding_risk: high

# Performance expectations (net of IL/LVR, gas, emissions decay, and reward-token depreciation)
expected_sharpe: 1.0         # disciplined, stable-focused, delta-hedged; volatile unhedged farming is far lower
expected_max_drawdown: 0.25  # driven by exploit/depeg tail, not day-to-day fee variance
breakeven_cost_bps: 40       # round-trip entry/exit + rotation/compounding gas drag

# Decay history
decay_evidence: "DeFi Summer (2020) 100%+ APYs from COMP/SUSHI/CRV emissions compressed to single-digit real yields as mercenary capital arbitraged incentives and reward tokens fell 80-95% from peaks. Terra/Anchor's 20% 'stable' APY (unsustainable subsidy) collapsed May 2022. Curve-Wars bribe yields compressed as veCRV emissions rolled off."

# Lifecycle
kill_criteria: |
  - real (fee) APR falls below the position's risk-adjusted hurdle for > 14 days
  - TVL exodus: pool TVL drops > 40% in 7 days (yield about to spike then collapse; exit-liquidity risk)
  - exploit / security signal on the protocol or a composed dependency (any size) -> exit immediately
  - stablecoin in the pool depegs > 1% sustained, or a volatile-pair IL exceeds cumulative fees earned
  - reward token down > 50% in 30 days with emissions still the majority of APR (unsustainable)

related: ["[[impermanent-loss]]", "[[loss-versus-rebalancing]]", "[[automated-market-maker]]", "[[liquidity-pool]]", "[[delta-neutral]]", "[[funding-rate-arbitrage]]", "[[smart-contract-risk]]", "[[stablecoin-depeg]]", "[[curve]]", "[[convex]]", "[[aave]]", "[[pendle]]", "[[ethena-usde]]", "[[mev-strategies]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[kelly-criterion]]"]
---

# DeFi Yield Farming

DeFi yield farming deploys crypto assets into decentralized protocols to earn a **blend of trading fees, token emissions, and incentives** — most commonly by providing liquidity to an [[automated-market-maker|AMM]] pool and staking the LP token for extra rewards. Built as a systematic strategy rather than APY-chasing, it is a **risk-premium harvest**: the farmer is paid to bear impermanent loss / [[loss-versus-rebalancing|LVR]], smart-contract risk, and reward-token depreciation. The buildable version decomposes the headline APR into sustainable vs subsidized components, sizes inversely to smart-contract risk, optionally **delta-hedges** the directional exposure away, and rotates on hard numerical rules — because the number displayed on a farm's dashboard is almost never the number you keep.

## Edge source

Per [[edge-taxonomy]], yield farming is **structural + risk-bearing + behavioral**:

- **Structural.** An LP is the mechanical counterparty to every swap in the pool and is paid a fee for it. As long as the pool sees volume, fee yield accrues — contractually, not on opinion.
- **Risk-bearing.** The farmer absorbs risks passive holders will not: [[impermanent-loss|IL]]/LVR (the LP loses to arbitrageurs when price moves), smart-contract exploit risk, and depeg risk. The excess yield above a risk-free stable rate is the premium for bearing these.
- **Behavioral.** Protocols systematically **overpay emissions** to bootstrap TVL (the "mercenary capital" dynamic since DeFi Summer 2020). Early farmers capture subsidy that later farmers arbitrage away — a real but decaying source of return.

The strategy does **not** rely on informational or latency edge; every APR, TVL, and emission schedule is public. The edge is in *correctly pricing the risks the headline APR ignores* and sizing accordingly.

## Why this edge exists

Three persistent frictions keep paying disciplined farmers:

1. **Bootstrapping subsidy.** New protocols must attract liquidity and pay for it in their own token. This is a deliberate wealth transfer from token-holders (future dilution) to early LPs. It is real yield to the farmer even as it is inflationary to the protocol — the farmer's job is to harvest it and exit before the token depreciates.
2. **Mispriced risk.** Most participants read the headline APR and ignore IL/LVR, emissions decay, and exploit probability. The disciplined farmer prices those and only enters when the *risk-adjusted, cost-corrected* yield clears a hurdle — capturing the gap between naive and true expected return.
3. **Complexity and gas friction.** Correctly composing pools, hedging delta, and timing rotation is operationally hard and gas-costly, so the crowd under-does it. That friction is exactly why the premium persists rather than being instantly arbitraged to the risk-free rate.

## Null hypothesis

Under no-edge conditions, farming yield equals the risk-free stable rate plus fair compensation for IL/LVR, exploit, and depeg risk — i.e., **risk-adjusted excess return of zero**, with the headline APR being pure illusion once reward-token depreciation and IL are netted out. Predictions of the null world: (1) after subtracting realized IL/LVR and marking reward tokens at their *depreciated* exit price, net APR ≈ the stable risk-free rate; (2) "high-APR" farms deliver *lower* risk-adjusted returns than boring stable pools because their yield is emissions that fall as fast as they are earned. The historical record partly *confirms* the null for naive farmers (most high-APR farms were net-negative after token collapse) and rejects it for disciplined ones (stable, real-yield, hedged farming produced steady positive risk-adjusted returns). If your farming P&L, marked honestly (reward tokens at exit price, IL realized), cannot beat holding a stablecoin money-market position, you are harvesting illusion.

## Rules

### APR decomposition (the entry screen)

Never act on a headline APR. Decompose it:

```
total_APR = fee_APR            # REAL yield: share of swap fees; sustainable, scales with volume
          + emission_APR       # protocol token emissions (CRV/CVX/etc.); inflationary, decays
          + incentive_APR      # external bribes/incentives; episodic, ends abruptly
```

- **Real-yield ratio** = `fee_APR / total_APR`. Prefer pools where this is high; a 90%-emissions APR is a countdown timer, not an income stream.
- Mark `emission_APR` and `incentive_APR` at the reward token's **expected exit price**, not spot — most farming tokens fall 80–95% from peak.

### Entry conditions (all required)

1. **Risk-adjusted hurdle:** `fee_APR + haircut(emission_APR) − expected_IL − expected_exploit_cost > required_return`.
2. **Real-yield floor:** `fee_APR / total_APR` above a threshold (e.g., ≥ 30%) unless you are explicitly running a short-dated emissions harvest with a pre-planned exit.
3. **TVL health:** pool TVL stable or rising; avoid pools where a single whale is most of the TVL (exit-liquidity risk).
4. **Protocol risk gate:** audited by reputable firms (Trail of Bits, OpenZeppelin, Spearbit), meaningful "TVL-days" of survival, no unresolved critical findings. Unaudited/new farms are treated as venture bets, not income.
5. **Pair-risk gate:** stable-stable (minimal IL) or a pair you intend to **delta-hedge** (below). Naked volatile-pair LPing without a hedge is only justified when `fee_APR` demonstrably exceeds expected LVR.

### Smart-contract-risk-adjusted sizing

Size **inversely to exploit probability**, not to headline APR:

```
expected_net = nominal_APR * (1 - P_exploit_annual) - P_exploit_annual * loss_given_exploit  # ~100%
```

- Estimate `P_exploit_annual` from audits, code maturity, TVL-days, prior incident history, and dependency complexity (each composed protocol multiplies exposure).
- Convert `expected_net` and its (fat, left-skewed) distribution into a fractional [[kelly-criterion|Kelly]] size — the exploit tail makes full-Kelly reckless, so use a heavy fraction (≤ 0.25×).
- **Hard caps:** never > 25% of the DeFi book in one pool; never > a set % in one protocol across pools (composability multiplies, it does not diversify); weight battle-tested venues ([[aave]], [[curve]], [[uniswap]]) over new farms.

### Delta-hedge overlay (turning an LP into a market-neutral yield position)

A volatile-pair LP carries directional exposure and bleeds IL/LVR as price moves. Neutralize it:

- A 50/50 ETH/USDC LP is ~**+0.5 delta** to ETH at entry; short an ETH perp of matching notional to zero net delta so the position earns fees/emissions with the price risk hedged.
- **Concentrated (v3) positions have changing delta and negative gamma** — delta swings across the range and IL accelerates near the edges — so the hedge must be **rebalanced** as delta drifts (and the position re-ranged), a gas-and-funding cost that the fee yield must exceed.
- The hedge **costs funding** (you pay/receive perp [[funding-rate]]); a hedged farm is only worth it when `fee_APR + haircut(emission_APR) > hedge_funding_cost + rebalance_gas + expected_residual_LVR`. This is the same delta-neutral discipline as [[funding-rate-arbitrage]], applied to LP income. Stable-stable pools need no hedge (near-zero delta).

### Exit and rotation

- **Yield degradation:** `fee_APR` (real yield) falls below the risk-adjusted hurdle for > 14 days → rotate out.
- **IL threshold:** on a volatile pair, cumulative IL exceeds cumulative fees earned → exit (the LP is now worse than holding).
- **Risk event:** any exploit, governance attack, or [[stablecoin-depeg|depeg]] on the protocol or a composed dependency → exit *immediately*, do not wait for recovery (UST/Anchor, May 2022, is the archetype).
- **Reward-token management:** harvest and **sell/hedge** reward tokens on a schedule rather than accumulating; do not let un-sold CRV/CVX/etc. become the position's real (unhedged) exposure.
- **Rotation gate:** only rotate when `new_risk_adj_APR − old_risk_adj_APR` exceeds the **round-trip gas + swap cost** of moving; churning small yield differences on L1 is a guaranteed loss to gas. Consolidate/compound when gas is cheap or on L2 ([[arbitrum]], [[optimism]], Base).

## Implementation pseudocode

```python
# yield_farm.py — decompose, risk-adjust, hedge, rotate
HURDLE = 0.06            # required risk-adjusted APR
REAL_YIELD_FLOOR = 0.30  # fee_APR / total_APR
MAX_PER_POOL = 0.25
TVL_EXODUS = -0.40       # 40% drop in 7d -> exit

def evaluate(pool, book):
    fee, emis, inc = decompose_apr(pool)                 # real vs subsidized
    total = fee + emis + inc
    real_yield_ratio = fee / total if total else 0
    haircut_emis = emis * expected_token_retention(pool.reward_token)  # mark at exit price
    exp_il  = expected_il_or_lvr(pool)                   # 0 for stable-stable
    p_hack  = exploit_probability(pool.protocol)         # audits, TVL-days, deps
    exp_net = fee + haircut_emis - exp_il - p_hack * 1.0 # loss_given_exploit ~= 100%

    # --- kill/exit checks first ---
    if security_event(pool.protocol) or depeg(pool) > 0.01:
        return {"action": "EXIT_NOW", "reason": "exploit/depeg"}
    if pool.tvl_change_7d < TVL_EXODUS:
        return {"action": "EXIT", "reason": "TVL exodus"}
    if pool in book and cumulative_il(pool) > cumulative_fees(pool):
        return {"action": "EXIT", "reason": "IL > fees"}

    # --- entry / sizing ---
    if exp_net < HURDLE or real_yield_ratio < REAL_YIELD_FLOOR:
        return {"action": "SKIP", "reason": "below risk-adjusted hurdle / too much emission"}
    size = min(MAX_PER_POOL * book.capital, kelly_fraction(exp_net, p_hack) * book.capital)
    hedge = delta_hedge_notional(pool, size)             # short perp if volatile pair
    if hedge and fee + haircut_emis < hedge_cost(hedge) + rebalance_gas(pool):
        return {"action": "SKIP", "reason": "hedge cost exceeds yield"}
    return {"action": "ENTER", "size": size, "hedge": hedge}
```

## Indicators / data used

- **APR decomposition** — fee vs emission vs incentive APR (DefiLlama Yields, protocol subgraphs). The single most important input.
- **TVL and TVL trend** — level, 7d/30d change, and concentration (whale share).
- **Pool reserves / ratio** — for IL and delta computation; v3 tick/range for concentrated positions.
- **Emissions schedule** — when reward emissions step down (directly cuts APR).
- **Reward-token price and liquidity** — to mark yield at a realistic exit price and gauge sell impact.
- **[[funding-rate]]** — the cost of the delta-hedge overlay.
- **Audit / incident data and gas** — for exploit-probability sizing and rotation economics.

## Example trade (delta-neutral ETH/USDC LP)

1. **Screen:** a concentrated ETH/USDC 0.05% pool shows 22% APR — decomposed as **9% fee_APR + 13% emissions**. Real-yield ratio 41% (above floor). Emissions marked at exit price → haircut to ~6%.
2. **Risk-adjusted:** expected IL/LVR on the chosen range ≈ 5% annualized; `P_exploit` low (audited, high TVL-days). `exp_net ≈ 9% + 6% − 5% ≈ 10%` before hedge — above the 6% hurdle.
3. **Deploy:** $50,000 into the pool (within the 25% cap). Position delta ≈ +0.5 ETH per $1 of ETH exposure ≈ ~8 ETH-equivalent long.
4. **Hedge:** short ~8 ETH of perp to zero net delta. Hedge cost = perp funding (say 8% APY paid) on the hedged notional; rebalance the short as the range delta drifts.
5. **Net:** fees + haircut emissions (~15%) − IL residual (~2% after hedging most of it) − hedge funding drag − rebalance gas ≈ **7–9% net, market-neutral** on the $50k — versus a naked LP that would show 22% on the dashboard and deliver far less after IL and token depreciation.
6. **Exit:** emissions step down and fee_APR drifts below hurdle after 6 weeks → unwind LP, close the perp hedge, sell accumulated reward tokens (which have already fallen 30%).

The point of the worked example: the honestly-computed **7–9% market-neutral** beats the naive 22% headline that, after IL and an 80%+ reward-token drawdown, would have been low-single-digits or negative.

## Performance characteristics (realistic cost overlay)

Marked honestly — reward tokens at exit price, IL/LVR realized, gas and hedge costs included:

| Metric | Value | Note |
|---|---|---|
| Net APY (stable, real-yield) | 3–9% | Curve/Aave-class stable pools; steady in any regime |
| Net APY (volatile, delta-hedged) | 5–12% | After IL residual + hedge funding; market-neutral |
| Net APY (naive volatile, unhedged) | often < 0 after token depreciation | The "great APR, terrible realized" trap |
| Sharpe (disciplined, hedged) | ~1.0 | Tail-dominated by exploit/depeg, not fee variance |
| Max drawdown | up to 25%+ | Exploit or depeg on a single position; diversification caps it |
| Breakeven cost | ~40 bps round-trip + rotation gas | On L1, gas alone kills small-position economics |

**Cost overlay that naive backtests omit:**
- **[[impermanent-loss|IL]] / [[loss-versus-rebalancing|LVR]]** — LVR (Milionis–Moallemi–Roughgarden–Zhou, 2022) is the systematic loss LPs pay arbitrageurs, scaling with volatility²; it is the *fundamental* cost of AMM LPing and dwarfs IL-vs-holding in high-vol pairs.
- **Reward-token depreciation** — mark emissions at exit price; farming tokens routinely fall 80–95%.
- **Gas** — Ethereum L1 claim/compound can be $20–100+ per action; small positions are uneconomic to compound on L1.
- **Hedge funding + rebalance drag** — the cost of the delta overlay.
- **Emissions decay** — the headline APR falls as TVL rises and emissions step down; the number at entry is not the number over the hold.

## Capacity limits

High capacity but **yield-compressing with size**: adding capital to a pool dilutes your share of a fixed fee flow, so APR falls as you scale. Deep stable pools (Curve stable pools, Aave money markets) absorb tens of millions at a *compressed* yield; mid-cap and volatile pools cap a single farmer at low hundreds of thousands to low millions before their own capital moves the APR against them. Reward-token sell impact is a second ceiling — harvesting large emissions positions can crater the token you are trying to realize. Realistic single-operator capacity: **low-to-mid seven figures** across diversified pools; `capacity_usd: 10000000` reflects the point beyond which yield compression and exit-liquidity dominate.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Smart-contract exploit (tail realised).** A hack or logic bug can take a position to zero regardless of yield — the dominant, un-diversifiable tail. Composability multiplies exposure across every protocol touched.
2. **Reward-token collapse (edge decay).** When APR is mostly emissions and the token falls 80–95%, realized yield is a fraction of the headline. The DeFi-Summer-to-now compression is the secular version.
3. **Stablecoin depeg / regime change.** UST/Anchor (May 2022) is the archetype: a 20% "stable" APY that was an unsustainable subsidy; the pool rebalanced entirely into the depegged asset. Any stable in a pool depegging turns a "safe" position into a directional loss.
4. **TVL exodus / mercenary flight.** When incentives end, capital flees, fee yield dries up, and the last LPs out are exit liquidity.
5. **IL/LVR overwhelming fees.** On volatile pairs in trending markets, LVR exceeds fee income; an unhedged LP would have been better off just holding.
6. **Gas/rotation drag.** On L1, churning between farms burns the edge in transaction costs.

## Kill criteria

The sleeve exits a position (or the strategy pauses) on any of:

1. **Real (fee) APR below the risk-adjusted hurdle for > 14 days.**
2. **TVL exodus:** pool TVL down **> 40% in 7 days**.
3. **Exploit / security signal** on the protocol or a composed dependency (any size) → immediate exit.
4. **Stablecoin depeg > 1% sustained**, or **volatile-pair IL > cumulative fees earned**.
5. **Reward token down > 50% in 30 days** while emissions remain the majority of APR (unsustainable subsidy).

See [[when-to-retire-a-strategy]]. Yield farming is *position-rotational*: individual farms are retired constantly as their subsidy decays, while the strategy itself migrates to the next real-yield opportunity — so per-pool kill-and-rotate is the norm, whole-strategy retirement rare.

## Advantages

- **Real, structural yield** where fee_APR dominates — a genuine risk premium, not just token inflation.
- **Market-neutral when delta-hedged** — converts LP income into a funding-like carry uncorrelated to price direction.
- **Permissionless and composable** — no KYC, no minimums, and "money-lego" stacking of fee + emissions + boost + bribes.
- **Transparent** — every APR, TVL, and emission is on-chain and verifiable before committing.
- **Stable-pool option** — stablecoin farming delivers steady yield with minimal IL in any regime.

## Disadvantages

- **Smart-contract risk** — the un-diversifiable tail; audited protocols still get exploited, and composability multiplies exposure.
- **IL / LVR** — providing to volatile pairs can lose to arbitrageurs faster than fees accrue; LVR scales with volatility².
- **Reward-token depreciation** — most farming tokens lose 80–95%, so "real" APY is far below headline.
- **Emissions decay and crowding** — mercenary capital compresses yields quickly; the entry APR is not the hold APR.
- **Gas and operational drag** — L1 compounding/rotation is expensive; hedged positions need active rebalancing.
- **Regulatory and rug risk** — token rewards may be reclassified as securities; unaudited farms can be outright scams.

## Sources

- Milionis, Moallemi, Roughgarden, Zhou, *Automated Market Making and Loss-Versus-Rebalancing* (2022) — the LVR framework; the fundamental cost of AMM liquidity provision.
- Uniswap v3 core whitepaper (2021) — concentrated-liquidity mechanics (changing delta, negative gamma) underlying the hedge overlay.
- DeFi Summer (2020): Compound COMP liquidity mining (June 2020); SushiSwap vampire attack (Aug–Sep 2020) — origin of emissions-driven farming.
- Terra/UST and Anchor 20% APY collapse (May 2022) — canonical unsustainable-subsidy / depeg failure.
- DefiLlama Yields and protocol documentation for APR/TVL decomposition (public data).
- General DeFi market knowledge; delta-neutral discipline shared with this wiki's [[funding-rate-arbitrage]]. No single external source ingested yet.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI supports the screening, security-gating, and hedge-cost sides of the strategy (pool APR/TVL themselves come from DefiLlama Yields and protocol subgraphs):

- `GET /api/v1/dex/trending` — trending DEX pools across Solana/Ethereum/Base/BSC/Arbitrum (candidate discovery)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection) — the protocol-risk gate
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score (feeds the exploit / kill trigger)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the cost of the delta-hedge overlay
- `GET /api/v1/on-chain/stablecoin-reserves` — stablecoin supply/reserve context for depeg-risk monitoring

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/dex/security/ethereum/0xTOKEN"
```

Auth: `X-API-Key` header. Catalogs: [[cryptodataapi-dex]], [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Screening** — candidates from `GET /api/v1/dex/trending` / `GET /api/v1/dex/new-pools`, each gated through `GET /api/v1/dex/security/{chain}/{address}` before capital touches the pool (APR/TVL decomposition still comes from DefiLlama)
- **Kill-switch watch** — `GET /api/v1/security/regime` + `GET /api/v1/security/regime/score` automate the exploit/depeg exit triggers; poll them more often than the yield scan
- **Hedge costing** — `GET /api/v1/derivatives/funding-rates?coin=ETH` re-prices the delta-neutral overlay every funding period
- **Regime gate** — `GET /api/v1/quant/market` — emissions-heavy APYs decay fastest in bear states; scale the farm book with the HMM bull/bear probabilities
- **Backtest** — replay reward-token price paths via `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d to 2017-08) paired with point-in-time state from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) so exploit-adjusted EV estimates avoid lookahead
- **Tips** — respect `new_listing` flags on farm/reward tokens; batch peg and market checks through the cached `/api/v1/daily` bundle hourly

## Related

- [[impermanent-loss]] — the price-divergence LP loss vs holding
- [[loss-versus-rebalancing]] — the deeper, volatility²-scaling LP cost vs arbitrageurs
- [[automated-market-maker]] / [[liquidity-pool]] — the mechanism being provided to
- [[delta-neutral]] / [[funding-rate-arbitrage]] — the hedge overlay and its funding-carry cousin
- [[smart-contract-risk]] / [[stablecoin-depeg]] — the dominant tail risks
- [[curve]] / [[convex]] / [[aave]] / [[pendle]] — core venues and the Curve-Wars / yield-token ecosystem
- [[ethena-usde]] — synthetic-dollar yield that industrialized part of this trade
- [[mev-strategies]] — interacts with farming (JIT liquidity dilutes passive LPs; arbitrageurs are who LPs lose to)
- [[kelly-criterion]] — exploit-adjusted position sizing
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]]
