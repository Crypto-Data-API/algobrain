---
title: "Crypto Yield Stack"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, crypto, defi, yield-farming, staking, restaking, liquidity, on-chain]
aliases: ["Yield Stacking", "Crypto Yield Stacking Strategy", "Layered DeFi Yield", "Restaking Stack"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced

backtest_status: naive-backtested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, risk-bearing, informational]
edge_mechanism: "Each DeFi layer pays a protocol-native yield (issuance, fees, interest, incentive emissions) to whoever supplies the same base capital; you collect all layers at once and are paid to warehouse the stacked smart-contract, slashing, depeg, and impermanent-loss risk that conservative holders refuse to bear. The informational sliver is picking which points programs will actually pay."

# Data and infrastructure requirements
data_required: [staking-yield, lst-peg, defi-tvl, lending-rates, lp-fees, gas-price, security-events, spot-price]
min_capital_usd: 10000
capacity_usd: 500000000
crowding_risk: high

# Performance expectations (net of gas, IL, and realistic points haircut — NOT market-neutral)
expected_sharpe: 0.6
expected_max_drawdown: 0.60
breakeven_cost_bps: 40

# Decay history
decay_evidence: "ETH staking yield fell from ~5% (2022) to ~3% (2025) as the validator set grew. EigenLayer restaking incentives compressed after the 2024 points-to-token conversion. Points/airdrop realised value collapsed through 2024-2025 as 'points fatigue' set in and several high-TVL programs (e.g. large restaking and L2 farms) delivered airdrops worth a fraction of the implied APY farmers had modelled."

# Lifecycle (only if deployed — see [[live-journal]])
kill_criteria: |
  - any layer's protocol suffers an exploit, emergency-pause, or governance takeover
  - stETH / LRT peg deviates > 2% from underlying and does not recover in 24h
  - realised incremental yield of the top 2 layers < gas + monitoring cost for 60 days
  - underlying ETH position drawdown > 50% (this book is long-biased, not neutral)
  - EigenLayer / AVS slashing event touches a delegated operator

related: ["[[delta-neutral-yield-farming]]", "[[eth-staking]]", "[[liquid-staking]]", "[[restaking]]", "[[liquidity-provision]]", "[[defi-lending]]", "[[stablecoin-yield]]", "[[points-farming]]", "[[airdrop]]", "[[lido]]", "[[eigenlayer]]", "[[etherfi]]", "[[impermanent-loss]]", "[[smart-contract-risk]]", "[[slashing]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Crypto Yield Stack

The crypto yield stack layers multiple DeFi yield sources on top of the **same base capital** so that one unit of ETH earns staking issuance, restaking rewards, LP swap fees, lending interest, and points simultaneously. A fully stacked ETH position has historically produced 10-25%+ *effective* APY versus ~3% for plain staking. The catch, stated up front, is that **this is not a market-neutral trade** — it carries full directional ETH price risk — and **yield stacking is risk stacking**: every layer adds a smart-contract, slashing, depeg, or impermanent-loss failure point. This page treats the stack as a *managed book* with an honest, tail-aware cost overlay, not a naive APY brochure.

## Edge source

Mapping to [[edge-taxonomy]]:

- **Structural (primary).** Each layer is a *contractual protocol payment*: ETH staking issuance, restaking AVS rewards, LP fees from swap flow, lending interest from borrowers. You are not predicting price; you are positioning to receive hard-coded cash-flows for supplying productive capital.
- **Risk-bearing (secondary).** The incremental yield above plain staking is compensation for the incremental risk each layer adds — smart-contract exploit, AVS [[slashing]], LST/LRT [[depeg-risk|depeg]], and [[impermanent-loss]]. This is the core honesty of the trade: the extra 2-3% per layer *is* a risk premium, not free money.
- **Informational (tertiary, weak).** The one genuinely skill-based sliver is *points/airdrop selection* — judging which incentive programs will convert to real token value and which are vapour. This edge has decayed sharply as points fatigue set in.

Crucially, the base ETH price exposure is **not** an edge — it is a beta you are choosing to hold. A -50% ETH move overwhelms any yield the stack produces. If you want the yield without the beta, hedge the base with a perp short — that is [[delta-neutral-yield-farming]], a different strategy.

## Why this edge exists

1. **Yields are additive on the same collateral.** A liquid-staking token (stETH) remains transferable, so the *same* ETH can be restaked, then LP'd, then used to farm points. Protocols deliberately allow this composability to bootstrap TVL.
2. **Most holders under-stack.** The median ETH holder stayes at layer 1-2 because each additional layer demands active monitoring, gas, and risk tolerance. The unmet supply of stacked capital leaves incentive emissions available to operators who will climb.
3. **Protocols pay to rent risk-bearing capital.** New AVSs, L2s, and DEXs bootstrap security and liquidity by paying emissions/points to early suppliers. Those payments are, in effect, a risk-underwriting fee for capital willing to be first.

The persistence is real but *decaying*: as more capital climbs the stack, per-layer yield compresses and the points-to-value conversion worsens.

## Null hypothesis

Under efficient risk pricing, each incremental layer's yield exactly compensates its incremental risk, so the *risk-adjusted* return of a 5-layer stack equals that of plain staking:

- Sharpe of the full stack ≈ Sharpe of layer-1 staking; the extra APY is pure risk premium with zero alpha.
- Points expected value ≈ 0 after weighting for programs that never launch a token or launch worthless ones.
- LST/LRT peg deviations are noise with zero expected P&L.
- Realised drawdowns scale with the number of layers, cancelling the higher headline yield.

Empirically the null is *partly* rejected — early EigenLayer/EtherFi/L2 farmers captured airdrops worth far more than the risk premium implied — but it is *increasingly accepted* as the space matures: 2024-2025 points programs delivered airdrops worth a fraction of modelled APY, and several LRTs traded at persistent discounts. If a live stack's realised risk-adjusted return over 12 months is indistinguishable from plain staking, you are being paid exactly the null: bearing more risk for no extra alpha.

## Rules

### Layer selection (the risk ladder)

| Layer | Source | Incremental yield (2025) | Added risk |
|---|---|---|---|
| 1 | [[eth-staking]] (direct or via [[lido]]) | ~3.0% | Slashing (rare), ETH beta |
| 2 | [[liquid-staking]] (stETH / rETH) | +0.0-0.5% | LST depeg |
| 3 | [[restaking]] ([[eigenlayer]] / [[etherfi]]) | +1-4% | AVS slashing, extra contract |
| 4 | [[liquidity-provision]] (stETH/ETH pool) | +2-6% | Impermanent loss (small for correlated pair), contract |
| 5 | [[points-farming]] → [[airdrop]] | speculative, model at **0.3x** of hype | Program may never pay; opportunity cost |

### Entry conditions

1. **Base position first.** Only stack capital you are willing to hold as directional ETH; the stack does not remove ETH price risk.
2. **Per-layer viability.** Add a layer only if its *net incremental* yield (after gas amortised over the intended hold) exceeds **1.5%** annualised — below that the marginal risk is not worth it.
3. **Peg gate.** Every LST/LRT in the stack must trade within **0.5%** of underlying at entry.
4. **TVL + security gate.** Each protocol has TVL > $100M, a clean audit, and no exploit/emergency-pause in the trailing 30 days (monitor via a security feed).
5. **Points haircut.** Model any points layer at **0.3x** the community-implied APY; never size the stack assuming full points value.

### Exit / de-risk conditions

1. **Any-layer exploit or emergency-pause** — exit *that* layer immediately; the composability means a lower-layer failure can cascade upward.
2. **LST/LRT depeg > 2%** not recovering within 24h — unwind the affected layers.
3. **Slashing event** on a delegated AVS/operator — exit restaking layer, reassess operator selection.
4. **Incremental yield of top layers < gas + monitoring cost for 60 days** — collapse back to layer 1-2.
5. **Base ETH drawdown > 50%** — this is the dominant risk; consider whether to hold the beta at all (or hedge, converting to [[delta-neutral-yield-farming]]).

### Sizing

- **Minimum ~$10,000** (5-10 ETH) to amortise gas across multiple protocols; below this, gas eats the stack.
- **Cap per protocol at 25%** of the book so a single exploit is survivable.
- **Reserve gas + margin buffer** (~2-3% of book) for rebalancing and emergency exits.

## Implementation pseudocode

```python
# yield_stack.py — layer manager for a long-ETH DeFi yield book
MIN_INCREMENTAL_APR = 0.015   # 1.5% floor to add a layer
PEG_TOLERANCE       = 0.005   # 0.5% LST/LRT band at entry
DEPEG_EXIT          = 0.02    # 2% depeg exit
POINTS_HAIRCUT      = 0.30    # model points at 30% of hyped value
MAX_PER_PROTOCOL    = 0.25
MIN_TVL_USD         = 100e6

def effective_apr(layer):
    pts = layer.points_hyped_apr * POINTS_HAIRCUT if layer.is_points else 0.0
    return layer.base_apr + pts - layer.gas_apr - layer.il_apr

def manage(stack, market):
    actions = []
    # ---- de-risk first ----
    for layer in stack.layers:
        if layer.exploit_flag or layer.emergency_pause:
            actions.append(("EXIT_LAYER", layer, "protocol event"))
        elif layer.is_lst and layer.peg_dev > DEPEG_EXIT and not layer.peg_recovering:
            actions.append(("EXIT_LAYER", layer, "depeg"))
        elif layer.slashing_event:
            actions.append(("EXIT_LAYER", layer, "slashing"))
    if actions:
        return actions

    # ---- consider climbing another layer ----
    nxt = stack.next_candidate_layer()
    if (nxt and nxt.tvl_usd >= MIN_TVL_USD and nxt.audited
            and nxt.peg_dev <= PEG_TOLERANCE
            and effective_apr(nxt) >= MIN_INCREMENTAL_APR
            and stack.exposure(nxt.protocol) < MAX_PER_PROTOCOL):
        return [("ADD_LAYER", nxt, f"+{effective_apr(nxt)*100:.1f}% net")]

    # ---- prune dead layers ----
    for layer in stack.layers:
        if effective_apr(layer) < 0:
            actions.append(("EXIT_LAYER", layer, "net-negative after gas/IL"))
    return actions or [("HOLD", None, "stack stable")]
```

The production system adds: a security-feed watcher (exploit/depeg alerts), an LRT redemption-queue monitor, weekly peg + TVL + IL review, and gas-batched entry/exit.

## Indicators / data used

- **Staking / restaking APR** — layer-1/3 base yields (protocol dashboards; issuance schedule).
- **LST/LRT peg** — depeg guard for every liquid layer.
- **LP fee APR + [[impermanent-loss]] estimate** — layer-4 net yield.
- **DeFi TVL trend** — falling TVL is an early risk/withdrawal signal.
- **Lending rates** — layer for idle stablecoins; also the risk-free comparison.
- **Security/hack + depeg feed** — the single most important monitor for a stacked book.
- **Gas price** — determines minimum viable position size and rebalance cadence.
- **ETH spot price** — the dominant P&L driver (this is a long book).

## Example trade

**Setup (2026-04-15): 10 ETH ($32,000 at $3,200).**

| Layer | Protocol | Position | Gross APR | Net after gas/IL/haircut |
|---|---|---|---|---|
| 1+2 | [[lido]] stETH | 10 ETH staked | 3.2% | 3.1% |
| 3 | [[eigenlayer]] via [[etherfi]] | 6 ETH restaked | +2.5% | +2.2% |
| 4 | stETH/ETH Curve pool | 4 ETH LP'd | +4.5% | +3.8% (IL ~0.2%) |
| 5 | points (EtherFi + AVS) | interactions | +9% *hyped* | +2.7% (0.3x haircut) |
|  | **Blended** |  |  | **~9.4% effective APY** |

- Plain staking alone: 3.1% = ~0.31 ETH/yr.
- Stacked (net, haircut applied): ~9.4% = ~0.94 ETH/yr — roughly **3x** the yield on the same capital.
- **But**: over the same year ETH fell from $3,200 to $2,100 (−34%). Book value: 10 ETH × $2,100 = $21,000 + ~0.94 ETH yield ≈ $23,000 vs $32,000 start = **−28% in USD** *despite* the yield. The yield stack enhanced the ETH-denominated return; it did **not** protect against the beta.

This is the essential lesson the naive "15% APY" framing hides: on an un-hedged stack, the ETH price path dominates every yield decision.

## Performance characteristics

Honest, tail-aware picture (2024-2026):

| Metric | Value | Note |
|---|---|---|
| Effective yield (ETH-denominated) | 6-15% net | After gas, IL, and 0.3x points haircut. |
| USD Sharpe | ~0.6 | Dominated by ETH beta, not the yield. Low. |
| Max drawdown (USD) | up to 60% | Set by ETH price, not yield. |
| Max drawdown (ETH-denominated) | 5-30% | From depeg/exploit/slashing tail events. |
| Breakeven cost budget | ~40 bps | Gas-heavy; scales badly for small books. |
| Points realisation | ~0.2-0.4x of hyped value | 2024-2025 empirical haircut. |

**Realistic cost overlay (never assume naive APY):**
- **Gas:** entry across 4-5 protocols can cost $50-300; exits similar. On a $10k book that is 100-600 bps round-trip — the single biggest reason small stacks fail.
- **Impermanent loss:** ~0.1-0.5% on correlated stETH/ETH; 2-10%+ if any layer uses a volatile pair.
- **Points haircut:** apply 0.3x — the difference between a modelled 15% and a realised 9%.
- **Depeg/exploit tail:** low-probability, high-severity; a single layer exploit can zero 25% of the book.
- **ETH beta:** the dominant term and *not a cost you can net out* — it is the risk you chose.

A naive stack model that sums gross APRs, counts points at face value, and ignores gas and ETH drawdown can show "25% APY" on a position that lost 28% in USD. The gap between those two numbers is the entire point of this page.

## Capacity limits

Very high on the yield side — DeFi TVL is in the tens of billions — so aggregate capacity is effectively **$100M-$1B+** before an operator's own deposits materially move per-layer APR. The binding constraints are instead:
- **Per-pool depth** (large LP entries move the pool and worsen IL/slippage).
- **Restaking/AVS caps** (some AVSs cap delegated stake).
- **Points program dilution** (a whale's own deposits dilute the very points APR they farm).
- **Redemption-queue depth** on LSTs/LRTs during a rush to exit.

For an individual operator the practical range is **$10k-$50M**; above that, per-pool and redemption depth dominate. The frontmatter `capacity_usd` reflects the aggregate strategy ceiling, not the size any one participant should target.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Smart-contract exploit (#7).** The signature risk of a stacked book: a bug in *any* layer can cascade because layers are composed on the same collateral. Ronin, Euler, and countless smaller DeFi hacks are the reference class.
2. **LST/LRT depeg (#6).** June 2022 stETH to ~0.94; LRT discounts through 2024. A depeg during a redemption rush breaks the exit path.
3. **Slashing (#6).** An AVS/operator misbehaviour slashes restaked capital — a risk *added* purely by climbing to layer 3.
4. **Points collapse (#4/#5).** The informational sliver decayed hardest: 2024-2025 airdrops widely disappointed relative to modelled APY. A stack sized on face-value points is over-levered to a mirage.
5. **ETH beta (#5).** Not a "failure mode" so much as the elephant: the un-hedged base position can lose 50%+ in a bear market, dwarfing all yield. This is why the hedged cousin [[delta-neutral-yield-farming]] exists.
6. **Gas regime shift (#7).** An L1 fee spike can make small-book rebalancing uneconomic, trapping capital in dead layers.
7. **Regulatory action.** Staking/restaking restrictions can force protocol shutdowns or geo-blocks.

## Kill criteria

De-risk or unwind on any of:

1. **Any layer's protocol** suffers an exploit, emergency-pause, or hostile governance action.
2. **LST/LRT peg** deviates > 2% from underlying and does not recover within 24h.
3. **Realised incremental yield of the top two layers < gas + monitoring cost for 60 days** — collapse to layer 1-2.
4. **AVS/operator slashing event** touches a delegated position.
5. **Base ETH drawdown > 50%** — reassess holding the beta at all, or hedge it (see [[delta-neutral-yield-farming]]).

Re-climb only when the affected protocol is post-mortem'd and re-audited, pegs are restored, and incremental net yield again clears the 1.5% floor. See [[when-to-retire-a-strategy]].

## Advantages

- **Yield multiplication on the same capital** — 3-5x plain-staking yield in ETH terms when programs pay.
- **Composable and modular** — climb or descend the risk ladder to match tolerance.
- **Structural, transparent cash-flows** on the lower layers (staking, fees, interest).
- **Optionality from points** — occasional large airdrops (early EigenLayer/EtherFi) delivered outsized returns.
- **Accessible** — permissionless; no venue KYC beyond the wallet.

## Disadvantages

- **Risk stacking.** Every layer is a new failure point; risks compound faster than yields.
- **Not market-neutral.** Full ETH beta dominates USD returns — the headline APY is misleading without the price context.
- **Gas-heavy.** Uneconomic below ~$10k; rebalancing costs erode small books.
- **Points are speculative and decaying.** Modelling them at face value is the classic over-sizing error.
- **Active monitoring required.** Weekly peg/TVL/IL/slashing review is mandatory; a passive stack is a landmine.
- **Correlated tail risk.** In a systemic DeFi event (mass depeg + redemption rush), the layers fail together, exactly when you most want to exit.
- **Tax complexity.** Staking rewards, LP fees, and airdrops are often taxed as income at receipt regardless of price path.

## Sources

- Lido / EigenLayer / EtherFi official documentation — staking, restaking, and LRT mechanics; slashing and AVS delegation models (see [[eth-staking]], [[restaking]], [[liquid-staking]]).
- June 2022 stETH depeg (~0.94 low) — the canonical LST depeg event; see [[2022-06-steth-depeg]].
- DefiLlama TVL and yield dashboards — per-protocol TVL trend and realised APR (risk/withdrawal monitoring).
- 2024-2025 points-program post-mortems (EigenLayer, major L2 and restaking farms) — documented gap between modelled points APY and realised airdrop value; basis for the 0.3x haircut.
- [[impermanent-loss]] literature — IL on correlated vs volatile LP pairs (layer-4 cost modelling).
- [[delta-neutral-yield-farming]] — the hedged variant that removes the ETH beta this book retains.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score (the key stacked-book tail monitor)
- `GET /api/v1/security/events` — filterable recent security events (exploit/depeg early warning)
- `GET /api/v1/on-chain/score` — On-Chain Health composite 0-100
- `GET /api/v1/sentiment/stablecoins` — stablecoin mcap + flows (lending-demand / dry-powder context)
- `GET /api/v1/dex/trending` — trending DEX pools by chain (LP-layer selection)
- `GET /api/v1/market-data/ticker/price?symbol=ETHUSDT` — ETH spot (the dominant P&L driver)

**Historical data:**
- `GET /api/v1/security/regime/score` — Security Stress composite over time
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin mcap timeseries
- `GET /api/v1/backtesting/klines?symbol=ETHUSDT&interval=1d` — ETH price history for USD-return modelling

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/security/regime"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]], [[cryptodataapi-on-chain]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Tail monitor** — `GET /api/v1/security/regime` + `GET /api/v1/security/events` — the stacked book's exploit/depeg early-warning system
- **Health gates** — `GET /api/v1/on-chain/score` + `GET /api/v1/sentiment/stablecoins` — on-chain health and dry-powder context for the lending layer
- **P&L driver** — `GET /api/v1/market-data/ticker/price?symbol=ETHUSDT` — ETH spot dominates USD-denominated returns of the whole stack
- **Backtest** — `GET /api/v1/backtesting/klines?symbol=ETHUSDT&interval=1d` (back to 2017-08) for the ETH leg; `GET /api/v1/market-intelligence/stablecoin-history` for supply cycles — pool-level APR history is not on CryptoDataAPI and must come from DeFiLlama or subgraphs
- **Tips** — when Security Stress spikes, de-risk the whole stack rather than one layer (the layers share tail events); poll `GET /api/v1/daily` hourly and hit per-layer endpoints only when the composite moves

## Related

- [[delta-neutral-yield-farming]] — the hedged, market-neutral cousin (adds a perp short to strip ETH beta).
- [[eth-staking]] / [[liquid-staking]] / [[restaking]] — the lower layers and their mechanics.
- [[liquidity-provision]] / [[impermanent-loss]] — the LP layer and its signature cost.
- [[defi-lending]] / [[stablecoin-yield]] — the idle-capital and risk-free comparison layer.
- [[points-farming]] / [[airdrop]] — the speculative top layer and its haircut.
- [[smart-contract-risk]] / [[slashing]] — the risks that stack alongside the yields.
- [[lido]] / [[eigenlayer]] / [[etherfi]] — the reference protocols per layer.
- [[edge-taxonomy]] — where this strategy sits among the six edge categories.
- [[failure-modes]] / [[when-to-retire-a-strategy]] — kill-criteria methodology.
