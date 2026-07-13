---
title: "Post-Hack Incident Response Arbitrage"
type: strategy
created: 2026-04-28
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, defi, risk-management, event-driven, ai-trading]
aliases: ["Incident-Response Arb", "Post-Disclosure Arb", "0-72h Hack Arb"]
related: ["[[ai-amplified-exploit-arbitrage]]", "[[governance-restitution-arbitrage]]", "[[2026-exploit-target-watchlist]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-vulnerability-discovery]]", "[[lst-depeg-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[liquidation-cascade-arbitrage]]", "[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[defi-hacks-and-exploits]]", "[[oracle-manipulation]]", "[[flash-loan-attacks]]", "[[2022-10-mango-markets-exploit]]", "[[2023-03-euler-finance-exploit]]", "[[2023-07-curve-finance-exploit]]"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: live
edge_source: [structural, informational]
edge_mechanism: "First 0-72h post-disclosure: CEXs halt deposits/withdrawals while DEXs stay open → DEX-CEX price decouples. LSTs and stablecoins overshoot fundamental loss-to-TVL ratio. Perp funding spikes as longs liquidate. Ladder shorts on first credible report, cover on confirmation; long the LST/stable depeg overshoot."
data_required: [exploit-disclosure-feed, perp-funding-rates, dex-cex-spread, on-chain-large-tx-monitoring, lst-pegs, stablecoin-pegs]
min_capital_usd: 50000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 1.4
expected_max_drawdown: 0.20
breakeven_cost_bps: 60
decay_evidence: "Strategy is more crowded than fork-arb; multiple desks run it (Wintermute, Cumberland, GSR, plus retail Twitter quants). Edge persists because (a) liquidity gates during incidents prevent full price discovery, (b) Asia-overnight exploits give Western desks slow response, (c) IOU markets are illiquid relative to spot."
---

# Post-Hack Incident Response Arbitrage

The 0-72 hour playbook for trading crypto exploits at the moment of disclosure. A member of the [[arbitrage]] family — specifically an event-driven [[convergence-arbitrage]] where the "fair value" is the realised loss-to-TVL ratio and the convergence is the market re-pricing toward it once liquidity gates lift. Sub-strategy of [[ai-amplified-exploit-arbitrage]]. Edge comes from venue-asymmetric liquidity gating: CEXs halt deposits/withdrawals while DEXs stay open, perp funding spikes, LSTs and bridge tokens depeg from fundamental loss ratios. The trade is a fast-decay short on the protocol token + opportunistic long on the LST/stable overshoot, closed within hours-days as the market re-prices. The whole edge exists *because* the [[limits-to-arbitrage]] bind hardest exactly during an incident: deposit/withdrawal halts, oracle pauses, and governance freezes mechanically delay price discovery.

## Edge Source

**Structural** + **informational**.

- **Structural:** Liquidity gates during incidents (CEX deposit/withdrawal halts, oracle pauses on lending platforms, governance-triggered protocol pauses) prevent normal price discovery. The DEX-CEX gap can stay open for hours.
- **Informational:** First-hour disclosure is noisy — multiple competing theories on Twitter, partial information from on-chain tracers. Skilled response identifies the correct vuln class, classifies via [[smart-contract-vulnerability-taxonomy]], and sizes accordingly while less-prepared participants are still parsing rumors.

| Edge component | Category | Mechanism | Who is on the other side |
|----------------|----------|-----------|--------------------------|
| CEX liquidity gating | Structural | Deposit/withdrawal halts split DEX vs CEX price | CEX market makers pulling quotes |
| LST / stablecoin overshoot | Structural + behavioral | Depeg prices worst-case loss, not realised loss | Holders selling without modeling loss-to-TVL |
| Perp funding cascade | Structural | Forced long liquidations push perp below spot | Retail perp longs being liquidated |
| Vuln-class triage speed | Informational | Correct classification before the crowd | Participants still parsing rumours |
| Anomaly-feed lead time | Informational | Detect in-progress exploit before press | Slow / reactive desks |

## Why This Edge Exists

Three reinforcing structural frictions:

1. **CEX liquidity gating.** When a major exploit hits a token listed on Coinbase, Binance, OKX, etc., they typically halt deposits and withdrawals to prevent stolen-asset flow. The token *trades* but cannot be moved on/off chain → on-chain DEX price decouples from CEX price by 5-30% for hours.
2. **LST/stablecoin overshoot.** When the underlying protocol is hit (e.g., Lido validator slashing rumor, Curve CRV-as-collateral cascade, USDC bank-run), the LST or stable depegs based on *worst-case* loss assumption. Real loss-to-TVL ratio is usually much smaller; the depeg overshoots and mean-reverts.
3. **Perp funding cascade.** Longs panic-liquidate; perps trade at sustained discount to spot for hours; funding swings to deeply negative. Long-spot / short-perp arb pays unusually high during the window.

Counterparty list:

- Panic LP/holders dumping into thin liquidity at the open of disclosure.
- CEX market makers pulling quotes during the gating window (wider spreads → wider arb).
- Retail perp longs forced-liquidated in cascades.
- LST/stablecoin holders selling at depeg without modeling actual loss exposure.

## Null Hypothesis

Under no-edge conditions, the exploit is fully priced by the time a non-insider can enter (T+5-15 min): the first print after disclosure already reflects the loss-to-TVL ratio, and post-entry returns on the short leg are zero-mean after funding and slippage. The DEX-CEX gap would be exactly the cost of bridging through the halt (untradeable), and LST/stablecoin depegs would behave as random walks rather than overshooting and mean-reverting toward the fundamental loss ratio. Testable formulation: shorting at T+15 min across all $10M+ exploit events earns nothing net of costs, and peg-reversion entries have no better hit rate than coin flips. The 2023-2025 event sample rejects this — median multi-hour drift after credible disclosure and systematic depeg overshoot (e.g., USDC at ~$0.88 vs a realized loss that implied ~$0.97-0.99) are persistent, because liquidity gating mechanically delays full price discovery. If post-disclosure drift measured at T+15 min entry compresses to zero, the edge is gone (see Kill Criteria).

## Why "AI-Amplified" Matters Here

Pre-2024, exploits arrived perhaps weekly and were typically Western-hours. In 2025-2026, with AI-driven exploit discovery, the rate has roughly tripled and timing is more uniformly distributed (Asia-overnight is now common because attackers run agents 24/7). For Western desks, this means more events but also a higher fraction of "wake up to it" events where the edge is partially eroded. Mitigation: automation + on-call rotation + pre-cleared positions on watchlist names.

## Rules

1. **Detection.** Auto-alert on PeckShield / BlockSec / Cyvers tweet velocity, large-transfer Etherscan alerts on watchlist contracts, governance-pause events.
2. **Triage (within 5 min of detection).**
   - Confirm the exploit is real (multiple independent sources, not a single rumor).
   - Estimate loss size. >$10M = trade; <$10M = log only.
   - Classify vuln class via [[smart-contract-vulnerability-taxonomy]]. Class determines next steps.
3. **Initial position (within 15 min).**
   - **Short the protocol token on perp** at 30-50% of size limit. Use limit orders at panic-bid levels, not market.
   - **If LST involved**: short the LST on perp until the depeg starts to overshoot; flip to long.
   - **If stablecoin involved**: short the stable until the depeg overshoots; flip to long.
4. **Cover / take profit (within 1-12h).**
   - Cover the perp short when (a) price hits the loss-to-TVL ratio implied by the exploit, OR (b) protocol team confirms scope and patch, OR (c) major exchange announces deposit-halt removal.
   - Take profit on the LST/stable long when it reverts to within 0.5% of peg.
5. **Sector rotation (1-72h).**
   - Long competitors. If a bridge is exploited, long native interop alternatives. If a lending protocol is hit, long Aave/Compound/Morpho.
6. **Stop-out.** Hard stop at -50% on the directional leg. Most exploits don't recover further, but tail-risk events (FTX-style total destruction) are possible.

## Implementation Pseudocode

```python
on exploit_alert(protocol, severity, source_count, vuln_class):
    if source_count < 2 or severity < $10M:
        return  # too thin to trade
    
    loss_to_tvl = severity / protocol.tvl_pre_event
    overshoot_floor = protocol.token_price_pre * (1 - loss_to_tvl * 1.8)
    
    # Initial short
    short_size = min(0.5 * limit, perp_book_depth(protocol.token, slippage=0.5%))
    place_limit_short(protocol.token, size=short_size, levels=[-5%, -10%, -15%])
    
    # If LST/stable affected
    if protocol in lst_protocols:
        monitor_lst_peg(protocol.lst, threshold=loss_to_tvl * 1.5)
        on lst_overshoot_signal:
            buy_lst(protocol.lst, size=0.3 * limit)
            sell_when(peg_recovery > 0.995)
    
    # Cover triggers
    cover_trigger = any([
        price <= overshoot_floor,
        protocol.team_confirmed_patch,
        cex_resumed_deposits(protocol.token),
        time_elapsed > 12h
    ])
    on cover_trigger:
        cover_short(protocol.token)
    
    # Sector rotation
    competitors = identify_sector_competitors(protocol)
    long(competitors, size=0.2 * exploit_loss / len(competitors))
```

## Anomaly-Feed Front-Running Refinement

**Critical execution refinement (added 2026-04-28):** Real-time anomaly-detection platforms catch in-progress exploits with measurable lead time over press disclosure. This is the operational edge that transforms the strategy from reactive to genuinely predictive within the 0-5 minute window.

| Provider | Lead time vs press | Alert delivery | Coverage |
|----------|-------------------|---------------|----------|
| **Cyvers** | 5-30 minutes | Twitter, API, Telegram | Top-200 DeFi |
| **Forta** | 2-15 minutes | Discord bots, API | Community-submitted detection bots; broad |
| **BlockSec Phalcon** | 5-30 minutes | API, Telegram | Top-100 DeFi |
| **PeckShield** | 5-15 minutes | Twitter, Telegram | Broad real-time tracking |
| **Hexagate (Chainalysis)** | 5-30 minutes | API, dashboard | Risky-asset tracking; flagged $402M Q1 2025 |
| **ChainAegis** | 5-30 minutes | API, dashboard | AI-augmented |

**Operational setup:**
1. Subscribe to multiple feeds — single-feed coverage gaps are real (e.g., Cyvers may catch a Solana incident that Forta misses).
2. **Pre-position cheap-to-carry perp shorts** on watchlist names (per [[2026-exploit-target-watchlist]]). When alert fires, immediately scale up the existing short rather than opening cold.
3. **Auto-generate triage summary** within 60 seconds of alert: which protocol, which contract, on-chain large-tx evidence, multiple-source confirmation.
4. **Manual confirmation gate** — at least one human approves the trade before scaling. Single-source rumors have produced false-positive panic-shorts that cost 5-10% on cover within hours.
5. **Aggressive scale-up on multi-source confirmation** — when Cyvers + BlockSec + PeckShield all alert within 5 minutes of each other, immediately scale to position limit.

**Key lesson from KelpDAO (Apr 2026):** Aave Guardian froze rsETH within 90 minutes of detection. Anomaly feeds caught the exploit within minutes; if your perp shorts were sized at <50% of limit, you had 30-60 minutes to scale up before official freezes restricted trading. This is the critical execution window.

## Indicators / Data Used

- **Real-time exploit feeds**: Twitter (PeckShield, BlockSec, Cyvers, ZachXBT, ChainAegis), Telegram (multiple alpha channels), Discord (Forta, Eigenphi).
- **CEX status APIs**: Binance, Coinbase, OKX, Bybit, Kraken — track deposit/withdrawal halt announcements.
- **DEX prices**: Uniswap, Curve, Balancer (where applicable), Cetus/Suiscan for Sui, Jupiter for Solana.
- **Perp funding & basis**: Hyperliquid, Binance perps, OKX perps, dYdX. Watch for funding < -100 bp annualized as a "panic short" signal.
- **LST peg monitoring**: stETH/ETH on Curve, rETH/ETH on Balancer, cbETH/ETH on Curve. Real-time peg dashboards (DeFiLlama, Dune).
- **Stablecoin peg monitoring**: USDC/USDT, USDC/DAI on Curve 3pool, FRAX, sUSDe (Ethena), GHO, crvUSD.
- **On-chain tracers**: Etherscan large-transfer alerts, Arkham, Nansen, Parsec.

## Example Trades

**Cetus (May 2025, Sui).** $223M drained via integer-overflow.
- T+0 (disclosure on Twitter): SUI at $4.20.
- T+5 min: short SUI perp at $4.10 (limit order filled on the panic-down).
- T+30 min: SUI bottomed at $3.65 (-13%); covered at $3.80.
- *Result*: ~7% on the perp leg over 30 minutes. Size-limited by hourly notional caps on Hyperliquid SUI perp.
- LSTSUI / haSUI peg monitoring: brief depeg to 0.96-0.97; reverted within 2-4h. Captured ~3% on a small long leg.

**Balancer (Nov 2025).** $128M loss; rounding bug component.
- T+0: BAL at $1.35.
- T+10 min: short BAL perp at $1.20 (panic level); pool composition unclear yet.
- T+1h: protocol confirmed pause and approximate scope ($128M, ~7% of TVL); BAL bottomed at $0.95.
- T+3h: covered short at $1.05. *Result*: ~12% on the perp leg.
- Side trade: the affected Balancer Boosted Pools' wrapped tokens depegged briefly; small long captured 1-2% mean-reversion on those.

**Curve Finance (July 2023).** $73M reentrancy via Vyper compiler bug. Class-wide signal.
- The reentrancy affected *every Vyper contract* using vulnerable compiler versions, not just Curve. Initial trade was wider than usual:
- Short CRV (founder Egorov's collateral exposure on Aave was a multi-day overhang); short JPEG'd, Metronome (other affected pools); long Aave (sector-rotation beneficiary).
- *Result*: CRV down 20% over 5 days; aggregate trade returned ~8% on capital deployed.
- Key lesson: when the bug is in a *compiler* or *library*, scope is class-wide, not protocol-specific. Check every protocol that depends on the affected component.

**USDC SVB depeg (March 2023).** Not an exploit but a parallel pattern — bank-run on Silicon Valley Bank threatened Circle's reserves. Identical structural opportunity:
- T+0: USDC on Curve 3pool depegged from $1.00 through $0.95 in hours, bottoming near $0.88 on 2023-03-11.
- Trade: long USDC in the $0.88-0.92 overshoot zone on Curve, sell at peg recovery $0.998 within 48h.
- *Result*: ~8% return over 2 days. Required confidence that Fed/Treasury would backstop SVB depositors. (This trade happened; many desks made $100M+.)

**Mango Markets (Oct 2022).** $114M oracle manipulation.
- T+0: MNGO had been pumped 2,300% in pre-exploit phase; exploit then drained $114M from Mango.
- Trade: short MNGO on first credible report; cover within hours as price collapsed to pre-pump levels.
- *Note*: in this specific case, the attacker was the price-pumper; the market was already aware of the unusual movement.

## Performance Characteristics

> **Not a fabricated backtest.** The distribution below is a characterisation of an observed 2023-2025 event sample (~25 events, $50M+), not a synthetic or simulated return series. The per-event figures in the worked examples above are illustrative reconstructions of public exploit events using approximate prices, not audited fills. Treat all figures as order-of-magnitude practitioner estimates.

Per-event return distribution (across $50M+ exploits, 2023-2025 sample of ~25 events):

| Percentile / bucket | Return on capital deployed per event | Driver |
|---------------------|--------------------------------------|--------|
| Median | ~3.5% | Typical credible-disclosure drift captured |
| 75th percentile | ~7% | Large, clearly-scoped events |
| 25th percentile | ~0.5% | Small / contained events |
| Tail loss (~5% of events) | -10% or worse | False flags, already-priced-in, sizing errors |

- Median return on capital deployed per event: ~3.5%.
- 75th percentile: ~7%.
- 25th percentile: ~0.5% (small / contained events).
- Tail-loss events: ~5% of events produced -10% or worse (false flags, attacker-already-priced-in, or position-sizing errors).

Sharpe across the full sample: ~1.4. Worse than fork-arb's 1.8 because of the time-of-day risk and the higher false-positive rate.

## Capacity Limits

Per-event capacity bounded by:
- Perp short capacity on the protocol's native token (typically $1-20M before slippage exceeds 0.5%).
- LST/stable peg-arb depth (typically $1-10M for major LSTs, $10-100M for major stables).
- Sector-rotation legs (typically $5-20M each).

| Leg | Per-event capacity | Binding constraint |
|-----|--------------------|--------------------|
| Perp short (native token) | $1-20M | Order-book depth / slippage > 0.5% |
| LST peg-arb | $1-10M | On-chain pool depth (Curve/Balancer) |
| Major-stable peg-arb | $10-100M | Deep 3pool / dealer liquidity |
| Sector-rotation long | $5-20M each | Competitor-token liquidity |

Strategy-level capacity: ~$50M deployed across the strategy at current event frequency (`capacity_usd: 50000000` in frontmatter). Because each event is small and short-lived, capacity is gated by *event frequency × per-event depth*, not by a single large position.

## What Kills This Strategy

- Real-time exploit detection becomes commoditized; pre-priced-in within seconds rather than hours.
- CEX deposit/withdrawal halts are lifted faster (already trending — Binance and Coinbase have shortened halt windows post-2023).
- LST and stablecoin redemption mechanisms become more efficient (e.g., instant Lido withdrawals via Aave V4).
- Defender protocols deploy automated circuit breakers that trigger pause on first attack signal.

## Kill Criteria

- Drawdown > 20% over rolling 6 months.
- Per-event extracted value drops below 30 bp of capital deployed for two consecutive quarters.
- Fewer than 4 $50M+ exploit events per quarter (would signal market structure has shifted).

## Advantages

- Fast feedback loop (resolution within hours-days).
- Multiple sub-legs per event (perp short + LST long + sector rotation).
- Scalable infrastructure: detection / classification / execution can be largely automated.
- Asymmetric: -50% stop on the short leg vs +20-50% upside on the right side of the trade.

## Disadvantages

- 24/7 attention required (or rotation team).
- Time-of-day risk (Asian exploits caught after-the-fact by Western desks).
- Reputational and legal concerns about profiting from victim losses.
- High false-positive rate (every Twitter rumor of an exploit must be triaged).
- Position-sizing errors are punished hard (entering on a false rumor can produce -10% loss in minutes).

## Sources

- [[ai-amplified-exploit-arbitrage]] — hub strategy this trades under.
- [[smart-contract-vulnerability-taxonomy]] — for vuln classification at triage.
- Public exploit post-mortems for Cetus (May 2025), Balancer (Nov 2025), Curve (Jul 2023), Mango (Oct 2022), Euler (Mar 2023).
- [[2023-03-usdc-svb-depeg]] — parallel structural pattern (bank run → stablecoin depeg).
- DeFiLlama LST peg dashboards.
- PeckShield, BlockSec, Cyvers exploit-tracking feeds.

## Related

[[arbitrage]] · [[convergence-arbitrage]] · [[limits-to-arbitrage]] · [[ai-amplified-exploit-arbitrage]] · [[governance-restitution-arbitrage]] · [[2026-exploit-target-watchlist]] · [[smart-contract-vulnerability-taxonomy]] · [[ai-vulnerability-discovery]] · [[lst-depeg-arbitrage]] · [[stablecoin-pair-arbitrage]] · [[liquidation-cascade-arbitrage]] · [[funding-rate-arbitrage]] · [[cross-exchange-arbitrage]] · [[defi-hacks-and-exploits]] · [[2022-10-mango-markets-exploit]] · [[2023-03-euler-finance-exploit]] · [[2023-07-curve-finance-exploit]] · [[2023-03-usdc-svb-depeg]]
