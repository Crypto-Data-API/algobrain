---
title: "Pump.fun vs LetsBonk.fun vs Believe vs Moonshot vs Heaven"
type: comparison
created: 2026-05-04
updated: 2026-06-21
status: excellent
tags: [crypto, solana, memecoin, launchpad, comparison]
subjects: ["[[pump-fun]]", "[[letsbonk]]", "[[believe]]", "[[moonshot]]", "[[heaven-launchpad]]"]
comparison_dimensions: [chain, fee-model, bonding-curve, graduation-threshold, target-audience, mobile-support, revenue-burn, ecosystem-stickiness]
related: ["[[bonding-curve-analysis]]", "[[memecoin-sniping]]", "[[token-migration-sniping]]", "[[low-cap-crypto-trading-map]]", "[[axiom-pro]]", "[[gmgn]]", "[[bitquery]]", "[[raydium]]", "[[pumpswap]]", "[[solana]]"]
---

# Pump.fun vs LetsBonk.fun vs Believe vs Moonshot vs Heaven

By mid-2026, [[solana|Solana]]'s [[meme-coins|memecoin]] launchpad market is no longer a [[pump-fun|Pump.fun]] monopoly — it is a fragmented arena where five major venues ([[pump-fun|Pump.fun]], [[letsbonk|LetsBonk.fun]], [[believe]], [[moonshot]], and [[heaven-launchpad|Heaven]]) compete for the deployer's first click and the sniper's first buy. Each platform optimizes a different axis (fairness, mobile UX, creator monetization, dual-token burn, branded distribution), and the volume leadership has rotated multiple times in a single year as the [[meme-coin-cycle]] churns through narratives. For a trader, choosing where to camp determines fill quality, [[token-migration-sniping|migration]] timing, exposure to [[mev]] sandwich competition, and the realistic edge of every [[memecoin-sniping|sniping]] strategy.

> ⚠️ **Risk note.** Every launchpad on this page is a venue for trading [[meme-coins]], the highest-loss-probability asset class covered in this wiki. The launchpad choice changes *fill quality and competition*, not the underlying base rate — the vast majority of launches on every platform go to zero. This page compares venues for execution, not as an endorsement of memecoin trading.

---

## Why this comparison matters

The launchpad you camp on dictates three things that bound every memecoin trade:

1. **Deal flow** — how many launches per hour and how many of them have any chance of graduating
2. **Migration mechanics** — at what market cap the bonding curve hands liquidity to a DEX, and which DEX
3. **Sniper density** — how many bots are already sitting on the deployer wallets you're trying to front-run

Pump.fun set the template (one-click free launch, deterministic bonding curve, automatic [[raydium|Raydium]]/[[pumpswap|PumpSwap]] migration). Every entrant since has copied the UX while differentiating on tokenomics, distribution, or audience. The result is that flow follows narrative as much as it follows fees — and the narrative changes every 60-90 days.

---

## At-a-Glance Comparison

| Dimension | [[pump-fun\|Pump.fun]] | [[letsbonk\|LetsBonk.fun]] | [[believe]] | [[moonshot]] | [[heaven-launchpad\|Heaven]] |
|---|---|---|---|---|---|
| **Chain** | [[solana\|Solana]] (+ Base, Blast since 2024) | [[solana\|Solana]] | [[solana\|Solana]] | [[solana\|Solana]] (mobile-first) | [[solana\|Solana]] |
| **Launch fee** | Effectively zero (~$2 SOL seed) | Low (data not available in source — verify on platform) | Low; creator-monetization fee model | Low; in-app purchase friendly | Low; 100% revenue burn redirects fees |
| **Bonding curve** | Deterministic constant-product curve | Pump.fun-style bonding curve | Bonding curve with creator-share | Pump.fun-style curve, mobile-optimized | Bonding curve + dual-token sink |
| **Graduation threshold** | ~$69k market cap → migrates to [[raydium\|Raydium]]/[[pumpswap\|PumpSwap]] | Comparable to Pump.fun (data not available in source — verify on platform) | data not available in source — verify on platform | data not available in source — verify on platform | data not available in source — verify on platform |
| **Mobile support** | Web-first; mobile via browser | Web-first | Web-first | **Mobile-first** (native app) | Web-first |
| **Dual-token model** | No (single token per launch) | No | No (creator share, but single token) | No | **Yes** — LIGHT / DARK platform tokens |
| **Revenue model** | Platform fee + revenue-share programs (2025-26) | Platform fee; "600% revenue surge" headline early 2026 | Creator-monetization split | In-app fees | **100% revenue burn** into LIGHT/DARK |
| **Target audience** | Generalist degen flow, snipers, bot operators | Bonk-ecosystem loyalists, fairness-narrative traders | Creators wanting recurring revenue | Mobile-only / casual / non-crypto-native | Tokenomics maximalists, burn-narrative traders |
| **Status (mid-2026)** | Dominant by cumulative volume; defended position with revenue programs | Briefly #1 in daily deployments; 600% revenue surge early 2026 | Active challenger; creator-monetization niche | Active; mobile distribution edge | Surged to #2 on LIGHT launch (800%+ gains), then cooled |

> Where a cell reads "data not available in source — verify on platform," the [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo|source material]] did not specify a number. Confirm on the platform's docs before sizing on the assumption.

---

## Pump.fun

[[pump-fun|Pump.fun]] is the original Solana memecoin launchpad and the venue every other entrant is benchmarked against. It introduced the **one-click, zero-presale, instant-deployment** UX: a creator pays roughly $2 SOL to seed liquidity, the contract follows a deterministic [[bonding-curve-analysis|bonding curve]], and at ~$69k market cap the bonding curve automatically migrates liquidity to a DEX (originally [[raydium|Raydium]], later also [[pumpswap|PumpSwap]]) and burns the LP tokens. By December 2024 the platform had processed **10M+ token launches**, and in 2024 it expanded beyond Solana to **Base** and **Blast** Ethereum L2s. Through 2025-26 Pump.fun introduced revenue-sharing programs explicitly to defend share against [[letsbonk|LetsBonk.fun]] (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

**Strengths**
- Largest historical deal flow → the deepest pool of "lottery ticket" launches for [[memecoin-sniping|sniping]]
- Deterministic bonding curve and well-documented migration trigger → predictable [[token-migration-sniping]]
- Multi-chain footprint (Solana, Base, Blast) gives traders cross-chain optionality
- Mature third-party tooling: [[axiom-pro]], [[gmgn]], [[bitquery]] all index Pump.fun launches in real time

**Weaknesses**
- Sniper density is highest here — fills are competitive and bot-vs-bot
- Quality-to-quantity ratio is brutal; the vast majority of launches die before graduation
- Has had to launch defensive revenue programs in response to challengers, signalling pricing pressure

---

## LetsBonk.fun

[[letsbonk|LetsBonk.fun]] is the [[solana|Solana]] launchpad most associated with the BONK ecosystem narrative. It briefly **dethroned Pump.fun in daily token deployments** and saw a documented **600% revenue surge in early 2026** — the clearest evidence that flow can rotate aggressively to a challenger when the narrative aligns (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

**Strengths**
- Captured measurable flow rotation away from Pump.fun in early 2026 — the only challenger with hard "we briefly led" data
- Tied to an existing ecosystem brand (BONK), giving warm distribution and a built-in narrative buyer base
- Lower sniper density than Pump.fun during off-peak hours → better fills for non-HFT operators

**Weaknesses**
- Narrative-dependent; revenue surges concentrated in short windows, not steady-state
- Smaller indexer/tooling coverage than Pump.fun (verify your sniping infra supports it)
- History of challengers (Heaven, Moonshot) suggests platforms can give back gains as fast as they take them

---

## Believe

[[believe]] is a [[solana|Solana]] launchpad oriented around **creator monetization** — letting deployers retain a share of platform fees rather than a one-shot launch profit. This positions it for creators who want recurring revenue from a community, not just a pump-and-walk.

**Strengths**
- Creator-revenue-share model attracts a different deployer cohort (community-builders, content creators) than pure-degen launchpads
- Deployers with reasons to stick around tend to produce slightly higher-quality launches → marginally better graduation odds
- Useful diversification venue when Pump.fun and LetsBonk are saturated with sniper bots

**Weaknesses**
- Smaller daily volume than Pump.fun or post-surge LetsBonk → thinner exit liquidity
- Specific bonding-curve parameters and graduation thresholds: data not available in source — verify on platform before sizing
- Narrative tailwind is weaker than Heaven's burn story or LetsBonk's BONK tie-in

---

## Moonshot

[[moonshot]] is the **mobile-first** [[solana|Solana]] launchpad — built around in-app purchases and onboarding non-crypto-native users from a phone rather than a desktop wallet. Like Heaven, Moonshot is part of the documented pattern where new launchpads **surge briefly then lose momentum** (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

**Strengths**
- Mobile distribution reaches users who never touch a desktop Solana wallet → genuinely incremental flow
- Lower sniper bot density (most sniper infra is desktop/server-side) → better fills for retail-style entries
- In-app purchase rails reduce on-ramp friction for narrative-driven memecoin buyers

**Weaknesses**
- Mobile-first UX limits power-user features that snipers and bot operators rely on
- Fits the "surge then fade" pattern — flow is event-driven, not structural
- Specific fee schedule and graduation threshold: data not available in source — verify on platform

---

## Heaven

[[heaven-launchpad|Heaven]] is the most tokenomics-distinctive challenger: a [[solana|Solana]] launchpad with a **dual-token model (LIGHT / DARK)** and **100% revenue burn** into those tokens. On the LIGHT launch the platform surged to second-place daily deployments and LIGHT itself printed **800%+ gains**, demonstrating how aggressively a "we burn everything" narrative can pull flow away from Pump.fun in the short term (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

**Strengths**
- 100% revenue burn is the clearest tokenomics differentiation in the launchpad space → strong narrative magnet
- Dual-token (LIGHT/DARK) creates two distinct trading vehicles tied to platform success
- Surge-pattern means there are repeatable windows where Heaven becomes the dominant deal-flow venue for hours-to-days

**Weaknesses**
- Fits the "surge briefly then lose momentum" pattern observed across launchpad challengers — sticky daily volume is unproven
- Platform-token tokenomics (LIGHT/DARK) themselves carry reflexive risk: if burn-narrative cools, LIGHT/DARK price drops, which can drag launchpad activity with it
- Dual-token model adds a second layer to model: traders must understand LIGHT vs DARK roles before sizing

---

## Cross-chain note: SunPump (TRON)

[[pump-fun|Pump.fun]]'s model is no longer Solana-exclusive. **SunPump** is a [[tron|TRON]]-based memecoin launchpad emerging as a cross-chain competitor, representing the broader shift past Solana-only dominance (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]). For traders, the relevance is asymmetric:

- TRON has a different user base (high USDT activity, Asia-leaning retail) → SunPump deal flow is correlated with different narratives than Solana launchpads
- Tooling overlap with Solana sniper infra is low — most [[axiom-pro]] / [[gmgn]] / [[bitquery]] coverage is Solana-first
- Useful as a **diversification venue** when Solana launchpads are saturated, but not a primary camping ground unless you're already running TRON infra

Pump.fun's own 2024 expansion to **Base** and **Blast** is the parallel multi-chain story on the EVM side. The strategic read: launchpad competition in 2026 is multi-chain by default, even if Solana remains the volume leader.

---

## Trader's playbook by launchpad

| If you want… | Camp on | Why |
|---|---|---|
| Maximum raw deal flow, deepest tooling | **[[pump-fun\|Pump.fun]]** | Most launches/hour, every indexer covers it, best-documented [[bonding-curve-analysis\|bonding curve]] and [[token-migration-sniping\|migration]] mechanics |
| Narrative-rotation flow when Pump.fun feels saturated | **[[letsbonk\|LetsBonk.fun]]** | Demonstrated ability to capture flow rotation; BONK tie-in gives warm distribution |
| Slightly less crowded sniping with quality skew | **[[believe]]** | Creator-monetization model selects for slightly stickier deployers |
| Reach non-crypto-native buyers / less bot competition | **[[moonshot]]** | Mobile-first means most sniper bots aren't competing for the same fills |
| Burn-narrative event trades and platform-token (LIGHT/DARK) plays | **[[heaven-launchpad\|Heaven]]** | Dual-token + 100% burn creates discrete event windows that can be traded twice (the launch + the platform token) |
| Cross-chain diversification | **SunPump** ([[tron\|TRON]]) | Different user base, uncorrelated narratives |

Universal rules across all five:

1. **Snipe at deployment** only if your infra can compete with the bots already on the deployer wallet — otherwise you're exit liquidity for the bots' first sell
2. **Snipe at migration** is structurally cleaner: the ~$69k threshold (Pump.fun) is deterministic and indexed in real time by [[axiom-pro]], [[gmgn]], and [[bitquery]]
3. **Treat platform tokens** (LIGHT, DARK, BONK, etc.) as derivatives of launchpad daily volume — when daily launches drop, the token drops
4. **Always verify graduation thresholds and fee schedules** on the actual platform before sizing — see [[low-cap-crypto-trading-map]] for the broader stack

---

## Risk profile by launchpad

The launchpad changes *which* risks dominate, even though the base rate of memecoin failure is high everywhere. Relative exposure (not absolute — all are high-risk):

| Risk | [[pump-fun\|Pump.fun]] | [[letsbonk\|LetsBonk.fun]] | [[believe]] | [[moonshot]] | [[heaven-launchpad\|Heaven]] |
|------|:-:|:-:|:-:|:-:|:-:|
| **Sniper-bot density** (you become exit liquidity) | Highest | Medium-high | Medium | Lower | Spiky (high on surges) |
| **[[mev]] sandwich exposure** | High | Medium | Medium | Lower | Medium |
| **Rug / low-quality launch rate** | High (volume = noise) | High | Slightly lower (sticky deployers) | Medium | High |
| **Exit-liquidity thinness** | Lowest (deep flow) | Medium | Higher | Higher | Spiky |
| **Platform-token reflexivity** | Low (no single token) | Medium (BONK tie-in) | Low | Low | High (LIGHT/DARK) |
| **Tooling / indexer gaps** | Lowest | Medium | Higher | Higher | Higher |
| **Narrative-fade risk** | Low (defended position) | Medium | Medium | High | High |

Universal across all five: rug pulls, honeypots, and total-loss base rates remain dominant regardless of venue. The venue choice optimizes *competition and fill quality* at the margin — see [[rug-detection-checklist]] and [[holder-concentration-analysis]] for the filters that matter on every platform.

---

## Sniper infrastructure coverage by venue

A practical constraint often overlooked: your sniping stack must actually *support* the venue. Indexer and bot coverage is uneven:

| Tooling | [[pump-fun\|Pump.fun]] | [[letsbonk\|LetsBonk.fun]] | [[believe]] | [[moonshot]] | [[heaven-launchpad\|Heaven]] |
|---------|:-:|:-:|:-:|:-:|:-:|
| [[axiom-pro]] | ✅ deep | ⚠️ verify | ⚠️ verify | ⚠️ verify | ⚠️ verify |
| [[gmgn]] | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [[bitquery]] (on-chain API) | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [[bullx]] | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Telegram bots ([[bonkbot]], [[banana-gun]], [[trojan-bot]], [[maestro-bot]]) | ✅ | ⚠️ varies | ⚠️ varies | ❌ mobile-first | ⚠️ varies |

Legend: ✅ confirmed strong coverage · ⚠️ verify current support before relying on it · ❌ generally not covered. Coverage shifts as challengers gain volume; the consistent pattern is that **Pump.fun has the deepest, best-tested tooling**, and every challenger requires you to verify your specific [[memecoin-sniping|sniping]] infra before committing capital.

---

## Migration patterns and volume leadership

Volume leadership has rotated multiple times in 12 months:

- **Baseline (2024 → early 2025)**: Pump.fun dominant, processed 10M+ launches by Dec 2024
- **Heaven LIGHT launch window**: Heaven surges to #2 in daily deployments, LIGHT prints 800%+ gains, then cools (fits the documented surge-then-fade pattern)
- **Early 2026 LetsBonk surge**: LetsBonk briefly dethrones Pump.fun in **daily deployments** and posts a **600% revenue surge**
- **Pump.fun response (2025-26)**: Launches revenue-sharing programs explicitly to counter LetsBonk gains — the first time Pump.fun has competed on trader incentives rather than UX alone

(Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]])

Practical implication: **leadership is event-driven**. A trader who hard-commits to one launchpad will miss 30-60 day windows where another venue is producing 2-5x the deal flow. The right operating mode is to maintain warm infra (indexer access, wallet funding, sniper config) on **at least three** launchpads simultaneously, and rotate camping intensity based on observed daily-launch counts.

---

## Hype-cycle warning

The single most repeated pattern in the [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo|source material]]: **most challengers fade after their initial surge.** Heaven and Moonshot are explicitly cited as fitting this pattern. LetsBonk's 600% revenue surge is impressive, but whether it converts into structural share or reverts to challenger status remains unsettled.

Implications for traders:

- **Don't anchor to "Pump.fun is dead"** narratives — Pump.fun's defensive moves (revenue programs, multi-chain expansion) keep it sticky even when it loses daily-deployment leadership
- **Don't chase the surge late** — by the time a launchpad's surge is in mainstream Crypto Twitter, the easiest sniper-density-arbitrage window has closed
- **Treat platform tokens as event trades, not buy-and-hold** — LIGHT, BONK-tied tokens, and any future Pump.fun / Believe / Moonshot platform tokens will move with daily volume, which is itself cyclical
- **Build infra portably** — anything that ties your sniping stack to a single launchpad is a liability when flow rotates

---

## Sources

- [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]] — Perplexity gap-finder run on Pump.fun competitors (Apr 2026), citing KuCoin coverage of LetsBonk's 600% revenue surge, Binance Square coverage of Heaven's LIGHT/DARK dual-token model and 800%+ LIGHT gains, and antiersolutions / blockchainappfactory coverage of bonding-curve mechanics and the ~$69k Raydium migration trigger
- Public knowledge: Pump.fun expansion to Base and Blast (April 2024); 10M+ token launches milestone (Dec 2024)

---

## Related

- [[pump-fun]] — The dominant Solana memecoin launchpad and the benchmark for every entrant
- [[letsbonk]] — Bonk-ecosystem launchpad; briefly led daily deployments and posted 600% revenue surge early 2026
- [[believe]] — Creator-monetization-focused Solana launchpad
- [[moonshot]] — Mobile-first Solana launchpad
- [[heaven-launchpad]] — Dual-token (LIGHT/DARK) launchpad with 100% revenue burn
- [[bonding-curve-analysis]] — How deterministic bonding curves price launchpad tokens
- [[memecoin-sniping]] — Sniper strategies at deployment
- [[token-migration-sniping]] — Sniping the bonding-curve → DEX migration moment
- [[low-cap-crypto-trading-map]] — Where launchpads sit in the broader low-cap stack
- [[axiom-pro]] — Real-time launchpad indexer / sniper tooling
- [[gmgn]] — Memecoin scanner and trading frontend
- [[bitquery]] — On-chain data API used to track launchpad deployments and migrations
- [[raydium]] — Solana AMM that receives Pump.fun graduated liquidity
- [[pumpswap]] — Pump.fun's own DEX for graduated tokens
- [[solana]] — Underlying chain for all five launchpads
- [[tron]] — Underlying chain for SunPump cross-chain context
- [[meme-coins]] — The asset class every launchpad produces
- [[meme-coin-cycle]] — The boom/bust cycle that drives launchpad volume rotation
- [[sniping]] — Parent taxonomy for the strategies these venues enable
- [[mev]] — Sandwich/extraction dynamics that bound fill quality on every venue
- [[jito-bundle-sniping]] — MEV-protected execution used across these launchpads
- [[rug-detection-checklist]], [[holder-concentration-analysis]] — Filters that matter on all five
- [[bullx]], [[bonkbot]], [[banana-gun]], [[trojan-bot]], [[maestro-bot]] — Sniper tooling with uneven venue coverage
