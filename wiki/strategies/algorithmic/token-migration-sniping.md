---
title: "Token Migration Sniping"
type: strategy
created: 2026-05-04
updated: 2026-07-19
status: excellent
tags: [algorithmic, crypto, scalping, event-driven]
aliases: ["Migration Sniping", "Pump.fun Migration Snipe", "Bond-to-Raydium Sniping", "Graduation Sniping"]
related: ["[[pump-fun]]", "[[raydium]]", "[[pumpswap]]", "[[memecoin-sniping]]", "[[bitquery]]", "[[jito-bundle-sniping]]", "[[axiom-pro]]", "[[trojan-bot]]", "[[pump-fun-bonding-curve-sniping]]", "[[low-cap-crypto-trading-map]]", "[[cryptodataapi]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: live
edge_source: [latency, structural]
edge_mechanism: "When a Pump.fun token's bonding curve completes (~$69k MC cumulative buys), the token 'graduates' and migration to Raydium (or PumpSwap) is triggered. Migration creates a discrete liquidity event: a fresh AMM pool is seeded, the price discovery regime changes from a deterministic curve to a CPMM, and a wave of FOMO buyers arrives at the new venue. Volatility on the listing block and minute is dramatically higher than steady-state. Snipers detect the migration tx via API/RPC alerts and front-run retail by being the first market buyer on the new pool."
data_required: [pump-fun-launch-events, bonding-curve-progress, raydium-pool-creation-events, pumpswap-pool-creation-events, jito-bundle-feed, holder-distribution]
min_capital_usd: 500
capacity_usd: 2000000
crowding_risk: high
expected_sharpe: null
expected_max_drawdown: 0.7
breakeven_cost_bps: 300
decay_evidence: "Pump.fun launched Jan 2024. Migration sniping was a high-edge meta in 2024; PumpSwap (Pump.fun's native DEX, launched March 20, 2025) made migrations instant and free and became the default venue, ending the Raydium-specific migration-lag arb. Bot competition compressed first-block advantage to single-slot precision; manual snipers are no longer competitive on graduations alone."
---

# Token Migration Sniping

**Token migration sniping** is the practice of buying a [[solana|Solana]] [[meme-coins|memecoin]] in the same block (or within seconds) of its bonding-curve completion and migration from [[pump-fun|Pump.fun]] to a public AMM venue — historically [[raydium|Raydium]]; since March 2025, [[pumpswap|PumpSwap]] (Pump.fun's native DEX, the default migration venue from its March 20, 2025 launch). The migration event is a **discrete liquidity and price-discovery regime change**: bonding-curve buyers convert into liquid AMM positions, a fresh pool is seeded, and a fresh wave of dexscreener-discovered buyers arrives. Listing-block volatility is observed at 5-50x the steady-state baseline, and the first executed buy on the new pool typically captures most of that move. It is one of the cleaner, more programmable variants of [[memecoin-sniping]] and a recurring profit point inside the [[meme-coin-cycle]]; see [[sniping]] for the parent taxonomy.

> ⚠️ **Risk warning — read first.** Migration sniping is lottery-shaped: the median trade is a loss and the strategy depends entirely on a small right-tail of large winners. Most graduating tokens rug, dump, or stall within hours. You are racing well-capitalized bots for a fill on a thin, freshly-seeded pool — execution risk, [[mev]] sandwich risk, and rug risk are all live simultaneously. Size each snipe as capital you have already written off.

## Edge Source

**Latency** + **structural**.

- **Latency:** Migration is a single on-chain transaction. Bots that detect the bond completion and submit a buy in the same slot (or the next slot) capture pricing that retail will not see on charts for tens of seconds.
- **Structural:** The migration event is a *protocol-defined* state transition, not a continuous market. The bonding curve ends at a deterministic threshold; the AMM seed amount is deterministic; the order-of-operations is predictable. This makes the opportunity programmable in a way that subjective alpha is not.

There is no informational edge in the source-document sense — the migration trigger is publicly observable on-chain. The edge is purely *who acts on it first*.

## Why This Edge Exists

Pump.fun's mechanics create the structural setup:

1. A token launches on Pump.fun with deterministic bonding-curve pricing.
2. As cumulative buys grow, the price climbs the curve.
3. At the graduation threshold (SOL-denominated on the curve; ~$69k market cap at historical SOL prices, higher in USD terms as SOL appreciates), Pump.fun automatically:
   - Closes the bonding curve.
   - Seeds an AMM pool on Raydium (historically) or PumpSwap (the default venue since its March 20, 2025 launch — migrations became instant and free; see also the [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi|April 2026 gap-finder source]]) with a portion of accumulated SOL + token.
   - Burns the LP keys (irrevocable liquidity in most configurations).
4. The token is now tradeable on a public AMM at a new starting price.

Three frictions create the edge for fast bots:

1. **Discovery lag.** Manual traders watching dexscreener.com or [[birdeye-so|Birdeye]] don't see the new pool until the indexer catches up — typically 5-30 seconds after the migration block.
2. **Routing lag.** [[jupiter-exchange-solana|Jupiter]] aggregator takes time to index the new pool; until then, manual users can't easily route through it.
3. **FOMO arrival.** When discovery happens, retail piles in *as market buyers*, sweeping the order book and lifting the price.

The first programmatic buyer in the migration block captures the gap between "fresh AMM seed price" and "post-FOMO market price."

The counterparty is the discovery-lagged retail buyer who arrives 10-60 seconds late and pays the swept price.

## Migration Mechanics by Venue

The migration *destination* materially changes the edge. The 2025 shift from Raydium to PumpSwap collapsed the original lag-arb:

| Dimension | [[raydium\|Raydium]] (historical default, pre-Mar 2025) | [[pumpswap\|PumpSwap]] (default since Mar 20 2025) |
|-----------|--------------------------------------------------------|----------------------------------------------------|
| Migration cost | Migration fee charged | Instant and free |
| Discovery lag | Larger — third-party indexer + Jupiter routing lag | Smaller — native to Pump.fun ecosystem |
| Pool seed depth | ~$12k equivalent at standard config | Comparable seed config |
| LP key handling | Burned (irrevocable in most configs) | Burned per Pump.fun config |
| Edge today | Original lag-arb largely gone | Default venue; competition concentrated here |

The strategic read: the *Raydium-specific migration-lag arb is dead*. What remains is the slot-level race to be the first market buyer on whichever venue is current, plus residual discovery/FOMO lag on the broader market.

## Timing Window

Migration alpha is sharply time-concentrated. The decay profile of edge after the migration block:

| Window after migration | Typical state | Sniper action |
|------------------------|---------------|---------------|
| Slot N (migration block) | Fresh seed price; near-zero outside buyers | Land buy here — the prize slot |
| Slot N+1 to ~5s | First bots fill; price begins lifting | Acceptable if bundle landed late |
| ~5-30s | Indexers catch up; [[jupiter-exchange-solana\|Jupiter]] routes the pool | Retail discovery begins |
| 30-60s | FOMO wave sweeps the book | You are now the exit liquidity, not the sniper |
| >60s | Price discovery complete | This is a momentum trade, not a snipe |

If your bundle does not land within the first few slots, the honest move is to *not chase* — the structural edge has already transferred to whoever filled first.

## Null Hypothesis

If migration sniping had no edge, the listing-block fill price would equal the price 1-5 minutes after migration in expectation. Empirically, listing-block buys on graduating tokens that did not immediately rug have historically traded 5-50x higher within minutes (per the gap-finder source [8] and bot vendor performance pages — note these are vendor-selected examples). The null is rejected for the *winning* graduations; the strategy's challenge is the conditional distribution given that 95%+ of all bond completions still produce losses (rug, immediate dump, or no follow-through) within hours.

A more honest null: even with edge, the strategy is **lottery-shaped**. Median trade is a loss. Mean is dominated by a small number of large wins. Sharpe is unstable and likely uninformative.

## Rules

1. **Subscribe to bond-progress feed.** Monitor [[bitquery|Bitquery]] GraphQL subscriptions or a self-run Pump.fun program-account watcher (program ID `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P` per the gap-finder source).
2. **Pre-filter bond candidates** before they complete:
   - Holder concentration: top 10 holders < 40% of supply (filters bundled launches).
   - Dev wallet has not previously rugged (cross-reference rug DB).
   - Bonding curve velocity: organic-looking buys (many small wallets) vs. obvious sybil farming.
3. **Detect migration trigger.** Watch for the migration instruction in the Pump.fun program; the slot in which this lands is the target slot.
4. **Submit buy in the migration slot or next slot.** Use a [[jito-bundle-sniping|Jito bundle]] that pays a competitive tip (current floor varies; see the linked page) and includes only the buy tx (not the migration tx itself — that's not yours to land).
5. **Position size: 0.5-2 SOL per snipe.** Larger sizes hit slippage on the freshly-seeded pool and surrender most of the edge.
6. **Take-profit ladder.**
   - 50% out at +100% (2x).
   - 30% out at +300%.
   - 15% out at +1000% (rare).
   - 5% moonbag held indefinitely or to a fundamental signal.
7. **Hard stop at -50%.** No averaging down.
8. **Time stop: 15 minutes.** If the position is flat or down at +15 minutes, exit. Migration alpha is concentrated in the first minutes.

## Implementation Pseudocode

```python
# Pre-filter loop (runs continuously on near-bonding tokens)
for token in pump_fun.tokens_above_bond_progress(threshold=0.85):
    if token.holder_top10_pct() > 0.40: blacklist(token); continue
    if dev_wallet_db.has_rugged(token.dev): blacklist(token); continue
    if not buy_pattern_organic(token): blacklist(token); continue
    watchlist.add(token)

# Migration detection (subscribed to program logs)
on pump_fun_event(evt):
    if evt.kind != "migrate": return
    if evt.token not in watchlist: return

    bundle = JitoBundle(
        tip_lamports=PRIORITY_TIP,
        txs=[
            buy_tx(
                pool=evt.new_pool_address,
                size_sol=position_size(evt.token),
                max_slippage_bps=2000,  # listing block is volatile
            )
        ]
    )
    submit_bundle(bundle, target_slot=evt.slot)

    set_take_profit_ladder(evt.token, [(2.0, 0.50), (4.0, 0.30), (11.0, 0.15)])
    set_hard_stop(evt.token, -0.50)
    set_time_stop(evt.token, minutes=15)
```

## Indicators / Data Used

- **Pump.fun program logs** (via [[bitquery|Bitquery]], Helius, QuickNode, or self-run RPC).
- **Bonding curve progress** (cumulative SOL in vs. graduation threshold).
- **Holder distribution snapshots** (top-N concentration; bundle detection).
- **Dev wallet rug history** (community DBs, on-chain heuristics).
- **Raydium pool creation events** and **PumpSwap pool creation events**.
- **[[jito-bundle-sniping|Jito]] bundle infrastructure** for slot-targeted execution.
- **Mempool-equivalent feeds** (Solana lacks a true mempool; use leader-forwarded streams, ShredStream where licensed).

## Example Trade

The gap-finder source notes 5-50x post-listing pumps as the *upside tail* for migration sniping, with API alerts as the timing tool. Public, reproducible "the tape said X then Y at slot Z" examples for migration-block fills are scarce because the data lives behind bot vendor dashboards. The honest example is the *distribution shape*:

- 100 graduations sniped at 1 SOL each.
- ~60 trades stop out at -50% (rug or immediate dump): -30 SOL.
- ~30 trades take partial profits at +100% to +300%, exit roughly flat to +30%: +0 to +9 SOL.
- ~8 trades hit the +300% to +1000% ladder: +24 to +80 SOL.
- ~2 trades hit the moonbag tail (one token reaches multi-million MC): +50 to +500 SOL.

Net expected outcome per 100 trades: positive but with massive variance and heavy dependence on the tail. The strategy is structurally similar to [[pump-fun-bonding-curve-sniping|bonding-curve sniping]] — same lottery shape, different entry point.

## Performance Characteristics

**Expected Sharpe: unknown.** This strategy is too capacity-constrained, decay-prone, and tail-dependent for stable Sharpe estimation. Top operators in 2024-25 reported triple-digit APR on small books (per vendor marketing and [[axiom-pro|Axiom Pro]] community discussion), but reported numbers are not audited and are subject to severe survivorship bias.

What is defensible:
- **Win rate: 5-25%** (positive-PnL trades / total trades) depending on filter quality.
- **Average winner:** 2-5x average loser in good regimes; 1.2-2x in saturated regimes.
- **Cost floor:** ~3% round-trip (priority fee + Jito tip + AMM fee + slippage on a thin seed pool).
- **Drawdown:** -50% to -80% drawdowns are routine even for profitable books because the strategy depends on the right-tail.

## Capacity Limits

Per-trade capacity is bounded by the **freshly-seeded AMM pool depth** (typically equivalent to ~$12k of liquidity at migration in standard Pump.fun config). A buy of 1-2 SOL ($150-300) is the practical ceiling before slippage destroys the edge.

Strategy-level capacity is therefore bounded by:
- Number of qualifying graduations per day (varies; 10s to 100s in active regimes).
- Per-trade ceiling × graduation count.

A reasonable upper bound on captured edge: ~$1-2M deployed capital before the strategy runs into either (a) graduation supply, or (b) self-impact (your own fills crowd out follow-on edge).

## What Kills This Strategy

Per [[failure-modes]] and the structural realities of the Pump.fun meta:

- **Migration mechanics change.** Pump.fun has unilateral control over migration parameters (graduation threshold, AMM venue, seed amount, LP burn behavior). Any change resets the strategy.
- **PumpSwap dominance shift.** Migration to PumpSwap (the default migration venue since its March 2025 launch) routes around Raydium and around Jupiter's index, changing the discovery-lag dynamic the strategy exploits.
- **Saturation.** Multiple competing bots in the migration slot push the marginal fill toward zero edge. The bot whose buy lands first captures most of the value; everyone else gets the post-sweep price.
- **Solana network congestion.** Failed transactions during congestion mean missed migrations and wasted priority fees.
- **Pump.fun protocol risk.** Shutdown, regulatory action against the launchpad, or major UX change all kill the strategy.
- **Sybil / bundle-launch evolution.** As detection improves, launchers evolve. New bundling techniques periodically reset the holder-filter edge.

## Kill Criteria

Retire the strategy if:

- Rolling 30-day net PnL < 0 with > 200 graduations sniped.
- Daily Pump.fun graduation count drops below 5 for 14+ consecutive days.
- PumpSwap migration share exceeds 90% AND PumpSwap-specific edge cannot be replicated.
- Jito tip floor for migration-slot bundles exceeds 50% of expected per-trade gross profit.
- Pump.fun changes graduation threshold or AMM seed mechanics.

## Advantages

- **Discrete, programmable trigger.** No subjective signal; either the migration tx lands or it doesn't.
- **Decoupled from broad crypto beta.** Works in any market regime where Pump.fun has graduation flow.
- **Repeatable.** Dozens of opportunities per active day.
- **Pairs naturally with [[pump-fun-bonding-curve-sniping|bonding-curve sniping]].** A single watchlist feeds both the curve-snipe and migration-snipe entries.

## Disadvantages

- **Lottery-shaped PnL.** Median trade loses; strategy depends on the right-tail.
- **High infrastructure overhead.** Self-run RPC or paid API + Jito bundle infra + holder-filter pipeline.
- **Severe competition.** Slot-level race against well-capitalized bots.
- **Edge decay observed.** 2024 was easier than 2025; 2025 was easier than 2026.
- **Regulatory tail risk.** Any enforcement action against Pump.fun or against memecoin launchpads broadly is an instant kill event.
- **Reputational risk.** Many migrating tokens are pump-and-dump operations; participation in the early flow may be viewed unfavorably.

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]] — Pump.fun migration mechanics, PumpSwap launch, Bitquery API.
- [[pump-fun-bonding-curve-sniping]] — sister strategy on the curve side of the migration boundary.
- [[jito-solana-mev-arbitrage]] — Jito bundle infrastructure that this strategy depends on.
- [[memecoin-sniping]] — broader category context.
- Pump.fun protocol documentation (program ID `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`).
- Bitquery Pump.fun API docs — referenced in gap-finder source [8].
- PumpSwap launch date (March 20, 2025), instant/free migrations, and Raydium-to-PumpSwap default switch verified via Perplexity (sonar), 2026-06-10: cryptoslate.com/pumpfun-launches-its-own-dex-called-pumpswap-amid-falling-revenue/, en.wikipedia.org/wiki/Pump.fun.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Watchlist** — `GET /api/v1/dex/new-pools` and `GET /api/v1/dex/trending` surface bonding-curve tokens approaching graduation; the migration trigger itself comes from the on-chain program feed (Bitquery/Geyser)
- **Safety gate** — `GET /api/v1/dex/security/solana/{address}` on every watchlist candidate before the bundle path arms
- **Regime gate** — `GET /api/v1/meme/regime/score` (`meme_season` flag) gates the whole strategy; per-asset lifecycle from `GET /api/v1/meme/regime/{symbol}` stages the post-migration exit ladder
- **Backtest** — migration-slot fills are not replayable over REST; use `GET /api/v1/backtesting/klines` (1m only since 2026-03-30) for post-migration decay studies and forward-test the race itself
- **Tips** — keep CryptoDataAPI calls in the slow pre-trade loop; the latency path is Geyser → Jito bundle, per [[jito-bundle-sniping]]

## Related

[[pump-fun]] · [[raydium]] · [[pumpswap]] · [[solana]] · [[meme-coins]] · [[meme-coin-cycle]] · [[sniping]] · [[memecoin-sniping]] · [[mev]] · [[bitquery]] · [[jito-bundle-sniping]] · [[axiom-pro]] · [[trojan-bot]] · [[pump-fun-bonding-curve-sniping]] · [[jito-solana-mev-arbitrage]] · [[low-cap-crypto-trading-map]] · [[failure-modes]] · [[edge-taxonomy]]
