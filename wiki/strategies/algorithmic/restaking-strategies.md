---
title: "Restaking Strategies"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [crypto, defi, restaking, eigenlayer, staking, liquid-staking, avs, ethereum, yield, lrt, slashing]
aliases: ["Restaking", "EigenLayer Strategies", "Liquid Restaking", "LRT Strategies"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced

backtest_status: untested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [risk-bearing, structural, informational]
edge_mechanism: "AVSs and LRT protocols pay a yield to whoever will pledge already-staked ETH as slashable economic security they cannot bootstrap themselves; the restaker is paid a risk premium for bearing slashing, LRT-depeg, withdrawal-queue, and stacked smart-contract risk that passive stakers refuse to hold."

# Data and infrastructure requirements
data_required: [eth-price, lrt-price, lrt-eth-peg, avs-reward-rate, staking-yield, tvl, withdrawal-queue, borrow-rate]
min_capital_usd: 2000
capacity_usd: 500000000
crowding_risk: high

# Performance expectations (net of gas, depeg risk, and slashing haircut)
expected_sharpe: 0.9
expected_max_drawdown: 0.35
breakeven_cost_bps: 40

# Decay history
decay_evidence: "EigenLayer restaking points/APR fell sharply after the EIGEN TGE (Oct 2024) and as TVL diluted a roughly fixed AVS reward pool; ether.fi/Renzo/Kelp LRT native yields compressed from double-digit points-era implied APRs to low-single-digit base+AVS yield by 2025. Renzo ezETH depegged to ~$0.69 on 2024-04-24, cascading ~$60M+ of leveraged-loop liquidations."

# Kill criteria (numeric — see [[when-to-retire-a-strategy]])
kill_criteria: |
  - net AVS yield (after expected slashing loss) < base ETH staking yield for 30+ days
  - LRT/ETH secondary-market peg deviation > 2%
  - any confirmed AVS slashing event touching a delegated operator
  - LRT protocol changes slashing/operator parameters or pauses withdrawals
  - leverage-loop health factor < 1.15 on any position

related: ["[[defi-yield-farming]]", "[[points-farming]]", "[[airdrop-farming]]", "[[leveraged-yield-farming]]", "[[staking]]", "[[eigenlayer]]", "[[ethereum]]", "[[lido]]", "[[ethena-usde]]", "[[aave]]", "[[expected-value]]", "[[kelly-criterion]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Restaking Strategies

Restaking takes already-staked ETH — or a liquid staking token like stETH/rETH — and re-pledges it through [[eigenlayer]] to secure additional protocols (Actively Validated Services, or AVSs) in exchange for a layered yield on the same capital. In practice most operators hold a **Liquid Restaking Token (LRT)** — eETH (ether.fi), ezETH (Renzo), pufETH (Puffer), rsETH (Kelp) — which keeps the restaked position liquid and composable so it can be looped as collateral. The strategy is a **risk-premium harvest, not an arbitrage**: the extra yield is compensation for bearing slashing, LRT-depeg, withdrawal-queue, and stacked smart-contract risk. Since EigenLayer's slashing/redistribution went live in 2025, that risk is no longer theoretical.

## Edge source

Mapping to [[edge-taxonomy]], restaking is a hybrid:

- **Risk-bearing (primary).** AVSs need slashable economic security they cannot cheaply bootstrap. Restakers rent their staked-ETH's security and are paid for accepting that their principal can be slashed if a delegated operator misbehaves. This is an insurance-underwriting premium, in the same family as [[ethena-usde|Ethena]] being paid to hold basis risk.
- **Structural (secondary).** The same ETH earns base consensus rewards *and* AVS rewards *and* (via an LRT) can be used as DeFi collateral — three yield layers stacked on one unit of capital because the instrument is designed to be rehypothecable.
- **Informational (tertiary).** Choosing *which* AVSs and operators to delegate to, and *which* LRT will convert its [[points-farming|points]] into the most valuable airdrop, is an information/selection edge — early, well-researched restakers captured EIGEN, ETHFI, REZ, and similar distributions.

There is **no latency or analytical pricing edge** — restaking APRs are published. The edge is being willing and operationally able to hold layered tail risk that passive stakers avoid.

## Why this edge exists / who's on the other side

- **AVSs** (data-availability layers, oracles, bridges, coprocessors) pay rewards because renting EigenLayer security is cheaper than launching their own token and bootstrapping a validator set. They are the natural yield payer.
- **LRT protocols** subsidise headline APRs with their own token emissions and points to win TVL market-share, pulling forward yield that later dilutes.
- **Leverage loopers** who mint an LRT and lever it on [[aave]] are forced buyers of LRT and provide exit liquidity — and are the first to be liquidated in a depeg, handing disciplined restakers a cheaper entry.
- **Later token buyers** absorb the LRT/AVS tokens farmers distributed to.

The restaker sits on the paid side of an economic-security rental market. The counterparties are paying for security, market-share, or convex exposure they cannot otherwise obtain.

## Null hypothesis

Under no edge, restaking yield equals plain ETH staking yield and every extra layer is exactly offset by its expected loss:

- Net AVS reward ≈ 0 after subtracting expected slashing loss and token-emission dilution.
- LRT native APR converges to base staking APR once points/airdrop hype normalises.
- The LRT trades permanently at peg with no depeg tail, so no risk premium is warranted.
- Looping an LRT adds return exactly equal to the extra liquidation risk taken.

The record partly rejects and partly confirms this. During the 2024 points era, implied LRT APRs ran well above base staking as protocols bid for TVL — a real (if temporary) premium. But post-EIGEN-TGE and post-Renzo-depeg, headline yields compressed toward base staking plus a thin AVS reward, and the 2024-04-24 ezETH depeg proved the tail is real, not null. A restaking book whose net-of-slashing, net-of-dilution yield sits at or below base staking for 30+ days is living in the null world and should unwind the extra layers.

## Rules

### Entry

1. **Yield hurdle.** Net AVS yield (headline AVS reward − expected slashing loss − emission dilution haircut) exceeds base ETH staking yield by a margin that pays for the added risk — target **≥ +150 bps** over base staking.
2. **Peg check.** LRT trades within **50 bps of its ETH NAV** on secondary markets (Curve/Balancer/Uniswap). A discount is a live risk flag, not a discount to buy blindly.
3. **Operator/AVS diversification.** Delegate across ≥ 3 AVSs and reputable operators; never concentrate all restaked ETH behind a single slashing condition.
4. **Withdrawal-queue awareness.** Confirm the EigenLayer/LRT unbonding path (often 7+ days) and secondary-market exit depth before sizing.
5. **Leverage gate.** If looping on [[aave]]/Morpho, cap loop LTV so a 2% LRT depeg does not breach the liquidation threshold (health factor buffer ≥ 1.3 at entry).

### Exit

1. **Yield compression** — net-of-slashing AVS yield falls below base staking; unwind the AVS layer, keep plain staking.
2. **Peg break** — LRT/ETH deviation > 2%; de-risk the loop first (repay borrow), then decide on the base position.
3. **Slashing/parameter event** — any slashing touching a delegated operator, or an LRT changing slashing/operator parameters or pausing withdrawals.
4. **Loop stress** — leverage-loop health factor < 1.15; delever immediately.
5. **Post-airdrop** — once the LRT/AVS token has distributed, re-underwrite whether the residual yield still clears the hurdle.

### Sizing

- **Expected-value sized.** Size each layer by `EV = base_yield + p(AVS reward) − p(slash) × slash_loss − emission_dilution` (see [[expected-value]]); only add a layer whose EV clears the hurdle.
- **Per-LRT cap** ≤ 25% of the sleeve so one depeg/exploit cannot wipe the book.
- **Leverage cap** ≤ 2x on any LRT loop, well below what the venue permits, because LRT collateral is depeg-prone.
- **Kelly-fractional** ~0.05-0.10 of book per LRT given the fat slashing/depeg tail (see [[kelly-criterion]]).

## Implementation pseudocode

```python
# restaking_alloc.py — layered-yield EV gate + risk kill switches
BASE_STAKING_APR   = 0.035     # plain ETH staking
YIELD_HURDLE_BPS   = 0.015     # require net AVS yield >= base + 150 bps
PEG_WARN           = 0.005     # 0.5% LRT/ETH deviation -> no new size
PEG_KILL           = 0.02      # 2% deviation -> de-risk
HF_ENTRY_MIN       = 1.30      # loop health-factor buffer at entry
HF_DELEVER         = 1.15      # emergency delever
MAX_PER_LRT        = 0.25
MAX_LOOP_LEVERAGE  = 2.0

def net_avs_yield(avs_reward_apr, p_slash, slash_loss_frac, emission_dilution):
    # expected-value net of slashing loss and token dilution
    return avs_reward_apr - p_slash * slash_loss_frac - emission_dilution

def decide(lrt, book):
    # lrt: symbol, peg_dev, avs_reward_apr, p_slash, slash_loss_frac,
    #      emission_dilution, health_factor, slashing_event, param_change
    pos = book["positions"].get(lrt.symbol)

    # ---- kill switches ----
    if pos and (lrt.slashing_event or lrt.param_change):
        return {"action": "EXIT", "symbol": lrt.symbol, "reason": "slash/param event"}
    if pos and abs(lrt.peg_dev) > PEG_KILL:
        return {"action": "DERISK", "symbol": lrt.symbol, "reason": "peg break"}
    if pos and pos.get("looped") and lrt.health_factor < HF_DELEVER:
        return {"action": "DELEVER", "symbol": lrt.symbol, "reason": "loop HF low"}

    net = net_avs_yield(lrt.avs_reward_apr, lrt.p_slash,
                        lrt.slash_loss_frac, lrt.emission_dilution)

    if pos:
        if net < BASE_STAKING_APR:
            return {"action": "UNWIND_AVS", "symbol": lrt.symbol, "reason": "yield compressed"}
        return {"action": "HOLD", "symbol": lrt.symbol}

    # ---- entry ----
    if net - BASE_STAKING_APR < YIELD_HURDLE_BPS:
        return {"action": "WAIT", "reason": "net AVS yield below hurdle"}
    if abs(lrt.peg_dev) > PEG_WARN:
        return {"action": "WAIT", "reason": "LRT off peg"}
    size = MAX_PER_LRT * book["sleeve_capital"]
    return {"action": "OPEN", "symbol": lrt.symbol, "notional": size,
            "loop_leverage": min(MAX_LOOP_LEVERAGE,
                                 book["target_leverage_if_HF_ok"]),
            "reason": f"net AVS yield {net*100:.2f}%"}
```

## Indicators / data used

- **ETH price** — the base asset and the denominator for LRT NAV.
- **LRT secondary price + implied ETH peg** — depeg is the fastest live-risk signal; monitor the Curve/Balancer LRT/ETH pool ratio.
- **AVS reward rate / native APR** — from EigenLayer + LRT dashboards; net it against expected slashing loss and emission dilution.
- **Base staking yield** — the hurdle to beat.
- **TVL** — rising TVL against a fixed AVS reward pool dilutes yield (the core decay mechanism).
- **Withdrawal-queue length** — governs exit speed and secondary-market pressure.
- **Loop health factor / borrow rate** — for any levered position on [[aave]]/Morpho.
- **Points/airdrop tracking** — see [[points-farming]] for valuing the LRT/AVS token component.

Peg, TVL, and points balances come from protocol dashboards (EigenLayer, ether.fi, Renzo, DeFiLlama); CryptoDataAPI covers the ETH leg and the tradable LRT/AVS tokens (see *Getting the Data*).

## Example trade

**Setup (2026-04-19):** operator deploys **10 ETH ($31,250 at $3,125/ETH)**.

1. **Base stake** via [[lido]] → 10 stETH, ~3.5% APY ($1,094/yr).
2. **Restake** stETH into ether.fi → 10 eETH; eETH delegated across 3 AVSs paying a combined **~1.8% net-of-slashing** ($563/yr) plus ether.fi points.
3. **Optional loop** — supply eETH on Aave, borrow ETH at 60% LTV, re-stake once (1.6x effective). Adds base+AVS yield on the borrowed leg minus ~2.5% borrow cost → net **~+1.4%** on the looped notional, at the cost of depeg-liquidation risk. Entry health factor 1.35.

**Hold (6 months):** eETH holds peg; no slashing; AVS rewards accrue; ETHFI-equivalent points accumulate. Realised yield ≈ base 3.5% + AVS 1.8% + loop 1.4% ≈ **~6.7% annualised on the base 10 ETH**, plus a points/airdrop option.

**Exit:** unwind the loop (repay ETH borrow, ~$8 gas + ~5 bps swap), redeem or sell eETH near peg. Net realised ≈ **~6.3% APY after gas and exit slippage** — *conditional on no slashing and no depeg*. The 2024-04-24 ezETH scenario shows the other tail: a depeg to ~$0.69 would have liquidated the looped leg near the bottom, converting the year's yield into a double-digit principal loss.

## Performance characteristics (realistic cost overlay)

The naive "10.5% layered yield" of the old write-up is **not** the number to size on. Cost-corrected:

| Metric | Value | Note |
|---|---|---|
| Headline layered yield | 6-12% | Base + AVS + loop, pre-cost, pre-tail. |
| Net expected yield | 4-7% | After gas, exit slippage, and expected slashing/depeg haircut. |
| Expected Sharpe | ~0.9 | Positive-carry with a fat, rare left tail. |
| Max drawdown | 25-35% | Dominated by depeg/slashing tails, not ETH direction (which is hedged out only if you hedge — most restakers don't). |
| Breakeven cost budget | ~40 bps round trip | Gas + LRT/ETH slippage on entry/exit. |

**Cost overlay (never naive):**

- **Gas** — deposit, delegate, loop, and unwind are multiple Ethereum L1 transactions; ~$5-30 each at 2026 gas, i.e. tens of dollars round-trip per position.
- **LRT/ETH slippage** — secondary-market exit of a large LRT position can cost 20-100+ bps into thin depeg liquidity precisely when you most want out.
- **Withdrawal-queue drag** — native redemption locks capital 7+ days; forced fast exits pay the secondary-market discount.
- **Borrow cost** — loops pay ~2-4% ETH borrow, netted against the extra yield.
- **Slashing haircut** — expected-loss term; small probability, but the loss is a fraction of principal, so it dominates the tail.
- **Emission dilution** — points-era APRs partly paid in tokens that sell off at TGE; discount them heavily.
- **Directional ETH exposure** — unless separately hedged (e.g. via [[funding-rate-arbitrage]] shorts), the whole position is long ETH; the "yield" sits on top of full ETH drawdown risk.

## Capacity limits

Very high headline capacity (EigenLayer TVL has run into the tens of billions), but **yield capacity is bounded by the AVS reward pool**: as TVL rises against a roughly fixed reward budget, net AVS yield per dollar falls. So the *strategy* scales while its *edge* dilutes — the opposite of a size-limited arb. For an individual operator, the binding constraints are LRT secondary-market exit depth (tens of millions before slippage bites) and loop liquidity on [[aave]]. `capacity_usd` of $500M reflects a large desk that can still exit the LRT leg in a stress window; beyond that, exit becomes the risk.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Slashing event (Failure Mode #6, tail realised).** A delegated operator gets slashed; restaked principal is cut. Multiple AVS delegations multiply the surface. Now live post-2025.
2. **LRT depeg + leverage cascade (Failure Mode #6).** The 2024-04-24 Renzo ezETH depeg to ~$0.69 liquidated leveraged loops and cascaded — the canonical failure precedent.
3. **Yield-reward collapse (Failure Mode #5, regime change).** AVS reward sustainability is unproven; if AVSs stop paying or emissions roll off, net yield falls to base staking or below.
4. **Correlation/contagion (Failure Mode #1).** A major Ethereum, Lido, or EigenLayer incident cascades across every stacked layer simultaneously — the layers are not independent.
5. **Smart-contract exploit.** Four-protocols-deep (staking → EigenLayer → LRT → lending) multiplies exploit vectors.
6. **Points/airdrop disappointment.** A large chunk of the "yield" is a token option that can convert poorly or dump at TGE — see [[points-farming]] and [[airdrop-farming]].
7. **Withdrawal congestion.** A queue backlog in a stress window forces exit through a discounted secondary market.

## Kill criteria

Unwind the extra layers (keep base staking) or exit entirely on any of:

1. **Net AVS yield (after expected slashing loss) < base ETH staking yield for 30+ days.**
2. **LRT/ETH peg deviation > 2%.**
3. **Any confirmed slashing event** touching a delegated operator.
4. **LRT protocol changes slashing/operator parameters or pauses withdrawals.**
5. **Leverage-loop health factor < 1.15.**

Re-enter only when peg, yield, and parameters are stable for 14+ days. See [[when-to-retire-a-strategy]].

## Advantages

- **Capital efficiency** — multiple yield layers on one unit of ETH.
- **Liquid** — LRTs stay usable across DeFi, unlike locked native staking.
- **Optionality** — early restakers capture AVS/LRT token airdrops on top of yield.
- **Flexible risk dial** — choose AVSs, operators, and leverage to match appetite.
- **Low minimum** — works from a couple thousand dollars of ETH.

## Disadvantages

- **Compounding smart-contract risk** — every layer is another exploit vector.
- **Real slashing risk** — live since 2025; multiplied across AVS delegations.
- **Depeg tail** — LRTs can and do depeg (ezETH 2024); loops amplify the loss.
- **Not market-neutral** — full long-ETH drawdown unless separately hedged.
- **Yield decay** — AVS rewards dilute with TVL and compressed hard post-TGE.
- **Withdrawal illiquidity** — multi-day unbonding forces stress exits into discounts.
- **Complexity and tax** — multi-protocol positions and token rewards are an accounting burden.

## Sources

- [[eigenlayer]] — restaking primitive, AVS design, and the 2025 slashing/redistribution launch.
- Renzo ezETH depeg, 2024-04-24 — depeg to ~$0.69 and ~$60M+ of cascaded leveraged-loop liquidations; the canonical LRT tail event (contemporaneous CoinDesk/The Block coverage).
- [[lido]] — stETH, the dominant base liquid-staking token feeding restaking.
- ether.fi / Puffer / Kelp / Renzo LRT documentation — yield composition, points, and withdrawal mechanics (protocol docs).
- [[points-farming]] / [[airdrop-farming]] — for valuing the LRT/AVS token component of the yield.
- [[ethena-usde]] — comparison risk-premium harvest (basis risk vs slashing risk).

## Getting the Data (CryptoDataAPI)

CryptoDataAPI covers the **ETH leg and the tradable LRT/AVS tokens**; restaking-specific TVL, AVS APRs, and LRT peg come from protocol dashboards and DeFiLlama.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ETHUSDT` — ETH spot price (base asset / NAV denominator)
- `GET /api/v1/coins/search?q=ether.fi` — locate LRT/AVS tokens (ETHFI, EIGEN, REZ, PUFFER)
- `GET /api/v1/coins/{symbol}` — token profile for the LRT/AVS token (e.g. EIGEN, ETHFI)
- `GET /api/v1/on-chain/exchange-flows/ETH` — ETH CEX inflow/outflow (de-risking / stress signal)
- `GET /api/v1/on-chain/score` — On-Chain Health composite (regime backdrop)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=500` — ETH OHLCV
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for ETH and listed LRT/AVS tokens

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=ETHUSDT"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-data]], [[cryptodataapi-on-chain]].

## Related

- [[eigenlayer]] — the restaking primitive and AVS marketplace.
- [[staking]] — the base proof-of-stake yield layer.
- [[lido]] — leading liquid-staking provider (stETH).
- [[ethereum]] — the underlying chain.
- [[defi-yield-farming]] / [[leveraged-yield-farming]] — the yield strategies restaking layers upon.
- [[points-farming]] / [[airdrop-farming]] — how the LRT/AVS token option is farmed and valued.
- [[ethena-usde]] — a comparable risk-premium harvest.
- [[aave]] — the venue for restaking leverage loops.
- [[expected-value]] / [[kelly-criterion]] — sizing framework.
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]] — methodology.
