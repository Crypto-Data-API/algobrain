---
title: "Play-to-Earn"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
tags: [crypto, nft, gamefi, behavioral-finance, on-chain]
aliases: ["P2E", "Play to Earn", "Earn-to-Play"]
domain: [crypto, market-microstructure]
difficulty: beginner
prerequisites: ["[[gamefi]]", "[[nft]]"]
---

# Play-to-Earn

**Play-to-earn (P2E)** is a blockchain game model where players earn crypto tokens or tradeable NFTs through in-game activity — battles, tasks, breeding, quests, or simply time spent — and can convert those earnings to real economic value. Unlike traditional games where in-game assets are owned by the developer and have no exit value, P2E games run on transparent blockchains where assets are player-owned NFTs and earnings are liquid tokens tradeable on DEXs or centralised exchanges. The model reached mainstream attention with Axie Infinity in 2021, when players in the Philippines and Venezuela were earning more than local minimum wages through gameplay.

## How It Works

A P2E game's economy has four fundamental components:

1. **Entry NFTs:** To play, users must own or rent an NFT (character, equipment, land). The NFT's floor price determines the cost of participation — and the breakeven time for new players.
2. **Reward tokens:** Gameplay earns in-game tokens (e.g., SLP in Axie Infinity, GST in StepN). These are typically high-emission, low-supply-cap tokens intended to be spent on in-game actions.
3. **Sinks (burning mechanisms):** Mechanisms that consume reward tokens: breeding new NFTs, upgrading equipment, crafting. Insufficient sinks cause token inflation and game economic collapse.
4. **Liquidity and exit:** Reward tokens are listed on DEXs; players sell them to convert gameplay to real money.

**The economic sustainability condition:** A P2E game is sustainable only if:
> **daily_token_burn_value ≥ daily_token_emission_value**

When this condition breaks (almost inevitably as user growth slows), the reward token inflates and the real value of playing approaches zero. New users require NFT entry costs while earning less — the game becomes uneconomical for new participants first, then for existing ones as selling pressure mounts.

**Scholarship/delegation:** Axie Infinity pioneered "scholarship" — NFT owners (managers) lend their Axie NFTs to players (scholars) who split earnings ~30/70 or 40/60. This democratised access for players without capital and created a management layer of "guilds" like Yield Guild Games (YGG). Scholarships extract value from NFT holders' otherwise idle assets while expanding the player base.

## Concrete Examples

- **Axie Infinity (AXS/SLP, 2021 peak):** The canonical P2E game. At peak (Jul-Aug 2021), over 2 million daily active users. A scholar in the Philippines earned 150-300 SLP/day (~$30-60/day when SLP was $0.20-0.30), exceeding local minimum wage. By early 2022, SLP had fallen to $0.005 (from a peak of $0.35) as breeding emission overwhelmed sinks. The March 2022 Ronin bridge hack ($625M) dealt the final blow to user confidence. AXS governance token fell 95%+ from peak.
- **StepN (GMT/GST, 2022):** Move-to-earn variant — players earn GST tokens by walking/running with NFT sneakers tracked by GPS. At peak (Apr-May 2022), sneaker NFTs traded for thousands of dollars. GST fell from $8.00 to under $0.05 within 6 months as the user-growth flywheel reversed.
- **Gods Unchained:** Free-to-play trading card game where earned cards are NFTs tradeable on Immutable X. More game-design-first than pure P2E; sustainability has been better than pure reward-token models.
- **Pixels (PIXEL, 2024):** Migrated to Ronin and relaunched with improved sink mechanics. Demonstrated that the P2E model can be iterated on — the 2024 cohort applied lessons from 2021-22 failures.

## Trading Relevance

P2E dynamics intersect with several AlgoBrain strategy approaches:

- **[[vampire-attack-arbitrage]] analogue:** P2E launch phases are bootstrap events — the protocol overpays early players in token emissions to build critical mass. The same playbook applies: analyse emission schedule, enter early, harvest reward tokens, exit before the taper. The specific risk is that P2E games have *entry NFT costs* that create a higher breakeven than a pure token farm.
- **NFT floor price as a leading indicator:** When a P2E game's floor price for entry NFTs falls below the time-to-breakeven threshold, new user inflows stop. Monitoring floor price vs. daily token emissions on Dune Analytics or game-native dashboards provides advance warning of economic breakdown.
- **[[governance-token]] vs reward token distinction:** In two-token P2E models, the governance token (AXS, GODS, ILV) often holds value better than the reward token (SLP, GST, FLUX). Traders who stay long governance tokens after exiting reward tokens capture the slower-decaying value while avoiding the emission-driven collapse.
- **[[gamefi]] sector rotation:** P2E tokens exhibit strong sector-beta during crypto bull markets (new game announcements, viral growth stories) and disproportionate drawdowns in bear markets. The [[multi-strategy-crypto-portfolio]] memecoin/convexity sleeve might include early-stage P2E launches but requires hard cap sizing (≤ 3-5% NAV total) due to smart-contract and economic collapse risk.
- **On-chain activity metrics:** P2E games generate high-frequency on-chain data — daily active wallets, token burn rates, NFT sales volume — that can be monitored as leading indicators of game health and token price direction before it appears in price action.
- **Strategy pages:** [[gaming-gamefi-basket]] (sector perp basket), [[unlock-heavy-basket]] / [[unlock-aware-momentum]] (vesting cliffs, which most P2E governance tokens carry), and [[nft-trading]] (the entry-NFT layer).

### A worked breakeven check

Using this page's own Axie numbers: an entry team costing **$1,000** of NFTs, a scholar earning **150 SLP/day**, and SLP at **$0.25** give $37.50/day gross. An owner playing their own team breaks even in ~27 days. A manager keeping 30% of a scholar's earnings (~$11/day) needs ~89 days. At SLP $0.05, the owner-player needs ~133 days. At $0.005 (early-2022 levels) the owner-player needs ~3.7 years and the manager ~12 years, so no new player rationally enters. The reward-token price feeds back into the NFT floor, which is why P2E collapses are reflexive rather than gradual. *(Illustrative arithmetic only; the $1,000 team cost is an assumption, not a dated quote.)*

### Kill signals for a P2E position

1. Daily reward-token emission value exceeds daily burn value for **4+ consecutive weeks**.
2. Entry-NFT floor falls while new-wallet growth is flat or negative: the onboarding funnel has stalled.
3. A large vesting cliff (≥ 5% of float) falls within 30 days with no matching sink launch.
4. A bridge or game-contract exploit. Exit first and reassess later (Ronin, March 2022: [[2022-03-ronin-bridge-hack]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/coins/category-groups` — curated **gaming** group (AXS, PIXEL, GMT-type tokens) with price, market cap, rank and 24h/7d change
- `GET /api/v1/supply/unlocks?symbol=PIXEL` — dated vesting cliffs sized against float (kill signal 3)
- `GET /api/v1/nfts/volume?by=category` — daily NFT volume by category, including `gaming` (Pro)

**Historical data:**
- `GET /api/v1/nfts/collections/{slug}?days=3650` — per-collection daily volume, e.g. a game's entry-NFT collection
- `GET /api/v1/backtesting/klines?symbol=AXSUSDT&interval=1d&start=2021-01-01` — governance and reward-token OHLCV

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/supply/unlocks?symbol=PIXEL"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-coins]], [[cryptodataapi-supply]], [[cryptodataapi-nft]]. Player counts and burn and emission rates come from game dashboards or Dune, not CryptoDataAPI.

## Related

- [[gamefi]] — the broader category encompassing P2E and other blockchain game models
- [[axie-infinity]] — the canonical P2E protocol
- [[nft]] — the asset type underpinning P2E character/item ownership
- [[governance-token]] — the more stable token tier in P2E two-token models
- [[vampire-attack-arbitrage]] — emission-capture strategy applicable to P2E launch phases
- [[yield-guild-games]] — the largest P2E scholarship guild
- [[liquidity-mining]] — the DeFi cousin of P2E reward token mechanics
- [[multi-strategy-crypto-portfolio]] — portfolio context for P2E as a convexity position
- [[on-chain-analysis]] — using game activity metrics as trading signals

## Sources

- General crypto/gaming knowledge; no specific wiki source ingested yet.
