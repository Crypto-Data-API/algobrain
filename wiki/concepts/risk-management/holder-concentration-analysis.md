---
title: "Holder Concentration Analysis"
type: concept
created: 2026-05-04
updated: 2026-06-11
status: good
tags: [crypto, risk-management, defi, market-microstructure, memecoin]
aliases: ["holder analysis", "wallet concentration", "top-holder scan", "bundle detection"]
domain: [risk-management]
difficulty: intermediate
prerequisites: ["[[rug-pulls]]", "[[memecoin-sniping]]"]
related: ["[[rug-pulls]]", "[[rug-detection-checklist]]", "[[pump-fun]]", "[[memecoin-sniping]]", "[[birdeye]]", "[[gmgn]]", "[[bitquery]]"]
---

Holder concentration analysis is the pre-trade practice of inspecting a token's top wallet holders, looking for evidence of bundling, dev pre-allocation, and coordinated wallet clusters before risking capital on a low-cap launch. On Solana launchpads like [[pump-fun|Pump.fun]] — where thousands of new tokens appear daily and the great majority are scams or exit-liquidity traps — this scan is the single highest-leverage filter a trader can run, often discarding 80-99% of candidate plays in seconds. It is the most quantitative leg of the [[rug-detection-checklist|rug detection checklist]] and the foundation of nearly every serious sniper bot's filter stack.

## Why concentration matters

A new memecoin's holder distribution determines who controls the float and therefore who controls the price. Three patterns predict near-certain losses for outside buyers:

1. **Bundled launches** — the deployer used a single transaction or atomic bundle (e.g., via [[jito-bundling|Jito]]) to buy a large fraction of supply across many wallets. These wallets look diverse on-chain but are one entity. They will dump in coordination on the first wave of organic buyers.
2. **Dev / insider over-allocation** — the contract deployer or a small set of pre-launch wallets hold a disproportionate share (often 10-50%+). They have full control of supply and zero cost basis.
3. **Sniper concentration** — the first ~1-20 buyers (sniper bots competing for block-zero entry) hold the majority of circulating tokens. Even with no malicious intent, their exit will crush the chart.

A useful framing: if the **top 10 holders excluding the LP and burn address** control more than ~30-40% of supply on a fresh Pump.fun launch, that is a strong concentration signal that may indicate coordinated allocation, insider distribution, or dangerous low-float risk — those wallets can dump into your buys at will. Concentration alone does not *prove* a distribution scheme (some legitimate community launches seed multiple wallets intentionally), but as a pre-trade *filter* it correctly discards the large majority of structurally hostile launches.

## What to look for

### Bundling signals

- **Same-block or same-bundle buys** — multiple wallets purchasing within the deploy transaction or the immediately following Jito bundle.
- **Funding from one source wallet** — top holders all funded by the same wallet (often the dev's hot wallet) shortly before launch.
- **Identical buy sizes** — top 10 wallets each holding ~1-3% with near-identical SOL spend, a fingerprint of bundle-buy software.
- **Transaction-graph clustering** — wallets that share intermediaries, deposit addresses, or CEX off-ramps. Tools like [[bitquery|Bitquery]] and Arkham expose these graphs.

### Dev wallet behavior

- **Dev wallet % held** — Pump.fun deployers default to 0% supply at deploy, so any dev holding above the bonding-curve baseline is a flag.
- **Dev wallet cluster** — the deployer EOA plus any wallets it funded in the prior 24 hours. Sum these.
- **Multi-token deployers** — if the deployer has launched 50 tokens in the last week and rugged 49, the prior is overwhelming.
- **Funding origin** — wallets freshly funded from Tornado Cash, FixedFloat, or other no-KYC bridges immediately before deploy correlate with rugs.

### Holder list shape

- **Top 10 % of supply** — under ~15% on a post-bond token is a reasonable bar; over ~25% on a fresh launch is a near-automatic skip.
- **Number of unique holders relative to age** — a 10-minute-old token with 500 unique holders is organic; with 30 holders, it's a few wallets passing the bag.
- **Holder-count growth rate** — accelerating linearly with volume = organic; flat with rising MC = bundlers walking the price.
- **Whale top-up patterns** — single wallets adding aggressively after the initial pump are a different (and sometimes tradable) signal than dev distribution.

## Tools that automate this

| Tool | What it shows | Notes |
|------|---------------|-------|
| [[birdeye|Birdeye]] (`birdeye.so`) | Top holder list, holder count, whale activity, Pump.fun leaderboards | First-stop scanner for Solana low-caps |
| [[gmgn|GMGN]] (`gmgn.ai`) | Bundle %, dev wallet %, sniper %, top 10 %, holder PnL distribution | Most popular all-in-one rug filter for Solana memecoins |
| [[bitquery|Bitquery]] (`bitquery.io`) | GraphQL feed of Pump.fun trades and holder snapshots | Powers custom dashboards and bot filters |
| Dexscreener + boosts | Holders tab, links to GMGN/Birdeye for one-click verification | Primary chart UI; not a real concentration tool by itself |
| SolanaFM | Tx decoding and wallet labeling | Useful for tracing bundle funding |
| Photon / [[axiom-pro|Axiom Pro]] / [[trojan-bot|Trojan]] | Inline rug-check panel before buy click | Embeds top-holder, bundle-%, and dev-% in the order ticket |
| XXYY bot | Pre-bond holder filtering with auto-skip rules | Marketed as raising sniper win rates from ~1% to 20%+ via this filter |

In practice, serious sniper workflows pipe new mints through GMGN or an Axiom-style ticket and reject anything failing thresholds before a human ever sees the chart. Note that the exact metric labels and calculations differ across platforms — GMGN's "bundle %" is not computed identically to Photon's, and holder snapshots can disagree second-to-second — so treat the numbers as directional risk indicators rather than a standardized cross-tool schema, and confirm a borderline read on a second tool before sizing.

## A typical pre-trade scan (Pump.fun)

1. Token appears on Dexscreener / a sniper bot feed.
2. Open GMGN or Birdeye on the contract.
3. Check **bundle %**: skip if > ~10-20% bought in deploy bundle.
4. Check **dev %**: skip if dev (and dev-funded cluster) > ~5%.
5. Check **top 10 holders %** (excluding bonding curve / LP): skip if > ~25-30% on a fresh launch.
6. Check **holder count vs. age**: skip if growth is flat or supply is held by < ~50 wallets at non-trivial MC.
7. Check **dev wallet history**: skip if deployer has prior rugs in the last 24-72 hours.
8. Only then look at the chart, narrative, and [[market-cap-level-trading|MC level structure]].

The whole sequence takes 5-10 seconds with the right tooling and is the difference between a viable sniping process and gambling.

## Examples of patterns

- **Bundle-and-dump**: 8 wallets each buy 2.5% in the deploy bundle, walk the price up to ~$200k MC over 4 minutes, then dump simultaneously. Outside buyers see "20% top holders" pre-trade.
- **Dev sneak**: deployer holds 0% on contract but funded 3 wallets with 1.5 SOL each 2 minutes pre-launch from a freshly bridged address; those wallets accumulate 12% of supply through "organic-looking" market buys.
- **Sniper congestion**: a viral narrative attracts 200 sniper bots in block 0; top 20 wallets end up holding 60% with sub-penny cost basis. Even without malice, the next $50k of buys will be sold into immediately.

## Limitations

- **Cluster detection is probabilistic.** Sophisticated rugs split funding across many hops, age wallets for weeks, and route through CEX deposits to break the on-chain trail. The cleanest-looking holder list can still be one entity.
- **Post-migration shifts.** After a Pump.fun → [[raydium|Raydium]] or [[pumpswap|PumpSwap]] migration, holder composition resets meaningfully and snapshots taken pre-bond may stop being predictive.
- **Tools lag the chain.** GMGN/Birdeye snapshots can be seconds to minutes stale during high-throughput launches; a "clean" scan can miss a dump already in flight.
- **False positives.** Some legitimate community launches use multi-wallet seeders intentionally; not every clustered launch is a scam, just most of them.
- **Concentration alone is not edge.** It is a *filter*. Profitability still depends on entry timing, [[market-cap-level-trading|MC level]] reads, exit discipline, and avoiding the long tail of soft rugs that pass the scan.

## Related

- [[rug-pulls]] — the conceptual / historical page on rug pulls
- [[rug-detection-checklist]] — the broader pre-trade checklist that wraps this scan
- [[pump-fun]] — the launchpad where this analysis matters most
- [[memecoin-sniping]] — the strategy class this filter underpins
- [[birdeye]], [[gmgn]], [[bitquery]] — primary tools
- [[market-cap-level-trading]] — what to do *after* a token passes the scan

## Sources

- [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]] — Pump.fun ecosystem and tooling overview
- Public documentation of GMGN (`gmgn.ai`), Birdeye (`birdeye.so`), and Bitquery (`bitquery.io`) Pump.fun / Solana token APIs — top-holder, dev-wallet, bundle, and sniper metrics
- Bitquery, *Pump Fun API* docs and *How to detect bundled / sniper buys on Solana* guides — methodology for transaction-graph clustering and same-bundle detection
- Arkham Intelligence — entity-clustering and funding-trace tooling referenced for cross-wallet attribution
- Perplexity verification (June 2026) confirming the current tool set (GMGN, Birdeye, Bitquery, Axiom, Photon, Trojan) and that concentration is a risk indicator rather than definitive proof of a scheme
