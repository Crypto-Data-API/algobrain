---
title: "Liquidity Sniping"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [liquidity-sniping, dex, token-launch, bot-trading, mempool, frontrunning, crypto, algorithmic, memecoins]
aliases: ["Liquidity Snipe", "Token Launch Sniping", "DEX Sniping Bot", "New-Pool Sniping"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [latency, structural, informational]
edge_mechanism: "You buy in the same block that initial liquidity is added, at the pool's opening price, before the crowd that discovers the token on DEX Screener/Telegram minutes later can bid it up — a pure speed-and-position-in-block race against other bots and the retail buyers on the other side."

# Data and infrastructure requirements
data_required: [mempool-stream, dex-new-pools, token-security, gas-oracle, dex-liquidity-depth, priority-fee-oracle]
min_capital_usd: 2000        # gas/tip buffer + enough tickets to survive the loser base rate
capacity_usd: 1500000        # bounded by launch-pool depth; per-token capacity is tiny
crowding_risk: high

# Performance expectations (net of gas, priority fees, buy/sell tax, slippage)
expected_sharpe: 0.6         # lottery-shaped; Sharpe understates a fat right tail and is unstable
expected_max_drawdown: 0.50
breakeven_cost_bps: 1000     # only multi-x winners justify the ~5-15% all-in round-trip drag

# Decay history
decay_evidence: "Naive same-block sniping was highly profitable on 2021 Uniswap V2 and early 2024 Pump.fun launches; edge compressed sharply as (a) hundreds of competing bots bid priority fees up, (b) Pump.fun/launchpads added anti-sniper mechanics (dev-buy caps, dynamic bonding curves, first-block bundling by the deployer themselves), and (c) private orderflow / MEV-protected RPCs hid the mempool signal. Solana Jito tip auctions now routinely exceed the per-token expected edge on contested launches."

# Lifecycle
kill_criteria: |
  - 30-day net P&L across all snipes < 0 after full cost accounting
  - honeypot/rug rate on filled snipes > 60% over trailing 50 fills
  - median priority-fee/tip on wins exceeds 30% of gross win
  - anti-sniper launch mechanics make >70% of monitored launches un-snipeable

related: ["[[memecoin-sniping]]", "[[jito-bundle-sniping]]", "[[token-migration-sniping]]", "[[mev-strategies]]", "[[telegram-bot-trading]]", "[[on-chain-flow-trading]]", "[[airdrop-farming]]", "[[defi-yield-farming]]", "[[algorithmic-trading]]", "[[sentiment-trading]]", "[[slippage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Liquidity Sniping

Liquidity sniping is a bot-driven [[algorithmic-trading|algorithmic]] strategy that **buys a token in the same block (or within milliseconds) that its initial liquidity is added** on a decentralized exchange — Uniswap on Ethereum/Base, Raydium and Pump.fun on Solana, PancakeSwap on BSC. The bot detects the `addLiquidity` / pool-migration event (via the mempool on EVM chains, or via validator/Geyser streams on Solana), then submits a buy with a high priority fee to land at or near the opening pool price, before the wave of retail buyers who find the token on DEX Screener, Telegram, or X can push it up. It is the fastest, most latency-sensitive member of the crypto launch-trading family alongside [[memecoin-sniping]], [[jito-bundle-sniping]], and [[token-migration-sniping]].

## Edge source

Mapping to the six categories in [[edge-taxonomy]], sniping is primarily a **latency** edge wrapped around a **structural** flow imbalance:

- **Latency (primary).** The entire edge is *position in the block*. The first buyer after liquidity is added transacts against a price that literally no one else has seen yet. Whoever is fastest — lowest wire latency to the block builder / validator, highest effective priority fee, tightest simulation loop — wins the fill. This is a race, and races are won on infrastructure, not opinion.
- **Structural (secondary).** New-pool launches are a *predictable, mechanical supply event*: the deployer adds a fixed reserve, and price is deterministic at t=0. The buyers who arrive over the next minutes are non-price-sensitive momentum chasers reacting to a screener alert. The sniper systematically sits between the deterministic opening price and the crowd's higher fills.
- **Informational (tertiary).** A sniper with a good pre-buy filter (contract bytecode analysis, deployer-history database, honeypot simulation) knows something the crowd does not in the first seconds: whether the token is sellable at all. That informational filter is what separates a profitable operation from one that is farmed by rug deployers.

The trade has **no** analytical or risk-bearing edge in the investment sense — you are not valuing the token, you are winning a footrace and dumping into discovery flow.

## Why this edge exists

Three forces keep (a shrinking version of) the edge alive:

1. **Discovery latency of the crowd.** Retail finds tokens through DEX Screener trending, Telegram call channels, and influencer posts — all of which fire *seconds to minutes* after the pool goes live. That lag is the sniper's entire window. As long as humans discover launches after machines do, an opening-price fill is cheaper than a discovery-price fill.
2. **Non-price-sensitive momentum buyers.** The marginal buyer in minute 1-5 of a viral launch is buying *because it is going up*, not because of a valuation. They provide the exit liquidity into which the sniper sells. This is the same behavioural fuel as [[memecoin-sniping]] and [[sentiment-trading]].
3. **A fee-auction that is not yet fully efficient on every chain/launchpad.** Where the priority-fee / Jito-tip auction has not fully competed away the expected per-token edge (new launchpads, low-attention hours, niche chains), positive EV remains. On the most contested Solana launches the auction *has* competed it away — see decay below.

The edge exists in an equilibrium: it is exactly as large as (crowd markup) minus (priority-fee auction clearing price) minus (rug/honeypot base rate). All three terms move against the sniper over time.

## Null hypothesis

Under a no-edge world, the opening-block price is an unbiased estimate of the token's near-term traded price, and the priority-fee auction prices the race efficiently. In that world:

- The expected forward return from an opening-block fill, net of the priority fee paid to win it, is zero.
- Winning the block faster would cost exactly what the head start is worth — the auction is efficient.
- After honeypot/rug losses, the blended EV per snipe is negative (you pay costs for nothing).
- A safety filter would not improve the return distribution because rug tokens would be priced into the auction.

The null is **partially true and increasingly so**. On the most contested launches (top Pump.fun graduations, competitive Base launches), the Jito/priority auction now clears at or above the expected crowd markup, driving blended EV toward or below zero — this is the null world. The null is *falsified* only in the un-competed pockets: off-peak launches, newer launchpads, chains with thinner bot competition, and tokens where a superior safety filter avoids the rug base rate that farms everyone else. If a live sniping operation's 30-day net P&L is indistinguishable from zero after full cost accounting, the auction has caught up and the operation should stop.

## Rules

### Entry (per candidate launch)

A buy is submitted only when **all** hold, evaluated in the sub-second pre-buy simulation:

1. **New-pool / migration event detected** on a targeted router (Uniswap V2/V3, Raydium AMM/CLMM, Pump.fun→Raydium migration, PancakeSwap) for a token not previously seen.
2. **Initial liquidity ≥ floor** — e.g. ≥ $8k on Solana graduations, ≥ $15k on EVM — to avoid dust pools that cannot absorb the exit.
3. **Sell simulation passes** — a simulated buy-then-sell round trip succeeds in the same call (anti-honeypot). Reject if the sell reverts or returns < 90% of the theoretical output (hidden sell tax).
4. **Tax check** — combined buy+sell tax ≤ 10%.
5. **Deployer not blacklisted** — deployer address is not in the local rug/honeypot database; no prior removed-liquidity events from this deployer.
6. **Liquidity disposition** — LP tokens burned or locked at launch (or migration guarantees it, as on Pump.fun).

### Exit

- **Scale-out ladder:** sell 50% of the position at +100% (2x), sell 25% at +300% (4x), let the final 25% ride behind a trailing stop.
- **Trailing stop:** close the runner if it retraces 40% from its post-entry high.
- **Hard time stop:** if not at +100% within 10 minutes, exit at market — attention has not arrived and it likely won't.
- **Instant abort:** if post-buy monitoring detects an LP-removal or blacklist transaction from the deployer, market-sell immediately (accept the loss; a honeypot that flips is worse).

### Sizing

- **Fixed ticket per token** — $50-$500 equivalent, identical across launches. The distribution is lottery-shaped; you cannot pick winners ex ante, so you buy a diversified basket at constant size.
- **Never exceed ~2-5% of a launch pool's reserve** on entry — a larger buy moves the opening price against you and worsens the exit.
- **Portfolio cap:** total capital at risk in open snipes ≤ 5-10% of trading capital.
- **Daily loss limit:** stop for the session if cumulative net loss exceeds a preset threshold (e.g. 15% of the sniping sleeve).

## Implementation pseudocode

```python
# liquidity_snipe.py — decision core for a new-pool sniper
# Reality check: the hard part is the infra (mempool/Geyser latency, block
# building, tip auction), not this logic. This is the filter + sizing layer.

FIXED_TICKET_USD   = 150
MAX_POOL_FRACTION  = 0.03      # never take >3% of the opening reserve
MIN_LIQ_USD        = 8_000
MAX_TAX            = 0.10
MAX_TIP_FRAC_EV    = 0.30      # don't tip more than 30% of expected gross edge

def evaluate_launch(evt, sim, deployer_db, tip_oracle):
    # ---- hard safety gates (any failure => skip) ----
    if evt.initial_liq_usd < MIN_LIQ_USD:
        return skip("liquidity too thin")
    if deployer_db.is_blacklisted(evt.deployer):
        return skip("blacklisted deployer")

    probe = sim.buy_then_sell(evt.token, FIXED_TICKET_USD)   # local fork sim
    if not probe.sell_ok:
        return skip("honeypot: sell reverts")
    if probe.effective_tax > MAX_TAX:
        return skip(f"tax {probe.effective_tax:.0%} too high")
    if probe.round_trip_out < 0.90 * probe.theoretical_out:
        return skip("hidden sell tax / slippage")

    # ---- economic gate: is the race worth winning at the clearing tip? ----
    ticket   = min(FIXED_TICKET_USD, MAX_POOL_FRACTION * evt.initial_liq_usd)
    exp_edge = ticket * expected_markup(evt)      # calibrated crowd markup, e.g. 0.25
    tip      = tip_oracle.clearing_tip(evt.chain) # current auction clearing price
    if tip > MAX_TIP_FRAC_EV * exp_edge:
        return skip("tip auction eats the edge")

    return submit_buy(
        token=evt.token, size_usd=ticket,
        priority_tip=tip,                 # Jito bundle tip / EIP-1559 priority fee
        max_slippage_bps=1500,            # opening pools are violent; wide but capped
        exit_plan=LADDER,                 # 2x/4x/runner + 40% trailing + 10-min stop
    )
```

The production system wraps this with: a co-located mempool/Geyser listener, a private submission path (Jito block-engine on Solana, MEV-Boost/private RPC on EVM), a same-slot fork simulator for the honeypot probe, a deployer-reputation database updated from every observed rug, and a hard kill switch.

## Indicators / data used

- **Mempool / validator stream** — pending `addLiquidity` and Pump.fun migration transactions. The raw, latency-critical signal; must come from a co-located node or a service (bloXroute, Helius Geyser, Jito).
- **New-pool feed** — [[cryptodataapi]] `GET /api/v1/dex/new-pools` for multi-chain launch discovery and post-hoc universe reconstruction.
- **Token security report** — `GET /api/v1/dex/security/{chain}/{address}` for rug/honeypot flags as a second opinion alongside the local sim.
- **DEX liquidity / depth** — opening reserve size and the exit-side depth that caps ticket size and slippage. See [[slippage]].
- **Priority-fee / Jito-tip oracle** — the live clearing price of the block-position auction; the single most important cost input.
- **Meme regime** — `GET /api/v1/meme/regime/score` gates the whole strategy: launch-sniping only has crowd exit liquidity when `meme_season` is active.
- **Deployer reputation** — a self-maintained database of addresses tied to prior rugs/honeypots.

## Example trade

**Setup (Solana, Pump.fun graduation):**

- 10:03:15.20 — bot's Geyser stream sees `CATMOON` graduating from the Pump.fun bonding curve to Raydium with ~$12k liquidity (≈69 SOL). Deployer not blacklisted.
- 10:03:15.35 — same-slot fork sim: buy-then-sell round trip succeeds, 0% tax, LP burned on migration. Passes all gates.
- 10:03:15.45 — economic gate: expected crowd markup ~25% on a $150 ticket ⇒ ~$37 expected edge; current Jito clearing tip ~$3 (< 30% of edge). Submit.

**Entry:**

- Buy $150 of CATMOON via a Jito bundle, tip 0.02 SOL (~$3). Filled in the same slot as migration at ~$69k FDV.
- Realistic entry slippage on a $12k pool for a $150 buy: ~120 bps. Effective cost basis ≈ $151.80 + $3 tip = **$154.80 all-in**.

**Exit (ladder):**

- 10:05:10 — DEX Screener trending; FDV ~$350k (~5x). Sell 50% ($75 cost basis) at ~4.9x after 90 bps exit slippage and 0.5% Raydium fee ⇒ ~$360 gross.
- 10:07:40 — influencer post; FDV ~$1.1M. Sell 25% at ~15x ⇒ ~$560 gross.
- 10:12:00 — runner (25%) trails off the high, trailing stop hits at ~10x ⇒ ~$375 gross.
- Sell-side priority tips + Raydium 0.25-0.5% fees + gas: ~$8 total.

**Net:** ~$360 + $560 + $375 − $8 = ~$1,287 out on $154.80 in ⇒ **≈ +$1,132 (~8.3x) on this token**.

**Portfolio reality:** the same bot sniped ~20 launches that session. ~14 went to zero or rugged ($150 × 14 ≈ $2,100 of tickets, most recovered partially before zero, call it $1,700 lost), 4 were small wins (+$50 to +$300 each), 1 was flat, and this CATMOON 8x carried the day. Session net was positive **only because of the single fat-tail winner** — which is the entire risk profile of the strategy.

## Performance characteristics

Cost-corrected, this is a **negative-median, positive-mean lottery**. There is no honest naive backtest: any simulation that assumes you always won the block, always sold at the top, and never got rugged overstates the edge by an order of magnitude.

| Metric | Realistic value | Note |
|---|---|---|
| Per-snipe win rate | 10-25% | Most tokens die; the strategy lives on the right tail. |
| Median snipe outcome | small loss | Gas + tip + slippage on a token that never moves. |
| Mean snipe outcome | small positive (regime-dependent) | Entirely carried by rare multi-x winners. |
| Blended net APY | wildly variable | Strongly positive in meme-season, negative in dead markets. |
| Sharpe (net) | ~0.6 and unstable | Fat right tail; Sharpe is a poor descriptor here. |
| Max drawdown | 40-60% | Losing streaks between winners are long and deep. |

**Cost overlay (never naive):**

- **Priority fee / Jito tip:** the dominant cost. Uncontested launches ~$0.5-5; contested Solana graduations regularly $20-200+ per attempt, frequently exceeding the per-token expected edge.
- **Gas (EVM):** $2-10 on Base/L2s, $20-200 on Ethereum mainnet per leg — often the reason EVM sniping is uneconomic below large tickets.
- **DEX fee:** Raydium 0.25-0.5%, Uniswap V2 0.30%, per leg.
- **Slippage:** opening pools are violent — 50-200 bps on a $150 buy into a $10-15k pool; worse on the exit if the crowd has already dumped.
- **Buy/sell tax:** 0-10% each way on tax-token launches (rejected by the filter above 10%).
- **Rug/honeypot losses:** treat as a portfolio cost line — a 40-60% rug rate on filled snipes is normal and must be funded by the winners.

The `breakeven_cost_bps: 1000` figure captures that only winners of several hundred percent justify the ~5-15% all-in round-trip drag; the strategy is un-runnable on thin-margin moves.

## Capacity limits

Brutally low, and set by **launch-pool depth**, not by the operator's capital:

- **Per token:** the ~2-5% pool-fraction rule caps a single snipe at ~$250-$750 on a typical $12-15k Solana graduation, and a few thousand dollars on a deep EVM launch. Bigger and you move the opening price against yourself and cannot exit without collapsing the pool.
- **Per session:** capacity is (tokens you can snipe) × (per-token cap). Even a busy meme-season day of hundreds of launches with a strict safety filter yields maybe low-hundreds of thousands of dollars of *deployable* size before the safety filter and pool-depth caps bind.
- **Aggregate working capacity:** ~$1-1.5M is a generous ceiling for a single operator; beyond that the per-token caps and the shrinking count of snipeable launches dominate. This is a satellite / solo-operator strategy, not a fund book.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **The fee auction eats the edge (crowding — Failure Mode #4).** The dominant risk. As bots proliferate, the Jito-tip / priority-fee clearing price rises to meet the expected crowd markup. On contested launches this has already happened; blended EV goes to zero.
2. **Anti-sniper launch mechanics (regime change — #5).** Launchpads fight back: dev-buy caps, dynamic/anti-sniper bonding curves, deployer-bundled first blocks, randomized migration, and MEV-protected private launches that hide the mempool signal. Each removes the opening-price window.
3. **Rug/honeypot base rate (tail realised — #6).** A superior safety filter is the only durable moat; when deployers out-innovate the filter (delayed-enable taxes, blacklist-after-buy, proxy-upgradeable honeypots), the rug rate spikes and farms the operation.
4. **Getting sandwiched (adverse selection).** On EVM, the sniper's own buy can be sandwiched by a faster MEV bot, guaranteeing a worse fill. See [[mev-strategies]].
5. **Infrastructure loss.** The moment a competitor has lower latency to the builder/validator or a better private orderflow deal, you lose every contested race and only win the un-contested (worse) launches — adverse selection on which races you win.
6. **Meme-season dependence.** No crowd, no exit liquidity. In risk-off regimes the strategy has no counterparties to sell into and bleeds costs.

## Kill criteria

Pause (do not permanently retire — the mechanism returns with the next meme-season) on any of:

1. **30-day net P&L < 0** after full accounting for tips, gas, tax, slippage, and rug losses.
2. **Rug/honeypot rate > 60%** on the trailing 50 filled snipes — the filter has been out-innovated.
3. **Median winning-trade tip > 30% of gross win** — the auction has priced out the edge.
4. **> 70% of monitored launches un-snipeable** due to anti-sniper mechanics or private launches.
5. **`meme_regime/score` in `dormant`/`bleeding`** for 30+ days — no crowd exit liquidity.

Re-deploy when meme-season returns, the tip auction cheapens on a fresh launchpad or chain, and a paper run shows positive net EV across ≥ 50 simulated fills. See [[when-to-retire-a-strategy]].

## Advantages

- **Highest capture of launch upside** — an opening-block fill is the cheapest possible entry; a single 10-100x winner can carry a month.
- **Fully automated and unemotional** — the bot enforces the safety filter and the exit ladder that a human panicking in a live launch cannot.
- **Very fast capital cycle** — winners resolve in minutes; capital is rarely tied up.
- **Cheap to attempt on Solana/L2s** — sub-dollar-to-single-digit gas makes a high-frequency basket approach viable where mainnet Ethereum does not.
- **Rich, composable tooling** — Photon, Trojan, BonkBot, Maestro, Banana Gun lower the infra barrier, and it composes with [[sentiment-trading]] for exit timing.

## Disadvantages

- **Negative median outcome** — most snipes lose; the strategy is psychologically brutal and easy to abandon right before a winner.
- **Latency arms race** — the edge decays continuously and requires ongoing infra spend just to stand still.
- **High rug/honeypot exposure** — a large fraction of filled snipes are on tokens engineered to trap buyers.
- **Sandwich/adverse-selection risk** on EVM from faster [[mev-strategies|MEV bots]].
- **Regime-dependent** — dead in risk-off markets; only works in [[sentiment-trading|sentiment]]-driven meme regimes.
- **Legal/ethical grey area** — bot-driven front-running of retail discovery is contested in several jurisdictions.
- **Un-backtestable honestly** — survivorship and look-ahead bias make naive backtests wildly optimistic; only forward paper/live testing is credible.

## Sources

- Pump.fun and Raydium migration mechanics; Jito block-engine bundle/tip auction documentation (public docs) — the cost structure that dominates Solana sniping.
- Uniswap V2/V3 and PancakeSwap router `addLiquidity` semantics (public docs) — the EVM launch event the mempool listener targets.
- DEX Screener / GeckoTerminal new-pool and trending feeds — the crowd-discovery latency the edge depends on.
- Honeypot/rug detection literature and tools (Honeypot.is, GoPlus security, Token Sniffer) — the basis for the pre-buy safety filter; see also [[cryptodataapi]] `dex/security`.
- Practitioner accounts of sniper-bot economics and the priority-fee auction's erosion of edge (2024-2025 Solana meme cycle) — evidence for the decay documented in frontmatter.
- Related wiki strategies: [[memecoin-sniping]], [[jito-bundle-sniping]], [[token-migration-sniping]], [[mev-strategies]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain (the launch universe)
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum) — crowd-attention signal
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection) — second-opinion safety gate
- `GET /api/v1/dex/token/{chain}/{address}` — token info + top pools (depth for ticket sizing)
- `GET /api/v1/dex/promoted` / `GET /api/v1/dex/promoted/top` — recently promoted tokens (marketing-spend signal that a crowd may arrive)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + `meme_season` flag (the strategy's on/off gate)

**Historical / regime data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history
- `GET /api/v1/meme/regime` — per-asset meme lifecycle classifier (euphoric/distribution/ignition/bleeding/dormant)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/new-pools"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/security/solana/<TOKEN_ADDRESS>"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]]. Note: the *latency-critical* mempool/Geyser stream is not a CryptoDataAPI product — use it for universe discovery, safety second-opinions, and regime gating, not for the same-block race itself.

## Related

- [[memecoin-sniping]] — the closely related speculative launch-trading strategy in the fungible-token space
- [[jito-bundle-sniping]] — the Solana bundle/tip-auction mechanics that dominate sniping costs
- [[token-migration-sniping]] — sniping the bonding-curve→AMM migration specifically
- [[mev-strategies]] — the broader on-chain extraction family; also the source of sandwich risk
- [[telegram-bot-trading]] — the trader-facing tooling layer (Maestro, Banana Gun, BonkBot)
- [[on-chain-flow-trading]] — using on-chain flow rather than the mempool race
- [[sentiment-trading]] — social-momentum reading for exit timing
- [[slippage]] — the execution cost that caps ticket size on thin launch pools
- [[airdrop-farming]], [[defi-yield-farming]] — lower-variance crypto-native strategies
- [[algorithmic-trading]] — the automation framework
- [[edge-taxonomy]] — where this sits among the six edge categories
- [[failure-modes]], [[when-to-retire-a-strategy]] — the kill-criteria framework
- [[cryptodataapi]] — the data layer; see [[cryptodataapi-dex]]
