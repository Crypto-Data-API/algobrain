---
title: "Delta-Neutral Yield Farming"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, delta-neutral, yield-farming, funding-rate, defi, market-neutral, quantitative, staking]
aliases: ["Delta-Neutral Yield", "Hedged Staking", "Synthetic Dollar Farm", "Market-Neutral Yield Farm"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced

backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, risk-bearing, behavioral]
edge_mechanism: "Stakers and LPs earn a protocol-native yield on a volatile asset while leveraged perp longs pay funding; you hold the yield-bearing asset and short an equal-notional perp to strip out price risk, keeping staking + LP + funding income and being paid to bear the basis, depeg, smart-contract, and liquidation risk the yield-chaser will not."

# Data and infrastructure requirements
data_required: [funding-rates, spot-price, perp-price, staking-yield, lst-peg, open-interest, mark-price, defi-tvl]
min_capital_usd: 5000
capacity_usd: 25000000
crowding_risk: high

# Performance expectations (net of fees, funding drag, and rebalance slippage)
expected_sharpe: 1.3
expected_max_drawdown: 0.12
breakeven_cost_bps: 15

# Decay history
decay_evidence: "Ethena's sUSDe yield averaged ~19% APY through 2024 and compressed to ~5% by mid-2025 as USDe supply scaled to a $14.8B peak (Oct 2025) and industrialised the hedge. ETH staking yield itself fell from ~5% (2022) to ~3% (2025) as the validator set grew. Funding — the second yield leg — briefly went negative on 2025-10-10 as $5.7B redeemed from USDe in a month."

# Lifecycle (only if deployed — see [[live-journal]])
kill_criteria: |
  - 7-day funding average turns negative AND staking+LP yield < |funding drag|
  - LST/LP long leg depegs > 2% from the perp's underlying and does not recover in 24h
  - drawdown > 12% on the sleeve
  - perp-venue insurance-fund socialised loss or withdrawal halt
  - net hedged yield < risk-free stablecoin lending rate for 30+ days

related: ["[[funding-rate-arbitrage]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[delta-neutral]]", "[[basis]]", "[[cash-and-carry]]", "[[ethena-usde]]", "[[stablecoin-yield]]", "[[crypto-yield-stack]]", "[[liquid-staking]]", "[[eth-staking]]", "[[defi-lending]]", "[[hyperliquid]]", "[[binance]]", "[[liquidation-risk]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Delta-Neutral Yield Farming

Delta-neutral yield farming holds a **yield-bearing crypto asset** (a liquid-staking token, an LP position, or a restaked asset) and simultaneously **shorts an equal-notional [[perpetual-futures|perp]]** to cancel the price delta. The net position has (close to) zero directional exposure, so the return stream is the underlying protocol yield — staking rewards, LP fees, lending interest — plus or minus the perp [[funding-rate]]. It is the generalisation of [[funding-rate-arbitrage]]: instead of a plain spot long, the long leg is itself productive, stacking a structural yield on top of (or instead of) the funding carry. [[ethena-usde|Ethena's USDe]] is the largest live implementation of exactly this construction.

## Edge source

Mapping to the six categories in [[edge-taxonomy]], this is a hybrid of three:

- **Structural (primary).** Two contractual cash-flows drive the return. (1) Proof-of-stake and DeFi protocols pay a *protocol-native* yield — ETH staking issuance, LP swap fees, lending interest — to whoever supplies the productive asset. (2) The perpetual contract's funding mechanism *must* transfer cash from longs to shorts whenever the perp trades above index. Neither is an opinion; both are hard-coded flows you position to receive.
- **Risk-bearing (secondary).** You are paid to warehouse risks the naive yield-chaser refuses: LST/LP-vs-underlying basis and depeg risk, smart-contract risk on the yield leg, perp-venue counterparty risk, funding inversion, and liquidation risk on the short. The excess of hedged yield over the risk-free stablecoin rate *is* that risk premium — not a free lunch.
- **Behavioural (tertiary).** The funding leg is positive because leveraged retail persistently bids perps above spot for convex, one-click long exposure (see [[funding-rate-arbitrage]] for the full treatment). When funding is positive it *adds* to the staking yield; when it is negative it is a drag you must cover from the staking leg.

The trade needs no informational, analytical, or latency edge. Everything (funding, staking APR, LST peg) is publicly observable. The edge is operational: running two legs across two systems and surviving the tail.

## Why this edge exists

1. **Yield-chasers want yield without hedging.** The typical DeFi user stakes ETH or LPs a pool and simply *eats* the price risk. Very few pair the position with a perp short, because it requires a second venue, margin management, and rebalancing. The unmet hedging supply leaves a structural premium for operators who can run both legs.
2. **Leverage preference funds the second leg.** Perp longs pay funding for the same reason as in [[funding-rate-arbitrage]]: leveraged bull exposure is cheaper to express on a perp than via spot-plus-margin. In bull regimes this makes the hedge *pay you* rather than cost you.
3. **Segmented capital.** Staking yield lives on-chain; funding lives on perp venues; the risk-free rate lives in stablecoin lending. Capital does not flow frictionlessly between them (gas, KYC, bridge risk, custody), so the three yields do not equalise. The delta-neutral farmer arbitrages that segmentation.

Empirically, [[ethena-usde|Ethena]] scaled USDe to a $14.8B peak precisely because the hedged yield sat persistently above the risk-free rate — a market-cap-weighted vote that the premium is real.

## Null hypothesis

Under an efficient, no-edge world the hedged return equals the risk-free stablecoin rate and nothing more:

- Staking/LP yield would be *exactly* offset by negative funding drag plus basis convergence, leaving net yield ≈ risk-free rate (~4-5% USDC lending).
- The 7-day funding average would oscillate near the interest-rate baseline (~0.01%/8h) with no persistence.
- LST peg deviations would be pure noise with zero expected P&L.
- A hedged farm's Sharpe would be indistinguishable from holding T-bill-equivalent stablecoin loans.

The record falsifies this: sUSDe delivered ~19% APY through 2024, well above risk-free, and hedged ETH-staking farms cleared 10-15% net in the same window. But the null is *not* rejected in every regime — the 2025-10-10 funding crash pushed hedged yield to roughly the risk-free rate for weeks, which is exactly what the null world looks like. If your live sleeve produces net yield indistinguishable from stablecoin lending for 30+ days, the regime has changed and the trade should be paused.

## Rules

### Entry conditions

1. **Yield leg viable.** Underlying protocol yield (staking APR, or realised LP fee APR over trailing 30d) ≥ 3% and the yield token trades within **0.5%** of its redemption/underlying value.
2. **Funding not deeply negative.** 8h funding on the hedge perp ≥ **−0.01%** (i.e., funding drag, if any, is smaller than the staking yield). Positive funding is a bonus, not a requirement — the staking leg can carry the trade.
3. **Combined carry positive.** Projected net = staking/LP APR + annualised funding − all-in costs > risk-free stablecoin rate + a **300 bps** premium for the risk borne. If it does not clear that hurdle, hold stablecoins instead.
4. **Peg + OI health.** LST peg within 0.5%; perp open interest stable or rising (real long flow, not an illiquid quote).
5. **Counterparty health.** No active insurance-fund draw-down, no LST-vs-underlying oracle deviation > 50 bps, no protocol exploit flag in the last 7 days.

### Exit conditions (whichever first)

1. **7d funding average turns negative AND staking/LP yield < |funding drag|** — the hedge now costs more than the yield leg earns.
2. **LST/LP depeg > 2%** from underlying and not recovering within 24h — basis risk on the long leg dominates.
3. **Net hedged yield < risk-free stablecoin rate for 30 days** — edge compressed out; redeploy to lending.
4. **Sleeve drawdown > 12%** — kill criterion (see below).
5. **Counterparty event** — perp-venue withdrawal halt, LST protocol exploit, or oracle divergence.

### Position sizing

- **1:1 delta hedge.** Perp short notional = long-leg USD notional. Verify delta after every rebalance; re-hedge when delta drift > **2%**.
- **1x-2x on the perp short, isolated margin.** Higher leverage cuts capital outlay but adds liquidation risk on the short during sharp rips. Keep **2-3x** the maintenance-margin buffer on the short.
- **Per-protocol cap 25%** of the sleeve so a single smart-contract exploit or LST depeg cannot wipe the book.
- **Max 3 concurrent yield legs** to bound operational surface (rebalancing, monitoring, withdrawals).

## Implementation pseudocode

```python
# delta_neutral_yield.py — decision loop for a hedged staking/LP farm
STAKING_MIN_APR   = 0.03     # 3% floor on the yield leg
PEG_TOLERANCE     = 0.005    # 0.5% LST/underlying peg band at entry
DEPEG_KILL        = 0.02     # 2% depeg exit
FUNDING_FLOOR_8H  = -0.0001  # -0.01%/8h: hedge drag must stay below yield
DELTA_REHEDGE     = 0.02     # re-hedge when |delta| > 2%
RISK_PREMIUM_APR  = 0.03     # required spread over risk-free
MAX_PER_PROTOCOL  = 0.25
DRAWDOWN_KILL     = 0.12

def net_carry(sig):
    funding_apr = sig.funding_8h * 3 * 365
    return sig.staking_apr + funding_apr - sig.all_in_cost_apr

def decide(sig, book):
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    peg_dev = abs(sig.lst_price - sig.underlying_price) / sig.underlying_price
    pos = book["positions"].get(sig.asset)

    # ---- exits ----
    if pos is not None:
        if peg_dev > DEPEG_KILL and not sig.peg_recovering:
            return {"action": "EXIT", "asset": sig.asset, "reason": "LST depeg"}
        if sig.funding_7d_avg < 0 and sig.staking_apr < abs(sig.funding_7d_avg*3*365):
            return {"action": "EXIT", "asset": sig.asset, "reason": "hedge costs > yield"}
        if net_carry(sig) < sig.risk_free_apr:
            return {"action": "EXIT", "asset": sig.asset, "reason": "carry below risk-free"}
        if abs(sig.net_delta) > DELTA_REHEDGE:
            return {"action": "REHEDGE", "asset": sig.asset, "target_delta": 0.0}
        return {"action": "HOLD", "asset": sig.asset}

    # ---- entry ----
    if len(book["positions"]) >= 3:
        return {"action": "WAIT", "reason": "max concurrent legs"}
    if sig.staking_apr < STAKING_MIN_APR or peg_dev > PEG_TOLERANCE:
        return {"action": "WAIT", "reason": "yield leg not viable"}
    if sig.funding_8h < FUNDING_FLOOR_8H:
        return {"action": "WAIT", "reason": "funding too negative"}
    if net_carry(sig) < sig.risk_free_apr + RISK_PREMIUM_APR:
        return {"action": "WAIT", "reason": "carry does not clear risk hurdle"}

    notional = MAX_PER_PROTOCOL * book["sleeve_capital"]
    return {
        "action": "OPEN", "asset": sig.asset,
        "yield_leg_notional": notional,   # stake / LP the underlying
        "perp_short_notional": notional,  # isolated, 1x-2x, delta-neutral hedge
        "reason": f"net carry {net_carry(sig)*100:.1f}% APR",
    }
```

The production system adds: LST redemption-queue monitoring, hourly delta re-hedge, gas-aware rebalancing (skip re-hedge if gas cost > drift P&L), and a manual kill switch.

## Indicators / data used

- **[[funding-rate]] (8h/1h)** — the second yield leg; annualise as `rate × periods/yr`.
- **Staking / LP APR** — the primary yield leg (ETH issuance yield; trailing-30d realised LP fee APR).
- **LST peg** — LST price vs underlying; the basis-risk and depeg guard.
- **[[open-interest]]** — confirms real long-side flow behind positive funding.
- **Mark / index price** — for the delta-hedge and oracle-divergence guard.
- **DeFi TVL + protocol health** — exploit/withdrawal-risk monitoring on the yield leg.
- **Risk-free reference** — stablecoin lending rate (Aave/Compound USDC) as the hurdle the trade must beat.

## Example trade

**Setup (2026-05-10):**

- Capital: $50,000. Long leg: stETH earning **3.1%** staking APR; stETH/ETH peg 0.999 (within band).
- Hedge: short ETH perp on [[hyperliquid]], 8h funding **+0.012%** (~13% APY), 7d avg +0.010%, OI rising.
- Projected net carry: 3.1% (staking) + 13% (funding) − ~2% (all-in costs) ≈ **14.1% APR**, clears the risk-free (~4.5%) + 3% hurdle.

**Entry:**

1. Hold $50,000 stETH (already staked; earns 3.1% via rebasing).
2. Short ~15.6 ETH perp on Hyperliquid at $3,205 with $30,000 isolated USDC margin (~1.7x), delta ≈ 0.
3. Verify: long 15.6 ETH-equivalent (stETH), short 15.6 ETH perp. Net delta ≈ 0.

**Hold (30 days):**

- Staking income: 3.1%/12 × $50,000 ≈ **$129**.
- Funding income: ~0.011%/8h × $50,000 × 90 periods ≈ **$495**.
- Price moves cancel (stETH long vs ETH short); residual basis P&L ≈ ±$10.
- Re-hedged twice on 2%+ delta drift; gas + slippage ≈ **$18**.

**Exit (day 30):** Funding compresses to +0.004%/8h but staking still carries the trade; hold. If instead funding had gone negative below the staking yield, close the perp short and either unstake or convert to a plain stablecoin loan.

**Net for the month: ~$129 + $495 − $18 fees ≈ $606 on $50,000 ≈ 14.5% annualised**, market-neutral. In 2021-style regimes with 0.05%/8h funding this pushes toward 30%+; post-Ethena, 8-15% is the realistic band.

## Performance characteristics

Cost-corrected picture (2024-2026 regime):

| Metric | Value | Note |
|---|---|---|
| Net APY on capital | 6-15% | Was 20-40% pre-Ethena. Regime-dependent. |
| Sharpe (target) | 1.3 | Collapses toward 0 in funding inversions / depeg events. |
| Max drawdown (sleeve) | 8-12% | Driven by depeg + funding-flip + basis events, not price. |
| Win rate (per funding period) | 80-92% | Most periods positive; tails dominate losses. |
| Breakeven cost budget | ~15 bps per held period | Spread + taker fees + gas + rebalance slippage. |
| Capital efficiency | ~50-65% | Yield leg + perp margin ≈ 1.5-2x outlay per $1 of hedged yield. |

**Realistic cost overlay (never assume naive):**
- Perp round-trip (maker/taker mix): ~4-8 bps.
- Yield-leg entry/exit: LST mint/redeem spread ~2-10 bps; LP entry + IL on non-correlated pairs (immaterial for stETH/ETH, material for volatile pairs).
- Delta re-hedge: ~1-2 bps/day when drift > 2%.
- Gas: $1-20 per DeFi tx (batching essential for smaller sleeves).
- Funding drag: whenever funding is negative, it subtracts directly from staking yield.
- Slippage: <2 bps on ETH majors; 10-30 bps on smaller LSTs/perps.

A naive backtest that counts staking APR + positive funding and ignores negative-funding drag, LST redemption spreads, and depeg tail losses overstates net yield by roughly 30-50%.

## Capacity limits

Bounded by the *long-side willingness to pay funding* plus LST redemption depth:

- **Per LST/perp on a single venue:** ~$10-50M before short-side stacking compresses funding against the farm itself.
- **Aggregate:** [[ethena-usde|Ethena]] at $14.8B TVL is the real-world ceiling demonstration — at that scale USDe's hedge inventory measurably compressed BTC/ETH funding on every major venue.
- **For an individual operator:** **$25k-$25M** is a workable band, above which LST redemption queues and perp OI depth become the binding constraint. Beyond that you are effectively running a synthetic-dollar protocol.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Crowding (#4).** The dominant secular risk. Ethena, Resolv, and Pendle industrialised the hedged-yield trade; sUSDe yield fell from ~19% (2024) to ~5% (2025). The trade is not dead but the reward has compressed.
2. **Regime change / funding inversion (#5).** In bear markets funding goes negative and *drains* the staking yield. 2025-10-10 is the canonical case: funding to zero/negative within hours, $5.7B redeemed from USDe in a month.
3. **LST depeg / basis blowup (#6).** The long leg is *not* the perp's underlying — stETH is not ETH. A staking-withdrawal jam or protocol scare (June 2022 stETH to ~0.94) breaks the hedge: the LST falls while the perp underlying does not, producing a one-sided loss on a "neutral" book.
4. **Smart-contract exploit (#7).** The yield leg lives in a contract (Lido, EigenLayer, a Curve pool). An exploit can zero the long leg while the short still owes margin.
5. **Liquidation on the short.** A violent upward rip plus rebalance latency can chew the short's margin buffer; if it liquidates, the hedge breaks at the worst moment.
6. **Perp-venue counterparty failure.** [[ftx]]-style insolvency or withdrawal halt on the hedge venue leaves the long leg naked.
7. **Stablecoin/margin depeg.** USDT/USDC-margined shorts become a hidden directional bet if the margin stablecoin depegs.

## Kill criteria

Pause (not retire) the sleeve on any of:

1. **7d funding average < 0 AND staking/LP yield < |funding drag|** on more than half of held legs.
2. **LST/LP depeg > 2%** from underlying, not recovered within 24h.
3. **Sleeve drawdown > 12%** in any rolling 30-day window.
4. **Net hedged yield < risk-free stablecoin rate for 30+ days** — regime confirmation the edge is arb'd out.
5. **Perp-venue insurance-fund socialised loss, or withdrawal halt > 4h** on any leg.
6. **Yield-leg protocol exploit or emergency-pause** event.

Re-deploy when all clear and projected net carry again clears risk-free + 300 bps on ≥ 2 eligible legs. Like [[funding-rate-arbitrage]], this is a *pause-able* strategy: the mechanism (staking + funding) does not vanish, only the rate level does. See [[when-to-retire-a-strategy]].

## Advantages

- **Market-neutral yield.** Decouples return from crypto price direction — the profile institutions and risk-averse allocators want.
- **Two structural cash-flows.** Staking yield *and* funding, either of which can carry the trade if the other compresses.
- **Predictable income.** Funding pays every 1-8h; staking rebases continuously.
- **Transparent inputs.** Funding, staking APR, and LST peg are all publicly observable in real time.
- **Battle-tested at scale.** [[ethena-usde]] proves the construction works into the billions.
- **Composable.** The stablecoin margin and idle collateral can be lent for an additional risk-free-ish layer (see [[crypto-yield-stack]]).

## Disadvantages

- **Two-leg operational complexity.** Yield leg + perp hedge + rebalancing + withdrawal management; a bug in any layer is live-fire risk.
- **LST ≠ underlying.** Basis and depeg risk on the long leg is the signature failure mode and is *not* present in plain [[funding-rate-arbitrage]].
- **Capital-intensive.** ~1.5-2x capital outlay per dollar of hedged yield.
- **Funding can flip negative fast**, converting the hedge from income to drag.
- **Smart-contract + counterparty risk** on every venue and protocol touched.
- **Edge decay.** Documented and ongoing via Ethena/Resolv/Pendle.
- **Tax complexity.** Staking rewards, funding, and perp P&L are often taxed differently; headline net APY overstates after-tax return.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (2023). Documents crypto carry averaging above 10% annually; the funding leg's theoretical basis. https://www.bis.org/publ/work1087.pdf
- He, Manela, Xu, Yan, *Fundamentals of Perpetual Futures* (2022/2024), Wharton/WashU. Perp-vs-index deviation and carry Sharpe estimates. arxiv.org/abs/2212.06888
- [[ethena-usde|Ethena]] official documentation — synthetic-dollar architecture (staked-ETH/BTC long + equivalent perp short). docs.ethena.fi
- CoinMetrics, *State of the Network* Issue 335, "Ethena and the Mechanics of USDe" — Tanay Ved (2024). Walk-through of the industrialised hedged-yield trade and its yield compression.
- Lido / EigenLayer documentation — stETH rebasing mechanics and restaking yield/slashing model (yield-leg mechanics; see [[liquid-staking]], [[eth-staking]]).
- June 2022 stETH depeg (~0.94 low) — the canonical LST-vs-underlying basis event; see [[2022-06-steth-depeg]].
- AMBCrypto / DLNews coverage of the 2025-10-10 funding crash — $5.7B USDe outflows in October 2025, TVL from $14.8B to $7.6B; concrete record of hedged-yield decay in a regime flip.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — cross-exchange funding (the hedge-leg income signal)
- `GET /api/v1/derivatives/open-interest?coin=ETH` — cross-exchange OI (confirms real long flow)
- `GET /api/v1/hyperliquid/funding-rates?coin=ETH` — Hyperliquid perp funding (hourly)
- `GET /api/v1/sentiment/stablecoins` — stablecoin mcap + flows (risk-free demand / dry powder context)
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score (yield-leg tail-risk monitor)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ETHUSDT&limit=500` — funding history for carry backtests
- `GET /api/v1/backtesting/funding` — deep funding archive
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=365` — ETH price for delta-hedge modelling

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-sentiment]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Hedge-income leg** — `GET /api/v1/derivatives/funding-rates?coin=ETH` + `GET /api/v1/hyperliquid/funding-rates?coin=ETH` — short-perp funding is half the yield stack; HL's hourly cadence re-prices fastest
- **Flow confirm** — `GET /api/v1/derivatives/open-interest?coin=ETH` — verify real long flow sits behind positive funding before relying on the carry
- **Tail monitor** — `GET /api/v1/security/regime` — exploit/depeg stress on the yield leg
- **Backtest** — `GET /api/v1/backtesting/funding` — Hyperliquid hourly since 2023-05 (Binance daily since 2026-03-30) covers the carry leg honestly; ETH price paths for delta-drift modelling from `GET /api/v1/backtesting/klines` (daily back to 2017-08)
- **Tips** — the position is only neutral between rebalances: schedule delta checks on funding settlement boundaries, and treat sustained negative funding as a regime change (exit trigger), not noise

## Related

- [[funding-rate-arbitrage]] — the plain-spot-long ancestor of this trade.
- [[funding-rate]] / [[perpetual-futures]] — the hedge-leg mechanism.
- [[delta-neutral]] / [[basis]] / [[cash-and-carry]] — the hedging principle and basis-trade family.
- [[ethena-usde]] — the largest live implementation and primary alpha-decay agent.
- [[crypto-yield-stack]] — the directional (un-hedged) cousin that layers yields without a perp short.
- [[liquid-staking]] / [[eth-staking]] — the yield-leg mechanics and depeg risk.
- [[stablecoin-yield]] — the risk-free hurdle the trade must beat.
- [[liquidation-risk]] — what breaks the hedge on the short leg.
- [[edge-taxonomy]] — where this strategy sits among the six edge categories.
- [[failure-modes]] / [[when-to-retire-a-strategy]] — kill-criteria methodology.
