---
title: "Memecoin Sniping"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [crypto, memecoins, sniping, pump-fun, raydium, solana, degen, bots, high-risk, token-launch, algorithmic]
aliases: ["Memecoin Trading", "Token Launch Sniping", "Pump.fun Sniping", "Degen Sniping"]
strategy_type: algorithmic
timeframe: scalp|day
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [latency, informational, risk-bearing]
edge_mechanism: "Late retail buyers, FOMO traders and slower bots are on the other side; they pay snipers a premium for the right to buy after price discovery has begun."
data_required: [solana-geyser-stream, pump-fun-program-events, raydium-pool-creations, holder-distribution, dev-wallet-history]
min_capital_usd: 500
capacity_usd: 2000000
crowding_risk: high
expected_sharpe: null
expected_max_drawdown: 0.95
breakeven_cost_bps: null
decay_evidence: "Pre-bond Pump.fun win rates fell from ~10% (early 2024) to <1% by mid-2025 before XXYY-style filters lifted top-quartile rates back to ~20%. See [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]."
related: ["[[telegram-bot-trading]]", "[[mev-strategies]]", "[[liquidity-sniping]]", "[[copy-trading]]", "[[2024-meme-coin-supercycle]]", "[[sniping]]", "[[pump-fun-bonding-curve-sniping]]", "[[token-migration-sniping]]", "[[jito-bundle-sniping]]", "[[axiom-pro]]", "[[bonkbot]]", "[[trojan-bot]]", "[[banana-gun]]", "[[maestro-bot]]", "[[photon-sol]]", "[[gmgn]]", "[[bullx]]", "[[holder-concentration-analysis]]", "[[rug-detection-checklist]]", "[[cryptodataapi]]"]
---

Memecoin sniping is the practice of using automated bots to buy newly launched [[meme-coins]] within seconds of liquidity being added to a DEX. The strategy targets the explosive price appreciation that occurs when memecoins launch on platforms like [[pump-fun|Pump.fun]] ([[solana|Solana]]), [[raydium|Raydium]], or Base DEXs and attract viral attention. Snipers aim to be among the first buyers, riding the initial pump before selling into retail demand. This is an extremely high-risk, high-reward strategy — the vast majority of memecoins go to zero, but early entries on tokens that gain traction can return 10-1000x within hours. The strategy is bot-driven, requires fast execution, and sits at the intersection of technical infrastructure and social-media sentiment reading. It is the most contested sub-game inside the [[meme-coin-cycle]], and the canonical example of a Solana-native execution race built on top of [[mev]] infrastructure. See [[sniping]] for the broader taxonomy and [[low-cap-crypto-trading-map]] for where it sits in the wider stack.

> ⚠️ **Risk warning — read first.** Memecoin sniping is among the highest-loss-probability activities in all of trading. The base rate for an unfiltered snipe is a near-total loss (-90% to -100%). Rug pulls, honeypots, MEV sandwiching, and bot-operator custodial theft can each independently wipe an entire bankroll. Treat any capital deployed here as already lost; size accordingly. This page is descriptive, not an endorsement.

## Edge Source

Memecoin sniping draws on three of the five edge categories from [[edge-taxonomy]]:

1. **Latency edge** - landing in the first 1-3 slots after liquidity exists, before slower bots and retail can buy.
2. **Informational edge** - knowing which devs/wallets are credible (via [[copy-trading]] of proven snipers), which call-channels move markets, and which filter heuristics actually predict survival.
3. **Risk-bearing edge** - tolerating a 90%+ loss rate per trade in exchange for fat-tailed winners. Most market participants psychologically cannot do this, which is why the edge persists.

## Why This Edge Exists

The other side of the trade is, in roughly equal parts:

- **Retail FOMO buyers** who arrive after a token has already 5-50x'd and pay snipers' exit prices
- **Slower bots** lacking Jito-bundle access or co-located RPCs
- **Call-channel followers** who buy on Telegram/Discord pumps minutes after the original alpha was distributed

These cohorts keep losing because the structural information asymmetry persists: by the time a token is "trending," the original snipers have already exited or are exiting into the volume. Memecoin markets behave like a continuous Ponzi where each cohort is the exit liquidity for the previous one; snipers are simply the earliest cohort. This dynamic is the micro-scale engine of the broader [[meme-coin-cycle]].

## Launch Lifecycle and Entry Points

A memecoin's life has several discrete moments, each a distinct snipe opportunity with its own risk profile. Understanding which moment you are sniping is the first decision:

| Stage | What happens | Snipe technique | Risk profile |
|-------|-------------|-----------------|--------------|
| **Mint / deploy** | Token created, bonding curve seeded | First-block buy on the curve — see [[pump-fun-bonding-curve-sniping]] | Highest rug risk; lowest entry price |
| **Early curve** | First buyers climb the deterministic curve | Filter-then-buy within first 30-60s | Bundle/sybil risk dominant |
| **Bonding-curve completion** | Cumulative buys hit graduation threshold (~$69k MC historical) | Detect bond completion, pre-position | Race against other bots |
| **Migration to AMM** | Curve closes; liquidity seeds a fresh [[raydium\|Raydium]]/[[pumpswap\|PumpSwap]] pool | [[token-migration-sniping]] — first market buy on new pool | Discovery-lag arb; listing-block volatility |
| **Post-migration / trending** | Dexscreener discovery, CT virality, FOMO wave | Momentum/breakout entry, NOT a snipe | You are likely exit liquidity here |

The earlier the entry, the higher both the upside multiple and the probability of total loss. Snipers who specialize tend to pick one or two stages and build dedicated infrastructure for them rather than chasing the whole lifecycle.

## Risk Taxonomy

Memecoin sniping carries layered, partly-independent risks. Any single one can cause near-total loss; they compound:

| Risk | Mechanism | Mitigation | Residual exposure |
|------|-----------|------------|-------------------|
| **Rug pull** | Dev/LP removes liquidity or dumps held supply | [[rug-detection-checklist]], dev-wallet blocklist, LP-burn check | High — new rug techniques outrun filters |
| **Honeypot** | Contract permits buys but blocks sells | Simulate a sell pre-buy; honeypot scanners | Medium — time-delayed honeypots evade checks |
| **MEV sandwich** | Frontrun buy + backrun sell taxes your fill | [[jito-bundle-sniping\|Jito bundles]] (atomic, unsandwichable) | Low if bundled; high on naive RPC |
| **Bundle/sybil launch** | Dev pre-buys via many wallets, dumps on snipers | [[holder-concentration-analysis]], top-N concentration filter | Medium |
| **Bot competition** | Faster bots win the block; you get the swept price | Tip optimization, co-located RPC, ShredStream | Structural — edge decays as competition rises |
| **Custodial bot rug** | Telegram bot operator steals keys/funds | Use non-custodial path; cap bot-wallet balance | Total loss of bot wallet if it happens |
| **Dry meta** | No winners materialize regardless of execution | Pause trading; do not force volume | Cannot be hedged; sit out |
| **Slow death** | Token bleeds out over hours; no rug, no pump | Time-stop, hard-stop discipline | -50% to -80% typical |

The defining feature is that **the median outcome is a loss** and the strategy only works because of a small number of fat-tailed winners. Anyone who cannot psychologically tolerate a long string of losers should not run this strategy — see the risk-bearing edge above.

## Null Hypothesis

Under no-edge / random conditions:

- A naive buyer of every Pump.fun launch should achieve a return matching the average curve outcome - approximately -90% to -99% per coin given that ~99% never bond.
- Random sells (e.g. holding for 1 hour then market-selling) should produce a sharply negative expected return after fees, slippage, and rug losses.
- Win rates on un-filtered snipes are reported at ~1% pre-2025 (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]).

A real edge must outperform "buy random new token, hold 1 hour, market-sell" by enough to cover the cost of infrastructure, gas, bot fees, and rugs.

## Rules

### Entry

- Subscribe to Pump.fun program events (`6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`) via geyser/[[bitquery]]
- On new mint, run filter stack within <100ms:
  - Holder distribution: reject if top 5 wallets hold >50% (bundle indicator)
  - Dev-wallet history: reject if dev has >3 prior rug pulls
  - Bonding-curve velocity: prefer tokens with >5 unique buyers in first 30s
  - Liquidity at launch: reject if initial SOL liquidity < threshold
- Submit buy via [[jito-bundle-sniping|Jito bundle]] with tip sized to current competition

### Position sizing

- Each snipe sized at 0.5-2% of total sniping bankroll
- Total sniping bankroll typically <10% of overall portfolio
- Never size based on conviction - the win rate is too low for sizing-on-conviction to converge

### Exit

- Tiered take-profit: scale out 30-50% at 3-5x, another 25-30% at 10-20x, leave a moonbag of 10-25% to ride
- Hard stop: market-sell entire position if price falls 50% from entry within first 10 minutes
- Time-based stop: market-sell after 4 hours if position is below 2x

### Sizing notes

- Slippage tolerances of 10-20% are normal at launch and should be priced in
- Priority fees / Jito tips are part of the entry cost; track separately for true PnL

## Implementation Pseudocode

```python
# Simplified sniper loop
geyser = subscribe_pump_fun_events()
filters = RugFilter(
    max_top5_concentration=0.50,
    min_unique_buyers_first_30s=5,
    min_initial_liquidity_sol=2.0,
    blocklist=load_known_rug_devs(),
)

for event in geyser:
    if event.type != "mint":
        continue
    if not filters.passes(event):
        continue
    if dev_in_blocklist(event.dev_wallet):
        continue

    bundle = build_jito_bundle(
        buy_tx=build_buy_tx(
            mint=event.mint,
            sol_amount=bankroll * 0.01,
            slippage_bps=1500,
        ),
        tip_lamports=current_competitive_tip(),
    )
    submit_jito_bundle(bundle)

    track_position(
        mint=event.mint,
        tp_levels=[3.0, 10.0, 20.0],
        tp_fractions=[0.40, 0.30, 0.20],  # 10% moonbag
        stop_loss_pct=-0.50,
        time_stop_minutes=240,
    )
```

## Indicators / Data Used

- **Bonding-curve progress** (Pump.fun) - see [[pump-fun-bonding-curve-sniping]]
- **Holder concentration** - see [[holder-concentration-analysis]]
- **Dev-wallet rug history** - see [[rug-detection-checklist]]
- **Market-cap thresholds** - $100k / $500k / $1M as psychological S/R levels (Sajad's "2-indicator" framework, Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]])
- **Migration events** - Pump.fun -> Raydium / PumpSwap, see [[token-migration-sniping]]
- **Geyser/Yellowstone streams**, [[bitquery]] GraphQL, Birdeye, Dexscreener, GMGN

## Example Trade

A sniper bot detects a new token "DOGE2049" launched on Pump.fun with 50 SOL initial liquidity. Contract passes automated safety checks (top-5 holders 28%, dev wallet has no prior rugs, 7 unique buyers in first 30s). The bot submits a [[jito-bundle-sniping|Jito bundle]] buying 0.5 SOL worth within 3 seconds of launch at a market cap of $5,000. The token trends on crypto Twitter and reaches a $500,000 market cap within 2 hours (100x). The bot sells 50% at 20x ($10 cost becomes $100), 25% at 50x ($62.50), and the final 25% at 80x ($100). Total return: $262.50 on a $0.50 investment - a 525x return. However, the previous 15 snipes were total losses totaling $7.50. Net session profit: $255 on $15 total deployed.

## Performance Characteristics

Realistic per-trade and aggregate expectations (cost-corrected, not naive):

| Metric | Naive | Realistic (top-quartile sniper, 2026) |
|--------|-------|----------------------------------------|
| Win rate | 1-5% | 15-25% with serious filtering |
| Average winner | 5-20x | 5-20x |
| Average loser | -100% | -100% (rug) or -50 to -80% (slow death) |
| Median outcome per snipe | -100% | -90% to -100% |
| Annualised PnL (top operators) | n/a | Highly variable; reportedly 5-20x bankroll in good metas, -50% in bad ones |

Naive backtests showing positive PnL almost always omit slippage, Jito tips, failed-tx gas costs, and survivorship bias in token selection. The strategy is fat-tailed; Sharpe ratios are not a meaningful measure here - tail-PnL ratios and Kelly-adjusted growth are more relevant.

## Capacity Limits

Capacity is sharply constrained:

- **Per-trade**: most Pump.fun launches have <$10k of liquidity in the first minute. Buying more than ~$500-2,000 per snipe causes >10% slippage.
- **Per-day**: a single operator can typically deploy $50k-500k/day across hundreds of snipes before hitting saturation.
- **Aggregate strategy capacity**: estimated at $1-5M per operator before the bot's own footprint distorts price discovery.

This is fundamentally a *small-bankroll* strategy. Whales cannot scale into it; their capital must go to [[copy-trading]], private call-channels, or LP provision instead.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Filter degradation** - rug techniques evolve faster than detectors. Bundled holders, hidden mint authority, and time-delayed honeypots periodically render existing filters obsolete.
2. **Latency arms race** - tip inflation eats edge. As more bots compete, expected PnL on the marginal snipe trends toward zero.
3. **Venue migration** - Pump.fun was the dominant venue 2024-2025; PumpSwap and other launchpads are taking share. Bots not adapted to new venues lose edge.
4. **Regulatory action** - bot-driven sniping at the expense of retail has obvious regulatory exposure; an SEC or EU action could shut down major bots.
5. **Custodial bot risk** - using a Telegram bot means the bot operator holds keys. A single rug by Banana Gun / Maestro / BonkBot could wipe an entire bankroll.
6. **Dry meta** - in low-volatility months, even perfect execution loses money because no winners materialize. The strategy requires an active memecoin meta to function.
7. **Honeypot epidemics** - waves of tokens that buy fine but cannot be sold trap sniper capital permanently.

## Kill Criteria

Numerical conditions for retiring the strategy (see [[when-to-retire-a-strategy]]):

- **Drawdown**: pause if rolling 30-day drawdown exceeds 60% of allocated bankroll
- **Win rate collapse**: pause if rolling 200-snipe win rate drops below 5% (filters are broken)
- **PnL trend**: retire if 6-month rolling PnL is negative *and* trending down
- **Tip inflation**: pause if average Jito tip > 30% of position size for >2 weeks
- **Honeypot rate**: pause if >20% of "passed" snipes turn out to be honeypots (filter is broken)
- **Bot rug**: immediate full exit from any bot whose operator shows signs of compromise

## Bot / Tooling Landscape

A serious sniper today picks one or more of these execution venues:

| Tool | Type | Chains | Strengths | Trade-offs |
|------|------|--------|-----------|------------|
| [[axiom-pro]] | Web platform | Solana | Promoted by top traders (e.g. Sajad); deep Pump.fun integration | Requires desktop |
| XXYY | Web platform | Solana | Industry-leading holder/bundle filters | Niche, smaller community |
| [[photon-sol]] | Web platform | Solana | Fast execution, copy-trading | Subscription cost |
| [[gmgn]] | Web platform | Multi-chain | Discovery + execution; excellent trending screens | Slightly slower than specialists |
| [[bullx]] | Web platform | Multi-chain | Pro multi-chain terminal | Steeper learning curve |
| [[bonkbot]] | Telegram bot | Solana | Original Solana TG sniper; simple UX | Higher fees than platforms |
| [[trojan-bot]] | Telegram bot | Solana | Copy-trade + sniping + portfolio | Custodial |
| [[banana-gun]] | Telegram bot | Solana, ETH, Base | MEV protection via Jito bundles; multi-chain | Fee per trade |
| [[maestro-bot]] | Telegram bot | Multi-chain | Limit orders, whale tracking, notifications | Complex fee schedule |

See [[telegram-bot-trading]] for a deeper comparison of the Telegram bot category.

## Infrastructure Stack

Serious sniping is an infrastructure game more than a "trading" game. The full stack a competitive operator assembles:

| Layer | Purpose | Typical providers |
|-------|---------|-------------------|
| **Event stream** | Detect new mints / pool creations in real time | Geyser / Yellowstone gRPC, [[bitquery]] GraphQL, Helius, QuickNode |
| **Filter pipeline** | Reject rugs/honeypots/bundles in <100ms | Custom heuristics, [[holder-concentration-analysis]], [[rug-detection-checklist]] |
| **Execution** | Land the buy first, MEV-protected | [[jito-bundle-sniping\|Jito Block Engine]], co-located RPC, ShredStream |
| **Position management** | Tiered take-profit, hard/time stops | Custom bot logic, on-chain TP/SL |
| **Discovery / analytics** | Trending screens, copy-trade targets | [[gmgn]], [[bullx]], Birdeye, Dexscreener |
| **Wallet hygiene** | Isolate bankroll, rotate wallets | Burner wallets, hardware-backed signing |

The economics: geyser subscriptions and dedicated RPC run hundreds of dollars a month; [[jito-bundle-sniping|Jito]] tips are per-trade and scale with competition. These fixed and variable costs mean a sub-scale operator is structurally disadvantaged against larger ones — the latency arms race is partly a capital arms race. Sandwich-protection economics tie this strategy directly to the [[mev]] market: the tip you pay Jito is, in part, a payment to *not* be the victim of someone else's MEV extraction.

## Edge Decay History

| Period | Median sniper outcome | Notes |
|--------|------------------------|-------|
| Jan 2024 (Pump.fun launch) | Highly profitable for any bot | Few competitors; minimal rug evolution |
| Mid-2024 | Win rates collapsing as bots multiply | Bundled-holder rugs become widespread |
| Apr 2025 | XXYY-style filters lift top-quartile win rates to ~20% | Filter quality becomes the bottleneck (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]) |
| Oct 2025 | Sajad's "$100k/$500k/$1M MC + S/R" framework popularised | Adopted by retail pros |
| Nov 2025 | Sniper-bot guides proliferate; Axiom and XXYY dominate | ~90% of early-stage memecoin volume is bot-driven |
| Dec 2025 | PumpSwap launches as native DEX for graduates | New arb opportunities between Raydium and PumpSwap |
| 2026 | "Ecosystem plays" emerge as edge shifts beyond single snipes | CoinMarketCap tracks 100+ Pump-ecosystem tokens |

## Advantages

- **Asymmetric payoffs** - small bets can generate 10-1000x returns on successful snipes
- **Automated execution** - bots eliminate emotional decision-making and ensure speed
- **Low capital per trade** - individual snipes are small, limiting downside per attempt
- **First-mover advantage** - early buyers have a structural edge over later retail entrants
- **Capital-efficient** - small bankrolls can compete; not whale-scalable

## Disadvantages

- **Extremely high failure rate** - 75-99% of sniped tokens go to zero; strategy requires high volume to find winners
- **Rug pulls and scams** - many token creators deliberately drain liquidity after attracting buyers
- **Honeypot contracts** - some tokens are coded to prevent selling, trapping sniper capital permanently
- **Bot competition** - other snipers compete for the same early blocks, driving up tips and reducing edge
- **Custodial risk** - Telegram bots hold private keys; a bot rug is a single point of failure
- **Legal and ethical grey area** - bot-driven sniping at the expense of retail buyers raises regulatory and ethical concerns
- **Psychological toll** - constant losses interspersed with rare wins requires significant mental resilience
- **Infrastructure cost** - co-located RPCs, geyser subscriptions, and tip budgets are non-trivial

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]

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

- **Universe** — `GET /api/v1/dex/new-pools` + `GET /api/v1/dex/trending` feed the candidate queue the bot filters
- **Screening** — `GET /api/v1/dex/security/{chain}/{address}` as the automated rug/honeypot gate on every candidate before capital moves
- **Regime gate** — `GET /api/v1/meme/regime/score` (`meme_season` flag) sizes the whole book up or down; per-asset `GET /api/v1/meme/regime/{symbol}` (euphoric/distribution/ignition/bleeding/dormant, 60d history) stages the exit ladder
- **Backtest** — same-block entries are un-replayable from REST; validate the post-entry take-profit ladder on `GET /api/v1/backtesting/klines` (1m only since 2026-03-30, growing forward) and treat naive win-rate backtests as inflated
- **Tips** — nearly every snipe target carries `new_listing` / `insufficient_history` flags — handle them explicitly; keep discovery/regime polling on cached endpoints and spend the latency budget on execution only

## Related

- [[sniping]] - parent concept page
- [[meme-coins]], [[meme-coin-cycle]] - the asset class and the boom/bust cycle this strategy lives inside
- [[telegram-bot-trading]] - the primary retail interface for executing memecoin snipes
- [[mev]], [[mev-strategies]] - the block-level competition and extraction dynamics snipers must defend against
- [[solana]], [[pump-fun]] - the dominant chain and launchpad for the strategy
- [[liquidity-sniping]] - the broader strategy of detecting and trading new liquidity events
- [[pump-fun-bonding-curve-sniping]], [[token-migration-sniping]], [[jito-bundle-sniping]] - sub-techniques
- [[copy-trading]] - an alternative approach of following successful memecoin traders
- [[holder-concentration-analysis]], [[rug-detection-checklist]] - survival filters
- [[low-cap-crypto-trading-map]] - where sniping sits in the broader low-cap stack
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] - methodology
- [[axiom-pro]], [[bonkbot]], [[trojan-bot]], [[banana-gun]], [[maestro-bot]], [[photon-sol]], [[gmgn]], [[bullx]] - tooling
