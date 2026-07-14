---
title: "Staking Yield Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [arbitrage, crypto, defi, staking, liquid-staking, funding-rate, delta-neutral, restaking, leverage]
aliases: ["Staking Arb", "LST Basis Trade", "Staking-vs-Borrow Carry", "DeFi Yield Arb"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, risk-bearing, behavioral]
edge_mechanism: "Liquid-staking tokens yield the consensus/restaking reward, but ETH can be borrowed for less. The arbitrageur loops LST collateral against borrowed ETH to lever the staking-minus-borrow spread, or hedges LST spot with a short perp to isolate the yield. The counterparty is the leverage-hungry LST holder (who bids the borrow rate) and the market's refusal to bear LST depeg / liquidation / smart-contract tail risk — which is exactly what the arb is paid to absorb."

# Data and infrastructure requirements
data_required: [lst-eth-price, staking-yield, defi-borrow-rate, perp-funding-rate, lending-pool-liquidity, gas-price]
min_capital_usd: 10000
capacity_usd: 200000000
crowding_risk: high

# Performance expectations (net of gas, borrow-rate drift, and depeg risk)
expected_sharpe: 1.2
expected_max_drawdown: 0.15
breakeven_cost_bps: 30

# Decay history
decay_evidence: "The stETH/ETH staking-minus-borrow spread compressed as looping was industrialised: Aave's ETH borrow rate tracks looping demand and repeatedly spikes toward (and briefly above) the stETH staking yield, collapsing net carry to near zero on the majors. EigenLayer restaking (peaked ~$15B+ TVL, 2024) pulled forward and then compressed restaking yields as points/airdrop incentives normalised. LST discounts that were 5-7% in June 2022 (Terra/3AC deleverage) are now typically <30 bps outside stress — the fat convergence profits are episodic, not standing."

# Lifecycle
kill_criteria: |
  - staking yield minus DeFi borrow rate turns negative on the looped asset for > 3 consecutive days
  - LST discount to underlying widens past the position's liquidation buffer
  - protocol exploit, governance attack, or > 25% TVL outflow on any leg's protocol
  - perp funding (delta-neutral variant) averages negative and exceeds staking yield for 3+ days

related: ["[[lst-depeg-arbitrage]]", "[[restaking-token-arbitrage]]", "[[funding-rate-arbitrage]]", "[[pendle-pt-yt-arbitrage]]", "[[babylon-bitcoin-staking-arbitrage]]", "[[liquid-staking]]", "[[aave]]", "[[defi]]", "[[delta-neutral]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Staking Yield Arbitrage

Staking yield arbitrage harvests the spread between what a [[liquid-staking|liquid-staking token]] (LST) *earns* and what its underlying asset *costs to borrow or hedge*. The canonical, buildable form is the **staking-vs-borrow carry loop**: deposit an LST (stETH, rETH, weETH) as collateral, borrow ETH against it below the staking yield, buy more LST, and repeat — levering the `staking_yield − borrow_rate` spread. Two adjacent forms share the same data rails: the **LST basis / depeg-convergence trade** (buy the LST at a discount to its redemption value and earn the convergence plus base yield), and the **delta-neutral staking trade** (stake ETH, short an equal-notional [[perpetual-futures|perp]] to strip out price risk, keeping staking yield ± funding). All three are market-neutral in spirit but carry a sharp left tail: when the borrow rate spikes above the staking yield, or the LST depegs and triggers a liquidation cascade, the "safe carry" inverts violently.

## Edge source

Mapping to [[edge-taxonomy]], staking yield arbitrage is **structural + risk-bearing + behavioural**:

- **Structural.** LSTs pay a protocol-hardcoded reward (Ethereum consensus issuance + priority fees + restaking points); ETH can be borrowed from a lending market at a utilisation-driven rate that is *usually* below that reward. The gap is a mechanical property of two separate rate-setting systems (consensus vs lending utilisation) that do not have to agree.
- **Risk-bearing.** The looper is *paid* to absorb the risks the passive LST holder will not: LST depeg, forced liquidation if collateral value drops through the loan-to-value threshold, staking slashing (amplified by restaking), and smart-contract failure on the LST, the lending market, and any restaking layer. The standing spread is compensation for that stacked tail, not a free lunch.
- **Behavioural.** Leverage-hungry LST holders bid the borrow rate up because they want convex, levered staking exposure — the same leverage-preference bias that drives [[funding-rate-arbitrage|perp funding]]. The arb sits on the other side of that demand.

It is **not** an informational or analytical edge — every rate is on-chain and public. The edge is the operational capability to run the loop with disciplined LTV/liquidation management and to size for the depeg tail.

## Why this edge exists

- **Two rate systems, no arbitrage-forcing link.** Consensus issuance sets the LST yield; lending-pool utilisation sets the borrow rate. Nothing forces `borrow_rate ≤ staking_yield` at every instant — when looping demand surges, utilisation and the borrow rate spike, sometimes above the yield.
- **Leverage demand from LST holders.** Holders want to lever staking returns; each new looper adds borrow demand, pushing the rate up until the spread compresses. The spread is the market clearing the supply of "someone willing to bear the levered tail."
- **Depeg convergence is structurally anchored (once withdrawals exist).** Post-Shapella (April 2023), stETH is redeemable 1:1 for ETH through the validator exit queue, so a discount *must* converge — but only on the queue's timescale (hours to weeks), during which the holder bears price and liquidity risk. Pre-withdrawal LSTs had no such anchor, which is why the June 2022 stETH discount blew out to 5-7%.
- **Why it does not fully close.** Bearing the depeg + liquidation + smart-contract + slashing stack is genuinely risky and genuinely industrialised (Aave loops, Ethena-style hedged dollars, Pendle yield tokenisation). Capital floods in until the net spread barely compensates the tail — and then a stress event periodically clears out the under-hedged, resetting the spread wide.

## Null hypothesis

Under efficient, frictionless yield markets, capital flows until every comparable-risk yield source pays the same risk-adjusted rate and the strategy earns nothing after costs and a fair risk premium. Concretely, under the null:

- `staking_yield − borrow_rate ≈ 0` after adjusting for the depeg/liquidation/smart-contract risk premium; the loop earns only fair compensation for tail risk, not excess return.
- LST trades within a tight band of redemption value (≤ a few bps outside stress); any discount equals the carrying cost over the withdrawal-queue horizon.
- Delta-neutral staking earns `staking_yield − funding`, which nets to roughly the risk-free rate plus a thin premium.

The empirical record partially confirms the null (standing spreads are thin and periodically negative on the majors) and partially fails it (episodic depeg discounts of 1-7% and restaking-incentive windows produced large, real excess returns). **If the levered loop's net carry is indistinguishable from the ETH risk-free/borrow rate for 30+ days, the standing spread has been arbed into the null and the position should be de-levered to a depeg-convergence-only posture (wait for the next stress dislocation).**

## Rules

### Entry conditions

1. **Positive net carry gate (loop).** `staking_yield − borrow_rate ≥ carry_floor`, with `carry_floor ≥ 150 bps annualised` at the chosen leverage after gas amortisation — thin spreads do not justify the liquidation tail.
2. **Depeg entry (basis variant).** Enter the buy-the-discount trade when the LST trades **≥ 50-100 bps below redemption value** with a functioning withdrawal queue; size for the discount to widen further before it converges.
3. **Liquidation buffer.** Set leverage so the position survives a **≥ 5% adverse LST/ETH move** (empirically the depeg magnitude to plan for) without hitting the lending-market liquidation threshold. On stETH/ETH E-Mode this means materially below the max LTV.
4. **Funding gate (delta-neutral variant).** Only run stake-and-short-perp when `staking_yield − |negative_funding| > 0` and funding is not persistently negative; monitor daily.
5. **Protocol health.** No active exploit, governance attack, oracle anomaly, or > 25% TVL outflow on the LST, lending market, or restaking layer; withdrawal queue functioning.

### Exit conditions

1. **Carry inversion.** `borrow_rate > staking_yield` for > 3 consecutive days on the looped asset — de-lever immediately; negative carry compounds against you.
2. **Depeg convergence (basis variant).** LST discount narrows to < 10 bps or flips to premium — sell and realise the convergence + accrued yield.
3. **Liquidation-buffer breach.** LST/ETH moves toward the liquidation threshold — de-lever *before* the protocol does it for you at a worse price.
4. **Funding flip (delta-neutral variant).** Perp funding averages negative and exceeds staking yield for 3+ days — the short leg now costs more than the stake earns; close.
5. **Protocol-risk escalation.** Exploit, governance attack, or large TVL flight on any leg — exit that leg first, then the hedge.

### Position sizing

- **Leverage.** Choose loop leverage from the liquidation-buffer rule, not the maximum LTV. A typical stETH/ETH loop runs ~3-5× effective, well inside the ~93% E-Mode LTV, to survive a 5% depeg.
- **Per-protocol cap.** ≤ 20-25% of book in any single LST, lending market, or restaking protocol — smart-contract risk is the dominant tail and must be diversified.
- **Gas-aware minimum.** Below ~$10k, Ethereum L1 gas on entry/loop/rebalance/exit erodes the carry; use an L2 LST market or larger size.

## Implementation pseudocode

```python
# staking_yield_arb.py — staking-vs-borrow loop with liquidation-buffer discipline
CARRY_FLOOR_APY   = 0.015     # 150 bps min net carry after gas, else don't lever
DEPEG_ENTRY_BPS   = 75.0      # buy the LST discount at >= 75 bps below redemption
DEPEG_EXIT_BPS    = 10.0      # realise convergence under 10 bps
DEPEG_BUFFER      = 0.05      # position must survive a 5% adverse LST/ETH move
MAX_PER_PROTOCOL  = 0.25      # 25% book cap per protocol (smart-contract tail)
CARRY_INV_DAYS    = 3         # de-lever after 3 days of negative carry

def loop_leverage(max_ltv: float, buffer: float) -> float:
    # pick target LTV so a `buffer` drop in collateral value stays below liquidation LTV
    target_ltv = max_ltv * (1 - buffer) - 0.02      # extra safety margin
    return 1 / (1 - target_ltv)                      # effective leverage from geometric loop

def decide(mkt, pos, book) -> dict:
    # mkt: {staking_yield, borrow_rate, lst_discount_bps, lst_eth_move, max_ltv,
    #       funding_apy, protocol_ok, neg_carry_days}
    if not mkt.protocol_ok:
        return {"action": "EXIT_ALL", "reason": "protocol risk flag"}

    # ---- levered carry loop ----
    net_carry = mkt.staking_yield - mkt.borrow_rate
    if pos and pos.kind == "loop":
        if mkt.neg_carry_days >= CARRY_INV_DAYS:
            return {"action": "DELEVER", "reason": "carry inverted"}
        if mkt.lst_eth_move <= -DEPEG_BUFFER * 0.8:              # approaching buffer
            return {"action": "DELEVER", "reason": "liquidation buffer at risk"}
        return {"action": "HOLD"}
    if net_carry >= CARRY_FLOOR_APY:
        lev = loop_leverage(mkt.max_ltv, DEPEG_BUFFER)
        if book["protocol_exposure"] + 1 <= MAX_PER_PROTOCOL * book["capital"]:
            return {"action": "OPEN_LOOP", "leverage": round(lev, 2),
                    "reason": f"net carry {net_carry*100:.2f}% APY"}

    # ---- depeg / basis convergence (unlevered or lightly levered) ----
    if pos and pos.kind == "basis":
        if mkt.lst_discount_bps <= DEPEG_EXIT_BPS:
            return {"action": "SELL_LST", "reason": "discount converged"}
        return {"action": "HOLD"}
    if mkt.lst_discount_bps >= DEPEG_ENTRY_BPS:
        return {"action": "BUY_DISCOUNT", "reason": f"LST {mkt.lst_discount_bps:.0f}bps below redemption"}

    return {"action": "WAIT", "reason": "no qualifying spread"}
```

The production version wraps this with: on-chain LTV/health-factor monitoring (auto-delever before the protocol liquidates), a withdrawal-queue tracker for the convergence horizon, gas-aware batching of the loop, and a per-protocol exposure ledger. For the delta-neutral variant, add the perp leg and a funding-flip monitor (shared with [[funding-rate-arbitrage]]).

## Indicators / data used

- **LST/underlying price (stETH/ETH, weETH/ETH)** — the depeg signal and the collateral-value input for liquidation risk.
- **Staking / restaking yield** — the income side; consensus issuance + priority fees + restaking points.
- **DeFi borrow rate (Aave/Morpho ETH)** — the cost side; utilisation-driven and the key mean-reverting risk.
- **Lending-market LTV / liquidation threshold** — sets safe leverage.
- **Perp [[funding-rate]] (delta-neutral variant)** — the hedge cost; shared rail with [[funding-rate-arbitrage]].
- **Lending-pool + LST-pool liquidity** — caps size and governs unwind slippage in a rush.
- **Gas price** — determines the minimum economic ticket and rebalance cadence.
- **Sources** — on-chain protocol data (Lido, Aave, EigenLayer), [[pendle-pt-yt-arbitrage|Pendle]] implied yields, plus cryptodataapi.com for funding, a CEX borrow-rate proxy, and LST/ETH DEX price.

## Example trade

**Setup (illustrative, stETH/ETH loop, 2026-05):**

- stETH staking + restaking yield: **3.8% APY**. Aave ETH borrow rate: **2.6% APY**. Net carry: **1.2%** per unit of borrowed ETH.
- stETH/ETH E-Mode max LTV: 93%. Buffer rule (survive 5% depeg): target LTV ≈ 88% → effective leverage ≈ **8.3×** (we cap at 5× for extra depeg headroom).
- Capital: $50,000; single-protocol cap 25% respected (this is the only LST loop in book).

**Levered loop, 5× effective on $50k → $250k stETH exposure, $200k borrowed ETH:**

| Line | Annualised on $50k equity |
|---|---|
| Staking/restaking yield on $250k @ 3.8% | +$9,500 |
| Borrow cost on $200k @ 2.6% | −$5,200 |
| Gross levered carry | +$4,300 (**8.6% on equity**) |
| Gas (entry loop ~6 tx + monthly rebalance, L1 ~$25/tx amortised) | −$300 |
| **Net carry** | **~$4,000 ≈ 8.0% APY on equity** |

**The realistic tail (why this is not risk-free):**
- If Aave ETH borrow rate spikes to **4.0%** (a routine looping-demand event), gross carry inverts to `3.8% − 4.0% = −0.2%` × 5× = **−1.0% on equity** plus gas — the position now bleeds until you de-lever.
- If stETH depegs **3%** (a 3AC/June-2022-style deleverage), the $250k collateral drops $7,500, pushing the health factor toward liquidation; the auto-delever sells stETH *into* the discount, crystallising a real loss far larger than a year of carry.

**Depeg-convergence alternative (unlevered):** buy 100 stETH at a 1.5% discount (98.5 ETH cost), earn ~3.8% base yield, and realise ~1.5% convergence when the discount closes over the following weeks → ~5.3% blended over the hold with a much smaller left tail (no liquidation vector). The honest cost-corrected takeaway: **the standing levered spread (~1-1.5% net) barely pays for the liquidation tail, so most of the durable money is in the episodic depeg-convergence trade, not the always-on loop.**

## Performance characteristics

Cost-corrected picture (2024-2026):

| Metric | Value | Note |
|---|---|---|
| Net standing carry (levered loop, majors) | 0-3% on equity | Thin; periodically negative when borrow spikes. |
| Depeg-convergence return (episodic) | 1-7% per event + base yield | Where the durable excess return concentrates. |
| Delta-neutral staking (stake + short perp) | staking_yield ± funding | Roughly risk-free-plus in calm; negative when funding inverts. |
| Sharpe (target, blended) | 1.2 | Carry-like body with a fat left tail; not a smooth 3.0. |
| Max drawdown | 10-15% | Driven by depeg + forced liquidation, not directional price. |
| Win rate (per position) | 80-90% | Losses are rare but large (the tail dominates the loss distribution). |
| Breakeven cost budget | ~30 bps round-trip | Gas (loop/rebalance/exit) + swap slippage on entry/exit. |

**Costs the naive version ignores:** (1) **borrow-rate drift** — the borrow leg is *floating*, not fixed, and mean-reverts up toward the yield exactly when looping is crowded; (2) **forced-liquidation slippage** — an auto-delever sells into the same depeg that triggered it, at the worst price; (3) **stacked smart-contract risk** — LST + lending market + restaking layer, each a potential total loss; (4) **L1 gas** — the loop is many transactions, punishing sub-$10k tickets; (5) **slashing tail** — restaking multiplies the slashing surface.

## Capacity limits

- **stETH/rETH/weETH loops:** bounded by lending-market ETH liquidity — Aave ETH markets support hundreds of millions, but the *net carry* compresses as looping utilisation rises, so effective capacity before the spread vanishes is lower than raw liquidity suggests.
- **Depeg-convergence:** bounded by the size of the discount and LST-pool depth at the moment of stress — episodic, tens to low-hundreds of $M in a real deleveraging event.
- **Delta-neutral staking:** bounded by perp OI / funding capacity (shared with [[funding-rate-arbitrage]]) — tens to hundreds of $M on ETH.

Aggregate strategy capacity is large in dollars (the LST market is tens of $B) but the *arb-specific* capacity — the amount that can earn positive net carry before it competes the spread to zero — is much smaller and is what EigenLayer/Aave-loop industrialisation already largely consumed. Working capacity for an individual operator: **$10k-$5M**, above which liquidation-management and unwind slippage dominate.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Carry inversion / crowding (Failure Mode #4).** As looping industrialised, the borrow rate rose to meet the staking yield, compressing net carry toward (and past) zero on the majors. The standing loop is the most crowded, lowest-margin version.
2. **LST depeg + forced liquidation (Failure Mode #6, the dominant tail).** The June 2022 stETH 5-7% discount and the recurring 3AC/FTX-era deleverages are the templates: a discount widens, levered positions breach their liquidation threshold, forced sales deepen the discount, cascade. This is how a "safe carry" becomes a large loss.
3. **Smart-contract / slashing failure (Failure Mode #6).** LST, lending market, and restaking layer each carry exploit and (for restaking) slashing risk; the loop stacks all three.
4. **Funding inversion (delta-neutral variant).** The stake-and-short trade turns negative when perp funding flips persistently negative (e.g. the Nov-2022 FTX crash), as documented in [[funding-rate-arbitrage]].
5. **Withdrawal-queue congestion (Failure Mode #7).** A long validator-exit queue delays convergence and traps capital exactly when you want out.
6. **Regulatory reclassification.** Staking-as-a-service and LSTs face securities-classification uncertainty in several jurisdictions; an adverse ruling can force protocol/geography changes.

## Kill criteria

Pause or de-lever on any of:

1. **`staking_yield − borrow_rate < 0` for > 3 consecutive days** on the looped asset — de-lever to convergence-only posture.
2. **LST discount widens past the position's liquidation buffer** — de-lever before the protocol liquidates you.
3. **Protocol exploit, governance attack, or > 25% TVL outflow** on any leg's protocol — exit that leg.
4. **Perp funding (delta-neutral variant) averages negative and exceeds staking yield for 3+ days** — close the hedged-stake trade.
5. **Withdrawal queue non-functional or > 4-week backlog** — do not enter new convergence trades until it clears.

Re-deploy: net carry back above the 150 bps floor with a functioning withdrawal queue, or a fresh depeg ≥ 50-100 bps for the convergence trade. See [[when-to-retire-a-strategy]] — the *mechanism* (two rate systems + leverage demand) does not disappear, so this is pause-able; the always-on loop is the part most prone to null, the episodic depeg trade the part most worth keeping ready.

## Advantages

- **Multiple related expressions** — levered carry, depeg convergence, and delta-neutral staking share one data stack and can be rotated by regime.
- **Structural depeg convergence (post-Shapella).** Redeemable LSTs must converge to underlying, giving the basis trade a real anchor absent in pre-withdrawal designs.
- **Delta-neutral variant strips price risk** — earn staking yield with the ETH exposure hedged by a short perp.
- **Composable and transparent** — every rate and price is on-chain and publicly observable; no KYC for the DeFi legs.
- **Yields can stack** — stake → restake → use the receipt as collateral, for genuinely higher (if riskier) gross yield.

## Disadvantages

- **Floating borrow leg.** The cost side is not fixed; it rises toward the yield precisely when the trade is crowded, and can invert the carry.
- **Depeg + liquidation tail.** The signature failure mode: a discount cascades levered positions into forced liquidation at the worst price.
- **Stacked smart-contract risk.** LST + lending + restaking, each an exploit surface; diversification is mandatory but imperfect.
- **Gas-inefficient at small size.** The loop is many L1 transactions; sub-$10k tickets bleed to gas.
- **Slashing risk (restaking).** Multiplies the operational tail beyond base staking.
- **Yield compression / crowding.** Industrialisation (EigenLayer, Aave loops, Pendle) has already competed the standing spread thin.
- **Regulatory uncertainty** around staking income classification.

## Sources

- stETH depeg (June 2022) — Terra/Luna collapse + [[three-arrows-capital|Three Arrows]] deleverage drove stETH to a 5-7% discount to ETH; the canonical depeg-convergence and forced-liquidation case study. Recovered over subsequent months.
- Ethereum Shapella upgrade (April 2023) — enabled validator withdrawals, giving stETH a hard 1:1 redemption anchor and structurally bounding future discounts (the reason post-2023 depegs are shallower and faster to converge).
- EigenLayer restaking boom (2024) — peaked ~$15B+ restaked ETH; additional restaking yield (points/AVS) on top of base staking drew massive capital and then compressed as incentives normalised. See [[restaking-token-arbitrage]].
- Aave / Morpho ETH lending-market mechanics — utilisation-driven floating borrow rates and stETH/ETH E-Mode LTVs; the borrow-rate leg and liquidation-threshold inputs.
- Delta-neutral basis blow-ups (Nov 2022, FTX crash) — funding flipped negative as the market crashed, turning hedged-stake positions into losses; shared failure mode with [[funding-rate-arbitrage]].
- [[pendle-pt-yt-arbitrage|Pendle]] — tokenises LST/restaking future yield, providing an implied-yield reference and a fixed-rate alternative to the floating loop.

## Getting the Data (CryptoDataAPI)

Native ETH staking yields and DeFi (Aave/Morpho) borrow rates come from on-chain protocol reads, not CryptoDataAPI. Use CryptoDataAPI for the **perp funding leg (delta-neutral variant)**, a **CEX borrow-rate proxy**, and the **LST/ETH DEX price** that signals depeg.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — cross-exchange ETH perp funding (delta-neutral hedge cost)
- `GET /api/v1/market-intelligence/borrow-interest` — margin borrow rate (BTC/Binance) as a CEX borrow-cost proxy
- `GET /api/v1/dex/token/{chain}/{address}` — LST pool price on a DEX (e.g. stETH/ETH Curve pool) → depeg signal
- `GET /api/v1/liquidity/depth` — per-coin depth/spread (unwind-slippage gate for the LST leg)

**Historical / research:**
- `GET /api/v1/backtesting/funding` — deep funding archive (delta-neutral carry backtest)
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ETHUSDT&limit=500` — ETH funding history
- `GET /api/v1/backtesting/klines` — OHLCV archive for LST/ETH basis studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/borrow-interest"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-dex]].

## Related

- [[lst-depeg-arbitrage]] — the pure depeg-convergence sibling in detail.
- [[restaking-token-arbitrage]] — the restaking-yield-stacking extension (EigenLayer/Symbiotic).
- [[funding-rate-arbitrage]] — the perp-funding leg of the delta-neutral variant; shared failure modes.
- [[pendle-pt-yt-arbitrage]] — fixed-vs-floating yield tokenisation over the same LST cash flows.
- [[babylon-bitcoin-staking-arbitrage]] — the BTC-staking analogue.
- [[liquid-staking]] — the LST infrastructure (Lido, Rocket Pool, EtherFi) that enables the trade.
- [[aave]] — the lending market for the borrow leg.
- [[delta-neutral]] — the hedging principle behind the stake-and-short variant.
- [[defi]] — the ecosystem context.
- [[edge-taxonomy]] — structural + risk-bearing + behavioural edge categories.
- [[failure-modes]] — the kill-criteria source taxonomy.
- [[when-to-retire-a-strategy]] — pause-vs-retire framework.
